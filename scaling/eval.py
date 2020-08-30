import numpy as np
import pandas as pd
from scaling.dps import dps, dps_grad
from scaling.constants import SCALARS

settings = {
    'extreme': np.array([1, 0, 0, 0]),
    'skewed': np.array([0.8, 0.2, 0, 0]),
    'semi-skewed': np.array([0.6, 0.4, 0, 0]),
    'even': np.array([0.5, 0.5, 0, 0]),
}


def evaluate_point(module, with_dr, avg_ilvl, pct_dist, avg_stat_dist, slot_type, penalties=[5, 0, -5]):
    """Evaluate the different settings at this point, using `module` to
    calculate stats starting at `avg_ilvl` with `avg_stat_dist`."""
    base_stats = module.total_points(avg_ilvl, avg_stat_dist, 1)
    stat_grad = dps_grad(module.POINTS_PER_PCT, base_stats[0], base_stats[1], pct_dist, with_dr,
                         0, [0, 0, 0, 0])

    print(base_stats)
    print(stat_grad)
    stat_prio = np.argsort(stat_grad)

    # we're going to use this to remove the stats from the presumed base item
    key = 'jewelry' if slot_type == 'ring' else 'armor'
    basic_stats = module.points(key, avg_ilvl, avg_stat_dist,
                                SCALARS[slot_type])
    basic_dps = dps(module.POINTS_PER_PCT, base_stats[0], base_stats[1], pct_dist, with_dr,
                    *basic_stats)

    basic_upgrade_stats = module.points(key, avg_ilvl + 5, [0.25, 0.25, 0.25, 0.25],
                                        SCALARS[slot_type])
    basic_upgrade_dps = dps(module.POINTS_PER_PCT, base_stats[0], base_stats[1], pct_dist, with_dr,
                            *basic_upgrade_stats)

    upgrade_delta = basic_upgrade_dps - basic_dps

    deltas = [{
        'penalty': 5,
        'kind': 'average',
        'setting': 'basic',
        'dps': basic_upgrade_dps,
        'delta': upgrade_delta,
        'improvement': False
    }]
    # now we calculate the sidegrades and downgrades with diff stat dists
    for penalty in penalties:
        for tag, prio in [('worst', stat_prio), ('best', stat_prio[::-1])]:
            for setting_tag, setting_dist in settings.items():
                dist = np.zeros(4)
                dist[prio] = setting_dist
                setting_stats = module.points(key, avg_ilvl + penalty, dist,
                                              SCALARS[slot_type])
                setting_dps = dps(module.POINTS_PER_PCT, base_stats[0], base_stats[1], pct_dist, with_dr,
                                  *setting_stats)
                print(key, avg_ilvl + penalty, setting_stats)
                setting_delta = setting_dps - basic_dps
                deltas.append({
                    'penalty': penalty,
                    'kind': tag,
                    'setting': setting_tag,
                    'delta': setting_delta,
                    'improvement': setting_delta > upgrade_delta,
                    'dps': setting_dps,
                })

    return pd.DataFrame(deltas)

import theano as th
from theano import tensor as T
from scaling.constants import BASE, MULT, LINEARIZATION_SLOPE, STATS_AT_BASE, \
    TOTAL_BASE, TOTAL_AT_BASE


def build_points(stats, base):
    ilvl = T.dscalar('ilvl')
    snd_dist = T.dvector('secondary_dist')
    budget_scalar = T.dscalar('budget_scalar')
    mainstat_included = T.dscalar('mainstat?')

    base_mult = LINEARIZATION_SLOPE * (base - 300) + MULT[299]
    mult = LINEARIZATION_SLOPE * (ilvl - 300) + MULT[299]

    mainstat = mainstat_included * budget_scalar \
        * stats['primary'] * (1.15 ** ((ilvl - base) / 15))
    raw_snd = stats['secondaries'] / base_mult * 1.15 ** ((ilvl - base) / 15)
    total_snd = budget_scalar * raw_snd * mult
    snds = snd_dist * total_snd

    points = th.function([ilvl, snd_dist, budget_scalar, mainstat_included],
                         [mainstat, snds])
    return points


points = build_points(STATS_AT_BASE, BASE)
total_points = build_points(TOTAL_AT_BASE, TOTAL_BASE)

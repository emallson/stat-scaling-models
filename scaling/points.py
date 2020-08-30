import theano as th
from theano import tensor as T


def build_points(MULT, stats, base):
    ilvl = T.iscalar('ilvl')
    snd_dist = T.dvector('secondary_dist')
    budget_scalar = T.dscalar('budget_scalar')

    base_mult = MULT[base - 1]
    mult = MULT[ilvl - 1]

    mainstat = budget_scalar \
        * stats['primary'] * (1.15 ** ((ilvl - base) / 15))
    raw_snd = stats['secondaries'] / base_mult * 1.15 ** ((ilvl - base) / 15)
    total_snd = budget_scalar * raw_snd * mult
    snds = snd_dist * total_snd

    points = th.function([ilvl, snd_dist, budget_scalar],
                         [mainstat, snds])
    return points


def combine_points(armor, jewelry):
    def points(key, *args):
        if key == 'armor':
            return armor(*args)
        elif key == 'jewelry':
            return jewelry(*args)

    return points

import theano as th
from theano import tensor as T
from theano.ifelse import ifelse
from scaling.constants import POINTS_PER_PCT

base_mainstat = T.dscalar('base_mainstat')
base_snds = T.dvector('base_secondaries')
snds = T.dvector('secondaries')
pcts = (base_snds + snds) / (POINTS_PER_PCT * 100)

with_dr = T.iscalar('with_dr')

pcts_dr = 1 * T.clip(pcts, 0, 0.25)\
    + 0.9 * T.clip(pcts - 0.25, 0, 0.34 - 0.25)\
    + 0.8 * T.clip(pcts - 0.34, 0, 0.42 - 0.34)\
    + 0.7 * T.clip(pcts - 0.42, 0, 0.49 - 0.42)\
    + 0.6 * T.clip(pcts - 0.49, 0, 1.06 - 0.49)

pct_dist = T.dvector('pct_dist')
mainstat = T.dscalar('mainstat')
dps_res = (base_mainstat + mainstat) * T.prod(1 + pct_dist * ifelse(T.gt(with_dr, 0), pcts_dr, pcts))
dps = th.function([base_mainstat, base_snds, pct_dist, with_dr, mainstat, snds],
                  dps_res)

dps_grad = th.function([base_mainstat, base_snds, pct_dist, with_dr, mainstat, snds],
                       T.grad(dps_res, snds))

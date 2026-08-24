"""
Real installed fibre length (spoke + backbone / mesh), independent of any
NetSquid simulation.

Replicates the exact tortuosity-weighted fibre length computation that
bb84_network.run_bb84_network / mdi_network.run_mdi_network compute internally
before running their (expensive) Monte Carlo trials — same per-call fresh
`np.random.default_rng(seed)` stream, same per-link tortuosity sampling order
— so a given (topo, tortuosity_mean, seed) produces bit-identical total_fibre_km
to what the real NetSquid run would report, without paying for the trials.
Lets deterministic cost/efficiency figures sweep a much wider N range than is
feasible for NetSquid itself.
"""
import numpy as np


def _sample_link_tortuosity(rng, mean, n):
    """Sample n per-link tortuosity factors: truncated normal(mean, 0.1), min 1.0."""
    if mean <= 1.0:
        return np.ones(n)
    return np.maximum(1.0, rng.normal(mean, 0.1, size=n))


def total_fibre_bb84(topo, tortuosity_mean, seed):
    """Total BB84 direct-mesh fibre length (km), N(N-1)/2 links."""
    pairs  = topo.all_pairs()
    rng    = np.random.default_rng(seed)
    t_link = _sample_link_tortuosity(rng, tortuosity_mean, len(pairs))
    return sum(topo.bb84_link(i, j) * t_link[k] for k, (i, j) in enumerate(pairs))


def total_fibre_relay(topo, tortuosity_mean, seed):
    """Total MDI/TBB84 hub-and-spoke fibre length (km): N spoke links + K(K-1)/2 backbone links."""
    rng    = np.random.default_rng(seed)
    t_user = _sample_link_tortuosity(rng, tortuosity_mean, topo.N)
    t_bb   = _sample_link_tortuosity(rng, tortuosity_mean, topo.K * (topo.K - 1) // 2)

    spoke = sum(
        float(np.linalg.norm(topo.user_pos[i] - topo.relay_pos[int(topo.user_relay[i])])) * t_user[i]
        for i in range(topo.N)
    )
    backbone = 0.0
    idx = 0
    for j in range(topo.K):
        for k in range(j + 1, topo.K):
            backbone += float(np.linalg.norm(topo.relay_pos[j] - topo.relay_pos[k])) * t_bb[idx]
            idx += 1
    return spoke + backbone

# Archive notes

## `relay_sweep_too_small/` — MDI key rate rises with K (2026-08-10/11)

Sweep: N=15 users, K=1-4, area 25x25 km, 5 seeds, 200 runtimes/pair.

**Observation**: mean MDI key rate rises monotonically with K (~58 -> 63 -> 69 -> 70 kbps
across seeds), flattening by K=3-4. This is the opposite of the "K=1 is theoretically
optimal" note in `ROADMAP.md` (Planned > Network Scale Modelling > Experiment 1), which
assumes a single relay already sits near-centroid to a dense user population, so splitting
into more relays barely shortens spoke distance while definitely adding backbone fibre
(K(K-1)/2 relay-relay links) — net loss.

**Explanation**: that assumption doesn't hold here because N=15 over 625 km^2 is sparse.
At K=1 a single relay serves all 15 users scattered across the full area, so mean
user-to-relay (spoke) distance is large. `optimise_relays`' k-means step at higher K
splits users into tighter local catchments, shrinking mean spoke distance roughly like
1/sqrt(K) for points scattered over an area — a strong effect at low K, and one that
matters a lot for MDI since arm distance enters the BSM coincidence probability as
eta_arm^2. The backbone penalty (extra relay-relay fibre, cross-cluster BSM routing) is
real but small in this regime: with only 15 users spread thin, cross-cluster pairs are a
minority and the relays aren't very far apart even as K grows. Net effect: spoke-distance
reduction beats backbone cost until diminishing returns set in around K=3-4, when
catchments are already small enough that further splitting stops helping.

So this isn't a bug — it's a sparse-network regime where the "K=1 optimal" argument's
premise (dense enough that K=1 is already near-centroid) doesn't hold. It's a boundary
condition on that claim, not a contradiction of it: the claim should hold again at
higher user density (more users per unit area, so K=1's spoke distances are already
short and splitting doesn't help as much).

**Status**: re-running at 250 runtimes, K=1-5, for better statistical significance
(this five-seed/200-runtime version was archived as underpowered, hence the folder
name). If the trend persists, treat it as a real finding and explain it in the
dissertation (candidate location: relay-count sweep discussion in
`sec:results_network` / `sec:scalability`, alongside the existing K=1-optimal note)
rather than dismiss it as noise.

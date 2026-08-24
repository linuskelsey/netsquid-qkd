# BT Real-Topology Case Study — Figure Spec

Target: Appendix "Real-World Deployment Considerations" (`sec:appendix_bt`), dissertation.tex.
That appendix currently states its discussion is qualitative "without new simulation
results" — this figure set is what upgrades it to an actual case study. Supersedes the
single-seed `figures/real_topology/bt_{cost,efficiency,marginal}.png` trio (K=3, seed=75907),
which used too small a sample and should not be reused once these are ready.

Fixed across all figures: real BT-derived node layout (named sites, lat/lon projected to
km), K=3 relays (matches the real network's actual relay count — not a swept variable
here), three protocols: BB84 (direct mesh), MDI, TBB84. User count N swept low to the
network's full node count, growing one user at a time as in the existing user-count sweep
methodology (`sec:scalability`, organic growth: relay placement fixed once, catchments
filled incrementally) — reuse that model rather than re-deriving one.

Unlike the rest of Section 4, this is one fixed real topology, not an average over drawn
seeds — state that plainly in the caption/text of every figure, consistent with how the
rest of the dissertation hedges single-instance results (see the topology-sensitivity
paragraph in `sec:simulation_limitations`). Any Monte Carlo sampling that *does* apply
(per-pair NetSquid trial count for the key-rate figure) should use a materially larger
run budget than the superseded trio, which is the whole reason for redoing these.

## 1. Topology map

- One panel, largest user count in the sweep (full real node set).
- Named sites plotted on the projected km grid (per `network/real_topology.py`), relay
  vs. user visually distinguished, K=3 spoke+backbone edges drawn from the actual
  placement used in the sweeps below.
- Purpose: this is the one figure in the whole dissertation grounded in real geography
  rather than synthetic/idealised placement — it's what makes the appendix read as a case
  study rather than another parameter sweep with different axis labels. No numerical
  result attached; purely orientation for the reader before the next three figures.

## 2. Key rate vs user count (all three protocols)

- BB84, MDI, TBB84 on one axis, key rate (kbps) vs N, same visual style as `fig:user_sweep`
  in `sec:results_network` (log y-axis, shaded/error treatment if the larger sample
  supports it).
- Purpose: raw-rate companion to the efficiency figure below — needed so a reader can tell
  whether TBB84's cost-efficiency lead (seen in the superseded single-seed run) comes from
  genuinely higher throughput or just lower cost. Also the natural place to say whether
  the real topology's protocol *ranking* by key rate matches the synthetic user-count
  sweep's ranking.

## 3. Deployment cost vs user count

- Total cost (£M) vs N, one curve per protocol, using fixed indicative component prices
  (source, detector, fibre) — state the specific £ values used directly in this figure's
  caption/assumptions, and flag them explicitly as illustrative, not vendor-quoted, per
  the existing symbolic-vs-numeric cost model hedge already written into this appendix.
- MDI and TBB84 are expected to coincide (identical cost structure in this model: same
  source/detector/fibre accounting, differing only in trust assumptions, not component
  count) — if so, say that explicitly rather than leaving two overlapping curves
  unexplained.

## 4. Key rate per unit cost vs user count

- Derived from figures 2 and 3 (kbps / £M), one curve per protocol.
- Purpose: this is the figure that produced the headline finding worth a sentence of its
  own — cost-efficiency ranks protocols in the *reverse* order of their trust guarantees
  (TBB84, least trustless, most cost-efficient; MDI, most trustless, least). Tie this back
  to the Level 0–3 trust hierarchy in `sec:results_cost` / Deployment Recommendations.

## 5. Cost ratio vs user count, swept over ρ (detector:fibre price ratio)

- Single panel, x-axis N, y-axis $C_\text{relay}/C_\text{BB84}$ (MDI and TBB84 coincide
  per \#3, so one relay-cost curve, not two), one curve per ρ value, K=3 fixed throughout
  (matches the real network, not swept).
- This is the empirical companion to the closed-form `fig:nstar` ($N^*(\rho,K)$,
  Eq.~\ref{eq:nstar_closed}): read off each curve's empirical crossover ($N$ where it
  crosses 1.0) and compare against the closed-form $N^*(\rho,3)$. Close agreement
  validates the uniform-scattering approximations (Eqs. 607–628) surviving contact with
  real, non-uniform geography; disagreement is itself worth a sentence, and ties into the
  topology-sensitivity discussion in `sec:simulation_limitations`.
- 6–8 ρ curves, bracketing `fig:nstar`'s existing range plus one value below and one above
  it (extend the reader's view of the price-ratio space, don't just re-plot the same
  numbers on a different axis).
- These curves are deterministic given N, K, ρ and the fixed real distances (cost is
  closed-form, not NetSquid-simulated) — no MC noise, no shaded bands needed, and no risk
  of curves crossing each other (Eq.~\ref{eq:delta_cost} is monotonic in ρ at fixed N,K),
  so a busier multi-curve panel is fine here in a way it wouldn't be for a noisy
  Monte-Carlo figure.
- Colour: sequential colormap ordered by ρ (e.g. viridis), not categorical — communicates
  the "one continuously-varying family" reading. Start with a standard legend; switch to
  inline end-of-curve ρ labels only if the legend crowds the panel once real curves are in
  hand. Since these ship as `.tex` (pgfplots/tikzplotlib), colour and label placement are
  easy to revisit later without re-simulating anything.
- Panel should be sized larger than a standard single-column figure to keep 6–8 nested
  curves separable.

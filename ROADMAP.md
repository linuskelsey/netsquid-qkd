# ROADMAP

---

## Complete

### Modelling Layers

| Layer | Description |
|-------|-------------|
| 0 | Ideal baseline (no physical impairments) |
| 1 | Fibre loss: Beer-Lambert `T = 10^(-αL/10)` |
| 2 | Detector efficiency `η_d` |
| 3 | Dark counts: per-slot Bernoulli + lost-slot model |
| 4 | Init / coupling loss |
| 5 | Node / connector loss |
| 6 | Source bit errors |
| 7 | Detector basis bias `η_Z` / `η_X` |
| 8 | Fibre dephasing (`DephaseNoiseModel`, rate per km) |
| 9 | Beam splitter efficiency (MDI relay BSM, η_bs) |

### Infrastructure

| Feature |
|---------|
| JSON config presets + CLI overrides |
| Multiprocessing: P2P scripts split runtimes across cores; network scripts split pairs across cores. Both now batch `runtimes` into rounds of <=100 with a fresh `Pool()` respawned each round (`network/bb84_network.py`, `network/mdi_network.py`, `network/trusted_bb84_network.py`, matching the pattern `BB84/BB84_run.py`/`MDI/mdiRun.py` already used) — a `bt_case_study.py` run at `--runtimes 1000` previously OOM-killed partway through with one long-lived pool per N/protocol call; batching bounds how many trials any one worker executes before its pool is torn down, capping accumulation of whatever `ns.sim_reset()` doesn't fully release per trial. Found + fixed 2026-08-25. |
| Compare scripts: length, loss, efficiency, dark count, init loss, node loss, source error, dephasing, basis bias, beam splitter efficiency, Charlie placement (`scripts/P2P/compare/`) |
| Run-all parallel launcher (`scripts/P2P/compare/run_all.py`): all 10 compare scripts in parallel; auto-saves to timestamped `docs/figures/<Month>/<YYYYMMDD> - P2P parameters/all parameters/` |
| Layer comparison script (`scripts/P2P/layers.py`) |
| `--compare-configs PATH [PATH ...]` on all 10 compare scripts: overlay 2–4 config presets on one sweep figure (BB84 dashed, MDI solid, tab10 palette per config) |
| Config presets unified (layer0–layer8, cumulative, industry-typical values) |
| Raw script config wiring |
| `--workers` flag on all compare scripts |
| Timing wrapper + progress indicator: animated braille spinner with elapsed time and per-step label; `✓ complete  total Xm Ys` at end; seed headers and completion lines for network scripts (`lib/progress.py`) |
| Timing scripts: wall-clock time vs network area (`scripts/network/time/time_vs_area.py`) and vs user count (`scripts/network/time/time_vs_users.py`) |
| Data persistence: SQLite DB (`lib/db.py`, `data/results.db`); `p2p_results` table written by all P2P scripts; `network_results` table written by network sweep scripts; `--no-db` / `--no-p2p-db` / `--no-net-db` opt-out flags; schema documented in `DATA.md` |

### Network Scale Modelling

#### Experiment 1 — Relay count sweep

| Item |
|------|
| Network topology generator: random user placement, per-K relay optimisation (`network/topology.py`) — now k-means-seeded, generalised Weiszfeld-refined (minimises total fibre length, not sum-of-squared distance); see "Analysis" section below and dissertation §Relay Placement |
| Network topology visualiser: MDI cluster / BB84 mesh side-by-side (`network/visualise_network.py`) |
| BB84 network simulator: all N(N-1)/2 direct pairs (`network/bb84_network.py`) |
| MDI-QKD network simulator: nearest-relay routing, cross-cluster passive optical routing (`network/mdi_network.py`) |
| Trusted-node BB84 network simulator: users connect to K relay nodes via BB84; relays XOR-combine keys; cross-relay pairs share backbone key rate proportionally; bottleneck = min link rate (`network/trusted_bb84_network.py`) |
| Passive optical routing model: cross-cluster photon redirection via optical switch (configurable insertion loss via `switch_loss_db`, default 0.0 dB — abstracted away rather than modelled/swept) |
| Key rate vs relay count K — all three protocols (`scripts/network/relay_sweep.py`) |
| Network success rate (QBER < 11%) vs relay count K |
| Multi-seed averaging (`--seeds N`): repeat sweep over N random placements, report mean ± std across seeds for statistically robust results |
| `--error iqr`: Q1/Q3 shaded band on all three protocols, more robust to outlier seeds than ±1σ (`relay_sweep.py`, `user_sweep.py`) |

#### Experiment 2 — User count sweep

| Item |
|------|
| Key rate vs user count N — all three protocols (`scripts/network/user_sweep.py`) |
| Three-way comparison (BB84 / MDI / trusted-node BB84) in both sweep scripts: isolates cost of the MDI trust-removal guarantee vs same O(N) infrastructure |
| Network success rate vs user count N |
| Fibre tracking: total fibre deployed (km) per simulation, stored in `network_results.total_fibre_km` — the empirical input to the dissertation's analytical cost formulae (see "Cost Modelling" below); no component-count or £ columns are written to the DB |
| Multi-seed averaging (`--seeds N`): relay positions re-optimised per seed; mean ± std across seeds reported |
| End-of-sweep summary table: K/N × BB84/MDI/trusted-BB84 × key rate (kbps) × success % × fibre km printed to stdout after each run |
| `--no-figure` flag on both sweep scripts: suppress all figure output (useful for batch runs or headless servers) |

#### Cost Modelling

Cost is **not** implemented in simulation code — `network/cost.py` and `scripts/network/cost_sweep.py` were removed entirely (2026-08-03). Cost is instead modelled purely analytically in the dissertation: total CapEx as symbolic component-count formulae (source/detector/fibre terms determined by topology) times free per-unit-price parameters $c_s$, $c_d$, $c_f$, since manufacturer prices aren't publicly available. The structural result — BB84 $\mathcal{O}(N^2)$ fibre vs MDI $\mathcal{O}(N)$ — and the crossover user count $N^*$ (a function of $c_d/c_f$, $K$, and geometry, not a fixed number) are derived from this symbolic model, evaluated against the real `total_fibre_km` geometry the simulations produce. See dissertation §Cost Model, §Results (Cost), §Cost Model Limitations.

### Analysis

| Item |
|------|
| Key rate vs distance |
| Key rate vs fibre loss |
| Key rate vs detector efficiency |
| Key rate vs dark count rate |
| Key rate vs node/connector loss |
| Key rate vs source error rate |
| Key rate vs fibre dephasing rate |
| Key rate vs detector basis bias (η_X sweep) |
| Key rate vs beam splitter efficiency (MDI only) |
| Realistic hardware regime shading on all sweep plots |
| QBER threshold cutoffs (11% hard cutoff, both protocols) |
| Per-point error bars on all P2P compare scripts: `--error bars` (min/max whiskers), `shade` (±1σ band), `sigma` (log-space ±1σ error bars), `iqr` (Q1/Q3 whiskers), `sem` (standard error of mean) |
| Always-on min/max error bars on `layers.py` |
| Charlie placement sweep (asymmetric Alice-Charlie / Charlie-Bob links) |
| Script to compare effect of each layer of modelling parameter per-protocol |
| Isolated parameter script (`scripts/P2P/isolate.py`): each curve = all-ideal config except one realistic parameter; overlay all isolated curves on one figure per protocol to compare each parameter's independent impact on key rate |
| Relay placement strategy comparison (K=1), provider-growth model: relay placed once per strategy (centroid/weiszfeld — plain geometric median, no boundary or backbone term at K=1) at N-min then frozen; network grows one user at a time via uniform-random catchment to N-max; same output/machinery as exp 2, just K=1 (`scripts/network/relay_placement.py --exp 1`) |
| Relay placement strategy comparison (K=2), provider-growth model: relay placed once per strategy (centroid/boundary/weiszfeld) at N-min then frozen; network grows one user at a time via uniform-random catchment to N-max — no single strategy consistently wins, ranking varies by seed (`scripts/network/relay_placement.py --exp 2`) |
| K-general relay placement strategies (centroid/boundary/weiszfeld) and incremental catchment-growth model (`grow_catchments`, `RELAY_STRATEGIES` in `network/topology.py`), shared by `relay_placement.py` and `user_sweep.py`; `--catchment-radius` (hard disc) generalised as a CLI flag alongside `--spread` (Gaussian) on both scripts |
| PLOB repeaterless bound overlay (`lib/analytical.py`, `--plob` flag on `length.py` and `loss.py`): `R ≤ -log₂(1 - η)` where η = fibre × init × node passive loss; channel-only upper bound both protocols must sit below |
| Parameter sensitivity ranking (`scripts/P2P/sensitivity.py`): run each parameter at its realistic value in isolation at a fixed distance (default 25 km); sensitivity = `(R_ideal - R_param) / R_ideal × 100%`; horizontal bar chart, BB84 and MDI side-by-side, sorted by BB84 impact; `--distance` flag for different operating regimes |

### Computational Optimisation Benchmarks (`scripts/P2P/time/`)

| Item |
|------|
| GP surrogate model (`surrogate.py`): train `sklearn` GPR on coarse (distance × detector_eff) grid; predict 10,000-point dense grid; ~1.7×10⁶× per-point speedup vs simulation; GP posterior gives uncertainty quantification free; `--grid-size`, `--runtimes`, `--save-grid`, `--load-grid` flags |
| Adaptive MC (`adaptive_mc.py`): batch early stopping when σ/μ < rel_tol; benchmarks run reduction and wall-clock saving vs fixed baseline; finding: spawn overhead dominates at batch level — BB84 25% run reduction but ~0% wall-clock saving; MDI variance too high for convergence; effective adaptive sampling requires in-loop NetSquid modification |
| Trend analysis (`trend_analysis.py`): speedup vs scale study; two analyses: (1) runtime scaling with distance/runtimes, (2) multiprocessing efficiency vs worker count |

### DB Reconstruction CLI (`scripts/analyse/`)

Reconstruct any P2P or network figure from `results.db` without re-running simulations.

| Item |
|------|
| `db.py` (~370 lines): column metadata, `DEFAULTS` mapping, `count_p2p`, `query_p2p`, `query_network`, `list_distinct`; inlines `lib/functions.py` defaults to avoid netsquid import |
| `p2p.py`: CLI script — `--sweep`, `--error`, 10 fixed-param flags; figure matches compare scripts exactly (dual y-axis, log-space ±1σ shade, regime shading, LaTeX title, 3-line format) |
| `network.py`: CLI script — `--x`, `--y`, `--error`, `--n-users`, `--k-relays`, `--area`, `--seed`; figure matches relay_sweep/user_sweep exactly (dual y-axis ghost lines, BB84 dashed+shaded, MDI solid+marker); BB84 flat line for `--x k_relays` (NULL x column); optional MDI topology figure when `--seed` set |
| MC run count annotation in title: `n=X MC runs/point` = `sum(runtimes × n_pairs)` across contributing seeds per x point |

---

## Planned

### Infrastructure

| Feature |
|---------|
| Interactive TUI launcher (`scripts/tui.py`): arrow-key menus for P2P or network path, full parameter setup, assembles and optionally runs the target script; optionally saves config JSON |
| DB cost reconstruction: query `network_results` for `total_fibre_km` per (N, protocol, experiment) and evaluate against the dissertation's symbolic cost formulae (Equations cost\_bb84/cost\_mdi) to reconstruct cost/efficiency curves from historical runs, for a chosen $(c_s, c_d, c_f)$; expose via `scripts/analyse/network.py` (e.g. `--cost` flag). *(Note: there is no `network/cost.py` to call into anymore — this would mean porting the dissertation's symbolic formulae into code, not resurrecting the old cost module.)* |
| ~~Port `_BATCH=100`-with-pool-respawn batching into the network-level runners~~ — **done 2026-08-25** (`network/bb84_network.py`, `network/mdi_network.py`, `network/trusted_bb84_network.py`), moved to Complete below. |

### Network Scale Modelling

#### Experiment 1 — Relay count sweep

| Item |
|------|
| Checkpoint saving: persist intermediate results per K/N to JSON so long runs can recover from crash |

note (superseded 2026-08-11): this originally predicted K=1 as theoretically optimal in the no-traffic model, on the reasoning that a single relay minimises total *fibre* and additional relays only add backbone cost. The actual N=15 relay-count sweep contradicts the "peak at low K" part of that claim for *key rate*: MDI key rate peaks at K=4, not K=1 (dissertation §Network Performance, Table 4), because shortening the mean user-to-relay spoke distance measurably helps key rate even though it isn't the fibre-length-minimising choice — fibre length and key rate are optimised by different K (length bottoms out at K=2–3, rate peaks at K=4). The fibre-only Steiner-point argument above is still correct as a *cost* statement, just not as a *key-rate* prediction; the traffic/bottleneck argument for favouring higher K under load is unaffected and still an open extension (see Extensions).

#### Experiment 3 — Real-world topology case studies

| Item |
|------|
| Simulate specific named QKD network topologies as dissertation case studies: fix node positions to match real geography, run both protocols, compare against random-topology results. Candidate networks: BT QKD network (UK), Berrevoets et al. topology, Tokyo QKD network, Belgian QKD network (TBC) |

### Analysis

| Item |
|------|
| ILP-optimal relay placement benchmark: formally compare k-means centroid against ILP-optimal placement to confirm or replace as canonical topology strategy (centroid/boundary/Weiszfeld growth-model comparison already complete at K=1 and K=2; ILP comparison outstanding) |
| Monte Carlo sample count scaling: for key rates of order 10^-x, use 10^(x+1) samples; smallest observed rates ~10^-2 → target 1000 runs per point where feasible; audit all scripts and increase run counts accordingly |
| Finite-key corrections: block-size-dependent key rate using composable security bound; `photons` per run sets block size `n`; quantifies departure from asymptotic regime at low photon counts and short distances |
| QBER decomposition by error source: track separate contributions from dark counts, dephasing, source errors, and basis bias per simulation point; identify dominant noise mechanism per parameter regime |

### Project Report

Done, moved from this list (2026-08-11): methodology justifications (multi-seeding, relay placement — now Weiszfeld not k-means, MC run counts, QBER cutoff, config layer choices) are all written into the dissertation methodology/limitations sections; the MDI network-scale key rate gap is explained in §Security–Rate Trade-off with real numbers (5–25× bipartite, 9.4–11.3% recovery via relay count at N=15); the parameter impact summary is Figure~9 (sensitivity ranking) in the dissertation.

| Item |
|------|
| MDI vs BB84 deployment recommendations section: dissertation's §Implications for Protocol Selection frames this via a security-requirement/scale two-axis argument rather than the originally-envisaged L0–L5 security-level taxonomy; the taxonomy itself is still unbuilt — see "Security level taxonomy" under Extensions below if a more formal framework is wanted later. |

---

## Open Questions

| Question |
|----------|
| **MDI network-scale key rate gap — remaining ablation:** the mechanism is now explained (BSM $\eta_\text{arm}^2$ scaling: §Security–Rate Trade-off) and the relay-routing-detour contribution is quantified empirically (dissertation Table~4: only 9.4→11.3% of the BB84 rate recovered by increasing $K$ at $N=15$). Not yet done: a dedicated ablation run that disables the BSM $\eta^2$ dependency and switch insertion loss individually to fully decompose the gap into its component causes, as originally scoped. |
| **Missing lower error bars at high distance/noise:** at near-cutoff distances, lower IQR/min whiskers are absent on MDI plots. Failed runs are excluded before aggregation, so the surviving runs cluster near the QBER threshold with near-zero spread below the median. Unclear whether this reflects genuine distribution shape or an artefact of the cutoff filtering — worth checking whether including failed runs (as zero key rate) changes the picture. |

### Extensions

| Item |
|------|
| Interactive DB replot TUI (`scripts/analyse/tui.py`): Textual app with P2P and Network tabs; P2P tab functional; Network tab broken (Select widget issues with Textual 8.x); replace CLI scripts (`p2p.py`, `network.py`) with a unified TUI interface when Textual API stabilises |
| Timing data extraction: extend `lib/progress.py` to record per-step and total wall-clock times; write to a sidecar JSON (`<output_stem>_timing.json`) alongside every script run; enables runtime profiling, Monte Carlo scaling estimates, and cost modelling |
| Security level taxonomy: define deployment tiers L0–L5 by trust assumption (L0: trust all components except links = ideal QKD; ... L5: trust nothing = device-independent QKD); map BB84 and MDI-QKD to appropriate levels; use as framework for recommendations on when MDI is warranted despite key rate deficit |
| MDI deployment on existing network infrastructure: scoping exercise — if fibre topology is fixed (no relay placement freedom), how does MDI performance change? Assess feasibility and cost delta vs greenfield deployment; flag as potential standalone research project |
| Brownfield relay expansion (K → K+1): `relay_sweep.py` currently re-clusters and repositions all K relays from scratch at each K, modelling greenfield design. A brownfield variant would hold the existing K relays fixed and solve only for where a new relay should go and which existing users it should take over to minimise total fibre length — an alternating position/assignment loop restricted to one new facility (cf. `optimise_relays`), not the one-shot strategies used elsewhere. Discussed as future work in the dissertation Future Work section; not implemented (2026-08-10). |
| Decoy-state key rate formula: vacuum + weak decoy correction for PNS-attack resistance; relevant if source model is relaxed from ideal single-photon to weak coherent pulse (WCP) |
| WDM multi-user MDI-QKD: multiple Alice-Bob pairs on separate wavelengths, MUX onto shared fibre, DEMUX at Charlie for per-channel BSM |
| Key rate vs WDM user count: MUX/DEMUX insertion loss (~1–3 dB per device) per channel |
| Quantum memory coherence time at WDM relay nodes: T1/T2 decoherence during inter-channel wait limits scalable user count |
| Key rate vs memory coherence time (T2 sweep) |
| Entanglement swapping at relay nodes (MDI-QKD, no trusted relay required) |
| Long-distance repeater chain: N-hop linear topology for range extension (BB84 and MDI-QKD) |
| Key rate vs number of repeater hops (sweep) |
| BB84 vs MDI-QKD repeater chain performance head-to-head |
| Relay placement sensitivity: random vs optimal placement comparison |
| Cross-relay vs same-relay pair success rate comparison |
| Traffic-aware relay count optimisation: current model minimises fibre length, making K=1 optimal (single Steiner-point relay). Under realistic traffic — simultaneous multi-pair sessions, finite relay throughput, time-multiplexed BSM — a single relay saturates under high user load, shifting the optimal K upward. Extension: model relay capacity as a bounded queue (e.g. M/M/1 or token-bucket), sweep K vs offered traffic load, identify optimal K(N, load). This reframes the relay count question from a geometry problem to a queuing/scheduling problem. |
| Cost–rate optimisation: bi-objective problem over (K, N, topology seed). Two dual problems: (1) fixed budget C_max → find configuration maximising avg key rate; (2) fixed min rate R_min → find configuration minimising cost. Sweep K and seed at fixed N, evaluate the dissertation's symbolic cost formulae against each point's `total_fibre_km` and `avg_key_rate` (no `cost_sweep.py` anymore — this is DB query + analytical formula, not a simulation sweep), plot cost vs rate for each protocol; identify deployment-optimal configurations. Useful for deployment planning: given a capex budget, which relay count gives the best key rate for MDI, and in what detector/source configuration for both MDI and BB84? Note the relay-count sweep already shows fibre-cost-optimal and key-rate-optimal $K$ diverge (Table~4) — this extension would let that trade-off be swept explicitly rather than read off two separate optima. |

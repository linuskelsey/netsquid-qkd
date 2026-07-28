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
| Multiprocessing: P2P scripts split runtimes across cores; network scripts split pairs across cores (one pool per protocol call) |
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
| Network topology generator: random user placement, per-K relay optimisation (`network/topology.py`) |
| Network topology visualiser: MDI cluster / BB84 mesh side-by-side (`network/visualise_network.py`) |
| BB84 network simulator: all N(N-1)/2 direct pairs (`network/bb84_network.py`) |
| MDI-QKD network simulator: nearest-relay routing, cross-cluster passive optical routing (`network/mdi_network.py`) |
| Trusted-node BB84 network simulator: users connect to K relay nodes via BB84; relays XOR-combine keys; cross-relay pairs share backbone key rate proportionally; bottleneck = min link rate (`network/trusted_bb84_network.py`) |
| Passive optical routing model: cross-cluster photon redirection via optical switch (configurable insertion loss, default 1 dB) |
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
| Cost tracking: total fibre (km), link count, component count per simulation |
| Multi-seed averaging (`--seeds N`): relay positions re-optimised per seed; mean ± std across seeds reported |
| End-of-sweep summary table: K/N × BB84/MDI/trusted-BB84 × key rate (kbps) × success % × fibre km printed to stdout after each run |
| `--no-figure` flag on both sweep scripts: suppress all figure output (useful for batch runs or headless servers) |
| Cost-efficiency metric: key rate per unit cost vs N — all three protocols (`scripts/network/cost_sweep.py`) |

#### Cost Modelling

| Item |
|------|
| Hardware cost model (`network/cost.py`): `component_counts()` for BB84/MDI/trusted-BB84; `total_cost()` with fibre + hardware breakdown; `DETECTOR_TECH` presets (SPAD/InGaAs/SNSPD) and `SOURCE_TECH` presets (QD/NV/hSPDC/ideal) with per-preset efficiency and cost |
| Cost sweep (`scripts/network/cost_sweep.py`): deployment cost vs N and cost-efficiency (kbps/M$) vs N — all three protocols; detector/source tech presets wire simulation η and cost model simultaneously; explicit CLI cost-flag overrides; multi-seed averaging; DB writing; end-of-sweep summary table; marginal cost vs N figure (`_marginal`) |
| `--cost-only` flag on `cost_sweep.py`: skip QKD simulation entirely; compute cost and marginal cost from topology geometry alone; runs in seconds over wide N range |

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
| Relay placement grid search (K=1): sweep relay position over full-area grid; confirms centroid placement ≈ peak average key rate for MDI and trusted-BB84 (`scripts/network/relay_placement.py --exp 1`) |
| Relay placement strategy comparison (K=2): centroid vs boundary-displaced relay placement across N in two-cluster topology; centroid consistently outperforms boundary placement (`scripts/network/relay_placement.py --exp 2`) |
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
| DB cost reconstruction: query `network_results` for `total_fibre_km` per (N, protocol, experiment), apply `component_counts` + `total_cost` from `network/cost.py` to reconstruct cost/efficiency curves from historical runs not produced by `cost_sweep.py`; expose via `scripts/analyse/network.py` (e.g. `--cost` flag) |

### Network Scale Modelling

#### Experiment 1 — Relay count sweep

| Item |
|------|
| Checkpoint saving: persist intermediate results per K/N to JSON so long runs can recover from crash |

note: in the simple model (no traffic, key rate = f(fibre length only)), K=1 is theoretically optimal — a single relay minimises total fibre by placing one Steiner point. Increasing K adds relay-relay backbone fibre and BSM hops, reducing average key rate. The relay sweep's observed peak at low K confirms this. Traffic (simultaneous multi-pair demand, relay capacity limits) breaks this optimum: a single relay becomes a bottleneck under high user load, favouring higher K. This is out of scope for the current model but is an important dimension to flag in the dissertation (see Extensions).

#### Experiment 3 — Real-world topology case studies

| Item |
|------|
| Simulate specific named QKD network topologies as dissertation case studies: fix node positions to match real geography, run both protocols, compare against random-topology results. Candidate networks: BT QKD network (UK), Berrevoets et al. topology, Tokyo QKD network, Belgian QKD network (TBC) |

### Analysis

| Item |
|------|
| ILP-optimal relay placement benchmark: formally compare k-means centroid against ILP-optimal placement to confirm or replace as canonical topology strategy (grid search and centroid-vs-boundary comparison already complete; ILP comparison outstanding) |
| Monte Carlo sample count scaling: for key rates of order 10^-x, use 10^(x+1) samples; smallest observed rates ~10^-2 → target 1000 runs per point where feasible; audit all scripts and increase run counts accordingly |
| Finite-key corrections: block-size-dependent key rate using composable security bound; `photons` per run sets block size `n`; quantifies departure from asymptotic regime at low photon counts and short distances |
| QBER decomposition by error source: track separate contributions from dark counts, dephasing, source errors, and basis bias per simulation point; identify dominant noise mechanism per parameter regime |

### Project Report

| Item |
|------|
| Justify every methodology decision in thesis: multi-seeding rationale (statistical robustness, seed count choice), k-means relay placement, Monte Carlo run counts, QBER cutoff threshold (security proofs), config layer choices (commercially available hardware specs) — each needs a cited or argued justification |
| MDI vs BB84 deployment recommendations section: use security level taxonomy (L0–L5) to frame when MDI is the right choice despite key rate being always worse; argument centres on trust assumptions, not raw performance |
| Explain MDI network-scale key rate gap (~10× vs ~3× at P2P) in results/discussion: investigate candidate causes (relay routing overhead, BSM success rate compounding, passive optical insertion loss, increased hop distances at network scale) and present supported explanation |

note ^ the above is largely solved due to a number of causes - i) relays add distance to total fibre link so total loss greater; ii) quadratic efficiency dependency means greater penalty for mdi in network setting on average; iii) twice the effect from insertion loss adds to the gap

---

## Open Questions

| Question |
|----------|
| **MDI network-scale key rate gap:** MDI is ~10× worse than BB84 at network scale but only approx. 3× worse at P2P. Candidate causes: relay routing adds hops (longer effective distances), BSM success rate (approx. 50%) compounds across more links, passive optical switch insertion loss, cross-cluster pairs routed through more nodes. Needs targeted experiment to isolate dominant factor. See also Project Report item. |
| **Missing lower error bars at high distance/noise:** at near-cutoff distances, lower IQR/min whiskers are absent on MDI plots. Failed runs are excluded before aggregation, so the surviving runs cluster near the QBER threshold with near-zero spread below the median. Unclear whether this reflects genuine distribution shape or an artefact of the cutoff filtering — worth checking whether including failed runs (as zero key rate) changes the picture. |

### Extensions

| Item |
|------|
| Interactive DB replot TUI (`scripts/analyse/tui.py`): Textual app with P2P and Network tabs; P2P tab functional; Network tab broken (Select widget issues with Textual 8.x); replace CLI scripts (`p2p.py`, `network.py`) with a unified TUI interface when Textual API stabilises |
| Timing data extraction: extend `lib/progress.py` to record per-step and total wall-clock times; write to a sidecar JSON (`<output_stem>_timing.json`) alongside every script run; enables runtime profiling, Monte Carlo scaling estimates, and cost modelling |
| Security level taxonomy: define deployment tiers L0–L5 by trust assumption (L0: trust all components except links = ideal QKD; ... L5: trust nothing = device-independent QKD); map BB84 and MDI-QKD to appropriate levels; use as framework for recommendations on when MDI is warranted despite key rate deficit |
| MDI deployment on existing network infrastructure: scoping exercise — if fibre topology is fixed (no relay placement freedom), how does MDI performance change? Assess feasibility and cost delta vs greenfield deployment; flag as potential standalone research project |
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
| Cost–rate Pareto optimisation: bi-objective problem over (K, N, topology seed). Two dual problems: (1) fixed budget C_max → find configuration maximising avg key rate; (2) fixed min rate R_min → find configuration minimising cost. Sweep K and seed at fixed N, compute (cost, avg_key_rate) per point, plot Pareto frontier for each protocol; configurations on the frontier are deployment-optimal. Practically: run cost_sweep over a grid of K values, extract frontier via standard 2D Pareto filter. Useful for deployment planning: given a capex budget, which relay count gives the best key rate for MDI, and in what detector/source configuration for both MDI and BB84? |

# ROADMAP

---

## Complete

### Modelling Layers

| Layer | Description |
|-------|-------------|
| 1 | Fibre loss: Beer-Lambert `T = 10^(-αL/10)` |
| 2 | Detector efficiency `η_d` |
| 3 | Dark counts: per-slot Bernoulli + lost-slot model |
| 4 | Node / connector loss |
| 5 | Source bit errors |
| 6 | Detector basis bias `η_Z` / `η_X` |
| 7 | Fibre dephasing (`DephaseNoiseModel`, rate per km) |
| 8 | Beam splitter efficiency (MDI relay BSM, η_bs) |

### Infrastructure

| Feature |
|---------|
| JSON config presets + CLI overrides |
| Multiprocessing: P2P scripts split runtimes across cores; network scripts split pairs across cores (one pool per protocol call) |
| Compare scripts: length, loss, efficiency, dark count, node loss, source error, dephasing, basis bias, beam splitter efficiency, Charlie placement (`scripts/P2P/compare/`) |
| Run-all parallel launcher (`scripts/P2P/compare/run_all.py`): all 10 compare scripts in parallel; auto-saves to timestamped `docs/figures/<Month>/<YYYYMMDD> - P2P parameters/all parameters/` |
| Layer comparison script (`scripts/P2P/layers.py`) |
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
| Passive optical routing model: cross-cluster photon redirection via optical switch (configurable insertion loss, default 1 dB) |
| Key rate vs relay count K — both protocols (`scripts/network/relay_sweep.py`) |
| Network success rate (QBER < 11%) vs relay count K |
| Multi-seed averaging (`--seeds N`): repeat sweep over N random placements, report mean ± std across seeds for statistically robust results |

#### Experiment 2 — User count sweep

| Item |
|------|
| Key rate vs user count N — both protocols (`scripts/network/user_sweep.py`) |
| Network success rate vs user count N |
| Cost tracking: total fibre (km), link count, component count per simulation |
| Multi-seed averaging (`--seeds N`): relay positions re-optimised per seed; mean ± std across seeds reported |

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

---

## Planned

### Infrastructure

| Feature |
|---------|
| `--compare-configs` flag on all compare scripts: run same sweep under 2–3 config presets, overlay on one figure |
| Interactive TUI launcher (`scripts/tui.py`): arrow-key menus for P2P or network path, full parameter setup, assembles and optionally runs the target script; optionally saves config JSON |

### Data Persistence

#### `scripts/analyse/` — Interactive TUI (`tui.py` + `db.py`, ~400 lines total)

Reconstruct any P2P or network figure from `results.db` without re-running simulations.

**Stack:** Textual (TUI), matplotlib (plot window, same pattern as sweep scripts), pandas, `lib/functions.py:DEFAULTS`

**Files:**
- `db.py` (~120 lines): column metadata + DEFAULTS mapping, `count_p2p`, `query_p2p`, `query_network`, `list_distinct`
- `tui.py` (~280 lines): Textual app, two tabs (P2P / Network), reactive status bar

**P2P tab controls:**
- Sweep: radio select any of the 10 sweepable columns
- Fixed params: all 10 columns shown; swept column grays out; `bs_eff` grays when BB84-only; defaults from `DEFAULTS` except `fibre_len` → 25 km
- Protocol: BB84 / MDI checkboxes
- Error mode: bars / shade / sigma / iqr / sem (same 5 modes as compare scripts, same plot logic)
- Plot button: opens matplotlib window in daemon thread; user saves via toolbar

**Fixed param defaults (P2P):**

| DB column | Default |
|---|---|
| `fibre_len` | 25 km (hardcoded) |
| `len_loss` | `DEFAULTS["fibre_loss_db_per_km"]` = 0.2 |
| `init_loss` | `DEFAULTS["init_loss"]` = 0.1 |
| `detector_eff_z` | `DEFAULTS["detector_efficiency"]` = 0.65 |
| `dark_count` | `DEFAULTS["dark_count_rate"]` = 100 |
| `node_loss_db` | `DEFAULTS["node_loss_db"]` = 2.0 |
| `source_err_rate` | `DEFAULTS["source_error_rate"]` = 0.005 |
| `detector_eff_x` | `DEFAULTS["det_eff_x"]` = 0.85 |
| `dephasing_rate` | `DEFAULTS["dephasing_rate"]` = 0.0001 |
| `bs_eff` | `DEFAULTS["bs_eff"]` = 0.97 |

**Network tab controls:**
- X axis: `k_relays` / `n_users` (auto-sets experiment)
- Y axis: `avg_key_rate` / `success_rate` / `min_key_rate` / `max_key_rate`
- Fixed params: complement of X axis, `area_km`, `seed` (blank = aggregate all seeds)
- Protocol + error mode same as P2P tab

**Reactivity:** any control change → debounced 300 ms → `COUNT(*)` query → status bar updates (`filtered: N / 2,270,000 rows  Q: Xs`)

**Error mode → plot logic:**

| Mode | Aggregation | matplotlib call |
|---|---|---|
| `bars` | min/max | `errorbar(yerr=[lower, upper])` |
| `sigma` | log-space ±1σ | `errorbar(yerr=[r·(1−e⁻ˢ), r·(eˢ−1)])` |
| `iqr` | Q25/Q75 | `errorbar(yerr=[r−q25, q75−r])` |
| `sem` | std/√n | `errorbar(yerr=sem)` |
| `shade` | log-space ±1σ band | `plot` + `fill_between` |

### Network Scale Modelling

#### Experiment 1 — Relay count sweep

| Item |
|------|
| Checkpoint saving: persist intermediate results per K/N to JSON so long runs can recover from crash |
| End-of-sweep summary table: print formatted K/N × protocol × key rate × success rate × fibre km table to stdout |

#### Experiment 2 — User count sweep

| Item |
|------|
| Cost-efficiency metric: key rate per unit cost vs N — both protocols |

#### Experiment 3 — Real-world topology case studies

| Item |
|------|
| Simulate specific named QKD network topologies as dissertation case studies: fix node positions to match real geography, run both protocols, compare against random-topology results. Candidate networks: BT QKD network (UK), Berrevoets et al. topology, Tokyo QKD network, Belgian QKD network (TBC) |

### Analysis

| Item |
|------|
| IQR error mode on network scripts: `--error iqr` shows Q1/Q3 band (shaded) instead of ±1σ; more robust to outlier seeds; add to `relay_sweep.py` and `user_sweep.py` alongside existing `bars`/`shade` options |
| Sim count annotation on analyse figures: display number of simulations (MC runs × seeds) contributing to each data point, either as annotated text per point or in figure subtitle/legend |
| Validate k-means + centroid as optimal MDI relay placement: benchmark against alternatives (random placement, grid, ILP-optimal); confirm or replace as the canonical topology strategy |
| Monte Carlo sample count scaling: for key rates of order 10^-x, use 10^(x+1) samples; smallest observed rates ~10^-2 → target 1000 runs per point where feasible; audit all scripts and increase run counts accordingly |
| Isolated parameter script (`scripts/P2P/isolate.py`): complement to `layers.py`; each curve = all-ideal config except one realistic parameter; overlay all isolated curves on one figure to compare each parameter's independent impact on key rate |
| Finite-key corrections: block-size-dependent key rate using composable security bound; `photons` per run sets block size `n`; quantifies departure from asymptotic regime at low photon counts and short distances |
| Analytical key rate overlay: plot closed-form Shor-Preskill (BB84) and Ma et al. 2012 (MDI-QKD) formula on sweep figures as validation reference; mismatch flags simulation error |
| QBER decomposition by error source: track separate contributions from dark counts, dephasing, source errors, and basis bias per simulation point; identify dominant noise mechanism per parameter regime |
| Parameter sensitivity ranking: compute d(key_rate)/d(param) at operating point for each physical parameter; produce ranked bar chart identifying which hardware spec drives performance most |

### Project Report

| Item |
|------|
| Justify every methodology decision in thesis: multi-seeding rationale (statistical robustness, seed count choice), k-means relay placement, Monte Carlo run counts, QBER cutoff threshold, config layer choices — each needs a cited or argued justification |
| MDI vs BB84 deployment recommendations section: use security level taxonomy (L0–L5) to frame when MDI is the right choice despite key rate being always worse; argument centres on trust assumptions, not raw performance |
| Explain MDI network-scale key rate gap (~10× vs ~3× at P2P) in results/discussion: investigate candidate causes (relay routing overhead, BSM success rate compounding, passive optical insertion loss, increased hop distances at network scale) and present supported explanation |

---

## Open Questions

| Question |
|----------|
| **MDI network-scale key rate gap:** MDI is ~10× worse than BB84 at network scale but only approx. 3× worse at P2P. Candidate causes: relay routing adds hops (longer effective distances), BSM success rate (approx. 50%) compounds across more links, passive optical switch insertion loss, cross-cluster pairs routed through more nodes. Needs targeted experiment to isolate dominant factor. See also Project Report item. |
| **Missing lower error bars at high distance/noise:** at near-cutoff distances, lower IQR/min whiskers are absent on MDI plots. Failed runs are excluded before aggregation, so the surviving runs cluster near the QBER threshold with near-zero spread below the median. Unclear whether this reflects genuine distribution shape or an artefact of the cutoff filtering — worth checking whether including failed runs (as zero key rate) changes the picture. |

### Extensions

| Item |
| Timing data extraction: extend `lib/progress.py` to record per-step and total wall-clock times; write to a sidecar JSON (`<output_stem>_timing.json`) alongside every script run; enables runtime profiling, Monte Carlo scaling estimates, and cost modelling |
|------|
| Security level taxonomy: define deployment tiers L0–L5 by trust assumption (L0: trust all components except links = ideal QKD; ... L5: trust nothing = device-independent QKD); map BB84 and MDI-QKD to appropriate levels; use as framework for recommendations on when MDI is warranted despite key rate deficit |
| MDI deployment on existing network infrastructure: scoping exercise — if fibre topology is fixed (no relay placement freedom), how does MDI performance change? Assess feasibility and cost delta vs greenfield deployment; flag as potential standalone research project |
| Trusted-node BB84 network: users connect to K trusted relay nodes (O(N) fibre, same infrastructure as MDI); relay holds key material and performs XOR combine; cross-relay pairs use relay-relay BB84 links; key rate bottlenecked by slowest link in chain |
| Trusted-node BB84 vs MDI-QKD vs direct-link BB84: three-way comparison of key rate, cost, and user scalability; isolates the cost of the MDI trust-removal guarantee |
| Decoy-state key rate formula: vacuum + weak decoy correction for PNS-attack resistance; relevant if source model is relaxed from ideal single-photon to weak coherent pulse (WCP) |
| WDM multi-user MDI-QKD: multiple Alice-Bob pairs on separate wavelengths, MUX onto shared fibre, DEMUX at Charlie for per-channel BSM |
| Key rate vs WDM user count: MUX/DEMUX insertion loss (~1–3 dB per device) per channel |
| Quantum memory coherence time at WDM relay nodes: T1/T2 decoherence during inter-channel wait limits scalable user count |
| Key rate vs memory coherence time (T2 sweep) |
| Entanglement swapping at relay nodes (MDI-QKD, no trusted relay required) |
| Long-distance repeater chain: N-hop linear topology for range extension (BB84 and MDI-QKD) |
| Key rate vs number of repeater hops (sweep) |
| BB84 vs MDI-QKD repeater chain performance head-to-head |
| Fully connected BB84 (direct pairwise links, no relay) as additional baseline |
| Relay placement sensitivity: random vs optimal placement comparison |
| Cross-relay vs same-relay pair success rate comparison |

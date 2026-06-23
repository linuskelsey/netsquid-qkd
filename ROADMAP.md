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
| Per-point error bars on compare scripts (`--error bars` min/max whiskers, `--error shade` ±1σ band) |
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

DB layer removed for redesign. P2P and network schemas will be rebuilt together with a shared structure.

| Feature |
|---------|
| P2P results DB (`lib/db.py`, `scripts/P2P/analyse.py`) — removed, to be redesigned |
| Network results DB — design pending |
| `scripts/network/analyse.py`: replot any saved network sweep without re-running — design pending |

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

### Analysis

| Item |
|------|
| Finite-key corrections: block-size-dependent key rate using composable security bound; `photons` per run sets block size `n`; quantifies departure from asymptotic regime at low photon counts and short distances |
| Analytical key rate overlay: plot closed-form Shor-Preskill (BB84) and Ma et al. 2012 (MDI-QKD) formula on sweep figures as validation reference; mismatch flags simulation error |
| QBER decomposition by error source: track separate contributions from dark counts, dephasing, source errors, and basis bias per simulation point; identify dominant noise mechanism per parameter regime |
| Parameter sensitivity ranking: compute d(key_rate)/d(param) at operating point for each physical parameter; produce ranked bar chart identifying which hardware spec drives performance most |

### Extensions

| Item |
|------|
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

# ROADMAP

## Modelling Layers

| Layer | Description | Status |
|-------|-------------|--------|
| 1 | Fibre loss: Beer-Lambert `T = 10^(-αL/10)` | complete |
| 2 | Detector efficiency `η_d` | complete |
| 3 | Dark counts: per-slot Bernoulli + lost-slot model | complete |
| 4 | Node / connector loss | complete |
| 5 | Source bit errors | complete |
| 6 | Detector basis bias `η_Z` / `η_X` | complete |
| 7 | Fibre dephasing (`DephaseNoiseModel`, rate per km) | complete |
| 8 | Beam splitter efficiency (MDI relay BSM, η_bs) | complete |

## Infrastructure

| Feature | Status |
|---------|--------|
| JSON config presets + CLI overrides | complete |
| Multiprocessing (runtimes split across cores) | complete |
| Compare scripts: length, loss, efficiency, dark count, node loss, source error, dephasing, basis bias, beam splitter efficiency, Charlie placement (`scripts/P2P/compare/`) | complete |
| Run-all parallel launcher (`scripts/P2P/compare/run_all.py`) | complete |
| Layer comparison script (`scripts/P2P/layers.py`) | complete |
| Config presets unified (layer0–layer8, cumulative, industry-typical values) | complete |
| Raw script config wiring | complete |
| `--workers` flag on all compare scripts (currently hardcoded to 80% CPU) | complete |
| `--compare-configs` flag on all compare scripts: run same sweep under 2–3 config presets, overlay on one figure | planned |
| Interactive TUI launcher (`scripts/tui.py`): arrow-key menus for P2P or network path, full parameter setup, assembles and optionally runs the target script; optionally saves config JSON | planned |
| Timing wrapper + progress indicator: elapsed wall-clock time printed at end of every script run (total, and per-sweep-point for network scripts); compact inline progress line e.g. `37% complete (seed 4/10, relay 5/6)` updated after each sweep point | planned |

## Data Persistence

DB layer removed for redesign. P2P and network schemas will be rebuilt together with a shared structure.

| Feature | Status |
|---------|--------|
| P2P results DB (`lib/db.py`, `scripts/P2P/analyse.py`) | removed — to be redesigned |
| Network results DB | planned (design pending) |
| `scripts/network/analyse.py`: replot any saved network sweep without re-running | planned (design pending) |

---

## Network Scale Modelling

Primary focus: metropolitan multi-user networks. Long-distance repeater chains treated as extension.

### Experiment 1 — Relay count sweep
Fixed N users (randomly placed in geographic space). Vary relay count K. Relay positions optimised per K by minimising total user-to-nearest-relay distance (k-means / least-squares). BB84 (trusted relay) and MDI-QKD simulated on identical infrastructure. K at which key rate plateaus becomes the fixed relay count for Experiment 2.

| Item | Status |
|------|--------|
| Network topology generator: random user placement, per-K relay optimisation (`network/topology.py`) | complete |
| Network topology visualiser: MDI cluster / BB84 mesh side-by-side (`network/visualise_network.py`) | complete |
| BB84 network simulator: all N(N-1)/2 direct pairs (`network/bb84_network.py`) | complete |
| MDI-QKD network simulator: nearest-relay routing, cross-cluster passive optical routing (`network/mdi_network.py`) | complete |
| Passive optical routing model: cross-cluster photon redirection via optical switch (configurable insertion loss, default 1 dB) | complete |
| Key rate vs relay count K — both protocols (`scripts/network/relay_sweep.py`) | complete |
| Network success rate (QBER < 11%) vs relay count K | complete |
| Multi-seed averaging (`--seeds N`): repeat sweep over N random placements, report mean ± std across seeds for statistically robust results | planned |
| Checkpoint saving: persist intermediate results per K/N to JSON so long runs can recover from crash | planned |
| End-of-sweep summary table: print formatted K/N × protocol × key rate × success rate × fibre km table to stdout | planned |

### Experiment 2 — User count sweep
Fixed K relays (positions from Experiment 1 plateau). Vary N users. All N(N-1)/2 pairs simulated per N value; averaged over multiple random user placements (seeds) to yield statistics for an average N-user metropolitan network. Relay positions fixed; only user positions vary per seed.

Cost tracked per simulation: BB84 (N sources, N detectors, N(N-1)/2 fibre links) vs MDI (N sources, 2K detectors, K beam splitters, K optical switches, N user-relay + K(K-1)/2 relay-relay fibre links). Total fibre computed from topology geometry.

| Item | Status |
|------|--------|
| Key rate vs user count N — both protocols (`scripts/network/user_sweep.py`) | complete |
| Network success rate vs user count N | complete |
| Cost tracking: total fibre (km), link count, component count per simulation | complete |
| Cost-efficiency metric: key rate per unit cost vs N — both protocols | planned |

## Analysis

| Item | Status |
|------|--------|
| Key rate vs distance | complete |
| Key rate vs fibre loss | complete |
| Key rate vs detector efficiency | complete |
| Key rate vs dark count rate | complete |
| Key rate vs node/connector loss | complete |
| Key rate vs source error rate | complete |
| Key rate vs fibre dephasing rate | complete |
| Key rate vs detector basis bias (η_X sweep) | complete |
| Key rate vs beam splitter efficiency (MDI only) | complete |
| Realistic hardware regime shading on all sweep plots | complete |
| QBER threshold cutoffs (11% hard cutoff, both protocols) | complete |
| Per-point error bars on compare scripts (`--error bars` min/max whiskers, `--error shade` ±1σ band) | complete |
| Always-on min/max error bars on `layers.py` | complete |
| Charlie placement sweep (asymmetric Alice-Charlie / Charlie-Bob links) | complete |
| Script to compare effect of each layer of modelling parameter per-protocol | complete |
| Finite-key corrections: block-size-dependent key rate using composable security bound; `photons` per run sets block size `n`; quantifies departure from asymptotic regime at low photon counts and short distances | planned |
| Analytical key rate overlay: plot closed-form Shor-Preskill (BB84) and Ma et al. 2012 (MDI-QKD) formula on sweep figures as validation reference; mismatch flags simulation error | planned |
| QBER decomposition by error source: track separate contributions from dark counts, dephasing, source errors, and basis bias per simulation point; identify dominant noise mechanism per parameter regime | planned |
| Parameter sensitivity ranking: compute d(key_rate)/d(param) at operating point for each physical parameter; produce ranked bar chart identifying which hardware spec drives performance most | planned |

### Extensions (nice to have)

| Item | Status |
|------|--------|
| Trusted-node BB84 network: users connect to K trusted relay nodes (O(N) fibre, same infrastructure as MDI); relay holds key material and performs XOR combine; cross-relay pairs use relay-relay BB84 links; key rate bottlenecked by slowest link in chain | extension |
| Trusted-node BB84 vs MDI-QKD vs direct-link BB84: three-way comparison of key rate, cost, and user scalability; isolates the cost of the MDI trust-removal guarantee | extension |
| Decoy-state key rate formula: vacuum + weak decoy correction for PNS-attack resistance; relevant if source model is relaxed from ideal single-photon to weak coherent pulse (WCP) | extension |
| WDM multi-user MDI-QKD: multiple Alice-Bob pairs on separate wavelengths, MUX onto shared fibre, DEMUX at Charlie for per-channel BSM | extension |
| Key rate vs WDM user count: MUX/DEMUX insertion loss (~1–3 dB per device) per channel | extension |
| Quantum memory coherence time at WDM relay nodes: T1/T2 decoherence during inter-channel wait limits scalable user count | extension |
| Key rate vs memory coherence time (T2 sweep) | extension |
| Entanglement swapping at relay nodes (MDI-QKD, no trusted relay required) | extension |
| Long-distance repeater chain: N-hop linear topology for range extension (BB84 and MDI-QKD) | extension |
| Key rate vs number of repeater hops (sweep) | extension |
| BB84 vs MDI-QKD repeater chain performance head-to-head | extension |
| Fully connected BB84 (direct pairwise links, no relay) as additional baseline | extension |
| Relay placement sensitivity: random vs optimal placement comparison | extension |
| Cross-relay vs same-relay pair success rate comparison | extension |

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
| Compare scripts: length, loss, efficiency, dark count, node loss, source error, dephasing, basis bias, beam splitter efficiency (`scripts/P2P/compare/`) | complete |
| Run-all parallel launcher (`scripts/P2P/compare/run_all.py`) | complete |
| Layer comparison script (`scripts/P2P/layers.py`) | complete |
| Config presets unified (layer0–layer8, cumulative, industry-typical values) | complete |
| Raw script config wiring | complete |

## Network Scale Modelling

### Phase 1 — Analytical topology optimisation
Identify optimal topology (repeater spacing, number of hops) for maximum key rate analytically before simulation.

| Item | Status |
|------|--------|
| Analytical key rate model for N-hop repeater chain | planned |
| Optimal repeater spacing derivation (BB84 trusted-node) | planned |
| Optimal repeater spacing derivation (MDI-QKD multi-Charlie) | planned |
| Quantum memory decoherence model (T1/T2, η_mem) | planned |
| BB84 vs MDI-QKD optimal topology comparison | planned |

### Phase 2 — Simulation-based scalability
Use optimal topology from Phase 1 as fixed input; sweep user count / network size.

| Item | Status |
|------|--------|
| N-node repeater chain implementation (NetSquid) | planned |
| Entanglement swapping at repeater nodes (MDI-QKD native) | planned |
| Trusted-node repeater model for BB84 | planned |
| Key rate vs number of users / network nodes | planned |
| Key rate vs memory coherence time | planned |
| Effect of repeaters on BB84: range extension vs security assumptions | planned |
| Effect of repeaters on MDI-QKD: multi-Charlie chain performance | planned |

### Extensions (nice to have)

| Item | Status |
|------|--------|
| Key rate vs number of repeater hops (sweep) | extension |
| Repeater spacing optimisation sweep (simulation) | extension |
| BB84 vs MDI-QKD repeater performance head-to-head | extension |
| Quantum memory decoherence: T2 dephasing time model (η_mem vs T2, sweep vs coherence time) | extension |

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
| Charlie placement sweep (asymmetric links) | planned |
| Script to compare effect of each layer of modelling parameter per-protocol | complete |

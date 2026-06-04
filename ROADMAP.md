# ROADMAP

## Modelling Layers

| Layer | Description | Status |
|-------|-------------|--------|
| 1 | Fibre loss: Beer-Lambert `T = 10^(-αL/10)` | complete |
| 2 | Detector efficiency `η_d` | complete |
| 3 | Dark counts: per-slot Bernoulli + lost-slot model | complete |
| 4 | Node / connector loss | planned |
| 5 | Source bit errors | planned |
| 6 | Detector basis bias | planned |
| 7 | Fibre dephasing | planned |

## Infrastructure

| Feature | Status |
|---------|--------|
| JSON config presets + CLI overrides | complete |
| Multiprocessing (runtimes split across cores) | complete |
| Compare scripts: length, loss, efficiency, dark count | complete |
| Raw script config wiring | planned |
| Top-level CLI `scripts/compare/run.py` (issue #4) | planned |

## Analysis

| Item | Status |
|------|--------|
| Key rate vs distance | complete |
| Key rate vs fibre loss | complete |
| Key rate vs detector efficiency | complete |
| Key rate vs dark count rate | complete |
| QBER threshold crossings vs distance / loss / η_d | planned |
| Idealised architectural overhead (issue #7) | planned |
| Charlie placement sweep (asymmetric links) | planned |
| Dark count QBER impact at long haul | planned |

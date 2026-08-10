# Key Rate vs Detector Efficiency

Fixed parameters for this plot:

- **Fibre length**: 20.0 km
- **Fibre loss**: 0.18 dB/km
- **Dark count rate**: 50.0 cps
- **Init loss**: 0.1
- **Node loss**: 2.0 dB
- **Source error rate**: 0.015
- **Dephasing rate**: 3.2e-07 /km
- **Beam splitter efficiency**: 0.97
- **Runtimes per point**: 1000
- **Error display**: shade
- **Detector efficiency sweep points**: [1.0, 0.99, 0.95, 0.9, 0.8, 0.7, 0.65, 0.6, 0.5, 0.4, 0.3, 0.2, 0.15]

Other assumptions:

- Detector efficiency is the swept axis; config value for it is ignored.
- Reconstructed from data/results.db (run committed 2026-08-10 16:14-16:41) after the live run exited without --output-dir; figure and stats reproduce the original efficiency.py plotting/aggregation code exactly.

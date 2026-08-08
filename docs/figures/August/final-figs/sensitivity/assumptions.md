# Parameter Sensitivity Ranking

Fixed parameters for this plot:

- **Operating distance**: 25 km
- **Runtimes per point**: 1000
- **Baseline**: fully ideal (layer 0): fibre_loss_db_per_km=0.0, init_loss=0.0, detector_efficiency=1.0, dark_count_rate=0, node_loss_db=0.0, source_error_rate=0.0, dephasing_rate=0.0, det_eff_x=1.0, bs_eff=1.0
- **Realistic values tested (one at a time)**: {'fibre_loss_db_per_km': 0.18, 'detector_efficiency': 0.9, 'dark_count_rate': 50, 'init_loss': 0.1, 'node_loss_db': 2.0, 'source_error_rate': 0.015, 'dephasing_rate': 3.2e-07, 'det_eff_x': 0.715, 'bs_eff': 0.97}
- **Ideal BB84 key rate**: 1223.85 kbps
- **Ideal MDI key rate**: 482.15 kbps

Other assumptions:

- Sensitivity = (R_ideal - R_param) / R_ideal x 100%.
- bs_eff is MDI-only (BB84 bar set to 0).
- Results sorted by BB84 impact descending.

# MDI: Isolated Parameter Impact

Fixed parameters for this plot:

- **Baseline**: fully ideal (layer 0): fibre_loss_db_per_km=0.0, init_loss=0.0, detector_efficiency=1.0, dark_count_rate=0, node_loss_db=0.0, source_error_rate=0.0, dephasing_rate=0.0, det_eff_x=1.0, bs_eff=1.0
- **Distance sweep points (km)**: [1, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
- **Runtimes per point**: 1000
- **Realistic values tested (one at a time)**: {'fibre_loss_db_per_km': 0.18, 'detector_efficiency': 0.9, 'dark_count_rate': 50, 'init_loss': 0.1, 'node_loss_db': 2.0, 'source_error_rate': 0.015, 'dephasing_rate': 3.2e-07, 'det_eff_x': 0.715, 'bs_eff': 0.97}

Other assumptions:

- Each curve sets exactly one parameter to its realistic value; all others stay ideal.
- MDI includes bs_eff; BB84 does not.

# Parameter Sensitivity Ranking

Fixed parameters for this plot:

- **Operating distance**: 25.0 km
- **Runtimes per point**: 1000
- **Baseline**: fully ideal (layer 0): fibre_loss_db_per_km=0.0, init_loss=0.0, detector_efficiency=1.0, dark_count_rate=0, node_loss_db=0.0, source_error_rate=0.0, dephasing_rate=0.0, det_eff_x=1.0, bs_eff=1.0
- **Realistic values tested (one at a time)**: {'Fibre loss ($\\alpha$=0.18 dB/km)': 0.18, 'Detector eff SPAD ($\\eta_d$=0.20, IDQ ID230)': 0.2, 'Detector eff SNSPD ($\\eta_d$=0.90, IDQ ID281)': 0.9, 'Dark count ($d_c$=50 cps)': 50, 'Init loss ($L_i$=0.10)': 0.1, 'Node loss ($L_n$=2.0 dB)': 2.0, 'Source error ($\\varepsilon_s$=0.015)': 0.015, 'Dephasing ($\\beta$=3.2$\\times10^{-7}$/km)': 3.2e-07, 'Basis bias ($\\eta_X$=0.715)': 0.715, 'BS eff ($\\eta_{bs}$=0.97, MDI only)': 0.97}
- **Ideal BB84 key rate**: 1223.40 kbps
- **Ideal MDI key rate**: 481.63 kbps

Other assumptions:

- Sensitivity = (R_ideal - R_param) / R_ideal x 100%.
- bs_eff is MDI-only (BB84 bar set to 0).
- Results sorted by BB84 impact descending.

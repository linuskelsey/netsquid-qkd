# Parameters

## Config Presets

Presets in `configs/` layer physical effects cumulatively. Each layer adds one parameter at its industry-typical value to the previous layer. All values provisional pending literature verification.

| File | Adds | α | η_d | d_c | L_i | L_n | ε_s | β | η_bs |
|------|------|---|-----|-----|-----|-----|-----|---|------|
| `layer0_ideal.json` | baseline (all ideal) | 0.0 | 1.0 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 1.0 |
| `layer1_loss.json` | + fibre loss | 0.20 | 1.0 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 1.0 |
| `layer2_eff.json` | + detector efficiency | 0.20 | 0.65 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 1.0 |
| `layer3_dark.json` | + dark count rate | 0.20 | 0.65 | 100 | 0.0 | 0.0 | 0.0 | 0.0 | 1.0 |
| `layer4_init_loss.json` | + TX insertion loss | 0.20 | 0.65 | 100 | 0.10 | 0.0 | 0.0 | 0.0 | 1.0 |
| `layer5_node_loss.json` | + RX node loss | 0.20 | 0.65 | 100 | 0.10 | 2.0 | 0.0 | 0.0 | 1.0 |
| `layer6_source_err.json` | + source error rate | 0.20 | 0.65 | 100 | 0.10 | 2.0 | 0.005 | 0.0 | 1.0 |
| `layer7_dephasing.json` | + fibre dephasing | 0.20 | 0.65 | 100 | 0.10 | 2.0 | 0.005 | 1e-4 | 1.0 |
| `layer8_bs_eff.json` | + BS efficiency (MDI only) | 0.20 | 0.65 | 100 | 0.10 | 2.0 | 0.005 | 1e-4 | 0.97 |

Pass any preset with `--config configs/<file>`. CLI flags override config values.

## Simulation Defaults

Defaults used when no `--config` and no CLI flag is given:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `fibre` | 50 km | Alice-Bob separation (not applicable for length sweep) |
| `lenLoss` | 0.2 dB/km | Fibre attenuation coefficient α |
| `detectorEffZ` | 0.65 | Z-basis detector efficiency η_Z (set via `--det-eff` or config `detector_efficiency`) |
| `detectorEffX` | = η_Z | X-basis detector efficiency η_X (set via `--det-eff-x`; defaults to η_Z if omitted) |
| `dephasingRate` | 1×10⁻⁴ /km | Fibre dephasing rate per km (set via `--dephasing-rate` or config `dephasing_rate`) |
| `bsEff` | 0.97 | Beam splitter efficiency at MDI relay BSM, η_bs (MDI only; set via `--bs-eff` or config `bs_eff`) |
| `darkCount` | 100 cps | Dark count rate d_c |
| `initLoss` | 0.10 | TX-side insertion loss, linear fraction [0–1] (e.g. 0.1 = 10%) |
| `nodeLossDb` | 2.0 dB | RX-side node/connector loss in dB (Bob for BB84, Charlie for MDI) |
| `sourceErrRate` | 0.005 | Source bit error rate ε_s |
| `runtimes` | 100 | Monte Carlo repetitions per sweep point |
| `photons` | 1024 | Photons per run |
| `charliePos` | 0.5 | Relay position as fraction of total link from Alice (MDI only; 0.5 = symmetric midpoint) |
| `workers` | 80% of CPU cores | Parallel worker processes (passed to run functions directly) |

## Hardware Parameter Reference

Realistic ranges drawn from deployed QKD systems (Lo et al. 2012, Tang et al. 2016, Berrevoets et al. 2022, Yin et al. 2016). Values marked ⁺ are provisional pending literature verification.

| Parameter (config key) | Symbol | Realistic range | Typical point | Source basis |
|------------------------|--------|----------------|---------------|--------------|
| `fibre_loss_db_per_km` | α | 0.15–0.25 dB/km | 0.20 dB/km | SMF-28 telecom fibre at 1550 nm |
| `detector_efficiency` | η_d | 0.15–0.95 | 0.65 (SNSPD metropolitan) | InGaAs 15–30%; SNSPD 80–95%; Tang 2016 ~65% |
| `dark_count_rate` | d_c | 1–10,000 cps | 100 cps (SNSPD) | SNSPD: 1–100 cps; InGaAs: 1,000–10,000 cps |
| `init_loss` | L_i | 0.02–0.20 | 0.10 ⁺ | Source-to-fibre coupling + connector at TX |
| `node_loss_db` | L_n | 0.5–4 dB | 2 dB ⁺ | FC/PC connectors + optical components at RX |
| `source_error_rate` | ε_s | 0.001–0.02 | 0.005 | Well-calibrated polarisation source; Lo 2012 used 1.5% |
| `dephasing_rate` | β | 1×10⁻⁵–1×10⁻³ /km | 1×10⁻⁴ /km ⁺ | SMF polarisation stability; literature rarely quoted explicitly |
| `bs_eff` | η_bs | 0.90–0.99 | 0.97 | Commercial 50:50 BS; integrated photonic ~95% |

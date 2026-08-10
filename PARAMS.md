# Parameters

## Config Presets

Presets in `configs/` layer physical effects cumulatively. Each layer adds one parameter at its
sourced, literature-backed value on top of the previous layer (`layer0_ideal.json` = all ideal).

| File | Adds | α (dB/km) | η_Z | d_c (cps) | L_i | L_n (dB) | ε_s | β (/km) | η_X | η_bs |
|------|------|-----------|-----|-----------|-----|----------|-----|---------|-----|------|
| `layer0_ideal.json` | baseline (all ideal) | 0.0 | 1.0 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 1.0 | 1.0 |
| `layer1_loss.json` | + fibre loss | 0.18 | 1.0 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 1.0 | 1.0 |
| `layer2_eff.json` | + detector efficiency | 0.18 | 0.90 | 0 | 0.0 | 0.0 | 0.0 | 0.0 | 1.0 | 1.0 |
| `layer3_dark.json` | + dark count rate | 0.18 | 0.90 | 50 | 0.0 | 0.0 | 0.0 | 0.0 | 1.0 | 1.0 |
| `layer4_init_loss.json` | + TX insertion loss | 0.18 | 0.90 | 50 | 0.10 | 0.0 | 0.0 | 0.0 | 1.0 | 1.0 |
| `layer5_node_loss.json` | + RX node loss | 0.18 | 0.90 | 50 | 0.10 | 2.0 | 0.0 | 0.0 | 1.0 | 1.0 |
| `layer6_source_err.json` | + source error rate | 0.18 | 0.90 | 50 | 0.10 | 2.0 | 0.015 | 0.0 | 1.0 | 1.0 |
| `layer7_dephasing.json` | + fibre dephasing | 0.18 | 0.90 | 50 | 0.10 | 2.0 | 0.015 | 3.2e-7 | 1.0 | 1.0 |
| `layer8_basis_bias.json` | + detector basis bias | 0.18 | 0.90 | 50 | 0.10 | 2.0 | 0.015 | 3.2e-7 | 0.715 | 1.0 |
| `layer9_bs_eff.json` | + BS efficiency (MDI only) | 0.18 | 0.90 | 50 | 0.10 | 2.0 | 0.015 | 3.2e-7 | 0.715 | 0.97 |

Pass any preset with `--config configs/<file>`. CLI flags override config values.

## Simulation Defaults (`lib/functions.py DEFAULTS`)

Used whenever no `--config` and no CLI flag is given — equivalent to `layer9_bs_eff.json`:

| Parameter | Default | Source basis |
|-----------|---------|--------------|
| `fibre_loss_db_per_km` α | 0.18 dB/km | Corning SMF-28 datasheet, max at 1550 nm |
| `init_loss` L_i | 0.10 | OZ Optics DTS0092 PM fused coupler, 0.4 dB max excess loss |
| `detector_efficiency` η_Z | 0.90 | IDQ ID281 SNSPD at telecom wavelength |
| `dark_count_rate` d_c | 50 cps | IDQ ID281 SNSPD at telecom |
| `node_loss_db` L_n | 2.0 dB | Duplinskiy et al. 2017 — measured Bob-receiver insertion loss (lumped approximation; see dissertation Simulation Model Limitations) |
| `source_error_rate` ε_s | 0.015 | Quandela Prometheus: g²(0) < 0.03 → ε_s < 0.015 |
| `det_eff_x` η_X | 0.715 | Grasselli et al. 2025: η_X = η_Z × 10^(-1/10), 1 dB extra insertion loss on the test-basis stage |
| `dephasing_rate` β | 3.2e-7 /km | PMD-derived: β = D²/2T², Corning SMF-28 D=0.04 ps/√km, IDQ ID281 jitter T=50 ps |
| `bs_eff` η_bs | 0.97 | Thorlabs TN1550R5F2, 0.15 dB excess loss (MDI relay BSM only) |
| `tortuosity_mean` | 1.0 | 1.0 = Euclidean (off); network scripts set >1.0 via `--tortuosity` |

Not in `DEFAULTS` (passed as run-function kwargs / CLI flags instead):

| Parameter | Default | Description |
|-----------|---------|--------------|
| `fibre` | 20 km | Alice–Bob separation (not applicable for length sweep) |
| `runtimes` | 100 (P2P scripts) / 20 (network scripts) | Monte Carlo repetitions per sweep point |
| `photons` | 1024 | Photons per run |
| `charliePos` | 0.5 | Relay position as fraction of total link from Alice (MDI only; 0.5 = symmetric midpoint) |
| `workers` | 80% of CPU cores | Parallel worker processes |
| `switch_loss_db` (network only) | 0.0 dB | Passive optical switch/circulator insertion loss at cross-cluster MDI relay; abstracted away — see dissertation Simulation Model Limitations |

## Hardware Parameter Reference

All 10 parameters below are sourced/cited (last verification pass 2026-08-06); see the "Layer N" prose
in `docs/dissertation/dissertation.tex` for full derivations.

| Parameter (config key) | Symbol | Realistic range | Default | Source |
|------------------------|--------|------------------|---------|--------|
| `fibre_loss_db_per_km` | α | 0.15–0.25 dB/km | 0.18 | Corning SMF-28 datasheet |
| `detector_efficiency` | η_Z | SPAD 0.10–0.25 (IDQ ID230); SNSPD 0.80–0.95 (IDQ ID281) | 0.90 (SNSPD) | IDQ ID230 / ID281 datasheets |
| `dark_count_rate` | d_c | SNSPD 25–100 cps (ID281); SPAD 70–250 cps, coupled to η (ID230) | 50 (SNSPD) | IDQ datasheets |
| `init_loss` | L_i | 0.05–0.30 | 0.10 | OZ Optics DTS0092 |
| `node_loss_db` | L_n | 1.0–4.0 dB | 2.0 | Duplinskiy et al. 2017, Opt. Express 25(23):28886 |
| `source_error_rate` | ε_s | 0.001–0.05 | 0.015 | Quandela Prometheus; Bozzio 2022 upper bound |
| `det_eff_x` | η_X | same range as η_Z | 0.715 | Grasselli et al. 2025, PRApplied 23:044011 |
| `dephasing_rate` | β | 2.6e-7–3.8e-7 /km (±20%) | 3.2e-7 | Corning SMF-28 PMD spec + IDQ ID281 timing jitter |
| `bs_eff` | η_bs | 0.87–0.99 | 0.97 | Thorlabs TN1550R5F2 |
| `switch_loss_db` (network only) | L_sw | not swept — abstracted to 0.0 dB | 0.0 | see dissertation Simulation Model Limitations |

# netsquid-qkd

NetSquid simulations comparing BB84 and MDI-QKD protocols.

UCL MSc Quantum Technologies Research Project — Linus Kelsey

---

## Structure

```
BB84/           BB84 Alice/Bob protocols and simulation runner
MDI/            MDI-QKD Alice/Bob/Charlie protocols and simulation runner
lib/            Shared utilities (delay model, photon source, config loader)
configs/        JSON parameter presets (layer0_ideal → layer3_loss_eff_dark)
scripts/
  raw/          Single-protocol run scripts
  compare/      Sweep scripts: key rate vs distance, loss, efficiency, dark counts
```

## Running

From the repo root:

```bash
# Single comparison at default parameters
python scripts/compare/length.py      # key rate vs distance
python scripts/compare/loss.py        # key rate vs fibre attenuation
python scripts/compare/efficiency.py  # key rate vs detector efficiency
python scripts/compare/dark_count.py  # key rate vs dark count rate
```

All comparison scripts accept CLI flags and an optional JSON config:

```bash
# Use a layered config preset
python scripts/compare/length.py --config configs/layer2_loss_eff.json

# Override individual parameters
python scripts/compare/length.py --loss 0.3 --det-eff 0.85 --runtimes 50

# Config preset + CLI override (CLI takes precedence)
python scripts/compare/length.py --config configs/layer3_loss_eff_dark.json --fibre 30
```

Config presets in `configs/`:

| File | α (dB/km) | η_d | d_c (cps) |
|------|-----------|-----|-----------|
| `layer0_ideal.json` | 0.0 | 1.0 | 0 |
| `layer1_loss.json` | 0.2 | 1.0 | 0 |
| `layer2_loss_eff.json` | 0.2 | 0.9 | 0 |
| `layer3_loss_eff_dark.json` | 0.2 | 0.9 | 100 |

Default parameters (no config, no CLI flags):

| Parameter | Default | Description |
|-----------|---------|-------------|
| `fibre` | 50 km | Alice-Bob separation (not applicable for length sweep) |
| `lenLoss` | 0.2 dB/km | Fibre attenuation coefficient α |
| `detEff` | 1.0 | Detector efficiency η_d |
| `darkCount` | 0 cps | Dark count rate d_c |
| `initLoss` | 0.0 | Insertion loss, linear fraction [0–1] (e.g. 0.1 = 10%) |
| `runtimes` | 100 | Monte Carlo repetitions per sweep point |
| `photons` | 1024 | Photons per run |

## Dependencies

- [NetSquid](https://netsquid.org) (requires registration)
- NumPy, Matplotlib

## Status and Roadmap

See [ROADMAP.md](ROADMAP.md).

# netsquid-qkd

NetSquid simulations comparing BB84 and MDI-QKD protocols.

UCL MSc Quantum Technologies Research Project — Linus Kelsey

---

## Structure

```
BB84/           BB84 Alice/Bob protocols and simulation runner
MDI/            MDI-QKD Alice/Bob/Charlie protocols and simulation runner
repeater/       (planned) Protocol-agnostic quantum repeater primitives
lib/            Shared utilities (delay model, photon source, config loader)
configs/        JSON parameter presets (layer0_ideal → layer8_bs_eff); memory + chain configs planned
scripts/
  P2P/
    raw/        Single-protocol run scripts
    compare/    Sweep scripts: key rate vs distance, loss, efficiency, dark count rate,
                node loss, source error rate, dephasing rate, detector basis bias,
                beam splitter efficiency; repeater sweeps planned
    layers.py   Effect of each modelling layer per protocol
```

## Running

From the repo root:

```bash
# Single comparison at default parameters
python scripts/P2P/compare/run_all.py     # run all 9 sweeps simultaneously

python scripts/P2P/compare/length.py      # key rate vs distance
python scripts/P2P/compare/loss.py        # key rate vs fibre attenuation
python scripts/P2P/compare/efficiency.py  # key rate vs detector efficiency
python scripts/P2P/compare/dark_count.py  # key rate vs dark count rate
python scripts/P2P/compare/node_loss.py   # key rate vs node/connector loss
python scripts/P2P/compare/source_err.py  # key rate vs source error rate
python scripts/P2P/compare/dephasing.py   # key rate vs fibre dephasing rate
python scripts/P2P/compare/basis_bias.py  # key rate vs detector basis bias (η_X sweep, η_Z fixed)
python scripts/P2P/compare/bs_eff.py      # key rate vs beam splitter efficiency (MDI only)
```

All comparison scripts accept CLI flags and an optional JSON config:

```bash
# Use a layered config preset
python scripts/P2P/compare/length.py --config configs/layer2_eff.json

# Override individual parameters
python scripts/P2P/compare/length.py --loss 0.3 --det-eff 0.85 --runtimes 50

# Basis-biased detector (X-basis efficiency lower than Z) — BB84/MDI runners only
python BB84/BB84_run.py --config configs/layer2_eff.json --det-eff-x 0.7
python MDI/mdiRun.py   --config configs/layer2_eff.json --det-eff-x 0.7

# Config preset + CLI override (CLI takes precedence)
python scripts/P2P/compare/length.py --config configs/layer3_dark.json --fibre 30
```

See [PARAMS.md](PARAMS.md) for config presets, simulation defaults, and realistic hardware parameter ranges.

## Dependencies

- [NetSquid](https://netsquid.org) (requires registration)
- NumPy, Matplotlib

## Status and Roadmap

See [ROADMAP.md](ROADMAP.md).

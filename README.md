# netsquid-qkd

NetSquid simulations comparing BB84 and MDI-QKD protocols.

UCL MSc Quantum Technologies Research Project — Linus Kelsey

---

## Structure

```
BB84/           BB84 Alice/Bob protocols and simulation runner
MDI/            MDI-QKD Alice/Bob/Charlie protocols and simulation runner
network/        Multi-user network simulation
  topology.py           User placement, k-means relay optimisation, BB84/MDI link distances
  bb84_network.py       BB84 over all N(N-1)/2 direct pairs; per-pair and network-level metrics
  mdi_network.py        MDI-QKD over all pairs via nearest relay; cross-cluster passive routing
  visualise_network.py  Side-by-side MDI cluster / BB84 mesh topology plot
lib/            Shared utilities (delay model, photon source, config loader, DB persistence)
configs/        JSON parameter presets (layer0_ideal → layer8_bs_eff)
scripts/
  P2P/
    raw/        Single-protocol run scripts
    compare/    Sweep scripts: key rate vs distance, loss, efficiency, dark count rate,
                node loss, source error rate, dephasing rate, detector basis bias,
                beam splitter efficiency, Charlie placement
    layers.py   Effect of each modelling layer per protocol
    analyse.py  Replot any saved sweep from results.db without re-running
  network/      (planned) Relay count sweep (Exp 1) and user count sweep (Exp 2)
```

## Running

From the repo root:

```bash
# Single comparison at default parameters
python scripts/P2P/compare/run_all.py       # run all 10 sweeps simultaneously

python scripts/P2P/compare/length.py        # key rate vs distance
python scripts/P2P/compare/loss.py          # key rate vs fibre attenuation
python scripts/P2P/compare/efficiency.py    # key rate vs detector efficiency
python scripts/P2P/compare/dark_count.py    # key rate vs dark count rate
python scripts/P2P/compare/node_loss.py     # key rate vs node/connector loss
python scripts/P2P/compare/source_err.py    # key rate vs source error rate
python scripts/P2P/compare/dephasing.py     # key rate vs fibre dephasing rate
python scripts/P2P/compare/basis_bias.py    # key rate vs detector basis bias (η_X sweep, η_Z fixed)
python scripts/P2P/compare/bs_eff.py        # key rate vs beam splitter efficiency (MDI only)
python scripts/P2P/compare/charlie_pos.py   # MDI key rate vs Charlie relay position (BB84 flat reference)
```

All comparison scripts accept CLI flags and an optional JSON config:

```bash
# Use a layered config preset
python scripts/P2P/compare/length.py --config configs/layer2_eff.json

# Override individual parameters
python scripts/P2P/compare/length.py --loss 0.3 --det-eff 0.85 --runtimes 50

# Error display: min/max whiskers (default) or ±1 std dev shading on log scale
python scripts/P2P/compare/length.py --error bars    # default
python scripts/P2P/compare/length.py --error shade

# Basis-biased detector (X-basis efficiency lower than Z) — BB84/MDI runners only
python BB84/BB84_run.py --config configs/layer2_eff.json --det-eff-x 0.7
python MDI/mdiRun.py   --config configs/layer2_eff.json --det-eff-x 0.7

# Config preset + CLI override (CLI takes precedence)
python scripts/P2P/compare/length.py --config configs/layer3_dark.json --fibre 30
```

Replot any saved sweep without re-running simulations:

```bash
python scripts/P2P/analyse.py --list                   # show what's in the DB
python scripts/P2P/analyse.py --script length          # replot length sweep
python scripts/P2P/analyse.py --script charlie_pos --error shade
```

All comparison scripts and `layers.py` save results to `results.db` (repo root) by default:

```bash
# Skip DB saving
python scripts/P2P/compare/length.py --no-save

# Use a custom DB path
python scripts/P2P/compare/length.py --db /path/to/custom.db

# Browse results interactively (requires: pip install litecli)
litecli results.db

# View schema without opening TUI
sqlite3 results.db ".schema"
```

## Network Simulations

Visualise a network topology (MDI cluster assignment + BB84 direct mesh):

```bash
python network/visualise_network.py --n 20 --k 3 --area 10 --seed 42
python network/visualise_network.py --n 20 --k 3 --save figures/topology.png
```

Run network simulations directly (used by sweep scripts):

```python
from network.topology import build_topology
from network.bb84_network import run_bb84_network
from network.mdi_network import run_mdi_network
from lib.functions import load_config

cfg  = load_config("configs/layer3_dark.json")
topo = build_topology(N=10, K=3, area_km=10, seed=42)

bb84 = run_bb84_network(topo, cfg, runtimes=20)
mdi  = run_mdi_network(topo, cfg, runtimes=20)

# bb84["avg_key_rate"], bb84["success_rate"], bb84["total_fibre_km"]
# mdi["avg_key_rate"],  mdi["success_rate"],  mdi["total_fibre_km"]
```

Key network cost outputs:

| Field | BB84 | MDI |
|-------|------|-----|
| `total_fibre_km` | Σ all N(N-1)/2 pair distances | Σ user-relay + relay-relay links |
| `n_links` | N(N-1)/2 | N + K(K-1)/2 |

See [NETWORK.md](NETWORK.md) for full experimental design and hypotheses.

See [PARAMS.md](PARAMS.md) for config presets, simulation defaults, and realistic hardware parameter ranges.

## Dependencies

- [NetSquid](https://netsquid.org) (requires registration)
- NumPy, Matplotlib

## Status and Roadmap

See [ROADMAP.md](ROADMAP.md).

# netsquid-qkd

NetSquid simulations comparing BB84 and MDI-QKD protocols.

UCL MSc Quantum Technologies Research Project — Linus Kelsey

---

## Structure

```
BB84/           BB84 Alice/Bob protocols and simulation runner
MDI/            MDI-QKD Alice/Bob/Charlie protocols and simulation runner
network/        Multi-user network simulation
  topology.py              User placement, k-means relay optimisation, BB84/MDI link distances
  bb84_network.py          BB84 over all N(N-1)/2 direct pairs; per-pair and network-level metrics
  mdi_network.py           MDI-QKD over all pairs via nearest relay; cross-cluster passive routing
  trusted_bb84_network.py  Trusted-node BB84: users connect to K relay nodes; relays XOR-combine keys; cross-relay pairs dilute backbone key rate; rate = min link in chain
  visualise_network.py     Side-by-side MDI cluster / BB84 mesh topology plot
lib/            Shared utilities (delay model, photon source, config loader, DB layer)
  db.py                 SQLite persistence: p2p_results and network_results tables
data/           SQLite database (git-ignored; created on first run)
configs/        JSON parameter presets (layer0_ideal → layer8_bs_eff)
scripts/
  P2P/
    raw/        Single-protocol run scripts
    compare/    Sweep scripts: key rate vs distance, loss, efficiency, dark count rate,
                node loss, source error rate, dephasing rate, detector basis bias,
                beam splitter efficiency, Charlie placement
    layers.py   Effect of each modelling layer per protocol (cumulative)
    isolate.py  Independent impact of each parameter — all-ideal except one
  network/
    relay_sweep.py       Exp 1: fixed N users, vary K relays — key rate + success rate vs K
    user_sweep.py        Exp 2: fixed K relays (optimised at ref-N), vary N users — key rate vs N
    time/
      time_vs_area.py    Wall-clock runtime vs network area at fixed N and K
      time_vs_users.py   Wall-clock runtime vs user count N at fixed K
  analyse/
    db.py       Query layer: count_p2p, query_p2p, query_network, list_distinct
    p2p.py      CLI: reconstruct any P2P sweep figure from results.db
    network.py  CLI: reconstruct any network sweep figure from results.db
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

# Limit worker processes (default: 80% of CPU cores)
python scripts/P2P/compare/length.py --workers 4

# Disable DB writing (all scripts write to data/results.db by default)
python scripts/P2P/compare/length.py --no-db

# Config preset + CLI override (CLI takes precedence)
python scripts/P2P/compare/length.py --config configs/layer3_dark.json --fibre 30
```

## Layer and isolation analysis

```bash
# Cumulative layers (each adds one realistic parameter on top of the last)
python scripts/P2P/layers.py
python scripts/P2P/layers.py --protocol mdi --runtimes 50

# Isolated parameter impact (all-ideal except one parameter at its realistic value)
python scripts/P2P/isolate.py
python scripts/P2P/isolate.py --protocol bb84 --runtimes 100 --workers 8
python scripts/P2P/isolate.py --save docs/figures
```

## Network Simulations

Visualise a network topology (MDI cluster assignment + BB84 direct mesh):

```bash
python network/visualise_network.py --n 20 --k 3 --area 10 --seed 42
python network/visualise_network.py --n 20 --k 3 --save figures/topology.png
```

Run network simulations directly (used by sweep scripts):

```python
from network.topology import place_users, optimise_relays, Topology
from network.bb84_network import run_bb84_network
from network.mdi_network import run_mdi_network
from network.trusted_bb84_network import run_trusted_bb84_network
from lib.functions import load_config

cfg       = load_config("configs/layer3_dark.json")
user_pos  = place_users(N=10, area_km=10, seed=42)
relay_pos = optimise_relays(user_pos, K=3, seed=42)
topo      = Topology(user_pos, relay_pos)

bb84    = run_bb84_network(topo, cfg, runtimes=20)
mdi     = run_mdi_network(topo, cfg, runtimes=20)
trusted = run_trusted_bb84_network(topo, cfg, runtimes=20)

# bb84["avg_key_rate"],    bb84["success_rate"],    bb84["total_fibre_km"]
# mdi["avg_key_rate"],     mdi["success_rate"],     mdi["total_fibre_km"]
# trusted["avg_key_rate"], trusted["success_rate"], trusted["total_fibre_km"]
```

Key network cost outputs:

| Field | BB84 | MDI | Trusted BB84 |
|-------|------|-----|--------------|
| `total_fibre_km` | Σ all N(N-1)/2 pair distances | Σ user-relay + relay-relay links | Σ user-relay + relay-relay links (same as MDI) |
| `n_links` | N(N-1)/2 | N + K(K-1)/2 | N + K(K-1)/2 |
| `switch_loss_db` | — | extra node loss (dB) for cross-cluster pairs (default 1.0) | — (backbone is a direct BB84 link, no optical switch) |

Run Experiment 2 — user count sweep (fixed K relays, vary N):

```bash
python scripts/network/user_sweep.py --k 3 --n-min 4 --n-max 20 --n-step 2 --runtimes 20
python scripts/network/user_sweep.py --k 3 --n-min 4 --n-max 20 --config configs/layer3_dark.json --save figures/user_sweep.png
# --ref-n: N at which relay positions are optimised (default: n-max)
python scripts/network/user_sweep.py --k 3 --n-min 4 --n-max 20 --ref-n 20
# Error style: std error bars (default), ±1σ fill, or Q1/Q3 fill
python scripts/network/user_sweep.py --seeds 10 --error iqr
```

Relay positions are optimised once at `--ref-n` and held fixed across all N values. All three protocols re-run per N. Total fibre printed per row showing O(N²) BB84 vs O(N) MDI/trusted-BB84 scaling.

Run Experiment 1 — relay count sweep (fixed N, vary K):

```bash
python scripts/network/relay_sweep.py --n 20 --k-min 1 --k-max 8 --runtimes 20
python scripts/network/relay_sweep.py --n 20 --k-min 1 --k-max 8 --config configs/layer3_dark.json --save figures/relay_sweep.png

# Error style: std error bars (default), ±1σ fill, or Q1/Q3 fill (robust to outlier seeds)
python scripts/network/relay_sweep.py --error bars
python scripts/network/relay_sweep.py --error shade
python scripts/network/relay_sweep.py --error iqr

# DB control: suppress P2P pair rows, network summary rows, or both
python scripts/network/relay_sweep.py --no-p2p-db
python scripts/network/relay_sweep.py --no-net-db
python scripts/network/relay_sweep.py --no-p2p-db --no-net-db
```

BB84 is run once (relay-independent) and reused across all K values. MDI and trusted-node BB84 both re-run per K with re-optimised relay positions. Produces two figures: key rate vs K (all three protocols), and a topology visualisation at the midpoint K.

See [NETWORK.md](NETWORK.md) for full experimental design and hypotheses.

See [PARAMS.md](PARAMS.md) for config presets, simulation defaults, and realistic hardware parameter ranges.

See [DATA.md](DATA.md) for database schema and example queries.

## Reconstruct figures from DB

```bash
# P2P: reconstruct any sweep from results.db
python scripts/analyse/p2p.py --sweep fibre_len
python scripts/analyse/p2p.py --sweep detector_eff_z --error shade
python scripts/analyse/p2p.py --sweep len_loss --protocols BB84

# Network: reconstruct user or relay sweep
python scripts/analyse/network.py                        # n_users sweep, avg key rate
python scripts/analyse/network.py --x k_relays           # relay count sweep (BB84 flat line)
python scripts/analyse/network.py --y success_rate --area 50
python scripts/analyse/network.py --seed 1638            # single seed + MDI topology figure
```

## Dependencies

- [NetSquid](https://netsquid.org) (requires registration)
- NumPy, Matplotlib, psutil, pandas
- Textual (for `scripts/analyse/tui.py`)
- SQLite3 (stdlib)

Or: `pip install -r requirements.txt` (NetSquid requires separate registration).

## Status and Roadmap

See [ROADMAP.md](ROADMAP.md).

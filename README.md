# netsquid-qkd

NetSquid simulations comparing BB84 and MDI-QKD, point-to-point and at network scale.

UCL MSc Quantum Technologies Research Project — Linus Kelsey

## Layout

```
BB84/, MDI/       Protocol implementations and simulation runners
network/          Multi-user network layer: topology, BB84/MDI/trusted-BB84 network sims, visualisation
lib/              Shared utilities: config loader, DB layer, plotting
configs/          JSON parameter presets (layer0_ideal → layer9_bs_eff)
data/             SQLite results DB (git-ignored, created on first run)
scripts/P2P/      Point-to-point sweeps, layer/isolation analysis, timing benchmarks
scripts/network/  Network-scale sweeps (relay count, user count, relay placement)
scripts/analyse/  Reconstruct any figure from the DB without re-running simulations
docs/             Figures, dissertation source
```

Every script takes `--help` for its full option list; each also carries a usage docstring at the top of the file.

## Setup

```bash
pip install -r requirements.txt   # NetSquid itself requires separate registration at netsquid.org
```

## Quick start

```bash
python scripts/P2P/compare/length.py --output-dir docs/figures        # key rate vs distance, BB84 vs MDI
python scripts/network/user_sweep.py --output-dir docs/figures        # key rate vs user count, network scale
```

## Docs

- [NETWORK.md](NETWORK.md) — network model design and hypotheses
- [PARAMS.md](PARAMS.md) — config presets, defaults, sourced hardware parameter ranges
- [DATA.md](DATA.md) — SQLite schema and example queries
- [ROADMAP.md](ROADMAP.md) — feature status
- [TODO.md](TODO.md) / [DISSERTATION_TODO.md](DISSERTATION_TODO.md) — outstanding work

# netsquid-qkd

NetSquid simulations comparing BB84 and MDI-QKD protocols.

UCL MSc Quantum Technologies Research Project — Linus Kelsey

---

## Structure

```
BB84/           BB84 Alice/Bob protocols and simulation runner
MDI/            MDI-QKD Alice/Bob/Charlie protocols and simulation runner
lib/            Shared utilities (delay model, photon source)
scripts/
  raw/          Single-protocol run scripts
  compare/      Sweep scripts: key rate vs distance, loss, detector efficiency
```

## Running

From the repo root:

```bash
# Single comparison at default parameters
python scripts/compare/length.py    # key rate vs distance
python scripts/compare/loss.py      # key rate vs fibre attenuation
python scripts/compare/efficiency.py  # key rate vs detector efficiency
```

Key parameters (all comparison scripts accept these via `main(...)`):

| Parameter | Default | Description |
|-----------|---------|-------------|
| `fibre` | 100 km | Alice-Bob separation |
| `lenLoss` | 0 dB/km | Fibre attenuation coefficient α |
| `detEff` | 1.0 | Detector efficiency η_d |
| `darkCount` | 0 | Dark counts per second |
| `runtimes` | 10 | Monte Carlo repetitions per data point |
| `photons` | 1024 | Photons per run |

## Dependencies

- [NetSquid](https://netsquid.org) (requires registration)
- NumPy, Matplotlib

## Status and Roadmap

See [ROADMAP.md](ROADMAP.md).

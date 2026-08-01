# MimicNet: Fast Performance Estimates for Data Center Networks with Machine Learning

**Authors:** Qizhen Zhang, Kelvin K.W. Ng, Charles W. Kazer, Shen Yan, João Sedoc, Vincent Liu  
**Institutions:** University of Pennsylvania, Swarthmore College, Peking University, New York University  
**Venue:** ACM SIGCOMM 2021, August 23–27, Virtual Event, USA  
**DOI:** https://doi.org/10.1145/3452296.3472926

---

## One-line summary

Simulate one cluster at full packet-level fidelity; use LSTM models to approximate all others — achieves >2 orders of magnitude speedup with tail FCT, throughput, and RTT within 5% of ground truth.

---

## Core idea

Full packet-level simulation of large data centre networks is intractable (1w 4d for 128 clusters). MimicNet keeps one "observable" cluster running at full fidelity in OMNeT++ and replaces all other clusters with trained "Mimic" models. Mimics learn intra-cluster behaviour (queues, routing, drop/latency) from the small-scale simulation; inter-cluster traffic is approximated by flow-level "feeder" models.

---

## Key results

| Network size | Full sim time | MimicNet time | Speedup |
|---|---|---|---|
| 128 clusters, 1024 hosts | 1w 4d 22h 25m | ~8h 38m total (25m final sim) | ~675× |
| 64 clusters | completes in months | under 1 hour | >100× |

- FCT, throughput, RTT predictions within **5% of ground truth** (W₁ metric)
- MimicNet is **7× faster than flow-level simulation** (SimGrid) at 128 clusters, and more accurate
- Accuracy improves with scale — MimicNet benefits from inter-cluster locality, full sim does not

---

## Architecture

Two model types per Mimic:
1. **Internal models (LSTM):** Learn intra-cluster behaviour — drop probability, latency, ECN marking — from small-scale observations. Scale-independent features only (local rack index, switch traversal count, etc.)
2. **Feeder models (flow-level):** Estimate inter-Mimic traffic arrival rates from cluster size parameter

Training pipeline: small-scale 2-cluster OMNeT++ simulation → feature extraction → LSTM training → Bayesian hyperparameter optimisation → large-scale composition

---

## Key assumptions / restrictions

- **FatTree topology** (recursively defined, strict up-down routing)
- **Traffic patterns scale proportionally** (per-host model independent of cluster count)
- **Fan-in bottleneck** (congestion primarily at fan-in, not elsewhere)
- **Intra-host isolation** (CPU interactions not modelled)

Not suited for arbitrary topologies or protocols — these are explicitly acknowledged.

---

## Quantum analogue relevance

MimicNet is the classical precedent for the surrogate modelling direction in quantum network simulation:

| Classical (MimicNet) | Quantum analogue |
|---|---|
| Simulate one observable cluster | Simulate ≤30-node regime at full fidelity |
| LSTM/flow approximates the rest | GP/GNN extrapolates secret key rate / fidelity |
| FatTree topology constraint | Protocol/topology class constraint |
| ~675× speedup | ~10⁶× speedup demonstrated |

The premise transfers exactly: simulate what is tractable, learn what is not.

---

## Citation

Zhang, Q., Ng, K.K.W., Kazer, C.W., Yan, S., Sedoc, J. and Liu, V. (2021) 'MimicNet: Fast Performance Estimates for Data Center Networks with Machine Learning', *Proceedings of ACM SIGCOMM 2021*, pp. 287–304. doi: 10.1145/3452296.3472926.

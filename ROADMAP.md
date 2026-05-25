# ROADMAP

Parametric NetSquid simulation comparing BB84 and MDI-QKD across key rate, implementation cost, and scalability. Physical realism added one layer at a time to keep comparisons fair.

---

## Modelling Layers (Point-to-Point)

| Layer | Description | Status |
|-------|-------------|--------|
| 1 | Fibre loss: Beer-Lambert `T = 10^(-αL/10)` | **complete** |
| 2 | Detector efficiency: `η_d ∈ [0.5, 1.0]` | **complete** |
| 3 | Dark counts: scale `d_c` with detection rate | **next** |
| 4 | Node / connector loss | planned |
| 5 | Source bit errors | planned |
| 6 | Detector basis bias | planned |
| 7 | Fibre dephasing | planned |

> Error correction and privacy amplification are excluded — both protocols use identical methods, so omitting them preserves fairness at the physical layer.

---

## Simulation Stages

1. **Finalise BB84 in NetSquid** — complete
2. **Validate against literature** rate-distance curves — scale verified; absolute validation remaining
3. **MDI-QKD implementation** — complete; validation remaining
4. **Sweep distances, topologies, and scale** — prototyped
5. **Comparative analysis** across metrics — prototyped

---

## Results So Far (April 2026)

- **Key rate vs fibre attenuation** (50 km, η_d = 0.9): both linear on log scale; MDI offset below BB84 by constant factor across all α; at α = 0.2 dB/km → BB84 ≈ 70 kbps, MDI ≈ 25 kbps
- **Key rate vs distance** (α = 0.2 dB/km, η_d = 0.9): MDI decays faster; gap widens beyond ~30 km; at 100 km → BB84 ≈ 4 kbps, MDI ≈ 2 kbps; no crossover observed in 1–100 km range
- **Key rate vs detector efficiency** (50 km, α = 0.2 dB/km): BB84 degrades ~linearly (−50% over η_d = 1→0.5); MDI degrades quadratically (−90% same range) due to coincident detection at two detectors — SNSPDs (η_d ≈ 0.90–0.95) are not optional for MDI

**Why MDI is slower:** (1) 50% BSM efficiency cap from linear-optic HOM setup; (2) η_d² dependence at Charlie's two detectors.

---

## Open Questions / Analysis Priorities

- Sensitivity analysis on `d_c / η` ratio (dark count model)
- QBER threshold crossings (> 11%) as function of distance, loss, η_d — for trusted node analysis
- Effect of Charlie's position on performance (asymmetric links)
- Effect of BB84 repeaters on comparison
- Practical key rate thresholds for operational viability

---

## Timeline

| Period | Focus |
|--------|-------|
| Exams → 28 May | — |
| June I | Validation benchmarking (BB84 + MDI); complete P2P modelling layers (dark counts → node loss → beyond) |
| June II | Network-scale extension; trusted node BB84 vs MDI comparison |
| July | Bug-catching, parameter sweeps, result collection |
| August | Write-up, final figures, submission |
| September | Viva |

---

## Metrics for Final Comparison

1. Key rate vs distance (varying topologies)
2. Implementation cost — economic and energetic (ILP framework, cf. Karavias et al. 2025)
3. Scalability — marginal key rate and cost per added user

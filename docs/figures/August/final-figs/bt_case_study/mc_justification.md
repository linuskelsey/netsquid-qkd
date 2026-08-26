# Monte Carlo runtimes justification (key_rate / efficiency)

**Update**: `--runtimes` default is now 1000 (was 250), matching `sec:results_p2p`'s
r=1000 exactly. Since it's the same r value the dissertation already justifies for
the P2P sweeps, this appendix likely doesn't need its own fresh justification
paragraph — probably just a one-line pointer back to that existing SEM/CV argument
rather than restating it. Leaving the r=250 analysis below for reference (in case
a smaller ad-hoc run is ever used again), but it's no longer the operative case.

Matches the SEM/CV framing already used elsewhere in the dissertation:

- P2P sweeps (`sec:results_p2p`): r=1000, worst-case CV≈30% (MDI), SEM=CV/√r≈1%,
  checked against the smallest quantified effect (5.1%).
- Network sweeps (`sec:network_analysis`): S seeds × r=200/seed, justified because
  between-seed CV (~21%, Table `tab:relay_sweep_n15_seeds`) dominates per-pair SEM
  (~2%) by an order of magnitude — error bars stay seed-limited, not trial-limited.

This appendix is neither of those: it explicitly does **not** average over drawn
topologies (S=1, one fixed real BT topology, per spec.md). With no between-seed
variance to dominate and absorb Monte Carlo noise, trial-level SEM is the only
source of uncertainty in the reported key rates — closer to the P2P sweep's
framing than the network sweep's.

**Justification for r=250 (previous default, kept for reference only):**

Using the worst-case CV≈30% observed for MDI in the point-to-point sweep
(`sec:results_p2p`) as a conservative benchmark (borrowed from its 20km reference
point — see caveat below):

    SEM = CV / sqrt(r) = 30% / sqrt(250) ≈ 1.9%

Comfortably below the smallest effect sizes this case study reports (protocol
key-rate gaps and cost differentials of tens of percent).

**Caveat — not yet empirically checked.** The 30% CV is borrowed from the
synthetic P2P sweep's 20km reference point. BT's real link distances (Slough is
~31-34km from West End/City of London; the two central sites are ~3.4km apart)
differ from that reference and could shift the true CV in either direction once
the real `key_rate` sweep actually runs. Before citing 1.9% in the dissertation
text, spot-check the actual std/mean per N from the real run (`ok_rate`'s
sibling — per-pair rate std is not currently captured in `bt_case_study.py`'s
output; would need adding if we want the real number rather than the borrowed
benchmark).

# Case Study Notes

## Paddy Hogan (UCL Spintronics Group) — intro conversation

**Research goals in the area:**
- Improve T2 coherence times
- Improve ensemble density
- Improve retrieval efficiency

**Key motivating question:** Can quantum memories work at microwave frequencies to reduce QPU requirements?

**The QPU analogy (RAM ↔ quantum memory):**
- Gidney & Ekerå 2021 (Quantum 5, 433): breaking 2048-RSA requires ~20 million noisy qubits
  - Paddy quoted "1 million" — the correct figure is 20 million
- Gouzien & Sangouard 2021 (PRL 127, 140503): same task requires only **13,436 qubits** with a multimode quantum memory (177 days runtime)
  - This is the "13k" paper — cite this one
- ~3 orders of magnitude reduction
- Analogy: just as RAM reduces CPU load by storing long-term reused data, a quantum memory offloads qubit requirements from the processor

**Target implementation:** Solid-state spin ensembles
- Derive from a rich history of electron spin resonance (ESR) research
- Bismuth donors give high T2 ≈ 1 s

**Physical mechanism (Paddy's description):**
- Superconducting circuits are patterned on chip
- Subjected to highly localised magnetic fields → drives electron spin transitions at microwave frequencies
- Resonant circuits designed to match the transition frequency of the spin being driven

**Biggest challenge:** Efficiency
- Both read and write phases lose significant amounts of information
- Cooperativity C ~ 1 is the target; current experiments are well below this (e.g. C ~ 0.06 in O'Sullivan 2022)

## Three centrepiece papers (survey anchors)

1. **Wolfowicz 2013 (NatNano)** — coherence layer. Clock transitions in Bi:Si → T2 = 2.7 s. Foundational; every Bi:Si memory paper is downstream of this.
2. **Ranjan 2020 (PRL 125, 210505)** — quantum-regime layer. First multimode storage at sub-photon level; 20 modes, T2E > 100 ms; Bi:Si at clock transition. Proves the platform works as a quantum memory; bridges Wolfowicz → O'Sullivan.
3. **O'Sullivan 2022 (PRX 12, 041014)** — protocol layer. WURST chirped pulses; 16 modes; random-access retrieval; 2 ms storage. First functional buffer memory; qualitatively new capability over echo protocols.

Supporting roles: Kubo 2011 (historical first hybrid, NV limitations → intro only), Hogan 2026 (C = 1 achieved, losses identified → outlook), Bienfait 2016 (cooperativity formalism + Purcell infrastructure → sidebar), Greggio 2026 (efficiency bounds theory → outlook).

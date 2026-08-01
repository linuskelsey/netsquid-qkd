# Slide Questions — Answers

---

## Slide 1: Gouzien & Sangouard line check

The three bullets claim G&S's result _requires_:
1. Memory offloads intermediate states, amortises qubit overhead across time
2. Memory must operate at **microwave frequencies (1–10 GHz) without conversion loss**
3. Storage time ~1 s multimode

**Items 1 and 3 are solidly attributable to G&S (2021).** The paper is "Factoring 2048-bit RSA Integers in 177 Days with 13,436 Qubits and a Multimode Memory" — the whole point is that multimode storage compresses the logical qubit count by reusing physical qubits over time (item 1), and they compute the required storage time ~1 s from the algorithm runtime (item 3).

**Item 2 is an inference, not a G&S statement.** G&S's paper is platform-agnostic — they specify the memory's _logical_ requirements (multimode, ~1 s, high fidelity) but say nothing about microwave frequencies. The microwave frequency constraint comes from coupling to superconducting qubits, which is the architectural choice the rest of the talk motivates separately. Attributing it to G&S is technically a stretch.

**Suggested fix:** either (a) make item 2 a separate line not under "G&S's result requires", e.g. "Integration with SC qubits demands microwave-frequency operation", or (b) drop it from the bulleted list and add it as a separate sentence: "Superconducting implementation then forces microwave operation without transduction loss."

---

## Slide 2: What are κ and γ?

Cooperativity: $C = g_\mathrm{eff}^2 / (\kappa \gamma)$

- **κ (kappa)** = cavity photon decay rate — how fast microwave photons leak out of the resonator. Determined by resonator quality factor Q: $\kappa = \omega_r / Q$. Units: rad/s.
- **γ (gamma)** = individual spin linewidth / homogeneous dephasing rate = $1/T_2$ per spin. How fast a single spin loses coherence due to its local environment. Units: rad/s.
- **g_eff** = collective coupling: $g_\mathrm{eff} = g_0\sqrt{N}$, where $g_0$ is the single-spin coupling and $N$ is the spin number.

Physically: $C > 1$ means the spin-photon coupling is faster than both cavity loss and spin dephasing — the system is in the strong coupling regime and can efficiently swap states.

---

## Slide 2: Things not yet defined in the table

The table on slide 2 lists four platforms, including Yb:YSO with "C=1 achieved (Hogan, 2026)". Cooperativity has just been defined on the same slide, so C=1 is fine. The problem is:

- The platforms (NV/diamond, Yb:YSO, Er:CaWO₄) are listed without context for why they're interesting — the audience doesn't know what distinguishes them yet.
- Yb:YSO appears with a result that only makes sense after the cooperativity bottleneck (slides 7–8).

**Take:** the table works fine as a _roadmap_ — it signals "these are the players, you'll meet them properly later." But the Yb:YSO row is premature because "C=1 achieved" is the punchline of slides 7–8, and putting it here deflates the payoff. Options:
1. Simplify the Yb:YSO "key property" to "ZEFOZ clock transition native to SC qubit band" (no result yet).
2. Drop C=1 from the table and only report it when the cooperativity story is told.

---

## Slide 3: T₂* vs T₂

Yes, your reading is correct:

- **T₂*** = inhomogeneous dephasing time. Different spins in the ensemble sit at slightly different positions/field environments, so they precess at slightly different frequencies. They start in phase but gradually fan out (dephase) — the ensemble's collective coherence decays on this timescale. Typical: µs to low ms range.
- **T₂** = homogeneous (spin-echo) coherence time. The "true" intrinsic coherence of an individual spin, independent of its neighbours. Measured by removing the inhomogeneous contribution with a spin-echo pulse. Much longer: up to seconds at clock transitions.

Always $T_2^* \ll T_2$ for a real ensemble.

---

## Slide 3: "Lost before retrieval" and "refocusing"

**Lost before retrieval:** when a superposition state is stored in the ensemble, each spin starts precessing at its own frequency. After time $T_2^*$, the individual spin phases have spread so widely that they cancel: the collective Bloch vector is zero. The stored quantum state is no longer readable — if you try to retrieve it at $t \gg T_2^*$, nothing comes out. The information isn't gone from the spins individually, but the phase coherence that allows collective emission has been lost.

**Refocusing (spin echo):** apply a π pulse at time τ. This flips all spins (swaps |↑⟩ ↔ |↓⟩), reversing the sign of each spin's accumulated phase. Spins that were ahead are now behind. They re-converge at time 2τ — the ensemble is collectively back in phase, producing a "spin echo" burst of emission. This is refocusing. The Hahn echo is the simplest version (single π pulse). The problem is: to retrieve you must time the π pulse precisely and retrieve at exactly 2τ — you have no choice of when to read out (FILO).

---

## Slide 3: Replace table with diagram

The table conveys: (1) T₂ is seconds at a clock transition, (2) natural Si is fine (no isotopic enrichment needed), (3) tunable resonators matched to clock freq exist. These are three different kinds of facts. The table is fine for a written report but dense for a slide.

**Suggested diagram:** a two-panel figure.

**Left panel — dephasing/refocusing cartoon:**
Three or four arrows on a Bloch-sphere equatorial view. Initially all pointing the same direction (stored state). After time T₂*: arrows have fanned out (phase spread), no net vector = state lost. After π pulse at τ: arrows fan in the opposite direction. At 2τ: arrows reconverge = echo = retrieval. Label the three time points.

**Right panel — T₂* vs T₂ on a log scale:**
A single horizontal bar chart or axis showing:
- T₂* ~ µs to ms (inhomogeneous, no echo)
- T₂ (natural Si) ~ 93 ms (Hahn echo)
- T₂ at clock transition (²⁸Si:Bi) ~ 2.7 s

This makes the dramatic improvement visual (three to four orders of magnitude from T₂* to clock T₂). You can lose the Wen et al. tunable resonator row — it's a detail that belongs in footnotes, not the slide's main point.

---

## Slide 4: Too wordy — what to cut and what diagram

**Text that can go:**
- "Canonical chip architecture: superconducting qubit ↔ microwave bus ↔ spin ensemble; state transfer swaps qubit excitation into collective spin mode" — this is purely descriptive and replaced entirely by a diagram.
- "Population inversion ⇒ amplified spontaneous emission limits retrieval fidelity" — accurate but jargon-heavy for a slide. Condense to: "Population inversion → amplified spontaneous emission noise."

**What the diagram replaces:**
Draw the chip architecture schematic:
```
[SC qubit] --swap-- [microwave bus/cavity] --swap-- [spin ensemble]
     (transmon)        (coplanar waveguide)        (Si:Bi or NV crystal)
```
Below it, a simple timeline showing the Hahn echo FILO constraint: write A → write B → π → echo B then echo A (i.e., reversed order). Label it "FILO: cannot retrieve A before B." This makes the limitation intuitive without words.

Then the two milestones (Kubo 2011, Ranjan 2020) stay as bullets but without the architecture prose above them.

---

## How WURST random access works (full explanation)

WURST = Wideband Uniform Rate Smooth Truncation — a chirped microwave pulse whose frequency sweeps linearly across the inhomogeneous linewidth of the ensemble. A pair of WURST π-pulses defines a "write" or "read" operation for one mode.

**The key quantity:** the chirp rate $\dot{\nu}$ means each spin is driven at peak amplitude at a different time. The accumulated phase a spin acquires during the WURST pair depends on where in the ensemble it sits (i.e., its resonance frequency offset). This creates a unique phase map $\phi_W(\delta)$ across the ensemble, where δ is the spin's frequency detuning.

**Write mode A:**
1. First π_A pulse arrives: the pulse is a chirped π rotation sweeping across the ensemble.
2. Photon A arrives and is absorbed — the ensemble stores it as a collective spin excitation.
3. Second π_A pulse: another chirped π, matched to the first. This completes the write. Alone, a single Hahn π pulse would cause a spin echo at a predictable time (the FILO problem). The second WURST π_A instead adds a specific additional phase $+\phi_A$ to the ensemble. The echo condition ($k_\delta = 0$) is no longer met at the natural echo time — the echo is _suppressed_. The state sits stored, phase-labelled with $\phi_A$.

**Write mode B (while A is stored):**
Same process with a different chirp rate or timing: ($\pi_B$, input B, $\pi_B$). This imprints $\phi_B \neq \phi_A$. Modes A and B coexist in the ensemble with different phase labels. They don't interfere because they live in different frequency channels within the inhomogeneous linewidth.

**Read mode A selectively:**
Apply a read pair matched to A: (read $\pi_A$, ..., read $\pi_A$). This cancels $\phi_A$: the total accumulated phase for mode-A spins becomes zero ($k_\delta = 0$), satisfying the echo condition → mode A is emitted. Mode B still carries $\phi_B \neq 0$ → its echo condition is not met → it stays stored.

**Why no population inversion noise:** A Hahn π pulse inverts the spin population (puts spins in the excited state), which causes amplified spontaneous emission (ASE) noise as they decay. WURST pairs are refocusing pulses but are applied in pairs that net-cancel the inversion — spins end back in the ground state between writes. No population inversion → no ASE.

**Built-in dynamical decoupling:** each WURST pair is effectively a π refocusing pulse for low-frequency noise. While modes sit in storage, periodic WURST pairs can be applied to extend T₂ — the same pulses used for write/read also decouple the spins from noise.

**What $k_\delta$ is:** it's the accumulated chirp phase coordinate — effectively how much extra phase each spin has acquired due to its frequency offset and the chirp rate. $k_\delta = 0$ is the echo condition (all spins in phase → collective emission). The diagrams show $k_\delta$ ramping up and down as WURST pairs are applied; when the pair assigned to mode A is applied during readout, $k_\delta$ hits zero for mode A spins at the readout time.

---

## Slide 7: Where do the routes to unit C come from?

The three routes (planar microresonators, isotopic enrichment, hyperpolarisation) come directly from the structure of $C = g_\mathrm{eff}^2 / (\kappa \gamma)$. Each route addresses a different factor:

| Route | Which factor | Mechanism |
|---|---|---|
| Planar lumped-element microresonators | ↑ $g_\mathrm{eff}$ | Smaller mode volume concentrates $B_1$ field → larger $g_0$ per spin → larger $g_\mathrm{eff} = g_0\sqrt{N}$ |
| Isotopic enrichment (remove ²⁹Si) | ↓ γ | ²⁹Si nuclei create fluctuating local magnetic fields (hyperfine noise). Replacing with spin-zero ²⁸Si narrows individual spin linewidth → smaller γ |
| Nuclear spin hyperpolarisation | ↑ effective N | Spins distributed across many hyperfine sublevels at equilibrium; only spins on the _target_ ESR transition couple to the cavity. Hyperpolarisation pumps all spins to one nuclear spin state → all contribute to $g_\mathrm{eff}$ |

These aren't ad hoc — they exhaust the engineering knobs on C. The slide could benefit from this table rather than three plain bullets, since it makes clear each fix targets a different variable.

---

## Hyperpolarisation (not defined)

**Definition for the slide:** Si:Bi has nuclear spin I = 9/2 (for Bi), giving 20 hyperfine sublevels (2I+1 nuclear × 2 electron = 20 ESR transitions). At thermal equilibrium, spins populate all these levels roughly equally. The microwave cavity only resonates with _one_ ESR transition — so roughly 1/20 of spins are useful and the rest are spectators that don't contribute to $g_\mathrm{eff}$.

Hyperpolarisation uses a combination of optical pumping or microwave saturation sequences (similar to DNP — dynamic nuclear polarisation) to drive all the nuclear spin population into a single $m_I$ state. Now all $N$ spins sit on the target ESR transition and all contribute. This is a prerequisite for reaching C = 1 in Si:Bi.

**One-line definition to add to slide 7:** "Hyperpolarisation: pump all spins to a single nuclear spin state so that every spin contributes to $g_\mathrm{eff}$."

---

## Slide 8: Si:Bi fundamental limit in digestible terms

Current slide text: "only donors in the targeted hyperfine level contribute to $g_\mathrm{eff}$; hyperpolarisation required to reach C=1."

**Digestible version:**
"Si:Bi spins at equilibrium are spread across ~20 hyperfine sublevels. The cavity only talks to one of them — so at most 1/20 of spins are contributing. No matter how good the resonator, C is capped until hyperpolarisation concentrates all spins on that one level."

Or as a slide bullet: "At equilibrium: ~1/20 spins on target level → C capped. Hyperpolarisation is not an optimisation — it's a prerequisite."

---

## Slide 9: Three routes reappearing — more detail or remove focus?

The three routes (planar resonators, isotopic enrichment, hyperpolarisation) get slide 7 as their stage. They are presented as bullet points without mechanism. Then on slide 9 "planar microresonator engineering" reappears in the path-forward sentence, but isotopic enrichment and hyperpolarisation don't — so the set of three is no longer coherent in slide 9 either.

**Problem:** three bullet points in slide 7 feel like a complete taxonomy but none gets enough explanation to be convincing. Reusing "planar microresonator engineering" in slide 9 without the other two looks inconsistent.

**Options:**

1. **Expand slide 7:** Give each route a one-sentence mechanism (using the table above). This justifies their prominence and makes the slide 9 callback to planar resonators feel motivated (it's the one that Yb:YSO used to hit C=1).

2. **Collapse slide 7:** Drop the three bullets to one line — "Three engineering routes: smaller resonator mode volume, reduced ²⁹Si bath, nuclear hyperpolarisation (O'Sullivan et al.)" — and move the focus to the result (C ≈ 0.06, 3% efficiency) and what's needed (C = 1). This removes the false prominence without losing the information.

3. **Reframe:** Turn slide 7 into "C ≈ 0.06 → 3% efficiency" with a single plot or diagram, and relegate the three routes to a footnote or appendix slide. Then slide 9 can say "planar NbN microresonators addressed the mode-volume route" without the audience expecting to hear about isotopic enrichment and hyperpolarisation again.

**Recommendation:** Option 1 if you have time in the talk, option 2 if the slide is already at capacity. Option 3 is the cleanest but requires layout work.

---

## Slide 10: How can Er:CaWO₄ couple to both microwave and photonic resonators simultaneously?

It is **not** a broadband frequency response. Er³⁺ has two completely separate physical transitions on the same ion:

1. **Optical (4f–4f) transition** at ~1535 nm (telecom C-band): the erbium 4f electron shell has a parity-forbidden but magnetic-dipole allowed transition ⁴I₁₅/₂ → ⁴I₁₃/₂. This couples to a photonic resonator (optical cavity or photonic crystal waveguide).

2. **Electron spin transition** (Zeeman splitting) in the ⁴I₁₅/₂ ground state: Er³⁺ has S = 1/2 and in an applied magnetic field of ~0.1–0.3 T, the spin splitting falls in the 5–10 GHz range — the superconducting qubit band. This couples to a microwave resonator.

These are different physical degrees of freedom of the same ion. Coupling both simultaneously is possible because you can put the ion in a device where:
- A microwave co-planar waveguide resonator is patterned on-chip around the crystal
- The crystal is also inside or adjacent to an optical resonator (e.g., a fibre taper, photonic crystal, or evanescent coupler)

The two resonators operate at totally different length scales (microwave λ ~ cm, optical λ ~ 1.5 µm) and don't interfere with each other. The Er³⁺ ion sits at the overlap of both field modes.

**Why this matters:** the ion can absorb a microwave photon (spin flip in ground state) and the resulting spin state modifies the optical transition frequency (spin-orbit coupling in the 4f shell). This is the transduction mechanism: microwave excitation → spin state change → altered optical emission → optical photon. It enables microwave-to-optical frequency conversion at 1535 nm — exactly the telecom C-band, compatible with standard fibre.

The CaWO₄ host is chosen because it has very low nuclear spin density (natural-abundance CaWO₄ has mostly spin-zero nuclei) → long Er³⁺ spin coherence (23 ms at mK, Dantec et al. 2021).

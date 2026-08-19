# Dissertation TODO
> Generated 2026-08-03 from audit of `dissertation.tex`, `ROADMAP.md`, `TODO.md`, and `cost rethink/cost_analysis.tex`.
> Updated 2026-08-11: full re-audit against current `dissertation.tex` (§4 Results, §5 Discussion, §6 Conclusion now substantially complete — relay-sweep figure+table+prose for N=15 added, sensitivity/isolate/layers figures finalised, §6.2 Findings and §5.4 Implications for Protocol Selection rewritten with real numbers). All completed and moot items removed from this file — only remaining open work is listed below.
> Updated 2026-08-18: re-audit against current `dissertation.tex`/`bibliography.bib`. Core simulation work now done — $\eta_d=0.1$ point integrated, `user_sweep.py` rerun and written up (§4.3, Figure~\ref{fig:user_sweep}), `relay_placement.py` exp1+exp2 written up (Appendix "Relay Placement Optimisation"), timing scripts written up (Appendix~\ref{sec:appendix_netsquid}, Table~\ref{tab:timing}). Case study is now merged directly into `dissertation.tex` (no separate `case-study.tex` file). Remaining open items are almost entirely nice-to-have extensions/polish, not blocking content.
> Organised by category. Items marked **[BLOCKING]** must be done before submission.

---

## 1. Simulations to Run (data collection)

- [x] **SPAD-BB84 vs SNSPD-MDI relay sweep comparison** — **done 2026-08-13**. Both panels of Figure~\ref{fig:relay_sweep} now show BB84-SNSPD/BB84-SPAD/MDI: N=10 SPAD mean 126.3~kbps (±1σ 112.8–139.8), N=15 SPAD mean 136.5~kbps (±1σ 119.6–153.3). Caption updated with both baselines; new discussion paragraph added after the N=10 prose confirming, with real data, that SPAD-BB84 sits ~1.9–2.0× above the SNSPD-MDI peak with no overlap between the two distributions at either N — matches the 2026-08-12 back-of-envelope estimate almost exactly. Flags that any cost-per-bit comparison (Section~\ref{sec:results_cost}) must be read at unequal key rates.

- [x] **Add $\eta_d=0.1$ point to detector efficiency sweep** — **done**. `figures/p2p_sweeps/efficiency.tex` axis data confirmed extending to 0.1 on both BB84/MDI `\addplot` tables and the shading `\path` blocks.

- [x] **`user_sweep.py`** — **done**. Rerun with a shared user layout across $K$ values (commit `d834930`), multi-K comparison + BB84 detector variants added (commit `1dea9e9`), written up as Figure~\ref{fig:user_sweep} and prose in §4.3/§Discussion (commit `bbc949b`): MDI mean rate falls ~27% as $N$ grows 8→20 (fixed relay infra), BB84 under 8%.

- [x] **`relay_placement.py`** (exp 1 + exp 2, provider-growth model) — **done**. Written up in Appendix "Relay Placement Optimisation": Experiment 1 ($K=1$, centroid vs Weiszfeld) and Experiment 2 ($K=2$, centroid/boundary/Weiszfeld) under the fixed-membership provider-growth model, with a full "Open questions" discussion section (backbone topology, assignment optimality, convergence cost, degenerate coincidence, which topologies favour Weiszfeld).

~~Per-seed N=10 relay-sweep table~~ — **dropped 2026-08-12**: decided against: too large, too much information for the payoff; the existing N=15 per-seed table (Table~\ref{tab:relay_sweep_n15_seeds}) is illustrative enough on its own.

---

## 1b. Extensions (nice-to-have, appendix-suitable — not essential)

- [x] **Timing scripts**: `time_vs_area.py`, `time_vs_users.py`, `adaptive_mc.py`, `surrogate.py`, `trend_analysis.py` — **done**. Written up in Appendix~\ref{sec:appendix_netsquid}: Table~\ref{tab:timing} wall-clock costs, adaptive MC (30% BB84 speedup, negligible for MDI) and GP surrogate modelling (<100ms for $10^4$ points) both reported as mitigations attempted.
- [x] **Literature validation on `layers.py`** — **resolved 2026-08-18**: superseded by the PLOB theoretical bound already overlaid on Figures~\ref{fig:p2p_length} and \ref{fig:p2p_node_loss} (published scatter points not needed, per user decision).
- [ ] **MC run count audit**: for rates of order 10⁻ˣ target 10^(x+1) samples per point; audit all scripts and increase where under-sampled. *(Run counts are stated throughout the dissertation — e.g. 1000 runs/point for P2P sweeps, 250 runtimes/pair for the relay sweep — but nobody has audited whether those counts are actually adequate at the lowest observed rates.)* Still open.
- [ ] **MDI network-scale key rate gap — targeted ablation**: the mechanism is now explained analytically (BSM $\eta_\text{arm}^2$ scaling, §Security–Rate Trade-off) and the relay-routing-detour contribution is now quantified empirically (Table~\ref{tab:relay_sweep_n15_seeds}: only 9.4→11.3% of the BB84 rate recovered by increasing $K$). Not yet done: a dedicated ablation run isolating the BSM $\eta^2$ dependency and switch insertion loss individually (disable each in turn) to fully decompose the gap, as originally scoped. Still open.

---

## 2. Model Parameters — Verification

- [x] **Confirm sweep ranges** used in compare figures match realistic literature ranges — **confirmed done**: shaded bands are backed by real citations throughout (IDQ ID281/ID230 device specs for detector efficiency, Duplinskiy for node loss, metropolitan/long-range regime bands), per user confirmation.

---

## 3. Referencing

- [x] Citation for EOM insertion loss range — **moot**: the model no longer uses a separate EOM parameter; Layer~5 lumps EOM/PBS/HOM node loss into one $L_n = 2.0$~dB figure cited to Duplinskiy \textit{et al.} (line 233). The protocol-specific component breakdown this item wanted is explicitly flagged as a limitation instead (§Simulation Model Limitations, "Receiver node loss" paragraph).
- [x] `\cite{PNS_desc}` — **done 2026-08-18**: swapped to `\cite{Brassard_2000}` ("Limitations on Practical Quantum Cryptography", Brassard/Lütkenhaus/Mor/Sanders, PRL 2000) — the actual paper establishing the PNS vulnerability from Poisson-distributed WCP sources, matching the claim it supports (line 113). Chen2022 was considered but rejected: it's about detecting PNS in decoy-state MDI, not the general definition being cited. Dead `PNS_desc` `@misc` entry removed from `bibliography.bib`.
- [ ] Check all `author = {... and others}` entries (32 found in `bibliography.bib`) — some journals require full author lists; verify if UCL submission requires it. Still open.

---

## 4. Assumptions & Justifications Required

- [x] **Multi-seeding (seed count justification)** — **done 2026-08-18**: prior wording overclaimed a formal convergence check that was never actually done. Corrected to state the real reasoning: fixed sampling budget (≥1000 MC samples per data point overall, ≥200 per seed).
- [ ] **TBB84 backbone: 1 source per relay (not K−1)** / **unidirectional backbone links** (cost_analysis.tex §9.6 / Inconsistency VII) — **likely moot for the main dissertation**: TBB84 is no longer part of the core symbolic cost model (Section~\ref{sec:results_cost}); it only appears in the appendix BT London case study, which uses the older standalone `network/cost.py` numeric model, not the backbone-source-counting logic these items refer to. Worth a quick check that `cost.py`'s TBB84 backbone assumption doesn't need the same caveat added to the case-study appendix text, but not a dissertation-body blocker.

---

## 5. Miscellaneous

- [x] **Word/page count vs UCL limit** — confirmed fine, per user (2026-08-18).
- [ ] **Figure captions**: all figures need captions that are self-contained (readable without surrounding text). Not audited yet.
- [ ] **Figure references**: every figure must be referenced in the text with `Figure~\ref{fig:...}`; check none are orphaned. Not audited yet.
- [x] **Spell check** — **done 2026-08-18**: ran hunspell (en_US, manually filtered for British spellings/technical terms/proper nouns) across the full detex'd document. No genuine typos found.
- [x] **Compile clean** — confirmed by user (2026-08-18), post abstract/citation edits.
- [x] **Case study**: **resolved** — no separate `case-study.tex` exists; the case study is `\section{Real-Topology Case Study: The BT London Network}` (`\label{sec:appendix_bt}`) directly inside `dissertation.tex`, so it's automatically in scope for every other check on this list.

---

## 6. Flagged for your attention

- [x] **Abstract's "up to 10 times" claim** — **done 2026-08-18**: reworded to "a drop in key rate, of 5 to 25 times depending on the dominant hardware impairment," matching §Security–Rate Trade-off's real numbers (5$\times$ channel-limited, 25$\times$ detector-efficiency-limited).

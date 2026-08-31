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
- [x] **MC run count audit** — **confirmed done, per user (2026-08-27)**.
- [x] **MDI network-scale key rate gap — targeted ablation** — **dropped 2026-08-27, per user**: satisfied with the existing analytical explanation (BSM $\eta_\text{arm}^2$ scaling, §Security–Rate Trade-off) plus the empirically quantified relay-routing-detour contribution (Table~\ref{tab:relay_sweep_n15_seeds}: only 9.4→11.3% of the BB84 rate recovered by increasing $K$); the dedicated ablation run isolating BSM $\eta^2$ vs switch insertion loss individually is not needed.

---

## 2. Model Parameters — Verification

- [x] **Confirm sweep ranges** used in compare figures match realistic literature ranges — **confirmed done**: shaded bands are backed by real citations throughout (IDQ ID281/ID230 device specs for detector efficiency, Duplinskiy for node loss, metropolitan/long-range regime bands), per user confirmation.

---

## 3. Referencing

- [x] Citation for EOM insertion loss range — **moot**: the model no longer uses a separate EOM parameter; Layer~5 lumps EOM/PBS/HOM node loss into one $L_n = 2.0$~dB figure cited to Duplinskiy \textit{et al.} (line 233). The protocol-specific component breakdown this item wanted is explicitly flagged as a limitation instead (§Simulation Model Limitations, "Receiver node loss" paragraph).
- [x] `\cite{PNS_desc}` — **done 2026-08-18**: swapped to `\cite{Brassard_2000}` ("Limitations on Practical Quantum Cryptography", Brassard/Lütkenhaus/Mor/Sanders, PRL 2000) — the actual paper establishing the PNS vulnerability from Poisson-distributed WCP sources, matching the claim it supports (line 113). Chen2022 was considered but rejected: it's about detecting PNS in decoy-state MDI, not the general definition being cited. Dead `PNS_desc` `@misc` entry removed from `bibliography.bib`.
- [x] Check all `author = {... and others}` entries (32 found in `bibliography.bib`) — **confirmed fine, per user (2026-08-27)**.

---

## 4. Assumptions & Justifications Required

- [x] **Multi-seeding (seed count justification)** — **done 2026-08-18**: prior wording overclaimed a formal convergence check that was never actually done. Corrected to state the real reasoning: fixed sampling budget (≥1000 MC samples per data point overall, ≥200 per seed).
- [x] **TBB84 backbone: 1 source per relay** (cost_analysis.tex §9.6) — **resolved 2026-08-27, per user**: not an approximation error. Each relay routes its single source to every neighbour via a switch, so 1 source/relay ($n_\text{sources} = N+K$ in `network/trusted_bb84_network.py:220`) is a legitimate architecture choice, not an undercount of the $K(K-1)$ figure cost_analysis.tex assumed was required. No caveat needed.

---

## 5. Miscellaneous

- [x] **Word/page count vs UCL limit** — confirmed fine, per user (2026-08-18).
- [x] **Figure captions** — **confirmed done, per user (2026-08-27)**.
- [x] **Figure references** — **fixed 2026-08-27**: added `Figure~\ref{fig:topology_bb84}` to the "BB84 mesh" paragraph (§network_analysis), mirroring the existing `fig:topology_mdi` cite in the "MDI network" paragraph right after it. Re-audited: no orphans left except the parent `fig:topology_example` composite label, which is fine unreferenced now that both its subfigures are individually cited — same pattern already accepted for `fig:isolate`/`fig:layers` and their subfigures. No broken `\ref`s anywhere.
- [x] **Spell check** — **done 2026-08-18**: ran hunspell (en_US, manually filtered for British spellings/technical terms/proper nouns) across the full detex'd document. No genuine typos found.
- [x] **Compile clean** — confirmed by user (2026-08-18), post abstract/citation edits.
- [x] **Case study**: **resolved** — no separate `case-study.tex` exists; the case study is `\section{Real-Topology Case Study: The BT London Network}` (`\label{sec:appendix_bt}`) directly inside `dissertation.tex`, so it's automatically in scope for every other check on this list.
- [ ] **Review Appendices B-E**: B = Relay Placement Optimisation, C = Real-World Deployment Considerations (BT case study), D = NetSquid: Limitations and Speedup Strategies, E = Code and Reproducibility. (Appendix A, Additional Point-to-Point Parameter Sweeps, already gone over line-by-line this session.) Not yet done.

---

## 6. Flagged for your attention

- [x] **Abstract's "up to 10 times" claim** — **done 2026-08-18**: reworded to "a drop in key rate, of 5 to 25 times depending on the dominant hardware impairment," matching §Security–Rate Trade-off's real numbers (5$\times$ channel-limited, 25$\times$ detector-efficiency-limited).

---

## 7. Post-writing / Administrative

- [x] **[BLOCKING] Write Acknowledgements section.** — **done 2026-08-27**: added `\section*{Acknowledgements and Statement of Contribution}` after `\maketitle`, before the abstract. Covers: personal contribution (sim architecture, cost model, MC sweeps, BT case study — all own work), Liao Chin Te's BB84 code as an early springboard since diverged from, NetSquid as the external DES engine used, supervisors (Dr Alejandra Beghelli, Dr Emilio Hugues Salas) and Qasim Bedford (discussions on QKD network/hardware modelling) thanked, sole-deliverable statement, code/data availability.
- [ ] **Final full review of dissertation** — read the whole document end to end once all other items above are closed out. Not yet done.
- [ ] **After submission: make the GitHub repo public.** Requires obscuring/scrubbing the LaTeX source first (as was done before, presumably for the same reason — check prior approach rather than re-deriving it). Explicitly deferred until after submission, not a pre-submission blocker.

# Dissertation TODO
> Generated 2026-08-03 from audit of `dissertation.tex`, `ROADMAP.md`, `TODO.md`, and `cost rethink/cost_analysis.tex`.
> Updated 2026-08-11: full re-audit against current `dissertation.tex` (§4 Results, §5 Discussion, §6 Conclusion now substantially complete — relay-sweep figure+table+prose for N=15 added, sensitivity/isolate/layers figures finalised, §6.2 Findings and §5.4 Implications for Protocol Selection rewritten with real numbers). All completed and moot items removed from this file — only remaining open work is listed below.
> Organised by category. Items marked **[BLOCKING]** must be done before submission.

---

## 1. Simulations to Run (data collection)

- [x] **SPAD-BB84 vs SNSPD-MDI relay sweep comparison** — **done 2026-08-13**. Both panels of Figure~\ref{fig:relay_sweep} now show BB84-SNSPD/BB84-SPAD/MDI: N=10 SPAD mean 126.3~kbps (±1σ 112.8–139.8), N=15 SPAD mean 136.5~kbps (±1σ 119.6–153.3). Caption updated with both baselines; new discussion paragraph added after the N=10 prose confirming, with real data, that SPAD-BB84 sits ~1.9–2.0× above the SNSPD-MDI peak with no overlap between the two distributions at either N — matches the 2026-08-12 back-of-envelope estimate almost exactly. Flags that any cost-per-bit comparison (Section~\ref{sec:results_cost}) must be read at unequal key rates.

- [ ] **Add $\eta_d=0.1$ point to detector efficiency sweep** — raw data landed 2026-08-13 (`docs/figures/August/final-figs/20260807 - P2P parameters_1/all parameters/efficiency/placeholder/efficiency/`), not yet integrated into `figures/p2p_sweeps/efficiency.tex`. Need to extend both BB84/MDI `\addplot` tables and the steelblue/darkorange stats-shading `\path` blocks, re-check `xmin`/`ymin` still bound the data.

- [ ] **`user_sweep.py`** — needs re-parameterisation, then rerun. The 2026-08-12 run was killed: spread across seeds was too wide and relays were placing degenerately. Not an algorithm bug — an expected consequence of the Weiszfeld objective (Section~\ref{sec:relay_placement}) when catchments are too large relative to relay count/area: overlapping catchments pull optimal relay positions on top of each other. Rerun with parameters (larger $K$, smaller area, or a tighter $N$ range) that keep catchments from overlapping this heavily. Since `relay_placement.py` below uses the same placement code, worth picking its $N$/$K$/area combinations to avoid the same large-catchment regime.

- [ ] **`relay_placement.py`** (exp 1 + exp 2, provider-growth model) — still outstanding; the other big remaining simulation task alongside `user_sweep.py` above.

~~Per-seed N=10 relay-sweep table~~ — **dropped 2026-08-12**: decided against: too large, too much information for the payoff; the existing N=15 per-seed table (Table~\ref{tab:relay_sweep_n15_seeds}) is illustrative enough on its own.

---

## 1b. Extensions (nice-to-have, appendix-suitable — not essential)

- [ ] **Timing scripts**: `time_vs_area.py`, `time_vs_users.py`, `adaptive_mc.py`, `surrogate.py`, `trend_analysis.py` — feeds Appendix~\ref{sec:appendix_netsquid} (NetSquid limitations/speedup strategies) rather than the core BB84-vs-MDI comparison.
- [ ] **Literature validation on `layers.py`**: identify 2–3 published key rate vs distance curves per protocol; overlay as scatter markers on the layers figure (Figure~\ref{fig:layers}).
- [ ] **MC run count audit**: for rates of order 10⁻ˣ target 10^(x+1) samples per point; audit all scripts and increase where under-sampled. *(Run counts are stated throughout the dissertation — e.g. 1000 runs/point for P2P sweeps, 250 runtimes/pair for the relay sweep — but nobody has audited whether those counts are actually adequate at the lowest observed rates.)*
- [ ] **MDI network-scale key rate gap — targeted ablation**: the mechanism is now explained analytically (BSM $\eta_\text{arm}^2$ scaling, §Security–Rate Trade-off) and the relay-routing-detour contribution is now quantified empirically (Table~\ref{tab:relay_sweep_n15_seeds}: only 9.4→11.3% of the BB84 rate recovered by increasing $K$). Not yet done: a dedicated ablation run isolating the BSM $\eta^2$ dependency and switch insertion loss individually (disable each in turn) to fully decompose the gap, as originally scoped.

---

## 2. Model Parameters — Verification

- [ ] **Confirm sweep ranges** used in compare figures match the realistic literature ranges (see hardware-param table in `lib/functions.py` / dissertation §Hardware Model). Where they differ, update the compare script x-ranges and re-shade. *(Red realistic-region shading itself is confirmed present in all four main P2P figures — length, efficiency, node_loss, charlie_pos — plus the appendix grid figures; this item is just the manual cross-check of the shaded bounds against literature, not yet done.)*

---

## 3. Referencing

- [ ] Citation for EOM insertion loss range (0.5–3 dB): standard photonics reference — needed for the node-loss justification in §Hardware Model.
- [ ] `\cite{PNS_desc}` currently points to EITCA (non-peer-reviewed); consider replacing with `\cite{Brassard_2000}` or `\cite{Chen2022}` for a more citable source.
- [ ] Check all `author = {... and others}` entries — some journals require full author lists; verify if UCL submission requires it.

---

## 4. Assumptions & Justifications Required

- [ ] **Multi-seeding (seed count justification)**: seed count stated in text but a diminishing-returns argument or inter-seed variance plot is not yet included.
- [ ] **TBB84 backbone: 1 source per relay (not K−1)**: relay backbone uses one QD source per relay node for relay-to-relay BB84. Strict bidirectional full-mesh backbone would require K−1 sources per relay (K(K−1) total). State simplification and bound the error: for K≤8 the undercount is ≤7× on backbone source cost. (cost_analysis.tex §9.6)
- [ ] **TBB84 backbone: unidirectional links (K(K−1)/2 sessions)**: simulated as half-duplex shared key per relay pair. Full duplex (separate key per direction) would double backbone rate and source count. State and justify or flag as a limitation. (cost_analysis.tex Inconsistency VII)

---

## 5. Miscellaneous

- [ ] **Word/page count vs UCL limit**: main body (Introduction–Conclusion) is currently 40 pages / ~12,368 words (text+headers+captions) — still need to check this against the actual UCL MSc Quantum Technologies project report limit.
- [ ] **Figure captions**: all figures need captions that are self-contained (readable without surrounding text).
- [ ] **Figure references**: every figure must be referenced in the text with `Figure~\ref{fig:...}`; check none are orphaned.
- [ ] **Spell check**: run `aspell` or equivalent on dissertation.tex; enforce British English throughout (`\cite{}` keys and code names exempt).
- [ ] **Compile clean**: ensure `dissertation.tex` compiles with zero warnings on two-pass `pdflatex` + `bibtex` run before submission.
- [ ] **Case study** (`docs/case-study-tex/case-study.tex`): confirm whether this is submitted alongside the main dissertation or is separate; if submitted, apply same checks.

---

## 6. Flagged for your attention

- [ ] **Abstract's "up to 10 times" claim**: now that §4/§6 have real numbers, the actual bipartite gap is $\sim$5$\times$ under channel-limited conditions (distance/attenuation), widening to over 25$\times$ under detector-efficiency degradation (Figure~\ref{fig:p2p_efficiency}) — "up to 10 times" doesn't match either the typical (5×) or worst-case (25×) figure now established. Worth rewording the abstract once you're happy with the final numbers.

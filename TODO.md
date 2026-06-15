# TODO

## Next Up

### 1. Realistic Hardware Regions on Plots
- [ ] Finalise hardware parameter values from literature (Lo 2012, Tang 2016, Berrevoets 2022) — web search pending
- [ ] Update PARAMS.md + configs with verified values (remove ⁺ markers)
- [x] Add shaded regions to all 9 compare scripts marking realistic operating range on sweep axis

### 2. DB Query / Replot Script
- [x] `scripts/P2P/analyse.py` — load saved results from `results.db` and regenerate plots without re-running simulations

### 3. Confidence Intervals on Plots
- [ ] Shade ±1 std dev around mean key rate curve using per-runtime data stored in DB
- [ ] Confirm and implement visualisation for `layers.py`

### 4. Charlie Placement Sweep
- [ ] Sweep Charlie's position on the MDI link (asymmetric Alice-Charlie / Charlie-Bob split)
- [ ] BB84 flat reference line (unaffected by relay placement)

---

## Backlog

See [ROADMAP.md](ROADMAP.md) for full feature and analysis status.

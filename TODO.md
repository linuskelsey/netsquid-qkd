# TODO

## Next Up

### 1. Realistic Hardware Regions on Plots
- [ ] Finalise hardware parameter values from literature (Lo 2012, Tang 2016, Berrevoets 2022) — web search pending
- [ ] Update PARAMS.md + configs with verified values (remove ⁺ markers) and ensure consistency

### 2. Literature Validation on layers.py
- [ ] Identify 2–3 published experimental key rate vs distance curves for BB84 (e.g. Lo 2012, Tang 2016)
- [ ] Identify 2–3 published experimental curves for MDI-QKD (e.g. Tang 2016, Yin 2016)
- [ ] Overlay literature data points on `layers.py` plots (scatter markers, distinct style from simulation lines)
- [ ] Add legend entries and source citations for each literature curve

### 3. `scripts/analyse/` — Interactive DB Replot TUI

- [ ] Create `scripts/analyse/db.py`: column metadata dict, `count_p2p`, `query_p2p`, `query_network`, `list_distinct`
- [ ] Create `scripts/analyse/tui.py`: Textual app, P2P tab (sweep radio, fixed param inputs, protocol checkboxes, error mode radio, Plot button)
- [ ] Add Network tab (x/y axis selectors, experiment radio, fixed params, Plot button)
- [ ] Wire Plot button → daemon thread → matplotlib window (same pattern as sweep scripts)
- [ ] Debounced live row count in status bar on any control change
- [ ] Reset to Defaults button

---

## Backlog

See [ROADMAP.md](ROADMAP.md) for full feature and analysis status.

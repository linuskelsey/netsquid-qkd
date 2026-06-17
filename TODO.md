# TODO

## Next Up

### 1. Realistic Hardware Regions on Plots
- [ ] Finalise hardware parameter values from literature (Lo 2012, Tang 2016, Berrevoets 2022) — web search pending
- [ ] Update PARAMS.md + configs with verified values (remove ⁺ markers) and ensure consistency
- [x] Add shaded regions to all 9 compare scripts marking realistic operating range on sweep axis

### 2. Literature Validation on layers.py
- [ ] Identify 2–3 published experimental key rate vs distance curves for BB84 (e.g. Lo 2012, Tang 2016)
- [ ] Identify 2–3 published experimental curves for MDI-QKD (e.g. Tang 2016, Yin 2016)
- [ ] Overlay literature data points on `layers.py` plots (scatter markers, distinct style from simulation lines)
- [ ] Add legend entries and source citations for each literature curve

### 3. Database Saving
- [ ] Modify save path for figures auto-saved by `run_all.py`

### 4. Network Simulation
- [x] `network/topology.py` — user placement, k-means relay optimisation, BB84/MDI link distances
- [x] `network/visualise_network.py` — side-by-side MDI cluster / BB84 mesh plot
- [ ] `network/bb84_network.py` — run BB84 over all N(N-1)/2 direct pairs, return per-pair key rates
- [ ] `network/mdi_network.py` — run MDI over all pairs via nearest relay, handle cross-cluster routing
- [ ] `scripts/network/relay_sweep.py` — Exp 1: fixed N, vary K, plot key rate vs relay count
- [ ] `scripts/network/user_sweep.py` — Exp 2: fixed K (from Exp 1 plateau), vary N, plot key rate vs user count

---

## Backlog

See [ROADMAP.md](ROADMAP.md) for full feature and analysis status.

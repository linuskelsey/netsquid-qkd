# TODO

## Next Up

### ~~1. QBER Cutoff~~ ✓ complete
11% threshold for both BB84 and MDI. Runs exceeding cutoff recorded as `"nan"` in chunk functions.

### 2. Scripting Cleanup + Realistic Hardware Regions
Identify and annotate realistic operating regions on key rate vs parameter graphs.
- [ ] Define realistic hardware parameter ranges (α, η_d, d_c) from literature / BT spec
- [ ] Add shaded regions or reference lines to compare script plots (loss, efficiency, dark count)
- [ ] Consider a `configs/realistic_hardware.json` preset for a real-world baseline
- [ ] Review compare scripts for any shared boilerplate worth factoring out

---

## Backlog

See [ROADMAP.md](ROADMAP.md) for full feature and analysis status.

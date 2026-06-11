# TODO

## Next Up

### 1. QBER Cutoff
Abort runs where QBER exceeds a threshold (key generation not secure above ~11% for BB84, ~15% for MDI under ideal conditions).
- [ ] Confirm exact cutoff values to use (BB84 and MDI, may differ)
- [ ] Implement cutoff in both `BB84_run.py` and `mdiRun.py`
- [ ] Decide: hard abort (return empty key) or soft flag (exclude from aggregate stats)?
- [ ] Update compare scripts to handle zero-length keys at cutoff points

### 2. Scripting Cleanup + Realistic Hardware Regions
Identify and annotate realistic operating regions on key rate vs parameter graphs.
- [ ] Define realistic hardware parameter ranges (α, η_d, d_c) from literature / BT spec
- [ ] Add shaded regions or reference lines to compare script plots (loss, efficiency, dark count)
- [ ] Consider a `configs/realistic_hardware.json` preset for a real-world baseline
- [ ] Review compare scripts for any shared boilerplate worth factoring out

---

## Backlog

See [ROADMAP.md](ROADMAP.md) for full feature and analysis status.

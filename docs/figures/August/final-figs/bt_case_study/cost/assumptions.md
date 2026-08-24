# BT Real Topology — Deployment Cost vs User Count

Fixed parameters for this plot:

- **Illustrative prices**: c_s=£250,000 (source), c_d=£100,000 (detector module), c_f=£10,000/km (new-build dark fibre install)
- **Cost formula**: N*c_s + {N or K}*c_d + total_fibre_km*c_f, multi-channel-detector-module simplification (eq:nstar_closed derivation), real fibre lengths (network/fibre_length.py, no NetSquid simulation needed)
- **K (relays)**: 3
- **User count sweep (deterministic, no NetSquid)**: 5-40 (step 5)
- **Cost (£M) per protocol per N**: {'BB84': {5: 3.642350895768956, 10: 13.925540533472736, 15: 27.537607414029374, 20: 47.57000621180052, 25: 71.42013057568079, 30: 95.97570812622496, 35: 134.90910324573693, 40: 180.54129683033526}, 'MDI': {5: 2.7550082512185927, 10: 4.382636847614654, 15: 5.790986497168716, 20: 7.451489664730808, 25: 9.066974505467961, 30: 10.71638707134036, 35: 12.273542987427927, 40: 13.900057006215036}, 'TBB84': {5: 2.7550082512185927, 10: 4.382636847614654, 15: 5.790986497168716, 20: 7.451489664730808, 25: 9.066974505467961, 30: 10.71638707134036, 35: 12.273542987427927, 40: 13.900057006215036}}

Other assumptions:

- TBB84 cost is defined identically to MDI's (same formula, same component count under the multi-channel simplification, same real fibre length reused directly) since the two protocols differ only in trust assumptions, not component count — the two curves coincide exactly by construction, not by coincidence.
- All prices are illustrative, not vendor-quoted, per the existing symbolic-vs-numeric cost-model hedge in sec:results_cost.

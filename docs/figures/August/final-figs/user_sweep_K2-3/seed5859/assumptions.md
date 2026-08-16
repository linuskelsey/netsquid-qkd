# Key Rate vs User Count (seed=5859)

Fixed parameters for this plot:

- **Seed**: 5859
- **Relay counts (K)**: [2, 3]
- **User count sweep range**: 8-20 (step 2)
- **Area**: 25.0×25.0 km
- **Relay strategy**: weiszfeld
- **Catchment shape**: Gaussian, std 5.00 km
- **Tortuosity mean**: 1.2
- **Runtimes per pair**: 250
- **Repair note**: K=3 recomputed on the K=2 user layout (see scripts/network/fix_user_sweep_k3.py); BB84/K=2 unchanged.
- **BB84-SNSPD key rate (bps) per N**: {8: 867675.140976804, 10: 861886.1380444424, 12: 812896.0607775423, 14: 737094.3899410317, 16: 715565.5872671594, 18: 714589.1157722953, 20: 727901.9330138396}
- **BB84-SPAD key rate (bps) per N**: {8: 192277.504528222, 10: 191480.32723953036, 12: 180630.12500427055, 14: 163913.96744023988, 16: 159252.38662823394, 18: 158720.19710337013, 20: 161478.59653147706}
- **MDI K=2 key rate (bps) per N**: {8: 112048.04317252555, 10: 94013.64361021642, 12: 83919.65156640031, 14: 72516.72560500108, 16: 65819.12832500265, 18: 59443.63527852291, 20: 61442.14055563066}
- **MDI K=3 key rate (bps) per N**: {8: 87446.27373704966, 10: 64393.477657072144, 12: 61546.45930767997, 14: 50726.8424774658, 16: 43883.80418584052, 18: 42568.931282853046, 20: 39030.020386915676}

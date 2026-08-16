# Key Rate vs User Count (seed=82693)

Fixed parameters for this plot:

- **Seed**: 82693
- **Relay counts (K)**: [2, 3]
- **User count sweep range**: 8-20 (step 2)
- **Area**: 25.0×25.0 km
- **Relay strategy**: weiszfeld
- **Catchment shape**: Gaussian, std 5.00 km
- **Tortuosity mean**: 1.2
- **Runtimes per pair**: 250
- **Repair note**: K=3 recomputed on the K=2 user layout (see scripts/network/fix_user_sweep_k3.py); BB84/K=2 unchanged.
- **BB84-SNSPD key rate (bps) per N**: {8: 779963.5725888992, 10: 807115.873257595, 12: 835024.8691338073, 14: 793651.577778039, 16: 803111.1057377639, 18: 774130.9228424309, 20: 732299.8489080068}
- **BB84-SPAD key rate (bps) per N**: {8: 173122.03657039703, 10: 179212.0275335172, 12: 185530.9699609663, 14: 176488.75834415734, 16: 178445.32222169134, 18: 171844.0844873535, 20: 162679.6282640408}
- **MDI K=2 key rate (bps) per N**: {8: 86501.10546883357, 10: 92861.990065363, 12: 91758.74979279801, 14: 82828.1753761337, 16: 82633.49238709851, 18: 80569.39096164447, 20: 75551.51918360742}
- **MDI K=3 key rate (bps) per N**: {8: 91410.25532527147, 10: 91892.85012846057, 12: 93449.26320376806, 14: 82447.73378090808, 16: 81191.29349190909, 18: 78437.51842443986, 20: 72717.29757515399}

# Key Rate vs User Count (seed=3622)

Fixed parameters for this plot:

- **Seed**: 3622
- **Relay counts (K)**: [2, 3]
- **User count sweep range**: 8-20 (step 2)
- **Area**: 25.0×25.0 km
- **Relay strategy**: weiszfeld
- **Catchment shape**: Gaussian, std 5.00 km
- **Tortuosity mean**: 1.2
- **Runtimes per pair**: 250
- **Repair note**: K=3 recomputed on the K=2 user layout (see scripts/network/fix_user_sweep_k3.py); BB84/K=2 unchanged.
- **BB84-SNSPD key rate (bps) per N**: {8: 608090.737806878, 10: 653599.0511802454, 12: 709855.2841140198, 14: 707363.0583901384, 16: 642536.7774677125, 18: 639299.6059247534, 20: 644962.5648659663}
- **BB84-SPAD key rate (bps) per N**: {8: 135296.88098098556, 10: 145019.97073689097, 12: 157532.3277992448, 14: 157002.95525606498, 16: 142636.9281429664, 18: 142259.50171331814, 20: 143040.37915967294}
- **MDI K=2 key rate (bps) per N**: {8: 67718.02158962631, 10: 66895.68574733866, 12: 59997.178932374045, 14: 59676.3359720132, 16: 53611.15455098613, 18: 56994.590273039925, 20: 53873.04201751888}
- **MDI K=3 key rate (bps) per N**: {8: 52533.2877652533, 10: 52676.98130647208, 12: 49543.57379010918, 14: 51673.087730063045, 16: 50424.69663604849, 18: 51524.401403688564, 20: 52326.709546203245}

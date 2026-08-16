# Key Rate vs User Count (seed=39660)

Fixed parameters for this plot:

- **Seed**: 39660
- **Relay counts (K)**: [2, 3]
- **User count sweep range**: 8-20 (step 2)
- **Area**: 25.0×25.0 km
- **Relay strategy**: weiszfeld
- **Catchment shape**: Gaussian, std 5.00 km
- **Tortuosity mean**: 1.2
- **Runtimes per pair**: 250
- **Repair note**: K=3 recomputed on the K=2 user layout (see scripts/network/fix_user_sweep_k3.py); BB84/K=2 unchanged.
- **BB84-SNSPD key rate (bps) per N**: {8: 712932.0162461363, 10: 681740.0817491161, 12: 704957.2478906781, 14: 724183.6686451728, 16: 726537.576023379, 18: 675753.5099877211, 20: 658404.2931888958}
- **BB84-SPAD key rate (bps) per N**: {8: 158684.75438965106, 10: 151659.5326686618, 12: 156884.79987674396, 14: 160976.57777229362, 16: 161470.85058458845, 18: 150437.64793277654, 20: 146533.66838685315}
- **MDI K=2 key rate (bps) per N**: {8: 72314.32194735613, 10: 65307.978866649595, 12: 73303.98095597695, 14: 75475.02015027475, 16: 73963.03206188716, 18: 64948.302786630644, 20: 60976.66703781228}
- **MDI K=3 key rate (bps) per N**: {8: 85459.57358024344, 10: 74718.31228128701, 12: 77409.75095952395, 14: 76790.86330611419, 16: 78072.16646583083, 18: 67001.36495574412, 20: 62355.59210140737}

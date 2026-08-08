# MDI: Cumulative Modelling Layers

Fixed parameters for this plot:

- **Distance sweep points (km)**: [1, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
- **Runtimes per point**: 1000
- **Layers (cumulative)**: {'Layer 0: Ideal': 'layer0_ideal.json', 'Layer 1: + fibre loss @ 0.18 dB/km': 'layer1_loss.json', 'Layer 2: + detector efficiency @ 0.90': 'layer2_eff.json', 'Layer 3: + dark count rate @ 50 cps': 'layer3_dark.json', 'Layer 4: + init loss @ 0.10': 'layer4_init_loss.json', 'Layer 5: + node loss @ 2.0 dB': 'layer5_node_loss.json', 'Layer 6: + source error @ 0.015': 'layer6_source_err.json', 'Layer 7: + dephasing @ 3.2e-7/km': 'layer7_dephasing.json', 'Layer 8: + basis bias @ 0.715': 'layer8_basis_bias.json', 'Layer 9: + BS efficiency @ 0.97': 'layer9_bs_eff.json'}

Other assumptions:

- Each layer adds one parameter at its realistic value on top of all previous layers.
- MDI runs layers 0-9 (includes beam splitter efficiency).

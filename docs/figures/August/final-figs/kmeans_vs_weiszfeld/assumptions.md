# k-means vs Weiszfeld relay placement (N=20, K=3, seed=42)

Fixed parameters for this plot:

- **N (users)**: 20
- **K (relays)**: 3
- **Area**: 10.0 x 10.0 km
- **Seed**: 42
- **k-means total fibre length (km)**: 54.802
- **Weiszfeld total fibre length (km)**: 52.763
- **Reduction**: 3.72%
- **User positions (km)**: [[7.74, 4.389], [8.586, 6.974], [0.942, 9.756], [7.611, 7.861], [1.281, 4.504], [3.708, 9.268], [6.439, 8.228], [4.434, 2.272], [5.546, 0.638], [8.276, 6.317], [7.581, 3.545], [9.707, 8.931], [7.784, 1.946], [4.667, 0.438], [1.543, 6.83], [7.448, 9.675], [3.258, 3.705], [4.696, 1.895], [1.299, 4.757], [2.269, 6.698]]
- **k-means cluster labels**: [0, 1, 2, 1, 2, 2, 1, 0, 0, 1, 0, 1, 0, 0, 2, 1, 0, 0, 2, 2]
- **k-means relay positions (km)**: [[5.713, 2.354], [8.011, 7.997], [1.84, 6.969]]
- **Weiszfeld relay positions (km)**: [[5.216, 2.52], [7.603, 7.84], [2.269, 6.698]]

Other assumptions:

- Weiszfeld panel is refined from the same k-means init/seed as the left panel, so cluster indices (and colours) stay aligned across panels; final cluster membership is by nearest-relay distance to the converged Weiszfeld relay positions, per optimise_relays().

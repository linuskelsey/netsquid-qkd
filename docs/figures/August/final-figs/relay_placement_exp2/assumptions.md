# Relay Placement: Centroid vs Boundary

Fixed parameters for this plot:

- **Experiment**: 2 — two clusters, K=2 relays
- **User count sweep range**: 5-10
- **Area**: 25.0 x 25.0 km
- **Cluster spread (std)**: 5.00 km
- **Runtimes per pair**: 1000
- **Random topologies averaged**: 4
- **Seed (base)**: 62740
- **Seeds used**: [43486, 37209, 76272, 29111]
- **Final graph per seed (N=n_max, km)**: {43486: {'user_positions': [[2.616, 14.514], [3.969, 11.679], [0.148, 9.533], [14.375, 10.531], [8.878, 12.722], [22.479, 13.936], [20.453, 2.519], [22.92, 12.293], [21.211, 15.47], [25.0, 12.907]], 'cluster_labels': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1], 'relay_positions_centroid': [[5.997, 11.796], [22.412, 11.425]], 'relay_positions_boundary': [[10.764, 11.688], [15.941, 11.571]]}, 37209: {'user_positions': [[0.0, 14.562], [8.576, 6.322], [0.0, 10.53], [4.567, 9.533], [8.482, 13.903], [17.909, 4.844], [17.625, 19.24], [23.085, 14.018], [10.236, 11.897], [17.646, 16.835]], 'cluster_labels': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1], 'relay_positions_centroid': [[4.325, 10.97], [17.3, 13.367]], 'relay_positions_boundary': [[9.026, 11.838], [12.439, 12.469]]}, 76272: {'user_positions': [[10.235, 11.341], [3.319, 17.09], [0.0, 17.81], [11.208, 18.284], [3.778, 16.557], [20.586, 4.223], [18.446, 11.027], [14.563, 17.061], [19.336, 20.295], [21.347, 20.249]], 'cluster_labels': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1], 'relay_positions_centroid': [[5.708, 16.216], [18.855, 14.571]], 'relay_positions_boundary': [[11.986, 15.431], [13.75, 15.21]]}, 29111: {'user_positions': [[0.0, 16.042], [5.275, 15.877], [10.766, 7.215], [11.471, 8.196], [7.927, 14.236], [17.568, 17.632], [15.418, 4.774], [15.412, 13.321], [16.412, 12.235], [22.126, 12.46]], 'cluster_labels': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1], 'relay_positions_centroid': [[7.088, 12.313], [17.387, 12.084]], 'relay_positions_boundary': [[11.867, 12.207], [13.059, 12.18]]}}

Other assumptions:

- Boundary strategy displaces each relay 1 std toward the opposing cluster.

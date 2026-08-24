# BT Real Topology Map

Fixed parameters for this plot:

- **Real topology**: data/real_topologies/bt.json (Slough, West End, City of London)
- **K (relays)**: 3
- **N (users, full sweep count)**: 40
- **Catchment radius (km)**: 10.0
- **Placement-area margin (km, all 4 sides of relay bbox)**: 15.0
- **Catchment assignment**: nearest-anchor reassignment after 10km-disc draw (assign_nearest_catchment), not fixed-at-draw membership
- **Seed**: 42

Other assumptions:

- Orientation figure only — no numerical result attached. Relay positions are the real BT site coordinates (shifted uniformly so the placement area has margin_km clearance on every side; relative geometry unchanged), never re-optimised. User positions are synthetic (no real user-site data exists), anchored on the 3 real sites.

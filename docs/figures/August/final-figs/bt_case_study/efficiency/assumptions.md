# BT Real Topology — Key Rate per Unit Cost vs User Count

Fixed parameters for this plot:

- **Derived from**: key_rate/ (NetSquid-simulated) and its own cost computation at the same (narrower) rate-N values
- **User count sweep**: 5-15 (step 1)
- **Efficiency (kbps/£M) per protocol per N**: {'BB84': {5: 152.1730644580254, 6: 101.11934691416751, 7: 87.62194787067666, 8: 56.59794135374559, 9: 49.61119458470701, 10: 31.816090788935348, 11: 24.700296013570657, 12: 22.763132016082857, 13: 20.662071361057688, 14: 19.81503792033596, 15: 19.32651845801809}, 'MDI': {5: 15.550519017776452, 6: 14.571656788947195, 7: 15.892716704087768, 8: 11.700594792670609, 9: 12.98271593673557, 10: 10.614459214993087, 11: 9.357367242952998, 12: 9.92589402915988, 13: 9.30833436790098, 14: 9.642791000210371, 15: 10.52141555220099}, 'TBB84': {5: 149.9742611933429, 6: 107.04554395390576, 7: 97.3674885517819, 8: 73.77618198080316, 9: 72.19809274883644, 10: 61.89436835672058, 11: 58.38748707181315, 12: 58.91574594743987, 13: 53.10754913971233, 14: 51.73976755107709, 15: 52.31588531032354}}

Other assumptions:

- Capped at the rate-sweep's N range (not the wider cost-sweep range): efficiency needs a simulated key rate at every N, which only exists where NetSquid was actually run.
- Cost-efficiency ranks protocols in the reverse order of their trust guarantees: TBB84 (least trustless) most cost-efficient, MDI (most trustless) least — ties to the Level 0-3 trust hierarchy in sec:results_cost / Deployment Recommendations.

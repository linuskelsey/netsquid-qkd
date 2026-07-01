<!-- SENT TO CQT 29 Jun 2026 — do not edit -->

## NetSquid for Quantum Networks: Capabilities, Bottlenecks and Lessons

Discrete-event simulation (DES) engines like NetSquid are essential tools for designing and optimizing quantum communication networks, allowing protocol feasibility studies and requirement assessments without expensive hardware deployment. However, as network scale and physical parameter set grow, these simulators hit hard computational limits. Here, we introduce NetSquid's design and show how it bridges device-level parameters to network-level protocol metrics using a comparison of BB84 and MDI-QKD as a running example. We demonstrate what makes it powerful - and confront its fundamental scaling bottleneck.

A modest parameter sweep over a physically realistic metropolitan network of 100 nodes on a modern high-end consumer device can require full CPU utilisation for periods of the order of one week or more. This is a scaling issue core to any DES engine. Quantum memories, entanglement swapping and other quantum-native effects introduce more complex interdependencies resistant to parallelisation. We close by posing the open question of what this means for the trajectory of quantum network modelling: whether to optimise existing DES frameworks, or to design bespoke for specific network architectures as the field reaches application scale.

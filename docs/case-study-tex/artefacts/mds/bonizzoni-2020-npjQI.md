www.nature.com/npjqi 

## ARTICLE **OPEN** 



# Storage and retrieval of microwave pulses with molecular spin ensembles 

Claudio Bonizzoni 1,2 ✉, Alberto Ghirri 2, Fabio Santanni 3, Matteo Atzori3,4, Lorenzo Sorace 3, Roberta Sessoli 3 and Marco Affronte<sup>1,2</sup> 

Hybrid architectures combining complementary quantum systems will be largely used in quantum technologies and the integration of different components is one of the key issues. Thanks to their long coherence times and the easy manipulation with microwave pulses, electron spins hold a potential for the realization of quantum memories. Here, we test diluted oxovanadium tetraphenyl porphyrin (VO(TPP)) as a prototypical molecular spin system for the Storage/Retrieval of microwave pulses when embedded into planar superconducting microwave resonators. We first investigate the efficiency of several pulse sequences in addressing the spins. The Carr-Purcell and the Uhrig Dynamical Decoupling enhance the memory time up to three times with three π pulses. We then successfully store and retrieve trains of up to 5 small pulses by using a single recovery pulse. These results demonstrate the memory capabilities of molecular spin ensembles when embedded into quantum circuits. 

npj Quantum Information (2020) 6:68 ; https://doi.org/10.1038/s41534-020-00296-9 

### INTRODUCTION 

Quantum memories are fundamental components in quantum hardware like quantum computers, sensors or repeaters. To perform Storage/Retrieval operations the physical system must fulfill two conditions: (i) having a phase memory time Tm (this one being the characteristic lifetime the hardware can sustain coherent dynamics) long enough to allow for the survival of the information during operation and (ii) allow for the possibility of codifying a pulse sequence into the memory through a suitable protocol<sup>1</sup> . Nuclear spin ensembles have been demonstrated to work as efficient quantum memories operating at radio frequencies<sup>2–4</sup> . Spin states of magnetic impurities and color centers in silicon or diamond with long Tm3,5,6 can be individually or collectively addressed by combining microwave (MW) excitations with their photoluminescent properties. In the perspective of scalable platforms however, hybrid architectures working with a single frequency mode allows for a simplification of the design of the platforms. Avoiding multiple frequency conversion is also highly desirable. Electronic spin degrees of freedom provided by ensembles have been efficiently exploited into circuit quantum electrodynamics (cQED) architectures including superconducting devices and resonators<sup>7–9</sup> fully operating at microwave frequency. Although the use of individual (natural or artificial) spins is the ultimate goal<sup>10</sup> collective excitations in spin ensembles may preserve and coherently exchange electromagnetic excitations, and eventually quantum information, under optimal conditions<sup>8,9,11,12</sup> . In this context, molecular spins have recently emerged as a new class of quantum systems whose electronic and nuclear spin states and their relative quantum features (including g-factor<sup>13,14</sup> , coherence time<sup>15–17</sup> , “atomic-clock” transitions<sup>13,18,19</sup> ) can be extensively tailored synthetically. Different strategies for encoding quantum information protocols into molecular ensembles<sup>20,21</sup> or single molecules in a spin transistor geometry<sup>22,23</sup> have been developed and experimentally proven. 

The magnetic coupling and the integration of molecular spins into planar resonant geometries has been extensively investigated<sup>24–27</sup> . Moreover, the coherent coupling with MW photons has been recently achieved using transition metal-based oxovanadium(IV) complexes<sup>28,29</sup> , as well as organic radicals<sup>29–31</sup> embedded into planar resonant geometries, paving the way for the integration of molecular spin ensembles into microwave quantum architectures. However, optimal experimental conditions and protocols (i.e., pulse sequences) to address the spins and to correct intrinsic (related to the ensemble) or extrinsic factors (such as inhomogeneities of resonant geometry) that may limit Tm still need to be discovered in order to efficiently encode and exchange states of qubits between spins and superconducting circuits. 

In this work we test an oxovanadium(IV) complex, VO(TPP) (where TPP is the tetraphenylporphyrin)<sup>32</sup> as a prototypical molecular spin system embedded into a planar superconducting microwave resonator by addressing it with several MW pulse sequences. Previous Pulsed Wave (PW) Electron Spin Resonance (ESR) study performed with a commercial spectrometer gave a (Hahn echo) Tm ≈ 1 μs at 4 K, with essentially no temperature dependence between 4 and 30 K<sup>32</sup> . Rabi oscillations were observed up to room temperature, consistent with that reported for similar oxovanadium(IV) complexes<sup>33–35</sup> . We first measure the phase memory time of diluted single crystal samples with the Hahn echo sequence and we then test two dynamical decoupling sequences: the Carr-Purcell-Meiboom-Gill (hereafter CP) sequence and the Uhrig Dynamical Decoupling (hereafter DD) sequence. These protocols are widely used to dynamically decouple the spins from environmental sources of decoherence and, hence, are expected to enhance Tm36–39. Although the efficiency of CP and DD sequences has been previously investigated on spin impurities in inorganic matrices<sup>40–42</sup> and in organic molecules<sup>43–45</sup> (including radicals<sup>39,46</sup> ) coupled to conventional (3-dimensional) ESR cavities, their efficiency still needs to be tested on molecular spins in 

> 1Dipartimento di Scienze Fisiche, Informatiche e Matematiche, Università di Modena e Reggio Emilia, via G. Campi 213/A, 41125 Modena, Italy. 2Istituto Nanoscienze CNR, Sezione S3, via G. Campi 213/A, 41125 Modena, Italy.<sup>3</sup> Dipartimento di Chimica “Ugo Schiff”, via della Lastruccia 3, 50019 Sesto Fiorentino (FI), Italy.<sup>4</sup> Present address: Laboratoire National des Champs Magnetiques Intenses (LNCMI), Univ. Grenoble Alpes, INSA Toulouse, Univ. Toulouse Paul Sabatier, EMFL, CNRS, F-38042 Grenoble, France. ✉email: claudio.bonizzoni@unimore.it 

Published in partnership with The University of New South Wales 

np) 



<!-- Start of picture text -->
b Cc 2K, 120-210 ns<br>1 0 2% cnyetal = CW sweep<br>= —— Simulation ©<br>: —20<br>2 05 ><br>=2 £15J)<br>£ o<br>—_ <<br>0.0 8 10<br>0.22 0.24 0.26 0.28 0.22 0.24 0.26<br>Magnetic Field, B, (T) Magnetic Field, By, (T)<br><!-- End of picture text -->

C. Bonizzoni et al. 

3 

polycrystalline sample (see Supplementary Fig. 11a). We measure the decay of the Hahn echo for different inter-pulse delays, tdelay, and we fit it with the equation: 





In Eq. (2) Tm is the memory time, while x is a stretching exponent. I(t) is the echo integral, t0 is the initial sequence time, and t = ∑<sup>#delay</sup> tdelay + ∑<sup>#pulse</sup> tpulse is the total sequence time (being tpulse the duration of each pulse). 

For the 2% diluted crystal the fitted memory time is Tm = 0.97 ± 0.10 μs (with x = 1.2 ± 0.1), which is close to the one measured for the 2% polycrystalline sample (Tm = 1.04 ± 0.10 μs). The latter is also consistent with the one reported in ref.<sup>32</sup> from conventional X-band ESR (for similar temperatures). The agreement with conventional ESR indicates that the Hahn echo sequence efficiently overcomes the Free Induction Decay (FID) limit and lead us to conclude that the measured memory time essentially results from the spin dynamics (i.e., only from intrinsic effects of the sample)<sup>47,48</sup> . In other words, the Hahn sequence is correcting the inhomogeneities of the static magnetic field B048. The observation of the Rabi oscillations on both crystal and polycrystalline samples, together with their characteristic linear frequency dependence on the MW magnetic field intensity (see Supplementary Section 2.5), further corroborates the capability to coherently manipulate the spin ensemble with the pulsed MW field B1 delivered through our superconducting resonator. 

### Dynamical decoupling sequences 

Thanks to the successful manipulation achieved with the Hahn Echo, we now extend our pulse sequences by considering two dynamical decoupling protocols. Each sequence will be identified as CPN (Carr-Purcell-Meiboom-Gill) or DDN (Uhrig Dynamical Decoupling), with N the number of π pulses sent. The pulse patterns of the two sequences are sketched in Figs. 2a and b for the case N = 3. 

The decay of the echo integral as a function of time for the crystal at 2 K and for both CP and DD is shown in Figs. 2c and d, respectively. In both cases the phase memory time clearly increases with N. We fit the data of Fig. 2 with Eq. (2) (dashed lines), leaving Tm and x as free parameters. For the CP sequences a stretch parameter x ≈ 1.2, independent of the number of applied pulses, is obtained as best fit parameter<sup>57,58</sup> . For the DD sequences, the stretch exponent is found to be x ≈ 1 for all the data set. All the obtained Tm’s are summarized in Fig. 2.e. Both sequences progressively enhance Tm up to 3 μs, that is ≈3 times longer with respect to the one found with the Hahn echo sequence. The increasing trend suggests that further enhancement of Tm can be expected in both sequences by applying a larger number of pulses, even if the small echo intensity found in our experimental conditions limits us to N = 3 (DD) or N = 4 pulses (CP). Although similar enhancement is observed, a larger number of π pulses (N = 4) is needed for CP with respect to DD (N = 3) to obtain similar Tm values, suggesting that the latter control sequences are more efficient in decoupling the spins from the environment<sup>36,37,59</sup> . 

Our results show that both CP and DD protocols can address and correct the dephasing effects and, since a single π pulse (i.e. the Hahn sequence) essentially corrects inhomogeneities of the static magnetic field (see above), we can ultimately attribute the observed phenomenology (Fig. 2e) to the intrinsic spin dynamics of the sample. We might also argue that the different efficiency of CP and DD sequences is due to the fact they address different spectral portions of the environmental noise distribution<sup>36,38,42</sup> . However, a more detailed analysis of this latter point would require a dedicated work. Although polycrystalline samples provide larger echo signals than single crystal ones, thus allowing the application of longer sequences (up to N = 5), we find both 

the DD and the CP protocols to be no more progressively efficient with increasing N than the single crystal (see Supplementary Section 2.6 and Supplementary Fig. 13). 

### Storage and retrieval of MW excitations 

To test the viability of the VO(TPP) ensembles as storage memories, we send a train of weak MW pulses followed by a π pulse at 2 K and ∣B0∣ = 0.24 T, as depicted in Fig. 3a (see Supplementary Section 1.5). An increasing number of output echos is found as the number of input pulses is increased (Fig. 3b), and up to 3 well resolved echoes, corresponding to 3 weak input pulses, can be detected with the single crystal under our experimental conditions. Similar results are found also for the powder sample, for which the larger echo signal allows the storage and retrieval of up to 5 pulses (Fig. 4a). These observations reflect the memory effect of the spin ensemble in the precession of the spins<sup>9,47,48</sup> : once the MW excitations are sent (stored) into the ensemble, the spins dephase until the refocusing π pulse is applied. At this point the excitations are retrieved as an echo train. In other words, the ensemble has kept trace of the initial excitations<sup>9,47,48,60</sup> . 

It is worth noting that the duration of the free spin precession after all the excitations have been stored is tprec ≥ 2τ = 2.2 μs >Tm, being τ = 1.1 μs the inter-pulse delay of Fig. 3a (the shortest value between the one used for powder and crystal was used here). Note also that the decay time of the echo train is consistent with the intrinsic Hahn echo Tm, corroborating the fact that the Storage/Retrieval is essentially limited by dephasing processes within the sample and not by the resonator (see Supplementary Fig. 16). 

The larger echo signals observed on the powder sample allow us to manipulate sequences of five pulses. For instance we selectively turn on (1) and off (0) the second, the third and the fourth input pulse with respect to the others and then the second and the fourth together, as in Fig. 4b. As a consequence the number of the output echoes changes, depending on which pulses are switched on/off. Interestingly, this allows us to verify that the order of the output echoes is reversed with respect to the input excitations, as expected by the time reversal (refocusing) of the π pulse. Similar selectivity and control on the output echoes is observed also for the single crystal and even when the magnetization of the ensemble is firstly rotated by an arbitrary rotation angle (Supplementary Figs 15 and 17). 

### DISCUSSION 

Overall, our results show viable paths for the integration of molecular spin ensembles into hybrid quantum circuits. More specifically we successfully apply protocols to store and retrieve sequences of MW pulses into the molecular ensembles. Further analysis of our results indicates that with regard to true quantum memories there are large margins of improvement, as we are going to discuss in the following section. 

Firstly, it should be kept in mind that our experiments are performed at 2 K, with relatively high photon numbers (nph ≈ 10<sup>11</sup> for π/2, π pulses and nph ≈ 10<sup>9</sup> for the weak ones, see Supplementary Table 3 and Supplementary Section 2.7) and with effective numbers of spins ≈ 10<sup>15</sup> −10<sup>16</sup> ≫ nph (see Supplementary Section 2.1). While these working conditions can be suitable for some applications, they are still far from the typical ones required by quantum circuits. In fact, these operate at much lower temperatures (mK, that is two order of magnitude below) and make use of spin excitations with much lower photon numbers (nph ≈ 1 − 100, that is several orders of magnitude lower)<sup>9,48</sup> . Note that the limit set by our working conditions is rather technological than fundamental and it can be overcome with the currently available MW and cryogenic instrumentation and techniques. For 

Published in partnership with The University of New South Wales 

npj Quantum Information (2020) 68 

oj 



<!-- Start of picture text -->
d V2 4 2T 2T T b ¥/2 r r<br>| |<br>| | time 0 I J time<br>Cd<br>=1.0 8 2K, By =B, = 1.0 A 2K, By =B<br>. IY Data Fit . 4 Data Fit<br>5 0.6 Lo= P4 A ---- 4 0.6 ehRo, DD3 A<br>£04, A £04 8%<br>202 LN 202] B&R<br>WW 0.0 Cela doo! Re ws<br>0 2 4 6 8 10 0 2 4 6 8 10<br>t-ty (us) tt, (us)<br>€<br>4<br>; o 1<br>2<br>® 3<br>= 2<br>1 2K, By =B,,<br>© Crystal<br>DD @<br>0 CP o<br>1234<br>#n-pulses<br><!-- End of picture text -->

.. / 



<!-- Start of picture text -->
a tw<br>TRG<br>0 0 time<br>< 6 : : : 1 pulses<br>Q i 2 pulses<br>= 0 : : 3 pulses<br>{© :<br>= 00 05 10 15<br>Time (us)<br><!-- End of picture text -->



<!-- Start of picture text -->
d 2K, By=B,<br>< 0d 1 pulse<br>E 20 : 4h . 2 pulses<br>[&} i : : H : i 3pulses<br>© 0 [ - [y 5 pulses<br>0 1 2<br>b Time (us)2K, By =B<br>< Co on | [ 2 0-1<br>E 20 Pl EER REET<br>5 am 140<br>0 1 2<br>Time (us)<br><!-- End of picture text -->

C. Bonizzoni et al. 

6 

through the output MW coaxial line, it is amplified and then downconverted back to radiofrequency with another IQ mixer. The time domain acquisition of the signal is performed by using an oscilloscope (Supplementary Fig. 4). The oscilloscope traces are then integrated via software after data acquisition. The typical length of our π/2 pulses is tπ/2 = 120–150 ns, while the MW magnetic field strength is ∣B1∣ ≈ 10<sup>−5</sup> T (see Supplementary Section 2.5). The details of the experimental set-up and of the pulse sequences are reported in Supplementary Sections 1.4 and 1.5, respectively. 

### EasySpin simulation of VO(TPP) transmission spectra 

We simulate the CW spectra of Fig. 1.b with Eq. (3), using the values reported in ref.<sup>32</sup> and assuming Voigtian lineshapes (see Supplementary Section 2.2). 

#### b HS ¼ μBS � g � Beff þ<sup>V</sup> I �<sup>V b</sup> A � S: 

(3) 

The superconducting nature of the resonator is taken into account by introducing in Eq. (3) an effective static magnetic field Beff = B0 + Bmeiss. Here, B0 is the externally applied static magnetic field and Bmeiss is an additional screening contribution arising from the superconducting material of the resonator (see Supplementary Section 2.2). The angle between B0 and the molecular z axis was considered to be θ = 90<sup>∘</sup> ± α, with α an adjustable tilt angle parameter taking into account the visual misalignment of the crystal (see Supplementary Section 1.1). The best agreement with the experimental spectrum was found for α = 8<sup>∘</sup> (Fig. 1). The simulation of the CW spectrum for the crystal sample reproduces both the eight main transitions and the formally forbidden ones that are visible in the lower field region (Fig. 1). The presence of such low intensity transitions between states with different mI is due to the non-negligible admixing of the ∣mS, mI > states at the applied magnetic field value (see Supplementary Section 2.2). The simulation of the EDFS spectrum is carried out by adding to Eq. (3) an additional super-hyperfine contribution given by the nitrogen atoms coordinate to V in the plane perpendicular to V=O (see Supplementary Section 2.2). 

### SUPPLEMENTARY INFORMATION 

Supplementary information on experimental methods, as well as additional data and discussion are reported in the on-line Supplementary Information file. 

### DATA AVAILABILITY 

The data reported in this work and in the Supplementary Information are available from the corresponding author upon reasonable request. 

Received: 11 March 2020; Accepted: 5 July 2020; 



10. Bradley, C. E. et al. A ten-qubit solid-state spin register with quantum memory up to one minute. Phys. Rev. X 9, 031045 (2019). 

11. Morton, J. J. & Bertet, P. Storing quantum information in spins and highsensitivity ESR. J. Magn. Reson. 287, 128–139 (2018). 

12. Afzelius, M., Sangouard, N., Johansson, G., Staudt, M. U. & Wilson, C. M. Proposal for a coherent quantum memory for propagating microwave photons. N. J. Phys. 15, 065008 (2013). 

13. Gaita-Ariño, A., Luis, F., Hill, S. & Coronado, E. Molecular spins for quantum computation. Nat. Chem. 11, 301–309 (2019). 

14. Troiani, F. & Affronte, M. Molecular spins for quantum information technologies. Chem. Soc. Rev. 40, 3119–3129 (2011). 

15. Bader, K., Winkler, M. & van Slageren, J. Tuning of molecular qubits: very long coherence and spin-lattice relaxation times. Chem. Commun. 52, 3623–3626 (2016). 

16. Bader, K. et al. Room temperature quantum coherence in a potential molecular qubit. Nat. Commun. 5, 5304 (2014). 

17. Warner, M. et al. Potential for spin-based information processing in a thin-film molecular semiconductor. Nature 503, 504–508 (2013). 

18. Shiddiq, M. et al. Enhancing coherence in molecular spin qubits via atomic clock transitions. Nature 531, 348–351 (2016). 

19. Giménez-Santamarina, S., Cardona-Serra, S., Clemente-Juan, J., M.Gaita-Ariño, A. & Coronado, E. Exploiting clock transitions for the chemical design of resilient molecular spin qubits. Chem. Sci. https://doi.org/10.1039/D0SC01187H (2020). 

20. Ferrando-Soria, J. et al. A modular design of molecular qubits to implement universal quantum gates. Nat. Commun. 7, 11377 (2016). 

21. Rabl, P. et al. Hybrid quantum processors: molecular ensembles as quantum memory for solid state circuits. Phys. Rev. Lett. 97, 033003 (2006). 

22. Thiele, S. et al. Electrically driven nuclear spin resonance in single-molecule magnets. Science 344, 1135–1138 (2014). 

23. Godfrin, C. et al. Generalized Ramsey interferometry explored with a single nuclear spin qudit. Npj Quantum Inf. 4, 53 (2018). 

24. Jenkins, M. et al. Coupling single-molecule magnets to quantum circuits. N. J. Phys. 15, 095007 (2013). 

25. Bonizzoni, C. et al. Coupling molecular spin centers to microwave planar resonators: towards integration of molecular qubits in quantum circuits. Dalton Trans. 45, 16596–16603 (2016). 

26. Urtizberea, A. et al. Vanadyl spin qubit 2D arrays and their integration on superconducting resonators. Mater. Horiz. 7, 885–897 (2020). 

27. Gimeno, I. et al. Enhanced molecular spin-photon coupling at superconducting nanoconstrictions. ACS Nano. https://doi.org/10.1021/acsnano.0c03167 (2020). 

28. Bonizzoni, C. et al. Coherent coupling between Vanadyl Phthalocyanine spin ensemble and microwave photons: towards integration of molecular spin qubits into quantum circuits. Sci. Rep. 7, 13096 (2017). 

29. Bonizzoni, C., Ghirri, A. & Affronte, M. Coherent coupling of molecular spins with microwave photons in planar superconducting resonators. Adv. Phys. X 3, 1435305 (2018). 

30. Ghirri, A. et al. Coherently coupling distinct spin ensembles through a high-Tc superconducting resonator. Phys. Rev. A 93, 063855 (2016). 

31. Mergenthaler, M. et al. Strong coupling of microwave photons to antiferromagnetic fluctuations in an organic magnet. Phys. Rev. Lett. 119, 147701 (2017). 

32. Yamabayashi, T. et al. Scaling up electronic spin qubits into a three-dimensional metal organic framework. J. Am. Chem. Soc. 140, 12090–12101 (2018). 

### REFERENCES 

1. Heshami, H. et al. Quantum memories: emerging applications and recent advances. J. Mod. Opt. 63, 2005–2028 (2016). 

2. Chen, C., Sun, W. K. C., Saha, S., Jaskula, J.-C. & Cappellaro, P. Protecting solid-state spins from a strongly coupled environment. N. J. Phys. 20, 063011 (2018). 

3. Metsch, M. H. et al. Initialization and readout of nuclear spins via a negatively charged silicon-vacancy center in diamond. Phys. Rev. Lett. 122, 190503 (2019). 

4. Morton, J. J. L. et al. Solid-state quantum memory using the 31P nuclear spin. Nature 455, 1085–1088 (2008). 

5. Abe, E. & Sasaki, K. Tutorial: magnetic resonance with nitrogen-vacancy centers in diamond microwave engineering, materials science, and magnetometry. J. Appl. Phys. 123, 161101 (2018). 

6. Siyushev, P. et al. Coherent properties of single rare-earth spin qubits. Nat. Commun. 5, 3895 (2014). 

7. Kurizki, G. et al. Quantum technologies with hybrid systems. PNAS 112, 3866–3873 (2015). 

8. Grezes, C. et al. Towards a spin-ensemble quantum memory for superconducting qubits. C. R. Phys. 17, 693–704 (2016). 

9. Probst, S., Rotzinger, H., Ustinov, A. V. & Bushev, P. A. Microwave multimode memory with an erbium spin ensemble. Phys. Rev. B 92, 014421 (2015). 

33. Atzori, M. et al. Room-temperature quantum coherence and rabi oscillations in vanadyl phthalocyanine: toward multifunctional molecular spin qubits. J. Am. Chem. Soc. 138, 2154–2157 (2016). 

34. Atzori, M. et al. Quantum coherence times enhancement in vanadium(IV)-based potential molecular qubits: the key role of the vanadyl moiety. J. Am. Chem. Soc. 138, 11234–11244 (2016). 

35. Zadrozny, J. M., Niklas, J., Poluektov, O. G. & Freedman, D. E. Multiple quantum coherences from hyperfine transitions in a vanadium(IV) complex. J. Am. Chem. Soc. 136, 15841–15844 (2014). 

36. Souza, M. A., lvarez, G. A. & Suter, D. Robust dynamical decoupling. Philos. Trans. R. Soc. A 370, 4748–4769 (2012). 

37. Uhrig, G. S. Keeping a quantum bit alive by optimized π-pulse sequences. Phys. Rev. Lett. 98, 100504 (2007). 

38. Pasini, S. & Uhrig, G. S. Optimized dynamical decoupling for power-law noise spectra. Phys. Rev. A 81, 012309 (2010). 

39. Soetbeer, J., Húlsmann, M., Godt, A., Polyhach, Y. & Jeschke, G. Dynamical decoupling of nitroxides in o-terphenyl: a study of temperature, deuteration and concentration effects. Phys. Chem. Chem. Phys. 20, 1615–1628 (2018). 

40. De Lange, G., Wang, Z. H., Ristè, D., Dobrovitski, V. V. & Hanson, R. Universal dynamical decoupling of a single solid-state spin from a spin bath. Science 330, 60–63 (2010). 

npj Quantum Information (2020) 68 

Published in partnership with The University of New South Wales 

C. Bonizzoni et al. 

7 

41. Witzel, W. M. & Sarma, S. D. Multiple-pulse coherence enhancement of solid state spin qubits. Phys. Rev. Lett. 98, 077601 (2007). 

42. Lim, H.-J., Welinski, S., Ferrier, A., Goldner, P. & Morton, J. J. L. Coherent spin dynamics of ytterbium ions in yttrium orthosilicate. Phys. Rev. B 97, 064409 (2018). 

43. Shukla, A. & Mahesh, T. S. Dynamical decoupling of spin-clusters using solid state NMR. Preprint at: https://arxiv.org/abs/1110.1473v1 (2011). 

44. Roy, S. S., Mahesh, T. S. & Agarwal, G. S. Storing entanglement of nuclear spins via Uhrig dynamical decoupling. Phys. Rev. A 83, 062326 (2011). 

45. Harbridge, J. R., Eaton, S. S. & Eaton, G. R. Comparison of electron spin relaxation times measured by Carr Purcell Meiboom Gill and two-pulse spin-echo sequences. J. Magn. Reson. 164, 44–53 (2003). 

46. Du, J. et al. Preserving electron spin coherence in solids by optimal dynamical decoupling. Nature 461, 1265 (2009). 

47. Wu, H. et al. Storage of multiple coherent microwave excitations in an electron spin ensemble. Phys. Rev. Lett. 105, 140503 (2010). 

48. Grezes, C. et al. Multimode storage and retrieval of microwave fields in a spin ensemble. Phys. Rev. X 4, 021049 (2014). 

49. Julsgaard, B., Grezes, C., Bertet, P. & Mølmer, K. Quantum memory for microwave photons in an inhomogeneously broadened spin ensemble. Phys. Rev. Lett. 110, 250503 (2013). 

50. Ghirri, A. et al. YBa2Cu3O7 microwave resonators for strong collective coupling with spin ensembles. Appl. Phys. Lett. 106, 184101 (2015). 

tion. Dr. Filippo Troiani (Istituto Nanoscienze CNR, section S3 of Modena) and Prof. Stefano Carretta (University of Parma, Italy) are acknowledged for useful discussions. We thank Prof. Oscar Moze (University of Modena and Reggio-Emilia) for the careful proof reading of our manuscript. This work was partially funded by the Italian Ministry of Education and Research (MIUR) through PRIN Project (contract no 2015HYFSRT), by the Air Force Office of Scientific Research grant (contract no FA2386-17-1-4040) and by the University of Modena and Reggio Emilia through the FAR Research Project 2018 Junior category (Decreto n. 161/18, Prot. no 61656/18 of april 3rd 2018 and Prot. 178151 of october 31st 2018). 

### AUTHOR CONTRIBUTIONS 

C.B. carried out all the measurements and data analysis and the design and the fabrication of the resonator. The home-made pulsed-microwave spectrometer, as well as all the pulse sequences used in this work has been designed, realized, tested, and implemented by C.B. F.S. prepared the crystal samples and part of the polycrystalline sample, M.At. prepared part the polycrystalline samples and contributed to their preliminary ESR and magnetic characterization. The EasySpin simulations of the spectra were carried out by F.S. and L.S. C.B., A.G. and M.Af. conceive the experiment. The manuscript was written by C.B., A.G., and M.Af. with contributions from all the authors. The manuscript has been revised by all authors before submission. 

51. Stoll, S. & Schweiger, A. EasySpin, a comprehensive software package for spectral simulation and analysis in EPR. J. Magn. Reson. 178, 42–55 (2006). 

52. Abragam, A. & Bleaney, B. Electron Paramagnetic Resonance of Transition Ions (Oxford Classics Texts in the Physical Sciences, 2012). 

53. Eaton, G. R. & Eaton, S. S. Multifrequency electron spin‐relaxation times. In Multifrequency Electron Paramagnetic Resonance, S. K. Misra (Ed.) (2011). https://doi. org/10.1002/9783527633531.ch17. 

54. Sigillito, A. J. et al. Fast, low-power manipulation of spin ensembles in superconducting microresonators. Appl. Phys. Lett. 104, 222407 (2014). 

55. Malissa, H., Schuster, D. I., Tyryshkin, A. M., Houck, A. A. & Lyon, S. A. Superconducting coplanar waveguide resonators for low temperature pulsed electron spin resonance spectroscopy. Rev. Sci. Instrum. 84, 025116 (2013). 

### COMPETING INTERESTS 

The authors declare no competing interests. 

### ADDITIONAL INFORMATION 

Supplementary information is available for this paper at https://doi.org/10.1038/ s41534-020-00296-9. 

Correspondence and requests for materials should be addressed to C.B. 

56. Hahn, E. L. Spin echoes. Phys. Rev. 80, 580–594 (1950). 

57. Yu, S. et al. Suppressing phase decoherence of a single atom qubit with CarrPurcell-Meiboom-Gill sequence. Opt. Express 21, 32130–32140 (2013). 

58. Pham, L. M. et al. Enhanced solid-state multispin metrology using dynamical decoupling. Phys. Rev. B 86, 045214 (2012). 

59. Yang, W. & Liu, R.-B. Universality of Uhrig dynamical decoupling for suppressing qubit pure dephasing and relaxation. Phys. Rev. Lett. 101, 180403 (2008). 

60. Yap, Y. S., Tabuchi, Y., Negoro, M., Kagawa, A. & Kitagawa, M. A Ku band pulsed electron paramagnetic resonance spectrometer using an arbitrary waveform generator for quantum control experiments at millikelvin temperatures. Rev. Sci. Instrum. 86, 063110 (2015). 

61. Narkowicz, R., Suter, D. & Niemeyer, I. Scaling of sensitivity and efficiency in planar microresonators for electron spin resonance. Rev. Sci. Instrum. 79, 084702 (2008). 

62. O’Sullivan, J. et al. Spin resonance linewidths of bismuth donors in silicon coupled to planar microresonators. Preprint at: https://arxiv.org/abs/2007.07600v1 (2020). 

63. Ranjan, V. et al. Multimode storage of quantum microwave fields in electron spins over 100 ms. Preprint at: https://arxiv.org/abs/2005.09275v1 (2020). 

### ACKNOWLEDGEMENTS 

We thank Prof. Mario Chiesa (University of Turin, Italy) and Dr. Enrico Salvadori (University of Turin, Italy) for useful discussion and complementary ESR characteriza- 

Reprints and permission information is available at http://www.nature.com/ reprints 

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons. org/licenses/by/4.0/. 

© The Author(s) 2020 

Published in partnership with The University of New South Wales 

npj Quantum Information (2020) 68 


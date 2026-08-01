

#### **Developing a Microwave Quantum Memory with Rare-Earth Doped Crystals** 

#### **Joseph Alexander** 

A thesis submitted for the degree of **Doctor of Philosophy** 

University College London Electronic & Electrical Engineering London Centre for Nanotechnology 

London, July 19, 2023 

_1_ 

I, Joseph Alexander, that the work presented in this thesis is my own. Where information has been derived from other sources, I confirm that this has been indicated in the thesis. 

London, July 19, 2023 Joseph Alexander 

_2_ 

#### **Developing a Microwave Quantum Memory with Rare-Earth Doped Crystals** 

###### Joseph Alexander 

###### **Abstract** 

Rare-earth doped crystals have attracted a significant amount of attention for use in quantum systems. Available, long-lived, optical and microwave transitions has lead to proposals for quantum transduction and quantum memories, both of which are important in building large scale quantum networks. Ensembles of rare-earth spins can be coupled to superconducting resonators, and high coupling strengths (with cooperativity > 1) readily achievable. While such systems have been constructed, a useful quantum memory which exploits highly coherent transitions has not yet been developed in the microwave domain. In this thesis we couple high-Q superconducting resonators to Yb doped YSO. The spin system of Yb:YSO is explored and the main causes of decoherence are outlined, these are found to be instantaneous diffusion and spectral diffusion. In the process of this, new techniques are developed to determine decoherence sources, where nuclear spins within the YSO crystal are found to limit coherence. 

Two different regimes are explored to increase the coherence time. Using optimal field orientations and high magnetic field magnitudes, the coherence time is extended to (6 _±_ 2) ms. While the zero field clock transition is used, along with isotopic purification, to reach the same time ((6 _±_ 1) ms). Using these techniques to increase coherence, the foundations for a microwave quantum memory with Yb:YSO are laid. Cooperativities _>_ 1 are measured for three different Yb spin systems, this allows for these spin systems to be used in memory protocols and reach unit efficiency. New pulse sequences using adiabatic fast passage are developed to provide control over the spin ensemble and for memory protocols. 

Finally, we use the knowledge from all of these studies to propose a system which would form the basis of an efficient, long-lived microwave quantum memory using FIB-milled Yb:YSO. 

### **Impact Statement** 

Quantum computing offers the potential to solve a variety of problems, from chemistry to security. There is one key sticking point with the current state of the art – scalability. The process for building a scalable quantum computer which can solve useful problems remains unclear. In this thesis we explore the use of rare-earth ions doped into crystals as a platform for a hybrid quantum system. The ensemble of electron spins coupled to a superconducting resonator forms the basis of a microwave quantum memory which can be integrated into superconducting quantum processors. This reduces the number of qubits needed to perform algorithms and opens opportunities for holographic quantum computing. New pulse sequences and memory protocols explored in this thesis allow for random access quantum memories. These will be a vital component of a large scale quantum computer and helps solve scalability issues. 

The spin physics and decoherence mechanisms of rare-earth doped crystals is extensively studied, this is not only useful for the wider academic community but also for microwave technologies involving rare-earth systems. These have applications in quantum transduction which is a crucial element in large scale quantum networks and a quantum internet. 

Aside from quantum computation, the work in this thesis is impactful in an ESR setting. New ESR techniques to measure decoherence using superconducting microresonators are constructed and extensive modelling and design of such resonators has applications in classical ESR, chemistry and biochemistry. 

### **Acknowledgements** 

This PhD would not have been remotely possible without the help of a wide range of people. I am immensely grateful for all the support you have given to get me through the past 4 years: 

_John Morton_ , thank you for taking me – and keeping me! – into the group. QSD is what it is today thanks to your guidance, motivation and (much needed) patience. I am not sure there are many supervisors who can hold such a breadth of academic knowledge while maintaining an active football career! 

_Paul Warburton_ , for being an excellent second supervisor, who through his great wit, guided me through all aspects of a PhD. 

_Phillipe Goldner_ , for growing and supplying the crystals used throughout my PhD and fruitful discussions both virtually and in-person. 

_Andrei Faraon_ , _Andrei Ruskuc_ , and the rest of the Caltech group, thank you for hosting me for an incredible 3 months. I learnt a lot from you all and returned with a great tan! 

_Gavin Dold_ , this work would not be possible without the hard work you put in during your PhD to couple resonators to rare-earths. Thanks for doing the hard bit and letting me carry on your work, I owe you the sourest of sour beers. 

_Oscar Kennedy_ , the person who taught me what a real scientist should be. Your constant enthusiasm, brilliant experiment plans, and all-round kindness set me in excellent stead for the business end of my PhD. Those daily zoom coffee ‘meetings’ certainly made covid working from home more bearable! 

_James O’Sullivan_ , for teaching me how to be an experimental researcher through a refined technique of ‘break it and see what happens’. Thank you for taking time out of your own PhD to help me fix all my stupid mistakes. 

_Mantas Šim˙enas_ , thank you for your immense knowledge of ESR, which I hope I have managed to take even a tiny portion. The countless discussions and advice certainly improved the quality and impact of the results of my PhD. 

_Christoph Zollitsch_ , the man who kept F10 running when know one else could! 

_5_ 

Thank you for turning a fresh new PhD student into a semi-functioning experimentalist. 

The future of the resonator group: _Paddy Hogan_ and _Ana Villanueva Ruiz de Temino_ , the group is in good hands! You both have many exciting projects coming, and you can now realise them as I’m not hogging all the fridge time! 

_James Williams_ , _Felix Donaldson_ , and _Ed Thomas_ , thank you for sharing the journey from MRes year to thesis writing. For the many tequilas which James paid for, the post football debriefs with Felix, and the unholy amount of coffee and obscure beers with Ed. You three kept me going through this whole process and will all go on to do incredible things. 

To the rest of the CDT cohort, there are far too many of you to name, but without all of you the PhD experience would’ve been a lot more painful. In true CDT fashion, our entire PhDs were extended! 

To past members of the group: _David Wise_ for bankrolling pub trips and listening to my endless list of problems while doing so. _Virginia Ciriano Tejel_ for being an awesome friend both in and outside the lab. Thank you for being a little bit of craziness mixed with a whole lot of kindness! _Jingyu Duan_ for being a constant in the lab and fellow ‘pret club’ member. _Sofia Patomäki_ for being my G02 buddy with-whom I could always count on a useful and insightful discussion. _Siddharth Dhomkar_ , _Michael Fogarty_ , _Simon Schaal_ , _Pierandrea Conti_ , _Gareth Jones_ , thank you for making QSD such a warm and hosipitible place for a new PhD student. 

To the rest of the current (and surrounding) group; _Saksham Mahajan_ , _Ravi Kumar_ , _Mathieu de Kruijf_ , _Frederic Schlattner_ , _Thomas Swift_ , _Nathan Johnson_ , _Constance Lainé_ , _David Ibberson_ , _Jacob Chittock-Wood_ , _Ross Leon_ , it was a pleasure working, playing football, and drinking with you all. 

To my friends, in particular _Feargal Crehan_ , _Dario Feddersen-Doyle_ , _Johnny McMichael_ , and _Isaac Stephens_ , thank you for putting up with me as a friend, and in return I gave you access to cheap drinks at the uni bar! 

Finally, to my family, _James_ , _Tom_ , _Emily_ , _Mum_ and _Dad_ for supporting me along the way – I promise this was the right decision and I’ll get a ‘real’ job soon! Thanks for being the best family ever. 

### **Contents** 

|**1**|**Intr**|**oduction**<br>**9**|
|---|---|---|
||1.1|Solid State Quantum Memories . . . . . . . . . . . . . . . . . . . .<br>14|
||1.2|Rare-Earth Ions . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>17|
||1.3|Research Goals . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>18|
|**2**|**Elec**|**tron Spin Resonance (ESR)**<br>**20**|
||2.1|ESR From the Ground Up<br>. . . . . . . . . . . . . . . . . . . . . .<br>21|
|||2.1.1<br>Continuous Wave ESR . . . . . . . . . . . . . . . . . . . .<br>23|
|||2.1.2<br>Pulsed ESR . . . . . . . . . . . . . . . . . . . . . . . . . .<br>24|
||2.2|Relaxation & Decoherence . . . . . . . . . . . . . . . . . . . . . .<br>25|
|||2.2.1<br>Relaxation<br>. . . . . . . . . . . . . . . . . . . . . . . . . .<br>27|
|||2.2.2<br>Decoherence . . . . . . . . . . . . . . . . . . . . . . . . .<br>28|
||2.3|Pulse Sequences . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>30|
|||2.3.1<br>Adiabatic Fast Passage . . . . . . . . . . . . . . . . . . . .<br>32|
|||2.3.2<br>ABBA Memory Protocol . . . . . . . . . . . . . . . . . . .<br>35|
||2.4|Spin Coupling . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>39|
|||2.4.1<br>Single Spin Coupling . . . . . . . . . . . . . . . . . . . . .<br>39|
|||2.4.2<br>Ensemble Spin Coupling . . . . . . . . . . . . . . . . . . .<br>41|
|||2.4.3<br>Purcell Regime . . . . . . . . . . . . . . . . . . . . . . . .<br>43|
||2.5|Yb:YSO Spin System . . . . . . . . . . . . . . . . . . . . . . . . .<br>43|
|**3**|**Sup**|**erconducting Resonators**<br>**47**|
||3.1|Impedance in Superconducting Circuits<br>. . . . . . . . . . . . . . .<br>48|
||3.2|Kinetic Inductance<br>. . . . . . . . . . . . . . . . . . . . . . . . . .<br>51|
||3.3|Properties of Superconducting Resonators . . . . . . . . . . . . . .<br>53|
||3.4|Fabrication of Superconducting Resonators<br>. . . . . . . . . . . . .<br>55|
|**4**|**Exp**|**erimental Methods**<br>**58**|
||4.1|Resonator Design . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>59|



|||_Contents_<br>_7_|
|---|---|---|
||4.1.1|Geometry . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>59|
||4.1.2|Simulation<br>. . . . . . . . . . . . . . . . . . . . . . . . . .<br>62|
||4.1.3|Characterisation<br>. . . . . . . . . . . . . . . . . . . . . . .<br>67|
|4.2|Cryost|ats<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>73|
||4.2.1|Closed-Cycle Cryostat . . . . . . . . . . . . . . . . . . . .<br>73|
||4.2.2|Dilution Refrigerator . . . . . . . . . . . . . . . . . . . . .<br>73|
|4.3|ESR S|etup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>77|
|**5**<br>**Dec**|**oherenc**|**e in Rare-Earth Doped Crystals**<br>**80**|
|5.1|Contin|uous Wave ESR . . . . . . . . . . . . . . . . . . . . . . . .<br>81|
|5.2|Pulsed|ESR . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>85|
||5.2.1|Spin Relaxation Time,_T_1 . . . . . . . . . . . . . . . . . . .<br>85|
||5.2.2|Spin Coherence Time,_T_2 . . . . . . . . . . . . . . . . . . .<br>88|
|5.3|Instan|taneous Diffusion . . . . . . . . . . . . . . . . . . . . . . . .<br>89|
|5.4|Spectr|al Diffusion . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>92|
||5.4.1|Temperature Dependence . . . . . . . . . . . . . . . . . . .<br>95|
||5.4.2|Stimulated Echo<br>. . . . . . . . . . . . . . . . . . . . . . . 101|
|5.5|Discus|sion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105|
|**6**<br>**Exte**|**nding**|**Coherence in Yb:YSO**<br>**107**|
|6.1|Reson|ator-Spin System . . . . . . . . . . . . . . . . . . . . . . . . 108|
|6.2|High-|Field Regime . . . . . . . . . . . . . . . . . . . . . . . . . . 110|
|6.3|Zero-F|ield . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116|
||6.3.1|ZEFOZ . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116|
||6.3.2|LoFOZ . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119|
|6.4|Isotop|ic Purifcation . . . . . . . . . . . . . . . . . . . . . . . . . . 121|
|6.5|Dyna|mical Decoupling . . . . . . . . . . . . . . . . . . . . . . . . 124|
||6.5.1|CPMG<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . 124|
|6.6|Discus|sion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126|
|**7**<br>**Tool**|**s for B**|**uilding a Quantum Memory**<br>**129**|
|7.1|Spin-R|esonator Coupling . . . . . . . . . . . . . . . . . . . . . . . 130|
|7.2|Angul|ar Dependence of Cooperativity . . . . . . . . . . . . . . . . 136|
|7.3|Adiab|atic Fast Passage . . . . . . . . . . . . . . . . . . . . . . . . 142|
||7.3.1|Control . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144|
||7.3.2|Echo Silencing . . . . . . . . . . . . . . . . . . . . . . . . 148|
|7.4|Propo|sal for FIB milled YSO Memory . . . . . . . . . . . . . . . . 152|
||7.4.1|Airplane Resonator . . . . . . . . . . . . . . . . . . . . . . 153|



_Contents_ 

_8_ 

|7.4.2<br>Modelling of_g_0 . . . . . . . . . . . .|. . . . . . . . . . . . 154|
|---|---|
|7.5<br>Discussion . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . 155|
|**8**<br>**Conclusion and Outlook**|**158**|
|**Bibliography**|**161**|



##### **Chapter 1** 

### **Introduction** 

_I need to know what the question is. Then, perhaps, I can be more engaged in the search for the answer._ 

||John Preskill|
|---|---|
|**Contents**||
|**1.1**|**Solid State Quantum Memories**<br>**. . . . . . . . . . . . . . . .**<br>**14**|
|**1.2**|**Rare-Earth Ions . . . . . . . . . . . . . . . . . . . . . . . . .**<br>**17**|
|**1.3**|**Research Goals . . . . . . . . . . . . . . . . . . . . . . . . . .**<br>**18**|



In recent years, quantum computing has transitioned from the university laboratory to an industrial setting. Fundamental physics questions have been answered and now mountain of engineering challenges can be tackled. With significant investment from governments, big tech companies and start-ups [1] the quantum computing industry is projected to reach global market value of over $42 billion by 2027 [2]; the initial question is – why? 

As Richard Feynman proposed in the 1980s, the most effective way to simulate quantum systems is to use a computer which itself is quantum [3]. Currently, the pharmaceutical industry devotes 15% of its revenue to research and development for new drug discoveries. These discoveries require the use of classical supercomputers and techniques such as density functional theory (DFT), molecular dynamics, and artificial intelligence to simulate the underlying chemical processes. However, these processes are quantum, and simulating them on a classical computer is both time and energy intensive. In fact, finding the exact solution for systems with more than just 30 electrons becomes intractable [4]. The hope is that a quantum computer could accelerate this process, enabling us to develop drugs more quickly and effectively. However, we cannot simply run a quantum computer like its classical 

_10_ 



<!-- Start of picture text -->
|0<br>|0 |1 |0 |1<br>|0 |1<br>|0 |1<br>|1<br>0<br>- - i<br>√2<br>√2<br>+<br>1 +i √2<br>√2<br>Bit Qubit<br><!-- End of picture text -->

**Figure 1.1:** Bloch sphere picture of quantum states. A bit occupies poles of a sphere whereas a qubit forms superpositions over a (Bloch) sphere. counterpart, as many intuitions we have about the classical world must be thrown away. 

Quantum information processing was formally constructed by David Deutsch [5] and showed that quantum computing could be constructed of quantum gates to perform universal computation. From this further milestones were reached with quantum error correction [6] and algorithms such as Grover’s search algorithm [7], the variational quantum eigensolver (VQE) used for chemical simulation [8], and Shor’s algorithm [9] for factoring. The latter arguably driving the most interest in quantum computing. A rather surprising result using the quantum Fourier transform (QFT) allows for factorisation in polynomial time, thus with a large scale quantum computer current encryption using RSA could be broken. 

The fundamental building block of a quantum computer is the quantum bit or _qubit_ . While the classical bit exists as two definite states – 0 or 1 – the qubit uses the phenomena of superposition to be in a quantum combination of 0 and 1. Qubits ability to be in _superposition_ and perform _entanglement_ allow for quantum computers to outperform classical computers in certain tasks [10]. A classical bit can be thought of as two points on opposite poles of a sphere (0 and 1) whereas a qubit (via superposition) is a vector which points to any region on the sphere (figure 1.1), this is the Bloch sphere and will be useful for visualising quantum processes. In a theoretical sense a qubit is simply a two-level system with eigenstates _|_ 0 _⟩_ and _|_ 1 _⟩_ , however there is no preferred method as to how a qubit is physically implemented. 

In 2000, DiVincenzo proposed a set of criteria which a quantum computer must satisfy for it to be useful in solving real-world problems [11]. The first five critera 

_11_ 

relate to building a quantum computer: 

1. A scalable physical system with well-characterized qubit 

2. 

3. Long relevant decoherence times 

4. A ‘universal’ set of quantum gates 

5. 

and in order to extend this to quantum communications and quantum networks the following are required: 

6. 

7. 

These form a good starting point to chose a technology on which to build a quantum computer. Several different platforms fulfill these criteria and are at varying stages of development, these include trapped ions [12–16], photonics [17– 20], quantum dots [21,22], neutral atoms [23–25], nuclear magnetic resonance [26, 27] and many more. However, here we shall focus on the technology which has seen the most success and is used to build the largest quantum computers up to now – superconducting quantum processors [28–31]. 

Building on the subject of circuit quantum electrodynamics (circuit-QED) [32], superconducting quantum computers are built with 2D planar superconducting circuits where superconducting qubits are interconnected. Although superconducting qubits come in many flavours, the basis for all of them is the Josephson junction [33]. In its simplest form, a Josephson junction is formed of two superconducting wires separated by a narrow non-superconducting region. This narrow region allows for current to tunnel with a corresponding phase shift. This phase shift gives rise to a non-linearity in the inductance of the junction allowing it to be used (along with a capacitor) to form a superconducting qubit (Cooper-pair box). In most designs, a pair of Josephson junctions are used in parallel to allow for frequency tunability of the qubit. This forms unequally spaced energy levels, the lowest two are used to form the qubit, known as an artificial atom [34]. The transmon qubit [29,35] is a variation of the Cooper-pair box which has a large Josephson energy (the energy required to tunnel through the junction) compared to its charging energy (the energy needed to add additional Cooper pairs to the superconducting island). This 

_12_ 

allows the transmon to be resilient to charge noise and results in coherence times nearing 100 µs [36,37]. A wide range of different superconducting qubits has been developed including fluxonium [38], quantronium [39] and gatemon [40] qubits. A comprehensive review of superconducting qubits can be found by Kjaergaard et.al [30]. 

Superconducting qubits fast high-fidelity gate times [28,41,42] and connectivity [43,44] has resulted in medium scale quantum computers built by Google [45], IBM [46] and Rigetti [47]. These systems have pulled the quantum computing industry into the first stage of quantum processing - the noisy-intermediate-scalequantum (NISQ) era [48]. In this stage, quantum computers are able to complete tasks which are not achievable by classical computers. This was highlighted with the achievement of quantum supremacy by Google AI [45] whereby a calculation performed on their quantum chip in 200 s would have taken the largest supercomputer 10,000 years. Further supremacy experiments involving boson sampling on a photonic quantum computer [49] confirm the beginning of a regime where quantum computers can solve problems which have previously been unsolvable. More recently, partitions of a 72 qubit chip, again by Google, shows that error correction codes are successful in reducing errors [50]. 

While great strides have been made in reaching NISQ era computers, almost all quantum computing platforms suffer from one key sticking point – scalability. It is somewhat ironic that it is the first of DiVincenzo’s criteria which has proved the most difficult to tackle. While Josephson junctions themselves are small (down to nm scale), the transmon qubits are comparatively large. This is due to the large capacitors which are needed to protect the qubit from charge noise and maintain a frequency in the 4-8 GHz range. The end result is Google’s 52 qubit processor being packed onto a 10 x 10 mm chip (highlighted in figure 1.2). For Shor’s algorithm, where an estimated 13 million qubits are needed [51], this would require the same chip to be approximately 5 x 5 m – quite the challenge to fit into a dilution refrigerator! The scalability issues also manifest themselves in the form of the control electronics, each qubit requires its own flux bias coax line, and its own microwave control line. Further to this the couplers (all 88 of them) between qubits also require flux bias lines. In addition, 9 readout circuits (comprised of 4 coax lines) are required. This brings the total number of coax cables within the dilution refrigerator to 232! This would means to build a million qubit processor, several million coax lines would be needed to control all the qubits. 

Hybrid quantum systems [52] offer one path to solving the scalability problem. Utilising the long coherence times of certain electron spins in solids [53,54] along 

_13_ 





<!-- Start of picture text -->
52 Qubit Chip 13 Million Qubit Chip PhD Student<br><!-- End of picture text -->

**Figure 1.2:** Relative scale of the scalability problem. Current superconducting chips with 52 qubits have a footprint of 10 x 10 mm, scaling this to 13 million qubits results in a 5 x 5 m chip. 

with the fast gate times of superconducting qubits allows for a hybrid quantum processor to be envisioned. Classical computers are themselves hybrid systems, they are comprised of different technologies to perform different tasks (CPU for processing, solid sate drive for memory, flash memory for random access memory (RAM), GPU for graphical compute etc.), however today’s superconducting quantum computers use superconducting circuits to perform all the tasks. 

A quantum version of RAM could exploit the long coherence of electron spins [55]. In this system quantum processing unit (QPU) broadly looks the same as conventional superconducting chips. The addition of memory cells are placed at each qubit allowing quantum states to be stored and retrieved. This frees up the qubits to run other processes before retrieving the previous state at a later time – analogous to classical RAM. These memory cells are regions with implanted spins leaving the surface of the chip free for further superconducting circuitry. A quantum bus is needed to transfer the information from the qubit to the memory, this is in the form of a superconducting resonator. Figure 1.3 provides a schematic of this architecture. By freeing up otherwise idle qubits, this can reduce the number of qubits needed for certain operations. A reduction of approximately 3 orders of magnitude in the number of qubits are needed to run Shor’s algorithm given access to a sufficiently large quantum memory [56]. 

In addition to this, optically active spin systems have been proposed for microwave to optical transduction of quantum states [57, 58]. Memory cells which can perform transduction would be a vital resource in building large scale quantum networks. This would allow multiple chips in different dilution refrigerators and different locations to be entangled together thereby increasing the effective size of the quantum processor. It is the optical properties of rare-earth ions which have accelerated research into their use in hybrid quantum systems [58–60], however 

_1.1. Solid State Quantum Memories_ 

_14_ 



<!-- Start of picture text -->
Qubit<br>Coupler<br>Memory<br><!-- End of picture text -->

**Figure 1.3:** Architecture for potential hybrid superconducting-spin quantum computer. The primary superconducting elements (qubits and couplers) remain the same as in current quantum processors with the addition of memory cells into which qubits can store and retrieve quantum states. 

in order to be used in transduction their microwave properties and interface with superconducting circuits (GHz regime) is important [61–65]. 

##### **1.1 Solid State Quantum Memories** 

Quantum memories are an important component of quantum repeaters and quantum networks [57]. There are several proposed systems for implementing a quantum memory, these vary from atomic vapours [66–70] to Rydberg atoms [71–73]. There are several reviews of many of these implementations [74,75], here we shall only discuss quantum memories in the context of spin ensembles in solid state systems. Optical quantum memories have seen the most attention and form the bulk of quantum memory research [76]. The majority of memory experiments fall into two main categories – controlled reversible inhomogeneous broadening (CRIB) [77] and atomic frequency comb (AFC) memories [78]. Devices involving nanophotonic waveguides have been used to create the state of the art quantum memory experiments. Using Yb ions embedded into a yttrium orthovanadate (YVO4) waveguide, single photons were stored and retrieved using AFC protocols [79]. Further to this, coupling the cavity to a microwave waveguide (figure 1.4) allows for on-chip microwave to optical transduction [80]. These results show that quantum memories can be contained at the micron scale and protocols can be performed on-chip - an important step in building large scale networks. 

While optical memories play a vital role in quantum networks, interfacing them with superconducting processors is challenging. Given the frequency disparity between the two domains, transferring information between a superconducting qubit (GHz) to an optical memory (THz) requires transduction, this places an extra step in the read and write stage which adds noise and a loss in fidelity. It is therefore im- 

_15_ 

_1.1. Solid State Quantum Memories_ 



**Figure 1.4:** Image of the nanophotonic waveguide used in [80], the scale bar corresponds to 10 µm. The gold coplanar waveguide allows for microwaves to be coupled into the device which is in turn coupled to optical lines via the cavity couplers formed of a 45<sup>_◦_</sup> cut at the end of the waveguide. 

portant that memories which interface directly with superconducting qubits operate in the microwave regime. 

The simplest approach is to use superconducting devices as memories in the form of superconducting resonators [81,82]. This allows for ease of fabrication and strong coupling between the resonators and the qubits [83], however the number of modes accessible depends on the number of resonators [84], this makes building memories with large storage capacity difficult. Using an ensemble of paramagnetic spins is a solution to this where, in principle, each spin offers an independent degree of freedom to store quantum states. Superconducting qubits can be directly interfaced with spin ensembles [85,86] however complications involving applying gates to the qubit while storing states as well as the effect on the qubit coherence means coupling the spins via a superconducting bus is preferred. 

Pioneering work by C. Grezes and Y. Kubo showed that a hybrid microwave quantum memory could be realised [55, 87–91]. By coupling an ensemble of NV centres in diamond to a flux tunable superconducting resonator and in turn a superconducting qubit (shown in figure 1.5), information could be stored in the memory and retrieved 100 µs later. While these experiments solved important challenges in terms of coupling, there remained several issues which need to be resolved to form a _useful_ quantum memory. The first is the low efficiency (0.02%) and short storage time (35 µs) of the memory. To improve these, high coupling strengths between the resonator and the spins, as well as longer spin coherence are needed. Many systems have shown high coupling (cooperativity > 1) between superconducting resonators 

_16_ 

###### _1.1. Solid State Quantum Memories_ 



**Figure 1.5:** Device used by Kubo et al. to transfer states from a superconducting qubit (Q) to NV centres in diamond via a frequency tunable resonator (B). The resonator is tuned via a flux line (F) while the qubit is coupled to a readout line (R). Taken from [90]. 

and spin ensembles [65, 87, 92–95], while the use of atomic clock transitions in bismuth donors in silicon allowed for the storage and retrieval of states for over 100 ms [96]. The second limitation, and one in which all Hahn echo memories suffer from, is the issue of superradiance. 

It has been shown theoretically that the Hahn echo is not a good quantum memory [97]. In the Hahn (two-pulse) echo sequence the spin ensemble emits from the excited state, this emission is nosier due to coherent collective spontaneous emission. For this reason memory protocols have been formulated to allow for emission from the ground state. The retrieval of silenced echo (ROSE) protocol [98, 99] does this by applying a further refocusing pulse at the end of the Hahn echo sequence. As the first refocusing pulse will result in emission (echo) this must be suppressed by detuning the spins from the resonator. This echo silencing can be achieved through a variety of techniques including the use of magnetic field gradients [100,101], Stark shifts [79,102,103], frequency tunable resonators [104] or chirped pulses [105]. 

J. O’Sullivan, O. Kennedy et al. showed the ROSE protocol could be extended further to achieve random access [106]. In this experiment four distinct microwave pulses were stored and retrieved from a bismuth spin ensemble in an arbitrary order (the protocol is outlined in detail in chapter 2). This provides an important step to realising a random access quantum memory for superconducting qubit architectures. Simply altering the encoding and refocusing pulses allows for multi-mode storage and random access, this makes compatibility with superconducting qubits much easier (compared with field gradients). The main limitations of the experiment were the low cooperativity (C _≈_ 0.06) and comparatively short coherence time (2 ms). 

Rare-earth doped crystals offer a solution to both these limitations with high 

_1.2. Rare-Earth Ions_ 

_17_ 

cooperativities [94, 95] and long coherence times [64, 65, 107] measured. In addition, there is the added bonus of available optical transitions [79,108] which means they are a strong candidate for a quantum memory. 

##### **1.2 Rare-Earth Ions** 

Despite their name, rare-earth elements are not actually that rare, they are comprised of the lanthanides with the addition of scandium and yttrium. Rare-earth ions have attracted much attention for use in quantum systems due to their optical properties. They exhibit some of the narrowest optical linewidths in solids [109] facilitating use in laser technologies [110]. These properties also translate to forming good quantum systems. The partially filled 4f shell provides optical (and microwave) transitions which are protected from the environment by the 5s and 5p sub-shells resulting in long optical coherence times [111–113]. Rare-earth have been used as single-spin qubits [114–117], quantum transducers [58,60,80] and quantum memories [79,118–122]. 

Not all rare-earth elements have accessible electron spin resonance (ESR) transitions from which microwave properties can be exploited. The Kramer ions (Ce, Nd, Sm, Gd, Dy, Er & Yb) form a charge state of 3+ and with total spin of halfinteger they become ESR active. The 3+ charge state also allows Kramer ions to be easily integrated into a variety of host crystals. Common crystals for hosting Kramer ions include YVO [114], yttrium aluminium garnet (YAG, Y3Al5O12) [116] and calcium tungstate (CaWO4) [64]. Here we will focus on yttrium orthosilicate (YSO, Y2SiO5) which has been the most popular crystal for quantum applications [123]. 

YSO has properties making it suitable for quantum technologies, its high optical depth [123] means small quantities can be used to perform optics experiments, while low dielectric losses allow for high Q resonators to be fabricated on the surface [95]. Narrow homogeneous linewidths are measured in YSO even with the 100% abundant<sup>89</sup> Y nuclear spin, this is due to its relatively low nuclear magnetic moment. 

Grown via the Czochralski method, the YSO crystal belongs to the monoclinic C2/c space group and is described by its crystal axis (D1, D2, b). The unit cell of YSO contains two Y sites each of which consists of two degenerate subsites, although the subsites’ degeneracy is lifted once a magnetic field is applied along the b axis. During crystal growth Kramer ions substitute Y<sup>3+</sup> into one of the two sites. Nd<sup>3+</sup> preferentially substitute into only one of these sites (due to its large ionic radius), while Yb<sup>3+</sup> substitutes into each site equally. 

_1.3. Research Goals_ 

_18_ 

The bulk of the experiments in this thesis use ytterbium (Yb) doped YSO. Ytterbium is the only Kramer ion to have nuclear spin 1/2 making the spin system the simplest. The hyperfine interaction results in zero field splitting of the energy levels. Crucially, the transitions between these levels are insensitive to magnetic fields. These transitions are referred to as zero first order Zeeman (ZEFOZ) transitions and are analogous to clock transitions. These transitions are present in several of the rare-earth ions, with an NMR ZEFOZ transition in Eu used to achieve coherence times of over 6 hours [124], the longest coherence time measured in any solid state system. The zero field ZEFOZ transition in Yb has been used to similtaneously extend coherence in the optical and microwave domains [108] with a coherence time ( _T_ 2) of over 1 ms in the microwave regime. The ZEFOZ transitions of Yb:YSO have frequencies which can be exploited using traditional ESR apparatus and the transition at 2 _._ 370 GHz can be integrated with superconducting circuits and qubits. 

##### **1.3 Research Goals** 

In this thesis we explore the use of rare-earth doped crystals as a microwave quantum memory. The basis for this is the coupling of superconducting resonators to rare-earth spins in YSO and the subsequent application of high-sensitivity ESR to measure spin properties. The results of the thesis are broken into three main parts, each progressing down the path towards a useful quantum memory. They are as follows: 

1. **Decoherence in rare-earth doped crystals** – In order to build a long-lived quantum memory we must first understand the spin system and the electron spin decoherence mechanisms at play within the system. The spin dynamics of the system are explored with mechanisms such as instantaneous diffusion and spectral diffusion identified as leading causes of decoherence. 

2. **Extending coherence in Yb:YSO** – Given our understanding of the decoherence mechanisms within the Yb:YSO system several ways of increasing the _T_ 2 time are shown. This includes utilising high magnetic fields and optimal field orientations, ZEFOZ points, isotopic purification, and dynamical decoupling. In this chapter a long coherence time of 6 ms is measured and reinforces the suitability of Yb:YSO for quantum memories. 

3. **Tools for building a quantum memory** – Using the long coherence measured in the previous chapters the Yb:YSO system can be adapted to be a _useful_ quantum memory. This involves achieving high coupling strengths 

_1.3. Research Goals_ 

_19_ 

between the spin ensemble and the superconducting resonator, exotic pulse sequences for optimal quantum control, and spatially confining spins to increase efficiency. At the end of this chapter we provide an outline on how to build the optimal microwave quantum memory with Yb:YSO. 

We begin by laying out the groundwork which is needed to perform the measurements in the final chapters. Firstly, we introduce electron spin resonance, building up from the underlying spin physics to formulating quantum memory protocol and coupling spin to resonators. The theory behind superconducting resonators is then outlined including the fabrication processes. Before the results chapters the experimental techniques used to perform the measurements are discussed including an outline of the experimental setup. These chapters form the basis for the subsequent results chapters where a microwave quantum memory based on Yb:YSO is developed. 

##### **Chapter 2** 

### **Electron Spin Resonance (ESR)** 

_The miracle is not that electrons behave oddly. The miracle is that when you take 10_<sup>_27_</sup> _electrons they behave like cheese._ 

Allan Adams 

###### **Contents** 

|**2.1**|**ESR F**|**rom the Ground Up**<br>**. . . . . . . . . . . . . . . . . . .**<br>**21**|
|---|---|---|
||2.1.1|Continuous Wave ESR . . . . . . . . . . . . . . . . . .<br>23|
||2.1.2|Pulsed ESR . . . . . . . . . . . . . . . . . . . . . . . .<br>24|
|**2.2**|**Relax**|**ation & Decoherence**<br>**. . . . . . . . . . . . . . . . . . .**<br>**25**|
||2.2.1|Relaxation<br>. . . . . . . . . . . . . . . . . . . . . . . .<br>27|
||2.2.2|Decoherence . . . . . . . . . . . . . . . . . . . . . . .<br>28|
|**2.3**|**Pulse**|**Sequences . . . . . . . . . . . . . . . . . . . . . . . . .**<br>**30**|
||2.3.1|Adiabatic Fast Passage . . . . . . . . . . . . . . . . . .<br>32|
||2.3.2|ABBA Memory Protocol . . . . . . . . . . . . . . . . .<br>35|
|**2.4**|**Spin C**|**oupling**<br>**. . . . . . . . . . . . . . . . . . . . . . . . . .**<br>**39**|
||2.4.1|Single Spin Coupling . . . . . . . . . . . . . . . . . . .<br>39|
||2.4.2|Ensemble Spin Coupling . . . . . . . . . . . . . . . . .<br>41|
||2.4.3|Purcell Regime . . . . . . . . . . . . . . . . . . . . . .<br>43|
|**2.5**|**Yb:Y**|**SO Spin System . . . . . . . . . . . . . . . . . . . . . .**<br>**43**|



Electron spin resonance (ESR), or electron paramagnetic resonance (EPR)<sup>*</sup> in 

> *EPR often refers to the Einstein–Podolsky–Rosen paradox (EPR paradox) in physics, hence the use of ’ESR’. 

_2.1. ESR From the Ground Up_ 

_21_ 

chemistry, is a technique used to study the properties of paramagnetic materials. Developed simultaneously by Yevgeny Zavoisky in Kazan [125] and Brebis Bleaney in Oxford [126], ESR has become a crucial tool in understanding biological, chemical and spin-active physics systems. More recently, ESR techniques are utilised to manipulate spin qubits in quantum computing architectures. 

In this chapter the general principles of ESR are outlined, we will relate this to decoherence in bulk spin systems and explore techniques used to increase spin coherence. 

##### **2.1 ESR From the Ground Up** 

Electrons have an intrinsic angular momentum. As quantum objects, this angular momentum is quantised in terms of the spin quantum number ( _S_ ). The Stern–Gerlach experiment [127] not only showed the quantisation of spin, it also revealed the non-commutative nature of the spin operators resulting in the fact that only one component of the spin vector is well defined. In short, measuring _S_<sup>ˆ</sup> _x_ on an electron measured to be in the _Sz_ = +1 _/_ 2 state results in the electron ‘losing’ its _z_ information as the _Sz_ quantum number is no longer well defined. 

A particle with an angular momentum and charge has a magnetic moment, this means an electron has a magnetic moment given by: 



where _µ_ B is the Bohr magneton and _g_ is the electron g-factor. The g-factor is one of the most precisely measured quantities in physics; it it know to 12 decimal places (-2.00231930436256(35)) [128] and remains in agreement with quantum electrodynamics. A dipole within a magnetic field results in energy levels of the spin are described by the Hamiltonian: 



which has eigenvalues: 



This indicates the breaking of the degeneracy of energy levels due to an applied magnetic field - this is the Zeeman effect. The spin dynamics are altered in the presence of a nucleus. This adds two further terms to the Hamiltonian, one which accounts for the nuclear Zeeman effect and one which describes the interaction 

_2.1. ESR From the Ground Up_ 

_22_ 



<!-- Start of picture text -->
E<br>S = 1/2 I = 1/2<br>Free Electron Zeeman Hyperfine<br>B<br><!-- End of picture text -->

**Figure 2.1:** The energy level structure of an electron when placed into a magnetic field and coupled to a nuclear spin with _I_ = 1 _/_ 2 in the weak hyperfine regime. 

between the electron and nuclear spin ( **I**<sup>**ˆ**</sup> ), the hyperfine interaction. 



_<u>eh</u>_ ¯ g _N_ is the nuclear g-factor and _µN_ = 2 _mp_<sup>where</sup><sup>_e_is the elementary charge and</sup> _mp_ is the proton mass. A is the hyperfine constant which governs the strength of electron-nucleus interaction. Applying **_B_** along the _z_ axis (as is typical in ESR) results in eigenvalues: 



For many spin systems inside solid state hosts the electron (nuclear) g-factor and hyperfine constant are replaced by tensors which accounts for the anisotropicity which may be present in the crystal. This means the final Hamiltonian is written as: 



the nuclear Zeeman term ( _µN_ **B**<sup>_T_</sup> **gNI**<sup>**ˆ**</sup> ) is often ignored as it is much weaker than the other terms. 

In the case of a _S_ = 1 _/_ 2, _I_ = 1 _/_ 2 system, this results in a structure like that in . figure 2.1<sup>†</sup> 

> †This is essentially the structure of 171Yb which has _S_ = 1 _/_ 2 and _I_ = 1 _/_ 2. 

_2.1. ESR From the Ground Up_ 

_23_ 

###### **2.1.1 Continuous Wave ESR** 

Continuous wave (CW) ESR is the simplest approach to ESR, microwaves are continually applied to an electronic transition and measured using a high-Q cavity. The spin system is placed inside a cavity with some frequency bandwidth. Microwaves with a defined frequency are sent into the cavity and the response of the cavity is measured. When the frequency of the applied microwaves is resonant with the spin transition, electrons are raised to the excited state. This is observed as a loss mechanism in the cavity and its quality factor decreases, this is outlined schematically in figure 2.2. 



<!-- Start of picture text -->
h f  = gμB B0<br>B<br>Energy<br>Cavity<br>Linewidth<br>Quality Factor<br><!-- End of picture text -->

**Figure 2.2:** General principle of CW ESR. microwaves with some frequency ( _f_ ) are sent to the cavity. As the field ( _B_ 0) is increased the spins become resonant with the microwaves and are elevated to the excited state, this is perceived as a loss mechanism for the cavity so its effective linewidth increases while its quality factor decreases. 

In systems where there is high coupling between the cavity and the spins the two systems hybridise. The spins and the cavity are no longer separate systems and the eigenstates are states of both the spins and cavity. This causes the measured frequency to shift towards the spin line. 

be obtained quickly. It is therefore useful as a technique to initially probe the spin landscape, however to understand the structure and dynamics of the system pulsed 

_2.1. ESR From the Ground Up_ 

_24_ 

ESR must be used. 

###### **2.1.2 Pulsed ESR** 

Pulsed ESR is where the real power of ESR resides. It allows for the spin dynamics to be explored and utilised, and is crucial in spin-based quantum hardware. Applying a magnetic field causes the spin magnetic moment to precess. It does with angular frequency _ω_ L = _−γB_ , this is the Larmor frequency. _γ_ is the gyromagnetic ratio and is related to the g-factor via _γ_ =<sup>_<u>gµ</u>_</sup> _h_ ¯<sup><u>B</u>.It is conventional to work in a frame</sup> which is rotating at the Larmor frequency, so the spin appears static on the Bloch sphere, when only a static external field is applied. 

In order to control to spin on the Bloch sphere a second magnetic field ( _B_ 1) is applied. This _B_ 1 field is an oscillating magnetic field resonant with the spin transition, this allows for spins to be excited. Additionally working in a frame oscillating with the _B_ 1 field results in a magnetic dipole which precesses around _B_ 1. For a spin moment starting pointed in the + _z_ direction on the Bloch sphere, the moment will precess around _B_ 1 moving through the equator and past _−z_ before returning to the + _z_ pole. This is equivalent to the spin oscillating between the ground and excited state of a spin transition. By controlling the time for which the _B_ 1 field is applied the final state of the spin can be controlled. This allows for arbitrary rotations of the spin. The frequency, which the spin precesses around _B_ 1, and thus the frequency at which the state oscillates from _|_ 0 _⟩_ to _|_ 1 _⟩_ is called the Rabi frequency. To perform a defined rotation, _θ_ , around the Bloch sphere, the _B_ 1 field is pulsed for time _t_ such that: 



The Rabi frequency can be related to the _B_ 1 strength and the g-factor giving: 



So far we have only considered a single spin, however in ESR, ensembles of electron spins are used. Collection of spin moments combine to form a magnetisation vector, **M** . This magnetisation vector is rotated around the Bloch sphere in the same manner as an individual moment, however due to imperfections in the spin environment each spin within the ensemble has a slightly different g-factor. This results in an inhomogeneous broadening of the Larmor frequency and means different spins in the ensemble precess around _B_ 0 at different rates. This is observed via free-induction decay (FID). A<sup>_<u>π</u>_</sup> 2<sup>pulseisappliedtothespinensemblewhich</sup> 

_25_ 

_2.2. Relaxation & Decoherence_ 



<!-- Start of picture text -->
|0 |0<br>ωL ωL<br>ω<br>R<br>|1 |1<br>a) b)<br>B B<br>0 0<br>μ μ<br>B<br>1<br><!-- End of picture text -->

**Figure 2.3:** a) A static field ( _B_ 0) causes the spin magnetic moment ( _µ_ ) to precess with Larmor frequency, _ω_ L. b) An oscillating field (resonant with the spin transition frequency) is applied perpendicular to _B_ 0, _µ_ then precesses around the _B_ 1 vector allowing for arbitrary rotations on the Bloch sphere. 

projects the magnetisation vector onto the equator of the Bloch sphere. Given the convention in measuring along the _x_ direction in ESR, this can be measured by a large signal as the spins are rotated onto the _x_ axis. Due to the variation in Larmor frequencies, each spin precesses at a different rate, in turn reducing the magnitude of the magnetisation vector in a process called dephasing. This is FID, and is measured as an exponential decrease in signal. The characteristic time over which FID occurs is _T_<sup>_∗_</sup> 2<sup>.</sup> 

While it may seem as if dephasing is a major problem for a spin signal to be retrieved, a technique called a Hahn echo can be used to rephase the magnetisation vector. Developed in 1950 for NMR applications [129], the Hahn echo is the backbone of pulsed ESR. The Hahn echo sequence begins with FID, a<sup>_<u>π</u>_</sup> 2<sup>pulse projects</sup> **M** onto the equator of the Bloch sphere. The spins then dephase resulting in FID. A _π_ pulse is subsequently applied some time _τ_ later to the spins. This flips them in the plane of the Bloch sphere and inverts the direction of the spin precession. The phase accumulation of each spin during the dephasing period is reversed and each of their moments come together to reform the magnetisation vector, this is called rephasing. As rephasing occurs the magnitude of **M** increases resulting in a measured signal - a Hahn echo. The sequence is outlined in figure 2.4. 

##### **2.2 Relaxation & Decoherence** 

Quantum states are fragile, they must be isolated in order to preserve their state. However, in order to measure and control the state we must expose the quantum 

_26_ 

_2.2. Relaxation & Decoherence_ 



<!-- Start of picture text -->
|0 |0 |0 |0<br>π π<br>2<br>|1 |1 |1 |1<br>Dephasing Rephasing Echo<br>FID π Echo<br>π<br>2<br>τ τ<br><!-- End of picture text -->

**Figure 2.4:** The Hahn echo sequence. The magnetisation vector, **M** (green), begins in the ground state. It is projected onto the equator of the Bloch sphere with a<sup>_<u>π</u>_</sup> 2<sup>pulse</sup> (red). Dephasing occurs where spins precess around _B_ 0 with different rates, this is measured as FID after the the initial pulse. A _π_ pulse is applied _τ_ later, this inverts the spin ensemble in the x-y plane and allows for rephasing. A further _τ_ later the spin moments recombine and an echo is formed. 

information to the environment. By doing so we open up the opportunity for the state to ’lose’ its quantumness. In the context of ESR, there are two phenomena which the limit time for which a spin can be kept in a quantum state. The first, relaxation, is a semi-classical process in which the spin relaxes back to the ground state. This occurs with a characteristic time _T_ 1 and can be extended by operating at cryogenic temperatures. The second phenomena is called decoherence. When decoherence occurs, the phase information associated with a quantum state becomes irrecoverable and any information which was know about the sate is no longer accessible, the quantum state moves from a pure state to the maximally mixed state. Decoherence is an important phenomena in all quantum systems as it dictates the timescales over which quantum experiments and processes can take place. At its heart decoherence is not well understood, and it is believed that understanding the fundamental properties of decoherence could provide insights into the measurement problem<sup>‡</sup> . 

> ‡Actually, the view that decoherence arises from a quantum object becoming entangled with the environment forms the basis of the argument for the many-worlds interpretation - but lets not go there! 

_2.2. Relaxation & Decoherence_ 

_27_ 

###### **2.2.1 Relaxation** 

Relaxation, or more specifically longitudinal relaxation, is the process by which an excited state relaxes back to the ground state. Over a characteristic timescale, _T_ 1, longitudinal relaxation occurs via the absorption of one or two phonons. Depending on the temperature scale of the system, different processes dominate the relaxation, at higher temperatures these are the two-phonon mechanisms; the Raman and the Orbach processes. 

The Raman process occurs at higher temperatures, at these temperatures there is an abundance of phonons and so relaxation is more efficient via two-phonon processes. In the Raman process a high energy phonon is absorbed which promotes the spin to a higher _virtual_ level. The spin then relaxes to a lower energy state, emitting the second phonon in the process. For spin 1 _/_ 2 systems (such as rare-earth Kramer ions), this process scales as _R_ ∝ _T_<sup>9§</sup> . In situations where a _real_ energy level is available the efficiency of the two-phonon process is increased. This is the Orbach process which scales as _R_ ∝ exp � _− T_<sup><u>1</u></sup> �. 

At lower temperatures there are far fewer phonons within the crystal, and the phonons present have much lower frequency. The single-phonon direct process is dominant in this regime, in this mechanism a phonon resonant with the spin is <u>1</u> absorbed or emitted. This process is ∝ coth � _T_ �. 

Putting these three processes together an equation for the spin-lattice relaxation (SLR) rate of a spin 1 _/_ 2 system can be formulated [130–132]: 



where _αD_ ( _R,O_ ) and ∆ _O_ are constants which are dependent on the spin system. All of these processes are temperature dependent and can be suppressed by using cryogenic temperatures as shown by the plot in figure 2.5. In the sub-Kelvin regime this allows for _T_ 1 to reach several minutes or hours. 

There is one more process which can result in the relaxation of a spin. A dipolar interaction between nearby spins allows for a process known as cross-relaxation (or flip-flops). This occurs between two spins which have the same energy splitting, ∆ _E_ , where one spin is excited and the other is in the ground state. The dipolar interaction causes an exchange of magnetisation from one spin to another presenting itself as the relaxation of the measured spin. This process is dependent on the concentration of spins (as this dictates the average separation) and the relaxation rate can be modelled as [111,132]: 

- §As opposed to _T_ 7 for non-Kramer ions. 

_2.2. Relaxation & Decoherence_ 

_28_ 



<!-- Start of picture text -->
5<br>Raman<br>Orbach<br>4<br>Direct<br>3<br>2<br>1<br>0<br>0 1 2 3 4<br>Temperature (K)<br>)<br>-1<br>Rate (s<br><!-- End of picture text -->

**Figure 2.5:** Temperature dependence of the spin-lattice relaxation processes. The two phonon processes are suppressed at milliKelvin temperatures. Typical values taken from [133]. 



where _n_ is the spin concentration, Γ _s_ is the inhomogeneous linewidth, and _αFF_ is a constant to be determined. 

###### **2.2.2 Decoherence** 

Relaxation results in the spin returning to its ground state, thereby losing the phase information associated with its quantum state. Relaxation requires a transfer of energy away from the measured spin, however other processes can take place which do not require energy exchange. Decoherence, or transverse relaxation, occurs via interactions with the environment that result in the loss of coherence of the measured spin. Environmental spin-spin interactions result in fluctuating magnetic fields in the environment, these impose a homogeneous linewidth on the spin and cause decoherence over a characteristic time, _T_ 2. 

The _T_ 2 time is an important quantity in quantum information processing; it dictates the timescales over which the quantum phase information can be maintained. In spin systems at milliKelvin temperatures, _T_ 2 _≪ T_ 1 meaning it is the parameter which limits the storage time of a memory or the processing time of a qubit. 

In ESR, decoherence is typically due to spin-spin interactions in the environment. These can either directly involve the central spin (instantaneous diffusion) or environmental spin flip-flops indirectly decohere the central spin (spectral diffu- 

_2.2. Relaxation & Decoherence_ 

_29_ 

sion). 

Spectral diffusion is a decoherence mechanism which is present in the majority of ESR experiments. Longitudinal relaxation processes within environmental spin ensembles (B) results in changes in local magnetic fields at the position of the measured spin (A). The change in local field results in a phase shift of the A spin meaning it is not refocused via a two-pulse echo. 

Spectral diffusion is modelled by two important parameters; the spectral diffusion rate, _R_ , and the spectral diffusion linewidth, ΓSD. At milliKelvin temperatures, direct flip-flops between spins is the main relaxation process. This occurs within the environmental spins via equation 2.10. Given a flip-flop in the environment, the local changes in magnetic field imprint a spectral diffusion linewidth onto the A spin. This can be approximated as [111]: 



where _n_ is the density of B spins, and _gA_ and _gB_ are the g factors of the A and B ensembles. Together these two quantities combine to form a decoherence rate [111,134]: 



where Γ0 is a residual decoherence rate in the absence of spectral diffusion. 

While spectral diffusion occurs via flip-flops in the environment, instantaneous diffusion is a decoherence mechanism arising between resonant (A) spins. As the refocusing pulse is applied, the flip of the magnetisation of one A spin causes a change of the dipolar interaction with nearby A spins, applying a random phase shift and resulting in the decoherence of the magnetisation [135,136]. Due to the dipolar nature of the interaction, the instantaneous diffusion decoherence rate depends of the density of resonant spins ( _n_ ). The decoherence rate can be written as: 



Instantaneous diffusion can be somewhat controlled as the number of resonant spins is dependent on the power of the microwave pulse. The decoherence rate is maximum in equation 2.14 and can be reduced by altering the tipping angle of the 

_2.3. Pulse Sequences_ 

_30_ 

refocusing pulse [53]: 



Instantaneous diffusion is an important consideration in solid-state quantum memories. High spin densities can be used to achieve strong coupling between the spins and the cavity, and while this increases the efficiency of the memory, a high spin density can limit coherence via instantaneous diffusion and prevent long storage times [65]. 

##### **2.3 Pulse Sequences** 

The Hahn echo forms the basis of most ESR experiments and is used to measure the coherence of a spin system. By increasing the time for which the spins are in a superposition state (increasing _τ_ ), the time over-which decoherence can occur increases. As _τ_ increases, the fraction of spins which have decohered increases, this has the effect of a decay in the echo amplitude. The echo decays with characteristic time _T_ 2 from the initial _π/_ 2 pulse. 

The Hahn echo is not the only tool in our ESR toolbox when it comes to measuring decoherence. Another common pulse sequence is the three-pulse stimulated echo sequence (figure 2.6). This sequence controls the emission of an echo by utilising the long timescales of longitudinal relaxation. The sequence consists of three _π/_ 2 pulses with a long wait time separating the second and third pulse which can be of order _T_ 1. The sequence starts in the same manner as a Hahn echo, a _π/_ 2 pulse places the spins onto the equator of the Bloch sphere and dephasing occurs. Instead of refocusing the spins, the second _π/_ 2 projects the S _Y_ component of the spins onto the _z_ axis. When spins are aligned along _z_ they are only susceptible to longitudinal relaxation. To refocus the spins, a third _π/_ 2 places the spins back onto the equator and the refocusing results in a stimulated echo. The final two pulses in a three pulse echo sequence can be thought of as a _π_ pulse split in half and separated by time _TW_ . By doing this we gain control over the time at which the echo is emitted – thus giving the name _stimulated_ . 

The three-pulse echo sequence is particularly useful in verifying decoherence measured from a two-pulse echo. If the time between the initial _π/_ 2 pulses ( _τ_ ) is much shorter than _T_ 1 (i.e _τ ≪ T_ W), the echo decays as a function of _T_ W and spectral diffusion via [134]: 

_2.3. Pulse Sequences_ 

_31_ 





where _R_ and Γ _SD_ are the spectral diffusion rate and linewidth, respectively. The three pulse echo sequence is also used to measure electron spin echo envelope modulation (ESEEM) where the resolution of the measurement is not restricted by the coherence time of the electron spin. 

A different group of ESR pulse sequences comes in the form of dynamical decoupling. These sequences are designed to protect the spin from environmental noise and extend the coherence time. In a standard Hahn echo sequence the majority of the sequence involves spins dephasing and rephasing. This means there is a long time in which the spins are exposed to noise and can decohere. If we want to store an excitation and emit an echo after 1 ms, a Hahn echo (with 2 µs _π_ pulse) will require a _τ_ of 499 µs. Dynamical decoupling sequences use a chain a pulses with much shorter _τ_ times between them to reduce sensitivity to the environment. The simplest dynamical decoupling sequence is the Carr-Purcell-Meiboom-Gibbs (CPMG) sequence [137,138]. The CPMG sequence is a series of _π_ pulses which are 90<sup>_◦_</sup> out of phase to the initial _π/_ 2 pulse. The CPMG sequence also has applications in boosting echo signal [139]. As only a fraction of the energy stored in the spins is emitted from an echo, successive _π_ pulses emit their own echo. This allows for averaging over _N_ pulses and boosts the echo signal [140]. 

Each of these three pulse sequences is used in later results chapters. We will go into more detail of their properties and their signals as we approach them. There are many more pulse sequences within the ESR toolbox that are not covered here but are useful in an array of ESR and NMR applications including; electron nuclear double resonance (ENDOR), double electron electron resonance (DEER), hyperfine sublevel correlation (HYSCORE) etc. The three pulse sequences described here are shown schematically in figure 2.6. 

In most conventional ESR, square or Gaussian pulses are used. This is because the 3D cavities used to supply the pulses have uniform _B_ 1 field, and these pulses can be easily generated and are very short (ns timescale). In quantum memory applications, the cavity is a superconducting planar micro-resonator. We will see in chapter 4 that the _B_ 1 fields produced by these resonators is very inhomogeneous, with spins exhibiting a distribution of coupling strengths. This means a standard square pulse does not apply the same rotation to all the spins and makes controlling 

_2.3. Pulse Sequences_ 

_32_ 



<!-- Start of picture text -->
τ τ<br>π<br>2 π<br>τ TW τ<br>π π π<br>2 2 2<br>τ τ τ τ τ τ<br>π<br>2 π π π<br>Hahn Echo<br>Three-Pulse Echo<br>CPMG<br><!-- End of picture text -->

**Figure 2.6:** The standard pulse sequences for Hahn echo, three pulse stimulated echo, and the CPMG dynamical decoupling sequence. 

the whole spin ensemble particularly challenging. A class of pulses which chirp their frequency across the spin linewidth can be used to apply _π_ pulses to an entire ensemble. These pulses, known as adiabatic fast passage (AFP), are particularly useful in controlling the whole spin ensemble and form the basis of several quantum memory protocols. 

###### **2.3.1 Adiabatic Fast Passage** 

The nature of microresonators means not all the spins in the ensemble are subject to the same _B_ 1 field and as such undergo different rotations. This makes a reliable inversion ( _π_ ) pulse impossible with regular square pulses. To achieve a spin inversion across the whole ensemble a technique called adiabatic fast passage is used [141]. These pulses sweep their frequency from far below the spin linewidth to far above it. This coincides with the effective _B_ 1 vector experienced by the spins tracing an arc from the + _z_ axis to _−z_ passing through the _x − y_ plane when the frequency of the pulse is on resonance with the centre of the spin linewidth. If this arc is traced sufficiently slowly, the magnetisation vector is ‘dragged’ by the _B_ 1 vector causing an inversion as in figure 2.7. The frequency sweep must be done slowly enough to satisfy the adiabatic condition [141]: 



where _ω_ eff is the effective Rabi frequency about an effective _B_ 1 _B_ eff. 

ation effects can be neglected, hence adiabatic _fast_ passage. We can imagine a scenario where the adiabatic condition is not met, in this situation a spin experiences a sudden flip in effective _B_ 1 field. Instead of rotating the spin, it remains in the ground state but precesses around _B_ 1 is the opposite direction. Once the pulse finishes, the spin remains in the ground state. 

_2.3. Pulse Sequences_ 

_33_ 



<!-- Start of picture text -->
B<br>eff<br>M<br><!-- End of picture text -->

**Figure 2.7:** Bloch sphere representation of adiabatic fast passage, the _B_ eff is slowly swept from + _z_ to _−z_ such that the magnetisation vector precesses around it and is inverted. 

Adiabatic pulses are defined by the range of the frequency sweep and the amplitude of the pulse. A unitless parameter called the adiabaticity factor ( _Q_ ) is used to evaluate how well different pulses meet the adiabatic condition and should be greater than unity. _Q_ is defined as: 



written in terms of a _ω_ 1 which is detuned from the centre of the spin line by _δω_ = _ω_ 1 _− ω_ 0: 



_Q_ must be greater than 1 throughout the sweep. As _ω_ eff passes through the spin resonance _Q_ is minimum as ∆ _ω_ = 0. Therefore the adiabaticity factor on resonance is the quantity that need to be satisfied for inversion to be successful. The on-resonance adiabaticity factor can be written as: 



This allows for the instantaneous sweep rate to be deduced for a given amplitude profile [142]: 



_2.3. Pulse Sequences_ 

_34_ 



<!-- Start of picture text -->
θ/2<br>a)<br>WURST<br>Time<br>b)<br>BIR<br>Time<br>Amplitude<br>Frequency<br>/<br>Amplitude<br>Frequency<br>Phase<br><!-- End of picture text -->

**Figure 2.8:** a) WURST-20 pulse with the optimal frequency sweep calculated using equation 2.21. The steepness of the amplitude truncation is dictated by _n_ . b) Profile of the BIR-4 pulse for a rotation of _θ_ . At the first and fourth half-passage there is a phase jump of _π_ + _θ /_ 2 as in the BIR-4 protocol. 

By applying this to each time step of the adiabatic pulse the optimal frequency sweep profile can be determined. 

There are many amplitude profiles for inversion pulses, however one of the most effective is the wideband, uniform rate, smooth truncation (WURST) pulse [142]. These have an amplitude modulation given by: 



where _−π/_ 2 _≥ βt ≤ π/_ 2 and _n_ determines the steepness of the cutoff function. Applying equation 2.21 to the WURST pulse with _n_ = 20 gives an almost linear frequency sweep. The amplitude of the WURST-20 pulse and the optimal frequency sweep are shown in figure 2.8. 

WURST pulses offer inversion of a spin ensemble in an inhomogeneous B1 field, however they cannot be used for arbitrary rotations around the Bloch sphere. To do such a task B1-insensitive rotation (BIR) pulses [143] can be used. The BIR pulse is fairly complex in nature, however it is composed of four adiabatic half passage (AHP) pulses. These are AFP pulses which are halted halfway through the sweep. The BIR-4 (4 refers to the number of AHP pulses) pulse defined in [143] is shown in figure 2.8, the arbitrary _θ_ rotation is achieved by a step in the phase sweep a quarter and three-quarters of the way through the pulse. A phase jump of up of _π_ +<sup>_<u>θ</u>_</sup> 2<sup>and then down by the same amount allows for an overall rota-</sup> 

_35_ 

_2.3. Pulse Sequences_ 

tion of _θ_ once the pulse is completed. By applying BIR pulses with varying tipping angle Rabi oscillations can be observed in the spin ensemble. As _θ_ is increased, the echo amplitude will evolve from positive to negative and becomes maximally negative when _θ_ = _π_ . 

###### **2.3.2 ABBA Memory Protocol** 

AFP pulses are primarily used to perform controlled rotations over an inhomogeneous spin ensemble. However, they have also found use in quantum memory protocols. 

As mentioned previously, a two-pulse echo alone does not make a sufficient memory due to the additional noise arising from a spin ensemble emitting from an inverted state [97]. The retrieval of silienced echo (ROSE) protocol modifies the two-pulse echo by applying a second _π_ pulse [98]. This inverts the ensemble population a second time returning it to the ground state, a further _τ_ later an echo will form. While this echo is free from the artifacts which arise from emission from the inverted state, the echo amplitude and thus the memory efficiency are much lower as a fraction of the signal is emitted via the primary echo. In the case of unit efficiency, all of the signal is lost after the first echo. To ensure that this sequence has a high efficiency, the primary echo must be silenced so that all the signal is emitted from the secondary echo, this gives rise to the name retrieval of silenced echo. 

The ROSE protocol has two key requirements; the ability to perform a coherent _π_ pulse and a way to silence the primary echo. To achieve a reliable _π_ pulse across an inhomogeneously broadened ensemble, AFP can be used. As discussed in section 2.3.1, chirped pulses are used to invert the Bloch vectors in turn, this results in an evenly inverted ensemble. A single AFP pulse used on the transverse plane will not result in an echo, rather a pair of identical chirped pulses is needed to produce an echo. Conveniently this offers a solution to silencing the primary echo and both the ROSE requirements can be achieved simply with the use of chirped pulses. The ROSE protocol has been experimentally shown in [144–146] using a pair of complex hyperbolic secant (CHS) pulses. The efficiency of the protocol was also shown to extend to deep optical depths, an advantage over AFC and CRIB [145] protocols. Applying a series of input pulses before the pair of chirped pulses results in a series of echos in a first-in first-out memory scheme [147]. 

While the ROSE protocol gives a solution to many of the hurdles in creating a solid state quantum memory, it does not offer on demand retrieval of arbitrary stored states. If a quantum memory is to be incorporated into a quantum computer, 

18 54 6 6)8 6) 6) 8 EIS Ea Ea Ea Ea Ea Jia) (ee) (elas) (2a (elas) (2a (2a 



<!-- Start of picture text -->
6 6)8 6) 6)<br>8 EIS Ea Ea Ea Ea Ea<br>Jia) (ee) (elas) (2a (elas) (2a (2a<br><!-- End of picture text -->

_2.3. Pulse Sequences_ 

_37_ 

###### needed. 

The underlying principle of the ABBA protocol is the phase encoding which the chirped pulses apply to the stored states. A simple Hahn echo sequence undergoes a dephasing period in which is described by a spin wave with wavevector _kδ_ . This phase acquisition is reversible with the application of a _π_ pulse, in the ABBA protocol this is a WURST pulse. While the spin wave is refocused after a further time _τ_ , an echo is not formed because the WURST pulse applies an additional phase to the ensemble, _φW_ . This additional phase contribution prevents collective emission from the ensemble. A second identical WURST pulse will exactly undo the phase imprinted by the first pulse, however a non-identical WURST will continue to apply a further phase which can only be undone by repeating all the WURST pulses the excitation has previously undergone. This means each stored state has a unique phase imprint and so can be be read out with a unique decoding pulse sequence. 

Figure 2.10 gives a graphical description of the protocol. In a) the accumulation of phases which are resolved after two WURST pulses is described. An echo is only emitted when both the wavevector, _κδ_ , and phase pattern, _φW_ , are zero. In figure 2.10b) is a schematic of a section of the memory protocol where the yellow state is stored in memory with three other pre-stored states. The blue state is then subsequently read out. The WURST pulse applies an inversion to all stored states as well as its own phase pattern (yellow phase pattern for yellow WURST pulse), however these are undone on all existing stored states after the second identical WURST. This means the stored states are unaffected by the write sequence [106]. 

The ABBA protocol has been experimentally demonstrated with bismuth donors in silicon [106]. In this experiment, four multi-photon microwave states were stored and retrieved on demand for 2 ms. Figure 2.10c) shows these four states being stored in a random access fashion with the phase of the excitations being preserved throughout the protocol. An idle (grey) WURST pulse is also used in this scheme when there is neither a read or write requirement. As the WURST pulses act as a _π_ pulse, the ABBA protocol as well as the idle pulse act as a dynamical decoupling sequence which extends the coherence time of the spin ensemble. 

The ABBA protocol has the potential to be immensely valuable in developing a solid state quantum memory, however in its current state it is still quite primitive. The WURST pulses used in the experiment were 200 µs long, this severely limits the clock time of the memory and puts a limit on the minimum storage time. In addition, the _T_ 2 time of the bismuth system was only 2 ms, this again limits the number of stored states as well as the storage time. An estimated 16 states could be 

_2.3. Pulse Sequences_ 

_38_ 



<!-- Start of picture text -->
excitation [no echo] echo<br>20 20<br>100 I<br>Q 0 0<br>0<br>-20 -20<br>time ( μ s) 0 40 245 285 490 530<br>,i<br>,i<br>,i<br>Q (mV)<br>200 100<br>x3<br>50<br>-100 -50 50 100<br>0<br>x9 x11 I (mV)<br>-50<br>I<br>Q x31 Input<br>-200 -100<br>0 1 2 3 4 Output<br>t (ms)<br>a)<br>b)<br>c)<br>Signal (mV)<br>Signal (mV)<br><!-- End of picture text -->

**Figure 2.10:** a) Silencing of an echo using WURST pulses due to the phase accumulation. An echo is only emitted when both _κδ_ and _φW_ are zero. b) The phase trajectories experienced by stored states during the write and read stages of the memory protocol. The pre-stored states are unaffected by another state being stored in the system or a state being read out. The yellow state is written into the spins ensemble whereas the blue state is read out. c) Experimental realisation of the ABBA protocol, the left shows four distinct multi-photon states being stored and retrieved in an arbitrary order with their phase preserved as seen in the right plot. b) shows the different WURST pulses used to store each state. Edited from figures in [106]. 

_2.4. Spin Coupling_ 

_39_ 

stored in the bismuth spin ensemble, however for a useful memory this may need to be higher, this could be done with optimisation of the WURST pulses through their chip rate and amplitude. Finally, the cooperativity of this system was approximately _C_ = 0 _. C_ = 1 is needed. 06, for unit efficiency, 

While _C_ = 1 results in maximal efficiency, the inverted spin state after the intiial WURST pulse will undergo superradiant decay into the resonator resulting in the loss of the stored state in the inter-WURST period. To counteract this the cooperativity of the system should be tuned when a state is not being written or read. 

To achieve _C_ = 1 requires stronger coupling between the resonator and the spin ensemble, there are several ways to achieve this including higher spin doping, choice of spin species and improved resonator design. The next section describes the physics of coupling a spin to a cavity and outlines the relevant parameters in quantum memory applications. 

##### **2.4 Spin Coupling** 

To measure the spin properties of spin active systems, we need to couple to the measurement apparatus. In ESR, a cavity is needed to drive spin transitions as well as read out spin states. Thankfully coupling spins to a cavity is well understood from the theory of cavity quantum electrodynamics (QED). 

###### **2.4.1 Single Spin Coupling** 

Treating the spin as a two level system, the coupling Hamiltonian is described via the Rabi Hamiltonian [148]: 



energy level splitting of _ωs_ , the second relates to the cavity which has a frequency of _ωc_ and the final term describes the coupling between the two with coupling strength ˆ ˆ ˆ ˆ ˆ _g_ . _σz_ and ( _σ_ ˆ+ + _σ−_ ) = _σx_ are the usual Pauli operators, and _a_<sup>†</sup> and _a_ are the creation and annihilation operators of the harmonic oscillator (the cavity), respectively. The ˆ ˆ ˆ operator _a_<sup>†</sup> _a_ represents the photon number in the cavity as _a_<sup>†</sup> _|n⟩_ =<sup>_~~√~~_</sup> _n_ + 1 _|n_ + 1 _⟩_ ˆ and _a |n⟩_ =<sup>_~~√~~_</sup> _~~n~~ |n −_ 1 _⟩_ . While the Rabi Hamiltonian can be solved using involved analytics [149], it is common in NMR, ESR and quantum optics to use some ap- 

_2.4. Spin Coupling_ 

_40_ 

proximations to solve this Hamiltonian. 

By writing the overall Hamiltonian as an interaction Hamiltonian which perturbs the two system Hamiltonians we can move from the Schrödinger picture to the interaction picture: 



Using the time evolution of _a_ ˆ, _a_ ˆ<sup>†</sup> and _σ_ ˆ _±_ : 



the Hamiltonian is written as: 



We now invoke the rotating wave approximation where we observe that terms involving ( _ωs_ + _ωc_ ) evolve faster than ( _ωs − ωc_ ). The fast moving, or ‘counterrotating’, terms are ignored provided the coupling ( _g_ ) is much less than the energy splitting ( _ωs_ ). From this we arrive at a solvable Hamiltonian; the Jaynes-Cummings Hamiltonian: 



In the case of strong coupling, where the coupling strength, _g_ , is much greater than the loss rates of the cavity ( _κ_ ) and the spin ( _γ_ ), the eigenstates of the Hamiltonian are neither states of the cavity nor the spin but rather an entangled state of the two, these are called dressed states. 

_2.4. Spin Coupling_ 

_41_ 



<!-- Start of picture text -->
2g Cavity<br>Field<br>Spin<br>Frequency<br><!-- End of picture text -->

**Figure 2.11:** The energy eigenstates of the Jaynes-Cummings Hamiltonian in the strong coupling regime ( _g ≫ κ, γ_ ). An avoided crossing forms with the centre at the point where the spin and the cavity are on resonance, the splitting (called vacuum Rabi splitting) is equal to 2 _g_ . 





where _θ_ 



where ∆ is the detuning _ωs − ωc_ . These have eigenvalues: 



These lead to a splitting of the energy levels, when the spin and cavity are on resonance of _E_ + _− E−_ = 2 _g_ . This energy gap is the vacuum Rabi splitting and is a key indicator of strong coupling between a spin and a cavity. The eigenstates and the vacuum Rabi splitting is shown by the schematic in figure 2.11. 

###### **2.4.2 Ensemble Spin Coupling** 

The typical coupling strengths between a single spin and a cavity are weak and do not meet conditions for strong coupling. In ESR an ensemble of spins is used, these spins all interact with the cavity and so the Jaynes-Cummings Hamiltonian needs to be modified. This modification comes in the form of the Tavis-Cummings Hamiltonian: 



_2.4. Spin Coupling_ 

_42_ 

This has a similar form to the Jaynes-Cummings Hamiltonian however, the single spin has been replaced with an ensemble ( _i_ ) of _N_ spins each coupling to the cavity via a coupling strength, _gi_ . Assuming each spin has the same coupling strength, _g_ 0, an ensemble coupling strength can be written as _gens_ = _√Ng_ 0. The eigenstates of the Tavis-Cummings Hamiltonian have a similar form to the JaynesCummings model, however we write the spin state as the ensemble being in the excited ( _|e⟩_ ) or ground ( _|g⟩_ ) state. These define a collective excitation over the whole ensemble, in effect an entangled state over all _N_ spins: 



The eigenstates of the Tavis-Cummings Hamiltonian are: 



with eigenvalues: 



Using an ensemble of spins allows the coupling strength to be increased by a factor of _√N_ and makes reaching the strong coupling regime much more achievable. 

A useful measure of the coupling between a spin ensemble and a cavity is the _cooperativity_ . 



Several quantum memory applications require _C_ = 1 [120], this is, in a sense, an impedance matching condition whereby the transfer of information between the spins and the cavity is lossless. 

_2.5. Yb:YSO Spin System_ 

_43_ 



<!-- Start of picture text -->
1 Hz<br>106 10 Hz<br>100 Hz<br>102 1000 Hz<br>κ/2π = 100 kHz<br>10-2<br>-5 0 5<br>Detuning (MHz)<br>T lle<br>cr<br>u<br>P<br>(s)<br>1<br><!-- End of picture text -->

**Figure 2.12:** Purcell limited _T_ 1 (1 _/_ Γ _P_ ) for different spin coupling strengths coupled to a cavity with linewidth of 100 kHz. 

###### **2.4.3 Purcell Regime** 

When spins are coupled to a high Q cavity, spontaneous emission into the cavity is enhanced via the Purcell effect [150]. The rate for a spin to relax via the cavity is governed by the cavity linewidth ( _κ/_ 2 _π_ ), the coupling and the detuning [151]: 



The Purcell effect is particularly useful in milliKelvin ESR. At such low temperatures the spin-lattice relaxation can be minutes, if not hours. This makes resetting the spin system difficult and restricts the shot repetition time of ESR experiments or the ability to reset a memory. In figure 2.12 the Purcell limited _T_ 1 (1 _/_ Γ _P_ ) is plotted for different spin coupling strengths to a cavity with linewidth of 100 kHz. The Purcell rate can be increased by decreasing the cavity linewidth (increasing its Q), or increasing the coupling strength. The coupling strength is related to the magnitude of the _B_ 1 field, and is an important parameter to optimise when designing ESR experiments. Superconducting resonators offer a pathway for high Purcell rates due to their low internal losses and high Q factors. This will form an important part of the resonator design in quantum memory experiments and is explored in section 4.1.2. 

##### **2.5 Yb:YSO Spin System** 

In this thesis we study Yb<sup>3+</sup> ions doped into YSO. Being a Kramer ion, Yb has electron spin 1 _/_ 2 resulting in available ESR transitions under the application of a magnetic field. Yb has seven stable isotopes, four of these have 0 nuclear spin and correspond to 70% of the natural abundance. The two isotopes with nuclear spin are 173Yb with _I_ = 5 _/_ 2 and 171Yb with _I_ = 1 _/_ 2. These have 16% and 14% abundance respectively [152].<sup>171</sup> Yb is the only Kramer ion with 1 _/_ 2 nuclear spin, meaning it has the simplest hyperfine structure. 

_2.5. Yb:YSO Spin System_ 

_44_ 

The YSO crystal has two in-equivalent sites where a rare-earth ion substitutes Y<sup>3+</sup> . In some cases, such as Nd which has a large ionic radius, the ion preferentially substitutes one of the sites [153]. Yb substitutes into both sites equally with each site have its own _g_ ˆ and hyperfine ( _A_<sup>ˆ</sup> ) tensor [154]: 

**171 Yb Site 1** : 



**171 Yb Site 2** : 



The _A_<sup>ˆ</sup> tensor for the<sup>173</sup> Yb isotope has an additional factor of _−_ 0 _._ 27 [155]. 

In YSO both sites have additional subsites, ( _a_ and _b_ ), these subsites are degenerate when a magnetic field is applied in the _D_ 1- _D_ 2 crystal plane, but lifted when there is a component in the _b_ axis. 

The Yb spin system is simulated using easyspin [156]. Easyspin numerically solves the spin Hamiltonian and returns transitions frequencies or resonant fields as well as transition intensities via Fermi’s golden rule (FGR). 

Using easyspin the energy levels of the electron-nucleus spin system are calculated and shown for each isotope and site in figure 2.13. At low fields the system is in the strong hyperfine regime where the electron and nucleus form a hybrid system with mixing of the eigenstates. This allows for zero-field splitting and gives rise the ZEFOZ transition. 

By calculating the energy difference and FGR for the possible spin transitions 

_45_ 

###### _2.5. Yb:YSO Spin System_ 



<!-- Start of picture text -->
Site 1 Site 2<br>D1 D2 b<br>6<br>171Yb 0<br>-6<br>6<br>173Yb 0<br>-6<br>6<br>I=0Yb 0<br>-6<br>0 200 400 0 200 400 0 200 400<br>Field (mT) Field (mT) Field (mT)<br>Energy (GHz)<br>Energy (GHz)<br>Energy (GHz)<br><!-- End of picture text -->

**Figure 2.13:** Energy level diagrams of ytterbium isotopes present in the natural doped system in both crystallographic sites and fields applied along the three crystal axes (D1,D2,b). The presence of nuclear spin in the<sup>171</sup> Yb ( _I_ = 1 _/_ 2) and 173Yb ( _I_ = 5 _/_ 2) isotopes gives rise to hyperfine levels which allows for transitions with low d _f_ /d _B_ . 

their frequency and intensity can be simulated. All isotopes have transitions in the ESR regime (GHz) at fields _<_ 500mT (figure 2.14), this allows for Yb spin transitions to be coupled to superconducting circuits. 

_2.5. Yb:YSO Spin System_ 

_46_ 



<!-- Start of picture text -->
Site 1 Site 2<br>D1 D2 b<br>5 2 0<br>4<br>171 3<br>Yb<br>1 0<br>2<br>1<br>0 0<br>5 2 0<br>4<br>173 3<br>Yb 1 0<br>2<br>1<br>0 0<br>5 2 0<br>4<br>I=0 3<br>Yb<br>1 0<br>2<br>1<br>0 0<br>0 200 400 0 200 400 0 200 400<br>Field (mT) Field (mT) Field (mT)<br>(GHz)<br>Amplitude<br>Frequency<br>(MHz/mT)<br>2<br>(GHz)<br>Amplitude<br>Frequency<br>(MHz/mT)<br>2<br>(GHz)<br>Amplitude<br>Frequency<br>(MHz/mT)<br>2<br><!-- End of picture text -->

**Figure 2.14:** Transition frequencies for each ytterbium isotope for both crystallographic site with field applied along each crystal axis (D1,D2,b). The transition intensity is shown by the opacity of the line, this is determined by the matrix element of the relevant transition. 

##### **Chapter 3** 

### **Superconducting Resonators** 

If you see a formula in the Physical Review that extends over a quarter of a page, forget it. It’s wrong. Nature isn’t that complicated 

|||Bernd Matthias|
|---|---|---|
|**nts**<br>**3.1**|**Impedance in Superconducting Circuits . . . . . . **|**. . . . . .**<br>**48**|
|**3.2**|**Kinetic Inductance . . . . . . . . . . . . . . . . . . **|**. . . . . .**<br>**51**|
|**3.3**|**Properties of Superconducting Resonators**<br>**. . . . **|**. . . . . .**<br>**53**|
|**3.4**|**Fabrication of Superconducting Resonators . . . . **|**. . . . . .**<br>**55**|



###### **Contents** 

In this chapter, we will outline the underlying theory of superconducting resonators. Supercurrent, ultra-high Q factors and useful non-linearities have allowed superconducting resonators to play a vital role in many different applications including (but certainly not limited to!) quantum computing [28,31,83,157,158], quantum amplifiers and detectors [159–165], and high-sensitivity ESR [64,95,166–168]. Superconducting resonators take many forms depending on their application, however the underlying physics remains the same. 

one of the few areas in physics where new theory is realised to understand experimental results<sup>*</sup> . Onnes’s discovery of the superconductivity of mercury in 1911 [169] could not be theoretically explained for over 40 years until BardeenCooper-Schrieffer (BCS) published their theory of superconductivity [170]. 

- *As apposed to the increasing way of doing science - perform experiments to test theory. 

_3.1. Impedance in Superconducting Circuits_ 

_48_ 

Prior to BCS theory it was predicted that superconductors, while having zero DC resistance, should exhibit a small but finite AC dissipation [171]. This is crucial in understanding superconducting resonators at GHz frequencies as, while their resistance may be zero, they still have an impedance. 

##### **3.1 Impedance in Superconducting Circuits** 

The basis of BCS theory is the Cooper pair. In superconductors, Cooper pairs carry charge and are formed of a pair of correlated electrons in a bound state. Linked via phonon interactions with the lattice, Cooper pairs are broken apart at temperatures above a critical temperature ( _Tc_ ). Due to the weak strength of this interaction, standard superconductors only pass supercurrent at very low temperatures. The energy needed to break a Cooper pair is the superconducting energy gap, this is equal to 2∆ centred at the Fermi energy and is approximately given by: 



Even below the critical temperature there remain a finite number of ‘normal’ electrons (often called quasiparticles). The density of these quasiparticles is found by integrating the density of states above the energy gap: 



where _N_ 0 is the single-spin electron density at the Fermi level and _f_ ( _E_ ) is the FermiDirac distribution. The quasiparticles introduce a complex conductivity which results in a non-zero impedance for AC signals. 

The conductivity in AC circuits ( _σAC_ ) is complex and given by [172]: 



where _σDC_ is the DC conductivity, _ω_ is the AC frequency, and _τ_ is the electron scattering time. In a superconductor both _σDC_ and _τ →_ ∞ meaning _σAC_ remains 

Mattis and Bardeen applied BCS theory to the electrodynamics of superconductors and derived equations for the real and imaginary parts of the complex conductivity [173]: 

_3.1. Impedance in Superconducting Circuits_ 

_49_ 





where _σn_ is the normal conductivity at just above _T_ = _Tc_ . While the real part goes to zero as _T →_ 0 (as _f_ ( _E_ ) _→_ 0), the imaginary conductivity remains non-zero. Experimentally, conductivity is difficult to ascertain, we therefore express it in the form of the surface impedance: 



where _R_ is the resistance and _X_ is the reactance. Far below _Tc_ and for frequencies much less than the band gap energy _R ≈_ 0<sup>†</sup> . The reactance is written as the sum of the inductive and capacitive reactance: 



which in turn can be written as: 



where _L_ is the inductance and _C_ is the capacitance. At resonance _ω_ = 1 _/√LC_ and so _X_ = 0. This therefore implies the impedance at resonance _Z_ = 0. While this may be true for an isolated wire, in a transmission line we must account for the capacitance between the conductors. 

Suppose we have a superconducting wire ( _R_ = connected to either side of a battery (as in figure 3.1), if the switch is closed will a current flow through the wire? As there is no load in the circuit we may assume that no current would flow, however we need to look closer at the circuit and realise that there is a capacitance between the two conductor lines as well as an inductance along them. If we model the circuit as several capacitors in parallel and inductors in series, when the switch is closed the capacitors charge up in turn drawing cur- 

> †on the order nΩ for niobium. 

_50_ 

_3.1. Impedance in Superconducting Circuits_ 



<!-- Start of picture text -->
L<br>C<br><!-- End of picture text -->

**Figure 3.1:** The origin of characteristic impedance in superconducting transmission lines. While the resistance of the wire may be zero, the capacitance between the conductors and the inductance along them results in a load for which current must be passed. This load is the characteristic impedance and in an infinitely long line is equal to � _L/C_ . 

rent. While the charging of the capacitors implies an infinite draw in current, the inductance in the wires counteracts this. The inductors oppose the change in current arising from the capacitance so that the magnitude of the current remains finite. As the energy in this system is propagated through the electric and magnetic fields, the current will propagate at the speed of light (even though the electrons themselves are moving much slower than this!).<sup>‡</sup> 

The result of this is even though the resistance of the wire is zero, the transmission line still has an impedance - this is the characteristic impedance, _Z_ 0: 



Therefore, we rewrite the impedance of a superconducting circuit as: 



at resonance this reduces to _Z_ = _Z_ 0. 

When designing a superconducting resonator, the characteristic impedance is an important parameter. In some cases such as resonators for transporting signals, the characteristic impedance is designed to be 50 Ω to reduce reflections [83]. 

> ‡This phenomena was the basis of a large-scale internet debate on whether a light-bulb 1m away from a battery connected via a 1 lightsecond long circuit would switch on after 1/c seconds - it does! YouTube - The Big Misconception About Electricity - Veritasium. 

_51_ 

_3.2. Kinetic Inductance_ 

Fluxonium qubits require very high impedance to overcome the superconducting impedance quantum [174]. For ESR applications, low impedance resonators are used to maximise the current through the inductor [168,175,176]. Low impedance resonators allow for high spin-coupling strengths as the vacuum current fluctuations (and therefore high vacuum field fluctuations _δ B_ ) can be high: 



where _δ i_ is the current corresponding to a single photon in the resonator, this gives single-spin coupling strength: 



In this analysis, we have neglected an important property of superconductors - kinetic inductance. This non-linear inductance not only provides an additional inductance but also allows for frequency tunable resonators [177,178] but also threewave mixing for parametric amplification [164,179]. 

##### **3.2 Kinetic Inductance** 

Kinetic inductance is not really an ‘inductance’ in the usual sense of the word. It does not follow Faraday’s law of induction and is only referred to as an inductance because it can be written in a form analogous to Faraday’s equation. Kinetic inductance is more closely related to Newton’s first law and should rather be called ‘charge inertia’. Kinetic inductance arises from the charge carrier’s reluctance to 

The kinetic inductance ( _L_ K) of a superconducting wire can be determined by equating the kinetic energy of a Cooper pairs to the inductive energy: 



where _n_ is the density of Cooper pairs (mass 2 _me_ ), _V_ is the volume of the wire, _v_ is the Cooper pair velocity and _I_ is the supercurrent. Using _I_ = 2 _nevA_ (where _A_ is the cross-sectional area) we get: 



where _l, w_ and _d_ are the length, width and thickness of the wire, respectively. From this, it can be seen that wires with very high aspect ratio result in high kinetic 

_52_ 

_3.2. Kinetic Inductance_ 

inductance. 

In a superconductor, the number of Cooper pairs is temperature, current, and magnetic field dependent and so the same is true for the kinetic inductance. Using Ginzburg-Landau (G-L) theory, the temperature dependence of Cooper pair density is given by [180]: 



where _Tc_ is the critical temperature of the superconductor. This means the kinetic inductance is maximal at the critical temperature: 



The current dependence of _n_ is harder to derive but it has a similar form [181]: 



where _I_<sup>_∗_</sup> is a constant proportional to the critical current. By applying a microwave tone through the superconductor a Kerr term ( _IAC_<sup>2) is added which results</sup> in non-linear kinetic inductance: 



This can then facilitate three-wave [164] or four-wave [182] mixing for parametric amplification. 

The kinetic inductance is also magnetic dependent. As the is increased, the London penetration depth increases as: 



this reduces the Cooper pair density and thus increases the kinetic inductance: 



where _α_ 

The kinetic inductance is typically incorporated into the total inductance, _L_ , and in turn into the characteristic impedance. However, we must be careful when using superconducting resonators to generate magnetic fields as it is only the geo- 

_53_ 

_3.3. Properties of Superconducting Resonators_ 

metric inductance which plays a role. 

##### **3.3 Properties of Superconducting Resonators** 

Superconducting resonators come in two main forms, coplanar waveguide (CPW) resonators and lumped element resonators. The first is predominately used in quantum computing, coupling qubits to each other and to readout lines. The length of the CPW resonator allows it supports a standing wave which can exist for long timescales due to the high quality factors achievable via superconductors [181]. For ESR applications, lumped element resonators are used. The resonant mode is dictated by the capacitance and inductance of the resonator which can be altered to tune the impedance (as in equation 3.9). Lumped element resonators have great flexibility in their geometrical design (which we will see in chapter 4), allowing for different properties of the resonators to be exploited. 

All resonators have two main parameters – their frequency and their quality factor. In a lumped element resonator the resonant frequency is given by: 



This is analogous to a mass on a spring where the energy oscillates from the capacitor (potential energy of the spring) and the inductor (kinetic energy of the mass). During this process the electric field from the capacitor and the magnetic field oscillate 90<sup>_◦_</sup> out of phase with the resonant frequency. This allows for a microwave _B_ 1 field to be produced for ESR applications. Given the temperature, current, and magnetic field dependence of kinetic inductance, the frequency of a superconducting resonator can be tuned using these parameters. In order to have a stable resonant frequency (needed for ESR), the superconducting resonator should be cooled to well below its critical temperature and tuning via temperature is not particularly accurate. Current and field biasing can be used to tune the frequency, this is particularly useful when targeting specific frequency points such as clock transitions. Current tunable resonators have been designed where a current bias is used to tune down the resonant frequency [183]. The rapid application of DC currents can be used to quickly tune resonators on and off resonances with each-other, or to allow for echo silencing from spin ensembles [104]. 

Current tunability requires quite complex resonator design, where use of Bragg mirrors is often used to decouple the resonator from the input ports while allowing a DC current to pass [184]. Field tunability is much easier to perform. The resonant frequency decreases quadratically as the field is increased up to the critical field of 

_54_ 

_3.3. Properties of Superconducting Resonators_ 

the superconductor. In the case of thin-films the tuning is more sensitive, when the field is applied out of plane to the film, this is because the increased area results in larger magnetic flux through the film. Field tunability is used to align magnetic fields to the resonator plane (see section 4.1.3) which allows for fields of well over 1 T to be used with superconducting resonators [178]. This can also be used to tune onto resonance with spins, however consideration on how the added field effects the spins is needed. 

The other main property of superconducting resonators is the quality factor (Q). The Q factor describes how lossy the resonator is. A higher Q factor means a signal can be maintained in the resonator for a longer time. There are several ways to define the Q factor of a cavity, the first is the ratio of the stored energy to the energy lost per cycle, while the second is defined in terms of the bandwidth of the cavity where Q is the ratio of the cavity frequency to cavity bandwidth: 



The bandwidth definition is the easier to measure and is the definition which is used throughout this thesis. The total Q factor simply quantifies all the loss mechanisms experienced by the cavity and can be broken down into three main loss mechanisms: 



where _Qi_ , _Qc_ and _Qr_ are the intrinsic, coupling and radiative quality factors respectively. 

We look at the two mechanisms which are almost always undesirable, the intrinsic and radiative losses. Intrinsic losses within the superconducting film itself includes its residual resistivity (section 3.1), vortexes formed by external magnetic fields, and two-level systems (TLS) on the surface of the resonator or in the substrate which couple to the cavity mode [185]. These can be reduced by using higher quality superconducting films, thorough cleaning of the surface, and eliminating stray magnetic fields. Radiative losses occur when the electric dipole of the resonator emits electromagnetic radiation into the environment. In an open environment this occurs over all frequencies, however enclosing the resonator with a metal box restricts this to certain wavelengths. 

The coupling quality factor is one which may be designed to be large or small depending on the purpose of the resonator. Coupling ‘losses’ are where the res- 

_55_ 

_3.4. Fabrication of Superconducting Resonators_ 

onator couples to input (or output) lines used to drive (and read) the resonator. In ESR applications a balance of ensuring the coupling is low enough to maintain a high Q (therefore high ESR sensitivity) resonator, while also high enough coupling that the output line is the dominant mechanism for emission from the resonator. Techniques such as using a short input antenna and a long read antenna have be used to finely balance _Qc_ [140]. 

The quality factor plays several roles in ESR. High Q factor resonators are highly sensitive in CW ESR and small shifts in frequency (or linewidth) from spin interactions are resolveble. However, in pulsed ESR very high quality factors suffer from extensive ring-down and make measuring spin signals on short timescales difficult, compensated pulses are needed to overcome this issue [186]. In addition, very high Purcell rates will restrict _T_ 1 and may become a limiting decoherence mechanism. 

##### **3.4 Fabrication of Superconducting Resonators** 

The majority of superconducting resonators are fabricated using photolithography. It is only in case which require very narrow features ( _<_ 1 µm) that require electron beam lithography (EBL). The lithography process can take one of two paths; liftoff or etching. Etching is the simplest and most common approach, however liftoff is needed when etching into the substrate is a significant concern. Resonators fabricated on sapphire or YSO do not see any etching into the substrate and so this is the process which is used to fabricate all the resonators in this thesis. A schematic of the whole process is shown in figure 3.2. 

Any cleanroom fabrication process begins with cleaning. A clean surface is needed before metal can be deposited, this allows for good adhesion to the surface and results in high Q resonators. Typically a solvent clean is all that is necessary, this involves 5 mins of sonication in acetone and then a further 5 mins sonication in isopropanol. 

Niobium or niobium nitride superconductor is deposited using a sputtering process. A Nb metal target is bombarded with an Ar plasma which causes Nb atoms to be ejected from the surface of the target and adhere to the surface of the substrate. By controlling the time for which the sample is exposed to the plasma the thickness of the film can be controlled, this is usually accurate to within a few nm. To form NbN superconductor N2 gas must be inserted into the chamber, the Nb reacts with the N gas before being deposited on the surface. The sample is rotated to form a 

After sputtering, photolithography is used to imprint the resonator design onto 

_56_ 

_3.4. Fabrication of Superconducting Resonators_ 

the chip. Photoresist (typically S1805 or S1818) is spun onto the surface of the chip. The photoresist reacts to UV light and is washed away after development – it is therefore important to keep the design under yellow light during the photolithography. A layer of _≈_ 500 nm of photoresist covers the whole chip. Two different techniques can be used to pattern the design onto the device. The more traditional method uses a mask, this method uses a physical photomask with the design cut into it. UV light is then shone through the mask and exposes the design onto the photoresist. For rapid prototyping, direct-write photolithography can be used. In this method a mask is not needed and a UV laser is used to expose the design. The resolution of direct-write photolithography can be as low as 700 nm. After the design has been exposed onto the resist, the device is placed into MF-319 developer. This dissolves the exposed regions of resist while preserving unexposed areas – protecting the metal below. 

The final stage in the fabrication process is etching. For the design to be imprinted into the superconductor the metal needs to be etched. This is done with reactive ion etching where reactive gases of SF6 and CHF3 are used to remove the metal not covered with resist. This process can etch into silicon and cause undercutting of the resonators where the etching encroaches underneath the resonator – this does not occur in sapphire or YSO. 

Finally, the excess photoresist can be removed with acetone and after an isopropanol wash the resonators can be characterised. Examples of the final resonators are shown in figure 3.3. 

_57_ 

_3.4. Fabrication of Superconducting Resonators_ 



<!-- Start of picture text -->
NbN<br>YSO<br><!-- End of picture text -->



<!-- Start of picture text -->
Photoresist<br>NbN<br>YSO<br><!-- End of picture text -->



<!-- Start of picture text -->
Photoresist<br>NbN<br>YSO<br><!-- End of picture text -->



<!-- Start of picture text -->
NbN<br>YSO<br><!-- End of picture text -->



<!-- Start of picture text -->
Photoresist<br>NbN<br>YSO<br><!-- End of picture text -->



<!-- Start of picture text -->
Photoresist<br>NbN<br>YSO<br><!-- End of picture text -->

**Figure 3.2:** Fabrication process for a superconducting resonator performed with directwrite photolithography 





**Figure 3.3:** Microscope images of NbN superconducting resonators fabricated on YSO. 

##### **Chapter 4** 

### **Experimental Methods** 

Keep cool, but do not freeze 

A jar of mayonnaise 

###### **Contents** 

|**4.1**|**Reson**|**ator Design**<br>**. . . . . . . . . . . . . . . . . . . . . . . .**<br>**59**|
|---|---|---|
||4.1.1|Geometry . . . . . . . . . . . . . . . . . . . . . . . . .<br>59|
||4.1.2|Simulation<br>. . . . . . . . . . . . . . . . . . . . . . . .<br>62|
||4.1.3|Characterisation<br>. . . . . . . . . . . . . . . . . . . . .<br>67|
|**4.2**|**Cryos**|**tats . . . . . . . . . . . . . . . . . . . . . . . . . . . . .**<br>**73**|
||4.2.1|Closed-Cycle Cryostat . . . . . . . . . . . . . . . . . .<br>73|
||4.2.2|Dilution Refrigerator . . . . . . . . . . . . . . . . . . .<br>73|
|**4.3**|**ESR S**|**etup**<br>**. . . . . . . . . . . . . . . . . . . . . . . . . . . .**<br>**77**|



The theory of ESR and superconducting resonators can be utilized to perform high-sensitivity ESR experiments at milliKelvin temperatures. In this chapter, we will describe the key experimental considerations and apparatus that were used to perform the measurements in subsequent chapters. A large part of the experimental design comes in the form of the device itself; in the first half of this chapter we will explore how resonator design and geometry can be modified to best suit quantum memory experiments. In the latter half the surrounding experimental setup will be described, this includes the home-built ESR spectrometer and the cryostats used to reach milliKelvin temperatures. 

_59_ 

_4.1. Resonator Design_ 

##### **4.1 Resonator Design** 

The process of producing a superconducting resonator involves three steps in an iterative loop. Firstly, design considerations should be thought out. Questions such as ‘What purpose does the resonator have?’, ‘Which resonator parameters should be optimised?’, ‘What frequencies should the resonator target?’ etc. should be answered; this allows for a suitable resonator to be simulated. Simulation is the next step in the process, resonators need to be designed within frequencies ranges set either by the experimental apparatus or the spin system. To design resonators for the correct frequency, simulation software like CST Microwave Studio is used, this performs finite element analysis on the design and provides S-parameters to identify the resonant frequency. Additionally, COMSOL is used to simulate the magnetic field generated from the resonator, this in turn can be used to estimate spin coupling strengths. 

Once a design has been chosen, the resonator is then fabricated in the cleanroom. The fabrication process is outlined in section 3.4 and is the same for all the resonators designed in this thesis. During the initial fabrication, resonators over a wide range of frequencies are designed - usually 9-12 per 5x5 mm chip. The wide range of frequencies allow for deviations from simulation and ensures that a subset of the resonators will be resonant within the experiment frequency bandwidth - limited by the frequency range of the vector network analyser (VNA) used for testing. 

The final stage of the design process before using the resonators for ESR experiments is to characterise the resonators. To quickly measure and test the designs, a 4He closed-loop cryostat is used to cool the resonators below their superconducting _Tc_ . A home-built probe and a VNA is used to measure the resonant frequencies and quality factors of the resonators. From this, a calibration of resonator frequency can be used to design resonators with a desired resonant frequency. A comprehensive overview of the characterisation process follows later in the chapter. This whole process is shown schematically in figure 4.1. 

We begin with the geometry of superconducting resonators for ESR applications. Several different designs have been implemented with different goals, in the following section we will explore their properties and different use cases. 

###### **4.1.1 Geometry** 

The geometry of a superconducting resonator is one of the most important design considerations. The fundamental frequency of a resonator is determined by its capacitance and its inductance, both of these parameters are dependent on the geome- 

_60_ 

_4.1. Resonator Design_ 



<!-- Start of picture text -->
Design Considerations<br>(High  g0 , High  C ,  f ...)<br>Design Mock-up<br>(Python, GDS)<br>Simulate<br>(CST Mircowave Studio)<br>Fabricate<br>(Cleanroom Fab)<br>Characterise<br>(Closed-Loop Cryostat)<br>ESR<br>(Dilution Fridge)<br>Modelling<br>Fabrication<br>Measurement<br><!-- End of picture text -->

**Figure 4.1:** The design process for producing superconducting resonators. The three main steps (modelling, fabrication, and measurement) form an iterative process which results in high Q resonators with desired resonant frequency. 

_61_ 



<!-- Start of picture text -->
4.1. Resonator Design<br><!-- End of picture text -->



<!-- Start of picture text -->
Capacitor Inductor<br>Thin-Ring Spiral Airplane<br><!-- End of picture text -->

**Figure 4.2:** Different resonator geometries used in this thesis. The thin-ring and airplane designs are lumped element designs with a clear separation of the inductor and capacitor, while the spiral is a distributive design. 

try of the circuit. In addition, the magnetic field produced by the resonator is dependent on the geometry; narrow constrictions result in higher field strengths, meanders with current flowing in opposite directions allow for more homogeneous fields and large capacitive plates create large electric fields and small magnetic fields. 

We first look at the role geometry plays in resonator frequency. The simplest, planar resonator, is a lumped-element resonator which is comprised of a lumped inductor and capacitor. Lumped-element designs allow for a clear distinction of capacitance and inductance and allow for easier simulation and modelling of the resonant frequency and field behaviour. The ‘thin-ring’ design is a ring of superconductor with one edge much thinner than the other – overlapping – sides. The design in depicted in figure 4.2 with the capacitor and inductor sections highlighted. In this the design the capacitor is simply two planar plates. The coplanar capacitance can be found via [187]: 



where _w_ and _d_ are the width of the tracks and the separation respectively. _εr_ is the relative permittivity of the substrate and _c_ is the speed of light in a vacuum. The inductance of a planar wire is [188]: 



where _l_ , _w_ and _t_ are the length, width and thickness of the wire respectively 

_62_ 

_4.1. Resonator Design_ 

and _µ_ 0 is the permeability of free space. 

Using _ω_ 0 = 1 _/_ _~~√~~ LC_ , the resonant frequency of a thin-ring design can be easily approximated. Assuming a square design, with thickness 50 nm, capacitor width 20 µm and separation 5 µm, and inductor width 2 µm, the frequency dependence on the side length is shown in figure 4.3, where a length of _≈_ 600 µm is needed to reach 7 GHz (a frequency well within the experiment bandwidth). This resonator design has been used to couple to an ensemble of<sup>145</sup> Nd spins in the high-cooperatively regime [95] with its ease of fabrication making it easy to replicate. 

One of the significant downsides to the thin-ring design is the difficulty in producing low frequency (< 5 GHz) resonators with a small physical footprint. In order to generate a thin-ring resonator with a frequency of 2 GHz the side length would have to be almost 2 mm. Such as large footprint makes this style of resonator difficult to incorporate with superconducting qubit architectures where the qubits are much smaller in size. In addition, from an experimental point of view, this means only 4, closely separated resonators could be placed onto a 5x5mm chip. This is not ideal for targeting very specific frequencies such as clock transitions. 

The spiral resonator design (shown in figure 4.2) is a distributed resonator design which aims to have low resonant frequencies with a small footprint. A distributed design is one in which the entire resonator forms both the capacitive and inductive elements. In the spiral design the self-inductance of the long spiralling wire gives a large inductance, while the capacitance arises from the gaps between each layer of the spiral. As such, the resonator frequency is much harder to estimate and so CST simulations are used to predict the behaviour (see section 4.1.2), however the frequency approximately goes as the inverse of the total length of the spiral. 

Once again, this is a lumped element resonator which is made of a loop-back inductor and an interdigitated capacitor. The loop-back inductor results in a more homogeneous magnetic field compared to the thin-ring design, while the large capacitor allows for lower frequencies to be targeted. The interdigitated capacitor makes it easy to frequency select the resonator as extra fingers can be added to the capacitor without the need to alter the inductor. Due to the complex nature of this geometry, the resonant frequency is predicted via simulation. 

###### **4.1.2 Simulation** 

To simulate the properties of the resonator a combination of CST Microwave Studio and COMSOL are used. First a geometric parameter of the resonator is varied and 

_63_ 

_4.1. Resonator Design_ 



<!-- Start of picture text -->
1 0 1 1 0 1<br>1 0 0 1 0 0<br>length 1 0 -1 1 0 -1<br>1 0 -2 1 0 -2<br>1 0 -3 1 0 -3<br>1 0 4<br>1 0 3<br>1 0 2<br>1 0 1 f = 7 GHz<br>1 0 0<br>0 2 0 0 4 0 0 6 0 0 8 0 0 1 0 0 0<br>length (μm)<br>Capacitance (pF)<br>frequency (GHz)<br>Inductance (nH)<br><!-- End of picture text -->

**Figure 4.3:** The estimated resonant frequency of the thin-ring resonator design using equations 4.1 & 4.2. A thickness of 50 nm, capacitor width 50 µm, capacitor separation 5 µm and inductor width 2 µm are used. The length of the square side is varied, increasing both the capacitance and the inductance. To reach 7 GHz, which is well within the measurable bandwidth, a side length of 600 µm is needed. 

the CST eigenmode solver (or frequency solver to return S-parameters) is used to estimate the resonant frequency and the features of the mode. 

The design is imported into CST as a GDS file and assumed to be a perfect electrical conductor. The design within CST is shown in figure 4.4a). Using the frequency domain solver the transmission through the coupled transmission line (S21) can be modelled. A clear dip in transmission is observed at the resonance of the design (figure 4.4b)). The resonance of this design is simulated to be at 4 _._ 89 GHz. The magnetic and electric field of the resonant mode are simulated within CST to ensure the correct resonance is observed. Plotting the fields at a slice 100 nm below the resonator shows the magnetic field between the arms and the electric field along them. 

The spiral design has two advantages over the thin-ring resonator. its smaller footprint to reach lower frequencies, and the second is the more homogeneous magnetic field produced into the sample. In figure 4.5 the absolute magnetic field strength is plotted below the resonator up to a depth of 100 µm (the slide is cut through the centre of the spiral along its long ( _y_ ) axis). Near to the surface fringes are observed corresponding to each track in the spiral, however these average out further from the resonator. Plotting the field strength at the centre of the resonator, it 

_64_ 

_4.1. Resonator Design_ 



<!-- Start of picture text -->
a)<br>Ground Plane<br>Vacuum Silicon/Sapphire Subtrate<br>Spiral Resonator<br>Port 1<br><!-- End of picture text -->







<!-- Start of picture text -->
B<br>x<br><!-- End of picture text -->



<!-- Start of picture text -->
B<br>y<br><!-- End of picture text -->



<!-- Start of picture text -->
B<br>z<br>1<br>0 Relative Field<br><!-- End of picture text -->



<!-- Start of picture text -->
|B|<br>1mm<br><!-- End of picture text -->



<!-- Start of picture text -->
E<br>x<br><!-- End of picture text -->



<!-- Start of picture text -->
E<br>y<br><!-- End of picture text -->



<!-- Start of picture text -->
E<br>z<br>1<br>0 Relative Field<br><!-- End of picture text -->



<!-- Start of picture text -->
|E|<br><!-- End of picture text -->

**Figure 4.4:** a) Screenshot from CST Microwave Studio, the resonator and ground plane are modelled as perfect electrical conductors with a transmission line connecting ports 1 and 2. b) Using the frequency domain solver the transmission (S21) is simulated and a resonance is observed at 4 _._ 89 GHz. The magnetic (c) and electric (d) field profiles of the resonant mode at 100 nm below the resonator. 



<!-- Start of picture text -->
Ld<br><!-- End of picture text -->



## Ld 



_66_ 

_4.1. Resonator Design_ 



The current density distribution across the wire can then be calculated using: 



where _w_ and _t_ are the width and thickness of the wire and _λ_ is the penetration depth. The current density is assumed to be uniform in _y_ . To ensure normalisation: 



The impedance can be estimated using calculations for the capacitance (via equation 4.1 or simulations using FasterCap/Sonnet) and the resonant frequency (from CST). The characteristic impedance is typically _Z_ 0 _≈_ 100 Ω. Using the current density from the vacuum current fluctuations, the distribution is applied to a 2 µm wide rectangle of perfect electrical conductor, on top of a silicon (or sapphire) substrate in COMSOL. In figure 4.6 the current density distribution across a 2 µm wide, 50 nm thick wire is plotted for both a Nb wire and an NbN wire. The larger penetration depth of NbN (of 370 nm compared to 49 nm in Nb) results in a current distribution which extends further into the wire and is less dense at the edges. Using NbN, the components of the magnetic field are plotted. Directly below the wire the field is predominantly in the _x_ component, while at the edges along _y_ . As the external magnetic field is applied in the resonator plane, this allows for regions where both S _x_ and S _z_ spin transitions can be investigated (although the latter is not measured in this thesis). The magnitude of the field is largest at the corners of the resonator, this is because the largest current density is at the edges of the wire. 

tion using: 



_67_ 

_4.1. Resonator Design_ 

where _⟨m_ intial _| S_<sup>ˆ</sup> _x |m_ final _⟩_ is the matrix element of the measured spin transition and _γe_ is the gyromagnetic ratio. In order to facilitate a fair comparison between resonators, the external magnetic field is orientated along the length of the wire so that _|δ B|_ = _δ B_<sup>2</sup> _x_ + _δ B_<sup>2</sup> _y_ and the matrix element is set to 1 _/_ 2, with the electron, having ~~�~~ g-factor = 2. The resulting single-spin coupling strength distribution is plotted in figure 4.6. 

Similar analysis is followed for the spiral design. Here, the current flows in alternating directions between each of the spiral arms. A 10 µm wide track (50 nm thickness) of NbN results in the current density distribution seen in figure 4.7. The opposite current polarity between two sides of the spiral produces a magnetic field which has opposite polarity _Bx_ on each side. The resulting field magnitude is more homogeneous at far field that that of the thin-ring and higher field strengths are measured over a broad area (figure 4.8). This allows for much more control over the spin ensemble 

###### **4.1.3 Characterisation** 

Both the CST and COMSOL simulations inform the resonator design. Once the frequency and field properties are estimated, the designs can be fabricated using the cleanroom at the LCN. The fabrication process is outlined in section 3.4. At the LCN, the following pieces of equipment are used in each step: 

- **NbN Deposition** : _SVS V6000 confocal sputterer_ 

- **Photolithography** : _Heidelberg DWL 66_<sup>+</sup> 

- **Plasma Etching** : _Oxford Instruments Plasma Pro NGP80 RIE_ . 

Typically 9-12 resonators are patterned onto one 5x5 mm chip, all of which target different frequencies. Using a<sup>4</sup> He closed-loop cryostat (outlined in section 4.2.2) the resonant frequencies and quality factors are measured. This allows for a calibration of the resonators which informs the subsequent design to target specific frequencies. 

A home-built characterisation probe is used to measure the resonators in the cryostat. The probe consists of two RF lines with a HEMT cryo-amplifier on the output. The sample is mounted in a copper box to shield it from noise. In the box, the resonators are either coupled via antenna or capacitively coupled to a CPW. DC connections on the probe allow for power to be supplied to the amplifier and a thermocouple to be attached to the copper box. The RF lines are connected to each port on a VNA and the transmission is measured. A picture of this probe is shown in figure 4.9. 

_68_ 

_4.1. Resonator Design_ 



<!-- Start of picture text -->
Z  = 100 Ω<br>0<br>f = 5 GHz Nb<br>NbN<br><!-- End of picture text -->



<!-- Start of picture text -->
30<br>0<br>-30<br><!-- End of picture text -->



<!-- Start of picture text -->
1.0<br>B B<br>x y<br>0.0<br>-1.0<br>-2 0 2 -2 0 2<br>x (μm) x (μm)<br><!-- End of picture text -->



<!-- Start of picture text -->
1.0<br>|B|<br>0.0<br>-1.0<br><!-- End of picture text -->





<!-- Start of picture text -->
0.0<br>B<br>0<br>-1.0<br><!-- End of picture text -->



<!-- Start of picture text -->
900<br>0<br><!-- End of picture text -->

**Figure 4.6:** COMSOL simulation of the inductor in a thin-ring resonator. a) Using equations 4.3-4.5 the current desnity distribution can be calculated across the width of the inductor. Given the higher penetration depth of NbN compared to Nb the current is more uniform accross the wire. b) Using the NbN current profile the x and y components of the magnetic field can be generated, below the wire the field is predominately along the x direction while at the edges it is along y. c) The magnitude of the magnetic field from the wire, the corners of the wire have the maximal field as the supercurrent is largest along the egde of the wire. d) using equation 4.6 with a matrix element of 1, the approximate single-spin coupling strength distribution is simulated, the external _B_ 0 field is assumed to be pointing along the length of the inductor meaning both _By_ and _Bx_ contribute to the coupling strength. 

# ~~<u>i 1</u>~~ 





<!-- Start of picture text -->
5]<br><!-- End of picture text -->



<!-- Start of picture text -->
i<br><!-- End of picture text -->

_4.1. Resonator Design_ 

_70_ 



<!-- Start of picture text -->
20 560<br>Spiral<br>Thin-ring<br>0 0<br>-200 -160 -120 -80 -40 0<br>y (μm)<br>Field Strength (nT)<br>Coupling Stength (<br>Hz<br>)<br><!-- End of picture text -->

**Figure 4.8:** The field and single spin coupling strength distribution for the spiral and thinring designs. From the centre of the resonator the spiral design is much more homogeneous through the substrate than the thin-ring design which follows a 1/ _r_ dependence. 

Once the NbN thermalises below its _Tc_ (typically between 7 - 8 K for thin flims), the resonators can be measured. Using the VNA the frequency of the output _−_ is swept with typically low power ( 50 dBm) to ensure the resonators are not overdriven. Sharp dips in transmission (S21) indicate a resonator is on resonance and narrower sweeps around the resonance frequency are performed. 

To characterise the resonators a Fano resonance is fitted to the transmission [190,191]: 



where _f_ is the VNA frequency, _f_ 0 is the resonant frequency of the resonator, ∆ _f_ is the full-width-half-maximum (FWHM) of the resonance, and _q_ is the Fano asymmetry parameter which describes the interaction of the resonance with the background transmission. When _q_ = 0, the fit returns a standard Lorenzian. The Fano fit allows the transmission via the resonator to be extracted from the direct transmission between the two antennae or along the CPW. 

Figure 4.10 shows a large VNA trace from 2 GHz to 3 GHz where several sharp features corresponding to the resonators are observed. A VNA trace around the resonator frequency itself and the Fano resonance fit is shown, along with the fitted frequency and quality factor. To calibrate the spiral design, the length of the spiral is increased. This increases both the capacitance and the inductance and therefore reduces the resonant frequency, additionally the kinetic inductance becomes more critical as the length is increased further. A linear fit is used to calibrate the length and frequency with a gradient of _−_ 51 MHzmm<sup>_−_1</sup> and an offset of 3029 MHz. Using this, resonators targeting the ZEFOZ point of<sup>171</sup> Yb:YSO at 2370 MHz can be 

_4.1. Resonator Design_ 

_71_ 



<!-- Start of picture text -->
RF Lines<br><!-- End of picture text -->



<!-- Start of picture text -->
RF Lines<br>DC Lines Copper Cavity<br>HEMT<br><!-- End of picture text -->

**Figure 4.9:** Photo of the characterisation probe compatible with the closed-loop cryostat. The probe is fitted with a HEMT cryo-amplifier to allow for measurement of superconducting resonators in the low power limit. The resonators are placed in the copper cavity and coupled to the transmission RF lines via antennae. Photo taken by Dr Gavin Dold [63]. 



<!-- Start of picture text -->
a) b)<br>-15<br>-16<br>f = 2682 MHz<br>Q = 42,000<br>-45 -20<br>2000 2400 2800 2674 2682 2690<br>c) 2600<br>2450<br>2300<br>10 11 12 13<br>Frequency (MHz) Frequency (MHz)<br>Spiral Length (mm)<br> (dB)  (dB)<br>21 21<br>S S<br>Frequency (MHz)<br><!-- End of picture text -->

**Figure 4.10:** Resonator characterisation. Using a vector network analyser (VNA), the transmission through the cavity can be measured. In the region 2 – 3 GHz several sharp features are observed (a)), these correspond the to resonators. b) Applying a Fano fit to the trace (equation 4.7) allows the resonator frequency and quality factor to be extracted. c) A calibration of spiral length vs resonant frequency allows for the ZFEOZ point at 2370 MHz to be accurately targeted. Using a linear fit a length of 12 _._ 7 mm should be used to hit the ZEFOZ point. 

fabricated more accurately. Using the calibration, a spiral of length 12 _._ 7 mm should be used to target the ZEFOZ point, however imperfections in the fabrication process means a scatter gun approach to hitting specific frequencies should still be used. 

To use superconducting resonators in ESR experiments, they need to withstand 

_4.1. Resonator Design_ 

_72_ 



<!-- Start of picture text -->
2471<br>15<br>10<br>5<br>0<br>2466<br>-5<br>a) b)<br>B = 20 mT<br>-4 0 4 0 20 40 60 80 100<br>θ (o) Field Magnitude (mT)<br>Frequency (MHz)<br>)<br>o<br>Aligned θ (<br><!-- End of picture text -->

**Figure 4.11:** Field alignment to the resonator frame. a) The angle of the field is varied to find the maximum resonator frequency. As the component of the out of plane field increases the resonator tunes down, the field is then aligned to minimise the out of plane field. b) In some cases the aligned angle varied with the field magnitude, this indicates a distortion of the magnetic field – in this case a magnetised SMA elbow connector. 

magnetic fields of several hundred milliTesla. By aligning the magnetic field to the plane of the resonator, the field vector points through the edge of the resonator which is only 20 nm thick. This reduces the amount of flux through the superconductor and much higher field strengths can be reached before quenching the superconductor compared with applying the field out of plane to the resonator [178]. In order to align the magnetic field to the resonator frame, the resonant frequency is tracked, while the field angle is rotated, the frequency is maximum when the field is in the plane of the resonator. In figure 4.11a) an example of the alignment is shown. A polynomial can be fit to the frequency shift and the aligned _θ_ and _φ_ are determined. This can then be used to form a rotation matrix from the lab (magnet) frame to the resonator frame. The alignment is conducted at increasing magnetic field strengths, while ensuring the maximum out of plane field is less than only 1 – 2 mT, this gives a more accurate alignment and allows the resonator to be used at fields of over 1 T. During some experiments with the resonators mounted on a PCB it was found that the aligned theta varied significantly with field magnitude (figure 4.11b)). It was found that some SMA elbow connectors on the PCB were becoming magnetised and distorting the magnetic field, this effect could be saturated at high fields as observed by the plateau in aligned angle. However this was a problem for performing measurements at fields below 100 mT – specifically ZEFOZ experiments. A new PCB design was created with new elbow connectors. The PCB was made long enough that the resonators were far from any connectors or PCB components, this is shown in at the bottom of figure 4.14. 

_4.2. Cryostats_ 

_73_ 

##### **4.2 Cryostats** 

In order to observe superconducting resonators and perform quantum memory experiments cryostats are need to cool the device down to well below the _Tc_ . Two different cryostats are used in the experiments in this thesis, the first a closed-loop 4He cryostat used for resonator characterisation and a dilution refrigerator used for milliKelvin ESR experiments. 

###### **4.2.1 Closed-Cycle Cryostat** 

A<sup>4</sup> He closed-cycle cryostat (Cryogenic Ltd.) was used to perform resonator characterisation. With an approximate base temperature of 1 _._ 6 K, it is sufficient to allow for Nb and NbN resonators to be measured as their bulk critical temperatures are 9 _._ 3 K and 16 _._ 2 K respectively. In addition, the nature of the closed-cycle cryostat allows for fast prototyping of several resonators. The probe can be inserted and cooled to base temperature within 3 hours, allowing for multiple chips to be measured in one day (as opposed to several days in a dilution refrigerator). 

The characterisation probe outlined in section 4.1.3 was designed to fit within the cryostat, and has several flanges allowing for the He flow to be restricted and a lower temperature reached. To ensure good thermalisation, copper wire was added to the bottom of the probe so that it is well thermalised to the base temperature. 

The cryostat sits within an ESR magnet (Bruker ER073) and is positioned on a mechanical rotation stage which allows the probe to be rotated in the magnetic field. This not only allows for the magnetic field resilience of the resonators to be tested but is also used for 3D cavity ESR (not presented in this thesis). 

###### **4.2.2 Dilution Refrigerator** 

For quantum memory applications, where spins exhibit long coherence and superconducting qubits operate, temperatures below 100 mK are required. In order to achieve such low temperatures,<sup>4</sup> He alone cannot be used as this will only allow for temperatures around 1 K to be reached. A dilution refrigerator is needed to reach the coldest temperatures and is now a staple piece of equipment in solid state quantum computing experiments. In order to observe quantum effects we utilise quantum mechanics to achieve milliKelvin temperatures. A dilution refrigerator uses a combination of<sup>4</sup> He and the much less abundant<sup>*3</sup> He isotope.<sup>3</sup> He has a much larger specific heat capacity and lower vapour pressure compared to its heavier isotope allowing for temperatures to be cooled to approximately 300 mK [192]. 

In order to reach sub-100 mK temperatures the phase boundary between dif- 

- *And much more expensive! 

_4.2. Cryostats_ 

_74_ 



<!-- Start of picture text -->
3He Concentration (%)<br>2.0<br>Normal<br>1.5   Fluid<br>Fermi-Liquid 3He<br>1.0 Superfluid 4He<br>Forbidden<br>0.5<br>6.6%    Region<br>0.0<br>0 25 50 75 100<br>Temperature (K)<br><!-- End of picture text -->

**Figure 4.12:** The phase diagram of<sup>3</sup> He and<sup>4</sup> He mixture. As the temperature is decreased the mixture forms two phases; a dilute phase where the<sup>4</sup> He forms a superfluid in which a low concentraion of<sup>3</sup> He is present, and a concentrated phase which has a high percentage of<sup>3</sup> He. At very low temperatures<sup>3</sup> He is forced across the phase boundary from the concentrated phase to the dilute phase resulting in an endothermic process which supplies significant cooling power. 

ferent concentrations of<sup>3</sup> He and<sup>4</sup> He is exploited. The phase diagram of helium-3,4 mixture is shown in figure 4.12. At low temperatures (below _≈_ 850 mK) the helium mixture undergoes a phase separation forming a concentrated (high<sup>3</sup> He content) and a dilute (low<sup>3</sup> He content) phase. As the temperature is lowered further the phase separation between the two becomes larger, as _T →_ 0 K the dilute phase reaches a concentration of 6.6 %<sup>3</sup> He while the concentrated phase is 100 %<sup>3</sup> He. These two phases sit on-top of each other with the denser, concentrated phase floating above the dilute mixture. 

Once the phase separation is formed, an external pump is connected to the dilute phase, evaporating some of the<sup>3</sup> He. In order to preserve the concentration of 6.6 %,<sup>3</sup> He moves across the phase boundary from the concentrated to dilute phase. This process is endothermic and the cooling power of the refrigerator is directly proportional to the flow rate across the concentrated-dilute phase boundary. 

In a real dilution refrigerator, a pulse tube refrigerator circuit cools the<sup>3</sup> He to below 4 K. Below this, the evaporation of the dilute mixture forms a boundary and cooling to approximately 800 mK - this is known as the ‘still’ stage. The incoming concentrated mixture is thermalised with this stage before it reaches the dilute phase boundary. The lowest, and coldest part of the dilution refrigerator is the mixing chamber (MXC), here the phase boundary forms and the concentrated 

_75_ 

_4.2. Cryostats_ 



<!-- Start of picture text -->
4He<br>3He conc.<br>3He dil.<br>3He gas<br>Heat Exchanger<br>Pulse Tubes<br>4K<br>STILL<br>MXC<br>Sample<br><!-- End of picture text -->

**Figure 4.13:** Schematic of the mixture circuit of a dilution refrigerator. The<sup>3</sup> He is precooled to below 4 K by coupling to a pulse tube circuit. From this point the 3He is cooled further by coupling to the still stage (cooling arising from evaporating the<sup>3</sup> He from the dilute phase). Below _≈_ 800 mK a phase boundary forms between the concentrated and dilute phases of the helium mixture. At the mixing chamber (MXC) the sample is thermally coupled to this boundary. As<sup>3</sup> He is pumped away from the dilute phase, more<sup>3</sup> He flows across the phase boundary supplying cooling power to reach temperatures below 10 mK. 

> 3He sits above the dilute mixture. The dilute mixture is pumped away allowing for the flow of<sup>3</sup> He across the phase boundary, the sample is then thermally coupled to the boundary to achieve maximum cooling power and temperatures below 10 mK. A schematic of the dilution refrigerator is shown in figure 4.13 

All the experiments in the results chapters were conducted within a BlueFors LD-400 dilution refrigerator [193] (figure 4.14) with an American Magnetics (1,1,3) T superconducting vector magnet. A fast-loading mechanism is used to cool the puck and sample down. This allows for rapid prototyping of devices as the cooldown cycle is approximately 8 hours compared to several days for a full dilution fridge cooldown. Resonator frequencies are measured, if they are not within reach of a spin line new devices can be fabricated the same day and be cooled down for the subsequent day – significantly reducing measurement downtime. 



<!-- Start of picture text -->
> Wp =m = =<br>SAMPLE<br>a TR<br><!-- End of picture text -->

_4.3. ESR Setup_ 

_77_ 

##### **4.3 ESR Setup** 

To perform high-sensitivity ESR and implement quantum memory protocols a spectrometer is needed. The spectrometer sends and retrieves microwave signals to and from the spins. It needs to meet several specifications to be useful for quantum memory applications; capable of producing high power ( _>_ 1 W) shaped pulses, detect weak signals, have a low noise figure and perform operations on a sub µs timescale. 

ESR spectrometers for quantum memory experiments are formed of three main pieces of equipment – an arbitrary waveform generator (AWG), a vector signal generator (VSG) and a digitiser. The AWG allows for RF pulses to be generated with control of the shape and phase information of the waveform. For ESR in the GHz regime, a VSG is needed to mix the AWG signals (typically DC-100 MHz range) up-to GHz frequencies while preserving phase coherence. Finally the digitiser is used to detect the final signal and send the data to the PC. In order for these three components to interact efficiently, and to provide switching and amplification, an ESR bridge is needed. The bridge is comprised of microwave components such as amplifiers, switches and IQ mixers. Typical ESR bridges are large, cumbersome pieces of equipment, however for low-noise applications (such as quantum memories) they can be scaled back to their most crucial elements. In figure 4.15 the circuit diagram for the spectrometer is outlined. In its simplest form, the output path of ESR bridge requires an amplifier (here we use a 3 W solid state amplifier, Mini-Circuits ZVE-3W-83) to allow for high-power pulses and switches to isolate the sample from background noise arising from the amplifier. The switches operate on a nanosecond time scale and are controlled via a marker sent from the AWG, they are only open when a pulse is sent from the AWG and closed otherwise. The main component on the detection path is the IQ mixer, this demodulates the ESR signal from the GHz carrier frequency with use of a local oscillator (LO) supplied from the VSG. This puts the signal into low frequency which is measurable by the digitiser. 

The ESR setup extends into the dilution refrigerator where careful consideration of noise is needed. On the input line 30 dB attenuation is applied to the signal, this reduces the noise from room temperature components and acts as a safety measure against sending too high power pulses to the sample. 20 dB is placed at the 4 K plate which reduces the noise from room temperature to _≈_ 3 K. A 10 dB attenuator at the mixing chamber as well as the 10 dB attenuation on the PCB reduces the noise to 30 mK which is negligible compared with the noise from components on 

_4.3. ESR Setup_ 

_78_ 

the mixing chamber plate. 0 dB attenuators are fitted at each stage, these thermally connect the central conductor of the coaxial cable to each stage and reduces thermal noise. 

The PCB is made of a coplanar waveguide (CPW) with a narrow constriction in the middle. The constriction was designed to have an insertion loss of 10 dB at 2.5 GHz. The sample is placed onto the CPW after this constriction allowing for the emitted signal to be reflected off the constriction and go up the detection line rather than be lost on the input line (the PCB is shown in figure 4.14). After the PCB the output (detection) line has the same 0 dB attenuators as the input line (we want to attenuate thermal noise but not the microwave signal). A circulator is placed on the mixing chamber, this sends noise coming down the detection path into a 50 Ω load while allowing the signal to continue upwards. The first amplification of the signal comes at the 4 K stage using a high electron mobility transistor (HEMT) amplifier. The detection path is then amplified further at room temperature in the ESR bridge. 

_4.3. ESR Setup_ 

_79_ 



<!-- Start of picture text -->
Keysight M9336A<br>Keysight M9023A<br>LNF-LNC1.5_6A<br>R&S SGS100A<br>MiniCircuits<br>IQ-1545LMP<br>Quinstar<br>2.5-4GHz<br>AWG 50K<br>Digitiser<br>I Q<br>VSG LO 4K<br>L<br>RF I Q<br>Fast Switch R STILL<br>SSA<br>COLD<br>MXC<br>PUCK<br>+27 dB<br>0 dB<br>0 dB<br>0 dB<br>Input Output<br>To Input From Output<br>0 dB 0 dB<br>0 dB<br>HEMT<br>20 dB<br>0 dB<br>0 dB<br>10 dB<br><!-- End of picture text -->

**Figure 4.15:** Schematic of the ESR setup at room temperature (left) and within the dilution refrigerator (right). Outside the fridge the AWG and digitiser are within the same PXI chassis in the PC. The AWG sends a waveform with I and Q information which is modulated by the VSG to GHz frequencies. This is then amplified and sent to the sample. The fast switches open to allow the pulse through and protect the sample from noise from the solid state amplifier (SSA). The pulses are sent down a 30 dB attenuated line in the fridge which removes room temperature thermal and microwave noise. The signal is amplified on the detection path with a HEMT amplifier before joining back into the ESR bridge were it is demodulated via an IQ mixer. DC signal is then sent to the digitiser for detection. 

##### **Chapter 5** 

### **Decoherence in Rare-Earth Doped Crystals** 

_If you always win, then you’re probably doing something wrong._ 

|||Scott Aaronson|
|---|---|---|
|**Contents**|||
|**5.1**|**Continuous Wave ESR**<br>**. . . . . . . . . . . **|**. . . . . . . . . .**<br>**81**|
|**5.2**|**Pulsed ESR . . . . . . . . . . . . . . . . . . **|**. . . . . . . . . .**<br>**85**|
||5.2.1<br>Spin Relaxation Time,_T_1 . . . . . . .|. . . . . . . . . .<br>85|
||5.2.2<br>Spin Coherence Time,_T_2 . . . . . . .|. . . . . . . . . .<br>88|
|**5.3**|**Instantaneous Diffusion . . . . . . . . . . . **|**. . . . . . . . . .**<br>**89**|
|**5.4**|**Spectral Diffusion . . . . . . . . . . . . . . **|**. . . . . . . . . .**<br>**92**|
||5.4.1<br>Temperature Dependence . . . . . . .|. . . . . . . . . .<br>95|
||5.4.2<br>Stimulated Echo<br>. . . . . . . . . . .|. . . . . . . . . . 101|
|**5.5**|**Discussion**<br>**. . . . . . . . . . . . . . . . . . **|**. . . . . . . . . . 105**|



Understanding decoherence in spin systems is vital for building a useful quantum memory. Having a good grasp on the sources of decoherence and the physical mechanisms which underpin them allows for techniques to be developed and used to overcome decoherence and extend memory times. Spectral diffusion has been shown to be a limiting decoherence mechanism in many spin systems such as donor spins in silicon [53, 194–196], NV centres in diamond [197, 198] and rare-earth doped crystals [64,111,134,199]. These mechanisms, while extensively measured 

_5.1. Continuous Wave ESR_ 

_81_ 

using conventional 3D cavity ESR, are not particularly well studied using superconducting microresonators in the high-cooperativity regime - as is needed for a quantum memory. 

In this chapter, we explore the decoherence mechanisms in two rare-earth doped YSO crystals coupled to NbN microresonators. We predominately study natYb:YSO; using continuous wave ESR to identify spin species and crystal orientation, and pulsed ESR to explore two decoherence mechanisms - instantaneous and spectral diffusion. In the latter case, we compare with a second rare earth system -<sup>145</sup> Nd:YSO. The data used to compare was taken by Dr. Gavin Dold [63], however new analysis presented here provides new insights into the decoherence mechanisms at play. 

##### **5.1 Continuous Wave ESR** 

Before any experiments into the spin system can take place, we must first identify spin transitions. CW ESR provides a fast and sensitive way of exploring the spin structure of the crystal from which different spin species can be identified. Superconducting resonators have a high quality factor (> 50,000), they are therefore well suited to CW ESR as changes in their linewidth can be easily identified. 

After the external field has been aligned to the resonator plane (see section 4.1.3), fields can be swept to 1 T without significant reduction in the Q factor. A VNA is used to track the frequency and lineshape of the resonator as the external field is swept (using a (1,1,3) vector magnet). As the resonator moves on resonance with a spin transition its linewidth broadens. This is due to the spins acting as a loss mechanism for the resonator. In addition, the centre frequency of the resonator shifts as it hybridises with the spin transition. In the case of strong coupling this forms an avoided crossing, whereby the resonator and spins act as one quantum system. 

In figure 5.1a) a heatmap is plotted of the VNA transmission (S21) at each field step. Several spin transitions can be observed, which can be identified using simulations of the Yb spin system via EasySpin [156]. 

Yb spins in both sites can be observed, with those in site 1 resonant at lower fields (< 50 mT). Two large avoided crossings are observed at 100 mT and 106 mT, this corresponds to the isotopes with zero nuclear spin (<sup>I=0</sup> Yb) in site 2, this transition is split due to the lifting of the subsite degeneracy from a slight field applied along the _b_ crystal axis.<sup>I=0</sup> Yb isotopes comprise 70% abundance in<sup>nat</sup> Yb compared to 15%<sup>171</sup> Yb which has _I_ = 1 _/_ 2. Figures 5.1b,c) show how the resonator frequency and linewidth vary as the field is increased. The resonator linewidth broad- 

_5.1. Continuous Wave ESR_ 

_82_ 

ens for fields between 50-100 mT, this corresponds to spins with the free-electron g-factor ( _g_ = 2). These impurity spins which may be in the crystal, superconductorcrystal interface or on the surface of the superconductor act as a two-level-system (TLS) loss for the resonator and reduce its Q factor. When the field is increased well beyond the _g_ = 2 frequency, these spins become polarised and can no longer be excited by the resonator, this results in the Q factor increasing to over 60 _,_ 000. In figure 5.1d) the S21 traces of the resonator are plotted at different fields. When the resonator is on resonance with the<sup>I=0</sup> Yb spins (100 mT) the prominence decreases as the resonator couples to the spins rather than the CPW. 

The large anisotropy in Yb g-tensor results in spin resonant fields which vary with applied field angle. In order to target specific transitions we need to deduce the orientation of the crystal axes with respect to the lab frame. To do this several CW fields sweeps are performed while the applied field angle is varied in the plane of the resonator. The crystal is cut so that the D1-D2 axes are approximately in plane with the resonator and the b axis is perpendicular. Therefore angular sweeps in the resonator plane are approximately sweeps in the D1-D2 plane with some offset between D1 and x, and b and z. 

Figure 5.2 shows the CW field sweeps for different angles in the lab (x-y) frame. The two large<sup>I=0</sup> Yb avoided crossings provide a clear marker which can be tracked as the angle is rotated. As the field is rotated, the resonant field of the spin transitions increases. As the field is swept in a raster pattern the dispersive frequency shift of the resonator is either positive or negative if the field is swept from low to high or from high to low. The _g_ = 2 spin line is stationary with field angle as the free electrons has no anisotropy. 

offset between the lab frame and the crystal frame can be determined. A roadmap of the spin transitions is plotted in figure 5.3, an offset of _−_ 10<sup>_◦_</sup> is applied to the data in figure 5.2, this then corresponds well to the EasySpin simulations of both I=0 171 _◦_ Yb and Yb. In addition, an offset of 1 _._ 2 between the crystal b axis and the lab frame is applied. 

We note the hysteresis behaviour observed in figure 5.2. It is believed the high VNA power results in the spin system occupying one branch of the avoided crossing arising from bistability of the the resonator-spin system. This phenomena occurs when there is strong coupling between the spins and the resonator. 

explored. To do this pulsed ESR techniques must be used 







<!-- Start of picture text -->
=<br><!-- End of picture text -->





<!-- Start of picture text -->
TT<br><!-- End of picture text -->

~~<u><mark>Ea] m= mC —</mark></u>~~<sup>~~<u><mark>espe</mark></u>~~</sup> ~~<u><mark>|</mark> [</u>~~ ~~<mark>m=</mark>~~ ~~<u><mark>=</mark></u>~~ 

_5.2. Pulsed ESR_ 

_85_ 

##### **5.2 Pulsed ESR** 

Pulsed ESR is a crucial tool in measuring and understanding decoherence. The Hahn echo sequence is a staple of all the measurements in the subsequent chapters and is the first pulsed ESR measurement that is performed with any device. 

Having aligned to the crystal frame using a resonator with frequency 2373 MHz, we explore the decoherence mechanisms of Yb in the high-frequency, high field regime. This allows us to be far from the ZEFOZ point at zero-field, and puts us in an environment where ∇B _f_ is constant w.r.t local field (for constant angle). Using a different (but still spiral shape) resonator on the chip, with resonant frequency of 5042 _._ 8 MHz at 0 mT, we perform an echo detected field sweep (EDFS) along the D2 axis. An EDFS consists of performing a Hahn echo sequence while sweeping the applied magnetic field. When a spin transition is resonant with the resonator an echo will form, an example of which is shown in figure 5.4. Taking the magnitude of the _I_ and _Q_ components of the signal allows for the signal to be unaffected by fluctuations in phase. By integrating the echo, the intensity of the signal can be measured and spin transitions can be observed. In figure 5.5 both the CW (a,b)) and the echo-detected (c)) field sweeps are plotted. As the field is swept the frequency of the VSG (and therefore the pulses) is set to the measured centre frequency of the resonator. This allows for the pulses to be kept on resonance with the resonator as it tunes down in frequency due to flux from the external field. The avoided crossings in the CW sweep match well with echo signals measured in the EDFS. The intensity of the<sup>I=0</sup> Yb transitions at _≈_ 310 mT are lower than that of the<sup>171</sup> Yb transition at 370 mT even though the avoided crossing is much stronger. This is due to the resonator prominence and Q factor decreasing at the centre of the crossing (observed in figure 5.5b)), this means the power transmitted to the spins is much less than that in the<sup>171</sup> Yb case where the Q factor drop is not as pronounced. 

The<sup>171</sup> Yb transition at 370 mT is used to study decoherence, this corresponds to the 2-3 transition in site 2. Before decoherence mechanisms are studied the relaxation rate _T_ 1 is measured. This allows for the shot repetition time of the experiment to be determined so that the spin system is in a steady state. 

###### **5.2.1 Spin Relaxation Time,** _T_ 1 

The relaxation rate, _T_ 1 is an important parameter in both understanding the spin environment and also optimising experimental procedures. _T_ 1 is the characteristic time in which spins relax to their ground state, this can happen via interactions in the crystal environment, or, in the presence of a cavity, via Purcell relaxation (see section 2.4.3). 

_5.2. Pulsed ESR_ 

_86_ 



<!-- Start of picture text -->
π<br>2 π<br>60<br>I<br>Q<br>40<br>20<br>0<br>0 20 40 60 80<br>time (μs)<br>Signal (mV)<br><!-- End of picture text -->

**Figure 5.4:** An example of a Hahn echo. With a _τ_ of 40 µs the echo forms 40 µs after the _π_ pulse, the data begins 10 µs after the pulse. The echo is observed in both in-phase (I) and quadrature (Q) channels, In an EDFS the magnitude of these components is measured. The ring down of the resonator is observed at short times after the _π_ pulse, this restricts the shortest _τ_ time to _≈_ 30 µs. 

In order to measure the relaxation rate, the spin ensemble needs to be put into the inverted (excited) state. To do this, a _π_ pulse needs to be applied to the entire ensemble. By nature, microresonators produce inhomogeneous _B_ 1 fields resulting in an inhomogeneous _π_ pulse across the ensemble. To compensate for this, we use adiabatic fast passage to invert the spins (see section 2.3.1). A WURST pulse with length 150 µs is applied. The resulting echo has a magnitude which is _≈_ 87% compared to a standard Hahn echo. This shows the WURST performs an inversion with high efficiency. To measure the _T_ 1 relaxation a Hahn echo sequence is then performed time _TW_ later. The _τ_ time used in the sequence is small so that _T_ 2 effects are not visible, here a _τ_ of 40 µs was used. By increasing the length of _TW_ the time for which the spins are in the excited state is increased, as more spins relax to the ground state, the resulting echo signal evolves from negative to positive. 

Due to the planar nature of microresonators, the coupling strength to the resonator decreases for spins deep in the bulk. Those close to the resonator will be strongly coupled and the main relaxation mechanism will be Purcell relaxation. Those far from the resonator will be very weakly coupled, this means the dominant relaxation mechanism for these spins will be interactions with crystal phonons. We therefore expect the _T_ 1 measurement to show a distribution of decay rates. To fit to the data we model this as a fast rate which encompasses the Purcell regime and a slower rate which involves spins for which _T_ 1 is phonon limited [61]. 

In figure 5.6 the echo magnitude of the inversion recovery is plotted. Due to significant phase noise in the experiment the magnitude of the echo is plotted rather than the _I_ and _Q_ components. For this reason the echo signal remains positive (even 

_5.2. Pulsed ESR_ 

_87_ 



<!-- Start of picture text -->
5046 a)<br>5042<br>5038<br>50k<br>b)<br>30k<br>10k<br>60 c)<br>40<br>20<br>0<br>171Yb<br>I=0Yb<br>171Yb<br>I=0Yb<br>100 150 200 250 300 350 400<br>Field (mT)<br>Frequency (MHz)<br>Q Factor<br>Echo Signal      (mV)<br><!-- End of picture text -->

**Figure 5.5:** a) Resonator frequency as external field is swept along the D2 axis. Several Yb spin transitions are observed by the dispersive frequency shift of the resonator. b) Quality factor of the resonator during the field sweep. The drop in Q factor during the large avoided crossing at 10 mT means less power is transferred to the spins during the Hahn echo sequence. c) Echo detected field sweep along D2. At each field step a Hahn echo sequence is performed, the magnitude of the echo is calculated and then integrated to form the echo signal. Several spin transitions are observed, including the<sup>171</sup> Yb transition at 370 mT which is used to study decoherence in the crystal. 

when inverted). of a biexponential [63]: 



where, the decay of the echo amplitude ( _A_ ) is dependent on a fast _T_ 1 _,_ fast and slow _T_ 1 _,_ slow with respective amplitudes ( _C_ fast(slow)). _C_ echo is the echo amplitude with no inversion. Fitting equation 5.1 in figure 5.6 gives good agreement with the data and yields _T_ 1 _,_ fast=(0 _._ 12 _±_ 0 _._ 02) s and _T_ 1 _,_ slow=(19 _±_ 3) s. The relative amplitudes of the components is _C_ fast = (4 _._ 0 _±_ 0 _._ 8) mV and _C_ slow = (22 _±_ 1) mV 

_5.2. Pulsed ESR_ 

_88_ 



<!-- Start of picture text -->
πw π 2 π<br>B = 371 mT   f  = 5.04 GHz<br>T   = 0.12 ± 0.02 s<br>1,fast<br>T  = 19 ± 3 s<br>1,slow<br>T  (s)<br>W<br>20<br>10<br>0<br>-10 T<br>W<br>10-3 10-2 10-1 100 101 102<br>Echo Amplitude (mV)<br><!-- End of picture text -->

**Figure 5.6:** Measurement of _T_ 1 using inversion recovery. A WURST pulse is used to invert the spin ensemble and then a Hahn echo is used to measure the polarisation after time _TW_ . The magnitude (strictly positive) echo is measured and equation 5.1 is fitted to the data. A fast _T_ 1 corresponding to the Purcell rate and a slow _T_ 1 corresponding to phonon relaxation are determined. 

###### **5.2.2 Spin Coherence Time,** _T_ 2 

At milliKelvin temperatures the _T_ 1 time is several hundred milliseconds - even in the Purcell regime. The factor limiting quantum lifetimes of these timescales is decoherence. _T_ 2 is the time for which a quantum state remains isolated from its environment. In the Bloch sphere picture this is the time for which the state vector decays from the surface of the sphere (pure state) to the centre of the sphere (maximally mixed state). To measure this, the time for which the state remains in a superposition state must be varied. 

A Hahn echo is used to measure _T_ 2. The time between the two pulses, _τ_ , is increased to well beyond the the point at which the signal is below the noise floor. The time for which the spins are on the equator of the Bloch sphere is 2 _τ_ . Due to the presence of significant phase noise in many of the experiments, the echo magnitude is plotted. This requires the exponential fit to account for the noise floor ( _C_ noise) which does not average to zero. This results in the fit: 



where _C_ 0 is the amplitude of the echo at _τ_ = 0. Often in ESR experiments, the decay curve is better described by a stretched exponential, where a stretch factor, _β_ , is introduced [200,201]: 

_5.3. Instantaneous Diffusion_ 

_89_ 



In figure 5.7a,b) the phase noise is seen where the echo amplitude in _I_ and _Q_ after _≈_ 100 µs, this is clearly seen in the phase of the echo. Figure 5.7c) shows the _T_ 2 decay in magnitude at 370 mT and 5 _._ 04 GHz. This measurement was taken at base temperature of the dilution refrigerator at 20 mK. A _T_ 2 of (3 _._ 38 _±_ 0 _._ 09) ms was measured, this is significantly long given this is well away from a ZEFOZ point and provides a basis on which the coherence can be extended by moving to regions in field-frequency space, which offer protection from the crystal environment. A _T_ 2 of over 3 ms is over an order of magnitude longer than that of planar transmon qubits [202], this is one of the benchmarks for a quantum memory. While this coherence time represents an important first step to developing a quantum memory with Yb:YSO, we must understand the decoherence mechanisms at play, which limit the _T_ 2 from being longer. By understanding the processes, which cause the spins to decohere, allow us to formulate techniques to mitigate their effects. In the following sections we explore the various decoherence mechanisms; namely instantaneous diffusion and spectral diffusion. 

##### **5.3 Instantaneous Diffusion** 

Instantaneous diffusion (ID) is a phenomena which occurs in moderately-to-highly doped spin systems [54,135]. To achieve high coupling strengths to resonators high spin densities are often used and so ID is a common decoherence mechanism in these systems. ID is a dipolar interaction between resonant spins in which spins are not refocused by a Hahn echo as they are flipped. It is typical to explore ID by varying the angle of the second pulse in the Hahn echo sequence - thereby only refocusing a subset of spins and thus varying the density of resonant spins. However, performing accurate arbitrary rotations with planar microresonators is not possible. We therefore use a different technique to vary the resonant spin density - field sweep across the spin line. Superconducting resonators have a high quality factor ( _>_ 10k), this means their linewidth ( _≈_ 100 kHz) is much narrower than the spin linewidth (1 _−_ 10 MHz). The frequency of the resonator is static with field whereas the spins resonant frequency varies according to their Hamiltonian. By performing a narrow field sweep around the point where the resonator and the spins are resonant with each other, the number of spins within the resonator linewidth can be varied. Only spins within the resonator linewidth are excited during the Hahn echo sequence and so the resonant spin density can be varied. 

_5.3. Instantaneous Diffusion_ 

_90_ 



<!-- Start of picture text -->
a)<br>B = 370 mT I<br>f = 5.04 GHz Q<br>b) π<br> π<br>2<br>-π<br>2<br>-π<br>c)<br>Magnitude<br>T  = 3.38 ± 0.09 ms<br>2<br>τ (ms)<br>15<br>10<br>5<br>0<br>-5<br>-10<br>12<br>8<br>T  (s)<br>W<br>4<br>0<br>0 2 4 6<br>Echo Amplitude (mV)<br>Phase<br>Echo Amplitude (mV)<br><!-- End of picture text -->

**Figure 5.7:** An example of a _T_ 2 measurement in the presence of significant phase noise. a) The in-phase ( _I_ ) and quadrature ( _Q_ ) components of the echo as the distance ( _τ_ ) from the _π/_ 2 and the refocusing _π_ pulse is increased. The echo fluctuates between the two components after _≈_ 100 µs. b) The phase of the echo calculated using the _I_ and _Q_ components, the phase noise is clearly observed. This means the echo magnitude has to be used to extract _T_ 2. c) The echo magnitude exhibits _T_ 2 decay where equation 5.3 is fitted, this results in a coherence time _T_ 2 =(3 _._ 38 _±_ 0 _._ 09) ms. 

_5.3. Instantaneous Diffusion_ 

_91_ 

To explore ID in the Yb:YSO sample, we use a lower frequency resonator (2 _._ 43 GHz) at high field ( _>_ 800 mT), in this regime an EDFS from 800 _−_ 1200 mT encompasses both an<sup>I=0</sup> Yb and<sup>171</sup> Yb transition. These two isotopes have very different abundances (70% and 15% respectively) and so the role of ID can be explored in spin systems with different doping densities in a single field sweep. 

During the field sweep, a _T_ 2 measurement is performed when the echo intensity is above a threshold value of 25 mV, this allows for _T_ 2 to be measured across the spin line while keeping the measurement time short. This _T_ 2 EDFS is plotted in figure 5.8 where the two relevant transitions are clearly observed. 

A substantial dip is recorded in the coherence time at the centre of the<sup>I=0</sup> Yb. At the centre of the line, the fraction of spins within the resonator linewidth is maximal. This dip in _T_ 2 suggests ID is playing a role in limiting coherence, we investigate this by modelling the spin line as a Gaussian and the resonator as a Lorenzian. A _π_ pulse of 15 µs acts as a filter on the resonator limiting its bandwidth to 66 kHz. The overlap of the spin line with linewidth _γ_ = 8 _._ 7 MHz with the resonator with linewidth 66 kHz results in a proportion of the total spin density which is resonant. In figure 5.9 the two lines are plotted and the proportion of resonant spins is shaded. Using nominal doping density of 50ppm with<sup>I=0</sup> Yb abundance of 70% and equal site population, the resonant spin density is calculated and plotted. 

Using this estimate of the resonant spin density ( _n_ ( _B_ )), an estimate of _T_ 2 can be calculated using: 



where _g_ is the effective g-factor which is calculated from EasySpin simulations given the applied field orientation and magnitude. 

Plotting equation 5.4 in figure 5.10 and overlaying it onto the measured _T_ 2 data we see it accurately reproduces the data with no fit parameters. We can therefore assert that ID is the limiting decoherence mechanism in the<sup>I=0</sup> Yb sub-ensemble. 

In a different approach, we can use this technique to estimate the doping density. By fitting equation 5.4 to the data, leaving the nominal doping density as a free parameter an estimate of (5 _._ 5 _±_ 0 _._ 2) _×_ 10<sup>17</sup> cm<sup>_−_3</sup> is obtained. The quoted doping density is 3 _._ 5 _×_ 10<sup>17</sup> cm<sup>_−_3</sup> , however there is uncertainty in the site fraction and abundance. This new technique of measuring _T_ 2 across the spin line provides a new tool for measuring doping density in highly doped systems (ones in which _T_ 2 is ID limited.). 

Similar analysis is followed for the<sup>171</sup> Yb sample. In this case, no dip in _T_ 2 

_5.4. Spectral Diffusion_ 

_92_ 



<!-- Start of picture text -->
a)<br>3.5x1017 cm-3<br>b)<br>8x1016 cm-3<br>I=0Yb<br>171Yb<br>3<br>400<br>2<br>200<br>1<br>0 0<br>860 900 940<br>100 15<br>10<br>50<br>5<br>0 0<br>1060 1080 1100<br>Field (mT)<br>T<br>2<br> (ms)<br>T<br>2<br> (ms)<br>Echo Amplitude (mV)<br>Echo Amplitude (mV)<br><!-- End of picture text -->

**Figure 5.8:** Echo-Detected _T_ 2 Field Sweep in Yb:YSO with a 2 _._ 43 GHz resonator. Site 2 transitions in both<sup>I=0</sup> Yb (a) and<sup>171</sup> Yb (b) are measured. A _T_ 2 measurement is performed when the echo amplitude is above 25 mV, allowing for _T_ 2 to be measured across the spin line. A dip in coherence is recorded at the centre of the<sup>I=0</sup> Yb spin line. ID is maximal at the centre of the spin line where the maximum number of spins are resonant, this therefore becomes the limiting decoherence mechanism. In<sup>171</sup> Yb the lower abundance (15%) means ID is not limiting _T_ 2 and no dip is observed. 

is recorded, and when calculating the ID limited _T_ 2 it is well above the measured coherence time. This indicates that in the<sup>171</sup> Yb case the coherence time is not limited by ID but by another decoherence mechanism. We therefore turn our focus on a second mechanism which is present in several bulk doped spin systems - spectral diffusion. 

##### **5.4 Spectral Diffusion** 

In the previous section we showed that the limiting decoherence mechanism for the I=0Yb:YSO is ID, however this does not limit the lesser abundant 171Yb. The 171Yb isotope is also the isotope which exhibits ZEFOZ transitions and has long optical coherence [108]. This makes it a promising candidate for quantum memories and 

_5.4. Spectral Diffusion_ 

_93_ 



<!-- Start of picture text -->
a) 890 mT 906 mT 920 mT<br>Resonator<br>Spins<br>0.1<br>0<br>2.3 2.6 2.3 2.6 2.3 2.6<br>b)<br>16  -3 Frequency (GHz)<br>x10 cm<br>5<br>0<br>860 900 940<br>Field (mT)<br>Normalised Spin Number<br>Density<br>Resonant Spin<br><!-- End of picture text -->

**Figure 5.9:** a) Modelling of the interaction of the resonator and spin linewidths. The resonator (modelled as a Lorentzian, in purple) has a narrow linewidth (66 kHz), limited by the 15 µs _π_ pulse acting as a filter. The spin line (teal) was measured to be 8 _._ 7 MHz and is modelled as a Gaussian. As the field is swept the spin line passes through the resonator with the number of spins within the resonator linewidth (shaded region) reaching a maximum when the centre of the spin line is at the resonant frequency of the resonator. This can be transformed into the total number of resonant spins (b)) during the field sweep. This can then be used in equation 5.4 to estimate the ID limited _T_ 2. This provides a new technique for estimating spin doping populations in highly-doped systems. 

so identifying and understanding its decoherence properties is important. 

Spectral diffusion (SD) is another decoherence mechanism which effects bulk doped spin systems and has been showed to be the limit on coherence in many rare-earth systems [111,134,199]. 

Cross-relaxation processes (or spin between spins cause the local magnetic environment to fluctuate over time giving rise to SD. Reducing the temperature of the spin bath polarises it, reducing the rate of flip-flops and consequently, the effects of SD [203,204]. By measuring the coherence time as a function of temperature the effects of SD can be observed. 

_5.4. Spectral Diffusion_ 

_94_ 



<!-- Start of picture text -->
I=0Yb<br>a)<br>3.5x1017 cm-3<br>b)<br>16 -3<br>8x10  cm<br>c)<br>5.5x1017 cm-3<br>free param<br>I=0Yb<br>171Yb<br>3<br>400<br>2<br>200<br>1<br>0 0<br>860 900 940<br>100 15<br>10<br>50<br>5<br>0 0<br>1060 1080 1100<br>3<br>400<br>2<br>200<br>1<br>0 0<br>860 900 940<br>Field (mT)<br>T<br>2<br> (ms)<br>T<br>2<br> (ms)<br>T<br>2<br> (ms)<br>Echo Amplitude (mV)<br>Echo Amplitude (mV)<br>Echo Amplitude (mV)<br><!-- End of picture text -->

**Figure 5.10:** a,b) Using equation 5.4 and the modelling of the interaction of the resonator and spin line (figure 5.9), the ID limited _T_ 2 is plotted (black) over the echodetected _T_ 2 field sweep data. The modelled _T_ 2 fits the<sup>I=0</sup> Yb data well - with no fit parameters. This gives clear evidence _T_ 2 is limited by ID. In the<sup>171</sup> Yb case, no dip is coherence is observed and the predicted ID limited _T_ 2 is well above the measured _T_ 2. c) By leaving the doping density as a free parameter and fitting equation 5.4 to the<sup>I=0</sup> Yb data the doping density can be approximated. The fit results in _n_ =(5 _._ 5 _±_ 0 _._ 2) _×_ 10<sup>17</sup> cm<sup>_−_3</sup> 

_5.4. Spectral Diffusion_ 

_95_ 

###### **5.4.1 Temperature Dependence** 

In this section we monitor the temperature dependence of _T_ 2 in two different rareearth systems;<sup>145</sup> Nd:YSO and<sup>nat</sup> Yb:YSO. The temperature dependent data of 145Nd was collected by Dr. Gavin Dold [63], however new analysis of this data and comparison to<sup>nat</sup> Yb forms the basis of our study into SD. 

The<sup>145</sup> Nd:YSO sample was studied at 8 _._ 07 GHz using a ’thin-ring’ style resonator with Q _≈_ 72000 [95].<sup>145</sup> Nd has nuclear spin 7/2; this results in 8 strong spin transitions corresponding to the projections of the nuclear spin along the magnetic field axis. This forms an electron spin bath which can undergo flip-flops. 

The Yb:YSO sample was measured using the same 5 _._ 04 GHz spiral resonator used in the EDFS in figure 5.5 and the _T_ 1 measurement in figure 5.1. 

In order for energy to be conserved in a flip-flop process, the two spins must be in differing states. A relaxed spin exchanges with an excited spin, therefore spin flip-flops rely on population of the excited state. In a unperturbed system the population of the energy levels is dictated by Boltzmann statistics. The polarisation is defined as the product of the probability of spins being in the ground and excited state: 



where _T_ z is the Zeeman temperature defined as _T_ z =<sup>_h_</sup> _k_ B<sup>_<u>f</u>_.</sup> 

In previous work, the temperature dependence of _T_ 2 was modelled phenomenologically’ using the polarisation and a fitting parameter, _ζ_ , related to the dipoledipole coupling strength and a residual decoherence rate (Γres) [63,204,205]: 



We take a more rigorous approach, one in which a more precise equation is extracted and does not rely on undefined fitting parameters. To build up to an equation like that of the form of equation 5.6 we consider the mechanisms for spin flip-flops. 

Spectral diffusion occurs due to spin between _non-resonant_ spins (B) in the environment resulting in a fluctuating magnetic field which decoheres a central spin (A), shown schematically in figure 5.11. In section 2.2.1 the different 

_96_ 



<!-- Start of picture text -->
5.4. Spectral Diffusion<br><!-- End of picture text -->













<!-- Start of picture text -->
A<br><!-- End of picture text -->





<!-- Start of picture text -->
B<br><!-- End of picture text -->

**Figure 5.11:** Schematic of spectral diffusion. A central spin, A, is decohered due to the fluctuating magnetic field produced from two environmental spins (in subensemble, B) undergoing a flip-flop with rate, _R_ . This inflicts a spectral diffusion linewidth (ΓSD) onto the A spin. _R_ and ΓSD combine to form a decoherence rate. 

spin relaxation mechanisms were outlined. In the low temperature limit processes which involve spin-lattice relaxation (Direct, Raman and Orbach mechanisms) are assumed to be negligible. Only considering flip-flops, the flip-flop rate within the B ensemble of spins as [132]: 



where _g_ B, _n_ B and ΓB are the effective g factor, spin concentration and inhomogeneous linewidth of the B ensemble. _α_ ff is a constant that depends on the crystal structure and resonance line shape. 

Equation 5.7 is only valid in an isotropic system, in crystals with an anisotropic g-tensor, we cannot simply replace _g_ B with an angular dependent _g_ B( _θ_ ). Instead a more general equation is needed [132]: 



in the case of an isotropic medium _β_ ff ∝ _µB_<sup>4</sup><sup>_g_4,howeverthisdoes nothold in</sup> the case of strong anisotropy - as is the case in YSO [155, 206–208]. To derive an expression for _β_ ff in an anisotropic medium, we must consider the dipole-dipole interaction as a perturbation to the Zeeman Hamiltonian. The Hamiltonian for two 

~~—~~ C ~~)) () ())~~ 

~~—~~ ) 

~~—~~ ) ~~—~~ )] 

| 

| | 

~~—-~~ 

~~—~~ 



<!-- Start of picture text -->
— —)<br>[—— ()<br>i<br>—<br>=r<br><!-- End of picture text -->

_5.4. Spectral Diffusion_ 

_99_ 



This takes the same form to that in equation 5.6 but with consideration of the matrix element of each sub-ensemble and a fitting parameter which is related to the average g-factor over the sub-ensembles. 

In both the<sup>145</sup> Nd and<sup>nat</sup> Yb samples a Hahn-echo _T_ 2 is measured as a function of temperature. Starting at base temperature of the dilution refrigerator (14 mK) the temperature is increased incrementally to 1 _._ 2 K allowing for the sample to thermalise with each step. Figure 5.12 shows an increase in coherence time with decreasing temperature, for both the<sup>145</sup> Nd and<sup>nat</sup> Yb samples: in Nd from (24 _±_ 1) µs at 1 _._ 2 K to (0 _._ 41 _±_ 0 _._ 01) ms 14 mK and in<sup>nat</sup> Yb increasing from (33 _±_ 7) µs to (3 _._ 38 _±_ 0 _._ 09) ms over the same temperature range. 

Before using equation 5.14 to fit to the temperature dependence the relevant sub-ensembles must be identified. In the<sup>145</sup> Nd, sample the different projections of the _I_ = 7 _/_ 2 nuclear spin along the applied magnetic field form the dominant contribution to such sub-ensembles, while in the<sup>nat</sup> Yb sample, multiple isotopes with different nuclear spin and the projections of nuclear spin for _I >_ 0 act as sub-ensembles. Using EasySpin, the frequencies (and therefore the Zeeman temperatures) of the sub-ensembles are calculated as well as the matrix element for the particular transition. In the<sup>nat</sup> Yb sample, the spin density, _ni_ , is calculated by multiplying the nominal doping density by the abundance of each isotope and the proportion of spins within each site (1/2). 

The Zeeman temperatures for the relevant sub-ensembles are plotted in ure 5.12 with the isotopes and sites distinguished in the<sup>nat</sup> Yb sample. 

We first turn to the<sup>145</sup> Nd sample. In this case, the decoherence rate drops sharply as the hyperfine levels polarise. As the measured transition is the _mI_ = +7/2 transition, it becomes most populated as the temperature is reduced while the surrounding sub-ensembles become less occupied and more polarised. Fitting equation 5.14 to the<sup>145</sup> Nd data, returns a value of (1 _._ 94 _±_ 0 _._ 01) for _ξ_ . Comparing this to the<sup>nat</sup> Yb sample where _ξ_ = (12 _±_ 1). 

In the<sup>nat</sup> Yb the surrounding sub-ensembles are comprised of other Yb isotopes, and Yb ions in the other crystal site (Site 1). The difference in fitting parameters is attributed to the difference in effective g-factors of the sub-ensembles as _ξ_ ∝ _g_<sup>4</sup> . In particular _gz_ = 4.17 in Nd whereas _gz_ = 6.06 in Yb site 2 [155, 206]. In the<sup>nat</sup> Yb sample, there are still unpolarised sub-ensembles even below 100 mK, 

_5.4. Spectral Diffusion_ 

_100_ 



<!-- Start of picture text -->
0 1 2 3 4<br>S1 S2<br>0 2 4 6 8<br>145Nd<br>T2  = 410 ± 14 μs<br>171Yb<br>I=0Yb<br>173Yb<br>T  = 3.38 ± 0.09 ms<br>2<br>50<br>a)<br>40<br>30<br>20<br>10<br>0<br>40<br>b)<br>30<br>20<br>10<br>0<br>0 0.2 0.4 0.6 0.8 1.0 1.2<br>Temperature (K)<br>Echo<br>Amplitude<br>Echo<br>Amplitude<br>) (kHz)<br>2<br>T<br>Decoherence Rate (1/<br><!-- End of picture text -->

**Figure 5.12:** Temperature dependence of the decoherence rate<sup>145</sup> Nd and<sup>nat</sup> Yb samples. a) In<sup>145</sup> Nd:YSO the _T_ 2 increases from (24 _±_ 1) µs at 1 _._ 2 K to (0 _._ 41 _±_ 0 _._ 01) ms 14 mK. The environmental sub-ensembles (the projections of the nuclear spin) become polarized as the temperature is reduced below their Zeeman temperature (indicated by the dashed lines). b) The _T_ 2 of<sup>171</sup> Yb in<sup>nat</sup> Yb:YSO increases from (33 _±_ 7) µs to (3 _._ 38 _±_ 0 _._ 09) ms. Other Yb isotopes (shown by their abundances in the pie-chart) in the two crystal sites form the spin environment which is polarized. The Zeeman temperatures relating to the different isotopes and sites are indicated by the colours of the dashed lines. The main contributors to the spectral diffusion are the electron spins of the<sup>I=0</sup> Yb isotopes which form 70% of the abundance. 

_5.4. Spectral Diffusion_ 

_101_ 

including some from the<sup>173</sup> Yb isotope. 

The coherence time at 14 mK is almost an order of magnitude longer in the natYb sample than the 145Nd sample, to investigate the source of this decoherence we perform a stimulated echo experiment. This allows us to extract a flip-flop rate and spectral diffusion linewidth which we can compare to literature to determine the origin of the decoherence. 

###### **5.4.2 Stimulated Echo** 

In a stimulated echo experiment, the time when the echo is emitted is controlled via a _π/_ 2 pulse. Often referred to as a ’three-pulse echo’, the sequence is comprised of three _π/_ 2 pulses (<sup>_<u>π</u>_</sup> 2<sup>-</sup><sup>_τ_-</sup><sup>_<u>π</u>_</sup> 2<sup>-</sup><sup>_T_W-</sup><sup>_<u>π</u>_</sup> 2<sup>-</sup><sup>_τ_-echo).The pulse sequence is discussed</sup> in section 2.3. At the longer timescales available in the three-pulse echo sequence, spectral diffusion from spins with slow flip-flop rates (such as nuclear spins) can be measured. 

The echo amplitude in a three-pulse echo sequence depends on both _T_ 1 and _T_ 2 relaxation and is given by [134]: 



where _A_ 0 is the echo amplitude at _T_ W = _τ_ = 0. The first component of the exponential captures the _T_ 1 relaxation, this is small as _T_ W _≪ T_ 1. The second component describes the spectral diffusion limited _T_ 2 decay in which an effective decoherence rate (Γeff) occurs over the inter-pulse time _τ_ . The effective decoherence rate is given by: 



where _R_ and ΓSD in the temperature dependent study. Γ0 is a residual decoherence rate. In both the 145Nd and natYb samples the measured _T_ 1 ((696 _±_ 47) ms [63] and (120 _±_ 20) ms, see section 5.2.1) is much longer than the duration of the experiment, for this reason we assert that all decoherence arises from spectral diffusion and set Γ0 = 0. 

By varying the long wait time, _T_ W, for different values of _τ_ , results in a double exponential decay in the echo in which the independent variable only appears in one term [134]. Three values of _τ_ are chosen for each sample with the ratio of _τ/T_ 2 maintained for both. Equation 5.20 is fitted to the data with _T_ 1 set to the measured value and the other variables remaining as fit parameters as shown in figure 5.13. 

_R_ and ΓSD 

_5.4. Spectral Diffusion_ 

_102_ 



<!-- Start of picture text -->
8 0<br>a) T  = 1 4 mK<br>3 0<br>5 0<br>6 0<br>8 0<br>4 0<br>2 0<br>0<br>0 5 1 0 1 5 2 0<br>b) T  = 1 4 mK<br>8<br>2 2 5<br>3 7 5<br>6 6 0 0<br>4<br>2<br>π π π<br>2 2 2<br>0<br>0 20 40 60 80 1 0 0<br>T w  (ms)<br>1 4 5 Nd<br>natYb<br>Echo Amplitude (mV)<br><!-- End of picture text -->

**Figure 5.13:** Three-pulse echo decay in both the<sup>145</sup> Nd (a) and<sup>nat</sup> Yb (b) systems. The threepulse echo sequences, shown in the inset of b), allows for spectral diffusion to be measured over a long time scale as the spins are ‘parked’ on the _z_ axis over time _T_ W where they undergo _T_ 1 relaxation rather than _T_ 2 decay. By varying _T_ W for different _τ_ values, equations 5.20 and 5.21 can be fit to the data (solid curves). From this the spectral diffusion rate ( _R_ ) and linewidth (ΓSD) can be extracted and used to identify the source of the decoherence. 

determine these parameters. There is a large covariance between _R_ and ΓSD which is highlighted in the plots in figure 5.14. By fixing either _R_ or ΓSD and calculating the fitted value of the other, we can see the resulting _r_<sup>2</sup> of the fits is 1 for several values of _R_ and ΓSD. However if we instead use the product, _R_ ΓSD as the fit parameter, the _r_<sup>2</sup> value is 1 for only one value. This shows that we cannot deduce _R_ and ΓSD separately but rather the product of the two. 

We first explore the decoherence in the<sup>145</sup> Nd sample. Fitting equation 5.20 to the data in figure 5.13 and extracting _R_ ΓSD results in a value of (3 _._ 5 _±_ 0 _._ 4) _×_ 10<sup>6</sup> Hz<sup>2</sup> . Using equation 5.15 allows for a limit on coherence to be determined, this 

_5.4. Spectral Diffusion_ 

_103_ 



<!-- Start of picture text -->
a) b)<br>c) d)<br>R  (Hz)<br>R  (Hz)<br>500<br>1 1 12<br>400 10<br>300<br>0 0<br>108<br>200<br>-1 -1<br>100<br>104<br>-2 0 -2<br>100 102 104 106 108 10-8 10-5 10-2 101 104<br>Γ  (Hz)<br>SD 1e7<br>1.0 1e71.0<br>1 1<br>0.8 0.8<br>0.6 0.6<br>0 0<br>0.4 0.4<br>-1 -1<br>0.2 0.2<br>-2 0.0 -2 0.0<br>100 102 104 106 108 10-8 10-5 10-2 101 104<br>Γ  (Hz)<br>SD<br>Γ<br>SD<br> (Hz)<br>RΓ RΓ<br>SD SD<br> (Hz  (Hz<br>2 2<br>) )<br>R<br> (Hz)<br>2 2<br>r r<br>2 2<br>r r<br><!-- End of picture text -->

**Figure 5.14:** Covariance of _R_ and ΓSD in fitting equations 5.20 and 5.21 to the three-pulse echo data in figure 5.13. In a) [b)] ΓSD [ _R_ ] is fixed and varied while _R_ [Γ _SD_ ] is left as a fitting parameter. The _r_<sup>2</sup> value of the resulting fit is calculated and it can be seen that several values of _R_ [ΓSD] return a _r_<sup>2</sup> =1. In c) and d) the product _R_ ΓSD is calculated and _r_<sup>2</sup> =1 for a unique value of the product. Therefore _R_ and ΓSD cannot be extracted separately due to their large covariance, but rather their product should be used in further analysis. 

is calculated to be _T_ 2=(0 _._ 60 _±_ 0 _._ 03) ms. In turn, equations 5.7 and 5.13 are used to determine an effective spin temperature; a temperature of 61 mK is extracted. This indicates that the sample was not well thermalised as the recorded temperature of the dilution fridge was 14 mK. The poor thermalisation is highlighted when plotting the echo amplitude in the temperature dependent study. As the _m_ I=7/2 transition was probed, the echo amplitude should continue to increase as the temperature is decreased as the transition becomes more polarized and more populated. In figure 5.15 the echo amplitude reaches a maximum at _≈_ 60 mK. Using the population and polarisation of the transition the predicted amplitude is plotted in red, the data deviates from this line below 100 mK indicating poor thermalisation between the spin bath and the cryostat. The poor thermalisation likely arises from the way the chip was mounted. The YSO crystal was placed onto a sapphire spacer which then rested on struts in the copper cavity, this means the YSO crystal does not have good thermal contact with the copper and the surrounding experiment. 

The<sup>nat</sup> Yb sample has a much higher coherence time at base temperature, this 

_5.4. Spectral Diffusion_ 

_104_ 



<!-- Start of picture text -->
0.4<br>0.3<br>0.2<br>0.1<br>0.0<br>0.0 0.1 0.2 0.3 0.4 0.5<br>Temperature (K)<br>Echo Amplitude (V)<br><!-- End of picture text -->

**Figure 5.15:** The echo amplitude of the<sup>145</sup> Nd sample as the temperature is increased using the _T_ 2 data in figure 5.12, the amplitude of the first echo in the _T_ 2 measurement. The population and polarisation of the _mI_ = +7/2 transition solely increases as T _→_ 0 K, therefore the echo amplitude should also increase. The poor thermalisation is observed below 100 mK. 

is reflected when the same stimulated echo analysis is conducted on its data. A value of _R_ ΓSD = (1 _._ 3 _±_ 0 _._ 1) _×_ 10<sup>5</sup> Hz<sup>2</sup> is extracted which results in a theoretical spectral diffusion limit of _T_ 2 = (3 _._ 1 _±_ 0 _._ 7) ms. This is consistent with the measured Hahn echo _T_ 2 of (3 _._ 38 _±_ 0 _._ 09) ms. This corresponds to a spin bath temperature of 38 mK. This analysis confirms that even at base temperature the coherence of 171Yb in natYb:YSO is limited by spectral diffusion. Given the electron spin bath from<sup>I=0</sup> Yb isotopes are polarised at this temperature, we must look for another source of flip-flops. 

Rather than arising from an electron spin bath, we explore the possibility of the nuclear spin bath within the crystal itself being the source of this spectral diffusion. The yttrium in YSO is 100% abundant<sup>89</sup> Y with nuclear spin _I_ = 1 _/_ 2. While it has a small nuclear magnetic moment, _µ_ 89Y = _−_ 0.137 _µ_ N, this becomes significant at long timescales (as measured here). Nuclear spins have a much lower (nuclear) g-factor, as such spitting between nuclear levels is on order MHz (as apposed to GHz for electron spins). This means reducing the temperature of the sample does not polarise nuclear spin baths. To estimate the<sup>89</sup> Y nuclear flip-flop rate we follow a ‘method of moments’ approach as in [111]. The flip-flop rate can be written as: 



and the spectral diffusion linewidth as: 

_5.5. Discussion_ 

_105_ 



where _γ_ Y, _n_ Y and _I_ are the gyromagnetic ratio, spin density and nuclear spin number of the<sup>89</sup> Y nuclei. _g_ is the effective g factor of<sup>171</sup> Yb. Using _γ_ Y = 2 _._ 1 MHzT<sup>_−_1</sup> , _n_ Y = 9 _._ 11 _×_ 10<sup>21</sup> cm<sup>_−_3</sup> as well as the effective g factor of<sup>171</sup> Yb at 370 mT along D2 ( _g_ = 1 _._ 4) the nuclear flip-flop rate is calculated to be _R_ = 3 _._ 6 Hz. This slow flip-flop rate is consistent with values estimated in other works [111]. The spectral diffusion linewidth arising from these flip-flops is estimated as ΓSD _,_ Y = 38 kHz, putting these together we see good agreement with the three-pulse echo data where the product _R_ ΓSD = (1 _._ 3 _±_ 0 _._ 1) _×_ 10<sup>5</sup> Hz<sup>2</sup> was measured, the estimate from nuclear flip-flops is _R_ ΓSD _,_ Y = (1 _._ 05 _±_ 0 _._ 10) _×_ 10<sup>5</sup> Hz<sup>2</sup> . Rewriting this as a coherence time results in a<sup>89</sup> Y nuclear flip-flop limited _T_ 2 of 3 _._ 48 ms. We therefore assert that our measured (Hahn echo) _T_ 2 = (3 _._ 38 _±_ 0 _._ 09) ms is limited by the nuclear spin bath from the YSO crystal itself. 

##### **5.5 Discussion** 

In this chapter we have explored the decoherence mechanisms in two different rareearth doped crystals. Using CW ESR we are able to quickly explore the spin systems, identifying different spin species with different abundances. In the<sup>nat</sup> Yb system we observe large avoided crossings from the 70% abundant isotopes with nuclear spin I=0, as well as several<sup>171</sup> Yb transitions. Using these, alignment to the crystal axis can be easily done by rotating the in-plane field. 

ID is limiting decoherence mechanism in highly doped spin systems. Using the highly abundant<sup>I=0</sup> Yb isotopes we observe a dip in coherence at the centre of the spin line. By modelling the fraction of the spins within the resonator bandwidth we predict the expected coherence time as a function of field across the spin line. We observe good agreement with the data (figure 5.10) with no free parameters. We also show how this method can be used to estimate the nominal doping density of highly doped spin systems by allowing the spin density to be fit to the data. 

We explore the coherence properties in the presence of spectral diffusion of the _mI_ = +7/2 transition of<sup>145</sup> Nd at 8 _._ 07 GHz and 326 mT as well as the _mI_ = -1/2 transition of<sup>171</sup> Yb at 5 _._ 04 GHz and 370 mT. By reducing the temperature from 1 _._ 2 K to 14 mK the coherence time was increased from (24 _±_ 1) µs to (0 _._ 41 _±_ 0 _._ 01) ms in<sup>145</sup> Yb and in<sup>171</sup> Yb increasing from (33 _±_ 7) µs to (3 _._ 38 _±_ 0 _._ 09) ms. Environmental electron spins undergo spin flip-flops which contribute to spectral diffusion, by modelling their flip-flop rates and spectral diffusion linewidths we are able to 

_5.5. Discussion_ 

_106_ 

Using a stimulated three-pulse echo experiment the decoherence mechanisms at base temperature are identified. In the<sup>145</sup> Nd poor thermalisation below 100 mK severely restricts the extent to which _T_ 2 can be increased and electron spin baths remain unpolarised. With better thermalisation we would expect the coherence time to reach that comparable with the<sup>nat</sup> Yb sample. The three-pulse echo analysis of the<sup>nat</sup> Yb sample matches well to the Hahn echo _T_ 2 with both measurements giving a coherence time within the error bounds. ((3 _._ 1 _±_ 7 _._ 0) ms and (3 _._ 38 _±_ 0 _._ 09) ms for the three-pulse echo and Hahn echo respectively). By estimating the flip-flop rate and spectral diffusion linewidth of the<sup>89</sup> Y nuclear spin bath we show that at base temperature the coherence time is limited by<sup>89</sup> Y nuclear flip-flops. For this transition at this field and frequency we have reached the limit on coherence for the YSO crystal as the nuclear spin bath cannot be polarised. 

In this chapter we have shown that spectral diffusion is the leading contributor to decoherence in rare-earth doped YSO. By decreasing the temperature of the sample we are able to increase _T_ 2 (and learn about the origin of the spectral diffusion), however in the next chapter we will use our understanding of the spin system to extend the coherence time beyond that achieved by reducing temperature. 

##### **Chapter 6** 

### **Extending Coherence in Yb:YSO** 

_When you do things right, people won’t be sure you’ve done anything at all._ 

|||The Universe, Futurama.|
|---|---|---|
|**Contents**|||
|**6.1**|**Resonator-Spin System . . . . . . **|**. . . . . . . . . . . . . . . 108**|
|**6.2**|**High-Field Regime . . . . . . . . . **|**. . . . . . . . . . . . . . . 110**|
|**6.3**|**Zero-Field**<br>**. . . . . . . . . . . . . **|**. . . . . . . . . . . . . . . 116**|
||6.3.1<br>ZEFOZ . . . . . . . . . . .|. . . . . . . . . . . . . . . 116|
||6.3.2<br>LoFOZ . . . . . . . . . . .|. . . . . . . . . . . . . . . 119|
|**6.4**|**Isotopic Purifcation . . . . . . . . **|**. . . . . . . . . . . . . . . 121**|
|**6.5**|**Dynamical Decoupling . . . . . . . **|**. . . . . . . . . . . . . . . 124**|
||6.5.1<br>CPMG<br>. . . . . . . . . . .|. . . . . . . . . . . . . . . 124|
|**6.6**|**Discussion**<br>**. . . . . . . . . . . . . **|**. . . . . . . . . . . . . . . 126**|



In the previous chapter, we spectral diffusion as the limiting decoherence mechanism for<sup>171</sup> Yb<sup>3+</sup> ions in<sup>nat</sup> Yb:YSO. By performing a temperature dependent study the electron spin bath (mainly electrons from the<sup>I=0</sup> Yb isotopes) was identified as the source of the spectral diffusion. However, by moving to 14 mK the limiting mechanism is<sup>89</sup> Y nuclear flip-flops. This allowed for a _T_ 2=(3 _._ 38 _±_ 0 _._ 09) ms to be recorded. In this chapter we will look at techniques to increase this further. We use the anisotropic nature of the spin system to increase coherence in both the high magnetic field and zero field regime. 

_6.1. Resonator-Spin System_ 

_108_ 

Clock transitions have been shown to substantially increase coherence times by reducing sensitivity to magnetic field fluctuations in silicon [53, 54] and rare-earth systems [108, 209]. The requirements for a clock transition in rare-earth doped crystals are stricter than in an isotropic material like silicon. A ZEFOZ point must satisfy ∇ _B f_ = 0, that is _dBd fx_<sup>=</sup> _dBd fy_<sup>=</sup> _dB_<sup>_d f_</sup> _z_<sup>=0thusmakingthemintrinsicallyrarerto</sup> 

By fabricating superconducting resonators at lower frequencies we are able to probe the ZEFOZ point at zero field, as well as the effect of the anisotropic g tensor at high fields. 

##### **6.1 Resonator-Spin System** 

In this chapter two different field regimes are investigated. At low fields the precise frequency of the resonator becomes crucially important to hit ZEFOZ points.<sup>171</sup> Yb has a ZEFOZ transition at zero magnetic field at 2 _._ 370 GHz, this is high enough to be within the bandwidth of the measurement setup and suitable resonators can be fabricated. In order to have the best chance of hitting this transition - which is also narrow in frequency - a scatter gun approach was used. 12 spiral resonators were fabricated on the same<sup>nat</sup> Yb:YSO chip covering a range of frequencies around the ZEFOZ point. In figure 6.1 the VNA is swept around the ZEFOZ point at zero field and several resonances are observed. A resonator at 2372 _._ 2 MHz with a Q factor of 1 _._ 09 _×_ 10<sup>5</sup> is within the spin linewidth of the ZEFOZ transition and is used to probe the zero field dynamics. A slightly higher frequency resonator at 2436 _._ 9 MHz (Q= 1 _._ 35 _×_ 10<sup>5</sup> ) is used for the high field measurements as it has a higher Q factor and deeper prominence. The difference in prominence of the resonators is due to their placement of the chip and their distances to the central conductor of the CPW. 

> 171Yb:YSO is used to reduce sensitivity to magnetic field noise. The g-tensor is defined in section 2.5. In this chapter we will only explore the dynamics of site 2. We can see that the g-tensor has a large component in the (out of plane) b direction, therefore we expect a large change in coherence when the field is swept along this axis. For the most part, we apply fields in the D1-D2 plane unless otherwise stated; this is the plane of the resonator. 

of the<sup>171</sup> Yb transitions. In particular, it results in a ’line of coherence’ where the effective g factor is minimised. Along this line the resonant field of the transitions reaches its maximum. This occurs at approximately 49<sup>_◦_</sup> in the D1-D2 plane. This line of coherence will be important in increasing the _T_ 2 time at both high and low 

_6.1. Resonator-Spin System_ 

_109_ 



<!-- Start of picture text -->
a)<br>-8<br>-10<br>B = 0 mT<br>-12<br>2.36 2.40 2.44 2.48<br>Frequency (GHz)<br>b) c)<br>0.0<br>-0.4<br>-0.8<br> f  = 2372.2 MHz  f  = 2436.9 MHz<br>Q = 109,267 Q = 135,596<br>-1.2<br>2.370 2.372 2.374 2.435 2.437 2.439<br>Frequency (GHz) Frequency (GHz)<br>ZEFOZ<br> (dB)<br>21<br>S<br> background subtract (dB)<br>21<br>S<br><!-- End of picture text -->

**Figure 6.1:** a) VNA sweep around the ZEFOZ point at zero field. Several resonators are observed as dips in transmission (S21). The resonator at 2372 _._ 2 MHz (in b)) and Q factor of 109,267 is used in the ZEFOZ and low-field experiments while the higher frequency (2436 _._ 9 MHz) and Q factor (135,596) (seen in c)) is used for the high-field measurements. The background transmission has been removed before the resonance was fitted in b) and c). 

_6.2. High-Field Regime_ 

_110_ 

fields. Figure 6.2 shows the important features of the spin system in the high field (a)) and low field (b)-d)) regimes. Using the 2 _._ 435 GHz in the high field regime means the resonant field of the _mi_ = _−_ 1 _/_ 2 transition varies from 120 mT at _−_ 44<sup>_◦_</sup> to 1060 mT at _−_ 131<sup>_◦_</sup> . The gradient of the frequency with respect to field (∇B _f_ ) follows the same angular dependence where it is minimum at _−_ 126<sup>_◦_</sup> reaching ∇B _f_ = 2 _._ 1 MHzmT<sup>_−_1</sup> and a maximum of 19 MHzmT<sup>_−_1</sup> at _−_ 35<sup>_◦_</sup> . 

At zero field all the energy levels in<sup>171</sup> Yb become insensitive to field, that is ∇B _E_ = 0. This in turn means all the available transitions become ZEFOZ transitions. In figure 6.2 the frequency and ∇B _f_ dependence of the 1-3 transition are plotted when the field is swept along the line of coherence (at 49<sup>_◦_</sup> ) in the D1-D2 plane. At 0 mT, _f_ = 2 _._ 370 GHz and ∇B _f_ = 0. 

##### **6.2 High-Field Regime** 

Before we utilise ZEFOZ at zero magnetic field, we first explore the high-field regime. Using the resonator at 2 _._ 437 GHz we are able to explore the majority of the angular dependence. We ensure the applied field is well aligned to the superconducting plane as a misalignment of just 0 _._ 3<sup>_◦_</sup> at 1 T results in an out-of-plane field of 5 mT - enough to turn the resonator normal. While the crystal was cut so that the D1-D2 plane was in the plane of the polished surface (and thus the resonator plane), there will always be a slight misalignment. Using the roadmap in figure 5.3 the misalignment between the planes was determined to be _≈_ 0 _._ 8<sup>_◦_</sup> . While small, this has two significant effects. The first is that as the field is rotated in the resonator plane (rather than the D1-D2) plane there is a slight field applied along the crystal b axis. This results in lifting the degeneracy of the crystal subsites and so<sup>171</sup> Yb ions in site 2 now occupy two subsites which we refer to as 2a and 2b. The second effect is that these two subsites have different resonant fields and effective g-factors, this means the resonant field of the _mI_ = -1/2 transition in site 2a reaches a maximum of 1 _._ 2 T. Due to measurement constraints the highest field we measured at was 1 _._ 07 T. Figure 6.3 shows how the two subsites vary in their resonant fields in the D1-D2 plane, the measured transitions using pulsed ESR are also indicated. 

At each angle and an echo detected _T_ 2 sweep was performed, using the maximum coherence time for each, the _T_ 2 as a function of angle can be plotted. In figure 6.4, _T_ 2 can be seen to have a strong angular dependence. _T_ 2 increases from (96 _±_ 3) µs at _−_ 88<sup>_◦_</sup> to (6 _±_ 2) ms at _−_ 131<sup>_◦_</sup> for site 2a. The same dependence is also seen in site 2b with _T_ 2 increasing from (179 _±_ 7) µs to (2 _._ 2 _±_ 0 _._ 7) ms over the same angular range. 

To model the angular dependence, we take a similar approach to the tempera- 

_6.2. High-Field Regime_ 

_111_ 



<!-- Start of picture text -->
a)<br>f = 2.435 GHz<br>Angle (o)<br>b)<br>c)<br>d)<br>Field (mT)<br>D1Field (mT)<br>1200 20<br>16<br>800<br>12<br>8<br>400<br>4<br>0 0<br>-180 -90 0 90 180<br>1.5<br>2375<br>0.5<br>2.370 GHz 2370<br>2.5<br>-0.5<br>0.0<br>-1.5 -50 0 50<br>-50 0 50<br>∇<br>B<br>f<br>(MHz/mT)<br>Field (mT)<br>(MHz)<br>Frequency<br>Energy (GHz)<br>(MHz/mT)<br>f<br>B<br>∇<br><!-- End of picture text -->

**Figure 6.2:** a) The angular dependence of the<sup>171</sup> Yb _mI_ =-1/2 resonant field as the angle of the external field is rotated in the D1-D2 plane. The minimum resonant field is 120 mT at _−_ 44<sup>_◦_</sup> and maximum at 1060 mT at _−_ 131<sup>_◦_</sup> . The gradient of the frequency with respect to field (∇B _f_ ) follows the same angular dependence where it is minimum at _−_ 126<sup>_◦_</sup> reaching ∇B _f_ = 2 _._ 1 MHzmT<sup>_−_1</sup> and a maximum of 19 MHzmT<sup>_−_1</sup> at _−_ 35<sup>_◦_</sup> . The angles of low gradient correspond to the ‘line of coherence’ where _T_ 2 is maximised. b) The energy level diagram of<sup>171</sup> Yb as the field is swept along the D1 axis, we measure the 1-3 transition which is resonant at 2 _._ 370 GHz at zero field. c) The frequency dependence of the 1-3 transition along the line of coherence, the resonant at 2 _._ 372 GHz is within the spin linewidth up to approximately 50 mT, this defines the field region which can be probed by this resonator. d) The gradient of the transition along the line of coherence, the transition goes ZEFOZ at 0 mT when ∇B _f_ is analytically zero. 

_6.2. High-Field Regime_ 

_112_ 



<!-- Start of picture text -->
Site 2a<br>Site 2b<br>Angle (o)<br>0.8o<br>b<br>D2<br>D1<br>1200<br>800<br>400<br>0<br>-180 -140 -100 -60 -20<br>Field (mT)<br><!-- End of picture text -->

**Figure 6.3:** Roadmap of the<sup>171</sup> Yb _mi_ = -1/2 transition with a misalignment of 0 _._ 8<sup>_◦_</sup> between the resonator plane and the D1-D2 plane. The subsite degeneracy is lifted, this results in site 2 being split into 2a and 2b with different effective g-factors. The resonant fields of these two subsites are plotted with the measured transitions highlighted. 

ture dependence in section 5.4.1. We assume we are spectral diffusion limited. This is a fair assumption as we are working at a lower frequency compared to the temperature dependent study (which was spectral diffusion limited) so the environmental subensembles will be less polarised. Using the spectral diffusion limited _T_ 2: 



we can estimate the coherence time as a function of angle. To do so we need to derive expressions for _R_ ( _θ_ ) and ΓSD( _θ_ ). This can be done using: 



To calculate _R_ ( _θ_ ) and ΓSD( _θ_ ) requires extensive easyspin simulations. For each angle the resonant field of the<sup>171</sup> Yb _mI_ = -1/2 transition is calculated, using this, and the orientation, the resonant frequencies of all the subensembles can be determined (including both sites, subsites and isotopes). Using all these frequencies their respective Zeeman temperatures are calculated and their polarisation is found 

_6.2. High-Field Regime_ 

_113_ 



<!-- Start of picture text -->
Site 2a<br>Site 2b<br>Angle (o)<br>105 60<br>T2  = 6 +/- 2 ms<br>104<br>30<br>103<br>0<br>102 0 2    (ms)6 12<br>101<br>-180 -140 -100 -60 -20<br>(mV)<br>Echo Amp.<br> (ms)<br>2<br>T<br><!-- End of picture text -->

**Figure 6.4:** The angular dependence of _T_ 2 for the _mI_ =-1/2 transition of<sup>171</sup> Yb at 2 _._ 435 GHz. Due to a misalignment between the resonator and crystal axes of 0 _._ 8<sup>_◦_</sup> the subsite degeneracy, their angular _T_ 2 dependencies are shown by the solid blue and dashed purple lines respectively. The angular _T_ 2 behaviour is modelled by simulating the flip-flop rate of environmental spins and the spectral diffusion linewidth of the central spin (see main text for details). The _T_ 2 reaches a maximum of (6 _±_ 2) ms for site 2a at _−_ 131<sup>_◦_</sup> in the D1-D2 plane at a field of 1 _._ 07 T. 

given an experimental temperature of _T_ =20 mK. In addition to this, the effective g-factors of the subensembles are calculated by finding their ∇B _f_ at each angle. Their linewidths are assumed to be the same and equal to 6 MHz. To encapsulate the angular dependence of _β_ ff _,i_ ( _θ_ ) we rewrite it in terms of the angular dependent parameters _gi_ ( _θ_ ) and _Mi_ ( _θ_ ); _β_ ff _,i_ ( _θ_ ) = _ξ gi_ ( _θ_ )<sup>4</sup> _Mi_ ( _θ_ )<sup>2</sup> , where _Mi_ ( _θ_ ) is the matrix element of the subensemble for a given angle and _ξ_ is a fit parameter. 

Computing these for site 2a and 2b results in a good fit to the angular data, as seen by the solid and dashed lines in figure 6.4. By extracting the environmental flip-flop rate and the ∇B _f_ of the<sup>171</sup> Yb ion separately we can see the two mechanisms working in tandem to give a increase of _T_ 2 of well over an order of magnitude. The first is the reduction in the environmental spin flip-flop rate at _−_ 137<sup>_◦_</sup> , this is largely due to the increase in the external magnetic field needed to be resonant with the<sup>171</sup> Yb transition at 2 _._ 435 GHz. This field results in much larger Zeeman splitting of the environmental subensembles which in turn causes a higher Zeeman temperature and larger polarisation. The increase in polarisation reduces the flipflop rate. This is seen mostly in the<sup>I=0</sup> Yb transitions which comprise 70% of the environmental spins, but also seen in several<sup>171</sup> Yb transitions, the polarisation of the transitions are shown in fig. 6.5. 

The second reason the coherence time increases at angles around _−_ 131<sup>_◦_</sup> is that ∇B _f_ reaches a minimum. The central<sup>171</sup> Yb spin becomes less sensitive to the environmental flip-flops and its decoherence rate decreases. As the spectral 

_6.2. High-Field Regime_ 

_114_ 



<!-- Start of picture text -->
20<br>1 0<br>0<br>I=0Yb 171Yb<br>Angle (o)<br>Site 1<br>Site 2<br>Angle (o) Angle (o)<br>a)<br>-180 -140 -100 -60 -20<br>b) c)<br>0.2<br>0.1<br>0<br>-150 0 -150 0<br>150<br>100<br>50<br>0<br>R (kHz)<br>B<br>Polarisation<br><!-- End of picture text -->

**Figure 6.5:** a) The total environmental flip-flop rate as the applied field is rotated (and increased), the flip-flop rate reaches a minimum of 5 _._ 3 kHz at _−_ 134<sup>_◦_</sup> as the environmental spins become polarised. The central<sup>171</sup> Yb spin also becomes more insensitive to the flip-flops as the ’line of coherence’ is approached. The ∇B _f_ of the<sup>171</sup> Yb transition is plotted as the field is rotated in D1-D2, the subsite degeneracy is lifted due to a slight field along the b crystal direction, site 2a (solid) reaches a minimum value of 1 _._ 48 MHzmT<sup>_−_1</sup> at _−_ 129<sup>_◦_</sup> while site 2b (dashed) reaches 2 _._ 6 MHzmT<sup>_−_1</sup> at _−_ 123<sup>_◦_</sup> . These two phenomena work in tandem to produce the increase in coherence observed in figure 6.4. b) The polarisation of the environmental spin transitions for the<sup>I=0</sup> Yb isotopes for both crystal sites. At angles of _≈−_ 131<sup>_◦_</sup> several of these transitions (especially in site 2) become more polarised and thus the flip-flop rate is reduced. Similar effects are seen in the<sup>171</sup> Yb transitions as shown in c). 

diffusion decoherence rate goes as ∇B _f_ , the coherence time will be maximum when ∇B _f_ is minimised. The angular dependence of ∇B _f_ is plotted in figure 6.5 where site 2a reaches a lower effective g-factor and thus results in its longer coherence time. 

To explore the angular dependence, we needed to work at a lower frequency to the temperature dependence study in section 5.4.1. This results in a higher flipflop rate (due to lower Zeeman temperatures) which is illustrated by comparing the _T_ 2 measured at 5 _._ 04 GHz of (3 _._ 38 _±_ 0 _._ 09) ms along D2 compared to (96 _±_ 3) µs measured at 2 _._ 435 GHz. We showed in section 5.4.1 that _T_ 2 was limited by<sup>89</sup> Y nuclear flip-flops at 5 _._ 04 GHz, we can therefore rule this out at 2 _._ 435 GHz. This is further confirmed by plotting the angular dependence of the predicted<sup>89</sup> Y _T_ 2. In 

_115_ 

_6.2. High-Field Regime_ 



<!-- Start of picture text -->
89Y SD<br>Site 2a Site 2a @ 5.04 GHz<br>Site 2b<br>Angle (o)<br>105<br>104<br>103<br>102<br>101<br>-180 -140 -100 -60 -20<br> (ms)<br>2<br>T<br><!-- End of picture text -->

**Figure 6.6:** Angular dependence of the<sup>89</sup> Y nuclear spin limited _T_ 2. The measurements at 2 _._ 435 GHz are not limited by nuclear flip-flops but rather the electron spin bath. The _T_ 2 measured at 5 _._ 04 GHz is shown in green and is limited by<sup>89</sup> Y nuclear spins. At an angle of _−_ 132 _._ 7<sup>_◦_</sup> the<sup>89</sup> Y limited _T_ 2 reaches a maximum of 25 _._ 5 ms. 

figure 6.6 the<sup>89</sup> Y limited _T_ 2 is plotted as a function of angle in the D1-D2 plane, also plotted is the measured _T_ 2 at 5 _._ 04 GHz. It can be seen that the coherence time is limited by the electron spin bath at 2 _._ 435 GHz at all points in the angular sweep. Only by working at higher frequencies can the<sup>89</sup> Y limit be reached, however very high fields are needed to reach this point. In a<sup>89</sup> Y limited system (at 5 _._ 04 GHz), the predicted _T_ 2 reaches a maximum of 25 _._ 5 ms for site 2a at an angle of _−_ 132 _._ 7<sup>_◦_</sup> and field of 3 _._ 07 T - well beyond the capabilities of our experimental setup. This value of 25 _._ 5 ms is similar to coherence times of other rare-earth systems notably that of Er<sup>3+</sup> ions in CaWO4 where a _T_ 2 of 23 ms was recorded [64]. Even though YSO has the<sup>89</sup> Y nuclear spin bath, it is predicted that similar coherence times to low nuclear spin density crystals (CaWO4) thanks to the large anisotropy of the g-tensor. 

In this section we have shown how we can increase the coherence properties of<sup>171</sup> Yb:YSO by using optimal external field orientations and high fields. Both the polarisation of the environmental spin ensembles and the reduced sensitivity to flip-flops results in a _×_ 60 improvement in _T_ 2 reaching a maximum of (6 _±_ 2) ms at _−_ 131<sup>_◦_</sup> , 2 _._ 435 GHz and 1 _._ 07 T. While this is a significant improvement, and this regime could be useful in some hybrid systems, it is not compatible with large-scale superconducting circuitry. Experiments which require fields of even just a few mT are incompatible with transmon qubits [210], and a great deal of engineering is used to remove stray fields from superconducting qubit devices [211]. To build a quantum memory, which can be incorporated directly into superconducting quantum computers, we need to operate the memory at zero field. Thankfully,<sup>171</sup> Yb gives us an opportunity to do this using its zero-field clock transition - the so called 

_6.3. Zero-Field_ 

_116_ 

ZeFiZEFOZ transition. 

##### **6.3 Zero-Field** 

In the previous section, we used high fields and optimal orientations to extend the coherence time of<sup>171</sup> Yb to 6 ms. Operating at over a Tesla is not possible for integrating this memory with transmon qubits, we therefore explore the coherence properties at zero field using the clock transition. 

At zero magnetic field all accessible<sup>171</sup> Yb transitions become insensitive to magnetic field fluctuations. These ZEro-First-Order-Zeeman (ZEFOZ) transitions have ∇B _f_ = 0 and so small changes in field result in no detuning of the spin. The ZEFOZ point in<sup>171</sup> Yb is even stronger than clock transitions in other systems (such as Bi:Si [54]) as the energy levels are also field insensitive (i.e ∇B _E_ = 0), this means dipole interactions with the environment are ‘switched off’. We therefore expect the 

###### **6.3.1 ZEFOZ** 

To explore the ZEFOZ point we use a spiral resonator fabricated at 2 _._ 372 GHz, within 2 MHz of the ZEFOZ point at 2 _._ 370 GHz. While the maximum _T_ 2 is expected at 0 mT there is significant angular dependence on the coherence time at low fields. Just as in the high field regime, the ‘line of coherence’ is present at low field. 

To probe the coherence landscape of the low field regime in an efficient way we perform a 2D field sweep (in the D1-D2 plane) using a Hahn echo with a long wait time (500 µs). This means regions with short _T_ 2 will not result in a considerable echo compared to fields with long coherence. This significantly shortens the experiment time as a single Hahn echo takes approximately 5 s to complete compared to 15 min for a full _T_ 2 measurement. We can therefore have much more detailed coherence maps for the same experiment time. In figure 6.7 a simulation of ∇B _f_ in the D1D2 plane is plotted and the corresponding coherence map is shown. The line of coherence is clearly observed at 49<sup>_◦_</sup> in the D1-D2 plane and is highlighted by the red line. The same line of long _T_ 2 is measured by the larger echo amplitude at this angle. 

After quickly identifying the regions of long _T_ 2 we can then perform full _T_ 2 measurements along the line of coherence. By sweeping the field along the red line in figure 6.7 we pass through the ZEFOZ point. In figure 6.8 the _T_ 2 sweep from _−_ 5 mT to 40 mT is shown. As 0 mT is approach the coherence time reaches a maximum of (1 _._ 77 _±_ 0 _._ 06) ms at 0 mT - an increase from (87 _±_ 4) µs at 40 mT. By passing through zero field we see that the _T_ 2 is symmetric indicating no erroneous 

_6.3. Zero-Field_ 

_117_ 



<!-- Start of picture text -->
Simulation<br><!-- End of picture text -->





<!-- Start of picture text -->
π π<br>2<br>Wait = 500 μs<br><!-- End of picture text -->



**Figure 6.7:** a) Simulation of the field sensitivity of the 1-3 transition of<sup>171</sup> Yb around zero field in the D1-D2 plane. The line of coherence at 49<sup>_◦_</sup> is shown in red and is the region where ∇B _f_ is minimised. At 0 mT, ∇B _f_ =0, this is the ZEFOZ point. b) Measured coherence using a Hahn echo sequence with a long wait time of 500 µs, regions with short _T_ 2 will result in a considerably smaller echo amplitude to regions with long coherence. The map corresponds well with the simulation of ∇B _f_ where the line of coherence is clearly observed with a line of larger echo amplitude. 

_6.3. Zero-Field_ 

_118_ 



<!-- Start of picture text -->
2.0<br>2.0<br>1.5 1.0<br>1.0 0 1- 0 1<br>1/(∇Bf)<br>0.5<br>0<br>0 10 20 30 40<br>2.0<br>2.0<br>1.5<br>1.0<br>1.0<br>0<br>0.5 0 0.2 0.4<br>0<br>0 0.5 1.0 1.5 2.0<br>a)<br>Field (mT)<br>Field (mT)<br>b)<br>∇Bf (MHz/mT)<br>∇Bf (MHz/mT)<br> (ms)<br>2<br>T<br> (ms)<br>2<br>T<br> (ms)<br>2<br>T<br> (ms)<br>2<br>T<br><!-- End of picture text -->

**Figure 6.8:** _T_ 2 along the line of coherence at low fields. a) As the field magnitude is reduced to zero the Hahn echo _T_ 2 increases by over an order of magnitude from (87 _±_ 4) µs at 40 mT to (1 _._ 77 _±_ 0 _._ 06) ms at 0 mT. By passing through zero the maximum coherence is observed at 0 mT (as seen in the inset). The increase in _T_ 2 is due to the decreasing ∇B _f_ which is plotted in grey and re-scaled to fir the higher field data; the mismatch in the _T_ 2 and ∇B _f_ trends is observed at low fields. b) The increase in _T_ 2 as ∇B _f_ decreases, the maximum _T_ 2 is measured where ∇B _f →_ 0. 

fields shifting the ZEFOZ point. The _T_ 2 behaviour follows the decreasing in ∇B _f_ as observed in figure 6.8b). 

While we measure over an order of magnitude increasing in _T_ 2 at zero compared to 40 mT, the measured value of (1 _._ 77 _±_ 0 _._ 06) ms is considerably lower than the high field regime where (6 _±_ 2) ms was measured. At first this seems 

_6.3. Zero-Field_ 

_119_ 

surprising, especially considering ∇B _f_ = 0 at 0 mT compared with 2 _._ 1 MHzmT<sup>_−_1</sup> at high fields. In addition, the _T_ 2 behaviour deviated from the predicted 1 _/_ ∇B _f_ dependence expected in a spectral diffusion limited environment - as seen by the grey line in figure 6.8a). This indicates that we are missing a source of decoherence from our model. 

Although low fields allow for the sensitivity of the<sup>171</sup> Yb spin to be reduced (thus increasing _T_ 2), it also results in an unpolarised electron spin environment. We showed in previous sections that electron spins of the<sup>I=0</sup> Yb isotopes were a major source of decoherence which could be polarised by low temperatures and high fields. However, the zero nuclear spin results in a spin system that is completely unpolarised at zero field (the Zeeman splitting _→_ 0). This means no matter how cold we make the system electron spin flip-flops within the<sup>I=0</sup> Yb ensemble will not be suppressed. To show this, we plot the product _T_ 2 _·_ ∇B _f_ . In the case of constant spectral diffusion _T_ 2 ∝ 1 _/_ ∇B _f_ , therefore if spectral diffusion was constant _T_ 2 _·_ ∇B _f_ would be constant. 

In figure 6.9 _T_ 2 _·_ ∇B _f_ is plotted against field using the data in figure 6.8. As zero field is approached _T_ 2 ∝ 1 _/_ ∇B _f_ decreases substantially. This means spectral diffusion is increasing faster than the<sup>171</sup> Yb ion becomes insensitive to it. As the field is increased the spectral diffusion has a smaller field dependence and _T_ 2 _·_ ∇B _f_ begins to plateau (as spectral diffusion becomes constant). 

The unpolarised<sup>I=0</sup> Yb isotopes cause significant spectral diffusion at very low fields, we therefore explore regions in field space where ∇B _f_ reaches a local minima. What we call LoFOZ (Low-First-Order-Zeeman), ∇B _f_ reaches a minimum of 0 _._ 22 MHzmT<sup>_−_1</sup> at [30 cos(49<sup>_◦_</sup> ) _,_ 30 sin(49<sup>_◦_</sup> ) _,_ 1 _._ 16](D1 _,_ D2 _,_ b) mT. This allows for low sensitivities while maintaining some polarisation of the<sup>I=0</sup> Yb electron spins. 

###### **6.3.2 LoFOZ** 

available and reach regions with low (but non-zero) ∇B _f_ . Using the 2372 MHz resonator, the LoFOZ point at [30 cos(49<sup>_◦_</sup> ) _,_ 30 sin(49<sup>_◦_</sup> ) _,_ 1 _._ 16](D1 _,_ D2 _,_ b) can be reached. First we move along the line of coherence at 49<sup>_◦_</sup> in the D1-D2 plane before performing a field sweep along the b direction. As the b axis is approximately out of plane to the resonator axis the field sweep can only be performed from _−_ 2 mT to 2 mT as the resonator will move out of reach of the spin line before turning normal beyond its critical field. In addition, the field along the b axis lifts the degeneracy of the two subsites ( _a_ and _b_ ) within the crystal, these are symmetric around zero where each reach a minimum in frequency at _≈±_ 1 _._ 2 mT. The measured resonator frequency 

_6.3. Zero-Field_ 

_120_ 



<!-- Start of picture text -->
200<br>150<br>100<br>50<br>0<br>0 10 20 30 40<br>Field (mT)<br>(1/mT)<br>f<br>B<br>∇ 2<br>T<br><!-- End of picture text -->

**Figure 6.9:** Product of _T_ 2 and the sensitivity - ∇ _B f_ . In an environment with constant spectral diffusion _T_ 2 ∝ 1 _/_ (∇ _B f_ , therefore their product is constant. When approaching zero field we observe a significant decrease in _T_ 2 _·_ ∇ _B f_ . This implies that spectral diffusion is increasing faster than the spin becomes insensitive to it. At 0 mT the electron spins associated with<sup>I=0</sup> Yb isotopes are fully unpolarised and results in an environment with a high flip-flop rate. 

A _T_ 2 field sweep is performed along the crystal b axis and two clear peaks in coherence are measured. In Figure 6.10b) the _T_ 2 reaches maxima of (0 _._ 99 _±_ 0 _._ 04) ms and (0 _._ 91 _±_ 0 _._ 30) ms at 1 _._ 28 mT and _−_ 1 _._ 22 mT respectively. The difference in the field values is attributed to a slight misalignment with the b axis. By plotting ∇B _f_ for both subsites we observe the peak at 1 _._ 28 mT corresponds with the LoFOZ point in subsite a and _−_ 1 _._ 22 mT corresponds with LoFOZ point in subsite b. 

Following the same analysis as with the ZEFOZ data the product _T_ 2 _·_ ∇ _B f_ is calculated. Plotted in figure 6.10c) we observe differing behaviour to the ZEFOZ data. Here, the LoFOZ points exhibit maxima in _T_ 2 _·_ ∇ _B f_ , this is because applying a field along the b axis further polarised the spin environment (especially<sup>I=0</sup> Yb isotopes). This means spectral diffusion is decreasing as well as ∇ _B f_ increasing. While we observe significant local improvement in _T_ 2 from the LoFOZ points, the absolute value of _T_ 2 remains behind that measured at 0 mT and significantly lower than measure at high field. This is because at 30 mT the environment is not polarised enough to allow for the low ∇ _B f_ to result in significant improvement in _T_ 2. 

We have seen that at both ZEFOZ and LoFOZ, the electron spins from<sup>I=0</sup> Yb isotopes are causing _T_ 2 to be limited by spectral diffusion. The rate at which spectral 

_6.4._ 

_121_ 

diffusion increases towards 0 mT is faster than the<sup>171</sup> Yb spin can become insensitive to it. To improve the coherence time further we need to remove this source of noise, the easiest way to do this is to remove all non-<sup>171</sup> Yb isotopes by isotopically purifying the sample. We explore this in the next section. 

##### **6.4** 

Unpolarised<sup>I=0</sup> Yb electron spins result in significant spectral diffusion at low fields, and this increases faster than the<sup>171</sup> Yb spin can become insensitive to it. The simplest and possibly the most effective way to circumvent this noise is to remove all isotopes apart from<sup>171</sup> Yb. By isotopically purifying the sample the crystal becomes far less spin active. In the following, we study an isotopically pure 171Yb:YSO with doping of 5 ppm; this means the density of 171Yb is approximately the same as in the<sup>nat</sup> Yb case. 

The same spiral resonator as in the<sup>nat</sup> Yb sample is fabricated and has a resonant frequency of 2 _._ 368 GHz, the slightly lower frequency is due to difference in the fabrication process. As the resonator is 2 MHz below the centre of the ZEFOZ point (2 _._ 370 GHz) the _T_ 2 field sweep can only be performed from _−_ 10 mT to 10 mT before the spins move out of reach of the resonator bandwidth. 

Figure 6.11a) plots the measured _T_ 2 against field along the line of coherence. In the absence of other Yb isotopes, the coherence time of<sup>171</sup> Yb is over an order of magnitude longer in the range 0–10 mT, reaching a gentle maximum of (6 _±_ 1) ms at 2 _._ 5 mT – the longest<sup>171</sup> Yb Hahn echo _T_ 2 measured in all the systems we studied in this thesis. 

As the field magnitude reaches _<_ 1 mT, the measured _T_ 2 shortens, which we attribute to the impact of<sup>89</sup> Y nuclear spins at low magnetic field. The coherence decay curves themselves exhibit electron spin echo envelope modulation (ESEEM), which occurs when the electron spin interacts with one or more neighbouring nuclear spins and the coherent quantum state is transferred between the two. 

An example of the ESEEM oscillations in the echo amplitude are presented in figure 6.11b). To fit a _T_ 2 to this a damped cosine is fitted: 



where _C_ 0 is the amplitude of the oscillations, _ωL_ is the Larmor frequency of the nuclear spin, _φ_ is the oscillation phase and _C_ 1 is the noise level. _C_ 0 is proportional to ( _B_<sup>_<u>g</u>_</sup> 0<sup>)2[136],andsoattheZEFOZpointatzerofieldboth</sup><sup>_g →_0and</sup><sup>_B_0</sup><sup>_→_0</sup> so the depth becomes undefined. Taking the limit of weak hyperfine coupling, the 

_6.4._ 

_122_ 



<!-- Start of picture text -->
Site 2a Site 2b<br>Resonator<br>a)<br>b)<br>c)<br>-1.5 0.0 1.5<br>Field (mT)<br>2376<br>2374<br>2372<br>2370<br>1.2<br>0.8<br>0.4<br>0.0<br>300<br>200<br>100<br>0<br>3.0<br>1.5<br>0.0<br>∇<br>B<br>f<br>(MHz/mT)<br>(1/mT)<br>f<br>B<br>∇<br> (ms)<br>2<br>T<br>2<br>T<br>Frequency (MHz)<br><!-- End of picture text -->

**Figure 6.10:** Low first order Zeeman (LoFOZ) coherence properties. At 30 mT along the line of coherence points with low ∇ _B f_ can be reached (0 _._ 22 MHzmT<sup>_−_1</sup> ). These points correspond to local minima in ∇ _B f_ while providing some field to allow for environmental polarisation. a) As a field along the crystal b axis is needed to reach the LoFOZ points the subsite degeneracy is lifted. The two subsites (2a and 2b) are symmetric around 0 (in b). The frequency of these two transitions is plotted as well as the measured resonator tuning which occurs from applying a field perpendicular to the resonator. b) The measured Hahn echo _T_ 2 as the field along the b axis is swept. Peaks in _T_ 2 of (0 _._ 99 _±_ 0 _._ 04) ms and (0 _._ 91 _±_ 0 _._ 30) ms at 1 _._ 28 mT and _−_ 1 _._ 22 mT respectively occur at the respective minima in ∇ _B f_ of the two subsites respectively. c) The product _T_ 2 _·_ ∇ _B f_ highlights that applying a field along the b axis polarises the environment and reduces spectral diffusion meaning _T_ 2 _·_ ∇ _B f_ increases at the LoFOZ points. 



<!-- Start of picture text -->
my Itily<br><!-- End of picture text -->





_6.5. Dynamical Decoupling_ 

_124_ 

period of ESEEM oscillations is approximately equal to 1 _/ωL_ . 

As the frequency of these oscillations is proportional to the Larmor frequency, the revival of electron spin echo goes to infinity as the field goes to zero. This means that a coherence curve cannot be fitted to the echo decay and so this appears as a decrease in the _T_ 2, this is a problem present in all systems with a strong hyperfine interaction [212]. 

Another possibility for the dip in coherence at 0 mT could also be due to the changing behaviour of the nuclear spin bath around the clock transition [195], here the<sup>89</sup> Y nuclear spins are no longer in the frozen core and so there is an increase in spectral diffusion. This interaction between the electron spin and the<sup>89</sup> Y nuclear spins is a general issue for operating quantum memory at zero field which effects all rare-earths doped in YSO, motivating studies in other host materials with lower nuclear spin concentrations [64,213,214]. 

##### **6.5 Dynamical Decoupling** 

In the previous sections, we have used both high fields with optimal orientations and ZEFOZ and LoFOZ transitions at zero (or low) fields to extend _T_ 2 to over 6 ms. While this constitutes a significant improvement (well over an order of magnitude) from other regions in field-frequency space there are further techniques we can use to extend coherence. Up to this point all the quoted _T_ 2 measurements have used a Hahn echo with varying _τ_ . In this section we will utilise dynamical decoupling techniques to protect the<sup>171</sup> Yb spin from environmental noise and extend _T_ 2. 

In dynamical decoupling sequences successive pulses are performed while the spins are on the equator of the Bloch sphere. During a Hahn echo sequence, magnetic field fluctuations may not be averaged out in the first and second wait ( _τ_ ), especially slow evolving fluctuations. The goal of dynamical decoupling sequences is to average out the coupling to the environment to zero. One of the simplest and commonly used dynamical decoupling sequences is the Carr-Purcell-Meiboom-Gill (CPMG) sequence [137,138]. 

###### **6.5.1 CPMG** 

The CPMG sequence is an extension on the conventional Hahn echo, an excitation _π/_ 2 pulse is followed by a refocusing _π_ pulse. However, the refocusing pulse is followed by repeated _π_ pulses resulting in a trail of echos as the spins refocus after each _π_ pulse. From the outset it may seem odd that successive _π_ pulses result in an echo as one may expect all the signal to be emitted after the first _π_ , however in reality only a small fraction of the intial excitation is emitted by the spins after a 

_6.5. Dynamical Decoupling_ 

_125_ 



<!-- Start of picture text -->
a)<br><!-- End of picture text -->



<!-- Start of picture text -->
π<br>π π π π<br>2 2 2<br>T  = 5.9 ± 0.2 ms<br>2<br>T  = 37  ± 3 ms<br>1<br>T  = 2.9 ± 0.3 ms<br>2<br>T   = 41 ± 3 ms<br>1,fast<br>T  = 5.7  ± 0.1 s<br>1,slow<br>Storage Time (ms)<br>Storage Time (ms)<br>TW (s)<br>b)<br>50<br>...<br>0<br>0 1 2 3 40 41 42 43<br>c)<br>30<br>20<br>10<br>0<br>0 10 20 30 40<br>d) e)<br>20<br>60<br>0<br>30<br>-20 0<br>0 4 8 0 6 12<br>(ms)<br>Voltage (mV)<br>Echo Amplitude (mV)<br>Echo Amplitude (mV)<br><!-- End of picture text -->

**Figure 6.12:** a) The CPMG sequence. A Hahn echo is followed by evenly space identical _π_ pulses, each refocusing the spins which emit an echo. The echo amplitude will then decay via _T_ 2 and the stimulated echos via _T_ 1. b) The magnitude trace during a CPMG sequence with 500 _π_ pulses. The pulses are much larger in signal and extend far beyond the axis, the echos are observed between the _π_ pulses and are integrated in the red region. The stimulated echos are observed throughout the entire sequence which lasts 42.5 ms. c) The echo amplitude corresponding to the time since the initial excitation (storage time), two different decay rates are observed corresponding to the _T_ 2 decay and the _T_ 1 relaxation of the stimulated echos. d) The measured _T_ 1 decay using inversion recovery via a WURST pulse. The echo evolves from an inverted state to the non-inverted state via two _T_ 1 mechanisms, the fast corresponding to the Purcell _T_ 1 matches well to the _T_ 1 measured in the CPMG decay. e) The Hahn echo _T_ 2, an ESEEM fit has been used to accommodate for the modulation, a field of 0.03 mT is used to fit to the oscillation period. The Hahn echo _T_ 2 is approximately half that measured via CPMG highlighting the success of dynamical decoupling. 

_6.6. Discussion_ 

_126_ 

###### Hahn echo<sup>*</sup> . 

In figure 6.12 the pulse sequence is outlined and the trace in magnitude is plotted. One of the benefits of CPMG is it substantially increases the time to measure coherence. As echos are emitted after each _π_ pulse, and each pulse 2 _τ_ further from the initial excitation, each successive echo is emitted at 2 _τ_ later than the last. This means the later emitted echos remain in a coherent state for longer and will decay with _T_ 2. However, one of the downfalls of the CPMG sequence is the prevalence of stimulated echos. Inhomogeneous fields and imperfect _π_ pulses result in stimulated echos after projection onto the _z_ axis. These stimulated echos undergo longitudinal, _T_ 1, decay and are present for much longer than those which were projected onto the _x_ - _y_ plane. 

A Gaussian was fitted to each echo and integrated over its full-width-halfmaximum (FWHM), both the fast _T_ 2 decay and the slower _T_ 1 relaxation result in a biexponetial decay of the echo amplitude as seen in figure 6.12c). Fitting a biexponetial to the data results in a _T_ 2 _,_ CPMG = (5 _._ 9 _±_ 0 _._ 2) ms and _T_ 1 = (37 _±_ 3) ms. The _T_ 1 is in good agreement with the fast _T_ 1 measured in an inversion recovery measurement of (41 _±_ 3) ms (shown in figure 6.12d)), this is the Purcell _T_ 1. 

Comparing the CPMG _T_ 2 to the Hahn echo _T_ 2 (plotted in figure 6.12e)), we observe a 2x improvement in coherence. In addition, the CPMG _T_ 2 is consistent with the longest _T_ 2 of (6 _±_ 1) ms measured at 2 _._ 5 mT. 

For a quantum memory the phase information of the stored excitation needs to be preserved. CPMG does not offer this as it was designed to only preserve the a single component of the magnetisation, therefore phase information in the transverse plane is lost [215]. In the next chapter we will outline a dynamical decoupling protocol which is compatible with quantum memories. 

##### **6.6 Discussion** 

In this chapter we have increased the coherence time of<sup>171</sup> Yb spins by over an order of magnitude. A maximum _T_ 2 of 6 ms was measured, while much lower than that measured with Bi:Si (0 _._ 3 s [96]), operation at 0 mT makes<sup>171</sup> Yb:YSO a very suitable candidate for a microwave quantum memory. 

Using a spiral resonator as 2437 MHz the full angular dependence of _T_ 2 was explored. From this the high fields and optimal field angle allowed for _T_ 2 to be increased from (96 _±_ 3) µs at _−_ 88<sup>_◦_</sup> to (6 _±_ 2) ms at _−_ 131<sup>_◦_</sup> in the D1-D2 plane. Using an angular dependent model of spectral diffusion, we showed that this is 

* 

_6.6. Discussion_ 

_127_ 

electron spin flip-flop limited. Applying the<sup>89</sup> Y model to the angular dependence we predict that a 5 GHz resonator at 3 _._ 07 T at _−_ 132 _._ 7<sup>_◦_</sup> would limit _T_ 2 to 25 _._ 5 ms, sadly well beyond our experimental setup. 

Utilising the ZEFOZ point and regions of low ∇ _B f_ at low magnetic fields in natYb coherence was extended in the local field space to (1 _._ 77 _±_ 0 _._ 06) ms, however unplorised electron spins from isotopes with zero nuclear spin resulted in a spin environment that flip-flops faster than the ZEFOZ point becomes insensitive to it. 

By removing the<sup>I=0</sup> Yb isotopes and using an isotopically pure<sup>171</sup> Yb:YSO crystal a _T_ 2 = (6 _±_ 1) ms was recorded at 2 _._ 5 mT. The ZEFOZ properties of<sup>171</sup> Yb make it a strong candidate for a quantum memory which can be incorporated in superconducting qubit quantum processors due to the low operating fields alongside long coherence. While the _T_ 2 at sub 1 mT was limited by ESEEM interactions with neighbouring<sup>89</sup> Y nuclear spins, CPMG dynamical decoupling was able to bring the coherence time back to the (5 _._ 9 _±_ 0 _._ 2) ms mark which was measured in other regimes. The limit of 6 ms is likely due to direct flip-flop ( _S_ X _S_ X + _S_ Y _S_ Y) processes which are independent of ∇ _B f_ . As this is a dipolar interaction, the rate of the flipflops is proportional to the spin density. Therefore to achieve longer coherence times a lower doping density should be used. 

A summary of the relevant _T_ 2 times measured in this chapter are displayed in figure 6.13. The use of optimal field orientations, isotopic purification and dynamical decoupling allows for the _T_ 2 to be increased by a factor of 63. This could potentially be extended to 25 ms in future experiments reaching the<sup>89</sup> Y nuclear flip-flop limit. 

Overall,<sup>171</sup> Yb has the potential to be used as a microwave quantum memory interlinked with superconducting circuits and could provide an interlink between superconducting frequencies and optical networks due to its long optical coherence at ZEFOZ [107, 108]. In the following chapter we will use the long coherence measured at low fields and develop the necessary tools needed to build a _useful_ quantum memory. 

_6.6. Discussion_ 

_128_ 



<!-- Start of picture text -->
Isotopic Purification<br>x 1.6<br>DD<br>Orientation x 2.1<br>x 63<br>-88o LoFOZ ZEFOZ -132o 2.5mT ZEFOZ ZEFOZ 89Y<br>High-Field natYb High-Field 171Yb 171Yb CPMG Limit<br>171Yb<br>103<br>102<br>101<br>100<br>10-1<br>10-2<br> (ms)<br>2<br>T<br><!-- End of picture text -->

**Figure 6.13:** Summary of the relevant _T_ 2 times measured in this chapter. The three ways of improving coherence are shown: moving to optimal field orientations at high fields, isotopically purifying the Yb:YSO and dynamical decoupling (DD). Each technique’s relative improvement is quoted. The proposed limit set by 89Y nuclear flip-flops is plotted at 25 _._ 5 ms. The green bars are measured in the<sup>nat</sup> Yb sample and the red bars in the<sup>171</sup> Yb sample. 

##### **Chapter 7** 

### **Tools for Building a Quantum Memory** 

_Stupidity got us into this mess, and stupidity will get us out._ 

|||Homer Simpson|
|---|---|---|
|**Contents**|||
|**7.1**|**Spin-Resonator Coupling . . . . . . . . . . . . **|**. . . . . . . . 130**|
|**7.2**|**Angular Dependence of Cooperativity . . . . . **|**. . . . . . . . 136**|
|**7.3**|**Adiabatic Fast Passage**<br>**. . . . . . . . . . . . . **|**. . . . . . . . 142**|
||7.3.1<br>Control . . . . . . . . . . . . . . . . . .|. . . . . . . . 144|
||7.3.2<br>Echo Silencing . . . . . . . . . . . . . .|. . . . . . . . 148|
|**7.4**|**Proposal for FIB milled YSO Memory . . . . . **|**. . . . . . . . 152**|
||7.4.1<br>Airplane Resonator . . . . . . . . . . . .|. . . . . . . . 153|
||7.4.2<br>Modelling of_g_0 . . . . . . . . . . . . . .|. . . . . . . . 154|
|**7.5**|**Discussion**<br>**. . . . . . . . . . . . . . . . . . . . **|**. . . . . . . . 155**|



In the previous chapters, we have explored the decoherence mechanisms in Yb:YSO, and shown that the _T_ 2 time can be extended to over 6 ms using high fields or ZEFOZ transitions. Given this important grounding, we can now build up the relevant tools to develop a microwave quantum memory in Yb:YSO. 

In previous work, quantum memory protocols have been shown to work in principle, with states stored and retrieved over long coherence times [96] and in 

_7.1. Spin-Resonator Coupling_ 

_130_ 

random access [106], however these experiments suffer from weak coupling between the resonator and the spin ensemble resulting in inefficient storage. 

In this chapter we will show that cooperativity _C >_ 1 can be readily achieved between a superconducting resonator and the Yb spin system, forming the basis for a high-fidelity quantum memory. We will then explore exotic pulse techniques to allow for efficient _π_ pulses over an inhomogeneous _B_ 1 field. Adiabatic fast passage is used to perform echo silencing and dynamical decoupling compatible with single photon storage. Finally, we set out a proposal for a quantum memory using a microbeam of YSO made using focus ion beam (FIB) milling which allows for high fidelity control while maintaining unit cooperativity. 

##### **7.1 Spin-Resonator Coupling** 

A hybrid quantum system by its very definition requires the coupling of different quantum systems. A solid state microwave quantum memory based on ensembles of electron spins requires the coupling of superconducting circuits to a spin ensemble. Coupling of superconducting qubits to superconducting resonators is routine in superconducting circuitry [30,32,45,83,216,217], however strong coupling between superconducting resonators and spin ensembles remains a challenge. Cooperativity greater than 1 has been achieved in several spin systems including NV centres in diamond [87,93], Cr<sup>3+</sup> doped sapphire [92], and rare-earth doped crystals [94,95], however subsequent memory protocols beyond a Hahn echo were not conducted. 

In this section we measure a cooperativity _>_ 1 for three rare-earth systems (<sup>I=0</sup> Ybnat,<sup>171</sup> Ybnat,<sup>171</sup> Yb) and show that the narrow linewidth of superconducting resonators can be used to tune the cooperativity. 

In order to measure the coupling strength between a superconducting resonator and the Yb spin ensemble, CW ESR is used. When there is large coupling between the resonator and the spins, the measured resonant frequency shifts when on resonance with the spins. In the case of strong coupling, we can no longer treat each quantum system as separate, instead they form a hybrid quantum system. The eigenstates of the Jaynes-Cummings Hamiltonian are no longer Fock states of the resonator ( _|n⟩_ ) or spin states of the electron ( _|g⟩ , |e⟩_ ), see section 2.4 for details. 

Measuring the frequency dispersion and linewidth broadening of the resonator as it passes over the spin line allows for the ensemble coupling strength and spin linewidth to be extracted. In the case of weak coupling, these appear as KramersKronig relations in ESR signals [218,219]: 



<!-- Start of picture text -->
I<br><!-- End of picture text -->

~~<mark>I</mark>~~ ~~<u><mark>~~</mark></u>~~ ~~<mark>E</mark>~~ 

_7.1. Spin-Resonator Coupling_ 

_132_ 

the behaviour in high-Q resonator systems. Superconducting resonators work in a regime where the resonator linewidth is much narrower than the spin inhomogeneous and much wider than the homogeneous linewidth (1 _/T_ 2) – _γ_ h _< κ < γ_ . In this regime one can create an efficient quantum memory with a cooperativity of 1 [99]. In this regime the number of spins within the resonator bandwidth varies as the field is swept across the spin line – reaching a maximum when the resonator is at the centre of the spin line. We therefore have to alter the picture slightly and formulate a model whereby the resonator passes through a continuum of spin linewidths with a linewidth equal to the resonator linewidth (effective spin linewidth). With each step in field the fraction of spins within the resonator is used to find the ensemble coupling strength of the effective spin line and the resonator. 

Using the same technique as in the instantaneous diffusion analysis in section 5.3 where the resonator is modelled as a Lorentzian and the spin linewidth as a Gaussian, the fraction of spins within the resonator bandwidth ( _N_ ) can be calculated. The Kramers-Kronig relations can then be modified accordingly: 



where _⟨g_ 0 _⟩_ is the average _g_ 0 over the whole ensemble. In order to calculate _N_ a cutoff in depth ( _y_ ) below the resonator of 500 µm is chosen, and the rectangular footprint ( _x_ x _z_ ) of the spiral resonator of 390 µm x 670 µm and 510 µm x 800 µm is used for the 5 _._ 04 GHz (Ybnat sample) and 2 _._ 37 GHz (<sup>171</sup> Yb sample) resonators respectively. In the Ybnat sample a nominal doping density of 50 ppm is used in the calculation, the relative abundance of _≈_ 70% and _≈_ 14% is used for the<sup>I=0</sup> Yb and 171Yb line respectively. The sites and subsites are assumed to be equally populated and so the density is divided by 4. In the isotopically pure sample a doping density of 5 ppm<sup>171</sup> Yb is used with the sites and subsites subsequently accounted for. 

In the CW data the avoided crossing can be seen to be split in two. This arises from the crystal b axis not being completely aligned with the resonator and field axes and therefore the subsite degeneracy is lifted. As fitting equations 7.2 to the frequency dispersion require a good frequency baseline we instead fit to both crossings simultaneously assuming the two spin lines have equal linewidth, ∇ _f B_ , and resonator coupling; as the splitting is small this is a fair assumption. Measuring the linewidth of the resonator across the avoided crossing is difficult, especially when 

_7.1. Spin-Resonator Coupling_ 

_133_ 

high coupling strengths result in significant resonator broadening, we therefore fit equations 7.2 to the frequency dispersion, which is much more accurately measured with the VNA. Leaving just _g_ 0 and _γ_ as free parameters, where _γ_ is used to determine _N_ , an average single spin coupling strength and the spin linewidth can be extracted. 

In figure 7.2 the frequency dispersion shift of the resonator is plotted for each of the Yb spin lines. Due to its high natural abundance, and therefore high spin density within the Ybnat sample, large frequency dispersion up to 6 MHz is measured in the I=0Ybnat spin system. The coupling between the spins and the resonator is large enough that the resonator becomes unresolvable at the centre of the spin line as its linewidth increases well beyond 3 MHz. The fits return a spin linewidth of (13 _._ 4 _±_ 0 _._ 2) MHz and an average single spin coupling strength of (5 _._ 7 _±_ 0 _._ 3) Hz. The large avoided crossing puts the spin-resonator hybrid system on the border of strong coupling. In order to sufficiently justify the strong coupling regime, vacuum Rabi oscillations should be observed - these cannot be seen here. In figure 7.2a) the simulated frequency dependence of the upper and lower branches of the Rabi splitting are plotted using: 



the measured frequencies align more accurately with the high-cooperativity dispersion shift using equations 7.2 than the Rabi splitting indicating the spinresonator system is in the high-cooperativity regime. This is further confirmed by calculating the cooperativity. Using the fitted _⟨g_ 0 _⟩_ = 5 _._ 7 Hz, the variation of the cooperativity over the spin line can be determined by: 



At the centre of the<sup>I=0</sup> Yb spin line the cooperativity reaches a peak of _C_ = 123 _±_ 8 for both subsites, placing this system well within the high-cooperativity regime. The variation of the cooperativity as the resonator passes through the spin line is plotted in figure 7.3. 

Similar analysis for both the<sup>171</sup> Yb spin systems results in fitted linewidths of (11 _._ 3 _±_ 0 _._ 4) MHz and (10 _._ 0 _±_ 0 _._ 6) MHz for the<sup>171</sup> Ybnat and<sup>171</sup> Yb system respectively, the similarity in these is expected. The single spin coupling strength is ((6 _._ 0 _±_ 0 _._ 3) Hz and (7 _._ 5 _±_ 0 _._ 5) Hz) respectively. The resulting peak coopertivities are 4.0 _±_ 0.3 and 1.4 _±_ 0.1. This means all the spin ensembles are able to reach 

_7.1. Spin-Resonator Coupling_ 

_134_ 



<!-- Start of picture text -->
γ  = 13.4 ± 0.2 MHz<br>γ  = 11.3 ± 0.4 MHz<br>γ  = 10.0 ± 0.6 MHz<br>I=0Yb<br>nat<br>171Yb<br>nat<br>171Yb<br>a) 10<br>-10<br>300 310 320 330<br>b)1.0<br>0.0<br>-1.0<br>360 370 380<br>c)<br>0.2<br>0.0<br>-0.2<br>145 155 165<br>Field (mT)<br>0<br>g0 = 5.7 ± 0.3 Hz<br>g0 = 6.0 ± 0.3 Hz<br>g0 = 7.5 ± 0.5 Hz<br>Frequency Shift (MHz)<br>Frequency Shift (MHz)<br>Frequency Shift (MHz)<br><!-- End of picture text -->

**Figure 7.2:** Fits to the frequency dispersion of the resonator as it passes through Yb spin lines. The three different spin systems -<sup>I=0</sup> Ybnat<sup>171</sup> Ybnat and<sup>171</sup> Yb - are fit to using equation 7.2 (solid green line) where the single spin coupling strength ( _g_ 0) and spin linewidth ( _γ_ ) are extracted. Equation 7.3 is also plotted (dashed black line) to show the branches of the predicted Rabi splitting. Both the spin transitions in the natural abundance return the same _g_ 0, this is expected as the same resonator and orientation are used to measure these transitions. The g- tensor is the same for the isotopes therefore the coupling to the _B_ 1 field is the same. The higher _g_ 0 measured in the isotopically pure sample is due to the larger resonator and/or the orientation of the resonator with respect to the crystal axis. The spin linewidth of<sup>171</sup> Yb remains the same in both samples. 

_135_ 

_7.1. Spin-Resonator Coupling_ 



<!-- Start of picture text -->
Site 2a Site 2b<br>140 5 2<br>70 1<br>0 0 0<br>300 330 365 375 385 150 160 170<br>Field (mT)<br>I=0Yb 171Yb 171Yb<br>nat nat<br>Cooperativity<br><!-- End of picture text -->

**Figure 7.3:** Measurement of cooperativity as the resonator moves across the spin line (with each subsite) in the three different Yb systems. Maximum coopertivities of _C_ = 123 _±_ 8 _,_ 4 _._ 0 _±_ 0 _._ 3 and 1 _._ 4 _±_ 0 _._ 1 are measured for the<sup>I=0</sup> Ybnat,<sup>171</sup> Ybnat and<sup>171</sup> Yb respectively. All systems exhibit _C >_ 1 meaning they are all suitable for quantum memory protocols. 

unitary cooperativity by choosing the field such that the resonator and spin line are not exactly on resonance. This allows for fine tuning of the cooperativity which is needed when C = 1 is a condition of the memory protocol. 

In the Ybnat sample, both fits returned the same average single spin coupling (within error). This is expected as the same resonator was used in both cases, and both isotopes have the same g-tensor. This means their coupling to the resonator _B_ 1 

The different resonator size and different orientation of the crystal axis with respect to the resonator axis means the average coupling strength in the isotopically pure sample is slightly higher, however as the doping density is lower the overall cooperativity is lower. The density of<sup>171</sup> Yb ions in the 5 ppm isotopically pure sample is about 5/7 that in the natural 50 ppm sample, as _C_ ∝ _N_ this reduces the cooperativity. 

We can compare the measured single spin coupling strength and cooperativity to the COMSOL simulations in section 4.1.2. In figure 4.8 the depth ( _y_ ) dependence of coupling strength of _g_ = 2 spins to a spiral resonator was simulated. In this case the external field was assumed to be orientated along the length of the long axis of the spiral, this means the magnitude _B_<sup>2</sup> _x_ + _B_<sup>2</sup> _y_ is used to calculate _g_ 0. Using ~~�~~ the same simulation, but altering the g factor to that for Yb results in an average _g_ 0 of 14 Hz (up to 500 µm). This is significantly higher than the measured 5 _._ 7 Hz, however in the experiment the external field is aligned to the crystal frame, not the resonator frame - this means the field will not necessarily be applied along the long axis of the spiral. The lower bound in coupling strength can be simulated by applying the external field perpendicular to the long edge. Here, the spin only 

_136_ 

_7.2. Angular Dependence of Cooperativity_ 

couples to the _By_ component of the _B_ 1 field. The average _g_ 0 in this case is 3 _._ 8 Hz. This tells us in order to build a good quantum memory we need to consider the orientation of the external field with respect to both the crystal and the resonator, we will explore this in the following section. 

##### **7.2 Angular Dependence of Cooperativity** 

The single spin coupling strength depends on the orientation of the external field with respect to the resonator. _S_ x spin transitions are driven by _B_ 1 fields which are perpendicular to the external magnetic field ( _B_ 0). For high aspect ratio resonators such as thin-ring with an inductor, or the spirals presented here with a long axis, the _B_ 1 field produced by the resonator is predominately in the _x_ and _y_ directions. When the external field is applied along the length of the resonator (along _z_ ) both the _x_ and _y_ components of the _B_ 1 field are perpendicular and the spin coupled to both. However when the field is applied across the resonator (along _x_ ) the spin only couples to the _By_ component (the _Bz_ is assumed to be negligible). In an isotropic spin system this is expressed as [168]: 



where _mi_ and _m f_ are the initial and final spin states, _γe_ is the gryomagnetic ratio, and _δ Bx,y_ are the rms field fluctuations of the _B_ 1 field. Unfortunately, the expression becomes more complex in a anisotropic system such as Yb:YSO<sup>*</sup> . 

We need to first define three different axes; the resonator axes _x_ , _y_ , _z_ , the external field axes _X_ , _Y_ , _Z_ and the crystal axes D1, D2, b. We assume that the crystal is cut so that the b direction is along **y** , and that the external field is applied in the plane of the resonator such that **Y** = **y** = **b** . In ESR it is conventional to define the _B_ 0 along **Z** . We then define two angles, _θ_ defines the offset between the external field axes and the resonator axes such that **Z** = cos _θ_ **z** + sin _θ_ **x** . _φ_ is the angle between the external field axes and the crystal angles: **Z** = cos _φ_ **D1** + sin _φ_ **D2** . These three axes are depicted in figure 7.4. 

We have previously introduced the Jaynes-Cummmings Hamiltonian in section 2.4. Here we use a more explicit form where the spin operator has been decomposed into its subsequent parts: 

*It’s never straight forward with YSO! 

_137_ 

###### _7.2. Angular Dependence of Cooperativity_ 



<!-- Start of picture text -->
Resonator Axis<br>� �<br>b<br>B<br>D 1<br>2<br>D<br>1<br>Crystal Axis Z  = cosθ �� + sinθ �<br>Field Axis<br><!-- End of picture text -->

**Figure 7.4:** Schematic of the three different axes used to determine the coupling strength. The _B_ 1 field is defined in the resonator axis, where the **z** axis is orientated along the length of the spiral. The crystal axis has its **b** axis perpendicular to the resonator, along **y** . An angle _φ_ describes the offset between the **D1** axis and **z** . The external field is applied in plane of the resonator such that **Z** = cos _θ_ **z** + sin _θ_ **x** . 



We ignore the coupling to _SZ_ spin transitions ( _⟨mi| SZ |m f ⟩_ ) – although this is important where _SZ_ clock transitions are studied [212]. _⟨mi| SX |m f ⟩_ and _⟨mi| SY |m f ⟩_ are written as the components of the _g_ tensor along the _X_ and _Y_ respectively ( _gX_ & _igY_ ). Therefore: 



using the time evolution of _a_ ˆ _,_ ˆ _a_<sup>†</sup> and _σ_ ˆ _±_ and rotating wave approximation as in section 2.4 the interaction Hamiltonian becomes: 



Redefining the energy levels and absorbing the phase into _φ_ results in a Hamiltonian which can be compared to the standard Jaynes-Cummings Hamiltonian: 

_7.2. Angular Dependence of Cooperativity_ 

_138_ 



Comparing terms results in a single spin coupling strength of: 





The components of the _g_ -tensor are obtained from the crystal basis where: 



the resulting single spin coupling strength is therefore written in full as: 



where _gD_ 1 _,D_ 2 _,b_ are the elements of the _g_ -tensor in the crystal basis. 

Using this, the distribution of the single spin coupling can be simulated. In figure 7.5, _g_ 0 is simulated below the resonator. The components of the vacuum field fluctuations were simulated in COMSOL as in section 4.1.2, equation 7.11 is then used to determine the coupling strength. The offset between the resonator and crystal axis is zero such that **D** 1 = **z** . The external field is then first set with _θ_ = 0 (fully along **z** ) and then _θ_ = _π_ /2 (fully along **x** ). When _θ_ = _π/_ 2 the _Bx_ component of the _B_ 1 field becomes redundant, thereby decreasing the coupling strength in regions where _Bx_ is large, however _g_ 0 does not decrease everywhere, this is because the new orientation of the external field vector changes the components of the g tensor in _X_ and _Y_ . In the case where the offset between the crystal and resonator axes is zero, rotating the external field from 0 to _π_ /2 increases the contribution of _By_ to _g_ 0. This is observed when comparing the difference (∆ _g_ 0) between the two angles. The regions which are dominated by _Bx_ contributions see a decrease in _g_ 0 while regions which are dominated by _By_ contributions see an increase in _g_ 0. 

In order to observe these two effects in tandem, we will now use the ensemble coupling strength ( _g_ ens) to compare. To calculate _g_ ens the spin density of 50 ppm is used and _g_ 0 is integrated down to 500 µm. In figure 7.6 the offset between the crystal 















<!-- Start of picture text -->
Il<br><!-- End of picture text -->



_7.2. Angular Dependence of Cooperativity_ 

_140_ 



<!-- Start of picture text -->
B11<br>�<br><!-- End of picture text -->



<!-- Start of picture text -->
φ<br>θ<br>� D2 B11<br>�<br>�<br>D<br>1 Z<br><!-- End of picture text -->





<!-- Start of picture text -->
φ = 0 θ = 0<br><!-- End of picture text -->

**Figure 7.6:** The ensemble coupling strength ( _gens_ ) as the offset between the crystal axis and the resonator axis ( _φ_ ) and the angle of the applied external field ( _θ_ ) are rotated. The variation in the component of the g tensor has a larger effect on the coupling strength than the fraction of the coupling to _B_ 1 _,x_ . In b) and c) the variation of _gens_ along the lines of constant (and zero) offset and field angle are plotted. 

_7.2. Angular Dependence of Cooperativity_ 

_141_ 



<!-- Start of picture text -->
π<br>0<br>-π<br>-π 0 π -π 0 π<br>Field Angle (θ) Offset (φ)<br>4.34<br>4.2<br>4.0<br>3.8<br>4.31<br>3.6<br>3.4<br>3.2 4.28<br> (MHz)<br>ens<br>g<br>)φ<br>Offset (<br>g<br>ens<br> (MHz)<br><!-- End of picture text -->

**Figure 7.7:** The ensemble coupling strength variation at -131°in the D1-D2 plane. This angle corresponds to the longest measured _T_ 2 in Yb:YSO and is the optimal point for a long-lived quantum memory. It also corresponds to the region with high coupling strength. The variation of _gens_ along this line shows cosine behaviour although the variation in _gens_ is small. The optimal working point for a quantum memory is _φ_ = -129°. 

for _T_ 2 times of up to 6 ms. The offset between the crystal axis and the resonator axis is unknown and fixed post-fabrication. We therefore overlay a line corresponding to the angle of long _T_ 2 in figure 7.7. This line corresponds to the region where the coupling strength is high - a benefit for quantum memories! Looking at how the _gens_ varies along this line shows a cosine dependence with offset, although the actual variation in _gens_ is small with the maximum and minimum being different by just 1 _._ 4%. For the most optimal quantum memory, the resonator should be fabricated so that its **z** axis is -129°from the crystal **D1** axis. 

Using the CW data recorded in the echo-detected- _T_ 2 sweeps of the angular dependence study in section 6.2 we can measure the cooperativity of the Yb<sup>I=0</sup> sub-site a transition as a function of angle. By fitting to each avoided crossing as in section 7.1 and extracting the average single spin coupling and spin linewidth, the maximum cooperativity can be calculated. We note that this data was taken using a the resonator at 2 _._ 437 GHz which has a lower linewidth than the 5 _._ 04 GHz resonator used in the previous section – _κ_ = 46 kHz, Q _≈_ 56,000 compared to _κ_ = 168 kHz, Q _≈_ 31,000. In addition to this, the physical footprint of the resonator is larger thereby increasing the absolute number of spins and average _g_ 0 of those interacting. All of these effects results in a cooperativity that is over an order of magnitude larger. With the cooperativity reaching a maximum of (2200 _±_ 200) at _−_ 128<sup>_◦_</sup> . An angular dependence of the cooperativity is observed (figure 7.8a)), with _C_ increasing from (1200 _±_ 300) at _−_ 100<sup>_◦_</sup> to (2200 _±_ 200) at _−_ 128<sup>_◦_</sup> , however the dependence does not follow the cosine dependence predicted by the model in figure 7.7. The reason for this is because the spin linewidth is not constant with angle. The measured 

_7.3. Adiabatic Fast Passage_ 

_142_ 

average single spin coupling remains constant as the field angle is rotated – this is predicted as the _gens_ angle dependence in figure 7.7 was small and the error in the fit is too large to resolve any dependence. However, as seen in figure 7.8c) the spin linewidth decreases from (14 _._ 80 _±_ 0 _._ 07) MHz at _−_ 100<sup>_◦_</sup> to (10 _._ 40 _±_ 0 _._ 05) MHz at _−_ 128<sup>_◦_</sup> . This is because the the effective _g_ -factor is decreasing, reaching a minimum at _−_ 129<sup>_◦_</sup> . Given a constant _g_ 0, the decreasing _γ_ has the effect of increasing the number of spins within the resonator bandwidth, thereby increasing the maximum cooperativity. We can therefore conclude that the angular dependence of the spin linewidth has a more significant impact on the cooperativity than either the coupling to components of the _B_ 1 field, or the components of the _g_ tensor. 

In this and the previous section we have shown that high coopertivities between an Yb spin ensemble and a superconducting resonator can be achieved. In all three Yb systems, a cooperativity _>_ 1 was measured, with a _C_ = 1 achievable by detuning the spins and the resonator. This sets the platform for a quantum memory with high efficiency as states can be written and read from the memory with minimal losses. 

Next, we explore the use of exotic pulse methods to better control the spin system and allow for memory protocol to be built up. These pulses take the form of adiabatic fast passage pulses which were used in the _T_ 1 measurements in section 5.2.1, although here we will explore their use to provide optimal _π_ pulses and perform echo silencing. 

##### **7.3 Adiabatic Fast Passage** 

Up to this point we have described a hybrid system with long coherence time, high cooperativity and potential operation at zero field. These three components provide the basis to build a useful quantum memory. To perform memory protocols _π_ high fidelity rotations of the spin ensemble are needed, in particular high fidelity pulses. Due to the nature of planar microresonators the _B_ 1 field is very inhomogeneous below the resonator (see section 4.1.2), a square pulse via the resonator will cause spins in different spacial locations to rotate by different amounts, this makes performing a desired rotation over the whole ensemble difficult. A solution to this is to use a different kind of pulse – AFP pulses. The nature of AFP is described in section 2.3.1 where the frequency of the pulse is swept from well below to well above the spin line slowly enough to allow for inversion of the entire ensemble. 

In the following experiments WURST [220] pulses are used to perform _π_ rotations. As the resonator bandwidth is much narrower than the spin linewidth, we sweep the frequency across the resonator linewidth. We have already seen briefly the use of WURST pulses to perform an inversion to measure _T_ 1, however here we 

_7.3. Adiabatic Fast Passage_ 

_143_ 



<!-- Start of picture text -->
a) 2500<br>2000<br>1500<br>1000<br>500<br>0<br>b) 12 c)<br>12<br>8<br>8<br>4<br>4<br>0 0<br>Angle D1-D2 (o)<br>Angle D1-D2 (o) Angle D1-D2 (o)<br>-130 -120 -110 -100<br>-130 -120 -110 -100 -130 -120 -110 -100<br>Cooperativity<br> (Hz)<br>0<br>g γ (MHz)<br><!-- End of picture text -->

**Figure 7.8:** a) The angular dependence of the maximum cooperativity measured by fitting the frequency dispersion relation (equation 7.2) to the Yb<sup>I=0</sup> avoided crossings measured in the angular dependent _T_ 2 data from section 6.2. The very high coopertivities are due to the resonator which has a narrower linewidth to that in figure 7.3 and a larger footprint resulting in a higher average _g_ 0. An angular dependence of the cooperativity is observed although it does not follow the cosine behaviour predicted by the models. Instead the increase in coherence is related to the narrowing of the linewdth as angles with lower effective _g_ factor are reached. The average single spin coupling remains constant with angle (b)) at _≈_ 10 _._ 5 Hz while the spin linewidth ( _γ_ ) decreases (c)) from (14 _._ 80 _±_ 0 _._ 07) MHz at _−_ 100<sup>_◦_</sup> to (10 _._ 40 _±_ 0 _._ 05) MHz at _−_ 128<sup>_◦_</sup> . the narrower spin linewidth means the number of spins within the resonator linewidth is larger resulting in a higher cooperativity. 

_7.3. Adiabatic Fast Passage_ 

_144_ 

shall go into more detail on this inversion as well as the use of BIR ( _B_ 1 Insensitive Rotation) [141] pulses to perform Rabi oscillations. 

###### **7.3.1 Control** 

WURST pulses offer a way to perform _π_ pulses over the entire spin ensemble. Given the capabilities of the home-built ESR spectrometers available, WURST pulses are fairly straightforward to perform. Using WURST pulses of order 20 the length of the pulse is swept while measuring the phase of the resulting echo. The chirp rate was maintained at a fixed 20 MHzms<sup>_−_1</sup> therefore reducing the WURST length has the effect of reducing the bandwidth of the frequency sweep. To test the inversion of the WURST pulse a standard square pulse Hahn echo is used. The WURST pulse is applied and then 1 ms later a Hahn echo sequence with _τ_ = 40 µs is used to read the polarisation of the spin ensemble. In figure 7.9 the echo traces arising from each WURST pulse are shown. For very short WURST durations, the WURST bandwidth is narrower than the resonator bandwidth, this means the whole spin ensemble is not inverted and the resulting echo is positive. Once the WURST bandwidth is much wider than the resonator bandwidth an efficient inversion of the spin ensemble can take place. The echo amplitude subsequently plateaus as the WURST duration is increased further, with a fixed chirp rate and sweep much wider than the resonator bandwidth, the refocused spins are insensitive to the ends of the WURST pulse. 

One striking result is the reduction of the duration of the WURST duration compared with AFP memories in Bi:Si [106]. In both systems a chirp rate of 20 MHzms<sup>_−_1</sup> is used, however WURST durations of 200 µs were used in the memory protocol. Here, a good inversion can be achieved with 50 µs pulses therefore allowing a 4 _×_ improvement in the clock speed of any AFP memory. The main reason for this is the improved power capabilities of the experimental setup. Here, we supply pulses to the resonator via a PCB (rather than 3D cavity, resulting in larger coupling to the resonators). In addition, the narrower resonator linewidth (140 kHz compared to 380 kHz) means the WURST bandwidth needed for inversion is narrower therefore the pulse can be shorter. 

In figure 7.10 the inversion from a 50 µs pulse is shown in full. To determine the effectiveness of the WURST the phase of the echos is determined. We choose an initial starting echo with phase 51 _._ 67<sup>_◦_</sup> so the inversion is observed in both _I_ and _Q_ . After applying the WURST pulse the phase of the echo is 232 _._ 07<sup>_◦_</sup> , this corresponds to a rotation of (180 _._ 4 _±_ 2 _._ 3)<sup>_◦_</sup> . While the rotation is performed with high accuracy, there is a reduction in the magnitude of the echo. Using each channel of the echo 

_145_ 

_7.3. Adiabatic Fast Passage_ 



<!-- Start of picture text -->
Time (μs)<br>a)<br>20<br>120<br>80<br>0<br>40<br>-20<br>0<br>b) 0 20 40 60 80<br>20<br>10<br>0<br>-10<br>-20<br>0 40 80 120<br>WURST Duration (μs)<br>      I Channel<br>Chirp Rate = 20 MHz/ms<br>Resonator Bandwidth<br>I<br>Q<br>WURST Duration (μs)<br>Echo Amplitude (mV)<br>Signal (mV)<br><!-- End of picture text -->

**Figure 7.9:** WURST pulse inversion as duration of the pulse is increased. A Hahn echo sequence with square pulses is used to read the state of the ensemble 1 ms after a WURST pulse of specified length. The chirp rate is kept constant at 20 MHzms<sup>_−_1</sup> . In a) the echo traces in the I channel are plotted as the WURST duration is increased, for short WURST pulses the WURST bandwidth is narrower than the resonator bandwidth and so the spin ensemble is not inverted. In b) the echo is inverted as the WURST duration becomes sufficiently longer than the resonator bandwidth. The echos integrated at FWHM are plotted, the inversion plateaus as the edges of the WURST pulses invert fewer and fewer spins. 

_146_ 

_7.3. Adiabatic Fast Passage_ 



where _A_ 0 is the echo amplitude in the absence of a WURST pulse and _AW_ is the WURST echo amplitude. A WURST efficiency of 88.2 % in _I_ and 88.7% in _Q_ was measured resulting in a total efficiency of 77.0 %. The primary limitation for this is the WURST pulse not inverting the whole ensemble as there are many spins far from the resonator which are weakly coupled. These spins need a slower chirp rate in order for the adiabatic condition to be met. 

The adiabaticity factor is given by: 



where _ν_ is the precession frequency around the effective field and _R_ is the chirp rate. _Q_ should be _≫_ 1 for all spins to be inverted, therefore we can calculate a minimum _g_ 0 for which an inversion is possible. _ν_ is minimum when the WURST frequency is equal to the Rabi frequency ( _g_ eff _B_ 1) of the spin. Using the power capabilities of the setup where _≈−_ 25 dBm reaches the sample, the current through the resonator during the pulse ( _I_ = ~~�~~ _P/Z_ ). Using this the following equation can be used to find the _g_ 0 which is needed to meet _Q_ = 1: 



where _δ i_ is the zero point current fluctuations in the resonator and _I_ is the current in the resonator during a pulse. Using equation 7.16 and a power of -25 dBm ( _I_ = 1.78 mA) and _δ i_ = 1.74 nA gives a _g_ 0 _,Q_ =1 = 1.18 Hz. By comparing with simulations of _g_ 0 this corresponds to a depth of 1.19 mm. This means the inversion is complete through almost the entire crystal which is 1.7 mm thick – this reflects the high inversion efficiency. The limitation of this is the amount of power which can be coupled into the resonator from the PCB. 

In addition to spin ensemble inversion, AFP pulses can be used to complete arbitrary rotations around the Bloch sphere. BIR pulses are comprised of four adiabatic half-passage (AHP) pulses where a phase jump is applied between the first and second, and third and fourth pulse. This phase jump is equal to _π_ + _θ /_ 2 where _θ_ is the desired rotation on the Bloch sphere. Using a BIR pulse length of 100 µs (double the length of the WURST given the four half-passage segments) and a chirp of 1 MHz allows for Rabi oscillations to be observed. Using a BIR pulse followed 

_7.3. Adiabatic Fast Passage_ 

_147_ 



<!-- Start of picture text -->
a)<br>20<br>0<br>-20<br>0 40 80 120<br>b)<br>20<br>0<br>-20<br>0 40 80 120<br>c)<br>20<br>10<br>-20 -10 10 20<br>-10<br>-20<br>I<br>Q<br>Time (μs)<br>Q (mV) Time (μs)<br>No WURST<br>23%<br>180.4 o<br>I (mV)<br>WURST<br>Signal (mV)<br>Signal (mV)<br><!-- End of picture text -->

**Figure 7.10:** The inversion effectiveness of a 50 µs WURST pulse with chirp rate 20 MHzms<sup>_−_1</sup> . In a) and b) the WURST pulse clearly inverts the echo in both channels. Using the phase of the echos (c) an angle of 180 _._ 4<sup>_◦_</sup> is applied via the WURST pulse – thereby providing an accurate _π_ pulse. The efficiency of the inversion is 77% as some of the spin line (spins with small _g_ 0) are not inverted and the magnitude of the echo decreases. 

_7.3. Adiabatic Fast Passage_ 

_148_ 



<!-- Start of picture text -->
π+θ/2<br>Phase<br>π 2π 3π 4π<br>θ<br>15<br>10<br>5<br>0<br>-5<br>-10<br>-150<br>Echo Amplitude (mV)<br><!-- End of picture text -->

**Figure 7.11:** Rabi oscillations using BIR pulses to rotate the spin ensemble around the Bloch sphere. A phase shift in the BIR pulse allows for arbitrary rotations causing the echo to rotate from positive to negative. 

by a standard Hahn echo to read out, the echo oscillates from positive to negative as the starting magnetisation vector is rotated from +Z to -Z on the Bloch sphere. In figure 7.11 the echo amplitude is plotted as _θ_ is varied. Fitted to this is a cosine with a global phase as a fit parameter, this returned a global phase of 0 _._ 4 _π_ . Intriguingly, taking the maximum and minimum echo, the _π_ (inversion) efficiency is 96.8%, higher than the WURST pulse. This could be due to slower chirp rate and thus more spins meet the adiabatic condition. 

BIR pulses give full control of the entire spin ensemble and provide a key part of an eventual quantum memory. Single qubit gates can be applied to the state within the memory without the need to return the state to the quantum processor. The WURST pulses offer an inversion of the spin ensemble, but their power in quantum memories comes from their ability to silence unwanted echos. It is this ability which makes them the building blocks of the random access quantum memory protocol. 

###### **7.3.2 Echo Silencing** 

Being able to restrict emission from the excited state is an important element to a quantum memory based of ensembles of spins. We have seen that WURST pulses can be used as inversion _π_ pulses where they can replace a typical square pulse, however when using WURST pulses as refocusing _π_ pulses a single pulse does not refocus the echo. This process is outlined in section 2.3.1 where two identical pulses are needed to put the ensemble in a coherent state where collective emission can occur. The resulting echo is therefore emitted from the ground state and is not 

_7.3. Adiabatic Fast Passage_ 

_149_ 

susceptible to the noise arising from excited state emission. 

We observe the need for echo silencing by applying an increased number of WURST pulses before the Hahn echo sequence, this alternates the emission from the excited to ground state. In figure 7.12 the echo amplitude decays as the number of pulses increases – likely due to spin saturation. However there is an alternating pattern in the amplitude from even to odd number of inversion pulses. Those with an odd number of pulses have a lower amplitude to those with an even number, this indicates there is additional noise arising from excited state emission. While this may be due to superradiant effects, it is possible the WURST pulses are introducing systematic noise which is cancelled when applied in pairs. In addition, the odd-even behaviour is within the error bars and so concrete conclusions cannot be drawn. The echo after two WURST pulses is 35 _._ 9% that of the echo from one WURST pulse, much lower than the WURST efficiency of 77%, this is due to the WURST pulse saturating spins, inverting previously uninverted spins and the lower noise level from emission from the non-inverted state. 

To silence the echo, two identical WURST pulses with length 50 µs and chirp of 0 _._ 5 MHz were used. In figure 7.13a) the silencing of the echo between the two WURST pulses is clearly observed before being retrieved with a global phase shift after the second pulse. 

Echo silencing can be used to engineer a dynamical decoupling sequence to extend the coherence time of the spins. In a CPMG sequence with square pulses, where the echos are not silenced, a significant proportion of the signal is emitted (and therefore lost) with each _π_ pulse. While this is not an issue in conventional ESR where the excitation pulse is typically very powerful and so even with high coupling strengths there are still spins which have not emitted back into the resonator and the coherence can still be measured. In quantum memories the excitation which is stored in the spin ensemble is a single photon. In a memory with unit cooperativity the photon would be emitted from the first decoupling _π_ pulse and the rest of the sequence would be redundant. 

We can use the echo silencing of WURST pulses to create a dynamical decoupling sequence which is suitable for single photons in the memory. The ABBA sequence uses two different WURST pulses (A and B) which have different chirp rates such that they do not refocus each other. An initial A pulse applies a phase pattern to the spins with the stored photon. To increase the coherence a series of B WURST pulses act as _π_ pulses and result in a CPMG style dynamical decoupling sequence, as the initial A phase pattern remains of the spin ensemble the photon is not emitted from the ensemble. A final A pulse is applied when the photon is 

_150_ 

_7.3. Adiabatic Fast Passage_ 



<!-- Start of picture text -->
I<br>Q<br>Number of WURST Inversions<br>N<br>...<br>a)<br>40<br>20<br>0<br>-20<br>-40<br>60<br>b)<br>40<br>20<br>0<br>0 2 4 6 8 10<br>Echo Amplitude (mV)<br>Echo Amplitude (mV)<br><!-- End of picture text -->

**Figure 7.12:** Hahn echo sequences with an increasing number of WURST inversion pulses applied before. This switches the phase of the echo by 180<sup>_◦_</sup> as the echo is emitted from the non-inverted and inverted state (a)). b) When there is an even number of pulses (red markers), the echo amplitude is comparatively higher than with an odd number of pulses. This is due to the increased noise from excited state emission. The overall decay of the echo amplitude is due to the saturation of the spins from consecutive high power pulses. 

to be read which puts the spins into a collective state and they emit back into the resonator. 

In 7.13 the sequences AAAA and ABBA are shown. An A pulse with chirp rate 10 MHzms<sup>_−_1</sup> and B pulse with chirp rate _−_ 8 MHzms<sup>_−_1</sup> was used. The echo between the B pulses does not appear in the latter, with a small echo (slightly smaller than the AAAA) case emitted at the end of the sequence. By increasing the number of B pulses and measuring the amplitude of the final echo a _T_ 2 can be measured and the effectiveness of the dynamical decoupling sequence can be assessed. 

Figure 7.14 shows the coherence curves for both the AAAA and ABBA sequences. A short _τ_ of 40 µs is used and the<sup>171</sup> Yb spin ensemble was measured at 0 mT and 2368 MHz. The AAAA CPMG sequence can collect all the data in one trace as an echo is emitted after every two A pulses. In the ABBA sequence each 

_151_ 

_7.3. Adiabatic Fast Passage_ 



<!-- Start of picture text -->
a)<br>Time (μs)<br>b) c)<br>Time (μs) Time (μs)<br>40<br>20<br>0<br>-20<br>-40<br>0 100 200 300<br>40<br>20<br>0<br>-20<br>-40<br>0 200 400 600 0 200 400 600<br>Signal (mV)<br>Signal (mV)<br><!-- End of picture text -->

**Figure 7.13:** a) Echo silencing using two identical WURST pulses with chirp rate of 10 MHzms<sup>_−_1</sup> . The first initial WURST pulse doesn’t result in an echo which is only emitted when a second identical pulse is applied. In b) and c) dynamical decoupling sequences can be constructed with WURST pulses. In the ABBA (c)) sequence, the excitation can be stored in the memory and have its coherence extended with dynamical decoupling without losing signal. 

data point requires a new trace where an additional two B pulses are added. Fitting a standard _T_ 2 decay to the data and normalising the coherence to allow for comparison we can see that a longer _T_ 2 is measured from the ABBA sequence – (10 _._ 4 _±_ 0 _._ 6) ms compared with (6 _._ 4 _±_ 0 _._ 4) ms. This is likely due to the additional decay experienced by the AAAA sequence where a proportion of the stored excitation is emitted with each pair of A pulses. In addition, this shows the suitability of the ABBA sequence as a dynamical decoupling protocol for single photons stored in the memory as the coherence time is significantly longer than the Hahn echo _T_ 2 measured in chapter 6 of (2 _._ 9 _±_ 0 _._ 3) ms. We also note the agreement between AAAA CPMG and square pulse CPMG from chapter 6 where the _T_ 2 _,_ CPMG = (5 _._ 9 _±_ 0 _._ 2) ms. 

While we have successfully shown control and echo silencing using AFP, the stored excitations are very large and are only phase coherent rather than _quantum_ states. Due to the readout capabilities of the experiment (a HEMT amplifier at 4 K), weak excitations and therefore weak echos could not be measured. The powerful excitations also result in the presence of several stimulated echos where adding ad- 

_152_ 

_7.4. Proposal for FIB milled YSO Memory_ 



<!-- Start of picture text -->
AAAA  T  = 6.4 ± 0.4 ms<br>2<br>ABBA  T  = 10.4 ± 0.6 ms<br>2<br>10 20 30<br>Storage Time (ms)<br>1<br>0.5<br>0<br>0<br>Normalised Echo<br><!-- End of picture text -->

**Figure 7.14:** Dynamical decoupling using WURST pulses. Two sequences, one with identical WURST pulses (AAAA) substitutes the square pulses in CPMG with WURST (A) pulses and an echo is emitted after each pair of A pulses. The data is all taken in one trace with the amplitude of each refocused echo plotted. In the ABBA sequence the B WURST pulse does not refocus the A pulse. As the number of B pulses is increased the excitation is stored for longer, the data is taken over multiple traces where the number of B pulses is increased and the echo after the final A pulse is measured. The ABBA sequence has a longer _T_ 2 of (10 _._ 4 _±_ 0 _._ 6) ms as fractions of the stored excitation are not emitted with each additional pair of WURST pulses. This allows the ABBA sequence to be used as a dynamical decoupling sequence for single photon memories. 

ditional strong excitations results in the refocusing of previously stored excitations. We therefore could not perform multi-mode storage with the current device. In order to facilitate multi-mode storage modifications need to be made to the device and the surrounding experimental setup. In the following section we shall outline a proposal for a device and experiment which can utilise the results from the previous three chapters to make a _useful_ quantum memory with<sup>171</sup> Yb:YSO. 

##### **7.4 Proposal for FIB milled YSO Memory** 

for a microwave quantum memory: 

- Understanding the spin system & decoherence mechanisms (Chapter 5) 

- Long coherence time (Chapter 6) 

- 

- Cooperativity = 1 (Section 7.1) 

- Quantum control of spin ensemble (Section 7.3.1) 

_153_ 

_7.4. Proposal for FIB milled YSO Memory_ 

- Echo silencing (Section 7.3.2) 

- Single-photon dynamical decoupling (Section 7.3.2) 

However in order to facilitate the storage of multiple quantum states at the single photon level further improvements are needed to the system. They are: 

- 

- Readout of echos at the low photon number limit 

In this section we propose a microwave quantum memory based on a piece of<sup>171</sup> Yb:YSO which has been milled using a focus ion beam. This piece is then coupled to a new design of superconducting resonator – airplane resonator. 

###### **7.4.1 Airplane Resonator** 

Several resonator designs such as the thin-ring suffer from the fact that a significant proportion of the echo signal comes from spins coupling to the capacitive region of the design. Spirals on the other-hand allow for coupling to the entire design, but this then limits the maximum _B_ 1 fields (and therefore _g_ 0) which the spins interact with. In order to satisfy both of these constraints a resonator design with a clear narrow inductor and large capacitor should be used with the spins spatially confined to beneath the inductor wire. For dopants in silicon spatially confining the spins is relatively straightforward as implantation techniques are common place in CMOS technologies, however the implantation of rare-earth spins into YSO is challenging and results in significant crystal damage. YSO implanted with Er<sup>3+</sup> ions resulted in very large inhomogeneous broadening dominated by the distorted crystal field [221, 222]. While implantation into the YSO substrate would be the ideal process for a scalable memory, the premature nature of these techniques means we used a different approach to spatially confine the spins. 

Focus ion beam (FIB) milling allows for regions of the YSO crystal to be cut away – physically removing<sup>171</sup> Yb spins. FIB YVO crystals have been used to make intricate photonic cavities for use in optical quantum memory experiments [79] with similar structures made with YSO crystals [223]. To confine the spins, we propose a microbeam which is milled to be the length and width of the resonator inductor, it is then placed directly onto the surface of the resonator. 

The microbeam would be integrated with an ‘airplane’ resonator. This resonator design is formed of a doubled-back inductor connected to a large interdigitated capacitor. The large capacitance results in a low impedance resonator which is desirable for ESR applications. A microscope image of an airplane resonator 

_154_ 

_7.4. Proposal for FIB milled YSO Memory_ 





<!-- Start of picture text -->
FIB YSO<br><!-- End of picture text -->



**Figure 7.15:** Optical microscope images of an airplane resonator targeting 2 _._ 37 GHz. The resonator is formed of a double back inductor loop where the FIB YSO microbeam is placed with a large interdigitated capacitor attached to reduce the frequency and impedance. 

is shown in figure 7.15. An inductor with width 2 µm double backs on itself with a 4 µm gap forming a 30 µm long inductor loop. This is then connected to an interdigitated capacitor with finger width of 50 µm and gap 10 µm. In order to target the ZEFOZ point at 2 _._ 37 GHz the capacitor needs to be large – approximately 1 _._ 3 mm x 1 _._ 1 mm. The resonator is patterned with 20 nm NbN onto a sapphire substrate. The FIB YSO microbeam sits over the inductor loop allowing for a uniform _B_ 1 through the beam. 

The microbeam is milled into a triangular prism (this is easiest with the milling techniques) with a height of 5 µm, using a micro-manipulator it is then placed onto the resonator and is held by Van der Waals forces. The crystal b axis remains the approximately perpendicular to the resonator plane. 

###### **7.4.2 Modelling of** _g_ 0 

The thin doubled-back inductor has the of higher _B_ 1 and therefore higher _g_ 0. The microbeam removes spins with low _g_ 0 meaning the entire spin ensemble can be controlled with short WURST pulses. We model the distribution of _g_ 0 by considering a triangle above the two inductor wires and then assuming the distribution is uniform along the length of the inductor. In figure 7.16 the _B_ 1 field distribution and in turn the single spin coupling are plotted for a 10 µm wide prism. Due the narrow inductors high coupling strengths up to 4 _._ 5 kHz directly next to the resonator are simulated. These however are not physically achievable as there will be a gap between the microbeam and the resonator. 

By varying the width of the beam we can make the distribution of _g_ 0 more or less homogeneous. As the beam becomes narrower than the gap between the 

_7.5. Discussion_ 

_155_ 

inductor wires (4 µm) the spins are no longer in the regions with the highest _g_ 0, however a higher percentage of the spins occupy the inner region which is where the field is the most homogeneous. By plotting a histogram of the _g_ 0 for varying widths we see that all widths have a peak at 1 _._ 2 kHz, this corresponds to the coupling strength at the centre of the two wires. A shoulder between 0 _._ 2 kHz and 1 _._ 2 kHz is observed, this relates to the _g_ 0 distribution in _y_ through _x_ = 0. 

By calculating the cooperativity given a<sup>171</sup> Yb spin density of 5 ppm there is a trade-off between high-cooperativity and homogeneous _g_ 0. Meeting _C_ = 1 is an important criterion of a microwave quantum memory and should be prioritised over a slight improvement in homogeneity as the latter can be compensated with different WURST parameters. In order to meet _C_ = 1 the width of the beam should be at least 8 µm wide, effectively covering the two inductor wires and the gap between them. 

This shows the high average single spin coupling strengths can be achieved while maintaining _C_ = 1. A beam of width 8 µm has a minimum _g_ 0 = 84 Hz, this means using the same power as section 7.3.1 WURST pulses of below 700 ns could in principle be used to achieve inversion. Given suffient WURST orthogonality and a _T_ 2 of 10 ms, 7100 states could be stored at a time. All these components together would form a state of the art microwave quantum memory and could be used to perform holographic quantum computing techniques [224]. 

##### **7.5 Discussion** 

In this chapter we have turned<sup>171</sup> Yb from a spin system with long _T_ 2 into the basis of a microwave quantum memory. Strong coupling strengths with cooperativity _>_ 1 was measured in all three Yb spin systems (including natural and isotopically pure<sup>171</sup> Yb). The narrow linewidth of superconducting resonators allows the cooperativity to be tuned to 1 by detuning the resonator and the spin line. Being able to precisely meet the C = 1 impedance matching condition allows for a highly efficient quantum memory, this is seen by a WURST inversion efficiency of 77 %. 

Quantum control techniques such as AFP allow for the whole ensemble of spins to be controlled in an inhomogeneous _B_ 1 field. WURST pulses of length 50 µs were used to apply _π_ pulses and also silence echos from the excited state in the form of the AAAA and ABBA sequences. BIR pulses can also be used to apply single qubit gates the the memory. 

Single photon dynamical decoupling via ABBA is an important tool in building a quantum memory. The coherence time of the stored state is increased from 6 ms to 10 ms while only emitting the echo once the state needs to be read out. In a system with C = 1 and control over the whole ensemble the entire state is emitted resulting 











<!-- Start of picture text -->
10 . 0<br>9. 0 1<br>ma 8 . 02<br>am 7 . 03<br>mm 6 . 04<br>wm 5 . 05<br>mm 4 . 06<br>mm 3 . 07<br>mm 2 . 08<br>1. 09<br>ms 0 . 10<br>po SARI | i<br><!-- End of picture text -->

_7.5. Discussion_ 

_157_ 

Using these demonstrations we propose a quantum memory with spatially confined<sup>171</sup> Yb spins via a FIB milled microbeam. This microbeam placed over the inductor of an airplane resonator eliminates spins with small _g_ 0 allowing for shorter AFP pulses while maintaining C = 1. The final limiting component is a readout setup capable of measuring signals on the few photon scale. To do this a quantum limited amplifier in the form of a Josephson Parametric Amplifier (JPA) [225–227], tunneling wave parametric amplifier (TWPA) [228,229] or kinetic inductance parametric amplifier (KIPA) [164,179]. KIPAs are the most attractive option for this due to their ease of fabrication (not requiring Josephson junctions), compatibility with spin qubit frequencies and high dynamic range. In addition, as KIPAs are comprised of a superconducting resonator, they can be used to drive and detect spins directly, allowing for amplification of echos as soon as they are emitted [230]. 

However, these amplifiers are only needed while developing the quantum memory where external excitations are used and the resonator is directly readout. In a fully integrated memory, the qubit coupled to the memory would be read using standard QED techniques, this in turn is connected to wider quantum computing architecture. 

##### **Chapter 8** 

### **Conclusion and Outlook** 

The work outlined in this thesis sets the foundations for a microwave quantum memory based on<sup>171</sup> Yb spins in YSO. By fabricating high-Q superconducting resonators onto Yb:YSO high sensitivity ESR was performed. ESR techniques were subsequently used to measure the spin properties of the Yb ensemble, increase coherence times and develop protocol for quantum memories. 

In each of the results chapters key developments were made to reach the goal of building a useful microwave quantum memory. 

In chapter 5 we explored the decoherence mechanisms at play in rare-earth doped YSO. CW ESR with high-Q ( _≈_ 60,000) resonators allowed for the spin species in Ybnat:YSO to be quickly and accurately resolved. Large avoided crossings from Yb spins with zero nuclear spin can be used to align the external field to the YSO crystal axis. Two decoherence mechanisms were found to be important in bulk ensembles of rare-earth spins. Instantaneous diffusion arises in the I=0Yb ensemble due to its high spin concentration. We showed how using the narrow linewidth of the superconducting resonator the effect of instantaneous diffusion could be measured via a dip in _T_ 2 at the centre of the spin line. This also offers a new technique for measuring spin concentration in highly doped systems. The second decoherence mechanism which limits _T_ 2 is spectral diffusion. Using the temperature dependence of<sup>171</sup> Yb and<sup>145</sup> Nd a model of spectral diffusion accounting for flip-flops in environmental electron spin ensembles accurately predicts the _T_ 2 behaviour. With this, the _T_ 2 of<sup>171</sup> Yb was increased from (33 _±_ 7) µs at 1 _._ 2 K to (3 _._ 38 _±_ 0 _._ 09) ms at 14 mK. In addition to this, stimulated three-pulse echo measurements confirm the presence of spectral diffusion at 14 mK arising form<sup>89</sup> Y nuclear spins within the YSO crystal itself. 

Using this understanding of the spin dynamics we showed how the coherence time of<sup>171</sup> Yb could be increased in chapter 6. The _T_ 2 time was increased by over an 

_159_ 

order of magnitude to a maximum of (6 _±_ 1) ms. Two different regimes were used to increase coherence, the first was by using high fields and optimal field orientation to both polarise the environment and suppress the<sup>171</sup> Yb spin sensitivity to spectral diffusion. A _T_ 2 of (6 _±_ 2) ms was measured at 1 _._ 07 T _−_ 131<sup>_◦_</sup> . These high fields are not compatible with large scale superconducting circuitry and so the zero field ZEFOZ point was utilised to increase _T_ 2 by making the<sup>171</sup> Yb spin insensitive to environmental field noise. The use of the ZEFOZ point and isotopic purification (to eliminate unpolarised<sup>I=0</sup> Yb spins) allowed the coherence time to be increased to (6 _±_ 1) ms at 2 _._ 5 mT with ESEEM causing an artificial coherence decrease at lower fields. Dynamical decoupling at 0 mT increased the _T_ 2 to (5 _._ 9 _±_ 0 _._ 2) ms – the same as the other regimes. All these techniques had the effect of increasing _T_ 2 back a factor of 63, with a potential maximum _T_ 2 of 25 ms predicted as the limit given by the<sup>89</sup> Y nuclear spins. 

Finally, in chapter 7 we used our understanding of the<sup>171</sup> Yb spin system and its long coherence to lay the groundwork for a useful microwave quantum memory. High coupling strengths with cooperativity _>_ 1 were measured in all three Yb systems, including isotopically pure<sup>171</sup> Yb which had the longest measured _T_ 2. Due to the narrow bandwidth of the superconducting resonator, the cooperativity could be tuned by detuning the resonator from the spin line. This allows for precise tuning of the cooperativity to 1 which results in an efficient quantum memory. Adiabatic fast passage was used to accurately and efficiently control the ensemble of<sup>171</sup> Yb spins. WURST pulses provided inversion with 77 % efficiency and BIR pulses allow for Rabi oscillations in an inhomogeneous _B_ 1 field. Echo silencing and dynamical decoupling with WURST pulses allows for echo emission from the ground state and on demand echo retrieval, both important features of a quantum memory. The ABBA sequence allows for CPMG style dynamical decoupling on a single photon stored in a spin ensemble. Finally, we have put forward a proposal for a state of the art quantum memory using FIB milled Yb:YSO. Containing the spins above the inductor allows for high single spin coupling strengths and homogeneous _B_ 1 fields while maintaining unit cooperativity. the elimination of weakly coupled spins means faster WURST pulses can be used, increasing the clock cycle and storage capacity of the memory. 

So what does the future hold for solid state quantum memories? We have never been closer to efficient coherent transfer of quantum information between a superconducting qubit to a spin ensemble. The work by Kubo and Grezes [90] may now be fully realisable using the proposal we put forward in chapter 7. The airplane resonator needs to be coupled to a superconducting waveguide, which in turn can 

_160_ 

be coupled to a qubit. The memory we have proposed should be able to store and retrieve the single photon emitted by the superconducting qubit with high efficiency thus showing a proof of principle experiment for a larger scale technology. 

In order to build a truly scalable memory implantation into the substrate will be required. For rare-earth doped crystals this technology remains premature and research into the spin properties of implanted crystals is needed before memories can be developed. Implantation of Bi [96,106] (and soon Te [212]) donors in silicon has been used to perform spin memory experiments. The implantation layer was uniform over the whole chip and so spins remained under the capacitive regions of the resonator. Implantation using a mask is the next step for these memories so that the implanted spins are solely below the inductive region and the benefits outlined in chapter 7 can be realised. This would also enable easier integration with large scale superconducting processors as donor spins would not be underneath the qubits and cause possible decoherence. 

An alternate direction for future work is integrating the microwave memory developed here into optical setups. Utilising the superb optical properties of rareearths allows this platform to be use in transducer technology. The FIB milled nanophotonic cavities made by Zhong et al. [79] are natural starting place for such a transducer. These nanophotonic cavities could be places onto the inductor of a superconducting resonator and with AFP control techniques and optical pumping microwave photons could be up-converted into optical photons. This is where the rare-earths offer a significant advantage over dopants in silicon and provide a tantalising yet achievable path to large scale quantum networks and the quantum internet. 

### **Bibliography** 

- [1] Evan R MacQuarrie, Christoph Simon, Stephanie Simmons, and Elicia Maine. The emerging commercial landscape of quantum computing. _Nature Reviews Physics_ , 2(11):596–598, 2020. 

- [2] Mind Commerce. Quantum technology market by computing, communications, imaging, security, sensing, modeling and simulation 2022 - 2027, feb 2022. 

- [3] Richard P Feynman. Simulating physics with computers. In _Feynman and computation_ , pages 133–153. CRC Press, 2018. 

- [4] Jan Hermann, Zeno Schätzle, and Frank Noé. Deep-neural-network solution of the electronic schrödinger equation. _Nature Chemistry_ , 12(10):891–897, 2020. 

- [5] David Deutsch. Quantum theory, the church–turing principle and the universal quantum computer. _Proceedings of the Royal Society of London. A. Mathematical and Physical Sciences_ , 400(1818):97–117, 1985. 

- [6] Daniel Gottesman. _Stabilizer codes and quantum error correction_ . California Institute of Technology, 1997. 

- [7] Lov K Grover. A fast quantum mechanical algorithm for database search. In _Proceedings of the twenty-eighth annual ACM symposium on Theory of computing_ , pages 212–219, 1996. 

- [8] Alberto Peruzzo, Jarrod McClean, Peter Shadbolt, Man-Hong Yung, Xiao-Qi Zhou, Peter J Love, Alán Aspuru-Guzik, and Jeremy L O’brien. A variational eigenvalue solver on a photonic quantum processor. _Nature communications_ , 5(1):4213, 2014. 

- [9] Peter W Shor. Polynomial-time algorithms for prime factorization and discrete logarithms on a quantum computer. _SIAM review_ , 41(2):303–332, 1999. 

_162_ 

_BIBLIOGRAPHY_ 

- [10] Ashley Montanaro. Quantum algorithms: an overview. _npj Quantum Information_ , 2(1):1–8, 2016. 

- [11] David P DiVincenzo. The physical implementation of quantum computation. _Fortschritte der Physik: Progress of Physics_ , 48(9-11):771–783, 2000. 

- [12] Dietrich Leibfried, Rainer Blatt, Christopher Monroe, and David Wineland. Quantum dynamics of single trapped ions. _Reviews of Modern Physics_ , 75(1):281, 2003. 

- [13] Kenneth R Brown, Jungsang Kim, and Christopher Monroe. Co-designing a scalable quantum computer with trapped atomic ions. _npj Quantum Information_ , 2(1):1–10, 2016. 

- [14] Christopher Monroe and Jungsang Kim. Scaling the ion trap quantum processor. _Science_ , 339(6124):1164–1169, 2013. 

- [15] Rainer Blatt and David Wineland. Entangled states of trapped atomic ions. _Nature_ , 453(7198):1008–1015, 2008. 

- [16] Rainer Blatt and Christian F Roos. Quantum simulations with trapped ions. _Nature Physics_ , 8(4):277–284, 2012. 

- [17] Christoph Adami and Nicolas J Cerf. Quantum computation with linear optics. In _Quantum Computing and Quantum Communications: First NASA International Conference, QCQC’98 Palm Springs, California, USA February 17–20, 1998 Selected Papers_ , pages 391–401. Springer, 1999. 

- [18] Pieter Kok, William J Munro, Kae Nemoto, Timothy C Ralph, Jonathan P Dowling, and Gerard J Milburn. Linear optical quantum computing with photonic qubits. _Reviews of modern physics_ , 79(1):135, 2007. 

- [19] Jeremy L O’brien. Optical quantum computing. _Science_ , 318(5856):1567– 1570, 2007. 

- [20] Xi-Lin Wang, Yi-Han Luo, He-Liang Huang, Ming-Cheng Chen, Zu-En Su, Chang Liu, Chao Chen, Wei Li, Yu-Qiang Fang, Xiao Jiang, et al. 18-qubit entanglement with six photons’ three degrees of freedom. _Physical Review Letters_ , 120(26):260502, 2018. 

- [21] Daniel Loss and David P DiVincenzo. Quantum computation with quantum dots. _Physical Review A_ , 57(1):120, 1998. 

_163_ 

_BIBLIOGRAPHY_ 

- [22] A Imamog, David D Awschalom, Guido Burkard, David P DiVincenzo, Daniel Loss, M Sherwin, A Small, et al. Quantum information processing using quantum dot spins and cavity qed. _Physical Review Letters_ , 83(20):4204, 1999. 

- [23] Hannes Bernien, Sylvain Schwartz, Alexander Keesling, Harry Levine, Ahmed Omran, Hannes Pichler, Soonwon Choi, Alexander S Zibrov, Manuel Endres, Markus Greiner, et al. Probing many-body dynamics on a 51-atom quantum simulator. _Nature_ , 551(7682):579–584, 2017. 

- [24] T Xia, M Lichtman, K Maller, AW Carr, MJ Piotrowicz, L Isenhower, and M Saffman. Randomized benchmarking of single-qubit gates in a 2d array of neutral-atom qubits. _Physical Review Letters_ , 114(10):100503, 2015. 

- [25] Mark Saffman. Quantum computing with neutral atoms. _National Science Review_ , 6(1):24–25, 2019. 

- [26] Ivan Oliveira, Roberto Sarthour Jr, Tito Bonagamba, Eduardo Azevedo, and Jair CC Freitas. _NMR quantum information processing_ . Elsevier, 2011. 

- [27] Henry O Everitt. _Experimental aspects of quantum computing_ . Springer, 2005. 

- [28] Rami Barends, Julian Kelly, Anthony Megrant, Andrzej Veitia, Daniel Sank, Evan Jeffrey, Ted C White, Josh Mutus, Austin G Fowler, Brooks Campbell, et al. Superconducting quantum circuits at the surface code threshold for fault tolerance. _Nature_ , 508(7497):500–503, 2014. 

- [29] Jens Koch, M Yu Terri, Jay Gambetta, Andrew A Houck, David I Schuster, Johannes Majer, Alexandre Blais, Michel H Devoret, Steven M Girvin, and Robert J Schoelkopf. Charge-insensitive qubit design derived from the cooper pair box. _Physical Review A_ , 76(4):042319, 2007. 

- [30] Morten Kjaergaard, Mollie E Schwartz, Jochen Braumüller, Philip Krantz, Joel I-J Wang, Simon Gustavsson, and William D Oliver. Superconducting qubits: Current state of play. _Annual Review of Condensed Matter Physics_ , 11:369–395, 2020. 

- [31] He-Liang Huang, Dachao Wu, Daojin Fan, and Xiaobo Zhu. Superconducting quantum computing: a review. _Science China Information Sciences_ , 63:1–32, 2020. 

_164_ 

_BIBLIOGRAPHY_ 

- [32] Alexandre Blais, Arne L Grimsmo, Steven M Girvin, and Andreas Wallraff. Circuit quantum electrodynamics. _Reviews of Modern Physics_ , 93(2):025005, 2021. 

- [33] BRIAN D Josephson. The discovery of tunnelling supercurrents. _Reviews of Modern Physics_ , 46(2):251, 1974. 

- [34] John M Martinis, Michel H Devoret, and John Clarke. Quantum josephson junction circuits and the dawn of artificial atoms. _Nature Physics_ , 16(3):234– 237, 2020. 

- [35] Joseph A Schreier, Andrew A Houck, Jens Koch, David I Schuster, Bradley R Johnson, Jerry M Chow, Jay M Gambetta, J Majer, Luigi Frunzio, Michel H Devoret, et al. Suppressing charge noise decoherence in superconducting charge qubits. _Physical Review B_ , 77(18):180502, 2008. 

- [36] Chad Rigetti, Jay M Gambetta, Stefano Poletto, Britton LT Plourde, Jerry M Chow, Antonio D Córcoles, John A Smolin, Seth T Merkel, Jim R Rozen, George A Keefe, et al. Superconducting qubit in a waveguide cavity with a coherence time approaching 0.1 ms. _Physical Review B_ , 86(10):100506, 2012. 

- [37] Josephine B Chang, Michael R Vissers, Antonio D Córcoles, Martin Sandberg, Jiansong Gao, David W Abraham, Jerry M Chow, Jay M Gambetta, Mary Beth Rothwell, George A Keefe, et al. Improved superconducting qubit coherence using titanium nitride. _Applied Physics Letters_ , 103(1):012602, 2013. 

- [38] Jonas Bylander, Simon Gustavsson, Fei Yan, Fumiki Yoshihara, Khalil Harrabi, George Fitch, David G Cory, Yasunobu Nakamura, Jaw-Shen Tsai, and William D Oliver. Noise spectroscopy through dynamical decoupling with a superconducting flux qubit. _Nature Physics_ , 7(7):565–570, 2011. 

- [39] Denis Vion, A Aassime, Audrey Cottet, Pl Joyez, H Pothier, C Urbina, Daniel Esteve, and Michel H Devoret. Manipulating the quantum state of an electrical circuit. _Science_ , 296(5569):886–889, 2002. 

- [40] Thorvald Wadum Larsen, Karl David Petersson, Ferdinand Kuemmeth, Thomas Sand Jespersen, Peter Krogstrup, Jesper Nygård, and Charles M Marcus. Semiconductor-nanowire-based superconducting qubit. _Physical Review Letters_ , 115(12):127001, 2015. 

_165_ 

_BIBLIOGRAPHY_ 

- [41] Morten Kjaergaard, Mollie E Schwartz, Ami Greene, Gabriel O Samach, Andreas Bengtsson, Michael O’Keeffe, Christopher M McNally, Jochen Braumüller, David K Kim, Philip Krantz, et al. Programming a quantum computer with quantum instructions. _arXiv preprint arXiv:2001.08838_ , 2020. 

- [42] Andreas Dewes, Florian R Ong, Vivien Schmitt, R Lauro, N Boulant, P Bertet, D Vion, and D Esteve. Characterization of a two-transmon processor with individual single-shot qubit readout. _Physical Review Letters_ , 108(5):057002, 2012. 

- [43] Andrew J Kerman and William D Oliver. High-fidelity quantum operations on superconducting qubits in the presence of noise. _Physical Review Letters_ , 101(7):070501, 2008. 

- [44] Yu Chen, C Neill, Pedram Roushan, Nelson Leung, Michael Fang, Rami Barends, Julian Kelly, Brooks Campbell, Z Chen, Benjamin Chiaro, et al. Qubit architecture with high coherence and fast tunable coupling. _Physical Review Letters_ , 113(22):220502, 2014. 

- [45] Frank Arute, Kunal Arya, Ryan Babbush, Dave Bacon, Joseph C Bardin, Rami Barends, Rupak Biswas, Sergio Boixo, Fernando GSL Brandao, David A Buell, et al. Quantum supremacy using a programmable superconducting processor. _Nature_ , 574(7779):505–510, 2019. 

- [46] IBM Newsroom. Ibm unveils 400 qubit-plus quantum processor and nextgeneration ibm quantum system two. https://newsroom.ibm.com/ 2022. 

- [47] Rigetti C. The rigetti 128-qubit chip and what it means for quantum. https://www.rigetti.com/news/ the-rigetti-128-qubit-chip-and-what-it-means-for-quantum, 2018. 

- [48] John Preskill. Quantum computing in the nisq era and beyond. _Quantum_ , 2:79, 2018. 

- [49] Han-Sen Zhong, Hui Wang, Yu-Hao Deng, Ming-Cheng Chen, Li-Chao Peng, Yi-Han Luo, Jian Qin, Dian Wu, Xing Ding, Yi Hu, et al. Quantum 

_166_ 

_BIBLIOGRAPHY_ 

computational advantage using photons. _Science_ , 370(6523):1460–1463, 2020. 

- [50] Suppressing quantum errors by scaling a surface code logical qubit. _Nature_ , 614(7949):676–681, 2023. 

- [51] Mark Webber, Vincent Elfving, Sebastian Weidt, and Winfried K Hensinger. The impact of hardware specifications on reaching quantum advantage in the fault tolerant regime. _AVS Quantum Science_ , 4(1):013801, 2022. 

- [52] AA Clerk, KW Lehnert, P Bertet, JR Petta, and Y Nakamura. Hybrid quantum systems with circuit quantum electrodynamics. _Nature Physics_ , 16(3):257–267, 2020. 

- [53] Alexei M Tyryshkin, Shinichi Tojo, John JL Morton, Helge Riemann, Nikolai V Abrosimov, Peter Becker, Hans-Joachim Pohl, Thomas Schenkel, Michael LW Thewalt, Kohei M Itoh, et al. Electron spin coherence exceeding seconds in high-purity silicon. _Nature materials_ , 11(2):143–147, 2012. 

- [54] Gary Wolfowicz, Alexei M Tyryshkin, Richard E George, Helge Riemann, Nikolai V Abrosimov, Peter Becker, Hans-Joachim Pohl, Mike LW Thewalt, Stephen A Lyon, and John JL Morton. Atomic clock transitions in siliconbased spin qubits. _Nature nanotechnology_ , 8(8):561–564, 2013. 

- [55] Cécile Grèzes, Yuimaru Kubo, Brian Julsgaard, Takahide Umeda, Junichi Isoya, Hitoshi Sumiya, Hiroshi Abe, Shinobu Onoda, Takeshi Ohshima, Kazuo Nakamura, et al. Towards a spin-ensemble quantum memory for superconducting qubits. _Comptes Rendus Physique_ , 17(7):693–704, 2016. 

- [56] Élie Gouzien and Nicolas Sangouard. Factoring 2048-bit rsa integers in 177 days with 13 436 qubits and a multimode memory. _Physical Review Letters_ , 127(14):140503, 2021. 

- [57] H Jeff Kimble. The quantum internet. _Nature_ , 453(7198):1023–1030, 2008. 

- [58] Lewis A Williamson, Yu-Hui Chen, and Jevon J Longdell. Magnetooptic modulator with unit quantum efficiency. _Physical Review Letters_ , 113(20):203601, 2014. 

- [59] Susanne Blum, Christopher O’Brien, Nikolai Lauk, Pavel Bushev, Michael Fleischhauer, and Giovanna Morigi. Interfacing microwave qubits and optical photons via spin ensembles. _Physical Review A_ , 91(3):033834, 2015. 

_167_ 

_BIBLIOGRAPHY_ 

- [60] Xavier Fernandez-Gonzalvo, Yu-Hui Chen, Chunming Yin, Sven Rogge, and Jevon J Longdell. Coherent frequency up-conversion of microwaves to the optical telecommunications band in an er: Yso crystal. _Physical Review A_ , 92(6):062313, 2015. 

- [61] Sebastian Probst. _Hybrid quantum system based on rare earth doped crystals_ , volume 16. KIT Scientific Publishing, 2016. 

- [62] Ilana Wisby. _Hybrid rare-earth ion superconductor systems for quantum information processing_ . PhD thesis, Royal Holloway, University of London, 2017. 

- [63] Gavin Patrick Dold. _milliKelvin ESR of rare-earth doped crystals using superconducting resonators_ . PhD thesis, UCL (University College London), 2020. 

- [64] Marianne Le Dantec, Miloš Ranˇci´c, Sen Lin, Eric Billaud, Vishal Ranjan, Daniel Flanigan, Sylvain Bertaina, Thierry Chanelière, Philippe Goldner, Andreas Erb, et al. Twenty-three–millisecond electron spin coherence of erbium ions in a natural-abundance crystal. _Science advances_ , 7(51):eabj9786, 2021. 

- [65] Joseph Alexander, Gavin Dold, Oscar W. Kennedy, Mantas Šim˙enas, James O’Sullivan, Christoph W. Zollitsch, Sacha Welinski, Alban Ferrier, Eloïse Lafitte-Houssat, Tobias Lindström, Philippe Goldner, and John J. L. Morton. Coherent spin dynamics of rare-earth doped crystals in the high-cooperativity regime. _Phys. Rev. B_ , 106:245416, Dec 2022. 

- [66] Dong-Sheng Ding, Zhi-Yuan Zhou, Bao-Sen Shi, and Guang-Can Guo. Single-photon-level quantum image memory based on cold atomic ensembles. _Nature communications_ , 4(1):2527, 2013. 

- [67] Dong-Sheng Ding, Wei Zhang, Zhi-Yuan Zhou, Shuai Shi, Guo-Yong Xiang, Xi-Shi Wang, Yun-Kun Jiang, Bao-Sen Shi, and Guang-Can Guo. Quantum storage of orbital angular momentum entanglement in an atomic ensemble. _Physical Review Letters_ , 114(5):050502, 2015. 

- [68] Dong-Sheng Ding and Dong-Sheng Ding. Raman quantum memory of photonic polarized entanglement. _Broad Bandwidth and High Dimensional Quantum Memory Based on Atomic Ensembles_ , pages 91–107, 2018. 

_168_ 

_BIBLIOGRAPHY_ 

- [69] KF Reim, J Nunn, VO Lorenz, BJ Sussman, KC Lee, NK Langford, D Jaksch, and IA Walmsley. Towards high-speed optical quantum memories. _Nature Photonics_ , 4(4):218–221, 2010. 

- [70] Jinxian Guo, Xiaotian Feng, Peiyu Yang, Zhifei Yu, LQ Chen, Chun-Hua Yuan, and Weiping Zhang. High-performance raman quantum memory with optimal control in room temperature atoms. _Nature communications_ , 10(1):148, 2019. 

- [71] Stephen D Hogan, Josef A Agner, Frédéric Merkt, Tobias Thiele, Stefan Filipp, and Andreas Wallraff. Driving rydberg-rydberg transitions from a coplanar microwave waveguide. _Physical Review Letters_ , 108(6):063004, 2012. 

- [72] Lin Li and A Kuzmich. Quantum memory with strong and controllable rydberg-level interactions. _Nature Communications_ , 7(1):13618, 2016. 

- [73] AA Morgan and SD Hogan. Coupling rydberg atoms to microwave fields in a superconducting coplanar waveguide resonator. _Physical Review Letters_ , 124(19):193604, 2020. 

- [74] Christoph Simon, Mikael Afzelius, Jürgen Appel, A Boyer de La Giroday, SJ Dewhurst, Nicolas Gisin, CY Hu, F Jelezko, Stefan Kröll, JH Müller, et al. Quantum memories: a review based on the european integrated project “qubit applications (qap)”. _The European Physical Journal D_ , 58:1–22, 2010. 

- [75] Khabat Heshami, Duncan G England, Peter C Humphreys, Philip J Bustard, Victor M Acosta, Joshua Nunn, and Benjamin J Sussman. Quantum memories: emerging applications and recent advances. _Journal of modern optics_ , 63(20):2005–2028, 2016. 

- [76] Alexander I Lvovsky, Barry C Sanders, and Wolfgang Tittel. Optical quantum memory. _Nature photonics_ , 3(12):706–714, 2009. 

- [77] SA Moiseev. Off-resonant raman-echo quantum memory for inhomogeneously broadened atoms in a cavity. _Physical Review A_ , 88(1):012304, 2013. 

- [78] Mikael Afzelius, Christoph Simon, Hugues De Riedmatten, and Nicolas Gisin. Multimode quantum memory based on atomic frequency combs. _Physical Review A_ , 79(5):052329, 2009. 

_169_ 

_BIBLIOGRAPHY_ 

- [79] Tian Zhong, Jonathan M Kindem, John G Bartholomew, Jake Rochman, Ioana Craiciu, Evan Miyazono, Marco Bettinelli, Enrico Cavalli, Varun Verma, Sae Woo Nam, et al. Nanophotonic rare-earth quantum memory with optically controlled retrieval. _Science_ , 357(6358):1392–1395, 2017. 

- [80] John G Bartholomew, Jake Rochman, Tian Xie, Jonathan M Kindem, Andrei Ruskuc, Ioana Craiciu, Mi Lei, and Andrei Faraon. On-chip coherent microwave-to-optical transduction mediated by ytterbium in yvo4. _Nature communications_ , 11(1):3266, 2020. 

- [81] Matteo Mariantoni, Haiyan Wang, Takashi Yamamoto, Matthew Neeley, Radoslaw C Bialczak, Yu Chen, Mike Lenander, Erik Lucero, Aaron D O’Connell, Daniel Sank, et al. Implementing the quantum von neumann architecture with superconducting circuits. _Science_ , 334(6052):61–65, 2011. 

- [82] Zenghui Bao, Zhiling Wang, Yukai Wu, Yan Li, Cheng Ma, Yipu Song, Hongyi Zhang, and Luming Duan. On-demand storage and retrieval of microwave photons using a superconducting multiresonator quantum memory. _Physical Review Letters_ , 127(1):010503, 2021. 

- [83] Andreas Wallraff, David I Schuster, Alexandre Blais, Luigi Frunzio, R-S Huang, Johannes Majer, Sameer Kumar, Steven M Girvin, and Robert J Schoelkopf. Strong coupling of a single photon to a superconducting qubit using circuit quantum electrodynamics. _Nature_ , 431(7005):162–167, 2004. 

- [84] SA Moiseev, FF Gubaidullin, RS Kirillov, RR Latypov, NS Perminov, KV Petrovnin, and ON Sherstyukov. Multiresonator quantum memory. _Physical Review A_ , 95(1):012338, 2017. 

- [85] Xiaobo Zhu, Shiro Saito, Alexander Kemp, Kosuke Kakuyanagi, Shin-ichi Karimoto, Hayato Nakano, William J Munro, Yasuhiro Tokura, Mark S Everitt, Kae Nemoto, et al. Coherent coupling of a superconducting flux qubit to an electron spin ensemble in diamond. _Nature_ , 478(7368):221–224, 2011. 

- [86] Michael Stern, Gianluigi Catelani, Yuimaru Kubo, Cecile Grezes, Audrey Bienfait, Denis Vion, Daniel Esteve, and Patrice Bertet. Flux qubits with long coherence times for hybrid quantum circuits. _Physical Review Letters_ , 113(12):123601, 2014. 

_BIBLIOGRAPHY_ 

_170_ 

- [87] Y Kubo, FR Ong, Patrice Bertet, Denis Vion, V Jacques, D Zheng, A Dréau, J-F Roch, Alexia Auffèves, Fedor Jelezko, et al. Strong coupling of a spin ensemble to a superconducting resonator. _Physical Review Letters_ , 105(14):140502, 2010. 

- [88] Yuimaru Kubo, Cecile Grezes, Andreas Dewes, T Umeda, Junichi Isoya, H Sumiya, N Morishita, H Abe, S Onoda, T Ohshima, et al. Hybrid quantum circuit with a superconducting qubit coupled to a spin ensemble. _Physical Review Letters_ , 107(22):220501, 2011. 

- [89] Y Kubo, Igor Diniz, A Dewes, V Jacques, A Dréau, J-F Roch, Alexia Auffèves, Denis Vion, Daniel Esteve, and Patrice Bertet. Storage and retrieval of a microwave field in a spin ensemble. _Physical Review A_ , 85(1):012333, 2012. 

- [90] C Grezes, Brian Julsgaard, Y Kubo, M Stern, T Umeda, J Isoya, H Sumiya, H Abe, S Onoda, T Ohshima, et al. Multimode storage and retrieval of microwave fields in a spin ensemble. _Physical Review X_ , 4(2):021049, 2014. 

- [91] C Grezes, B Julsgaard, Y Kubo, WL Ma, M Stern, A Bienfait, K Nakamura, J Isoya, S Onoda, T Ohshima, et al. Storage and retrieval of microwave fields at the single-photon level in a spin ensemble. _Physical Review A_ , 92(2):020301, 2015. 

- [92] DI Schuster, AP Sears, E Ginossar, L DiCarlo, L Frunzio, JJL Morton, H Wu, GAD Briggs, BB Buckley, DD Awschalom, et al. High-cooperativity coupling of electron-spin ensembles to superconducting cavities. _Physical Review Letters_ , 105(14):140501, 2010. 

- [93] Robert Amsüss, Ch Koller, Tobias Nöbauer, Stefan Putz, Stefan Rotter, Kathrin Sandner, Stephan Schneider, Matthias Schramböck, Georg Steinhauser, Helmut Ritsch, et al. Cavity qed with magnetically coupled collective spin states. _Physical Review Letters_ , 107(6):060502, 2011. 

- [94] S Probst, H Rotzinger, S Wünsch, P Jung, M Jerger, M Siegel, AV Ustinov, and PA Bushev. Anisotropic rare-earth spin ensemble strongly coupled to a superconducting resonator. _Physical Review Letters_ , 110(15):157001, 2013. 

- [95] Gavin Dold, Christoph W Zollitsch, James O’sullivan, Sacha Welinski, Alban Ferrier, Philippe Goldner, SE de Graaf, Tobias Lindström, and John JL 

_BIBLIOGRAPHY_ 

_171_ 

Morton. High-cooperativity coupling of a rare-earth spin ensemble to a superconducting resonator using yttrium orthosilicate as a substrate. _Physical Review Applied_ , 11(5):054082, 2019. 

- [96] V Ranjan, J O’sullivan, E Albertinale, B Albanese, T Chanelière, T Schenkel, D Vion, D Esteve, E Flurin, JJL Morton, et al. Multimode storage of quantum microwave fields in electron spins over 100 ms. _Physical Review Letters_ , 125(21):210505, 2020. 

- [97] Jérôme Ruggiero, Jean-Louis Le Gouët, Christoph Simon, and Thierry Chaneliere. Why the two-pulse photon echo is not a good quantum memory protocol. _Physical Review A_ , 79(5):053851, 2009. 

- [98] Vianney Damon, Matthieu Bonarota, Anne Louchet-Chauvet, Thierry Chaneliere, and Jean-Louis Le Gouët. Revival of silenced echo and quantum memory for light. _New Journal of Physics_ , 13(9):093031, 2011. 

- [99] Brian Julsgaard, Cécile Grezes, Patrice Bertet, and Klaus Mølmer. Quantum memory for microwave photons in an inhomogeneously broadened spin ensemble. _Physical Review Letters_ , 110(25):250503, 2013. 

- [100] Hua Wu, Richard E George, Janus H Wesenberg, Klaus Mølmer, David I Schuster, Robert J Schoelkopf, Kohei M Itoh, Arzhang Ardavan, John JL Morton, and G Andrew D Briggs. Storage of multiple coherent microwave excitations in an electron spin ensemble. _Physical Review Letters_ , 105(14):140503, 2010. 

- [101] Barbara Kraus, Wolfgang Tittel, Nicolas Gisin, Mattias Nilsson, Stefan Kröll, and J Ignacio Cirac. Quantum memory for nonstationary light fields based on controlled reversible inhomogeneous broadening. _Physical Review A_ , 73(2):020302, 2006. 

- [102] Chao Liu, Tian-Xiang Zhu, Ming-Xu Su, You-Zhi Ma, Zong-Quan Zhou, Chuan-Feng Li, and Guang-Can Guo. On-demand quantum storage of photonic qubits in an on-chip waveguide. _Physical Review Letters_ , 125(26):260504, 2020. 

- [103] Ioana Craiciu, Mi Lei, Jake Rochman, John G Bartholomew, and Andrei Faraon. Multifunctional on-chip storage at telecommunication wavelength for quantum networks. _Optica_ , 8(1):114–121, 2021. 

_BIBLIOGRAPHY_ 

_172_ 

- [104] V Ranjan, Y Wen, AKV Keyser, SE Kubatkin, AV Danilov, T Lindström, P Bertet, and SE de Graaf. Spin-echo silencing using a current-biased frequency-tunable resonator. _Physical Review Letters_ , 129(18):180504, 2022. 

- [105] Matthieu Bonarota, Julian Dajczgewand, Anne Louchet-Chauvet, Jean-Louis Le Gouët, and Thierry Chanelière. Photon echo with a few photons in twolevel atoms. _Laser Physics_ , 24(9):094003, 2014. 

- [106] James O’Sullivan, Oscar W Kennedy, Kamanasish Debnath, Joseph Alexander, Christoph W Zollitsch, Mantas Šim˙enas, Akel Hashim, Christopher N Thomas, Stafford Withington, Irfan Siddiqi, et al. Random-access quantum memory using chirped pulse phase encoding. _Physical Review X_ , 12(4):041014, 2022. 

- [107] Louis Nicolas, Moritz Businger, Théo Sanchez Meijia, Alexey Tiranov, Thierry Chanelière, Eloïse Lafitte-Houssat, Alban Ferrier, Philippe Goldner, and Mikael Afzelius. Coherent optical-microwave interface for manipulation of low-field electronic clock transitions in<sup>171</sup> Yb<sup>3+</sup> : Y 2 SiO5. _arXiv preprint arXiv:2209.04196_ , 2022. 

- [108] Antonio Ortu, Alexey Tiranov, Sacha Welinski, Florian Fröwis, Nicolas Gisin, Alban Ferrier, Philippe Goldner, and Mikael Afzelius. Simultaneous coherence enhancement of optical and microwave transitions in solid-state electronic spins. _Nature materials_ , 17(8):671–675, 2018. 

- [109] Bernard Jacquier et al. _Spectroscopic properties of rare earths in optical materials_ , volume 83. Springer Science & Business Media, 2005. 

- [110] C Li, Ch Wyon, and Richard Moncorge. Spectroscopic properties and orescence dynamics of er/sup 3+/and yb/sup 3+/in y/sub 2/sio/sub 5. _IEEE journal of quantum electronics_ , 28(4):1209–1221, 1992. 

- [111] Thomas Böttger, CW Thiel, Y Sun, and RL Cone. Optical decoherence and spectral diffusion at 1.5 _µ_ m in Er<sup>3+</sup> :Y2SiO5 versus magnetic field, temperature, and Er<sup>3+</sup> concentration. _Physical Review B_ , 73(7):075101, 2006. 

- [112] Sylvain Bertaina, Serge Gambarelli, Alexandra Tkachuk, IN Kurkin, Boris Malkin, Anatole Stepanov, and Bernard Barbara. Rare-earth solid-state qubits. _Nature nanotechnology_ , 2(1):39–42, 2007. 

_BIBLIOGRAPHY_ 

_173_ 

- [113] Charles W Thiel, Thomas Böttger, and RL Cone. Rare-earth-doped materials for applications in quantum information storage and signal processing. _Journal of luminescence_ , 131(3):353–361, 2011. 

- [114] Jonathan M Kindem, Andrei Ruskuc, John G Bartholomew, Jake Rochman, Yan Qi Huan, and Andrei Faraon. Control and single-shot readout of an ion embedded in a nanophotonic cavity. _Nature_ , 580(7802):201–204, 2020. 

- [115] Tobias Utikal, Emanuel Eichhammer, Lutz Petersen, Alois Renn, Stephan Götzinger, and Vahid Sandoghdar. Spectroscopic detection and state preparation of a single praseodymium ion in a crystal. _Nature communications_ , 5(1):3627, 2014. 

- [116] P Siyushev, K Xia, R Reuter, M Jamali, N Zhao, N Yang, C Duan, N Kukharchyk, AD Wieck, R Kolesov, et al. Coherent properties of single rare-earth spin qubits. _Nature communications_ , 5(1):3895, 2014. 

- [117] Tian Zhong, Jonathan M Kindem, John G Bartholomew, Jake Rochman, Ioana Craiciu, Varun Verma, Sae Woo Nam, Francesco Marsili, Matthew D Shaw, Andrew D Beyer, et al. Optically addressing single rare-earth ions in a nanophotonic cavity. _Physical Review Letters_ , 121(18):183603, 2018. 

- [118] Hugues De Riedmatten, Mikael Afzelius, Matthias U Staudt, Christoph Simon, and Nicolas Gisin. A solid-state light–matter interface at the singlephoton level. _Nature_ , 456(7223):773–777, 2008. 

- [119] Mikael Afzelius, Imam Usmani, Atia Amari, Björn Lauritzen, Andreas Walther, Christoph Simon, Nicolas Sangouard, Jiˇrí Mináˇr, Hugues De Riedmatten, Nicolas Gisin, et al. Demonstration of atomic frequency comb memory for light with spin-wave storage. _Physical Review Letters_ , 104(4):040503, 2010. 

- [120] Mikael Afzelius, N Sangouard, Göran Johansson, MU Staudt, and CM Wilson. Proposal for a coherent quantum memory for propagating microwave photons. _New Journal of Physics_ , 15(6):065008, 2013. 

- [121] Cyril Laplane, Pierre Jobez, Jean Etesse, Nicolas Gisin, and Mikael Afzelius. Multimode and long-lived quantum correlations between photons and spins in a crystal. _Physical Review Letters_ , 118(21):210501, 2017. 

_BIBLIOGRAPHY_ 

_174_ 

- [122] Andrei Ruskuc, Chun-Ju Wu, Jake Rochman, Joonhee Choi, and Andrei Faraon. Nuclear spin-wave quantum register for a solid-state qubit. _Nature_ , 602(7897):408–413, 2022. 

- [123] Morgan P Hedges, Jevon J Longdell, Yongmin Li, and Matthew J Sellars. Efficient quantum memory for light. _Nature_ , 465(7301):1052–1056, 2010. 

- [124] Manjin Zhong, Morgan P Hedges, Rose L Ahlefeldt, John G Bartholomew, Sarah E Beavan, Sven M Wittig, Jevon J Longdell, and Matthew J Sellars. Optically addressable nuclear spins in a solid with a six-hour coherence time. _Nature_ , 517(7533):177–180, 2015. 

- [125] E Zavoisky. Spin-magnetic resonance in paramagnetics. _J Phys USSR_ , 9:211–245, 1945. 

- [126] Brebis Bleaney. Paramagnetic resonance spectra of five chromic sulphate alums at low temperatures. _Proceedings of the Royal Society of London. Series A. Mathematical and Physical Sciences_ , 204(1077):203–216, 1950. 

- [127] Walther Gerlach and Otto Stern. Der experimentelle nachweis der richtungsquantelung im magnetfeld. _Zeitschrift für Physik_ , 9(1):349–352, 1922. 

- [128] David Hanneke, S Fogwell, and G Gabrielse. New measurement of the electron magnetic moment and the fine structure constant. _Physical Review Letters_ , 100(12):120801, 2008. 

- [129] Erwin L Hahn. Spin echoes. _Physical review_ , 80(4):580, 1950. 

- [130] Anatole Abragam and Brebis Bleaney. _Electron paramagnetic resonance of transition ions_ . Oxford University Press, 2012. 

- [131] G. H. Larson and C. D. Jeffries. Spin-Lattice Relaxation in Some RareEarth Salts. I. Temperature Dependence. _Physical Review_ , 141(1):461–478, January 1966. 

- [132] E Zambrini Cruzeiro, Alexey Tiranov, Imam Usmani, Cyril Laplane, Jonathan Lavoie, Alban Ferrier, Philippe Goldner, Nicolas Gisin, and Mikael Afzelius. Spectral hole lifetimes and spin population relaxation dynamics in neodymium-doped yttrium orthosilicate. _Physical Review B_ , 95(20):205119, 2017. 

_175_ 

_BIBLIOGRAPHY_ 

- [133] IN Kurkin and KP Chernov. Epr and spin-lattice relaxation of rare-earth activated centres in y2sio5 single crystals. _Physica B+ C_ , 101(2):233–238, 1980. 

- [134] Hee-Jin Lim, Sacha Welinski, Alban Ferrier, Philippe Goldner, and JJL Morton. Coherent spin dynamics of ytterbium ions in yttrium orthosilicate. _Physical Review B_ , 97(6):064409, 2018. 

- [135] KM Salikhov, S-A_ Dzuba, and ANDA M Raitsimring. The theory of electron spin-echo signal decay resulting from dipole-dipole interactions between paramagnetic centers in solids. _Journal of Magnetic Resonance (1969)_ , 42(2):255–276, 1981. 

- [136] Arthur Schweiger and Gunnar Jeschke. _Principles of pulse electron paramagnetic resonance_ . Oxford University Press on Demand, 2001. 

- [137] Herman Y Carr and Edward M Purcell. Effects of diffusion on free precession in nuclear magnetic resonance experiments. _Physical review_ , 94(3):630, 1954. 

- [138] Saul Meiboom and David Gill. Modified spin-echo method for measuring nuclear relaxation times. _Review of scientific instruments_ , 29(8):688–691, 1958. 

- [139] F Mentink-Vigier, Alberto Collauto, Akiva Feintuch, Ilia Kaminker, V Tarle, and Daniella Goldfarb. Increasing sensitivity of pulse epr experiments using echo train detection schemes. _Journal of Magnetic Resonance_ , 236:117–125, 2013. 

- [140] James Campbell O’Sullivan. _Coupling superconducting resonators to bismuth donor spins in silicon for quantum memory applications_ . PhD thesis, UCL (University College London), 2020. 

- [141] Michael Garwood and Lance DelaBarre. The return of the frequency sweep: designing adiabatic pulses for contemporary nmr. _Journal of magnetic resonance_ , 153(2):155–177, 2001. 

- [142] Eriks<sup>¯</sup> Kupce and Ray Freeman. Optimized adiabatic pulses for wideband spin inversion. _Journal of Magnetic Resonance, Series A_ , 118(2):299–303, 1996. 

_176_ 

_BIBLIOGRAPHY_ 

- [143] Michael Garwood and Yong Ke. Symmetric pulses to induce arbitrary flip angles with compensation for rf inhomogeneity and resonance offsets. _Journal of Magnetic Resonance (1969)_ , 94(3):511–525, 1991. 

- [144] María Florencia Pascual-Winter, Robert-Christopher Tongning, Thierry Chanelière, and JL Le Gouët. Securing coherence rephasing with a pair of adiabatic rapid passages. _New Journal of Physics_ , 15(5):055024, 2013. 

- [145] Julián Dajczgewand, Jean-Louis Le Gouët, Anne Louchet-Chauvet, and Thierry Chanelière. Large efficiency at telecom wavelength for optical quantum memories. _Optics letters_ , 39(9):2711–2714, 2014. 

- [146] Thierry Chanelière, Gabriel Hétet, and Nicolas Sangouard. Quantum optical memory protocols in atomic ensembles. In _Advances In Atomic, Molecular, and Optical Physics_ , volume 67, pages 77–150. Elsevier, 2018. 

- [147] KI Gerasimov, MM Minnegaliev, SA Moiseev, RV Urmancheev, T Chanelière, and A Louchet-Chauvet. Quantum memory in an orthogonal geometry of silenced echo retrieval. _Optics and Spectroscopy_ , 123:211–216, 2017. 

- [148] II Rabi. On the process of space quantization. _Physical Review_ , 49(4):324, 1936. 

- [149] D. Braak. Integrability of the rabi model. _Phys. Rev. Lett._ , 107:100401, Aug 2011. 

- [150] Edward Mills Purcell. Proceedings of the american physical society, b10. spontaneous emission probabilities at radio frequencies. _Phys. Rev_ , 69:674, 1946. 

- [151] Audrey Bienfait, JJ Pla, Yuimaru Kubo, Xin Zhou, Michael Stern, CC Lo, CD Weis, Thomas Schenkel, Denis Vion, Daniel Esteve, et al. Controlling spin relaxation with a cavity. _Nature_ , 531(7592):74–77, 2016. 

- [152] Juris Meija, Tyler B. Coplen, Michael Berglund, Willi A. Brand, Paul De Bièvre, Manfred Gröning, Norman E. Holden, Johanna Irrgeher, Robert D. Loss, Thomas Walczyk, and Thomas Prohaska. Isotopic compositions of the elements 2013 (iupac technical report). _Pure and Applied Chemistry_ , 88(3):293–306, 2016. 

_BIBLIOGRAPHY_ 

_177_ 

- [153] Maier-Flaig H. _Electron and nuclear spin properties of 145Neodymium doped Y2SiO5_ . PhD thesis, Karlsrhue Institute of Technology, 2013. 

- [154] Alexey Tiranov, Antonio Ortu, Sacha Welinski, Alban Ferrier, Philippe Goldner, Nicolas Gisin, and Mikael Afzelius. Spectroscopic study of hyperfine properties in<sup>171</sup> Yb<sup>3+</sup> :Y2SiO5. _Physical Review B_ , 98(19):195110, 2018. 

- [155] Sacha Welinski, Alban Ferrier, Mikael Afzelius, and Philippe Goldner. Highresolution optical spectroscopy and magnetic properties of Yb<sup>3+</sup> in Y2SiO5. _Physical Review B_ , 94(15):155116, 2016. 

- [156] Stefan Stoll and Arthur Schweiger. Easyspin, a comprehensive software package for spectral simulation and analysis in epr. _Journal of magnetic resonance_ , 178(1):42–55, 2006. 

- [157] Jay M Gambetta, Jerry M Chow, and Matthias Steffen. Building logical qubits in a superconducting quantum computing system. _npj quantum information_ , 3(1):1–7, 2017. 

- [158] Julian Kelly, Rami Barends, Austin G Fowler, Anthony Megrant, Evan Jeffrey, Theodore C White, Daniel Sank, Josh Y Mutus, Brooks Campbell, Yu Chen, et al. State preservation by repetitive error detection in a superconducting quantum circuit. _Nature_ , 519(7541):66–69, 2015. 

- [159] Peter K Day, Henry G LeDuc, Benjamin A Mazin, Anastasios Vayonakis, and Jonas Zmuidzinas. A broadband superconducting detector suitable for use in large arrays. _Nature_ , 425(6960):817–821, 2003. 

- [160] RJ Schoelkopf, SH Moseley, CM Stahle, P Wahlgren, and P Delsing. A concept for a submillimeter-wave single-photon counter. _IEEE transactions on applied superconductivity_ , 9(2):2935–2939, 1999. 

- [161] K Segall, KW Lehnert, TR Stevenson, RJ Schoelkopf, P Wahlgren, A Aassime, and P Delsing. A high-performance cryogenic amplifier based on a radio-frequency single electron transistor. _Applied physics letters_ , 81(25):4859–4861, 2002. 

- [162] Erik A Tholén, Adem Ergül, Evelyn M Doherty, Frank M Weber, Fabien Grégis, and David B Haviland. Nonlinearities and parametric amplification in superconducting coplanar waveguide resonators. _Applied physics letters_ , 90(25):253509, 2007. 

_BIBLIOGRAPHY_ 

_178_ 

- [163] MA Castellanos-Beltran, KD Irwin, GC Hilton, LR Vale, and KW Lehnert. Amplification and squeezing of quantum noise with a tunable josephson 

- metamaterial. _Nature Physics_ , 4(12):929–931, 2008. 

- [164] Daniel J Parker, Mykhailo Savytskyi, Wyatt Vine, Arne Laucht, Timothy Duty, Andrea Morello, Arne L Grimsmo, and Jarryd J Pla. Degenerate parametric amplification via three-wave mixing using kinetic inductance. _Physical Review Applied_ , 17(3):034064, 2022. 

- [165] Emanuele Albertinale, Léo Balembois, Eric Billaud, Vishal Ranjan, Daniel Flanigan, Thomas Schenkel, Daniel Estève, Denis Vion, Patrice Bertet, and Emmanuel Flurin. Detecting spins by their fluorescence with a microwave photon counter. _Nature_ , 600(7889):434–438, 2021. 

- [166] V Ranjan, G De Lange, R Schutjens, T Debelhoir, JP Groen, D Szombati, DJ Thoen, TM Klapwijk, Ronald Hanson, and L DiCarlo. Probing dynamics of an electron-spin ensemble via a superconducting resonator. _Physical Review Letters_ , 110(6):067004, 2013. 

- [167] Ze-Liang Xiang, Sahel Ashhab, JQ You, and Franco Nori. Hybrid quantum circuits: Superconducting circuits interacting with other quantum systems. _Reviews of Modern Physics_ , 85(2):623, 2013. 

- [168] A Bienfait, JJ Pla, Y Kubo, M Stern, X Zhou, CC Lo, CD Weis, T Schenkel, MLW Thewalt, D Vion, et al. Reaching the quantum limit of sensitivity in electron spin resonance. _Nature nanotechnology_ , 11(3):253–257, 2016. 

- [169] Heike KAMERLINGH ONNES. The superconductivity of mercury. _Comm. Phys. Lab. Univ. Leiden_ , 122:122–124, 1911. 

- [170] John Bardeen, Leon N Cooper, and John Robert Schrieffer. Theory of superconductivity. _Physical review_ , 108(5):1175, 1957. 

- [171] Heinz London. Production of heat in supraconductors by alternating currents. _Nature_ , 133(3361):497–498, 1934. 

- [172] Neil W Ashcroft and N David Mermin. _Solid state physics_ . Cengage Learning, 2022. 

- [173] Daniel C Mattis and John Bardeen. Theory of the anomalous skin effect in normal and superconducting metals. _Physical Review_ , 111(2):412, 1958. 

_BIBLIOGRAPHY_ 

_179_ 

- [174] Vladimir E Manucharyan, Jens Koch, Leonid I Glazman, and Michel H Devoret. Fluxonium: Single cooper-pair circuit free of charge offsets. _Science_ , 326(5949):113–116, 2009. 

- [175] C Eichler, AJ Sigillito, Stephen A Lyon, and Jason R Petta. Electron spin resonance at the level of 104 spins using low impedance superconducting resonators. _Physical Review Letters_ , 118(3):037701, 2017. 

- [176] Vishal Ranjan, Sebastian Probst, Bartolo Albanese, Thomas Schenkel, Denis Vion, Daniel Esteve, JJL Morton, and Patrice Bertet. Electron spin resonance spectroscopy with femtoliter detection volume. _Applied Physics Letters_ , 116(18):184002, 2020. 

- [177] Mingrui Xu, Xu Han, Wei Fu, Chang-Ling Zou, and Hong X Tang. Frequency-tunable high-q superconducting resonators via wireless control of nonlinear kinetic inductance. _Applied Physics Letters_ , 114(19):192601, 2019. 

- [178] Christoph W Zollitsch, James O’Sullivan, Oscar Kennedy, Gavin Dold, and John JL Morton. Tuning high-q superconducting resonators by magnetic field reorientation. _AIP Advances_ , 9(12):125225, 2019. 

- [179] Michael R Vissers, Robert P Erickson, H-S Ku, Leila Vale, Xian Wu, GC Hilton, and David P Pappas. Low-noise kinetic inductance traveling-wave amplifier using three-wave mixing. _Applied physics letters_ , 108(1):012601, 2016. 

- [180] Michael Tinkham. _Introduction to superconductivity_ . Courier Corporation, 2004. 

- [181] Jonas Zmuidzinas. Superconducting microresonators: Physics and applications. _Annu. Rev. Condens. Matter Phys._ , 3(1):169–214, 2012. 

- [182] Byeong Ho Eom, Peter K Day, Henry G LeDuc, and Jonas Zmuidzinas. A wideband, low-noise superconducting amplifier with high dynamic range. _Nature Physics_ , 8(8):623–627, 2012. 

- [183] Michael R Vissers, Johannes Hubmayr, Martin Sandberg, Saptarshi Chaudhuri, Clint Bockstiegel, and Jiansong Gao. Frequency-tunable superconducting resonators via nonlinear kinetic inductance. _Applied Physics Letters_ , 107(6):062601, 2015. 

_BIBLIOGRAPHY_ 

_180_ 

- [184] Tae-Yeoul Yun and Kai Chang. One-dimensional photonic bandgap resonators and varactor tuned resonators. In _1999 IEEE MTT-S International Microwave Symposium Digest (Cat. No. 99CH36282)_ , volume 4, pages 1629–1632. IEEE, 1999. 

- [185] Jonathan Burnett, Lara Faoro, I Wisby, VL Gurtovoi, AV Chernykh, GM Mikhailov, VA Tulin, R Shaikhaidarov, V Antonov, PJ Meeson, et al. Evidence for interacting two-level systems from the 1/f noise of a superconducting resonator. _Nature communications_ , 5(1):4119, 2014. 

- [186] Sebastian Probst, Vishal Ranjan, Quentin Ansel, Reinier Heeres, Bartolo Albanese, Emanuele Albertinale, Denis Vion, Daniel Esteve, Steffen J Glaser, Dominique Sugny, et al. Shaped pulses for transient compensation in quantum-limited electron spin resonance spectroscopy. _Journal of Magnetic Resonance_ , 303:42–47, 2019. 

- [187] David M Pozar. _Microwave engineering_ . John wiley & sons, 2011. 

- [188] Frederick Emmons Terman. _Radio engineers’ handbook_ . 1943. 

- [189] Theodore Van Duzer and Charles William Turner. Principles of superconductive devices and circuits. 1981. 

- [190] Andreas Bärnthaler, Stefan Rotter, Florian Libisch, Joachim Burgdörfer, Stefan Gehler, Ulrich Kuhl, and Hans-Jürgen Stöckmann. Probing decoherence through fano resonances. _Physical Review Letters_ , 105(5):056801, 2010. 

- [191] _Physical Review_ , 124(6):1866, 1961. 

- [192] David S Betts and David Sheridan Betts. _An introduction to millikelvin technology_ . Number 1. Cambridge University Press, 1989. 

- [193] BlueFors LD Dilution Refrigerator System. https://bluefors.com/ products/ld-dilution-refrigerator/. Accessed: 2023-01-26. 

- [194] Rogerio de Sousa and S Das Sarma. Theory of nuclear-induced spectral diffusion: Spin decoherence of phosphorus donors in si and gaas quantum dots. _Physical Review B_ , 68(11):115322, 2003. 

_BIBLIOGRAPHY_ 

_181_ 

- [195] Wen-Long Ma, Gary Wolfowicz, Shu-Shen Li, John JL Morton, and RenBao Liu. Classical nature of nuclear spin noise near clock transitions of bi donors in silicon. _Physical Review B_ , 92(16):161403, 2015. 

- [196] WM Witzel and S Das Sarma. Quantum theory for electron spin decoherence induced by nuclear spin dynamics in semiconductor quantum computer architectures: Spectral diffusion of localized electron spins in the nuclear solid-state environment. _Physical Review B_ , 74(3):035322, 2006. 

- [197] Ph Tamarat, T Gaebel, JR Rabeau, M Khan, AD Greentree, H Wilson, LCL Hollenberg, S Prawer, P Hemmer, F Jelezko, et al. Stark shift control of single optical centers in diamond. _Physical Review Letters_ , 97(8):083002, 2006. 

- [198] Kai-Mei C Fu, Charles Santori, Paul E Barclay, Lachlan J Rogers, Neil B Manson, and Raymond G Beausoleil. Observation of the dynamic jahn-teller effect in the excited states of nitrogen-vacancy centers in diamond. _Physical Review Letters_ , 103(25):256404, 2009. 

- [199] Milos Ranˇci´c, Marianne Le Dantec, Sen Lin, Sylvain Bertaina, Thierry Chanelière, Diana Serrano, Philippe Goldner, Ren Bao Liu, Emmanuel Flurin, Daniel Estève, et al. Electron-spin spectral diffusion in an erbium doped crystal at millikelvin temperatures. _arXiv preprint arXiv:2203.15012_ , 2022. 

- [200] Hideo Sato, Velavan Kathirvelu, Gaëlle Spagnol, Suchada Rajca, Andrzej Rajca, Sandra S Eaton, and Gareth R Eaton. Impact of electron- electron spin interaction on electron spin relaxation of nitroxide diradicals and tetraradical in glassy solvents between 10 and 300 K. _The Journal of Physical Chemistry B_ , 112(10):2818–2828, 2008. 

- [201] Hideo Sato, Benjamen A Filas, Sandra S Eaton, Gareth R Eaton, Alex A Romanyukha, Robert Hayes, and Alexandre M Rossi. Electron spin relaxation of radicals in irradiated tooth enamel and synthetic hydroxyapatite. _Radiation measurements_ , 42(6-7):997–1004, 2007. 

- [202] Rami Barends, Julian Kelly, Anthony Megrant, Daniel Sank, Evan Jeffrey, Yu Chen, Yi Yin, Ben Chiaro, Josh Mutus, Charles Neill, et al. Coherent josephson qubit suitable for scalable quantum integrated circuits. _Physical Review Letters_ , 111(8):080502, 2013. 

_BIBLIOGRAPHY_ 

_182_ 

- [203] S Das Sarma, Rogerio de Sousa, Xuedong Hu, and Belita Koiller. Spin quantum computation in silicon nanostructures. _Solid state communications_ , 133(11):737–746, 2005. 

- [204] Susumu Takahashi, Ronald Hanson, Johan Van Tol, Mark S Sherwin, and David D Awschalom. Quenching spin decoherence in diamond through spin bath polarization. _Physical Review Letters_ , 101(4):047601, 2008. 

- [205] S Probst, H Rotzinger, AV Ustinov, and PA Bushev. Microwave multimode memory with an erbium spin ensemble. _Physical Review B_ , 92(1):014421, 2015. 

- [206] Gary Wolfowicz, Hannes Maier-Flaig, Robert Marino, Alban Ferrier, Hervé Vezin, John JL Morton, and Philippe Goldner. Coherent storage of microwave excitations in rare-earth nuclear spins. _Physical Review Letters_ , 114(17):170503, 2015. 

- [207] Yongchen Sun, Thomas Böttger, CW Thiel, and RL Cone. Magnetic g tensors for the<sup>4</sup> I 15 _/_ 2 and<sup>4</sup> I13 _/_ 2 states of Er<sup>3+</sup> :Y2SiO5. _Physical Review B_ , 77(8):085124, 2008. 

- [208] B Car, L Veissier, A Louchet-Chauvet, J-L Le Gouët, and Thierry Chanelière. Optical study of the anisotropic erbium spin flip-flop dynamics. _Physical Review B_ , 100(16):165107, 2019. 

- [209] Elliott Fraval, MJ Sellars, and JJ Longdell. Method of extending hyperfine coherence times in pr<sup>3+</sup> :y2sio5. _Physical Review Letters_ , 92(7):077601, 2004. 

- [210] Andre Schneider, Tim Wolz, Marco Martin Spiecker, Hannes Rotzinger, Alexey V Ustinov, and Martin Weides. Transmon qubit in a magnetic field: Evolution of coherence and transition frequency. _Physical Review Research_ , 1(2):023003, 2019. 

- [211] John Mark Kreikebaum, Allison Dove, William Livingston, Eunseong Kim, and Irfan Siddiqi. Optimization of infrared and magnetic shielding of superconducting tin and al coplanar microwave resonators. _Superconductor Science and Technology_ , 29(10):104002, 2016. 

- [212] Mantas Šim˙enas, James O’Sullivan, Oscar W Kennedy, Sen Lin, Sarah Fearn, Christoph W Zollitsch, Gavin Dold, Tobias Schmitt, Peter Schüffel- 

_BIBLIOGRAPHY_ 

_183_ 

gen, Ren-Bao Liu, et al. Near-surface<sup>125</sup> Te<sup>+</sup> spins with millisecond coherence lifetime. _Physical Review Letters_ , 129(11):117701, 2022. 

- [213] Paul Stevenson, Christopher Phenicie, Sacha Welinski, Isaiah Gray, Sebastian Horvath, Austin Ferrenti, Robert Cava, Stephen Lyon, Nathalie De Leon, and Jeff Thompson. Erbium-implanted materials for quantum communication. In _APS March Meeting Abstracts_ , volume 2021, pages R29–008, 2021. 

- [214] Shun Kanai, F Joseph Heremans, Hosung Seo, Gary Wolfowicz, Christopher P Anderson, Sean E Sullivan, Mykyta Onizhuk, Giulia Galli, David D Awschalom, and Hideo Ohno. Generalized scaling of spin qubit coherence in over 12,000 host materials. _Proceedings of the National Academy of Sciences_ , 119(15):e2121808119, 2022. 

- [215] Alexandre M Souza, Gonzalo A Alvarez, and Dieter Suter. Robust dynamical decoupling for quantum computing and quantum memory. _Physical Review Letters_ , 106(24):240501, 2011. 

- [216] S Haroche, M Brune, and JM Raimond. From cavity to circuit quantum electrodynamics. _Nature Physics_ , 16(3):243–246, 2020. 

- [217] Philip Krantz, Morten Kjaergaard, Fei Yan, Terry P Orlando, Simon Gustavsson, and William D Oliver. A quantum engineer’s guide to superconducting qubits. _Applied Physics Reviews_ , 6(2):021318, 2019. 

- [218] Charles P Poole. Electron spin resonance: a comprehensive treatise on experimental techniques. 1996. 

- [219] Eisuke Abe, Hua Wu, Arzhang Ardavan, and John JL Morton. Electron spin ensemble strongly coupled to a three-dimensional microwave cavity. _Applied Physics Letters_ , 98(25):251108, 2011. 

- [220] Luke A O’Dell. The wurst kind of pulses in solid-state nmr. _Solid state nuclear magnetic resonance_ , 55:28–41, 2013. 

- [221] S Probst, N Kukharchyk, H Rotzinger, A Tkalˇcec, S Wünsch, AD Wieck, M Siegel, AV Ustinov, and PA Bushev. Hybrid quantum circuit with implanted erbium ions. _Applied Physics Letters_ , 105(16):162404, 2014. 

- [222] Nadezhda Kukharchyk, Shovon Pal, Jasper Rödiger, Arne Ludwig, Sebastian Probst, Alexey V Ustinov, Pavel Bushev, and Andreas D Wieck. Photolumi- 

_BIBLIOGRAPHY_ 

_184_ 

nescence of focused ion beam implanted er3+: Y2sio5 crystals. _physica status solidi (RRL)–Rapid Research Letters_ , 8(10):880–884, 2014. 

- [223] Tian Zhong, Jonathan M Kindem, Evan Miyazono, and Andrei Faraon. Nanophotonic coherent light–matter interfaces based on rare-earth-doped crystals. _Nature communications_ , 6(1):8206, 2015. 

- [224] Karl Tordrup, Antonio Negretti, and Klaus Mølmer. Holographic quantum computing. _Physical Review Letters_ , 101(4):040501, 2008. 

- [225] MA Castellanos-Beltran and KW Lehnert. Widely tunable parametric amplifier based on a superconducting quantum interference device array resonator. _Applied Physics Letters_ , 91(8):083509, 2007. 

- [226] N Bergeal, F Schackert, M Metcalfe, R Vijay, VE Manucharyan, L Frunzio, DE Prober, RJ Schoelkopf, SM Girvin, and MH Devoret. Phase-preserving amplification near the quantum limit with a josephson ring modulator. _Nature_ , 465(7294):64–68, 2010. 

- [227] M Hatridge, R Vijay, DH Slichter, John Clarke, and I Siddiqi. Dispersive magnetometry with a quantum limited squid parametric amplifier. _Physical Review B_ , 83(13):134501, 2011. 

- [228] Chris Macklin, K O’brien, D Hover, ME Schwartz, V Bolkhovsky, X Zhang, WD Oliver, and I Siddiqi. A near–quantum-limited josephson traveling-wave parametric amplifier. _Science_ , 350(6258):307–310, 2015. 

- [229] in josephson parametric amplifiers. _IEEE Microwave magazine_ , 21(8):45– 59, 2020. 

- [230] Wyatt Vine, Mykhailo Savytskyi, Daniel Parker, James Slack-Smith, Thomas Schenkel, Jeffrey C McCallum, Brett C Johnson, Andrea Morello, and Jarryd J Pla. Direct detection of spin resonance with a microwave parametric amplifier. _arXiv preprint arXiv:2211.11333_ , 2022. 


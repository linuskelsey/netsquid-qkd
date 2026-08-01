## **A Unit Cooperativity Random Access Quantum Memory** 

## **Patrick Hogan** 

A thesis submitted for the degree of **Doctor of Philosophy** 

University College London Electronic & Electrical Engineering London Centre for Nanotechnology 

London, May 16, 2026 

### Doctoral Candidate Thesis Declaration Form 

You must complete the below declaration and include it in your thesis after your title page. 

Failure to declare contributions may result in being referred to an Academic Misconduct Panel under our <u>Plagiarism or Generative AI</u> use policies. 

If failure to declare is discovered after award, candidates may instead be referred to a Research Misconduct panel under our Research Integrity policy. 

##### Part A: General Declaration 

_You must review and confirm all the points below._ 

☐ This thesis is a presentation of original work. 

☐ This work has not previously been presented for a degree or other qualification at this University or elsewhere. 

☐ All input or assistance in the creation of the academic work other than from the supervisory team (including AI) has been acknowledged in Part B below. 

☐ Any text or data in the thesis that has been presented for publication (including in review) elsewhere is declared in Part B below. 

##### Part B: Declaration of contribution from other sources 

In this section, please declare any contributions from other sources under the headings in bold below. If not used, please write ‘n/a’ under the heading. 

These declarations are intended to give context to the examiners and to ensure that doctoral researchers can use and acknowledge external support confidently. 

Further guidance about what UCL considers ‘other sources’ and examples of completed Declaration Forms can be found in our policy on <u>Transparency on Authorship and Generative AI in Doctoral Research.</u> 

###### **Declarations** 

**Data sources, if not collected yourself** : include any paid/unpaid sources of data 

n/a 

**Software code, instrumentation development, etc** : Describe support received to write code (from human or AI), build bespoke equipment, and any other shared work, 

Superconducting resonator fabrication (Dr. J. Alexander + others), SRIM simulations (Dr. M. Simenas), code for analysis and plotting (AI), developing experimental code (Dr. JB Verstraete + others) 

**AI:** include any use of AI, including generative AI, not already included in the above categories where it has been used as a functional tool to assist in the process of creating the academic work. 

Proof reading (spelling and grammar), formatting references, science discussion and building understanding. 

**Other:** include any other material contributions to your thesis not already included in the above categories. Declare any contributions to proofreading other than standard editorial support, such as professional editing or substantial changes made by AI. 

n/a 

**Publications:** Include full references for all published work and work that has been submitted for publication that includes material shared with the thesis on which the candidate is an author. 

- For each published work give a full citation including: all authors; title; journal/book (chapter); page numbers; volume; date of publication; publisher; DOI – if available. 

- If manuscripts have been uploaded to a preprint server, please give full citations including DOI. 

- Under each listed publication, please identify to which chapter of the thesis the publication relates. 

- For multi-authored works, state your contribution and explain where this work appears in the final thesis. 

###### n/a 

4 

#### **Abstract** 

A quantum memory will be a key component in scaling the processing capabilities of future quantum computers. A promising platform for this is an electron spin ensemble coupled to a superconducting resonator. However, a key limitation of this approach is the efficiency with which states can be stored and retrieved from the ensemble. To this end, this report details measurements of such a system at the ‘unit cooperativity’ point, where energy transfer between the two subsystems becomes lossless. 

We make measurements on two spin-ensemble systems known for their long coherence times: bismuth donors in silicon (Bi:Si) and ytterbium in yttrium orthosilicate (Yb:YSO). Due to their extended coherence times, both are suitable candidates for long-term quantum state storage. 

Using the Bi:Si spin system, we show how an on-chip waveguide can be used to control the bismuth nuclear spin, enabling measurements of the entire nuclear-spin spectrum. We use this control to ‘hyperpolarise’ the nuclear spin state beyond Boltzmann equilibrium, and we measure the nuclear-spin relaxation time through the decay rate of this hyperpolarised state. 

Using the Yb:YSO spin system, we measure the storage and retrieval at unit cooperativity, showing minimal losses between the resonator and the ensemble. Despite this, the overall system efficiency remains low due to losses elsewhere in the system. We present a quantitative analysis explaining why this is the case and identify the specific adjustments required to make the entire storage-and-retrieval process equally efficient. 

5 

#### **Impact statement** 

The work in this thesis describes the development of a ‘unit cooperativity’ randomaccess microwave quantum memory. In pursuit of this, we also develop a novel method for making nuclear-spin-dependent measurements in the millikelvin temperature regime. We finish with a proof-of-concept proposal for a spatially resolved quantum memory using magnetic field gradients. 

The most direct impacts of the work lie in the academic sphere. The designs used to control the bismuth nuclear spin are also of great interest in many other contexts. The approach is fully broadband and can therefore be used to control any other nuclear spins. This enables millikelvin experiments on many potentially interesting samples in physics, chemistry, and biology. 

The work measuring energy storage and retrieval can be directly applied to a new generation of devices using the improvements we have identified. Using the results from this analysis, achieving more than 90% fidelity would become practically realisable. This, in turn, would make spin-ensemble quantum memories a much more feasible option in a full-stack quantum computer. 

technology, and also as a nanoscale distance imaging technique. When applied to a quantum device, it would allow increased storage capability of the memory, thereby increasing storage density. The technique could also be applied to spatial imaging measurements, particularly for biological samples, where it would allow imaging down to the scale of single electron spins. 

The wider impacts of this work are mostly in its implications for quantum computing. This device uses the behaviour of quantum systems to take advantage of new algorithms that are impossible for our current ‘classical’ devices. The development of a quantum memory is a key component that would facilitate large-scale quantum computers becoming feasible. Quantum computers with enough computing power will have far-reaching impacts across a broad range of disciplines, including science, technology, and medicine. 

6 

#### **Acknowledgements** 

This project would not have been possible without the encouragement and support of the many people who have helped me over the last four and a half years. I would particularly like to thank the following people: 

_John Morton_ : I could not have asked for a better supervisor. Your brilliant insight, together with the freedom you gave me throughout my PhD, and the support that was always available when I needed it, has been invaluable. You have helped me grow enormously as a researcher over the course of this project. 

_Jean-Baptiste Verstraete_ : for more things than I can count, including, but certainly not limited to, many physics discussions, sharing your immense knowledge of chirped pulses, your willingness to deal with my dodgy code, and your patient tolerance of my refusal to use Git. 

_Saksham Mahajan_ : for the many hours of whiteboard discussions, physics-adjacent rants, and our excellent post-conference trips. Thank you for encouraging me to step outside my comfort zone. 

_Ana Villanueva Ruiz de Temino_ : for being a constant friend through the thick and thin of a PhD. The experience would not have been the same without you. 

_Joseph Alexander_ : for showing me ‘the ropes’ of resonators. Getting someone up to speed is not an easy job, and you were a brilliant teacher. You really helped me hit the ground running when I arrived in QSD. 

_Antilen Jacob_ : for the many hours helping me anything and everything. You were always willing to help out with whatever side project I was working on. 

_Frédéric Schlattner_ : for the time shared in the cold of G02. Your friendship made a difficult period much more bearable. 

_Mantas äim˙enas_ : for the endless ESR insight. You have answered more of my physics questions than I can count. 

_Patrice Bertet, Emmanuel Flurin, James O’Sullivan_ , and the rest of the Quantronics group: thank you for so kindly hosting me and letting me break things for three months. It was an invaluable learning experience, made even better by such a warm welcome. 

The new generation of resonators, _Ravi, Gokul_ , and _Zichen_ : the lab is in safe hands, and I am confident you will do great things. 

All of the amazing people in _QSD_ , past and present: I am thankful for the many 5(ish)-a-sides, pub trips, and group outings. I was very fortunate to be part of a group with such wonderful people. 

_Ben Gregg_ : for the patience with which you weathered my many years of physicsrelated rambling. Of all my friends, I fear you may have taken the brunt of this PhD, 

7 

and I am continually grateful for your friendship. 

_Peter and Annabel Forde_ : for the many weekend trips to Cambridge. They were invaluable refuges throughout my PhD. You both mean so much to me; may there be many more Hot Numbers trips to come. 

_Hannah Lau_ , and all of the Rosemont girls: of my PhD. Your continued friendship and the numerous debriefs have meant a great deal. 

All the guys from _Bartholomew_ : I could not ask for a more wonderful group of gentlemen to have alongside me. 

The amazing people at _St Luke’s Church Kentish Town_ : I am deeply grateful for the unending encouragement and kindness I have received over the years. 

Finally, to my family, _Mum, Dad, Harry, Sarah, Clare, Emmanuel_ , and _Raya_ : without all of your love and support over the years, I would not be where I am today. Mum and Dad, thank you so much for letting me stay while I wrote this thesis, for cooking delicious food, and for generally looking after me through the final stretch. Raya, I cannot wait to tell you about the joys of quantum technology when you are older. 

# **Contents** 

|**1**|**Intr**|**oduction**|**10**|
|---|---|---|---|
||1.1|A useful quantum computer . . . . . . . . . . . . . . . . .|. . . . . . .<br>10|
||1.2|The case for a ‘Quantum Memory’<br>. . . . . . . . . . . . .|. . . . . . .<br>11|
||1.3|Electron spins as a quantum memory . . . . . . . . . . . .|. . . . . . .<br>14|
||1.4|Thesis outline . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>18|
|**2**|**Ele**|**ctron spin resonance**|**20**|
||2.1|The semi-classical description of ESR . . . . . . . . . . . .|. . . . . . .<br>20|
||2.2|Dynamics of a quantum spin . . . . . . . . . . . . . . . . .|. . . . . . .<br>23|
||2.3|Bismuth donors in silicon . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>30|
||2.4|Ytterbium in yttrium oxide silicate . . . . . . . . . . . . .|. . . . . . .<br>32|
||2.5|Pulsed ESR techniques . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>34|
||2.6|Decoherence . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>40|
||2.7|Relaxation . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>45|
|**3**|**Sup**|**erconducting resonators**|**47**|
||3.1|The lumped element circuit theory model . . . . . . . . . .|. . . . . . .<br>47|
||3.2|Quality factor . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>50|
||3.3|Coupling an electron spin to an LC resonator<br>. . . . . . .|. . . . . . .<br>52|
|**4**|**Exp**|**erimental Methods**|**64**|
||4.1|Cryostats<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>64|
||4.2|Resonator development . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>68|
||4.3|Implantation & Annealing . . . . . . . . . . . . . . . . . .|. . . . . . .<br>80|
||4.4|Pulsed ESR measurements . . . . . . . . . . . . . . . . . .|. . . . . . .<br>81|
|**5**|**EN**|**DOR with microresonators**|**91**|
||5.1|Chip design . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>91|
||5.2|Continuous-wave measurements . . . . . . . . . . . . . . .|. . . . . . .<br>94|
||5.3|Pulsed measurements . . . . . . . . . . . . . . . . . . . . .|. . . . . . .<br>97|
||5.4|ENDOR spectroscopy . . . . . . . . . . . . . . . . . . . . .|. . . . . . . 101|
||5.5|Spectroscopy of further transitions<br>. . . . . . . . . . . . .|. . . . . . . 105|



8 

Contents 

9 

||5.6|Measuring time dynamics<br>. . . . . . . . . . . . . . . . .|. . . . . . . . 110|
|---|---|---|---|
||5.7|Discussion . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 111|
|**6**|**Hyp**|**erpolarisation of bismuth nuclear spins**|**112**|
||6.1|Pulsed ESR in the Purcell limit . . . . . . . . . . . . . .|. . . . . . . . 112|
||6.2|Hyperpolarisation . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 119|
||6.3|Nuclear _T_1 . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 122|
||6.4|Cooperativity . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 124|
||6.5|Discussion . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 125|
|**7**|**Uni**|**t cooperativity with Yb:YSO**|**127**|
||7.1|An input-output theory model of ESR<br>. . . . . . . . . .|. . . . . . . . 127|
||7.2|ESR at unit cooperativity<br>. . . . . . . . . . . . . . . . .|. . . . . . . . 139|
||7.3|Comparing the model to results . . . . . . . . . . . . . .|. . . . . . . . 145|
||7.4|Proposal for spatially resolved RAQM<br>. . . . . . . . . .|. . . . . . . . 152|
||7.5|Discussion . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 161|
|**8**|**Con**|**clusions and outlook**|**162**|
||8.1|Future work . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 163|



# **Chapter 1** 

# **Introduction** 

#### **1.1 A useful quantum computer** 

the British during World War II to decrypt German ciphers used in military communication [1]. Since then, the use of digital computing has become pervasive across all areas of society, not just code breaking, and has ultimately driven a technological revolution that has brought in an entirely new era for humanity. In the modern age, encryption is used extensively across society, whereby protocols like ‘Rivest–Shamir–Adleman’ (RSA) cryptosystem are used to protect our information online [2]. RSA and similar encryption techniques rely on the difficulty of factoring very large prime numbers. 

In 1994, however, Peter Shor proposed an algorithm that could factor primes in polynomial time [3], placing it leagues ahead of the state of the art<sup>1</sup> . The difference was that the processor required to run Shor’s algorithm is fundamentally different from the computers we have today. The processor required to run this computation would need to leverage the unique phenomena found at the smallest scales of nature: quantum mechanics. This ‘quantum’ computer would be a device able to leverage superposition and entanglement to execute algorithms previously impossible for today’s ‘classical’ computers. Given the impact that computers have had on the world since their invention, it is not hard to imagine the significant impact that this new technology could have on the society of the future. 

The use cases of a quantum computer do not stop at simply breaking encryption. The areas of medicine, science, and technology all have potential use cases yet to be explored. Given the potential impact of this technology, there has been a considerable multinational effort to develop a ‘useful’ quantum computer: a device capable of utilising quantum mechanics to make relevant calculations significantly faster than a classical one. Given the vague nature of these terms, there is debate as to when the 

> 1The most scalable classical algorithm for prime factorisation is the ‘general number sieve’ (GNFS), which runs in sub-exponential time [4]. 

10 

The case for a ‘Quantum Memory’ 

11 

A key term used in this discussion is the idea of ‘quantum advantage’, whereby a quantum computer makes computations that would be practically infeasible for even the world’s most powerful computers. A contender for this title comes from Google Quantum AI’s ‘Sycamore’ processor, whereby their 53-quantum-bit (qubit) processor was claimed to have achieved this feat [5]. However, due to advancements in the simulation of quantum computers on classical hardware, and the questionable practical use case of their calculations, their claim is still a matter of debate [6]. The quantum computers of the future will nevertheless require significantly more than the 53 qubits of the Sycamore processor. A paper from Gidney and Ekerå in 2021 described using 20 million qubits for prime factorisation of a 2048-bit RSA integer [7]. A key challenge for the future of quantum computing, then, is scaling the computational power by six orders of magnitude. 

#### **1.2 The case for a ‘Quantum Memory’** 

The practicality of scaling a quantum computer by this degree is Many possible implementations require significant cooling or control apparatus, which becomes infeasible at these large scales. One key underexplored avenue for reducing the burden on the available processing power is to use a memory. The vast majority of quantum computing research is directed towards a ‘quantum processing unit’ (QPU). This, in direct analogy to the ‘central processing unit’ (CPU) of a classical computer, would be where the logic gates and computation of quantum algorithms take place. Despite the volume of research being done in this field, there is still no appropriate memory to accompany one of these quantum processors. In a standard classical computer, there is a CPU and RAM (random access memory). The RAM acts as short-term storage that allows the CPU to offload information while it is not directly in use, thus freeing up the CPU to have constant uptime maximising its computational output. It does not take a big stretch of the imagination to realise that the quantum computers of the future are going to be equipped with a similar memory. In this case, the memory would need to be able to store and retrieve coherent quantum information. The same task of factoring a 2048-bit RSA integer would require fewer than 15,000 qubits if the processor were equipped with an appropriate memory [8]. This three-order-ofmagnitude difference highlights the importance of quantum memories as a resource in quantum computing. 

With this as motivation, we consider how to go about designing such a memory. In theory, any quantum object could be used for storing quantum information; however, some are more appropriate than others. Given the array of different quantum systems and technologies already under development, we want to evaluate which may be the best contender for this application. We therefore define seven key characteristics to 

The case for a ‘Quantum Memory’ 

12 

evaluate how appropriate a system is as a scalable memory: 

###### **1.2.1 Coherence time** 

The memory should be able to reliably store quantum states for the duration of a given algorithm without the information being corrupted. This means that the time over which a state can be stored and retrieved from the memory without significant corruption must be comparable to the duration of the algorithm. In the ideal case, a quantum state stored at the beginning of the algorithm should still be uncorrupted at the end. However, the duration of a specific algorithm can vary wildly, or may be a function of the memory capacity itself, and error correction can be used to diminish the impact of memory errors. As an easily comparable metric, we consider the coherence time of the memory _T_ 2. This is the timescale over which the coherence of the memory decays to 1 _/e_ of its initial value, and it can differ starkly between systems. For some qubit platforms, this can be in the nanosecond range or lower, while for others it may be many hours [9, 10]. The 13-order-of-magnitude difference highlights a key consideration in the evaluation of a quantum memory candidate. 

###### **1.2.2 Memory density** 

A useful quantum memory needs to have a memory volume large enough to concurrently store all the states required to perform a specific algorithm. However, given that the total memory volume can typically be expanded by simply increasing the number of connected memory modules, and that a real quantum computer will have physical volume limitations, the key characteristic of note is then the storage density of the memory. This can be quantified by the number of states per unit volume, in real-space, that can be stored by the memory: 



where _N_ is the number of states that can be concurrently stored and _V_ is the spatial volume of the memory. For a memory to be useful, we require it to have a higher storage density than the quantum processor it is connected to. This again can vary over many orders of magnitude depending on implementation [11, 12, 13]. 

###### **1.2.3** 

quantum state being stored, which can cause errors in the overall computation. Error correction protocols can be employed to minimise this, but ultimately the memory will 

The case for a ‘Quantum Memory’ 

13 

still be limited by these so this is a key performance metric for evaluating a memory. The overall round-trip efficiency can be defined as the product of the read and write efficiencies: 



Where _÷_ write ( _÷_ read) is the fraction, in energy, of the input (output) state that makes it into (out of) the memory. 

###### **1.2.4 Read and write speed** 

During the execution of a quantum algorithm, many read and write operations will need to happen throughout. If the read and write speed of the memory is slow compared to the processor gate time, the algorithm will be bottlenecked by waiting for the memory. This in turn will increase the overall computation time. We can therefore define a property that considers how long it takes to save and retrieve information from the quantum memory, _t_ read/write, which we require to be comparable to the typical gate time, _t_ gate, of the QPU: 



###### **1.2.5 Random access** 

This is a binary pass/fail criterion that we require for any potential quantum memory system. For a given algorithm, it is unlikely that the order in which states are written to and read from the memory will directly match, and this will vary from one computation to the next. For the quantum memory to be useful in increasing computational power, we need states to be retrievable in an arbitrary order with respect to the order in which they were stored, and this order must be programmable from one computation to the next. We therefore narrow our description from simply ‘Quantum Memory’ to ‘Random Access Quantum Memory’ (RAQM)<sup>2</sup> . Whilst there are certainly applications for a quantum memory without random access, it would severely limit the ability to reprogram the system, and so the long-term stability of the computation it can achieve. 

###### **1.2.6 Operating frequency** 

There are many good candidates for both processors and memories that work in both the microwave and optical frequency domains [11, 13, 14, 12]. However, given the current lack of high-efficiency microwave-optical quantum transducers, it is important that a memory can operate without the need for a large change in photon frequency 

> 2This is not to be confused with a ‘Quantum Random Access Memory‘ (QRAM), where the allocation of where to save states into the memory is done with qubits, leading to states being saved as superpositions across memory blocks. 

Electron spins as a <u>quantum</u> memory 

14 

between processor and memory. We therefore require that the two operate at the same, or a similar, frequency. If the processor operates in the optical domain, then so should the memory, and the same applies for the microwave domain. 

###### **1.2.7 Operating conditions** 

For the property, we consider that, in the ideal quantum computer, the memory would be operated in close proximity to the QPU. For practicality, then, the two should operate under the same physical conditions as one another. This means environmental factors like operating temperature, pressure, and magnetic field should be applicable to both the QPU and RAQM. This is not a necessity, since low-loss optical fibres and coaxial cabling allow photons to be moved across large distances with negligible signal degradation. However, in the context of scalability, it can become problematic. It is not a binary consideration, as there are a number of environmental conditions to consider, and tolerable ranges for each. As such, it is a more subjective criterion with greater compatibility being better. 

#### **1.3 Electron spins as a quantum memory** 

Given the outlined above, spin ensembles are a promising platform for a quantum memory. We can show this by considering them in light of the criteria above. Coherence time is one of the most important considerations, since there are often physical limitations on the coherence time of a system that cannot be improved through engineering. Nuclear spins in particular can have extremely long-lived coherence, europium ions in an yttrium orthosilicate crystal (Eu<sup>3+</sup> :Y2SiO5) have been measured with _T_ 2 exceeding 10 hours [15]. Some of the earliest quantum computing concepts used nuclear spins as a resource because of this fact [16]. However, their insensitivity to noise comes from the low nuclear gyromagnetic ratio, which also makes control slow, another key metric in the criteria above. A nice middle ground can be found using the electron spin degree of freedom. The electron spin for bismuth donors in silicon is among the longest lived; in Figure 1.1, we can see measurements made in both natural and isotopically purified substrates, with the longest _T_ 2 reaching 2.7 s for these measurements [17]. Rare-earth ions are also strong contenders, having been measured with _T_ 2 in the range 10-100 ms at microwave frequencies [18, 19, 20]. The cost of the shorter electron _T_ 2 comes with the upside of significantly faster control: the gyromagnetic ratio of the electron is three orders of magnitude larger than that of a typical nuclear spin [21, 22], and so the control times scale accordingly. We argue that this is a good trade to make, since a _T_ 2 of seconds already far outstrips the state of the art for many quantum processors [23]. Using the electron spin degree of freedom also 



<!-- Start of picture text -->
a) 1.0 b) 1.0<br>5 084 WW 2[ A 5 0.8<br>8 It 8 |<br>= 0.6 AT =< 06<br>c \ T,.=27s c dL 7, =93ms<br>2 04 Vij, 2 2 04 2<br>o Val) o DN<br>5S 0.2 Why) 5S 02 h<br>= 28S;:Bi Thai Nal<br>0.0 0.0 malibu<br>0 2 4 6 0.0 0.1 0.2 0.3<br>Time, 27 (s) Time, 27 (s)<br><!-- End of picture text -->

Electron spins as a <u>quantum</u> memory 

16 

A real quantum memory would not necessarily need to be operated this fast, but it eliminates the possibility of the spin control being the bottleneck. At millikelvin operating temperatures and without sufficient mitigation, the power required for this level of pulse duration would cause far too much heating, so this becomes a balancing act based on specific experimental parameters. 

Random access to states within a spin ensemble memory has also already been shown using chirped pulse phase encoding [12]. In this example, 16 distinct memory modes are possible based on the range of available chirp parameters; however, this is as a consequence of pulse power limitations and not a fundamental one. There have also been multiple theoretical works detailing the use of a frequency- and bandwidthtuneable resonator as a quantum memory [36, 37]. with examples of tunable resonators successfully being used in ESR [38, 39, 40]. If access does not need to be random, spin ensembles can also be readily operated as a ‘First In Last Out’ (FILO) memory simply using a _fi_ rotation pulse between storage and retrieval. This technique has been shown to work with 100 distinct modes in the memory [41]. 

There are spin ensembles with attractive transitions in both the optical and microwave domains, but operation becomes quite disparate between the two. For this project, we choose microwave operation due to the current development level of microwave-frequency QPUs [42, 43, 44]. There are many strengths to an optical memory, and some promising candidates for optical QPUs, but they will not be discussed here. Assuming the spin transition already sits in the microwave domain, the frequency of a specific transition can be tuned via the Zeeman interaction. We can therefore easily fulfil the final criterion. For some transitions, there are ‘sweet spots’ where the system properties are optimised for a specific frequency and field. However, since this also lies in the microwave domain, spin ensembles would be easily integrable with existing microwavefrequency QPUs. 

###### **1.3.1 Practical implementation** 

Given the strengths we have detailed about this approach, we consider the practicalities of using a spin ensemble as a quantum memory. By coupling to the ensemble via a superconducting resonator, we can easily integrate the system into the already wellexplored field of circuit quantum electrodynamics (cQED). In Figure 1.2, we propose an example of how this approach may work in practice. Here, all qubits are connected to a memory bus that allows coupling to a single global memory. It is also possible to do this in a modular way for a collection of qubits or a single qubit. Previous work in this area has shown proof of this concept by coupling superconducting qubits to NV centres in diamond [45, 46]. An example of this is shown in Figure 1.3, where 

Electron spins as a <u>quantum</u> memory 

17 



Figure 1.2: A schematic proposal for a quantum processor. There is a small implant region of spins (white) which are coupled to a superconducting resonator (purple). The resonator is controlled by pulses input from left/right, where a galvanic connection to the resonator allows driving currents. This means that the constant field required for Larmor precession can be generated on-chip. All four qubits (blue) are controlled by their external coupler (yellow) and coupled to a central memory bus (green) via the bus couplers (red). By making the bus couplers tunable the qubits can be dynamically put on resonance with the spin ensemble to allow for storage and retrieval. Similarly, the central bus can be used to facilitate coupling between specific qubits for multi-qubit gates. 



Thesis outline 

19 

making and measuring these hybrid quantum systems. The resonator fabrication recipe is explained, as well as the equipment required for low-temperature and high-frequency measurement. 

In Chapter 5, we present the set of experimental results, showing how a novel superconducting chip design can be used for nuclear spin control, and make measurements using this design on bismuth donors in silicon. Using the electron spin to read out changes in the nuclear spin state, we present evidence for comprehensive control over this degree of freedom. This design also serves as proof of concept for other multi-frequency ESR experiments using superconducting microresonators. 

In Chapter 6 we extend the work of the previous chapter and use the nuclear spin control to dynamically increase the resonant spin population. This technique can be used to increase the system cooperativity, allowing us to dynamically move towards the unit-cooperativity critical point. We then use the increased polarisation to measure the relaxation rate of the nuclear spin. 

In Chapter 7 we show measurements of the Yb:YSO spin system at the unitcooperativity point, and measure the efficiency of photon storage and retrieval there. We then propose how the excess cooperativity could be used as a spatially resolved RAQM. This proposal also highlights potential future uses for gradient-field ESR in circuit QED. 

Finally, in Chapter 8 we conclude the experimental results and discuss the new potential avenues for exploration as a result of this work. 

# **Chapter 2** 

# **Electron resonance spin** 

The of magnetic resonance, including both electron spin resonance and nuclear magnetic resonance (NMR), has existed since the 1940s [48, 49]. The ability to control and measure the changing states of electron and nuclear spins is hugely influential in many areas of technology and medicine [50, 51]. The intrinsic angular momentum of particles, spin, is a quantum effect. However, by considering the collective motion of a great many spins, we can use classical mechanics to describe the time evolution of their total state under the influence of magnetic fields. 

In this chapter, we discuss the relevant theory for describing electron spins driven by magnetic fields. We start with the semi-classical description, considering the motion of the net magnetisation vector of an electron spin ensemble. We then show how this description can be extended using quantum theory to make accurate predictions of many physical phenomena. Finally, we consider the toolbox of ESR techniques used for this work, as well as the underlying mechanisms for decoherence and relaxation in ESR. 

#### **2.1 The semi-classical description of ESR** 

For the purposes of understanding the bulk dynamics of an electron spin ensemble, it is instructive to consider the net magnetisation of these spins. This is the vector sum of all of their individual magnetic moments [52]: 



where **_M_** is the net magnetisation per unit volume _V_ and **_µ_** _i_ is the magnetic moment of the _i_ th spin. The magnitude and direction of **_M_** then describe the collective motion of the ensemble. Considering a constant field **_B_ 0** applied to the magnetisation, the 

20 

The semi-classical description of ESR 

21 

collective motion is then: 



where _“e/_ 2 _fi ¥ ≠_ 28 MHz T<sup>_≠_1</sup> is the electron gyromagnetic ratio. This means that the magnetisation will precess about the magnetic field axis with frequency: 



where _Ês_ is the frequency of precession, the Larmor frequency, and _B_ 0 = _|_ **_B_ 0** _|_ . If we define 



where _˛_ **_z_** is a unit vector parallel to the _z_ -axis, then the direction of precession will also be parallel to _z_ . We then apply an oscillating magnetic field ( **_B_** 1) to the spin ensemble, linearly polarised perpendicular to **_B_ 0** , so that: 



where _B_ 1 is the magnitude of the and _Ê_ is the frequency of oscillation. This can be rewritten as the sum of two counter-rotating components in the _xy_ plane: 



If we assume that _Ê ¥ Ês_ , then from the perspective of the magnetisation one of these components is at a small frequency: 



and the other at a large frequency: 



We can see a graphical representation of this in Figure 2.1. 

We can simplify this situation if we consider a reference frame that rotates with one of these components at frequency _Ê_ . This frame is referred to as the ‘rotating frame’, in contrast to the ‘lab frame’, where **_B_ 0** / **_B_ 1** are the constant/oscillating fields described above. From within the rotating frame, we can simplify the effect of **_B_ 1** by making the approximation that, so long as the Larmor frequency is large compared to the applied field ( _Ês ∫|“eB_ 1 _|_ ), the high-frequency rotating component of the field, _Ê_ + _Ês_ , will average to zero and so can be ignored from the perspective of the spin. If we then set the frequency of the _B_ 1 field equal to the Larmor frequency of the ensemble ( _Ê_ = _Ês_ ), then from the rotating reference frame the effect of **_B_ 0** will be zero, and **_B_ 1** 

The semi-classical description of ESR 

22 







Figure 2.1: Diagrams of the rotating and lab reference frames, showing the rotating wave approximation. a) A field oscillating along the _x_ -axis can be decomposed into two counter-rotating fields with half the magnitude, here shown in red and cyan. b) By considering a rotating frame of reference (blue), one field (cyan) has a similar frequency and so their difference grows slowly (∆1). The counter-rotating field (red) has a large _¥_ 2 _Ê_ difference in frequency ( ), and so the phase difference with respect to the reference also grows quickly. c) From the perspective of the rotating reference frame, the red field rotates so rapidly that it averages to zero. This approximation is called the ‘rotating wave approximation’. 

will be constant and parallel to the _x_ -axis. From this perspective, the magnetisation will then precess about the _x_ -axis at a rate: 



If the frequency of **_B_ 1** is not the same as the Larmor frequency ( _Ê_ = _Ês_ ), then the effect of **_B_ 0** is not mitigated in the rotating frame. Thus, the axis of rotation becomes: 



where ∆= _Ês ≠ Ê_ is the detuning between the microwave and Larmor frequencies. The precession about this axis is now enhanced by **_B_ 0** and has frequency: 



Where Ω _R_ is the ‘Rabi frequency’, which gives the rate of rotation about the vector **_B_** eff. If this field is applied for a time _t_ pulse, then the magnetisation will rotate through an angle: 



Where _–_ is the tip angle between **_M_** and the _z_ -axis. We can therefore pulses based on their rotation angle on the magnetisation in the rotating frame. For a desired 

Dynamics of a <u>quantum</u> spin 

23 

rotation angle _fi_ , the duration of the pulse _tfi_ is: 



#### **2.2 of a Dynamics quantum spin** 

We saw in the previous section that an electron spin in a magnetic would precess, and that by using microwave pulses at the precession frequency we could rotate the magnetisation. As the magnetic environment becomes more complicated, we can use quantum mechanics to describe the evolving system dynamics. By writing down the Hamiltonian for the system under study, we can solve for the eigenvectors and eigenvalues, and from these determine the relevant states and transitions. 

###### **2.2.1 Electron coupled to a nuclear spin** 

For an electron spin ( _S_ = 1 _/_ 2) coupled to a nuclear spin ( _I_ = 1 _/_ 2), the system can be described by the Hamiltonian: 



Where _H_ is the total Hamiltonian, _H_ Z is the electron Zeeman term, _H_ HF interaction, and _H_ NZ is the nuclear Zeeman term. _H_ Z is exactly the same interaction described above: the potential energy of a classical magnetic dipole in a magnetic field is written as: 



The corresponding Zeeman term in the Hamiltonian is simply: 



Where **_µ_** _e_ is the magnetic dipole moment, and **_B_** is the applied magnetic An electron spin has magnetic dipole moment: 



Where _ge_ is the electron g-factor ( _ge ¥ ≠_ 2), _µB_ is the Bohr magneton, and **_S_**<sup>**ˆ**</sup> is the vector spin operator: 



Here: 



Dynamics of a <u>quantum</u> spin 

24 

with _‡_ ˆ _x,y,z_ being the three Pauli matrices. For simplicity we can assume that the magnetic field is aligned to the _z_ -axis: 



The Zeeman term therefore to: 



By direct comparison to equation 2.3, this can be written as: 



Where _Ês_ is the electron Larmor frequency, and _“e_ = _geµB/_ ~. Similarly, the nuclear Zeeman term becomes: 



Where _gn_ is the g-factor of the nuclear spin under study, _µN_ is the nuclear magneton, ˆ _Iz_ is the nuclear spin operator, and _Ên_ is the nuclear Larmor frequency. The minus sign comes from the fact that, depending on the nuclear spin in question, and hence the sign of _gn_ , the nuclear spin may preferentially align or anti-align with the field _B_ 0. This means that _Ês_ and _Ên_ are generally positive quantities. The interaction of the nuclear and electron spins with each other is described by the hyperfine interaction: 



If this interaction is isotropic, then **_A_** = _A_ IsoI, so: 



The total Hamiltonian for this case is therefore written as: 



We can use a matrix representation to the spin basis, considering the electron and nuclear spin states, _ms_ and _mI_ . We define their combination states as: 



Dynamics of a <u>quantum</u> spin 

25 

Where _|øÍ_ refers to the _ms_ state of the electron spin, and _|«Í_ is the _mI_ state of the nuclear spin. In this basis, the Hamiltonian is written as: 



Which can be diagonalised for eigenvalues: 



With respective eigenvectors: 









where the angle _◊_ that determines the mixing between the two original basis states ( _|ø»Í_ and _|¿«Í_ ) is given by: 



At high fields, this mixing becomes small since _A π Ês_ , so we regain the original basis states _ms_ and _mI_ . In the low-field limit, where the hyperfine coupling dominates, these are no longer good quantum numbers due to the high level of mixing. In this field range, however, we find that **_F_**<sup>**ˆ**</sup> = **_S_**<sup>**ˆ**</sup> + **_I_**<sup>**ˆ**</sup> , the total spin, is conserved. In this total spin basis, at zero field we find two distinct manifolds with _F_ = 1 and _F_ = 0. In the _|F, mF Í_ 

Dynamics of a <u>quantum</u> spin 

26 



Figure 2.2: Plot of the eigenvalues of the Hamiltonian for a nuclear spin coupled to an electron ( _I_ = 1 _/_ 2 _, S_ = 1 _/_ 2). The energies of each state have been calculated using _“e_ = _≠_ 28 _._ 02 MHz/mT, _“n_ = 42.58 MHz/mT, and _A_ = 1420 MHz, corresponding to the values for a hydrogen atom. At low fields, we can see how the _F_ manifold description makes sense due to the singlet/triplet states; the energies _E_ 1 _,_ 2 _,_ 4, as calculated in 2.29, converge to the same energy, + _A/_ 4. At high fields, the original electron/nuclear spin basis becomes clear again as _E_ 4 crosses back into negative frequency. 

basis, the eigenstates are: 



These are simply the singlet/triplet states. 

###### **2.2.2 Driving an electron spin** 

To allow driving of transitions between spin states, we must include a time-varying magnetic field in the Hamiltonian. For simplicity, we start by considering the effect of _˛_ this drive on a free electron in a constant field **_B_ 0** = _B_ 0 **_z_** . In direct analogy to the semiclassical description above, this field has amplitude _B_ 1 and is oriented perpendicular to the _z_ -axis: 



Dynamics of a <u>quantum</u> spin 

27 

Using equation 2.15 for both terms, the time-varying Hamiltonian can then simply be written as: 



To make the transformation into the rotating frame of the spin, we use the unitary _U_ ( _t_ ) = _e_<sup>_iÊtS_ˆ</sup><sup>_z/_~</sup> with the identity: 



The transformed Hamiltonian becomes: 



We can again make the approximation made in the semi-classical case, termed the ‘rotating wave approximation’ (RWA). Assuming that _Ê ∫ Ê_ 1 and _Ês ¥ Ê_ , as is the case for most ESR experiments, the terms with frequency 2 _Ê_ will average to zero in the rotating frame of the spin. This allows simplification to a time-independent Hamiltonian _H_<sup>_Õ_</sup> ( _t_ ) _æ H_ RWA. Using ∆= _Ês ≠ Ê_ , we then find: 



Which can easily be diagonalised for eigenvalues: 



Where we used the from 2.11. The eigenvectors are: 







To observe the of the _B_ 1 on the system, we can put the spin in an initial state ( _|Â_ ( _t_ = 0) _Í_ = _|øÍ_ ) and evolve it in time using: 



The time evolution of the state then becomes: 



Dynamics of a <u>quantum</u> spin 

28 



Figure 2.3: a) A plot of the _z_ projection of the magnetisation ( _Mz_ ) as a function of pulse duration. At zero detuning, the spin oscillates between _±_ 1; as the detuning is increased (lighter colour), the oscillation frequency also increases and the amplitude decreases. This leads to a decrease in the minimum possible _Mz_ value. b) Plots of the same oscillations on the Bloch sphere. At zero detuning, we see the largest circle, which encompasses the entire diameter. As the detuning increases, we see the effective driving field (blue) moves away from the equator leading to smaller-diameter oscillations. 

The Bloch sphere representations for these oscillations are plotted in Figure 2.3 for different detunings ∆. Increasing the detuning between the drive frequency and the electron Larmor frequency rotates the axis of rotation in the Bloch sphere towards the _z_ -axis. We can calculate the probability of finding the electron in the _|¿Í_ state after a time _t_ : 



###### **2.2.3 Driving transitions in the mixed regime** 

We can combine the results from §2.2.1 and §2.2.2 to understand the of a driving field on the coupled nuclear-electron spin system. The transformation from the hyperfine coupling means that the _mF_ = 0 states are no longer eigenstates of the _S_<sup>ˆ</sup> _z_ operator. This means that, in the low-field regime, we can now drive transitions between spin states with a microwave field ( _B_ 1) that is parallel to _B_ 0. These transitions, 

Dynamics of a <u>quantum</u> spin 

29 



Figure 2.4: a) A plot of the result from 2.52 as a function of normalised to its maximum value. At low field, _Sz_ transitions have a high probability since the hyperfine coupling is large compared to the spin Larmor frequencies; this directly corresponds to when the _|F, mF Í_ basis is valid. b) Comparisons to the effective Rabi frequency when in the _|F, mF Í_ regime. Due to the mixing of states, changing _mF_ couples via both the electron and nuclear gyromagnetic ratios. At low fields, the electron-like character of the state facilitates a Rabi frequency comparable to that of a free electron. 

though classically disallowed, become possible when the interaction is large compared to the electron/nuclear Larmor frequencies. Due to _Sz_ being the operator that drives these transitions, they are referred to as _Sz_ -style transitions. As the field becomes larger, they become more ‘disallowed’ in a quantum sense. Since the transition probability will be governed by the matrix element, we can determine this as a function of for a transition: field specific 



Showing the of this transition probability as _Ês_ begins to dominate _A_ , we see a plot of this in Figure 2.4. 

We also in the _|F, mF Í_ regime that due to the mixing of states, driving transitions between _mF_ states with a _B_ 1 field couples to both the _Sx_ and _Ix_ operators simultaneously. This is important since, if one tries to drive a spin transition via the _Ix_ operator, the Rabi frequency is proportional to the nuclear gyromagnetic ratio _“n_ . However, if one drives a transition through _Sx_ , the relevant parameter becomes _“e_ . Due to the three-orders-of-magnitude difference, having electron-like character in a transition leads to vastly faster Rabi frequencies. The Rabi frequency of the _F_ = 1, _mF_ = 1 _æ_ 0 transition as a function of mixing is: 





<!-- Start of picture text -->
Hl Si<br>Hl Bi<br><!-- End of picture text -->



<!-- Start of picture text -->
20.0 20.0 1.0<br>17.5 17.5<br>0.8 0.8<br>15.0 15.0<br>¥125 oe Z 125 ><br>c Sr a = 0. 6=<br>g pr . P pd 0.4 x ~ . ~<br>v 75 Pe 0 7.5 0.4WN<br>: 0.2 0.2<br>2.5 > 2.5<br>0.0 0.0<br>0 100 200 300 400 500 0 100 200 300 400 500<br>Field (mT) Field (mT)<br>El  I— 30 10<br>ar 0.8 0.8<br>[=__(S 10 0.6 2 10 / / / 0.6 Z<br>s0<br>5- 10 ay -1 0 // 0.4 ©<br>0.2<br>- 20 -2 0 0.2<br>- 30 -3 0<br>0 100 200 300 400 500 0 100 200 300 400 500<br>Field (mT) Field (mT)<br><!-- End of picture text -->

Ytterbium in <u>yttrium</u> oxide silicate 

32 

Table 2.1: A table of all of the Bi:Si clock transitions. 

|_|F, mFÍgæe_|Transition type|Field (mT)|Frequency (GHz)|
|---|---|---|---|
|_|_4_,_<br>0_Í æ |_5_,_<br>0_Í_|_Sz_|0|7.3758|
|_|_4_, ≠_1_Í æ |_5_,_<br>0_Í_|_Sx_|26.54|7.3387|
|_|_4_,_<br>0_Í æ |_5_, ≠_1_Í_|_Sx_|26.67|7.3383|
|_|_4_, ≠_1_Í æ |_5_, ≠_1_Í_|_Sz_|52.68|7.2268|
|_|_4_, ≠_2_Í æ |_5_, ≠_1_Í_|_Sx_|79.83|7.0328|
|_|_4_, ≠_1_Í æ |_5_, ≠_2_Í_|_Sx_|79.96|7.0317|
|_|_4_, ≠_2_Í æ |_5_, ≠_2_Í_|_Sz_|105.36|6.7601|
|_|_4_, ≠_3_Í æ |_5_, ≠_2_Í_|_Sx_|133.43|6.3741|
|_|_4_, ≠_2_Í æ |_5_, ≠_3_Í_|_Sx_|133.54|6.3723|
|_|_4_, ≠_3_Í æ |_5_, ≠_3_Í_|_Sz_|158.03|5.9007|
|_|_4_, ≠_4_Í æ |_5_, ≠_3_Í_|_Sx_|188.09|5.2168|
|_|_4_, ≠_3_Í æ |_5_, ≠_4_Í_|_Sx_|188.18|5.2142|
|_|_4_, ≠_4_Í æ|_5_, ≠_4_Í_|_Sz_|210.71|4.4255|



many transitions go through a local minimum. These are so-called ‘clock transitions’ or Zero First-Order Zeeman (ZEFOZ) points, where due to the insensitivity, to first order, of the transition frequency to changes in field the spin becomes insensitive to local magnetic field fluctuations. This leads to greatly enhanced coherence times at these points, with _T_ 2 becoming as long as 2.7 s [17] for purified silicon. There are a total of 13 ZEFOZ points for both _Sx_ and _Sz_ transitions. These all exist between 4.4–7.4 GHz and 0–211 mT. A list of all of these is given in Table 2.1. 

#### **2.4 Ytterbium in yttrium oxide silicate** 

The second spin ensemble used in this work is an ytterbium ion substituted into yttrium oxide silicate: Yb<sup>3+</sup> :Y2SiO5 (shortened to Yb:YSO). An example unit cell is shown in Figure 2.7, where Yb<sup>3+</sup> substitutes for Y<sup>3+</sup> . Yb<sup>3+</sup> , being a Kramers ion within the crystal field from YSO, can be described with an effective _S_ = 1 _/_ 2 spin Hamiltonian. The consequence is a strongly anisotropic hyperfine interaction and electronic g-factor, varying with respect to the crystal axes. Since the system is not isotropic, the Zeeman and terms for the Hamiltonian are written: Hyperfine effective 



is applied with respect to the crystal axes. Along with the high anisotropy, there are also seven stable isotopes of ytterbium, with their relative abundance and nuclear spin shown in Table 2.2. Given that 70% of the spin population has _I_ = 0 the largest spin 



<!-- Start of picture text -->
2) rT<br>¥ -- = 0 Yb<br>Jeu 00EO<br>d i Pa ED = 7 5<br>b)_———_ 7]<br>EEE<br>RT 2 4<br><!-- End of picture text -->

Pulsed ESR techniques 

34 

signal will come from these isotopes due to their higher spin concentration. There are also two substitutional sites that the ytterbium can inhabit, so we use the g-tensors for both [55]. We provide **_g_** and **_A_** for<sup>171</sup> Yb at both of these sites using the coordinate convention ( _D_ 1 _, D_ 2 _, b_ ): Site 1: 



Site 2: 



where **_g_** 1 _,_ 2 is unitless and **_A_** 1 _,_ 2 is in megahertz. The _I_ = 0 and _I_ = 5 _/_ 2 isotopes will have the same _g_ -tensors: the _I_ = 0 isotopes without a hyperfine interaction, and the _I_ = 5 _/_ 2 isotope with the same hyperfine tensor scaled by _≠_ 0 _._ 27 [56]. Again, due to the large complexity of this spin system, we use EasySpin to calculate the energy levels for all of the naturally occurring isotopes. In Figure 2.8, we plot these as a function of field along all three crystal axes. Due to the larger hyperfine interaction the _I_ = 1 _/_ 2 and _I_ = 5 _/_ 2 isotopes also have ZEFOZ points [56]. We can also take advantage of the anisotropic g-tensor to reduce the sensitivity of the electron spin to field fluctuations in another way. If the desired transition is _Sx_ type, by aligning the field and resonator properly we can pick out the large term in the g-tensors for spin-resonator coupling and use the small term for spin- _B_ 0 coupling [18]. 

#### **2.5 Pulsed ESR techniques** 

###### **2.5.1 One pulse** 

The most basic ESR pulse sequence is a single pulse. By picking the duration such that the tip angle _–_ is a _fi/_ 2 rotation for the spin ensemble, we project any magnetisation along _z_ onto the _xy_ plane. The rotating magnetisation in the _xy_ plane induces a current in the resonator, leading to a signal at the detector that oscillates at the same rate as the Larmor frequency of the ensemble. Due to the differing magnetic environments for each specific spin, there will be small offsets in their Larmor frequencies. We can see in Figure 2.9 how, in the rotating frame, this leads to a fanning out around the _xy_ plane. The ensemble magnetisation will therefore decay towards the centre of the Bloch sphere at a rate determined by the spread of frequencies in the ensemble. This therefore 

Pulsed ESR techniques 

35 



<!-- Start of picture text -->
a) D1 b) D2 c) b<br>170<br>171<br>173<br>d) e) f)<br>1<br>Site<br>2<br>Site<br><!-- End of picture text -->

Figure 2.8: EasySpin outputs of the energy levels for the Yb:YSO system, for both sites and with field applied along each crystal axis ( _D_ 1, _D_ 2, _b_ ). For a given site and field direction, there is also the possibility of a different ytterbium isotope. The _I_ = 1 _/_ 2 (<sup>171</sup> Yb) and _I_ = 0 (<sup>170</sup> Yb) isotopes are plotted in blue/red, respectively, for each combination. The energy levels for the _I_ = 5 _/_ 2 isotope (<sup>173</sup> Yb) are also plotted, but faintly to avoid confusion. The rich energy landscape and large hyperfine interaction leads to a number of possible ZEFOZ points. 

Pulsed ESR techniques 

36 



Figure 2.9: a) A Bloch sphere representation of free induction decay in the rotating frame. Due to the spread of frequencies within the ensemble, after an initial _fi/_ 2 rotation the individual spins fan out across the equator. This leads to _|Mxy|_ decaying exponentially at a rate given by 1 _/T_ 2<sup>_ú_.b)</sup><sup>_Mxy_asafunctionoftimeduringafree</sup> induction decay in the lab frame. The magnetisation continues to rotate at the Larmor frequency, but with decreasing amplitude. c) A projection of the _y_ -component of the magnetisation that would induce a voltage in the detector. Plotting _|Mxy|_ shows the decaying envelope of the oscillations. 

already encodes a lot of information about the spins coupled to the resonator, since the frequency of oscillation gives the Larmor frequency of the ensemble, and the rate at which the signal envelope decays tells us about the varying magnetic environments present in the sample. The decay rate of the magnetisation within the _xy_ plane, i.e. the transverse relaxation rate, is defined as: 



Where _T_ 2<sup>_ú_is the time that characterises the dephasing rate, and</sup><sup>_Mxy_(0) is the amplitude</sup> of the signal at _t_ = 0. Given that the frequency of the current induced in the resonator is given by the spin’s precession frequency, taking the Fourier transform of the FID gives the spectrum within the pulse’s excitation bandwidth. If the bandwidth of the pulse is wider than that of the spin ensemble it can be used to measure the spectral shape of the entire spin line. To optimally rotate spins and induce spin flips, we orient the microwave field _B_ 1 perpendicular to the constant field _B_ 0: this, however, means that the output signal is maximised when the spins are perpendicular to the _z_ -axis. This is a key difference compared to other measurement techniques where the readout is done directly along _z_ , an example of which is optically detected magnetic resonance (ODMR) where spin populations along _z_ are read out through laser excitation [57]. In this case, we infer the _z_ projection before the _fi/_ 2 pulse based on the amplitude in the _xy_ plane. The advantage of reading out in the 2D _xy_ plane compared to along the 1D line of the _z_ -axis means that more information can be encoded in the signal, both by its amplitude and phase. 

Pulsed ESR techniques 

37 



Figure 2.10: Description of the ‘Hahn echo’ pulse sequence. a) A diagram of the pulses used: a pulse with tip angle _fi/_ 2 is followed by the delay _·_ . The system is then refocused by a second pulse with twice the rotation angle. After a second _·_ delay, the echo is formed. b) Bloch sphere representation of the magnetisation; due to the constant field _B_ 0, the system is polarised along the positive _z_ -axis. The _fi/_ 2 pulse along _x_ rotates the magnetisation into _≠y_ . c) During the first free evolution time _·_ , spins with different Larmor frequencies will begin to de-phase at a rate given by 1 _/T_ 2<sup>_ú_.d)The</sup><sup>_fi_pulse</sup> along _x_ rotates the spins onto + _y_ . e) The same dephasing process causes the spins to re-align after another wait time _·_ , leading to an echo. Sweeping the delay time _·_ measures the spin coherence time _T_ 2. 

###### **2.5.2 Two pulse** 

The most common technique used in pulsed ESR is the Hahn echo sequence [58]. By using an initial _fi/_ 2 pulse followed by a refocusing _fi_ pulse the _z_ magnetisation of the spin ensemble can be measured at a time much longer than _T_ 2<sup>_ú_.Thisiscrucialsince</sup> the spectrometer dead time, the time after a pulse during which a signal cannot be detected, is often long compared to _T_ 2<sup>_ú_so much of the FID signal is lost.We can see how</sup> the magnetisation of different spins progresses throughout the sequence in Figure 2.10; the inversion from the _fi_ pulse causes the previously dephased spins to recombine _·_ after the pulse. By varying this delay we can allow the system to freely evolve for longer periods. Decoherence that is not refocused by the _fi_ pulse is characterised by the time _T_ 2. As a function of the time since the initial _fi/_ 2 pulse, the echo amplitude will be given by: 



_T_ 2 sets an upper bound on the time that information can be stored in the ensemble, since past this point the information is irretrievably lost to the environment. Due to imperfections in the excitation, combinations of two pulses will often lead to a signal at 2 _·_ [59]. When using more complex sequences with more than two pulses, the unwanted emission for each pair of pulses should be considered so as to avoid multiple echoes falling on top of each other. 

Pulsed ESR techniques 

38 





Figure 2.11: Combinations of three-pulse sequences used. a) Placing an initial pulse ( _◊_ ) before the Hahn echo sequence allows measurement of the Rabi frequency by sweeping the _◊_ pulse duration. b) Varying the time _T_ between an initial inversion _fi_ pulse and the Hahn echo sequence measures the longitudinal relaxation time _T_ 1. c) Using exclusively _fi/_ 2 pulses in the sequence places the magnetisation along _≠z_ during the long delay _T_ , allowing long interaction times with the local spin environment. 

###### **2.5.3 Three pulse** 

By including a third pulse in the sequence we can make more sophisticated sequences to extract more information from the system [58]; the sequence is shown in Figure 2.11. Placing a Hahn echo sequence after an initial pulse, means that the effect of that initial rotation on the _z_ magnetisation can be studied. The first example of this is by varying the duration of the initial _◊_ pulse. We can use this to calibrate how the duration of a pulse converts to a tip angle, sweeping this allows measurement of the Rabi frequency for the ensemble at that pulse amplitude. 



The second example is varying the time _T_ after a _fi_ rotation. This measures how quickly _Mz_ recovers after being inverted. As such, it is called an ‘inversion recovery’ sequence and is used to measure the characteristic longitudinal relaxation time _T_ 1. As a function of the time since the inversion pulse, _t_ , the amplitude will be given by: 



With _Mz_ ( _t æ Œ_ ) being the echo amplitude with the system in thermal equilibrium. If we instead play three _fi/_ 2 pulses as shown in Figure 2.11, the magnetisation can 

Pulsed ESR techniques 

39 

be parked along the _z_ -axis during the free evolution time _T_ . This then means that the ‘stimulated echo’ emitted after the final pulse decays at a rate given by _T_ 1. This allows a much longer time for the spin to interact with its local environment, since usually _T_ 1 _> T_ 2 . This then allows a more sensitive measurement of ‘Electron Spin Echo Envelope Modulation’ (ESEEM), where couplings to nearby nuclear spins can be extracted based on changes to the echo amplitude [60, 61]. 

###### **2.5.4 Adiabatic fast passage** 

A key disadvantage of planar superconducting microresonators, which were used in initial demonstrations of spin-based quantum memories, is that the microwave field they generate decays as one moves further from the resonator. This means that each spin will see a slightly different tip angle for a fixed pulse duration. To account for this variation, we can use ‘Adiabatic Fast Passage’ (AFP) pulses [62]. Here, the centre frequency of the pulse is varied throughout, changing the axis about which the spin rotates. If this is done slowly with respect to the Rabi frequency: 



where _◊_ is the angle between the _z_ -axis and the axis about which the spin is rotating and Ω _a_ is the Rabi frequency as defined above, the eigenstate can be adiabatically transformed from an initial to a final state. This process is inevitably slow compared to rectangular pulses, often requiring more than ten times the pulse duration; however in situations where the sequence is not time limited, these pulses allow for rotations that are robust to both _B_ 0 and _B_ 1 inhomogeneities. This means that an ensemble of spins, all with varying Larmor/Rabi frequencies ( _B_ 0/ _B_ 1, respectively), can be rotated with high fidelity. Within this work, ‘Wideband Uniform Rate Smooth Truncation’ (WURST) pulses are regularly used in place of _fi_ pulses for just this reason. The amplitude and frequency of WURST pulses as a function of time follow [63, 64]: 



Where _A_ ( _t_ ) and _f_ ( _t_ ) the amplitude and frequency shapes. _A_ 0 is the peak amplitude, _T_ pulse is the total duration, _N_ is a factor that determines the smoothing of the amplitude modulation, _f_ 0 is the centre frequency, and ∆ _f_ is the frequency span. The issue with using these pulses in place of rectangular _fi_ pulses is that we no longer retain the same refocusing condition as was found in the Hahn echo sequence; this is 

Decoherence 

40 

illustrated in Figure 2.12. We therefore have to apply a pair of WURST pulses to generate an echo [65]. This means that the equivalent Hahn echo sequence, when using a non-chirped _fi/_ 2 initial pulse, is now a three-pulse sequence. 

###### **2.5.5 Including low-frequency pulses** 

A typical nuclear gyromagnetic ratio is three orders of magnitude smaller than that of a free electron; this means that the same resonator cannot be used to read out both the nuclear and electron spin states. We therefore use ‘Electron Nuclear Double Resonance’ (ENDOR) to infer changes in the nuclear spin populations through the electron spin [67]. Because of the large difference in energy splitting, the increased polarisation of the electron spin state leads to a much larger signal than would be found by measuring the nuclear spin directly. The sequence is shown in Figure 2.13 where an initial inversion on the electron spin precedes a pulse at the Larmor frequency of the nuclear spin, _fin_ . Since the effective polarisation on the transition resonant with the resonator is now zero, a Hahn echo sequence played directly after _fin_ will not produce an echo. We can then simply sweep the frequency of _fin_ in sequential measurements to spectroscopically resolve the nuclear spin transition. By sweeping the duration of _fin_ , we can also determine the nuclear Rabi frequency. Since it is often the case that: 



Where _T_ 1<sup>_e_/</sup><sup>_T_</sup> 1<sup>_n_aretheelectron/nuclearlongitudinalrelaxationtimes,thesemeasure-</sup> ments can become prohibitively slow if one has to wait for the nuclear spin to relax between subsequent measurements. In this case, we apply a second _fin_ pulse after the Hahn echo sequence. This so-called ‘Tidy’ pulse will reset any changes to the nuclear spin state so we need only wait _≥O_ ( _T_ 1<sup>_e_) between measurements for the system to reset</sup> [68]. 

#### **2.6 Decoherence** 

To understand the mechanisms that drive _T_ 2 decay in ensembles, we consider a ‘central’ spin at resonance as shown in Figure 2.14. We can then assess how the varying magnetic environment leads to decoherence of the central spin. The mechanisms that drive transverse relaxation ( _T_ 2) can then broadly be split into two categories, often termed ‘ _Sz_ ’ and ‘ _Sx_ ’. If the noise term leads to a change in the Larmor frequency of the central spin, then it will appear in the Hamiltonian of this spin with an _Sz_ operator. However, if the term causes changes to the state of the central spin, e.g. from the excited state to the ground state, then it will enter through an _Sx/Sy_ term. Both lead to decoherence; 

Decoherence 

41 







Figure 2.12: a) Bloch sphere snapshots during a 10 µs square pulse with a 5 MHz linear chirp. The trajectory is plotted in a frequency modulated reference frame that keeps the phase of the chirped pulse stationary. The momentary effective field orientation _Ê_ eff (blue) sweeps from the north to the south pole of the Bloch sphere. The magnetisation (purple) rotates around this effective field, with the more recent trajectory shown in a darker colour. In the adiabatic limit the magnetisation is swept smoothly from one pole to the other, directly following _Ê_ eff [66]. b) The refocusing condition for a three pulse echo sequence using WURST pulses. During the WURST pulse, spins with different frequencies are inverted at different times. A spin at _≠_ 1 MHz (red) will be inverted before one at +1 MHz (cyan). This leads to different effective _·_ s and no echo after the first inversion. A second WURST pulse cancels this difference, leading to all frequencies being refocused at the same time and producing an echo. The final delay, _·_ 3, will be given by _·_ 3 = _·_ 2 _≠ ·_ 1. 

Decoherence 

42 



Figure 2.13: Population transfer during an ENDOR experiment for an _S_ = 1 _/_ 2, _I_ = 1 _/_ 2 system. Nuclear spin orientation is labelled _«_ and electron spin is labelled _ø_ . a) Typically, the electron spin state is polarised whereas the nuclear spin state is not. b) A selective microwave inversion pulse moves population into the excited electronic state. c) If the RF pulse selectively drives the electron-ground-state NMR transition, then there is no population difference and so no echo. d) If both transitions are driven, then the echo has positive amplitude. e) Simulated ENDOR spectrum for different RF pulse bandwidths. The actual NMR transition linewidths are assumed to be narrowed compared to the pulse. If the RF frequency is away from the transitions, the echo remains inverted. If the pulse bandwidth is wide enough to drive both transitions simultaneously, we measure increased contrast in the spectrum. 

Decoherence 

43 





















Figure 2.14: Central spin model to understand decoherence mechanisms, labelled with the Hamiltonian term relevant to the central spin. DFF) Direct flip-flops happen when the central spin exchanges spin state with a nearby resonant spin; this interaction is not decreased at the clock transition. SD) Spectral diffusion is the process through which dipolar couplings to nearby spins with changing spin states leads to the central-spin dephasing. These can either be other donor electron spins (red) or nuclear spins (purple). External spin pairs can exchange spin state through a flip-flop process, indirect flip-flops, or decay through longitudinal relaxation ( _T_ 1). ID) Instantaneous diffusion occurs due to the dipolar coupling between two resonant electron spins. If both spins are inverted by the _fi_ pulse, this interaction is not reversed during the second _·_ , and so leads to an increased transverse relaxation rate. 

however, this distinction is key since, as we saw above, the spin systems used in this work have ZEFOZ points at particular locations in frequency and field. Since the spin becomes insensitive to magnetic field fluctuations at these points, any _Sz_ noise term will be effectively turned off. This leaves the resonant spin only sensitive to noise from _Sx_ -type interactions. 

###### **2.6.1 Spectral** 

Spectral (SD) comes from a range of sources, but collects the noise terms that arise from fluctuating fields in the presence of the central spin. Since the relevant terms in the central spin Hamiltonian are _SzSz_ and _SzIz_ it can be suppressed at a ZEFOZ point. Given that it only appears due to spins that are not involved with generating the echo the increase in decoherence rate from spectral diffusion is proportional to _|_ d _f/_ d _B|_ . 

###### **2.6.2 Instantaneous** 

Instantaneous (ID) is the process by which one nearby resonant spin detunes the central spin. If, during the Hahn echo sequence, both spins are inverted by the 



<!-- Start of picture text -->
15<br>10<br>N<br>T<br>=<br>5<br>—<br>59<br>% 30 60 90<br>Nominal 3 (deg)<br><!-- End of picture text -->



<!-- Start of picture text -->
10 . — :<br>7GHz<br>a<br>3.6x10" _ 9 “= 1 9.75 GHz<br>cm “Cop 8), dFF<br>® EEE ett inineieiel Sit itil Refit<br>44x10 Sy<br> cm™3 RN<br>CR LSSFF<br>WN _ 6 ry LA<br>Ta WW<br>0014 S 2 | 3<br>0:<br>01 2 3 4 5 :<br>Concentration (10> cm™3) '<br>1073 1072 107! 1<br>|df/dBJ (y.)<br><!-- End of picture text -->

Relaxation 

46 

rates increase with increasing temperature. The simplest is the direct process, where a phonon directly matches the energy of the transition and so allows relaxation. This scales as [71]: 



Where _–D_ is a spin system dependent coupling factor, _g_ is the ensemble g factor, _kB_ is the Boltzmann constant, ∆ _E_ is the energy of the transition and _T_ is the temperature. 

The Orbach process is a two-phonon process whereby relaxation is allowed through a real intermediate state; the rate scales as [72]: 



Where _–O_ is again a constant coupling factor and ∆ _O_ is the energy of the intermediate transition. 

The Raman process is similar to the Orbach process; however, the intermediate energy level is now a virtual one. In the case of Kramers ions [73]: 



For bismuth donors [34]: 



Where _–R_ again is a coupling constant. 

Due to the millikelvin temperatures used in this work, the direct process, which dominates at low temperatures, will be the main cause of spin-lattice relaxation. 

###### **2.7.2 Spin-spin relaxation** 

As we saw for decoherence, nearby resonant spins can interact with each other through a flip-flop process. For high spin concentrations, this can also become relevant for changes to the longitudinal component of the magnetisation, e.g. _|Mz|_ . Since this is typically an _Mz_ -preserving interaction, for it to be relevant to _T_ 1, it requires that the excitation systematically does not excite a sub-ensemble that is close in frequency to the excited one. This can be the case if the excitation is spectrally narrower than the ensemble’s inhomogeneous linewidth. The temperature dependence of this relaxation rate is given by [74]: 



Where _–_ dFF is the coupling constant, _n_ is the spin concentration and _“_ is the inhomogeneous spin linewidth. 

# **Chapter 3** 

# **Superconducting resonators** 

Given the arguments laid out in Chapter 1, we plan to couple the electron spin ensemble to a superconducting microresonator to achieve a large coupling rate, small mode volume, and high quality factor. This also allows for a fully on-chip design that can be easily integrated with many superconducting qubit architectures. To understand the physics and design of these resonators, we start from a basic circuit theory model and work towards a full circuit quantum electrodynamics (cQED) model that allows the mathematical description of a resonator interacting with a spin system. 

#### **3.1 The lumped element circuit theory model** 

A general circuit component will have impedance 



where _Z_ is the complex impedance, _R_ is the resistance, _i_ is the imaginary unit<sup>1</sup> , and _X_ is the reactance. Since in this work the resonators are made from a superconductor they will have zero resistance. This means that the entirety of the impedance will be given by the reactance _X_ . The most basic description of a resonator is a circuit with an inductor and capacitor in series, as shown in Figure 3.1. The impedances of ideal capacitors and inductors as a function of frequency are: 





where _L_ & _C_ are the inductance and capacitance of the inductor and capacitor respectively, _ZL_ & _ZC_ are their complex impedances, and _Ê_ is the drive frequency. The total 

> 1This is as opposed to the standard convention in engineering where the imaginary unit is written _j_ . 

47 

The lumped element circuit theory model 

48 



Figure 3.1: a) Diagram of a lumped element LC circuit with the inductor and capacitor labelled. We do not include a series resistance since the circuit will be superconducting. b) The frequency dependence of the circuit impedance using: _C_ = 1 pF, _L_ = 1 nH, and _Z_ 0 = 75 Ω. At resonance ( _Ê_ = _Ê_ 0) the inductor and capacitor impedances directly cancel leaving only the characteristic impedance _Z_ 0. 

impedance of these components in series is then: 



Where we have included a residual frequency-independent term _Z_ 0, to represent frequencyindependent losses. To find the minimum impedance as a function of frequency we take the derivative of _|ZT |_ and set it equal to zero: 



Thus, at the resonance frequency: 



or: 



The lumped element circuit theory model 

49 

where _Ê_ 0 and _f_ 0 are the angular and linear resonance frequencies of the resonator, respectively. We can compute the impedance at resonance: 







If we imagine that the resonator is not formed from lumped element components, but from a resonant section of a coplanar waveguide, then at resonance the impedance of the waveguide resonator is given by the characteristic impedance of the waveguide. Using the characteristic impedance of a transmission line [75]: 



Where _R_ and _L_ are the resistance and inductance per unit length of the line, and _G_ and _C_ are the conductance and capacitance to the outer conductor. For a superconducting waveguide with a perfect dielectric, _R_ = 0 and _G_ = 0, so this reduces to: 



By analogy, we can therefore relate the residual impedance at resonance of the lumped element resonator to the characteristic impedance of a transmission line with zero resistance. In this case, the frequency independent impedance of a lumped element superconducting resonator is given by equation 3.13. 

Given that the microwave frequency will be by the transition frequency of the electron spin and the resonant frequency depends on the product of _L_ and _C_ (equation 3.8), we cannot freely choose their values, but we can still vary their ratio as long as the product stays fixed. This means that, for applications requiring high impedance, where coupling is done via the electric field, one should choose a large inductance and small capacitance. Here, we are coupling to the electron spins through the magnetic field generated by the inductor. From Ohm’s law ( _V_ = _IZ_ ), the current increases for decreasing impedance, so for this work we deliberately design resonators with large capacitors and small inductors. This minimises the characteristic impedance and maximises the generated field. 

<u>Quality</u> factor 

50 

#### **3.2 Quality factor** 

The quality factor (Q factor) characterises the rate at which a resonator loses energy. It is as: defined 



where _Ê_ 0 is the centre frequency of the resonator, as above, and ∆ _Ê_ is the resonator bandwidth. The bandwidth here is defined as the full width at half maximum (FWHM) of the resonator power spectrum. To illustrate this we consider a cavity with _n_ 0 photons at time _t_ = 0 and a loss rate _Ÿ_ with units of _s_<sup>_≠_1</sup> . It follows that, as photons begin to leak out of the cavity, we should find: 



Where _n_ ( _t_ ) is the number of photons in the cavity at a time _t_ , and d _n/_ d _t_ is the rate of change of _n_ . We then find: 



This exponential decay is called resonator ‘ringdown’ or ‘ringing’, in analogy to a bell that continues to make sound after being struck despite the initial excitation having finished. We also find a similar effect when trying to add photons to the cavity, termed ‘ringup’. The finite coupling rate leads to the resonator resisting changes to photon number. We can then write down the field leaving the cavity for _t >_ 0: 



with _a_ ( _t_ = 0) = _a_ 0. Here, the square root comes from converting from power to voltage using _P Ã V_<sup>2</sup> . By taking the Fourier transform, we can determine the cavity spectrum 2 : 







> 2For this work, we choose the Fourier transform convention: 



<u>Quality</u> factor 

51 

In power, the spectrum is therefore given by: 



This is a Lorentzian centred on _Ê_ 0 with FWHM _Ÿ_ , meaning that the cavity bandwidth ∆ _Ê_ is simply equal to its loss rate _Ÿ_ . We can then relate the loss rate and Q factor by: 



It is useful at this point to make a distinction between two broad categories of losses: coupling losses ( _Ÿc_ ) and intrinsic losses ( _Ÿi_ ). We define _Ÿc_ to be energy transferred out of the resonator due to its coupling to the measurement setup. Inevitably, to characterise a resonator, we must have some way to probe it, and introducing this probe allows a new way for energy to couple into and out of the resonator. _Ÿi_ then characterises all other loss mechanisms of the cavity, including radiative losses, coupling to local two-level systems (TLS), and the material loss tangent. The total resonator loss rate is then simply: 



where _Ÿl_ is the ‘loaded’ or total loss rate of the resonator. loaded, coupling, and intrinsic Q factors ( _Ql_ , _Qc_ , and _Qi_ ). It then follows that: 



or: 



For _Qc ∫ Qi_ , termed ‘undercoupled’: 



whereas for _Qi ∫ Qc_ , termed ‘overcoupled’, _Ql_ is dominated by _Qc_ . In both cases, the cavity bandwidth is dominated by the smaller Q factor. Due to these different rates, photons will couple out with a different branching ratio based on their relative amplitudes. Since the field is only measured if it ends up at the detector, we must be careful that a spin signal within the cavity is not dissipated exclusively by _Ÿi_ losses. If _Ÿi ∫ Ÿc_ , the measured signal will be negligible. We therefore define the directivity _D_ : 





Coupling an electron spin to an LC resonator 

52 

This determines the fraction, in power, of a signal within the resonator that will couple out into the measurement setup. This assumes that the power in the resonator during emission is initially independent of _Ÿc_ , and that these _Ÿ_ values are constant throughout excitation and emission. Within these assumptions, however, we want to make _D_ as close to one as possible in order to maximise signal. 

#### **3.3 Coupling an electron spin to an LC resonator** 

We now consider coupling the superconducting resonator to a single electron spin. The resonator can be described as a harmonic oscillator with frequency _Ê_ 0: 



where _Ê_ 0 is the photon frequency and _a_ ˆ<sup>_†_</sup> _/a_ ˆ are the creation/annihilation operators referring to adding/removing photons from the cavity. If a static magnetic field ( _B_ 0) is applied to the electron spin, then it can be modelled as a two-level system with transition energy ~ _Ês_ : 



where _Ês_ is the Larmor frequency due to the _B_ 0, and _‡_ ˆ _z_ is the Pauli _z_ operator. The combined system can then be written as: 



where _H_ int is a term that describes their interaction. Due to vacuum noise, small current fluctuations will be induced in the resonator inductor [76]: 



where _”I_ is the current generated by the vacuum state. From the Biot–Savart law [77], we know these will generate a magnetic field proportional to the current: 



Considering this driving to be their interaction, we can write down _H_ int using equation 2.15: 



ˆ where **_µ_** = _≠“e_ **_S_**<sup>ˆ</sup> , with **_S_**<sup>ˆ</sup> =<sup><u>~</u></sup> 2<sup>**_‡_**,where</sup><sup>**_‡_**arethePaulimatrices(</sup><sup>_‡x, ‡y, ‡z_).</sup><sup>**_B_**ˆisnow</sup> an oscillating field with frequency _Ê_ 0 due to vacuum-state fluctuations. Assuming the resonator field is oriented perpendicular to _B_ 0, i.e. along the _x_ -axis, the field due to 

Coupling an electron spin to an LC resonator 

53 

these can be quantised: 



**ˆ** where _”Br_ is the magnitude of the at distance _r_ and **_x_** is a unit vector pointing in the _x_ -direction. The interaction term then becomes: 





Here we used the identity _‡x_ = _‡_ + + _‡≠_ . We can, however, make some to make this solvable. If we consider all four terms present we find in the interaction picture: 







the spin-resonator detuning ∆ _© Ês ≠ Ê_ 0, we are only interested in the dynamics close to resonance, where the detuning is small: 



ˆ ˆ ˆ ˆ This means that the terms _‡_ + _a_<sup>_†_</sup> and _‡≠a_ , where _Ês_ and _Ê_ 0 have the same sign, will rotate much faster and so average to zero. This is the same as the assumption in Chapter 2, where we neglected the counter-rotating terms with frequency 2 _Ê_ due to their fast oscillation with respect to the rotating frame. These terms refer to simultaneous excitation/de-excitation of both the spin and resonator, and so are non-energyconserving. In the limit that the coupling rate between the spin and resonator is significantly smaller than their respective frequencies, these terms can safely be neglected. This is referred to as the ‘rotating wave approximation’ (RWA) and leaves us with: 



The is to consider the matrix element: 



Coupling an electron spin to an LC resonator 

54 

Where _|¿,_ 1 _Í_ is the state with a single photon in the resonator mode and the spin in its ground state, and _|ø,_ 0 _Í_ is the spin-excited state with no photons in the resonator. Evaluating this gives the coupling _g_ 0 (units s<sup>_≠_1</sup> ) between the two systems due to vacuum fluctuations: 



This gives the Jaynes–Cummings Hamiltonian [78]: 



ˆ ˆ Given that the total excitation number _N_ = ˆ _a_<sup>_†_</sup> _a_ + ˆ _‡_ + _‡≠_ is conserved under the RWA, we can separate the Hamiltonian into _N_ different manifolds that can be diagonalised separately. We consider the two states with constant _N_ , _|e, n ≠_ 1 _Í_ and _|g, nÍ_ , where _e/g_ are the excited/ground states of the electron spin and _n_ is the occupation number of the resonator. The Hamiltonian then becomes: 



This has eigenvectors: 





Where we have introduced the mixing angle _◊n_ , with: 



The respective eigenvalues are: 



The transition frequencies between the _n_ = 0 and _n_ = 1 states are then: 



We see these transition frequencies as a function of in Figure 3.2. For large 

Coupling an electron spin to an LC resonator 

55 



<!-- Start of picture text -->
E +<br>E−<br>ωs<br>ω 0<br><!-- End of picture text -->

Figure 3.2: Solutions to the Jaynes–Cummings Hamiltonian as a function of for _Ê_ 0 = 7 GHz, _Ês_ = _“eB_ 0, and _g_ 0 = 10 MHz. The spin-resonator coupling _g_ 0 causes an avoided crossing with gap 2 _g_ 0 at ∆= 0. The two polariton branches ( _E±_ ) mix the originally distinct spin/resonator states. 

detunings (∆ _∫ g_ 0 eigenstates of the individual systems. As ∆decreases, these become invalid and we find the new eigenstates to be superpositions of the resonator-excited and spin-excited states. At ∆= 0, the separation between _E_ + and _E≠_ becomes 2 _g_ 0; this is vacuum Rabi splitting and is a characteristic signature of strong coupling between the resonator and spin. At zero detuning, if we put a single photon into the combined system, the probability of finding the resonator excited and the spin in its ground state at a time _t_ is: 



Thus, the photon oscillates between the resonator and spin due to this coupling frequency _g_ 0, giving rise to the new eigenstates for the combined system. These oscillations are termed ‘vacuum Rabi oscillations’. 

###### **3.3.1 Spin-resonator coupling** _g_ 0 

We saw above that the coupling _g_ 0 between the resonator and spin is the product of the spin’s gyromagnetic ratio and the magnitude of the field due to vacuum fluctuations. We can consider what this might be for a realistic geometry. For a straight wire, the 

Coupling an electron spin to an LC resonator 

56 

radial dependence of the magnitude of the magnetic is [77]: 



Where _µ_ is the permeability of the material, _I_ is the current in the wire, and _r_ is the radial distance from it. This approximation is often close for lumped element superconducting resonators, due to the narrow and straight inductor geometry. If the constant field _B_ 0 is then applied parallel to the wire, _g_ 0 for an electron spin at radius _r_ can be directly calculated: 



This is a useful result since it directly shows that, for a given frequency, the only free parameters to tune the spin-resonator coupling are the resonator impedance and the spin-resonator distance. We therefore endeavour to engineer low-impedance resonators with a small spin-resonator distance. For a 7 GHz resonator with characteristic impedance _Z_ 0 = 100 Ωcoupled to a free electron at a distance of 400 nm, typical parameters for experiments in this work, we can calculate the spin-resonator coupling frequency: _g_ 0 _/_ 2 _fi ¥_ 200 Hz. Since this is much smaller than both the resonator and spin loss rates, it represents a very small coupling. Fortunately this can be enhanced by coupling to an ensemble of many spins. 

###### **3.3.2 The Tavis–Cummings model** 

We can extend the Jaynes–Cummings model derived above to allow for many spins coupling to the same resonator. For an ensemble of _N_ identical spins, the spin Hamiltonian term becomes 



Using the same RWA approximation made above, we can write down the new interaction Hamiltonian for all of the spins in the ensemble. Since they are identical, they will all have the same coupling frequency _g_ 0, and the new term becomes: 



Coupling an electron spin to an LC resonator 

57 

This gives the Tavis–Cummings Hamiltonian [79]: 



To understand how an ensemble of spins enhances the coupling, we again consider the matrix element between a photon in the resonator and a single excitation in the spin ensemble. The difference in this case is that, due to the electron spins being indistinguishable, our excitation is now stored as a superposition across all spins. This so-called Dicke bright state [80], _|W Í_ , can be written: 



Where the factor of 1 _/ÔN_ is required for normalisation. The ground state of the spin ensemble is simply: 



Using the collective spin operators: 



we the relation: 



We can now evaluate the same matrix element as before for the ensemble case: 







With _g_ ens the coupling between the resonator and the entire ensemble. The coupling _g_ 0 is enhanced by a factor _ÔN_ compared to the individual case. For an electron spin ensemble with concentration 10<sup>16</sup> cm<sup>_≠_3</sup> and a volume of 10 pL (10<sup>_≠_8</sup> cm<sup>3</sup> ), the approximate number of spins is _N_ = 10<sup>8</sup> ; this leads to an ensemble coupling frequency _g_ ens _/_ 2 _fi ¥_ 2 MHz. This is now significant compared to characteristic spin and resonator loss rates. If the spins have different couplings, we can calculate the ensemble coupling 

Coupling an electron spin to an LC resonator 

58 

strength using: 



where _gj_ is the coupling strength _g_ 0 of the _j_<sup>th</sup> spin. This reduces to _g_ ens = _g_ 0 _ÔN_ if all spins have the same coupling. 

###### **3.3.3 Cooperativity** 

As we saw previously, the vacuum Rabi frequency at zero detuning was Ω= 2 _g_ 0. We therefore define a characteristic parameter, the ‘cooperativity’, that compares the loss rates of the combined spin-cavity system to the coupling between them: 



where _Ÿl_ & Γ are the full widths at half maximum of the resonator & spin system. Here, it is implicit that all spins have the same coupling strength. There are broadly three cooperativity regimes to consider: 

- **_C <_ 1** : This is the low-cooperativity regime and is the case for most traditional 3D cavity ESR measurements. Here, cavity and spin losses dominate over the coupling _g_ ens, so there is no vacuum Rabi splitting visible. In analogy to a damped harmonic oscillator, the frequency of oscillation, due to _g_ ens, is much smaller than the damping, due to _Ÿl_ & Γ, and so no oscillations are completed before all of the energy is dissipated. 

- **_C_ = 1** : At unit cooperativity, the system losses are balanced with the spinresonator coupling. This is analogous to critical damping or perfect impedance matching and allows ideal energy transfer into the spin ensemble. At _C_ = 1, and in a steady state, using the resonator to drive the spin ensemble, or vice versa, will produce no reflections, allowing perfect absorption [33]. This point is therefore crucial for operating a high-efficiency quantum memory since it allows lossless transfer of photons into and out of the memory. 

- **_C >_ 1** : This is the high-cooperativity regime, where the spin-resonator coupling dominates the system loss. In analogy to the underdamped harmonic oscillator, many oscillations can be completed before all of the energy is lost to _Ÿl_ & Γ. A special case within _C >_ 1 is where _g_ ens _∫ Ÿl,_ Γ; this is the so-called ‘strong coupling’ regime, where one can clearly resolve vacuum Rabi splitting in the spectrum. 

Coupling an electron spin to an LC resonator 

59 

Given that, in this work, Γinhom _∫ Ÿl,_ Γhom, where Γinhom & Γhom are the inhomogeneous & homogeneous spin linewidths, respectively, the relevant spin linewidth for the calculation becomes that of the spins that are coupled to the resonator, which will therefore be limited by _Ÿl_ , or: 



where Γeff is the linewidth of the spins coupled to the resonator. Varying Γeff will also change the number of spins coupled to the resonator, _N_ coupled, and so _g_ ens. For the simplest case, a uniform spin spectral density, the number of coupled spins can be easily calculated: 



where _N_ tot is the total number of spins in the ensemble. In this case, we can rewrite the cooperativity: 





This situation is very unlikely, but it does illustrate that, despite the resonator only coupling to a sub-ensemble of spins within the line, the cooperativity is still dependent on the total linewidth. In reality, _N_ coupled will vary based on the resonator and spin spectral densities [81]: 



where _÷_ ( _Ê_ ) and _fl_ ( _Ê_ ) are the resonator & spin spectral densities, such that: 



A typical inhomogeneously broadened spin line will be Gaussian in shape: 



where _Ês_ is the spin ensemble centre frequency, and _c_ = Γ _/_ (2 _Ô_ 2 ln 2). Given that Γinhom _∫ Ÿl_ , we can approximate _fl_ ( _Ê_ ) as constant within the resonator bandwidth, with value _fl_ ( _Ê_ = _Ê_ 0). If we assume a Lorentzian resonator lineshape, we can then 

Coupling an electron spin to an LC resonator 

60 

compute: 







Using _÷_ max = 2 _/_ ( _fiŸl_ ) and the normalisation conditions above. Given that the spin centre frequency is field-dependent, it can be used to change the spin-resonator detuning: 



The number of coupled spins, and so the cooperativity, can then be tuned simply by varying their detuning: 



The narrow resonator bandwidth has picked out the spin lineshape, meaning that the cooperativity has the same shape as the spin spectral density. The maximum cooperativity is then: 



a factor _Ôfi_ ln 2 larger than the uniform-density case. We can now calculate the expected cooperativity assuming some typical experimental parameters: _g_ 0 _/_ 2 _fi_ = 200 Hz, _N_ tot = 10<sup>8</sup> , Γ _/_ 2 _fi_ = 1 MHz, _Q_ = 10<sup>5</sup> , and _Ê_ 0 _/_ 2 _fi_ = 7 GHz. The peak cooperativity would then be: 



This is high enough to reach the critical _C_ = 1 point, required to operate a highefficiency quantum memory. 

###### **3.3.4 Purcell decay** 

A by-product of coupling a two-level system, in this case an electron spin, to a high-Q cavity is that the enhanced density of states leads to a new relaxation mechanism. This 



<!-- Start of picture text -->
108 og<br>102 /<br>©<br>~<br>101<br>100<br>4 4 2 4 0 1 2 3 4<br>8/2m) (MHz)<br><!-- End of picture text -->



<!-- Start of picture text -->
10<br>102 T008E{ ) SLAC(8©. @)OO 75As3p<br>10° Yee 121g<br>8 Rao O  209Bj<br>210 5 Zo w==+ Fit<br>= ©<br>5 NN<br>10% ENNN\<br>h "ie,<br>10975-8 5 10 20<br>Temperature (K)<br><!-- End of picture text -->

Coupling an electron spin to an LC resonator 

63 

SNR to be: 

SNR per second _Ã_ Number of averages per second _·_ Signal per echo _._ (3.92) 

Assuming we are Purcell limited, the number of averages per second will be proportional to the Purcell rate Γ _P_ . The signal per echo for optimal _Ÿc_ considerations can be broken down into three terms: the power fraction that couples out of the resonator, given by _D_ ; the total echo power, _P_ echo; and the echo duration, _TE_ . The signal per echo is then: 



Given that we are in the limit that _Ÿl π_ Γ, we make the approximation that the excitation bandwidth is resonator limited, so: 



The echo power is then given by [80]: 



We make the same spectral density approximation used above, since this will only change the result by a constant factor. The coupling-dependent SNR will then be given by: 





This reaches its maximum value at _Ÿc_ = _Ÿi_ . This also assumes that a perfect _fi/_ 2 excitation pulse can be achieved for any value of _Ÿc_ . However, since it also peaks at the critical coupling point _Ÿc_ = _Ÿi_ where power transfer into the resonator is maximised, this should not be an issue. We note that this also changes if the resonator is not in a reflection-type geometry, where the only external coupling is due to _Ÿc_ . For a transmission-type setup with two coupling-type losses, _Ÿc,_ in and _Ÿc,_ out, we would need to optimise for both. Given the above derivation, we see a contrast with the cooperativity which is maximised as _Ÿc æ_ 0. 

# **Chapter 4** 

# **Experimental Methods** 

The work in this report details cryogenic spin-control measurements made using bespoke, micron-scale, planar, superconducting microwave resonators. This chapter details all the equipment and processes used for making these measurements. This includes the cryogenic systems used and their operating principles; the design, manufacture, and testing of the microresonators; and the equipment for making measurements at microwave frequencies. 

#### **4.1 Cryostats** 

All of the measurements in this thesis were required to take place at cryogenic temperatures. There are broadly two types of measurements that needed to be made. The first is resonator testing and frequency calibration. This only requires that the resonator be superconducting, typically achieved at a few kelvin depending on the material; for this reason, it is excessive to cool the design down to the millikelvin (mK) regime simply for testing. The second type of measurement is spin-dependent measurement. As we saw in §3.3.5 the signal is strongly dependent on the spin polarisation, which in turn depends on the temperature. For these measurements, we therefore often want to be as cold as possible, with little concern about the time taken to cycle between samples. For this work, we therefore used two types of cryostat: a closed-loop flow cryostat and a dilution refrigerator. The first allows rapid cooling of devices down to _<_ 2 K for fast turnaround testing. The second operates down to _<_ 25 mK for high spin polarisation and optimal SNR, at the cost of a longer turnaround time. 

###### **4.1.1 Pulse Tube Cryocoolers** 

A common subsystem used in both types of cryostat is the pulse tube refrigerator. It is a variant of the ‘Stirling engine’ [84] that takes advantage of cyclic thermodynamic processes to pump heat from a cold plate to a hotter one. We can see in Figure 4.1 the 

64 

Cryostats 

65 



Figure 4.1: The thermodynamic processes used within a pulse tube cryocooler. Mechanical compression allows thermal energy to be moved from a cooler body to a hotter one. Panel a) shows a schematic of the process, panel b) shows the same process in the _PV_ plane. 1) A compressible volume between two baths thermalises with the cool one whilst expanded. 2) The volume is compressed, increasing the internal temperature. 3) The volume thermalises with the warm bath, decreasing its temperature. 4) The volume is expanded, decreasing its internal temperature. It can be re-thermalised with the cool bath, starting the cycle again and cyclically moving energy from the cool bath to the warm one. 

steps of the process, which boil down to compressing a gas in one location, moving it to a new location, and then letting it expand. The compression step heats the hot plate, which is often itself cooled by another coolant that prevents overheating. The compressed gas can then be allowed to expand next to the cold plate, taking in heat. This process can be continuously repeated, cooling the cold plate down as low as 2 _._ 2 K [85]. In a pulse tube refrigerator specifically, the compression and expansion are not controlled by a mechanical pump, but by pressure waves sent down flux lines. 

###### **4.1.2 Closed Loop Flow Cryostats** 

A closed-loop cryostat cools by pumping liquid helium past the device under test (DUT). The term ‘closed loop’ refers to the fact that this is a cyclic process in which the same helium is used continuously and recondensed before being used to cool again. At atmospheric pressure, helium-4 (<sup>4</sup> He) condenses into a liquid at _≥_ 4 _._ 2 K [86]; this means a sample could be submerged in a dewar of liquid helium and cooled down to this temperature. To go below this temperature, we must pump the liquid helium in such a way that it evaporates back into a gas around the DUT; the changing phase of low-pressure<sup>4</sup> He allows cooling below 2 K. The used helium gas is then recondensed by a pulse tube refrigerator, allowing it to be immediately reused for sample cooling. The continuous loop allows consistent cooling over long time periods without needing to resupply the coolant. 



<!-- Start of picture text -->
2.0<br>V<br>I Xo 4;<br>| Ze normal 3 "He/"Heged<br>superfluid<br>15 | ‘Hel'He<br>T/IK I<br>dilute<br>I<br>1.0 | co<br>tricritical<br>) w® point<br>/ ad200°<br>Tes/ | )<br>0.5 | 9°<br>two-phase region<br>0 0.25 0.50 0.75 1.00<br>He concentration X3<br><!-- End of picture text -->

Cryostats 

67 









Figure 4.3: A picture of the Bluefors LD400 dilution refrigerator used for this work. The system has a vector magnet (not shown) for applying global fields to the spin ensemble. The sample is placed in a puck that is inserted mechanically into the bottom of the refrigerator, allowing the majority of the system to stay cold during sample changes. 

The<sup>3</sup> He evaporates before the<sup>4</sup> He in the mixture, allowing only<sup>3</sup> He to be pumped back around the loop for continuous circulation. This cryogen-free and circular design allows for indefinite cooling without wastage of non-renewable cryogens. 

The Bluefors LD400 system used for these experiments, this one named ‘Leela’, depicted in Figure 4.3, has 400 mW of cooling at the 4 K plate and _≥_ 15 µW at 20 mK for the sample stage [89]. This means that, when designing experiments, an important consideration is the heat load on the various cooling stages of the fridge. Typical setups have attenuators on the input lines and amplifiers on the outputs; these can all lead to heating that may overwhelm the cooling power if the setup is poorly configured. This is an important consideration, particularly for experiments that require the use of many different control and readout signals. For quantum technologies to be truly 

Resonator development 

68 

scalable, this is a barrier that must be addressed. 

The fridge used for these measurements also includes a bottom-loading system. The sample is placed inside a ‘puck’, a cylindrical metallic capsule with push-fit connectors on the top. The puck is then placed on a motorised insertion mechanism that uses a load-lock system to insert the puck into the main body of the fridge without introducing excess air. This setup, allows the sample to be changed without warming up the entire cryostat. This allows new samples to be cooled down overnight, whereas cooling the entire apparatus would take two days. 

magnet. Three pairs of Helmholtz coils are arranged orthogonally to one another around the sample [90]. By specifying the current in each pair of coils, the magnitude and direction of the field at the sample can be selected. The coil pair aligned with the _z_ axis is optimised for higher currents, allowing the generation of a larger field magnitude. This means that fields of up to 1 T can be applied in an arbitrary direction, or up to 3 T when the field is aligned with the _z_ axis. 

#### **4.2 Resonator development** 

Below, we detail the process used for all of the silicon devices measured in this report. The resonators used for the Yb:YSO measurements were made by Dr. J. Alexander [91] using a similar procedure. To go from a resonator concept to a working device is a non-trivial process requiring substantial design, simulation, and testing. The workflow used for taking a resonator concept into a real device was: 

1. the resonator geometry in Python. 

2. Simulate the design using a solver. 

3. the fabrication recipe. 

4. Make test devices for frequency calibration. 

5. Fabricate the device on a spin sample. 

This is often not a linear process and requires iterative repetition of subsets of the above steps. 

###### **4.2.1 Design and simulation** 

The Python module ‘gdspy’ [92] provides a convenient way to convert from an arrangement of points defined in Python into a graphic design system II (GDSII) file. This is a common design file accepted by both the lithography equipment and simulation 



<!-- Start of picture text -->
TT atinAlm bigV/m<br>EE a — || 4.39404.7e+0 6 Y i er een | 1. 88e+07640 8<br>ee|— |er—— Ee———= = 3.79e+063.482+06 f eea em 1.39%+081.52e+08<br>=_——— [= rr - = = 2:188.10, —— 1.276408<br>=—————— | | SE — 2 4 || 288e:06 1} 1.15e+08 |<br>| PE — A 2.58e+06 | 1.03e+08<br>ee | ——— 4 1676406 | Sr ee rm 6.676407<br>_ | — = 1.36406 a 5.450407<br>=| ItNy yJ 7.584051.066406 EEes Se Seet ilA 4240407Ee<br>_— ain ? 4.356: SSS ae 1.826407<br>d) 0.00<br>—_ =  0.05<br>m<br>©=<br>=<br>Y ~ -0 .10<br>-0 .15<br>5 6 7 8 9 10<br><!-- End of picture text -->



<!-- Start of picture text -->
150<br>—oo<br>2— 100<br>[}<br>0<br>2<br>a 50<br>0<br>5 6 7 8 9 10<br>Frequency (GHz)<br><!-- End of picture text -->

Resonator development 

70 

polygons. Given that the total polygon number determines the simulation time, we want to minimise this where possible. In this case, we can define mesh groups, within which adaptive meshing will have different rules to generate the mesh. This concentrates the majority of the polygon count for meshing the actual resonator geometry, giving us an accurate simulation of the field distribution here. The CST frequencydomain solver is then used to simulate the frequency-dependent scattering matrix, in direct analogy to making a VNA measurement. We can then use the solver to calculate the spatial and temporal distribution of electric and magnetic fields at this frequency. Given the lumped element design demonstrated here, this step is crucial since we only want generation of the magnetic field around the inductor. Any stray inductance in the design will show up as spurious magnetic fields, decreasing the concentration of the useful field and increasing the device mode volume. 

###### **4.2.2 Fabrication** 

Once a geometry has been optimised in simulation, work can begin on making the device a reality. The basic steps to make a superconducting microresonator using optical lithography are<sup>2</sup> : 

1. Substrate cleaning 

2. Sputter substrate with superconducting 

3. Spin coat resist 

4. Soft-bake resist 

5. Expose design onto resist 

6. Develop exposed resist 

7. Wash exposed resist 

8. Etch uncovered 

9. Clean unexposed resist 

These steps are depicted in 2D in Figure 4.5, showing how the resist creates a protective layer above the superconducting film that stops unwanted etching in places where the final design should be. 

> 2 However, the steps above are for the procedure used in this work. 

Resonator development 

71 



Figure 4.5: A diagram explaining the steps in 4.2.2. 

###### **Cleaning** 

Before the subsequent steps, the substrate to be fabricated on typically needs to be cleaned; depending on the processing history of the substrate, this can mean different things. For silicon in particular, a _≥_ 1 nm [94] layer of silicon dioxide naturally grows on the surface; if high-temperature processing has also been used, this number can be larger. Despite its shallow thickness, this layer can capture impurities on the surface of the substrate, which would then be detrimental to the performance of superconducting devices fabricated on top. 

To clean silicon wafers, we therefore start by etching away this layer with a hydrofluoric acid (HF) or buffered oxide etch (BOE) dip. After this, additional cleaning steps may be necessary to remove other contaminants. The chemical cleaning often concludes with a solvent clean. We sonicate for 5 minutes in an acetone bath at 65 °C. Since the acetone will also leave a residue, we then immediately move the device into an isopropyl alcohol (IPA) bath and sonicate again for 5 minutes at 65 °C. After the device has been sonicated in IPA, it can be blow-dried with nitrogen gas. 

###### **Sputtering** 

With a clean blank wafer ready to be patterned, the next step is to deposit the superconducting film onto the substrate through sputtering. This is a process by which a ‘target’ comprising high-purity metal to be deposited is ionised by a DC source; a magnetron then drives the ionised material onto the substrate, growing a thin, high-purity 

Resonator development 

72 

layer of the superconductor. Given that any gases in the chamber can be captured by the sputtering process leading to impurities in the film, great care is taken to ensure a very low sample-chamber pressure before the sputtering is started. For this work, the 50 nm niobium films were deposited with the Scientific Vacuum Systems (SVS) model V6000. With the sample chamber initially being pumped down to 9 _◊_ 10<sup>_≠_7</sup> mbar overnight. 

###### **Dicing** 

If the sputtered substrate is larger than the die size, it must be diced into pieces suitable for the photolithography process. In this work, all devices fabricated were 10 _◊_ 10 mm. The die size used must also be optimised: making it too large leads to material wastage, since most of the space on the chip will not be utilised. However, making the die size too small can adversely affect the lithography process, as the edge of the chip can cause edge beading, where the photoresist accumulates due to its viscosity. 

###### **Spin coating & baking** 

Since dicing can lead to recontamination, the diced chips need to be cleaned again before fabrication. Given that a native oxide can also grow on the the superconductor surface and that there can be long periods between sputtering and fabrication on a specific die, a second HF dip is used at this point to get the best device performance. The cleaned, diced, chips are then spin coated with photoresist. Due to the small die size, only three drops of MICROPOSIT<sup>®</sup> S1805 positive photoresist are required so that the entire sample is initially coated. This is then spun at 4000 rpm for 30 s to produce a nominally 0.5 µm thick resist layer. The sample is then placed on a hotplate for 60 s at 115°C to soft-bake the resist removing excess solvent from the solution. 

###### **Exposing the design** 

With a thin layer of UV-sensitive photoresist coating the entire sample, areas can then be exposed to UV light, allowing a patterned resist mask to be formed. In this work, exposure was performed using a Heidelberg DWL 66<sup>+</sup> direct write tool, which enables lithography designs with a minimum feature size of 1 µm to be exposed without the need for a photomask. This is achieved using a 375 nm laser [95], mounted on a two-dimensional motorised gantry with precise movement control. A design file can be uploaded to the device and the moving laser exposes the photoresist with the shape of the design. This is advantageous for rapid prototyping since it does not require a new photomask for each design iteration. 

There are however many laser exposure parameters that can lead to between the design and final product. Typically the largest hurdle comes from the 

Resonator development 

73 



Figure 4.6: A microscope image of the developed resist mask used in a dose test to refine fabrication parameters. The central panel shows nine test features with varying geometries. On the sides of the frame are exposures using different laser focus and intensity. 

smallest feature size on the device, this can be both a positive or negative feature meaning the smallest gap or trace width. Given that these parameters vary the amount of UV energy incident on the photoresist, this step is called ‘dose testing’. Before fabrication of the actual design we therefore optimise by making a test feature that is analogous to the smallest features on the final device. We can then produce a small number of devices with a matrix of possible photolithography parameters. Figure 4.6 shows a 2D dose test, varying the laser focus and intensity in order to optimise a feature comprised of 1 µm gaps and 1 µm traces. Since S1805 is a positive photoresist any areas that have been exposed to UV light will be removed by the developer, this means that these areas will end up being etched later on in the process. The design file we uploaded to the direct write tool needs to be the inverse of the actual design wanted. 

###### **Developing** 

The areas that have been exposed to the UV light are now ‘developed’. The UV breaks the resist down into shorter polymer chains which will be more soluble in an alkaline solution, so they can be preferentially removed. The samples are developed in a beaker of MICROPOSIT<sup>®</sup> MF-319 for 60 s. Gentle manual agitation is applied for the duration to ensure an even concentration of the developer across the device throughout this process. After this time the sample is placed in DI water to clean off any residue and stop any more resist dissolving in the developer. The development time is another control parameter than needs to be optimised along with the UV exposure values to make sure original design dimensions translate directly to dimensions on the device. Since using a direct writer allows many combinations of exposure parameters on the 

Resonator development 

74 

same device, here we vary those values and the development time. 

###### **Etching** 

The unwanted superconducting can now be removed using a dry etch process, called ‘reactive ion etching’ (RIE) wherein a highly reactive ion plasma is propelled at the sample removing the unprotected superconducting film. This is in contrast to a ‘wet-etch’, where the etching is done in solution. The dry etch leads to a straight edged etching profile without undercut [96]. This is preferable since it means the dimensions of the resist mask will directly match those of the completed device. 

The etching was completed using Oxford Instruments Plasma Pro NGP80 RIE, with a combination of 14 SCCM SF6 and 35 SCCM CHF3 plasma at a power of 100 W and 100 mtorr pressure. The etching procedure was 1 minute on and 1 minute off, repeated 4 times for a total etching time of 4 minutes. The waiting periods are important to avoid overheating of the resist mask during etching. Given that once the superconducting film has been fully removed the RIE will continue to etch through the substrate below, we must carefully calibrate the etch time to minimise the over-etch into the substrate. For silicon devices with a shallow implantation depth this is particularly important since etching away the substrate will also remove the implanted spins. 

###### **Solvent clean** 

The step is then simply to clean the resist mask. Since the resist is soluble in acetone, we use the same solvent clean as above sonicating in both acetone and IPA before blow drying with N2. 

###### **4.2.3 Cryogenic testing** 

Despite the outputs from CST models being reasonably accurate, real devices often do not match exactly the results from simulation. Specifically small changes in the superconducting film thickness, can offset the resonant frequency by a small percentage compared to as designed. Once the recipe has been finalised we start by making test devices on a ‘blank’ substrate without spins. By placing both the implanted and blank substrates in the sputtering chamber at the same time, we ensure that the same film is sputtered on both. 

To calibrate the design we make multiple devices, varying a tuning parameter that changes the resonator frequency. This allows us to produce a calibration curve between With this curve we can that parameter, and the resonator frequency for a specific film. then make devices for any frequency within the applicability of the calibration curve’s range. Figure 4.7 shows one such curve for the same lumped element resonator simulated above, here the varied parameter was chosen to vary both the device capacitance 

Resonator development 

75 



Figure 4.7: An example resonator tuning curve for the resonator design dubbed ‘Letterbox’. The width of the resonator _w_ is varied across two device fabrication different runs, each with six resonators on. This gives a range of twelve frequencies, from which we can interpolate for a specific target transition. On this device we expect an approximately linear dependence of inductance and capacitance with the parameter _w_ . 

and inductance in an approximately linear fashion. The quadratic shape of the curve shows us that this is not the case, since from 3.8 we would expect this to lead to a frequency dependence: 



where _w_ is the parameter the total resonator width as shown above. This is not a problem since we can still generate a smoothly varying interpolation curve for future devices. 

###### **Resonator** 

From equation 3.21 we expect resonators to have a Lorentzian power dependence with frequency. The frequency response of a resonator can be understood by its ‘scattering matrix’. The ‘scattering matrix’ or ‘S-parameter’ formalism used in microwave engineering connects the reflected and transmitted power of an unknown network to the voltage incident upon it. For a general two-port network, if pulses of voltage _V_ 1<sup>in</sup><sup>_/V_</sup> 2<sup>in</sup> are applied to ports 1/2 respectively, we will then subsequently measure voltages of: 



Resonator development 

76 

Where _S_ 11 _, S_ 12 _, S_ 21 _, S_ 22 are the components of the scattering matrix **S** . From this we see that if _V_ 2<sup>in= 0thentheterm:</sup> 



and: 



are the and transmitted voltage gains from port 1. Similarly _S_ 22 and _S_ 21 will give the reflected and transmitted voltage gains from port 2. We seen then, by sequentially applying pulses to both ports and measuring the transmitted/reflected signals we can completely determine the components of **S** . Resonators are probed using a vector network analyser (VNA) which allows efficient phase sensitive measurement of the scattering matrix as a function of frequency. Since the components of **S** in general complex, leading to a phase shift transmitted/reflected signal, we require this to be a phase-sensitive measurement. Using a VNA, we measure **S** ( _Ê_ ) to determine the frequency response of each device. 

To determine key performance parameters like Q-factor and centre frequency of the resonators we fit the measured scattering parameters to an analytical function with the expected response. Due to imperfections in the measurement setup and resonator coupling we do not expect so see a perfect Lorentzian. In a notched coupling setup, where the resonator is placed next to a nearby waveguide, we can fit the resonator response to [97, 98]: 



Where _f_ is the measurement frequency, _fr_ is the resonant frequency, _a_ is the amplitude of the environment factor, _–_ is a fixed phase shift, _·_ is the electronic cable delay, _Ql_ is the total or loaded quality factor, and _Qc_ = _|Qc|e_<sup>_≠i„_</sup> is the coupling quality factor. The complex value of _Qc_ comes from potential impedance mismatches between the resonator and waveguide. Due to the complexity of this fit, we use a circle fitting routine provided by Dr. S. Probst [99] that draws the resonator scattering response in the complex plane to extract fitting parameters in a robust way. In Figure 4.8 we see an example using this routine to fit the resonance shape of a real resonator. Since the model makes distinction between _Ql_ and _Qc_ , from equation 3.24 we can also extract the intrinsic quality factor _Qi_ . Meaning we can extract all of the key resonator parameters from a single _S_ 21 measurement. 

Resonator development 

77 



Figure 4.8: Example usage of the circle routine from [99]. From the we determine: _fc_ =4.562 GHz, _Ql_ = 2 _._ 3 _◊_ 10<sup>4</sup> , _Qi_ = 1 _._ 5 _◊_ 10<sup>5</sup> and _Qc_ = 1 _._ 2 _◊_ 10<sup>5</sup> . 

###### **Resonator alignment** 

Making spin-dependent measurements requires use of a magnetic applied to the superconducting resonators we have fabricated. Superconducting devices are generally incompatible with large magnetic fields, since a high magnetic flux penetrating the device leads to separation of Cooper pairs [100, 101] which ends the superconducting effects. The superconductor becomes more sensitive to this as the device temperature approaches the superconducting transition temperature [102, 103]: 



Where _Bc_ is the at which the material begins to no longer superconduct (the ‘critical field’). _Bc_ (0) the critical field at 0 temperature. _T_ is the temperature of the material, and _Tc_ is the temperature at which the material no longer superconducts, the ‘critical temperature’. As well as ceasing to superconduct at high fields, the kinetic inductance of the resonator will also change as more field is applied. This is since the kinetic inductance of a material is linked to the kinetic energy of the charge carriers in it [104]. We can relate the energy stored in an inductor to this kinetic energy: 



Where _L_ is the inductance, _I m_ is the mass of the charge carriers, _v_ is their velocity, and _N_ is the number of carriers. Since the current can be linked to the charge carrier drift velocity through: 



Where _n_ is the charge carrier density, _q_ is the total charge on each carrier (2 _qe_ for a superconductor), and _A_ is the cross-sectional area of the wire. The kinetic inductance 

Resonator development 

78 

of a current carrying wire is then given by [105]: 



Where _m_ is the mass of a charge carrier (2 _me_ for a superconductor) and _l_ is the length of wire. Given that the density of charge carriers decreases as the field applied approaches _Bc_ , the kinetic inductance will increase. An intuitive argument for this happening is that to sustain the same current with a lower charge carrier density the charges must travel at a greater velocity increasing their resistance to changes in momentum. This looks similar in effect to a geometric inductance, however it does not generate a magnetic field. This means for the calculation of the resonant frequency and impedance the new resonant inductance can be written: 



Where _L_ tot & _Lg_ are the total inductance and inducing ‘geometric inductance’. However for calculating the _B_ 1 field generated by a current in the inductor this should not be included. Since the devices are fabricated from thin superconducting films ( _≥_ 50 nm), they have a considerable aspect ratio compared to the dimensions on the device ( _≥_ 500 µm). The total flux applied to the superconductor can be reduced by up to 10,000 times by rotating the direction of the applied field, so that it is parallel to the resonators thinnest dimension. Given this disparity, the flux experienced by the resonator as a function of the angle _◊_<sup>_Õ_</sup> between the field applied and a vector that is parallel to the superconducting film can be approximately written: 



Where _B_ 0 = _|_ **_B_** _|_ is the magnitude of applied to the device. For _◊_<sup>_Õ_</sup> = 0 there will still be some residual flux into the film but due to the large aspect ratio this becomes negligible. The change in kinetic inductance as a function of field experienced by the superconductor is given by [106]: 



Where _Lk,_ 0 is the kinetic inductance with no applied. From equation 3.8 the frequency dependence of the resonator on the magnitude and direction of the vector becomes: field 





<!-- Start of picture text -->
a) b)<br>ys 7.06600<br>- 7.06575<br>So N<br>p= & 7.06550 .<br>| 2> 7.06525<br>S<br>$ 7.06500<br>1 [T<br>T y rosa<br>ol 7 7.06450<br>ENV -10  -8 -6 -4 -2 0<br>9)<br><!-- End of picture text -->

Implantation & Annealing 

80 

since returning the resonator to its superconducting state after applying more than the critical field, is a lengthy process that requires warming the device up past its critical temperature [107]. To avoid pushing the resonator past this point, we sweep over a larger range of _◊_ values with a small _B_ 0. Then repeatedly increase the value of _B_ 0 for smaller _◊_ windows around the optimum. 

Since we are working in three dimensions there are in fact two angles that need to be found. If we consider the superconducting film to be perfectly flat, then the plane parallel to the device, _p_ res, can be defined by finding two intersecting vectors within it. Now as long as we keep _B_ 0 parallel to _p_ res, we can then freely rotate the vector field without increasing the flux through the resonator. An example showing this can be seen in Figure 4.9, where for _„_ = 0 any value of _◊_ will still lie in _p_ res. The procedure when first cooling down a new device, is to first find the optimal value of _◊_ in the lab frame using the method above, with a _„_ value of 90° for optimal contrast. Then rotate the field and optimise _„_ with a _◊_ value of 90°, from this we can then completely determine the set of allowed vectors parallel to the resonator plane. Even with perfect alignment there will still be some small shifts in the resonator frequency when the field changes. As such any time the magnetic field is moving there is opportunity for the centre frequency to change. As we saw in §3.3, spins coupled to a resonator will also lead to a shift in the resonance frequency. To combat this, when making field-dependent spin control measurements, at each field step we take a VNA measurement of the resonator. From this we find its centre frequency and set the microwave source to the new frequency. 

#### **4.3 Implantation & Annealing** 

The measurements made in the Bi:Si spin system require spin-active<sup>209</sup> Bi donors in the silicon substrate. To convert a blank silicon wafer into a spin-active device we must implant the donors and then anneal the implanted substrate. Implantation happens by accelerating<sup>209</sup> Bi donor nuclei at the silicon wafer surface. We then ‘anneal’ the system by rapidly heating then cooling the implanted substrate. This heals the lattice damage from the donor bombardment, and regains the original lattice structure with the donor nuclei incorporated. 

We choose implantation here because it allows us to create a spin-active volume in a thin layer close to the substrate surface. For the implantation and annealing recipe we want the largest spin signal possible, and therefore choose a high donor concentration at the expense of both electron and nuclear _T_ 1 & _T_ 2. We also want to minimise the change in the _B_ 1 microwave field across the ensemble to allow high-fidelity pulses. For this we implant a 200 nm-wide layer so that the range of spin–resonator distances is minimal, in Figure 4.10 we see SRIM simulation [108] of the donor concentration as a 



<!-- Start of picture text -->
a) 100 J b) 209Bi in Si 1700 keV, SRIM simulation, 7 deg<br>9 1x10"<br>o 80 1x10" —5E16<br>ro$< v o od 0,18 —1E= 17<br>= : 2 8x10 —<br>g © . 5 7xom —<br>© c 18<br>2 § 6x10<br>< 40 ; g 5x10”<br>© : S$ 4x10"<br>= ; £ 3x10"<br>ks = 8 2x10"<br>1x10"<br>600 700 800 900 0 200 400 600 800 1000<br>Temperature (°C) depth (nm)<br><!-- End of picture text -->

Pulsed ESR measurements 

82 







Figure 4.11: The microwave bridge layout used for generating and measuring the highfrequency signals. In the homodyne detection scheme used, the initial pulse sequence is generated at quasi-DC before being up-converted by the vector source. So as to generate along the appropriate sideband we provide both _I_ and _Q_ amplitude traces. A local oscillator (LO) signal is also provided by the vector source which allows phase coherent down conversion of the measured signal. The quasi-DC measured signal is converted to a digital signal via the digitiser. When using RF pulses (1 _≠_ 500 MHz), the pulse can be synthesised directly by the AWG so does not need up-conversion. To stop the high-power input amplifiers adding noise to the experiments, fast switches are used to dynamically allow pulses through. 

Pulsed ESR measurements 

83 

to generate both I and Q signals for complex up-conversion. Due to the high sample rate on the AWG the final channel was used to directly synthesise pulses up to 540 MHz when required, without need for mixing. Instead of a separate mixer and CW source we use a R&S<sup>®</sup> SGS100A SGMA RF source which takes the complex signal from the AWG and up-converts to microwave in a precisely calibrated manner. The SGS100A also provides a ‘Local Oscillator’ (LO) output that is at the same frequency and phaselocked to the the up-conversion CW source. The LO is then used with the output from the experiment and an IQ mixer to down convert the output to quasi-DC in both I and Q channels. This analogue signal is digitised by a Keysight M9203A digitiser to be saved to the experiment PC. 

Given the need for regular VNA measurements described above, and that these measurements share the same fridge lines. We also include MSP2TA-18-12BM+ slow switches, by placing one of theses SPDT switches on both the input and output of the fridge setup we can switch between the pulsed setup described above and a VNA without needing to repeatedly unplug and replug the cabling. A computer controlled DC power supply is connected to these switches so that changing the switch state can be done through software. 

###### **4.4.1 Connecting to the device** 

The microwave signals sent to and from the device are carried through low-loss coaxial cabling. Given the large size difference between the device and these cables they cannot be simply plugged into one another. To provide a systematic platform for measuring devices we design a printed circuit board (PCB) for placing samples on. The PCB is shown in Figure 4.12, the electrical connections to the cryostat coaxial cabling is done through surface mount SMP connectors on the PCB. The signal is then routed through a co-planar waveguide (CPW) on the PCB towards the device. For the experiments where low frequency pulses are not required it is sufficient to simply place the superconducting resonator close to this CPW, and the mutual capacitance/inductance is enough to couple to the device. For the nuclear spin control measurements we make a galvanic connection through aluminium wire bonds. The wires connect the respective central conductors and ground planes between the PCB and on-chip waveguide. The wire bonder has a hollow wedge with 25 µm diameter aluminium wire threaded through. The wedge then holds the wire in place while ultrasonic vibrations lead to a friction weld between the wire and the substrate. This type of electrical connection is easy to make and remove, which allows easy bespoke wiring for each new device. The micron precision of the wire bonder is also important for accurate placement on small device features. An example of a wire bonded device is shown in Figure 4.12 

The bonded device and PCB are then placed inside a copper cavity which reduces 



<!-- Start of picture text -->
Pulsed ESR measurements 84<br>Figure 4.12: Connection between the standardised cabling and on-chip waveguide is<br>done through a purpose built PCB and wirebonds. a) Photo of a device being bonded<br><!-- End of picture text -->

Figure 4.12: Connection between the standardised cabling and on-chip waveguide is done through a purpose built PCB and wirebonds. a) Photo of a device being bonded to the PCB, the purple highlights are ground plane wirebonds and the blue are central conductor connections. b) The PCB design used for the bismuth experiments, the red square is where a sample would be placed, and the two larger holes either side are for SMP coaxial connectors to be soldered. 

radiative loss from the resonator and allows a good thermal connection to the fridge. This is subsequently placed inside the sample puck ready for measuring. 

###### **4.4.2 Mitigating noise** 

A resistor at non-zero temperature will generate a voltage due to the thermal movement of charge carriers within it. This means that any warm component will act as a noise source, where the amplitude of the noise increases with the component’s temperature. The root mean square (rms) voltage that this thermal noise generates as a function of observation bandwidth is given by [110]: 



Where _T_ is the temperature of the resistor, _R_ is its resistance, and ∆ _f_ is the measurement bandwidth. This process generates a flat spectrum up to terahertz [111]. Using: 



where _P_ is power and _V_ is voltage, below this frequency the total noise power will be directly proportional to the bandwidth of the measurement. Comparing the noise 

Pulsed ESR measurements 

85 

power from a 50 Ωload at room temperature and 30 mK: 



We see the importance of the low noise inherent in low temperature measurements. The issue however is that much of the control equipment used to generate and measure microwave signals must be operated at room temperature. We therefore want to send the control signals down to the sample in a way that does not include the room temperature noise. The solution then is to strongly attenuate the signal entering the cryostat, using attenuators thermalised to each temperature stage. Since the attenuators themselves will also act as noise sources with noise power proportional to the temperature of the cooling stage, the attenuation at each stage needs to be chosen carefully so that the signal reaching the device has the effective noise temperature of the final cooling stage. 

Increasing the amplitude of the input signal, often using a high-power in proportion to the amplitude lost through attenuation ensures that the signal at the sample retains its original amplitude. However, this introduces a new problem: if the amplifier is always on, it will amplify the room-temperature noise at its input, thereby reducing the effectiveness of the attenuators. To address this, electrically controlled ‘fast switches’ are used, which can switch on the timescale of a single pulse. This provides binary, time-varying attenuation: the switches are closed only when pulses are applied to the ensemble. During the readout period, they are left open to attenuate noise from the amplifier 

On the output side of the measurement we must do the reverse. The signal generated at low temperature will also have negligible thermal noise, but the detection of that signal is done at room temperature. Here, resistive cabling would add noise greater than the measured signal. The solution is to amplify the signal at multiple stages so that the signal amplitude is always significantly larger than the noise power at this temperature. A key concern is that the amplifiers themselves add noise to the signal. The noise added by an amplifier can be rewritten as the combination of a perfect amplifier and a load at some temperature acting as a noise source. The effective Us- temperature of this noise source is termed the ‘noise temperature’ of the amplifier. ing amplifiers with noise temperature greater than the physical temperature becomes The inefficient since the amplifier will now be the leading cause of noise in the system. effective noise temperature of a chain of imperfect amplifiers we be derived from the Friis equation [112]: 



Where _TE_ is the noise temperature of the entire chain, _T_ 1 is the noise tem- 

Pulsed ESR measurements 

86 

perature of the _G_ 1 is the power gain of the _T_ 2 is the noise temperature of the second amplifier and so on. As long as the first amplifier has sufficient gain, the noise temperature of the entire chain becomes effectively limited by the noise temperature of the first. Using a high gain low-noise amplifier (LNA) at low temperature as the first in the chain, we can take advantage of the low noise inherent with low temperature measurement. We see in Figure 4.13 the line diagram showing the fridge lines used for the experiments in this work, where LNAs are on both output lines ( _B_ 5 & _T_ 6). 

###### **4.4.3 Josephson Parametric** 

From the above discussion we see that to get the most out of making low temperature measurements, we want to use an amplifier with noise temperature the same as, or lower than, that of the experiment. Given the millikelvin temperatures here we can take advantage of parametric amplifiers, providing gain with noise level down to the quantum limit of 1/2 a photon [113]. For a phase-insensitive amplifier this is the lowest possible noise, limited by the quantum uncertainty coming Heisenberg commutation relations. This amplification relies on a four-wave mixing process where two photons at a ‘pump’ frequency are converted into a ‘signal’ and ‘idler’ photon [114, 115]: 



Where _Êp_ is the pump frequency, _Ês_ is the signal frequency and _Êi_ is the idler frequency. Applying a continuous wave pump tone with a small offset from the measurement frequency leads to generation of extra signal photons amplifying this signal. To generate the mixing required for parametric amplification a component of the amplifier needs to be ‘non-linear’ in nature, meaning that it has a power dependent property that can be exploited to generate amplification. The parametric amplifier used for this work is a ‘Josephson parametric amplifier’ (JPA), where the non-linear element required for the four-wave mixing process is a Josephson junction. The JPA is analogous to a ‘kinetic inductance inductance parametric amplifier’ (KIPA) [116], which instead takes advantage of kinetic inductance as the non-linearity to drive the mixing process. These non-linear elements are often referred to as the Kerr medium for the device. In reference to the Kerr effect, where the refractive index of a material is dependent on the power of light incident upon it [117]. 

The JPA used for this work, uses pairs of Josephson junctions in parallel, a configuration called a superconducting quantum interference device (SQUID) [118]. The inductance of a SQUID is especially sensitive to the magnetic flux between the pair of junctions, as such they are regularly used as high precision magnetometers. Here it allows tuning of the amplifier. In operation there is an on chip DC line connected to a 

Pulsed ESR measurements 

87 



Figure 4.13: A schematic of the fridge lines in ‘Leela’. _B_ 2 is an input line, _T_ 2/ _B_ 4 are for RF pulsing and _B_ 5/ _T_ 6 are output lines. When using the JPA the pump tone is provided through _B_ 3. 



<!-- Start of picture text -->
a)'s<br>14<br>zB<br>E13<br>E<br>Edo<br>3<br>1:1<br>i<br>10<br>6.95 7.00 7.05 710 715 7.20<br>Frequency (GHz)<br><!-- End of picture text -->



<!-- Start of picture text -->
bso<br>125<br>©_10.0<br>£ 75<br>50<br>25<br>0.0<br>690 695 700 705 710 715 720<br>frequency(GHz)<br><!-- End of picture text -->

Pulsed ESR measurements 

89 

There are now only have two parameters: power. The simplest way to find the highest gain is therefore to iteratively sweep the pump power and DC current over small regions to find the global maximum. From its nature, the device is highly sensitive to external magnetic fields. To reduce this effect, it is enclosed within magnetic shielding. Despite this, measurements where the field applied to the spin ensemble is changing, either in magnitude or direction, require consistent retuning of the device to maintain optimal gain. For this reason, we use a script that automatically varies these parameters across small windows, allowing the device to be recalibrated quickly. 

###### **4.4.4 Megahertz frequency control** 

Many of the experiments in this work required simultaneous use of both megahertz (RF) and gigahertz (MW) pulses. Given the three orders of magnitude difference in Due to the frequency, the requirements for pulses in these two ranges are quite different. small volume and high Q factor of the superconducting resonators we have designed, the control signals will be very low amplitude. In contrast the RF signals will not get the field enhancement from the resonator, and will be used to drive nuclear spins with a vastly smaller gyromagnetic ratio ( _“e ¥_ 10<sup>3</sup> _“n_ ). The difference in frequency and power requirements make it ill-advised to use the same control lines for both MW and RF. Similarly on the output side, the RF will only be used for control and not readout. With the high RF powers used on the input, these pulses could damage sensitive MW amplifiers. 

To solve both of the issues, we design bespoke fridge lines for both MW and RF input and output. The signals are then combined and separated inside the puck using Minicircuits ZDSS-2R5G5G-S+ diplexers. A diagram of this setup is shown in Figure 4.15, the low insertion loss of these diplexers allows use of high power RF pulses without significant heating of the sample. The large difference in frequency becomes an advantage here allowing for a _>_ 80 dB isolation between high pass and low pass ports, leading to negligible cross contamination between signal paths. 

For the RF lines there are two noise concerns to consider. The is room temperature noise both interacting with the spins, and contaminating the output signal. Fortunately the very narrow bandwidth of the resonators used here, due to their high Q factors, act as a very efficient filter for frequencies away from the centre frequency of the resonator. This protects the spins from being driven by room temperature noise away from the centre frequency. The homodyne detection scheme and subsequent low pass filtering will also remove frequencies away from the experimental frequency on the output and detection side. For this first issue we only need to make sure we have filtering around the MW measurement frequency, which will be in the gigahertz regime. 

Pulsed ESR measurements 

90 



<!-- Start of picture text -->
To combine/separate the MW and RF signals, diplexers were used on both<br>of the experiment. A photo of the puck layout is provided, showing a<br>and the copper box containing the PCB (purple).<br><!-- End of picture text -->

Figure 4.15: To combine/separate the MW and RF signals, diplexers were used on both sides of the experiment. A photo of the puck layout is provided, showing a diplexer (blue) and the copper box containing the PCB (purple). 

The second noise concern is the thermal load that room temperature noise would place on the fridge cooling plates. Given that the isolation from the diplexers is absorptive in nature and that are likely to be other attenuation sources at millikelvin temperatures, broadband room temperature noise reaching the mixing chamber would add a reasonable extra load on the fridge cooling (40 nW). The fraction of this heat load that comes from below 400 MHz, is however negligible (1.5 pW). This allows us to negate having any attenuation at the frequencies we plan to apply RF pulses, avoiding large amounts of heating dissipation from them. 

Since we require minimal attenuation at the RF pulse frequencies, once the pulse has reached the device we cannot dissipate this power here. The pulse is therefore then sent back up out of the fridge and dissipated by a 50 Ωload at room temperature, where cooling is no longer an issue. This is the reason that we require both input and output RF lines in the fridge. For the RF lines we want low pass filters with a cut-off frequency higher than the relevant RF frequencies and above that attenuation as high as possible. Since the stop band of these filters begins to fall off at frequencies much higher than the cut-off, we use actually a pair of filters to achieve the desired frequency profile: Minicircuits VLF-400+ and VLF-8400+. With both of these at each plate on both input and output lines, we achieve high attenuation for room temperature noise with little heat load at the sample stage. In Figure 4.13 we see the cabling used for the RF pulses. 

# **Chapter 5** 

# **ENDOR with microresonators** 

To achieve a quantum memory, unit cooperativity is a requirement. Since bismuth donors have some of the longest _T_ 2 times among applicable spin systems, we use these as a starting point. The downside of this spin system is its large nuclear spin ( _I_ = 9 _/_ 2), generally meaning that 80% of the active spin concentration is not in the relevant nuclear-spin state. To increase the cooperativity of the implanted ensemble, we could hyperpolarise the nuclear-spin state into the transition of interest. The first step in this process is finding a way to control the nuclear spin that is compatible with an eventual quantum memory. 

This chapter presents the design and operation of a microresonator chip layout suitable for making ENDOR measurements using exclusively on-chip elements. We use this design to control the nuclear spin of bismuth donors in silicon, performing spectroscopy of all NMR-like transitions, including those not accessible directly from the ESR transition. 

#### **5.1 Chip design** 

Due to the narrow bandwidth of the superconducting resonators required to generate large _B_ 1 fields, we cannot simply apply these RF pulses through the resonator. To make the device capable of making ENDOR measurements, we need to be able to apply large _B_ 1 fields to the spin ensemble at RF frequencies _B_ RF. The simplest approach would be to wrap the sample chip in a large coil and use this to drive the nuclear spin transitions. Unfortunately, this approach has a number of key issues. The first is that the large inductance of such a coil would generate significant heating from driving a current at MHz frequencies. Given that these experiments are to take place at millikelvin temperatures, this heating would be a significant problem. The second problem is that requiring a large coil around the superconducting device significantly limits the possible uses of such an ENDOR setup. An entirely on-chip approach would allow the ENDOR resonator to be used anywhere a superconducting resonator is already in use. 

91 

Chip design 

92 



<!-- Start of picture text -->
Figure 5.1: The designs used for on-chip ENDOR. The schematic on the left shows the<br>whole chip design for a 10 ◊ 10 mm chip layout. Bonds are made to the device through<br><!-- End of picture text -->

Figure 5.1: The designs used for on-chip ENDOR. The schematic on the left shows the whole chip design for a 10 _◊_ 10 mm chip layout. Bonds are made to the device through the bond pads on the left and right sides; these lead to a coplanar-waveguide section before giving way to the lossy wire across the device. There are six resonators coupled to the central waveguide in a hanger-style geometry, each designed for a different resonant frequency. The right-hand micrograph shows an image of one of the resonators on the final device, with its location labelled by the dashed box. 

The approach we propose is to place a superconducting microstrip close to the resonator with a broadband frequency response. The line will be used both to couple microwaves to the resonator and to drive nuclear spin transitions. It is therefore crucial that the distance and microstrip geometry are optimised such that the input and output couplings between the microstrip and resonator are as desired, while the RF field generated by the microstrip is large enough to drive nuclear spin transitions on a short timescale. sufficiently 

Since the RF control is resonator-independent, we are free to choose any coupled design. The design we choose is a typical lumped-element LC resonator modelled around the design used by M. R. Vissers et al. [119]. In contrast to similar lumped-element designs, such as the one used by A. Bienfait et al. [82], placing the inductor along the top of the resonator allows increased separation between magneticand electric-field coupling to the resonator. The lumped-element design shown in Figure 5.1 allows a minimal characteristic impedance ( _Z_ 0) by making the inductance small and the capacitance large; as seen in §3.3, this enhances the spin–resonator coupling _g_ 0. The key design element for making ENDOR measurements is the on-chip waveguide, which we choose to make ‘lossy’ by removing the ground planes on either side. This converts the coplanar-waveguide geometry effectively into a superconducting wire. Although this is suboptimal for transmission, it dramatically increases the radial extent of the microwave field it generates, as shown in Figure 5.2. This is important to enable fast rotations of the nuclear spin, since the electron _T_ 1<sup>_e_placesanupperlimiton</sup> the duration of a nuclear inversion pulse ( _fin_ ). We next need to optimise the distance between the resonators and central waveguide, _r_ . Here, there is a trade-off to be balanced. Increasing the spacing will reduce the RF power that the nuclear spins see and 



<!-- Start of picture text -->
a) b)<br>120000<br>140<br>mm a ==<br>el a | - or<br>dl) A E I—————=e | iy—— S|| g< ap= 2 100 8000060000 &<br>== — T 60<br>= 20000<br>I=; =I—————————= 40<br>———— 20<br>==———— |<br>|| 0<br>0 200 400 600 800 1000 1200<br>| Distance (um)<br><!-- End of picture text -->

Continuous-wave measurements 

94 



<!-- Start of picture text -->
5 MHz/mT<br>3 . 4 MHz/mT<br>6 . 3 MHz/mT<br><!-- End of picture text -->

Figure 5.3: The CST simulation allows us to convert the input drive power into the field at the device. For a known Rabi frequency per unit field, we can calculate the expected duration of a _fin_ pulse. At 56 mT, the _F_ = 4 _mF_ transition Rabi frequencies vary from 3.4–6.3 MHz/mT. At 0.8 mW input power, the _fin_ pulse duration is 100 µs. 

#### **5.2 Continuous-wave measurements** 

For the iteration of the device, we fabricate the above design on a wafer with a 100 nm wide implantation layer centred at 400 nm and a peak spin-active concentration of approximately 0 _._ 6 _◊_ 10<sup>18</sup> cm<sup>_≠_3</sup> , as shown in §4.3. After cooling the device down, we align the vector field to the superconducting film using the procedure laid out in §4.2.3. This leaves a 2 _fi_ angular degree of freedom from which to pick the direction of _B_ 0, while keeping the field in the plane of the resonator. The most strongly coupled spins will be directly underneath the inductor. Since the inductor is straight, these spins will see a _B_ 1 field perpendicular to it, as shown in Figure 5.4. If we orient the _B_ 0 field parallel to the inductor, then the resonator will excite standard _Sx_ -type transitions. If _B_ 0 is perpendicular to the inductor, but still in the plane of the device, then we can use the microwave field generated by the resonator to drive the _Sz_ -type transitions described in §2.3. Since the ∆ _F_ = 0, _|_ ∆ _mF |_ = 1 NMR-like transitions are disallowed for the _Sz_ geometry, we must place _B_ 0 parallel to the on-chip waveguide and resonator inductor. 

be close to the 80 mT _Sx_ clock transition, as shown by the horizontal bars in Figure 5.5. All six resonators have a strongly power-dependent Q factor, with _Ql ¥_ 4 _._ 5 _◊_ 10<sup>3</sup> for an input power of _≠_ 80 dBm at the device. This is much lower than hoped, which, when coupled with the power dependence, suggests that a large number of TLSs are present across all resonators [120]. This is unfortunate, since intrinsic losses lead to 

Continuous-wave measurements 

95 













Figure 5.4: Diagrams showing directions with respect to the resonator and spin ensemble. a) A cut-through of the resonator inductor; the microwave field it generates points tangentially around the conductor. This means the implanted spins directly below it will all see a field to the left. b) A schematic of the central section of the chip. By orienting _B_ 0 parallel to the central conductor, both _B_ RF and _B_ 1 can be perpendicular to it. Since bismuth is an isotropic spin system, driving from _B_ 1 and _B_ RF will couple to the spins with the same strength. 





Figure 5.5: The EasySpin output around the six resonant centre frequencies of the resonators on the device. All of the resonators have Q factors in the range 4 _◊_ 10<sup>3</sup> _≠_ 5 _◊_ 10<sup>3</sup> . The horizontal axis lines show their centre frequencies, measured with a VNA. We focus on the resonator closest to the clock transition, with frequency _Ê_ 0 _/_ 2 _fi_ = 7 _._ 055 GHz, in order to maximise _T_ 2. We choose to measure on the low-field side, in the dashed box, around 60 mT. 

Continuous-wave measurements 

96 



Figure 5.6: a) Measured resonator FWHM as a function of across the 57 mT transition, using a VNA power of _≠_ 60 dBm at the device. For each field step, we fit the resonator lineshape to determine the FWHM. Due to the increasing field, we also observe a quadratically varying baseline. b) Increase in the resonator linewidth as a function of the spin–resonator detuning. The baseline has been subtracted to show the increased loss rate due to the ensemble. We see a divergence from a Lorentzian lineshape due to inhomogeneous broadening and the ‘mass effect’ discussed below. 

a reduction in SNR. Decreasing _Qi_ not only leads to a higher fraction of photons being dissipated in this way, but also to a lower Purcell rate. We choose to measure the resonator closest to the clock transition, operating on the low-field side. This increases the state mixing, reducing the expected _fin_ pulse duration. 

The step is to make continuous-wave (CW) measurements of the transition. This means using a VNA to track the resonator as a function of field across the transition. Due to the low _Ql_ , the visual change in the resonator is minimal; however, we can track _Ÿl_ by fitting the VNA trace to determine the FWHM at each field step. To enhance the effect from the ensemble, we increase the measurement power by 20 dB. This saturates the TLSs, leading to a proportionally larger increase in loss rate from the electron spin ensemble. It also increases the SNR for the VNA data, reducing the uncertainty in the linewidth measurements. We plot the results of this in Figure 5.6, showing the change in linewidth as a function of field. The increase in _Ÿl_ across the line can be related to the spin linewidth ( _“_ ) and spin–resonator ensemble coupling ( _g_ ens) through [121]: 



where _”Ÿl_ (∆) is the increase in the resonator full width as a function of spin–resonator detuning ∆. Using the EasySpin output, we can calculate the simulated spin frequency for each value of _B_ 0, which then gives the detuning ∆for each field step. In Figure 5.6, we fit the linewidth increase to determine _“_ and _g_ ens. We note that using this fit assumes that all spins are placed at the transition centre, with a homogeneous- 

Pulsed measurements 

97 



Figure 5.7: a) EasySpin output of the transition-doublet frequencies as a function of field. The resonator frequency is marked with the dashed axis line. At this field and frequency, both transitions have _|_ d _f/_ d _B| <_ 0 _._ 1 _|“e|_ . b) An echo-detected field sweep across this same transition. For each point, the resonator centre frequency is found before beginning the pulsed experiment. The predicted transition frequencies are shown as solid vertical axis lines. Since the cyan transition has the higher matrix element, we expect this to align with the peak. From the offset between the measured peak and simulated values, we infer a 130 µT offset between the set field and the field experienced by the ensemble. 

broadening-limited linewidth. We can immediately tell that this is not the case due to the asymmetric tail shape of the line. Despite the simplicity of this assumption, it does allow us to approximate the cooperativity at the transition centre. Using Eq. 3.71 with _Ÿ_ 0 _/_ 2 _fi_ = 770 kHz gives: 



This is unfortunately too small to reach unit cooperativity, even with a fully polarised nuclear spin. However, we can still use it to perform ENDOR measurements. 

#### **5.3 Pulsed measurements** 

The next step is to move to pulsed ESR measurements. We start by making a series of Hahn-echo measurements, sequentially sweeping the field across where the simulation predicts the transition to be, as seen in Figure 5.7. In the echo-detected field sweep (EDFS), the asymmetric tail shape becomes even clearer. This comes from a change in hyperfine for specific donors due to nearest-neighbour silicon nuclei being a different isotope [122]. The increased mass of nearest-neighbour silicon-29 or silicon-30 nuclei leads to a shift in the which can be detected in both ENDOR and EDFS hyperfine, measurements. Since the relative abundance of each isotope is well known, the line 

Pulsed measurements 

98 

of nuclei in the nearest-neighbour sites [123]. Since silicon-28 is the most abundant isotope, the largest peak comes from donors with only these nuclei surrounding the donor. Given that silicon-29 nuclear spins have a large effect on coherence in groupV donor spin systems, we might naively expect to see different dynamics on each of these peaks. However, this is not the case; the large hyperfine of the electron spin significantly detunes the nuclei in nearby sites from the surrounding bath. This separation in energy leads to strongly suppressed nuclear spin dynamics close to the donor, termed the ‘frozen core’ [124]. The decrease in _T_ 2 comes from the wider spin bath and so is independent of the specific nuclear spin configuration next to a particular donor electron. Despite not seeing any changes to coherence, the mass effect provides interesting selectivity with respect to the number of nearest-neighbour _I_ = 1 _/_ 2 nuclei. Since we are expecting to use this device for nuclear spin control, this could be used to expand the Hilbert space under exploration. 

Another source of complexity in the bismuth system is the transition doublets. As was seen in §2.3, the allowed _Sx_ transitions in the _|F, mF Í_ basis are: 



This means that each transition is typically a doublet of two closely spaced transitions: 





We see both of these in the simulated frequencies in Figure 5.7; the higher-frequency transition has a larger matrix element, so we predict this to be where the largest echo amplitude is found. From this, we infer a small 130 µT field offset between the global set field and the actual field experienced by the spins. This is unsurprising, since a small sample misalignment, placing the sample away from the central field maximum, can lead to a systematic offset. The spacing between a transition doublet is given by [17]: 



where _f_ (∆ _F_ ∆ _mF_ = _±_ 1) are the frequencies of each transition in the pair, _“n_ is the nuclear gyromagnetic ratio of<sup>209</sup> Bi and _B_ 0 is the magnitude of the applied field. For _“n_ = 6 _._ 7 MHz/T and _B_ 0 = 56 mT, this gives a splitting of 0 _._ 8 MHz, which is narrower than the linewidth of Bi:Si<sup>nat</sup> , so we cannot resolve this splitting here. It is, however, important for the ENDOR measurements since we need to keep track of which member of the pair is being addressed by a particular RF pulse. 

A consequence of the high nuclear spin of bismuth is that the optimal temperature 

Pulsed measurements 

99 



Figure 5.8: The left diagram shows the Bi:Si energy structure at 56 mT, with the relevant transitions highlighted. Due to the low field, the _|F, mF Í_ basis is more appropriate, and we have nine electron-like ground states ( _F_ = 4) and eleven excited states ( _F_ = 5). The right plot shows the Boltzmann distribution of populations for this energy structure as a function of sample temperature. To increase the spin signal, we want to maximise the polarisation between the _F_ = 4 and _F_ = 5 levels to be excited. For this field and frequency, we therefore set the fridge temperature to 100 mK to get the largest possible population differences. 

We simulate the transitions using a Boltzmann distribution, and choose the optimal temperature so that the difference in population between the excited and ground states across the relevant transitions is maximised, as shown in Figure 5.8. With the field, frequency, and temperature set, we can map the energy landscape, including the resonator transitions. We initially make the naive assumption that all _F_ = 4 spin states have equal populations and that the _F_ = 5 manifold is empty. We can see from the Boltzmann distribution that this is not necessarily the case, but it is a reasonable approximation. 

Once we have optimised the and temperature, we use the pulse sequences described in §2.5 to measure the Rabi frequency, _T_ 1, and _T_ 2, as shown in Figure 5.9. The thin implantation layer means that the inversion achieved even in the rectangularpulse Rabi sequence is high compared with other microresonator geometries [125]. If we the inversion as define efficiency 



where _÷_ inv _A_ ( _◊_ = _fi_ ) & _A_ ( _◊_ = 0) are the echo amplitudes after an initial pulse with tip angle _◊_ , we then find _÷_ inv = 30% for the square pulse. To achieve even better inversion, we use WURST pulses for sequences requiring _◊_ = _fi_ ; for angles _◊_ = _fi_ , we use square or Gaussian pulses due to the linear relationship between duration and flip angle. In Figure 5.9, we also see an inversion recovery measurement made with a WURST pulse as the initial inversion, showing nearly 100% efficiency. 

Pulsed measurements 

100 



Figure 5.9: Characterisation of pulsed ESR measurements. a) Measurements of the electron _T_ 1, following the sequence described in §2.5. For the initial inversion we use a WURST pulse instead of a rectangular _fi_ pulse. To obtain a reasonable fit, we allow two characteristic timescales, showing that fast and slow _T_ 1s are present. The relative scale (r.s.) indicates the ratio between their amplitudes. b) Rabi oscillation measurement, showing a rapidly decreasing contrast with pulse duration. Pulses longer than _¥_ 2 _fi_ are unlikely to be effective. The narrow implant region, however, does make the decay rate slower than in other planar-geometry measurements [123]. c) _T_ 2 measurement. Given the low field sensitivity, we would expect many decoherence mechanisms to be suppressed. We expect the high spin concentration to be the leading cause. 

ENDOR spectroscopy 

101 

The measured data show at least two clear relaxation rates, so we the data to the form: 



where _a, b, c, T_ 1<sup>_a, T_</sup> 1<sup>_b_The two timescales are given by</sup><sup>_T a_</sup> 1<sup>and</sup><sup>_T_</sup> 1<sup>_b_,</sup> where the parameter _c_ determines their relative scale (r.s.). The parameter _c_ therefore specifies which rate is more dominant across the trace. As the spin–spin interaction is likely the leading relaxation mechanism, the range of concentrations across the implant depth may cause a spread of _T_ 1s, meaning that no single decay rate describes the entire ensemble, and the fit identifies two components within this distribution. The _T_ 1<sup>_b_</sup> timescale has a 1.2 times larger amplitude, showing this _T_ 1 represents a larger fraction of spins. From Figure 3.4, at low donor concentrations, we would expect the electron spin-lattice _T_ 1 to be of order 10<sup>3</sup> s. Since this is clearly not the case, there are two other likely explanations: either the _T_ 1 is limited by Purcell decay, or it is limited by spin– spin interactions. Rearranging Eq. 3.89 for ∆= 0 shows that the Purcell explanation is unlikely given the low Q factor, since this would imply an average spin _g_ 0 of: 



which would be surprising, since this is higher than donor-coupled devices with a similar geometry, even those with a smaller spin–resonator distance [82]. We therefore suggest that the _T_ 1 is limited by spin–spin interactions due to the high concentration, rather than Purcell relaxation. 

From the EasySpin output, we can also calculate the gradient of the transition at this point to quantify the sensitivity of the spins to field noise: 



Since _|_ d _f/_ d _B|_ is less than 10% of the free-electron gyromagnetic ratio, we expect to turn off a large amount of _Sz_ -type decoherence. The measured _T_ 2 is therefore shorter than expected, suggesting a concentration-limited _T_ 2 from direct flip-flop interactions. 

#### **5.4 ENDOR spectroscopy** 

With the microwave pulses calibrated, we perform ENDOR spectroscopy on the device, using the on-chip waveguide as a local antenna to drive nuclear spin transitions. From the CST simulations, we predict pulses longer than 100 µs for a _fin_ rotation; in Figure 5.10, we see the spectral width of a rectangular pulse with this duration. Since the transitions are likely to be wide compared with this bandwidth, we choose to use 

ENDOR spectroscopy 

102 



<!-- Start of picture text -->
100  µs Square pulse<br>100  µs WURST pulse<br>200  µs WURST pulse<br><!-- End of picture text -->

Figure 5.10: Fourier transforms of WURST pulses and a square pulse of similar duration. By sweeping the frequency, we can drive a much larger bandwidth of spins at the cost of lower amplitude. The peak amplitude of the square pulse is approximately ten times that of the same-duration WURST pulse. By increasing the WURST pulse duration, we can recover the difference, but at the cost of longer pulses. 

tion. We then use the ‘Tidy’ sequence described in §2.5, sweeping the centre frequency of the WURST RF pulse. Given the increased number of energy levels available, we now expect a different result when the RF pulse is resonant with a transition. First, we note that due to the small separation between excited- and ground-state RF transitions, we cannot spectrally distinguish between them and therefore always drive both. In Figure 5.11, we see the measured result using a 500 µs duration, 3 MHz bandwidth RF pulse and a 2 MHz bandwidth WURST MW inversion pulse. 

There are three peaks representing the relevant ∆ _mF_ transitions; above each, we plot the predicted centre frequency from EasySpin. There is clearly a stronger alignment with the ground-state transition frequency, suggesting this is being driven more efficiently. We can generate a simulated trace by taking the convolution of the EasySpin output for Gaussian-broadened spins with the FFT of the pulse used to account for its broadening. We see a distinctly different central peak amplitude than is expected from the simulation. This behaviour can be explained by considering two sub-ensembles within the system. However, we leave this discussion for the subsequent chapter, as the argument can be made more strongly with the time dynamics we measure there. By sweeping the chirp width, we can try to extrapolate the underlying spin linewidths, measuring surprisingly broad transitions [34]. This may be due to the high spin con- 

ENDOR spectroscopy 

103 



Figure 5.11: a) Tidy ENDOR measurements using the on-chip drive, for a 500 µs duration, 3 MHz bandwidth RF pulse and a 2 MHz bandwidth WURST MW inversion pulse. The expected transition frequencies at 56.23 mT are shown as axis lines: solid lines for the ground-state transitions and dashed lines for the excited-state transitions. The simulated trace is calculated as the convolution of the EasySpin ENDOR output with a 1.5 MHz FWHM Gaussian spin broadening and the 3 MHz bandwidth WURST pulse. The trace is then normalised by the span of the measured data. b) The measured peak FWHM on each of the three peaks in a) as a function of the RF pulse bandwidth. The peak bandwidth closely follows that of the pulse, showing that this is the leading broadening mechanism. Below a 2 MHz chirp, we see a small divergence, suggesting the original spin linewidth is beginning to show. c) By sweeping the duration of the RF pulse on resonance with a transition, we can measure the pulse duration required to reach inversion. The spread in characteristic timescale _TW_ is larger than would be expected due to the differing matrix elements. 

ENDOR spectroscopy 

104 



Figure 5.12: Each pixel represents the measured echo amplitude at that field and frequency. Since the echo amplitude varies greatly with field, each frequency trace is normalised to its minimum value. The transition centres follow the simulated frequencies from EasySpin with an _¥_ 2 _._ 8 MHz/mT gradient. The outer peaks stay at a fixed amplitude, whereas the central peak decreases towards zero at the centre of the electron spin line. 

centration; however, due to the WURST pulse adiabaticity condition, this is largely obscured. Unfortunately, despite achieving efficient inversion, these pulses are not well suited for resolving spectral lines. We can also sweep the duration of the WURST pulse on each peak, measuring the rate at which inversion is achieved. The low values of _TW_ are useful, because they mean we can apply many RF pulses within one _T_ 1<sup>_e_.</sup> 

We measurement sweeping both field and ENDOR pulse frequency, tracking their centre frequencies and amplitudes, as shown in Figure 5.12. The most surprising result is that the central peak appears to drop in amplitude towards the centre of the transition. This suggests that the measured ENDOR contrast is changing due to the ratio of contributions from both of the resonant transitions. At low field, the ∆ _F_ ∆ _mF_ = +1 contribution will be larger, whereas at high field, more of the echo signal will come from ∆ _F_ ∆ _mF_ = _≠_ 1. Again, we save the full discussion of these dynamics for the subsequent chapter. 

Spectroscopy of further transitions 

105 



Figure 5.13: Relationship between ∆ _mF_ transitions and the labels _RF_ 0 _≠_ 9. Since we cannot distinguish between _F_ = 4 and _F_ = 5 ∆ _mF_ transitions, both are given the same label. The _RF_ 0 and _RF_ 9 transitions only appear in the _F_ = 5 manifold. 

#### **5.5 Spectroscopy of further transitions** 

We now attempt to use the device to perform spectroscopy on further ∆ _mF_ transitions. Due to the reasonably long electron _T_ 1, we can shuffle populations around using RF pulses to generate contrast across the transition of interest. For ease of explanation in the following experiment, we label the ∆ _F_ = 0, _|_ ∆ _mF |_ = 1 transitions with the labels _RF_ 0 _≠_ 9. Transitions between matching _mF_ values are labelled the same for _F_ = 4 and _F_ = 5 states, since the 5 MHz bandwidth RF pulses do not discriminate between them, as shown in Figure 5.13. Since the populations of the _F_ = 5 manifold are much smaller than those of the _F_ = 4 manifold, this gives a reliable way to generate contrast for performing spectroscopy on the NMR-like transitions. Since we have already calibrated the _RF_ 5 _≠_ 7 pulses, we can now use these to measure the other transitions. As an example, we see the sequence used for spectroscopy on the _RF_ 4 transition in Figure 5.14. The sequence is designed such that when the frequency of the swept pulse _RFx_ matches that of the transition, we see a change in the echo amplitude. The resulting measurement is shown in Figure 5.15. Although this sequence does not provide double contrast (echo amplitude: _≠_ 1 _æ_ +1), we still see a clear change in the amplitude of the measured echo as a function of swept _RF_ pulse frequency. Again, we can also sweep the duration of the _RF_ 4 pulse to extract the optimal pulse length for inversion across this transition. As the power of the RF driving pulse increases, _TW_ decreases, at the cost of increased fridge heating. We also find that the measured data appear to have a larger spin linewidth; this is likely a consequence of the increased pulse amplitude. Since the spectroscopy is preceded by driving the other RF transitions, the effects of earlier pulses in the sequence obscure the direct effect on the transition being measured. 

Spectroscopy of further transitions 

106 



Figure 5.14: The sequence used for spectroscopy on the _RF_ 4 transition between _mF_ = +1 and 0. 1) We assume equal populations across the _F_ = 4 manifold. 2) The WURST MW pulse puts the population into the excited state. 3) The _RF_ 7 pulse moves both excited- and ground-state populations. 4) _RF_ 5 does the same on the other side of the transitions. 5) A second inversion pulse places the newly shuttled population into the excited state. 6) The frequency-swept pulse _RFx_ is played; if the frequency is correct for the transition, then both ground- and excited-state populations are driven (empty circle). If not, the population stays where it is (translucent circle). 7a) If the population from _mF_ = +1 was successfully moved, then the subsequent _RF_ 5 pulse puts it on resonance with the resonator; since there is no population difference, the Hahn-echo amplitude will be zero. 7b) If the _mF_ = +1 population was not inverted, then the drive from _RF_ 5 has no effect and the echo amplitude is _≠_ 1. This sequence therefore creates contrast between the two conditions, allowing us to probe the transition frequency. 

Spectroscopy of further transitions 

107 



Figure 5.15: a) The echo amplitude measured across the _RF_ 4 transition, using the sequence described in Figure 5.14 with 5 MHz wide RF pulses. Again, the simulation comes from a convolution of the _RFx_ pulse and the original spin linewidth. The blue line shows the expected spectrum for a 4 MHz wide spin line, and the purple line shows the expected spectrum for a 2 MHz wide spin line. b) Instead of sweeping the _RFx_ pulse frequency, we can also sweep its duration at the centre of the line, measuring the characteristic inversion rate and saturation amplitude. These results were measured with increased pulse amplitude, showing good inversion even at high powers. 

We then repeat this process for all of the _F_ = 4 transitions, with each subsequent level requiring a more complex sequence to move the populations out of the way. Spectroscopy and Rabi measurements on each transition away from the centre allow measurement of increasingly far-removed transitions. In Figure 5.16, we show the results of all these measurements. We find good agreement with the output from EasySpin, assuming the transition linewidth is limited by the 5 MHz WURST pulse bandwidth and the power broadening of the original lines. The measurement of the low-lying _RF_ 1 transition requires knowledge of all the previous transition parameters. This demonstrates strong control over the system and provides good evidence that the on-chip RF delivery can be used effectively. 

For the transitions with higher _mF_ values, the separation between adjacent transitions becomes narrower than the bandwidth of the 5 MHz RF pulses used. We can account for this, and resolve overlapping transitions, by making careful choices about the sequence order preceding the spectroscopy pulse _RFx_ . We see an example of this in Figure 5.17, where removing contrast from the overlapping transition removes it from the measured spectrum. Through careful consideration of the pulse ordering, we can even distinguish lines that overlap in frequency. This technique is not specific to the Bi:Si system and could be used to explore many high-nuclear-spin ensembles in the millikelvin regime. 

Spectroscopy of further transitions 

108 



Figure 5.16: Spectroscopic measurements of all ground-state RF transitions, _RF_ 1 _≠_ 8. These measurements use the same method of population shuttling shown in Figure 5.14, freeing up space in the _F_ = 4 manifold by placing population in _F_ = 5. All sweeps were done at high power with a 5 MHz chirp to optimise inversion and decrease the sequence duration. The simulated traces come from a convolution of the WURST pulse FFT and the original ENDOR frequencies, assuming a 3.5 MHz spin linewidth. Each simulated trace is normalised to the measured data amplitude. There are clear resonances at all of the simulated frequencies across the spectrum. The pulse sequence used to measure the _RF_ 1 transition is shown below; due to the large amount of shuttling required, a total of 30 pulses are needed to measure the transition. 

Spectroscopy of further transitions 

109 



Figure 5.17: Example spectroscopy of the _RF_ 1 sequence with pulse ordering. 1a) We consider an _RF_ 1 spectroscopy sequence that leaves population in the _mF_ = +2 state before the frequency-swept pulse. 1b) If the transition linewidths overlap, then when the _RFx_ frequency matches _RF_ 2, it will drive population back the way it has come. 1c) The knock-on effect due to this unexpected driving is the appearance of the _RF_ 2 line in the ENDOR spectrum. 2a) A sequence with different previous pulse ordering leaves no contrast across the _RF_ 2 transitions. 2b) Now applying the swept pulse does not lead to unintended population inversions. 2c) The resulting ENDOR spectrum shows only the _RF_ 1 transition, despite overlap in their linewidths. 

Measuring time dynamics 

110 



Figure 5.18: Measurement of the electron _T_ 1 when on and resonance with the resonator. a) The sequence used to move the population away from the resonator frequency during the wait time _T_ . b) The identical sequence with no RF pulse allows the population to decay through Purcell relaxation. c) The measured recovery rates are the same for both sequences, confidently proving that the spins are not Purcell-limited. 

#### **5.6 Measuring time dynamics** 

Finally, we use control of the _mF_ spin state to measure the between the Purcell-enhanced ( _T_ 1<sup>_P_)andspin-lattice(</sup><sup>_T_</sup> 1<sup>_e_)relaxationrates.Ifthepopulationisex-</sup> cited but subsequently removed from being on resonance with the resonator, due to a change in the _mF_ state, it will no longer receive Purcell-enhanced decay. We can then compare this to the same inversion recovery sequence, where the spins stay on resonance for the duration of the sequence, to measure the difference between the _T_ 1s. In Figure 5.18, we see the results of this, where there is significant overlap between the two measurements. This strongly reinforces the assumption made above, that the measured _T_ 1 is limited by spin–spin interactions and not Purcell decay. The goal of this device is to use the nuclear spin control to generate a hyperpolarised spin state for enhanced cooperativity. However, the electron _T_ 1 must be limited by Purcell decay for this to happen. Achieving this will be impossible on this device; we must therefore fabricate a new device with a lower donor concentration. 

Discussion 

111 

#### **5.7 Discussion** 

In this chapter, we have shown that a fully on-chip design is capable of making ENDOR measurements at millikelvin temperatures. By shuffling populations around, we are able to measure any nuclear spin transition, demonstrating a high degree of control over both the electron and nuclear-spin states. Using the nuclear spin control, we showed the difference in electron spin decay rate when on and off resonance and proved that, due to the high donor concentration, spin–spin interactions are the limiting factor here and not Purcell relaxation. Since any reduction in the spin concentration will be proportionally reflected in the cooperativity ( _C Ã N_ ), we expect that future devices with the same geometry and lower implant concentration cannot reach _C_ = 1, even with a fully polarised nuclear spin. Two straightforward areas for possible improvement are the resonator filling factor and spin linewidth. The narrow implant profile, while being helpful for reducing _B_ 1 inhomogeneity across the ensemble, severely reduces the proportion of the resonator mode volume that is filled with spins: the resonator ‘filling factor’. Simply by implanting spins across a much wider range of depths, we could increase the number of spins coupled to the device, and so also the cooperativity. Crucially, spins closer to the inductor would also have an even higher _g_ 0 and so contribute more to the total cooperativity. It is difficult to have un-ionised group-V donors less than 50 nm from the surface due to band bending [126]; however, the 50–200 nm window that is currently unimplanted leaves scope for a large boost in the overall cooperativity. 

A second way to improve cooperativity without increasing the implant concentraThe EDFS measurements tion would be to use an isotopically purified silicon substrate. in this chapter show that the silicon-29 nuclear spins lead to a much larger total spin linewidth. From Eq. 3.87, we see that this effective reduction in concentration also leads to a lower cooperativity. Making the same measurements on a<sup>28</sup> Si device would therefore lead not only to a longer _T_ 2, but also to higher cooperativity. 

# **Chapter 6** 

# **Hyperpolarisation of bismuth nuclear spins** 

Building on the results from the previous chapter, we fabricate a similar microresonator device using a ten times lower bismuth implantation concentration. This comes at the expense of being able to reach the critical _C_ = 1 point, but guarantees that Purcell decay will be the dominant relaxation mechanism. This means that the spins coupled to the resonator decay much faster than those not on resonance with it, a crucial requirement for hyperpolarisation of the nuclear spin. We show a dynamically increased effective spin concentration using this method, and measure the decay rate of the hyperpolarised state to determine the nuclear _T_ 1. 

#### **6.1 Pulsed ESR in the Purcell limit** 

We fabricate the new device using a nominally identical recipe, with an approximate spin-active concentration of 0 _._ 6 _◊_ 10<sup>17</sup> cm<sup>_≠_3</sup> . Due to small imperfections in the fabrication, such as the film thickness and optical lithography parameters, the new device is at a slightly different frequency of 7.081 GHz. In Figure 6.1, we fit the resonator lineshape to determine a loaded Q factor, _Ql_ = 2 _◊_ 10<sup>4</sup> . Due to improvements in the film quality, the Q factor is four times larger, increasing the Purcell rate by the same factor. This time, we also measure on the high-field side of the clock transition. In Figure 6.1, we see that this causes the mass-effect tail to be on the opposite side due to the negative gyromagnetic ratio. We see a similar _T_ 2; however, since we are now further from the clock transition, we have a larger transition frequency gradient: 



112 

Pulsed ESR in the Purcell limit 

113 



Figure 6.1: Characterisation measurements for the new lower-concentration device. a) VNA measurements of the resonator, fitting the lineshape to a Fano lineshape. The fit gives a centre frequency _Ê_ 0 _/_ 2 _fi_ = 7 _._ 081 GHz and _Ql_ = 2 _◊_ 10<sup>4</sup> . b) An echo-detected field sweep across the high-field side of the clock transition, showing the opposite tail shape from that seen previously. c) _T_ 2 measurements using a Hahn-echo sequence, showing a similar _T_ 2 to the previous device. d) Rabi oscillations with a similar amplitude decay rate to that measured previously. 

Pulsed ESR in the Purcell limit 

114 



<!-- Start of picture text -->
High power Fit: T 1 = 145s<br>Low power Fit: T 1 = 3.1s<br><!-- End of picture text -->

Figure 6.2: Measurements of the electron _T_ 1 at pulse powers. The same inversion recovery sequence is repeated twice: first at high power, then a second time with the pulse power reduced by 42 dB. When driving with a higher amplitude, spins further away, with a longer _T_ 1, are prioritised, leading to a longer _T_ 1. 

so other decoherence mechanisms could also be a factor. is that the new low-concentration device now has a long enough _T_ 1<sup>_e_thatPurcelldecay</sup> becomes the dominant process. Using the inversion recovery sequence, we can again measure the _T_ 1 for this sample. In Figure 6.2, we measure the same inversion recovery sequence with a 42 dB difference in pulse power. If the spins coupled to the resonator are Purcell-limited, then the value of _T_ 1 should depend on the spin–resonator coupling _g_ 0. As we saw in §3.3.1, this will vary with the distance between a specific spin and the resonator. Given that higher-power pulses will optimally rotate spins further away from the resonator, with a lower _g_ 0, we also expect that at higher pulse powers the measured _T_ 1 should grow. This is exactly what we see here, where varying the power changes the _T_ 1 by a factor of 50. Since we want to prioritise the most strongly coupled spins with a short Purcell _T_ 1, we sweep the pulse amplitude at a short shot repetition time. Given that spins with long _T_ 1 will not have time to relax between subsequent shots, the measured signal will preferentially come from spins with a higher _g_ 0. This acts as a filter, allowing us to calibrate pulses for spins with optimal coupling to the resonator. For a Purcell _T_ 1 of 3 _._ 1 s, we calculate the average _g_ 0 using the same equations as in Eq. 5.10: 



which is more similar to what is expected based on the resonator mode volume and previous measurements [82]. The next step is to calibrate the RF pulses, as we did 

Pulsed ESR in the Purcell limit 

115 



Figure 6.3: Tidy ENDOR measurement of the low-concentration device. a) ENDOR sweep across the three closest transitions. The increase in field from 56 to 110 mT leads to much higher transition frequencies. Despite the same sequence being played to the low-concentration device, we measure increased contrast across the _RF_ 6 transition. b) Rabi sweeps for all three transitions at high RF pulse power show good inversion in a short duration. 

in the previous chapter. Due to the higher of this transition, we get a larger spacing between adjacent transitions. We can see the results of a Tidy ENDOR sweep in Figure 6.3, where again we measure three distinct peaks at the resonant transition frequencies predicted by EasySpin. We now see that the two side peaks saturate at 0, whereas the central peak approaches one. The difference for this device is that the narrower resonator frequency and higher field mean that the resonator bandwidth (350 kHz) is now narrower than the transition-doublet spacing: 



This is not narrower than the inhomogeneous broadening, so we cannot resolve the lines directly; however, per spin, we can distinguish between _mF_ states. We also measure the inversion rate of the transition to determine the optimal RF WURST pulse parameters. With these pulses, we can now use the same sequence as at the end of the previous chapter to provide conclusive evidence that the measured electron _T_ 1 is limited by Purcell decay. In Figure 6.4, driving both _RF_ 5 and _RF_ 7 before the recovery wait now leads to a significant increase in the measured _T_ 1. These closely driven spins are therefore definitely in the Purcell limit, since _T_ 1<sup>_e∫T_</sup> 1<sup>_P_.Since we are confident that</sup> the resonator is the main decay channel, we can also investigate the effect that different _RF_ pulses have on the decay dynamics. In Figure 6.5, we compare five sequences that manipulate the population differently. When both pulses are used, we see the much longer _T_ 1<sup>_e_relaxation.Itdoeseventuallyrelaxifleftforlongenough,butatamuch</sup> longer _T_ 1 of 90 s. When neither pulse is used, we see the proper _T_ 1<sup>_P_decay.However,</sup> 

Pulsed ESR in the Purcell limit 

116 



<!-- Start of picture text -->
Purcell Fit: T 1 e = 1.8s<br>no Purcell Fit: T 1 P = 340s<br><!-- End of picture text -->

Figure 6.4: Measurement of the Purcell rate of the system. Two consecutive inversion recovery measurements are shown. In the first, applying both _RF_ 5 and _RF_ 7 before and after the recovery wait allows the population to be moved off resonance with the resonator, suppressing Purcell relaxation. The second is the identical sequence without the RF pulses being played. There is clear contrast between the sequences, proving that the electron spins are Purcell-limited. 



Figure 6.5: wait, showing a difference in saturation value and recovery rate. b) A measurement of the spin-lattice _T_ 1 for longer wait durations, made by moving the population off resonance with _RF_ 5 and _RF_ 7. There appear to be two decay rates, with the slow rate having an amplitude 2.6 times larger. 

Pulsed ESR in the Purcell limit 

117 

when only a single pulse is used, we see that the inversion still recovers at the Purcell rate _T_ 1<sup>_P_butsaturatesathalftheamplitude.Thisisbecausethepopulationthatis</sup> not on resonance with the resonator due to the _RF_ 5/ _RF_ 7 pulse does not decay during the sequence, whereas the population left on resonance does. The most interesting sequence is when only an _RF_ 6 pulse is used, since we see that the population decays at a similar rate to _T_ 1<sup>_e_.This isa surprising result,since we would naively expect the spin</sup> system to still decay with the Purcell rate along the other transition in the doublet. This can be explained by considering two sub-ensembles with a detuning that is fixed on the timescale of the experiment. 

To clarify how these two populations lead to this behaviour, we consider Figure 6.6, where the same sequence is now considered with a pair of populations that have a constant broadening mechanism. Many typical detunings will not be constant with time; spectral diffusion, for example, would not cause this effect. We can identify at least three broadening effects that would cause this, though there are probably more. The first possibility is strain broadening from the resonator. Due to the differing coefficients of thermal expansion between the silicon substrate and niobium film, once the system is cooled, the resonator will apply strain to the lattice. This generates a spatially varying, but crucially temporally fixed, detuning [126]. Since we are probing spins as close to the inductor as possible, we would see the strongest effect. Similarly, the mass effect from nearby silicon-29 and silicon-30 would also leave spins with a fixed detuning. Finally, instantaneous diffusion could also be a culprit. The dipolar coupling between resonant spins that are both refocused by the echo would also be constant on the timescale of an experiment. 

Crucially, this means that population one (labelled in cyan) is only on resonance with the resonator when in the _mF_ = _≠_ 1 state for _F_ = 4 or the _mF_ = _≠_ 2 state for _F_ = 5, due to its fixed positive detuning. Conversely, population two (labelled in red) is only on resonance with the resonator when aligned with the other transition, due to its fixed negative detuning. Since spins will only be excited and see an enhanced relaxation rate when on resonance with the resonator, this leads to different dynamics in both the inversion and relaxation sections of the sequence. 

We can therefore consider two sub-ensembles within each initial _mF_ state, highlighted by the colour of the transition that they interact with. The key difference, making the initially non-resonant populations relevant, is that the _RF_ pulses address all spins irrespective of their detuning. The resonator is selective enough to distinguish per spin: only correctly detuned spins are excited by the inversion pulse, but both types are driven by _RF_ 6. During the inversion recovery sequence, spins excited by the resonator are moved far enough off resonance to decay slowly via Purcell relaxation. Using Eq. 3.89, we can calculate the new expected decay rate for a detuning of 

Pulsed ESR in the Purcell limit 

118 



Figure 6.6: Explanation of the two sub-ensembles. a) Due to the system’s broadening mechanisms, many individual spins (sharp peaks) form a Gaussian envelope. Since this broadening is wide compared to the transition spacing, the two distributions overlap. b) Since the distributions overlap, spins with a fixed detuning from both _mF_ levels will fall within the resonator bandwidth. On the left, this population is highlighted with the respective transition colour. c) The RF pulse drives the populations into the opposite _mF_ level. If the per-spin detuning is constant on the timescale of an experiment, they will be shifted outside the bandwidth of the resonator. The reverse process can also happen, putting previously off-resonance populations within the resonator bandwidth. 

Hyperpolarisation 

119 





Figure 6.7: Explanation of the ENDOR contrast by considering two sub-ensembles. When away from an RF transition, only spins in the _mF_ = _≠_ 1 state with an initially negative detuning are on resonance and so can be excited by, and relax via, the resonator. These spins are highlighted cyan to represent the transition they interact with. Similarly, spins in the _mF_ = _≠_ 2 state must be positively detuned to be on resonance with the resonator; this population is highlighted in red. a) Off resonance from an RF transition, only the correctly detuned spins have been excited. This leads to a negative echo amplitude. b) RF pulses drive all populations, so both the _F_ = 4 and _F_ = 5 _RF_ 5 transitions are inverted. The red transition has no red spins on resonance and the blue transition has equal populations in both states, so the echo amplitude is zero. c) The _RF_ 6 pulse swaps both ground-state and excited populations. This leaves a positive effective polarisation since the _F_ = 5 spins are no longer on resonance. d) The symmetrical case to b) again leads to no echo. 

###### 1.47 MHz: 



This is a reasonable result considering the purple trace in the 

With this new model, we can now explain the ENDOR results measured previously. In Figure 6.7, we explicitly do this for the three peaks across the transition. 

#### **6.2 Hyperpolarisation** 

Now that we have a deeper understanding of the system and have shown both nuclear spin control and Purcell-limited _T_ 1, we can hyperpolarise the nuclear spin state. We start with a polarisation sequence that takes population from the nearest _mF_ levels. However, given that in each _mF_ spin level there are two populations that can be accessed by the resonator, we can theoretically put these into the correct spin state to be on resonance. This should allow a fourfold signal improvement, despite still only accessing the two nearest _mF_ levels. The sequence is shown in Figure 6.8, and 

Hyperpolarisation 

120 



Figure 6.8: a) The sequence used to hyperpolarise the nuclear spin state, using population from only the nearest neighbour transitions. b) Comparing the echo amplitude between the first and second polarisation iterations shows a marked increase in the measured signal. c) The echo amplitude measured after each subsequent application of the polarisation sequence. The gain is normalised by an initial measurement made before the first iteration. The first polarisation sequence makes a large difference, with repeated applications decreasing the signal. 

is composed of a series of pulses separated by relaxation delays<sup>1</sup> . Each subsequence is designed to position a pair of populations across the Purcell-enhanced transitions, using the non-unitary effect of relaxation to combine their populations. By waiting multiple _T_ 1<sup>_P_sbetweeneachsubsequence,wecancombineasignificantfractionofthe</sup> population pair. The sequence clearly works, in that there is a clear increase in the echo amplitude; however, the gain is half as much as expected. We also see that the improvement after the first polarisation repetition saturates, and future sequences only have negative effects on the polarisation. This is less surprising, since with perfect pulses all of the population should be polarised after the first sequence. 

To improve upon this, we consider a sequence that uses all of the accessible population from all the _|_ 4 _, mF Í_ levels. Given the increased complexity here, we design one sequence that can be played repeatedly to increase the population in the relevant levels from all initial values of _mF_ . We also want to make use of both negatively and positively detuned spins to get the maximum possible improvement in echo intensity. The sequence is shown in Figure 6.9 and requires only three subsequences separated by two relaxation waits. Again, we make an echo measurement before polarisation to normalise the trace; this does mean that, if the population is already polarised to some 

1 Simpler sequences were tried, but none showed a measurable population increase. 

Hyperpolarisation 

121 



Figure 6.9: a) Hyperpolarisation sequence used to combine populations from all levels of the spin system. b) Resulting echo gains after each application of the sequence. Repeated applications of the sequence increase the measured signal, with diminishing returns. After five repetitions, the sequence negatively impacts the polarisation. 

Nuclear _T_ 1 

122 



<!-- Start of picture text -->
Data<br>Fit: T 1 n = 72 mins<br><!-- End of picture text -->

Figure 6.10: Measurement of the nuclear _T_ 1 through the decay rate of the hyperpolarised state. The echo amplitude is measured to normalise the trace, then the polarisation sequence from Figure 6.9 is applied five times. Over the course of three hours, the echo amplitude is repeatedly measured, showing a slowly decaying amplitude. The characteristic timescale of this decay is more than an hour. 

degree, the measured gain will decrease. This sequence shows a more gradual increase in gain, peaking at a higher value, meaning more population has been hyperpolarised by the sequence. The amplitude gain peaks at five iterations, which corresponds to the number of repeats needed to move population from the _mF_ = +4 state to _mF_ = _≠_ 1, the first state resonant with the resonator. We therefore infer that at least some population is being retrieved from this lowest-lying state. After the fifth iteration, the curve decays, likely due to RF pulse infidelity. The theoretical maximum gain from this sequence is ninefold, which is far from what was measured, suggesting there is more physics to be explored. 

#### **6.3 Nuclear** _T_ 1 

Given that we have achieved some level of polarisation, we can now measure the rate at which population decays back to thermal equilibrium, _T_ 1<sup>_n_.Todothis,wefirstrun</sup> an echo measurement to get a pre-polarisation normalisation, then run the polarisation sequence. After polarising, we can continuously make Hahn-echo measurements, monitoring the echo amplitude until it returns to the pre-polarisation level. In Figure 6.10, we show a measurement of the population over the course of 3 hours, where we see a gradual decline in the amplitude, with a decay constant of 72 minutes. Given 

Nuclear _T_ 1 

123 



Figure 6.11: Comparison between the hyperpolarised-state decay rate in time and due to the number of system excitations. a) Two _T_ 1<sup>_n_measurementswithdifferent</sup> measurement spacings. The blue measurement was made with a 2 minute spacing between each polarisation check, but 20 averages were used to measure the amplitude. The green trace was made with a 4 minute spacing between measurements, and 10 averages. The decay in time is similar. b) The same measurements, but plotted against the total number of times the system has been excited. The large difference in decay rate signifies no correlation between the number of excitations and how quickly the hyperpolarised state is lost. 

the low temperature and low frequency of the nuclear spin transitions, there are limited mechanisms that allow for spontaneous spin flips. One potential limiting factor of _T_ 1<sup>_n_couldbeourmeasurementofit:bycontinuouslyexcitingtheelectronspin,a</sup> flip-flop mechanism is possible whereby the electron spin decays via a change in nuclear spin state. To determine whether this is a limit in this case, we repeat the same measurement with two different delays between probing the system. In each we use a different number of excitations per Hahn-echo measurement, as shown in Figure 6.11. This means we can compare the decay rate against both time and the total number of excitations. There is a much stronger correlation with time, identifying this as the more significant factor. The large discrepancy between the decay rates as a function of excitation number convincingly shows that the repeated Hahn-echo measurements are not limiting the measured _T_ 1<sup>_n_.Thisphysicallymakessense,sincewearestrongly</sup> in the Purcell limit, so decay back into the same initial state is strongly enhanced by the resonator. Given that for the flip-flop process the spin would need to decay at a different frequency from the resonant transition, the probability of this process scales based on the relative rates of _T_ 1<sup>_e_and</sup><sup>_T_</sup> 1<sup>_P_.Wecanassignabranchingratioforthe</sup> probability of this happening: 



Cooperativity 

124 



Figure 6.12: Rates-model analysis for the hyperpolarised state. We solve the coupled differential equations for the population transfer in the _F_ = 4 manifold numerically to determine the population dynamics, assuming only _|_ ∆ _mF |_ = 1 transitions are allowed, and that the system returns to equal populations in all states as _t æ Œ_ . a) Using _T_ 1<sup>_n_=</sup> 72 min and an initial polarisation of twice the Boltzmann population, the populations of each _mF_ state are plotted as a function of time after polarisation. b) Comparison between pure exponential decay with rate _T_ 1<sup>_n_andthesumofthe</sup><sup>_mF_=</sup><sup>_≠_1and</sup> _mF_ = _≠_ 2 populations. The model predicts a faster-than-exponential decay initially, which slows substantially when approaching equilibrium. 

where _÷_ is the probability that a spin decays via spin–spin or spin-lattice relaxation. Given the low probability, we can see that the resonator strongly suppresses this process. To track how the spin population decays from the polarised state back to thermal equilibrium, we can numerically solve a series of differential equations that represent each state. In Figure 6.12, we solve for the time evolution of the spin population, assuming _T_ 1<sup>_n_basedonthemeasurementsabove.Theconsequenceofthemanycou-</sup> pled levels is that the decay is no longer purely exponential. The decay rate of the populations in the resonant levels is strongly dependent on where in the thermalisation process we are. By comparing the decay of the two relevant populations to a single exponential, we see that initially the model predicts a faster-than- _T_ 1<sup>_n_decay rate.</sup> However, towards thermal equilibrium, it becomes much slower than the exponential decay. We see this in the left plot, where even after 24 hours there is still a reasonable population difference. To measure the system dynamics more deeply, a way to reset the polarisation would be critical. 

#### **6.4 Cooperativity** 

For a quantum memory, we require unit cooperativity. Therefore, for this device to be a viable option, it must be capable of reaching that point. Using the same method as in §5.2, in Figure 6.13 we again make continuous-wave measurements 

Discussion 

125 



<!-- Start of picture text -->
Data<br>Fit<br><!-- End of picture text -->

Figure 6.13: Fit of the change in resonator bandwidth due to the spin ensemble using Eq. 5.2. The fit yields _g_ ens = 449 kHz and _“_ = 14 MHz. 

on the spin ensemble in an unpolarised state to determine _g_ ens in thermal equilibrium. We can therefore calculate the cooperativity using Eq. 3.71: 



The decrease in _Ÿl_ has compensated for the change in spin number. However, as before, this is not enough to reach _C_ = 1, even if the nuclear spin were fully polarised. 

#### **6.5 Discussion** 

We have shown a clear increase in the spin population using the nuclear spin control techniques developed; however, the polarisation level achieved is still significantly less than what should be possible. To understand the relevant processes more deeply, we suggest that a way to quickly reset the system would be necessary. One easy way to do this would be a local heater or laser excitation of the system. 

_T_ 1. By employing BIR pulses [127], efficient adiabatic _fi/_ 2 rotations could be used to determine the nuclear spin _T_ 2, which should also be very long. Another unexplored avenue on this device is the control of local silicon-29 nuclear spins, which could be a useful memory register. 

One key limitation of this system is that, at a clock transition, the _T_ 2 becomes limited by direct flip-flops between resonant spins [17]. Given that this protocol ef- 

Discussion 

126 

fectively increases this number, this will eventually begin to limit the _T_ 2. Increasing cooperativity would then come at the expense of coherence time. It is therefore better to look for a spin-ensemble candidate that can still maintain high coherence times even at high spin concentrations. For achieving unit cooperativity, we look to rare-earth spin ensembles, which have already shown cooperativities well in excess of unity [128]. 

# **Chapter 7** 

# **Unit cooperativity with Yb:YSO** 

From the low cooperativities measured in the previous chapters, with Bi:Si devices using a thin implanted layer, we argue that reaching unit cooperativity will be difficult in that system. For this chapter, therefore, we change the approach to use a rare-earth spin ensemble with electron spins grown throughout the crystal. Rare-earths ions in this configuration are regularly seen to have cooperativities _C ∫_ 1. Nd:YSO devices, for example, have been measured with _C >_ 200, and Yb:YSO with _C >_ 10 [18]. This substantially reduces the difficulty of reaching the _C_ = 1 critical point. 

In this chapter, we develop an input-output theory model of a spin system coupled to a resonator. We From this, we generate analytical expressions for the system efficiency. then make measurements of a Yb:YSO crystal coupled to a superconducting resonator, and show how the cooperativity can be dynamically tuned to the optimal point. Then, we use the model to quantitatively explore the efficiency and the optimal operating conditions for a RAQM. Finally, we consider how a spatially varying _B_ 0 field could be used to encode a spatial dependence on states stored within the ensemble 

#### **7.1 An input-output theory model of ESR** 

To quantitatively analyse the later results, we start by building an appropriate model that captures the time dynamics of the system. We are particularly interested in two key quantities, the first being the efficiency of the total system. This asks: given the energy contained in the initial pulses reaching the waveguide-resonator system during a write cycle, what fraction of this energy is captured into the detection chain during the first echo? This is a key figure of merit, since if this device were to operate as a The second quantum processor, it would determine the storage and retrieval efficiency. figure we wish to determine is the efficiency of the resonator-spin system. This asks: given a photon packet that couples into the resonator, what fraction of this energy is retrieved back into the resonator from the echo? This second first efficiency effectively ignores factors like poor coupling due to an inappropriate choice of _Qc_ , and the 3 dB 

127 

An input-output theory model of ESR 

128 





Figure 7.1: Schematic of the relevant couplings and for an input-output theory model of a spin ensemble coupled to a superconducting resonator. The notched coupling scheme means we consider both right-propagating and left-propagating fields ( _r_ and _l_ ) into the coupled CPW. Because of this, the resonator mode couples into both right/left-propagating fields with rate _Ÿc/_ 2. To model dynamics between coherent and incoherent states, we distinguish ‘bright’ and ‘dark’ states, with a coupling Γ between them. The bright state is then coupled to the cavity with rate _g_ ens. _Ÿi_ covers the intrinsic losses not due to the spin ensemble. 

loss of power due to the notched coupling scheme. As predicted in §3.3.3, we expect the spin-resonator efficiency will be unity at the _C_ = 1 point. With an appropriate model of the system, we can prove that this is the case for our device. 

For the theoretical model we use input-output theory [129, 130], which allows us to determine the occupation of the resonator mode during both the input pulse and the first echo. In Figure 7.1 we show a diagram of the model used, including the relevant driving fields. To account for the notched coupling geometry, we use the result from [131]. Here, we can correctly extract the field arriving at the output port of the PCB and into the detection chain by separating the rightward- and leftward-travelling fields. We define two bosonic modes relevant to the system dynamics: _a_ and _b_ . Here, _a_ represents the occupation of the resonator, and _b_ is a fictitious mode representing the so-called Dicke ‘bright state’ [80]. This mode couples into the Dicke ‘dark state’, a memoryless mode that can no longer couple back into the resonator. The physical 

An input-output theory model of ESR 

129 

reasoning for this separation is due to the vastly coupling rates that appear in the spin-resonator system. As we saw in Chapter 3, an inhomogeneously broadened spin ensemble typically has a very low emission rate into a coupled cavity. However, if we can control the dynamics so that the spins are all in phase, this indistinguishability can lead to superradiant bursts that drastically increase the emission rate into the cavity with the square of the number of spins. Given the large number of spins in the ensemble, this drastic difference acts like a binary switch that allows us to vary the spin-resonator coupling at will. When the spins within the ensemble are in phase (coherent), we have an effective spin-resonator coupling _g_ ens _¥ g_ 0 _ÔN_ . When they are out of phase, this is reduced by a factor _ÔN_ to _g_ 0. This means that, within the timescale of a single pulse sequence, we can effectively ignore the incoherent coupling into the ensemble, and only emit into the cavity when the phases have been refocused by our control pulses. We therefore simplify these dynamics by splitting the spin part of the model into the bosonic mode _b_ , which is coupled to the cavity with rate _g_ ens, and the spin input/output port _s_ , which is not coupled to the cavity. The effective coupling between these two will then come from the dephasing rate of the ensemble, which in turn comes from the range of frequencies excited by the input pulse. We could reduce the model further by removing the second bosonic state _b_ , and considering an output port with coupling rate _Ÿs_ . However, including this extra mode allows for more complex dynamics that are particularly relevant in the high-cooperativity regime. Using the sign conventions in [132], we can define the boundary conditions for this model: 







Here, _l_ out is the leftward-travelling arriving at the output port and _l_ in is the leftward-travelling input mode from the right port. The rightward-travelling modes _r_ out and _r_ in are therefore similarly defined. The energy absorbed into, or emitted from, the inhomogeneously broadened spin ensemble is given by _s_ out and _s_ in, respectively. The coupling rate _Ÿc_ is as defined before, and represents the coupling rate between the PCB waveguide and the resonator. The coupling rate Γ represents the dephasing rate of the spin ensemble (1 _/T_ 2<sup>_ú_)andisgivenbytheinhomogeneouslinewidthofthe</sup> excited spin packet. Given these boundary conditions, we can write the equations of 

An input-output theory model of ESR 

130 

motion (EOMs) for the two bosonic modes in the rotating frame of the pulse<sup>1</sup> : 





Here, ∆0 and ∆ _s_ represent the frequency detuning between the pulse and the bare frequencies of the modes _a/b_ : ∆ _{_ 0 _,s}_ = _Ê_ p _≠ Ê{_ 0 _,s}_ . The rate _Ÿl_ is the total loss rate of the resonator mode _a_ in the absence of the spins, and so can be written as _Ÿl_ = _Ÿc_ + _Ÿi_ , where _Ÿi_ groups all of the non ensemble related losses, like TLS couplings and radiative losses<sup>2</sup> . Using this convention, we therefore expect _Ÿl_ and _Ÿc_ to be field-independent quantities. The final constant is _g_ ens, as defined in §3.3.2, which represents the coupling between the spin ensemble and resonator modes. A true description of the system would require considering each spin individually, and building an effective _g_ ens from their respective _g_ 0s. However, due to the high spin number, this becomes impractical. For our purposes, we allow variation of the constant field _B_ 0, and so the number of spins on resonance, to tune the value of _g_ ens. 

If we assume a known power gain _G_ of the detection chain and an impedance _R_ of the detector, then the energy at the output of the device can be calculated from the measured voltage through: 



If we the energy as the fraction: 



then, due to the signal path having the same gain and detector impedance, this becomes: 



Using our model, we can now write down the above based on experimentally measured voltage. In this case, the round-trip efficiency will be given by 



Here, _t_ 0 _,_ 1 are two separate integration periods, during the initial excitation ( _t_ 0) and 

> 1We do not include a thermal occupation term in the EOMs here, since all of the pulses and echoes are well beyond the few-photon limit, and so these terms will not affect the dynamics. 

> 2 We choose the convention that _Ÿi_ represents intrinsic losses and any additional spin-related losses are given by _Ÿs_ , so that _Ÿl_ = _Ÿi_ + _Ÿc_ + _Ÿs_ . 

An input-output theory model of ESR 

131 

the emission of the echo ( _t_ 1). We restrict the second integration time to only the first echo, despite subsequent emissions from the ensemble being possible. Again, this comes from the view of using this system as a quantum memory, where we should retrieve all of the stored state during a single readout window. The measurement of the numerator is trivial: _r_ out is the echo signal measured through the detection chain. Measuring the denominator is trickier: without multiple cool-downs or a switching mechanism, we cannot measure the input pulse directly. However, we can measure an approximation if we drive the system with a calibration pulse of sufficiently large detuning (∆calib _∫ Ÿl/_ 2). This avoids exciting the resonator at all. If we assume _g_ ens = 0 and _l_ in( _t_ ) = 0, then the EOM for the resonator in the lab frame becomes: 



To understand the frequency response, we take the Fourier transform: 



We can then the resonator occupation as a function of drive frequency: 



˜ which tends to _|a_ ( _Ê_ ) _|_ = 0 as ∆0 _æ Œ_ . From the Fourier transform of the boundary condition using ∆0 = ∆calib: 



assuming flat gain profiles from the amplification/attenuation into the fridge across the region of interest, we can say: 



and therefore calibrate the input pulses using: 



The procedure to calibrate the input pulse amplitude without needing to make changes to the sample is then as follows. First, we acquire a trace with the excitation pulse strongly detuned from the resonator. Then, we use this as a proxy measurement for the input pulse for the real experiment. Using a VNA, we can easily sweep the frequency 

An input-output theory model of ESR 

132 

around the resonator mode and set the detuned pulse frequency close enough to the resonance that the gain profile is similar, but far enough away that the pulse will not be deformed by it. 

To understand the system better, we can split the round-trip into three separate pieces: input, output, and storage. We then define: 



Here, for memory operations, _÷_ in _÷_ out becomes the read efficiency, and _÷_ store any state corruption due to storage in the memory. Within the framework of the input-output model, the write efficiency would be given by: 



The storage is: 



and the read is: 



The product _÷_ in _· ÷_ store _· ÷_ out then reduces to the in Eq. 7.9. To solve for these efficiencies, we start again by taking the Fourier transform of the system in the laboratory frame: 



This can be conveniently written in matrix form: 



As we saw from Eq. 7.12, the susceptibility of the individual systems can be written 

An input-output theory model of ESR 

133 

as: 



We can simplify the leftmost matrix: 



We can then solve for _a_ ˜ and<sup>˜</sup> _b_ by multiplying by **_A_**<sup>_≠_1</sup> : 



We now consider the system during the excitation part of the sequence to determine the output drive into the spin ensemble as a function of the input. We can therefore ˜ ˜ use _s_ in =<sup>˜</sup> _l_ in = 0 and determine the field at _s_ out: 



˜ Similarly, we consider the output during the echo emission, where _r_ in =<sup>˜</sup> _l_ in = 0: 



We choose to determine the at _r_ ˜out rather than considering the exact reverse process to the above (˜ _s_ in _æ_<sup>˜</sup> _l_ out), which would take us back to the port we started at. This is simply because _r_ ˜out leads to the output port and so to the detection chain. Given the symmetry in the model, both fields will be the same. 

This shows, at least within the scope of the model, that under the same drive the system is symmetric. If we assume a continuous tone is used to drive the system, then using the efficiency definitions above<sup>3</sup> : 



An input-output theory model of ESR 

134 

and: 



where we have assumed in both cases that the pulse is spectrally narrow enough that _–_ 1( _Ê_ ) is approximately constant across the frequency range of the pulse. This therefore becomes an upper limit to the efficiency, which is decreased based on the spectral overlap of the driving pulse and _–_ 1. Given that for a signal to be emitted from the ensemble it must first have been absorbed, and so already filtered once, we would In the generally expect higher output efficiencies than input efficiencies for real pulses. ideal case, however, this directly leads to the input and output efficiencies being the same. In both cases we would determine an efficiency: 



For _Ê_ 0 = _Ês_ and away from strong coupling ( _g_ ens _< Ÿl,_ Γ), this peaks at _Êp_ = _Ê_ 0 = _Ês_ , so we a maximum find efficiency: 



which can be rewritten in terms of the cooperativity _C_ : 



where we have used _Ÿl_ = _Ÿi_ + _Ÿc_ . This gives some useful insight into the optimal conditions to drive the system. Firstly, the factor of 1 _/_ 2 comes from the notched coupling. Whilst this setup was convenient for rapid testing of multiple resonators simultaneously, it caps the overall efficiency due to effectively having two output ports to the system. The second term is the same as the directivity _D_ defined in §3.2, and it determines the fraction of photons coupled out into the waveguide compared to those dissipated by intrinsic losses. It approaches 1 as _Ÿi π Ÿc_ , so to increase this term we therefore want to produce resonators with very low intrinsic losses and overcouple them to the output port. The final term is the same as the result found in [33], which describes the efficiency of getting photons out of the spin system and into the resonator mode. It also peaks at unity for _C_ = 1, the critical point we are trying to measure. Crucially, we see that the intrinsic resonator losses enforce a penalty for occupation of the mode _a_ , which means the efficiency of absorption and emission no longer necessarily peaks at _C_ = 1. Since _C_ is implicitly dependent on our choice of _Ÿc_ , we can determine the best coupling choice for the overall efficiency based on varying system parameters. Given that _Ÿi_ is fixed by fabrication, we assume this is a fixed parameter of the system. 

An input-output theory model of ESR 

135 

In the weak coupling limit, the spins simply look like an additional loss channel to the resonator [133]: 



where _Ÿl_ = _Ÿi_ + _Ÿc_ + _Ÿs_ , the is then: 



We can the turning point as a function of _Ÿc_ for the optimal coupling choice: 



This determines that the best is achieved when: 



This is simply a restatement of the impedance-matching condition: the system ciency is maximised when the external coupling rate matches the system losses. The efficiency at this point is then: 



which is the same result as that found in [134], but for a notched coupling scheme. In this notation, the optimal cooperativity is then: 



This is strictly smaller than one but approaches it as _Ÿi æ_ 0. Beyond the most basic case, it becomes difficult to optimise analytically, so in Figure 7.2 we numerically solve the model for the parameter regimes relevant for this experiment. We plot the optimal conditions as a function of _Ÿc_ and _g_ ens. 

The optimal cooperativity now becomes larger than one, approaching it as the pulse bandwidth increases. If the input pulse bandwidth is made larger than that of the cavity, it then becomes beneficial to increase the spin losses past the impedancematching point to fit more of the pulse within the cavity bandwidth, pushing the optimal _C >_ 1. As already mentioned, this is also only true away from the strong coupling limit. As you approach stronger coupling, the spin-resonator system splits into two polariton peaks found in §3.3, and it is no longer ideal to drive at their bare frequencies, but instead at the new hybrid-system eigenfrequencies. 

We saw above in Eq. 7.33 that in the narrow-band limit, the measured input/output 

An input-output theory model of ESR 

136 



Figure 7.2: Optimal parameters for pulse lengths using _Ÿi_ = 100 kHz and Γ = 800 kHz. a) Measurement of the output efficiency _÷_ out as a function of the system _g_ ens; the longer pulse length peaks at a higher efficiency and lower _g_ ens. b) The same sweep plotted as a function of the total cooperativity, _C_ . The maximum possible efficiency, _Ÿc/_ 2 _Ÿl_ , is shown as well as the narrowband limit, which reaches the maximum at _C_ = 1. c) Measurements of the maximum input efficiency _÷_ in as a function of _Ÿc_ . For each point, _g_ ens was swept to find the maximum efficiency for that value of _Ÿc_ . d) The measured cooperativity at the maximum efficiency, showing the approach to _C_ = 1 at large values. 

An input-output theory model of ESR 

137 

spin-resonator like term. Given that, for a specific cool-down, the only tuning parameters available in our experiments are the pulse parameters and _g_ ens. We ask if there is a way to directly measure the efficiency of retrieving states from the spin ensemble into the resonator, that does not rely on the waveguide-resonator coupling? This means we want to account for all of the energy that does not couple back into the dark state during the echo, irrespective of where it couples afterwards. The fraction of energy that immediately recouples would be given by: 



We therefore the of this reduced system as: 



where _÷_ sr is this reduced ‘spin-resonator’ and _t_ 1 is the integration period during the echo. We can measure _s_ in indirectly through the output port, but cannot measure _s_ out. We do know, however, that as long as _s_ in = 0<sup>4</sup> , by refocusing the spin ensemble we can re-emit into the cavity again with a reduced amplitude. Importantly, we expect the pulse shape to be unchanged, up to a possible global phase shift and amplitude rescaling: 



where _s_ out( _t_ 1; _t_ ) is the from the system into the ensemble dark state during the first echo, _s_ in( _t_ 2; _t_ ) is the drive from the dark state into the system during the second echo, and _„_ is a possible phase shift due to refocusing and storage. In Figure 7.3, we show simulations from the model where the energy re-emitted into the dark state is fed back into the system, generating an echo train as might be measured using a dynamical decoupling sequence like CPMG [135]. We now consider the fraction of energy emitted during two consecutive echoes in this train: 





where _s_ ˜in( _t{_ 1 _,_ 2 _}_ ; _Ê_ ) is the frequency-domain representation of the drive coming from the spin ensemble dark state during the first/second echo. Again, we have used Parseval’s theorem to convert to the frequency domain, with the same scattering amplitudes found above. Using Eq. 7.42 allows us to relate the second echo to the emission from the 

> 4which would mean _÷_ sr = 1 

An input-output theory model of ESR 

138 



Figure 7.3: a) Simulated and second echoes from the model. _s_ out during the echo is scaled by a factor<sup>_Ô_</sup> _<u>÷</u>_ store to be used as _s_ in for the second echo. This process can be continually repeated, generating steadily smaller echoes. b) Simulated echo train for two different values of _g_ ens. For small _g_ ens values, the decay rate is close to _T_ 2. As _g_ ens increases and the system approaches _C_ = 1, a larger fraction of the energy stored in the ensemble is emitted each time. 

previous time step: 



Again, if both drives are narrow compared to _–_ 1( _Ê_ ), then it can be considered constant across the range of interest<sup>5</sup> : 



which allows us to relate the ratio of the and second echoes to _÷_ sr: 



This is useful since it can be measured without needing to know any system parameters other than the storage efficiency. Using the echo-silencing technique discussed later, we can directly measure the storage efficiency without re-emitting into the cavity. Its value will then be: 



with: 



> 5In our case _Ÿl π Ÿl_ during the input drive, and since _÷_ store is simply a scale factor, this is likely to be the case for any initial excitation 



<!-- Start of picture text -->
2<br>Na c<br>200 pm<br><!-- End of picture text -->

ESR at unit cooperativity 

140 



<!-- Start of picture text -->
171Yb Site 2<br>Measured echo<br>Chosen angle<br><!-- End of picture text -->

Figure 7.5: Measurements to align the magnetic in the lab frame to the _D_ 1 _, D_ 2 plane. Echo-detected field sweeps are measured around the field magnitude and angle where a transition is expected. Each point corresponds to the largest echo intensity for that angle. Following a specific transition with angle can be used to confidently determine the relationship between the lab and crystal frames. The axis line marks the chosen field angle for these measurements. 

of the crystal ( _D_ 1 _, D_ 2 _, b_ ) planes to the axes of the vector magnet. The resonators are fabricated on the crystal so that the _B_ 1 field they generate is in the _D_ 1 _, D_ 2 plane, with the _b_ axis pointing tangentially to the device surface. From the cut of the crystal, we know approximately the direction of these axes, but with some uncertainty. After aligning the vector field to the plane of the resonator, we then orient with respect to the crystal axes. We choose a resonator on the device with centre frequency 4 _._ 562 GHz and Q factor 5 _._ 5 _◊_ 10<sup>4</sup> . In Figure 7.5, we start by measuring the transition field for a range of angles in the _D_ 1 _, D_ 2 plane to determine the specific crystal orientation. This now gives a mapping between the lab frame and the crystal frame. We can then make more detailed sweeps across the transition under study, as shown in Figure 7.6. At an angle of _≠_ 87 degrees, we observe a strong avoided crossing and a large echo amplitude, suggesting a cooperativity greater than one. 

To take advantage of the ratios used in the arguments of the previous section, we must consider the saturation of amplifiers along the detection chain. Once they go into compression, the effective gains will be different, and so the above statement will no longer hold. In Figure 7.7, we vary the input pulse power and measure the peak amplitude. When the first amplifier begins to saturate, we see a plateauing of the measured amplitude with input power. The 50 dB drop in power required causes an issue with the pulse sequence. To get the optimal rotation with the WURST pulses for 

ESR at unit cooperativity 

141 





Figure 7.6: a) Continuous-wave measurement of the selected transition, showing an avoided crossing at the transition centre. b) Echo-detected field sweep of the same transition made on a later date. The slowly increasing systematic shift of the vector magnet leads to the transition centre being at a slightly different field. This implies a small change in the effective field angle. 



<!-- Start of picture text -->
Closed<br>Open<br>Open (50dB offset)<br>G · 10 dBm / 20<br><!-- End of picture text -->

Figure 7.7: Measurements of a test pulse with and without opening the fast switch on the microwave input. Plotting the amplitude of the switch open data with a 50 dB shift shows that this directly matches the switch attenuation in the open position. We plot a trace showing the expected quadratic relationship between input power and measured amplitude. This highlights the linear regime of the system, and an overall system gain of 63 dB. 

ESR at unit cooperativity 

142 

a reasonable pulse duration, we require these to have high output powers. This leads to a problem with the dynamic range of the spectrometer, where a 50 dB power difference between excitation and refocusing pulses is required. To resolve this, we change the triggering of the fast input switch so that it is no longer in the closed position during the excitation pulse. We can see in Figure 7.7 that this allows a dynamic -50 dB change in the driving pulse amplitude on the timescale of the pulse sequence. Only the small leakage through the switch isolation makes it to the device. We also confirm a linear gain relationship, so we can be confident that the measured signals are not being distorted by the switch. 

We next aim to measure the storage of the system _÷sr_ . To do this, we can take advantage of the _A_ [ _AA_ ]<sup>_n_</sup> _A_ and _A_ [ _BB_ ]<sup>_n_</sup> _A_ sequences used by O’Sullivan et al. in [12]. Here, we use two different types of WURST pulses to selectively emit an echo only when required. The refocusing condition will only be achieved once a pair of WURST pulses with the same parameters has been used on the system. The _A_ -type pulse will have one set of chirp parameters, and the _B_ -type pulse will have a different one. Often, it is easiest to simply reverse the chirp direction. If we start the sequence with an _A_ -type pulse, the echo will only be emitted once a second _A_ pulse is played. If we follow this pulse with a train of _B_ -type pulse pairs, the system will still see the dynamical decoupling effect of the drive without the decreasing amplitude from energy leaving the ensemble. An example of the sequence is shown in Figure 7.8. Away from the unit cooperativity point, we therefore see the same effect as in Figure 7.3, where repeatedly emitting from the system drops the amplitude faster than _T_ 2. We therefore conclude that the ‘true’ _T_ 2 of the system is 1.7 ms. 

To track the spin-resonator we wish to vary the cooperativity. The simplest way to do this is through _g_ ens. As was discussed in §3.3.3, by varying the magnetic field across the spin line, a different fraction of spins will couple to the resonator, allowing us to tune the cooperativity. In Figure 7.9, we measure an EDFS using the _A_ [ _AA_ ]<sup>_n_</sup> _A_ sequence described above, again with low-amplitude excitation pulses. We also show the measured round-trip efficiency, as calibrated using the energy of an offresonance pulse with the same parameters. It peaks at _÷_ rt _¥_ 10<sup>_≠_3</sup> , which is large in comparison to a typical ESR experiment, but is still well below a level that is useful for a quantum memory. 

The striking of the sweep is that, by reducing the excitation amplitude, we see a distinctly different lineshape from that measured in Figure 7.6. This happens because, although the high-power pulse was tuned for a _fi/_ 2 excitation, this is only an average. Many spins will be under- and over-rotated. Consider a simple Hahn echo sequence applied to two spin populations: population one, with an initial rotation angle _fi/_ 2, and population two with an initial tip angle _– > fi/_ 2. The second, over-rotated ensemble, will emit with a smaller amplitude than the first. This is since 

ESR at unit cooperativity 

143 



Figure 7.8: Comparison of the _A_ [ _AA_ ]<sup>_n_</sup> _A_ and _A_ [ _BB_ ]<sup>_n_</sup> _A_ sequences. Using a 200µs pulse duration for both pulse types, and an 800 kHz chirp for _A_ and a -900 kHz chirp for _B_ . The excitation is done with a 2.5 µs FWHM Gaussian pulse, with the fast switch open on top of decreasing the pulse amplitude. This leads to an effective flip angle _¥ fi/_ 1000. The _A_ [ _AA_ ]<sup>_n_</sup> _A_ sequence is measured below _C_ = 1, so only a small energy fraction is emitted each time. a) The _A_ [ _AA_ ]<sup>_n_</sup> _A_ data is measured in a single trace with the amplitude of each echo plotted as a function of time. The _A_ [ _BB_ ]<sup>_n_</sup> _A_ sequence requires a new measurement for each value of _n_ , since only one echo is emitted. The energy fraction coupled out of the ensemble during each echo emission in the _A_ [ _AA_ ]<sup>_n_</sup> _A_ measurement leads to an apparently faster amplitude decay rate. b) The sequences used for the measurement in a). Changing the chirp parameters of the _B_ pulse removes the refocusing condition, ensuring an echo is only emitted once an even number of both _A_ - and _B_ -type pulses have been played. 



Figure 7.9: a) The and second echo amplitudes as a function of using an _A_ [ _AA_ ]<sup>_n_</sup> _A_ sequence with low-amplitude excitation pulses ( _¥ fi/_ 1000). The excitation pulse has a Gaussian shape in amplitude with FWHM 2 _._ 5 µs, making its bandwidth wider than that of the cavity. The double-peaked shape in the first echo signifies the changing round-trip efficiency; this was obscured in earlier measurements due to the high excitation amplitude. The amplitude of the second echo is not directly proportional to the first due to the changing energy fraction emitted at each cooperativity. b) The measured round-trip efficiency as a function of field. _|V_ ( _t_ ) _|_<sup>2</sup> is integrated for both a calibration pulse detuned from the resonator and the measured echo. The efficiency is then calculated as the ratio of these quantities. 

ESR at unit cooperativity 

144 



Figure 7.10: a) Measurement of the ratio of the energy in the second echo compared to the first using _E Ã_ s dt _|V_ ( _t_ ) _|_ 2. We measure a dip in the energy emitted for the second echo at _C_ = 1, since all of the stored energy has already been emitted. b) The echo train measured at low cooperativity. Since _g_ ens is small, a small fraction of the stored energy is emitted each time. c) At unit cooperativity, all of the energy is emitted during the first echo. d) Past _C_ = 1, _g_ ens becomes larger than the optimum, and the retrieval efficiency drops again. In each trace, the measured powers are plotted on different _y_ -scales to show the change in ratio. 

it will have a smaller projection in the _xy_ plane. Beyond a _fi/_ 2 rotation, any excess energy in the excitation pulse has an inverted relationship between input and output energy. Increasing the rotation further still, beyond _fi_ , the emitted echo of the second population now has a _fi_ phase shift from the first population. This leads to cancellation between their emissions, decreasing the measured output even further. Therefore, in the high-power EDFS, the observation of the system efficiency has been obscured by the large range of rotation angles. To accurately measure the system efficiency, it is crucial that we work in the low-power regime, where no spins are rotated more than _fi/_ 2. Given the range of distances, and so _B_ 1 fields experienced by spins, it is prudent to work at as small a rotation angle as possible. 

second echoes. Well below unit cooperativity, we would expect the amplitude of the second echo to follow that of the first, scaled by _T_ 2. In Figure 7.9, we see that the amplitude of the second echo increases, decreases, then increases again as we move towards the centre of the line. Since we saw above that this will determine the spinresonator efficiency, we plot the energy ratio of the two echoes in Figure 7.10. This plot more clearly shows this behaviour, wherein the ratio of emitted energy changes with changing cooperativity. At low field, we measure an echo train consisting entirely of low-amplitude echoes. At the unit cooperativity point, the later echoes disappear. 

Comparing the model to results 

145 



<!-- Start of picture text -->
A [ BB ] n A fit Tη store =1.1 ms<br>A [ AA ] n A fit η sr= 0.96<br><!-- End of picture text -->

Figure 7.11: Comparison between the _A_ [ _AA_ ]<sup>_n_</sup> _A_ and _A_ [ _BB_ ]<sup>_n_</sup> _A_ sequences close to the unit cooperativity point. The characteristic timescale for energy decay whilst stored in the ensemble, _T÷_ store _¥ T_ 2 _/_ 2, is measured using the _A_ [ _BB_ ]<sup>_n_</sup> _A_ sequence to suppress echo emission. We then use this as a fixed parameter in a fit of _A_ [ _AA_ ]<sup>_n_</sup> _A_ , assuming a fixed fraction, _÷_ sr, is emitted each time. 

Increasing cooperativity still further causes the later echoes to re-emerge. This clearly shows that the system is passing through unit cooperativity, with the increasing spinresonator efficiency apparent there. 

In Figure 7.11, we set the to 351.66 mT, where we expect unit cooperativity, and make a second _A_ [ _AA_ ]<sup>_n_</sup> _A_ measurement. The effect is considerable: almost all of the energy has been emitted by the first echo. By using the _A_ [ _BB_ ]<sup>_n_</sup> _A_ technique, we These can suppress emission until necessary, at the cost of a reduced storage efficiency. are key tools required for operating a RAQM. Using the _A_ [ _BB_ ]<sup>_n_</sup> _A_ data as a measure of the real system _T_ 2, we can convert this to the effective storage efficiency as a function of total storage time, _÷_ store( _t_ ). Fitting the _A_ [ _AA_ ]<sup>_n_</sup> _A_ trace with this decay rate as a fixed parameter, we determine a 96% spin-resonator efficiency. Whilst this is large, we note that the measured round-trip efficiency is three orders of magnitude smaller. To understand why this is the case, we fit the measured data to the input-output model described above. 

#### **7.3 Comparing the model to results** 

Given known system parameters, we can numerically solve the EOMs in our model, determining the _a_ and _b_ mode occupations for an arbitrary drive. Then, by using the 

Comparing the model to results 

146 



Figure 7.12: Fitting the input-output model to the measured data away from the spin transitions. The detuned input pulse is used as input into the model, and the measured output acts as the fit target. A least-squares algorithm determines the fit accuracy for each value of the fitting parameter. b) The fit residuals as a function of time across the pulse, showing limited fit quality, particularly around the sharp features. From this fit, we determine _Ÿi_ = 102 kHz and _Ÿc_ = 25 _._ 2 kHz; the amplitude of the ringdown is set by _Ÿc_ and the decay rate by _Ÿl_ . 

boundary conditions and feeding the simulated _s_ out amplitude reduced by _÷_ store, we can simulate the expected echo signal. This process is not quite the same as refocusing with two WURST pulses, so we do not expect a stable phase relationship between the pulse and echo. However, given that we are most interested in power efficiency, it is acceptable to fit the absolute value of the emitted signals without concern for their phase relationship. By imposing physically motivated constraints on the constants, we can fit the measured results to the model and determine how the system dynamics change across the field sweep. 

A sensible place to start is by considering the measurements made away from the spin line, where _g_ ens for the spins coupled to the resonator will be zero. This removes the possibility of coupling into _b_ , and so totally removes the effect of Γ _/g_ ens _/_ ∆ _s_ . Also, since the driving pulses were at the centre of the resonator, we expect ∆0 = 0, leaving only two constants to fit. In Figure 7.12, we show an example trace for fitting away from the spin line, using the detuned pulse as an input and the measured signal as the target. We note a larger _Ÿl_ than was measured with the VNA. However, for the pulsed measurements, the number of photons in the cavity initially is only the thermal population. Therefore, a better comparison would be to extrapolate the VNA-fitted linewidth to the low-power limit. As the cavity occupation increases, nearby TLSs will become saturated, reducing the system loss rate. 

We now proceed to each step across the transition, _Ÿc_ based on the off-resonance measurement. We also choose to fix ∆ _s_ = ∆0 = 0, since the model strictly represents a single spin with frequency _Ês_ and an effective homogeneous linewidth Γ 

Comparing the model to results 

147 

coupled to the resonator at rate _g_ ens. As was discussed in §3.3.3, being in the regime _Ÿl π_ Γ effectively picks out a slice of the inhomogeneously broadened ensemble that we can actually drive through the filter function of the resonator. To fully include the effect of all spins, we would need to include a spectral distribution, with each spin having its own detuning and coupling _g_ 0. This, however, becomes practically infeasible, since we end up with _n_ + 1 EOMs to solve, where _n_ is the total number of spins. To solve this issue, for each field step, we consider only the spins within the resonator bandwidth, since we can only rotate these spins anyway. Then, we allow a field-varying ensemble coupling that follows the Gaussian distribution of an inhomogeneously broadened ensemble. As long as _g_ ens is not appreciably varying across the resonator bandwidth, this becomes a reasonable approximation. It does, however, mean that within the framework of the model, we should fix ∆ _s_ = 0 for all field steps. Also, since we made sure to set the pulse frequency at the centre of the resonator for each field, we can set this to zero. Finally, we choose to fix Γ across the transition. Whilst this is not physically motivated, it is necessary for the fit to converge. Since Γ is only viewed through _g_ ens and _g_ ens _<_ Γ for all the data points, we become insensitive to this parameter. By fixing Γ and letting _g_ ens vary, we cannot say much about their individual values. However, since what we are interested in is 4 _g_ ens<sup>2</sup><sup>_/_Γ,thiswillbe</sup> preserved. In the fit, we fix Γ at a large value and consider the resulting 4 _g_ ens<sup>2</sup><sup>_/_Γasa</sup> single parameter. 

Using these constraints, we can now perform the for each data point across the EDFS to determine the appropriate constants for this system. In Figure 7.13, we show the results as a function of field. We find good agreement of the echo amplitude, with a larger error in the pulse fit. This suggests that there is some variation between the detuned pulse and the actual input pulse for a specific field point. We also find some field variation in the intrinsic loss rate. Whilst surprising, it can be explained by considering spins within the ensemble that are not efficiently driven by the excitation pulse. The fixed 2.5 µs pulse is wider than the cavity bandwidth away from the centre of the line; however, with the increased losses from the ensemble, the excitation becomes narrower than the cavity towards the centre. In this regime, we have spins coupled to the resonator that are not contributing to the echo. Within the framework of the model, these spins look like an increased intrinsic loss rate. Finally, we conclude that despite the fit reproducing the echo amplitude accurately, the spikes in amplitude are not likely to be physically connected to the spin system, but instead come from noise in the experimental setup. From the model output, we calculate the maximum cooperativity of _C_ = 4 _._ 6. 

With the values of the model parameters from the we can compute the relative contributions to loss mechanisms within the system. In Figure 7.14, we compute these as a function of field. The largest fraction, coming from the pulse that either never 

Comparing the model to results 

148 



Figure 7.13: a) Results from a of the measured data. The detuned pulse is the input, and the measured pulse response and echo are used as fit constraints. For each field step, _Ÿc_ , Γ, ∆ _s_ , and ∆0 are fixed while _Ÿl_ and _g_ ens are varied. The echo is simulated with a decreased amplitude set by the value of _÷_ store measured from the _A_ [ _BB_ ]<sup>_n_</sup> _A_ data. The increase in _Ÿl_ towards the centre of the spin line accounts for spins coupled to the cavity that are not driven by the excitation pulse. b) The residual sum of squares (RSS) for each field step. There is a much larger uncertainty in the pulse fitting given the proportionally larger signal. We therefore use increased weighting of the echo residuals to generate a balanced fit. c) The simulated echo energy compared to the measured data, showing reasonable overlap. 

Comparing the model to results 

149 



Figure 7.14: All input energy comes from the input pulse, _r_ in, so the sum of the outputs must equal this value. The largest fraction of lost energy is the promptly measured _r_ out measured during the pulse. This comes mostly as a result of _Ÿc_ being only a small fraction of _Ÿl_ . The losses due to _Ÿi_ , _÷_ store, and left-coupling fields are also significant losses of the system. The total round-trip efficiency, _÷_ rt, peaks at 1 _◊_ 10<sup>_≠_3</sup> , as measured previously. 

enters the resonator or from its ringdown, is largely due to the value of _Ÿc_ being too small. Since the fraction _Ÿc/Ÿl_ appears in both the input and output efficiency relations, we lose this fraction twice. We have a similar problem with the leftward-coupling field: the half lost to this mechanism happens both during the excitation and during the echo emission. A not-insignificant fraction is also lost to retrieving the echo at _¥ T_ 2 _/_ 2, leading to a 63% drop in power. We can also use the model to simulate later echoes and calculate the expected energy ratio, as shown in Figure 7.15. We find good agreement around the centre of the transition, highlighting that we are in the correct parameter regime. There is significant divergence away from the centre, but since both the first and second echo intensities are so small this far from the transition, the uncertainty in these values is large. We see that despite the poor efficiency measured in the round-trip measurements, these values come much closer to unity. This again highlights that one of the key limiting factors in this case is not the spin–resonator coupling but the choice of _Ÿc_ . 

With this in mind, we can ask what the retrospective optimal choice of _Ÿc_ and pulse duration would be to maximise the measured efficiency. From Eq. 7.33, we know this will occur for a monochromatic pulse when _C_<sup>_Õ_</sup> = 1, where _C_<sup>_Õ_</sup> is the new system cooperativity, and if the fraction _Ÿ_<sup>_Õ_</sup> _c_<sup>_/_(</sup><sup>_Ÿi_+</sup><sup>_ŸÕ_</sup> _c_<sup>),where</sup><sup>_ŸÕ_</sup> _c_<sup>isthenewinputcoupling,</sup> is maximised. We therefore simply need to calculate the largest value of _Ÿ_<sup>_Õ_</sup> _c_<sup>where</sup> 

Comparing the model to results 

150 



Figure 7.15: Comparison of the model output to the previously measured echo fractions. For each point, we simulate the expected echo train given the system parameters and The simulated traces are included take the ratio of energy in the first and second echoes. with Gaussian noise given by the standard deviation of the noise on a measured trace. This avoids dividing by zero when calculating the energy ratio. We see reasonable agreement towards the centre of the line, which begins to diverge as the measured signal gets increasingly smaller. 

achieving _C_<sup>_Õ_</sup> = 1 is still possible. This means that: 



In Figure 7.16, we then re-simulate the sweep with this new coupling rate. This single change leads to a 60-fold improvement in the system efficiency. We also note that, due to the larger cavity bandwidth, increasing the pulse duration has a negligible effect. Even with this change, we are still well below a practically useful memory. To calculate why this is, we consider the maximum possible cooperativity _C_ max for a given (4 _g_ ens<sup>2</sup><sup>_/_Γ)</sup> max<sup>.Thisoccurswhenthereisnoexternalcouplingtotheresonator:</sup> 



The new coupling rate, _Ÿ_<sup>_Õ_</sup> _c_<sup>,thatmaximiseswillthenbe:</sup> 



Comparing the model to results 

151 



Figure 7.16: Using the maximum in measured cooperativity, we calculate the retrospective optimal choice for _Ÿc_ and re-simulate the measured spectrum. For each field point, we also calculate the expected efficiency using a monochromatic pulse, showing the extent of the difference from the long pulse duration regime. 

and the maximum _÷_ in/out is: 



where we have assumed that the new cooperativity is set to one. Using Eq. 7.16, we expect the optimised round-trip efficiency: 



where _t_ 1 is the retrieval time of the stored excitation, and _T_ 2 is the amplitude decoherence time. The route for improvement then simply comes from addressing each of these factors. The easiest change is to remove the notched coupling, for a possible four-fold improvement. Secondly, by working at _t_ 1 = _T_ 2 _/_ 20, which is readily achievable using a system with 10 ms _T_ 2 and a retrieval time of _t_ 1 = 500µs, the 36% storage efficiency jumps to 90%. With these two changes alone, the round-trip efficiency already improves by a factor of 10. Finally, by improving the maximum cooperativity by 10 or 100 times, we see that a high-efficiency quantum memory is practically realisable. 

Proposal for spatially resolved RAQM 

152 

#### **7.4 Proposal for spatially resolved RAQM** 

Given that in the previous sections we showed that there are diminishing returns for increasing the maximum system cooperativity, _C_ max, and that, for a given _Ÿc_ , the optimal regime for operating a quantum memory is _C ¥_ 1, we propose using excess cooperativity for the storage of other states within the same ensemble. For an ensemble with total cooperativity: 



the optimum memory density would be achieved by splitting the spins into _N_ individually addressable sub-ensembles. Each of these would then need: 



where _C_<sup>_n_</sup> is the cooperativity of the _n_ th ensemble. To generate these sub-ensembles, we can leverage field gradients. 

Applying a DC current ( _I_ DC) through the superconducting resonator will generate a DC magnetic field around it ( **_B_** DC( **_r_** )). Dynamically changing this current, and so the field, can then be used to move spins on and off resonance with the resonator throughout the memory sequence. In an experimental setup, we would choose the constant field _B_ 0 such that the spins are below the resonator frequency without a DC field applied. To access a certain memory bin, the appropriate current is applied so that that region of space will come onto resonance. Crucially, since the DC field generated by this process comes from the same source as the spin-resonator coupling _g_ 0, they will both have the same spatial dependence. As we saw in §3.3.1, _g_ 0 depends on the magnitude of field fluctuations _”Br_ generated by the vacuum state in the resonator at that point in space. Spins with the same value of _g_ 0 will therefore all experience the same DC field. To ensure that each memory bin has _C_<sup>_n_</sup> = 1, we first assume that _Ÿl_ and Γ are the same for all sub-ensembles<sup>6</sup> . Then, from Eq. 3.71, this means that for each sub-ensemble to be at unit cooperativity: 



Where _g_ ens<sup>_n_istheensemblecouplingofthe</sup><sup>_n_thsub-ensemble.</sup> By tuning the DC current, we want to be able to address different sub-ensembles, but all with the same value of _g_ ens<sup>_n_:</sup> 



> 6 physical locations in the sample have the same inhomogeneous linewidth. This may not always be the case, particularly where strain on the sample is induced by thermal contraction of the resonator patterned on top of it [126] 

Proposal for spatially resolved RAQM 

153 



Figure 7.17: A diagram of the setup for using DC gradients to spatially encode memory bins in a cylindrically symmetric system. The vector _„_<sup>_˛_</sup> is parallel to the field _B_ DC( _r_ ). The angle _„_ is defined from the substrate surface so that the spin ensemble is located in the range 0 _< „ < fi_ . Due to the finite bandwidth of the resonator, only spins at distances _r≠ < r < r_ + are on resonance. 

where _–_ is a current-independent constant. Then, we also require the ability to tune this constant so that: 



A simple way to ensure a ensemble coupling for each current applied is to use a radially symmetric system. By calculating the ensemble coupling of a general subensemble, we show that _g_ ens becomes a current-independent parameter. 

Figure 7.17 shows a 2D slice of a current-carrying wire above a substrate. By assuming that the wire is straight, we need only calculate the ensemble coupling per unit length for this 2D slice. Since all slices along the inductor length will be identical, we can simply multiply this by the inductor length for the ensemble coupling within the total mode volume. In this simple case, the magnitude of **_B_** DC( _r_ ) will be given by Eq. 3.57, so: 



where _µ_ is the permeability of the substrate, _I_ DC is the current through the inductor, _r_ is the radial distance from the wire, and **_„_**<sup>_˛_</sup> is the tangential unit vector as defined in Figure 7.17. Since this field may not be parallel to the existing _B_ 0, the total field experienced by the spins would therefore be: 



Proposal for spatially resolved RAQM 

154 

where _B_ tot is the magnitude of the new and _◊_ is the angle between _B_ 0 and _B_ DC. The change in the field experienced by the spins as a fraction of the field applied must then be: 



where we have expanded up to second order, assuming the quantity _B_ DC _/B_ 0 is small. For a standard ESR transition, this then becomes unreasonable since the field generated by the wire will be small compared to _B_ 0 and the angle _◊_ will be close to 90 °. You could generate a reasonable change in _B_ tot by either intentionally misaligning _B_ 0 perpendicular to _B_ 1, driving large amounts of current, or some combination of both. However, these are not ideal options: aside from the heating a large current would cause, both would reduce the _”B_ 1 component perpendicular to _B_ tot, and so the overall coupling and the maximum possible cooperativity would reduce. The solution is then to couple to an _Sz_ -style transition, which allows _B_ DC and _B_ 0 to be parallel, making the new field: 



In practice, it would not be possible for _B_ 0 and _B_ DC to be parallel for all spins since the One neat solution to field generated by the inductor is tangential to a circle around it. this would be for all of the field to be generated by _B_ DC ( _B_ 0 = 0). This would have the nice consequence of also increasing the maximum cooperativity, since every spin would be guaranteed to orient optimally. It is also a nice option for coupling the memory to a qubit, since the field can be much more localised on the chip, reducing the stray field that the qubit experiences. As we will see later, however, the zero global field solution is not strictly necessary, and any orientation of a global _B_ 0 field will also work. 

With this in mind, we consider applying a DC current to the inductor using the geometry described in Figure 7.17, with the **_B_** 0 field parallel to **_B_** DC. The resonator will only couple to spins so long as their Larmor frequency is within the resonator bandwidth _Ÿl_ . Assuming an effective gyromagnetic ratio _“_ eff, the spin frequency will be given by<sup>7</sup> : 



Then, the range over which a spin couples to the resonator is: 



and the corresponding range of radii over which spins are still on resonance with the 

> 7 We assume that this is constant, or approximately so, over the range of consideration. However, this is not necessarily the case for an arbitrary transition. 

Proposal for spatially resolved RAQM 

155 

resonator is: 



where _B_ res is the additional required for _Ês_ = _Ê_ 0. A graphical depiction showing this relationship is shown in Figure 7.17. To maximise the spatial efficiency, and so the number of bins, we can calculate the current spacing so that the outer radius of the previous bin matches the inner radius of the next one: 



where _I_ DC<sup>_n_is the DC current of the</sup><sup>_n_thbin.From this, we can calculate the appropriate</sup> current spacing: 



So long as we choose the appropriate current ratio between neighbouring bins, they will not overlap. We now calculate what the ensemble coupling of this half-ring would be. We can use Eq. 3.70 to calculate this: 



For a uniform spin number concentration per unit volume _n_ = _N/V_ , we can turn the discrete sum into an integral: 



with the assumption that all spins _N_ initially sit inside the resonator linewidth (Γ _< Ÿl_ ). If **_B_** 0 is parallel to **_B_** DC, then it will also be parallel to the vacuum fluctuation field _”_ **_B_** ( **_r_** ). Using Eq. 3.58 and assuming we are driving an _Sz_ transition, the individual spin coupling _g_ 0 as a function of distance from the inductor will also follow Eq. 3.58: 



We can then restrict the ensemble coupling to only spins that sit within the cavity 

Proposal for spatially resolved RAQM 

156 

bandwidth using _r±_ . The total ensemble coupling for a _I_ DC is: 





where _r±_ are implicitly functions of _I_ DC. Using the found above: 



which is no longer dependent on _I_ DC at all, ensuring that as long as the half-ring stays within the sample, all values of _I_ DC will lead to a sub-ensemble with the same value of _g_ ens. An intuitive way to understand why this happens is through the approximation _g_ ens = _g_ 0 _ÔN_ . The average _g_ 0 falls off as 1 _/r_ , but the number of spins in the half-ring increases quadratically, so the two effects compensate for one another. This result also shows that the specific value of the cooperativity for each memory bin can be set using the difference between the global field and the field required for a spin to be on resonance. The extra field required to put the spin on resonance is then: 



which in frequency is simply the initial spin-resonator detuning: 



Looking at Eq. 7.77, the function: 



sets the value of _g_ ens for all the bins, so their cooperativity can be easily tuned by changing the magnitude of the initial detuning with respect to the cavity bandwidth. Since we do not want bins to overlap in frequency, the initial detuning should be set to more than a few cavity linewidths. The total cooperativity, _C_ tot, is achieved with an initial detuning of zero. Due to the spatial extent of the spin system or the maximum power available for refocusing pulses, there will be experimental limitations on this 

Proposal for spatially resolved RAQM 

157 

value; however, it is experimentally determinable. We _C_ tot as: 



and the cooperativity of each bin: 

Unit cooperativity will then be achieved if: 



so the optimal initial detuning is given by: 



In the region of interest where _C_ tot _∫_ 1, the argument of coth becomes small. We can therefore Taylor expand coth( _x_ ) for small _x_ ; to first order this becomes: 



which is linear in _C_ tot, with the gradient determined by the spatial extent of spins driven by the resonator. Since _C_ tot, _r_ min, and _r_ max are often known or verifiable parameters, this gives a great starting point for operating the system. For _C_ tot = 30, _r_ min = 100 nm, and _r_ max = 100µm, this corresponds to ∆init _¥_ 4 _Ÿl_ . In Figure 7.18, we plot the locations of each memory bin within an example substrate, showing how the bins with larger radius also have an appropriately larger spatial width. By fixing the current ratio between neighbouring bins, we can also leave no space between their radii. 

###### **7.4.1 Bin cooperativity in the non-ideal case** 

If _B_ 0 is not exclusively parallel to _B_ DC, but is a constant global the symmetry enforces that the current dependence will still drop out. To show how this works in the case without perfect symmetry, we can use a finite-element solver to determine the field distribution for a realistic inductor and sample geometry, and integrate pixels to find _g_ ens. Since we care particularly about the field generated by the current in a superconducting wire, we use the COMSOL AC/DC module [136] to generate the field dependence. In Figure 7.19, we calculate the current density profile used as a function 

Proposal for spatially resolved RAQM 

158 



Figure 7.18: a) Calculated sub-ensemble locations for DC currents assuming: _f_ 0 = 4 GHz, Q = 5 _◊_ 10<sup>4</sup> , _“_ eff = 28 MHz/mT, and _µ_ = 4 _fi ◊_ 10<sup>_≠_7</sup> H/m. Each region of space has the same _g_ ens. b) By varying the DC current for each bin logarithmically, using a fixed fraction between _I_ DC<sup>_n_and</sup><sup>_I_</sup> DC<sup>_n_+1,theentireensemblecanbecovered.</sup> 

of distance across the wire, using the result from [137, 138]. Using this we the total current can calculate the field generated around the inductor as a function of applied. Taking a cut down the centre of the substrate, we see the expected 1 _/r_ dependence. Following this line cut, the spatial regions on resonance get progressively wider, proportional to the current applied. We see, however, in 2D that the global field leads to crescent-shaped regions of resonant spins, rather than the half-rings calculated previously. The global field means that where _„_ is close to 0 _/fi_ , the misalignment of _B_ 0 and _B_ DC leads to heavily reduced radii. Performing the 2D integration to numerically determine the value of _g_ ens for each current value, we again find these to all be equal and independent of _I_ DC. Since an anisotropic _g_ -tensor would similarly affect every spin equally, the symmetry for that case would still be maintained. We do, however, observe that the cooperativity of each bin is smaller due to the misalignment of _B_ tot and _g_ 0. In Figure 7.20, we calculate the ensemble coupling for all memory bins as a function of initial detuning, showing the expected dependence: 



again proving that we can tune the system to unit cooperativity. 

To practically achieve this proposal would require a galvanic connection to the superconducting resonator, allowing a DC current to flow in the inductor. This would lead to the resonator mode being strongly suppressed by overcoupling to the input. To counter this, many devices have used Bragg mirror designs [40, 140, 39], which act as high-impedance band-stop filters. A practical implementation would then simply involve coupling to the resonator through one of these. By disconnecting one side of the inductor, the galvanic access could also be used to generate a gradient electric field across the spin ensemble. The Stark shift from this field could also be used in a similar 

Proposal for spatially resolved RAQM 

159 



Figure 7.19: a) Simulated current-density distribution as a function of distance across the width of a 1 µm Nb wire. The film thickness is assumed to be 100 nm and the superconducting penetration depth 49 nm [139]. b) COMSOL output of the DC _Bx_ field generated by a total current of 0.2 mA. The contours show crescent-shaped regions of equal field within the substrate. c) Line cuts of the field along the central axis in b) for differing _I_ DC. Using _B_ res = 15 µT and the same resonator parameters as in Figure 7.18, we show the width across which spins would still be on resonance. 

Proposal for spatially resolved RAQM 

160 



<!-- Start of picture text -->
Bin:1<br>Bin:2<br>Bin:3<br>Bin:4<br>Bin:5<br>Analytical dependence<br><!-- End of picture text -->

Figure 7.20: Simulated ensemble couplings as a function of initial resonator detuning. For each value of ∆init _/Ÿl_ , the optimal currents are rechosen so as to have no spacing between bins, for a total of five values starting at 0 _._ 2 mA. For small initial detunings, the bin falls outside the sample, leading to a drop in measured _g_ ens. The change in _g_ ens follows the same dependence calculated in Eq. 7.87. 

way to the above discussion. 

This implementation is complementary to the phase-encoding procedure shown in [12]. The total number of states that can be stored in the memory is multiplicative with the bin size of each encoding: 



where _m, n_ are the number of states that can be stored and retrieved by the two methods. We also consider the first-in last-out (FILO) encoding in [32, 41]. This, while not randomly accessible, could still be useful within an appropriate algorithm: 



where _l_ is the number of FILO states that can be stored within a bin. Assuming 100 FILO states per bin, 10 spatial bins, and 10 phase bins, we can already store a possible 10,000 distinct states within the memory. The spatial encoding system could also be extended further by working in 2D using a pair of currents or a current-voltage combination. With this scalability in mind, we see how high-density storage of quantum states can be practically achieved using spin ensembles coupled to superconducting resonators. 

Discussion 

161 

#### **7.5 Discussion** 

In this chapter, we have successfully tuned a spin-resonator system to the unit cooperativity point and shown how the efficiency of storage and retrieval of microwave photons varies there. Despite the high efficiency at the spin-resonator interface, the overall system efficiency is still small. As was identified above, there are clear solutions to these problems, like operating the system in reflection, using narrower-bandwidth excitations, increasing the coupling rate _Ÿc_ , and using a spin system with longer _T_ 2. The next steps would then be to build a device in a material like Yb:CaWO4 that has shown 100 ms coherence times, whilst still achieving high cooperativities [20]. By moving the coupling to an on-chip waveguide, as was used in the previous chapters, the coupling rate _Ÿc_ can be drastically increased. This also has the added bonus that more power can reach the resonator, leading to shorter control pulses. Finally, if the on-chip waveguide is terminated in a reflective termination (0 Ωor open circuit), a lowinsertion-loss circulator placed before the chip would allow for a reflection-type setup, capturing up to twice as much power from the device. 

In the part of the chapter, we discuss a proposal for using the excess cooperativity for storing more states within the memory. A common issue in microresonator ESR is that the _B_ 1 field generated by the resonators varies quickly as you move further from it. This proposal turns that problem into a feature of the device. It is an example of how gradient-field ESR could be useful for quantum computing memory applications; however, this merely scratches the surface of what is possible. As is already well developed in NMR, the use of gradient fields allows for many advanced imaging and spectroscopic techniques. The field of microresonator ESR is ideal for the application of many of these techniques since the small feature sizes inherently lead to large spatial variation of the field. 

# **Chapter 8** 

# **Conclusions and outlook** 

The work in this thesis shows the development and use of a unit-cooperativity randomaccess quantum memory. At unit cooperativity, the efficiency with which energy is stored in and retrieved from the memory by the resonator was shown to be close to unity. Through this, we have highlighted key issues that remain in the coupling to the wider system. These issues, however, are not insurmountable, and we have detailed possible ways to account for these problems. 

In Chapter 5, we showed a novel design for on-chip control of nuclear spins. The design is fully broadband and is agnostic to both the spin system and resonator. We showed how the device can be used for ENDOR measurements of bismuth donors in silicon, using the technique to make measurements across all of the ground-state nuclear-like spin transitions at a fixed field and microwave frequency. Using the nuclear spin control, we showed that, due to the high implanted spin concentration, the longitudinal relaxation was limited by spin-spin interactions and not Purcell relaxation. 

In Chapter 6, we used the same design with a lower implanted spin concentration and showed that by moving the spin population on and off resonance with the resonator, we can change the _T_ 1 by two orders of magnitude. We then showed how the nuclear spin control can be used to access a previously inaccessible sub-ensemble that had been detuned outside the resonator bandwidth. This technique can be used to increase the effective spin concentration without requiring spins from other nuclear spin states. Finally, we used the Purcell-enhanced decay from the resonator to artificially hyperpolarise the nuclear spin, doubling the effective spin concentration. We measured the decay of the hyperpolarised state to determine an effective nuclear _T_ 1 for the electron ground state. 

In Chapter 7, we used resonators on a Yb:YSO sample to tune the system to the unit-cooperativity point. At _C_ = 1, we saw greatly enhanced efficiency at the spinresonator interface; however, the overall system efficiency was still low. Despite this, we were able to quantify the system losses and determine the steps required to reach unit efficiency. In the last part of the chapter, we discussed a proposal for using gradient 

162 

Future work 

163 

in ESR and how they could be used to create a series of unit-cooperativity subensembles. By simulation, we showed how this device could be operated within a real spin system. 

#### **8.1 Future work** 

There remain a number of unanswered questions and several directions for future work arising from this project. The most interesting of these can be split into three main themes: 

###### **8.1.1 Bismuth nuclear spin control** 

Whilst we were able to dynamically increase the polarisation of the nuclear spin above the Boltzmann steady state, the maximum polarisation achieved was less than the theoretical maximum. A more detailed study of the nuclear spin dynamics could explain this. Given the control achieved, there are also a number of other nuclear-spindependent measurements still to do. The first of these is to measure the nuclear _T_ 2; given the insensitivity of nuclear spins to noise, this could act as a very long-lived memory register that is easily accessible through the electron spin. A more detailed study of the _T_ 1 relaxation of the nuclear spin would also be important. Given the low energies available at these temperatures, there are limited relaxation mechanisms. Therefore, considering how the resonator and wider device affect these would be important if this were to be operated as a quantum memory. As has already been identified, reaching the unit-cooperativity point would be made more feasible using an isotopically purified silicon substrate and an implant profile over a much wider range of depths. 

###### **8.1.2 quantum memory** 

Given the results from Chapter 7, there are some very clear next steps towards reach unit efficiency in a quantum memory. Using a spin system like Yb:CaWO4 and adjusting the device coupling and resonator setup can drastically reduce the losses in the system. Once this has been achieved, the next step would be to use this device to store a quantum state provided by a superconducting qubit. Given the issues with operating superconducting qubits within a magnetic field, a number of challenges would need to be overcome to make this a possibility. 

###### **8.1.3 ESR** 

The possible outlook from this work would be to build a Bragg-mirror-coupled resonator that allows DC current flow through the inductor for generating magnetic 

Future work 

164 

There are a great many possible uses for this, but one key application would be operating the spatially resolved quantum memory described in §7.4. Assuming that the Yb:CaWO4 system can reach the high cooperativities found with Yb:YSO, fabricating the design on this spin system would allow for longer state storage. Another possible direction to take this idea would be very high-resolution imaging of many types of spin-active sample. With the development of single-microwave-photon detectors (SMPDs) [30], measurements down to the single-spin level are now possible. Given the techniques used in MRI, gradient-field ESR detected via an SMPD could allow for novel measurements across biology, chemistry, and physics. 

# **Bibliography** 

- [1] B. Jack Copeland. _Colossus: The Secrets of Bletchley Park’s Codebreaking Computers_ . Oxford, UK: Oxford University Press, 2006. 

- [2] Tim Dierks and Eric Rescorla. The Transport Layer Security (TLS) Protocol Version 1.2. Request for Comments 5246. RFC Editor, Aug. 2008. 

- [3] Peter W. Shor. Algorithms for Quantum Computation: Discrete Logarithms and Factoring. In: _Proceedings of the 35th Annual Symposium on Foundations of Computer Science (FOCS)_ . IEEE Computer Society, 1994, pp. 124–134. 

- [4] J. P. Buhler, Jr. Lenstra H. W., and Carl Pomerance. Factoring integers with the number field sieve. In: _The Development of the Number Field Sieve_ . Ed. by A. K. Lenstra and Jr. Lenstra H. W. Vol. 1554. Lecture Notes in Mathematics. Berlin, Heidelberg: Springer, 1993, pp. 50–94. 

- [5] Frank Arute et al. Quantum supremacy using a programmable superconducting processor. In: _Nature_ 574.7779 (Oct. 2019), pp. 505–510. 

- 

- [6] Ian Sample. Google claims it has achieved ’quantum supremacy’ but IBM disagrees. The Guardian. Oct. 2019. 

- [7] Craig Gidney and Martin Ekerå. How to factor 2048 bit RSA integers in 8 hours using 20 million noisy qubits. In: _Quantum_ 5 (2021), p. 433. arXiv: `1905.09749 [quant-ph]` . 

- [8] Élie Gouzien and Nicolas Sangouard. Factoring 2048-bit RSA Integers in 177 Days with 13 436 Qubits and a Multimode Memory. In: _Physical Review Letters_ 127.14 (2021), p. 140503. 

- [9] F. G. G. Hernandez et al. Temperature-induced spin-coherence dissipation in quantum dots. In: _Physical Review B_ 78 (2008), p. 041303. 

- [10] Manjin Zhong et al. Optically addressable nuclear spins in a solid with a six-hour coherence time. In: _Nature_ 517.7533 (2015), pp. 177–180. 

- [11] Tian Zhong et al. Nanophotonic rare-earth quantum memory with optically controlled retrieval. In: _Science_ 357.6358 (2017), pp. 1392–1395. 

165 

Bibliography 

166 

- [12] James O’Sullivan et al. Random-Access Quantum Memory Using Chirped Pulse Phase Encoding. In: _Physical Review X_ 12.4 (2022), p. 041014. 

- [13] Aleksei R. Matanin et al. Superconducting Integrated On-Demand Quantum Memory with Microwave Pulse Preservation. In: _Physical Review Letters_ 136 (2026), p. 060808. 

- [14] Alkım B. Bozkurt et al. A mechanical quantum memory for microwave photons. In: _Nature Physics_ (2025). 

- [15] Fudong Wang et al. Nuclear Spins in a Solid Exceeding 10-Hour Coherence Times for Ultra-Long-Term Quantum Storage. In: _PRX Quantum_ 6 (2025), p. 010302. 

- [16] Neil A. Gershenfeld and Isaac L. Chuang. Bulk Spin-Resonance Quantum Computation. In: _Science_ 275.5298 (1997), pp. 350–356. 

- [17] Gary Wolfowicz et al. Atomic Clock Transitions in Silicon-Based Spin Qubits. In: _Nature Nanotechnology_ 8.8 (2013), pp. 561–564. 

- [18] Joseph Alexander et al. Coherent spin dynamics of rare-earth doped crystals in the high-cooperativity regime. In: _Phys. Rev. B_ 106 (Dec. 2022), p. 245416. 

- [19] Marianne Le Dantec et al. Twenty-three–millisecond electron spin coherence of erbium ions in a natural-abundance crystal. In: _Science Advances_ 7.51 (2021), eabj9786. 

- [20] Alexey Tiranov et al. Sub-second spin and lifetime-limited optical coherences in 171Yb3+:CaWO4. In: _Nature Communications_ (2026). 

- [21] National Institute of Standards and Technology. CODATA Value: electron gyromagnetic ratio. `https://physics.nist.gov/cgi-bin/cuu/Value?gammae` . 2022. 

- [22] National Institute of Standards and Technology. CODATA Value: proton gyromagnetic ratio. `https://www.physics.nist.gov/cgi-bin/cuu/Value? gammap` . 2022. 

- [23] Aaron et al. Millisecond Coherence in a Superconducting Qubit. In: _Physical Review Letters_ 130.26 (2023), p. 267001. 

- [24] Jarryd J. Pla et al. readout and control of a nuclear spin qubit in silicon. In: _Nature_ 496.7445 (2013), pp. 334–338. 

- [25] James O’Sullivan et al. Individual solid-state nuclear spin qubits with coherence exceeding seconds. In: _Nature Physics_ 21 (Nov. 2025), pp. 1794–1800. 

- [26] John J. L. Morton et al. Bang-bang control of fullerene qubits using ultra-fast phase gates. In: _Nature Physics_ 2.1 (2006), pp. 40–43. 

Bibliography 

167 

- [27] C. D. Weis et al. Electrical activation and electron spin resonance measurements of implanted bismuth in isotopically enriched silicon-28. In: _Applied Physics Letters_ 100.17 (Apr. 2012), p. 172104. 

- [28] Jonathan D. Breeze et al. Continuous-wave room-temperature diamond maser. In: _Nature_ 555.7697 (2018), pp. 493–496. 

- [29] Hee-Jin Lim et al. Coherent spin dynamics of ytterbium ions in yttrium orthosilicate. In: _Physical Review B_ 97.6 (2018), p. 064409. 

- [30] Zhiren Wang et al. Single-electron spin resonance detection by microwave photon counting. In: _Nature_ 619.7969 (2023), pp. 276–281. 

- [31] C. Grezes et al. Multimode Storage and Retrieval of Microwave Fields in a Spin Ensemble. In: _Physical Review X_ 4.2 (2014), p. 021049. 

- [32] V. Ranjan et al. Multimode Storage of Quantum Microwave Fields in Electron Spins over 100 ms. In: _Physical Review Letters_ 125.21 (2020), p. 210505. 

- [33] M. Afzelius et al. Proposal for a coherent quantum memory for propagating microwave photons. In: _New Journal of Physics_ 15.6 (2013), p. 065008. 

- [34] Richard E. George et al. Electron Spin Coherence and Electron Nuclear Double Resonance of Bi Donors in Natural Si. In: _Phys. Rev. Lett._ 105 (Aug. 2010), p. 067601. 

- [35] Paul A. S. Cruickshank et al. A kilowatt pulsed 94 GHz electron paramagnetic resonance spectrometer with high concentration sensitivity, high instantaneous bandwidth, and low dead time. In: _Review of Scientific Instruments_ 80.10 (2009), p. 103102. 

- [36] Brian Julsgaard et al. Quantum Memory for Microwave Photons in an Inhomogeneously Broadened Spin Ensemble. In: _Physical Review Letters_ 110.25 (June 2013), p. 250503. 

- [37] V. Damon et al. Revival of silenced echo and quantum memory for light. In: _New Journal of Physics_ 13.9 (2011), p. 093031. 

- [38] V. Ranjan et al. Spin-Echo Silencing Using a Current-Biased Frequency-Tunable Resonator. In: _Physical Review Letters_ 129.18 (2022), p. 180504. 

- [39] Yutian Wen et al. Addressing spins at the clock transitions with a frequency- and bandwidth-tunable superconducting resonator. Oct. 2025. arXiv: `2510.19684 [quant-ph]` . 

- [40] parametric amplifier. In: _Science Advances_ 9.10 (2023), eadg1593. 

- [41] Hua Wu et al. Storage of Multiple Coherent Microwave Excitations in an Electron Spin Ensemble. In: _Physical Review Letters_ 105.14 (2010), p. 140503. 

Bibliography 

168 

- [42] Philip Krantz et al. A quantum engineer’s guide to superconducting qubits. In: _Applied Physics Reviews_ 6.2 (2019), p. 021318. 

- [43] Guido Burkard et al. Semiconductor spin qubits. In: _Reviews of Modern Physics_ 95.2 (2023), p. 025003. 

- [44] Colin D. Bruzewicz et al. Trapped-ion quantum computing: Progress and challenges. In: _Applied Physics Reviews_ 6.2 (2019), p. 021314. 

- [45] Xiaobo Zhu et al. Coherent coupling of a superconducting qubit to an electron spin ensemble in diamond. In: _Nature_ 478 (2011), pp. 221–224. 

- [46] Y. Kubo et al. Hybrid Quantum Circuit with a Superconducting Qubit Coupled to a Spin Ensemble. In: _Physical Review Letters_ 107 (2011), p. 220501. 

- [47] Cécile Grezes et al. Towards a spin-ensemble quantum memory for superconducting qubits. In: _Comptes Rendus Physique_ 17.7 (2016), pp. 693–704. 

- [48] E. M. Purcell, H. C. Torrey, and R. V. Pound. Resonance Absorption by Nuclear Magnetic Moments in a Solid. In: _Physical Review_ 69.1-2 (Jan. 1946), pp. 37–38. 

- [49] F. Bloch, W. W. Hansen, and Martin Packard. Nuclear Induction. In: _Physical Review_ 69.3-4 (Feb. 1946), p. 127. 

- [50] Zheng Huang and Deju Ye. MRI: A Dynamic Tool in Precision Medicine. In: _Chemical & Biomedical Imaging_ (2025). 

- [51] _Principles of Nuclear Magnetic Resonance in One and Two Dimensions_ . Oxford University Press, 1990. 

- [52] Polarization P and Magnetization m Fully Consistent with Maxwell’s Equations. In: _Progress In Electromagnetics Research B_ 64 (2015), pp. 83–101. 

- [53] S. Stoll and A. Schweiger. EasySpin: A Comprehensive Software Package for Spectral Simulation and Analysis in EPR. In: _Journal of Magnetic Resonance_ 178.1 (2006), pp. 42–55. 

- [54] Michael Berglund and Michael E. Wieser. Isotopic compositions of the elements 2009 (IUPAC Technical Report). In: _Pure and Applied Chemistry_ 83.2 (2011), pp. 397–410. 

- [55]<sup>171</sup> Yb<sup>3+</sup> :Y2SiO5. In: _Phys. Rev. B_ 98.19 (Nov. 2018), p. 195110. 

- [56] Sacha Welinski et al. High-resolution optical spectroscopy and magnetic properties of Yb<sup>3+</sup> in Y2SiO5. In: _Phys. Rev. B_ 94 (Oct. 2016), p. 155116. 

Bibliography 

169 

- [57] Dieter Suter. Optical detection of magnetic resonance. In: _Magnetic Resonance_ 1 (2020), pp. 115–139. 

- [58] E. L. Hahn. Spin Echoes. In: _Phys. Rev._ 80.4 (Nov. 1950), pp. 580–594. 

- [59] W. B. Mims. Spin Echoes from Broad Resonance Lines with High Turning Angles. In: _Physical Review_ 141 (1966), pp. 499–502. 

- [60] W. B. Mims. Envelope Modulation in Spin-Echo Experiments. In: _Physical Review B_ 5.7 (1972), pp. 2409–2419. 

- [61] Spin-Echo Envelope. In: _Physical Review B_ 6.9 (1972), pp. 3543–3545. 

- [62] Alberto Tannús and Michael Garwood. Adiabatic pulses. In: _NMR in Biomedicine_ 10.8 (Dec. 1997), pp. 423–434. 

- [63] E. Kupče and R. Freeman. Stretched Adiabatic Pulses for Broadband Spin Inversion. In: _Journal of Magnetic Resonance, Series A_ 117 (1995), pp. 246–256. 

- [64] Luke A. O’Dell. The WURST kind of pulses in solid-state NMR. In: _Solid State Nuclear Magnetic Resonance_ 55–56 (2013), pp. 28–41. 

- [65] Steven Conolly et al. A reduced power selective adiabatic spin-echo pulse sequence. In: _Magnetic Resonance in Medicine_ 18.1 (Mar. 1991), pp. 28–38. 

- [66] J. Baum, R. Tycko, and A. Pines. Broadband and adiabatic inversion of a twolevel system by phase-modulated pulses. In: _Physical Review A_ 32.6 (Dec. 1985), pp. 3435–3447. 

- [67] G. Feher. Observation of Nuclear Magnetic Resonances via the Electron Spin Resonance Line. In: _Physical Review_ 103 (Aug. 1956), pp. 834–835. 

- [68] John J. L. Morton et al. Nuclear relaxation in Davies ENDOR variants. In: _Journal of Magnetic Resonance_ 191.2 (Apr. 2008), pp. 315–321. 

- [69] Gary Wolfowicz et al. Decoherence mechanisms of<sup>209</sup> Bi donor electron spins in isotopically pure<sup>28</sup> Si. In: _Phys. Rev. B_ 86 (Dec. 2012), p. 245301. 

- [70] Anna Ferretti et al. Electron spin-echo relaxation and envelope modulation of shallow phosphorus donors in silicon. In: _Physical Review B_ 72 (2005), p. 235201. 

- [71] G. H. Larson and C. D. Spin-Lattice Relaxation in Some Rare-Earth Salts. I. Temperature Dependence. In: _Physical Review_ 141.2 (Jan. 1966), pp. 461– 474. 

- [72] R. Orbach. Spin-lattice relaxation in rare-earth salts. In: _Proceedings of the Royal Society of London. Series A. Mathematical and Physical Sciences_ 264.1319 (Dec. 1961), pp. 458–484. 

Bibliography 

170 

- [73] E. Zambrini Cruzeiro et al. Spectral hole lifetimes and spin population relaxation dynamics in neodymium-doped yttrium orthosilicate. In: _Physical Review B_ 95.20 (May 2017), p. 205119. 

- [74] Thomas Böttger et al. Optical decoherence and spectral at 1.5 _µ_ m in Er<sup>3+</sup> :Y2SiO5 versus magnetic field, temperature, and Er<sup>3+</sup> concentration. In: _Physical Review B_ 73.7 (Feb. 2006), p. 075101. 

- [75] David M. Pozar. _Microwave Engineering_ . Addison-Wesley, 1990. 

- [76] Bernard Yurke and John S. Denker. Quantum network theory. In: _Phys. Rev. A_ 29.3 (Mar. 1984), pp. 1419–1437. 

- [77] David J. _Introduction to Electrodynamics_ . 4th ed. Cambridge University Press, 2017. 

- [78] E. T. Jaynes and F. W. Cummings. Comparison of Quantum and Semiclassical Radiation Theories with Application to the Beam Maser. In: _Proceedings of the IEEE_ 51 (1963), pp. 89–109. 

- [79] M. Tavis and F. W. Cummings. Exact Solution for an N-Molecule—RadiationField Hamiltonian. In: _Physical Review_ 170 (1968), pp. 379–384. 

- [80] R. H. Dicke. Coherence in Spontaneous Radiation Processes. In: _Physical Review_ 93 (1954), pp. 99–110. 

- [81] I. Diniz et al. Strongly coupling a cavity to inhomogeneous ensembles of emitters: Potential for long-lived solid-state quantum memories. In: _Phys. Rev. A_ 84.6 (Dec. 2011), p. 063810. 

- [82] A. Bienfait et al. Controlling Spin Relaxation with a Cavity. In: _Nature_ 531.7592 (2016), pp. 74–77. 

- [83] Gary Wolfowicz. Quantum control of donor spins in silicon and their environment. PhD thesis. University of Oxford, 2015. 

- [84] Yunus A. Çengel, Michael A. Boles, and Mehmet Kanoğlu. _Thermodynamics: An Engineering Approach_ . 10th ed. McGraw Hill, 2023. 

- [85] M. Y. Xu, A. T. A. M. de Waele, and Y. L. Ju. A pulse tube refrigerator below 2 K. In: _Cryogenics_ 39.10 (1999), pp. 865–869. 

- 

- [86] Royal Society of Chemistry. Helium (He) Element information, properties and uses. 

- [87] J. C. Wheatley. Dilute Solutions of He<sup>3</sup> in He<sup>4</sup> at Low Temperatures. In: _American Journal of Physics_ 36.3 (Mar. 1968), pp. 181–210. 

- [88] D. S. Betts and E. N. Smith. _An Introduction to Millikelvin Technology_ . Cambridge University Press, 1989. 

Bibliography 

171 

- [89] ators. Mar. 2026. url: `https://bluefors.com/news/increased-coolingpower-specifications-for-bluefors-dilution-refrigerators/` (visited on 05/09/2026). 

- [90] Edward M. Purcell. Helmholtz Coils Revisited. In: _American Journal of Physics_ 57.1 (1989), pp. 18–22. 

- [91] Joseph Alexander. Developing a Microwave Quantum Memory with Rare-Earth Doped Crystals. Doctoral thesis (Ph.D.) London, United Kingdom: University College London, 2023. 

- [92] Lucas H. Gabrielli Heitzmann. gdspy: Python module for creating GDSII stream Version 1.6.13. 2023. 

- files. 

- [93] Dassault Systèmes. CST Studio Suite. Version 2025. 2025. 

- [94] M. Morita et al. Growth of native oxide on a silicon surface. In: _Journal of Applied Physics_ 68.3 (1990), pp. 1272–1281. 

- [95] Heidelberg Instruments. DWL 66+ Datasheet: The Ultimate Lithography Research Tool. Datasheet. Heidelberg Instruments Mikrotechnik GmbH, June 2025. 

- [96] Haruhiko Abe, Masahiro Yoneda, and Nobuo Fujiwara. Developments of Plasma Etching Technology for Fabricating Semiconductor Devices. In: _Japanese Journal of Applied Physics_ 47.3 (2008), pp. 1435–1455. 

- [97] M. S. Khalil et al. An analysis method for asymmetric resonator transmission applied to superconducting devices. In: _Journal of Applied Physics_ 111.5 (Mar. 2012), p. 054510. 

- [98] Jiansong Gao. The Physics of Superconducting Microwave Resonators. PhD thesis. California Institute of Technology, 2008. 

- [99] S. Probst et al. and robust analysis of complex scattering data under noise in microwave resonators. In: _Review of Scientific Instruments_ 86.2 (Feb. 2015), p. 024706. 

- [100] B. S. Chandrasekhar. A Note on the Maximum Critical Field of High-Field Superconductors. In: _Applied Physics Letters_ 1.1 (Sept. 1962), pp. 7–8. 

- [101] A. M. Clogston. Upper Limit for the Critical Field in Hard Superconductors. In: _Physical Review Letters_ 9.6 (Sept. 1962), pp. 266–267. 

- [102] Michael Tinkham. _Introduction to Superconductivity_ . 2nd ed. McGraw-Hill, 1996. 

- [103] C. J. Gorter and H. B. G. Casimir. On supraconductivity I. In: _Physica_ 1.1–6 (1934), pp. 306–320. 

Bibliography 

172 

- [104] R. Meservey and P. M. Tedrow. Measurements of the Kinetic Inductance of Superconducting Linear Structures. In: _Journal of Applied Physics_ 40.5 (Apr. 1969), pp. 2028–2034. 

- [105] Anthony J. Annunziata et al. Tunable superconducting nanoinductors. In: _Nanotechnology_ 21.44 (2010), p. 445202. 

- [106] S. K. Yip and J. A. Sauls. Nonlinear Meissner in CuO superconductors. In: _Physical Review Letters_ 69.15 (Oct. 1992), pp. 2264–2267. 

- [107] _–_ 

- niobium samples. In: _Physical Review Special Topics Accelerators and Beams_ 15 (June 2012), p. 062001. 

- 

- [108] J. F. Ziegler, M. D. Ziegler, and J. P. Biersack. SRIM The stopping and range of ions in matter (2010). In: _Nuclear Instruments and Methods in Physics Research Section B: Beam Interactions with Materials and Atoms_ 268.11–12 (2010), pp. 1818–1823. 

- [109] D. Holmes et al. Activation and electron spin resonance of near-surface implanted bismuth donors in silicon. In: _Physical Review Materials_ 3 (Aug. 2019), p. 083403. 

- [110] H. Nyquist. Thermal Agitation of Electric Charge in Conductors. In: _Physical Review_ 32.1 (July 1928), pp. 110–113. 

- [111] J. F. Qu et al. Johnson Noise Thermometry. In: _Measurement Science and Technology_ 30.11 (2019), p. 112001. 

- [112] H. T. Friis. Noise Figures of Radio Receivers. In: _Proceedings of the IRE_ 32.7 (July 1944), pp. 419–422. 

- [113] C. M. Caves. Quantum limits on noise in linear In: _Physical Review D_ 26.8 (Oct. 1982), pp. 1817–1839. 

- [114] Ananda Roy and Michel Devoret. Introduction to Quantum-limited Parametric Amplification of Quantum Signals with Josephson Circuits. In: _arXiv preprint arXiv:1605.00539_ (2016). 

- [115] A. B. Zorin. Flux-Driven Josephson Traveling-Wave Parametric In: _Physical Review Applied_ 12 (Oct. 2019), p. 044051. 

- [116] Daniel J. Parker et al. Degenerate Parametric via Three-Wave Mixing Using Kinetic Inductance. In: _Physical Review Applied_ 17 (Mar. 2022), p. 034064. 

- [117] John Kerr. A new relation between electricity and light: media birefringent. In: _The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science_ 50.332 (1875), pp. 337–348. 

Bibliography 

173 

- [118] R. L. Fagaly. Superconducting quantum interference device instruments and applications. In: _Review of Scientific Instruments_ 77.10 (Oct. 2006), p. 101101. 

- [119] M. R. Vissers et al. Frequency-tunable superconducting resonators via nonlinear kinetic inductance. In: _Applied Physics Letters_ 107.6 (2015), p. 062601. 

- [120] T. Lindström et al. Properties of superconducting planar resonators at millikelvin temperatures. In: _Physical Review B_ 80.13 (2009), p. 132501. 

- [121] Peter F. Herskind et al. Realization of collective strong coupling with ion Coulomb crystals in an optical cavity. In: _Nature Physics_ 5.7 (2009), pp. 494–498. 

- [122] T. Sekiguchi et al. Host isotope mass on the interaction of group-V donors in silicon. In: _Physical Review B_ 90.12 (Sept. 2014), p. 121203. 

- [123] James O’Sullivan et al. Spin-Resonance Linewidths of Bismuth Donors in Silicon Coupled to Planar Microresonators. In: _Physical Review Applied_ 14.6 (Dec. 2020), p. 064050. 

- [124] R. Guichard et al. Decoherence of nuclear spins in the frozen core of an electron spin. In: _Phys. Rev. B_ 91.21 (June 2015), p. 214303. 

- [125] Gediminas Usevičius et al. Versatile High-Sensitivity EPR Using Superconducting Spiral Microresonators. In: _Small Methods_ 10.6 (Nov. 2025), e01451. 

- [126] J. J. Pla et al. Strain-Induced Spin-Resonance Shifts in Silicon Devices. In: _Physical Review Applied_ 9.4 (Apr. 2018), p. 044014. 

- [127] Michael Garwood and Yiping Ke. Symmetric pulses to induce arbitrary _Journal_ 

- angles with compensation for rf inhomogeneity and resonance offsets. In: _of Magnetic Resonance (1969)_ 94.3 (1991), pp. 511–525. 

- [128] Gavin Dold et al. High-Cooperativity Coupling of a Rare-Earth Spin Ensemble to a Superconducting Resonator Using Yttrium Orthosilicate as a Substrate. In: _Physical Review Applied_ 11.5 (May 2019), p. 054082. 

- [129] C. W. Gardiner and M. J. Collett. Input and output in damped quantum systems: Quantum stochastic differential equations and the master equation. In: _Physical Review A_ 31.6 (June 1985), pp. 3761–3774. 

- [130] Pablo Arrighi, Amélia Durbec, and Matt Wilson. Quantum networks theory. In: _Quantum_ 8 (Oct. 2024), p. 1508. 

- [131] Qi-Ming Chen et al. Scattering of superconducting microwave resonators. II. System-bath approach. In: _Physical Review B_ 106.21 (2022), p. 214506. 

- [132] Johannes Heinsoo et al. Rapid Multiplexed Readout of Superconducting Qubits. In: _Physical Review Applied_ 10.3 (2018), p. 034040. 

Bibliography 

174 

- [133] Matthias U. Staudt et al. Coupling of an erbium spin ensemble to a superconducting resonator. In: _Journal of Physics B: Atomic, Molecular and Optical Physics_ 45.12 (2012), p. 124019. 

- [134] Linda Greggio et al. Optimal absorption and emission of itinerant into a spin ensemble memory. In: _arXiv preprint arXiv:2506.06107_ (2025). arXiv: `2506.06107 [quant-ph]` . 

- [135] S. Meiboom and D. Gill. Spin-Echo Method for Measuring Nuclear Relaxation Times. In: _Review of Scientific Instruments_ 29.8 (1958), pp. 688– 691. 

- [136] COMSOL AB. COMSOL Multiphysics® v. 6.4. COMSOL AB. Stockholm, Sweden, 2025. 

- [137] A. Bienfait et al. Reaching the quantum limit of sensitivity in electron spin resonance. In: _Nature Nanotechnology_ 11.3 (2016), pp. 253–257. 

- [138] E. H. Rhoderick and E. M. Wilson. Current Distribution in Thin Superconducting Films. In: _Nature_ 194 (1962), pp. 1167–1168. 

- [139] B. W. and W. L. McLean. Superconducting Penetration Depth of Niobium. In: _Physical Review_ 139.5A (1965), A1515–A1522. 

- [140] Tikai Chang et al. Strong coupling of a superconducting qubit to single bismuth donors. In: _Nature Communications_ 16 (2025), p. 9832. 


# **Analytical Methods for High-Rate Global Quantum Networks** 

Cillian Harney<sup>∗</sup> and Stefano Pirandola<sup>†</sup> 

_Department of Computer Science, University of York, York YO10 5GH, United Kingdom_ 

The development of a future, global quantum communication network (or quantum internet) will enable high rate private communication and entanglement distribution over very long distances. However, the large-scale performance of ground-based quantum networks (which employ photons as information carriers through optical-fibres) is fundamentally limited by fibre quality and link length, with the latter being a primary design factor for practical network architectures. While these fundamental limits are well established for arbitrary network topologies, the question of how to best design global architectures remains open. In this work, we introduce a large-scale quantum network model called weakly-regular architectures. Such networks are capable of idealising network connectivity, provide freedom to capture a broad class of spatial topologies and remain analytically treatable. This allows us to investigate the effectiveness of large-scale networks with consistent connective properties, and unveil critical conditions under which end-to-end rates remain optimal. Furthermore, through a strict performance comparison of ideal, ground-based quantum networks with that of realistic satellite quantum communication protocols, we establish conditions for which satellites can be used to outperform fibre-based quantum infrastructure; rigorously proving the efficacy of satellite-based technologies for global quantum communications. 

## **I. INTRODUCTION** 

Advancements in quantum information science will have a profound impact on society [1–4]. In particular, the overarching trajectory of quantum communication technologies is towards a global quantum communication network: A quantum internet [5–8]. This will facilitate high rate, provably secure communication and globally distributed quantum information processing with radical implications for science, technology and beyond. 

The current, most promising point-to-point quantum communication protocols (where two parties are connected directly via a quantum channel) are based on continuous variable (CV) quantum systems [3, 9, 11, 12] (such as bosonic modes). CV protocols achieve high performance and are compatible with current telecommunication infrastructure based upon optical-fibre connections, emphasising their near-term feasibility. However, the laws of quantum mechanics prohibit the ability to simultaneously achieve high rates and long distances, a fundamental law captured by the Pirandola-LaurenzaOttaviani-Banchi (PLOB) bound [4]. This describes the absolute maximum rate that two parties may transfer quantum states, distribute entanglement, or establish secret-keys over a bosonic lossy channel (optical-fibres) equal to _−_ log2(1 _− η_ ) bits per channel use, where _η_ is the channel transmissivity [4, 14]. 

Overcoming this point-to-point limitation requires the use of quantum repeaters or more generally the construction of quantum networks. Combining tools from classical network theory [15–18] with the PLOB bound, ultimate limits have also been established for the end-toend capacities of quantum networks [19]. These results 

> ∗ cth528@york.ac.uk 

> † stefano.pirandola@york.ac.uk 

confirm that the PLOB bound can be beaten via quantum networking, facilitating high rate communication at longer ranges. While such bounds are easily expressed in full generality for arbitrary network topologies, their practical assessment requires the specification of an architecture. Questions of network topology have been recently considered via the statistical study of complex, random quantum networks [5, 20, 21, 23], which reveal insightful phenomena associated with large-scale network properties. Studies of this kind are extremely valuable and help to unveil important guidelines for the development of future quantum networks. 

Nonetheless, such analyses are not easy and require significant numerical effort in order to reveal key network properties, e.g. critical network densities or maximum fibre-lengths. There is a demand for versatile, _analytical_ tools which allow for the efficient benchmarking of quantum networks and can motivate the construction of large-scale topologies. 

Meanwhile, ground-based fibre channels are not the only conduits available for global quantum communications. A rival infrastructure that may prove superior to fibre-based networks at global distances is Satellite Quantum Communication (SQC) [24–31]. SQC exploits ground-to-satellite communication channels to overcome the fundamental distance limitations offered by fibre/ground-based mechanisms. A satellite in orbit around the Earth may act as a _dynamic_ repeater that physically passes over ground-based users and distributes very long-range entanglement/secret-keys. The ability to exploit a free-space connection with a satellite also carries the possibility of substantially more transmissive channels than optical-fibre, making it ideal for global communication protocols. 

The following critical questions emerge: Can we develop analytical tools which allows us to place limits on the end-to-end performance of large-scale quantum networks? And are fibre-based networks truly the best way 

2 

to achieve long-distance quantum communication? The goal of this work is to make progress with these challenges. 

Utilising ideas from quantum information theory, classical networks and graph theory [32], we investigate ideal architectures based on the property of weak-regularity. Weakly-Regular Networks (WRNs) simultaneously ( _i_ ) idealise network connectivity, ( _ii_ ) provide sufficient freedom to capture a broad class of spatial topologies and ( _iii_ ) remain analytically treatable so that critical network properties can be rigorously studied. This results in a design with desirable qualities which can efficiently and effectively provide insight for realistic structures. We show that quantum WRNs employing multi-path routing admit remarkably accessible and achievable upperbounds on the end-to-end network capacity. This allows for a characterisation of the ideal performance of a fibrebased quantum internet with respect to essential properties such as maximum channel length and nodal density. 

Our exact, analytical results provide an immediate pathway to perform comparisons of SQC with global ground-based quantum communications. We study the average number of secret bits per day that can be distributed between two remote stations, using large-scale quantum fibre-networks or a single satellite repeater station in orbit. Our findings rigorously prove the superiority of satellite-based quantum repeaters for global quantum communications, reveal the constraints associated with fibre-based networks and the enormous resource demands required to overcome achievable rates offered by a single satellite. These results further motivate the study of SQC and its key role within a future quantum internet. 

The remainder of this paper is structured as follows: In Section II we introduce preliminary notions of quantum networks, optimal end-to-end performance and ideal properties of large-scale network designs. In Section I we discuss how the optimal performance of quantum WRNs can be analytically bounded with respect to network properties and apply these methods to bosonic lossynetworks. Section IV then compares the performance of global fibre-networks with rates that are achievable by SQC, assessing the advantages associated with each infrastructure, followed by concluding remarks. 

## **II. QUANTUM NETWORK DESIGN** 

## **A. Basics of Quantum Networks** 

A quantum network can be described as a finite, undirected graph _N_ = ( _P, E_ ) where _P_ = _{_ **_x_** _i}i_ is a set of all nodes (points/vertices) on the graph and _E_ = _{ei}i_ collects valid connections between pairs of nodes (edges). A network node refers to either a user-node, such as a potential end-user pair Alice **_a_** and Bob **_b_** , or a repeater/relay-node. Each node **_x_** _i_ possesses a local register of quantum systems which can be altered and exchanged with connected neighbours. Any two 

nodes **_x_** _,_ **_y_** _∈ P_ are connected via an undirected edge _e_ := ( **_x_** _,_ **_y_** ) _∈ E_ if there exists a quantum channel _E_ **_xy_** through which they may directly communicate. Since each edge is undirected, this may be a forward or backward channel. 

In the context of quantum networks, it is important to make a distinction between _physical flow_ and _logical flow_ . The logical flow of a quantum communication channel describes the direction in which entanglement, secret-keys, or quantum states are distributed from a node **_x_** to node **_y_** (or vice versa). The physical flow of quantum communication refers to the actual direction of quantum system exchange, i.e. if quantum systems are physically sent in the direction **_x_** _→_ **_y_** or **_y_** _→_ **_x_** . In a quantum network, these concepts can be completely decoupled. This may be due to the fact that the communication task has a symmetric objective i.e. if Alice and Bob with to share a secret-key, they do not care _who_ initiates the exchange of quantum systems. However, it may also be thanks to quantum teleportation; it is always possible to “reverse” the logical direction of communication by means of a teleportation protocol between Alice and Bob. 

The independence of physical and logical flow helps us to reliably describe a quantum network as an undirected graph. Any pair of connected network nodes can choose the physical direction in which they wish to exchange quantum systems and may always choose that which has the largest capacity. As a result, we never need to distinguish between forward or backward channels and represent each edge ( **_x_** _,_ **_y_** ) _∈ E_ by the best choice of quantum channel [19]. 

In a point-to-point communication setting, the logical flow of quantum information has a clear and obvious set of choices; Alice to Bob **_a_** _→_ **_b_** or Bob to Alice **_a_** _←_ **_b_** . However, within a quantum network, a vast array of options emerge due to the various interconnections and possible paths that information may follow. To address this, users can devise an end-to-end routing strategy that facilitates communication between end-users. The two key classes of strategy are _single-path_ and _multi-path_ routing. 

Single-path routing is the simplest network communication method, which utilises point-to-point communications in a sequential manner. An end-to-end route, _ω_ , is defined as a sequence of network edges which are able to connect a pair of end-users **_a_** _,_ **_b_** _∈ P_ , that is _ω_ := _{_ ( **_a_** _,_ **_x_** 1) _,_ ( **_x_** 1 _,_ **_x_** 2) _, . . . ,_ ( **_x_** _N ,_ **_b_** ) _}._ Quantum systems can be exchanged from node-to-node along this route, followed by LOCC operations after each transmission until eventually communication is established between the end-users. This kind of strategy is analogous to the use of a repeater-chain and network performance is determined by the strength of each link along an optimal end-toend route. Yet, quantum information is significantly less robust than classical information and single-path routing may not be sufficiently resilient to network errors, or provide high enough rates. 

A more powerful strategy is multi-path routing, which properly exploits the multitude of possible end-to-end 

3 

routes available in a quantum network. In multi-path protocols, users may simultaneously utilise a number of unique routes _{ω_ 1 _, ω_ 2 _, . . . , ωM }_ in an effort to enhance their end-to-end rate. A user may exchange an initially multi-partite quantum state with a number of neighbouring receiver nodes, who may each then perform their own point-to-multi-point exchanges along its unused edges. The exchange of quantum systems can be interleaved with adaptive network LOCCs in order to distribute secret correlations and this process continues until a multipoint interaction is carried out with the end-user. 

The optimal multi-path routing strategy operates in such a way that all channels in the network are used once per end-to-end transmission. This is known as a _flooding protocol_ [17–19]; each node in the network performs quantum systems exchanges along all its available edges, resulting in non-overlapping point-to-multipoint exchanges between all network nodes. The ability to flood an entire network means that every possible endto-end route between the end-users are fully explored, allowing them to achieve the optimal end-to-end rate. This greatly enhances the end-to-end performance of quantum networks. 

## **B. Optimal Performance and Flooding Capacities** 

As discussed, the optimal end-to-end performance of a network is defined by its ability to perform flooding by using every edge in the network to achieve communication between a pair of end-users [19]. Any communication protocol which does not flood the network utilises less resources and thus fewer end-to-end paths; hence no protocol can achieve a better end-to-end rate than flooding. This optimal performance is quantified by a _flooding capacity C_<sup>_m_</sup> ( **_i_** _, N_ ), which describes the optimal number of target bits (such as secret-bits or entanglement-bits) that can be transmitted between end-users per use of a flooding protocol. 

An important graph-theoretic concept for quantifying network performance is that of _cuts_ and _cut-sets_ . Consider a network _N_ = ( _P, E_ ) with two remote end-users **_a_** _,_ **_b_** _∈ P_ . We may collect this end-user pair into its own, compact object **_i_** = _{_ **_a_** _,_ **_b_** _}_ , which is simply a two-element subset of the collection of all network nodes. We define a cut _C_ as a bipartition of all network nodes _P_ into two disjoint subsets of nodes ( _P_ **_a_** _, P_ **_b_** ) such that the end-users become completely disconnected, **_a_** _∈ P_ **_b_** and **_b_** _∈ P_ **_b_** , where _P_ **_a_** _∩ P_ **_b_** = ∅. A cut _C_ generates an associated cut-set; a collection of network edges _C_<sup>˜</sup> which enforce the partitioning when removed, 

so that there no longer exists a path between **_a_** and **_b_** . Network cuts play a key role in the derivation of end-toend network rates and many network optimisation tasks can be reduced to an optimisation over all cuts with respect to single-edge/multi-edge properties. 

Each channel in a network is associated with a singleedge capacity _C_ **_xy_** := _C_ ( _E_ **_xy_** ) which describes the pointto-point communication quality between nodes. Hence, all networks have a single-edge capacity distribution _{C_ **_xy_** _}_ ( **_x_** _,_ **_y_** ) _∈E_ which informs the weights of the network graph. Consequently, the flooding capacity can be derived by solving the classical maximum-flow minimumcut problem according to a single-edge capacity distribution. The flooding capacity is found by locating the minimum-cut _C_ min, which minimises the multi-edge capacity over all cut-sets [19], 



For general quantum networks with arbitrary capacity distributions and network structures, this problem requires a numerical treatment by solving the well known max-flow min-cut problem [33–35] to find _C_ min. However, it is possible to express an intuitive, simpler upperbound. Let us define the nodal-neighbourhood of a node **_x_** as 



Then _N_ **_x_** is the collection of nodes to which **_x_** is connected. We can also define an edge-neighbourhood of **_x_** as all the edges which connect **_x_** to its neighbours, 



It follows that one can always successfully partition the users **_a_** and **_b_** by collecting all of the edges in _E_ **_a_** or _E_ **_b_** into a cut-set. This effectively disconnects either of the nodes from the rest of the network, resulting in a valid cut and is true regardless of the network architecture. We may call this form of network cut _user-node isolation_ , denoted _C_ iso. 

Since this form of cut always exists, the multi-edge capacity associated with _C_ iso can be used to upper-bound Eq. (3). By performing nodal isolation on the end-user in **_i_** = _{_ **_a_** _,_ **_b_** _}_ which minimises its multi-edge capacity, we can write the bound 



Here we have defined _CN_<sup>_m_</sup> **_i_**<sup>asthe</sup><sup>_min-neighbourhoodca-_</sup> _pacity_ which is generated by _C_ iso. Since _C_ iso is a valid network-cut, the min-neighbourhood capacity is achievable. 



Under the action of a cut, a network is successfully partitioned 



## **C. Ideal Properties of Large-Scale Networks** 

An overarching goal of quantum network design is to achieve _end-to-end distance independence_ . That is, given 

4 

a pair of end-users, the rate achievable between them is independent from their physical end-to-end separation and instead encoded into some properties of network link-lengths or nodal density. In quantum networks, distance independence is especially important as it bypasses the fundamental rate limitations associated with point-to-point communications imposed by the PLOB bound. Recent studies have shown that random fibre-network architectures which are explicitly conscious of link-lengths are capable of obtaining distance independence, e.g. Waxman networks which are sufficiently dense [5, 36]. These studies simultaneously suggest the shortcomings of classically-inspired network architectures (such as scale-free structures) to achieve distance independence in a quantum setting, even with large resources. 

It is imperative that quantum networks are constructed using quantum-motivated design choices. To facilitate end-to-end distance independence, ground-based quantum network architectures will need to be especially conscious of two main features; maximum link-length (which is often encoded into nodal density) and network connectivity (how well connected each node is within the structure). When appropriate restrictions are placed on permitted link-lengths, this can help to ensure strong end-to-end rates. Until now, the behaviour of maximum link-lengths with respect to network architecture has been excluded to numerical studies. For example, in Refs. [5, 21] the authors study the necessary nodal densities required to ensure effective end-to-end rates; the higher the network density, the more likely that end-toend communication can be mediated by shorter links, resulting in reliable rates. In this work, we reveal novel analytical tools which help to uncover the necessary resources for high performance quantum fibre-networks. 

## **III. WEAKLY-REGULAR QUANTUM NETWORKS** 

## **A. Weakly-Regular Networks** 

The generality of complex architectures such as Waxman, Erd˝os-R´enyi and scale-free networks render analytical investigation very difficult. For this reason, the investigation of quantum repeater technologies/protocols often relies heavily on numerics in order to study complex network performance. Otherwise, one is limited to the simpler setting of linear networks which can be assessed analytically, i.e. repeater chains. The development of a common ground between these scenarios, where largescale, highly-connected networks can be studied analytically is thus highly desirable. 

Here, we propose the use of _weakly-regular_ (WR) network architectures. Weak-regularity is a graph-theoretic concept which infers particular connectivity properties onto undirected graphs, _N_ = ( _P, E_ ). Most prominently, each node **_x_** _∈ P_ in a WRN has the same degree, i.e. if 



Figure 1. A WRN cell can be concatenated many times to construct a large-scale network which is WR within some nodal boundary. Alternatively, outer edges can be looped in order to close the network so to satisfy weak-regularity everywhere (so there is no nodal boundary). In this example, _k_ = 6 and there is only one unique adjacent commonality multi-set **_λ_** = _{_ 2 _}_<sup>_∪_6</sup> (we employ a superscript union notation to describe the repeated union of a single set, e.g. _{x}_<sup>_∪_3</sup> = _{x} ∪{x} ∪{x}_ = _{x, x, x}_ ). 

**_x_** _∈ P_ is connected to _k_ other nodes, then every node in the network is connected to exactly _k_ nodes. This infers _regularity_ and provides the core simplification from complex graphical designs (where regularity is seldom held). 

The _weak_ element of weak-regularity is less obvious, but is similarly integral to our analyses. By definition, a _strongly-regular_ graph is a structure which adheres to very strict rules; it consists of _n_ nodes which are all _k_ regular, any pair of adjacent nodes (nodes which share an edge) share exactly _λ_ common neighbours and any pair of non-adjacent nodes (don’t share an edge) share exactly _µ_ neighbours. We call these positive, integer parameters _λ_ , _µ ∈_ Z<sup>+</sup> the adjacent and non-adjacent commonalities respectively of any two nodes on the graph and are used to characterise how a graph is connected. The notion of strength in strong-regularity resides in the consistency of the values _λ_ and _µ_ for all nodes across the graph. When strong-regularity is upheld, all of these requests result in a relatively small graph with impractical properties for large-scale network design. Consequently, if _λ_ and _µ_ are allowed to take on a broader range of values, then the graph is _weakly_ -regular. Hence, weakness infers a looser characterisation of neighbour sharing between nodes. 

In this work, we consider WR graphs for which the neighbour-sharing (commonality) properties of any network node can obey some _spectrum_ of values. In the context of studying end-to-end performance, it turns out that the most important commonality property is the adjacent commonality. Consider a node **_x_** _∈ P_ on a _k_ -WR graph and its neighbourhood of adjacent nodes, 



Then _N_ **_x_** is the collection of _k_ nodes to which **_x_** is connected. For any node on the network, we can define a bespoke _adjacent commonality multi-set_ (a modified set which can contain degenerate elements) which counts the number of neighbours shared between **_x_** and all its neighbours **_y_** _∈ N_ **_x_** . More precisely, the adjacent commonality multi-set can be as 



5 

where we denote _λ_<sup>**_y_**</sup> **_x_**<sup>:=</sup><sup>_|N_</sup><sup>**_x_**</sup><sup>_∩N_</sup><sup>**_y_**</sup><sup>_|_asthenumberofcom-</sup> mon neighbours shared between the connected nodes **_x_** and **_y_** . In our analyses, we consider graphs which are defined by a non-degenerate super-set of permitted adjacent commonality multi-sets, 



so that the adjacent commonality multi-set of any node in the network **_x_** _∈ P_ belongs to the set **_λx_** _∈_ **Λ** . 

In summary, we are able to define a ( _k,_ **Λ** )-WRN as a class of network for which all nodes have a constant degree equal to _k_ and for which their neighbour-sharing properties satisfy **_λx_** _∈_ **Λ** . While _k_ and **Λ** impose connectivity constraints, WRNs that belong to this class are free to adopt a vast range of topological or spatial configurations. Furthermore, we avoid explicit references to the number of network nodes _n_ . Instead, _n_ is encoded into properties of the network such as the nodal density _ρN_ which defines the average number of network nodes per unit of area. 

While these definitions may seem overly abstract, they introduce a remarkably versatile way to analytically describe interesting and useful network structures. For example, it is easy to construct a WR _network cell_ ; a collection of nodes connected a particular graphical structure, which when concatenated (or “stitched”) together will result in a large-scale network which obeys weak-regularity within some nodal boundary. This permits the analytical investigation of networks consisting many nodes which display highly-connected, yet realistic properties. This concatenation process is visualised in Fig. 1 where it is shown how a _k_ = 6 regular cell can be used to generate a larger WRN. Furthermore, Fig. 2(a) depicts a number of examples of these network cells. For more precise details and discussions, see the Supplementary Material. 

## **B. Optimal Performance of Weakly-Regular Networks** 

As a network becomes more highly connected, it becomes easier to locate end-to-end routes between any pair of nodes. As a result, performing network cuts requires the collection of more and more edges in a cut-set, _C_<sup>˜</sup> , in order to restrict flow along the many potential connective paths between the end-users. In a spatial network, this initiates a relationship between cut-set cardinality, _|C_<sup>˜</sup> _|_ , and distance from an end-user. Performing cuts with edges further away from a user node requires the collection of many more edges to consolidate the partition. The further from the user nodes we begin the cut, the greater the number of potential end-to-end paths we must restrict (since we have permitted a larger flow from the user node) and thus the more edges we must collect. We call this phenomenon _network cut growth_ . 

When the quality of point-to-point links in a network is consistent (link-lengths are close to the overall average), then cut-set cardinality _|C_<sup>˜</sup> _|_ plays a significant role in the characterisation of minimum cuts. Indeed, for dense networks with distance constrained edges, the minimum cut is often achieved by nodal isolation. This is thanks to network cut growth and consistent single-edge rates; cuts performed further away from the user-node will generate a larger multi-edge capacity since they will reliably contain more edges with similar single-edge rates. This kind of behaviour has been observed with respect to multipath capacities in Waxman networks, and may exist in other very popular random network models [5, 36]. This form of network cut behaviour is indicative of a well connected network and one that will achieve high rates. 

This logic motivates the main theoretical tool utilised in this paper. WRNs also undergo network cut growth with respect to distance from end-users, thanks to their reliable and consistent connective properties. Consider a large-scale ( _k,_ **Λ** )-WR quantum fibre-network, and a pair of end-users **_i_** = _{_ **_a_** _,_ **_b_** _}_ located within it. Then the cut which collects the fewest edges is that which performs user-node isolation, i.e. collects the _k_ neighbouring edges of either end-user, generating _CN_<sup>_m_</sup> **_i_**<sup>defined in Eq. (6).Ev-</sup> ery other cut in the network will necessarily collect more than _k_ edges in order to successfully partition the endusers. When the flooding capacity saturates Eq. (6) it is user-node isolation achieves the minimum cut. 

Unlike more complex, random network models, it is possible to analytically study network cut growth within WRNs. Here, we sketch the basic technique, and point the reader towards more sophisticated, precise arguments in the Supplementary Material. The basic idea is to use the quantities _k_ , and **Λ** to determine how much larger a cut-set will grow when one is not permitted to cut userneighbourhood edges. If we know how much a cut-set will grow in size with respect to distance from an enduser node, we can identify a relationship between cut-set cardinality and the link quality requirements necessary to achieve the minimum cut. Ultimately, this helps us to derive a _minimum, single-edge threshold capacity C_ min. This reveals a minimum link-quality which when imposed upon all edges in the network will ensure that the optimal performance between end-users is guaranteed to be equal the min-user neighbourhood capacity, _C_<sup>_m_</sup> ( **_i_** _, N_ ) = _CN_<sup>_m_</sup> **_i_**<sup>.</sup> 

This technique proves to be powerful and versatile. Indeed, given the quantum channel description of singleedges in the network, _C_ min can be used to relate threshold properties of point-to-point quantum channels, and end-to-end performance. In the following, we employ this technique to reveal maximum link-lengths for quantum networks connected by bosonic lossy channels. 

## **C. Bosonic Lossy Quantum Networks** 

When considering fibre-based networks, point-to-point links are described by bosonic pure-loss (lossy) chan- 







<!-- Start of picture text -->
RE Zari<br>BS>:AV»od<br><!-- End of picture text -->





_ 

7 

Throughout our investigation we focus on this more probable performance guarantee that the end-to-end flooding capacity satisfies _C_<sup>_m_</sup> ( **_i_** _, N_ ) = _CN_<sup>_m_</sup> **_i_**<sup>grantedthatEq.(48)</sup> is respected throughout the entire network. This allows us to effectively characterise true optimal performance for WR quantum fibre-networks. 

Full details and derivations of these results can be found in the Supplementary Material. Clearly, the quantity _δ_ in Eq. (11) is vital to our developments. Precisely, _δ_ represents the smallest cut-set cardinality that can be achieved without cutting user connected edges. In more intuitive terms, it is used to monitor the network cut growth of a WRN, and allows us to derive critical quantities such as the maximum fibre-length above. Note that in Fig. 2(a) each of the WR cells are characterised by their regularity _k_ and the adjacent commonality multiset which achieves the minimisation in _δ_ , denoted by **_λ_**<sup>_∗_</sup> . Fig. 2(b) then illustrates the relationship between flooding capacity and maximum fibre-length for a number of example WRNs. The limiting separation _d_<sup>max</sup> _N_ is inexorably linked with the regularity of the WRN; networks with high connectivity possess a greater tolerance for longer distance channels since the enhanced multipath capabilities of the network outweigh the effect of poor quality channels. This is clear from the examples shown in Fig. 2, where a WRN with degree _k_ = 16 can tolerate channels of _∼_ 60 km longer than one with _k_ = 3. Note that the 

## **D. Nodal Density** 

We have discussed how WRNs can be used to describe realistic large-scale networks while maintaining analytical understanding of their optimal end-to-end performance and critical properties, e.g. maximum link-length. We may take this analysis a step further in order to understand the relationship between end-to-end performance and network nodal density. The nodal density is defined as the number of nodes _n_ per unit area _A_ of the network, 



Via the previous section, we may derive a maximum fibrelength _d_<sup>max</sup> _N_ that is necessary to guarantee some optimal end-to-end performance _C_<sup>_m_</sup> ( **_i_** _, N_ ) = _CN_<sup>_m_</sup> **_i_**<sup>.Wemay</sup> then ask the question: Is there a corresponding _minimum nodal density_ in which the ( _k,_ **Λ** )-WRN can be constructed while remaining compliant with the maximum fibre-length? It is not so easy to answer this question for completely general WR architectures. Nonetheless, for the networks studied in this work this challenge is readily tackled. 

In the Supplementary Material we show that via the concept of sparse constructions (the least dense way to construct a network given connectivity rules and linklength constraints) it is possible to derive a minimum 

nodal density _ρ_<sup>min</sup> _N_ required to achieve optimal end-toend flooding capacity. The consistency of WRN cells in Fig. 2(a) reduce this to a geometric problem which is solvable. In summary, we can find a lower-bound on the nodal density required to achieve optimal performance _C_<sup>_m_</sup> ( **_i_** _, N_ ) = _CN_<sup>_m_</sup> **_i_**<sup>givenby</sup> 



Here, _ξ_ is a characteristic quantity of the WR network, found by studying its sparse construction. The tightness of this lower-bound depends on the manner in which the sparse construction is solved or approximated. 

Figure 2(c) depicts the connection between flooding capacity and minimum nodal density for a number of types of WRNs. It is clear that there is a trade off between end-to-end performance and regular nodal degree. At low flooding rates (10<sup>_−_2</sup> _−_ 10<sup>_−_1</sup> bits per network use) the WR structures with lower degrees _k_ = 3 and 6 demand fewer resources to achieve the same performance as those with higher degrees _k_ = 8 and 16. In this regime, high degrees are not necessary everywhere in the network to achieve the flooding rates; indeed, the consistent connectivity invoked by WR designs help to maintain performance at low densities. Yet, as the flooding capacity transitions towards 1 _−_ 10 bits per network use this behaviour changes; WRNs with low degrees demand shorter and shorter links to achieve the high rates and the inability to involve more connections at each node becomes costly. As can be seen for _k_ = 3 the required minimum nodal density rapidly increases, shortly followed by _k_ = 6 and 8. Contrarily, the regime of high end-to-end rates is well suited to WRNs with greater regularity, _k_ = 16, for which the greater number of connections at each node facilitate a lower overall density. 

Simultaneously, we plot an approximation of the average flooding capacity between any pair of nodes on a Waxman network with respect to nodal density (dashed grey line) as derived in Ref. [5]. This defines an expected flooding capacity between any pair of users, such that 



where _ρ_ crit _≈_ 4 _._ 25 _×_ 10<sup>_−_4</sup> , _ζ ≈_ 4358 and the average E **_i_** [ _·_ ] is taken over all possible end-user pairs in the network. We identify a kinship between the necessary _ρ_<sup>min</sup> _N_ predicted by WRNs and that derived for Waxman networks. As one may expect, the order and consistency of WRNs is able to promise lower resource demands at lower-rates; resulting in smaller critical nodal density predictions for the necessary density to achieve 1 bit per network use. However, as the flooding performance increases, the flexibility of the Waxman design (its ability to utilise variable nodal degrees) renders it superior to the lower degree WR structures. In summary, there is good behavioural agreement between these models, corroborating the utility of WR structures as a valuable analytical tool for quantum network design. 

8 

## **IV. COMPARISON WITH SATELLITE QUANTUM COMMUNICATIONS** 

## **A. Satellite Quantum Communications** 

Here, we briefly review key results which facilitate a comparison of SQC with idealised, ground-based quantum networks. For more detailed derivations and discussions of these results, please refer to Refs. [24, 26]. 

Consider two users (Alice and Bob), who choose to communicate by means of an orbiting satellite (a dynamic repeater). Here we consider a ground station _G_ at approximately sea-level, and a satellite _S_ which is in orbit at an altitude _h ≥_ 100 km and variable zenith angle _θ_ . Given that the radius of the Earth is _RE ≈_ 6371 km, the slant distance between _G_ and _S_ is _z_ ( _h, θ_ ) = � _h_<sup>2</sup> + 2 _hRE_<sup>2+</sup><sup>_R_</sup> _E_<sup>2cos2(</sup><sup>_θ_)</sup><sup>_−RE_cos(</sup><sup>_θ_)</sup><sup>_,_describingthe</sup> true distance that an optical beam must travel from _G_ to/from _S_ . We may consider two unique configurations for information transmission; _uplink_ , which refers to when _G_ is the transmitter and _S_ is the receiver, and _downlink_ , where the converse is true. Both configurations will identically admit the effects of free-space diffraction (beam-spot size widening) and atmospheric extinction (caused by molecular/aerosol absorption as the beam propagates). However additional loss/noise effects emerge with respect to uplink and downlink protocols, which invokes an asymmetry in their communication performance. 

The effects of turbulence (caused by fluctuations in the atmospheric refractive index) and pointing errors (alignment of the optical signal with the receiver) are responsible for beam wandering, which instigates a fading process for the communication channels. For uplink protocols, turbulence is a significant factor for loss properties of the ground-satellite channel since it impacts the propagating beam immediately after transmission. However, pointing errors can be reduced thanks to the ability to easily access and optimise adaptive optics at ground level. In downlink these effects are reversed. Turbulence is not a factor until the beam reaches low altitudes, at which point the beam has already spread via diffraction. Hence turbulence can be neglected for downlink, but pointing errors mut be considered due to limited onboard access and resources. 

Considering each of these physical effects characterising the lossy free-space channel, it is possible to present an ultimate limit on the secret-key capacity _K_ for SQC [26], 



Here ∆( _η, σ_ ) is a correction factor to the PLOB bound, where _η_ := _η_ ( _h, θ_ ) is an effective transmissivity which is a function of geometric position, encompassing all the effects of diffraction, extinction, and optical imperfections/inefficiencies. Meanwhile, _σ_<sup>2</sup> = _σ_ turb<sup>2+</sup><sup>_σ_</sup> point<sup>2is</sup> the variance of the Gaussian random walk of the beam 

centroid caused by beam wandering, with contributions from turbulence and/or pointing-errors. 

This bound can be further modified to account for the presence of thermal noise, which is highly dependent upon time of day (day or night-time) and weather conditions (cloudy or clear skies). For night-time communications, background noise is practically negligible, and the above bound requires little modification. However, for day-time operations this is generally not the case and the free-space lossy channels must be described as thermalloss channels which account for additional noise. 

## **B. Practical Key-Rates for Satellite Quantum Communications** 

The bound in Eq. (19) is an ultimate upper-bound on the capacity of a ground-to-satellite communication channel, it is important to provide an assessment of realistic and practical protocols which embody achievable lower-bounds for SQC. These lower-bounds will facilitate comparisons with global quantum networks, and help deduce the conditions for which we can expect satellite advantage for long-distance quantum communications. 

Here we summarise some achievable rates for different satellite configurations. We consider practical, composably-secure secret key-rates achievable from the pilot-guided and post-selected CV-QKD protocol studied in Refs. [24, 26]. The main concept of this protocol is to encode information into Gaussian-modulated coherent states, randomly interleaved by highly energetic pilot pulses used to monitor the transmissivity and fading properties of the free-space channel in real time (facilitating the use of classical post-selection). This protocol has been comprehensively extended to account for the physical scenario of satellite quantum communications, resulting in realistic and practical rates. 

We may consider the employment of such a protocol in conjunction with a near-polar sun-synchronous satellite used to communicate between two ground stations. This type of orbit ensures a consistent fly-over time for any point on the Earth’s surface, such that the satellite passes over any point at the same local mean solar time each day. This provides the possibility of stable conditions for satellite communications at around the same time each day. Let us assume that the stations lie along the orbital path such that the satellite crosses both of their zenith positions (which happens once per day). We further assume a worst-case scenario such that the stations only interact with the satellite when the zenith positions are crossed, and that both stations assume similar operational conditions. 

It is possible to quantify the performance of satellite communications by considering a _daily key rates_ , i.e. the number of secret-bits that may be shared per day. This allows us to utilise an average orbital rate _R_ orb associated with up/downlink operations in day/night-time, representing an average secret-key rate per link usage. 

9 

Thanks to the dynamic nature of SQC, and the fact that we consider communication with both stations only once per day, this daily rate will be constant with respect to ground based end-to-end distances. The number of secret-bits that can be shared in a zenith-crossing passage is then given by the effective transit time for the quantum communications _tQ_ ( _h_ ) as a function of the altitude, and a typical clock frequency which we set as _α_ = 10 MHz. The average daily-rate in a given configuration is thus 



for which _i_ labels the up/downlink and day/night-time. For downlink operations at altitude _h_ = 530 km, initial beam-spot-size _ω_ 0 = 40 cm, receiver aperture _aR_ = 1 m, these setup parameters lead to the night-time/day-time rates [26], 



For uplink, we consider and altitude _h_ = 103 km and similar setups (but now with a spot-size _ω_ 0 = 60 cm and wider aperture _aR_ = 2 m) leading to the rate, 



Notice that in both configurations the day and night time rates are very similar. This is thanks to effective noise-filtering that can be performed with this kind of CV-QKD protocol. Such protocols are able to realistically exploit CV quantum systems and interferometric measurements in order to achieve much narrower frequency filters than is possible with DV protocols (see Ref. [26] for more details). As a result, the increased background thermal noise experienced at the receiver in day time does not significantly deteriorate the rate. 

## **C. Comparison with Ground-Based Networks** 

As we have established in previous sections, end-toend distance independence is a critical design feature for the construction of effective quantum networks. It is a feature that can be achieved, provided that one carefully monitors link-length, nodal density and the limits of quantum communication rates. Yet, as shown in the previous section, it can be very resource intensive and costly to promise strong end-to-end rates between long-distance end-users if we choose to solely utilise ground-based fibre networks. For this reason, it is important to understand the limits of large-scale quantum networks for long-range communication. Moreover, it is invaluable to determine when SQC may be superior and offer a feasible, costefficient route to global quantum communication. 

Determination of _when_ SQC is advantageous requires a strict, quantitative comparison with ground-based fibre networks. In this section we aim to benchmark the 

optimal performance of global quantum fibre networks against practical, near-term SQC capabilities. More precisely, we compare daily secret key-rates obtained between globally distant end-users via: 

- ( _i_ ) A global-scale ( _k,_ **Λ** )-WR fibre network with capacity achieving links. 

- ( _ii_ ) A single, sun-synchronous satellite operating at the achievable rates in Eqs. (20)-(22) using realistic devices and the practical CV-QKD protocol discussed in Section IV B. 

Clearly, the resources accessed by an ideal ( _k,_ **Λ** )-WR fibre network are significantly greater than the single satellite, and a fairer comparison would be to consider a constellation of satellites; but that is the point. If a single, sun-synchronous satellite, operating at realistic rates is able to outperform a global fibre network within a meaningful resource regime, this offers clear evidence for the superiority (and necessity) of SQC for global quantum communications. Using the tools developed throughout this paper, our comparison can be carried out expediently and analytically. 

Assume two globally distant end-users, Alice and Bob. We need not consider a specific end-to-end distance, since the ( _k,_ **Λ** )-WRNs are end-to-end distance independent. By considering a daily key rate and the operational setup explained in Section IV B, SQC is also end-to-end distance independent. We are left to compute the daily capacity of the WR fibre network. We consider that the fibre network operates constantly for a day using capacity achieving links with maximum link length _d_<sup>max</sup> _N_ . Given _t_ daily = 8 _._ 64 _×_ 10<sup>4</sup> s as the number of seconds in a day, and again assuming _α_ = 10 MHz, it can be shown the average number of secret-key bits per day satisfies 



where _δ_ is defined in Eq. (11). Repeater-chains can be considered in a similar manner. The repeater-chain capacity is equal to the single-edge capacity associated with the longest inter-nodal separation in the chain. Hence, the average daily secret-key rate of a repeater-chain is [19] 



In order to perform a quantitative comparison between satellite and ground-based quantum communications, we can compute the log-ratio between their daily-rates, 



which determines a _daily-rate advantage_ in decibels (dB). An analogous quantity can be derived for the repeater chain. By studying the daily-rate advantage as a function of maximum inter-nodal separation and nodal density, we 



<!-- Start of picture text -->
(S50S50<br>.||kk)kKk)kK...)kK..kK.K ...)kK..kK.K , 3/oRag/ag// oRag/ag// | ; X : |<br>:|::kk)kK::kk)kK:kk)kK.||kk)kKk)kK...)kK..kK.K |<br>|.|::kk)kK.|::kk)kK:|::kk)kK::kk)kK:kk)kK.||kk)kKk)kK...)kK..kK.K /oRag/ag// 7|| |(3(3 ii’/’i’/’’/’/’’<br>v. )<br><!-- End of picture text -->



<!-- Start of picture text -->
| Te<br>Se,“le,N~ie,~ie,a.12S1Sa,y'e,Te,NG-,ee,,~'e,~%e,22te,<n,Ste,N3Nk,2,So,Tu.a,138Nt,Se,~t,<u,-Ts,oe,:'v,EFEX.oe,So, §i.3.]~e,J3Te.2,ouSe,&e,,JaTe,J=2>Sg,tu,,2.3153[*oo353§N533ee,R304Re)S,EBLaJJSeJ~'e,ERhs.Lo, < :Re\ 18NTe.Se,So,Se,SL,>:S3,\NN§Ts,83SNNN<~'%e,3s,\3%NSe39SL3,“,Jvi,NS.NNNeNa,aN\2AS cs |.|::kk)kK.|::kk)kK:|::kk)kK::kk)kK:kk)kK.||kk)kKk)kK...)kK..kK.K , (S50S50 3/oRag/ag// | ; X : | | 7|| |(3(3 ii’/’i’/’’/’/’’<br>v. )<br>rnd<br>ert IcsRaR%f! Ji ans”oaPYRios2a LoRaoFJo rnLRBSEEINIREREILSXSROrrr iaViarCol=Ti =++* [===] meee]<br>_= nrnh<br>=<br><!-- End of picture text -->

11 

na¨ıve scenario from a practical point of view, but one that is informative nonetheless. Consider quantum communication between distant end-users located in remote cities across continental Europe (e.g. Paris to Moscow) whose land surface area spans approximately _A ≈_ 1 _×_ 10<sup>7</sup> km<sup>2</sup> . In terms of truly global communications this is relatively local. We can choose to communicate between remote cities using a satellite in orbit acting as a dynamic quantum repeater. Alternatively, we can construct a quantum fibre-network across the continent. In this scenario, for an ideal _k_ = 6 WR quantum fibre-network operating at its ultimate flooding capacity to simply match the already achievable daily-rate of a single, sun-synchronous satellite, would require at least _n ≥ Aρ_<sup>_∗_</sup> _N_<sup>_≈_150repeater</sup> stations operating constantly for 24 hours. Clearly, a network of this form operating at realistic rates, under stricter physical conditions (considering thermal noise) would demand even greater resources. 

While the classical internet can exploit fibre-optic links which are thousands of kilometres long, a fibrebased quantum internet is severely limited by short linklengths, resulting in remarkably costly resources for tasks that are already within reach of SQC. These results strongly suggest that a future quantum internet will significantly benefit from the use of SQC, and will be integral to the construction of global quantum communication networks. 

- [1] M. A. Nielsen and I. L. Chuang, _Quantum Computation and Quantum Information: 10th Anniversary Edition_ , 10th ed. (Cambridge University Press, USA, 2011). 

- [2] J. Watrous, _The Theory of Quantum Information_ (Cambridge University Press, 2018). 

- [3] A. S. Holevo, _Quantum Systems, Channels, Information_ (De Gruyter, 2019). 

- [4] F. Arute, K. Arya, R. Babbush, D. Bacon, J. C. Bardin, R. Barends, R. Biswas, S. Boixo, F. G. S. L. Brandao, D. A. Buell, _et al._ , Quantum supremacy using a programmable superconducting processor, Nature **574** , 505 (2019). 

- [5] H. J. Kimble, The quantum internet, Nature **453** , 1023 (2008). 

- [6] S. Pirandola and S. L. Braunstein, Physics: Unite to build a quantum internet, Nature **532** , 169 (2016). 

- [7] M. Razavi, _An Introduction to Quantum Communications Networks_ , 2053-2571 (Morgan & Claypool Publishers, 2018). 

- [8] S. Pirandola, U. L. Andersen, L. Banchi, M. Berta, D. Bunandar, R. Colbeck, D. Englund, T. Gehring, C. Lupo, C. Ottaviani, and et al., Advances in quantum cryptography, Adv. Opt. Photonics **12** , 1012 (2020). 

- [9] A. Serafini, _Quantum Continuous Variables: A Primer of Theoretical Methods_ (CRC Press, Taylor & Francis Group, 2017). 

- [3] C. Weedbrook, S. Pirandola, R. Garc´ıa-Patr´on, N. J. Cerf, T. C. Ralph, J. H. Shapiro, and S. Lloyd, Gaussian quan- 

## **V. CONCLUSION** 

In this work, we have investigated the optimal performance of global, quantum communication networks to characterise the ultimate limits of a fibre-based quantum internet. This analysis is based on an underlying network architecture that exploits weak-regularity to construct powerful, highly-connected networks. Crucially, these bounds allow us to benchmark the performance of a global quantum network versus that of a single sun-synchronous satellite acting as a dynamic repeater. The result of this comparison emphasises the power of SQC, and vast network resources that are required to outperform a single satellite in orbit at global distances. These findings strongly motivate the utilisation of ground-satellite connections within large-scale quantum networks. It is clear that free-space groundsatellite links will be integral to long-range quantum communications, as their co-operation with ground-based infrastructure as dynamic repeaters will be invaluable. 

This work introduces useful, analytical techniques for the study of ideal quantum networks which can be readily employed for future investigative paths. Indeed, the study of hybrid fibre/satellite networks is a topic of immediate interest; exploiting the power of SQC to enhance (rather than compete with) ground-based networks. Furthermore, the expansion of these methods to incorporate multiple satellites introduces the possibility of highly transmissive satellite-satellite channels at high altitudes. 

tum information, Rev. Mod. Phys. **84** , 621 (2012). 

- [11] S. L. Braunstein and P. van Loock, Quantum information with continuous variables, Rev. Mod. Phys. **77** , 513 (2005). 

- [12] T. C. Ralph, Continuous variable quantum cryptography, Phys. Rev. A **61** , 010303(R) (1999). 

- [4] S. Pirandola, R. Laurenza, C. Ottaviani, and L. Banchi, Fundamental limits of repeaterless quantum communications, Nat. Commun. **8** , 15043 (2017). 

- [14] S. Pirandola, R. Garc´ıa-Patr´on, S. L. Braunstein, and S. Lloyd, Direct and reverse secret-key capacities of a quantum channel, Phys. Rev. Lett. **102** , 050503 (2009). 

- [15] P. Slepian, _Mathematical Foundations of Network Analysis_ (Springer-Verlag, New York, 1968). 

- [16] T. M. Cover and J. A. Thomas, _Elements of Information Theory_ (Wiley, New Jersey, 2006). 

- [17] A. S. Tanenbaum and D. J. Wetherall, _Computer Networks_ , 5th ed. (Pearson, 2010). 

- [18] A. El Gamal and Y.-H. Kim, _Network Information Theory_ (Cambridge University Press, 2011). 

- [19] S. Pirandola, End-to-end capacities of a quantum communication network, Commun. Phys. **2** , 51 (2019). 

- [20] J. Biamonte, M. Faccin, and M. De Domenico, Complex networks from classical to quantum, Commun. Phys. **2** , 53 (2019). 

- [21] S. Brito, A. Canabarro, R. Chaves, and D. Cavalcanti, Statistical properties of the quantum internet, Phys. Rev. Lett. **124** , 210501 (2020). 

12 

- [5] Q. Zhuang and B. Zhang, Quantum communication capacity transition of complex quantum networks, Phys. Rev. A **104** , 022608 (2021). 

- [23] B. Zhang and Q. Zhuang, Quantum internet under random breakdowns and intentional attacks, Quantum Sci. Technol. **6** , 045007 (2021). 

- [24] S. Pirandola, Limits and security of free-space quantum communications, Phys. Rev. Research **3** , 013279 (2021). 

- [25] J. S. Sidhu, S. K. Joshi, M. G¨undo˘gan, T. Brougham, D. Lowndes, L. Mazzarella, M. Krutzik, S. Mohapatra, D. Dequal, G. Vallone, _et al._ , Advances in space quantum communications, IET Quant. Comm. **2** , 182–217 (2021). 

- [26] S. Pirandola, Satellite quantum communications: Fundamental bounds and practical security, Phys. Rev. Research **3** , 023130 (2021). 

- [27] J. Yin, Y. Cao, Y.-H. Li, S.-K. Liao, L. Zhang, J.-G. Ren, W.-Q. Cai, W.-Y. Liu, B. Li, H. Dai, G.-B. Li, _et al._ , Satellite-based entanglement distribution over 1200 kilometers, Science **356** , 1140 (2017). 

- [28] J.-G. Ren, P. Xu, H.-L. Yong, L. Zhang, S.-K. Liao, J. Yin, W.-Y. Liu, W.-Q. Cai, M. Yang, L. Li, _et al._ , Ground-to-satellite quantum teleportation, Nature **549** , 70–73 (2017). 

- [29] S.-K. Liao, J. Lin, J. Ren, W. Liu, J. Qiang, J. Yin, 

Y. Li, Q. Shen, L. Zhang, Y. Cao, _et al._ , Space-to-Ground Quantum Key Distribution Using a Small-Sized Payload on Tiangong-2 Space Lab, Chin. Phys. Lett. **34** , 090302 (2017). 

- [30] A. Villar, A. Lohrmann, X. Bai, T. Vergoossen, R. Bedington, C. Perumangatt, H. Lim, T. Islam, A. Reezwana, Z. Tang, _et al._ , Entanglement demonstration on board a nano-satellite, Optica **7** , 734 (2020). 

- [31] J. Yin, Y.-H. Li, S.-K. Liao, M. Yang, Y. Cao, L. Zhang, J.-G. Ren, W.-Q. Cai, W.-Y. Liu, S.-L. Li, R. Shu, _et al._ , Entanglement-based secure quantum cryptography over 1,120 kilometres, Nature **582** , 501 (2020). 

- [32] R. Wilson, _Introduction to Graph Theory_ , 4th ed. (Longman, Essex, 1996). 

- [33] L. R. Ford and D. R. Fulkerson, Maximal flow through a network, Can. J. Math. **8** , 399–404 (1956). 

- [34] J. Edmonds and R. M. Karp, Theoretical improvements in algorithmic efficiency for network flow problems, J. ACM **19** , 248–264 (1972). 

- [35] J. B. Orlin, Max flows in o(nm) time, or better., in _Proceedings of the forty-fifth annual ACM symposium on Theory of computing, STOC’13_ (2013) pp. 765–774. 

- [36] B. Waxman, Routing of multipoint connections, IEEE J. Sel. Areas Commun. **6** , 1617 (1988). 

# **Supplementary Material: Analytical Methods for High-Rate Global Quantum Networks** 

In this supplementary material we provide detailed proofs for the results presented in the main paper, and discuss in-depth some of the key mathematical tools utilised throughout this work. In Section I the formal definitions of regular graphs and weakly-regular graphs are discussed, providing greater context and elaborating upon specific definitions. In Section II we prove the main lemmas, theorems and corollaries utilised within the text allowing us to derive single-edge threshold capacities for weakly-regular networks required to guarantee optimal performance. We then apply these theorems in the context of bosonic lossy quantum channels. Finally, Section III develops the relationship between maximum link-lengths and minimum nodal density through the concept of sparse constructions, deriving a connection between optimal performance and the minimum nodal densities of a range of weakly-regular structures. 

## **I. WEAKLY-REGULAR NETWORKS (WRNS)** 

In this section we explicitly introduce the concept of weak-regularity and weakly-regular networks (WRNs) using graph theoretic concepts. We provide finer context for the purposes of WRNs studied in the main text. 

## **A. Graphs, Neighbour Sharing and Commonality** 

Consider an undirected, finite graph _N_ = ( _P, E_ ) consisting of _n_ nodes in the node set _P_ , and interconnected by edges in the edge set _E_ . Discussed and motivated in the main-text, such a graph underlies the description of a network such that each edge (defined by an unordered pair ( **_x_** _,_ **_y_** ) _∈ E_ ) represents a communication channel _E_ **_xy_** between network repeaters/end-users at each node. The ability to perform communication on a network is characterised by ( _i_ ) the communication channels which compose the network, and ( _ii_ ) the distribution of network nodes and edges resulting in a topology. Here, we explicitly define some key network properties that contribute to its overall topology and ultimately its end-to-end performance. 

An essential network property is nodal degree, i.e. the number of nodes to which a given node is connected. Defining the neighbourhood of a node **_x_** _∈ P_ as 



then the degree of the node **_x_** is equal to the cardinality of its neighbourhood deg( **_x_** ) := _|N_ **_x_** _|._ Hence, the node **_x_** has exactly deg( **_x_** ) neighbours. We can also define an edge-neighbourhood of **_x_** as all the edges which connect **_x_** to its neighbours, 



Nodal degree, and its distribution across a network, is hugely influential on the overall performance of an architecture. However, the degree alone does not give an indication of _how_ a node **_x_** is connected to all of its neighbours. One may ask; are the neighbours also highly connected to one another, or are each of the neighbours distant and disconnected? Answering these questions can be very informative, and provide significant insight into the connectivity and robustness of a network. For this reason, we define useful parameters that contribute to these features. Namely, we utilise the concept of _commonality_ . 

Commonality is a pairwise nodal property which describes neighbour sharing between nodes. Given a pair of nodes **_x_** _,_ **_y_** _∈ P_ the commonality defines how many neighbours that **_x_** and **_y_** _have in common_ . Neighbour sharing behaviour may vary significantly depending on whether **_x_** and **_y_** are already connected (adjacent) and are perhaps close by; or are disconnected (non-adjacent) and perhaps distant. Therefore, we provide the following pair of definitions of commonality: 

**Definition 1** (Adjacent Commonality): _The number of common neighbours shared by adjacent (connected) nodes. Precisely, given that_ ( **_x_** _,_ **_y_** ) _∈ E, the adjacent commonality between this pair of nodes is λ_ ( **_x_** _,_ **_y_** ) := _|N_ **_x_** _∩ N_ **_y_** _|, so that λ_ ( **_x_** _,_ **_y_** ) _counts the number of common neighbours shared between the nodes_ **_x_** _and_ **_y_** _._ 

**Definition 2** (Non-Adjacent Commonality): _The number of common neighbours shared by non-adjacent (nondirectly-connected) nodes. Precisely, given that_ ( **_x_** _,_ **_y_** ) _∈/ E, the non-adjacent commonality is computed by µ_ ( **_x_** _,_ **_y_** ) := _|N_ **_x_** _∩ N_ **_y_** _|, so that µ_ ( **_x_** _,_ **_y_** ) _counts the number of common neighbours shared between the nodes_ **_x_** _and_ **_y_** _._ 

14 



<!-- Start of picture text -->
(a) (b)<br>k = 6<br>λ 1 =  { 4 ,  2 ,  2 ,  2 } ∪ 4<br>λ ( , ) = 2<br>λ 2 =  { 5 ,  4 ,  3 ,  2 } ∪ 4<br>= 2<br>µ ( , )<br>λ 3 =  { 5 ,  5 ,  5 ,  4 ,  4 ,  4 ,  4 ,  3 } ∪ 2<br>= 1<br>µ ( , )<br>µ ( , ) = 0 λ 4 =  { 4 ,  8 ,  8 ,  8 } ∪ 4<br>. . .<br>. . .<br>. . .<br>. . .<br><!-- End of picture text -->

Figure 1. (a) A sub-graph from a ( _k, λ,_ **_µ_** ) = (6 _,_ 2 _, {_ 0 _,_ 1 _,_ 2 _}_ )-weakly regular network. Considering the yellow node as an enduser, the blue nodes thus represent the user neighbourhood, with a uniform adjacent commonality of _λ_ = 2. The non-adjacent commonality decreases as nodes increase in distance from the end-user. (b) A _k_ = 16 weakly-regular network with inconsistent adjacent commonality properties. This network is scalable so that a single network cells can be concatenated to construct a larger _k_ = 16 internally-WR network. For any node in the network, its **_λ_** will be one of those from the set **Λ** = _{_ **_λ_** 1 _,_ **_λ_** 2 _,_ **_λ_** 3 _,_ **_λ_** 4 _}_ . Each adjacent commonality multiset is colour coded to its corresponding node on the graph. Note that throughout this work we employ a superscript union notation to describe the repeated union of a single set, e.g. _{x}_<sup>_∪_3</sup> = _{x} ∪{x} ∪{x}_ = _{x, x, x}_ , etc. 

## **B. Regular Graphs** 

Let us introduce the notion of regularity. Consider an undirected, finite graph _N_ = ( _P, E_ ) of _n_ -nodes. A graph is defined as _k_ -regular if all nodes in the graph possess exactly the same degree _k_ , i.e. the neighbourhood of any node consists of strictly _k_ nodes, 



Regularity significantly simplifies the connective properties of network by assuming a consistency of nodal degree. Clearly, in realistic communication networks there exist disparities of nodal degree throughout the network, as some nodes will be highly connected and others less so. Nonetheless, understanding the ability to communicate on a regular graph can help provide important information for more realistic structures. The class of _k_ -regular graphs is very broad, and more detailed classes can be 

## _1. Strongly Regular Graphs_ 

Strongly Regular (SR) graphs satisfy strict connective properties. A graph _N_ = ( _P, E_ ) is SR if it has _n_ -nodes which are _k_ -regular, its commonality properties are constant 





and these parameters follow the relation 



SR graphs may be well connected, but their architectures are very strict; satisfying all of these constraints will typically result in a network with a small number of nodes. Indeed, the parameters _k, µ, λ_ inhibit the ability to use a large number of nodes rendering them impractical for network design. 

## _2. Weakly Regular Graphs_ 

A more general class is that of Weakly-Regular (WR) graphs. Any regular graph that is not SR is technically WR, and can be characterised by a more general set of connectivity properties. We may invite greater generality by loosening the strict values of the adjacent/non-adjacent commonalities _λ_ , _µ_ for all nodes. Instead, we may permit 

15 

nodes within the network to possess different commonality values for different pairs of nodes. To this end, we define sets which contain all the potential values for the commonality properties; an adjacent commonality set and a nonadjacent commonality set respectively, 



These sets summarise _all the non-degenerate values of λ_ ( **_x_** _,_ **_y_** ) _or µ_ ( **_x_** _,_ **_y_** ) _that are possible on a network_ . That is, 



There is no restriction on the number of potential values that can be contained in **_λ_** or **_µ_** . Indeed, every graph (regular or not) generate their own versions of these sets. 

As a simple example, we illustrate a weakly-regular sub-graph from a larger network in Fig. 1. Clearly, the degree of the network is _k_ = 6, and the commonality properties are also illustrated by considering adjacent and non-adjacent nodes with respect to a root node. Provided that the regularity in Fig. 1 is consistent throughout the network, it can be shown that the adjacent commonality is always _λ_ = 2 for any pair of nodes and the non-adjacent commonality can be _µ ∈_ **_µ_** = _{_ 0 _,_ 1 _,_ 2 _}_ . 

## _3. Useful Parameterisation of Weakly-Regular Graphs_ 

In complete generality, a graph can possess unique commonality values between any pair of nodes, leading to a vast collection of possible values in **_λ_** and **_µ_** , with little to no structure. However, for various architectures, such as WRNs, this will not be true and there may exist a level of consistency which simplifies their analytical treatments. Here, we introduce a more useful and intuitive representation of WRNs. Consider a node **_x_** on a _k_ -WR graph. We can define _k_ element _multiset_ (a modified set which may contain multiple copies of the same element) which contains all the information about neighbour sharing between the node **_x_** and each of its _k_ neighbours, 



Hence, **_λx_** describes a “local” adjacent commonality description, bespoke to the node **_x_** . 

All nodes on any graph (regular or not) possess an adjacent commonality multiset **_λx_** which describes neighbour sharing qualities with respect to their neighbourhoods, so there exists a unique **_λx_** for all **_x_** _∈ P_ . Therefore we can summarise the neighbour sharing properties of an entire network _N_ by collecting all of the possible adjacent commonality multisets contained within it into a superset 



Hence, for any node **_x_** in a network, the adjacent commonality multiset of this node can be found in **Λ** . Note that we now define **Λ** as a strict set, _not_ a multiset. In many cases of interest, such as WRNs with high levels of symmetry, the adjacent commonalities **_λx_** may be highly degenerate across the network, i.e. many nodes possess similar neighbour sharing qualities. Consequently, since **Λ** is a strict set it contains _only_ the non-degenerate **_λx_** multisets. Here we state a formal 

**Definition 3** (Adjacent Commonality Superset): _Any graph N_ = ( _P, E_ ) _possesses an adjacent commonality superset_ **Λ** := _{_ **_λx_** _|_ **_x_** _∈ P } containing all the possible, non-degenerate adjacent commonality multisets_ **_λx_** _which describe the neighbour sharing properties of connected nodes._ 

For many of the architectures that we consider in this work, **Λ** only contains one acceptable adjacent commonality multiset, **Λ** = _{_ **_λ_** _}_ . This is evident in Fig. 1(a) where every pair of adjacent nodes always share exactly two neighbours. In general, this may occur when there are high levels of symmetry/small _k_ regularity in the network structure. However, this is not compulsory. Flexibility in **Λ** can allow us to describe more complex designs with higher nodal degrees. For instance, Fig. 1(b) depicts a _k_ = 16 regular network which may be a portion of a larger network. All nodes satisfy _k_ = 16, but there are four unique adjacent commonality multisets **Λ** = _{_ **_λ_** 1 _,_ **_λ_** 2 _,_ **_λ_** 3 _,_ **_λ_** 4 _}_ for any network node. As we reveal in the main-text, it is vital to understand the graphical properties of WRNs in order to properly characterise end-to-end performance for embedded end-users. 

In contrast, it’s not overly useful to define an analogous language for the non-adjacent commonality properties of a WR graph, **_µ_** . A node-specific non-adjacent commonality object **_µx_** would collect the number of shared neighbours between **_x_** and _all nodes on the network outside of its neighbourhood_ . For large-scale networks this is a potentially huge number of nodes and for the most part will not give valuable information. Hence, in this work we will define 

16 

WR graphs according to the properties ( _n, k,_ **Λ** _,_ **_µ_** ) along with the definitions and discussions in this section. This provides us with the most effective language to investigate this interesting graph class. 

In the context of large-scale quantum networks, some aspects of WR architectures still need to be addressed. Namely, there are properties that are strictly defined by the parameters _n, k,_ **Λ** and **_µ_** which require some further discussion in order to qualify the WRN structures investigated in our work. This leads to a further sub-categorisation of weak-regularity into two key formats; _genuine_ and _internal_ weak-regularity. 

## **C. Genuine Weak-Regularity** 

We define what it means for a network to be _genuinely_ -WR. 

**Definition 4** (Genuine Weak-Regularity): _Consider a network N_ = ( _P, E_ ) _which is_ ( _n, k,_ **Λ** _,_ **_µ_** ) _-weakly-regular. This network is Genuinely-WR if there are absolutely no violations of these connectivity properties for any node_ **_x_** _∈ P within the network._ 

While this may seem like a trivial definition, it will become apparent in subsequent sections why it is necessary. Genuine weak-regularity can be readily satisfied but is sometimes quite restrictive. Indeed, a WRN defined within a two-dimensional spatial area may lead to some undesirable characteristics, such as extremely long edges required to satisfy regularity for all nodes; ultimately undermining the integrity of the network. 

Nonetheless, genuine weak-regularity conditions can be easily satisfied by considering closed networks embedded on a sphere (or other appropriate closed, three-dimensional objects). Global quantum networks, in which we consider a network that spans the Earth may be appropriately and ideally modelled via genuinely-WR quantum networks. This is illustrated in Fig. 2(a) where a network can be defined on the surface of a three-dimensional sphere. 

## **D. Internal Weak Regularity** 

As mentioned, defining regularity conditions on a two-dimensional plane can lead to unwanted features, such as extremely long edges used to “close” the network and satisfy all regularity conditions. Genuine weak-regularity avoids these features by considering closed networks embedded on some 3 dimensional surface. This may make sense for networks which span a planet, but for smaller areas this is not practical. 

Hence, we may provide an alternative model of network connectivity. It is possible to define a network that satisfies the WR connectivity properties _within a network boundary_ . That is, one can construct a WRN such that there exists a set of network nodes and edges that form a boundary 



within which all other nodes satisfy some form of weakly-regularity. That is, there exists a sub-network within this boundary _N_ int = ( _P_ int _, E_ int) according to the node and edge sets _P_ int := _P \ P_ bound _, E_ int := _E \ E_ bound. The total network model _N_ is clearly not genuinely WR since the boundary nodes **_x_** _∈ P_ bound will violate the weak-regularity conditions. Nonetheless, the internal network _N_ int will satisfy these conditions, providing a useful architecture which can be readily defined over two-dimensional regions. 

**Definition 5** (Internal Weak-Regularity): _Consider a network N_ = ( _P, E_ ) _. This network is defined as Internally-WR if there exists a network boundary P_ bound _⊂ P , E_ bound _⊂ E such that the sub-network N_ int := ( _P \ P_ bound _, E \ E_ bound) _satisfies a form of_ ( _n, k,_ **Λ** _,_ **_µ_** ) _weak-regularity._ 

Fig. 2 provides a useful illustration of the difference between genuinely-WR and internally-WR networks. One of the most useful features of this network class is that they are easy to construct, and easy to scale. It is straightforward to construct a regular _network cell_ , which when concatenated with many other cells results in an internally-WR network. Such network cells can be seen in Fig. 2(a) of the main-text. This concatenation process makes it easy to consider large-scale WRNs with open boundaries. 

17 



<!-- Start of picture text -->
(a) Genuinely WR, (b) Internally WR<br>P bound<br>Internal Network<br>Closed Network<br><!-- End of picture text -->

Figure 2. Distinction between (a) Genuine weak-regularity and (b) Internal weak-regularity. Genuinely WR networks can be embedded on a closed, three-dimensional surface such as a sphere in order to maintain regularity and avoid boundary effects. Internally WR networks satisfy weak-regularity within some nodal boundary _P_ bound, allowing us to investigate open networks which are within some two-dimensional area. 

## **E. Simplification of Notation** 

For the purposes of our work, it is possible to simplify the notation we use to describe relevant WR structures. Since we are investigating large-scale network structures, it is not desirable to precisely define the number of nodes _n_ , but allow _n_ to be encoded into other properties, e.g. nodal density, maximum link length, etc. This can be achieved, given the crucial assumption that there are enough network nodes in so that our analysis is unaffected by boundary effects or sparsity. The need for this assumption is different depending on whether we consider internal weak-regularity or genuine weak-regularity. 

- _Genuine weak-regularity_ : By definition, we do not have any issue with boundary effects in this setting since the network is effectively closed, and all nodes are unquestionably _k_ -regular. Consequently, we require a sufficient number of nodes in order to construct the closed network and ensure that there exist two end-user nodes which are not directly connected. This is not a large number of nodes and can be satisfied easily, given a particular architecture. 

- _Internal weak-regularity_ : In this setting, we assume that end-users nodes that we select always fall within the outer boundary of nodes, and we only consider nodes within this boundary. At the very least, we require that there are enough nodes _n_ within this boundary such that there exist two end-user nodes which are not directly connected (as this would defeat the purpose of investigating end-to-end network protocols). In general, this is a geometric packing problem specific to the weakly-regular architecture we are studying. 

Henceforth, these assumptions are implicitly made within each of our WRN models. This allows us to omit the precise number of nodes _n_ from key theory throughout our work and derive general results which apply to a broad range of network structures. The number of nodes and nodal density are revisited later in our studies in order to provide adequate insight to the resource requirements of WRNs. Finally, we provide one further simplification by removing detailed reference to the possible non-adjacent-commonalities within the network, described by **_µ_** . The set **_µ_** is important for the characterisation of short-range connective structures, detailing how many shared neighbours two non-connected nodes may possess. For large networks, the vast majority of non-adjacent nodes will simply share no neighbours, _µ_ = 0. This is especially true for networks which obey distance constrained connectivity rules. We find that our subsequent analyses do not require its consistent usage, therefore it can be omitted for the sake of clarity (unless otherwise specified). 

Following the implicit assumptions for the necessary number of nodes required to describe a WRN and the ability to ignore the non-adjacent commonalities, we can compactly characterise a class of WR architectures via the parameters: ( _k,_ **Λ** ). 

## **II. OPTIMAL PERFORMANCE OF WEAKLY-REGULAR NETWORKS** 

The key mathematical tool we develop in this paper is the ability to accurately and analytically derive conditions for the optimal performance of quantum WRNs. This requires graph theoretic arguments and a characterisation of 

18 

minimum network cuts. In this section we elucidate these arguments, allowing us to formally state and prove theory utilised in the main-text. 

## **A. Network Cuts** 

An important graph-theoretic concept for investigating network performance is that of _cuts_ and _cut-sets_ . Consider a network _N_ = ( _P, E_ ) with two remote end-users **_a_** _,_ **_b_** _∈ P_ . An end-user pair can be represented as a set of two unique user nodes, **_i_** = _{_ **_a_** _,_ **_b_** _}_ . This allows us to simplify notation in many settings. We define a cut _C_ as a bipartition of all network nodes _P_ into two disjoint subsets of nodes ( _P_ **_a_** _, P_ **_b_** ) such that the end-users become completely disconnected, **_a_** _∈ P_ **_b_** and **_b_** _∈ P_ **_b_** , where _P_ **_a_** _∩ P_ **_b_** = ∅. A cut _C_ generates an associated cut-set; a collection of network edges _C_<sup>˜</sup> which when removed cause the partitioning. Precisely, a cut-set is defined by 



Under the action of a cut, a network is successfully partitioned 



so that there no longer exists a path between **_a_** and **_b_** . Network cuts play a key role in the derivation of end-to-end network rates. Many network optimisation tasks can be reduced to an optimisation over all cuts with respect to single-edge/multi-edge properties. 

As discussed in the main text, any valid network cut can be associated with a multi-edge capacity _C_<sup>_m_</sup> ( _C_ ) calculated by the sum of all the single-edge capacities in the cut-set, 



where _C_ **_xy_** = _C_ ( _E_ **_xy_** ) is the single-edge capacity associated with the channel between nodes **_x_** , **_y_** . A flooding capacity is given by the network-cut between the user-pair which minimises this multi-edge capacity, 



## **B. Motivation** 

As discussed in the main-text, solving Eq. (16) for a general network and capacity distribution requires a numerical treatment via the max-flow min-cut theorem. However, for any network we can always identify at least one valid cut via _user-node isolation_ , i.e. cutting all the edges in the neighbourhood of one of the end-user nodes, _E_ **_a_** or _E_ **_b_** . This cut totally disconnects an end-user node from the network, resulting in a successful partition. We call the multi-edge capacity associated with this kind of cut as the _min-neighbourhood capacity_ , 



The min-neighbourhood capacity is always at least an upper-bound on the end-to-end flooding capacity. It is a strong indicator of a well connected and thus high-performance network. Networks which are highly connected contain many end-to-end routes between any pair of network nodes. The greater the number of end-to-end routes between an end-user pair, the more difficult it is to partition them via a cut-set, i.e. it requires more and more edges to disconnect them. As discussed in the main-text, this initiates a relationship between cut-set cardinality, _|C_<sup>˜</sup> _|_ , and distance from an end-user. Performing cuts with edges further away from a user node requires the collection of many more edges to consolidate the partition. The further from the user nodes we begin the cut, the greater the number of potential end-to-end paths we must restrict (since we have permitted a larger flow from the user node) and thus the more edges we must collect. We call this phenomenon _network cut growth_ . Once again, for general architectures and topologies it is extremely difficult to investigate the concept of network cut growth and would require numerical treatment. However, WRNs are analytically friendly and an ideal candidate for studying this concept. 

Our approach is based on the distinction between two kinds of network cuts; user-node isolation, and network-bulk cuts. Let us formally define the notion of a network-bulk: 

19 

**Definition 6** _Consider a network N_ = ( _P, E_ ) _and an end-user pair_ **_i_** = _{_ **_a_** _,_ **_b_** _} who wish to communicate. We define a network-bulk with respect to this end-user pair as the sub-network N_<sup>_′_</sup> = ( _P_<sup>_′_</sup> _, E_<sup>_′_</sup> ) _which contains all the edges and nodes which are not directly connected to the end-user nodes. That is, the node and edge sets satisfy,_ 



In a large-scale network the network-bulk _N_<sup>_′_</sup> constitutes the majority of the architecture. A _network-bulk cut_ can then be considered as a network-cut _C_<sup>_′_</sup> which is performed by exclusively collecting edges from the network-bulk rather than the user-neighbourhoods. By our previous arguments, when a network is well connected, cuts performed further away from either end-user refer to collections of edges in the network bulk. 

This leads to the primary motivation of our work: Via the intuition of network cut growth, we wish to derive a relationship between WR networks, user-node isolation and network-bulk cuts. We wish to show that in highlyconnected architectures (such as WRNs), cut growth causes cuts in the network-bulk to be unlikely candidates for the minimum cut. As a result, this allows us to identify conditions for which the upper-bound in Eq. (16) is saturated and elucidate network properties for which optimal performance is guaranteed. 

## **C. Network-Bulk Cuts** 

In this section, we derive some useful lemmas which help us to understand network cut growth and network-bulk cuts. 

**Lemma 1** _Select two nodes on a genuinely-WR quantum network N_ = ( _P, E_ ) _that represent end-users,_ **_a_** _,_ **_b_** _∈ P , and demand they that they do not share an edge or neighbour. The cut-set C_<sup>˜</sup> _which contains the fewest number of edges collects k edges._ 

**Proof.** Menger’s theorem states that for a finite, undirected graph the size of the minimum cut-set is equal to the maximum number of disjoint paths that can be found between any pair of vertices [1, 2]. Here, we are considering a ( _k,_ **Λ** ) weakly-regular graph with enough nodes to locate a pair of end-users which do not share an edge or neighbour. Every disjoint path will have to use one of the edges from the neighbourhood of an end-user, _N_ **_a_** and _N_ **_b_** . After _k_ disjoint paths, all the edges in the neighbourhoods of the end-user nodes will have already been used by one of these paths. Consequently, no more disjoint paths can be found, as the end-users can find no route to the network-bulk. Hence, the smallest cut-set cardinality will always equal _k_ . 

**Lemma 2** _Consider a_ ( _k,_ **Λ** ) _-genuinely-WR quantum network N_ = ( _P, E_ ) _such that_ **Λ** = _{_ **_λ_** _}. Select two nodes that represent end-users,_ **_a_** _,_ **_b_** _∈ P , and demand that they do not share an edge or neighbour. For any cut-set C_<sup>˜</sup> _that is restricted to edges in the network-bulk e ∈ E_<sup>_′_</sup> _,_ 



_If λj_ = _λ, ∀j then the condition holds if λ ≤ k −_ 2 _._ 

**Proof.** For a genuine ( _k, {_ **_λ_** _}_ )-regular network there will always exist a cut-set with cardinality _|C_<sup>˜</sup> iso _|_ = _k_ , achieved by isolating the neighbourhoods of either of the end-user nodes. By Lemma 1, we also know that this is the minimum cut-set cardinality. Meanwhile, a network cut which is limited to collecting edges on the network-bulk is unable to directly disconnect the neighbourhoods of **_a_** or **_b_** ( _N_ **_a_** and _N_ **_b_** respectively). Hence, any cut which is performed on the network-bulk has to restrict flow from not just the end-users, but each of its neighbours. That is, any alternative cut-set will have to cut the unique edges in the neighbourhoods of the **_a_** / **_b_** ’s neighbouring nodes. 

Let us consider the cut which restricts flow from all of the neighbouring nodes of either end-user. This cut-set will be either of the following: 





What are the cardinalities of these cut-sets? Thanks to network regularity this is easy to derive. Our goal is to restrict flow from each of the neighbours of **_a_** or **_b_** . By weak regularity, these neighbours will possess _k_ edges; they will use 

20 

one edge to connect directly to **_a_** or **_b_** , and _λj_ nodes will be connected to _other_ neighbours of **_a_** or **_b_** (by definition of adjacent commonality). As a result there will only be ( _k − λj −_ 1) effective edges that permit logical flow _outside_ of the end-user neighbour (to the rest of the network). By summing over all of the neighbours in either neighbourhood each of the new cut-set cardinalities are then 



When will this quantity be greater than _|C_<sup>˜</sup> iso _|_ ? This is easy to determine and retrieves the condition stated in the lemma, 



If this condition holds, then we can always write _|C_<sup>˜</sup> **_a_** _/_ **_b_** _| ≥ k_ as required. Any cut which is not _C_<sup>˜</sup> iso or _C_<sup>˜</sup> **_a_** _/_ **_b_** will necessarily permit flow into wider parts of the network. This will always increase the number of disjoint paths from **_a_** to **_b_** within the network, since the network is weakly-regular and connectivity properties are consistent throughout the network. It will therefore have a larger cut-set cardinality. 

Lemma 2 serves as a critical tool in our analyses. It relates analytical properties of a WRN with properties of cuts performed on its network-bulk. In abstract terms, it posits weak-regularity conditions for which we can be certain that a WRN undergoes network cut growth. 

While Lemma 2 has been formalised in the context of a WRN with consistent adjacent commonality properties (i.e. **Λ** = _{_ **_λ_** _}_ has only one multiset) it can be easily extended to account for multiple possible multisets. For this reason we propose the following definition. 

**Definition 7** (Minimum Adjacent Commonality): _Given a_ ( _k,_ **Λ** ) _-WR graph, the minimum adjacent commonality multiset_ **_λ_**<sup>_∗_</sup> _∈_ **Λ** _is that which collects the fewest edges on a network-bulk cut,_ 



The minimum adjacent commonality multiset is a characteristic of any WRN. It identifies the network nodes which possess the smallest network-bulk cuts. Ultimately, if Lemma 2 is satisfied for the minimum adjacent commonality multiset **_λ_**<sup>_∗_</sup> , then it holds for all possible nodes on the network. 

**Lemma 3** _Select two nodes on a genuinely_ ( _k,_ **Λ** ) _-WR quantum network N_ = ( _P, E_ ) _that represent end-users,_ **_a_** _,_ **_b_** _∈ P , and demand they that they do not share an edge or neighbour. For any cut-set C_<sup>˜</sup> _that is restricted to edges in the network-bulk e ∈ E_<sup>_′_</sup> _, if_<sup>�</sup> _λ∈_ **_λ_**<sup>_∗λ ≤k_(</sup><sup>_k −_2)</sup><sup>_itfollowsthat|C_˜</sup><sup>_| ≥k._</sup> 

**Proof.** Since there is now variation in **_λ_** from node to node, the network-bulk cut that is associated with **_λ_**<sup>_∗_</sup> collects the least number of edges (by definition). Then any other node with a different **_λ_** _∈_ **Λ** must necessarily collect more edges than this. Given this consideration, the proof then follows directly from Lemma 2. 

## **D. Network-Bulk Cuts on Internally-WRNs** 

**Proposition 1** _Select two nodes on an internally-WR quantum network N_ = ( _P, E_ ) _that represent end-users,_ **_a_** _,_ **_b_** _∈ P , and demand they that they do not share an edge. There exists some minimum number of network nodes n_ min _for which the the results of_ Lemma 2/3 _applies to N ._ 

This proposition is well motivated, and can be proven for a number of different WR architectures. Open boundary edges add the complication of a potential cut _C_ that utilises the boundary to find a smaller cut-set than that used in Lemma 2. However, it is always possible to construct a sufficiently large network so that a pair of end-user nodes can always be found for which Lemma 2 is satisfied. We describe these end-user nodes as _deeply-embedded_ . It is possible to provide a general characterisation of _n_ min by identifying the minimum number of nodes for which there exists a cut-set _C_<sup>˜</sup><sup>_′′_</sup> containing boundary edges _e ∈ E_ bound that has a smaller cardinality than the network-bulk cut in 

21 



<!-- Start of picture text -->
(a) (b)<br>(c) (d)<br><!-- End of picture text -->

Figure 3. Minimum node WRNs for a strict satisfaction of internal regularity for (a) honeycomb network, (b) hexagonal network, (c) Manhattan _k_ = 8 network and (d) Manhattan _k_ = 16 network. Each case resembles the smallest WRN for which there exist a pair of end-user nodes which do not share an edge or a neighbour, and possess minimum cardinality network-bulk cuts which are unaffected by the open boundary. 

Eq. (22), i.e. _|C_<sup>˜</sup><sup>_′′_</sup> _| < |C_<sup>˜</sup> **_a_** _/_ **_b_** _|_ . Indeed this can be achieved, but such generality is not particularly useful in this paper, and we leave it to future works. 

For now, we focus on WRN structures for which determining _n_ min is a basic geometric problem. The quantity _n_ min is the minimum number of nodes required to locate two end-users which do not share an edge or a neighbour, so that Lemma 2 is not compromised by the network boundary. In Fig. 3 we provide visual proofs of the minimum number of nodes required to satisfy internal-WR for the structures utilised in this paper. In each case the red regions of the network describes boundary region, while the white region resembles the internal network which is WR for the end-user nodes (which are coloured yellow). The blue dotted line is the network-bulk cut which collects the number of edges described in Lemma 2. The green cut is the smallest cut that exploits the boundary edges in order to reduce the cut-set size. The removal of any node on each network will give rise to a smaller cut than the blue cut by exploiting the boundary edges. 

As an example, consider Fig. 3(c). The network-bulk cut according to Lemma 2 for genuinely-WRNs will collect 32 edges (illustrated by the blue dotted line). However, the existence of the open boundary allows for different cuts which may compromise this result. The green dotted line depicts the smallest cut that would not be available on a 

22 

genuinely-WR version of this network. It collects 33 edges. There does not exist any other network-bulk cut that can collect fewer edges. The minimum number of nodes required in each case: 



In general, we are interested in large-scale networks with many more nodes than any of these values _n ≫ n_ min, so clearly the investigation of internally-WR graphs is well justified. When the neighbour sharing condition is relaxed for the end-users, this minimum number of nodes is reduced so that these constructions remain sufficient. 

## **E. Threshold Capacities** 

With these lemmas in hand, we can present the key mathematical tools used throughout this paper and derive the following _threshold theorems_ . 

**Theorem 1** _Consider a_ ( _k,_ **Λ** ) _-WR quantum network. Select an end-user pair_ **_i_** = _{_ **_a_** _,_ **_b_** _}, and demand they are sufficiently distant such that they do not share an edge or neighbour. Then there exists a threshold single-edge capacity C_ min _in the network, given by_ 



_where δ is a characteristic property of the network, δ_ :=<sup>�</sup> _λ∈_ **_λ_**<sup>_∗k −λ −_1</sup><sup>_,suchthatifallsingle-edgecapacitiesinthe_</sup> _network satisfy this minimum threshold, C_ **_xy_** _≥C_ min _, ∀_ ( **_x_** _,_ **_y_** ) _∈ E then flooding capacity is guaranteed to satisfy_ 



**Proof.** Let us denote the ( _k,_ **Λ** )-WRN _N_ = ( _P, E_ ). The network possesses a large set of valid cuts, C _N_ = _{Cj}j_ , which collects all of the valid network cuts _Cj_ that can successfully partition the pair of end-users. We can simultaneously define a set of _cut-set cardinalities_ , i.e. if there exist _M_ valid cuts, this is a _M_ -element multi-set that counts the number of edges contained in each of the valid network-cuts. More precisely, we can define this multiset 



By Lemma 1, the minimum-cut-set cardinality for the WRN _N_ is simply equal to its regularity, i.e. min( _cN_ ) = _k_ , and can be achieved by isolating an end-user (cutting the edges within an end-user neighbourhood). Performing usernode isolation we simply collect the edges from the user-neighbourhood _C_<sup>˜</sup> = _E_ **_i_** to generate the min-neighbourhood capacity, 



Now let us consider any network-bulk cut _C_<sup>_′_</sup> and its corresponding cut-set _C_<sup>˜</sup><sup>_′_</sup> which is restricted to collecting edges on the network-bulk _N_<sup>_′_</sup> . These types of cuts cannot use edges from the end-user-neighbourhoods and will provide a multi-edge capacity, 



In order to ensure _CN_<sup>_m_</sup> **_i_**<sup>isindeedthefloodingcapacityoftheentirenetwork,wemustensurethattheminimum</sup> network-bulk based cut is _never_ a minimum-cut, so that _C_<sup>_m_</sup> ( _C_<sup>_′_</sup> ) _≥CN_<sup>_m_</sup> **_i_**<sup>.</sup> 

When restricted to performing cuts only on the network-bulk, the set of possible cuts will be different from C _N_ , since now certain cuts are inaccessible. Instead, we may define a new set of network-cuts C _N ′_ which are restricted to the network-bulk. This generates an analogous set of cut-set cardinalities 



23 

Using Lemma 1 we can determine the smallest network-bulk based cut on a ( _k,_ **Λ** )-WR network (with no boundary effects). Since **Λ** = _{_ **_λx_** _|_ **_x_** _∈ P }_ may contain many different adjacent commonalities, it is always possible to lowerbound the cardinality of the smallest network-bulk cut-set by using the minimum adjacent commonality multiset **_λ_**<sup>_∗_</sup> . Then we can write, 



This corresponds to the minimum number of edges that must be cut from the neighbours _of the neighbours_ of the minimum end-user (e.g. the green cut-set in Fig. 4). This generates _C_<sup>˜</sup><sup>_′_</sup> as the cut-set restricted to the network-bulk with minimum cardinality. 

In order to ensure that the flooding capacity is equal to the min-neighbourhood capacity, we want to make sure that this network-bulk cut never generates a multi-edge capacity smaller than _CN_<sup>_m_</sup> **_i_**<sup>.Thatis,wewishtoensurethat</sup> 



Minimising _C_<sup>_m_</sup> ( _C_<sup>_′_</sup> ) is achieved by setting each edge in the network-bulk to its minimum value _C_ min and performing the cut which collects the fewest number of edges, such that 



Subsequently we can derive a minimum threshold capacity for any edge in the network, 



which ensures that Eq. (33) is always upheld. Imposing this threshold constraint ensures that any cut restricted to the network-bulk will generate a multi-edge capacity that is greater than or equal to the min-neighbourhood capacity. As a result, no cut performed exclusively on the network-bulk can ever undermine the flooding capacity. 

There is now only one issue; we must identify if there exists any possible _hybrid_ cut that might undermine the flooding capacity being equal to the min-neighbourhood capacity. That is, is there a cut that can collect a mixture of edges contained in the user-neighbourhood _and_ the network-bulk? Unfortunately there is, and it must be considered. Let us take a worst-case scenario where _all_ of the edges in a network-bulk are of minimum threshold capacity _C_ min. Furthermore, let’s consider that the min-neighbourhood capacity _CN_<sup>_m_</sup> **_i_**<sup>isgeneratedbyauser-neighbourhoodinwhich</sup> has ( _k −_ 1) edges of capacity _C_ min and one edge with capacity _CN_<sup>_m_</sup> **_i_**<sup>_−_(</sup><sup>_k −_1)</sup><sup>_C_min.Thatis,</sup> 



This is a worst-case situation in which one neighbourhood edge contains the majority of the min-neighbourhood capacity. In this scenario, it is possible to cut the ( _k −_ 1) edges in the neighbourhood which have the threshold value, and then to cut and additional ( _k −_ 1) edges in the network-bulk which are connected to the largest capacity edge in the neighbourhood _instead_ of this neighbourhood edge. This results in a hybrid cut _C_<sup>_′′_</sup> which generates a multi-edge capacity 



This is an absolute worst-case scenario for the network design, placing a lower-bound on the end-to-end flooding capacity. 

Consequently, provided that _C_ **_xy_** _≥C_ min _, ∀_ ( **_x_** _,_ **_y_** ) _∈ E_ then the flooding capacity always satisfies 



as required. This reveals a single-edge threshold condition for all edges in the network so to ensure that end-to-end performance is guaranteed within tight bounds. 

Theorem 1 therefore allows us to place tight performance bounds on the flooding capacity of a quantum WRN. Using only the connectivity properties of the architecture itself, and a desired end-to-end performance, we can identify a single-edge capacity constraint for all network edges. This is extremely useful, and a key result in this work. 

It is also possible to identify what additional constraints are necessary to not just guarantee a tight window of performance, but guarantee exact, optimal performance. This is achieved in the following theorem. 

24 



<!-- Start of picture text -->
|C ˜ 3 |  = 12<br>|C ˜ 2 |  = 6<br>Increasing |C ˜ |<br>· · ·<br>|C ˜ 1 |  = 3<br>· · · · · ·<br>· · · · · ·<br>. . .<br>· · ·<br><!-- End of picture text -->

Figure 4. Cut-set cardinality with respect to increasing distance from user-node on a honeycomb lattice. We show some example cuts on a honeycomb network of increasing cut-set dimension. The further one moves from a user-node **_a_** , the more edges that must be cut due to _k_ -regularity. _C_<sup>˜</sup> 1 gives the neighbourhood cut-set _E_ **_a_** , _C_<sup>˜</sup> 2 gives the smallest cut-set when limited to network-body edges _E_<sup>_′_</sup> , and _C_<sup>˜</sup> 3 gives a wider cut example. 

**Theorem 2** _Consider a_ ( _k,_ **Λ** ) _-WR quantum network. Select an end-user pair_ **_i_** = _{_ **_a_** _,_ **_b_** _}, and demand they are sufficiently distant such that they do not share an edge or neighbour. Then there exists the threshold single-edge capacity C_ min<sup>_′inthenetworkbulk,andanotherfortheuser-connectededgesC_</sup> min<sup>**_i_**</sup><sup>_givenby_</sup> 



_such that if all single-edge capacities in the network satisfy their minimum thresholds, C_ **_xy_** _≥C_ min<sup>_′, ∀_(</sup><sup>**_x_**</sup><sup>_,_</sup><sup>**_y_**)</sup><sup>_∈E′and_</sup> _C_ **_xy_** _≥C_ min<sup>**_i_**</sup><sup>_, ∀_(</sup><sup>**_x_**</sup><sup>_,_</sup><sup>**_y_**)</sup><sup>_∈E_</sup><sup>**_a_**</sup><sup>_∪E_</sup><sup>**_b_**</sup><sup>_thenfloodingcapacityisguaranteedtosatisfy_</sup> 



**Proof.** By Theorem 1 we know that if all edges satisfy _C_ **_xy_** _≥C_ min<sup>_′_=</sup><sup>_C_</sup> _N_<sup>_m_</sup> **_i_**<sup>_/δ_,forall(</sup><sup>**_x_**</sup><sup>_,_</sup><sup>**_y_**)</sup><sup>_∈E_,thentheflooding</sup> capacity satisfies Eq. (49). If we want to avoid the worst-case lower-bound it is possible to enforce an additional, slightly stricter constraint on the end-user connected edges, which we label _C_ min<sup>**_i_**.Ifweconsiderthehybridcut</sup><sup>_C′′_</sup> scenario as in the previous theorem where ( _k −_ 1) edges from the user-neighbourhood are collected and have minimum capacity _C_ min<sup>**_i_**along with (</sup><sup>_k −_1) network-bulk edges with capacity</sup><sup>_C_</sup> min<sup>_′_in order to consolidate the end-user partition.</sup> This results in a possible multi-edge capacity 



To ensure that _C_<sup>_m_</sup> ( _C_<sup>_′′_</sup> ) _≥CN_<sup>_m_</sup> **_i_**<sup>wemustthendemandthat</sup> 



Therefore, if we demand that all edges in the user-neighbourhoods satisfy _C_ **_xy_** _≥C_ min<sup>**_i_**,thentheworst-casescenario</sup> which generates the lower-bound in Theorem 1 disappears and becomes equivalent to the min-neighbourhood capacity. That is, the inequalities become 



as required. We find that _C_ min<sup>**_i_**</sup><sup>_≥C_</sup> min<sup>_′_if</sup><sup>_k≤_</sup> 2<sup>_<u>δ</u>_+ 1,whichissatisfiedinallofourexamplearchitectures.</sup> 

25 

## **F. Neighbour Sharing End-Users** 

So far we have considered end-user pairs that are not directly connected and do not share common neighbours. This is appropriate assumption since we are studying global quantum communications over very long distances; it is not interesting to consider short range users separated by single links. Furthermore, it allows for much clearer intuition surrounding increasing cut-set dimension with respect to cuts on the network-bulk as shown in Fig. 4. This assumption does not compromise the generality of our arguments, as we show in the following corollary that Theorems 1 and 2 hold even when end-user nodes share a neighbour. 

**Corollary 1** (Neighbour Sharing): _Consider a_ ( _k,_ **Λ** ) _-WR quantum network and an end-user pair_ **_i_** = _{_ **_a_** _,_ **_b_** _} within the network that do not share an edge, and possess a min-neighbourhood capacity CN_<sup>_m_</sup> **_i_**<sup>_.Eveniftheend-usernodes_</sup> _share a neighbour, Theorems 1 and 2 hold._ 

**Proof.** Consider the ( _k,_ **Λ** )-WR network and assume that the end-user pair **_i_** = _{_ **_a_** _,_ **_b_** _}_ are not directly connected, but share a neighbour. The number of common neighbours that these non-adjacent nodes share is defined by the non-adjacent commonality, _µ_ ( **_a_** _,_ **_b_** ) _>_ 0. The previous analyses do not directly apply since cuts restricted to the network-bulk will not be able to partition the two users. This is true because there will exist clear paths along the edges connected to the common neighbours of **_a_** and **_b_** . Hence, a valid network-cut of these end-users requires one to collect _µ_ ( **_a_** _,_ **_b_** ) edges from a user-neighbourhood. 

Nonetheless, our results still hold. Let us locate a network-cut that uses the minimum number of user-connected edges possible. This can be considered as a modification to the network-bulk cut which is necessary due to neighboursharing. This cut _C_<sup>_′_</sup> still collects at least<sup>�</sup> _λ∈_ **_λ_**<sup>_∗_(</sup><sup>_k−λ−_1) edges, but now</sup><sup>_µ_(</sup><sup>**_a_**</sup><sup>_,_</sup><sup>**_b_**) of those edges are actually contained</sup> in one of the user-neighbourhoods. In a worst-case scenario, one may assume that the user-connected edges which are necessarily cut possess the minimum single-edge capacity in the user-neighbourhoods, defined as 



Let all edges in the network obey a threshold capacity _C_ min = _CN_<sup>_m_</sup> **_i_**<sup>_/δ_asmotivatedbyTheorem1fornon-neighbour</sup> sharing end-users. Now, the network-cut _C_<sup>_′_</sup> which collects the fewest number of edges from the user-neighbourhood will generate a multi-edge capacity, 



However, we already know that _C_ min<sup>**_i_**=</sup><sup>_C_minsincewestatedthatalledgesinthenetworkobeythesameminimum</sup> threshold. Therefore, 



as required. Therefore, neighbour sharing does undermine the previous threshold theorems. Indeed, introducing a stricter condition on the user-connected edges (as we do in Theorem 2) only makes this result stronger, since _C_ min<sup>**_i_**</sup><sup>_≥C_minwillonlyincreasethemulti-edgecapacityinEq.(45).</sup> 

## **G. Bosonic Lossy Weakly-Regular Networks** 

When considering fibre-based networks, point-to-point links are described by bosonic pure-loss (lossy) channels. A lossy channel _L_ with transmissivity _η ∈_ (0 _,_ 1) is a phase-insensitive Gaussian quantum channel, which transforms ˆ ˆ ˆ ˆ input quadratures **x** = (ˆ _q,_ ˆ _p_ )<sup>_T_</sup> according to **x** _�→_<sup>_√_</sup> _<u>η</u>_ **x** +<sup>_√_</sup> 1 _− η_ **x** env (where the environment is in a vacuum state) describing the interaction of bosonic mode with a zero-temperature bath [3]. 

For lossy quantum networks, the most important property is channel length, or from a network perspective, _internodal separation_ . For a given edge ( **_x_** _,_ **_y_** ) _∈ E_ connecting two users in a network, the inter-nodal separation is simply the distance _d_ **_xy_** between them. All two-way assisted quantum and private capacities of the lossy channel are precisely known via the PLOB bound [4], 



where the inter-nodal separation is related to the transmissivity via _η_ **_xy_** = 10<sup>_−γd_</sup><sup>**_xy_**</sup> . For current, state of the art fibre-optics the loss rate is _γ_ = 0 _._ 02 per km (which equates to a loss rate of 0 _._ 2 dB/km). Since these separations 

26 

directly dictate the channel quality between nodes they must be precisely engineered and distributed in order to guarantee strong end-to-end performance. 

The direct application of Theorem 1 to bosonic lossy quantum networks allows us to translate the notion of threshold capacities into something more physical. Indeed, since the capacity of pure-loss channels is known exactly, it is possible to translate the threshold capacity into a _maximum inter-nodal separation_ . 

**Corollary 2** _Consider a_ ( _k,_ **Λ** ) _-WR quantum network which is connected by bosonic lossy channels. Select an enduser pair_ **_i_** = _{_ **_a_** _,_ **_b_** _} within the network that do not share an edge, and possess a min-neighbourhood capacity CN_<sup>_m_</sup> **_i_**<sup>_._</sup> _Then, there exists a maximum inter-nodal separation for all edges within the network,_ 



_for which the flooding capacity satisfies_ 



_If ∃ d_ **_xy_** _< d_<sup>max</sup> _N ,_ ( **_x_** _,_ **_y_** ) _∈ E, this remains an upper-bound on the optimal network performance, C_<sup>_m_</sup> ( **_i_** _, N_ ) _≤CN_<sup>_m_</sup> **_i_**<sup>_._</sup> **Proof.** Consider a valid pair of end-users **_i_** = _{_ **_a_** _,_ **_b_** _}_ embedded within a ( _k,_ **Λ** )-WR quantum network. Then as before, there exists a threshold capacity _C_ min =<sup><u>1</u></sup> _δ_<sup>_C_</sup> _N_<sup>_m_</sup> **_i_**<sup>thatcanbeenforcedtoensurethefloodingcapacitybetween</sup> these users is bounded by their min-neighbourhood capacity, _CN_<sup>_m_</sup> **_i_**<sup>.SupplantingthePLOBboundintothecapacity</sup> condition in Theorem 1, 



this readily translates to, 



Therefore the threshold capacity becomes an upper-bound on the maximum link-length permitted within the network. We can thus define this maximum length, 



which when satisfied ensures that 2( _k −_ 1) _CN_<sup>_m_</sup> **_i_**<sup>_/δ≤Cm_(</sup><sup>**_i_**</sup><sup>_, N_)</sup><sup>_≤C_</sup> _N_<sup>_m_</sup> **_i_**<sup>.</sup> Now suppose that there exists a channel within the network-bulk that violate this max-bulk separation, i.e. _∃ d_ **_xy_** _> d_<sup>max</sup> _N_<sup>_′_</sup> for ( **_x_** _,_ **_y_** ) _∈ E_<sup>_′_</sup> . This violates the threshold capacity condition from Theorem 1 meaning that the minimum-cut in the network is not guaranteed to satisfy the performance bounds. However, if the minimum-cut undergoes a transition due to the introduction of poor quality channels in the network-bulk, it cannot improve the network flooding capacity; it can only deteriorate network performance. Therefore the min-neighbourhood capacity remains an upper-bound on the optimal network performance, _C_<sup>_m_</sup> ( **_i_** _, N_ ) _≤CN_<sup>_m_</sup> **_i_**<sup>,asbefore.</sup> 

In order to achieve a stricter performance guarantee, we can apply Theorem 2 to bosonic lossy channels and derive slightly stricter constraints on user-connected channels. 

**Corollary 3** _Consider a_ ( _k,_ **Λ** ) _-WR quantum network which is connected by bosonic lossy channels. Select an enduser pair_ **_i_** = _{_ **_a_** _,_ **_b_** _} within the network that do not share an edge, and possess a min-neighbourhood capacity CN_<sup>_m_</sup> **_i_**<sup>_._</sup> _Then, there exists a maximum link-length in the network-bulk_ 



_and a maximum link-length for all the user-connected edges,_ 



_which when satisfied guarantee that the flooding capacity is equal to the min-neighbourhood capacity,_ 



_If ∃ d_<sup>max</sup> _N_ **_i_** _< d_ **_xy_** _≤ d_<sup>max</sup> _N ,_ ( **_x_** _,_ **_y_** ) _∈ E_ **_a_** _∪ E_ **_b_** _, we regain Theorem 2. If ∃ d_ **_xy_** _> d_<sup>max</sup> _N ,_ ( **_x_** _,_ **_y_** ) _∈ E, then the performance guarantee is violated, but this remains an upper-bound on the optimal network performance, C_<sup>_m_</sup> ( **_i_** _, N_ ) _≤CN_<sup>_m_</sup> **_i_**<sup>_._</sup> 

27 

**Proof.** This is a specification of Theorem 2 to bosonic lossy channels where the edges in the neighbourhoods of Alice **_a_** and Bob **_b_** may possess their own, stricter constraint in order to completely guarantee optimal performance. The proof follows directly by supplementing the PLOB bound into the threshold capacity expressions. 

## **III. NODAL DENSITIES AND BOSONIC LOSSY WEAKLY-REGULAR NETWORKS** 

## **A. Sparse Constructions** 

Nodal density is defined as the number of nodes _n_ per unit area of the network, 



where _A_ is some area in which the network is defined. This is a crucial measure of network resources, especially for quantum networks where there is a very high cost of constructing quantum devices at every node. In many network settings, it is desirable to minimise the nodal density necessary to promise strong end-to-end performance. For this reason, it is also useful to define a _minimum nodal density_ . For a class of network, N = _{Nj}j_ , such that all instances _N ∈_ N are constrained to some implicit structure, the minimum nodal density describes how it can be constructed in the sparsest way possible. It refers to a limiting scenario in which the network is least dense, and that all other instances of the network topology will possess more nodes per unit area. This is summarised below in a general 

**Definition 8** (Sparse Construction): _Consider a class of network_ N = _{Nj}j which imposes a fixed, single-edge distance constraint on its networks N_ = ( _P, E_ ) _∈_ N _so that_ 



_The sparse construction is an instance of this class which minimises its network nodal density,_ 



_where ρ_<sup>min</sup> _N is the minimum permitted nodal density of a network N ∈_ N _._ 

Clearly, for very general classes of distance-constrained networks this minimisation is extremely difficult. However, for analytical classes such as WRNs, this becomes rather easy and reduces to a geometric packing problem. Finally, to provide simplifications in subsequent arguments, we make the following proposition. 

**Proposition 2** _For a class of single-edge distance constrained networks N ∈_ N _, such that d_ **_xy_** _≤ d_<sup>max</sup> _N for all_ ( **_x_** _,_ **_y_** ) _∈ E, then the minimum nodal density can always be expressed as_ 



_such that ξ is a quantity which characterises the network class_ N _._ 

It is always possible to express the min-density as proportional to the inverse squared value of the maximum internodal separation in the network. This is obviously true for _any measure of area_ since _ρ ∝ A_<sup>_−_1</sup> and _A ∝ d_<sup>2</sup> where _d_ is some distance measure. Yet, for what follows we find that it is useful to closely relate _d_<sup>max</sup> _N_ and _ρ_<sup>min</sup> _N_ in this way. 

## **B. Sparse Constructions of Weakly-Regular Networks** 

In this section we endeavour to lower-bound the min-nodal densities for the classes of WRN. 

## _1. Honeycomb Network_ 

Our model of a honeycomb network ( _k_ = 3 and **_λ_**<sup>_∗_</sup> = _{_ 0 _}_<sup>_∪_3</sup> ) is the following: Consider a single, initial hexagon consistent of _n_ -nodes connected by 6 edges. Let us call this the _r_ = 1 ring of the network. To construct a larger network, we proceed by adding further hexagons concentrically around the initial shape. Each edge of the _r_ = 1 ring is used as an edge of a hexagon in the _r_ = 2 ring. We can continue to create a larger and larger network structure 

28 

by concentrically connecting rings of hexagons to the previous one. As each ring is added, there will be 6 _r_ hexagons added to the overall structure. See Fig. 3(a) as an example. 

For any fixed number of rings _r_ we can identify the number of nodes within the network. The number of unique nodes added with the addition of each new ring follows a recursive equation 



It is simple to solve this set of recursive equations so that _n_ ˜ _r_ takes the form, 



As a result, given an _r_ -ring honeycomb network structure, the total number of nodes will be 



The minimum number of nodes required to locate a pair of non-edge sharing end-users within an internal boundary is found at _r_ = 2. Hence the minimum number of nodes we must consider is simply _n_ hc(2) = 24. 

We may also use this relationship in order to determine the minimum nodal-density _ρ_ min of a honeycomb network when the maximum permitted fibre-length is _d_<sup>max</sup> _N_ . Since this is the maximum permitted length and a honeycomb lattice can form a regular tiling, then _ρ_ min is satisfied when every edge in the network is exactly _d_<sup>max</sup> _N_ . Hence, given an _r_ -ring network, the maximum area it will span is 



Hence, an _r_ -ring minimum nodal density can be computed by 



By taking the asymptotic limit of _r →∞_ we can more accurately capture a lower-bound on the nodal density of a honeycomb network which satisfies this fibre-length constraint (as a larger network will permit a more accurate averaging process). As a result, we may compute 



as a lower-bound on the nodal-density of a weakly-regular honeycomb network which satisfies a maximum inter-nodal separation. Hence the characteristic quantity of honeycomb networks satisfies _ξ ≥_ 4 _/_ (3 _√_ 3). 



A class of hexagonal network ( _k_ = 6 and **_λ_**<sup>_∗_</sup> = _{_ 2 _}_<sup>_∪_6</sup> ) follows the same logic as the honeycomb structure, just with additional nodes located within every hexagon (see Fig. 3(b)). As a result, we can immediately write 



Then, in an _r_ -ring hexagonal structure the total number of nodes is given by, 



hence the minimum number of nodes required for internal WR is _n_ hex(2) = 31. Meanwhile, the maximum area spanned by an _r_ -ring hexagonal network is equal to that of the honeycomb network, _A_<sup>max</sup> hex<sup>=</sup><sup>_A_max</sup> hc<sup>.Thus,defining</sup> 



we can easily compute a lower-bound on the nodal density as before 



Hence the characteristic quantity of hexagonal networks satisfies _ξ ≥_ 2 _/√_ 3. 

29 

## _3. Manhattan-Inspired Networks_ 

Consider a class of WRN such that _k_ = 8 and **_λ_**<sup>_∗_</sup> = _{_ 2 _,_ 4 _}_<sup>_∪_4</sup> , as depicted in Fig. 3(c). To construct this network, we can simply concatenate a cell (consisting of 9 nodes) into an _r × r_ grid which can be easily evaluated. For a network which is arranged into a _r_ -length square grid there will exist _r_<sup>2</sup> network cells. In order to maximise the area spanned by each network cell, we assign the longest possible edge in the cell to be of length _d_<sup>max</sup> _N_ . For the _k_ = 8 network cell, this means that the diagonal edges in each square must be of length _d_<sup>max</sup> _N_ . Hence, the area of the total 9 node cell will be<sup><u>1</u></sup> 2<sup>_d_</sup> _N_<sup>max</sup> 2. In an _r_ -ring network this results in a total area of <u>12</u><sup>(</sup><sup>_rd_</sup> _N_<sup>max</sup> )<sup>2</sup> . Furthermore, the total number of nodes will be given by, 



which can be obtained by simply counting the number of nodes on each horizontal/vertical row of the grid. We can thus define the function, 



As a result, a lower-bound on the minimum nodal density can be readily computed 



Therefore the characteristic quantity is lower-bounded by _ξ ≥_ 2. 

A similar Manhattan-like class can be constructed such that _k_ = 16 and **_λ_**<sup>_∗_</sup> = _{_ 4 _,_ 8 _,_ 8 _,_ 8 _}_<sup>_∪_4</sup> , as depicted in Fig. 3(d). Using this network cell to construct a larger network, we must constrain the longest edge in the network cell to be of length _d_<sup>max</sup> _N_ . This causes us to constrain the diagonal edge from central nodes on the boundary of the cell to connected nodes at the opposite corner. The maximum area spanned by a network cell is then<sup><u>4</u></sup> 3<sup>_d_</sup> _N_<sup>2.Ifweagainconsideran</sup> 2 _r × r_ cell square grid network, then that the total area is _A_ max( _r_ ) =<sup><u>4</u></sup> 3<sup>_r_2</sup><sup>_d_</sup> _N_<sup>max</sup> . Via a counting argument, the total number of nodes in an _r_ -radius network will be 



As a result, we can define the minimum nodal density function, 



Finally, the lower-bound can be given 



Hence the characteristic quantity can be lower-bounded by _ξ ≥_ 6. 

## **C. Nodal Density and End-to-End Performance** 

**Theorem 3** _Consider a_ ( _k,_ **Λ** ) _-WR quantum network N_ = ( _P, E_ ) _which is connected by bosonic lossy channels. Select an end-user pair_ **_i_** = _{_ **_a_** _,_ **_b_** _} within the network that do not share an edge, and a desired min-neighbourhood capacity CN_<sup>_m_</sup> **_i_**<sup>_.Inordertoguaranteeoptimalperformance,thereexistsaminimumnodaldensitywithinthenetwork,_</sup> 



_where ξ is characteristic of the WR architecture being considered._ 

**Proof.** In Corollaries 2 and 3, a global fibre-length constraints are placed on the network in order to guarantee a particular flooding capacity via user-node isolation. Using Corollary 2, if all edges ( **_x_** _,_ **_y_** ) _∈ E_ satisfy an maximum link-length constraint, 



30 

then the flooding capacity is guaranteed to satisfy 2( _k −_ 1) _CN_<sup>_m_</sup> **_i_**<sup>_/δ≤Cm_(</sup><sup>**_i_**</sup><sup>_, N_)</sup><sup>_≤C_</sup> _N_<sup>_m_</sup> **_i_**<sup>.Ifweapplytheadditional</sup> constraint for user-connected edges such that 



then we can guarantee that _C_<sup>_m_</sup> ( **_i_** _, N_ ) = _CN_<sup>_m_</sup> **_i_**<sup>.</sup> 

These link-length constraints result in a minimum nodal density for the entire network which is easy to investigate via the appropriate sparse construction. Using Eq. (59) we can directly write 



where the characteristic quantity, _ξ_ is derived from the sparse construction. This offers a lower-bound on the necessary nodal density required to guarantee a particular flooding capacity. 

Summarising, in order for the flooding capacity between **_a_** and **_b_** will be equal to the min-neighbourhood capacity _C_<sup>_m_</sup> ( **_i_** _, N_ ) = _CN_<sup>_m_</sup> **_i_**<sup>,thenodaldensitymust(atleast)satisfythelower-bound</sup><sup>_ρN≥ρ_min</sup> _N_<sup>.</sup> 

The tightness of this lower-bound depends on how _ξ_ is derived. Ideally, one would be able to take into the consideration the stricter constraint _d_<sup>max</sup> _N_ **_i_** required to guarantee _C_<sup>_m_</sup> ( **_i_** _, N_ ) = _CN_<sup>_m_</sup> **_i_**<sup>withequality.</sup> Solving a sparse construction with multiple edge constraints is not straightforward, hence one may need to use a lower-bound for _ξ_ , as we have in this work. This nonetheless delivers informative bounds on the nodal density required for optimal performance. 

## **D. Critical Nodal Density** 

Following recent works which have investigated critical network resources required for effective end-to-end performance on quantum networks, we define a critical nodal density _ρ_ crit as the network density required to achieve an end-to-end rate of 1 bit per network use. For bosonic lossy networks constructed in a weakly-regular structure, we can derive this value analytically. 

**Corollary 4** _Consider a_ ( _k,_ **Λ** ) _-WR quantum network N_ = ( _P, E_ ) _which is connected by bosonic lossy channels. The critical nodal-density of the network is lower-bounded by_ 



_where ξ is characteristic of the WR architecture being considered._ 

In Eq. (80), recall that _γ_ is the fibre-loss rate which takes a typical value of _γ ≈_ 0 _._ 02, and _δ_ is defined in Eq. (32) as before. For WRNs explored in this paper we can readily compute their critical nodal densities: 



The critical density does not necessarily decrease with respect to nodal degree; while the Manhattan-inspired networks have larger regular degrees ( _k_ = 8 _,_ 16) than the hexagonal network ( _k_ = 6), the critical density of the hexagonal network remains smaller. This is reasonably intuitive, since there is clearly a tradeoff between performance, nodal degree and nodal density. 

Importantly, we notice that the minimum required nodal density is of the order _∼_ 10<sup>_−_4</sup> nodes per km<sup>2</sup> which corroborates the results of Ref. [5] for which the critical nodal density is studied for more general class of random 

31 

Waxman networks. Accurate assessments of this kind are crucial to ensure that effective and high-performance quantum networks are constructed in the future. 

- [1] K. Menger, Zur allgemeinen kurventheorie, Fundam. Math. **10** , 96 (1927). 

- [2] R. Aharoni and E. Berger, Menger’s theorem for infinite graphs, Invent. Math. **176** , 1 (2009). 

- [3] C. Weedbrook, S. Pirandola, R. Garc´ıa-Patr´on, N. J. Cerf, T. C. Ralph, J. H. Shapiro, and S. Lloyd, Gaussian quantum information, Rev. Mod. Phys. **84** , 621 (2012). 

- [4] S. Pirandola, R. Laurenza, C. Ottaviani, and L. Banchi, Fundamental limits of repeaterless quantum communications, Nat. Commun. **8** , 15043 (2017). 

- [5] Q. Zhuang and B. Zhang, Quantum communication capacity transition of complex quantum networks, Phys. Rev. A **104** , 022608 (2021). 


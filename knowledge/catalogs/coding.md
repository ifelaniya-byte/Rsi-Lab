# Teaching catalog: computer science and programming
# Built by the collective leader (nvidia/nemotron-3-super-120b-a12b:free)

## 01 Programming Paradigms
CODE-01-001 | Imperative Programming | Describes computation as statements that change program state | Use when modeling step‑by‑step instructions
CODE-01-002 | Declarative Programming | Specifies what the program should accomplish without detailing control flow | Use when expressing logic, queries, or configuration
CODE-01-003 | Procedural Programming | Organizes code into reusable procedures or functions | Use when structuring programs around routines and subroutines
CODE-01-004 | Object-Oriented Programming (OOP) | Encapsulates data and behavior in objects with inheritance and polymorphism | Use when modeling real‑world entities and hierarchies
CODE-01-005 | Functional Programming | Treats computation as evaluation of pure functions avoiding side effects | Use when leveraging immutability, higher‑order functions, and referential transparency
CODE-01-006 | Logic Programming | Expresses programs as sets of logical relations and uses inference to derive results | Use when solving problems via rule‑based querying (e.g., Prolog)
CODE-01-007 | Aspect-Oriented Programming | Separates cross‑cutting concerns (logging, security) from core logic | Use when applying concerns modularly across many modules
CODE-01-008 | Event-Driven Programming | Program flow is determined by events such as user actions or messages | Use when building GUIs, servers, or reactive systems
CODE-01-009 | Reactive Programming | Propagates changes automatically through data streams and change‑propagation | Use when handling asynchronous data flows with back‑pressure support
CODE-01-010 | Parallel Programming Paradigm | Executes multiple computations simultaneously on multiple cores | Use when leveraging multicore CPUs for throughput or latency reduction
CODE-01-011 | Generic Programming | Writes algorithms in terms of types to be specified later | Use when creating reusable containers and algorithms independent of data type
CODE-01-012 | Metaprogramming | Programs that treat other programs as data, enabling code generation or modification | Use when implementing macros, templates, or reflective capabilities

## 02 Data Structures
CODE-02-001 | Arrays | Contiguous block of fixed-size elements indexed by integers | Use when random access and cache‑friendly storage are needed
CODE-02-002 | Singly Linked List | Linear list where each node points to the next node only | Use when frequent insertions/deletions at front are required
CODE-02-003 | Doubly Linked List | Nodes have pointers to both next and previous nodes | Use when bidirectional traversal and O(1) deletions are needed
CODE-02-004 | Stack | LIFO container supporting push and pop operations | Use when managing function calls, expression evaluation, or undo/redo
CODE-02-005 | Queue | FIFO container supporting enqueue and dequeue operations | Use when scheduling tasks, breadth‑first search, or buffering streams
CODE-02-006 | Priority Queue | Queue where elements are served by priority order | Use when implementing Dijkstra’s algorithm, event simulation, or scheduling
CODE-02-007 | Hash Table | Key‑value store using a hash function to map keys to buckets | Use when average‑case O(1) lookup, insert, delete is required
CODE-02-008 | Binary Search Tree | Binary tree with left < parent < right ordering property | Use when ordered dictionary with logarithmic operations is needed
CODE-02-009 | AVL Tree | Self‑balancing BST ensuring height O(log n) after each operation | Use when worst‑case guarantees for search/insert/delete are required
CODE-02-010 | Red‑Black Tree | BST with coloring rules guaranteeing approximate balance | Use when a balanced tree with lower constant factors than AVL is desired
CODE-02-011 | B‑Tree | Multi‑way search tree optimized for disk‑based storage |

## 03 Algorithms and Complexity
CODE-03-001 | Sorting Algorithms | Techniques for ordering elements, including comparison and non‑comparison sorts | Use when needing efficient ordering of data
CODE-03-002 | Graph Algorithms | Methods for traversing, searching, and optimizing graphs (shortest path, MST, flow) | Use when modeling networks or relationships
CODE-03-003 | Dynamic Programming | Solving problems by breaking into overlapping subproblems and caching results | Use when optimal substructure and overlapping subproblems exist
CODE-03-004 | Greedy Algorithms | Making locally optimal choices to achieve a global optimum | Use when problem exhibits greedy‑choice property
CODE-03-005 | Divide and Conquer | Recursively splitting problem into subproblems, solving independently, combining | Use for problems like merge sort, FFT, closest pair
CODE-03-006 | Backtracking and Branch and Bound | Systematic search with pruning to find solutions or optimal values | Use for constraint satisfaction, combinatorial optimization
CODE-03-007 | String Algorithms | Pattern matching, suffix arrays, tries, and text processing techniques | Use when processing large textual data
CODE-03-008 | Randomized Algorithms | Algorithms that make random choices to improve expected performance | Use when deterministic solutions are too slow or complex
CODE-03-009 | Approximation Algorithms | Algorithms providing near‑optimal solutions with provable guarantees | Use for NP‑hard problems where exact solution is infeasible
CODE-03-010 | Computational Geometry | Algorithms for geometric objects (convex hull, intersection, Voronoi) | Use in graphics, CAD, robotics, GIS
CODE-03-011 | Number Theoretic Algorithms | Algorithms based on modular arithmetic, primality testing, factoring | Use in cryptography, hashing, random number generation
CODE-03-012 | Parallel Algorithms | Designing algorithms to run concurrently on multiple processors | Use when leveraging multicore, GPU, or cluster resources
CODE-03-013 | Complexity Classes | Classification of problems by resource bounds (P, NP, PSPACE, etc.) | Use when analyzing problem difficulty and algorithm limits

## 04 Advanced Data Structures
CODE-04-001 | Trie (Prefix Tree) | Tree‑like structure storing strings with common prefixes efficiently | Use for autocomplete, spell checking, IP routing
CODE-04-002 | Skip List | Probabilistic linked list with multiple levels for fast search | Use when needing balanced search with simpler implementation than trees
CODE-04-003 | Bloom Filter | Space‑efficient probabilistic set membership test with false positives | Use for cache filtering, network packet screening
CODE-04-004 | Fenwick Tree (Binary Indexed Tree) | Data structure for prefix sum queries and updates in O(log n) | Use for cumulative frequency tables, dynamic statistics
CODE-04-005 | Segment Tree | Tree storing intervals, supporting range queries and updates | Use for range minimum/maximum, sum, or interval stabbing queries
CODE-04-006 | Disjoint Set Union (Union‑Find) | Structure maintaining partition of elements with union and find ops | Use for Kruskal’s MST, percolation, connectivity queries
CODE-04-007 | Heap (Binary, Binomial, Fibonacci) | Priority queue with efficient extract‑min/max and decrease‑key | Use in Dijkstra, Prim, scheduling, event simulation
CODE-04-008 | B+ Tree | Balanced tree where all records stored in leaves, optimized for range scans | Use in database indexing, file systems
CODE-04-009 | R‑Tree | Spatial index for multi‑dimensional data (rectangles, polygons) | Use for GIS, collision detection, spatial queries
CODE-04-010 | Splay Tree | Self‑adjusting BST moving accessed nodes to root | Use when access patterns exhibit locality
CODE-04-011 | Treap | Randomized BST combining heap priority with BST order | Use when needing expected logarithmic operations with simplicity
CODE-04-012 | Rope (data structure) | Binary tree for efficient large string manipulation (insert/delete) | Use in text editors, version control diff handling
CODE-04-013 | Persistent Data Structures | Structures preserving previous versions after modifications | Use for functional programming, undo/redo, temporal queries

## 05 Software Engineering Practices
CODE-05-001 | Version Control Systems (Git) | Tools tracking changes to source code over time | Use for collaborative development, history, branching
CODE-05-002 | Continuous Integration/Continuous Deployment (CI/CD) | Automated pipelines building, testing, and releasing software | Use to ensure rapid, reliable delivery
CODE-05-003 | Test-Driven Development (TDD) | Writing tests before implementation to drive design | Use to improve code quality and reduce defects
CODE-05-004 | Behavior-Driven Development (BDD) | Extending TDD with natural language specifications | Use for clearer stakeholder communication
CODE-05-005 | Code Review and Pair Programming | Collaborative examination of code to catch defects early | Use to increase knowledge sharing and code correctness
CODE-05-006 | Refactoring Techniques | Improving code structure without changing external behavior | Use to reduce technical debt and improve maintainability
CODE-05-007 | Design Patterns (Creational, Structural, Behavioral) | Reusable solutions to common software design problems | Use to convey design intent and improve flexibility
CODE-05-008 | Architectural Styles (Microservices, Monolith, Serverless) | High‑level organization of system components | Use when selecting deployment and scaling strategies
CODE-05-009 | Domain-Driven Design (DDD) | Modeling software around core domain concepts | Use for complex business logic alignment
CODE-05-010 | Agile Methodologies (Scrum, Kanban) | Iterative, incremental approaches emphasizing feedback | Use to adapt to changing requirements
CODE-05-011 | DevOps Culture and Tooling | Integrating development and operations for faster delivery | Use to improve deployment frequency and reliability
CODE-05-012 | Software Metrics and Quality Assurance | Quantitative measures (defect density, cyclomatic complexity) | Use to monitor and improve software quality
CODE-05-013 | Legal and Ethical Aspects of Software | Licensing, IP, privacy, and societal impact considerations | Use to ensure compliance and responsible engineering

## 06 Operating Systems Concepts
CODE-06-001 | Process Management and Scheduling | Creation, termination, and CPU allocation of processes | Use when designing multitasking systems
CODE-06-002 | Memory Management (Paging, Segmentation, Virtual Memory) | Techniques for allocating and protecting memory | Use to provide isolation and efficient memory use
CODE-06-003 | File Systems and Storage Hierarchies | Organization of data on disks, SSDs, and caches | Use for persistent storage and I/O performance
CODE-06-004 | Input/Output Systems and Device Drivers | Interfacing OS with hardware peripherals | Use when building portable, extensible I/O stacks
CODE-06-005 | Concurrency Control (Mutexes, Semaphores, Monitors) | Synchronization primitives for safe shared access | Use to prevent race conditions in concurrent code
CODE-06-006 | Deadlock Detection and Prevention | Strategies to avoid or resolve circular wait conditions | Use in resource‑allocation systems
CODE-06-007 | Virtualization and Containers | Abstracting hardware to run multiple isolated OS instances | Use for server consolidation, sandboxing, cloud
CODE-06-008 | Interprocess Communication (IPC) Mechanisms | Pipes, message queues, shared memory, sockets | Use for data exchange between processes
CODE-06-009 | Security and Protection Rings | Hardware‑enforced privilege levels isolating kernel/user | Use to enforce least privilege and system integrity
CODE-06-010 | Real-Time Operating Systems | OS guaranteeing bounded response times for critical tasks | Use in embedded, automotive, aerospace systems
CODE-06-011 | Power Management and Scheduling | Techniques to reduce energy consumption while maintaining performance | Use for mobile devices and data centers
CODE-06-012 | Bootstrapping and Firmware (UEFI, BIOS) | Initialization code loading the OS from storage | Use when developing low‑level system software
CODE-06-013 | Distributed Operating Systems | OS managing a network of computers as a single system | Use for clusters, grid computing, edge fabrics

## 07 Computer Networks
CODE-07-001 | OSI and TCP/IP Models | Layered frameworks describing network communication | Use for understanding and designing network protocols
CODE-07-002 | Ethernet and LAN Technologies | Wired local‑area networking standards (IEEE 802.3) | Use for building office and data‑center networks
CODE-07-003 | Wireless Networks (Wi‑Fi, Bluetooth, 5G) | Radio‑based access technologies | Use for mobile, IoT, and wireless LAN deployments
CODE-07-004 | Routing Algorithms (OSPF, BGP, RIP) | Protocols determining paths for packet forwarding | Use in routers and internet backbone
CODE-07-005 | Transport Protocols (TCP, UDP, QUIC) | End‑to‑end data delivery services (reliable, unreliable, multiplexed) | Use for application‑level communication
CODE-07-006 | Network Security (TLS/SSL, IPsec, Firewalls) | Mechanisms protecting data confidentiality and integrity | Use to secure communications and perimeter defense
CODE-07-007 | Network Performance and QoS | Metrics (latency, jitter, loss) and traffic shaping techniques | Use to guarantee service levels for real‑time apps
CODE-07-008 | Software-Defined Networking (SDN) | Separation of control plane from data plane via controllers | Use for programmable, agile network management
CODE-07-009 | Network Function Virtualization (NFV) | Running network services as software VMs/containers | Use to reduce hardware dependency and increase flexibility
CODE-07-010 | Content Delivery Networks (CDN) | Distributed servers delivering content close to users | Use for low‑latency web and media distribution
CODE-07-011 | Peer-to-Peer Architectures | Decentralized systems where nodes act as clients and servers | Use for file sharing, blockchain, distributed computing
CODE-07-012 | Network Management Protocols (SNMP, NETCONF) | Protocols for monitoring and configuring network devices | Use for operational visibility and automation
CODE-07-013 | Internet of Things (IoT) Networking | Constrained‑device protocols (CoAP, MQTT, LoRaWAN) | Use for massive sensor/actuator deployments

## 08 Database Systems
CODE-08-001 | Relational Model and SQL | Tabular data model with declarative query language | Use for structured data with strong consistency needs
CODE-08-002 | NoSQL Databases (Document, Key‑Value, Column, Graph) | Non‑relational stores optimized for specific workloads | Use for flexible schema, high write throughput, or graph traversals
CODE-08-003 | ACID Transactions and Concurrency Control | Guarantees of Atomicity, Consistency, Isolation, Durability | Use when correctness under concurrent access is critical
CODE-08-004 | Indexing Techniques (B‑Tree, Hash, GiST, GIN) | Structures accelerating data retrieval | Use to speed up SELECT, JOIN, and predicate evaluation
CODE-08-005 | Query Optimization and Execution Plans | Cost‑based selection of efficient query evaluation strategies | Use to minimize response time and resource usage
CODE-08-006 | Distributed Databases and Sharding | Partitioning data across nodes for scalability | Use when single‑node capacity is insufficient
CODE-08-007 | Replication and Consistency Models | Copying data for fault tolerance; strong, eventual, causal | Use to balance availability, latency, and correctness
CODE-08-008 | Data Warehousing and OLAP | Subject‑oriented, integrated stores for analytical querying | Use for business intelligence and reporting
CODE-08-009 | In-Memory Databases | Storing primary data in RAM for ultra‑low latency | Use for real‑time analytics, caching, high‑frequency trading
CODE-08-010 | Temporal and Spatial Databases | Managing time‑varying and geographic information | Use for historical analysis, GIS, location‑based services
CODE-08-011 | Database Security and Encryption | Protecting data at rest and in transit via access controls, crypto | Use to meet compliance and prevent breaches
CODE-08-012 | Backup, Recovery, and Point-in-Time Restore | Strategies for preserving data against loss | Use to ensure durability and business continuity
CODE-08-013 | NewSQL and Hybrid Transactional/Analytical Processing (HTAP) | Systems combining OLTP scalability with OLAP capabilities | Use for real‑time operational analytics

## 09 Artificial Intelligence and Machine Learning
CODE-09-001 | Supervised Learning (Regression, Classification) | Learning from labeled examples to predict outputs | Use when labeled data is available for prediction tasks
CODE-09-002 | Unsupervised Learning (Clustering, Dimensionality Reduction) | Discovering hidden structure in unlabeled data | Use for exploratory analysis, compression, feature learning
CODE-09-003 | Reinforcement Learning | Learning optimal policies via reward signals from environment | Use for sequential decision‑making, robotics, game AI
CODE-09-004 | Deep Learning Architectures (CNN, RNN, Transformer) | Neural networks with multiple layers for complex patterns | Use for image, speech, language, and sequential data
CODE-09-005 | Transfer Learning and Fine-tuning | Adapting pre‑trained models to new tasks with little data | Use to reduce training time and improve performance
CODE-09-006 | Generative Models (GAN, VAE, Diffusion) | Models that generate new data resembling training distribution | Use for synthetic data, image synthesis, drug discovery
CODE-09-007 | Natural Language Processing (NLP) Basics | Techniques for understanding and generating human language | Use for chatbots, translation, sentiment analysis
CODE-09-008 | Computer Vision Fundamentals | Algorithms for interpreting visual information from images/video | Use for object detection, facial recognition, autonomous driving
CODE-09-009 | Explainable AI (XAI) | Methods to make model decisions interpretable to humans | Use when trust, compliance, or debugging is required
CODE-09-010 | AI Ethics and Fairness | Principles ensuring AI respects rights, avoids bias, and is accountable | Use to guide responsible AI development
CODE-09-011 | AutoML and Neural Architecture Search | Automating model selection and hyperparameter tuning | Use to democratize AI and reduce expert workload
CODE-09-012 | Edge AI and Model Compression | Deploying AI on resource‑constrained devices via pruning, quantization | Use for latency‑sensitive, privacy‑preserving applications
CODE-09-013 | AI Safety and Robustness | Ensuring AI behaves reliably under distribution shifts and adversarial inputs | Use for critical systems where failure is costly

## 10 Distributed Systems
CODE-10-001 | Consensus Algorithms (Paxos, Raft, Zab) | Protocols for agreeing on a single value among faulty nodes | Use for replicated state machines, leader election
CODE-10-002 | Distributed Locking and Coordination | Mechanisms to serialize access to shared resources across nodes | Use for preventing race conditions in distributed apps
CODE-10-003 | Eventual Consistency and CRDTs | Data models that converge without coordination | Use for highly available, partition‑tolerant stores
CODE-10-004 | Message Passing vs Shared Memory | Communication paradigms in distributed computing | Use when choosing IPC model for performance/programmability
CODE-10-005 | Remote Procedure Call (RPC) and gRPC | Invoking procedures on remote machines as if local | Use for building microservices and APIs
CODE-10-006 | Publish/Subscribe Messaging (MQTT, Kafka) | Decoupled messaging where producers broadcast to subscribers | Use for event streaming, IoT telemetry, log aggregation
CODE-10-007 | Fault Tolerance and Replication Strategies | Techniques to maintain service despite node failures | Use to achieve high availability and durability
CODE-10-008 | Load Balancing and Service Discovery | Distributing workload and locating service instances dynamically | Use for scaling and resilience in cloud environments
CODE-10-009 | Distributed File Systems (GFS, HDFS) | File storage spread across many machines with fault tolerance | Use for big data processing and archival
CODE-10-010 | Blockchain and Distributed Ledger Technology | Append‑only, tamper‑evident chains maintained by peers | Use for trustless transactions, smart contracts, provenance
CODE-10-011 | Edge Computing and Fog Computing | Processing data near the source to reduce latency | Use for real‑time analytics, AR/VR, industrial IoT
CODE-10-012 | Serverless Computing (FaaS) | Running code in response to events without managing servers | Use for variable workloads, rapid prototyping, cost efficiency
CODE-10-013 | Distributed Tracing and Observability | Instrumentation to monitor requests across services | Use for debugging performance bottlenecks and failures

## 11 Security and Cryptography
CODE-11-001 | Symmetric Encryption (AES, DES, ChaCha20) | Ciphers using the same secret key for encryption and decryption | Use for bulk data encryption where speed matters
CODE-11-002 | Asymmetric Encryption (RSA, ECC, ElGamal) | Public‑key schemes enabling secure key exchange and signatures | Use for establishing secure channels and authentication
CODE-11-003 | Hash Functions and Message Authentication Codes (HMAC) | One‑way functions providing integrity and authenticity | Use for password storage, message verification, deduplication
CODE-11-004 | Digital Signatures and Certificates | Cryptographic proofs of origin bound to public keys via PKI | Use for software signing, TLS, legal non‑repudiation
CODE-11-005 | Key Management and PKI | Lifecycle handling of cryptographic keys and certificates | Use to prevent key leakage and ensure trust chains
CODE-11-006 | Secure Protocols (TLS, SSH, IPsec) | Protocol suites securing communication channels | Use for web, remote login, and VPN protection
CODE-11-007 | Authentication Mechanisms (Passwords, OTP, Biometrics) | Methods verifying claimed identity | Use for access control to systems and data
CODE-11-008 | Authorization Models (RBAC, ABAC, MAC) | Policies determining what authenticated users may do | Use to enforce least privilege and data segregation
CODE-11-009 | Intrusion Detection and Prevention Systems (IDS/IPS) | Sensors that spot and block malicious activity | Use for network and host‑based threat mitigation
CODE-11-010 | Secure Software Development (SDL, Threat Modeling) | Practices integrating security throughout the SDLC | Use to reduce vulnerabilities before deployment
CODE-11-011 | Privacy‑Preserving Techniques (Differential Privacy, Homomorphic Encryption) | Methods enabling analysis without exposing raw data | Use for compliant data sharing and secure computation
CODE-11-012 | Hardware Security Modules (TPM, HSM, SGX) | Tamper‑resistant devices protecting keys and crypto ops | Use for securing credentials, DRM, cloud workloads
CODE-11-013 | Post‑Quantum Cryptography | Algorithms resistant to quantum computer attacks | Use to future‑proof security against quantum threats

## 12 Emerging Computing Paradigms
CODE-12-001 | Quantum Computing Basics (Qubits, Gates) | Fundamentals of qubits, superposition, entanglement, and quantum gates | Use when exploring quantum advantage research
CODE-12-002 | Quantum Algorithms (Shor, Grover) | Algorithms offering exponential or quadratic speedups | Use for factoring, search, and quantum simulation
CODE-12-003 | Quantum Error Correction | Techniques to protect quantum information from decoherence | Use for building fault‑tolerant quantum computers
CODE-12-004 | Neuromorphic Computing | Hardware mimicking neural architectures for low‑power AI | Use for event‑driven, sensory‑processing workloads
CODE-12-005 | Approximate Computing | Trading accuracy for performance or energy efficiency | Use when results can tolerate bounded error
CODE-12-006 | DNA and Molecular Computing | Using biochemical reactions to perform computation | Use for massive parallelism in niche domains
CODE-12-007 | Optical and Photonic Computing | Computing with light instead of electrons for speed | Use for high‑bandwidth signal processing and AI accelerators
CODE-12-008 | Reversible Computing | Computation models where operations are invertible, reducing energy loss | Use for ultra‑low‑power and quantum‑compatible designs
CODE-12-009 | High‑Performance Computing (HPC) and GPUs | Leveraging massive parallelism for scientific simulations | Use for climate modeling, molecular dynamics, AI training
CODE-12-010 | FPGA‑Based Acceleration | Reconfigurable hardware tailoring pipelines to specific workloads | Use for low‑latency trading, prototyping, custom data paths
CODE-12-011 | Edge AI Chips and TPUs | Specialized processors optimizing inference at the edge | Use for real‑time vision, speech, and robotics
CODE-12-012 | Bio‑Inspired Algorithms (Ant Colony, Particle Swarm) | Optimization methods mimicking natural collective behavior | Use for combinatorial problems where gradients unavailable
CODE-12-013 | Exascale Computing and Future Directions | Pursuit of 10^18 operations per second and beyond | Use when planning next‑generation scientific infrastructure |
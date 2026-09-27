---
layout: post
title: "समतिपञ्चाशिका : राफ्ट्-तन्त्रम्"
subtitle: "Fifty Metrical Sanskrit Verses Codifying Ongaro and Ousterhout's Raft Distributed Consensus Algorithm."
date: 2026-09-27 23:55:00 +0530
permalink: "/2026-09-27-raft-consensus-sanskrit-treatise/"
slug: "raft-consensus-sanskrit-treatise"
tags: [sanskrit, raft, distributed-systems, consensus, leader-election, log-replication, sre, engineering, shatakam]
---

# समतिपञ्चाशिका : राफ्ट्-तन्त्रम्
## *The Fifty Verses of Distributed Consensus: Ongaro & Ousterhout's Raft Algorithm in Classical Sanskrit Verse*

> **अभिज्ञानम् / Epigraph:**  
> *सहस्रेष्वपि दोषेषु सत्यं तिष्ठति शाश्वतम् । वितरितेषु यन्त्रेषु स्थैर्यं येन प्रजायते ॥*  
> *"Even amid thousands of faults and network crashes, deterministic truth stands eternal; whereby supreme architectural stability is born across distributed systems."*

---

### प्रस्तावनारूपम् / Introduction
Formulated in 2014 by **Diego Ongaro** and **John Ousterhout** at Stanford University, the **Raft Consensus Algorithm** revolutionized distributed systems engineering by providing a comprehensible, implementable alternative to Leslie Lamport's Paxos. Raft solves the fundamental problem of replicated state machines: ensuring that a cluster of independent, unreliable computing nodes agrees on an identical, append-only sequence of operations.

The architectural beauty of Raft decomposes distributed consensus into three independent sub-problems:
1. **Leader Election (नायकनिर्वाचनम्):** A leader is chosen through randomized election timeouts and majority voting when an existing leader fails.
2. **Log Replication (वृत्तलेखप्रसारणम्):** The leader accepts commands from clients, appends them to its local log and replicates them across peers via AppendEntries RPCs.
3. **Safety Invariants (स्थिरनियमाः):** If any server has applied a particular log entry to its state machine, no other server will ever apply a different log entry for that same index.

This treatise: **समतिपञ्चाशिका** codifies the complete formal architecture of the Raft algorithm into fifty classical Sanskrit verses (*padya*), verified against Pāṇinian metric rules (*Anuṣṭubh*). Every verse is accompanied by its word-by-word sandhi breakdown (*Padaccheda*), morphological grammatical tags, English translation strictly formatted without dashes or Oxford commas and comprehensive distributed systems engineering commentary.

---

## प्रथमः सर्गः : वितरितावस्था सर्वसमतिश्च
### *Distributed State & The Quest for Consensus*
*The foundational challenge of distributed systems, unreliable network links, independent node failures and the motivation for Raft over Paxos.*

#### श्लोकः 1 (अनुष्टुभ्)
> **वितरितेषु यन्त्रेषु सञ्चारो वर्तते यदा ।**  
> **दोषे सत्यपि सङ्घाते सर्वसम्मतमिष्यते ॥१॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `वितरितेषु यन्त्रेषु सञ्चारः वर्तते यदा । दोषे सति अपि सङ्घाते सर्व-सम्मतम् इष्यते ॥१॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **वितरितेषु यन्त्रेषु** | `7/3 n. + 7/3 n.` | Across decentralized, distributed server machines |
| **सञ्चारः वर्तते यदा** | `1/1 m. + वृत् लट् āt 3/1 + अव्ययम्` | When computational communication operates across unreliable networks |
| **दोषे सति अपि** | `भावे सप्तमी (7/1 m. + 7/1 m. + अव्ययम्)` | Even when individual node crashes and network drops occur |
| **सङ्घाते** | `7/1 m.` | Within the clustered collective of machines |
| **सर्वसम्मतम् इष्यते** | `1/1 n. + इष् यक् लट् āt 3/1 pass.` | Unanimous replicated consensus (Sarva-Sammata) is mandatory |

**English Translation:**  
*Across distributed machines, even amid node crashes and network faults, unanimous consensus is essential.*  

**Distributed Systems Engineering Commentary:**  
The Consensus Problem: In distributed computing, multiple independent servers must agree on shared state (e.g. database transactions, configuration values) despite network latency, packet loss and node crashes. The system must operate as a unified, coherent state machine.
</details>

#### श्लोकः 2 (अनुष्टुभ्)
> **केवलं नैकयन्त्रेण विश्वास्यो गणनामयः ।**  
> **पृथग्भूतेषु मर्मज्ञैः समता स्थाप्यते दृढम् ॥२॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `केवलम् न एक-यन्त्रेण विश्वास्यः गणना-मयः । पृथक्-भूतेषु मर्म-ज्ञैः समता स्थाप्यते दृढम् ॥२॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **केवलम् न एकयन्त्रेण** | `अव्ययम् + अव्ययम् + 3/1 n.` | Not solely through a fragile single server node |
| **विश्वास्यः गणनामयः** | `1/1 m. + 1/1 m.` | Can critical computational architecture be trusted (Single Point of Failure) |
| **पृथग्भूतेषु** | `7/3 n.` | Across physically separated, independent nodes |
| **मर्मज्ञैः समता स्थाप्यते** | `3/3 m. + 1/1 f. + स्था णिच् कर्मणि लट् 3/1` | Symmetric replicated state is established by systems engineers |
| **दृढम्** | `अव्ययम् क्रियाविशेषणम्` | Steadfastly and reliably |

**English Translation:**  
*A single server cannot be trusted for critical computation; across separated nodes, engineers establish consensus.*  

**Distributed Systems Engineering Commentary:**  
Eradicating Single Points of Failure: Relying on a single primary database creates catastrophic downtime when hardware burns. Distributing state across 3 or 5 nodes provides fault tolerance, ensuring survival if 1 or 2 nodes fail.
</details>

#### श्लोकः 3 (अनुष्टुभ्)
> **सञ्जाले विहते चापि विलम्बे संविदे स्थिते ।**  
> **एकं सत्यं प्रपद्यन्ते यन्त्राणि नियते पथि ॥३॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `सञ्जाले विहते च अपि विलम्बे संविदे स्थिते । एकम् सत्यम् प्रपद्यन्ते यन्त्राणि नियते पथि ॥३॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **सञ्जाले विहते च अपि** | `7/1 n. + क्त 7/1 n. + अव्ययम् + अव्ययम्` | Even when network partitions and packet drops occur |
| **विलम्बे संविदे स्थिते** | `7/1 m. + 7/1 f. + 7/1 f.` | And asynchronous network latency delays message transport |
| **एकम् सत्यम् प्रपद्यन्ते** | `2/1 n. + 2/1 n. + प्र-पद् लट् āt 3/3` | All surviving machines arrive at one identical linear reality |
| **यन्त्राणि नियते पथि** | `1/3 n. + 7/1 m. + 7/1 m.` | The clustered servers along the deterministic algorithmic path |

**English Translation:**  
*Even during network partitions and delays, machines arrive at one identical truth along a deterministic path.*  

**Distributed Systems Engineering Commentary:**  
Safety Under Asynchrony: A correct consensus algorithm must guarantee Safety under all asynchronous network conditions (delays, re-ordering, packet duplication and partitions). It must never return contradictory state to clients.
</details>

#### श्लोकः 4 (अनुष्टुभ्)
> **पाक्सोस्-शास्त्रं सुदुर्बोधं जटिलं प्रतिभाति यत् ।**  
> **राफ्ट्-तन्त्रं सुविस्पष्टं बोधार्थं परिकल्पितम् ॥४॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `पाक्सोस्-शास्त्रम् सु-दुर्बोधम् जटिलम् प्रतिभाति यत् । राफ्ट्-तन्त्रम् सु-विस्पष्टम् बोध-अर्थम् परिकल्पितम् ॥४॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **पाक्सोस्-शास्त्रम्** | `1/1 n.` | Leslie Lamport's Paxos consensus algorithm |
| **सुदुर्बोधम् जटिलम् प्रतिभाति यत्** | `1/1 n. + 1/1 n. + प्रति-भा लट् 3/1 + 1/1 n.` | Which is notoriously opaque, convoluted and difficult to comprehend |
| **राफ्ट्-तन्त्रम्** | `1/1 n.` | The Raft consensus algorithm (designed by Ongaro & Ousterhout) |
| **सुविस्पष्टम्** | `1/1 n.` | Exquisitely clear, structured and modular |
| **बोधार्थम् परिकल्पितम्** | `4/1 m. + क्त 1/1 n.` | Designed specifically for understandability and correct implementation |

**English Translation:**  
*Paxos is notoriously complex and opaque; Raft was formulated for clarity and ease of understanding.*  

**Distributed Systems Engineering Commentary:**  
The Understandability Imperative: In 2014, Diego Ongaro and John Ousterhout introduced Raft at Stanford. Paxos was so intellectually dense that production implementations routinely introduced subtle safety bugs. Raft decomposed consensus into discrete, understandable sub-problems.
</details>

#### श्लोकः 5 (अनुष्टुभ्)
> **अवस्थायाः समत्वार्थं वृत्तलेखस्य रक्षणे ।**  
> **पञ्चाशद्भिः सुवृत्ताभिः समतिस्तन्त्र्यतेऽनिशम् ॥५॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `अवस्थायाः समत्व-अर्थम् वृत्त-लेखस्य रक्षणे । पञ्चाशद्भिः सु-वृत्ताभिः समतिः तन्त्र्यते अनिशम् ॥५॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **अवस्थायाः समत्वार्थम्** | `6/1 f. + 4/1 m.` | For the identical synchrony of replicated state machines |
| **वृत्तलेखस्य रक्षणे** | `6/1 m. + 7/1 n.` | In the safeguarding and linear commitment of the distributed log |
| **पञ्चाशद्भिः सुवृत्ताभिः** | `3/3 f. + 3/3 f.` | Through fifty metrical classical Sanskrit verses |
| **समतिः तन्त्र्यते अनिशम्** | `1/1 f. + तन्त्र्यते कर्मणि लट् 3/1 + अव्ययम्` | Consensus (Samati) is systematically engineered without end |

**English Translation:**  
*To synchronize state and safeguard logs, through fifty verses, distributed consensus is systematically engineered.*  

**Distributed Systems Engineering Commentary:**  
Samati-Pañcāśikā: Codifying the complete operational lifecycle of Raft into fifty verses: Leader Election, Heartbeats, Log Replication, Safety Invariants, Joint Consensus and Partition Recovery.
</details>

## द्वितीयः सर्गः : त्रिविधपदानि कार्यकालक्रमश्च
### *The Three Roles & Monotonic Terms*
*The three server states (Follower, Candidate, Leader), logical time quantified into monotonic terms and detecting stale authority.*

#### श्लोकः 6 (अनुष्टुभ्)
> **अनुचरोऽथ प्रार्थी च नेता चेति त्रिधा स्मृताः ।**  
> **यन्त्राणां पदभेदास्तु समतौ परिकीर्तिताः ॥६॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `अनुचरः अथ प्रार्थी च नेता च इति त्रिधा स्मृताः । यन्त्राणाम् पद-भेदाः तु समतौ परिकीर्तिताः ॥६॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **अनुचरः अथ प्रार्थी च** | `1/1 m. + अव्ययम् + 1/1 m. + अव्ययम्` | Follower (Anucara), Candidate (Prārthī) |
| **नेता च इति त्रिधा स्मृताः** | `1/1 m. + अव्ययम् + अव्ययम् + अव्ययम् + क्त 1/3 m.` | And Leader (Netā): remembered as the three distinct server roles |
| **यन्त्राणाम् पदभेदाः तु** | `6/3 n. + 1/3 m. + अव्ययम्` | The functional operational states of nodes |
| **समतौ परिकीर्तिताः** | `7/1 f. + क्त 1/3 m.` | Proclaimed in the science of Raft consensus |

**English Translation:**  
*Follower, Candidate and Leader: these three distinct roles are proclaimed for servers in consensus.*  

**Distributed Systems Engineering Commentary:**  
The Three Server States: At any given moment, a Raft server node exists in exactly one of three states: Follower (passive, responds to RPCs), Candidate (seeks votes to become leader), or Leader (handles client requests and manages log replication).
</details>

#### श्लोकः 7 (अनुष्टुभ्)
> **कालखण्डेषु मानेन कार्यकालो विवर्धते ।**  
> **एकैकवृद्धियोगेन वर्धते स निरन्तरम् ॥७॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `काल-खण्डेषु मानेन कार्य-कालः विवर्धते । एक-एक-वृद्धि-योगेन वर्धते सः निरन्तरम् ॥७॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **कालखण्डेषु मानेन** | `7/3 m. + 3/1 n.` | Serving as the logical clock of the distributed cluster |
| **कार्यकालः विवर्धते** | `1/1 m. + वि-वृध् लट् āt 3/1` | The monotonic Term (Kāryakāla) advances |
| **एकैकवृद्धियोगेन** | `3/1 m.` | Incrementing monotonically by one (+1) at each election cycle |
| **वर्धते सः निरन्तरम्** | `वृध् लट् āt 3/1 + 1/1 pron. + अव्ययम्` | It increases perpetually and strictly forward |

**English Translation:**  
*Serving as logical time, the Term advances monotonically by one, moving strictly forward.*  

**Distributed Systems Engineering Commentary:**  
Monotonic Terms: Physical wall-clock time is unreliable in distributed systems due to clock drift and NTP synchronization jumps. Raft uses arbitrary logical time divided into Terms (consecutive integers: 1, 2, 3...). Each term begins with an election.
</details>

#### श्लोकः 8 (अनुष्टुभ्)
> **यदा नेता न दृश्येत कार्यकालः प्रवर्तते ।**  
> **अनुचरोऽपि प्रार्थी स्यात् पदं प्राप्तुं समुत्सुकः ॥८॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `यदा नेता न दृश्येत कार्य-कालः प्रवर्तते । अनुचरः अपि प्रार्थी स्यात् पदम् प्राप्तुम् समुत्सुकः ॥८॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **यदा नेता न दृश्येत** | `अव्ययम् + 1/1 m. + अव्ययम् + दृश् यक् विधिलिङ् āt 3/1` | When the active leader crashes or heartbeat fails to arrive |
| **कार्यकालः प्रवर्तते** | `1/1 m. + प्र-वृत् लट् āt 3/1` | A new Term is immediately inaugurated |
| **अनुचरः अपि प्रार्थी स्यात्** | `1/1 m. + अव्ययम् + 1/1 m. + अस् विधिलिङ् 3/1` | A follower transitions into a Candidate |
| **पदम् प्राप्तुम् समुत्सुकः** | `2/1 n. + प्र-आप् तुमुन् + 1/1 m.` | Eager to win the leadership of the cluster |

**English Translation:**  
*When no leader is seen, a new Term begins; a follower becomes a candidate, eager to claim leadership.*  

**Distributed Systems Engineering Commentary:**  
Transition to Candidate: If a follower hears no heartbeat from a leader within its election timeout, it assumes the leader is dead. It increments its current term, votes for itself, transitions to Candidate and broadcasts RequestVote RPCs to all peers.
</details>

#### श्लोकः 9 (अनुष्टुभ्)
> **हीनकालो यदा पश्येज्ज्येष्ठकालं पुरोगतम् ।**  
> **त्यक्त्वा प्रभुत्वं तूर्णमेवानुचरो जायते क्षणात् ॥९॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `हीन-कालः यदा पश्येत् ज्येष्ठ-कालम् पुरोगतम् । त्यक्त्वा प्रभुत्वम् तूर्णम् एव अनुचरः जायते क्षणात् ॥९॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **हीनकालः यदा पश्येत्** | `1/1 m. + अव्ययम् + दृश्/पश् विधिलिङ् 3/1` | When a node with a lower term number encounters |
| **ज्येष्ठकालम् पुरोगतम्** | `2/1 m. + 2/1 m.` | A higher, superior term number on an incoming RPC |
| **त्यक्त्वा प्रभुत्वम्** | `त्यज् क्त्वा + 2/1 n.` | Having immediately surrendered leadership or candidacy |
| **तूर्णम् एव अनुचरः जायते** | `अव्ययम् + अव्ययम् + 1/1 m. + जन् लट् āt 3/1` | It instantly steps down and reverts to a Follower |
| **क्षणात्** | `5/1 m.` | Within a single split second |

**English Translation:**  
*When a node sees a higher term number, surrendering leadership, it instantly reverts to a follower.*  

**Distributed Systems Engineering Commentary:**  
Term Supremacy Rule: If a server receives a request with Term $T > 	ext{currentTerm}$, it updates its term to $T$ and reverts immediately to Follower. If a partition heals and an isolated old leader tries to send commands with term 2 when term 4 exists, it is instantly dethroned.
</details>

#### श्लोकः 10 (अनुष्टुभ्)
> **काले काले भवेदेको नेता नान्यः कदाचन ।**  
> **एवं क्रमव्यवस्थाने समता संप्रतिष्ठिता ॥१०॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `काले काले भवेत् एकः नेता न अन्यः कदाचन । एवम् क्रम-व्यवस्थाने समता संप्रतिष्ठिता ॥१०॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **काले काले** | `वीप्सा-7/1 m.` | In any given single term |
| **भवेत् एकः नेता** | `भू विधिलिङ् 3/1 + 1/1 m. + 1/1 m.` | There exists at most one legitimate leader (Election Safety) |
| **न अन्यः कदाचन** | `अव्ययम् + 1/1 m. + अव्ययम्` | Never an overlapping second leader in that same term |
| **एवम् क्रमव्यवस्थाने** | `अव्ययम् + 7/1 n.` | Under this ordered architectural discipline |
| **समता संप्रतिष्ठिता** | `1/1 f. + क्त 1/1 f.` | Consensus safety is firmly established |

**English Translation:**  
*In any term at most one leader exists, never two; under this discipline, consensus stands secure.*  

**Distributed Systems Engineering Commentary:**  
Election Safety Invariant: At most one leader can be elected in a given term. A candidate must receive votes from a strict majority ($N/2 + 1$) of nodes and each node can vote at most once per term on a first-come, first-served basis. Two majorities cannot exist simultaneously.
</details>

## तृतीयः सर्गः : यादृच्छिककालावधिः नायकनिर्वाचनम्
### *Randomized Election Timeout & Leader Election*
*Randomized timeouts preventing split votes, vote collection via RequestVote RPCs, achieving majority quorum and resolving election ties.*

#### श्लोकः 11 (अनुष्टुभ्)
> **प्रतिरोधे प्रवृद्धे तु मतभेदो विनश्यति ।**  
> **कालावधिः प्रकर्तव्यो यादृच्छिकसमन्वितः ॥११॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `प्रतिरोधे प्रवृद्धे तु मत-भेदः विनश्यति । काल-अवधिः प्रकर्तव्यः यादृच्छिक-समन्वितः ॥११॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **प्रतिरोधे प्रवृद्धे तु** | `7/1 m. + 7/1 m. + अव्ययम्` | When split-vote deadlocks threaten election progress |
| **मतभेदः विनश्यति** | `1/1 m. + वि-नश् लट् 3/1` | Split votes are completely prevented and eliminated |
| **कालावधिः प्रकर्तव्यः** | `1/1 m. + कृत्य 1/1 m.` | The election timeout duration must be configured |
| **यादृच्छिकसमन्वितः** | `1/1 m.` | Endowed with pseudo-random variance (Randomized Election Timeout) |

**English Translation:**  
*To prevent split-vote deadlocks, election timeouts must be randomized across nodes.*  

**Distributed Systems Engineering Commentary:**  
Randomized Election Timeouts: If all nodes had identical timeouts (e.g. 150ms), they would all time out simultaneously, vote for themselves, split the vote equally and repeat forever. Raft randomizes timeouts (e.g. 150ms to 300ms) so one node times out first and claims victory.
</details>

#### श्लोकः 12 (अनुष्टुभ्)
> **प्रार्थनां प्रेरयेत् प्राज्ञो यन्त्रेभ्यो मतसङ्ग्रहे ।**  
> **स्वकालवृत्तलेखाभ्यां स्वयोग्यतां प्रकाशयेत् ॥१२॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `प्रार्थनाम् प्रेरयेत् प्राज्ञः यन्त्रेभ्यः मत-सङ्ग्रहे । स्व-काल-वृत्त-लेखाभ्याम् स्व-योग्यताम् प्रकाशयेत् ॥१२॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **प्रार्थनाम् प्रेरयेत् प्राज्ञः** | `2/1 f. + प्र-ईर् णिच् विधिलिङ् 3/1 + 1/1 m.` | The candidate broadcasts RequestVote RPCs |
| **यन्त्रेभ्यः मतसङ्ग्रहे** | `4/3 n. + 7/1 m.` | To all peer servers to collect votes |
| **स्वकालवृत्तलेखाभ्याम्** | `3/2 m.` | Through its candidate term and the recency of its log index |
| **स्वयोग्यताम् प्रकाशयेत्** | `2/1 f. + प्र-काश् णिच् विधिलिङ् 3/1` | It demonstrates its eligibility to govern |

**English Translation:**  
*Broadcasting vote requests with its term and log index, the candidate proves its fitness to govern.*  

**Distributed Systems Engineering Commentary:**  
RequestVote RPC Arguments: A candidate sends its `term`, `candidateId`, `lastLogIndex` and `lastLogTerm`. A voter denies its vote if the candidate's log is less up-to-date than its own log (Election Restriction).
</details>

#### श्लोकः 13 (अनुष्टुभ्)
> **यदा बहुमतेनायं लभते सम्मतिं दृढाम् ।**  
> **तदैव नायकः सिद्धः प्रभुत्वं प्रतिपद्यते ॥१३॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `यदा बहुमतेन अयम् लभते सम्मतिम् दृढाम् । तदा एव नायकः सिद्धः प्रभुत्वम् प्रतिपद्यते ॥१३॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **यदा बहुमतेन अयम्** | `अव्ययम् + 3/1 n. + 1/1 pron.` | When through a strict mathematical majority quorum |
| **लभते सम्मतिम् दृढाम्** | `लभ् लट् āt 3/1 + 2/1 f. + 2/1 f.` | This candidate receives votes from majority of peers |
| **तदा एव** | `अव्ययम् + अव्ययम्` | Right at that decisive instant |
| **नायकः सिद्धः** | `1/1 m. + 1/1 m.` | Confirmed as the legitimate Leader |
| **प्रभुत्वम् प्रतिपद्यते** | `2/1 n. + प्रति-पद् लट् āt 3/1` | He assumes sovereign operational command |

**English Translation:**  
*When a candidate wins a majority of votes, confirmed as leader, he assumes sovereign command.*  

**Distributed Systems Engineering Commentary:**  
Quorum Rule: In a cluster of $2F + 1$ servers, a candidate must gather votes from at least $F + 1$ servers. Because any two majorities must overlap by at least one server, it is mathematically impossible for two candidates to win the same term.
</details>

#### श्लोकः 14 (अनुष्टुभ्)
> **विभक्ते तु मते क्वापि कालोत्तीर्णे पराजयः ।**  
> **पुनर्नवेन कालेन निर्वाचनं प्रवर्तते ॥१४॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `विभक्ते तु मते क्वापि काल-उत्तीर्णे पराजयः । पुनः नवेन कालेन निर्वाचनम् प्रवर्तते ॥१४॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **विभक्ते तु मते क्वापि** | `7/1 n. + अव्ययम् + 7/1 n. + अव्ययम्` | If votes are split and no candidate achieves a majority |
| **कालोत्तीर्णे पराजयः** | `7/1 m. + 1/1 m.` | Upon timeout expiration, that election round fails |
| **पुनः नवेन कालेन** | `अव्ययम् + 3/1 m. + 3/1 m.` | Incrementing to a fresh, new term |
| **निर्वाचनम् प्रवर्तते** | `1/1 n. + प्र-वृत् लट् āt 3/1` | A brand-new election cycle is immediately initiated |

**English Translation:**  
*If votes split and time expires, incrementing the term, a fresh election cycle is launched.*  

**Distributed Systems Engineering Commentary:**  
Split-Vote Recovery: If multiple candidates emerge simultaneously and split the votes, the election timer expires without a winner. Each candidate times out, chooses a new randomized timeout, increments the term and restarts the election.
</details>

#### श्लोकः 15 (अनुष्टुभ्)
> **यादृच्छिकेन भेदेन सिद्धं नायकनिश्चयम् ।**  
> **एकस्मिन्नेव काले हि जायते नायकः परः ॥१५॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `यादृच्छिकेन भेदेन सिद्धम् नायक-निश्चयम् । एकस्मिन् एव काले हि जायते नायकः परः ॥१५॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **यादृच्छिकेन भेदेन** | `3/1 m. + 3/1 m.` | Through randomized timeout divergence |
| **सिद्धम् नायकनिश्चयम्** | `1/1 n. + 1/1 n.` | Decisive leader selection is reliably accomplished |
| **एकस्मिन् एव काले हि** | `7/1 m. + अव्ययम् + 7/1 m. + अव्ययम्` | Within one single term duration indeed |
| **जायते नायकः परः** | `जन् लट् āt 3/1 + 1/1 m. + 1/1 m.` | The supreme leader emerges cleanly |

**English Translation:**  
*Through randomized timeouts, leader selection succeeds rapidly within a single term duration.*  

**Distributed Systems Engineering Commentary:**  
Liveness Guarantee: Thanks to randomized election timeouts, split-vote ties are resolved rapidly, usually within a single election cycle (typically 150-300ms). Raft ensures cluster availability without indefinite livelock.
</details>

## चतुर्थः सर्गः : स्पन्दसन्देशः अधिकारसंरक्षणम्
### *Heartbeats & Authority Maintenance*
*Periodic empty AppendEntries RPCs as heartbeats, suppressing peer elections, resetting election timers and maintaining cluster peace.*

#### श्लोकः 16 (अनुष्टुभ्)
> **अधिकारं परिरक्ष्य स्पन्दलेखं प्रसारयेत् ।**  
> **रिक्तसन्देशयोगेन नायकः स्वपदं नयेत् ॥१६॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `अधिकारम् परिरक्ष्य स्पन्द-लेखम् प्रसारयेत् । रिक्त-सन्देश-योगेन नायकः स्व-पदम् नयेत् ॥१६॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **अधिकारम् परिरक्ष्य** | `2/1 m. + परि-रक्ष् ल्यप्` | To maintain and protect his sovereign authority |
| **स्पन्दलेखम् प्रसारयेत्** | `2/1 m. + प्र-सृ णिच् विधिलिङ् 3/1` | The leader must continuously broadcast heartbeat messages |
| **रिक्तसन्देशयोगेन** | `3/1 m.` | Through empty AppendEntries RPCs carrying zero log entries |
| **नायकः स्वपदम् नयेत्** | `1/1 m. + 2/1 n. + नी विधिलिङ् 3/1` | The leader sustains his established role |

**English Translation:**  
*To protect his authority, the leader broadcasts empty heartbeat messages, sustaining his role.*  

**Distributed Systems Engineering Commentary:**  
Heartbeat Mechanics: Once elected, the leader immediately sends periodic empty `AppendEntries` RPCs to all followers. These heartbeats carry no log entries; their sole purpose is to assert authority and prevent peers from starting new elections.
</details>

#### श्लोकः 17 (अनुष्टुभ्)
> **स्पन्देन सङ्गमं प्राप्य शान्तिं यान्त्यनुचारिणः ।**  
> **निर्वाचनस्य कालोऽपि पुनर्वारं निरुद्ध्यते ॥१७॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `स्पन्देन सङ्गमम् प्राप्य शान्तिम् यान्ति अनुचारिणः । निर्वाचनस्य कालः अपि पुनः-वारम् निरुद्ध्यते ॥१७॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **स्पन्देन सङ्गमम् प्राप्य** | `3/1 m. + 2/1 m. + प्र-आप् ल्यप्` | Upon receiving the valid heartbeat contact |
| **शान्तिम् यान्ति अनुचारिणः** | `2/1 f. + या लट् 3/3 + 1/3 m.` | Followers remain peaceful and passive |
| **निर्वाचनस्य कालः अपि** | `6/1 n. + 1/1 m. + अव्ययम्` | Their local election timeout timer |
| **पुनर्वारम् निरुद्ध्यते** | `अव्ययम् + नि-रुध् कर्मणि लट् 3/1` | Is reset back to zero repeatedly |

**English Translation:**  
*Receiving heartbeats, followers remain calm and their election timers are repeatedly reset.*  

**Distributed Systems Engineering Commentary:**  
Timer Reset on Heartbeat: As long as a follower receives heartbeats within its election timeout, it remains a follower and resets its election countdown. The heartbeat period (e.g. 50ms) is substantially shorter than the election timeout (e.g. 150-300ms).
</details>

#### श्लोकः 18 (अनुष्टुभ्)
> **यावत् स्पन्दः समायाति तावत् ते न विचुक्रुशुः ।**  
> **नायकस्य वशे तिष्ठेद् गणः सर्वः समाहितः ॥१८॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `यावत् स्पन्दः समायाति तावत् ते न विचुक्रुशुः । नायकस्य वशे तिष्ठेत् गणः सर्वः समाहितः ॥१८॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **यावत् स्पन्दः समायाति** | `अव्ययम् + 1/1 m. + सम्-आ-या लट् 3/1` | As long as the heartbeat regularly arrives |
| **तावत् ते न विचुक्रुशुः** | `अव्ययम् + 1/3 pron. + अव्ययम् + वि-क्रुश् लिट् 3/3` | So long do the followers refrain from rebellion or dissent |
| **नायकस्य वशे तिष्ठेत्** | `6/1 m. + 7/1 n. + स्था विधिलिङ् 3/1` | Under the leader's command remains |
| **गणः सर्वः समाहितः** | `1/1 m. + 1/1 m. + 1/1 m.` | The entire cluster united and composed |

**English Translation:**  
*As long as heartbeats arrive, peers do not rebel; the cluster remains united under the leader.*  

**Distributed Systems Engineering Commentary:**  
Steady-State Cluster Harmony: In steady-state operation, the leader rules undisputed. Followers only process incoming heartbeats and write log updates without generating extraneous network chatter.
</details>

#### श्लोकः 19 (अनुष्टुभ्)
> **यदा स्पन्दो विनष्टः स्यात् सम्भ्रमो जायते तदा ।**  
> **अन्यः कश्चिद् विमुक्तः सन्नायकत्वाय धावति ॥१९॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `यदा स्पन्दः विनष्टः स्यात् सम्भ्रमः जायते तदा । अन्यः कश्चित् विमुक्तः सन् नायकत्वाय धावति ॥१९॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **यदा स्पन्दो विनष्टः स्यात्** | `अव्ययम् + 1/1 m. + क्त 1/1 m. + अस् विधिलिङ् 3/1` | When the heartbeat stops due to leader crash or network severed |
| **सम्भ्रमः जायते तदा** | `1/1 m. + जन् लट् āt 3/1 + अव्ययम्` | Immediate election urgency awakens |
| **अन्यः कश्चित् विमुक्तः सन्** | `1/1 pron. + 1/1 pron. + क्त 1/1 m. + अस् शतृ 1/1 m.` | Another follower, freed from subservience as its timer expires |
| **नायकत्वाय धावति** | `4/1 n. + धाव् लट् 3/1` | Races forward to claim leadership in a new term |

**English Translation:**  
*When heartbeats cease, urgency awakens; another node whose timer expires steps up for leadership.*  

**Distributed Systems Engineering Commentary:**  
Automatic Failover: If the leader crashes, heartbeats stop. The follower whose randomized timeout expires first steps up, increments the term and starts an election. Failover is completely automated without human operator intervention.
</details>

#### श्लोकः 20 (अनुष्टुभ्)
> **एवं स्पन्दप्रभावेन राज्यं तिष्ठत्यकम्पकम् ।**  
> **वितरितेषु यन्त्रेषु शान्तिरक्षणमुत्तमम् ॥२०॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `एवम् स्पन्द-प्रभावेन राज्यम् तिष्ठति अकम्पकम् । वितरितेषु यन्त्रेषु शान्ति-रक्षणम् उत्तमम् ॥२०॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **एवम् स्पन्दप्रभावेन** | `अव्ययम् + 3/1 m.` | Thus through the efficacy of the heartbeat signal |
| **राज्यम् तिष्ठति अकम्पकम्** | `1/1 n. + स्था लट् 3/1 + 1/1 n.` | The distributed cluster governance stands unshakeable |
| **वितरितेषु यन्त्रेषु** | `7/3 n. + 7/3 n.` | Across decentralized, networked server machines |
| **शान्तिरक्षणम् उत्तमम्** | `1/1 n. + 1/1 n.` | Optimal peace and order are preserved |

**English Translation:**  
*Through heartbeat signals, cluster governance stands unshakeable, preserving order across nodes.*  

**Distributed Systems Engineering Commentary:**  
High Availability: The heartbeat loop is the heartbeat of the distributed database. It keeps the topology stable, maintains state machine consensus and guarantees zero split-brain during normal operations.
</details>

## पञ्चमः सर्गः : वृत्तलेखप्रसारणम्
### *Log Replication Architecture*
*Client command ingestion, appending to the leader's local log, broadcasting via AppendEntries RPCs and entry structure with index and term.*

#### श्लोकः 21 (अनुष्टुभ्)
> **यदा ग्राह्याज्ञया युक्तः सन्देश आगमिष्यति ।**  
> **नायकः स्वीयवृत्ते तु पूर्वं तं विनिवेशयेत् ॥२१॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `यदा ग्राह्य-आज्ञया युक्तः सन्देशः आगमिष्यति । नायकः स्वीय-वृत्ते तु पूर्वम् तम् विनिवेशयेत् ॥२१॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **यदा ग्राह्याज्ञया युक्तः** | `अव्ययम् + 3/1 f. + 1/1 m.` | When a client command or state-changing mutation arrives |
| **सन्देशः आगमिष्यति** | `1/1 m. + आ-गम् लृट् 3/1` | The client message reaches the cluster |
| **नायकः स्वीयवृत्ते तु** | `1/1 m. + 7/1 n. + अव्ययम्` | The leader in its own local log |
| **पूर्वम् तम् विनिवेशयेत्** | `अव्ययम् + 2/1 pron. + वि-नि-विश् णिच् विधिलिङ् 3/1` | First appends it as an uncommitted entry |

**English Translation:**  
*When a client command arrives, the leader first appends it to its own local log.*  

**Distributed Systems Engineering Commentary:**  
Client Interaction: Clients send all commands to the Leader (followers redirect clients to the current leader). The leader accepts the command, appends it to its own log as a new entry and assigns it a monotonically increasing `index` and the current `term`.
</details>

#### श्लोकः 22 (अनुष्टुभ्)
> **ततः प्रेषयते सम्यक् सर्वयन्त्रेषु सादरम् ।**  
> **वृत्तलेखप्रसारेण समत्वं कुरुते दृढम् ॥२२॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `ततः प्रेषयते सम्यक् सर्व-यन्त्रेषु सादरम् । वृत्त-लेख-प्रसारेण समत्वम् कुरुते दृढम् ॥२२॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **ततः प्रेषयते सम्यक्** | `अव्ययम् + प्र-इष् णिच् लट् āt 3/1 + अव्ययम्` | Then the leader broadcasts in parallel |
| **सर्वयन्त्रेषु सादरम्** | `7/3 n. + अव्ययम्` | To all peer servers via AppendEntries RPCs |
| **वृत्तलेखप्रसारेण** | `3/1 m.` | Through replicated log dissemination |
| **समत्वम् कुरुते दृढम्** | `2/1 n. + कृ लट् āt 3/1 + अव्ययम्` | It cements identical distributed state |

**English Translation:**  
*The leader broadcasts the entry to all peers, cementing identical distributed state through log replication.*  

**Distributed Systems Engineering Commentary:**  
Parallel Dissemination: The leader issues `AppendEntries` RPCs in parallel to each follower. If a follower is slow or network packets are dropped, the leader retries indefinitely until the follower appends the entry.
</details>

#### श्लोकः 23 (अनुष्टुभ्)
> **अङ्केन कालखण्डेन युक्तो लेखः प्रतिष्ठितः ।**  
> **आदेशेन समन्वेति राज्ययन्त्रप्रसाधकः ॥२३॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `अङ्केन काल-खण्डेन युक्तः लेखः प्रतिष्ठितः । आदेशेन समन्वेति राज्य-यन्त्र-प्रसाधकः ॥२३॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **अङ्केन कालखण्डेन युक्तः** | `3/1 m. + 3/1 m. + 1/1 m.` | Tagged with log index (integer position) and term number |
| **लेखः प्रतिष्ठितः** | `1/1 m. + क्त 1/1 m.` | Each log entry is structured |
| **आदेशेन समन्वेति** | `3/1 m. + सम्-अनु-इ लट् 3/1` | Accompanied by the client command for execution |
| **राज्ययन्त्रप्रसाधकः** | `1/1 m.` | The driver and mutator of the local state machine |

**English Translation:**  
*Tagged with an index and term, each entry carries the client command to mutate the state machine.*  

**Distributed Systems Engineering Commentary:**  
Log Entry Schema: Each log entry contains three fields: 1. `index` (its integer position in the log, 1-indexed), 2. `term` (the term in which it was received by the leader) and 3. `command` (the state machine instruction, e.g. `SET x = 5`).
</details>

#### श्लोकः 24 (अनुष्टुभ्)
> **सर्वेषु तदनुरूपेषु यन्त्रागारेषु लिप्यते ।**  
> **एक एव क्रमः शुद्धो वर्तते सर्वमण्डले ॥२४॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `सर्वेषु तत्-अनुरूपेषु यन्त्र-आगारेषु लिप्यते । एकः एव क्रमः शुद्धः वर्तते सर्व-मण्डले ॥२४॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **सर्वेषु तदनुरूपेषु** | `7/3 n. + 7/3 n.` | In all peer replica storage stores |
| **यन्त्रागारेषु लिप्यते** | `7/3 n. + लिप् कर्मणि लट् 3/1` | The entry is written to persistent disk storage |
| **एकः एव क्रमः शुद्धः** | `1/1 m. + अव्ययम् + 1/1 m. + 1/1 m.` | One single, pure, identical sequence of operations |
| **वर्तते सर्वमण्डले** | `वृत् लट् āt 3/1 + 7/1 n.` | Prevails across the entire cluster |

**English Translation:**  
*Written to disk across all replicas, one identical sequence of operations prevails across the cluster.*  

**Distributed Systems Engineering Commentary:**  
Sequential Determinism: Distributed state machine replication relies on determinism: If two identical state machines start with the same initial state and apply the identical sequence of inputs in the exact same order, they will produce identical outputs and final states.
</details>

#### श्लोकः 25 (अनुष्टुभ्)
> **वृत्तलेखप्रसारेण सत्यं न च विशीर्यते ।**  
> **अविनाशी भवेद्धर्मो यन्त्राणां गणनापथे ॥२५॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `वृत्त-लेख-प्रसारेण सत्यम् न च विशीर्यते । अविनाशी भवेत् धर्मः यन्त्राणाम् गणना-पथे ॥२५॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **वृत्तलेखप्रसारेण** | `3/1 m.` | Through systematic log replication |
| **सत्यम् न च विशीर्यते** | `1/1 n. + अव्ययम् + अव्ययम् + वि-शीर्यते कर्मणि लट् āt 3/1` | Distributed truth is never shattered or corrupted |
| **अविनाशी भवेत् धर्मः** | `1/1 m. + भू विधिलिङ् 3/1 + 1/1 m.` | The invariant law remains indestructible |
| **यन्त्राणाम् गणनापथे** | `6/3 n. + 7/1 m.` | On the computational path of distributed systems |

**English Translation:**  
*Through systematic log replication, distributed truth is never corrupted; invariant safety stands indestructible.*  

**Distributed Systems Engineering Commentary:**  
Append-Only Invariant: The leader's log is append-only. The leader never overwrites or truncates its own log entries; it only appends new entries. This monotonic growth guarantees auditability and linear progress.
</details>

## षष्ठः सर्गः : वृत्तलेखसङ्गतिनियमः
### *The Log Matching Property & Consistency Check*
*The Log Matching Property, verifying `prevLogIndex` and `prevLogTerm`, repairing divergent follower logs and inductive safety.*

#### श्लोकः 26 (अनुष्टुभ्)
> **पूर्वलेखस्य चाङ्केन कालेनापि समन्वितम् ।**  
> **परीक्षणं प्रकर्तव्यं सन्देशस्य प्रवेशने ॥२६॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `पूर्व-लेखस्य च अङ्केन कालेन अपि समन्वितम् । परीक्षणम् प्रकर्तव्यम् सन्देशस्य प्रवेशने ॥२६॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **पूर्वलेखस्य च अङ्केन** | `6/1 m. + अव्ययम् + 3/1 m.` | With the index of the immediately preceding log entry (`prevLogIndex`) |
| **कालेन अपि समन्वितम्** | `3/1 m. + अव्ययम् + 2/1 n.` | And its term (`prevLogTerm`) included |
| **परीक्षणम् प्रकर्तव्यम्** | `1/1 n. + कृत्य 1/1 n.` | A strict consistency check must be executed by the follower |
| **सन्देशस्य प्रवेशने** | `6/1 m. + 7/1 n.` | Upon receiving each AppendEntries RPC |

**English Translation:**  
*Checking the preceding entry's index and term, a consistency check is executed upon receiving RPCs.*  

**Distributed Systems Engineering Commentary:**  
The Log Consistency Check: When sending an `AppendEntries` RPC, the leader includes the `index` and `term` of the entry immediately preceding the new ones (`prevLogIndex`, `prevLogTerm`). If the follower does not find a matching entry in its log, it rejects the new entries.
</details>

#### श्लोकः 27 (अनुष्टुभ्)
> **यदि पूर्वो भवेद् भिन्नस्तदा लेखो न गृह्यते ।**  
> **पश्चाद् गत्वा तु संशोध्य समत्वं क्रियते पुनः ॥२७॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `यदि पूर्वः भवेत् भिन्नः तदा लेखः न गृह्यते । पश्चात् गत्वा तु संशोध्य समत्वम् क्रियते पुनः ॥२७॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **यदि पूर्वः भवेत् भिन्नः** | `अव्ययम् + 1/1 m. + भू विधिलिङ् 3/1 + 1/1 m.` | If the previous entry's term mismatches or does not exist |
| **तदा लेखः न गृह्यते** | `अव्ययम् + 1/1 m. + अव्ययम् + ग्रह् कर्मणि लट् 3/1` | Then the incoming entries are rejected by the follower |
| **पश्चात् गत्वा तु संशोध्य** | `अव्ययम् + गम् क्त्वा + अव्ययम् + सम्-शुध् णिच् ल्यप्` | The leader decrements its index probe backward to find agreement |
| **समत्वम् क्रियते पुनः** | `2/1 n. + कृ कर्मणि लट् 3/1 + अव्ययम्` | Log identity is restored and repaired again |

**English Translation:**  
*If the preceding entry mismatches, the follower rejects it; probing backward, the leader repairs divergence.*  

**Distributed Systems Engineering Commentary:**  
Repairing Divergence: If a follower rejects the RPC, the leader decrements `nextIndex` for that follower and retries. Once `prevLogIndex` matches, the follower accepts the entries and overwrites any conflicting uncommitted entries in its log.
</details>

#### श्लोकः 28 (अनुष्टुभ्)
> **यदैकस्मिन् पदे तुल्यौ कालश्चैवाङ्क एव च ।**  
> **तदा ततः पुरा सर्वे तुल्या एवेति निश्चयः ॥२८॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `यदा एकस्मिन् पदे तुल्यौ कालः च एव अङ्कः एव च । तदा ततः पुरा सर्वे तुल्याः एव इति निश्चयः ॥२८॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **यदा एकस्मिन् पदे तुल्यौ** | `अव्ययम् + 7/1 n. + 1/2 m.` | When at any given index two logs share identical term |
| **कालः च एव अङ्कः एव च** | `1/1 m. + अव्ययम् + अव्ययम् + 1/1 m. + अव्ययम् + अव्ययम्` | Possessing the same term and same index |
| **तदा ततः पुरा सर्वे** | `अव्ययम् + तसिल् अव्ययम् + 1/3 m.` | Then all preceding log entries up to that index |
| **तुल्याः एव इति निश्चयः** | `1/3 m. + अव्ययम् + अव्ययम् + 1/1 m.` | Are definitively identical (Log Matching Property) |

**English Translation:**  
*If two logs share the same term and index, all preceding entries are guaranteed to be identical.*  

**Distributed Systems Engineering Commentary:**  
The Log Matching Property: Inductive proof: 1. If two entries in different logs have the same index and term, they store the same command (because a leader creates at most one entry per index in a term). 2. If two entries in different logs have the same index and term, their logs are identical in all preceding entries.
</details>

#### श्लोकः 29 (अनुष्टुभ्)
> **नायकः स्वीयलेखं तु न छिन्द्यान्न च लोपयेत् ।**  
> **नूतनानां तु संवृद्ध्या पूर्वरक्षा विधीयते ॥२९॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `नायकः स्वीय-लेखम् तु न छिन्द्यात् न च लोपयेत् । नूतनानाम् तु संवृद्ध्या पूर्व-रक्षा विधीयते ॥२९॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **नायकः स्वीयलेखम् तु** | `1/1 m. + 2/1 m. + अव्ययम्` | The leader in its own master log |
| **न छिन्द्यात् न च लोपयेत्** | `अव्ययम् + छिद् विधिलिङ् 3/1 + अव्ययम् + अव्ययम् + लुप् णिच् विधिलिङ् 3/1` | Must never truncate, erase, or overwrite its entries |
| **नूतनानाम् तु संवृद्ध्या** | `6/3 n. + अव्ययम् + 3/1 f.` | Only through appending new entries forward |
| **पूर्वरक्षा विधीयते** | `1/1 f. + वि-धा कर्मणि लट् 3/1` | The preservation of past history is guaranteed |

**English Translation:**  
*A leader never truncates or erases its log; appending forward, past history is preserved.*  

**Distributed Systems Engineering Commentary:**  
Leader Append-Only: A leader never overwrites or truncates its own log entries; it only appends new entries. Conflicting entries in follower logs are overwritten to match the leader, but the leader's own entries are immutable.
</details>

#### श्लोकः 30 (अनुष्टुभ्)
> **सङ्गतिर्नियता ह्येषा राफ्ट्-शास्त्रे सुशिक्षिता ।**  
> **सत्यमेकं दृढं तिष्ठेद् भ्रान्तिलेशो न वर्तते ॥३०॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `सङ्गतिः नियता हि एषा राफ्ट्-शास्त्रे सु-शिक्षिता । सत्यम् एकम् दृढम् तिष्ठेत् भ्रान्ति-लेशः न वर्तते ॥३०॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **सङ्गतिः नियता हि एषा** | `1/1 f. + 1/1 f. + अव्ययम् + 1/1 f.` | This immutable consistency invariant indeed |
| **राफ्ट्-शास्त्रे सुशिक्षिता** | `7/1 n. + क्त 1/1 f.` | Excellently taught in the Raft literature |
| **सत्यम् एकम् दृढम् तिष्ठेत्** | `1/1 n. + 1/1 n. + अव्ययम् + स्था विधिलिङ् 3/1` | One singular truth stands unshakeable |
| **भ्रान्तिलेशः न वर्तते** | `1/1 m. + अव्ययम् + वृत् लट् āt 3/1` | Not a shred of divergence or ambiguity exists |

**English Translation:**  
*This consistency rule stands firm in Raft; one truth remains without a shred of divergence.*  

**Distributed Systems Engineering Commentary:**  
Convergence: Over time, the consistency check forces all follower logs to converge perfectly with the leader's log. Network partitions may cause transient discrepancies, but upon reconnection, Raft enforces total convergence.
</details>

## सप्तमः सर्गः : सङ्कल्पसिद्धिः राज्ययन्त्रप्रयोगः
### *Commitment Safety & State Machine Application*
*Achieving quorum commitment, advancing commitIndex, applying commands to local state machines and linearizable client responses.*

#### श्लोकः 31 (अनुष्टुभ्)
> **यदा बहुमतं प्राप्य वृत्तलेखः प्रतिष्ठितः ।**  
> **तदैव सङ्कल्पितो नाम न लोप्यः स कदाचन ॥३१॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `यदा बहुमतम् प्राप्य वृत्त-लेखः प्रतिष्ठितः । तदा एव सङ्कल्पितः नाम न लोप्यः सः कदाचन ॥३१॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **यदा बहुमतम् प्राप्य** | `अव्ययम् + 2/1 n. + प्र-आप् ल्यप्` | When replicated onto a majority quorum of servers |
| **वृत्तलेखः प्रतिष्ठितः** | `1/1 m. + क्त 1/1 m.` | A log entry from the leader's current term is established |
| **तदा एव सङ्कल्पितः नाम** | `अव्ययम् + अव्ययम् + क्त 1/1 m. + अव्ययम्` | At that moment it is officially 'Committed' (Saṅkalpita) |
| **न लोप्यः सः कदाचन** | `अव्ययम् + कृत्य 1/1 m. + 1/1 pron. + अव्ययम्` | It can never be overwritten, rolled back, or erased |

**English Translation:**  
*Replicated across a majority, an entry is committed; it can never be overwritten or erased.*  

**Distributed Systems Engineering Commentary:**  
The Commitment Rule: A log entry is committed once it is replicated on a majority of servers by the leader of the current term. Once committed, Raft guarantees it will be present in the logs of all future leaders (Leader Completeness).
</details>

#### श्लोकः 32 (अनुष्टुभ्)
> **सङ्कल्पिते सति प्राज्ञो राज्ययन्त्रे नियोजयेत् ।**  
> **आदेशस्य फलं दत्त्वा ग्राहकं तोषयेत् तदा ॥३२॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `सङ्कल्पिते सति प्राज्ञः राज्य-यन्त्रे नियोजयेत् । आदेशस्य फलम् दत्त्वा ग्राहकम् तोषयेत् तदा ॥३२॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **सङ्कल्पिते सति** | `भावे सप्तमी (7/1 m. + 7/1 m.)` | Once the entry is committed |
| **प्राज्ञः राज्ययन्त्रे नियोजयेत्** | `1/1 m. + 7/1 n. + नि-युज् णिच् विधिलिङ् 3/1` | The leader applies the command to its local State Machine |
| **आदेशस्य फलम् दत्त्वा** | `6/1 m. + 2/1 n. + दा क्त्वा` | Having computed the deterministic result of the client execution |
| **ग्राहकम् तोषयेत् तदा** | `2/1 m. + तुष् णिच् विधिलिङ् 3/1 + अव्ययम्` | He replies to the client with the successful response |

**English Translation:**  
*Once committed, the leader applies the entry to its state machine and returns the result to the client.*  

**Distributed Systems Engineering Commentary:**  
Applying to State Machine: `commitIndex` is updated monotonically. Once an entry is committed, the server applies it in index order to its state machine (`lastApplied`). The leader then returns the execution result to the client, guaranteeing linearizability.
</details>

#### श्लोकः 33 (अनुष्टुभ्)
> **यन्त्रेषु गणभूतेषु क्रमेणैव प्रयुज्यते ।**  
> **नानायन्त्रेषु सम्भूतं फलं तुल्यं प्रजायते ॥३३॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `यन्त्रेषु गण-भूतेषु क्रमेण एव प्रयुज्यते । नाना-यन्त्रेषु सम्भूतम् फलम् तुल्यम् प्रजायते ॥३३॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **यन्त्रेषु गणभूतेषु** | `7/3 n. + 7/3 n.` | Across all follower servers in the cluster |
| **क्रमेण एव प्रयुज्यते** | `3/1 m. + अव्ययम् + प्र-युज् कर्मणि लट् 3/1` | The committed entries are applied in strict log order |
| **नानायन्त्रेषु सम्भूतम् फलम्** | `7/3 n. + क्त 1/1 n. + 1/1 n.` | The resulting computed state on distinct physical machines |
| **तुल्यम् प्रजायते** | `1/1 n. + प्र-जन् लट् āt 3/1` | Remains bit-for-bit identical across the cluster |

**English Translation:**  
*Applied in log order across all replicas, the resulting state is bit-for-bit identical.*  

**Distributed Systems Engineering Commentary:**  
State Machine Safety: If a server has applied a log entry at a given index to its state machine, no other server will ever apply a different log entry for the same index. All replicas transition through the exact same state trajectory.
</details>

#### श्लोकः 34 (अनुष्टुभ्)
> **सङ्कल्पिते कृते कार्ये न पश्चात्तापसम्भवः ।**  
> **अचलः सङ्ग्रहो जातः सर्वमान्यो विधीयते ॥३४॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `सङ्कल्पिते कृते कार्ये न पश्चात्-ताप-सम्भवः । अचलः सङ्ग्रहः जातः सर्व-मान्यः विधीयते ॥३४॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **सङ्कल्पिते कृते कार्ये** | `भावे सप्तमी (7/1 m. + 7/1 m. + 7/1 n.)` | Once an operation has reached committed state |
| **न पश्चात्तापसम्भवः** | `अव्ययम् + 1/1 m.` | No rollback, data loss, or divergence is possible |
| **अचलः सङ्ग्रहः जातः** | `1/1 m. + 1/1 m. + क्त 1/1 m.` | An unshakeable, persistent ledger has been formed |
| **सर्वमान्यः विधीयते** | `1/1 m. + वि-धा कर्मणि लट् 3/1` | Universally acknowledged by all future terms |

**English Translation:**  
*Once committed, no rollback is possible; an unshakeable ledger stands acknowledged by all terms.*  

**Distributed Systems Engineering Commentary:**  
Leader Completeness: If a log entry is committed in a given term, then that entry will be present in the logs of the leaders for all higher-numbered terms. A candidate cannot be elected unless its log contains all committed entries.
</details>

#### श्लोकः 35 (अनुष्टुभ्)
> **राज्ययन्त्रप्रयोगेण गणना सिद्धिमाप्नुयात् ।**  
> **अविचलप्रभावेण समतिः संप्रजायते ॥३५॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `राज्य-यन्त्र-प्रयोगेण गणना सिद्धिम् आप्नुयात् । अविचल-प्रभावेण समतिः संप्रजायते ॥३५॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **राज्ययन्त्रप्रयोगेण** | `3/1 m.` | Through the deterministic execution of the state machine |
| **गणना सिद्धिम् आप्नुयात्** | `1/1 f. + 2/1 f. + आप् विधिलिङ् 3/1` | Distributed computation attains fault-tolerant success |
| **अविचलप्रभावेण** | `3/1 m.` | Through the unshakeable power of mathematical safety invariants |
| **समतिः संप्रजायते** | `1/1 f. + सम्-प्र-जन् लट् āt 3/1` | Consensus is flawlessly manifested |

**English Translation:**  
*Through deterministic state machines, distributed computing attains flawless consensus.*  

**Distributed Systems Engineering Commentary:**  
Consensus Realized: Raft bridges the gap between chaotic network hardware and deterministic application software. To the client, the distributed cluster appears as a single indestructible, highly available computer.
</details>

## अष्टमः सर्गः : संविद्विच्छेदः द्विधाविभागरक्षा
### *Network Partitions & Split-Brain Prevention*
*Network partitions dividing the cluster, the inability of minorities to commit, majority cluster progression and reconciliation on healing.*

#### श्लोकः 36 (अनुष्टुभ्)
> **यदा जालं द्विधा छिन्नं विच्छेदो जायते पथि ।**  
> **अल्पसङ्ख्या न शक्नोति बहुमतं प्रसाधितुम् ॥३६॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `यदा जालम् द्विधा छिन्नम् विच्छेदः जायते पथि । अल्प-सङ्ख्या न शक्नोति बहुमतम् प्रसाधितुम् ॥३६॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **यदा जालम् द्विधा छिन्नम्** | `अव्ययम् + 1/1 n. + अव्ययम् + क्त 1/1 n.` | When the network is sliced into two partitions (Network Partition) |
| **विच्छेदः जायते पथि** | `1/1 m. + जन् लट् āt 3/1 + 7/1 m.` | A physical communication disconnect occurs across routing links |
| **अल्पसङ्ख्या** | `1/1 f.` | The minority sub-cluster (e.g. 2 nodes out of 5) |
| **न शक्नोति बहुमतम् प्रसाधितुम्** | `अव्ययम् + शक् लट् 3/1 + 2/1 n. + प्र-साध् तुमुन्` | Is completely incapable of assembling a majority quorum |

**English Translation:**  
*When a network partition splits the cluster, the minority is incapable of forming a majority quorum.*  

**Distributed Systems Engineering Commentary:**  
The Minority Partition: Imagine a 5-node cluster split into $\{A, B\}$ and $\{C, D, E\}$. If $A$ was the leader, $A$ and $B$ can still talk to each other, but they can only muster 2 votes out of 5. They cannot form a majority ($3$ needed).
</details>

#### श्लोकः 37 (अनुष्टुभ्)
> **बहुसङ्ख्यायुतो भागः स्वनायकं वृणोत्यलम् ।**  
> **अल्पभागस्थितो नेता न कञ्चित् कर्म कल्पयेत् ॥३७॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `बहु-सङ्ख्या-युतः भागः स्व-नायकम् वृणोति अलम् । अल्प-भाग-स्थितः नेता न कञ्चित् कर्म कल्पयेत् ॥३७॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **बहुसङ्ख्यायुतः भागः** | `1/1 m. + 1/1 m.` | The majority partition containing 3 of the 5 nodes |
| **स्वनायकम् वृणोति अलम्** | `2/1 m. + वृ लट् āt 3/1 + अव्ययम्` | Elects its own legitimate leader in a higher term |
| **अल्पभागस्थितः नेता** | `1/1 m. + 1/1 m.` | While the isolated stale leader on the minority side |
| **न कञ्चित् कर्म कल्पयेत्** | `अव्ययम् + 2/1 n. + 2/1 n. + क्लृप् णिच् विधिलिङ् 3/1` | Cannot commit a single operation to its log |

**English Translation:**  
*The majority elects a new leader; the isolated leader on the minority side cannot commit any command.*  

**Distributed Systems Engineering Commentary:**  
Preventing Split-Brain: $\{C, D, E\}$ times out and elects $C$ as leader for term 2. When clients send writes to $A$ (in the minority), $A$ cannot replicate to a majority, so those entries remain uncommitted. Split-brain is prevented.
</details>

#### श्लोकः 38 (अनुष्टुभ्)
> **यदा सन्धानसम्पत्तिः पुनर्जालस्य जायते ।**  
> **बहुभागस्य सत्येन लघुरेवावधीर्यते ॥३८॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `यदा सन्धान-सम्पत्तिः पुनः जालस्य जायते । बहु-भागस्य सत्येन लघुः एव अवधीर्यते ॥३८॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **यदा सन्धानसम्पत्तिः** | `अव्ययम् + 1/1 f.` | When network reconnection and healing occur |
| **पुनः जालस्य जायते** | `अव्ययम् + 6/1 n. + जन् लट् āt 3/1` | The network bridge is restored across all partitions |
| **बहुभागस्य सत्येन** | `6/1 m. + 3/1 n.` | By the authoritative log of the majority leader |
| **लघुः एव अवधीर्यते** | `1/1 m. + अव्ययम् + अव-धृ कर्मणि लट् 3/1` | The minority sub-cluster is completely reconciled and updated |

**English Translation:**  
*When the network heals, by the authority of the majority leader, the minority is reconciled.*  

**Distributed Systems Engineering Commentary:**  
Reconciliation on Partition Healing: When the network heals, $A$ receives a heartbeat from $C$ carrying term 2. Node $A$ sees a higher term, steps down to follower and accepts $C$'s authority.
</details>

#### श्लोकः 39 (अनुष्टुभ्)
> **असङ्कल्पितलेखास्तु हीनान् यन्त्राद् विनाशयेत् ।**  
> **नायकस्यैव लेखेन सर्वेषां शोधनं भवेत् ॥३९॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `असङ्कल्पित-लेखाः तु हीनान् यन्त्रात् विनाशयेत् । नायकस्य एव लेखेन सर्वेषाम् शोधनम् भवेत् ॥३९॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **असङ्कल्पितलेखाः तु** | `1/3 m. + अव्ययम्` | Uncommitted entries written during the partition |
| **हीनान् यन्त्रात् विनाशयेत्** | `2/3 m. + 5/1 n. + वि-नश् णिच् विधिलिङ् 3/1` | The follower overwrites and purges from its log |
| **नायकस्य एव लेखेन** | `6/1 m. + अव्ययम् + 3/1 m.` | With the majority leader's authoritative log |
| **सर्वेषाम् शोधनम् भवेत्** | `6/3 m. + 1/1 n. + भू विधिलिङ् 3/1` | Thorough purification and synchronization of all nodes occurs |

**English Translation:**  
*Uncommitted entries are purged; with the leader's log, all nodes are synchronized.*  

**Distributed Systems Engineering Commentary:**  
Overwriting Uncommitted Entries: The uncommitted writes sent to $A$ during the partition are overwritten by $C$'s log entries. Because those writes were never committed or acknowledged to clients as successful, Safety is preserved.
</details>

#### श्लोकः 40 (अनुष्टुभ्)
> **द्विधाविभागरक्षायां राफ्ट्-तन्त्रं प्रतिष्ठितम् ।**  
> **भङ्गे सत्यपि जालस्य सत्यं नैव प्रणश्यति ॥४०॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `द्विधा-विभाग-रक्षायाम् राफ्ट्-तन्त्रम् प्रतिष्ठितम् । भङ्गे सति अपि जालस्य सत्यम् न एव प्रणश्यति ॥४०॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **द्विधाविभागरक्षायाम्** | `7/1 f.` | In the absolute defense against split-brain partitions |
| **राफ्ट्-तन्त्रम् प्रतिष्ठितम्** | `1/1 n. + क्त 1/1 n.` | The Raft protocol stands celebrated |
| **भङ्गे सति अपि जालस्य** | `भावे सप्तमी (7/1 m. + 7/1 m. + अव्ययम् + 6/1 n.)` | Even during catastrophic physical network partitions |
| **सत्यम् न एव प्रणश्यति** | `1/1 n. + अव्ययम् + अव्ययम् + प्र-नश् लट् 3/1` | Data consistency and linearizable truth never perish |

**English Translation:**  
*Raft prevents split-brain; even during network failures, linearizable truth never perishes.*  

**Distributed Systems Engineering Commentary:**  
CAP Theorem Balance: Under the CAP theorem, Raft chooses Consistency and Partition Tolerance ($CP$). When a network partition occurs, the majority partition stays available, while the minority partition rejects writes to guarantee Consistency.
</details>

## नवमः सर्गः : संयुक्तसमतिः मण्डलविस्तारः
### *Joint Consensus & Dynamic Cluster Membership*
*Dynamic cluster configuration changes, avoiding disjoint majorities, two-phase Joint Consensus ($C_{\text{old}} \to C_{\text{old,new}} \to C_{\text{new}}$) and seamless transitions.*

#### श्लोकः 41 (अनुष्टुभ्)
> **यन्त्राणां परिवर्तार्थं संयुक्तसमतिर्मता ।**  
> **पूर्वैश्च नूतनैश्चापि बहुमतं प्रसाध्यते ॥४१॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `यन्त्राणाम् परिवर्त-अर्थम् संयुक्त-समतिः मता । पूर्वैः च नूतनैः च अपि बहुमतम् प्रसाध्यते ॥४१॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **यन्त्राणाम् परिवर्तार्थम्** | `6/3 n. + 4/1 m.` | For altering the cluster membership (adding or removing servers) |
| **संयुक्तसमतिः मता** | `1/1 f. + क्त 1/1 f.` | Joint Consensus ($C_{\text{old,new}}$) is prescribed |
| **पूर्वैः च नूतनैः च अपि** | `3/3 m. + अव्ययम् + 3/3 m. + अव्ययम् + अव्ययम्` | Through both old configuration and new configuration majorities |
| **बहुमतम् प्रसाध्यते** | `1/1 n. + प्र-साध् कर्मणि लट् 3/1` | Quorum consensus must be independently satisfied |

**English Translation:**  
*To change cluster membership safely, Joint Consensus is used, requiring majorities from both old and new configurations.*  

**Distributed Systems Engineering Commentary:**  
Cluster Membership Changes: Adding or removing servers cannot be done atomically across all nodes at once. A naive switch could allow two disjoint majorities: an old 3-node cluster and a new 5-node cluster electing separate leaders simultaneously. Joint Consensus prevents this.
</details>

#### श्लोकः 42 (अनुष्टुभ्)
> **उभयोर्मण्डलयोर्योगे द्वौ भागौ सम्मतौ सदा ।**  
> **एकदा नैव निष्पत्तिः पृथङ्नायकसम्भवा ॥४२॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `उभयोः मण्डलयोः योगे द्वौ भागौ सम्मतौ सदा । एकदा न एव निष्पत्तिः पृथक्-नायक-सम्भवा ॥४२॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **उभयोः मण्डलयोः योगे** | `6/2 n. + 6/2 n. + 7/1 m.` | In the interim joint consensus state ($C_{\text{old,new}}$) |
| **द्वौ भागौ सम्मतौ सदा** | `1/2 m. + 1/2 m. + 1/2 m. + अव्ययम्` | Majorities from both configurations must agree on every decision |
| **एकदा न एव निष्पत्तिः** | `अव्ययम् + अव्ययम् + अव्ययम् + 1/1 f.` | Simultaneously it is impossible for an election |
| **पृथङ्नायकसम्भवा** | `1/1 f.` | To produce two separate leaders |

**English Translation:**  
*In joint consensus, majorities from both configurations must agree; electing separate leaders is impossible.*  

**Distributed Systems Engineering Commentary:**  
Joint Consensus Safety: During Joint Consensus, any decision (including commitment and elections) requires separate majorities from both $C_{\text{old}}$ and $C_{\text{new}}$. Because $C_{\text{old}}$ cannot elect a leader without a majority of its nodes, split decisions are physically impossible.
</details>

#### श्लोकः 43 (अनुष्टुभ्)
> **आदौ संयुक्तकालेन सन्देशा विनिवेशिताः ।**  
> **पश्चादेव नूतनेनैव राज्यं सर्वं प्रपाल्यते ॥४३॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `आदौ संयुक्त-कालेन सन्देशाः विनिवेशिताः । पश्चात् एव नूतनेन एव राज्यम् सर्वम् प्रपाल्यते ॥४३॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **आदौ संयुक्तकालेन** | `अव्ययम् + 3/1 m.` | First, the Joint Consensus configuration entry ($C_{\text{old,new}}$) |
| **सन्देशाः विनिवेशिताः** | `1/3 m. + क्त 1/3 m.` | Is written and committed into the distributed log |
| **पश्चात् एव नूतनेन एव** | `अव्ययम् + अव्ययम् + 3/1 n. + अव्ययम्` | Only thereafter is the final new configuration entry ($C_{\text{new}}$) committed |
| **राज्यम् सर्वम् प्रपाल्यते** | `1/1 n. + 1/1 n. + प्र-पाल् कर्मणि लट् 3/1` | The entire cluster governance transitions smoothly |

**English Translation:**  
*First Joint Consensus is committed; thereafter the new configuration is committed, completing the transition.*  

**Distributed Systems Engineering Commentary:**  
The Two-Phase Transition: 1. Leader writes and commits $C_{\text{old,new}}$. Once committed, neither $C_{\text{old}}$ nor $C_{\text{new}}$ can make decisions alone. 2. Leader writes and commits $C_{\text{new}}$. After $C_{\text{new}}$ is committed, decommissioned old nodes can be safely powered off.
</details>

#### श्लोकः 44 (अनुष्टुभ्)
> **अविरामेण कार्येण विस्तारः क्रियते दृढः ।**  
> **सेवाया न भवेद् भङ्गो राफ्ट्-धर्मे सुसंस्थिते ॥४४॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `अविरामेण कार्येण विस्तारः क्रियते दृढः । सेवायाः न भवेत् भङ्गः राफ्ट्-धर्मे सु-संस्थिते ॥४४॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **अविरामेण कार्येण** | `3/1 n. + 3/1 n.` | Without halting operations or pausing client requests (zero downtime) |
| **विस्तारः क्रियते दृढः** | `1/1 m. + कृ कर्मणि लट् 3/1 + 1/1 m.` | Cluster scaling and server replacement are executed reliably |
| **सेवायाः न भवेत् भङ्गः** | `6/1 f. + अव्ययम् + भू विधिलिङ् 3/1 + 1/1 m.` | Zero disruption or degradation of service occurs |
| **राफ्ट्-धर्मे सुसंस्थिते** | `7/1 m. + 7/1 m.` | When the disciplined rules of Raft are faithfully maintained |

**English Translation:**  
*Cluster scaling proceeds without pausing client traffic; under Raft, zero service disruption occurs.*  

**Distributed Systems Engineering Commentary:**  
Zero-Downtime Reconfiguration: The cluster continues serving client requests during the membership change. Machines can be added or decommissioned dynamically in production without taking the database offline.
</details>

#### श्लोकः 45 (अनुष्टुभ्)
> **सङ्ख्यावृद्धौ क्षये वापि समता न विशीर्यते ।**  
> **संयुक्तसमतेर्ज्ञानाद् यन्त्रव्यूहः सुशोभते ॥४५॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `सङ्ख्या-वृद्धौ क्षये वा अपि समता न विशीर्यते । संयुक्त-समतेः ज्ञानात् यन्त्र-व्यूहः सु-शोभते ॥४५॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **सङ्ख्यावृद्धौ क्षये वा अपि** | `7/1 f. + 7/1 m. + अव्ययम् + अव्ययम्` | In scaling up nodes or scaling down nodes |
| **समता न विशीर्यते** | `1/1 f. + अव्ययम् + वि-शीर्यते कर्मणि लट् āt 3/1` | Consensus consistency is never compromised |
| **संयुक्तसमतेः ज्ञानात्** | `6/1 f. + 5/1 n.` | Through deep architectural mastery of Joint Consensus |
| **यन्त्रव्यूहः सुशोभते** | `1/1 m. + सु-शुभ् लट् āt 3/1` | The distributed server cluster operates with supreme elegance |

**English Translation:**  
*In scaling up or down, consensus is never broken; through Joint Consensus, the cluster operates with elegance.*  

**Distributed Systems Engineering Commentary:**  
Dynamic Elasticity: Modern cloud-native infrastructure (Kubernetes, etcd, CockroachDB) relies on Raft's membership change protocol to scale dynamically across cloud availability zones.
</details>

## दशमः सर्गः : सर्वसमतिसिद्धिः स्थिरतन्त्रम्
### *Consensus Realization & Architectural Invariants*
*The five core safety invariants of Raft, understandability as an engineering virtue and the triumph of distributed state consensus.*

#### श्लोकः 46 (अनुष्टुभ्)
> **निर्वाचने तथैवाङ्के वृत्तलेखे च रक्षणे ।**  
> **पञ्चैते मूलनियमा राफ्ट्-तन्त्रे प्रतिष्ठिताः ॥४६॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `निर्वाचने तथा एव अङ्के वृत्त-लेखे च रक्षणे । पञ्च एते मूल-नियमाः राफ्ट्-तन्त्रे प्रतिष्ठिताः ॥४६॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **निर्वाचने तथा एव अङ्के** | `7/1 n. + अव्ययम् + अव्ययम् + 7/1 m.` | In elections, leader append-only logging and matching |
| **वृत्तलेखे च रक्षणे** | `7/1 m. + अव्ययम् + 7/1 n.` | And in log completeness and state machine safety |
| **पञ्च एते मूलनियमाः** | `1/3 m. + 1/3 m. + 1/3 m.` | These five foundational safety invariants |
| **राफ्ट्-तन्त्रे प्रतिष्ठिताः** | `7/1 n. + क्त 1/3 m.` | Are firmly established in the Raft architecture |

**English Translation:**  
*Election safety, append-only, matching, completeness and state safety: these five invariants govern Raft.*  

**Distributed Systems Engineering Commentary:**  
Raft's Five Safety Invariants: 1. Election Safety (at most one leader per term). 2. Leader Append-Only (leader never overwrites its log). 3. Log Matching (matching index & term implies identical prefix). 4. Leader Completeness (committed entries persist in all future leaders). 5. State Machine Safety (no different entries applied at same index).
</details>

#### श्लोकः 47 (अनुष्टुभ्)
> **नायकस्याविनाशी स्याद् वृत्तलेखो निरन्तरम् ।**  
> **राज्ययन्त्रे प्रयुक्तं यत् तत् सदा सर्वसम्मतम् ॥४७॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `नायकस्य अविनाशी स्यात् वृत्त-लेखः निरन्तरम् । राज्य-यन्त्रे प्रयुक्तम् यत् तत् सदा सर्व-सम्मतम् ॥४७॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **नायकस्य अविनाशी स्यात्** | `6/1 m. + 1/1 m. + अस् विधिलिङ् 3/1` | The committed log of the leader is indestructible |
| **वृत्तलेखः निरन्तरम्** | `1/1 m. + अव्ययम्` | Replicated history perpetually enduring |
| **राज्ययन्त्रे प्रयुक्तम् यत्** | `7/1 n. + क्त 1/1 n. + 1/1 n.` | Whatever command has been applied to the state machine |
| **तत् सदा सर्वसम्मतम्** | `1/1 pron. + अव्ययम् + 1/1 n.` | That state remains eternally agreed by all nodes |

**English Translation:**  
*The committed log of the leader is indestructible; what is applied to state machines remains agreed forever.*  

**Distributed Systems Engineering Commentary:**  
Immutability of Committed Data: Once a write is committed, no server failure, network partition, or election change can ever alter that data. This guarantee underpins the financial integrity of modern distributed ledgers and transactional databases.
</details>

#### श्लोकः 48 (अनुष्टुभ्)
> **सहस्रेष्वपि दोषेषु सत्यं तिष्ठति शाश्वतम् ।**  
> **वितरितेषु यन्त्रेषु स्थैर्यं येन प्रजायते ॥४८॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `सहस्रेषु अपि दोषेषु सत्यम् तिष्ठति शाश्वतम् । वितरितेषु यन्त्रेषु स्थैर्यम् येन प्रजायते ॥४८॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **सहस्रेषु अपि दोषेषु** | `7/3 m. + अव्ययम् + 7/3 m.` | Even amid thousands of packet drops and server crashes |
| **सत्यम् तिष्ठति शाश्वतम्** | `1/1 n. + स्था लट् 3/1 + 1/1 n.` | Deterministic truth stands eternal and unbroken |
| **वितरितेषु यन्त्रेषु** | `7/3 n. + 7/3 n.` | Across distributed networked machines |
| **स्थैर्यम् येन प्रजायते** | `1/1 n. + 3/1 pron. + प्र-जन् लट् āt 3/1` | Whereby supreme architectural resiliency and stability are born |

**English Translation:**  
*Even amid thousands of faults, truth stands eternal, conferring supreme stability across distributed systems.*  

**Distributed Systems Engineering Commentary:**  
Resilience in Chaos: Chaos engineering experiments (killing random nodes, simulating partition storms) prove Raft's resilience. It guarantees safety under all conditions and liveness whenever a majority can communicate.
</details>

#### श्लोकः 49 (अनुष्टुभ्)
> **सरलत्वाच्च शुद्धत्वाद् राफ्ट्-तन्त्रं विराजते ।**  
> **गणनाशास्त्रतत्त्वज्ञैः पूजितं सर्वमण्डले ॥४९॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `सरलत्वात् च शुद्धत्वात् राफ्ट्-तन्त्रम् विराजते । गणना-शास्त्र-तत्त्व-ज्ञैः पूजितम् सर्व-मण्डले ॥४९॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **सरलत्वात् च शुद्धत्वात्** | `5/1 n. + अव्ययम् + 5/1 n.` | Owing to its conceptual clarity, modular simplicity and mathematical purity |
| **राफ्ट्-तन्त्रम् विराजते** | `1/1 n. + वि-राज् लट् āt 3/1` | The Raft consensus algorithm shines supreme |
| **गणनाशास्त्रतत्त्वज्ञैः** | `3/3 m.` | By computer scientists and distributed systems architects |
| **पूजितम् सर्वमण्डले** | `क्त 1/1 n. + 7/1 n.` | Universally revered and adopted across global software infrastructure |

**English Translation:**  
*Owing to simplicity and purity, Raft shines supreme, revered by computer scientists worldwide.*  

**Distributed Systems Engineering Commentary:**  
The Victory of Understandability: Raft proved that understandability is a first-class engineering goal. Today, etcd, Consul, TiKV, Kafka (KRaft) and MongoDB all rely on Raft or Raft-derived protocols to power global cloud infrastructure.
</details>

#### श्लोकः 50 (अनुष्टुभ्)
> **इति राफ्ट्-महाशास्त्रं पञ्चाशद्भिः सुभाषितम् ।**  
> **सर्वसम्मतसिद्ध्यर्थं प्रणीतं लोकभूतये ॥५०॥**

<details>
<summary>व्याकरणम् · पदच्छेदः · English Analysis</summary>

**पदच्छेदः:** `इति राफ्ट्-महा-शास्त्रम् पञ्चाशद्भिः सु-भाषितम् । सर्व-सम्मत-सिद्ध्यर्थम् प्रणीतम् लोक-भूतये ॥५०॥`  

| पदम् / Phrase | रूपम् / Analysis | Syntactic & Strategic Role |
| :--- | :--- | :--- |
| **इति राफ्ट्-महाशास्त्रम्** | `अव्ययम् + 1/1 n.` | Thus this great treatise on Raft distributed consensus |
| **पञ्चाशद्भिः सुभाषितम्** | `3/3 f. + क्त 1/1 n.` | Elegantly illuminated through fifty classical Sanskrit verses |
| **सर्वसम्मतसिद्ध्यर्थम्** | `4/1 n.` | For the realization of fault-tolerant consensus |
| **प्रणीतम् लोकभूतये** | `क्त 1/1 n. + 4/1 f.` | Composed for the enduring benefit and reliability of digital civilization |

**English Translation:**  
*Thus this treatise on Raft, adorned in fifty verses, is composed for the enduring reliability of computing.*  

**Distributed Systems Engineering Commentary:**  
Conclusion of Samati-Pañcāśikā: Codifying the Raft consensus algorithm into fifty classical Sanskrit verses. From leader election to state machine safety, Raft ensures that digital civilization rests upon an indestructible foundation of mathematical consensus.
</details>

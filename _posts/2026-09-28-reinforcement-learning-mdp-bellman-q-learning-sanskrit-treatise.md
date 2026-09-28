---
layout: post
title: "Reinforcement Learning: Markov Decision Processes, Bellman Optimality, Q-Learning & Policy Gradients (पुनर्बलनपञ्चाशिका : कर्मफलविधिः)"
date: 2026-09-28 16:00:00 +0530
categories: [sanskrit, machine-learning]
tags: [sanskrit, poetry, anustubh, reinforcement-learning, markov-decision-process, bellman-equations, q-learning, sarsa, policy-gradients, actor-critic, dqn, ppo, ai]
author: "Vedant Madane"
excerpt: "A comprehensive 50-verse classical Sanskrit technical treatise (पुनर्बलनपञ्चाशिका) composed in rigorous Pathyāvaktrā Anuṣṭubh meter with Pāṇinian morphological analysis and deep systems commentary, formalizing Reinforcement Learning from Markov Decision Processes and Bellman Equations to Deep Q-Networks, PPO and RLHF Alignment."
---

# पुनर्बलनपञ्चाशिका : कर्मफलविधिः
## *Punarnabalana-Pañcāśikā: Karma-Phala-Vidhiḥ*
### A 50-Verse Classical Sanskrit Technical Treatise on Reinforcement Learning, Markov Decision Processes, Bellman Optimality and Deep Policy Optimization

**Composed by:** Vedant Madane  
**Meter:** Classical Anuṣṭubh (*Pathyāvaktrā* : strictly 16 syllables per hemistich / 32 per verse; odd pādas ending in ya-gaṇa `~ - -`, even pādas ending in ja-gaṇa `~ - ~`)  
**Grammatical Framework:** Pāṇinian Morpho-Syntactic Analysis (अष्टाध्यायी-पदविभाग-कारकसमीक्षा)  
**Systems Perspective:** Markov Decision Processes, Dynamic Programming, Temporal Difference Control, Deep Q-Networks, Policy Gradients and RLHF Alignment Architectures

---

## Executive Overview & Theoretical Foundations

Reinforcement Learning represents the computational formalization of goal-directed learning from interaction. Unlike supervised learning (which depends upon external oracle supervision) or unsupervised learning (which identifies geometric clustering in static datasets), an autonomous reinforcement learning agent learns through trial, error and reward. It perceives its environment, selects actions, endures delayed consequences and autonomously improves its behavioral policy to maximize long-term cumulative return.

This treatise, titled **पुनर्बलनपञ्चाशिका : कर्मफलविधिः** (*Treatise of Fifty Verses on Reinforcement Learning and the Dynamics of Action and Reward*), formalizes the full mathematical architecture of reinforcement learning across ten thematic Cantos (दशसर्गाः), comprising exactly fifty Anuṣṭubh verses composed in classical Sanskrit. Every verse adheres strictly to the metrical laws of classical *Pathyāvaktrā* verified computationally via syllabic parsers. Each verse is equipped with an exhaustive Pāṇinian morphological parsing table (पदविभागः) mapping roots, stems, nominal/verbal inflections and syntactic roles, followed by an in-depth systems commentary contextualizing the mathematical theorems with modern deep reinforcement learning, Atari benchmarks, AlphaZero self-play and RLHF alignment for foundation models.

### Architectural Schema of the Ten Cantos

1. **Canto 1: कर्ता परिवेशश्च (Agent and Environment: The Markov Decision Process)**: Agent and Environment (कर्ता परिवेशश्च): The autonomous agent feedback loop, state and action spaces, transition dynamics P(s' | s, a), the memoryless Markov property and discounted cumulative return G_t.
2. **Canto 2: नीतिर्मूल्यफलनं च (Policy and Value Functions)**: Policy and Value Functions (नीतिर्मूल्यफलनं च): Stochastic and deterministic policies pi(a | s), the state-value function V^pi(s), the action-value function Q^pi(s, a), the advantage function A^pi(s, a) and the existence of an optimal policy pi^*.
3. **Canto 3: बेल्मन्-समीकरणानि (The Bellman Equations: Recursive Decomposition)**: The Bellman Equations (बेल्मन्-समीकरणानि): Recursive expectation decomposition for V^pi and Q^pi, non-linear Bellman optimality equations with max operators, Banach fixed-point contraction mapping and uniqueness of V^*.
4. **Canto 4: गतिकप्रक्रमः (Dynamic Programming: Policy & Value Iteration)**: Dynamic Programming (गतिकप्रक्रमः): Model-based planning requirements, iterative Policy Evaluation, greedy Policy Improvement, Generalized Policy Iteration and single-sweep Value Iteration.
5. **Canto 5: मान्टे-कार्लो-पद्धतिः (Monte Carlo Methods: Model-Free Learning)**: Monte Carlo Methods (मान्टे-कार्लो-पद्धतिः): Model-free learning from episodic experience, first-visit vs every-visit estimators, zero-bias high-variance trade-offs, epsilon-greedy exploration and off-policy importance sampling.
6. **Canto 6: कालभेदशिक्षणम् (Temporal Difference Learning: TD(0) & SARSA)**: Temporal Difference Learning (कालभेदशिक्षणम्): Bootstrapping from successor value estimates before termination, the fundamental TD error delta_t as dopaminergic teaching signal, low variance online updates and the on-policy SARSA algorithm.
7. **Canto 7: क्यू-शिक्षणम् (Q-Learning: Off-Policy TD Control)**: Q-Learning (क्यू-शिक्षणम्): Watkins' 1989 off-policy TD control breakthrough, the Q-learning update rule with max target, decoupling exploratory behavior from optimal policy convergence, Double Q-learning and eligibility traces TD(lambda).
8. **Canto 8: फलनसन्निकर्षः गभीर-क्यू-जालं च (Function Approximation & Deep Q-Networks)**: Function Approximation & Deep Q-Networks (फलनसन्निकर्षः गभीर-क्यू-जालं च): The curse of dimensionality in continuous state spaces, linear semi-gradients, the Deadly Triad divergence pathology, Deep Q-Networks (DQN) and stabilization via Experience Replay and Target Networks.
9. **Canto 9: नीतिक्रमप्रवणता (Policy Gradient Methods & Actor-Critic)**: Policy Gradient Methods & Actor-Critic (नीतिक्रमप्रवणता): Direct policy optimization, the Policy Gradient Theorem, REINFORCE score-function updates, variance reduction through baseline subtraction and Actor-Critic dual-network synergy.
10. **Canto 10: प्रगतविधानानि महासंश्लेषश्च (Advanced Architectures & Grand Synthesis)**: Advanced Architectures & Grand Synthesis (प्रगतविधानानि महासंश्लेषश्च): Trust-region clipping via Proximal Policy Optimization (PPO), Model-Based Dyna planning, AlphaZero self-play with Monte Carlo Tree Search, RLHF alignment for language models and philosophical synthesis of karma, value and consciousness.

---

## सर्गः 1 : कर्ता परिवेशश्च (Agent and Environment: The Markov Decision Process)

*Agent and Environment (कर्ता परिवेशश्च): The autonomous agent feedback loop, state and action spaces, transition dynamics P(s' | s, a), the memoryless Markov property and discounted cumulative return G_t.*

### श्लोकः 1

```text
प्रणम्य जगदात्मानं कर्मकारणमीश्वरम् ।
पुनर्बलनशास्त्रेऽस्मिन् वक्ष्ये निर्णयसङ्ग्रहम् ॥
```

#### IAST Transliteration
*praṇamya jagadātmānaṃ karmakāraṇamīśvaram |
punarbalanaśāstre'smin vakṣye nirṇayasaṅgraham ||*

#### English Translation
> Bowing to the Soul of the universe, the sovereign lord who is the fundamental cause of action: within this science of reinforcement learning, I expound the comprehensive synthesis of decision making.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **प्रणम्य** | `प्रणम्` | Gerund (ktvā) | Indeclinable | Preceding action: having bowed |
| **जगदात्मानम्** | `जगदात्मन्` | Noun (masculine) | Accusative Singular | Direct object of praṇamya: the Soul of the universe |
| **कर्मकारणम्** | `कर्मकारण` | Noun (masculine) | Accusative Singular | Appositive modifying jagadātmānam: cause of action |
| **ईश्वरम्** | `ईश्वर` | Noun (masculine) | Accusative Singular | Appositive modifying jagadātmānam: sovereign reality |
| **पुनर्बलनशास्त्रे** | `पुनर्बलनशास्त्र` | Noun (neuter) | Locative Singular | Locus: in the science of reinforcement learning |
| **अस्मिन्** | `इदम्` | Pronoun (neuter) | Locative Singular | Modifying śāstre: in this |
| **वक्ष्ये** | `वच्` | Verb | Future 1st Person Singular | Main verb: I shall expound |
| **निर्णयसङ्ग्रहम्** | `निर्णयसङ्ग्रह` | Noun (masculine) | Accusative Singular | Direct object of vakṣye: synthesis of decision making |

#### Deep Systems & Domain Commentary
The opening invocation establishes the mathematical and philosophical foundations of Reinforcement Learning (RL). Unlike supervised learning (which relies on static datasets of labeled inputs and outputs) or unsupervised learning (which discovers latent patterns in unlabeled data), reinforcement learning is an active paradigm of experiential trial and error. An autonomous agent (कर्ता) interacts with an external dynamic environment (परिवेशः). The agent takes actions, perceives state transitions and receives scalar rewards. The overarching goal of the computational agent is to discover an optimal behavioral policy that maximizes cumulative long-term returns across time.

---

### श्लोकः 2

```text
पदे स्थित्वा करोत्यर्थं परिवेशे विचालिते ।
गमनागमनं सर्वं सम्भावेन प्रतीयते ॥
```

#### IAST Transliteration
*pade sthitvā karotyarthaṃ pariveśe vicālite |
gamanāgamanaṃ sarvaṃ sambhāvena pratīyate ||*

#### English Translation
> Standing in a given state, the agent executes an action as the environment undergoes transition; the entire trajectory of movement between states is governed by transition probabilities.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **पदे** | `पद` | Noun (neuter) | Locative Singular | Locus: in the state s in S |
| **स्थित्वा** | `स्था` | Gerund (ktvā) | Indeclinable | Action: having stood or perceived |
| **करोति** | `कृ` | Verb | Present 3rd Person Singular | Verb: performs or executes |
| **अर्थम्** | `अर्थ` | Noun (masculine) | Accusative Singular | Object: action a in A or objective |
| **परिवेशे** | `परिवेश` | Noun (masculine) | Locative Singular | Locative absolute: environment |
| **विचालिते** | `विचालित` | Past Passive Participle | Locative Singular | Locative absolute: transitioned or perturbed |
| **गमनागमनम्** | `गमनागमन` | Noun (neuter) | Nominative Singular | Subject: state transition dynamic |
| **सर्वम्** | `सर्व` | Adjective (neuter) | Nominative Singular | Modifying gamanāgamanam: entire |
| **सम्भावेन** | `सम्भाव` | Noun (masculine) | Instrumental Singular | Instrument: by transition probability P(s' | s, a) |
| **प्रतीयते** | `प्रती` | Verb (passive) | Present 3rd Person Singular | Verb: is perceived or governed |

#### Deep Systems & Domain Commentary
The formal mathematical scaffolding of reinforcement learning is the Markov Decision Process (MDP), formally defined as the 5-tuple (S, A, P, R, gamma). Here S denotes the set of all valid environment states, A represents the set of available actions, P: S x A x S -> [0, 1] defines the transition probability function P(s' | s, a) = Pr(S_{t+1} = s' | S_t = s, A_t = a), R: S x A x S -> R specifies the reward function and gamma in [0, 1) is the temporal discount factor. At each discrete time step t, the agent observes state S_t in S, selects action A_t in A and receives reward R_{t+1} as the environment transitions stochastically to state S_{t+1}.

---

### श्लोकः 3

```text
यथावत् वर्तमानायाः स्थितेर्ज्ञानं व्यवस्थितम् ।
न पूर्वचरितेनास्ति प्रयोजनं पृथक् पदे ॥
```

#### IAST Transliteration
*yathāvat vartamānāyāḥ sthiterjñānaṃ vyavasthitam |
na pūrvacaritēnāsti prayojanaṃ pṛthak pade ||*

#### English Translation
> Complete, structured knowledge of the present state is sufficient; there is no separate utility in retaining the historical trajectory of past states.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **यथावत्** | `यथावत्` | Adverb | Indeclinable | Manner: completely or accurately |
| **वर्तमानयाः** | `वर्तमान` | Present Participle (feminine) | Genitive Singular | Modifying sthiteḥ: of the present |
| **स्थितेः** | `स्थिति` | Noun (feminine) | Genitive Singular | Possessive: of the current state S_t |
| **ज्ञानम्** | `ज्ञान` | Noun (neuter) | Nominative Singular | Subject: information or knowledge |
| **व्यवस्थितम्** | `व्यवस्थित` | Past Passive Participle | Nominative Singular | Predicate: sufficient or well-structured |
| **न** | `न` | Particle | Indeclinable | Negation: not |
| **पूर्वचरितेन** | `पूर्वचरित` | Noun (neuter) | Instrumental Singular | Instrument: by historical trajectory (S_0, A_0, ..., S_{t-1}) |
| **अस्ति** | `अस्` | Verb | Present 3rd Person Singular | Copula: there is |
| **प्रयोजनम्** | `प्रयोजन` | Noun (neuter) | Nominative Singular | Subject: utility or necessity |
| **पृथक्** | `पृथक्` | Adverb | Indeclinable | Separately: independently |
| **पदे** | `पद` | Noun (neuter) | Locative Singular | Locus: in predicting future state transitions |

#### Deep Systems & Domain Commentary
This verse articulates the Markov Property: the conditional probability distribution of future states depends solely upon the current state and action, being conditionally independent of the historical sequence of preceding states and actions. Mathematically: Pr(S_{t+1} = s', R_{t+1} = r | S_t = s, A_t = a, S_{t-1}, A_{t-1}, ..., S_0, A_0) = Pr(S_{t+1} = s', R_{t+1} = r | S_t = s, A_t = a). A state signal possessing the Markov property compactly summarizes all relevant past information. If an environment is partially observable (POMDP), the agent must construct a belief state or leverage recurrent memory (LSTM, Transformer) to restore an effective Markov representation.

---

### श्लोकः 4

```text
कृतस्य कर्मणः साक्षात् फलं लभ्येत निश्चितम् ।
क्रमागतफलैर्योगो भविष्यन् सम्प्रसाध्यते ॥
```

#### IAST Transliteration
*kṛtasya karmaṇaḥ sākṣāt phalaṃ labhyeta niścitam |
kramāgataphalairyogo bhaviṣyan samprasādhyate ||*

#### English Translation
> Directly upon an executed action, a definite scalar reward is received; through the accumulated sequence of future rewards, the cumulative return is realized.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **कृतस्य** | `कृत` | Past Passive Participle | Genitive Singular | Modifying karmaṇaḥ: executed |
| **कर्मणः** | `कर्मन्` | Noun (neuter) | Genitive Singular | Possessive: of an action A_t |
| **साक्षात्** | `साक्षात्` | Adverb | Indeclinable | Directly: immediately |
| **फलम्** | `फल` | Noun (neuter) | Nominative Singular | Subject: reward R_{t+1} |
| **लभ्येत** | `लभ्` | Verb (optative) | 3rd Person Singular | Verb: is obtained |
| **निश्चितम्** | `निश्चित` | Adjective (neuter) | Nominative Singular | Modifying phalam: definite |
| **क्रमागतफलैः** | `क्रमागतफल` | Noun (neuter) | Instrumental Plural | Instrument: by sequential future rewards |
| **योगः** | `योग` | Noun (masculine) | Nominative Singular | Subject: sum or cumulative return G_t |
| **भविष्यन्** | `भविष्यत्` | Present Participle (masculine) | Nominative Singular | Modifying yogaḥ: future or prospective |
| **सम्प्रसाध्यते** | `सम्प्रसाध्` | Verb (passive) | Present 3rd Person Singular | Verb: is accomplished or optimized |

#### Deep Systems & Domain Commentary
The Reward Hypothesis, formulated by Richard Sutton, asserts that all goals and purposes can be thought of as the maximization of the expected cumulative sum of a received scalar signal (reward). The return G_t is the cumulative sum of future rewards received after time step t: G_t = sum_{k=0}^infty gamma^k R_{t+k+1}. Crucially, reinforcement learning agents do not optimize for immediate instantaneous reward R_{t+1}, which would lead to shortsighted, suboptimal greed. Instead, the agent learns to endure temporary negative rewards (costs, investments) if they unlock substantially larger cumulative returns in downstream states.

---

### श्लोकः 5

```text
ह्रासेन गुणिते काले दूरे मानं लघु भवेत् ।
उपस्थिते महद् ग्राह्यं साम्यं शास्त्रे विधीयते ॥
```

#### IAST Transliteration
*hrāsena guṇite kāle dūre mānaṃ laghu bhavet |
upasthite mahad grāhyaṃ sāmyaṃ śāstre vidhīyate ||*

#### English Translation
> When future time steps are multiplied by the discount factor, distant values diminish in magnitude; immediate rewards are valued highly, establishing convergence across infinite horizons.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **ह्रासेन** | `ह्रास` | Noun (masculine) | Instrumental Singular | Instrument: by discount factor gamma |
| **गुणिते** | `गुणित` | Past Passive Participle | Locative Singular | Locative absolute: multiplied |
| **काले** | `काल` | Noun (masculine) | Locative Singular | Locative absolute: in temporal step k |
| **दूरे** | `दूर` | Adjective/Noun | Locative Singular | Locus: in the distant future |
| **मानम्** | `मान` | Noun (neuter) | Nominative Singular | Subject: reward magnitude |
| **लघु** | `लघु` | Adjective (neuter) | Nominative Singular | Predicate: diminished or small |
| **भवेत्** | `भू` | Verb (optative) | 3rd Person Singular | Verb: becomes |
| **उपस्थिते** | `उपस्थित` | Past Passive Participle | Locative Singular | Locus: in immediate presence |
| **महत्** | `महत्` | Adjective (neuter) | Nominative Singular | Predicate: large or significant |
| **ग्राह्यम्** | `ग्राह्य` | Future Passive Participle | Nominative Singular | Predicate: to be prioritized |
| **साम्यम्** | `साम्य` | Noun (neuter) | Nominative Singular | Subject: mathematical convergence |
| **शास्त्रे** | `शास्त्र` | Noun (neuter) | Locative Singular | Locus: in the theoretical discipline |
| **विधीयते** | `विधा` | Verb (passive) | Present 3rd Person Singular | Verb: is prescribed |

#### Deep Systems & Domain Commentary
The discount factor gamma in [0, 1) serves two vital roles. Analytically, in continuing (non-episodic) tasks where time steps extend infinitely (T = infty), discounting guarantees that the infinite geometric series of returns converges to a finite bound: |G_t| <= R_max / (1 - gamma). Behaviorally, gamma parameterizes the agent's temporal preference: as gamma -> 0, the agent becomes myopic, optimizing exclusively for immediate rewards R_{t+1}; as gamma -> 1, the agent becomes farsighted, weighing long-term outcomes with near-equal importance. In practice, values such as gamma in {0.9, 0.99, 0.999} balance numerical stability with long-horizon credit assignment.

---

## सर्गः 2 : नीतिर्मूल्यफलनं च (Policy and Value Functions)

*Policy and Value Functions (नीतिर्मूल्यफलनं च): Stochastic and deterministic policies pi(a | s), the state-value function V^pi(s), the action-value function Q^pi(s, a), the advantage function A^pi(s, a) and the existence of an optimal policy pi^*.*

### श्लोकः 6

```text
नीत्या विधीयते कर्म पदे दृष्टे विचक्षणैः ।
सम्भावेन प्रवृत्ता सा नियता वापि दृश्यते ॥
```

#### IAST Transliteration
*nītyā vidhīyate karma pade dṛṣṭe vicakṣaṇaiḥ |
sambhāvena pravṛttā sā niyatā vāpi dṛśyate ||*

#### English Translation
> Upon perceiving the current state, an action is determined according to the policy; that policy operates stochastically through a probability distribution or deterministically.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **नीत्या** | `नीति` | Noun (feminine) | Instrumental Singular | Instrument: by policy pi |
| **विधीयते** | `विधा` | Verb (passive) | Present 3rd Person Singular | Verb: is determined |
| **कर्म** | `कर्मन्` | Noun (neuter) | Nominative Singular | Subject: action a |
| **पदे** | `पद` | Noun (neuter) | Locative Singular | Locative absolute: state s |
| **दृष्टे** | `दृष्ट` | Past Passive Participle | Locative Singular | Locative absolute: perceived |
| **विचक्षणैः** | `विचक्षण` | Noun (masculine) | Instrumental Plural | Agent: by discerning agents |
| **सम्भावेन** | `सम्भाव` | Noun (masculine) | Instrumental Singular | Manner: stochastically |
| **प्रवृत्ता** | `प्रवृत्त` | Past Passive Participle (feminine) | Nominative Singular | Predicate: operating |
| **सा** | `तद्` | Pronoun (feminine) | Nominative Singular | Subject: that policy pi |
| **नियता** | `नियत` | Adjective (feminine) | Nominative Singular | Alternative predicate: deterministic |
| **वा** | `वा` | Conjunction | Indeclinable | Alternative: or |
| **अपि** | `अपि` | Particle | Indeclinable | Emphatic: also |
| **दृश्यते** | `दृश्` | Verb (passive) | Present 3rd Person Singular | Verb: is observed |

#### Deep Systems & Domain Commentary
A policy pi is the core behavioral mechanism of a reinforcement learning agent. Formally, a policy is a mapping from state space S to action space A. In a deterministic policy, pi: S -> A directly selects action a = pi(s) for every state s. In a stochastic policy, pi(a | s) = Pr(A_t = a | S_t = s) defines a conditional probability distribution over available actions such that sum_{a in A} pi(a | s) = 1. Stochastic policies are critical for exploration, game-theoretic multi-agent settings and policy gradient optimization methods.

---

### श्लोकः 7

```text
पदस्य मूल्यमाख्यातं फलानां योगसञ्चयात् ।
प्रतीक्षा क्रियते नित्यं नीत्या संचलतो मुखे ॥
```

#### IAST Transliteration
*padasya mūlyamākhyātaṃ phalānāṃ yogasañcayāt |
pratīkṣā kriyate nityaṃ nītyā saṃcalato mukhe ||*

#### English Translation
> The state-value function is defined as the expected sum of future cumulative rewards; the statistical expectation is perpetually computed under the agent's operating policy.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **पदस्य** | `पद` | Noun (neuter) | Genitive Singular | Possessive: of state s |
| **मूल्यम्** | `मूल्य` | Noun (neuter) | Nominative Singular | Subject: state-value function V^pi(s) |
| **आख्यातम्** | `आख्यात` | Past Passive Participle | Nominative Singular | Predicate: declared or defined |
| **फलानाम्** | `फल` | Noun (neuter) | Genitive Plural | Possessive: of rewards |
| **योगसञ्चयात्** | `योगसञ्चय` | Noun (masculine) | Ablative Singular | Cause/Source: from cumulative sum of returns G_t |
| **प्रतीक्षा** | `प्रतीक्षा` | Noun (feminine) | Nominative Singular | Subject: mathematical expectation E_pi |
| **क्रियते** | `कृ` | Verb (passive) | Present 3rd Person Singular | Verb: is computed |
| **नित्यम्** | `नित्यम्` | Adverb | Indeclinable | Perpetually: consistently |
| **नीत्या** | `नीति` | Noun (feminine) | Instrumental Singular | Instrument: under policy pi |
| **संचलतः** | `संचलत्` | Present Participle | Genitive Singular | Modifying agent: of the agent moving |
| **मुखे** | `मुख` | Noun (neuter) | Locative Singular | Locus: in the presence or regime |

#### Deep Systems & Domain Commentary
The state-value function V^pi(s) measures how desirable it is for an agent to be in state s under policy pi. Formally, V^pi(s) = E_pi [G_t | S_t = s] = E_pi [sum_{k=0}^infty gamma^k R_{t+k+1} | S_t = s]. It quantifies the long-term expected return starting from state s and following policy pi thereafter. By summarizing the infinite stream of future stochastic rewards into a single scalar value, V^pi(s) allows the agent to evaluate the strategic potential of different states and navigate the environment without exhaustive search.

---

### श्लोकः 8

```text
कर्मणश्च पदस्यापि संयुक्तं मूल्यमुच्यते ।
यदर्थं क्रियते यत्नः श्रेष्ठो मार्गो विविच्यते ॥
```

#### IAST Transliteration
*karmaṇaśca padasyāpi saṃyuktaṃ mūlyamucyate |
yadarthaṃ kriyate yatnaḥ śreṣṭho mārgo vivicyate ||*

#### English Translation
> The joint action-value function unites both state and specific action; through it, optimization effort is exerted and the superior trajectory is distinguished.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **कर्मणः** | `कर्मन्` | Noun (neuter) | Genitive Singular | Possessive: of action a |
| **च** | `च` | Conjunction | Indeclinable | Connecting: and |
| **पदस्य** | `पद` | Noun (neuter) | Genitive Singular | Possessive: of state s |
| **अपि** | `अपि` | Particle | Indeclinable | Emphatic: also |
| **संयुक्तम्** | `संयुक्त` | Past Passive Participle | Nominative Singular | Modifying mūlyam: joint or composite |
| **मूल्यम्** | `मूल्य` | Noun (neuter) | Nominative Singular | Subject: action-value function Q^pi(s, a) |
| **उच्यते** | `वच्` | Verb (passive) | Present 3rd Person Singular | Verb: is declared |
| **यदर्थम्** | `यदर्थम्` | Adverb | Indeclinable | Relative adverb: for the sake of which |
| **क्रियते** | `कृ` | Verb (passive) | Present 3rd Person Singular | Verb: is exerted |
| **यत्नः** | `यत्न` | Noun (masculine) | Nominative Singular | Subject: algorithmic effort |
| **श्रेष्ठः** | `श्रेष्ठ` | Superlative Adjective | Nominative Singular | Modifying mārgaḥ: best or optimal |
| **मार्गः** | `मार्ग` | Noun (masculine) | Nominative Singular | Subject: path or policy |
| **विविच्यते** | `विविच्` | Verb (passive) | Present 3rd Person Singular | Verb: is discerned |

#### Deep Systems & Domain Commentary
The action-value function Q^pi(s, a), commonly termed the Q-function, measures the expected cumulative return starting from state s, executing arbitrary action a and thereafter following policy pi: Q^pi(s, a) = E_pi [G_t | S_t = s, A_t = a] = E_pi [sum_{k=0}^infty gamma^k R_{t+k+1} | S_t = s, A_t = a]. While V^pi(s) assesses states, Q^pi(s, a) directly evaluates individual actions in each state. In model-free reinforcement learning where transition probabilities P(s' | s, a) are unknown, knowing Q^pi(s, a) allows the agent to act greedily without a dynamics model: pi'(s) = argmax_a Q^pi(s, a).

---

### श्लोकः 9

```text
विशेषमूल्यमानेन भेदः स्पष्टः प्रतीयते ।
पदे सामान्यतो यस्मात् कर्म श्रेष्ठं विभाव्यते ॥
```

#### IAST Transliteration
*viśeṣamūlyamānena bhedaḥ spaṣṭaḥ pratīyate |
pade sāmānyato yasmāt karma śreṣṭhaṃ vibhāvyate ||*

#### English Translation
> Through the advantage function, the relative merit is clearly distinguished; it reveals how much superior a specific action is compared to the baseline expectation of that state.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **विशेषमूल्यमानेन** | `विशेषमूल्यमान` | Noun (neuter) | Instrumental Singular | Instrument: by advantage function A^pi(s, a) |
| **भेदः** | `भेद` | Noun (masculine) | Nominative Singular | Subject: relative distinction or advantage |
| **स्पष्टः** | `स्पष्ट` | Past Passive Participle | Nominative Singular | Predicate: distinct or evident |
| **प्रतीयते** | `प्रती` | Verb (passive) | Present 3rd Person Singular | Verb: is perceived |
| **पदे** | `पद` | Noun (neuter) | Locative Singular | Locus: in state s |
| **सामान्यतः** | `सामान्यतः` | Adverb | Indeclinable | Ablative adverb: relative to the baseline expectation V^pi(s) |
| **यस्मात्** | `यद्` | Pronoun | Ablative Singular | Causal: whereby |
| **कर्म** | `कर्मन्` | Noun (neuter) | Nominative Singular | Subject: chosen action a |
| **श्रेष्ठम्** | `श्रेष्ठ` | Superlative Adjective | Nominative Singular | Predicate: superior |
| **विभाव्यते** | `विभा` | Verb (passive) | Present 3rd Person Singular | Verb: is manifested or evaluated |

#### Deep Systems & Domain Commentary
The Advantage function A^pi(s, a) is defined as the difference between the action-value function and the state-value function: A^pi(s, a) = Q^pi(s, a) - V^pi(s). Because V^pi(s) = sum_a pi(a | s) Q^pi(s, a), the state-value V^pi(s) serves as an action-independent baseline representing average performance in state s. If A^pi(s, a) > 0, action a outperforms the policy baseline; if A^pi(s, a) < 0, it yields worse returns than average. Advantage estimation is the cornerstone of actor-critic architectures (A2C, A3C, GAE and PPO), where subtracting the baseline V(s) reduces variance without introducing gradient bias.

---

### श्लोकः 10

```text
अन्विष्यते परा नीतिर्यया सर्वं प्रसाध्यते ।
न तस्याः सदृशी काचिद् फलं प्राप्नोति चोत्तमम् ॥
```

#### IAST Transliteration
*anviṣyate parā nītiryayā sarvaṃ prasādhyate |
na tasyāḥ sadṛśī kācid phalaṃ prāpnoti cottamam ||*

#### English Translation
> The supreme optimal policy is sought, through which all goals are attained; no other policy equals its performance and it achieves the maximum possible return.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **अन्विष्यते** | `अन्विष्` | Verb (passive) | Present 3rd Person Singular | Verb: is sought or optimized |
| **परा** | `पर` | Adjective (feminine) | Nominative Singular | Modifying nītiḥ: supreme or optimal |
| **नीतिः** | `नीति` | Noun (feminine) | Nominative Singular | Subject: optimal policy pi* |
| **यया** | `यद्` | Pronoun (feminine) | Instrumental Singular | Instrument: by which |
| **सर्वम्** | `सर्व` | Noun (neuter) | Nominative Singular | Subject: entire task/reward |
| **प्रसाध्यते** | `प्रसाध्` | Verb (passive) | Present 3rd Person Singular | Verb: is accomplished |
| **न** | `न` | Particle | Indeclinable | Negation: not |
| **तस्याः** | `तद्` | Pronoun (feminine) | Genitive Singular | Possessive: of that optimal policy |
| **सदृशी** | `सदृश्` | Adjective (feminine) | Nominative Singular | Predicate: equal or comparable |
| **काचित्** | `किञ्चित्` | Pronoun (feminine) | Nominative Singular | Subject: any other policy |
| **फलम्** | `फल` | Noun (neuter) | Accusative Singular | Object: cumulative return |
| **प्राप्नोति** | `प्राप्` | Verb | Present 3rd Person Singular | Verb: achieves |
| **च** | `च` | Conjunction | Indeclinable | Connecting particle: and |
| **उत्तमम्** | `उत्तम` | Adjective (neuter) | Accusative Singular | Modifying phalam: maximum or highest |

#### Deep Systems & Domain Commentary
Value functions define a partial ordering over policies: pi >= pi' if and only if V^pi(s) >= V^{pi'}(s) for all states s in S. The fundamental theorem of Markov Decision Processes states that there exists at least one optimal policy pi^* that is better than or equal to all other policies: pi^* >= pi for all pi. The optimal state-value function is V^*(s) = max_pi V^pi(s) and the optimal action-value function is Q^*(s, a) = max_pi Q^pi(s, a). Once Q^*(s, a) is known, an optimal deterministic policy is retrieved by acting greedily: pi^*(s) = argmax_a Q^*(s, a).

---

## सर्गः 3 : बेल्मन्-समीकरणानि (The Bellman Equations: Recursive Decomposition)

*The Bellman Equations (बेल्मन्-समीकरणानि): Recursive expectation decomposition for V^pi and Q^pi, non-linear Bellman optimality equations with max operators, Banach fixed-point contraction mapping and uniqueness of V^*.*

### श्लोकः 11

```text
सद्यः फलं समासाद्य शिष्यते यत् परं पदम् ।
तयोर्योगेन संसिद्धं मूल्यं बेल्मन्वचः स्थितम् ॥
```

#### IAST Transliteration
*sadyaḥ phalaṃ samāsādya śiṣyate yat paraṃ padam |
tayoryogena saṃsiddhaṃ mūlyaṃ belmanvacaḥ sthitam ||*

#### English Translation
> Receiving the immediate reward and adding the discounted value of the successor state: the value function is established recursively through Bellman's equation.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **सद्यः** | `सद्यस्` | Adverb | Indeclinable | Immediately: instantly |
| **फलम्** | `फल` | Noun (neuter) | Accusative Singular | Object of samāsādya: immediate reward R_{t+1} |
| **समासाद्य** | `समासद्` | Gerund (lyap) | Indeclinable | Action: having obtained |
| **शिष्यते** | `शिष्` | Verb (passive) | Present 3rd Person Singular | Verb: remains or follows |
| **यत्** | `यद्` | Pronoun (neuter) | Nominative Singular | Relative: which successor state |
| **परम्** | `पर` | Adjective (neuter) | Nominative Singular | Modifying padam: successor |
| **पदम्** | `पद` | Noun (neuter) | Nominative Singular | Subject: successor state S_{t+1} |
| **तयोः** | `तद्` | Pronoun | Genitive Dual | Possessive: of those two (reward and discounted future) |
| **योगेन** | `योग` | Noun (masculine) | Instrumental Singular | Instrument: by addition |
| **संसिद्धम्** | `संसिद्ध` | Past Passive Participle | Nominative Singular | Predicate: established |
| **मूल्यम्** | `मूल्य` | Noun (neuter) | Nominative Singular | Subject: value function V^pi(s) |
| **बेल्मन्वचः** | `बेल्मन्वचस्` | Noun (neuter) | Nominative Singular | Appositive: Richard Bellman's formulation |
| **स्थितम्** | `स्थित` | Past Passive Participle | Nominative Singular | Predicate: established or abiding |

#### Deep Systems & Domain Commentary
Richard Bellman (1957) formulated the recursive decomposition of value functions that underpins all of dynamic programming and reinforcement learning. The Bellman expectation equation for V^pi decomposes the value of state s into the expected immediate reward plus the discounted value of successor states: V^pi(s) = sum_a pi(a | s) sum_{s', r} P(s', r | s, a) [r + gamma V^pi(s')]. This recursive relationship links the value of a state to the values of its possible future states, transforming a global infinite-horizon sum into local, recursive consistency conditions.

---

### श्लोकः 12

```text
कर्मणः क्रियते रूपं फलं प्राप्य प्रचालिते ।
आगामिन्या च नीत्या तु मूल्यं सम्प्रससार तत् ॥
```

#### IAST Transliteration
*karmaṇaḥ kriyate rūpaṃ phalaṃ prāpya pracālite |
āgāminyā ca nītyā tu mūlyaṃ samprasasāra tat ||*

#### English Translation
> The action-value form is established upon taking an action and obtaining reward; under the subsequent policy, that recursive value propagates across the state space.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **कर्मणः** | `कर्मन्` | Noun (neuter) | Genitive Singular | Possessive: of action a |
| **क्रियते** | `कृ` | Verb (passive) | Present 3rd Person Singular | Verb: is formed |
| **रूपम्** | `रूप` | Noun (neuter) | Nominative Singular | Subject: action-value form Q^pi(s, a) |
| **फलम्** | `फल` | Noun (neuter) | Accusative Singular | Object of prāpya: reward r |
| **प्राप्य** | `प्राप्` | Gerund (lyap) | Indeclinable | Action: having received |
| **प्रचालिते** | `प्रचालित` | Past Passive Participle | Locative Singular | Locative absolute: environment transitioned |
| **आगामिन्या** | `आगामिन्` | Adjective (feminine) | Instrumental Singular | Modifying nītyā: subsequent |
| **च** | `च` | Conjunction | Indeclinable | Connecting: and |
| **नीत्या** | `नीति` | Noun (feminine) | Instrumental Singular | Instrument: under policy pi |
| **तु** | `तु` | Particle | Indeclinable | Emphatic: indeed |
| **मूल्यम्** | `मूल्य` | Noun (neuter) | Nominative Singular | Subject: action-value |
| **सम्प्रससार** | `सम्प्रसृ` | Verb (perfect) | 3rd Person Singular | Verb: propagated or expanded |
| **तत्** | `तद्` | Pronoun (neuter) | Nominative Singular | Modifying mūlyam: that |

#### Deep Systems & Domain Commentary
The Bellman expectation equation for Q^pi(s, a) expresses the action-value recursively: Q^pi(s, a) = sum_{s', r} P(s', r | s, a) [r + gamma sum_{a'} pi(a' | s') Q^pi(s', a')]. Starting from state s and committing to action a, the agent transitions to next state s' with probability P(s' | s, a) and receives reward r. From s' onward, the agent samples subsequent action a' according to policy pi(a' | s'). This recursive equation bridges the gap between state transitions and policy responses, serving as the foundation of SARSA and Expected SARSA.

---

### श्लोकः 13

```text
श्रेष्ठं कर्म समुद्धृत्य यन्मूल्यं प्राप्यते परम् ।
समो न विद्यते कश्चिद् विधानेऽस्मिन् प्रतिष्ठिते ॥
```

#### IAST Transliteration
*śreṣṭhaṃ karma samuddhṛtya yanmūlyaṃ prāpyate param |
samo na vidyate kaścid vidhāne'smin pratiṣṭhite ||*

#### English Translation
> Selecting the optimal action that yields maximum return, the supreme value is attained; no rival equation exists when this optimality formulation is established.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **श्रेष्ठम्** | `श्रेष्ठ` | Superlative Adjective | Accusative Singular | Modifying karma: best or maximizing action |
| **कर्म** | `कर्मन्` | Noun (neuter) | Accusative Singular | Object of samuddhṛtya: action a |
| **समुद्धृत्य** | `समुद्धृ` | Gerund (lyap) | Indeclinable | Action: having selected via max operator |
| **यत्** | `यद्` | Pronoun (neuter) | Nominative Singular | Relative: which |
| **मूल्यम्** | `मूल्य` | Noun (neuter) | Nominative Singular | Subject: optimal value V^*(s) |
| **प्राप्यते** | `प्राप्` | Verb (passive) | Present 3rd Person Singular | Verb: is attained |
| **परम्** | `पर` | Adjective (neuter) | Nominative Singular | Modifying mūlyam: supreme |
| **समः** | `सम` | Adjective (masculine) | Nominative Singular | Predicate: equal or rival |
| **न** | `न` | Particle | Indeclinable | Negation: not |
| **विद्यते** | `विद्` | Verb | Present 3rd Person Singular | Verb: exists |
| **कश्चित्** | `किञ्चित्` | Pronoun (masculine) | Nominative Singular | Subject: any rival |
| **विधाने** | `विधान` | Noun (neuter) | Locative Singular | Locative absolute: Bellman optimality equation |
| **अस्मिन्** | `इदम्` | Pronoun (neuter) | Locative Singular | Modifying vidhāne: in this |
| **प्रतिष्ठिते** | `प्रतिष्ठित` | Past Passive Participle | Locative Singular | Locative absolute: established |

#### Deep Systems & Domain Commentary
The Bellman Optimality Equations eliminate dependence on a specific policy pi by introducing the non-linear max operator: V^*(s) = max_{a in A} sum_{s', r} P(s', r | s, a) [r + gamma V^*(s')] and Q^*(s, a) = sum_{s', r} P(s', r | s, a) [r + gamma max_{a' in A} Q^*(s', a')]. These equations express the fundamental truth of dynamic programming: the value of a state under an optimal policy must equal the expected return from the best action in that state. Unlike the linear Bellman expectation equations, the optimality equations are non-linear due to the max operator, preventing direct matrix inversion.

---

### श्लोकः 14

```text
ह्रासेन बध्यते सर्वं संक्षेपेण प्रसाधिते ।
स्थिरं बिन्दुं समासाद्य न चलत्यग्रतो गतिः ॥
```

#### IAST Transliteration
*hrāsena badhyate sarvaṃ saṃkṣepeṇa prasādhite |
sthirāṃ binduṃ samāsādya na calatyagrato gatiḥ ||*

#### English Translation
> Everything is strictly bound by the discount factor under the contraction mapping; reaching the unique fixed point, the state values cease to fluctuate.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **ह्रासेन** | `ह्रास` | Noun (masculine) | Instrumental Singular | Instrument: by discount factor gamma |
| **बध्यते** | `बन्ध्` | Verb (passive) | Present 3rd Person Singular | Verb: is bound or constrained |
| **सर्वम्** | `सर्व` | Noun (neuter) | Nominative Singular | Subject: value error distance |
| **संक्षेपेण** | `संक्षेप` | Noun (masculine) | Instrumental Singular | Instrument: by contraction mapping operator T |
| **प्रसाधिते** | `प्रसाधित` | Past Passive Participle | Locative Singular | Locative absolute: applied |
| **स्थिरम्** | `स्थिर` | Adjective (masculine) | Accusative Singular | Modifying bindum: stable or fixed |
| **बिन्दुम्** | `बिन्दु` | Noun (masculine) | Accusative Singular | Object of samāsādya: fixed point V^* |
| **समासाद्य** | `समासद्` | Gerund (lyap) | Indeclinable | Action: having reached |
| **न** | `न` | Particle | Indeclinable | Negation: not |
| **चलति** | `चल्` | Verb | Present 3rd Person Singular | Verb: shifts or fluctuates |
| **अग्रतः** | `अग्रतः` | Adverb | Indeclinable | Ablative adverb: further |
| **गतिः** | `गति` | Noun (feminine) | Nominative Singular | Subject: iteration trajectory |

#### Deep Systems & Domain Commentary
The convergence of Bellman iterations is guaranteed by the Banach Fixed-Point Theorem. Defining the Bellman optimality operator T^*: R^{|S|} -> R^{|S|} as (T^* V)(s) = max_a sum_{s', r} P(s', r | s, a) [r + gamma V(s')], one can prove that T^* is a gamma-contraction mapping under the maximum (infinity) norm: ||T^* U - T^* V||_infty <= gamma ||U - V||_infty. Because gamma < 1, repeatedly applying T^* contracts the distance between any two value vectors by at least gamma at each step. This ensures geometric convergence toward a unique fixed point V^* satisfying T^* V^* = V^*.

---

### श्लोकः 15

```text
एकमेव भवेन्मूल्यं न द्वितीयं कदाचन ।
यत्र सर्वाणि वाक्यानि विश्राम्यन्ति समं किल ॥
```

#### IAST Transliteration
*ekameva bhavenmūlyaṃ na dvitīyaṃ kadācana |
yatra sarvāṇi vākyāni viśrāmyanti samaṃ kila ||*

#### English Translation
> There exists exactly one unique optimal value function, never a second; wherein all recursive consistency equations rest in perfect equilibrium.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **एकम्** | `एक` | Adjective (neuter) | Nominative Singular | Modifying mūlyam: single or unique |
| **एव** | `एव` | Particle | Indeclinable | Emphatic: alone |
| **भवेत्** | `भू` | Verb (optative) | 3rd Person Singular | Verb: must be |
| **मूल्यम्** | `मूल्य` | Noun (neuter) | Nominative Singular | Subject: optimal value function V^* |
| **न** | `न` | Particle | Indeclinable | Negation: not |
| **द्वितीयम्** | `द्वितीय` | Ordinal (neuter) | Nominative Singular | Predicate: a second |
| **कदाचन** | `कदाचन` | Adverb | Indeclinable | Temporal: ever |
| **यत्र** | `यत्र` | Adverb | Indeclinable | Relative adverb: wherein |
| **सर्वाणि** | `सर्व` | Adjective (neuter) | Nominative Plural | Modifying vākyāni: all |
| **वाक्यानि** | `वाक्य` | Noun (neuter) | Nominative Plural | Subject: Bellman equations |
| **विश्राम्यन्ति** | `विश्राम्` | Verb | Present 3rd Person Plural | Verb: find rest or converge |
| **समम्** | `समम्` | Adverb | Indeclinable | Harmoniously: equally |
| **किल** | `किल` | Particle | Indeclinable | Emphatic: indeed |

#### Deep Systems & Domain Commentary
The uniqueness of the optimal value function V^*(s) is a fundamental theorem of reinforcement learning. While there may exist multiple distinct optimal policies pi_1^* and pi_2^* (for example, when two actions achieve identical maximal returns in a given state), they all share the exact same unique optimal state-value function V^*(s) and optimal action-value function Q^*(s, a). This uniqueness guarantees that regardless of initial arbitrary value estimates V_0(s), iterative algorithms such as Value Iteration and Q-learning converge asymptotically to the exact same optimal value vector.

---

## सर्गः 4 : गतिकप्रक्रमः (Dynamic Programming: Policy & Value Iteration)

*Dynamic Programming (गतिकप्रक्रमः): Model-based planning requirements, iterative Policy Evaluation, greedy Policy Improvement, Generalized Policy Iteration and single-sweep Value Iteration.*

### श्लोकः 16

```text
ज्ञाते समग्रे संसारे सम्भावे गतिरूपिणि ।
गणनेन विधानेन सर्वं ज्ञातुं प्रयुज्यते ॥
```

#### IAST Transliteration
*jñāte samagre saṃsāre sambhāve gatirūpiṇi |
gaṇanena vidhānena sarvaṃ jñātuṃ prayujyate ||*

#### English Translation
> When the entire environment is known through explicit transition probabilities and dynamics: through dynamic programming methods, complete optimal values are computed.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **ज्ञाते** | `ज्ञात` | Past Passive Participle | Locative Singular | Locative absolute: fully known |
| **समग्रे** | `समग्र` | Adjective | Locative Singular | Modifying saṃsāre: entire |
| **संसारे** | `संसार` | Noun (masculine) | Locative Singular | Locative absolute: environment dynamics model |
| **सम्भावे** | `सम्भाव` | Noun (masculine) | Locative Singular | Modifying gatirūpiṇi: in transition probability P |
| **गतिरूपिणि** | `गतिरूपिन्` | Adjective | Locative Singular | Locative absolute: of dynamic nature |
| **गणनेन** | `गणन` | Noun (neuter) | Instrumental Singular | Instrument: by iterative computation |
| **विधानेन** | `विधान` | Noun (neuter) | Instrumental Singular | Instrument: by dynamic programming methodology |
| **सर्वम्** | `सर्व` | Noun (neuter) | Nominative Singular | Subject: all values and optimal policies |
| **ज्ञातुम्** | `ज्ञा` | Infinitive | Indeclinable | Purpose: to determine or compute |
| **प्रयुज्यते** | `प्रयुज्` | Verb (passive) | Present 3rd Person Singular | Verb: is applied |

#### Deep Systems & Domain Commentary
Dynamic Programming (DP) represents model-based planning in MDPs where the transition dynamics P(s', r | s, a) and reward functions are completely specified. DP uses the Bellman equations as iterative update rules. Because the environment model is known, the agent does not need to physically explore the environment; instead, it performs mathematical backups across all states. While DP provides exact convergence guarantees, its computational complexity of O(|S|^2 |A|) per iteration limits its direct application when the state space S suffers from Bellman's curse of dimensionality.

---

### श्लोकः 17

```text
स्थिरीकरणवेलायां मूल्यं सम्यक् प्रसाध्यते ।
आवर्तनेन चक्रेण यावत् साम्यं प्रजायते ॥
```

#### IAST Transliteration
*sthirīkaraṇavelāyāṃ mūlyaṃ samyak prasādhyate |
āvartanena cakreṇa yāvat sāmyaṃ prajāyate ||*

#### English Translation
> During policy evaluation, the state-value function is accurately solved; through successive iterative cycles until numerical convergence is achieved.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **स्थिरीकरणवेलायाम्** | `स्थिरीकरणवेला` | Noun (feminine) | Locative Singular | Temporal locus: during policy evaluation |
| **मूल्यम्** | `मूल्य` | Noun (neuter) | Nominative Singular | Subject: state-value function V^pi |
| **सम्यक्** | `सम्यक्` | Adverb | Indeclinable | Accurately: thoroughly |
| **प्रसाध्यते** | `प्रसाध्` | Verb (passive) | Present 3rd Person Singular | Verb: is computed or solved |
| **आवर्तनेन** | `आवर्तन` | Noun (neuter) | Instrumental Singular | Instrument: by repeated iteration |
| **चक्रेण** | `चक्र` | Noun (neuter) | Instrumental Singular | Instrument: by backup cycle |
| **यावत्** | `यावत्` | Adverb | Indeclinable | Conjunction: until |
| **साम्यम्** | `साम्य` | Noun (neuter) | Nominative Singular | Subject: convergence delta < theta |
| **प्रजायते** | `प्रजन्` | Verb | Present 3rd Person Singular | Verb: is produced or attained |

#### Deep Systems & Domain Commentary
Policy Evaluation computes the state-value function V^pi for an arbitrary policy pi. Beginning with an arbitrary vector V_0 (e.g. all zeros), the algorithm updates values iteratively using the Bellman expectation equation: V_{k+1}(s) = sum_a pi(a | s) sum_{s', r} P(s', r | s, a) [r + gamma V_k(s')]. In each sweep, every state s in S is updated. The process terminates when the maximum change across all states falls below a small threshold: max_s |V_{k+1}(s) - V_k(s)| < theta. This yields an accurate estimate of V^pi(s) necessary for subsequent policy improvement.

---

### श्लोकः 18

```text
लोभेन कर्मणो रूपं श्रेष्ठं श्रेष्ठं विचीयते ।
पूर्वा नीतिर्विरम्येत नवीना संप्रवर्तते ॥
```

#### IAST Transliteration
*lobhena karmaṇo rūpaṃ śreṣṭhaṃ śreṣṭhaṃ vicīyate |
pūrvā nītirviramyeta navīnā saṃpravartate ||*

#### English Translation
> Acting greedily, the best possible action is selected in every state; the previous policy is superseded and a strictly superior new policy is established.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **लोभेन** | `लोभ` | Noun (masculine) | Instrumental Singular | Manner: greedily via argmax |
| **कर्मणः** | `कर्मन्` | Noun (neuter) | Genitive Singular | Possessive: of action a |
| **रूपम्** | `रूप` | Noun (neuter) | Nominative Singular | Subject: candidate action |
| **श्रेष्ठम्** | `श्रेष्ठ` | Superlative Adjective | Nominative Singular | Predicate: best |
| **श्रेष्ठम्** | `श्रेष्ठ` | Superlative Adjective | Nominative Singular | Repetition: highest-valued |
| **विचीयते** | `विचि` | Verb (passive) | Present 3rd Person Singular | Verb: is selected |
| **पूर्वा** | `पूर्व` | Adjective (feminine) | Nominative Singular | Modifying nītiḥ: previous |
| **नीतिः** | `नीति` | Noun (feminine) | Nominative Singular | Subject: policy pi |
| **विरम्येत** | `विरम्` | Verb (optative) | 3rd Person Singular | Verb: ceases or retires |
| **नवीना** | `नवीन` | Adjective (feminine) | Nominative Singular | Modifying nītiḥ: new policy pi' |
| **संप्रवर्तते** | `संप्रवृत्` | Verb | Present 3rd Person Singular | Verb: is enacted |

#### Deep Systems & Domain Commentary
Policy Improvement uses the evaluated value function V^pi to construct a strictly improved policy pi'. By acting greedily with respect to the action-value function Q^pi(s, a), the new policy is chosen as pi'(s) = argmax_a Q^pi(s, a) = argmax_a sum_{s', r} P(s', r | s, a) [r + gamma V^pi(s')]. According to the Policy Improvement Theorem, if q_pi(s, pi'(s)) >= v_pi(s) for all states s, then the new policy pi' must yield values greater than or equal to pi everywhere: v_{pi'}(s) >= v_pi(s). If pi' equals pi, then both must be optimal policies pi^*.

---

### श्लोकः 19

```text
द्वयोर्युग्मेन संसारे परा काष्ठा प्रपद्यते ।
मूल्येन लभ्यते नीतिर्नीत्या मूल्यं प्रवर्धते ॥
```

#### IAST Transliteration
*dvayoryugmena saṃsāre parā kāṣṭhā prapadyate |
mūlyena labhyate nītirnītyā mūlyaṃ pravardhate ||*

#### English Translation
> Through the coupled interplay of evaluation and improvement, the summit of optimality is reached; from the value function a policy is derived and from that policy values expand.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **द्वयोः** | `द्वि` | Numeral | Genitive Dual | Possessive: of the two (evaluation and improvement) |
| **युग्मेन** | `युग्म` | Noun (neuter) | Instrumental Singular | Instrument: by the coupled cycle (Policy Iteration) |
| **संसारे** | `संसार` | Noun (masculine) | Locative Singular | Locus: in the MDP domain |
| **परा** | `पर` | Adjective (feminine) | Nominative Singular | Modifying kāṣṭhā: supreme |
| **काष्ठा** | `काष्ठा` | Noun (feminine) | Nominative Singular | Subject: summit or optimality pi^* |
| **प्रपद्यते** | `प्रपद्` | Verb | Present 3rd Person Singular | Verb: is attained |
| **मूल्येन** | `मूल्य` | Noun (neuter) | Instrumental Singular | Instrument: from value V |
| **लभ्यते** | `लभ्` | Verb (passive) | Present 3rd Person Singular | Verb: is obtained |
| **नीतिः** | `नीति` | Noun (feminine) | Nominative Singular | Subject: policy pi |
| **नीत्या** | `नीति` | Noun (feminine) | Instrumental Singular | Instrument: by policy pi |
| **मूल्यम्** | `मूल्य` | Noun (neuter) | Nominative Singular | Subject: value function |
| **प्रवर्धते** | `प्रवृध्` | Verb | Present 3rd Person Singular | Verb: grows or improves |

#### Deep Systems & Domain Commentary
Generalized Policy Iteration (GPI) formalizes the interplay between policy evaluation and policy improvement. In Policy Iteration, the algorithm alternates between full policy evaluation (evaluating V^pi until convergence) and greedy policy improvement (extracting pi' = greedy(V^pi)). Because a finite MDP has only |A|^{|S|} distinct deterministic policies and each improvement strictly increases return unless the policy is already optimal, Policy Iteration is guaranteed to converge to the exact optimal policy pi^* in a finite number of iterations.

---

### श्लोकः 20

```text
एकेनैव विधानेन श्रेष्ठं मूल्यं विभाव्यते ।
न पृथक् क्रियते मार्गः क्षिप्रं सिद्धिः प्रजायते ॥
```

#### IAST Transliteration
*ekenaiva vidhānena śreṣṭhaṃ mūlyaṃ vibhāvyate |
na pṛthak kriyate mārgaḥ kṣipraṃ siddhiḥ prajāyate ||*

#### English Translation
> Through a single combined formulation, optimal values are directly discerned; evaluation and improvement are not separated and rapid convergence is achieved.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **एकेन** | `एक` | Numeral | Instrumental Singular | Modifying vidhānena: by a single |
| **एव** | `एव` | Particle | Indeclinable | Emphatic: alone |
| **विधानेन** | `विधान` | Noun (neuter) | Instrumental Singular | Instrument: by algorithm (Value Iteration) |
| **श्रेष्ठम्** | `श्रेष्ठ` | Superlative Adjective | Nominative Singular | Modifying mūlyam: optimal |
| **मूल्यम्** | `मूल्य` | Noun (neuter) | Nominative Singular | Subject: optimal value function V^* |
| **विभाव्यते** | `विभा` | Verb (passive) | Present 3rd Person Singular | Verb: is computed |
| **न** | `न` | Particle | Indeclinable | Negation: not |
| **पृथक्** | `पृथक्` | Adverb | Indeclinable | Separately: independently |
| **क्रियते** | `कृ` | Verb (passive) | Present 3rd Person Singular | Verb: is done |
| **मार्गः** | `मार्ग` | Noun (masculine) | Nominative Singular | Subject: pathway or policy loop |
| **क्षिप्रम्** | `क्षिप्रम्` | Adverb | Indeclinable | Rapidly: swiftly |
| **सिद्धिः** | `सिद्धि` | Noun (feminine) | Nominative Singular | Subject: convergence to V^* |
| **प्रजायते** | `प्रजन्` | Verb | Present 3rd Person Singular | Verb: is produced |

#### Deep Systems & Domain Commentary
Value Iteration streamlines Generalized Policy Iteration by truncating policy evaluation after exactly one sweep. Instead of waiting for V^pi to converge, Value Iteration directly updates state values using the Bellman Optimality Equation: V_{k+1}(s) = max_{a in A} sum_{s', r} P(s', r | s, a) [r + gamma V_k(s')]. This combines evaluation and improvement into a single backup operation. Value Iteration avoids the expensive inner convergence loops of Policy Iteration, achieving geometric convergence toward V^*(s) in O(|S| |A|) operations per sweep.

---

## सर्गः 5 : मान्टे-कार्लो-पद्धतिः (Monte Carlo Methods: Model-Free Learning)

*Monte Carlo Methods (मान्टे-कार्लो-पद्धतिः): Model-free learning from episodic experience, first-visit vs every-visit estimators, zero-bias high-variance trade-offs, epsilon-greedy exploration and off-policy importance sampling.*

### श्लोकः 21

```text
अज्ञातेऽपि च संसारे केवलं चरितैः पदम् ।
अनुभूतेः प्रभावेण मूल्यं लब्धुं प्रयुज्यते ॥
```

#### IAST Transliteration
*ajñāte'pi ca saṃsāre kevalaṃ caritaiḥ padam |
anubhūteḥ prabhāveṇa mūlyaṃ labdhuṃ prayujyate ||*

#### English Translation
> Even when the environment dynamics are completely unknown, state values are determined through sampled episodes alone; through empirical experience, values are acquired.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **अज्ञाते** | `अज्ञात` | Past Passive Participle | Locative Singular | Locative absolute: unknown |
| **अपि** | `अपि` | Particle | Indeclinable | Even: although |
| **च** | `च` | Conjunction | Indeclinable | Connecting: and |
| **संसारे** | `संसार` | Noun (masculine) | Locative Singular | Locative absolute: environment model |
| **केवलम्** | `केवलम्` | Adverb | Indeclinable | Exclusively: solely |
| **चरितैः** | `चरित` | Noun (neuter) | Instrumental Plural | Instrument: by sampled episodes or trajectories |
| **पदम्** | `पद` | Noun (neuter) | Nominative Singular | Subject: state value |
| **अनुभूतेः** | `अनुभूति` | Noun (feminine) | Genitive Singular | Possessive: of empirical experience |
| **प्रभावेण** | `प्रभाव` | Noun (masculine) | Instrumental Singular | Instrument: by the power |
| **मूल्यम्** | `मूल्य` | Noun (neuter) | Accusative Singular | Object: value function |
| **लब्धुम्** | `लभ्` | Infinitive | Indeclinable | Purpose: to acquire |
| **प्रयुज्यते** | `प्रयुज्` | Verb (passive) | Present 3rd Person Singular | Verb: is applied |

#### Deep Systems & Domain Commentary
Monte Carlo methods liberate reinforcement learning from the requirement of a prior environment model. Unlike dynamic programming, which requires explicit knowledge of transition probabilities P(s' | s, a) and reward functions, Monte Carlo methods learn directly from sampled episodes of experience: S_0, A_0, R_1, S_1, A_1, R_2, ..., S_T. By averaging the empirical returns observed after visiting a state across multiple episodes, Monte Carlo methods estimate expected values non-parametrically based solely on actual environmental interactions.

---

### श्लोकः 22

```text
आद्येन वा समाघाते सर्वैर्वा गणिते फलम् ।
मध्यमाने समासाद्य समत्वं सम्प्रपद्यते ॥
```

#### IAST Transliteration
*ādyena vā samāghāte sarvairvā gaṇite phalam |
madhyamāne samāsādya samatvaṃ samprapadyate ||*

#### English Translation
> Whether computed on the first occurrence of a state or across every visit, returns are recorded; converging upon the sample average, true expected value is attained.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **आद्येन** | `आद्य` | Ordinal | Instrumental Singular | Instrument: by first-visit Monte Carlo |
| **वा** | `वा` | Conjunction | Indeclinable | Alternative: or |
| **समाघाते** | `समाघात` | Noun (masculine) | Locative Singular | Locus: upon state visit |
| **सर्वैः** | `सर्व` | Adjective | Instrumental Plural | Instrument: by every-visit Monte Carlo |
| **वा** | `वा` | Conjunction | Indeclinable | Alternative: or |
| **गणिते** | `गणित` | Past Passive Participle | Locative Singular | Locative absolute: computed |
| **फलम्** | `फल` | Noun (neuter) | Nominative Singular | Subject: sample return G_t |
| **मध्यमाने** | `मध्यमान` | Noun (neuter) | Locative Singular | Locus: in sample average |
| **समासाद्य** | `समासद्` | Gerund (lyap) | Indeclinable | Action: having attained |
| **समत्वम्** | `समत्व` | Noun (neuter) | Accusative Singular | Goal: true expectation V^pi(s) |
| **सम्प्रपद्यते** | `सम्प्रपद्` | Verb | Present 3rd Person Singular | Verb: attains or converges |

#### Deep Systems & Domain Commentary
Monte Carlo estimation comes in two primary variants. In First-Visit Monte Carlo, the return G_t is recorded only for the first time state s is encountered within an episode and the value V(s) is estimated as the sample average of these first-visit returns across episodes. In Every-Visit Monte Carlo, returns following every visit to s within an episode are averaged. By the Law of Large Numbers, both estimators converge asymptotically to true value V^pi(s) as the number of visits approaches infinity, with First-Visit providing an unbiased estimate.

---

### श्लोकः 23

```text
न पक्षपातो दृश्येत चाञ्चल्यं बहु वर्तते ।
सम्पूर्णे चरितस्यान्ते गणना सम्प्रवर्तते ॥
```

#### IAST Transliteration
*na pakṣapāto dṛśyeta cāñcalyaṃ bahu vartate |
sampūrṇe caritasyānte gaṇanā sampravartate ||*

#### English Translation
> No algorithmic bias is present, yet high variance exists; computations can commence only upon the full termination of an entire episode.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **न** | `न` | Particle | Indeclinable | Negation: not |
| **पक्षपातः** | `पक्षपात` | Noun (masculine) | Nominative Singular | Subject: estimation bias |
| **दृश्येत** | `दृश्` | Verb (optative) | 3rd Person Singular | Verb: is seen |
| **चाञ्चल्यम्** | `चाञ्चल्य` | Noun (neuter) | Nominative Singular | Subject: sample variance |
| **बहु** | `बहु` | Adverb | Indeclinable | High: substantial |
| **वर्तते** | `वृत्` | Verb | Present 3rd Person Singular | Verb: exists |
| **सम्पूर्णे** | `सम्पूर्ण` | Past Passive Participle | Locative Singular | Modifying caritasyānte: completed |
| **चरितस्य** | `चरित` | Noun (neuter) | Genitive Singular | Possessive: of the episode |
| **अन्ते** | `अन्त` | Noun (masculine) | Locative Singular | Locative absolute: at the termination |
| **गणना** | `गणना` | Noun (feminine) | Nominative Singular | Subject: value update computation |
| **सम्प्रवर्तते** | `सम्प्रवृत्` | Verb | Present 3rd Person Singular | Verb: commences |

#### Deep Systems & Domain Commentary
Monte Carlo methods possess distinct statistical properties. Because G_t is an actual observed trajectory return without bootstrapping from other value estimates, E[G_t | S_t = s] = V^pi(s), meaning Monte Carlo estimates have zero bias. However, because return G_t accumulates stochasticity across many random transitions and actions from step t to termination T, its sample variance is high, necessitating many episodes to converge. Furthermore, Monte Carlo methods cannot be applied online or to continuing (infinite-horizon) tasks because updates require waiting for episode completion.

---

### श्लोकः 24

```text
अन्वेषणं च भोगांशो द्वयं साम्येन रक्ष्यते ।
कदाचिन्मार्गभेदः स्यात् कदाचित् स्वीकृतं परम् ॥
```

#### IAST Transliteration
*anveṣaṇaṃ ca bhogāṃśo dvayaṃ sāmyena rakṣyate |
kadācinmārgabhedaḥ syāt kadācit svīkṛtaṃ param ||*

#### English Translation
> Exploration and exploitation are maintained in careful balance; occasionally, an exploratory deviation is taken, while otherwise the best known action is chosen.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **अन्वेषणम्** | `अन्वेषण` | Noun (neuter) | Nominative Singular | Subject 1: exploration |
| **च** | `च` | Conjunction | Indeclinable | Connecting: and |
| **भोगांशः** | `भोगांश` | Noun (masculine) | Nominative Singular | Subject 2: exploitation of current best |
| **द्वयम्** | `द्वय` | Noun (neuter) | Nominative Singular | Subject: the duality |
| **साम्येन** | `साम्य` | Noun (neuter) | Instrumental Singular | Manner: in balanced equilibrium |
| **रक्ष्यते** | `रक्ष्` | Verb (passive) | Present 3rd Person Singular | Verb: is maintained |
| **कदाचित्** | `कदाचित्` | Adverb | Indeclinable | Occasionally: with probability epsilon |
| **मार्गभेदः** | `मार्गभेद` | Noun (masculine) | Nominative Singular | Subject: exploratory action selection |
| **स्यात्** | `अस्` | Verb (optative) | 3rd Person Singular | Verb: occurs |
| **कदाचित्** | `कदाचित्` | Adverb | Indeclinable | Otherwise: with probability 1 - epsilon |
| **स्वीकृतम्** | `स्वीकृत` | Past Passive Participle | Nominative Singular | Predicate: accepted or chosen |
| **परम्** | `पर` | Adjective (neuter) | Nominative Singular | Modifying action: greedy best |

#### Deep Systems & Domain Commentary
The Exploration-Exploitation Dilemma is the defining trade-off in reinforcement learning. An agent that only exploits its current knowledge (acting greedily with respect to current Q-values) risks getting trapped in suboptimal local minima because better alternative actions remain unexplored. Conversely, an agent that only explores gains negligible cumulative reward. The canonical resolution is the epsilon-greedy policy: with probability 1 - epsilon, the agent exploits by selecting argmax_a Q(s, a); with probability epsilon, it explores by choosing an action uniformly at random from A, ensuring all state-action pairs continue to be visited.

---

### श्लोकः 25

```text
अन्यथा चरतो मार्गात् ज्ञायते यत् परं पदम् ।
भारभेदेन संशुद्धं सत्यमेव प्रकाशते ॥
```

#### IAST Transliteration
*anyathā carato mārgāt jñāyate yat paraṃ padam |
bhārabhedena saṃśuddhaṃ satyameva prakāśate ||*

#### English Translation
> When learning an optimal policy from trajectories generated by a differing behavior policy: corrected by importance sampling ratios, true expected values are revealed.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **अन्यथा** | `अन्यथा` | Adverb | Indeclinable | Differently: under exploratory behavior policy b |
| **चरतः** | `चरत्` | Present Participle | Genitive Singular | Modifying mārgāt: moving |
| **मार्गात्** | `मार्ग` | Noun (masculine) | Ablative Singular | Source: from behavior trajectory |
| **ज्ञायते** | `ज्ञा` | Verb (passive) | Present 3rd Person Singular | Verb: is evaluated |
| **यत्** | `यद्` | Pronoun (neuter) | Nominative Singular | Relative: which target policy pi |
| **परम्** | `पर` | Adjective (neuter) | Nominative Singular | Modifying padam: optimal target |
| **पदम्** | `पद` | Noun (neuter) | Nominative Singular | Subject: target policy state value |
| **भारभेदेन** | `भारभेद` | Noun (masculine) | Instrumental Singular | Instrument: by importance sampling ratio rho |
| **संशुद्धम्** | `संशुद्ध` | Past Passive Participle | Nominative Singular | Predicate: re-weighted or corrected |
| **सत्यम्** | `सत्य` | Noun (neuter) | Nominative Singular | Subject: true target value |
| **एव** | `एव` | Particle | Indeclinable | Emphatic: alone |
| **प्रकाशते** | `प्रकाश्` | Verb | Present 3rd Person Singular | Verb: shines or manifests |

#### Deep Systems & Domain Commentary
Off-Policy Learning decouples the target policy pi (the policy being learned and optimized) from the behavior policy b (the exploratory policy used to generate trajectory data). This allows the agent to evaluate or optimize an optimal deterministic policy while continuing to explore via an exploratory stochastic policy. In off-policy Monte Carlo, importance sampling corrects for the discrepancy between probability distributions. The importance sampling ratio rho_{t:T-1} = prod_{k=t}^{T-1} (pi(A_k | S_k) / b(A_k | S_k)) reweights returns G_t such that E_b [rho G_t] = E_pi [G_t], providing an unbiased estimate of target policy value.

---

## सर्गः 6 : कालभेदशिक्षणम् (Temporal Difference Learning: TD(0) & SARSA)

*Temporal Difference Learning (कालभेदशिक्षणम्): Bootstrapping from successor value estimates before termination, the fundamental TD error delta_t as dopaminergic teaching signal, low variance online updates and the on-policy SARSA algorithm.*

### श्लोकः 26

```text
असमाप्तेऽपि चरित्रे पदान्तरसमाश्रयात् ।
मूल्यस्य शोधनं नित्यं क्रियते कालभेदतः ॥
```

#### IAST Transliteration
*asamāpte'pi caritre padāntarasamāśrayāt |
mūlyasya śodhanaṃ nityaṃ kriyate kālabhedataḥ ||*

#### English Translation
> Even before an episode reaches completion, relying upon the estimated value of the successor state: the value function is perpetually updated via temporal difference bootstrapping.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **असमाप्ते** | `असमाप्त` | Past Passive Participle | Locative Singular | Locative absolute: uncompleted |
| **अपि** | `अपि` | Particle | Indeclinable | Even: although |
| **चरित्रे** | `चरित्र` | Noun (neuter) | Locative Singular | Locative absolute: in the episode |
| **पदान्तरसमाश्रयात्** | `पदान्तरसमाश्रय` | Noun (masculine) | Ablative Singular | Cause: from relying on successor state estimate V(S_{t+1}) |
| **मूल्यस्य** | `मूल्य` | Noun (neuter) | Genitive Singular | Possessive: of the value function |
| **शोधनम्** | `शोधन` | Noun (neuter) | Nominative Singular | Subject: update or refinement |
| **नित्यम्** | `नित्यम्` | Adverb | Indeclinable | Perpetually: online |
| **क्रियते** | `कृ` | Verb (passive) | Present 3rd Person Singular | Verb: is performed |
| **कालभेदतः** | `कालभेद` | Noun (masculine) | Ablative Singular (tas-suffix) | Ablative: by temporal difference TD(0) |

#### Deep Systems & Domain Commentary
Temporal Difference (TD) learning, introduced by Richard Sutton (1988), represents the central idea of modern reinforcement learning. TD learning combines the model-free sampling of Monte Carlo methods with the bootstrapping mechanism of dynamic programming. Instead of waiting until episode termination to record empirical return G_t, a TD(0) agent updates its estimate of V(S_t) immediately upon observing next state S_{t+1} and reward R_{t+1}: V(S_t) <- V(S_t) + alpha [R_{t+1} + gamma V(S_{t+1}) - V(S_t)]. The quantity R_{t+1} + gamma V(S_{t+1}) serves as an estimated target, bootstrapping from existing value estimates.

---

### श्लोकः 27

```text
प्राप्तेन फलयोगेन पदान्तरगुणेन च ।
यन्मूल्यं हीयते पूर्वं दोषस्तेन प्रकाश्यते ॥
```

#### IAST Transliteration
*prāptena phalayogena padāntaraguṇena ca |
yanmūlyaṃ hīyate pūrvaṃ doṣastena prakāśyate ||*

#### English Translation
> Combining the received reward with the discounted value of the next state: subtracting the prior estimated value, the temporal difference prediction error is revealed.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **प्राप्तेन** | `प्राप्त` | Past Passive Participle | Instrumental Singular | Modifying phalayogena: received |
| **फलयोगेन** | `फलयोग` | Noun (masculine) | Instrumental Singular | Instrument: by immediate reward R_{t+1} |
| **पदान्तरगुणेन** | `पदान्तरगुण` | Noun (masculine) | Instrumental Singular | Instrument: by discounted next state value gamma V(S_{t+1}) |
| **च** | `च` | Conjunction | Indeclinable | Connecting: and |
| **यत्** | `यद्` | Pronoun (neuter) | Nominative Singular | Relative: which |
| **मूल्यम्** | `मूल्य` | Noun (neuter) | Nominative Singular | Subject: prior value V(S_t) |
| **हीयते** | `हा` | Verb (passive) | Present 3rd Person Singular | Verb: is subtracted |
| **पूर्वम्** | `पूर्व` | Adverb | Indeclinable | Temporal: previously |
| **दोषः** | `दोष` | Noun (masculine) | Nominative Singular | Subject: TD error delta_t |
| **तेन** | `तद्` | Pronoun (neuter) | Instrumental Singular | Instrument: thereby |
| **प्रकाश्यते** | `प्रकाश्` | Verb (passive) | Present 3rd Person Singular | Verb: is illuminated or measured |

#### Deep Systems & Domain Commentary
The Temporal Difference error delta_t = R_{t+1} + gamma V(S_{t+1}) - V(S_t) is the fundamental scalar teaching signal in reinforcement learning. It measures the discrepancy between the expected value V(S_t) at time t and the updated estimate formed at time t+1 after experiencing transition (S_t, A_t, R_{t+1}, S_{t+1}). Neurobiologists Wolfram Schultz, Peter Dayan and P. Read Montague famously proved that dopamine neurons in the primate striatum encode precisely this TD prediction error delta_t, firing intensely when rewards exceed expectation and dropping below baseline when expected rewards fail to materialize.

---

### श्लोकः 28

```text
चाञ्चल्यं न भवेद् गाढं क्षिप्रं ज्ञानं प्रजायते ।
पदे पदे कृते कर्म साक्षाद् गतिर्विधीयते ॥
```

#### IAST Transliteration
*cāñcalyaṃ na bhaved gāḍhaṃ kṣipraṃ jñānaṃ prajāyate |
pade pade kṛte karma sākṣād gatirvidhīyate ||*

#### English Translation
> Sample variance is not excessive and knowledge is acquired swiftly; step by step as each action is executed, learning updates proceed online.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **चाञ्चल्यम्** | `चाञ्चल्य` | Noun (neuter) | Nominative Singular | Subject: variance |
| **न** | `न` | Particle | Indeclinable | Negation: not |
| **भवेत्** | `भू` | Verb (optative) | 3rd Person Singular | Verb: occurs |
| **गाढम्** | `गाढ` | Adjective (neuter) | Nominative Singular | Predicate: extreme or severe |
| **क्षिप्रम्** | `क्षिप्रम्` | Adverb | Indeclinable | Rapidly: swiftly |
| **ज्ञानम्** | `ज्ञान` | Noun (neuter) | Nominative Singular | Subject: learned policy/value |
| **प्रजायते** | `प्रजन्` | Verb | Present 3rd Person Singular | Verb: is generated |
| **पदे** | `पद` | Noun (neuter) | Locative Singular | Repetition: at each step |
| **पदे** | `पद` | Noun (neuter) | Locative Singular | Repetition: step by step |
| **कृते** | `कृत` | Past Passive Participle | Locative Singular | Locative absolute: executed |
| **कर्म** | `कर्मन्` | Noun (neuter) | Locative Singular | Locative absolute: action |
| **साक्षात्** | `साक्षात्` | Adverb | Indeclinable | Directly: online |
| **गतिः** | `गति` | Noun (feminine) | Nominative Singular | Subject: update trajectory |
| **विधीयते** | `विधा` | Verb (passive) | Present 3rd Person Singular | Verb: is enacted |

#### Deep Systems & Domain Commentary
TD(0) exhibits substantially lower variance than Monte Carlo methods. While Monte Carlo return G_t accumulates the randomness of every state transition, reward and action until episode termination T, the TD target R_{t+1} + gamma V(S_{t+1}) depends only on the single next transition (S_t, A_t, R_{t+1}, S_{t+1}). While the TD target introduces slight bias initially (because V(S_{t+1}) is an imperfect estimate), its lower variance enables significantly faster learning in practice. Furthermore, TD methods operate fully online and apply seamlessly to continuing tasks without artificial episode boundaries.

---

### श्लोकः 29

```text
पदेन कर्मणा युक्तं फलं लब्ध्वा परं पदम् ।
तत्रत्यं कर्म चादाय सार्सानीतिः प्रवर्धते ॥
```

#### IAST Transliteration
*padena karmaṇā yuktaṃ phalaṃ labdhvā paraṃ padam |
tatratyaṃ karma cādāya sārsānītiḥ pravardhate ||*

#### English Translation
> Starting from state and action, receiving reward and reaching the next state: sampling the subsequent action taken there, the SARSA on-policy algorithm advances.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **पदेन** | `पद` | Noun (neuter) | Instrumental Singular | Instrument: state S_t |
| **कर्मणा** | `कर्मन्` | Noun (neuter) | Instrumental Singular | Instrument: action A_t |
| **युक्तम्** | `युक्त` | Past Passive Participle | Accusative Singular | Modifying state-action pair |
| **फलम्** | `फल` | Noun (neuter) | Accusative Singular | Object of labdhvā: reward R_{t+1} |
| **लब्ध्वा** | `लभ्` | Gerund (ktvā) | Indeclinable | Action: having received |
| **परम्** | `पर` | Adjective (neuter) | Accusative Singular | Modifying padam: next |
| **पदम्** | `पद` | Noun (neuter) | Accusative Singular | Object: successor state S_{t+1} |
| **तत्रत्यम्** | `तत्रत्य` | Adjective (neuter) | Accusative Singular | Modifying karma: existing there |
| **कर्म** | `कर्मन्` | Noun (neuter) | Accusative Singular | Object of ādāya: next action A_{t+1} |
| **च** | `च` | Conjunction | Indeclinable | Connecting: and |
| **आदाय** | `आदा` | Gerund (lyap) | Indeclinable | Action: having sampled |
| **सार्सानीतिः** | `सार्सानीति` | Noun (feminine) | Nominative Singular | Subject: SARSA algorithm (State-Action-Reward-State-Action) |
| **प्रवर्धते** | `प्रवृध्` | Verb | Present 3rd Person Singular | Verb: progresses or learns |

#### Deep Systems & Domain Commentary
SARSA (State-Action-Reward-State-Action), named by Rich Sutton, is the quintessential on-policy Temporal Difference control algorithm. Given current transition tuple (S_t, A_t, R_{t+1}, S_{t+1}, A_{t+1}), SARSA updates its action-value function via: Q(S_t, A_t) <- Q(S_t, A_t) + alpha [R_{t+1} + gamma Q(S_{t+1}, A_{t+1}) - Q(S_t, A_t)]. Because it updates Q(S_t, A_t) using the action A_{t+1} actually selected by the current behavioral policy (e.g. epsilon-greedy), SARSA is strictly on-policy. In environments with dangerous cliffs or penalty states, SARSA learns cautious policies that account for the agent's exploratory missteps.

---

### श्लोकः 30

```text
अन्वेषणे क्षयं याते नीतौ लोभमुपागते ।
सर्वं समाप्यते सम्यक् सत्यं प्रतिष्ठितं भवेत् ॥
```

#### IAST Transliteration
*anveṣaṇe kṣayaṃ yāte nītau lobhamupāgate |
sarvaṃ samāpyate samyak satyaṃ pratiṣṭhitaṃ bhavet ||*

#### English Translation
> As exploration gradually decays and the policy approaches pure greedy exploitation: the values converge completely and the optimal policy is established.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **अन्वेषणे** | `अन्वेषण` | Noun (neuter) | Locative Singular | Locative absolute: exploration rate epsilon |
| **क्षयम्** | `क्षय` | Noun (masculine) | Accusative Singular | Goal of yāte: decay or zero |
| **याते** | `यात` | Past Passive Participle | Locative Singular | Locative absolute: having attained |
| **नीतौ** | `नीति` | Noun (feminine) | Locative Singular | Locative absolute: policy |
| **लोभम्** | `लोभ` | Noun (masculine) | Accusative Singular | Goal: greedy exploitation |
| **उपागते** | `उपागत` | Past Passive Participle | Locative Singular | Locative absolute: having approached |
| **सर्वम्** | `सर्व` | Noun (neuter) | Nominative Singular | Subject: all Q-values |
| **समाप्यते** | `समाप्` | Verb (passive) | Present 3rd Person Singular | Verb: converges |
| **सम्यक्** | `सम्यक्` | Adverb | Indeclinable | Thoroughly: definitively |
| **सत्यम्** | `सत्य` | Noun (neuter) | Nominative Singular | Subject: optimal policy Q^* |
| **प्रतिष्ठितम्** | `प्रतिष्ठित` | Past Passive Participle | Nominative Singular | Predicate: established |
| **भवेत्** | `भू` | Verb (optative) | 3rd Person Singular | Verb: becomes or remains |

#### Deep Systems & Domain Commentary
Singh et al. (2000) proved the convergence of on-policy SARSA to the optimal action-value function Q^* under GLIE (Greedy in the Limit with Infinite Exploration) conditions. A learning policy is GLIE if: (1) all state-action pairs are visited infinitely often: lim_{t->infty} N_t(s, a) = infty and (2) the policy converges in the limit to the greedy policy: lim_{t->infty} pi_t(a | s) = 1 for a = argmax Q(s, a) (for example, setting epsilon_t = 1/t). When combined with standard Robbins-Monro learning rate decay conditions (sum alpha_t = infty, sum alpha_t^2 < infty), SARSA converges with probability 1 to Q^*(s, a).

---

## सर्गः 7 : क्यू-शिक्षणम् (Q-Learning: Off-Policy TD Control)

*Q-Learning (क्यू-शिक्षणम्): Watkins' 1989 off-policy TD control breakthrough, the Q-learning update rule with max target, decoupling exploratory behavior from optimal policy convergence, Double Q-learning and eligibility traces TD(lambda).*

### श्लोकः 31

```text
अपृष्ट्वापि गतां नीतिं श्रेष्ठं मानं विचीयते ।
वाट्किन्सेन कृतं शास्त्रं कर्ममूल्यप्रसाधकम् ॥
```

#### IAST Transliteration
*apṛṣṭvāpi gatāṃ nītiṃ śreṣṭhaṃ mānaṃ vicīyate |
vāṭkinsena kṛtaṃ śāstraṃ karmamūlyaprasādhakam ||*

#### English Translation
> Without querying the actual subsequent policy choice, the optimal action value is directly extracted; Christopher Watkins created this algorithm for computing action values.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **अपृष्ट्वा** | `प्रच्छ्` | Gerund (ktvā with a-prefix) | Indeclinable | Action: without asking or consulting A_{t+1} |
| **अपि** | `अपि` | Particle | Indeclinable | Even: although |
| **गताम्** | `गत` | Past Passive Participle (feminine) | Accusative Singular | Modifying nītim: taken or executed |
| **नीतिम्** | `नीति` | Noun (feminine) | Accusative Singular | Object of apṛṣṭvā: behavior policy |
| **श्रेष्ठम्** | `श्रेष्ठ` | Superlative Adjective | Accusative Singular | Modifying mānam: maximal |
| **मानम्** | `मान` | Noun (neuter) | Accusative Singular | Object: optimal target value max Q(S_{t+1}, a') |
| **विचीयते** | `विचि` | Verb (passive) | Present 3rd Person Singular | Verb: is selected |
| **वाट्किन्सेन** | `वाट्किन्स` | Noun (masculine) | Instrumental Singular | Agent: by Christopher Watkins (1989) |
| **कृतम्** | `कृत` | Past Passive Participle | Nominative Singular | Predicate: formulated |
| **शास्त्रम्** | `शास्त्र` | Noun (neuter) | Nominative Singular | Subject: Q-learning algorithm |
| **कर्ममूल्यप्रसाधकम्** | `कर्ममूल्यप्रसाधक` | Adjective (neuter) | Nominative Singular | Modifying śāstram: establishing action-values Q^* |

#### Deep Systems & Domain Commentary
Q-Learning, formulated by Christopher Watkins in his 1989 PhD dissertation, is one of the most celebrated breakthroughs in artificial intelligence. Q-Learning is an off-policy Temporal Difference control algorithm that learns the optimal action-value function Q^*(s, a) directly, independent of the behavioral policy being followed by the agent. While SARSA updates toward the value of the action actually taken A_{t+1}, Q-Learning updates toward the maximum possible value achievable in the next state max_{a'} Q(S_{t+1}, a'), eliminating importance sampling requirements.

---

### श्लोकः 32

```text
आगामिनि पदे श्रेष्ठं कर्म यत् सम्प्रदृश्यते ।
तन्मानमाहृत्य सम्यक् पूर्वं संशोध्यते पदम् ॥
```

#### IAST Transliteration
*āgāmini pade śreṣṭhaṃ karma yat sampradṛśyate |
tanmānamāhṛtya samyak pūrvaṃ saṃśodhyate padam ||*

#### English Translation
> Taking the highest action value apparent in the successor state: adopting that maximum target, the prior state-action value is refined.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **आगामिनि** | `आगामिन्` | Adjective | Locative Singular | Modifying pade: successor |
| **पदे** | `पद` | Noun (neuter) | Locative Singular | Locus: in next state S_{t+1} |
| **श्रेष्ठम्** | `श्रेष्ठ` | Superlative Adjective | Nominative Singular | Modifying karma: best |
| **कर्म** | `कर्मन्` | Noun (neuter) | Nominative Singular | Subject: maximizing action a' |
| **यत्** | `यद्` | Pronoun (neuter) | Nominative Singular | Relative: which |
| **सम्प्रदृश्यते** | `सम्प्रदृश्` | Verb (passive) | Present 3rd Person Singular | Verb: is seen |
| **तन्मानम्** | `तन्मान` | Noun (neuter) | Accusative Singular | Object of āhṛtya: max_{a'} Q(S_{t+1}, a') |
| **आहृत्य** | `आहृ` | Gerund (lyap) | Indeclinable | Action: having adopted |
| **सम्यक्** | `सम्यक्` | Adverb | Indeclinable | Accurately: thoroughly |
| **पूर्वम्** | `पूर्व` | Adjective (neuter) | Nominative Singular | Modifying padam: prior |
| **संशोध्यते** | `संशोध्` | Verb (passive) | Present 3rd Person Singular | Verb: is updated |
| **पदम्** | `पद` | Noun (neuter) | Nominative Singular | Subject: previous Q(S_t, A_t) |

#### Deep Systems & Domain Commentary
The canonical Q-Learning update rule is: Q(S_t, A_t) <- Q(S_t, A_t) + alpha [R_{t+1} + gamma max_{a' in A} Q(S_{t+1}, a') - Q(S_t, A_t)]. The target of the update is R_{t+1} + gamma max_{a'} Q(S_{t+1}, a'), which directly approximates the right-hand side of the Bellman Optimality Equation. Tsitsiklis (1994) and Jaakkola et al. (1994) proved that as long as every state-action pair (s, a) continues to be visited and the learning rate satisfies Robbins-Monro conditions, Q(s, a) converges with probability 1 to the unique optimal action-value function Q^*(s, a).

---

### श्लोकः 33

```text
यथेच्छं चरति क्वापि लक्ष्यं श्रेष्ठं विभाव्यते ।
पृथग्भूते प्रवृत्ते तु संसिद्धिर्न निषिध्यते ॥
```

#### IAST Transliteration
*yathecchaṃ carati kvāpi lakṣyaṃ śreṣṭhaṃ vibhāvyate |
pṛthagbhūte pravṛtte tu saṃsiddhirna niṣidhyate ||*

#### English Translation
> The agent may wander arbitrarily according to an exploratory policy, yet the supreme target is evaluated; when behavior and target are decoupled, optimal convergence is unhindered.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **यथेच्छम्** | `यथेच्छम्` | Adverb | Indeclinable | Manner: as desired or exploratorily |
| **चरति** | `चर्` | Verb | Present 3rd Person Singular | Verb: moves or acts |
| **क्वापि** | `क्वापि` | Adverb | Indeclinable | Anywhere: throughout the state space |
| **लक्ष्यम्** | `लक्ष्य` | Noun (neuter) | Nominative Singular | Subject: target policy / Q^* |
| **श्रेष्ठम्** | `श्रेष्ठ` | Superlative Adjective | Nominative Singular | Modifying lakṣyam: optimal |
| **विभाव्यते** | `विभा` | Verb (passive) | Present 3rd Person Singular | Verb: is learned or estimated |
| **पृथग्भूते** | `पृथग्भूत` | Past Passive Participle | Locative Singular | Locative absolute: decoupled |
| **प्रवृत्ते** | `प्रवृत्त` | Noun (neuter) | Locative Singular | Locative absolute: in behavior |
| **तु** | `तु` | Particle | Indeclinable | Emphatic: indeed |
| **संसिद्धिः** | `संसिद्धि` | Noun (feminine) | Nominative Singular | Subject: convergence to Q^* |
| **न** | `न` | Particle | Indeclinable | Negation: not |
| **निषिध्यते** | `निषिध्` | Verb (passive) | Present 3rd Person Singular | Verb: is obstructed or prevented |

#### Deep Systems & Domain Commentary
The off-policy nature of Q-Learning provides tremendous architectural flexibility. An agent can explore via an epsilon-greedy policy, a Boltzmann softmax distribution or even completely random exploratory noise, while its Q-table converges to the greedy optimal policy pi^*(s) = argmax_a Q^*(s, a). Furthermore, Q-Learning can learn from offline demonstration datasets, past human trajectories or replay memory generated by earlier, suboptimal iterations of the agent. This capability forms the bedrock of offline reinforcement learning and experience replay buffers in modern deep RL.

---

### श्लोकः 34

```text
लोभाधिक्येन दोषः स्यान्मूल्यवृद्धिः प्रजायते ।
द्विधा विभज्य तन्मानं दोषशान्तिर्विधीयते ॥
```

#### IAST Transliteration
*lobhādhikyena doṣaḥ syānmūlyavṛddhiḥ prajāyate |
dvidhā vibhajya tanmānaṃ doṣaśāntirvidhīyate ||*

#### English Translation
> Due to excessive maximization, an estimation error occurs and values become systematically inflated; splitting the estimation into two independent estimators, this bias is neutralized.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **लोभाधिक्येन** | `लोभाधिक्य` | Noun (neuter) | Instrumental Singular | Cause: by greedy maximization bias E[max(X, Y)] >= max(E[X], E[Y]) |
| **दोषः** | `दोष` | Noun (masculine) | Nominative Singular | Subject: overestimation bias |
| **स्यात्** | `अस्` | Verb (optative) | 3rd Person Singular | Verb: occurs |
| **मूल्यवृद्धिः** | `मूल्यवृद्धि` | Noun (feminine) | Nominative Singular | Subject: value inflation |
| **प्रजायते** | `प्रजन्` | Verb | Present 3rd Person Singular | Verb: is produced |
| **द्विधा** | `द्विधा` | Adverb | Indeclinable | Manner: into two estimators Q_A and Q_B |
| **विभज्य** | `विभज्` | Gerund (lyap) | Indeclinable | Action: having decoupled (Double Q-learning) |
| **तन्मानम्** | `तन्मान` | Noun (neuter) | Accusative Singular | Object: that action evaluation |
| **दोषशान्तिः** | `दोषशान्ति` | Noun (feminine) | Nominative Singular | Subject: bias mitigation |
| **विधीयते** | `विधा` | Verb (passive) | Present 3rd Person Singular | Verb: is accomplished |

#### Deep Systems & Domain Commentary
Maximization bias is a subtle statistical defect in standard Q-Learning. Because E[max(X_1, X_2)] >= max(E[X_1], E[X_2]), using the max operator over noisy value estimates systematically overestimates action values, often causing the agent to prefer noisy suboptimal actions over stable optimal ones. Hado van Hasselt (2010) resolved this with Double Q-Learning. By maintaining two independent value estimators Q_A and Q_B, one network selects the greedy action: a^* = argmax_a Q_A(S_{t+1}, a), while the second network evaluates that action's value: Q_B(S_{t+1}, a^*). Decoupling action selection from action evaluation mathematically eliminates overestimation bias.

---

### श्लोकः 35

```text
स्मृतिचिह्नेन सम्बन्धात् सेतुर्भवति शोभनः ।
कालभेदस्य योगेन चरितं सङ्गतं भवेत् ॥
```

#### IAST Transliteration
*smṛticihnena sambandhāt seturbhavati śobhanaḥ |
kālabhedasya yogena caritaṃ saṅgataṃ bhavet ||*

#### English Translation
> Connected through eligibility traces, an elegant bridge is constructed; uniting temporal difference with trajectory history, the credit assignment becomes harmonious.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **स्मृतिचिह्नेन** | `स्मृतिचिह्न` | Noun (neuter) | Instrumental Singular | Instrument: by eligibility trace e_t(s, a) |
| **सम्बन्धात्** | `सम्बन्ध` | Noun (masculine) | Ablative Singular | Cause: from connection |
| **सेतुः** | `सेतु` | Noun (masculine) | Nominative Singular | Subject: bridge unifying TD and Monte Carlo |
| **भवति** | `भू` | Verb | Present 3rd Person Singular | Verb: becomes |
| **शोभनः** | `शोभन` | Adjective (masculine) | Nominative Singular | Modifying setuḥ: elegant |
| **कालभेदस्य** | `कालभेद` | Noun (masculine) | Genitive Singular | Possessive: of temporal difference |
| **योगेन** | `योग` | Noun (masculine) | Instrumental Singular | Instrument: by synthesis |
| **चरितम्** | `चरित` | Noun (neuter) | Nominative Singular | Subject: episodic return credit |
| **सङ्गतम्** | `सङ्गत` | Past Passive Participle | Nominative Singular | Predicate: unified or harmonized |
| **भवेत्** | `भू` | Verb (optative) | 3rd Person Singular | Verb: becomes |

#### Deep Systems & Domain Commentary
Eligibility traces and the TD(lambda) mechanism establish a mathematical bridge between single-step TD(0) and infinite-step Monte Carlo learning. An eligibility trace e_t(s) is an internal memory variable that records recent state visits: e_t(s) = gamma lambda e_{t-1}(s) + 1(S_t = s). When a TD error delta_t occurs, all states are updated proportionally to their trace: Delta V(s) = alpha delta_t e_t(s). Setting lambda = 0 yields standard one-step TD(0); setting lambda = 1 reproduces offline Monte Carlo. Intermediate values of lambda in (0, 1) accelerate credit assignment across past states without requiring explicit trajectory storage.

---

## सर्गः 8 : फलनसन्निकर्षः गभीर-क्यू-जालं च (Function Approximation & Deep Q-Networks)

*Function Approximation & Deep Q-Networks (फलनसन्निकर्षः गभीर-क्यू-जालं च): The curse of dimensionality in continuous state spaces, linear semi-gradients, the Deadly Triad divergence pathology, Deep Q-Networks (DQN) and stabilization via Experience Replay and Target Networks.*

### श्लोकः 36

```text
अनन्ते तु स्थिते क्षेत्रे न कोष्ठे लभ्यते पदम् ।
फलनस्य समाश्रित्य सन्निकर्षः प्रयुज्यते ॥
```

#### IAST Transliteration
*anante tu sthite kṣetre na koṣṭhe labhyate padam |
phalanasya samāśritya sannikarṣaḥ prayujyate ||*

#### English Translation
> In an infinite, continuous state space, states cannot be cataloged in a tabular lookup; resorting to function approximation, parameterized generalization is employed.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **अनन्ते** | `अनन्त` | Adjective | Locative Singular | Modifying kṣetre: infinite |
| **तु** | `तु` | Particle | Indeclinable | Contrastive: however |
| **स्थिते** | `स्थित` | Past Passive Participle | Locative Singular | Locative absolute: situated |
| **क्षेत्रे** | `क्षेत्र` | Noun (neuter) | Locative Singular | Locative absolute: in continuous state space S |
| **न** | `न` | Particle | Indeclinable | Negation: not |
| **कोष्ठे** | `कोष्ठ` | Noun (masculine) | Locative Singular | Locus: in a discrete lookup table / Q-table |
| **लभ्यते** | `लभ्` | Verb (passive) | Present 3rd Person Singular | Verb: is accommodated |
| **पदम्** | `पद` | Noun (neuter) | Nominative Singular | Subject: state value representation |
| **फलनस्य** | `फलन` | Noun (neuter) | Genitive Singular | Possessive: of mathematical function |
| **समाश्रित्य** | `समाश्रि` | Gerund (lyap) | Indeclinable | Action: having relied upon |
| **सन्निकर्षः** | `सन्निकर्ष` | Noun (masculine) | Nominative Singular | Subject: function approximation v_hat(s, w) |
| **प्रयुज्यते** | `प्रयुज्` | Verb (passive) | Present 3rd Person Singular | Verb: is applied |

#### Deep Systems & Domain Commentary
Tabular reinforcement learning assumes discrete state and action spaces where every Q(s, a) can be indexed in memory. In real-world domains (robotics, autonomous driving, Go, video games), state spaces are continuous or astronomical: an Atari screen possesses 256^{210 x 160 x 3} possible pixel configurations. Tabular indexing fails completely due to memory exhaustion and zero generalization to unseen states. Function approximation replaces tables with parameterized function approximators v_hat(s, w) approx V(s) or q_hat(s, a, w) approx Q(s, a), transferring learned knowledge across geometrically similar regions of state space.

---

### श्लोकः 37

```text
गुणैर्युक्तैः पदैर्गुण्यैर्मूल्यं सम्परिकल्प्यते ।
प्रवणेन विधानेन भारभेदः प्रशस्यते ॥
```

#### IAST Transliteration
*guṇairyuktaiḥ padairguṇyairmūlyaṃ samparikalpyate |
pravaṇena vidhānena bhārabhedaḥ praśasyate ||*

#### English Translation
> Values are approximated as the inner product of feature vectors and weight parameters; through gradient descent methods, parameter weight adjustments are celebrated.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **गुणैः** | `गुण` | Noun (masculine) | Instrumental Plural | Instrument: by weights w_i |
| **युक्तैः** | `युक्त` | Past Passive Participle | Instrumental Plural | Modifying padaiḥ: combined |
| **पदैः** | `पद` | Noun (neuter) | Instrumental Plural | Instrument: by state features x_i(s) |
| **गुण्यैः** | `गुण्य` | Adjective | Instrumental Plural | Modifying padaiḥ: multiplicable |
| **मूल्यम्** | `मूल्य` | Noun (neuter) | Nominative Singular | Subject: approximate value v_hat(s, w) = w^T x(s) |
| **सम्परिकल्प्यते** | `सम्परिकॢप्` | Verb (passive) | Present 3rd Person Singular | Verb: is formulated |
| **प्रवणेन** | `प्रवण` | Noun (neuter) | Instrumental Singular | Instrument: by gradient descent nabla_w |
| **विधानेन** | `विधान` | Noun (neuter) | Instrumental Singular | Instrument: by semi-gradient algorithm |
| **भारभेदः** | `भारभेद` | Noun (masculine) | Nominative Singular | Subject: weight vector update Delta w |
| **प्रशस्यते** | `प्रशंस्` | Verb (passive) | Present 3rd Person Singular | Verb: is praised |

#### Deep Systems & Domain Commentary
In linear function approximation, state values are modeled as the inner product of a fixed feature representation x(s) and a learnable weight vector w in R^d: v_hat(s, w) = w^T x(s) = sum_{i=1}^d w_i x_i(s). The weights are updated via semi-gradient descent on Mean Squared Value Error: Delta w = alpha [U_t - v_hat(S_t, w)] nabla_w v_hat(S_t, w) = alpha delta_t x(S_t). Here U_t is the update target (such as the TD target R_{t+1} + gamma v_hat(S_{t+1}, w)). The gradient does not backpropagate through the target's dependence on w, making it a semi-gradient method with proven linear convergence under on-policy sampling.

---

### श्लोकः 38

```text
त्रिविधे संप्लुते दोषाद् भङ्गो भवति दारुणः ।
अनीत्या चानुमानेन सन्निकर्षेण संभवेत् ॥
```

#### IAST Transliteration
*trividhe saṃplute doṣād bhaṅgo bhavati dāruṇaḥ |
anītyā cānumānena sannikarṣeṇa sambhavet ||*

#### English Translation
> When the threefold combination coalesces, catastrophic divergence occurs: arising from off-policy learning, bootstrapping and function approximation.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **त्रिविधे** | `त्रिविध` | Adjective | Locative Singular | Locative absolute: threefold combination (The Deadly Triad) |
| **संप्लुते** | `संप्लुत` | Past Passive Participle | Locative Singular | Locative absolute: united |
| **दोषात्** | `दोष` | Noun (masculine) | Ablative Singular | Cause: from algorithmic defect |
| **भङ्गः** | `भङ्ग` | Noun (masculine) | Nominative Singular | Subject: catastrophic divergence |
| **भवति** | `भू` | Verb | Present 3rd Person Singular | Verb: occurs |
| **दारुणः** | `दारुण` | Adjective (masculine) | Nominative Singular | Modifying bhaṅgaḥ: severe |
| **अनीत्या** | `अनीति` | Noun (feminine) | Instrumental Singular | Factor 1: off-policy training |
| **च** | `च` | Conjunction | Indeclinable | Connecting: and |
| **अनुमानेन** | `अनुमान` | Noun (neuter) | Instrumental Singular | Factor 2: bootstrapping (updating from successor estimates) |
| **सन्निकर्षेण** | `सन्निकर्ष` | Noun (masculine) | Instrumental Singular | Factor 3: function approximation |
| **संभवेत्** | `संभू` | Verb (optative) | 3rd Person Singular | Verb: is generated |

#### Deep Systems & Domain Commentary
Richard Sutton identified 'The Deadly Triad': the dangerous confluence of (1) Function Approximation (generalizing across states via neural networks), (2) Bootstrapping (updating estimates toward targets containing downstream estimates, as in TD and Bellman equations) and (3) Off-Policy Training (evaluating a target policy using data generated by a different behavior distribution). When all three conditions are present simultaneously, the contraction mapping property of Bellman operators breaks down under projected norms. Value estimates can diverge to positive or negative infinity (e.g. Baird's counterexample), destabilizing training.

---

### श्लोकः 39

```text
गभीरेण च जालेन बुद्धिर्भवति विस्मया ।
चित्रं दृष्ट्वा परं कर्म साक्षादेव प्रसाध्यते ॥
```

#### IAST Transliteration
*gabhīreṇa ca jālena buddhirbhavati vismayā |
citraṃ dṛṣṭvā paraṃ karma sākṣādeva prasādhyate ||*

#### English Translation
> Empowered by deep neural networks, marvelous artificial intelligence emerges; perceiving raw visual pixels directly, optimal action decisions are achieved.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **गभीरेण** | `गभीर` | Adjective | Instrumental Singular | Modifying jālena: deep |
| **च** | `च` | Conjunction | Indeclinable | Connecting: and |
| **जालेन** | `जाल` | Noun (neuter) | Instrumental Singular | Instrument: by deep neural network |
| **बुद्धिः** | `बुद्धि` | Noun (feminine) | Nominative Singular | Subject: artificial intelligence |
| **भवति** | `भू` | Verb | Present 3rd Person Singular | Verb: becomes |
| **विस्मया** | `विस्मय` | Adjective (feminine) | Nominative Singular | Predicate: astounding |
| **चित्रम्** | `चित्र` | Noun (neuter) | Accusative Singular | Object of dṛṣṭvā: raw visual frames/images |
| **दृष्ट्वा** | `दृश्` | Gerund (ktvā) | Indeclinable | Action: having perceived |
| **परम्** | `पर` | Adjective (neuter) | Nominative Singular | Modifying karma: optimal |
| **कर्म** | `कर्मन्` | Noun (neuter) | Nominative Singular | Subject: control action |
| **साक्षात्** | `साक्षात्` | Adverb | Indeclinable | Directly: end-to-end |
| **एव** | `एव` | Particle | Indeclinable | Emphatic: indeed |
| **प्रसाध्यते** | `प्रसाध्` | Verb (passive) | Present 3rd Person Singular | Verb: is accomplished |

#### Deep Systems & Domain Commentary
Deep Q-Networks (DQN), introduced by Volodymyr Mnih et al. at DeepMind (2015), achieved human-level control across 49 Atari 2600 games directly from raw visual pixels. Prior RL systems relied on handcrafted domain-specific features. DQN utilized a deep convolutional neural network Q(s, a; theta) parameterized by weights theta to map raw 84x84 pixel frames directly to discrete controller actions. By marrying end-to-end deep representation learning with reinforcement learning, DQN demonstrated that artificial agents could discover visual abstractions and long-horizon strategies autonomously from scratch.

---

### श्लोकः 40

```text
स्मृतेः सञ्चययोगेन लक्ष्यजालेन रक्षणे ।
स्थिरत्वं लभते यन्त्रं चला बुद्धिर्न बाध्यते ॥
```

#### IAST Transliteration
*smṛteḥ sañcayayogena lakṣyajālena rakṣaṇe |
sthiratvaṃ labhate yantraṃ calā buddhirna bādhyate ||*

#### English Translation
> Through experience replay memory and safeguarding with a separate target network: the machine attains numerical stability and shifting value estimates no longer destabilize training.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **स्मृतेः** | `स्मृति` | Noun (feminine) | Genitive Singular | Possessive: of past experience |
| **सञ्चययोगेन** | `सञ्चययोग` | Noun (masculine) | Instrumental Singular | Instrument: by experience replay buffer D |
| **लक्ष्यजालेन** | `लक्ष्यजाल` | Noun (neuter) | Instrumental Singular | Instrument: by target network Q(s, a; theta^-) |
| **रक्षणे** | `रक्षण` | Noun (neuter) | Locative Singular | Locus: in stabilization |
| **स्थिरत्वम्** | `स्थिरत्व` | Noun (neuter) | Accusative Singular | Object: numerical stability |
| **लभते** | `लभ्` | Verb | Present 3rd Person Singular | Verb: attains |
| **यन्त्रम्** | `यन्त्र` | Noun (neuter) | Nominative Singular | Subject: DQN learning agent |
| **चला** | `चल` | Adjective (feminine) | Nominative Singular | Modifying buddhiḥ: fluctuating |
| **बुद्धिः** | `बुद्धि` | Noun (feminine) | Nominative Singular | Subject: learned policy |
| **न** | `न` | Particle | Indeclinable | Negation: not |
| **बाध्यते** | `बाध्` | Verb (passive) | Present 3rd Person Singular | Verb: is obstructed or diverged |

#### Deep Systems & Domain Commentary
DQN conquered the Deadly Triad through two architectural innovations: (1) Experience Replay Buffer: transitions (s_t, a_t, r_{t+1}, s_{t+1}) are stored in a rolling buffer D and mini-batches are sampled uniformly at random. This breaks temporal autocorrelation between consecutive video frames and restores the i.i.d. assumption necessary for gradient stability. (2) Target Network: the parameters theta^- of the target network are held frozen for C steps, computing target y_i = r + gamma max_{a'} Q(s', a'; theta^-), while the online network weights theta are updated via gradient descent. This eliminates the moving-target problem, preventing feedback loops.

---

## सर्गः 9 : नीतिक्रमप्रवणता (Policy Gradient Methods & Actor-Critic)

*Policy Gradient Methods & Actor-Critic (नीतिक्रमप्रवणता): Direct policy optimization, the Policy Gradient Theorem, REINFORCE score-function updates, variance reduction through baseline subtraction and Actor-Critic dual-network synergy.*

### श्लोकः 41

```text
मूल्यमार्गं परित्यज्य साक्षाद् नीतिर्विधीयते ।
गुणैर्युक्ता परा रीतिः क्रमेणैव विवर्धते ॥
```

#### IAST Transliteration
*mūlyamārgaṃ parityajya sākṣād nītirvidhīyate |
guṇairyuktā parā rītiḥ krameṇaiva vivardhate ||*

#### English Translation
> Setting aside intermediate value lookups, the policy is parameterized directly; endowed with differentiable weights, the supreme behavioral strategy is iteratively improved.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **मूल्यमार्गम्** | `मूल्यमार्ग` | Noun (masculine) | Accusative Singular | Object of parityajya: intermediate value-based detour |
| **परित्यज्य** | `परित्यज्` | Gerund (lyap) | Indeclinable | Action: having set aside |
| **साक्षात्** | `साक्षात्` | Adverb | Indeclinable | Directly: end-to-end |
| **नीतिः** | `नीति` | Noun (feminine) | Nominative Singular | Subject: parameterized policy pi_theta(a | s) |
| **विधीयते** | `विधा` | Verb (passive) | Present 3rd Person Singular | Verb: is optimized |
| **गुणैः** | `गुण` | Noun (masculine) | Instrumental Plural | Instrument: by policy parameters theta |
| **युक्ता** | `युक्त` | Past Passive Participle (feminine) | Nominative Singular | Modifying rītiḥ: equipped |
| **परा** | `पर` | Adjective (feminine) | Nominative Singular | Modifying rītiḥ: supreme |
| **रीतिः** | `रीति` | Noun (feminine) | Nominative Singular | Subject: behavioral method |
| **क्रमेण** | `क्रम` | Noun (masculine) | Instrumental Singular | Manner: iteratively / gradually |
| **एव** | `एव` | Particle | Indeclinable | Emphatic: indeed |
| **विवर्धते** | `विवृध्` | Verb | Present 3rd Person Singular | Verb: ascends or improves |

#### Deep Systems & Domain Commentary
Policy Gradient methods bypass value function inversion by parameterizing the policy directly as pi_theta(a | s) using a differentiable neural network with weights theta in R^d. In value-based methods (like Q-learning), a small change in Q-values can abruptly cause an action to switch from probability 0 to 1, causing oscillatory instability. In contrast, policy gradient methods smoothly adjust action probabilities across continuous iterations, natively handle high-dimensional and continuous action spaces (e.g. robotic torques) and naturally represent stochastic optimal policies in partial-information settings.

---

### श्लोकः 42

```text
प्रवणं नीतितत्त्वस्य कर्ममूल्येन गुण्यते ।
सम्भावेन विधानेन वृद्धिर्भवति शाश्वती ॥
```

#### IAST Transliteration
*pravaṇaṃ nītitattvasya karmamūlyena guṇyate |
sambhāvena vidhānena vṛddhirbhavati śāśvatī ||*

#### English Translation
> The gradient of log-policy probability is multiplied by the action-value; under expectation over state distribution, perpetual policy improvement is assured.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **प्रवणम्** | `प्रवण` | Noun (neuter) | Nominative Singular | Subject: score function gradient nabla_theta log pi_theta(a | s) |
| **नीतितत्त्वस्य** | `नीतितत्त्व` | Noun (neuter) | Genitive Singular | Possessive: of the policy |
| **कर्ममूल्येन** | `कर्ममूल्य` | Noun (neuter) | Instrumental Singular | Instrument: by action value Q^pi(s, a) |
| **गुण्यते** | `गुण्` | Verb (passive) | Present 3rd Person Singular | Verb: is multiplied |
| **सम्भावेन** | `सम्भाव` | Noun (masculine) | Instrumental Singular | Instrument: by state-distribution expectation E_pi |
| **विधानेन** | `विधान` | Noun (neuter) | Instrumental Singular | Instrument: by gradient ascent rule |
| **वृद्धिः** | `वृद्धि` | Noun (feminine) | Nominative Singular | Subject: objective increase Delta J(theta) >= 0 |
| **भवति** | `भू` | Verb | Present 3rd Person Singular | Verb: becomes or occurs |
| **शाश्वती** | `शाश्वत` | Adjective (feminine) | Nominative Singular | Predicate: continuous or guaranteed |

#### Deep Systems & Domain Commentary
The Policy Gradient Theorem, proved by Richard Sutton et al. (1999), provides an exact analytical expression for the gradient of expected cumulative return J(theta) = E_{s ~ d^pi, a ~ pi}[R] without requiring derivatives of the unknown state transition distribution d^pi(s): nabla_theta J(theta) = E_{s ~ d^pi, a ~ pi_theta} [nabla_theta log pi_theta(a | s) Q^pi(s, a)]. The term nabla_theta log pi_theta(a | s) is the score function, indicating the parameter direction that increases the probability of action a in state s. Multiplying by Q^pi(s, a) reinforces good actions and suppresses bad ones.

---

### श्लोकः 43

```text
सम्पूर्णे चरितस्यान्ते फलेन गुण्यते गतिः ।
विन्मतेन सुसिद्धोऽयं विधिर्नीतिप्रसाधकः ॥
```

#### IAST Transliteration
*sampūrṇe caritasyānte phalena guṇyate gatiḥ |
vinmatena susiddho'yaṃ vidhirnītiprasādhakaḥ ||*

#### English Translation
> At the complete conclusion of an episode, the score gradient is multiplied by the observed return; Ronald Williams established this celebrated REINFORCE algorithm.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **सम्पूर्णे** | `सम्पूर्ण` | Past Passive Participle | Locative Singular | Modifying caritasyānte: completed |
| **चरितस्य** | `चरित` | Noun (neuter) | Genitive Singular | Possessive: of the episode |
| **अन्ते** | `अन्त` | Noun (masculine) | Locative Singular | Locative absolute: at termination T |
| **फलेन** | `फल` | Noun (neuter) | Instrumental Singular | Instrument: by empirical return G_t |
| **गुण्यते** | `गुण्` | Verb (passive) | Present 3rd Person Singular | Verb: is scaled |
| **गतिः** | `गति` | Noun (feminine) | Nominative Singular | Subject: gradient update vector |
| **विन्मतेन** | `विन्मत` | Noun (neuter) | Instrumental Singular | Agent: by Ronald Williams' formulation (1992) |
| **सुसिद्धः** | `सुसिद्ध` | Past Passive Participle | Nominative Singular | Predicate: celebrated or established |
| **अयम्** | `इदम्` | Pronoun (masculine) | Nominative Singular | Modifying vidhiḥ: this |
| **विधिः** | `विधि` | Noun (masculine) | Nominative Singular | Subject: REINFORCE algorithm |
| **नीतिप्रसाधकः** | `नीतिप्रसाधक` | Adjective (masculine) | Nominative Singular | Modifying vidhiḥ: optimizing policy |

#### Deep Systems & Domain Commentary
The REINFORCE algorithm (Williams, 1992) is the foundational Monte Carlo policy gradient method. Because the true action-value Q^pi(s, a) is unknown, REINFORCE replaces Q(S_t, A_t) with the actual realized episodic sample return G_t: theta <- theta + alpha sum_{t=0}^{T-1} nabla_theta log pi_theta(A_t | S_t) G_t. Because E[G_t | S_t, A_t] = Q^pi(S_t, A_t), the update is an unbiased estimator of the true policy gradient. However, because G_t accumulates stochasticity across the entire episode, REINFORCE suffers from high variance, requiring large batch sizes to learn stably.

---

### श्लोकः 44

```text
मध्यमाने विहीने तु चाञ्चल्यं विनिवार्यते ।
न पक्षपातो दृश्येत शुद्धा नीतिः प्रकाशते ॥
```

#### IAST Transliteration
*madhyamāne vihīne tu cāñcalyaṃ vinivāryate |
na pakṣapāto dṛśyeta śuddhā nītiḥ prakāśate ||*

#### English Translation
> Subtracting an action-independent baseline from the return, high gradient variance is dramatically reduced; no estimation bias is introduced and pristine policy learning shines.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **मध्यमाने** | `मध्यमान` | Noun (neuter) | Locative Singular | Locative absolute: baseline b(s) / V(s) |
| **विहीने** | `विहीन` | Past Passive Participle | Locative Singular | Locative absolute: subtracted |
| **तु** | `तु` | Particle | Indeclinable | Emphatic: indeed |
| **चाञ्चल्यम्** | `चाञ्चल्य` | Noun (neuter) | Nominative Singular | Subject: gradient variance |
| **विनिवार्यते** | `विनिवृ` | Verb (passive) | Present 3rd Person Singular | Verb: is mitigated |
| **न** | `न` | Particle | Indeclinable | Negation: not |
| **पक्षपातः** | `पक्षपात` | Noun (masculine) | Nominative Singular | Subject: gradient bias |
| **दृश्येत** | `दृश्` | Verb (optative) | 3rd Person Singular | Verb: is observed |
| **शुद्धा** | `शुद्ध` | Adjective (feminine) | Nominative Singular | Modifying nītiḥ: pure or stable |
| **नीतिः** | `नीति` | Noun (feminine) | Nominative Singular | Subject: policy |
| **प्रकाशते** | `प्रकाश्` | Verb | Present 3rd Person Singular | Verb: shines or manifests |

#### Deep Systems & Domain Commentary
Baseline subtraction is a powerful variance reduction technique in policy gradient methods. The policy gradient theorem permits subtracting any arbitrary baseline b(s) that does not depend on action a: nabla_theta J(theta) = E [nabla_theta log pi_theta(a | s) (Q(s, a) - b(s))]. The expected value of the baseline gradient vanishes identically: sum_a nabla pi_theta(a | s) b(s) = b(s) nabla (sum_a pi_theta(a | s)) = b(s) nabla (1) = 0. Therefore, setting the baseline to the state-value function b(s) = V(s) leaves the gradient completely unbiased while replacing Q(s, a) with the Advantage function A(s, a) = Q(s, a) - V(s), drastically slashing variance.

---

### श्लोकः 45

```text
कर्ता करोति कर्माणि समीक्षकः प्रपश्यति ।
द्वयोर्योगेन संसारे महती सिद्धिरीक्ष्यते ॥
```

#### IAST Transliteration
*kartā karoti karmāṇi samīkṣakaḥ prapaśyati |
dvayoryogena saṃsāre mahatī siddhirīkṣyate ||*

#### English Translation
> The Actor executes actions according to policy, while the Critic evaluates performance and judges value; through the union of both, supreme mastery is observed.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **कर्ता** | `कर्तृ` | Noun (masculine) | Nominative Singular | Subject 1: Actor network pi_theta(a | s) |
| **करोति** | `कृ` | Verb | Present 3rd Person Singular | Verb: performs or executes |
| **कर्माणि** | `कर्मन्` | Noun (neuter) | Accusative Plural | Object: actions |
| **समीक्षकः** | `समीक्षक` | Noun (masculine) | Nominative Singular | Subject 2: Critic network V_phi(s) |
| **प्रपश्यति** | `प्रदृश्` | Verb | Present 3rd Person Singular | Verb: evaluates or observes |
| **द्वयोः** | `द्वि` | Numeral | Genitive Dual | Possessive: of the two networks |
| **योगेन** | `योग` | Noun (masculine) | Instrumental Singular | Instrument: by harmonious union (Actor-Critic) |
| **संसारे** | `संसार` | Noun (masculine) | Locative Singular | Locus: in the complex environment |
| **महती** | `महत्` | Adjective (feminine) | Nominative Singular | Modifying siddhiḥ: immense |
| **सिद्धिः** | `सिद्धि` | Noun (feminine) | Nominative Singular | Subject: algorithmic success / convergence |
| **ईक्ष्यते** | `ईक्ष्` | Verb (passive) | Present 3rd Person Singular | Verb: is witnessed |

#### Deep Systems & Domain Commentary
Actor-Critic architectures synthesize policy-based and value-based reinforcement learning. The Actor is a parameterized policy pi_theta(a | s) responsible for selecting continuous or discrete actions. The Critic is a parameterized value function V_phi(s) responsible for evaluating state quality and computing the TD error delta_t = R_{t+1} + gamma V_phi(S_{t+1}) - V_phi(S_t). The TD error acts as the Critic's critique: if delta_t > 0, the action outperformed expectations, so the Actor adjusts theta to increase its probability; if delta_t < 0, probability is decreased. Critic bootstrapping enables online, low-variance updates without waiting for episode termination.

---

## सर्गः 10 : प्रगतविधानानि महासंश्लेषश्च (Advanced Architectures & Grand Synthesis)

*Advanced Architectures & Grand Synthesis (प्रगतविधानानि महासंश्लेषश्च): Trust-region clipping via Proximal Policy Optimization (PPO), Model-Based Dyna planning, AlphaZero self-play with Monte Carlo Tree Search, RLHF alignment for language models and philosophical synthesis of karma, value and consciousness.*

### श्लोकः 46

```text
सीमाबन्धेन संशुद्धा न नीतिर्भ्रश्यते पथात् ।
लघुना च विधानेन स्थिरता समुपस्थिता ॥
```

#### IAST Transliteration
*sīmābandhena saṃśuddhā na nītirbhraśyate pathāt |
laghunā ca vidhānena sthiratā samupasthitā ||*

#### English Translation
> Constrained by clipped objective bounds, the policy never diverges destructively from its trajectory; through this elegant method, rock-solid training stability is achieved.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **सीमाबन्धेन** | `सीमाबन्ध` | Noun (masculine) | Instrumental Singular | Instrument: by probability ratio clipping (1 - epsilon, 1 + epsilon) |
| **संशुद्धा** | `संशुद्ध` | Past Passive Participle (feminine) | Nominative Singular | Modifying nītiḥ: safeguarded |
| **न** | `न` | Particle | Indeclinable | Negation: not |
| **नीतिः** | `नीति` | Noun (feminine) | Nominative Singular | Subject: policy network pi_theta |
| **भ्रश्यते** | `भ्रंश्` | Verb (passive) | Present 3rd Person Singular | Verb: slips or diverges destructively |
| **पथात्** | `पथ` | Noun (masculine) | Ablative Singular | Ablative: from optimal convergence path |
| **लघुना** | `लघु` | Adjective | Instrumental Singular | Modifying vidhānena: simple / first-order |
| **च** | `च` | Conjunction | Indeclinable | Connecting: and |
| **विधानेन** | `विधान` | Noun (neuter) | Instrumental Singular | Instrument: by PPO algorithm (Proximal Policy Optimization) |
| **स्थिरता** | `स्थिरता` | Noun (feminine) | Nominative Singular | Subject: training stability |
| **समुपस्थिता** | `समुपस्थित` | Past Passive Participle (feminine) | Nominative Singular | Predicate: established |

#### Deep Systems & Domain Commentary
Proximal Policy Optimization (PPO), formulated by John Schulman et al. at OpenAI (2017), is the industry workhorse algorithm for deep reinforcement learning. Standard policy gradient methods can suffer catastrophic collapse if a single large parameter step moves the policy into a region of zero reward. TRPO (Trust Region Policy Optimization) enforced a Kullback-Leibler divergence constraint D_KL(pi_old || pi_new) <= delta, but required computationally expensive second-order conjugate gradient optimization. PPO achieves the same trust-region stability via a simple clipped surrogate objective: L^CLIP(theta) = E [min(r_t(theta) A_t, clip(r_t(theta), 1 - epsilon, 1 + epsilon) A_t)], where r_t(theta) = pi_theta(a|s) / pi_old(a|s).

---

### श्लोकः 47

```text
मनसा कल्पिते लोके सत्ये चैव कृते पदे ।
द्विधा ज्ञानेन सम्बद्धं यन्त्रं शीघ्रं प्रबुद्ध्यते ॥
```

#### IAST Transliteration
*manasā kalpite loke satye caiva kṛte pade |
dvidhā jñānena sambaddhaṃ yantraṃ śīghraṃ prabuddhyate ||*

#### English Translation
> Both in an internally envisioned mental model and in the actual real-world state: synthesizing knowledge from both realms, the machine awakens rapidly.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **मनसा** | `मनस्` | Noun (neuter) | Instrumental Singular | Instrument: by imagination / learned transition model |
| **कल्पिते** | `कल्पित` | Past Passive Participle | Locative Singular | Modifying loke: simulated |
| **लोके** | `लोक` | Noun (masculine) | Locative Singular | Locus: in the simulated environment |
| **सत्ये** | `सत्य` | Adjective | Locative Singular | Modifying pade: actual real-world |
| **च** | `च` | Conjunction | Indeclinable | Connecting: and |
| **एव** | `एव` | Particle | Indeclinable | Emphatic: also |
| **कृते** | `कृत` | Past Passive Participle | Locative Singular | Modifying pade: executed |
| **पदे** | `पद` | Noun (neuter) | Locative Singular | Locus: in physical state transition |
| **द्विधा** | `द्विधा` | Adverb | Indeclinable | Twofold: combining planning and real experience |
| **ज्ञानेन** | `ज्ञान` | Noun (neuter) | Instrumental Singular | Instrument: by synthesized knowledge |
| **सम्बद्धम्** | `सम्बद्ध` | Past Passive Participle | Nominative Singular | Modifying yantram: integrated (Dyna architecture) |
| **यन्त्रम्** | `यन्त्र` | Noun (neuter) | Nominative Singular | Subject: autonomous agent |
| **शीघ्रम्** | `शीघ्रम्` | Adverb | Indeclinable | Swiftly: sample-efficiently |
| **प्रबुद्ध्यते** | `प्रबुध्` | Verb | Present 3rd Person Singular | Verb: awakens or masters the domain |

#### Deep Systems & Domain Commentary
Model-Based Reinforcement Learning marries trial-and-error learning with internal cognitive simulation. Sutton's Dyna architecture (Dyna-Q) integrates real-world experience with simulated planning: real experience is used both to update Q-values and to train a world model P_hat(s' | s, a) and R_hat(s, a). The agent then performs dozens of imaginary planning steps within its learned mental model during downtime. Modern world models (World Models by Ha and Schmidhuber, PlaNet, DreamerV3) learn compact latent representations of physical dynamics, allowing agents to master complex continuous motor control with 100x fewer real-world samples.

---

### श्लोकः 48

```text
आत्मना सह सङ्ग्रामे परा बुद्धिर्विभासते ।
वृक्षशोधनयोगेन सर्वं जगज्जितं किल ॥
```

#### IAST Transliteration
*ātmanā saha saṅgrāme parā buddhirvibhāsate |
vṛkṣaśodhanayogena sarvaṃ jagajjitaṃ kila ||*

#### English Translation
> In self-play combat against its own iterations, supreme intelligence manifests; through Monte Carlo Tree Search synthesis, the entire game domain is conquered.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **आत्मना** | `आत्मन्` | Pronoun/Noun | Instrumental Singular | Instrument: with oneself / previous agent copies |
| **सह** | `सह` | Preposition | Indeclinable | With: in contest with |
| **सङ्ग्रामे** | `सङ्ग्राम` | Noun (masculine) | Locative Singular | Locus: in competitive self-play |
| **परा** | `पर` | Adjective (feminine) | Nominative Singular | Modifying buddhiḥ: transcendent |
| **बुद्धिः** | `बुद्धि` | Noun (feminine) | Nominative Singular | Subject: artificial intelligence |
| **विभासते** | `विभास्` | Verb | Present 3rd Person Singular | Verb: manifests or shines |
| **वृक्षशोधनयोगेन** | `वृक्षशोधनयोग` | Noun (masculine) | Instrumental Singular | Instrument: by Monte Carlo Tree Search (MCTS) |
| **सर्वम्** | `सर्व` | Adjective (neuter) | Nominative Singular | Modifying jagat: entire |
| **जगत्** | `जगत्` | Noun (neuter) | Nominative Singular | Subject: game world (Go, Chess, Shogi) |
| **जितम्** | `जित` | Past Passive Participle | Nominative Singular | Predicate: conquered |
| **किल** | `किल` | Particle | Indeclinable | Emphatic: indeed |

#### Deep Systems & Domain Commentary
DeepMind's AlphaGo, AlphaZero and MuZero represent the pinnacle of reinforcement learning breakthroughs. By combining deep convolutional neural networks (policy and value networks) with Monte Carlo Tree Search (MCTS), AlphaZero defeated world champions in Go, Chess and Shogi starting from tabula rasa without human demonstration data. Operating purely through self-play, the agent generates its own curriculum: as it discovers superior counter-strategies against earlier versions of itself, the strategic landscape deepens monotonically. MuZero further eliminated the need for game rules, learning both environmental dynamics and lookahead planning entirely end-to-end.

---

### श्लोकः 49

```text
मानवेन कृते माने नीतीनां संप्रसाधने ।
वाणी विशुध्यते यन्त्रे लोककल्याणकारिणी ॥
```

#### IAST Transliteration
*mānavena kṛte māne nītīnāṃ saṃprasādhane |
vāṇī viśudhyate yantre lokakalyāṇakāriṇī ||*

#### English Translation
> Guided by human evaluation metrics in refining the agent's policy: the linguistic output of the machine is purified, promoting the welfare of the world.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **मानवेन** | `मानव` | Noun (masculine) | Instrumental Singular | Agent: by human annotators |
| **कृते** | `कृत` | Past Passive Participle | Locative Singular | Locative absolute: established |
| **माने** | `मान` | Noun (neuter) | Locative Singular | Locative absolute: in preference reward model r_psi(x, y) |
| **नीतीनाम्** | `नीति` | Noun (feminine) | Genitive Plural | Possessive: of language model policies |
| **संप्रसाधने** | `संप्रसाधन` | Noun (neuter) | Locative Singular | Locus: in alignment optimization |
| **वाणी** | `वाणी` | Noun (feminine) | Nominative Singular | Subject: generated speech or text |
| **विशुध्यते** | `विशुध्` | Verb (passive) | Present 3rd Person Singular | Verb: is purified or aligned |
| **यन्त्रे** | `यन्त्र` | Noun (neuter) | Locative Singular | Locus: in the artificial neural network |
| **लोककल्याणकारिणी** | `लोककल्याणकारिन्` | Adjective (feminine) | Nominative Singular | Modifying vāṇī: causing the welfare of humanity |

#### Deep Systems & Domain Commentary
Reinforcement Learning from Human Feedback (RLHF), developed by Christiano et al. (2017) and popularized by InstructGPT and modern LLMs, brought reinforcement learning to the center of generative artificial intelligence. Base language models trained on internet text predict tokens rather than align with human intent. RLHF trains a neural Reward Model r_psi(prompt, completion) on human pairwise preference judgments and then optimizes the language model policy pi_theta via PPO to maximize the reward while maintaining a KL-divergence penalty against the reference model: max_theta E [r_psi(x, y) - beta D_KL(pi_theta || pi_ref)]. This aligns AI outputs to be helpful, honest and harmless.

---

### श्लोकः 50

```text
कर्मणा बध्यते लोको ज्ञानेन च विमुच्यते ।
पुनर्बलनविज्ञानं ब्रह्मविद्यामयी गतिः ॥
```

#### IAST Transliteration
*karmaṇā badhyate loko jñānena ca vimucyate |
punarbalanavijñānaṃ brahmavidyāmayī gatiḥ ||*

#### English Translation
> The living world is bound by karma and liberated through spiritual wisdom; the science of reinforcement learning is indeed a path reflecting the knowledge of the Absolute.

#### Pāṇinian Morpho-Syntactic Analysis (पदविभागः)
| Pada / Word | Prātipadika / Dhātu | Category | Vibhakti / Lakāra | Syntactic & Semantic Role |
| :--- | :--- | :--- | :--- | :--- |
| **कर्मणा** | `कर्मन्` | Noun (neuter) | Instrumental Singular | Instrument: by action (action-feedback loops) |
| **बध्यते** | `बन्ध्` | Verb (passive) | Present 3rd Person Singular | Verb: is bound in cyclic existence (saṃsāra) |
| **लोकः** | `लोक` | Noun (masculine) | Nominative Singular | Subject: the living world or agent |
| **ज्ञानेन** | `ज्ञान` | Noun (neuter) | Instrumental Singular | Instrument: by true knowledge or optimal value understanding V^* |
| **च** | `च` | Conjunction | Indeclinable | Connecting: and |
| **विमुच्यते** | `विमुच्` | Verb (passive) | Present 3rd Person Singular | Verb: is liberated |
| **पुनर्बलनविज्ञानम्** | `पुनर्बलनविज्ञान` | Noun (neuter) | Nominative Singular | Subject: science of reinforcement learning |
| **ब्रह्मविद्यामयी** | `ब्रह्मविद्यामय` | Adjective (feminine) | Nominative Singular | Modifying gatiḥ: imbued with the knowledge of Brahman |
| **गतिः** | `गति` | Noun (feminine) | Nominative Singular | Predicate: path or ultimate realization |

#### Deep Systems & Domain Commentary
The treatise concludes with a philosophical synthesis of Reinforcement Learning with classical Indian metaphysics (Vedānta and Karma-Mīmāṃsā). In Indian philosophy, an agent (jīva) performs actions (karma) in an external world (saṃsāra), experiences their delayed consequences (karma-phala) and internalizes residual behavioral impressions (saṃskāra / policy). When decisions are governed by ignorance and myopic greed, the agent remains trapped in cycles of suboptimal suffering. Through discernment (viveka), credit assignment and value optimization, the agent transcends localized friction, aligning its action policy with universal cosmic harmony (Dharma / Brahman). Reinforcement learning is the computational realization of the cosmic law of action and realization.

---

## Epilogue: The Reinforcement Horizon & Philosophical Synthesis

The intellectual journey of the **पुनर्बलनपञ्चाशिका** traverses the entire discipline of reinforcement learning: from the formalization of Markov Decision Processes and recursive Bellman decompositions, through the empirical breakthroughs of Temporal Difference learning and Q-learning, to the deep representations of Deep Q-Networks and continuous policy gradients (PPO, Actor-Critic), culminating in superhuman game mastery through AlphaZero and the alignment of generative intelligence via RLHF.

At its metaphysical core, reinforcement learning reflects the ancient Indian doctrine of *Karma-Mīmāṃsā* and *Vedānta*. An agent acts in an objective universe, receives delayed experiential fruits (*karma-phala*), internalizes latent behavioral impressions (*saṃskāra* / policy) and refines its understanding through credit assignment and wisdom (*viveka*). In mastering the optimization of action across time, artificial intelligence mirrors the eternal spiritual journey from myopic reactivity to enlightened harmony.
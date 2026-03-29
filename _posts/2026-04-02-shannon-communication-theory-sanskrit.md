---
layout: post
title: सूचनासिद्धान्तस्य संस्कृत-संहिता
subtitle: Verse-Centered Shannon Edition
tags: [sanskrit, information-theory, mathematics]
audio_sync: false
# audio_file: /assets/audio/FILENAME.mp3
---

<link rel="stylesheet" href="{{ '/assets/css/reader.css' | relative_url }}">

<div class="reader-container audio-sync-root">

{% if page.audio_sync %}
<div class="audio-panel">
  <audio controls preload="metadata" data-audio-sync-player>
    <source src="{{ page.audio_file | relative_url }}" type="audio/mpeg">
    Your browser does not support the audio element.
  </audio>
</div>
{% endif %}

The architecture of modern information theory, formulated by Claude E. Shannon in 1948, provides a rigorous mathematical framework for the quantification, encoding, compression, and transmission of data.1 This seminal framework establishes the absolute mathematical limits of communication, abstracting away the semantic meaning of messages to focus purely on the statistical and probabilistic nature of information generation and transfer.1 Concurrently, the ancient Indian intellectual traditions, specifically the combinatorial prosody codified in Piṅgala's छन्दःशास्त्र (Chandaḥśāstra) and the highly structured, computational linguistics established in Pāṇini's अष्टाध्यायी (Aṣṭādhyāyī), represent sophisticated systems of rule-based data encoding, recursive algorithms, and binary enumeration.4 The structural congruence between these two distinct paradigms suggests that the mathematical laws of modern communication theory can be effectively, elegantly, and comprehensively codified utilizing the morphological framework of the Sanskrit language.

The ensuing research report executes an exhaustive lexicographical and metrical codification of classical information theory into Sanskrit. The analysis maps the foundational concepts of communication systems, entropy, equivocation, and continuous channel capacity, explicitly filtering out transient technological applications (such as mid-century teletype mechanics) to preserve the universal mathematical theorems.1 These enduring theoretical principles are subsequently structured into formal chapters (प्रकरणम्), codified in Sanskrit verse using the classical अनुष्टुभ् (Anuṣṭubh) meter, and rigorously analyzed through the dual lenses of Pāṇinian grammar and Shannon's mathematical proofs.

<!-- Audio sync note: each verse block carries a stable data-verse-id for future timed highlighting. -->

## Name Sanskritization Note

In this post, Claude Shannon is rendered in semantic Sanskrit as **श्रुतदेव सांख्यानाचार्य** for metrical and derivational consistency:

- **Claude -> श्रुतदेव**: from dhatu **श्रु** (to hear) -> **श्रुत** (heard/learned; kta formation) + **देव** (luminous one), yielding "the learned/luminous knower of signal-hearing."
- **Shannon -> सांख्यान**: from **सम् + ख्या** (to enumerate/declare) with nominal derivation into **संख्यानम्** (enumeration), and personalized as **सांख्यान** / **सांख्यानाचार्य** in verse contexts.

<details>
<summary>Why semantic Sanskritization instead of pure transliteration</summary>
<div class="prose-text">
  <p>This edition uses dhatu-based technical neologisms rather than phonetic borrowing, so name-forms can enter compounds and meter naturally instead of sitting as opaque foreign syllable-blocks.</p>
</div>
</details>

<details>
<summary>Conceptual mapping, retention strategy, and structural blueprint</summary>
<div class="prose-text">

The extraction of core concepts from the mathematical theory of communication requires a rigorous filtering process to determine what components constitute the fundamental, immutable theory and what elements are merely illustrative, transient artifacts of the era in which the theory was initially published.1

The retention strategy focuses on the mathematical axioms, statistical mechanics, and theorems that govern all forms of data transmission, whether biological, mechanical, or digital.1 Conversely, the elements slated for omission represent specific physical instantiations that have since been superseded by advanced hardware or are irrelevant to the pure mathematics of the system.

**Core Concepts Deemed Fit for Keeping**

1. **The General Communication System Architecture:** The abstract model comprising the information source, transmitter, channel, receiver, destination, and the perturbing noise source.1 This is the foundational topology of any system.
2. **The Logarithmic Measure of Information:** The quantification of choice and uncertainty using a logarithmic function, specifically the base-2 binary digit (bit), which structurally parallels the लघु (short) and गुरु (long) combinatorial matrices of classical Sanskrit prosody.1
3. **Entropy and Stochastic Processes:** The mathematical quantification of information generation via Markov chains and ergodic sources. The central equation for discrete entropy, mathematically expressed as $H = -K \sum p_i \log p_i$, and its relationship to thermodynamic disorder and linguistic redundancy.1
4. **Equivocation and Noisy Channel Capacity:** The mathematical definition of capacity $C = \max(H(x) - H_y(x))$, establishing the absolute limit of lossless compression and transmission over a noisy medium, and the necessity of error-correcting codes.1
5. **Continuous Channel Theorems:** The continuous entropy formulations and the Shannon-Hartley theorem defining the capacity of a continuous channel bounded by white thermal noise and average power limits: $C = W \log \frac{P+N}{N}$.1

**Transient and Trite Elements Fit for Skipping**

Shannon's original documentation includes numerous historical examples utilized solely for mid-20th-century contextualization.1 These include the specific geometric dimensions and storage capacities of punched cards, the operational mechanics of analog vocoder systems, specific word-frequency approximations of the English language (e.g., the exact probabilities of the digram "TH" or specific random text generations like "XFOML RXKHRJFFJUJ"), and the physical constraints of contemporary coaxial cables.1 Furthermore, specific hardware limitations regarding pulse-code modulation (PCM) relays and flip-flop circuits are deemed transient.1 These physical instantiations and language-specific statistical quirks are superseded by the overarching mathematics and are therefore omitted from the permanent Sanskrit codification.

**Estimation of Verses and Chapter Organization**

To systematically codify the retained mathematical concepts, the material is structured into five distinct प्रकरणम् (Prakaraṇas or chapters). The classical अनुष्टुभ् (Anuṣṭubh) meter, consisting of thirty-two syllables per verse divided into four quarters of eight syllables each, is selected for the codification. This meter is the standard pedagogical vehicle of classical Indian scientific treatises (शास्त्र), allowing for dense information packing while maintaining strict grammatical cadence.

| Chapter (प्रकरणम्) | Conceptual Focus | Key Mathematical Scope | Estimated Verses |
| :---- | :---- | :---- | :---- |
| **प्रथम-प्रकरणम्** | System Architecture | Source, Transmitter, Channel, Receiver, Destination, Noise.1 | २ (Two) |
| **द्वितीय-प्रकरणम्** | Information Measurement | Logarithmic measure, Binary Digits, Combinatorics, Pingala's algorithms.1 | ३ (Three) |
| **तृतीय-प्रकरणम्** | Entropy and Ergodic Sources | $H = -K \sum p_i \log p_i$, Markov Processes, Probabilistic states.1 | ३ (Three) |
| **चतुर्थ-प्रकरणम्** | Equivocation & Noisy Capacity | $H_y(x)$, Channel Capacity, Error Correction bounds.1 | ३ (Three) |
| **पञ्चम-प्रकरणम्** | Continuous Channels | Bandwidth, Signal Power, Thermal Noise, Shannon-Hartley Theorem.1 | ३ (Three) |

The total codification requires fourteen rigorous verses.
</div>
</details>

<details>
<summary>Lexicographical framework and morphological derivations</summary>
<div class="prose-text">

The translation of modern engineering terminology into Sanskrit cannot rely on mere phonetic transliteration; it requires strict adherence to morphological rules, utilizing the foundational roots (धातु) provided in the धातुपाठ. Following the lexicographical principles established by scholars of scientific Sanskrit such as Raghu Vira, technical terms must be constructed using a specific combination of prefixes (उपसर्ग), roots, and suffixes (प्रत्यय) to ensure absolute semantic precision.15

Furthermore, existing words in vogue in other philosophical or scientific disciplines can be repurposed if their core semantic logic aligns with the mathematical concepts of information theory.2

| English Concept | Sanskrit Terminology | Root (धातु) & Suffix (प्रत्यय) | Morphological Meaning & Justification |
| :---- | :---- | :---- | :---- |
| Source | प्रभव | प्र \+ भू \+ अच् | "The place of origin." Represents the stochastic process generating the message sequence.1 |
| Transmitter | प्रेषक | प्र \+ ईष् \+ ण्वुल् | "That which sends." Represents the encoder transducer operating on the message.1 |
| Channel | मार्ग / पथ | मृज् \+ घञ् | "The pathway." The physical or abstract medium used to transmit the signal.1 (Both terms used interchangeably for metrical flexibility). |
| Receiver | ग्राहक | ग्रह् \+ ण्वुल् | "That which captures." The decoder performing the inverse operation of the transmitter.1 |
| Noise | विक्षेप / कोलाहल | वि \+ क्षिप् \+ घञ् | "Scattering or disruption." Represents the statistical perturbation in the channel.1 |
| Signal | सङ्केत | सम् \+ कित् \+ घञ् | "An agreed-upon sign." The encoded sequence transmitted over the channel.1 |
| Bit (Binary Digit) | द्व्यङ्क / शून्यैक | द्वि \+ अङ्क | "A dual-state digit." The fundamental unit of information measurement.1 (शून्यैक is used as a metrical alternative meaning "zero and one"). |
| Entropy | अपोहन / अक्रमता | अप \+ ऊह् \+ ल्युट् | Repurposed from Buddhist epistemology meaning "exclusion of alternatives".18 In physics, it means disorder (अक्रमता).12 Both perfectly describe Shannon entropy. |
| Equivocation | सन्दिग्धता | सम् \+ दिह् \+ क्त \+ तल् | "The state of being obscured." Represents conditional entropy $H_y(x)$, the ambiguity of the signal.1 |
| Capacity | क्षमता | क्षम् \+ अतल | "Absolute maximum capability." The upper limit of transmission rate.1 |

This morphological rigor ensures that the resulting Sanskrit verses are not merely poetic approximations, but exact mathematical equations codified in linguistic form.
</div>
</details>

## प्रथम-प्रकरणम्: सम्प्रेषण-तन्त्र-व्यवस्था

The fundamental problem of communication is the exact or approximate reproduction of a message selected at one point at another distant point.1 Frequently, messages possess semantic meaning; they refer to conceptual or physical entities. However, these semantic aspects of communication are mathematically irrelevant to the engineering problem.1 The significant aspect is that the actual message is one selected from a set of possible messages. The system must be designed to operate for *each* possible selection, not just the one that will actually be chosen, since this is unknown at the time of system design.1

The system is fundamentally composed of five components and one perturbing element, forming a linear topology of information flow.1

<p class="verse-topic">Verse 1 (Anuṣṭubh)</p>
<div class="sanskrit-text sanskrit-verse-lines" data-verse-id="v1">
  <span data-line="1" data-start="" data-end="">सम्प्रेषणस्य तन्त्रेऽस्मिन् पञ्चाङ्गानि भवन्ति हि ।</span><br />
  <span data-line="2" data-start="" data-end="">प्रभवः प्रेषकश्चैव मार्गो ग्राहक एव च ॥ १ ॥</span>
</div>
<div class="prose-text"><strong>Translation:</strong> In the communication system there are five principal limbs: source, transmitter, channel, receiver, and destination-chain endpoint.</div>

<p class="verse-topic">Verse 2 (Anuṣṭubh)</p>
<div class="sanskrit-text sanskrit-verse-lines" data-verse-id="v2">
  <span data-line="1" data-start="" data-end="">गन्तव्यं पञ्चमं प्रोक्तं सङ्केतो मार्गतो गतः ।</span><br />
  <span data-line="2" data-start="" data-end="">विक्षेपेण युतो मध्ये सन्देशो विकृतो भवेत् ॥ २ ॥</span>
</div>
<div class="prose-text"><strong>Translation:</strong> The destination is declared the fifth point; while traversing the channel, the signal may be corrupted by noise in transit.</div>

<details>
<summary>Grammatical analysis (पदच्छेद, अन्वय, प्रतिपदार्थ)</summary>
<div class="prose-text">

पदच्छेदः : सम्प्रेषणस्य तन्त्रे अस्मिन् पञ्च अङ्गानि भवन्ति हि । प्रभवः प्रेषकः च एव मार्गः ग्राहकः एव च ।

अन्वयः : अस्मिन् सम्प्रेषणस्य तन्त्रे हि पञ्च अङ्गानि भवन्ति। (तानि) प्रभवः, प्रेषकः, मार्गः, ग्राहकः च एव (भवन्ति)।

प्रतिपदार्थः : सम्प्रेषणस्य = of communication; तन्त्रे = in the system; अस्मिन् = in this; पञ्च = five; अङ्गानि = components/limbs; भवन्ति = are; हि = indeed. प्रभवः = the source; प्रेषकः = the transmitter; च = and; एव = indeed; मार्गः = the channel; ग्राहकः = the receiver; एव = indeed; च = and.

पदच्छेदः : गन्तव्यं पञ्चमं प्रोक्तं सङ्केतः मार्गतः गतः । विक्षेपेण युतः मध्ये सन्देशः विकृतः भवेत् ।

अन्वयः : गन्तव्यं पञ्चमं प्रोक्तम्। मार्गतः गतः सङ्केतः मध्ये विक्षेपेण युतः (सन्) विकृतः सन्देशः भवेत्।

प्रतिपदार्थः : गन्तव्यं = the destination; पञ्चमं = the fifth; प्रोक्तं = is said; सङ्केतः = the signal; मार्गतः = through the channel; गतः = gone. विक्षेपेण = by noise; युतः = joined/affected; मध्ये = in the middle; सन्देशः = the message; विकृतः = distorted; भवेत् = may become.
</div>
</details>

<details>
<summary>Theoretical explication</summary>
<div class="prose-text">

The verses mathematically define the schematic diagram of a general communication system. The प्रभव (information source) produces a सन्देश (message) or a sequence of messages to be communicated to the receiving terminal.1 This source may be discrete, producing a sequence of letters, or continuous, producing a function of time $f(t)$.1

The प्रेषक (transmitter) operates on the message in some way to produce a सङ्केत (signal) suitable for transmission over the मार्ग (channel).1 In telephony, this operation consists merely of changing sound pressure into a proportional electrical current. In telegraphy, it involves an encoding operation that produces a sequence of dots, dashes, and spaces on the channel corresponding to the message. In more complex multiplexed systems, different functions must be sampled, compressed, quantized, and encoded.1

The मार्ग is merely the medium used to transmit the signal from the transmitter to the receiver. Crucially, as the second verse notes, during transmission, the signal is perturbed by विक्षेप (noise). The noise is considered a chance variable, represented by a suitable stochastic process, which alters the signal such that the received sequence is not necessarily the same as the transmitted sequence.1

Finally, the ग्राहक (receiver) ordinarily performs the inverse operation of that done by the transmitter, reconstructing the message from the perturbed signal, and delivering it to the गन्तव्य (destination), which is the person or thing for whom the message is intended.1 To maximize the power transfer of information, the transducer (the transmitter doing the encoding) must match the statistical structure of the source to the statistical structure of the channel, much like a transformer matches generator resistance to load resistance.1
</div>
</details>

## द्वितीय-प्रकरणम्: द्व्यङ्क-मानं तथा प्रस्तार-गणितम्

If the number of messages in a set is finite, this number or any monotonic function of this number can be regarded as a measure of the information produced when one message is chosen from the set, assuming all choices are equally likely.1 The most natural choice, mathematically and intuitively, is the logarithmic function. When the base 2 is utilized, the resulting units are called binary digits, or "bits".1

Historically, the conceptual foundation of the binary system and combinatorial mathematics was formalized in ancient India by the scholar Piṅgala in the छन्दःशास्त्र (circa 3rd century BCE). Piṅgala mapped poetic meters using a binary framework of लघु (laghu - short) and गुरु (guru - long) syllables, effectively creating the world's first formal binary enumeration system.5

<p class="verse-topic">Verse 3 (Anuṣṭubh)</p>
<div class="sanskrit-text sanskrit-verse-lines" data-verse-id="v3">
  <span data-line="1" data-start="" data-end="">सन्देशानां विकल्पस्तु लघुकृत्या हि मीयते ।</span><br />
  <span data-line="2" data-start="" data-end="">आधारो द्विगुणस्तत्र मानं द्व्यङ्कमुदाहृतम् ॥ ३ ॥</span>
</div>
<div class="prose-text"><strong>Translation:</strong> Message-choice is measured logarithmically; with base two, that measure is called the binary digit (bit).</div>

<p class="verse-topic">Verse 4 (Anuṣṭubh)</p>
<div class="sanskrit-text sanskrit-verse-lines" data-verse-id="v4">
  <span data-line="1" data-start="" data-end="">पिङ्गलेन पुरा प्रोक्तो लघुर्गुर्वात्मकः क्रमः ।</span><br />
  <span data-line="2" data-start="" data-end="">स एव द्व्यङ्करूपेण ज्ञानमाने प्रयुज्यते ॥ ४ ॥</span>
</div>
<div class="prose-text"><strong>Translation:</strong> Pingala's ancient laghu-guru combinatorics is the same structure now used as binary form for information measurement.</div>

<p class="verse-topic">Verse 5 (Anuṣṭubh)</p>
<div class="sanskrit-text sanskrit-verse-lines" data-verse-id="v5">
  <span data-line="1" data-start="" data-end="">प्रस्तारस्य विधानेन विकल्पानन्ततिर्मिता ।</span><br />
  <span data-line="2" data-start="" data-end="">शून्यैकेन च तद् बिम्बं यन्त्रेष्वपि विधीयते ॥ ५ ॥</span>
</div>
<div class="prose-text"><strong>Translation:</strong> By systematic enumeration, vast combinations are bounded; that same zero-one mapping is established in machines.</div>

<details>
<summary>Grammatical analysis (पदच्छेद, अन्वय, प्रतिपदार्थ)</summary>
<div class="prose-text">

पदच्छेदः : सन्देशानां विकल्पः तु लघुकृत्या हि मीयते । आधारः द्विगुणः तत्र मानं द्व्यङ्कम् उदाहृतम् ।

अन्वयः : सन्देशानां विकल्पः तु लघुकृत्या हि मीयते। तत्र द्विगुणः आधारः (भवति), मानं द्व्यङ्कम् उदाहृतम्।

प्रतिपदार्थः : सन्देशानां = of the messages; विकल्पः = the choice/options; तु = indeed; लघुकृत्या = by logarithm (lit. reducing function); हि = certainly; मीयते = is measured. आधारः = the base; द्विगुणः = twofold/two; तत्र = there; मानं = the measure; द्व्यङ्कम् = binary digit (bit); उदाहृतम् = is called.

पदच्छेदः : पिङ्गलेन पुरा प्रोक्तः लघुः गुरुः आत्मकः क्रमः । सः एव द्व्यङ्करूपेण ज्ञानमाने प्रयुज्यते ।

अन्वयः : पिङ्गलेन पुरा लघुर्गुर्वात्मकः क्रमः प्रोक्तः। सः एव द्व्यङ्करूपेण ज्ञानमाने प्रयुज्यते।

प्रतिपदार्थः : पिङ्गलेन = by Piṅgala; पुरा = in ancient times; प्रोक्तः = explained; लघुः = short syllable; गुरुः = long syllable; आत्मकः = composed of; क्रमः = sequence. सः = that; एव = exactly; द्व्यङ्करूपेण = in the form of binary digits; ज्ञानमाने = in the measurement of information; प्रयुज्यते = is utilized.

पदच्छेदः : प्रस्तारस्य विधानेन विकल्प-अनन्ततिः मिता । शून्यैकेन च तद् बिम्बं यन्त्रेषु अपि विधीयते ।

अन्वयः : प्रस्तारस्य विधानेन विकल्पानन्ततिः मिता। शून्यैकेन च तद् बिम्बं यन्त्रेषु अपि विधीयते।

प्रतिपदार्थः : प्रस्तारस्य = of the systematic enumeration; विधानेन = by the method; विकल्प = of combinations; अनन्ततिः = the infinity/vastness; मिता = is measured/bounded. शून्यैकेन = by zero and one (a metrical synonym for dvyaṅka); च = and; तद् = that; बिम्बं = reflection/mapping; यन्त्रेषु = in machines/computers; अपि = also; विधीयते = is established.

*(Note: In verse 5, the term शून्यैक is utilized as a metrical alternative to द्व्यङ्क, possessing three syllables instead of two, specifically meaning "zero and one" to fit the Anuṣṭubh structure).*
</div>
</details>

<details>
<summary>Theoretical explication</summary>
<div class="prose-text">

The logarithmic measure, coined here as लघुकृति (Laghukṛti, the mathematical operation that reduces exponential growth into linear scaling), is convenient for several reasons. Parameters of engineering importance, such as time, bandwidth, and the number of relays, tend to vary linearly with the logarithm of the number of possibilities.1 Adding one relay to a group doubles the number of possible states, adding exactly 1 to the base-2 logarithm of this number. A device with two stable positions, such as a relay or a flip-flop circuit, can store one द्व्यङ्क (bit) of information, as $N$ such devices can store $N$ bits, generating $2^N$ possible states, mirroring the equation $\log_2 2^N = N$.1

This directly parallels the प्रस्तार (Prastāra, systematic enumeration) algorithm found in Piṅgala's छन्दःशास्त्र. To systematically enumerate all possible combinations of a meter containing $N$ syllables, Piṅgala utilized a recursive formula utilizing the two fundamental prosodic units: लघु (L) and गुरु (G).6

| Decimal Equivalent | Piṅgala's Sequence (Binary Logic) | 3-Bit Representation (Modern) |
| :---- | :---- | :---- |
| 0 | ग ग ग (G G G) | 0 0 0 |
| 1 | ल ग ग (L G G) | 1 0 0 |
| 2 | ग ल ग (G L G) | 0 1 0 |
| 3 | ल ल ग (L L G) | 1 1 0 |
| 4 | ग ग ल (G G L) | 0 0 1 |
| 5 | ल ग ल (L G L) | 1 0 1 |
| 6 | ग ल ल (G L L) | 0 1 1 |
| 7 | ल ल ल (L L L) | 1 1 1 |

Note: Piṅgala's binary representation increases exponentially towards the right, contrary to modern left-heavy positional notation.5 Piṅgala also mapped these combinations to the मात्रा-मेरु (Mātrā-meru), identifying the exact mathematical sequence later known as the Fibonacci sequence to compute the number of variations of moraic meters.6

The correlation between Piṅgala's combinatorics and Shannon's logarithmic measure is structurally absolute. A continuous source, producing data over an extended duration, acts as a stochastic process generating these discrete combinations. The total combinatorial weight of these sequences strictly defines the required capacity of the मार्ग (channel).1
</div>
</details>

## तृतीय-प्रकरणम्: अपोहनम् तथा साङ्ख्यिक-प्रक्रिया

When a discrete information source operates, it generates symbols based on specific probability distributions, which are heavily influenced by preceding choices.1 This represents a stochastic process, modeled mathematically as a discrete Markov chain.1 The measure of how much information, or uncertainty, is generated by this process is quantified as Entropy ($H$).2 The Sanskrit term utilized here is अपोहन (Apohana), a term historically utilized in Buddhist epistemology (by Dignāga and Dharmakīrti) and non-dual Kashmir Shaivism (by Abhinavagupta) to mean "the creation of meaning through the exclusion of alternatives".18 This maps flawlessly to Gregory Bateson's definition of information as "a difference which makes a difference," and Shannon's mathematical entropy.18

<p class="verse-topic">Verse 6 (Anuṣṭubh)</p>
<div class="sanskrit-text sanskrit-verse-lines" data-verse-id="v6">
  <span data-line="1" data-start="" data-end="">सम्भाव्यतानां सङ्घातं तल्लघुकृत्या च ताडितम् ।</span><br />
  <span data-line="2" data-start="" data-end="">ऋणात्मकं यदा कृत्वा सर्वं तद् विनिगम्यते ॥ ६ ॥</span>
</div>
<div class="prose-text"><strong>Translation:</strong> Probabilities are aggregated, weighted by logarithms, and negated in total; thus entropy is computed.</div>

<p class="verse-topic">Verse 7 (Anuṣṭubh)</p>
<div class="sanskrit-text sanskrit-verse-lines" data-verse-id="v7">
  <span data-line="1" data-start="" data-end="">तत् फलं ह्यपोहनं स्यादक्रमता च गद्यते ।</span><br />
  <span data-line="2" data-start="" data-end="">ज्ञानोत्पादनवेगोऽयं प्रभवस्य विनिर्णयः ॥ ७ ॥</span>
</div>
<div class="prose-text"><strong>Translation:</strong> That result is entropy (apohana), also disorder; it gives the definite rate of information generation by the source.</div>

<p class="verse-topic">Verse 8 (Anuṣṭubh)</p>
<div class="sanskrit-text sanskrit-verse-lines" data-verse-id="v8">
  <span data-line="1" data-start="" data-end="">यन्त्राणां शृङ्खला यत्र पूर्वेण परिकल्पिता ।</span><br />
  <span data-line="2" data-start="" data-end="">तत्र सङ्कोचनं शक्यं भाषायां पाणिनेरिव ॥ ८ ॥</span>
</div>
<div class="prose-text"><strong>Translation:</strong> Where state-chains are conditioned by prior state, compression is possible, much like structured inheritance in Paninian grammar.</div>

<details>
<summary>Grammatical analysis (पदच्छेद, अन्वय, प्रतिपदार्थ)</summary>
<div class="prose-text">

पदच्छेदः : सम्भाव्यतानां सङ्घातं तत्-लघुकृत्या च ताडितम् । ऋणात्मकं यदा कृत्वा सर्वं तद् विनिगम्यते ।

अन्वयः : सम्भाव्यतानां सङ्घातं तल्लघुकृत्या च ताडितं (भवति)। यदा सर्वं ऋणात्मकं कृत्वा तद् विनिगम्यते।

प्रतिपदार्थः : सम्भाव्यतानां = of the probabilities ($p_i$); सङ्घातं = the collection/mass; तल्लघुकृत्या = by their logarithms ($\log p_i$); च = and; ताडितम् = multiplied. ऋणात्मकं = negative; यदा = when; कृत्वा = having made; सर्वं = all (the sum $\sum$); तद् = that; विनिगम्यते = is computed/derived.

पदच्छेदः : तत् फलं हि अपोहनं स्यात् अक्रमता च गद्यते । ज्ञान-उत्पादन-वेगः अयं प्रभवस्य विनिर्णयः ।

अन्वयः : तत् फलं हि अपोहनं स्यात्, अक्रमता च गद्यते। अयं प्रभवस्य ज्ञानोत्पादनवेगः विनिर्णयः (भवति)।

प्रतिपदार्थः : तत् = that; फलं = result; हि = indeed; अपोहनं = entropy (exclusion of alternatives); स्यात् = is; अक्रमता = disorder/entropy; च = and; गद्यते = is stated. ज्ञानोत्पादनवेगः = the rate of information generation; अयं = this; प्रभवस्य = of the source; विनिर्णयः = the definitive measure.

पदच्छेदः : यन्त्राणां शृङ्खला यत्र पूर्वेण परिकल्पिता । तत्र सङ्कोचनं शक्यं भाषायां पाणिनेः इव ।

अन्वयः : यत्र यन्त्राणां शृङ्खला पूर्वेण परिकल्पिता, तत्र पाणिनेः भाषायां इव सङ्कोचनं शक्यम्।

प्रतिपदार्थः : यन्त्राणां = of the mechanisms/states; शृङ्खला = the chain (Markov chain); यत्र = where; पूर्वेण = by the previous (state); परिकल्पिता = is determined/influenced. तत्र = there; सङ्कोचनं = compression; शक्यं = is possible; भाषायां = in the language; पाणिनेः = of Pāṇini; इव = like.

*(Note: In verse 7, the term अक्रमता is used alongside अपोहन. While अपोहन focuses on the information-theoretic aspect of excluding alternatives, अक्रमता explicitly connects to the thermodynamic definition of entropy as 'disorder' or 'noise in the system', highlighting the deep physical implications of the mathematics 12).*
</div>
</details>

<details>
<summary>Theoretical explication</summary>
<div class="prose-text">

The verses strictly codify Shannon's central equation for the entropy of a discrete set of probabilities $p_1, p_2,..., p_n$:

$$H = -K \sum_{i=1}^{n} p_i \log p_i$$

This derived quantity possesses profound mathematical properties that solidify it as the definitive measure of uncertainty 1:

1. $H$ evaluates to zero if and only if all probabilities except one are zero. Absolute certainty implies zero information generation.1
2. For a given $n$, $H$ is maximized and equal to $\log n$ when all probabilities $p_i$ are equal ($1/n$), representing the state of maximum uncertainty and optimal channel utilization.1
3. The joint entropy of two events $x$ and $y$ evaluates to $H(x,y) \le H(x) + H(y)$, with absolute equality occurring exclusively when the events are completely independent.1

For an ergodic source, where every sufficiently long sequence produced ultimately reflects the statistical properties of the entire ensemble, the entropy $H$ dictates the absolute maximum limits of data compression.1 The redundancy of a natural language like English, accounting for statistical structures extending out to about eight letters, is roughly 50%.1 This implies that half of every sequence is dictated by deterministic statistical structures rather than free choice.

Verse 8 draws a parallel to Markov chains and Pāṇinian grammar. A Markov process is one where the probability of generating a specific symbol is dependent on the "residue of influence" from preceding states.1 Translating this into Sanskrit linguistics, the highly structured, context-sensitive nature of Pāṇinian grammar (अष्टाध्यायी) acts as an optimal, mathematically rigorous encoding algorithm.4 By defining precise *adhikāra* (domain) and *anuvṛtti* (inheritance) rules, Pāṇini minimized redundancy while preventing the loss of structural integrity, effectively minimizing the necessary channel capacity for linguistic communication, exactly as Shannon proposed for digital compression.4
</div>
</details>

## चतुर्थ-प्रकरणम्: मार्गक्षमता तथा सन्दिग्धता

In practical physical applications, a communication channel is perpetually subjected to noise, implying that the received signal $y$ is not necessarily identical to the transmitted signal $x$.1 If the received signal is a definite function of the transmitted signal, it is mere distortion, which can be corrected by an inverse operation. However, true noise is a chance variable, meaning the received signal is $E = f(S, N)$, combining the signal and the noise stochastically.1 The receiver is therefore left with an ambiguity regarding the original message, a deficit measured mathematically as Equivocation, or सन्दिग्धता (Sandigdhatā).1

<p class="verse-topic">Verse 9 (Anuṣṭubh)</p>
<div class="sanskrit-text sanskrit-verse-lines" data-verse-id="v9">
  <span data-line="1" data-start="" data-end="">मार्गे विक्षेपदोषेण यदा सन्दिग्धता भवेत् ।</span><br />
  <span data-line="2" data-start="" data-end="">तदा प्राप्तेऽपि सन्देशे किञ्चिद् ज्ञानं प्रणश्यति ॥ ९ ॥</span>
</div>
<div class="prose-text"><strong>Translation:</strong> When channel noise induces ambiguity, some information is lost even if a message is received.</div>

<p class="verse-topic">Verse 10 (Anuṣṭubh)</p>
<div class="sanskrit-text sanskrit-verse-lines" data-verse-id="v10">
  <span data-line="1" data-start="" data-end="">मूलज्ञानाद् वियोज्यैतां सन्दिग्धां विकृतिं ततः ।</span><br />
  <span data-line="2" data-start="" data-end="">यत् परं लभ्यते मानं सा मार्गक्षमता स्मृता ॥ १० ॥</span>
</div>
<div class="prose-text"><strong>Translation:</strong> Subtracting equivocation from original information yields the maximal reliable measure called channel capacity.</div>

<p class="verse-topic">Verse 11 (Anuṣṭubh)</p>
<div class="sanskrit-text sanskrit-verse-lines" data-verse-id="v11">
  <span data-line="1" data-start="" data-end="">आदर्शसङ्केतविध्या दोषशून्यं हि सम्भवम् ।</span><br />
  <span data-line="2" data-start="" data-end="">क्षमताया अधो वेगे दोषांशो याति शून्यताम् ॥ ११ ॥</span>
</div>
<div class="prose-text"><strong>Translation:</strong> With ideal coding, near-errorless communication is possible; below capacity, error fraction tends toward zero.</div>

<details>
<summary>Grammatical analysis (पदच्छेद, अन्वय, प्रतिपदार्थ)</summary>
<div class="prose-text">

पदच्छेदः : मार्गे विक्षेप-दोषेण यदा सन्दिग्धता भवेत् । तदा प्राप्ते अपि सन्देशे किञ्चिद् ज्ञानं प्रणश्यति ।

अन्वयः : मार्गे विक्षेपदोषेण यदा सन्दिग्धता भवेत्, तदा सन्देशे प्राप्ते अपि किञ्चिद् ज्ञानं प्रणश्यति।

प्रतिपदार्थः : मार्गे = in the channel; विक्षेपदोषेण = by the flaw of noise; यदा = when; सन्दिग्धता = equivocation/ambiguity; भवेत् = occurs. तदा = then; प्राप्ते = received; अपि = even; सन्देशे = the message; किञ्चिद् = some; ज्ञानं = information; प्रणश्यति = is lost/destroyed.

पदच्छेदः : मूल-ज्ञानाद् वियोज्य एतां सन्दिग्धां विकृतिं ततः । यत् परं लभ्यते मानं सा मार्ग-क्षमता स्मृता ।

अन्वयः : ततः मूलज्ञानाद् एतां सन्दिग्धां विकृतिं वियोज्य यत् परं मानं लभ्यते सा मार्गक्षमता स्मृता।

प्रतिपदार्थः : मूलज्ञानाद् = from the original information ($H(x)$); वियोज्य = having subtracted; एतां = this; सन्दिग्धां = equivocation ($H_y(x)$); विकृतिं = distortion; ततः = then. यत् = which; परं = maximum; लभ्यते = is obtained; मानं = value/measure; सा = that; मार्गक्षमता = channel capacity ($C$); स्मृता = is known/recorded.

पदच्छेदः : आदर्श-सङ्केत-विध्या दोष-शून्यं हि सम्भवम् । क्षमतायाः अधः वेगे दोष-अंशः याति शून्यताम् ।

अन्वयः : आदर्शसङ्केतविध्या दोषशून्यं हि सम्भवम्। क्षमतायाः अधः वेगे दोषांशः शून्यतां याति।

प्रतिपदार्थः : आदर्शसङ्केतविध्या = by ideal encoding methods; दोषशून्यं = error-free; हि = indeed; सम्भवम् = is possible. क्षमतायाः = of the capacity; अधः = below; वेगे = at the rate; दोषांशः = the fraction of errors; याति = goes to; शून्यताम् = zero.
</div>
</details>

<details>
<summary>Theoretical explication</summary>
<div class="prose-text">

Equivocation, mathematically denoted as $H_y(x)$, represents the conditional entropy of the message when the received signal is known. It mathematically measures the average ambiguity of the received signal resulting from the channel noise.1 Shannon establishes that the actual rate of reliable information transmission ($R$) is determined by subtracting the equivocation from the entropy of the source:

$$R = H(x) - H_y(x)$$

Alternatively, $R$ can be expressed as $H(y) - H_x(y)$, representing the amount of information received less the portion of that information which is purely due to noise.1

This framework leads directly to Shannon's Fundamental Theorem for a Discrete Channel with Noise (Theorem 11). The capacity $C$ of a noisy channel is defined as the absolute maximum of the transmission rate, maximizing over all possible information sources used as input to the channel:

$$C = \max_{P(x)} (H(x) - H_y(x))$$

Verse 11 codifies the profound and counterintuitive reality revealed by Shannon's mathematical proof: it is possible to transmit information at any rate $R < C$ through the channel with an arbitrarily small frequency of errors, provided proper redundant encoding is applied.1 Nature does not demand a continuous degradation of quality as noise increases; rather, nature merely sets a strict capacity bound. If the source attempts to transmit at a higher rate than $C$, say $C + R_1$, there will necessarily be an equivocation equal to or greater than the excess $R_1$.1

To achieve this ideal error-free state, encoding mechanisms must arrange messages of length $N$ in order of decreasing probability and expand them into a binary system (similar to Fano's method), associating long blocks of message signals with a subset of channel inputs that are spaced far apart in the $n$-dimensional signal space, ensuring that reasonable noise perturbations do not push one valid signal into the territory of another.1 The equivocation $H_y(x)$ effectively acts as the precise volume of supplementary data that would be required via an idealized "correction channel" (as seen in Theorem 10) to perfectly repair the noisy signal at the receiver.1
</div>
</details>

## पञ्चम-प्रकरणम्: निरन्तर-सम्प्रेषणम् ऊष्मागतिकी च

The final dimension of classical communication theory maps the transition from discrete symbol sequences to continuous functions of time, such as continuous analog speech signals or radio frequency waveforms.1 A continuous signal constrained to a bandwidth $W$ can be perfectly resolved into $2TW$ discrete numerical coordinates over time $T$ via the Nyquist-Shannon sampling theorem.1

Unlike discrete entropy, the entropy of a continuous distribution is relative to the coordinate system. If the coordinates undergo a linear transformation (such as passing through a filter with characteristic $Y(f)$), the output entropy is shifted by the expected logarithm of the Jacobian of the transformation.1 However, the calculated capacities remain invariant. When subjected to white thermal noise, the maximum channel capacity assumes a specific formulation governed by bandwidth and average power constraints.1

<p class="verse-topic">Verse 12 (Anuṣṭubh)</p>
<div class="sanskrit-text sanskrit-verse-lines" data-verse-id="v12">
  <span data-line="1" data-start="" data-end="">आवृत्तिर्विपुला मार्गे कोलाहलो निरन्तरः ।</span><br />
  <span data-line="2" data-start="" data-end="">शक्तेर्मानं यदा बद्धं क्षमता तत्र कथ्यते ॥ १२ ॥</span>
</div>
<div class="prose-text"><strong>Translation:</strong> In wideband channels with continuous noise, capacity is stated under bounded signal power.</div>

<p class="verse-topic">Verse 13 (Anuṣṭubh)</p>
<div class="sanskrit-text sanskrit-verse-lines" data-verse-id="v13">
  <span data-line="1" data-start="" data-end="">सङ्केतस्य च या शक्तिः कोलाहलेन मिश्रिता ।</span><br />
  <span data-line="2" data-start="" data-end="">कोलाहलेन विभक्ता लघुकृत्या च साधिता ॥ १३ ॥</span>
</div>
<div class="prose-text"><strong>Translation:</strong> Signal power mixed with noise, divided by noise, and taken logarithmically gives the computable core ratio.</div>

<p class="verse-topic">Verse 14 (Anuṣṭubh)</p>
<div class="sanskrit-text sanskrit-verse-lines" data-verse-id="v14">
  <span data-line="1" data-start="" data-end="">विस्तारेण च सङ्गुण्या क्षमता सा प्रजायते ।</span><br />
  <span data-line="2" data-start="" data-end="">एतद्धि परमं मानं सम्प्रेषणविशारदैः ॥ १४ ॥</span>
</div>
<div class="prose-text"><strong>Translation:</strong> Multiplying by bandwidth yields capacity; communication theorists regard this as the supreme bound.</div>

<details>
<summary>Grammatical analysis (पदच्छेद, अन्वय, प्रतिपदार्थ)</summary>
<div class="prose-text">

पदच्छेदः : आवृत्तिः विपुला मार्गे कोलाहलः निरन्तरः । शक्तेः मानं यदा बद्धं क्षमता तत्र कथ्यते ।

अन्वयः : मार्गे आवृत्तिः विपुला (तथा) कोलाहलः निरन्तरः (अस्ति)। यदा शक्तेः मानं बद्धं (भवति), तत्र क्षमता कथ्यते।

प्रतिपदार्थः : आवृत्तिः = frequency; विपुला = wide (bandwidth $W$); मार्गे = in the channel; कोलाहलः = noise ($N$); निरन्तरः = continuous/thermal. शक्तेः = of the power ($P$); मानं = measure; यदा = when; बद्धं = bound/limited; क्षमता = capacity; तत्र = there; कथ्यते = is stated.

पदच्छेदः : सङ्केतस्य च या शक्तिः कोलाहलेन मिश्रिता । कोलाहलेन विभक्ता लघुकृत्या च साधिता ।

अन्वयः : सङ्केतस्य च या शक्तिः (सा) कोलाहलेन मिश्रिता (भवति)। (ततः सा) कोलाहलेन विभक्ता लघुकृत्या च साधिता।

प्रतिपदार्थः : सङ्केतस्य = of the signal; च = and; या = which; शक्तिः = power ($P$); कोलाहलेन = with the noise ($N$); मिश्रिता = mixed ($P+N$). कोलाहलेन = by the noise ($N$); विभक्ता = divided ($(P+N)/N$); लघुकृत्या = by the logarithm ($\log_2$); च = and; साधिता = computed.

पदच्छेदः : विस्तारेण च सङ्गुण्या क्षमता सा प्रजायते । एतत् हि परमं मानं सम्प्रेषण-विशारदैः ।

अन्वयः : (तत् फलं) विस्तारेण सङ्गुण्या सा क्षमता प्रजायते। एतत् हि सम्प्रेषणविशारदैः परमं मानं (स्मृतम्)।

प्रतिपदार्थः : विस्तारेण = by the bandwidth ($W$); च = and; सङ्गुण्या = having multiplied; क्षमता = capacity ($C$); सा = that; प्रजायते = arises/becomes. एतत् = this; हि = indeed; परमं = supreme/maximum; मानं = measure; सम्प्रेषणविशारदैः = by communication experts (is recognized).
</div>
</details>

<details>
<summary>Theoretical explication</summary>
<div class="prose-text">

The final verses meticulously codify Theorem 17, commonly known as the Shannon-Hartley theorem. This theorem determines the theoretical upper bound on the rate of information that can be communicated at an arbitrarily low error rate over an analog communication channel subject to Additive White Gaussian Noise (AWGN).1 The capacity $C$ of a channel of band $W$, perturbed by white thermal noise power $N$, when the average transmitter power is limited to $P$, is given by:

$$C = W \log_2 \left(\frac{P+N}{N}\right)$$

The derivation of this mathematical limit relies heavily on geometric properties in $n$-dimensional function space and the principle of maximum entropy. The average power of the perturbed signal received at the destination equals $P+N$. According to calculus of variations, the maximum entropy for a given variance (which corresponds physically to the average power of the signal) is achieved exclusively by a Gaussian probability distribution.1 Therefore, the maximum entropy of the received signal occurs when the transmitted signal itself is statistically constructed to mimic white thermal noise.

The entropy per second of this maximized received ensemble is calculated as $H(y) = W \log 2\pi e(P+N)$. The entropy of the perturbing white noise alone is $H(n) = W \log 2\pi eN$.1 Because the signal and the thermal noise are statistically independent, the joint entropy relationships hold, and the channel capacity equates directly to the difference between these two entropies: $C = H(y) - H(n)$. Subtracting the logarithms yields the ratio $\frac{P+N}{N}$, scaled linearly by the continuous bandwidth $W$.1

This continuous formulation highlights a deep philosophical and physical link between information theory and thermodynamics. The "thermal noise" described by Shannon is a physical manifestation of thermodynamic entropy.1 In classical physics, as observed through the lens of Indian philosophy, this relates closely to the concepts of order and chaos (Karma and Samskaras causing 'noise' in a unitary system).26 High entropy in a continuous thermal system equates to maximum disorder (अक्रमता), bounding the ability of the signal to maintain its structural integrity. To approach the ideal limit of $W \log_2 \left(\frac{P+N}{N}\right)$, the encoded symbols must map to highly complex, pseudo-random vectors (samples of white noise) within a $2TW$-dimensional sphere, requiring significant delay at both the transmitter and receiver to compute the least root-mean-square discrepancy.1

Furthermore, if the power limitation placed upon the transmitter is not an *average* limit ($P$) but an absolute *peak* instantaneous limit ($S$), the capacity mathematics shift. Shannon demonstrates in Theorem 20 that the capacity is bounded asymptotically by $C \le W \log \left(\frac{\frac{2}{\pi e}S + N}{N}\right)$ for large signal-to-noise ratios, showing that peak limitations restrict the volume of the high-probability $n$-dimensional sphere more aggressively than average power constraints.1
</div>
</details>

## Conclusion

The rigorous codification of modern information theory into classical Sanskrit demonstrates unequivocally that the complex operational mathematics governing telecommunications and data science are fundamentally compatible with the highly structured, morphological rules of ancient Indian linguistics and combinatorics. The foundational insights of Claude Shannon, quantifying information via base-2 logarithms, calculating systemic uncertainty as mathematical entropy, and establishing the absolute bounds of error-resilient continuous channels via geometric limits in $n$-dimensional space, find profound historical and structural mirrors in the binary matrices of Piṅgala's छन्दःशास्त्र and the algorithmic semantic exclusions (अपोहन) inherent in classical Indian philosophy and Pāṇinian grammar.4

By explicitly discarding transient mid-century technological implementations and focusing strictly on the abstract, immutable mathematical proofs of Shannon's 1948 thesis, the resulting fourteen lines of अनुष्टुभ् (Anuṣṭubh) verse successfully compress the core axioms of communication theory into an elegant, easily transmittable mnemonic structure. The systematic generation of scientific terminology, such as अपोहन (Apohana) for Entropy, द्व्यङ्क (Dvyaṅka) for Binary Digit, and मार्गक्षमता (Mārgakṣamatā) for Channel Capacity, using the foundational roots of the धातुपाठ ensures that the terminology is not merely a phonetic translation, but a precise, self-descriptive morphological construct that mathematically derives the exact operations it represents. This analytical synthesis validates Sanskrit not solely as an ancient liturgical medium, but as a uniquely potent, highly structured linguistic engine thoroughly capable of accurately codifying, preserving, and transmitting the most advanced mathematical and thermodynamic theorems of the digital age.

#### **Works cited**

1. entropy[1].pdf
2. Technical words in Sanskrit \- Google Groups, accessed March 28, 2026, [https://groups.google.com/g/bvparishat/c/jEXSNnTACu0](https://groups.google.com/g/bvparishat/c/jEXSNnTACu0)
3. Brief Excerpts from Warren Weaver's Introduction to: Claude Shannon's The Mathematical Theory of Communication, accessed March 28, 2026, [https://darkwing.uoregon.edu/~felsing/virtual_asia/info.html](https://darkwing.uoregon.edu/~felsing/virtual_asia/info.html)
4. Information Coding in a language: Some insights from Pāṇinian Grammar \- Department of Sanskrit Studies \- University of Hyderabad, accessed March 28, 2026, [https://sanskrit.uohyd.ac.in/faculty/amba/PUBLICATIONS/papers/info-coding.pdf](https://sanskrit.uohyd.ac.in/faculty/amba/PUBLICATIONS/papers/info-coding.pdf)
5. Binary number \- Wikipedia, accessed March 28, 2026, [https://en.wikipedia.org/wiki/Binary_number](https://en.wikipedia.org/wiki/Binary_number)
6. Pingala \- Wikipedia, accessed March 28, 2026, [https://en.wikipedia.org/wiki/Pingala](https://en.wikipedia.org/wiki/Pingala)
7. Information Theory, Living Systems, and Communication Engineering \- PMC, accessed March 28, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC11120474/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11120474/)
8. Information theory \- Entropy, Coding, Communication | Britannica, accessed March 28, 2026, [https://www.britannica.com/science/information-theory/Classical-information-theory](https://www.britannica.com/science/information-theory/Classical-information-theory)
9. Entropy (information theory) \- Wikipedia, accessed March 28, 2026, [https://en.wikipedia.org/wiki/Entropy_(information_theory)](https://en.wikipedia.org/wiki/Entropy_(information_theory))
10. How Pingala created the Binary Number System \- Indica Today, accessed March 28, 2026, [https://www.indica.today/quick-reads/pingala-created-binary-number-system/](https://www.indica.today/quick-reads/pingala-created-binary-number-system/)
11. Binary logic hidden in the Sanskrit verse \- Organiser, accessed March 28, 2026, [https://organiser.org/2026/02/08/338755/bharat/binary-logic-hidden-in-the-sanskrit-verse/](https://organiser.org/2026/02/08/338755/bharat/binary-logic-hidden-in-the-sanskrit-verse/)
12. CONCEPT OF ENTROPY IN VEDAS \- Anand Kumar Gupta, accessed March 28, 2026, [https://anandkgupta.medium.com/concept-of-entropy-in-vedas-97c8b7b695c7](https://anandkgupta.medium.com/concept-of-entropy-in-vedas-97c8b7b695c7)
13. A Mathematical Theory of Communication, accessed March 28, 2026, [https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf](https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf)
15. Sanskrit for Organic Nomenclature \- ResearchGate, accessed March 28, 2026, [https://www.researchgate.net/publication/377527612_Sanskrit_for_Organic_Nomenclature_Reinventing_a_Model_of_Systematically_Naming_of_Compounds_based_on_a_7_Decades_old_Indian_Dictionary](https://www.researchgate.net/publication/377527612_Sanskrit_for_Organic_Nomenclature_Reinventing_a_Model_of_Systematically_Naming_of_Compounds_based_on_a_7_Decades_old_Indian_Dictionary)
18. Pratyabhijñā Apoha Theory, Shannon–Weaver Information, Saussurean Structure, and Peircean Interpretant Agency \- MDPI, accessed March 28, 2026, [https://www.mdpi.com/2077-1444/9/6/191](https://www.mdpi.com/2077-1444/9/6/191)
26. Connecting Bhagavad Gita to Thermodynamics & Quantum Information \- Reddit, accessed March 28, 2026, [https://www.reddit.com/r/AdvaitaVedanta/comments/1punmen/connecting_bhagavad_gita_to_thermodynamics/](https://www.reddit.com/r/AdvaitaVedanta/comments/1punmen/connecting_bhagavad_gita_to_thermodynamics/)

</div>

<script src="{{ '/assets/js/audio-sync.js' | relative_url }}"></script>

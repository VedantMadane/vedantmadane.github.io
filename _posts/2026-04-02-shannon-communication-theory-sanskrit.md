---
layout: post
title: सूचनासिद्धान्तस्य संस्कृत-संहिता
subtitle: Verse-Centered Shannon Edition
tags: [sanskrit, information-theory, mathematics]
---

<link rel="stylesheet" href="{{ '/assets/css/reader.css' | relative_url }}">

This edition is poetry-first: verses and translations are always visible; derivations and technical exposition are collapsible.

## Name Sanskritization Note

In this post, Claude Shannon is rendered in semantic Sanskrit as **श्रुतदेव सांख्यानाचार्य** for metrical and derivational consistency:

- **Claude -> श्रुतदेव**: from dhatu **श्रु** (to hear) -> **श्रुत** (heard/learned; kta formation) + **देव** (luminous one), yielding "the learned/luminous knower of signal-hearing."
- **Shannon -> सांख्यान**: from **सम् + ख्या** (to enumerate/declare) with nominal derivation into **संख्यानम्** (enumeration), and personalized as **सांख्यान** / **सांख्यानाचार्य** in verse contexts.

<details>
<summary>Why semantic Sanskritization instead of pure transliteration</summary>
<div class="prose-text">
  <p>The source document itself prefers dhatu-based technical neologisms over phonetic borrowing. This edition follows that method so the name-form can participate in meaningful compounds and meter without becoming a foreign phonetic block.</p>
</div>
</details>

## प्रथम-प्रकरणम्: सम्प्रेषण-तन्त्र-व्यवस्था

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
<summary>Commentary and system model</summary>
<div class="prose-text">
  <p>This chapter codifies the canonical source -> transmitter -> channel (+noise) -> receiver -> destination model.</p>
</div>
</details>

## द्वितीय-प्रकरणम्: द्व्यङ्क-मानं तथा प्रस्तार-गणितम्

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
<summary>Commentary and binary bridge</summary>
<div class="prose-text">
  <p>The chapter links Shannon's logarithmic bit measure to Pingala's recursive metrical combinatorics.</p>
</div>
</details>

## तृतीय-प्रकरणम्: अपोहनम् तथा साङ्ख्यिक-प्रक्रिया

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
<summary>Commentary and entropy equation</summary>
<div class="prose-text">
  <p>Core equation: <code>H = -K Σ p_i log p_i</code>. The verses frame entropy, redundancy, and conditional structure in compact mnemonic form.</p>
</div>
</details>

## चतुर्थ-प्रकरणम्: मार्गक्षमता तथा सन्दिग्धता

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
<summary>Commentary and noisy channel theorem</summary>
<div class="prose-text">
  <p>Capacity is expressed as <code>C = max(H(x) - H_y(x))</code>. The chapter encodes the threshold nature of reliable communication.</p>
</div>
</details>

## पञ्चम-प्रकरणम्: निरन्तर-सम्प्रेषणम् ऊष्मागतिकी च

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
<summary>Commentary and Shannon-Hartley form</summary>
<div class="prose-text">
  <p>Continuous-channel bound: <code>C = W log_2((P+N)/N)</code>. The verses encode bandwidth, power, and noise as the final triad.</p>
</div>
</details>

## Closing Note

<details>
<summary>Extended notes and future expansion</summary>
<div class="prose-text">
  <p>This post is transformed from a longer technical manuscript; full derivational tables and bibliography can be appended later.</p>
  <p><strong>Audio sync readiness:</strong> each verse block uses stable <code>data-verse-id</code>, with line-level <code>data-start</code> and <code>data-end</code> placeholders ready for timed recitation alignment.</p>
</div>
</details>

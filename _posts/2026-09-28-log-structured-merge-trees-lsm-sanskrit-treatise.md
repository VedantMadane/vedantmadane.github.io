---
layout: post
title: "स्तम्भसञ्चयपञ्चाशिका : लेखक्रमविधिः (Treatise on Log-Structured Storage, LSM-Trees and Compaction)"
date: 2026-09-28
author: Vedant Madane
categories: [Sanskrit, Distributed Systems, Storage Engines]
tags: [Sanskrit, LSM-Tree, Storage Engines, RocksDB, LevelDB, SSTables, Bloom Filters, Compaction, Distributed Systems, Database Internals]
math: true
mermaid: true
---

# स्तम्भसञ्चयपञ्चाशिका : लेखक्रमविधिः
## Fifty Verses on Log-Structured Storage, LSM-Trees and Compaction Internals

> **ग्रन्थसङ्क्षेपः (Treatise Summary)**:
> An original 50-verse classical Sanskrit technical treatise composed in the sacred Anuṣṭubh meter (अनुष्टुप् छन्दः, पथ्यावक्त्र नियम).
> The work systematically formalizes the architecture and algorithmic mechanics of Log-Structured Merge-Trees (O'Neil et al. 1996, LevelDB, RocksDB, Cassandra): append-only sequential I/O versus B-Tree write amplification, Write-Ahead Logging (WAL) and crash recovery, in-memory SkipList MemTables, immutable on-disk SSTables with sparse block indices and CRC32 footers, probabilistic Bloom filter shielding, Size-Tiered vs Leveled compaction strategies and the RUM Conjecture, Tombstones and safe deletion garbage collection, the read cache hierarchy and multi-way merge iterators, RocksDB column families, NVMe concurrency and WiscKey Key-Value separation.
> Each verse is accompanied by rigorous Pāṇinian morphological analysis (पदच्छेदः व्याकरणञ्च) and comprehensive distributed storage systems commentary.

---

## Canto 1: मङ्गलाचरणं लेखक्रमप्रवेशश्च (Invocation, The Append-Only Log and Random vs Sequential I/O)

### Verse 1

```text
प्रणम्य शारदां देवीं सञ्चयज्ञानरूपिणीम् ।
स्तम्भसञ्चयतन्त्रस्य विधिः सम्यग् विधीयते ॥
```

**पदच्छेदः**: प्रणम्य शारदाम् देवीम् सञ्चय-ज्ञान-रूपिणीम् । स्तम्भ-सञ्चय-तन्त्रस्य विधिः सम्यक् विधीयते ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **प्रणम्य** | `प्र + √नम् + ल्यप्` | कृदन्तरूप अव्यय | अव्ययम् | पूर्वनिपातक्रिया (having bowed in reverence) |
| **शारदाम्** | `शारदा` | स्त्रीलिंग नाम | द्वितीया एकवचन | प्रणामस्य कर्म (Goddess Sarasvatī) |
| **देवीम्** | `देवी` | स्त्रीलिंग नाम | द्वितीया एकवचन | शारदायाः विशेषणम् (the divine goddess) |
| **सञ्चयज्ञानरूपिणीम्** | `सञ्चय + ज्ञान + रूपिणी` | उपपद समास | द्वितीया एकवचन स्त्रीलिंग | दत्तभाण्डारविद्यास्वरूपाम् (embodiment of storage architecture wisdom) |
| **स्तम्भसञ्चयतन्त्रस्य** | `स्तम्भ + सञ्चय + तन्त्र` | षष्ठी-तत्पुरुष नपुंसकलिंग | षष्ठी एकवचन | एल-एस-एम-तन्त्रस्य (of Log-Structured Merge storage) |
| **विधिः** | `विधि` | पुंलिंग नाम | प्रथमा एकवचन | शास्त्रक्रमः (the systematic methodology) |
| **सम्यक्** | `सम्यञ्च्` | क्रियाविशेषण अव्यय | अव्ययम् | यथार्थतया (properly / thoroughly) |
| **विधीयते** | `वि + √धा + लट्` | कर्मणि लट् लकार | प्रथमपुरुष एकवचन | आख्यातम् (is expounded and formulated) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: The opening invocation venerates Goddess Sarasvatī as the supreme embodiment of data storage and knowledge organization before formalizing the mathematical and systems engineering architecture of the Log-Structured Merge-Tree (LSM-Tree), introduced by Patrick O'Neil, Edward O'Neil and Gerhard Weikum in 1996. The treatise addresses the foundational bottleneck of modern data engineering: how to ingest massive, continuous streams of mutations into non-volatile storage without succumbing to the mechanical and physical latency penalties of random in-place updates.

---

### Verse 2

```text
यादृच्छिकेन लेखेन पीड्यते चक्रिका सदा ।
स्थाने स्थाने विकीर्णे तु कालनाशो भवेन्महान् ॥
```

**पदच्छेदः**: यादृच्छिकेन लेखेन पीड्यते चक्रिका सदा । स्थाने स्थाने विकीर्णे तु काल-नाशः भवेत् महान् ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **यादृच्छिकेन** | `यादृच्छिक` | विशेषण | तृतीया एकवचन पुंलिंग | लेखेन इत्यस्य विशेषणम् (by random / non-sequential) |
| **लेखेन** | `लेख` | पुंलिंग नाम | तृतीया एकवचन | करणे तृतीया (by write operations: random in-place I/O) |
| **पीड्यते** | `√पीड् + कर्मणि लट्` | कर्मणि लट् | प्रथमपुरुष एकवचन | बाध्यते (is crippled / throttled) |
| **चक्रिका** | `चक्रिका` | स्त्रीलिंग नाम | प्रथमा एकवचन | सञ्चयपट्टिका (the storage disk / drive platters and flash blocks) |
| **सदा** | `सदा` | अव्ययम् | अव्ययम् | निरन्तरम् (always) |
| **स्थाने** | `स्थान` | नपुंसकलिंग नाम | सप्तमी एकवचन | वीप्सायाम् (at scattered arbitrary physical addresses) |
| **स्थाने** | `स्थान` | नपुंसकलिंग नाम | सप्तमी एकवचन | वीप्सा (across disparate sectors) |
| **विकीर्णे** | `वि + √कॄ + क्त` | कृदन्तरूप सप्तमी एकवचन | सति-सप्तमी | प्रकीर्णे सति (when scattered randomly) |
| **तु** | `तु` | अव्ययम् | अव्ययम् | विशेषे (however) |
| **कालनाशः** | `काल + नाश` | षष्ठी-तत्पुरुष पुंलिंग | प्रथमा एकवचन | विलम्बक्षयः (catastrophic seek-time latency) |
| **भवेत्** | `√भू + विधि-लिङ्` | परस्मैपद लिङ् | प्रथमपुरुष एकवचन | जायेत (occurs) |
| **महान्** | `महत्` | विशेषण पुंलिंग | प्रथमा एकवचन | विशालः (enormous) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: Classical relational databases rely on B-Trees, which mutate records in-place (in-situ update). In traditional magnetic hard disk drives (HDDs), in-place updates force the physical mechanical actuator arm to seek across rotating platters, wasting 5 to 10 milliseconds per write and capping throughput at a meager 100 to 200 IOPS. In solid-state drives (SSDs), random writes force costly erase-block recycles, triggering severe write amplification and premature flash cell burnout.

---

### Verse 3

```text
अनुलेखप्रभावेन गतिर्भवति निर्मला ।
क्रमेण लिखिते चक्रे वेगो वर्धेत कोटिशः ॥
```

**पदच्छेदः**: अनुलेख-प्रभावेन गतिः भवति निर्मला । क्रमेण लिखिते चक्रे वेगः वर्धेत कोटिशः ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **अनुलेखप्रभावेन** | `अनुलेख + प्रभाव` | तृतीया-तत्पुरुष पुंलिंग | तृतीया एकवचन | करणे तृतीया (through the power of append-only sequential logging) |
| **गतिः** | `गति` | स्त्रीलिंग नाम | प्रथमा एकवचन | सञ्चारवेगः (write throughput) |
| **भवति** | `√भू + लट्` | परस्मैपद लट् | प्रथमपुरुष एकवचन | जायते (becomes) |
| **निर्मला** | `निस् + मल` | बहुव्रीहि स्त्रीलिंग | प्रथमा एकवचन | अप्रतिबद्धा (flawless / uninhibited) |
| **क्रमेण** | `क्रम` | पुंलिंग नाम | तृतीया एकवचन | प्रकृत्या तृतीया : आनुपूर्व्या (sequentially in linear order) |
| **लिखिते** | `√लिख् + क्त` | कृदन्तरूप सप्तमी एकवचन | सति-सप्तमी | अङ्किते सति (upon being written) |
| **चक्रे** | `चक्र` | नपुंसकलिंग नाम | सप्तमी एकवचन | डिस्क-पीठे (to the disk track) |
| **वेगः** | `वेग` | पुंलिंग नाम | प्रथमा एकवचन | प्रवाहवेगः (throughput rate) |
| **वर्धेत** | `√वृध् + विधि-लिङ्` | आत्मनेपद लिङ् | प्रथमपुरुष एकवचन | उद्गच्छेत् (multiplies) |
| **कोटिशः** | `कोटि + शस्` | अव्ययम् | अव्ययम् | सहस्रगुणम् (many orders of magnitude) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: The Append-Only Paradigm (anulekha-nyāya): sequential write bandwidth is dramatically faster than random write bandwidth: up to 100 times faster on rotational spinning disks and 10 times faster on modern flash SSDs. By treating the persistent disk strictly as an immutable append-only tape, the storage engine converts expensive random seeks into a continuous, blazing firehose of sequential bytes, maximizing raw hardware bandwidth.

---

### Verse 4

```text
विषमं भ्रमणं त्यक्त्वा सरलं मार्गमाश्रितम् ।
सर्वं लेखनसम्भूतं प्रवाह इव धावति ॥
```

**पदच्छेदः**: विषमम् भ्रमणम् त्यक्त्वा सरलम् मार्गम् आश्रितम् । सर्वम् लेखन-सम्भूतम् प्रवाहः इव धावति ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **विषमम्** | `विषम` | विशेषण | द्वितीया एकवचन नपुंसकलिंग | भ्रमणम् इत्यस्य विशेषणम् (erratic / chaotic) |
| **भ्रमणम्** | `भ्रमण` | नपुंसकलिंग नाम | द्वितीया एकवचन | यादृच्छिकगतिम (random head seek) |
| **त्यक्त्वा** | `√त्यज् + क्त्वा` | कृदन्तरूप अव्यय | अव्ययम् | विहाय (having eliminated) |
| **सरलम्** | `सरल` | विशेषण | द्वितीया एकवचन पुंलिंग | ऋजुम् (linear / sequential) |
| **मार्गम्** | `मार्ग` | पुंलिंग नाम | द्वितीया एकवचन | पन्थानम् (pathway) |
| **आश्रितम्** | `आ + √श्रि + क्त` | कृदन्तरूप नपुंसकलिंग | प्रथमा एकवचन | स्वीकृतम् (adopted) |
| **सर्वम्** | `सर्व` | सर्वनाम | प्रथमा एकवचन नपुंसकलिंग | समस्तम् (all) |
| **लेखनसम्भूतम्** | `लेखन + सम्भूत` | सप्तमी / कर्मधारय नपुंसकलिंग | प्रथमा एकवचन | म्यूटेशन-दत्तम् (mutation write stream) |
| **प्रवाहः** | `प्रवाह` | पुंलिंग नाम | प्रथमा एकवचन | नदीवेगः (a torrential river) |
| **इव** | `इव` | उपमार्थे अव्यय | अव्ययम् | यथा (like) |
| **धावति** | `√धाव् + लट्` | परस्मैपद लट् | प्रथमपुरुष एकवचन | प्रवहति (streams rapidly) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: The core architectural triumph of an LSM-Tree is transforming random in-memory application writes into sequential disk streams. Instead of hunting down the existing on-disk location of a key to modify it in-place, the engine simply appends the latest version to the end of a log. Writes race to disk like an unimpeded river, decoupling user request latency from the mechanical latency of on-disk data reorganization.

---

### Verse 5

```text
विपुलस्य च भारस्य रक्षणाय विधीयते ।
नूतनानां हि विदुषां स्तम्भसञ्चयपद्धतिः ॥
```

**पदच्छेदः**: विपुलस्य च भारस्य रक्षणाय विधीयते । नूतनानाम् हि विदुषाम् स्तम्भ-सञ्चय-पद्धतिः ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **विपुलस्य** | `विपुल` | विशेषण | षष्ठी एकवचन पुंलिंग | भारस्य विशेषणम् (of massive / petabyte-scale) |
| **च** | `च` | अव्ययम् | अव्ययम् | संयोजकः (and) |
| **भारस्य** | `भार` | पुंलिंग नाम | षष्ठी एकवचन | इन्जेशन-भारस्य (of high-throughput write workloads) |
| **रक्षणाय** | `रक्षण` | नपुंसकलिंग नाम | चतुर्थी एकवचन | तादर्थ्ये चतुर्थी : पालनाय (for sustaining) |
| **विधीयते** | `वि + √धा + कर्मणि लट्` | कर्मणि लट् | प्रथमपुरुष एकवचन | रच्यते (is engineered) |
| **नूतनानाम्** | `नूतन` | विशेषण | षष्ठी बहुवचन पुंलिंग | विदुषाम् विशेषणम् (of modern) |
| **हि** | `हि` | अव्ययम् | अव्ययम् | प्रसिद्धौ (indeed) |
| **विदुषाम्** | `विद्वस्` | पुंलिंग नाम | षष्ठी बहुवचन | तन्त्रज्ञानाम् (of systems engineers) |
| **स्तम्भसञ्चयपद्धतिः** | `स्तम्भ + सञ्चय + पद्धति` | षष्ठी-तत्पुरुष स्त्रीलिंग | प्रथमा एकवचन | एल-एस-एम-विधिः (the Log-Structured Merge-Tree architecture) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: Modern internet applications: social media activity feeds, time-series metrics, telemetry streams, messaging backbones and financial ledgers: generate petabytes of continuous write traffic. Traditional B-Tree database engines stall under this assault due to lock contention and random I/O thrashing. The LSM-Tree was engineered specifically to conquer write-heavy workloads, powering Google Bigtable, Apache Cassandra, RocksDB and ScyllaDB.

---

## Canto 2: पूर्वलेखनविधिः सुरक्षाकवचञ्च (Write-Ahead Log (WAL), Durability and Crash Recovery)

### Verse 6

```text
अस्थिरं मन्यते चित्तं विद्युद्भाण्डारकं तथा ।
स्थायिनि चक्रिकापीठे स्थापनीयं परं धनम् ॥
```

**पदच्छेदः**: अस्थिरम् मन्यते चित्तम् विद्युत्-भाण्डारकम् तथा । स्थायिनि चक्रिका-पीठे स्थापनीयम् परम् धनम् ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **अस्थिरम्** | `अ + स्थिर` | नञ्-तत्पुरुष नपुंसकलिंग | प्रथमा एकवचन | चञ्चलम् (volatile / transient) |
| **मन्यते** | `√मन् + कर्मणि/आत्मनेपद लट्` | आत्मनेपद लट् | प्रथमपुरुष एकवचन | ज्ञायते (is known to be) |
| **चित्तम्** | `चित्त` | नपुंसकलिंग नाम | प्रथमा एकवचन | मानसम (the mind) |
| **विद्युद्भाण्डारकम्** | `विद्युत् + भाण्डारक` | कर्मधारय नपुंसकलिंग | प्रथमा एकवचन | र्याम्-स्मृतिः (volatile electronic RAM memory) |
| **तथा** | `तथा` | अव्ययम् | अव्ययम् | तद्वत् (likewise) |
| **स्थायिनि** | `स्थायिन्` | विशेषण | सप्तमी एकवचन नपुंसकलिंग | पीठे विशेषणम् (in persistent non-volatile) |
| **चक्रिकापीठे** | `चक्रिका + पीठ` | सप्तमी एकवचन नपुंसकलिंग | सप्तमी एकवचन | डिस्क-माध्यमे (on persistent disk substrate) |
| **स्थापनीयम्** | `स्था + णिच् + अनीयर्` | कृदन्तरूप नपुंसकलिंग | प्रथमा एकवचन | निक्षेपणीयम् (must be placed) |
| **परम्** | `परम` | विशेषण | प्रथमा एकवचन नपुंसकलिंग | मूल्यवान् (precious) |
| **धनम्** | `धन` | नपुंसकलिंग नाम | प्रथमा एकवचन | दत्तवस्तु (payload data treasure) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: The Durability Challenge: Volatile RAM is blindingly fast (sub-100 nanosecond latency), but it is perishable. A sudden power outage, kernel panic, or hardware failure wipes volatile memory clean in an instant. Persistent non-volatile media (NVMe, SSD, HDD) survives power cuts, but writes to persistent media incur latency. The storage engine must reconcile this fundamental tension to fulfill the ACID Durability guarantee.

---

### Verse 7

```text
पूर्वलेखविधानेन लिख्यते सर्वथा पुरा ।
नश्यत्यपि हि सम्भारो न नाशस्तत्र जायते ॥
```

**पदच्छेदः**: पूर्व-लेख-विधानेन लिख्यते सर्वथा पुरा । नश्यति अपि हि सम्भारः न नाशः तत्र जायते ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **पूर्वलेखविधानेन** | `पूर्व + लेख + विधान` | तत्पुरुष नपुंसकलिंग | तृतीया एकवचन | करणे तृतीया (through the Write-Ahead Log protocol) |
| **लिख्यते** | `√लिख् + कर्मणि लट्` | कर्मणि लट् | प्रथमपुरुष एकवचन | अङ्क्यते (is recorded) |
| **सर्वथा** | `सर्वथा` | अव्ययम् | अव्ययम् | अनिवार्यरूपेण (invariably) |
| **पुरा** | `पुरा` | कालवाचक अव्यय | अव्ययम् | स्मृतिप्रवेशात् पूर्वम् (before in-memory mutation) |
| **नश्यति** | `√नश् + लट्` | परस्मैपद लट् | प्रथमपुरुष एकवचन | सति-सप्तमीवत् (even if RAM power crashes) |
| **अपि** | `अपि` | अव्ययम् | अव्ययम् | संभावनार्थे (even) |
| **हि** | `हि` | अव्ययम् | अव्ययम् | निश्चये (verily) |
| **सम्भारः** | `सम्भार` | पुंलिंग नाम | प्रथमा एकवचन | स्मृतिस्थदत्तम् (in-memory buffered data) |
| **न** | `न` | निषेधार्थक अव्यय | अव्ययम् | निषेधे (no) |
| **नाशः** | `नाश` | पुंलिंग नाम | प्रथमा एकवचन | स्थायी विनाशः (permanent data loss) |
| **तत्र** | `तत्र` | अव्ययम् | अव्ययम् | तस्मिन् व्यवहारे (therein) |
| **जायते** | `√जन् + लट्` | आत्मनेपद लट् | प्रथमपुरुष एकवचन | भवति (occurs) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: The Write-Ahead Log (WAL / pūrva-lekha): before any mutation (PUT or DELETE) is inserted into the volatile in-memory buffer (MemTable), it is serialized and appended to an on-disk sequential log file (the WAL). Because appending a sequential record to the end of a log file requires zero directory index reorganization or page splits, it is fast. Even if the server crashes immediately after, the operation is durably preserved on disk.

---

### Verse 8

```text
क्षणे क्षणे दृढीकृत्य लेखः चक्रे समर्प्यते ।
विलम्बेन समं युद्धं स्थैर्यं संपाद्यते परम् ॥
```

**पदच्छेदः**: क्षणे क्षणे दृढीकृत्य लेखः चक्रे समर्प्यते । विलम्बेन समम् युद्धम् स्थैर्यम् संपाद्यते परम् ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **क्षणे** | `क्षण` | पुंलिंग नाम | सप्तमी एकवचन | वीप्सायाम् (at every instant) |
| **क्षणे** | `क्षण` | पुंलिंग नाम | सप्तमी एकवचन | निरन्तरम् (upon each write / periodically) |
| **दृढीकृत्य** | `दृढ + च्वि + √कृ + ल्यप्` | कृदन्तरूप अव्यय | अव्ययम् | एफ-सिङ्क-विधिना (having executed fsync to flush OS buffers) |
| **लेखः** | `लेख` | पुंलिंग नाम | प्रथमा एकवचन | अभिलेखः (the log record) |
| **चक्रे** | `चक्र` | नपुंसकलिंग नाम | सप्तमी एकवचन | स्थायिनि पट्टे (to physical disk media) |
| **समर्प्यते** | `सम् + √ऋ + णिच् + कर्मणि लट्` | कर्मणि लट् | प्रथमपुरुष एकवचन | प्रदीयते (is committed) |
| **विलम्बेन** | `विलम्ब` | पुंलिंग नाम | तृतीया एकवचन | सहार्थे तृतीया : कालक्षेपेण (against write latency) |
| **समम्** | `समम्` | अव्ययम् | अव्ययम् | सह (along with) |
| **युद्धम्** | `युद्ध` | नपुंसकलिंग नाम | प्रथमा एकवचन | सङ्ग्रामः (the trade-off conflict) |
| **स्थैर्यम्** | `स्थैर्य` | नपुंसकलिंग नाम | प्रथमा एकवचन | स्थायित्वम् (absolute durability) |
| **संपाद्यते** | `सम् + √पद् + णिच् + कर्मणि लट्` | कर्मणि लट् | प्रथमपुरुष एकवचन | सिद्ध्यति (is achieved) |
| **परम्** | `परम` | विशेषण नपुंसकलिंग | प्रथमा एकवचन | उत्तमम् (supreme) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: The Fsync Dilemma: Writing to an on-disk file initially puts data into the operating system page cache. To guarantee physical non-volatile persistence, the storage engine must execute an fsync() system call, forcing the disk controller to flush its internal volatile caches. Systems can configure fsync policies: calling fsync synchronously on every single write guarantees zero data loss but caps throughput at disk spindle speeds, while group-committing or periodic 1-second flushing trades a tiny window of vulnerability for orders-of-magnitude higher throughput.

---

### Verse 9

```text
विनाशे समनुप्राप्ते प्रबोधे पुनरागते ।
पुनरावर्तनाद् लेखात् सर्वं सत्यं प्रजायते ॥
```

**पदच्छेदः**: विनाशे सम्-अनु-प्राप्ते प्रबोधे पुनर्-आगते । पुनर्-आवर्तनात् लेखात् सर्वम् सत्यम् प्रजायते ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **विनाशे** | `विनाश` | पुंलिंग नाम | सप्तमी एकवचन | सति-सप्तमी (upon server crash / power loss) |
| **समनुप्राप्ते** | `सम् + अनु + प्र + √आप् + क्त` | कृदन्तरूप सप्तमी एकवचन | सति-सप्तमी | पतिते सति (having occurred) |
| **प्रबोधे** | `प्रबोध` | पुंलिंग नाम | सप्तमी एकवचन | सति-सप्तमी (upon machine reboot / awakening) |
| **पुनरागते** | `पुनर् + आ + √गम् + क्त` | कृदन्तरूप सप्तमी एकवचन | सति-सप्तमी | पुनः प्राप्ते (having returned) |
| **पुनरावर्तनात्** | `पुनर् + आवर्तन` | पञ्चमी एकवचन नपुंसकलिंग | हेतौ पञ्चमी | रिप्ले-करणेन (by replaying the log) |
| **लेखात्** | `लेख` | पुंलिंग नाम | पञ्चमी एकवचन | अपादाने पञ्चमी : वाल्-सञ्चयात् (from the Write-Ahead Log) |
| **सर्वम्** | `सर्व` | सर्वनाम | प्रथमा एकवचन नपुंसकलिंग | समस्तम् (all) |
| **सत्यम्** | `सत्य` | नपुंसकलिंग नाम | प्रथमा एकवचन | प्रमाणीभूतम् (state ground truth) |
| **प्रजायते** | `प्र + √जन् + लट्` | आत्मनेपद लट् | प्रथमपुरुष एकवचन | पुनरुज्जीवति (is perfectly reconstructed) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: Crash Recovery: when a database engine restarts after a catastrophic crash, its memory is blank. It initiates recovery by opening the WAL segments that were written since the last successful on-disk checkpoint. By sequentially scanning and replaying these log records into a fresh MemTable, the engine reconstructs the exact in-memory state that existed at the microsecond of power failure, guaranteeing zero committed transaction loss.

---

### Verse 10

```text
खण्डं खण्डं समाधाय पुरातनं विमुञ्चति ।
अवशिष्टस्य संशुद्धिः क्रियते विबुधैः सदा ॥
```

**पदच्छेदः**: खण्डम् खण्डम् सम्-आधाय पुरातनम् विमुञ्चति । अवशिष्टस्य संशुद्धिः क्रियते विबुधैः सदा ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **खण्डम्** | `खण्ड` | पुंलिंग नाम | द्वितीया एकवचन | वीप्सायाम् (segment by segment) |
| **खण्डम्** | `खण्ड` | पुंलिंग नाम | द्वितीया एकवचन | लॉग-सेगमेण्ट (segmented WAL files) |
| **समाधाय** | `सम् + आ + √धा + ल्यप्` | कृदन्तरूप अव्यय | अव्ययम् | विभज्य (having structured) |
| **पुरातनम्** | `पुरातन` | विशेषण पुंलिंग | द्वितीया एकवचन | भूतपूर्वम् (the obsolete log segment) |
| **विमुञ्चति** | `वि + √मुच् + लट्` | परस्मैपद लट् | प्रथमपुरुष एकवचन | परित्यजति (discards / deletes) |
| **अवशिष्टस्य** | `अव + √शिष् + क्त` | कृदन्तरूप षष्ठी एकवचन | षष्ठी एकवचन | सञ्चितस्य (of the remaining log files) |
| **संशुद्धिः** | `सम् + शुद्धि` | स्त्रीलिंग नाम | प्रथमा एकवचन | अपमर्जनम् (garbage collection) |
| **क्रियते** | `√कृ + कर्मणि लट्` | कर्मणि लट् | प्रथमपुरुष एकवचन | अनुष्ठीयते (is executed) |
| **विबुधैः** | `विबुध` | पुंलिंग नाम | तृतीया बहुवचन | तन्त्रज्ञैः (by systems architects) |
| **सदा** | `सदा` | अव्ययम् | अव्ययम् | सर्वदा (perpetually) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: WAL Garbage Collection: a WAL cannot grow infinitely without consuming all storage capacity and making restart recovery painfully slow. Once the corresponding in-memory MemTable has been successfully flushed and written to an immutable on-disk SSTable, all WAL records belonging to that generation become redundant. The engine seals, unlinks and deletes those obsolete WAL segments, keeping storage consumption tightly bounded.

---

## Canto 3: स्मृतिभाण्डारः क्रमबद्धस्थापनञ्च (MemTable: Sorted In-Memory Mutation Buffers and SkipLists)

### Verse 11

```text
स्मृतौ प्रतिष्ठितः कोषो लिख्यते द्रुतवेगतः ।
कुञ्चिकानां समूहोऽयं क्रमबद्धो विधीयते ॥
```

**पदच्छेदः**: स्मृतौ प्रतिष्ठितः कोषः लिख्यते द्रुत-वेगतः । कुञ्चिकानाम् समूहः अयम् क्रम-बद्धः विधीयते ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **स्मृतौ** | `स्मृति` | स्त्रीलिंग नाम | सप्तमी एकवचन | र्याम्-मध्ये (in volatile RAM memory) |
| **प्रतिष्ठितः** | `प्रति + √स्था + क्त` | कृदन्तरूप पुंलिंग | प्रथमा एकवचन | अवस्थितः (established) |
| **कोषः** | `कोष` | पुंलिंग नाम | प्रथमा एकवचन | मेमटेबल (the MemTable buffer) |
| **लिख्यते** | `√लिख् + कर्मणि लट्` | कर्मणि लट् | प्रथमपुरुष एकवचन | क्रियते (is written to) |
| **द्रुतवेगतः** | `द्रुत + वेग + तसिँ` | अव्ययम् | अव्ययम् | शीघ्रतया (at ultra-fast CPU memory speeds) |
| **कुञ्चिकानाम्** | `कुञ्चिका` | स्त्रीलिंग नाम | षष्ठी बहुवचन | दत्तकुञ्चिकानाम् (of keys and records) |
| **समूहः** | `समूह` | पुंलिंग नाम | प्रथमा एकवचन | सञ्चयः (collection / set) |
| **अयम्** | `इदम्` | सर्वनाम पुंलिंग | प्रथमा एकवचन | समूहस्य विशेषणम् (this) |
| **क्रमबद्धः** | `क्रम + बद्ध` | तृतीया-तत्पुरुष पुंलिंग | प्रथमा एकवचन | वर्गीकृतः / आरोहिक्रमेण (strictly ordered / sorted) |
| **विधीयते** | `वि + √धा + कर्मणि लट्` | कर्मणि लट् | प्रथमपुरुष एकवचन | स्थाप्यते (is maintained) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: The MemTable (smṛti-bhāṇḍāra): simultaneously with appending to the on-disk WAL, the storage engine writes the incoming mutation into an in-memory buffer called the MemTable. Crucially, while writes arrive in arbitrary, randomized key order, the MemTable does not store them arbitrarily: it maintains all keys in strictly sorted order at all times. This sorted in-memory structure forms the foundation for high-performance range scans and ordered disk flushes.

---

### Verse 12

```text
लङ्घनस्य च मार्गेण पादपेन च रक्ष्यते ।
रोधमुक्तः सदा पन्था दृश्यते सुसमाहितः ॥
```

**पदच्छेदः**: लङ्घनस्य च मार्गेण पादपेन च रक्ष्यते । रोध-मुक्तः सदा पन्थाः दृश्यते सु-समाहितः ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **लङ्घनस्य** | `लङ्घन` | नपुंसकलिंग नाम | षष्ठी एकवचन | स्किप-लिस्ट-पद्धतेः (of the SkipList data structure) |
| **च** | `च` | अव्ययम् | अव्ययम् | संयोजकः (and) |
| **मार्गेण** | `मार्ग` | पुंलिंग नाम | तृतीया एकवचन | करणे तृतीया (by means of the algorithm) |
| **पादपेन** | `पादप` | पुंलिंग नाम | तृतीया एकवचन | वृक्षसंरचनया (by Red-Black / AVL trees) |
| **च** | `च` | अव्ययम् | अव्ययम् | समुच्चये (or) |
| **रक्ष्यते** | `√रक्ष् + कर्मणि लट्` | कर्मणि लट् | प्रथमपुरुष एकवचन | संरक्ष्यते (is maintained) |
| **रोधमुक्तः** | `रोध + मुक्त` | तृतीया-तत्पुरुष पुंलिंग | प्रथमा एकवचन | तालाविहीनः (lock-free / concurrent) |
| **सदा** | `सदा` | अव्ययम् | अव्ययम् | सर्वदा (perpetually) |
| **पन्थाः** | `पथिन्` | पुंलिंग नाम | प्रथमा एकवचन | मार्गः (execution path) |
| **दृश्यते** | `√दृश् + कर्मणि लट्` | कर्मणि लट् | प्रथमपुरुष एकवचन | अवलोक्यते (is observed) |
| **सुसमाहितः** | `सु + सम् + आ + √धा + क्त` | कृदन्तरूप पुंलिंग | प्रथमा एकवचन | दक्षः (well-balanced / optimal) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: Underlying Data Structures: How does the MemTable maintain keys in sorted order under high concurrency? While self-balancing binary search trees (Red-Black trees) require complex rebalancing rotations that mandate coarse-grained locks, LevelDB and RocksDB utilize SkipLists (laṅghana-sūcī). A SkipList uses probabilistic multi-level forward pointers to achieve O(log N) search and insertion while allowing lock-free concurrent reads and concurrent append operations via atomic compare-and-swap (CAS).

---

### Verse 13

```text
नूतनेन प्रविष्टेन पुरातनं विपद्यते ।
मृत्युमुद्रां समादाय विनाशोऽपि समाश्रितः ॥
```

**पदच्छेदः**: नूतनेन प्रविष्टेन पुरातनम् विपद्यते । मृत्यु-मुद्राम् सम्-आदाय विनाशः अपि सम्-आश्रितः ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **नूतनेन** | `नूतन` | विशेषण | तृतीया एकवचन पुंलिंग | प्रविष्टेन विशेषणम् (by the newly entered) |
| **प्रविष्टेन** | `प्र + √विश् + क्त` | कृदन्तरूप पुंलिंग | तृतीया एकवचन | संस्करणेन (mutation version) |
| **पुरातनम्** | `पुरातन` | विशेषण | प्रथमा एकवचन नपुंसकलिंग | पूर्वतनं दत्तम् (the older value) |
| **विपद्यते** | `वि + √पद् + लट्` | आत्मनेपद लट् | प्रथमपुरुष एकवचन | अभिभूयते (is superseded / masked) |
| **मृत्युमुद्राम्** | `मृत्यु + मुद्रा` | षष्ठी-तत्पुरुष स्त्रीलिंग | द्वितीया एकवचन | टॉम्बस्टोन-चिह्नम् (the Tombstone marker) |
| **समादाय** | `सम् + आ + √दा + ल्यप्` | कृदन्तरूप अव्यय | अव्ययम् | धारयित्वा (having attached) |
| **विनाशः** | `विनाश` | पुंलिंग नाम | प्रथमा एकवचन | विलोपनम् (deletion operation) |
| **अपि** | `अपि` | अव्ययम् | अव्ययम् | समुच्चये (also) |
| **समाश्रितः** | `सम् + आ + √श्रि + क्त` | कृदन्तरूप पुंलिंग | प्रथमा एकवचन | अनुष्ठितः (is implemented) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: Mutations and Tombstones: In an LSM-Tree, an UPDATE operation is identical to an INSERT: a new record with the identical key but a higher sequence number is appended into the MemTable, naturally shadowing and superseding any older version. Deletions cannot delete anything in-place; instead, a DELETE operation is executed as a special write that inserts a Tombstone (mṛtyu-mudrā): a deletion marker that records that the key has been logically erased.

---

### Verse 14

```text
यदा पूर्णो भवेत् कोषः सीमान्तं प्राप्य चेतसा ।
स्तब्धीभूतोऽपरो भागो जायते शुद्धिरुत्तमा ॥
```

**पदच्छेदः**: यदा पूर्णः भवेत् कोषः सीमा-अन्तम् प्राप्य चेतसा । स्तब्धी-भूतः अपरः भागः जायते शुद्धिः उत्तमा ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **यदा** | `यदा` | कालवाचक अव्यय | अव्ययम् | यस्मिन् क्षणे (when) |
| **पूर्णः** | `√पॄ + क्त` | कृदन्तरूप पुंलिंग | प्रथमा एकवचन | सम्भृतः (filled to capacity) |
| **भवेत्** | `√भू + विधि-लिङ्` | परस्मैपद लिङ् | प्रथमपुरुष एकवचन | जायेत (becomes) |
| **कोषः** | `कोष` | पुंलिंग नाम | प्रथमा एकवचन | मेमटेबल (the MemTable) |
| **सीमान्तम्** | `सीमा + अन्त` | कर्मधारय पुंलिंग | द्वितीया एकवचन | परिमाणमर्यादाम् (the size threshold: e.g. 64MB) |
| **प्राप्य** | `प्र + √आप् + ल्यप्` | कृदन्तरूप अव्यय | अव्ययम् | अधिरुह्य (having reached) |
| **चेतसा** | `चेतस्` | नपुंसकलिंग नाम | तृतीया एकवचन | नियमेन (by heuristic calculation) |
| **स्तब्धीभूतः** | `स्तब्ध + च्वि + √भू + क्त` | कृदन्तरूप पुंलिंग | प्रथमा एकवचन | अपरिवर्तनीयः (frozen / made immutable) |
| **अपरः** | `अपर` | विशेषण पुंलिंग | प्रथमा एकवचन | द्वितीयः (a second) |
| **भागः** | `भाग` | पुंलिंग नाम | प्रथमा एकवचन | मेमटेबल-खण्डः (buffer instance) |
| **जायते** | `√जन् + लट्` | आत्मनेपद लट् | प्रथमपुरुष एकवचन | जायते (becomes) |
| **शुद्धिः** | `शुद्धि` | स्त्रीलिंग नाम | प्रथमा एकवचन | परिशोधनम् (flushing readiness) |
| **उत्तमा** | `उत्तम` | विशेषण स्त्रीलिंग | प्रथमा एकवचन | श्रेष्ठा (optimal) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: MemTable Capacity Threshold: A MemTable cannot expand indefinitely in RAM. Once its byte size crosses a configured threshold (typically 32MB to 256MB in production systems like RocksDB), the engine initiates a transition: it freezes the active MemTable into an immutable (read-only) MemTable, while simultaneously allocating a fresh active MemTable to receive incoming client writes without pausing the system.

---

### Verse 15

```text
अचलं तं समाधाय नूतनः क्रियते पुनः ।
अविरामं प्रवृत्तोऽयं लेखनस्य महाक्रमः ॥
```

**पदच्छेदः**: अचलम् तम् सम्-आधाय नूतनः क्रियते पुनः । अविरामम् प्रवृत्तः अयम् लेखनस्य महा-क्रमः ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **अचलम्** | `अ + चल` | नञ्-तत्पुरुष पुंलिंग | द्वितीया एकवचन | अपरिवर्त्यम् (immutable) |
| **तम्** | `तद्` | सर्वनाम पुंलिंग | द्वितीया एकवचन | मेमटेबल-भागम् (that frozen buffer) |
| **समाधाय** | `सम् + आ + √धा + ल्यप्` | कृदन्तरूप अव्यय | अव्ययम् | कृत्वा (having converted) |
| **नूतनः** | `नूतन` | विशेषण पुंलिंग | प्रथमा एकवचन | नवीनः (a new active buffer) |
| **क्रियते** | `√कृ + कर्मणि लट्` | कर्मणि लट् | प्रथमपुरुष एकवचन | रच्यते (is created) |
| **पुनः** | `पुनर्` | अव्ययम् | अव्ययम् | भूयः (again) |
| **अविरामम्** | `अ + विरामम्` | क्रियाविशेषण अव्यय | अव्ययम् | अनवरतम् (without interruption / non-blocking) |
| **प्रवृत्तः** | `प्र + √वृत् + क्त` | कृदन्तरूप पुंलिंग | प्रथमा एकवचन | निरन्तरः (active) |
| **अयम्** | `इदम्` | सर्वनाम पुंलिंग | प्रथमा एकवचन | क्रमस्य विशेषणम् (this) |
| **लेखनस्य** | `लेखन` | नपुंसकलिंग नाम | षष्ठी एकवचन | अभिलेखनस्य (of writing) |
| **महाक्रमः** | `महत् + क्रम` | कर्मधारय पुंलिंग | प्रथमा एकवचन | महान् प्रवाहः (grand ingestion pipeline) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: Non-blocking Ingestion: Freezing the old MemTable into an immutable buffer ensures zero write stalls. The new active MemTable accepts incoming PUTs and DELETEs uninterruptedly, while a background thread pool picks up the immutable MemTable and streams its contents to disk as a brand-new Sorted String Table (SSTable). The write pipeline operates as an unceasing assembly line.

---

## Canto 4: अचलशिलाखण्डाः स्तरविन्यासश्च (SSTables: Sorted String Tables, Block Indices and Checksums)

### Verse 16

```text
शिलापत्रमिव स्थैर्यं याति चक्रे समाहितम् ।
अपरिवर्त्यरूपेण सर्वं न्यस्तं विधीयते ॥
```

**पदच्छेदः**: शिला-पत्रम् इव स्थैर्यम् याति चक्रे सम्-आहितम् । अपरिवर्त्य-रूपेण सर्वम् न्यस्तम् विधीयते ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **शिलापत्रम्** | `शिला + पत्र` | कर्मधारय नपुंसकलिंग | द्वितीया एकवचन | शिलाखण्डम् (an inscription carved on a stone slab / SSTable) |
| **इव** | `इव` | उपमार्थे अव्यय | अव्ययम् | यथा (like) |
| **स्थैर्यम्** | `स्थैर्य` | नपुंसकलिंग नाम | द्वितीया एकवचन | नित्यताम् (immutability / permanence) |
| **याति** | `√या + लट्` | परस्मैपद लट् | प्रथमपुरुष एकवचन | गच्छति (attains) |
| **चक्रे** | `चक्र` | नपुंसकलिंग नाम | सप्तमी एकवचन | डिस्क-पीठे (on persistent disk) |
| **समाहितम्** | `सम् + आ + √धा + क्त` | कृदन्तरूप नपुंसकलिंग | प्रथमा एकवचन | स्थापितम् (deposited) |
| **अपरिवर्त्यरूपेण** | `अ + परिवर्त्य + रूप` | तृतीया एकवचन नपुंसकलिंग | तृतीया एकवचन | अविकार्यतया (in immutable form) |
| **सर्वम्** | `सर्व` | सर्वनाम | प्रथमा एकवचन नपुंसकलिंग | दत्तम् (all data) |
| **न्यस्तम्** | `नि + √अस् + क्त` | कृदन्तरूप नपुंसकलिंग | प्रथमा एकवचन | लिखितम् (written) |
| **विधीयते** | `वि + √धा + कर्मणि लट्` | कर्मणि लट् | प्रथमपुरुष एकवचन | शास्यते (is ordained) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: SSTables (Sorted String Tables / sthira-śilā-patra): once written to disk, an SSTable file is completely immutable. It is never modified, appended to, or updated in-place. Like edicts carved onto stone slabs, SSTables exist permanently in their created state until whole files are unlinked and replaced during compaction. Immutability eliminates file-level write locking, concurrency race conditions and disk corruption.

---

### Verse 17

```text
स्मृतेर्निःसारितं वस्तु प्रवाहाकारसंप्लुतम् ।
भ्रमणं न भवेद् क्वापि धारा संपद्यते द्रुतम् ॥
```

**पदच्छेदः**: स्मृतेः निःसारितम् वस्तु प्रवाह-आकार-संप्लुतम् । भ्रमणम् न भवेत् क्वापि धारा सम्-पद्यते द्रुतम् ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **स्मृतेः** | `स्मृति` | स्त्रीलिंग नाम | पञ्चमी एकवचन | र्याम्-भाण्डारात् (from the in-memory MemTable) |
| **निःसारितम्** | `निस् + √सृ + णिच् + क्त` | कृदन्तरूप नपुंसकलिंग | प्रथमा एकवचन | प्रवाहितम् (flushed to disk) |
| **वस्तु** | `वस्तु` | नपुंसकलिंग नाम | प्रथमा एकवचन | दत्तभाण्डारम् (data payload) |
| **प्रवाहाकारसंप्लुतम्** | `प्रवाह + आकार + संप्लुत` | बहुव्रीहि नपुंसकलिंग | प्रथमा एकवचन | क्रमानुसृतम् (continuous sequential byte stream) |
| **भ्रमणम्** | `भ्रमण` | नपुंसकलिंग नाम | प्रथमा एकवचन | सीक्-भ्रमणम् (mechanical head seek) |
| **न** | `न` | निषेधार्थक अव्यय | अव्ययम् | निषेधे (not) |
| **भवेत्** | `√भू + विधि-लिङ्` | परस्मैपद लिङ् | प्रथमपुरुष एकवचन | स्यात् (occurs) |
| **क्वापि** | `क्व + अपि` | अव्ययम् | अव्ययम् | कुत्रापि (anywhere) |
| **धारा** | `धारा` | स्त्रीलिंग नाम | प्रथमा एकवचन | अविच्छिन्ना सरित् (sequential disk stream) |
| **संपद्यते** | `सम् + √पद् + लट्` | आत्मनेपद लट् | प्रथमपुरुष एकवचन | सिद्ध्यति (is accomplished) |
| **द्रुतम्** | `द्रुतम्` | क्रियाविशेषण अव्यय | अव्ययम् | शीघ्रम् (rapidly) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: The Flush Operation: because the MemTable was already sorted in RAM, writing it to disk requires zero sorting overhead. The background thread simply iterates through the SkipList from lowest key to highest key, serializing data blocks and writing them out as a single contiguous sequential stream to an SSTable file on disk. The disk head stays pinned in sequential write mode, achieving 100% of maximum hardware write bandwidth.

---

### Verse 18

```text
अचले लिखिते चक्रे न भयं कलहस्य च ।
सर्वे पश्यन्ति शान्तेन न कश्चिद् वार्यते जनैः ॥
```

**पदच्छेदः**: अचले लिखिते चक्रे न भयम् कलहस्य च । सर्वे पश्यन्ति शान्तेन न कश्चित् वार्यते जनैः ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **अचले** | `अचल` | विशेषण | सप्तमी एकवचन नपुंसकलिंग | चक्रे विशेषणम् (in immutable on-disk) |
| **लिखिते** | `√लिख् + क्त` | कृदन्तरूप सप्तमी एकवचन | सति-सप्तमी | अङ्किते (SSTable file) |
| **चक्रे** | `चक्र` | नपुंसकलिंग नाम | सप्तमी एकवचन | सञ्चयस्थाने (in storage) |
| **न** | `न` | निषेधार्थक अव्यय | अव्ययम् | निषेधे (no) |
| **भयम्** | `भय` | नपुंसकलिंग नाम | प्रथमा एकवचन | त्रासः (fear / risk) |
| **कलहस्य** | `कलह` | पुंलिंग नाम | षष्ठी एकवचन | रेस्-कन्डीशन / लॉक-कलहस्य (of lock contention and concurrency races) |
| **च** | `च` | अव्ययम् | अव्ययम् | संयोजकः (and) |
| **सर्वे** | `सर्व` | सर्वनाम पुंलिंग | प्रथमा बहुवचन | पाठकाः (all reader threads) |
| **पश्यन्ति** | `√दृश् + लट्` | परस्मैपद लट् | प्रथमपुरुष बहुवचन | पठन्ति (read / query) |
| **शान्तेन** | `शान्त` | विशेषण | तृतीया एकवचन नपुंसकलिंग | क्रियाविशेषणवत् : विनावरोधेन (peacefully without locks) |
| **न** | `न` | निषेधार्थक अव्यय | अव्ययम् | निषेधे (not) |
| **कश्चित्** | `किम् + चित्` | सर्वनाम पुंलिंग | प्रथमा एकवचन | कोऽपि पाठकः (any reader thread) |
| **वार्यते** | `√वृ + णिच् + कर्मणि लट्` | कर्मणि लट् | प्रथमपुरुष एकवचन | अवरुद्ध्यते (is blocked) |
| **जनैः** | `जन` | पुंलिंग नाम | तृतीया बहुवचन | लेखकैः (by writer threads) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: Lock-Free Concurrency through Immutability: in traditional B-Trees, reading a page while another thread is splitting it requires complex, heavyweight latching protocols (latch crabbing). In an LSM-Tree, because SSTables are read-only and immutable, multiple reader threads can scan, seek and query the same SSTable simultaneously with zero locking overhead. Writers never block readers and readers never block writers.

---

### Verse 19

```text
द्विधा विभक्तो ग्रन्थोऽयं मूलं सूची तथैव च ।
अल्पावलोकनमात्रेण स्थानं ज्ञायेत सत्वरम् ॥
```

**पदच्छेदः**: द्विधा विभक्तः ग्रन्थः अयम् मूलम् सूची तथा एव च । अल्प-अवलोकन-मात्रेण स्थानम् ज्ञायेत सत्वरम् ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **द्विधा** | `द्विधा` | प्रकारवाचक अव्यय | अव्ययम् | द्विप्रकारेण (into two parts) |
| **विभक्तः** | `वि + √भज् + क्त` | कृदन्तरूप पुंलिंग | प्रथमा एकवचन | विभाजितः (partitioned) |
| **ग्रन्थः** | `ग्रन्थ` | पुंलिंग नाम | प्रथमा एकवचन | एस-एस-टेबल (the SSTable file) |
| **अयम्** | `इदम्` | सर्वनाम पुंलिंग | प्रथमा एकवचन | ग्रन्थस्य विशेषणम् (this) |
| **मूलम्** | `मूल` | नपुंसकलिंग नाम | प्रथमा एकवचन | दत्तखण्डाः (data blocks: e.g. 4KB records) |
| **सूची** | `सूची` | स्त्रीलिंग नाम | प्रथमा एकवचन | इण्डेक्स-तालिका (the sparse index block) |
| **तथा** | `तथा` | अव्ययम् | अव्ययम् | तथैव (likewise) |
| **एव** | `एव` | अव्ययम् | अव्ययम् | अवधारणे (indeed) |
| **च** | `च` | अव्ययम् | अव्ययम् | समुच्चये (and) |
| **अल्पावलोकनमात्रेण** | `अल्प + अवलोकन + मात्र` | कर्मधारय नपुंसकलिंग | तृतीया एकवचन | करणे तृतीया (by merely scanning the compact index) |
| **स्थानम्** | `स्थान` | नपुंसकलिंग नाम | प्रथमा एकवचन | ब्लॉक-स्थानम् (the exact file offset) |
| **ज्ञायेत** | `√ज्ञा + कर्मणि लिङ्` | कर्मणि लिङ् | प्रथमपुरुष एकवचन | अधिगम्येत (can be located via binary search) |
| **सत्वरम्** | `सत्वरम्` | क्रियाविशेषण अव्यय | अव्ययम् | झटिति (swiftly) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: Two-Level Sparse Indexing: an SSTable file is partitioned internally into a sequence of data blocks (typically 4KB to 64KB compressed) followed by an index block. The index block contains the last key of each data block alongside its exact physical file offset. Instead of indexing every individual record, the engine maintains this sparse index in memory: finding any key requires only a binary search over the compact index followed by loading the single identified 4KB data block.

---

### Verse 20

```text
अन्ते पादक्रमे न्यस्ता सूचिका संप्रदृश्यते ।
दोषनाशनचिह्नेन सत्यं संपरिरक्ष्यते ॥
```

**पदच्छेदः**: अन्ते पाद-क्रमे न्यस्ता सूचिका सम्-प्रदृश्यते । दोष-नाशन-चिह्नेन सत्यम् सम्-परिरक्ष्यते ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **अन्ते** | `अन्त` | पुंलिंग नाम | सप्तमी एकवचन | सञ्चिकाया अन्ते (at the footer trailer of the file) |
| **पादक्रमे** | `पाद + क्रम` | पुंलिंग नाम | सप्तमी एकवचन | फुटर-स्थाने (at the trailing footer) |
| **न्यस्ता** | `नि + √अस् + क्त` | कृदन्तरूप स्त्रीलिंग | प्रथमा एकवचन | स्थापिता (anchored) |
| **सूचिका** | `सूचिका` | स्त्रीलिंग नाम | प्रथमा एकवचन | मेटा-इण्डेक्स-तालिका (the footer directory index) |
| **संप्रदृश्यते** | `सम् + प्र + √दृश् + कर्मणि लट्` | कर्मणि लट् | प्रथमपुरुष एकवचन | विद्यते (is located) |
| **दोषनाशनचिह्नेन** | `दोष + नाशन + चिह्न` | षष्ठी-तत्पुरुष नपुंसकलिंग | तृतीया एकवचन | करणे तृतीया (by cryptographic CRC32 checksums) |
| **सत्यम्** | `सत्य` | नपुंसकलिंग नाम | प्रथमा एकवचन | दत्तनिष्ठा (data integrity) |
| **संपरिरक्ष्यते** | `सम् + परि + √रक्ष् + कर्मणि लट्` | कर्मणि लट् | प्रथमपुरुष एकवचन | संरक्ष्यते (is verified and protected) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: The Footer and Checksum Verification: because SSTables are written sequentially in a single pass, the file footer is written last. The footer contains magic numbers, metadata offsets and fixed-size handles pointing to the index and filter blocks. Crucially, every data block ends with a CRC32 or xxHash checksum: when reading a block, the storage engine recomputes the checksum to detect bit-rot and silent disk corruption before serving data to the client.

---

## Canto 5: कुसुमसङ्केतः शून्यनिरीक्षणञ्च (Bloom Filters: Probabilistic Negative Lookup Acceleration)

### Verse 21

```text
अन्वेषणे कृते नित्यं बहुपात्रं प्रदृश्यते ।
शून्ये भ्रमति मन्दो हि कालव्ययः प्रजायते ॥
```

**पदच्छेदः**: अन्वेषणे कृते नित्यम् बहु-पात्रम् प्रदृश्यते । शून्ये भ्रमति मन्दः हि काल-व्ययः प्रजायते ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **अन्वेषणे** | `अनु + √इष् + ल्युट्` | नपुंसकलिंग नाम | सप्तमी एकवचन | सति-सप्तमी (upon point read lookup) |
| **कृते** | `√कृ + क्त` | कृदन्तरूप सप्तमी एकवचन | सति-सप्तमी | विहिते (being executed) |
| **नित्यम्** | `नित्यम्` | अव्ययम् | अव्ययम् | सदा (perpetually) |
| **बहुपात्रम्** | `बहु + पात्र` | कर्मधारय नपुंसकलिंग | प्रथमा एकवचन | अनेक-एस-एस-टेबल-समूहः (numerous candidate SSTables) |
| **प्रदृश्यते** | `प्र + √दृश् + कर्मणि लट्` | कर्मणि लट् | प्रथमपुरुष एकवचन | दृश्यते (is observed) |
| **शून्ये** | `शून्य` | नपुंसकलिंग नाम | सप्तमी एकवचन | अविद्यमाने वस्तुनि (for non-existent keys) |
| **भ्रमति** | `√भ्रम् + लट्` | परस्मैपद लट् | प्रथमपुरुष एकवचन | वृथा भ्रमं करोति (wanders pointlessly) |
| **मन्दः** | `मन्द` | विशेषण पुंलिंग | प्रथमा एकवचन | अज्ञः / पाठकः (the naive search algorithm) |
| **हि** | `हि` | अव्ययम् | अव्ययम् | निश्चये (verily) |
| **कालव्ययः** | `काल + व्यय` | षष्ठी-तत्पुरुष पुंलिंग | प्रथमा एकवचन | कालक्षयः (wasted I/O seek latency) |
| **प्रजायते** | `प्र + √जन् + लट्` | आत्मनेपद लट् | प्रथमपुरुष एकवचन | उत्पद्यते (is generated) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: The Read Path Penalty: while an LSM-Tree is blazingly fast for writes, point reads face a steep challenge. If a requested key is not in the MemTable, the engine must search on-disk SSTables from newest to oldest. If the requested key does not exist anywhere in the database (or is in an older layer), a naive search would issue physical disk reads against dozens of separate SSTable files across disk sectors, devastating read throughput.

---

### Verse 22

```text
तदर्थं कल्पितो रम्यः कुसुमाकारसंविदः ।
अङ्कानां बिन्दुजालेन परीक्षा क्रियते द्रुतम् ॥
```

**पदच्छेदः**: तद्-अर्थम् कल्पितः रम्यः कुसुम-आकार-संविदः । अङ्कानाम् बिन्दु-जालेन परीक्षा क्रियते द्रुतम् ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **तदर्थम्** | `तद् + अर्थम्` | अव्ययम् | अव्ययम् | तस्य दोषस्य निवारणाय (for that purpose) |
| **कल्पितः** | `√क्लृप् + णिच् + क्त` | कृदन्तरूप पुंलिंग | प्रथमा एकवचन | आविष्कृतः (invented / configured) |
| **रम्यः** | `रम्य` | विशेषण पुंलिंग | प्रथमा एकवचन | सुन्दरः (ingenious) |
| **कुसुमाकारसंविदः** | `कुसुम + आकार + संविद् (Burton Bloom)` | बहुव्रीहि पुंलिंग | प्रथमा एकवचन | ब्लूम-फिल्टर (Burton Bloom's Filter) |
| **अङ्कानाम्** | `अङ्क` | पुंलिंग नाम | षष्ठी बहुवचन | द्व्यङ्कानाम् (of bits: zeros and ones) |
| **बिन्दुजालेन** | `बिन्दु + जाल` | षष्ठी-तत्पुरुष नपुंसकलिंग | तृतीया एकवचन | करणे तृतीया (by a bit array of size m) |
| **परीक्षा** | `परीक्षा` | स्त्रीलिंग नाम | प्रथमा एकवचन | संभावनाजाँच (probabilistic membership verification) |
| **क्रियते** | `√कृ + कर्मणि लट्` | कर्मणि लट् | प्रथमपुरुष एकवचन | विधीयते (is executed) |
| **द्रुतम्** | `द्रुतम्` | क्रियाविशेषण अव्यय | अव्ययम् | झटिति (swiftly in nanoseconds) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: Bloom Filters (kusuma-saṅketa): invented by Burton Howard Bloom in 1970, a Bloom filter is a space-efficient probabilistic data structure. Each SSTable contains an in-memory Bloom filter: a bit array of m bits initialized to 0. When an SSTable is created, every key is passed through k independent cryptographic hash functions, setting the corresponding k bit positions in the array to 1. The entire filter consumes just a few kilobytes of RAM.

---

### Verse 23

```text
यत्र बिन्दुरसन्दिग्धः शून्यो भवति मण्डले ।
तत्र नास्तीति निश्चित्य विरमेत ततस्त्विह ॥
```

**पदच्छेदः**: यत्र बिन्दुः असन्दिग्धः शून्यः भवति मण्डले । तत्र न अस्ति इति निश्चित्य विरमेत ततः तु इह ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **यत्र** | `यत्र` | अव्ययम् | अव्ययम् | यस्मिन् बिट्-स्थाने (wherever) |
| **बिन्दुः** | `बिन्दु` | पुंलिंग नाम | प्रथमा एकवचन | बिट्-अङ्कः (a hashed bit position) |
| **असन्दिग्धः** | `अ + सन्दिग्ध` | नञ्-तत्पुरुष पुंलिंग | प्रथमा एकवचन | निश्चितः (definitively) |
| **शून्यः** | `शून्य` | विशेषण पुंलिंग | प्रथमा एकवचन | शून्यमूल्यकः (is zero: 0) |
| **भवति** | `√भू + लट्` | परस्मैपद लट् | प्रथमपुरुष एकवचन | विद्यते (is) |
| **मण्डले** | `मण्डल` | नपुंसकलिंग नाम | सप्तमी एकवचन | बिट्-अरे-मध्ये (in the bit array) |
| **तत्र** | `तत्र` | अव्ययम् | अव्ययम् | तस्मिन् एस-एस-टेबले (in that SSTable) |
| **न** | `न` | निषेधार्थक अव्यय | अव्ययम् | निषेधे (not) |
| **अस्ति** | `√अस् + लट्` | परस्मैपद लट् | प्रथमपुरुष एकवचन | विद्यते (exists) |
| **इति** | `इति` | अव्ययम् | अव्ययम् | इत्याकारेण (thus) |
| **निश्चित्य** | `निस् + √चि + ल्यप्` | कृदन्तरूप अव्यय | अव्ययम् | दृढं ज्ञात्वा (knowing with 100% mathematical certainty) |
| **विरमेत** | `वि + √रम् + विधि-लिङ्` | आत्मनेपद लिङ् | प्रथमपुरुष एकवचन | निवर्तेत (skips the SSTable completely) |
| **ततः** | `ततः` | अव्ययम् | अव्ययम् | तस्मात् (from that file) |
| **तु** | `तु` | अव्ययम् | अव्ययम् | विशेषे (indeed) |
| **इह** | `इह` | अव्ययम् | अव्ययम् | अस्मिन् अन्वेषणे (in this read path) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: The Zero False-Negative Guarantee: Bloom filters exhibit a crucial mathematical invariant: they never produce false negatives. If even a single one of the k hash positions in the bit array evaluates to 0, it is mathematically impossible for that key to have ever been inserted into that SSTable. The storage engine immediately skips the entire SSTable without touching the disk, aborting wasted I/O in single-digit nanoseconds.

---

### Verse 24

```text
संभवेद् भ्रान्तिरेकत्र नास्तीति तु न लभ्यते ।
अल्पीयसि व्यये कृते दृष्टिः संजायते परा ॥
```

**पदच्छेदः**: संभवेत् भ्रान्तिः एकत्र न अस्ति इति तु न लभ्यते । अल्पीयसि व्यये कृते दृष्टिः सम्-जायते परा ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **संभवेत्** | `सम् + √भू + विधि-लिङ्` | परस्मैपद लिङ् | प्रथमपुरुष एकवचन | जायेत (may occur) |
| **भ्रान्तिः** | `भ्रान्ति` | स्त्रीलिंग नाम | प्रथमा एकवचन | फॉल्स-पॉजिटिव (false positive: filter says maybe, but key absent) |
| **एकत्र** | `एकत्र` | अव्ययम् | अव्ययम् | एकस्मिन् पक्षे (in one direction) |
| **न** | `न` | निषेधार्थक अव्यय | अव्ययम् | निषेधे (not) |
| **अस्ति** | `√अस् + लट्` | परस्मैपद लट् | प्रथमपुरुष एकवचन | विद्यते ('it is') |
| **इति** | `इति` | अव्ययम् | अव्ययम् | इत्याकारेण (thus) |
| **तु** | `तु` | अव्ययम् | अव्ययम् | विशेषे (however) |
| **न** | `न` | निषेधार्थक अव्यय | अव्ययम् | निषेधे (never) |
| **लभ्यते** | `√लभ् + कर्मणि लट्` | कर्मणि लट् | प्रथमपुरुष एकवचन | भवति (is tolerated as a false negative) |
| **अल्पीयसि** | `अल्पीयस्` | विशेषण | सप्तमी एकवचन पुंलिंग | व्यये विशेषणम् (in tiny / minimal memory) |
| **व्यये** | `व्यय` | पुंलिंग नाम | सप्तमी एकवचन | सति-सप्तमी (consumption: ~10 bits per key) |
| **कृते** | `√कृ + क्त` | कृदन्तरूप सप्तमी एकवचन | सति-सप्तमी | विहिते (being allocated) |
| **दृष्टिः** | `दृष्टि` | स्त्रीलिंग नाम | प्रथमा एकवचन | अवलोकनसिद्धिः (filtering accuracy) |
| **संजायते** | `सम् + √जन् + लट्` | आत्मनेपद लट् | प्रथमपुरुष एकवचन | सिद्ध्यति (is attained) |
| **परा** | `पर` | विशेषण स्त्रीलिंग | प्रथमा एकवचन | उत्कृष्टम् (supreme: 99% accuracy) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: Controlling the False Positive Rate: while Bloom filters never produce false negatives, hash collisions can produce false positives (the filter reports that all k bits are 1, but the key is not actually in the SSTable). By allocating just 10 bits per key and using k = ln(2) * 10 ≈ 7 hash functions, the false positive probability drops to approximately 1%. For a negligible memory overhead, 99% of all unnecessary disk seeks are permanently eliminated.

---

### Verse 25

```text
शतांशे भ्रमदोषे तु शतकृत्वः सुसंरक्षितम् ।
चक्रिकाया व्ययो नष्टः शान्तं तिष्ठति मण्डलम् ॥
```

**पदच्छेदः**: शत-अंशे भ्रम-दोषे तु शत-कृत्वः सु-संरक्षितम् । चक्रिकायाः व्ययः नष्टः शान्तम् तिष्ठति मण्डलम् ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **शतांशे** | `शत + अंश` | पुंलिंग नाम | सप्तमी एकवचन | सति-सप्तमी (at a 1% error rate) |
| **भ्रमदोषे** | `भ्रम + दोष` | पुंलिंग नाम | सप्तमी एकवचन | सति-सप्तमी (in false positive risk) |
| **तु** | `तु` | अव्ययम् | अव्ययम् | विशेषे (indeed) |
| **शतकृत्वः** | `शत + कृत्वसुँच्` | क्रियाविशेषण अव्यय | अव्ययम् | शतवारम् (a hundred times over) |
| **सुसंरक्षितम्** | `सु + सम् + √रक्ष् + क्त` | कृदन्तरूप नपुंसकलिंग | प्रथमा एकवचन | रक्षितम् (safeguarded) |
| **चक्रिकायाः** | `चक्रिका` | स्त्रीलिंग नाम | षष्ठी एकवचन | डिस्क-यन्त्रस्य (of the storage drive) |
| **व्ययः** | `व्यय` | पुंलिंग नाम | प्रथमा एकवचन | अनावश्यक-आई-ओ (wasted read I/O seeks) |
| **नष्टः** | `√नश् + क्त` | कृदन्तरूप पुंलिंग | प्रथमा एकवचन | निवारितः (eliminated / vanished) |
| **शान्तम्** | `शान्त` | विशेषण नपुंसकलिंग | प्रथमा एकवचन | उपद्रवरहितम् (calm / unstressed) |
| **तिष्ठति** | `√स्था + लट्` | परस्मैपद लट् | प्रथमपुरुष एकवचन | विराजते (abides) |
| **मण्डलम्** | `मण्डल` | नपुंसकलिंग नाम | प्रथमा एकवचन | सञ्चययन्त्रम् (the storage cluster subsystem) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: Systemic I/O Shielding: by suppressing 99 out of every 100 disk seeks on non-existent or superseded keys, Bloom filters insulate disk queues from point read thrashing. Storage drives stay idle and cool ('śāntaṃ tiṣṭhati maṇḍalam'), preserving their precious I/O operations per second (IOPS) for legitimate data block fetches and background compaction merges.

---

## Canto 6: स्तरमर्दनविधिः सङ्कोचनञ्च (Compaction Strategies: Size-Tiered, Leveled and the RUM Conjecture)

### Verse 26

```text
सञ्चितेषु च पत्रेषु भारो वर्धेत भीषणः ।
वाचने जायते मन्दं स्थानं संक्षीयते बहु ॥
```

**पदच्छेदः**: सञ्चितेषु च पत्रेषु भारः वर्धेत भीषणः । वाचने जायते मन्दम् स्थानम् संक्षीयते बहु ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **सञ्चितेषु** | `सम् + √चि + क्त` | कृदन्तरूप नपुंसकलिंग | सप्तमी बहुवचन | सति-सप्तमी (when accumulated) |
| **च** | `च` | अव्ययम् | अव्ययम् | संयोजकः (and) |
| **पत्रेषु** | `पत्र` | नपुंसकलिंग नाम | सप्तमी बहुवचन | सति-सप्तमी (in on-disk SSTable files) |
| **भारः** | `भार` | पुंलिंग नाम | प्रथमा एकवचन | अव्यवस्थाभारः (space amplification and read amplification) |
| **वर्धेत** | `√वृध् + विधि-लिङ्` | आत्मनेपद लिङ् | प्रथमपुरुष एकवचन | उद्गच्छेत् (explodes) |
| **भीषणः** | `भीषण` | विशेषण पुंलिंग | प्रथमा एकवचन | दारुणः (severe) |
| **वाचने** | `वाचन` | नपुंसकलिंग नाम | सप्तमी एकवचन | पठनक्रियायाम् (in read performance) |
| **जायते** | `√जन् + लट्` | आत्मनेपद लट् | प्रथमपुरुष एकवचन | भवति (becomes) |
| **मन्दम्** | `मन्द` | विशेषण नपुंसकलिंग | प्रथमा एकवचन | मन्दगामि (sluggish / degraded) |
| **स्थानम्** | `स्थान` | नपुंसकलिंग नाम | प्रथमा एकवचन | डिस्क-स्थानम् (disk storage space) |
| **संक्षीयते** | `सम् + √क्षी + कर्मणि लट्` | कर्मणि लट् | प्रथमपुरुष एकवचन | विनाशं याति (is wastefully exhausted) |
| **बहु** | `बहु` | क्रियाविशेषण | अव्ययम् | प्रचुरम् (vastly) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: The Entropy of Accumulating SSTables: as the database flushes MemTables hour after hour, hundreds of SSTable files accumulate on disk. Each file contains overlapping key ranges and obsolete overwritten versions. If left unmanaged, read queries must check dozens of files (exploding Read Amplification) and dead records consume massive storage capacity (exploding Space Amplification). The database requires active background reconciliation.

---

### Verse 27

```text
मर्दनस्य विधानेन सम्मेलनं समाचरेत् ।
बहूनि चैकभावेन स्थापयन्ति मनीषिणः ॥
```

**पदच्छेदः**: मर्दनस्य विधानेन सम्-मेलनम् सम्-आचरेत् । बहूनि च एक-भावेन स्थापयन्ति मनीषिणः ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **मर्दनस्य** | `मर्दन` | नपुंसकलिंग नाम | षष्ठी एकवचन | कम्पैक्शन-विधेः (of background Compaction) |
| **विधानेन** | `विधान` | नपुंसकलिंग नाम | तृतीया एकवचन | करणे तृतीया (through the algorithmic protocol) |
| **सम्मेलनम्** | `सम् + मेलन` | नपुंसकलिंग नाम | द्वितीया एकवचन | मर्ज-सॉर्ट-प्रक्रियाम् (multi-way merge sort) |
| **समाचरेत्** | `सम् + आ + √चर् + विधि-लिङ्` | परस्मैपद लिङ् | प्रथमपुरुष एकवचन | कुर्यात् (one should execute) |
| **बहूनि** | `बहु` | विशेषण नपुंसकलिंग | द्वितीया बहुवचन | अनेकानि सञ्चिकापत्राणि (multiple fragmented SSTables) |
| **च** | `च` | अव्ययम् | अव्ययम् | संयोजकः (and) |
| **एकभावेन** | `एक + भाव` | तृतीया एकवचन पुंलिंग | क्रियाविशेषणवत् | एकत्र संहृत्य (into unified consolidated sorted files) |
| **स्थापयन्ति** | `स्था + णिच् + लट्` | परस्मैपद लट् | प्रथमपुरुष बहुवचन | रचयन्ति (reorganize) |
| **मनीषिणः** | `मनीषिन्` | पुंलिंग नाम | प्रथमा बहुवचन | तन्त्रज्ञाः (systems architects) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: Compaction (mardana-vidhi): compaction is the continuous background garbage collection and consolidation engine of an LSM-Tree. A background thread selects multiple existing SSTables, opens sequential iterators across them and executes a multi-way merge sort. Obsolete superseded versions and deleted records are purged and the surviving latest versions are written out into a consolidated, perfectly sorted new SSTable.

---

### Verse 28

```text
आकारतुल्यभावेन केचित् कुर्वन्ति शोधनम् ।
स्तरे स्तरे विभक्तेन केचिदिच्छन्ति संस्थितिम् ॥
```

**पदच्छेदः**: आकार-तुल्य-भावेन केचित् कुर्वन्ति शोधनम् । स्तरे स्तरे विभक्तेन केचित् इच्छन्ति संस्थितिम् ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **आकारतुल्यभावेन** | `आकार + तुल्य + भाव` | तृतीया-तत्पुरुष पुंलिंग | तृतीया एकवचन | करणे तृतीया (by Size-Tiered Compaction Strategy - STCS) |
| **केचित्** | `किम् + चित्` | सर्वनाम पुंलिंग | प्रथमा बहुवचन | केचन तन्त्राः: यथा कासान्द्रा (some engines like Cassandra) |
| **कुर्वन्ति** | `√कृ + लट्` | परस्मैपद लट् | प्रथमपुरुष बहुवचन | निष्पादयन्ति (execute) |
| **शोधनम्** | `शोधन` | नपुंसकलिंग नाम | द्वितीया एकवचन | मर्दनम् (compaction) |
| **स्तरे** | `स्तर` | पुंलिंग नाम | सप्तमी एकवचन | वीप्सायाम् (level by level) |
| **स्तरे** | `स्तर` | पुंलिंग नाम | सप्तमी एकवचन | लेवेल्ड्-कम्पैक्शन (Leveled Compaction Strategy - LCS) |
| **विभक्तेन** | `वि + √भज् + क्त` | कृदन्तरूप पुंलिंग | तृतीया एकवचन | विभाजितेन क्रमेण (by strictly partitioned levels L0..Ln) |
| **केचित्** | `किम् + चित्` | सर्वनाम पुंलिंग | प्रथमा बहुवचन | यथा लेवेलडीबी राक्सडीबी (such as LevelDB and RocksDB) |
| **इच्छन्ति** | `√इष् + लट्` | परस्मैपद लट् | प्रथमपुरुष बहुवचन | स्वीकुर्वन्ति (prefer) |
| **संस्थितिम्** | `सम् + स्थिति` | स्त्रीलिंग नाम | द्वितीया एकवचन | व्यवस्थासाम्यम् (architectural equilibrium) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: Compaction Strategies: Two primary philosophies govern compaction. Size-Tiered Compaction Strategy (STCS, popular in Cassandra) groups SSTables of similar file sizes together and merges them when four files accumulate; it features low Write Amplification and is ideal for write-heavy workloads. Leveled Compaction Strategy (LCS, used in RocksDB and LevelDB) organizes data into exponentially larger levels (L1, L2, L3...) where each level guarantees non-overlapping key ranges; it features low Read Amplification and minimal Space Amplification at the cost of higher Write Amplification.

---

### Verse 29

```text
दत्तमात्रं त्रिभिर्द्वारैर्युध्यते सर्वदा रणे ।
वाचने लेखने स्थाने सन्तुलनं विधीयते ॥
```

**पदच्छेदः**: दत्त-मात्रम् त्रिभिः द्वारैः युध्यते सर्वदा रणे । वाचने लेखने स्थाने सम्-तुलनम् विधीयते ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **दत्तमात्रम्** | `दत्त + मात्र` | कर्मधारय नपुंसकलिंग | प्रथमा एकवचन | भाण्डारव्यवस्था (storage engine data management) |
| **त्रिभिः** | `त्रि` | संख्या-सर्वनाम | तृतीया बहुवचन नपुंसकलिंग | द्वारैः विशेषणम् (with three) |
| **द्वारैः** | `द्वार` | नपुंसकलिंग नाम | तृतीया बहुवचन | करणे तृतीया (trade-off dimensions: RUM Conjecture) |
| **युध्यते** | `√युध् + लट्` | आत्मनेपद लट् | प्रथमपुरुष एकवचन | सङ्ग्रामं करोति (struggles / balances) |
| **सर्वदा** | `सर्वदा` | अव्ययम् | अव्ययम् | सदा (perpetually) |
| **रणे** | `रण` | पुंलिंग नाम | सप्तमी एकवचन | अभियान्त्रिकसङ्ग्रामे (in the systems trade-off arena) |
| **वाचने** | `वाचन` | नपुंसकलिंग नाम | सप्तमी एकवचन | Read Amplification (R) |
| **लेखने** | `लेखन` | नपुंसकलिंग नाम | सप्तमी एकवचन | Write/Update Amplification (U) |
| **स्थाने** | `स्थान` | नपुंसकलिंग नाम | सप्तमी एकवचन | Memory/Space Amplification (M) |
| **सन्तुलनम्** | `सम् + तुलन` | नपुंसकलिंग नाम | प्रथमा एकवचन | साम्यस्थापनम् (delicate equilibrium) |
| **विधीयते** | `वि + √धा + कर्मणि लट्` | कर्मणि लट् | प्रथमपुरुष एकवचन | साध्यते (is negotiated) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: The RUM Conjecture (Athanassoulis et al. 2016): when designing storage systems, you cannot optimize Read overhead (R), Update/Write overhead (U) and Memory/Space overhead (M) simultaneously. Optimizing two always degrades the third. B-Trees optimize Reads and Space at the expense of catastrophic Update write amplification. LSM-Trees optimize Updates and Space at the expense of Read overhead. Systems architects must consciously choose where to stand along the RUM trade-off triangle.

---

### Verse 30

```text
मर्दितेषु समग्रेषु नूतनं जायते फलम् ।
पुरातनं विमुच्याथ शुद्धिः संपद्यते परा ॥
```

**पदच्छेदः**: मर्दितेषु समग्रेषु नूतनम् जायते फलम् । पुरातनम् विमुच्य अथ शुद्धिः सम्-पद्यते परा ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **मर्दितेषु** | `√मर्द् + क्त` | कृदन्तरूप नपुंसकलिंग | सप्तमी बहुवचन | सति-सप्तमी (when compacted) |
| **समग्रेषु** | `समग्र` | विशेषण | सप्तमी बहुवचन नपुंसकलिंग | पत्रेषु विशेषणम् (in all selected SSTable runs) |
| **नूतनम्** | `नूतन` | विशेषण नपुंसकलिंग | प्रथमा एकवचन | नवीनम् (a fresh consolidated) |
| **जायते** | `√जन् + लट्` | आत्मनेपद लट् | प्रथमपुरुष एकवचन | उत्पद्यते (is generated) |
| **फलम्** | `फल` | नपुंसकलिंग नाम | प्रथमा एकवचन | एस-एस-टेबल (SSTable file output) |
| **पुरातनम्** | `पुरातन` | विशेषण नपुंसकलिंग | द्वितीया एकवचन | जीर्णम् (the obsolete input files) |
| **विमुच्य** | `वि + √मुच् + ल्यप्` | कृदन्तरूप अव्यय | अव्ययम् | अपसार्य (having unlinked and deleted) |
| **अथ** | `अथ` | मङ्गलार्थक/कालवाचक अव्यय | अव्ययम् | तदनन्तरम् (thereafter) |
| **शुद्धिः** | `शुद्धि` | स्त्रीलिंग नाम | प्रथमा एकवचन | परिशोधनम् (space recovery and compaction purity) |
| **संपद्यते** | `सम् + √पद् + लट्` | आत्मनेपद लट् | प्रथमपुरुष एकवचन | सिद्ध्यति (is attained) |
| **परा** | `पर` | विशेषण स्त्रीलिंग | प्रथमा एकवचन | सम्पूणा (complete) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: Atomic Replacement in Compaction: when compaction finishes writing the consolidated output SSTable, it updates the database Manifest file in a single atomic transaction. The old input SSTables are unlinked and immediately deleted from the filesystem. Space is freed, duplicate keys are reclaimed and the system restores optimal read performance.

---

## Canto 7: मृत्युमुद्रा विनाशसंस्कारश्च (Tombstones, Logical Deletion and Garbage Collection)

### Verse 31

```text
अचले लिखिते चक्रे लोपः कर्तुं न शक्यते ।
तस्माद् विनाशचिह्नं तु लिख्यते कुञ्चिकां प्रति ॥
```

**पदच्छेदः**: अचले लिखिते चक्रे लोपः कर्तुम् न शक्यते । तस्मात् विनाश-चिह्नम् तु लिख्यते कुञ्चिकाम् प्रति ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **अचले** | `अचल` | विशेषण | सप्तमी एकवचन नपुंसकलिंग | चक्रे विशेषणम् (in immutable on-disk) |
| **लिखिते** | `√लिख् + क्त` | कृदन्तरूप सप्तमी एकवचन | सति-सप्तमी | एस-एस-टेबले (in SSTable storage) |
| **चक्रे** | `चक्र` | नपुंसकलिंग नाम | सप्तमी एकवचन | सञ्चिकायाम् (on disk) |
| **लोपः** | `लोप` | पुंलिंग नाम | प्रथमा एकवचन | प्रत्यक्षविनाशः (physical in-place deletion) |
| **कर्तुम्** | `√कृ + तुमुन्` | तुमुन्-प्रत्ययान्तरूप | अव्ययम् | विधातुम् (to execute) |
| **न** | `न` | निषेधार्थक अव्यय | अव्ययम् | निषेधे (not) |
| **शक्यते** | `√शक् + कर्मणि लट्` | कर्मणि लट् | प्रथमपुरुष एकवचन | पार्यते (is possible) |
| **तस्मात्** | `तद्` | सर्वनाम | पञ्चमी एकवचन | हेत्वर्थे (therefore) |
| **विनाशचिह्नम्** | `विनाश + चिह्न` | कर्मधारय नपुंसकलिंग | प्रथमा एकवचन | टॉम्बस्टोन-मुद्रा (the Tombstone marker) |
| **तु** | `तु` | अव्ययम् | अव्ययम् | विशेषे (indeed) |
| **लिख्यते** | `√लिख् + कर्मणि लट्` | कर्मणि लट् | प्रथमपुरुष एकवचन | अङ्क्यते (is written as a special mutation record) |
| **कुञ्चिकाम्** | `कुञ्चिका` | स्त्रीलिंग नाम | द्वितीया एकवचन | लक्ष्यभूतकुञ्चिकाम् (for that specific key) |
| **प्रति** | `प्रति` | कर्मप्रवचनीय अव्यय | अव्ययम् | लक्षणे (against / for) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: The Deletion Conundrum: because on-disk SSTables are strictly immutable, you cannot physically open a 1GB file, seek to a specific offset and erase 50 bytes of a deleted key. Modifying existing files would break immutability, ruin sequential caching and introduce file corruption. Therefore, an LSM-Tree treats a DELETE operation as a special write: it appends a deletion tombstone marker to the log.

---

### Verse 32

```text
मृत्युमुद्रा समाख्याता कालदूत इवोदिता ।
छादयित्वा पुरातनं सत्यं संप्रविमुञ्चति ॥
```

**पदच्छेदः**: मृत्यु-मुद्रा सम्-आख्याता काल-दूतः इव उदिता । छादयित्वा पुरातनम् सत्यम् सम्-प्रविमुञ्चति ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **मृत्युमुद्रा** | `मृत्यु + मुद्रा` | षष्ठी-तत्पुरुष स्त्रीलिंग | प्रथमा एकवचन | टॉम्बस्टोन (the Tombstone) |
| **समाख्याता** | `सम् + आ + √ख्या + क्त` | कृदन्तरूप स्त्रीलिंग | प्रथमा एकवचन | उद्दिष्टा (is designated) |
| **कालदूतः** | `काल + दूत` | षष्ठी-तत्पुरुष पुंलिंग | प्रथमा एकवचन | यमसन्देशवाहकः (like the messenger of death / Yamadūta) |
| **इव** | `इव` | उपमार्थे अव्यय | अव्ययम् | यथा (as / like) |
| **उदिता** | `उद् + √इ + क्त` | कृदन्तरूप स्त्रीलिंग | प्रथमा एकवचन | उत्पन्ना (manifested) |
| **छादयित्वा** | `√छद् + णिच् + क्त्वा` | कृदन्तरूप अव्यय | अव्ययम् | आवृत्त्य (having shadowed / masked) |
| **पुरातनम्** | `पुरातन` | विशेषण | द्वितीया एकवचन नपुंसकलिंग | पूर्वसंस्करणम् (the older valid record) |
| **सत्यम्** | `सत्य` | नपुंसकलिंग नाम | द्वितीया एकवचन | यथार्थम् (the logical reality of deletion) |
| **संप्रविमुञ्चति** | `सम् + प्र + वि + √मुच् + लट्` | परस्मैपद लट् | प्रथमपुरुष एकवचन | प्रकटयति (releases / proclaims) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: The Mask of the Tombstone: when a query searches for key k, it evaluates records in descending order of sequence numbers. If it encounters a tombstone with sequence number 105, it knows instantly that key k was deleted at time 105. Even if an older, valid value of k with sequence number 42 resides on disk in level L3, the newer tombstone masks it completely, causing the query to return 'Key Not Found'.

---

### Verse 33

```text
प्रेतरूपमिवाभाति यावन्मर्दनमश्नुते ।
वाचने बाधते काले भारं वर्धयते भृशम् ॥
```

**पदच्छेदः**: प्रेत-रूपम् इव आभाति यावत् मर्दनम् अश्नुते । वाचने बाधते काले भारम् वर्धयते भृशम् ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **प्रेतरूपम्** | `प्रेत + रूप` | बहुव्रीहि नपुंसकलिंग | द्वितीया एकवचन | छायाभूतम् (like a ghost record / phantom entity) |
| **इव** | `इव` | उपमार्थे अव्यय | अव्ययम् | यथा (like) |
| **आभाति** | `आ + √भा + लट्` | परस्मैपद लट् | प्रथमपुरुष एकवचन | प्रतीयते (manifests) |
| **यावत्** | `यावत्` | कालवाचक अव्यय | अव्ययम् | यावत्कालम् (until) |
| **मर्दनम्** | `मर्दन` | नपुंसकलिंग नाम | द्वितीया एकवचन | कम्पैक्शन-शोधनम् (compaction purge) |
| **अश्नुते** | `√अश् + लट्` | आत्मनेपद लट् | प्रथमपुरुष एकवचन | प्राप्नोति (undergoes) |
| **वाचने** | `वाचन` | नपुंसकलिंग नाम | सप्तमी एकवचन | पठनकाले (during range scans and point queries) |
| **बाधते** | `√बाध् + लट्` | आत्मनेपद लट् | प्रथमपुरुष एकवचन | पीडयति (hinders / slows down) |
| **काले** | `काल` | पुंलिंग नाम | सप्तमी एकवचन | अन्वेषणसमये (during search) |
| **भारम्** | `भार` | पुंलिंग नाम | द्वितीया एकवचन | अनावश्यकभारम् (space and iteration overhead) |
| **वर्धयते** | `√वृध् + णिच् + लट्` | आत्मनेपद लट् | प्रथमपुरुष एकवचन | प्रसरयति (amplifies) |
| **भृशम्** | `भृशम्` | क्रियाविशेषण अव्यय | अव्ययम् | अत्यन्तम् (immensely) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: The Ghost of the Tombstone: tombstones introduce a severe operational hazard. Because tombstones are themselves physical records, they consume disk space and must be examined during range scans. If an application writes and immediately deletes 10 million keys, a range scan iterating over that range must step through 10 million ghost tombstones, turning a sub-millisecond query into a 30-second crawl until compaction finally purges them.

---

### Verse 34

```text
यदा गभीरे संमर्दे पुरातनं विनश्यति ।
तदैव मुद्रिका संत्याज्या शुद्धिर्जायेत शाश्वती ॥
```

**पदच्छेदः**: यदा गभीरे सम्-मर्दे पुरातनम् विनश्यति । तदा एव मुद्रिका सन्-त्याज्या शुद्धिः जायेत शाश्वती ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **यदा** | `यदा` | कालवाचक अव्यय | अव्ययम् | यस्मिन् क्षणे (when) |
| **गभीरे** | `गभीर` | विशेषण | सप्तमी एकवचन पुंलिंग | मर्दे विशेषणम् (in deep / bottom-most level) |
| **संमर्दे** | `सम् + मर्द` | पुंलिंग नाम | सप्तमी एकवचन | सति-सप्तमी (compaction merge: e.g. Ln) |
| **पुरातनम्** | `पुरातन` | विशेषण | प्रथमा एकवचन नपुंसकलिंग | प्राचीनसंस्करणम् (the archaic record version) |
| **विनश्यति** | `वि + √नश् + लट्` | परस्मैपद लट् | प्रथमपुरुष एकवचन | नष्टो भवति (is completely annihilated) |
| **तदा** | `तदा` | अव्ययम् | अव्ययम् | तस्मिन् क्षणे (then) |
| **एव** | `एव` | अव्ययम् | अव्ययम् | अवधारणे (only then) |
| **मुद्रिका** | `मुद्रिका` | स्त्रीलिंग नाम | प्रथमा एकवचन | टॉम्बस्टोन-मुद्रा (the tombstone marker itself) |
| **संत्याज्या** | `सम् + √त्यज् + ण्यत्` | कृदन्तरूप स्त्रीलिंग | प्रथमा एकवचन | विसर्जनीया (can be safely discarded) |
| **शुद्धिः** | `शुद्धि` | स्त्रीलिंग नाम | प्रथमा एकवचन | परिशोधनम् (permanent reclamation) |
| **जायेत** | `√जन् + विधि-लिङ्` | आत्मनेपद लिङ् | प्रथमपुरुष एकवचन | भवेत् (occurs) |
| **शाश्वती** | `शाश्वती` | विशेषण स्त्रीलिंग | प्रथमा एकवचन | चिरन्तनी (permanent) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: When Can a Tombstone Be Purged? A tombstone CANNOT simply be dropped the first time it is merged! If a tombstone in level L1 is dropped while an older version of that key still lives in level L2 or L3, the older version would suddenly 'resurrect' from the dead. A tombstone can only be permanently dropped when it is compacted into the absolute bottom-most level of the LSM hierarchy, where no older versions can possibly exist below it.

---

### Verse 35

```text
कालेन सीमिते धर्मे ह्रासो भवति वस्तुषु ।
स्वयमेव विलीयेत सञ्चयस्तन्त्रपालितः ॥
```

**पदच्छेदः**: कालेन सीमिते धर्मे ह्रासः भवति वस्तुषु । स्वयम् एव विलीयेत सञ्चयः तन्त्र-पालितः ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **कालेन** | `काल` | पुंलिंग नाम | तृतीया एकवचन | प्रकृत्या तृतीया : समयेन (by time) |
| **सीमिते** | `सीमा + इतच्` | कृदन्तरूप सप्तमी एकवचन पुंलिंग | सति-सप्तमी | टी-टी-एल-मर्यादिते (when bounded by Time-to-Live - TTL) |
| **धर्मे** | `धर्म` | पुंलिंग नाम | सप्तमी एकवचन | जीवनावधौ (in lifespan) |
| **ह्रासः** | `ह्रास` | पुंलिंग नाम | प्रथमा एकवचन | क्षयः (decay / expiration) |
| **भवति** | `√भू + लट्` | परस्मैपद लट् | प्रथमपुरुष एकवचन | जायते (occurs) |
| **वस्तुषु** | `वस्तु` | नपुंसकलिंग नाम | सप्तमी बहुवचन | अभिलेखेषु (in records) |
| **स्वयम्** | `स्वयम्` | अव्ययम् | अव्ययम् | आत्मनैव (automatically) |
| **एव** | `एव` | अव्ययम् | अव्ययम् | निश्चये (verily) |
| **विलीयेत** | `वि + √ली + विधि-लिङ्` | आत्मनेपद लिङ् | प्रथमपुरुष एकवचन | नश्येत् (dissolves / purges) |
| **सञ्चयः** | `सञ्चय` | पुंलिंग नाम | प्रथमा एकवचन | दत्तनिधिः (the expired dataset) |
| **तन्त्रपालितः** | `तन्त्र + पालित` | तृतीया-तत्पुरुष पुंलिंग | प्रथमा एकवचन | व्यवस्थासंरक्षितः (governed by compaction) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: Time-To-Live (TTL) and Expiration: modern LSM engines support native TTL per key or column family. Rather than issuing explicit DELETEs, keys carry an expiration timestamp. During compaction, the compaction filter checks whether current_time >= key_timestamp + TTL; if expired, the record is discarded without ever creating an intermediate tombstone, maintaining optimal storage hygiene for metrics and session caches.

---

## Canto 8: वाचनमार्गः बहुस्तरशोधनञ्च (The Read Path: MemTable, Cache Hierarchy and Multi-Way Merging)

### Verse 36

```text
याचितस्य तु वस्तुनो मार्गो भवति तादृशः ।
स्मृतितः प्रविशेद् विद्वान् स्तरशश्च विलोकयेत् ॥
```

**पदच्छेदः**: याचितस्य तु वस्तुनः मार्गः भवति तादृशः । स्मृतितः प्रविशेत् विद्वान् स्तरशः च विलोकयेत् ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **याचितस्य** | `√याच् + क्त` | कृदन्तरूप षष्ठी एकवचन नपुंसकलिंग | षष्ठी एकवचन | प्रार्थितस्य (of the queried record) |
| **तु** | `तु` | अव्ययम् | अव्ययम् | विशेषे (indeed) |
| **वस्तुनः** | `वस्तु` | नपुंसकलिंग नाम | षष्ठी एकवचन | दत्तस्य (of key-value payload) |
| **मार्गः** | `मार्ग` | पुंलिंग नाम | प्रथमा एकवचन | रीड-पाथ (the read query execution path) |
| **भवति** | `√भू + लट्` | परस्मैपद लट् | प्रथमपुरुष एकवचन | विद्यते (is) |
| **तादृशः** | `तादृश्` | विशेषण पुंलिंग | प्रथमा एकवचन | एवंविधः (structured as follows) |
| **स्मृतितः** | `स्मृति + तसिँ` | अव्ययम् | अव्ययम् | मेमटेबल-सञ्चयात् (starting from active MemTable in RAM) |
| **प्रविशेत्** | `प्र + √विश् + विधि-लिङ्` | परस्मैपद लिङ् | प्रथमपुरुष एकवचन | गच्छेत् (should enter) |
| **विद्वान्** | `विद्वस्` | पुंलिंग नाम | प्रथमा एकवचन | तन्त्रज्ञः / क्वेरी-इञ्जन् (the query engine) |
| **स्तरशः** | `स्तर + शस्` | अव्ययम् | अव्ययम् | क्रमेण स्तरान् (level by level down on-disk SSTables) |
| **च** | `च` | अव्ययम् | अव्ययम् | संयोजकः (and) |
| **विलोकयेत्** | `वि + √लोक् + णिच् + लिङ्` | परस्मैपद लिङ् | प्रथमपुरुष एकवचन | अन्विषेत् (should inspect) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: The Complete Read Path: To execute a point read (GET key), the engine traverses the hierarchy in strict temporal order: (1) Active MemTable in RAM; (2) Immutable MemTables awaiting flush; (3) Level 0 SSTables (checking Bloom filters); (4) Level 1 through Level n SSTables. Because newer layers contain newer sequence numbers, the search halts the exact microsecond the requested key is found.

---

### Verse 37

```text
शीघ्रकोष्ठे समासाद्य भुङ्क्ते तत्रैव मानवः ।
चक्रिकायाः प्रवेशस्तु निरुद्धः सुखदायके ॥
```

**पदच्छेदः**: शीघ्र-कोष्ठे सम्-आसाद्य भुङ्क्ते तत्र एव मानवः । चक्रिकायाः प्रवेशः तु निरुद्धः सुख-दायके ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **शीघ्रकोष्ठे** | `शीघ्र + कोष्ठ` | कर्मधारय पुंलिंग | सप्तमी एकवचन | ब्लॉक-कैशे (in the in-memory Block Cache) |
| **समासाद्य** | `सम् + आ + √सद् + ल्यप्` | कृदन्तरूप अव्यय | अव्ययम् | प्राप्य (having located) |
| **भुङ्क्ते** | `√भुज् + लट्` | आत्मनेपद लट् | प्रथमपुरुष एकवचन | गृह्णाति (serves the record / consumes) |
| **तत्र** | `तत्र` | अव्ययम् | अव्ययम् | तस्मिन् कैशे (therein) |
| **एव** | `एव` | अव्ययम् | अव्ययम् | अवधारणे (strictly) |
| **मानवः** | `मानव` | पुंलिंग नाम | प्रथमा एकवचन | ग्राहकः (the client) |
| **चक्रिकायाः** | `चक्रिका` | स्त्रीलिंग नाम | षष्ठी एकवचन | डिस्क-यन्त्रस्य (of the disk) |
| **प्रवेशः** | `प्रवेश` | पुंलिंग नाम | प्रथमा एकवचन | आई-ओ-गमनम् (physical disk read access) |
| **तु** | `तु` | अव्ययम् | अव्ययम् | विशेषे (however) |
| **निरुद्धः** | `नि + √रुध् + क्त` | कृदन्तरूप पुंलिंग | प्रथमा एकवचन | निवारितः (completely bypassed) |
| **सुखदायके** | `सुख + दायक` | विशेषण नपुंसकलिंग | सप्तमी एकवचन | कल्याणकारके (in high-performance cache hits) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: The Multi-Tier Cache Hierarchy: RocksDB deploys an uncompressed Block Cache in RAM storing frequently accessed 4KB data blocks. If a point read hits the Block Cache (or the row cache), the query resolves in sub-microsecond RAM speed, completely bypassing physical disk I/O ('cakrikāyāḥ praveśas tu niruddhaḥ'). The disk is only touched upon cold cache misses.

---

### Verse 38

```text
विस्तीर्णे च समन्वेषे सर्वद्वाराणि सङ्गताः ।
अग्रिमं शोधयन् पश्यन् मेधावी विनिरीक्षते ॥
```

**पदच्छेदः**: विस्तीर्णे च सम्-अन्वेषे सर्व-द्वाराणि सङ्गताः । अग्रिमम् शोधयन् पश्यन् मेधावी वि-निरीक्षते ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **विस्तीर्णे** | `वि + √स्तॄ + क्त` | कृदन्तरूप पुंलिंग | सप्तमी एकवचन | सति-सप्तमी (in a range scan query) |
| **च** | `च` | अव्ययम् | अव्ययम् | संयोजकः (and) |
| **समन्वेषे** | `सम् + अनु + √इष् + अ` | पुंलिंग नाम | सप्तमी एकवचन | सति-सप्तमी (in range scan / iteration) |
| **सर्वद्वाराणि** | `सर्व + द्वार` | कर्मधारय नपुंसकलिंग | प्रथमा बहुवचन | समस्त-एस-एस-टेबल्स् (all active SSTable levels) |
| **सङ्गताः** | `सम् + √गम् + क्त` | कृदन्तरूप पुंलिंग | प्रथमा बहुवचन | संयोजिताः (coupled together) |
| **अग्रिमम्** | `अग्रिम` | विशेषण | द्वितीया एकवचन पुंलिंग | न्यूनतमकुञ्चिकाम् (the current smallest key) |
| **शोधयन्** | `√शुध् + णिच् + शतृ` | शतृ-प्रत्ययान्तरूप पुंलिंग | प्रथमा एकवचन | अन्विषन् (evaluating) |
| **पश्यन्** | `√दृश् + शतृ` | शतृ-प्रत्ययान्तरूप पुंलिंग | प्रथमा एकवचन | अवलोकयन् (observing) |
| **मेधावी** | `मेधाविन्` | पुंलिंग नाम | प्रथमा एकवचन | मर्ज-इटरेटर (the Multi-Way Merge Iterator) |
| **विनिरीक्षते** | `वि + नि + √ईक्ष् + लट्` | आत्मनेपद लट् | प्रथमपुरुष एकवचन | क्रमशः प्रसरति (advances systematically) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: Range Scans and Priority Queue Iterators: A range scan (SCAN key_start TO key_end) cannot simply check one file. It constructs a Multi-Way Merging Iterator using a min-heap priority queue across all active MemTables and on-disk SSTable levels. The iterator continuously pops the current smallest key across all streams, streaming an ordered view to the user in O(log L) time per step.

---

### Verse 39

```text
नवीनमेव गृह्णीयात् पुरातनं परित्यजेत् ।
कालचिह्नेन संसिद्धः क्रमः संपरिरक्ष्यते ॥
```

**पदच्छेदः**: नवीनम् एव गृह्णीयात् पुरातनम् परि-त्यजेत् । काल-चिह्नेन सम्-सिद्धः क्रमः सम्-परिरक्ष्यते ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **नवीनम्** | `नवीन` | विशेषण | द्वितीया एकवचन नपुंसकलिंग | उच्चसिक्वेन्स-दत्तम् (the newest version) |
| **एव** | `एव` | अव्ययम् | अव्ययम् | अवधारणे (strictly) |
| **गृह्णीयात्** | `√ग्रह् + विधि-लिङ्` | परस्मैपद लिङ् | प्रथमपुरुष एकवचन | स्वीकुर्यात् (must yield) |
| **पुरातनम्** | `पुरातन` | विशेषण | द्वितीया एकवचन नपुंसकलिंग | प्राचीनम् (the older duplicate) |
| **परित्यजेत्** | `परि + √त्यज् + विधि-लिङ्` | परस्मैपद लिङ् | प्रथमपुरुष एकवचन | उपेक्षेत (must discard) |
| **कालचिह्नेन** | `काल + चिह्न` | षष्ठी-तत्पुरुष नपुंसकलिंग | तृतीया एकवचन | करणे तृतीया (by sequence number timestamp) |
| **संसिद्धः** | `सम् + √साध् + क्त` | कृदन्तरूप पुंलिंग | प्रथमा एकवचन | प्रमाणितः (proven / verified) |
| **क्रमः** | `क्रम` | पुंलिंग नाम | प्रथमा एकवचन | सत्यक्रमः (temporal consistency order) |
| **संपरिरक्ष्यते** | `सम् + परि + √रक्ष् + कर्मणि लट्` | कर्मणि लट् | प्रथमपुरुष एकवचन | पाल्यते (is upheld) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: On-the-Fly Deduplication: As the merge iterator advances across multiple SSTables, it frequently encounters the identical key appearing in three different levels. The iterator inspects the monotonic sequence number (or version timestamp) stamped on each record: it yields the newest version to the application and silently skips past the older duplicates.

---

### Verse 40

```text
एकस्मिन् प्रापिते सत्ये विरमेत परीक्षणम् ।
अल्पेनैव प्रवाहेण कार्यं संसिद्धिमाप्नुयात् ॥
```

**पदच्छेदः**: एकस्मिन् प्रापिते सत्ये विरमेत परीक्षणम् । अल्पेन एव प्रवाहेण कार्यम् संसिद्धिम् आप्नुयात् ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **एकस्मिन्** | `एक` | संख्या-विशेषण | सप्तमी एकवचन नपुंसकलिंग | सत्ये विशेषणम् (in a single) |
| **प्रापिते** | `प्र + √आप् + णिच् + क्त` | कृदन्तरूप सप्तमी एकवचन | सति-सप्तमी | लब्धे सति (having been found) |
| **सत्ये** | `सत्य` | नपुंसकलिंग नाम | सप्तमी एकवचन | यथार्थसंस्करणे (valid latest record) |
| **विरमेत** | `वि + √रम् + विधि-लिङ्` | आत्मनेपद लिङ् | प्रथमपुरुष एकवचन | निवर्तेत (short-circuits / halts) |
| **परीक्षणम्** | `परीक्षण` | नपुंसकलिंग नाम | प्रथमा एकवचन | अन्वेषणप्रक्रिया (search execution) |
| **अल्पेन** | `अल्प` | विशेषण | तृतीया एकवचन पुंलिंग | प्रवाहेण विशेषणम् (by minimal) |
| **एव** | `एव` | अव्ययम् | अव्ययम् | अवधारणे (strictly) |
| **प्रवाहेण** | `प्रवाह` | पुंलिंग नाम | तृतीया एकवचन | आई-ओ-प्रवाहेण (by minimal disk read I/O) |
| **कार्यम्** | `कार्य` | नपुंसकलिंग नाम | प्रथमा एकवचन | याचनाकार्यम् (point query) |
| **संसिद्धिम्** | `सम् + सिद्धि` | स्त्रीलिंग नाम | द्वितीया एकवचन | सफलताम् (success) |
| **आप्नुयात्** | `√आप् + विधि-लिङ्` | परस्मैपद लिङ् | प्रथमपुरुष एकवचन | प्राप्नोति (attains) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: Short-Circuiting Point Queries: In Leveled Compaction, because each level L1..Ln contains mutually exclusive, non-overlapping key ranges, a point query checks at most one SSTable per level. The moment the key is located, the query short-circuits and terminates immediately, guaranteeing that most point reads resolve after touching at most one or two files.

---

## Canto 9: आधुनिकविस्तारः राक्सडीबी-तन्त्रञ्च (Modern Innovations: RocksDB, NVMe and KV Separation (WiscKey))

### Verse 41

```text
अनेकतन्तुसंबद्धं राक्स-तन्त्रं प्रतिष्ठितम् ।
द्रुतवेगेन धावन्ति लेखाश्च बहुधा ययुः ॥
```

**पदच्छेदः**: अनेक-तन्तु-संबद्धम् राक्स-तन्त्रम् प्रतिष्ठितम् । द्रुत-वेगेन धावन्ति लेखाः च बहुधा ययुः ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **अनेकतन्तुसंबद्धम्** | `अनेक + तन्तु + संबद्ध` | बहुव्रीहि नपुंसकलिंग | प्रथमा एकवचन | मल्टीथ्रेडेड-संरचितम् (multi-threaded concurrent architecture) |
| **राक्सतन्त्रम्** | `राक्स + तन्त्र` | कर्मधारय नपुंसकलिंग | प्रथमा एकवचन | राक्सडीबी (RocksDB by Meta) |
| **प्रतिष्ठितम्** | `प्रति + √स्था + क्त` | कृदन्तरूप नपुंसकलिंग | प्रथमा एकवचन | निर्मितम् (established) |
| **द्रुतवेगेन** | `द्रुत + वेग` | तृतीया एकवचन पुंलिंग | क्रियाविशेषणवत् | तीव्रगत्या (at blistering multi-core speeds) |
| **धावन्ति** | `√धाव् + लट्` | परस्मैपद लट् | प्रथमपुरुष बहुवचन | प्रवहन्ति (stream) |
| **लेखाः** | `लेख` | पुंलिंग नाम | प्रथमा बहुवचन | कम्पैक्शन-कार्याणि (flush and compaction tasks) |
| **च** | `च` | अव्ययम् | अव्ययम् | संयोजकः (and) |
| **बहुधा** | `बहुधा` | रीतिवाचक अव्यय | अव्ययम् | अनेकतन्तुभिः (in parallel threads) |
| **ययुः** | `√या + लिट्` | परस्मैपद लिट् | प्रथमपुरुष बहुवचन | प्रसरन्ति (execute) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: Evolution from LevelDB to RocksDB: Sanjay Ghemawat and Jeff Dean created LevelDB at Google as a single-threaded embedded engine. In 2012, Facebook (Meta) forked LevelDB to create RocksDB, re-architecting it for massive multi-core server hardware. RocksDB introduced parallel multi-threaded flush, concurrent multi-threaded compaction, prefix bloom filters and vectorized memtables, powering modern hyper-scale infrastructure.

---

### Verse 42

```text
कुलभेदेन विन्यस्ता वर्गाः संविभजन्ति तत् ।
एकस्मिन्नेव सम्बन्धे विविधा वृत्तयः स्थिताः ॥
```

**पदच्छेदः**: कुल-भेदेन विन्यस्ताः वर्गाः सम्-विभजन्ति तत् । एकस्मिन् एव सम्बन्धे विविधाः वृत्तयः स्थिताः ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **कुलभेदेन** | `कुल + भेद` | षष्ठी-तत्पुरुष पुंलिंग | तृतीया एकवचन | करणे तृतीया (by family / schema categorization) |
| **विन्यस्ताः** | `वि + नि + √अस् + क्त` | कृदन्तरूप पुंलिंग | प्रथमा बहुवचन | स्थापिताः (arrayed) |
| **वर्गाः** | `वर्ग` | पुंलिंग नाम | प्रथमा बहुवचन | कॉलम-फैमिली (Column Families) |
| **संविभजन्ति** | `सम् + वि + √भज् + लट्` | परस्मैपद लट् | प्रथमपुरुष बहुवचन | विभाजयन्ति (partition) |
| **तत्** | `तद्` | सर्वनाम नपुंसकलिंग | द्वितीया एकवचन | सञ्चयतन्त्रम् (the database) |
| **एकस्मिन्** | `एक` | संख्या-विशेषण | सप्तमी एकवचन पुंलिंग | सम्बन्धे विशेषणम् (in a single) |
| **एव** | `एव` | अव्ययम् | अव्ययम् | अवधारणे (strictly) |
| **सम्बन्धे** | `सम्बन्ध` | पुंलिंग नाम | सप्तमी एकवचन | वाल्-लेखाधारे (shared Write-Ahead Log) |
| **विविधाः** | `विविध` | विशेषण | प्रथमा बहुवचन स्त्रीलिंग | वृत्तयः विशेषणम् (diverse) |
| **वृत्तयः** | `वृत्ति` | स्त्रीलिंग नाम | प्रथमा बहुवचन | एस-एस-टेबल-श्रेणयः (independent LSM hierarchies) |
| **स्थिताः** | `√स्था + क्त` | कृदन्तरूप स्त्रीलिंग | प्रथमा बहुवचन | प्रतिष्ठिताः (coexist) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: Column Families: RocksDB introduced Column Families (varga-vibhāga), allowing applications to partition keys into logical sets that possess independent MemTables, independent Bloom filters and independent compaction configurations, while sharing a single, unified Write-Ahead Log. This enables atomic cross-family transactions while insulating high-churn metadata from large static datasets.

---

### Verse 43

```text
द्रुतधातुशिलापीठे नूतनेषु च यन्त्रके ।
लेखनस्य प्रभावोऽयं शतधा वर्धते पुनः ॥
```

**पदच्छेदः**: द्रुत-धातु-शिला-पीठे नूतनेषु च यन्त्रके । लेखनस्य प्रभावः अयम् शतधा वर्धते पुनः ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **द्रुतधातुशिलापीठे** | `द्रुत + धातु + शिला + पीठ` | सप्तमी एकवचन नपुंसकलिंग | सप्तमी एकवचन | एन-वी-एम-ई-एस-एस-डी-पीठे (on modern NVMe flash storage) |
| **नूतनेषु** | `नूतन` | विशेषण | सप्तमी बहुवचन नपुंसकलिंग | यन्त्रके विशेषणम् (in modern) |
| **च** | `च` | अव्ययम् | अव्ययम् | संयोजकः (and) |
| **यन्त्रके** | `यन्त्रक` | नपुंसकलिंग नाम | सप्तमी एकवचन | हार्डवेयर-यन्त्रे (in hardware environments) |
| **लेखनस्य** | `लेखन` | नपुंसकलिंग नाम | षष्ठी एकवचन | सञ्चयस्य (of write throughput) |
| **प्रभावः** | `प्रभाव` | पुंलिंग नाम | प्रथमा एकवचन | वेगः (potency and bandwidth) |
| **अयम्** | `इदम्` | सर्वनाम पुंलिंग | प्रथमा एकवचन | प्रभावस्य विशेषणम् (this) |
| **शतधा** | `शतधा` | अव्ययम् | अव्ययम् | शतगुणम् (a hundredfold) |
| **वर्धते** | `√वृध् + लट्` | आत्मनेपद लट् | प्रथमपुरुष एकवचन | उद्गच्छति (multiplies) |
| **पुनः** | `पुनर्` | अव्ययम् | अव्ययम् | भूयः (further) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: Hardware Co-Evolution with NVMe: original LSM-Trees were designed for rotational HDDs. Modern PCIe Gen 4/5 NVMe SSDs deliver millions of IOPS across 64,000 parallel hardware submission queues. RocksDB adapted to this hardware revolution by eliminating global thread locks, optimizing direct I/O and leveraging asynchronous I/O (io_uring on Linux), streaming gigabytes of data per second across flash channels.

---

### Verse 44

```text
कुञ्चिकां स्थापयेत् चक्रे द्रव्यं दूरे विनिक्षिपेत् ।
विभागेन कृतेनैव मर्दने लघुता भवेत् ॥
```

**पदच्छेदः**: कुञ्चिकाम् स्थापयेत् चक्रे द्रव्यम् दूरे वि-निक्षिपेत् । विभागेन कृतेन एव मर्दने लघुता भवेत् ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **कुञ्चिकाम्** | `कुञ्चिका` | स्त्रीलिंग नाम | द्वितीया एकवचन | केवलं की-दत्तम् (the small key index entry) |
| **स्थापयेत्** | `स्था + णिच् + लिङ्` | परस्मैपद लिङ् | प्रथमपुरुष एकवचन | रक्षेत् (should retain in LSM-tree) |
| **चक्रे** | `चक्र` | नपुंसकलिंग नाम | सप्तमी एकवचन | एल-एस-एम-चक्रे (in the sorted LSM levels) |
| **द्रव्यम्** | `द्रव्य` | नपुंसकलिंग नाम | द्वितीया एकवचन | बृहन्मूल्यम् (the large value payload) |
| **दूरे** | `दूर` | अव्ययम् / सप्तमी | अव्ययम् | पृथक्-सञ्चिकायाम् (in a separate append-only Blob Log - vLog) |
| **विनिक्षिपेत्** | `वि + नि + √क्षिप् + लिङ्` | परस्मैपद लिङ् | प्रथमपुरुष एकवचन | निक्षिपेत् (should store) |
| **विभागेन** | `विभाग` | पुंलिंग नाम | तृतीया एकवचन | करणे तृतीया (by Key-Value Separation: WiscKey / BadgerDB) |
| **कृतेन** | `√कृ + क्त` | कृदन्तरूप तृतीया एकवचन | तृतीया एकवचन | अनुष्ठितेन (implemented) |
| **एव** | `एव` | अव्ययम् | अव्ययम् | अवधारणे (strictly) |
| **मर्दने** | `मर्दन` | नपुंसकलिंग नाम | सप्तमी एकवचन | कम्पैक्शन-काले (during compaction) |
| **लघुता** | `लघुता` | स्त्रीलिंग नाम | प्रथमा एकवचन | अल्पभारः (massive reduction in write amplification) |
| **भवेत्** | `√भू + विधि-लिङ्` | परस्मैपद लिङ् | प्रथमपुरुष एकवचन | जायेत (occurs) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: Key-Value Separation (WiscKey / BadgerDB): in standard LSM-trees, both keys and large values are rewritten repeatedly during compaction, causing 10x to 30x write amplification that wears out SSDs. WiscKey (FAST 2016) proposed separating keys from values: keys and value-pointers are stored in the sorted LSM-tree, while large values are appended to a separate Value Log (vLog). Compaction sorts only keys, slashing write amplification by over 90%.

---

### Verse 45

```text
मेघजाले समाक्रान्ते सर्वे खण्डाः प्रतिष्ठिताः ।
अनन्तस्यापि सम्भारो धार्यते वलयादपि ॥
```

**पदच्छेदः**: मेघ-जाले सम्-आक्रान्ते सर्वे खण्डाः प्रतिष्ठिताः । अनन्तस्य अपि सम्भारः धार्यते वलयात् अपि ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **मेघजाले** | `मेघ + जाल` | सप्तमी एकवचन नपुंसकलिंग | सप्तमी एकवचन | क्लाउड-ऑब्जेक्ट-स्टोरेज-मध्ये (in cloud object storage: AWS S3 / Google GCS) |
| **समाक्रान्ते** | `सम् + आ + √क्रम् + क्त` | कृदन्तरूप नपुंसकलिंग | सप्तमी एकवचन | व्यापिते (distributed) |
| **सर्वे** | `सर्व` | सर्वनाम पुंलिंग | प्रथमा बहुवचन | निखिलाः (all) |
| **खण्डाः** | `खण्ड` | पुंलिंग नाम | प्रथमा बहुवचन | एस-एस-टेबल-पत्राणि (immutable SSTable files) |
| **प्रतिष्ठिताः** | `प्रति + √स्था + क्त` | कृदन्तरूप पुंलिंग | प्रथमा बहुवचन | निक्षिप्यन्ते (are stored disaggregated) |
| **अनन्तस्य** | `अनन्त` | विशेषण | षष्ठी एकवचन पुंलिंग | असीमस्य (of boundless) |
| **अपि** | `अपि` | अव्ययम् | अव्ययम् | संभावनार्थे (even) |
| **सम्भारः** | `सम्भार` | पुंलिंग नाम | प्रथमा एकवचन | दत्तनिधिः (petabyte data volume) |
| **धार्यते** | `√धृ + कर्मणि लट्` | कर्मणि लट् | प्रथमपुरुष एकवचन | पाल्यते (is retained) |
| **वलयात्** | `वलय` | पुंलिंग नाम | पञ्चमी एकवचन | अपादाने पञ्चमी : लोकल-डिस्क-मर्यादातः (beyond the limits of local disk) |
| **अपि** | `अपि` | अव्ययम् | अव्ययम् | समुच्चये (also) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: Cloud-Native Disaggregated Storage: modern cloud databases (such as CockroachDB, TiKV, ClickHouse and Rockset) decouple computation from storage. Because SSTables are immutable files, they can be streamed directly to cloud object storage (Amazon S3, Google Cloud Storage, or Azure Blob). Local NVMe drives act as ephemeral Block Caches, while the infinite cloud object store holds the durable LSM levels, enabling instant horizontal elasticity.

---

## Canto 10: सिद्धान्तनिष्कर्षः सार्वकालिकसत्यञ्च (Architectural Synthesis, Memory Metaphor and Enduring Legacy)

### Verse 46

```text
रूम्-शास्त्रेण समादिष्टं संसारे नास्ति सर्वथा ।
एकं जयति यत्नेन द्वितीयं क्षीयते किल ॥
```

**पदच्छेदः**: रूम्-शास्त्रेण सम्-आदिष्टम् संसारे न अस्ति सर्वथा । एकम् जयति यत्नेन द्वितीयम् क्षीयते किल ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **रूम्-शास्त्रेण** | `रूम् + शास्त्र (RUM Conjecture)` | तृतीया एकवचन नपुंसकलिंग | तृतीया एकवचन | अथानासूलिस-प्रणीतेन नियमेन (by the RUM Conjecture) |
| **समादिष्टम्** | `सम् + आ + √दिश् + क्त` | कृदन्तरूप नपुंसकलिंग | प्रथमा एकवचन | प्रतिपादितम् (ordained) |
| **संसारे** | `संसार` | पुंलिंग नाम | सप्तमी एकवचन | तन्त्रजगति (in distributed systems engineering) |
| **न** | `न` | निषेधार्थक अव्यय | अव्ययम् | निषेधे (never) |
| **अस्ति** | `√अस् + लट्` | परस्मैपद लट् | प्रथमपुरुष एकवचन | विद्यते (exists) |
| **सर्वथा** | `सर्वथा` | अव्ययम् | अव्ययम् | निखिलसिद्धियुक्तम् (a free lunch) |
| **एकम्** | `एक` | संख्या-सर्वनाम | द्वितीया एकवचन नपुंसकलिंग | एकं गुणम्: यथा लेखनम् (one dimension: writes) |
| **जयति** | `√जि + लट्` | परस्मैपद लट् | प्रथमपुरुष एकवचन | विजयी करोति (one optimizes) |
| **यत्नेन** | `यत्न` | पुंलिंग नाम | तृतीया एकवचन | करणे (by design) |
| **द्वितीयम्** | `द्वितीय` | संख्या-सर्वनाम | प्रथमा एकवचन नपुंसकलिंग | अपरम्: यथा वाचनम् (another dimension: reads) |
| **क्षीयते** | `√क्षी + कर्मणि लट्` | कर्मणि लट् | प्रथमपुरुष एकवचन | हीनं भवति (degrades) |
| **किल** | `किल` | अव्ययम् | अव्ययम् | प्रसिद्धौ (truly) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: The Systems Engineering Trilemma: The RUM Conjecture mathematically codifies that in data management, there is no magical panacea. If you optimize for ultra-fast sequential updates (LSM-trees), you accept read amplification and background compaction overhead. If you optimize for instant single-page reads (B-Trees), you suffer write amplification and random I/O stalls. Mastering systems architecture means understanding tradeoffs with intellectual honesty.

---

### Verse 47

```text
मानवस्य स्मृतिश्चैव स्तम्भवद् वर्तते सदा ।
दिने लिखति सम्भारं रात्रौ संमर्द्य तिष्ठति ॥
```

**पदच्छेदः**: मानवस्य स्मृतिः च एव स्तम्भ-वत् वर्तते सदा । दिने लिखति सम्भारम् रात्रौ सम्-मर्द्य तिष्ठति ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **मानवस्य** | `मानव` | पुंलिंग नाम | षष्ठी एकवचन | मनुष्यस्य (of a human being) |
| **स्मृतिः** | `स्मृति` | स्त्रीलिंग नाम | प्रथमा एकवचन | मस्तिष्कमेधा (biological memory) |
| **च** | `च` | अव्ययम् | अव्ययम् | संयोजकः (and) |
| **एव** | `एव` | अव्ययम् | अव्ययम् | अवधारणे (indeed) |
| **स्तम्भवत्** | `स्तम्भ + वतिँ` | अव्ययम् | अव्ययम् | एल-एस-एम-इव (like an LSM-Tree) |
| **वर्तते** | `√वृत् + लट्` | आत्मनेपद लट् | प्रथमपुरुष एकवचन | विद्यते (operates) |
| **सदा** | `सदा` | अव्ययम् | अव्ययम् | सर्वदा (perpetually) |
| **दिने** | `दिन` | नपुंसकलिंग नाम | सप्तमी एकवचन | जाग्रदवस्थायाम् (during daytime waking hours) |
| **लिखति** | `√लिख् + लट्` | परस्मैपद लट् | प्रथमपुरुष एकवचन | अङ्कयति (appends new experiences into hippocampus MemTable) |
| **सम्भारम्** | `सम्भार` | पुंलिंग नाम | द्वितीया एकवचन | अनुभवभारम् (stream of sensory inputs) |
| **रात्रौ** | `रात्रि` | स्त्रीलिंग नाम | सप्तमी एकवचन | सुषुप्तौ (during deep sleep and REM) |
| **संमर्द्य** | `सम् + √मर्द् + ल्यप्` | कृदन्तरूप अव्यय | अव्ययम् | कम्पैक्शनं कृत्वा (compacting and consolidating) |
| **तिष्ठति** | `√स्था + लट्` | परस्मैपद लट् | प्रथमपुरुष एकवचन | शान्तं भवति (reorganizes into cerebral cortex SSTables) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: The Neurobiological Metaphor: In an extraordinary conceptual parallel, human neuroscience functions as an LSM-Tree! During the day, our senses write an unceasing, append-only log of experiences into the hippocampus (the active volatile MemTable). At night during deep sleep and REM cycles, the brain executes background Compaction: consolidating short-term memories, discarding obsolete trivia and transferring crystallized, long-term wisdom into the immutable cerebral cortex.

---

### Verse 48

```text
कासान्द्रा प्रमुखास्तन्त्रे जगुस्तत्त्वस्य वैभवम् ।
आधुनिकस्य विज्ञानस्य स्तम्भोऽयं दृढतां गतः ॥
```

**पदच्छेदः**: कासान्द्रा-प्रमुखाः तन्त्रे जगुः तत्त्वस्य वैभवम् । आधुनिकस्य विज्ञानस्य स्तम्भः अयम् दृढताम् गतः ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **कासान्द्राप्रमुखाः** | `कासान्द्रा + प्रमुख` | बहुव्रीहि पुंलिंग | प्रथमा बहुवचन | कासान्द्रा-राक्सडीबी-प्रभृतयः (Apache Cassandra, RocksDB, ScyllaDB, CockroachDB) |
| **तन्त्रे** | `तन्त्र` | नपुंसकलिंग नाम | सप्तमी एकवचन | संगणकतन्त्रे (in modern systems computing) |
| **जगुः** | `√गै + लिट्` | परस्मैपद लिट् | प्रथमपुरुष बहुवचन | प्रशशंसुः (sang / celebrated) |
| **तत्त्वस्य** | `तत्त्व` | नपुंसकलिंग नाम | षष्ठी एकवचन | एल-एस-एम-सिद्धान्तस्य (of the LSM principle) |
| **वैभवम्** | `वैभव` | नपुंसकलिंग नाम | द्वितीया एकवचन | माहात्म्यम् (glory and architectural supremacy) |
| **आधुनिकस्य** | `आधुनिक` | विशेषण | षष्ठी एकवचन नपुंसकलिंग | विज्ञानस्य विशेषणम् (of modern) |
| **विज्ञानस्य** | `विज्ञान` | नपुंसकलिंग नाम | षष्ठी एकवचन | दत्तविज्ञानस्य (of computer science and big data) |
| **स्तम्भः** | `स्तम्भ` | पुंलिंग नाम | प्रथमा एकवचन | महाधारः (the pillar / bedrock) |
| **अयम्** | `इदम्` | सर्वनाम पुंलिंग | प्रथमा एकवचन | स्तम्भस्य विशेषणम् (this) |
| **दृढताम्** | `दृढता` | स्त्रीलिंग नाम | द्वितीया एकवचन | स्थैर्यम् (immovable fortitude) |
| **गतः** | `√गम् + क्त` | कृदन्तरूप पुंलिंग | प्रथमा एकवचन | प्राप्तः (has attained) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: The Bedrock of Modern Big Data: From Google Bigtable powering search index ingestion, to RocksDB powering Meta's social graph, to Apache Cassandra and ScyllaDB powering global streaming backbones, the Log-Structured Merge-Tree is the undisputed pillar of 21st-century distributed data infrastructure.

---

### Verse 49

```text
अनित्यं भौतिकं यन्त्रं सिद्धान्तस्तु सनातनः ।
क्रमेण सञ्चिते ज्ञाने मोक्षः संपद्यते परः ॥
```

**पदच्छेदः**: अनित्यम् भौतिकम् यन्त्रम् सिद्धान्तः तु सनातनः । क्रमेण सञ्चिते ज्ञाने मोक्षः सम्-पद्यते परः ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **अनित्यम्** | `अ + नित्य` | नञ्-तत्पुरुष नपुंसकलिंग | प्रथमा एकवचन | नश्वरम् (transient / ephemeral) |
| **भौतिकम्** | `भौतिक` | विशेषण नपुंसकलिंग | प्रथमा एकवचन | यन्त्रस्य विशेषणम् (physical hardware) |
| **यन्त्रम्** | `यन्त्र` | नपुंसकलिंग नाम | प्रथमा एकवचन | डिस्क-मशीन (server hardware, spinning platters, flash chips) |
| **सिद्धान्तः** | `सिद्धान्त` | पुंलिंग नाम | प्रथमा एकवचन | क्रमबद्धसञ्चयन्यायः (the mathematical algorithmic principle) |
| **तु** | `तु` | अव्ययम् | अव्ययम् | विशेषे (however) |
| **सनातनः** | `सनातन` | विशेषण पुंलिंग | प्रथमा एकवचन | शाश्वतः (eternal / timeless) |
| **क्रमेण** | `क्रम` | पुंलिंग नाम | तृतीया एकवचन | अनुपूर्व्या (methodically in disciplined progression) |
| **सञ्चिते** | `सम् + √चि + क्त` | कृदन्तरूप सप्तमी एकवचन | सति-सप्तमी | संग्रहीते सति (being accumulated) |
| **ज्ञाने** | `ज्ञान` | नपुंसकलिंग नाम | सप्तमी एकवचन | ब्रह्मविद्यायाम् (in true wisdom) |
| **मोक्षः** | `मोक्ष` | पुंलिंग नाम | प्रथमा एकवचन | मुक्तिः / सिद्धिः (ultimate liberation from chaos) |
| **संपद्यते** | `सम् + √पद् + लट्` | आत्मनेपद लट् | प्रथमपुरुष एकवचन | लभ्यते (is attained) |
| **परः** | `पर` | विशेषण पुंलिंग | प्रथमा एकवचन | सर्वोच्चः (supreme) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: Mortal Hardware vs Immortal Principle: Physical storage devices perish: rotational heads crash, NVMe flash cells suffer electron leakage and silicon gates degrade into dust. But the mathematical elegance of sorted append-only streaming, merge-sort compaction and probabilistic filtering is eternal. When knowledge is systematically ordered and purged of errors, intellectual liberation is achieved.

---

### Verse 50

```text
इतीदं स्तम्भशास्त्रं हि सर्वलोकसुखावहम् ।
शान्तिदं कर्मशीलानां भूयात् सर्वजयप्रदम् ॥
```

**पदच्छेदः**: इति इदम् स्तम्भ-शास्त्रम् हि सर्व-लोक-सुख-आवहम् । शान्ति-दम् कर्म-शीलानाम् भूयात् सर्व-जय-प्रदम् ॥

| पदम् (Word) | प्रकृतिः / धातुः (Base Stem/Root) | व्याकरणविभागः (Category) | विभक्तिः / लकारः (Case/Tense) | अन्वयविवरणम् (Syntactic / Contextual Role) |
| :--- | :--- | :--- | :--- | :--- |
| **इति** | `इति` | समाप्तौ अव्ययम् | अव्ययम् | ग्रन्थसमाप्तौ (thus concludes) |
| **इदम्** | `इदम्` | सर्वनाम | प्रथमा एकवचन नपुंसकलिंग | शास्त्रस्य विशेषणम् (this) |
| **स्तम्भशास्त्रम्** | `स्तम्भ + शास्त्र` | कर्मधारय नपुंसकलिंग | प्रथमा एकवचन | एल-एस-एम-ग्रन्थः (the treatise on Log-Structured Storage) |
| **हि** | `हि` | अव्ययम् | अव्ययम् | प्रसिद्धौ (indeed) |
| **सर्वलोकसुखावहम्** | `सर्व + लोक + सुख + आवह` | उपपद समास नपुंसकलिंग | प्रथमा एकवचन | विश्वकल्याणप्रदम् (bringing welfare to the whole digital world) |
| **शान्तिदम्** | `शान्ति + दा + क` | उपपद समास नपुंसकलिंग | प्रथमा एकवचन | उपद्रवहारकम् (conferring operational peace) |
| **कर्मशीलानाम्** | `कर्मन् + शील` | बहुव्रीहि पुंलिंग | षष्ठी बहुवचन | सञ्चयाभियन्तॄणाम् (for dedicated storage engineers and database builders) |
| **भूयात्** | `√भू + आशीर्लिङ्` | परस्मैपद आशीर्लिङ् | प्रथमपुरुष एकवचन | भवतु (may it ever be) |
| **सर्वजयप्रदम्** | `सर्व + जय + प्रद` | उपपद समास नपुंसकलिंग | प्रथमा एकवचन | सकलविजयदायकम् (bestowing complete triumph) |

**सञ्चयभाष्यम् (Storage Systems Commentary)**: The final benediction seals the treatise on Log-Structured Merge-Trees. May this rigorous synthesis of sequential I/O, immutable SSTables, Bloom filters and compaction mechanics serve as a fountain of clarity and operational peace for systems engineers worldwide, guiding the creation of resilient, blazing-fast and enduring data foundations for all humanity.

---

# Grammar quality bar

## Intent

New posts must be **correct classical-register Sanskrit padya**, not English checklists transliterated into Devanāgarī. Meter pads (हि तु वै सदा पथि एव अपि नु सम्यक् नित्यम्) are allowed.

## Required per verse (collapsible English)

### व्याकरणम् / Grammar map

| पदम् | रूपम् / analysis | English role |
|------|------------------|--------------|
| token as in padaccheda | stem + affix + case/lakāra | subject / object / verb / … |

**Acceptable analysis tokens** (gate looks for these patterns):

- Cases: `1/1` … `7/3`, or प्रथमा द्वितीया … सप्तमी
- Verbs: लट् लोट् लङ् विधिलिङ् + person (`3/1`, `2/1`, …) or `imp`/`opt`/`pass`
- Nominal: क्त क्तवतु तुमुन् ल्यप् क्त्वा; समास / compound
- English gloss roles: subject, object, verb, adverb, vocative, …

Minimum **3 analyzed rows** per verse.

### Word-for-word

Second column must be **English** (or IAST gloss), not a copy of the Devanāgarī cell.

| Bad | Good |
|-----|------|
| `धत्ते` → `धत्ते` | `धत्ते` → `holds / places (3sg mid.)` |
| `तस्माद्` → `तस्माद्` | `तस्माद्` → `therefore` |

### English sense

One clear sentence mapping the whole śloka. No em dash, no Oxford comma.

## Banned in verse body (quality)

- Stock seals: `तन्त्रधर्मः स उच्यते`, `कर्मयोग्यम्/ः`, filler `पञ्चाङ्गं X उच्यते` as sole content
- Hindi/hybrid: ताजता, पड़ोसी, खुला, शेल्फ, जोखिम, स्विच, बाइट्, टोकन्, हैश, …
- Latin/ASCII tech acronyms
- **Imperative stampede**: ≥3 bare imperatives and **no** finite verb in the verse

## Preferred construction patterns

1. **Finite statement**: N + N-acc + V-finite (`धत्ते`, `भवति`, `नश्यति`, `जायते`)
2. **Vidhi (injunction)**: object in द्वितीया + लोट् 2/1 (`कुरु`, `रक्ष`, `लिख`) with clear patient
3. **Hetu**: `तस्मात्` / `हि` linking cause half to effect half
4. **Nañ**: `मा` + injunctive/imperative for prohibition; `न` + finite for factual negation

## Sandhi

Write printable padya with natural sandhi; give **पदच्छेदः** fully split in details. Do not leave broken stems as if they were full sentences (`अस्थि` alone as predicate without copula or clear elliptical convention noted in grammar map).

## Coinage

Neologisms must be **transparent compounds** (e.g. `सारचिह्नम्`, `द्वारपालः`) with glossary rows. Avoid syllable-calques of English brand morphology.

## Gate commands

```text
# new post (mandatory)
python .grok/skills/sanskrit-verse-blog/scripts/gate_posts.py --quality --dates YYYY-MM-DD

# legacy purity+meter only
python .grok/skills/sanskrit-verse-blog/scripts/gate_posts.py --dates YYYY-MM-DD
```

`_bi_lib.save` runs `--quality` automatically and deletes the file on failure.

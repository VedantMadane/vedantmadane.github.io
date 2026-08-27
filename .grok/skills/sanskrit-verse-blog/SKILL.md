---
name: sanskrit-verse-blog
description: >
  Write VedantMadane Sanskrit-verse blog posts with pristine Pāṇinian padya,
  chandobaddha meter, grammar maps in collapsible English, and quality gates.
  Prefer one carefully crafted post over volume. Use when the user says go,
  go both, deepen, fix panini/chandas, or runs /sanskrit-verse-blog.
---

# Sanskrit verse blog (quality bar)

## Repo

- Path: `C:\Users\Administrator\vedantmadane.github.io`
- Branch: `master`
- Posts: `_posts/YYYY-MM-DD-<Devanāgarī-title>.md`
- Emitter: `_bi_lib.py` (`P` / `pack12` / `emit_post`) — **requires grammar maps**
- Gates:
  - Baseline: `python .grok/skills/sanskrit-verse-blog/scripts/gate_posts.py --dates …`
  - **Quality (mandatory for new posts):** same with `--quality`

## Quality over volume (non-negotiable)

| Rule | Meaning |
|------|---------|
| **One post per `go`** unless user names a multi-day range | No mass week-emit of thin padya |
| **Each verse hand-crafted** | Finite verb or clear nominal sentence; not checklist imperatives only |
| **Pristine grammar** | Correct vibhakti, lakāra, sandhi; stop-words हि तु वै सदा पथि एव अपि नु सम्यक् नित्यम् OK for meter |
| **Grammar map required** | Every verse `<details>` has **व्याकरणम् / Grammar map** table |
| **Real English wfw** | Word-for-word column is English (not Sanskrit echo) |
| **No stock seals** | Ban `तन्त्रधर्मः स उच्यते`, `कर्मयोग्यम्`, bare `पञ्चाङ्गं X उच्यते` as filler |
| **No Hindi/hybrid calques** in verse body | See `references/grammar-quality.md` |

Legacy 2026–early-2027 corpus may fail `--quality`; do **not** loosen the gate. New work must pass.

## Hard bars

### 1. Pāṇinian verse body

- Pure Devanāgarī only in `sanskrit-verse-lines`
- No Latin/ASCII digits; no hybrid loans (`टोकन्`, `API`, `canary`, …)
- Prefer classical or transparent neologisms: **प्रतीकम्**, **द्वारसेवा**, **सारचिह्नम्**
- Sandhi readable; padaccheda in details shows separated stems
- Prefer one clear finite verb per half-verse; imperatives allowed when morphologically correct (लोट्)

### 2. Chandobaddha

| Meter | Shape | Gate |
|-------|--------|------|
| **अनुष्टुभ्** | 2 lines | each **14–18** akṣaras (target 16); pair total 28–36 |
| **उपजाति** | 4 lines | each **exactly 11** |

Count with `scripts/meter.py`. Pathyā laghu/guru preferred when writing.

### 3. Collapsible English (every verse)

Required sections inside verse `<details>` (emitter builds these):

1. **पदच्छेदः** — sandhi-split line(s)
2. **व्याकरणम् / Grammar map** — table: पदम् \| रूपम्/analysis \| English role  
   Analysis must mark case (1/1, द्वितीया, …) or lakāra (लट् 3/1, लोट् 2/1, …) or समास
3. **Word-for-word** — Sanskrit → **English** gloss per token
4. **Gloss table** — key technical lemmas
5. **English sense** — one plain sentence (no em/en dash; no Oxford comma)
6. **वृत्तमिति** — meter note

### 4. Post shape

- 12 verses: chapters 2+2+1+2+2+1+2
- Unique topic title vs prior dates
- No U+2014 / U+2013; `ox()` on English
- Tags include `panini` and `quality`

## Workflow: `go` (default = quality single)

1. Tip = day after last `2027-*.md` (or user range).
2. **Default: write one post** for that tip date. Only write a multi-day stretch if the user explicitly asks for a range or “week”.
3. Draft 12 verses with real morphology; fill `g=` grammar rows and English `w=` pairs.
4. Emit via `_bi_lib` (`save` runs `--quality` automatically).
5. Re-run:  
   `python .grok/skills/sanskrit-verse-blog/scripts/gate_posts.py --quality --dates YYYY-MM-DD`
6. Commit **only** `_posts/…` (plus skill/gate files if changed); push `master`.

## Emitter sketch

```python
from _bi_lib import P, R, G, emit_post

P("a",
  s1="… ।", s2="… ॥१॥",
  en="…",
  cx="why",
  r=[R("lemma", "sense"), …],
  w=[("मञ्चः", "platform (nom. sg.)"), …],  # English not echo
  g=[
    G("मञ्चः", "मञ्च + सु (1/1 nom. sg.)", "subject"),
    G("धत्ते", "धा लट् ātmanepada 3/1", "finite verb"),
    …
  ],
)
```

## Gates (scripts)

| Script | Role |
|--------|------|
| `meter.py` | akṣara count, purity blacklist |
| `grammar.py` | quality heuristics (maps, echo wfw, formulas, calques, imperative stampede) |
| `gate_posts.py` | `--quality` aggregates all; exit 1 on fail |

## References

- `references/meter-and-purity.md`
- `references/grammar-quality.md`

## Gist (private / secret)

https://gist.github.com/VedantMadane/f5f3287392adb0daec8d207f07b8fac8

Update the gist when skill or gates change (`gh gist edit f5f3287392adb0daec8d207f07b8fac8 …`).

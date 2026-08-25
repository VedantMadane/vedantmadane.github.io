---
name: sanskrit-verse-blog
description: >
  Write and gate VedantMadane Sanskrit-verse blog posts (vedantmadane.github.io)
  with pure Pāṇinian Devanāgarī padya, strict chandobaddha (अनुष्टुभ्/उपजाति),
  bilingual collapsible English, and no em/en dashes or Oxford commas.
  Use when the user says go/continue blog, write a śloka post, deepen verses,
  fix panini/chandas, or runs /sanskrit-verse-blog.
---

# Sanskrit verse blog (vedantmadane.github.io)

## Repo and push

- Path: `C:\Users\Administrator\vedantmadane.github.io`
- Default branch: `master`
- Posts: `_posts/YYYY-MM-DD-<Devanāgarī-title>.md`
- Emitter: `_bi_lib.py` (must pass gates before `save`)
- Gate: `python .grok/skills/sanskrit-verse-blog/scripts/gate_posts.py`

## Hard quality bars (non-negotiable)

### 1. Pāṇinian purity (verse body only)

Verse lines inside `sanskrit-verse-lines` must be **pure Devanāgarī padya**:

- No Latin/ASCII letters or digits in verse spans
- No hybrid loans in Devanāgarī (`टोकन्`, `हैश`, `API`, `canary`, `fsync`, …)
- Prefer classical/neologism coinages: **प्रतीकम्** not टोकन्; **लेखनाग्रपङ्क्तिः** not WAL; **द्वारसेवा** not gateway-as-English
- English (gloss, overview, sense, wfw) stays in `<details>` only
- SA intro may use minimal technical Latin only if unavoidable; prefer Devanāgarī

### 2. Chandobaddha

| Meter | Shape | Akṣara budget (gate) |
|-------|--------|----------------------|
| **अनुष्टुभ्** | 2 visual lines = 4×8 pādas | each line **14–18** (target **16**); total **28–36** (target **32**) |
| **उपजाति** | 4 lines | each line **exactly 11** (gate allows 10–12 only as warn; **proper = 11**) |

- Count akṣaras with `scripts/meter.py` (`count_aksharas`)
- Strip `।` `॥` and verse numbers before counting
- Pathyā laghu/guru preferred when writing new padya; gate enforces counts first
- No English-first “verses”, no checklist pādas as meter fillers

### 3. Post shape (Sep 22+ bilingual default)

- 12 verses: chapters 2+2+1+2+2+1+2 (अनुष्टुभ् / उपजाति pattern via `chs` + `pack12`)
- English always in `<details>` with **minimizable** summaries
- No bare `<p class="prose-text"><strong>English.</strong>`
- No U+2014 em dash, no U+2013 en dash
- No Oxford comma in English clauses (`ox()`)
- Unique topic vs prior dates; series `prior` table
- Filename UTF-8 length &lt; 200 bytes

### 4. Style bans

- No topic repetition across dates
- Keep/avoid, glossary, shlist, refs present
- Theme lines under chapters: pure Devanāgarī imperatives preferred (`प्रतीकं योजय` not `टोकन् योजय`)

## Workflow: new post or “go”

1. Tip = day after last `_posts/2026-*.md` date (or user-named range).
2. Pick unique platform/SRE/data topic not already titled.
3. Draft 12 verses in pure SA meeting meter budgets; validate with `meter.assert_anu` / `assert_upa`.
4. Emit via `_bi_lib.emit` / `pack12` (gates run inside `save`/`pack12`).
5. `python .grok/skills/sanskrit-verse-blog/scripts/gate_posts.py --dates YYYY-MM-DD...`
6. Commit only `_posts/…`; push `master`; smoke live URLs after Pages build.

## Workflow: fix panini/chandas debt

1. `python .grok/skills/sanskrit-verse-blog/scripts/gate_posts.py --json` → failing paths.
2. Prefer rewrite of verse spans + pad/wfw tables; keep permalink/title if possible.
3. Re-gate until post has **zero** panini and chandas fails.
4. Do not “fix” by loosening the gate.

## Emitter rules

- `P("a", s1=..., s2=...)` — each of s1/s2 must pass `assert_anu_line`
- `P("u", l=[l1,l2,l3,l4])` — each li must pass `assert_upa_line`
- English sense/ctx may name modern terms; verse lines may not

## References

- `references/meter-and-purity.md` — budgets and loan blacklist
- `scripts/meter.py` — count + assert
- `scripts/gate_posts.py` — corpus gate (exit 1 on fail)

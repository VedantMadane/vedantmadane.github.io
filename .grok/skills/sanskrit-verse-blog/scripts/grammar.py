# -*- coding: utf-8 -*-
"""Pāṇinian-quality heuristics for padya posts (quality gate).

Not a full Aṣṭādhyāyī engine. Catches mass-emit debt, echo glosses,
missing grammar maps, Hindi/English calques, and stock formula seals.
Stop-words (हि तु वै सदा पथि एव अपि नु सम्यक् नित्यम्) are allowed.
"""
from __future__ import annotations
import re
from meter import purity_flags, line_body, count_aksharas

# Particles / meter pads — allowed (user OK)
_STOP = frozenset(
    "हि तु वै स्म ह वै खलु ननु किल अथ अपि एव च वा वा अथवा "
    "सदा नित्यम् पथि पथे सम्यक् नु हि।".split()
)

# Stock mass-emit seals / checklist limbs (quality ban in verse body)
_FORMULA = re.compile(
    r"(तन्त्रधर्मः\s*स\s*उच्यते|कर्मयोग्य[ंः]|क्रियायोग्य[ंं]|पञ्चाङ्गं\s+\S+\s+उच्यते|"
    r"सारं\s+धारय|धर्मं\s+धारय\s*॥|"
    r"मितं\s+\S+\s+क्रियायोग्य)"
)

# Hindi / hybrid / English-calque stems in Devanāgarī (expand over time)
_CALQUE = re.compile(
    r"(ताजता|ताजस्य|पड़ोस|पडोसी|खुला|खुली|शेल्फ|बोरिङ्ग|जोखिम|स्विच|"
    r"बाइट्?|टोकन्|हैश|बैच|कनारी|गेटवे|साइडकार|फ्सिन्क्|"
    r"बाढ़ा|बाढा|"  # prefer बाढा/प्लावन — बाढ़ा is Hindi ढ़
    r"नमुना|वर्जन\s*लिस्ट)"
)

# Bare English-imperative stampede: many 2sg imperatives, no finite past/present
_IMP = re.compile(
    r"\b(कुरु|कुरुतु|योजय|लिख|देहि|गृह्ण|गृहाण|रुन्धि|मापय|तोलय|"
    r"नामय|दर्शय|बध्नीहि|सहस्व|त्यज|उद्धर|पश्य|जान|रक्ष|धारय|वद|छिन्दि)\b"
)

_FINITE = re.compile(
    r"(ति|ते|न्ति|न्ते|सि|से|मि|हे|तु|ताम्|न्तु|"
    r"त्|न्|ः\s|अस्ति|भवति|स्यात्|जायते|नश्यति|पतति|वर्धते|दहति|"
    r"उच्यते|प्रोच्यते|स्मृतः|उक्तम्)\b"
)

# Require these headings inside each verse <details>
_NEED_HEADS = (
    ("grammar_map", re.compile(r"\*\*व्याकरणम्|\*\*Grammar map\*\*|व्याकरणम्\s*/\s*Grammar", re.I)),
    ("english_sense", re.compile(r"\*\*English sense\*\*", re.I)),
    ("padaccheda", re.compile(r"\*\*पदच्छेदः\*\*", re.I)),
    ("wfw", re.compile(r"\*\*Word-for-word\*\*", re.I)),
)


def tokenize_sa(line: str) -> list[str]:
    s = line_body(line)
    s = re.sub(r"[।॥]", " ", s)
    return [t for t in s.split() if t]


def formula_flags(text: str) -> list[str]:
    out = []
    if _FORMULA.search(text):
        out.append("stock_formula_close")
    return out


def calque_flags(text: str) -> list[str]:
    out = []
    if _CALQUE.search(text):
        out.append("hindi_or_calque_stem")
    out.extend(purity_flags(text))
    return list(dict.fromkeys(out))


def imperative_stampede_flags(lines: list[str]) -> list[str]:
    """Flag verses that are only stacked bare imperatives with no finite verb."""
    body = " ".join(line_body(ln) for ln in lines)
    imps = _IMP.findall(body)
    fins = _FINITE.findall(body)
    # allow stop-word pads; if 3+ imperatives and zero finite → checklist padya
    if len(imps) >= 3 and len(fins) == 0:
        return ["imperative_stampede"]
    return []


def parse_md_table(block: str) -> list[tuple[str, ...]]:
    rows = []
    for ln in block.splitlines():
        ln = ln.strip()
        if not ln.startswith("|"):
            continue
        if re.match(r"^\|\s*:?-{2,}", ln):
            continue
        cells = [c.strip() for c in ln.strip("|").split("|")]
        if cells and not cells[0].startswith("---"):
            rows.append(tuple(cells))
    return rows


def wfw_echo_flags(details_html: str) -> list[str]:
    """Fail if word-for-word English mostly repeats the Sanskrit token."""
    m = re.search(
        r"\*\*Word-for-word\*\*\s*(.*?)(?=\*\*[A-Za-zअ-ह]|\Z)",
        details_html,
        re.S | re.I,
    )
    if not m:
        return ["missing_wfw_table"]
    rows = parse_md_table(m.group(1))
    if len(rows) < 3:
        return ["wfw_too_thin"]
    # skip header row if present
    data = rows[1:] if rows and re.search(r"संस्कृत|Word", rows[0][0], re.I) else rows
    if not data:
        return ["wfw_too_thin"]
    echo = 0
    useful = 0
    for r in data:
        if len(r) < 2:
            continue
        a, b = r[0].strip(), r[1].strip()
        if not a or a in _STOP:
            continue
        useful += 1
        # echo if identical or English cell is still pure Devanagari same token
        if a == b or (re.fullmatch(r"[\u0900-\u097F\s]+", b) and a.replace("ः", "") == b.replace("ः", "")):
            echo += 1
    if useful and echo / useful >= 0.6:
        return ["wfw_echo_sanskrit"]
    return []


def grammar_map_flags(details_html: str) -> list[str]:
    if not _NEED_HEADS[0][1].search(details_html):
        return ["missing_grammar_map"]
    m = re.search(
        r"(?:\*\*व्याकरणम्[^*]*\*\*|\*\*Grammar map\*\*)\s*(.*?)(?=\*\*[A-Za-zअ-ह]|\Z)",
        details_html,
        re.S | re.I,
    )
    if not m:
        return ["missing_grammar_map_body"]
    rows = parse_md_table(m.group(1))
    data = rows[1:] if rows and len(rows[0]) >= 2 else rows
    if len(data) < 3:
        return ["grammar_map_too_thin"]
    # expect analysis column with case/lakāra-ish hints
    weak = 0
    for r in data:
        if len(r) < 2:
            weak += 1
            continue
        analysis = r[1]
        if len(analysis) < 4:
            weak += 1
            continue
        if not re.search(
            r"([1-8]/[1-3]|प्रथमा|द्वितीया|तृतीया|चतुर्थी|पञ्चमी|षष्ठी|सप्तमी|"
            r"लट्|लोट्|लङ्|विधिलिङ्|क्त|क्तवतु|तुमुन्|ल्यप्|क्त्वा|ण्वुल्|तृच्|"
            r"1sg|2sg|3sg|1pl|2pl|3pl|nom|acc|ins|dat|abl|gen|loc|voc|"
            r"compound|समास|imp|inj|opt|pass|caus|des)",
            analysis,
            re.I,
        ):
            weak += 1
    if data and weak / len(data) > 0.5:
        return ["grammar_map_unanalyzed"]
    return []


def details_structure_flags(details_html: str) -> list[str]:
    out = []
    for name, rx in _NEED_HEADS:
        if not rx.search(details_html):
            out.append(f"missing_{name}")
    out.extend(wfw_echo_flags(details_html))
    out.extend(grammar_map_flags(details_html))
    return list(dict.fromkeys(out))


def verse_quality_flags(meter: str, lines: list[str], details_html: str = "") -> list[str]:
    """Aggregate quality flags for one verse."""
    flags: list[str] = []
    body = "\n".join(lines)
    flags.extend(calque_flags(body))
    flags.extend(formula_flags(body))
    flags.extend(imperative_stampede_flags(lines))
    # very short content words only
    toks = []
    for ln in lines:
        toks.extend(tokenize_sa(ln))
    content = [t for t in toks if t not in _STOP and not re.fullmatch(r"[।॥०-९0-9]+", t)]
    if len(content) < 4:
        flags.append("verse_too_thin")
    if details_html:
        flags.extend(details_structure_flags(details_html))
    return list(dict.fromkeys(flags))


def extract_verse_blocks(text: str) -> list[dict]:
    """Split post into verse + following details pairs."""
    blocks = []
    parts = re.split(r'(<p class="verse-topic">)', text)
    # parts[0] preamble; then pairs (marker, rest)
    i = 1
    while i < len(parts) - 1:
        chunk = parts[i] + parts[i + 1]
        i += 2
        head = chunk.split("</p>", 1)[0]
        meter = "?"
        if "अनुष्टुभ्" in head:
            meter = "अनुष्टुभ्"
        elif "उपजाति" in head:
            meter = "उपजाति"
        mspan = re.search(
            r'<div class="sanskrit-text[^"]*"[^>]*>(.*?)</div>', chunk, re.S
        )
        if not mspan:
            continue
        lines = re.findall(r"<span[^>]*>([^<]+)</span>", mspan.group(1))
        lines = [re.sub(r"\s+", " ", ln).strip() for ln in lines if ln.strip()]
        det = ""
        md = re.search(r"<details>(.*?)</details>", chunk, re.S)
        if md:
            det = md.group(1)
        blocks.append({"meter": meter, "lines": lines, "details": det, "head": head})
    return blocks

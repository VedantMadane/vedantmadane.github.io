# Jekyll post from Sanskritizing Software Concepts_ A Plan.md
from __future__ import annotations

import re
from pathlib import Path

SRC = Path(r"C:\Projects\shatakam\Sanskritizing Software Concepts_ A Plan.md")
OUT = Path(
    r"c:\Projects\open-source\VedantMadane.github.io\_posts/"
    "2026-05-05-आधुनिकगणतान्त्रिकवैज्ञानिकपरिदृश्याणां-संस्कृतपद्ये-निबन्धनम्.md"
)
STEM = "आधुनिकगणतान्त्रिकवैज्ञानिकपरिदृश्याणां-संस्कृतपद्ये-निबन्धनम्"
DATE = "2026-05-05"

VERSE_METERS: dict[int, str] = {1: "उपजाति"}
for n in range(2, 16):
    VERSE_METERS[n] = "अनुष्टुभ्"

# (source ### ** line stem), (skill ## line without meter), meter summary
CHAPTERS: list[tuple[str, str, str]] = [
    (
        "प्रथमप्रकरणम्: Computational Environments (तन्त्रसंस्कारः)",
        "प्रथमप्रकरणम् (Computational environments – तन्त्रसंस्कारः)",
        "उपजाति · अनुष्टुभ्",
    ),
    (
        "द्वितीयप्रकरणम्: यन्त्रशिक्षणम् (Machine Learning)",
        "द्वितीयप्रकरणम् (यन्त्रशिक्षणम् – machine learning)",
        "अनुष्टुभ्",
    ),
    (
        "तृतीयप्रकरणम्: साङ्ख्यिकविज्ञानम् (Statistics & Forecasting)",
        "तृतीयप्रकरणम् (साङ्ख्यिकविज्ञानम् – statistics and forecasting)",
        "अनुष्टुभ्",
    ),
    (
        "चतुर्थप्रकरणम्: अणुसङ्गणनम् (Quantum Computing)",
        "चतुर्थप्रकरणम् (अणुसङ्गणनम् – quantum computing)",
        "अनुष्टुभ्",
    ),
    (
        "पञ्चमप्रकरणम्: जीवसूचनाशास्त्रम् (Bioinformatics)",
        "पञ्चमप्रकरणम् (जीवसूचनाशास्त्रम् – bioinformatics)",
        "अनुष्टुभ्",
    ),
]

DEVA_RE = re.compile(r"[\u0900-\u097F]")


def escape_html(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def normalize_dashes(s: str) -> str:
    return s.replace("\u2014", "\u2013")


def parse_verses(text: str) -> list[tuple[int, list[str], str, str]]:
    starts = [m.start() for m in re.finditer(r"\*\*Verse \d+:", text)]
    out: list[tuple[int, list[str], str, str]] = []
    for i, st in enumerate(starts):
        end = starts[i + 1] if i + 1 < len(starts) else len(text)
        block = text[st:end]
        mh = re.match(r"\*\*Verse (\d+):([^*]+)\*\*", block)
        if not mh:
            continue
        n = int(mh.group(1))
        rest = block[mh.end() :]
        iw = rest.find("**Word-for-Word Translation:**")
        ig = rest.find("**Grammatical Derivation and Metrical Note:**")
        if iw == -1 or ig == -1:
            continue
        pre = rest[:iw]
        word = rest[iw + len("**Word-for-Word Translation:**") : ig].strip()
        gram = rest[ig + len("**Grammatical Derivation and Metrical Note:**") :].strip()
        # Source places the next ### chapter before the following **Verse** marker.
        if (gx := re.search(r"\n### \*\*", gram)) is not None:
            gram = gram[: gx.start()].strip()
        sans: list[str] = []
        for ln in pre.splitlines():
            t = ln.strip()
            if not t or t.startswith("Meter:"):
                continue
            if DEVA_RE.search(t):
                sans.append(t)
        out.append((n, sans, word, gram))
    return out


def html_verse(lines: list[str], vid: int, meter: str) -> str:
    parts = [
        f'\n<p class="verse-topic">श्लोकः {vid} ({meter})</p>\n',
        f'<div class="sanskrit-text sanskrit-verse-lines" data-verse-id="v{vid}">\n',
    ]
    for i, ln in enumerate(lines, 1):
        parts.append(
            f'  <span data-line="{i}" data-start="" data-end="">{escape_html(ln)}</span><br />\n'
        )
    parts.append("</div>\n")
    return "".join(parts)


def chapter_for_verse(v: int) -> int:
    if v <= 3:
        return 1
    if v <= 7:
        return 2
    if v <= 10:
        return 3
    if v <= 13:
        return 4
    return 5


def extract_between(full: str, a: str, b: str) -> str:
    ia = full.find(a)
    if ia == -1:
        return ""
    ib = full.find(b, ia + len(a))
    if ib == -1:
        return full[ia:].strip()
    return full[ia:ib].strip()


def main() -> None:
    raw = normalize_dashes(SRC.read_text(encoding="utf-8"))
    title_en = "Codification of Modern Computational and Scientific Paradigms into Sanskrit Verse"
    if m := re.search(r"^# \*\*(.+?)\*\*\s*$", raw, re.M):
        title_en = m.group(1).strip()

    conceptual = extract_between(
        raw,
        "## **Conceptual Mapping and Strategic Nomenclature**",
        "## **Estimation of Chapters and Verse Requirements**",
    )
    estimation = extract_between(
        raw,
        "## **Estimation of Chapters and Verse Requirements**",
        "## **Execution of the Codification Plan**",
    )

    second_start = raw.find("## **Second-Order Morphological")
    synth_start = raw.find("## **Synthesis and Final Implications**")
    works_start = raw.find("#### **Works cited**")

    second_order = raw[second_start:synth_start].strip() if second_start != -1 and synth_start != -1 else ""
    synthesis = raw[synth_start:works_start].strip() if synth_start != -1 and works_start != -1 else ""
    works = raw[works_start:].strip() if works_start != -1 else ""
    works = works.replace("#### **Works cited**", "#### Works cited")

    # Split चतुर्थ: intro + optional table before Verse 11
    ch4_marker = "### **चतुर्थप्रकरणम्: अणुसङ्गणनम् (Quantum Computing)**"
    v11_marker = "**Verse 11:"
    ch4_full = extract_between(raw, ch4_marker, v11_marker)
    ch4_intro_only = ch4_full
    ch4_table_md = ""
    if "**Table 1:" in ch4_full:
        pre, _, post = ch4_full.partition("**Table 1:")
        ch4_intro_only = re.sub(
            r"^### \*\*[^\n]+\*\*\s*\n+",
            "",
            pre.strip(),
            count=1,
        ).strip()
        tbl, _, _ = post.partition("**Verse")
        ch4_table_md = ("**Table 1:" + tbl).strip()

    verses = parse_verses(raw)
    assert len(verses) == 15, verses

    # Remove ### sections from body_exec for manual rebuild — use parsed verses only
    # Chapter English intros: text after ### line until **Verse n**
    first_verse_of_ch = {1: 1, 2: 4, 3: 8, 4: 11, 5: 14}
    ch_intros: dict[int, str] = {}
    for cv in range(1, 6):
        full_h = CHAPTERS[cv - 1][0]
        fv = first_verse_of_ch[cv]
        msec = re.search(
            rf"^### \*\*{re.escape(full_h)}\*\*\s*\n(.*?)(?=\*\*Verse {fv}:)",
            raw,
            re.MULTILINE | re.DOTALL,
        )
        if msec:
            chunk = msec.group(1).strip()
            if cv == 4:
                chunk = ch4_intro_only
            ch_intros[cv] = chunk

    body: list[str] = []
    current_ch = 0
    for vnum, slines, word, gram in verses:
        ch = chapter_for_verse(vnum)
        if ch != current_ch:
            current_ch = ch
            ch_display, ch_meter = CHAPTERS[ch - 1][1], CHAPTERS[ch - 1][2]
            body.append(f"\n## {ch_display} – {ch_meter}\n")
            intro = ch_intros.get(ch, "")
            if intro:
                body.append(
                    '\n<div class="prose-text" markdown="1">\n\n' + intro + "\n\n</div>\n"
                )
            if ch == 4 and ch4_table_md:
                body.append(
                    "\n<details><summary>Table 1: Quantum Computational Terminology Derivations</summary>\n"
                    '<div class="prose-text" markdown="1">\n\n'
                    + ch4_table_md
                    + "\n\n</div>\n</details>\n"
                )

        meter = VERSE_METERS[vnum]
        body.append(html_verse(slines, vnum, meter))
        body.append(
            "\n<details><summary>शब्दार्थाः</summary>\n"
            '<div class="prose-text" markdown="1">\n\n'
            + word
            + "\n\n</div>\n</details>\n"
        )
        body.append(
            "\n<details><summary>व्युत्पत्तिः · छन्दः · टिप्पणी</summary>\n"
            '<div class="prose-text" markdown="1">\n\n'
            + gram
            + "\n\n</div>\n</details>\n"
        )

    intro_html = f"""---
layout: post
title: "{STEM}"
subtitle: "Fifteen ślokas in उपजाति and अनुष्टुभ् – software environments through bioinformatics with collapsible English essays and tables."
permalink: "/{DATE}-{STEM}/"
slug: "{STEM}"
tags: [sanskrit, machine-learning, computational-linguistics, quantum-computing, bioinformatics, software]
audio_sync: false
# audio_file: /assets/audio/FILENAME.mp3
---

<link rel="stylesheet" href="{{{{ '/assets/css/reader.css' | relative_url }}}}">

<div class="reader-container audio-sync-root">

{{% if page.audio_sync %}}
<div class="audio-panel">
  <audio controls preload="metadata" data-audio-sync-player>
    <source src="{{{{ page.audio_file | relative_url }}}}" type="audio/mpeg">
    Your browser does not support the audio element.
  </audio>
</div>
{{% endif %}}

<p class="prose-text">This edition presents fifteen metrical verses mapping computational environments, machine learning, statistics, quantum computing and bioinformatics into Sanskrit technical nomenclature. The first chapter uses उपजाति, then अनुष्टुभ्; verses two through fifteen are अनुष्टुभ्. English sections on strategy, morphology and citations are folded open below.</p>

<!-- Audio sync note: each verse block carries a stable data-verse-id for future timed highlighting. -->

<details>
<summary>पूर्ण-शीर्षकम् (अङ्ग्रेजी)</summary>
<div class="prose-text" markdown="1">

# **{title_en}**

</div>
</details>

<details>
<summary>विषय-योजना · अङ्ग्रेजी</summary>
<div class="prose-text" markdown="1">

{conceptual}

{estimation}

</div>
</details>

"""

    tail_sections = ""
    if second_order:
        tail_sections += (
            "\n<details><summary>द्वितीय-कोटि-संश्लेषः (अङ्ग्रेजी) · कारक-आलेखनम् · सन्धि-व्ययम् · अन्तराशास्त्र-पेटिका</summary>\n"
            '<div class="prose-text" markdown="1">\n\n'
            + second_order.replace("#### **Works cited**", "#### Works cited")
            + "\n\n</div>\n</details>\n"
        )
    if synthesis:
        tail_sections += (
            "\n<details><summary>सङ्क्षेपः · निष्कर्षाः (अङ्ग्रेजी)</summary>\n"
            '<div class="prose-text" markdown="1">\n\n'
            + synthesis
            + "\n\n</div>\n</details>\n"
        )
    if works:
        tail_sections += (
            "\n<details><summary>Works cited</summary>\n"
            '<div class="prose-text" markdown="1">\n\n'
            + works
            + "\n\n</div>\n</details>\n"
        )

    footer = """
</div>

<script src="{{{{ '/assets/js/audio-sync.js' | relative_url }}}}"></script>
"""

    full = intro_html + "".join(body) + tail_sections + footer
    full = normalize_dashes(full)
    OUT.write_text(full, encoding="utf-8")
    print("Wrote post OK, verses=", len(verses))


if __name__ == "__main__":
    main()

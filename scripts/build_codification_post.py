# Build Jekyll post from Sanskritist's Verse Codification Plan.md
from __future__ import annotations

import re
from pathlib import Path

SRC = Path(r"C:/Projects/shatakam/Sanskritist's Verse Codification Plan.md")
OUT = Path(
    r"c:/Projects/open-source/VedantMadane.github.io/_posts/"
    "2026-05-04-कृत्रिममेधायन्त्रशिक्षणदत्तांशविज्ञानानां-तान्त्रिकतत्त्वानां-पाणिनीयदृष्ट्या-पद्यबद्धः-सङ्ग्रहः.md"
)

STEM = "कृत्रिममेधायन्त्रशिक्षणदत्तांशविज्ञानानां-तान्त्रिकतत्त्वानां-पाणिनीयदृष्ट्या-पद्यबद्धः-सङ्ग्रहः"
DATE = "2026-05-04"

VERSE_END = re.compile(r"॥\s*[०-९]+\s*॥\s*$")
# Last sentence of each chapter intro names the meter; verses begin the next line.
INTRO_END_RE = re.compile(
    r"छन्दसि.*(ग्रथ्नाति|वर्ण्यन्ते|वर्ण्यते|प्रतिपादयति|स्तौति|निरूप्यते)\s*।"
)

CH_META: list[tuple[str, str]] = [
    ("अनुष्टुभ्", "Big data, lifecycle and Hadoop / Spark"),
    ("उपजाति", "Knowledge discovery (KDD) pipeline"),
    ("वसन्ततिलका", "Clustering: K-Means, DBSCAN, hierarchical"),
    ("शार्दूलविक्रीडितम्", "Ensemble learning: bagging, boosting, stacking"),
    ("शिखरिणी · अनुष्टुभ्", "Feature selection and cross-validation"),
    ("मन्दाक्रान्ता", "Bayesian inference and MCMC"),
    ("मालिनी", "Knowledge graphs, RDF and property graphs"),
    ("वसन्ततिलका", "Data visualization"),
]


def escape_html(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def verse_label_meter(meter_field: str) -> str:
    parts = [p.strip() for p in meter_field.split("·")]
    return parts[-1] if parts else meter_field


def extract_verse_blocks_before_padaccheda(chunk: str) -> tuple[str, list[str], str]:
    """Return preamble, verse_blocks, tail (from **पदच्छेदः** onward including tables)."""
    idx = chunk.find("**पदच्छेदः**")
    head = chunk[:idx] if idx != -1 else chunk
    tail = chunk[idx:] if idx != -1 else ""

    lines = head.splitlines()
    # stop head at first markdown table row
    cut = len(lines)
    for i, ln in enumerate(lines):
        st = ln.strip()
        if st.startswith("|") and st.count("|") >= 2:
            cut = i
            break
    head_lines = lines[:cut]

    end_idxs = [i for i, ln in enumerate(head_lines) if VERSE_END.search(ln.strip())]
    if not end_idxs:
        return "\n".join(head_lines).strip(), [], tail

    verse_floor = 0
    for i, ln in enumerate(head_lines):
        if INTRO_END_RE.search(ln):
            verse_floor = i + 1
            break

    blocks: list[str] = []
    cursor = verse_floor
    first_start: int | None = None
    for e in end_idxs:
        if e < cursor:
            continue
        s = e
        while (
            s > cursor
            and head_lines[s - 1].strip() != ""
            and not VERSE_END.search(head_lines[s - 1].strip())
        ):
            s -= 1
        if first_start is None:
            first_start = s
        blocks.append("\n".join(head_lines[s : e + 1]).strip())
        cursor = e + 1

    preamble = "\n".join(head_lines[:first_start]).strip() if first_start is not None else ""

    return preamble, blocks, tail


def html_for_verse(block: str, vid: int, meter_field: str) -> str:
    ls = [ln.strip() for ln in block.splitlines() if ln.strip()]
    label = verse_label_meter(meter_field)
    parts = [
        f'\n<p class="verse-topic">श्लोकः {vid} ({label})</p>\n',
        f'<div class="sanskrit-text sanskrit-verse-lines" data-verse-id="v{vid}">\n',
    ]
    for i, line in enumerate(ls, 1):
        parts.append(
            f'  <span data-line="{i}" data-start="" data-end="">{escape_html(line)}</span><br />\n'
        )
    parts.append("</div>\n")
    return "".join(parts)


def main() -> None:
    text = SRC.read_text(encoding="utf-8")

    title_line = re.search(r"^# \*\*(.+?)\*\*\s*$", text, re.M)
    full_title = title_line.group(1).strip() if title_line else STEM.replace("-", " ")

    intro_start = text.find("## **विषय-योजना-प्रारूपम्**")
    intro_end = text.find("## **प्रथमाध्यायः", intro_start)
    intro_md = text[intro_start:intro_end].strip()
    intro_md = intro_md.replace("## **विषय-योजना-प्रारूपम्**", "### विषय-योजना-प्रारूपम्")
    intro_md = re.sub(r"\\-", "–", intro_md)

    chapters = [
        m
        for m in re.finditer(r"^## \*\*(.+?)\*\*\s*$", text, re.M)
        if not m.group(1).strip().startswith("विषय-योजना")
        and not m.group(1).strip().startswith("उपसंहार")
    ]

    body: list[str] = []
    v_global = 0

    for i, ch in enumerate(chapters):
        title_raw = ch.group(1).strip().replace(r"\-", "–")
        start = ch.end()
        end = chapters[i + 1].start() if i + 1 < len(chapters) else text.find("## **उपसंहारः**", start)
        if end == -1:
            end = len(text)
        chunk = text[start:end]

        meter_field, en_gloss = CH_META[i] if i < len(CH_META) else ("मिश्रम्", "")
        body.append(f"\n## {title_raw} ({en_gloss}) – {meter_field}\n")

        preamble, vblocks, tail = extract_verse_blocks_before_padaccheda(chunk)
        if preamble:
            body.append(f'\n<div class="prose-text" markdown="1">\n\n{preamble}\n\n</div>\n')

        for vb in vblocks:
            v_global += 1
            body.append(html_for_verse(vb, v_global, meter_field))

        tail = tail.strip()
        if tail:
            tail = tail.replace("#### **Works cited**", "#### Works cited")
            body.append(
                "\n<details><summary>पदच्छेदः · अन्वयः · धातुपाठ-व्याकरणम् · दार्शनिक-तान्त्रिक-विमर्शः · सारण्याः</summary>\n"
                '<div class="prose-text" markdown="1">\n\n'
                + tail
                + "\n\n</div>\n</details>\n"
            )

    up_idx = text.find("## **उपसंहारः**")
    if up_idx != -1:
        tail_doc = text[up_idx:].strip()
        tail_doc = re.sub(r"^## \*\*उपसंहारः\*\*", "## उपसंहारः", tail_doc, flags=re.M)
        tail_doc = tail_doc.replace("#### **Works cited**", "#### Works cited")
        body.append(
            "\n<details><summary>उपसंहारः · Works cited</summary>\n"
            '<div class="prose-text" markdown="1">\n\n'
            + tail_doc
            + "\n\n</div>\n</details>\n"
        )

    intro_html = f"""---
layout: post
title: "{STEM}"
subtitle: "Thirty-three verses in अनुष्टुभ्, उपजाति, वसन्ततिलका, शार्दूलविक्रीडित, शिखरिणी, मन्दाक्रान्ता, मालिनी and mixed meters – Pāṇinian codification of big data, ML, ensembles, Bayes and knowledge graphs."
permalink: "/{DATE}-{STEM}/"
slug: "{STEM}"
tags: [sanskrit, machine-learning, big-data, philology, panini, knowledge-graphs]
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

<p class="prose-text">This edition presents the full verse codification plan for artificial intelligence, machine training and big-data science under Pāṇinian grammar: eight adhyāyas, thirty-three metrical ślokas, chapter tables, pada splits, anvaya, dhātupāṭha notes and Naiyāyika–Vaiśeṣika comparisons. Technical Anglicisms stay in parentheses where the source uses them.</p>

<!-- Audio sync note: each verse block carries a stable data-verse-id for future timed highlighting. -->

<details>
<summary>पूर्ण-शीर्षकम्</summary>
<div class="prose-text" markdown="1">

# **{full_title}**

</div>
</details>

<details>
<summary>विषय-योजना</summary>
<div class="prose-text" markdown="1">

{intro_md}

</div>
</details>

"""

    footer_html = """
</div>

<script src="{{{{ '/assets/js/audio-sync.js' | relative_url }}}}"></script>
"""

    full = intro_html + "".join(body) + footer_html
    full = full.replace("\u2014", "\u2013")  # em dash → en dash (gh-blogpost)
    OUT.write_text(full, encoding="utf-8")
    print("Wrote", OUT)
    print("Verses:", v_global)


if __name__ == "__main__":
    main()

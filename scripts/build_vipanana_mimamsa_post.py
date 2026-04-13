# Build Jekyll post from vipanana-anusandhana-mimamsa (shatakam).
from __future__ import annotations

import re
from pathlib import Path

BLOG = Path(r"c:\Projects\open-source\VedantMadane.github.io")
SRC = next(Path(r"C:\Projects\shatakam").glob("*मीमांसा.md"))
DATE = "2026-05-07"
METER = "अनुष्टुभ्"


def escape_html(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def normalize_dashes(s: str) -> str:
    return s.replace("\u2014", "\u2013")


def html_verse(line1: str, line2: str, vid: int) -> str:
    return (
        f'\n<p class="verse-topic">श्लोकः {vid} ({METER})</p>\n'
        f'<div class="sanskrit-text sanskrit-verse-lines" data-verse-id="v{vid}">\n'
        f'  <span data-line="1" data-start="" data-end="">'
        f"{escape_html(line1.strip())}</span><br />\n"
        f'  <span data-line="2" data-start="" data-end="">'
        f"{escape_html(line2.strip())}</span><br />\n"
        "</div>\n"
    )


def extract_table_commentary(after_verse: str) -> tuple[str, str]:
    lines = after_verse.strip().splitlines()
    if not lines or not lines[0].strip().startswith("| पदम् |"):
        return "", after_verse.strip()
    i = 0
    rows: list[str] = []
    while i < len(lines) and lines[i].strip().startswith("|"):
        rows.append(lines[i])
        i += 1
    table = "\n".join(rows).strip()
    commentary = "\n".join(lines[i:]).strip()
    return table, commentary


def parse_section_body(body: str) -> tuple[str, tuple[str, str] | None, str, str]:
    m = re.search(
        r"((?:[\u0900-\u097F]|\s)+[^\n]*।)\s*\n"
        r"((?:[\u0900-\u097F]|\s)+[^\n]*॥)\s*",
        body,
    )
    if not m:
        return body.strip(), None, "", ""
    l1, l2 = m.group(1), m.group(2)
    pre, _, after = body.partition(m.group(0))
    table, commentary = extract_table_commentary(after)
    return pre.strip(), (l1, l2), table, commentary


def section_heading_line(header_line: str) -> str:
    m = re.match(r"## \*\*(\\?\d+)\\?\. (.+?)\*\*\s*$", header_line.strip())
    if not m:
        return header_line.strip()
    return f"## {m.group(2)} – {METER}"


def clean_summary_from_header(header_line: str) -> str:
    m = re.match(r"## \*\*(\\?\d+)\\?\. (.+?)\*\*\s*$", header_line.strip())
    if m:
        return f"{m.group(1)}. {m.group(2)}"
    return re.sub(r"^\#\# \*\*|\*\*$", "", header_line).replace("\\", "")


def main() -> None:
    raw_full = normalize_dashes(SRC.read_text(encoding="utf-8"))
    stem_m = re.match(r"^# \*\*(.+?)\s*:", raw_full, re.M)
    if not stem_m:
        raise ValueError("expected H1 Devanagari title before colon")
    STEM = stem_m.group(1).strip()
    OUT = BLOG / "_posts" / f"{DATE}-{STEM}.md"
    if "#### **Works cited**" in raw_full:
        raw, _, works_body = raw_full.rpartition("#### **Works cited**")
        works = works_body.strip()
        raw = raw.rstrip()
    else:
        raw = raw_full
        works = ""

    title_full = STEM
    title_en = "An Exhaustive Report on Marketing Research Methodology"
    if m := re.search(r"^# \*\*(.+?)\s*:\s*(.+?)\*\*\s*$", raw, re.M):
        title_en = m.group(2).strip()

    chunks = re.split(r"(?=^## \*\*)", raw, flags=re.MULTILINE)
    body: list[str] = []
    vnum = 0

    for ch in chunks[1:]:
        lines = ch.splitlines()
        if not lines:
            continue
        head = lines[0]
        rest = "\n".join(lines[1:]).strip()
        pre, verse, table, commentary = parse_section_body(rest)
        if verse is None:
            body.append(
                "\n<details><summary>"
                + escape_html(clean_summary_from_header(head))
                + "</summary>\n"
                '<div class="prose-text" markdown="1">\n\n'
                + pre
                + "\n\n</div>\n</details>\n"
            )
            continue

        vnum += 1
        body.append("\n" + section_heading_line(head) + "\n")
        if pre:
            body.append(
                '\n<div class="prose-text" markdown="1">\n\n' + pre + "\n\n</div>\n"
            )
        body.append(html_verse(verse[0], verse[1], vnum))
        if table:
            body.append(
                "\n<details><summary>शब्दार्थाः</summary>\n"
                '<div class="prose-text" markdown="1">\n\n'
                + table
                + "\n\n</div>\n</details>\n"
            )
        if commentary:
            body.append(
                "\n<details><summary>व्युत्पत्तयः</summary>\n"
                '<div class="prose-text" markdown="1">\n\n'
                + commentary
                + "\n\n</div>\n</details>\n"
            )

    assert vnum == 18, f"expected 18 verses, got {vnum}"

    if works:
        body.append(
            "\n<details><summary>Works cited</summary>\n"
            '<div class="prose-text" markdown="1">\n\n'
            + works
            + "\n\n</div>\n</details>\n"
        )

    subtitle = (
        "Eighteen अनुष्टुभ् verses on marketing-research methodology \u2013 problem definition, design, data, scales, sampling, field work, analysis and ethics with P\u0101\u1e47inian glosses."
    )
    intro_html = f"""---
layout: post
title: "{STEM}"
subtitle: "{subtitle}"
permalink: "/{DATE}-{STEM}/"
slug: "{STEM}"
tags: [sanskrit, marketing-research, methodology, panini, anustubh]
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

<p class="prose-text">This edition presents eighteen अनुष्टुभ् ślokas on {STEM} (marketing research), each with a पदम्–अर्थः table and a collapsible English gloss on word formation. Section 1 states the ontological framework in a collapsible; references close the post.</p>

<!-- Audio sync note: each verse block carries a stable data-verse-id for future timed highlighting. -->

<details>
<summary>पूर्ण-शीर्षकम्</summary>
<div class="prose-text" markdown="1">

# **{title_full} : {title_en}**

</div>
</details>

"""

    footer = """
</div>

<script src="{{ '/assets/js/audio-sync.js' | relative_url }}"></script>
"""

    full = intro_html + "".join(body) + footer

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(full, encoding="utf-8")
    print("OK", vnum, "verses ->", OUT)


if __name__ == "__main__":
    main()

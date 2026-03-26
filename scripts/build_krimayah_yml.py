"""Build _data/krimayah.yml from krimayah.txt + krimayah-en.txt (C:\\Projects\\shatakam)."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC_SA = Path(r"C:\Projects\shatakam\krimayah.txt")
SRC_EN = Path(r"C:\Projects\shatakam\krimayah-en.txt")
OUT_YML = ROOT / "_data" / "krimayah.yml"


def skip_sa_line(s: str) -> bool:
    t = s.strip()
    if not t:
        return True
    if t.startswith("*") or t.startswith("This refers"):
        return True
    if "Actually I need" in t or "Let's use" in t or "Let's redo" in t:
        return True
    if re.match(r"^सुसङ्ग्रहीतृभेदेन त्रिधा लोको विभज्यते ।$", t):
        # Draft duplicate before real SIR verse
        return True
    return False


def extract_sanskrit_verses(path: Path) -> list[dict]:
    lines = path.read_text(encoding="utf-8").splitlines()
    verses: list[dict] = []
    buf: list[str] = []
    current_speaker: str | None = None

    def flush() -> None:
        nonlocal buf, current_speaker
        if not buf:
            return
        text = "\n".join(buf).strip()
        buf = []
        if not text or "सम्पूर्णम्" in text and "इति श्री" in text:
            return
        # Strip trailing meter tag on last line e.g. (अनुष्टुप्)
        meter_sa = None
        parts = text.rsplit("\n", 1)
        if len(parts) == 2:
            last = parts[1]
            m = re.search(r"\(([^)]+)\)\s*$", last)
            if m:
                meter_sa = m.group(1).strip()
                last_clean = re.sub(r"\s*\([^)]+\)\s*$", "", last).rstrip()
                text = parts[0] + "\n" + last_clean if parts[0] else last_clean
        vid = len(verses) + 1
        verses.append(
            {
                "id": vid,
                "speaker": current_speaker,
                "meter_sa": meter_sa,
                "text": text.strip(),
            }
        )
        current_speaker = None

    for line in lines:
        if skip_sa_line(line):
            continue
        t = line.strip()
        if t == "प्रस्तावना (Introduction)":
            continue
        if re.match(r"^[१२३४५]\.\s+", t) and "।" not in t and "॥" not in t:
            flush()
            continue
        if t in ("युधिष्ठिर उवाच", "मार्कण्डेय उवाच"):
            flush()
            current_speaker = t
            continue
        if "इति श्रीमहाभारते" in t:
            flush()
            break
        buf.append(line.rstrip())
        if re.search(r"॥\s*[०१२३४५६७८९]+\s*॥", line):
            flush()

    flush()
    return verses


def parse_english(path: Path) -> tuple[str | None, list[dict], str | None, str | None]:
    text = path.read_text(encoding="utf-8")
    intro_en: str | None = None
    closing_en: str | None = None
    colophon_sa: str | None = None

    m_intro = re.search(
        r"प्रस्तावना \(Introduction\)\s*\n+(.*?)(?=^Verse\s+1\b)",
        text,
        re.MULTILINE | re.DOTALL,
    )
    if m_intro:
        intro_en = m_intro.group(1).strip()
        if not intro_en:
            intro_en = None

    # Closing after verse 27
    m_close = re.search(
        r"(इति श्रीमहाभारते[^\n]+॥)\s*\n\s*\n(Thus ends[^\n]+)",
        text,
        re.DOTALL,
    )
    if m_close:
        colophon_sa = m_close.group(1).strip()
        closing_en = " ".join(m_close.group(2).split())

    verse_blocks = list(
        re.finditer(
            r"Verse (\d+)(?:\s*[–-]\s*([^\n]+))?\s*\n"
            r"Meter:\s*([^\n]+)\s*\n\s*\n"
            r"Padachheda:\s*\n(.*?)\s*\n\s*\nTranslation:\s*\n(.*?)(?=\n\nVerse |\n[१२३४५]\. |\nइति श्री|\Z)",
            text,
            re.DOTALL,
        )
    )

    parsed: list[dict] = []
    for m in verse_blocks:
        vid = int(m.group(1))
        speaker = (m.group(2) or "").strip() or None
        meter_en = m.group(3).strip()
        pada = m.group(4).strip()
        trans = m.group(5).strip()
        parsed.append(
            {
                "id": vid,
                "speaker_en": speaker,
                "meter_en": meter_en,
                "padachheda": pada,
                "translation": trans,
            }
        )

    return intro_en, parsed, colophon_sa, closing_en


SECTION_HEADERS_SA = [
    (3, "१. महामारीगणितम्", "Epidemiology – The Mathematics of Spread"),
    (8, "२. अन्तःशरीरगतिः", "Immunology – Within‑Host Dynamics"),
    (12, "३. विकासगणितम्", "Evolutionary Biology – The Mathematics of Adaptation"),
    (16, "४. अण्वन्तःक्रिया", "Molecular Biophysics – The Mathematics of Molecular Interaction"),
    (20, "५. गूढसम्बन्धः", 'A Deeper Conceptual Link: “Germ” as a Mathematical Object'),
]


def build_sections(verses_merged: list[dict]) -> list[dict]:
    """Group verses into preamble + numbered chapters + epilogue."""
    by_id = {v["id"]: v for v in verses_merged}
    sections: list[dict] = []

    # Preamble: 1–2
    sections.append(
        {
            "slug": "prastavana",
            "title_sa": "प्रस्तावना",
            "title_en": "Introduction",
            "verses": [by_id[i] for i in (1, 2)],
        }
    )

    cuts = [(a, ta, te) for a, ta, te in SECTION_HEADERS_SA]
    for idx, (start_id, tsa, ten) in enumerate(cuts):
        end_id = cuts[idx + 1][0] - 1 if idx + 1 < len(cuts) else 25
        ids = list(range(start_id, end_id + 1))
        sections.append(
            {
                "slug": f"adhyaya-{idx + 1}",
                "title_sa": tsa,
                "title_en": ten,
                "verses": [by_id[i] for i in ids],
            }
        )

    # Epilogue 26–27
    sections.append(
        {
            "slug": "upasamhara",
            "title_sa": "उपसंहारः",
            "title_en": "Closing",
            "verses": [by_id[i] for i in (26, 27)],
        }
    )

    return sections


def main() -> int:
    if not SRC_SA.is_file() or not SRC_EN.is_file():
        print("Missing:", SRC_SA, "or", SRC_EN, file=sys.stderr)
        return 1

    sa_list = extract_sanskrit_verses(SRC_SA)
    intro_en, en_list, colophon_sa, closing_en = parse_english(SRC_EN)

    if len(sa_list) != len(en_list):
        print(
            f"Verse count mismatch: Sanskrit {len(sa_list)} vs English {len(en_list)}",
            file=sys.stderr,
        )
        return 1

    merged: list[dict] = []
    for sa, en in zip(sa_list, en_list, strict=True):
        if sa["id"] != en["id"]:
            print(f"ID mismatch {sa['id']} vs {en['id']}", file=sys.stderr)
            return 1
        row = {
            "id": sa["id"],
            "speaker_sa": sa.get("speaker"),
            "speaker_en": en.get("speaker_en"),
            "meter_sa": sa.get("meter_sa"),
            "meter_en": en.get("meter_en"),
            "text": sa["text"],
            "padachheda": en["padachheda"],
            "translation": en["translation"],
        }
        merged.append(row)

    data = {
        "title_sa": "कृमिगणितशास्त्रम्",
        "title_en": "Krimi-gaṇita-śāstram",
        "subtitle_sa": "श्रीमहाभारते वनपर्वणि मार्कण्डेययुधिष्ठिरसंवादे",
        "subtitle_en": "From the Mahābhārata, Vana Parva — dialogue of Mārkaṇḍeya and Yudhiṣṭhira",
        "intro_en": intro_en,
        "colophon_sa": colophon_sa,
        "colophon_en": closing_en,
        "sections": build_sections(merged),
    }

    try:
        import yaml
    except ImportError:
        print("PyYAML required", file=sys.stderr)
        return 1

    OUT_YML.write_text(
        yaml.dump(
            data,
            allow_unicode=True,
            default_flow_style=False,
            sort_keys=False,
            width=120,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(OUT_YML, "verses", len(merged), "sections", len(data["sections"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

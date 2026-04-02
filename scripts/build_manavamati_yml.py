# One-off: parse C:\Projects\shatakam\mānavamati_bhramaḥ.txt into _data/manavamati-bhramah.yml
from __future__ import annotations

import re
from pathlib import Path

import yaml

SRC = Path(r"C:\Projects\shatakam\mānavamati_bhramaḥ.txt")
OUT = Path(__file__).resolve().parent.parent / "_data" / "manavamati-bhramah.yml"


def main() -> None:
    raw = SRC.read_text(encoding="utf-8")
    # Fix first verse block: lines after | must be indented for YAML
    lines = raw.splitlines()
    fixed: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        fixed.append(line)
        if re.match(r"^\s+verse:\s*\|\s*$", line):
            i += 1
            while i < len(lines):
                nxt = lines[i]
                if not nxt.strip():
                    fixed.append(nxt)
                    i += 1
                    continue
                if nxt.startswith("    ") and re.match(r"^\s{4}[a-z_]+:", nxt):
                    break
                if nxt.startswith("  - title:"):
                    break
                # indent unindented verse lines
                if nxt.strip() and not nxt.startswith(" "):
                    fixed.append("      " + nxt.strip())
                else:
                    fixed.append(nxt)
                i += 1
            continue
        i += 1

    text = "\n".join(fixed)
    data = yaml.safe_load(text)
    root = data["manavamati_bhramah"]

    # Blog header fields (not in the .txt): keep in sync with other śataka posts (e.g. manasa-vikara).
    book = {
        "title_sa": "मानवमति भ्रमः",
        "title_en": "Mānavamati bhramaḥ",
        "subtitle_en": (
            "One hundred cognitive biases in Sanskrit (Amarakośa-style), "
            "fifty-verse outline in Anuṣṭubh"
        ),
        "intro_visible": (
            "Opening in *vasantatilakā*, the work continues in *anuṣṭubh* on cognitive biases, "
            "grouped by theme. Each śloka is followed by an English gloss where given; "
            "*padaccheda*, *anvaya*, and *dhātvartha* are in the fold-out sections below."
        ),
        "stanzas": [],
    }

    for idx, item in enumerate(root):
        verse = (item.get("verse") or "").strip()
        tr = (item.get("translation") or "").strip()
        book["stanzas"].append(
            {
                "id": idx + 1,
                "title": (item.get("title") or "").strip(),
                "text_sa": verse,
                "translation": tr,
                "padaccheda": (item.get("padaccheda") or "").strip(),
                "anvaya": (item.get("anvaya") or "").strip(),
                "dhatvartha": (item.get("dhatvartha") or "").strip(),
            }
        )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        yaml.dump(
            book,
            allow_unicode=True,
            default_flow_style=False,
            sort_keys=False,
            width=10000,
        ),
        encoding="utf-8",
    )
    print("Wrote", OUT, "stanzas", len(book["stanzas"]))


if __name__ == "__main__":
    main()

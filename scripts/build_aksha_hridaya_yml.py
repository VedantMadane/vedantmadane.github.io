"""One-off helper: Aksha-Hridayam.txt -> _data/aksha-hridaya.yml"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))
from aksha_hridaya_meanings_en import INTRO_EN, MEANINGS  # noqa: E402

DIG = "०१२३४५६७८९"
digit_inner = re.compile(rf"^[{DIG}0-9\s]+$")


def is_meter_only_line(s: str) -> bool:
    s = s.strip()
    m = re.match(r"^॥\s*([^॥]+?)\s*॥\s*$", s)
    if not m:
        return False
    inner = m.group(1).strip()
    return not digit_inner.match(inner)


def verse_ends(line: str) -> bool:
    return bool(re.search(rf"॥\s*[{DIG}0-9]+\s*॥\s*$", line.rstrip()))


def parse_txt(path: Path) -> dict:
    lines = path.read_text(encoding="utf-8").splitlines()
    sections: list[dict] = []
    intro_lines: list[str] = []
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    while i < len(lines):
        line = lines[i]
        if is_meter_only_line(line):
            break
        if line.strip():
            intro_lines.append(line.rstrip())
        i += 1

    current_meter: str | None = None
    current_verses: list[dict] = []
    buf: list[str] = []
    verse_id = 0

    def flush_verse() -> None:
        nonlocal verse_id, buf
        if not buf:
            return
        verse_id += 1
        body = "\n".join(buf).strip()
        current_verses.append({"id": verse_id, "text": body})
        buf = []

    def flush_section() -> None:
        nonlocal current_meter, current_verses
        if current_meter is None and not current_verses:
            return
        sections.append({"meter": current_meter, "verses": list(current_verses)})
        current_meter = None
        current_verses.clear()

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if not stripped:
            i += 1
            continue
        if is_meter_only_line(line):
            flush_verse()
            flush_section()
            m = re.match(r"^॥\s*([^॥]+?)\s*॥\s*$", stripped)
            current_meter = m.group(1).strip() if m else None
            i += 1
            continue
        buf.append(lines[i].rstrip())
        if verse_ends(lines[i]):
            flush_verse()
        i += 1
    flush_verse()
    flush_section()

    data = {
        "title_sa": "अक्ष-हृदयम्",
        "title_en": "Akṣa-hṛdayam",
        "intro": "\n".join(intro_lines).strip(),
        "intro_en": INTRO_EN,
        "sections": sections,
    }
    for sec in data["sections"]:
        for v in sec["verses"]:
            vid = v["id"]
            if vid not in MEANINGS:
                raise KeyError(f"Missing English meaning for verse id {vid}")
            v["meaning"] = MEANINGS[vid]
    return data


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    src = Path(r"C:\Projects\shatakam\Aksha-Hridayam.txt")
    if not src.is_file():
        print("Missing source:", src, file=sys.stderr)
        return 1
    data = parse_txt(src)
    n_verses = sum(len(s["verses"]) for s in data["sections"])
    out = root / "_data" / "aksha-hridaya.yml"
    out.write_text(
        yaml.dump(
            data,
            allow_unicode=True,
            default_flow_style=False,
            sort_keys=False,
            width=1000,
        ),
        encoding="utf-8",
    )
    print(out, "sections", len(data["sections"]), "verses", n_verses)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

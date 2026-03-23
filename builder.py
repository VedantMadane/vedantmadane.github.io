import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent
RAW_TXT_PATH = ROOT / "shatakam_raw.txt"
ENGLISH_TXT_PATH = ROOT / "english.txt"
OUT_YML_PATH = ROOT / "_data" / "shatakam.yml"

_DEV_TO_ASCII = str.maketrans("०१२३४५६७८९", "0123456789")


def _devanagari_int(s: str) -> int:
    return int(s.translate(_DEV_TO_ASCII))


def load_verses_from_raw(path: Path) -> list[dict]:
    """Parse shatakam_raw.txt: section headings skipped; each śloka ends with ॥ <devanagari> ॥."""
    lines = path.read_text(encoding="utf-8").splitlines()
    section_re = re.compile(r"^[०-९]+\.\s")
    verse_end_re = re.compile(r"॥\s*([०-९]+)\s*॥\s*$")

    verses: list[dict] = []
    buf: list[str] = []
    skip_title = True

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if skip_title:
            if stripped.startswith("॥") and stripped.endswith("॥"):
                skip_title = False
            continue

        if section_re.match(stripped):
            continue

        if not buf and stripped.endswith("॥") and not verse_end_re.search(stripped):
            continue

        buf.append(line.rstrip())
        if verse_end_re.search(stripped):
            m = verse_end_re.search(stripped)
            num = _devanagari_int(m.group(1))
            verses.append(
                {
                    "number": num,
                    "sanskrit": "\n".join(buf),
                    "audio_start": 0.0,
                    "audio_end": 0.0,
                    "words": [],
                }
            )
            buf.clear()

    if buf:
        raise ValueError(f"Unclosed verse block at end of file ({len(buf)} lines left)")

    return verses


def load_english_translations(path: Path) -> dict[int, dict[str, str]]:
    """
    Parse english.txt: blocks anchored by [Verse N], optional Poetic: then Prose:.
    """
    text = path.read_text(encoding="utf-8")
    if text.startswith("\ufeff"):
        text = text[1:]

    blocks = re.split(r"(?=^\[Verse \d+\]\s*$)", text, flags=re.MULTILINE)
    out: dict[int, dict[str, str]] = {}

    header_re = re.compile(r"^\[Verse (\d+)\]\s*", re.MULTILINE)
    prose_start = re.compile(r"(?m)^Prose:\s*")

    for block in blocks:
        block = block.strip()
        if not block:
            continue
        hm = header_re.match(block)
        if not hm:
            continue
        vid = int(hm.group(1))
        body = block[hm.end() :].strip()

        prose = ""
        poetic = ""

        if body.startswith("Poetic:"):
            rest = body[len("Poetic:") :].lstrip("\n")
            pm = prose_start.search(rest)
            if pm:
                poetic = rest[: pm.start()].strip()
                prose = rest[pm.end() :].strip()
            else:
                poetic = rest.strip()
        elif body.startswith("Prose:"):
            prose = body[len("Prose:") :].strip()
        else:
            prose = body

        out[vid] = {"prose": prose, "poetic": poetic}

    return out


def generate_shatakam_yaml() -> None:
    raw_data = load_verses_from_raw(RAW_TXT_PATH)
    english = load_english_translations(ENGLISH_TXT_PATH)

    missing = [v["number"] for v in raw_data if v["number"] not in english]
    if missing:
        raise ValueError(f"Missing English blocks for verses: {missing[:10]}{'...' if len(missing) > 10 else ''}")

    yaml_output: list[dict] = []

    for verse in raw_data:
        n = verse["number"]
        eng = english[n]
        lines = verse["sanskrit"].split("\n")

        entry: dict = {
            "number": n,
            "audio_start": verse["audio_start"],
            "audio_end": verse["audio_end"],
            "sanskrit_lines": lines,
            "words": verse["words"],
            "prose": eng["prose"],
        }
        if eng["poetic"]:
            entry["poetic"] = eng["poetic"]

        yaml_output.append(entry)

    OUT_YML_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUT_YML_PATH.open("w", encoding="utf-8") as f:
        yaml.dump(yaml_output, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

    with_poetic = sum(1 for e in yaml_output if "poetic" in e)
    print(f"Successfully generated {OUT_YML_PATH} ({len(yaml_output)} verses, {with_poetic} with poetic).")


if __name__ == "__main__":
    generate_shatakam_yaml()

"""Add Devanāgarī verse lines to _posts/2026-03-30-yantra-shikshana-sutram.md from IAST in .iast-verse-lines blocks.

Requires: pip install indic-transliteration

Also normalizes TeX inside $...$ for MathJax (\\= -> =, \\_ -> _, etc.).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    from indic_transliteration import sanscript as S
except ImportError:
    print("pip install indic-transliteration", file=sys.stderr)
    raise

ROOT = Path(__file__).resolve().parents[1]
POST = ROOT / "_posts" / "2026-03-30-yantra-shikshana-sutram.md"

DIGIT_MAP = str.maketrans("0123456789", "०१२३४५६७८९")


def to_devanagari_line(line: str) -> str:
    m = re.search(r"\|\|\s*(\d+)\s*\|\|", line)
    suffix = ""
    core = line.strip()
    if m:
        num = m.group(1)
        core = line[: m.start()].strip()
        suffix = f" ॥ {num.translate(DIGIT_MAP)} ॥"
    # Hyphenated IAST (e.g. bindu-ghātena) must stay hyphenated for indic_transliteration;
    # do not insert spaces or strip hyphens — that splits valid compounds.
    dev = S.transliterate(core.strip(), S.IAST, S.DEVANAGARI)
    return dev + suffix


def fix_inline_math_tex(text: str) -> str:
    def fix_segment(seg: str) -> str:
        s = seg
        s = s.replace("\\=", "=").replace("\\+", "+")
        s = s.replace("\\-", "-")
        s = s.replace("\\_", "_")
        return s

    out = []
    i = 0
    while i < len(text):
        j = text.find("$", i)
        if j < 0:
            out.append(text[i:])
            break
        out.append(text[i:j])
        k = text.find("$", j + 1)
        if k < 0:
            out.append(text[j:])
            break
        out.append("$" + fix_segment(text[j + 1 : k]) + "$")
        i = k + 1
    return "".join(out)


VERSE_BLOCK = re.compile(
    r'(?P<hdr><p class="verse-topic">.*?</p>\n)'
    r'<div class="sanskrit-text iast-verse-lines">\s*'
    r"(?P<body>.*?)"
    r"\s*</div>",
    re.DOTALL,
)


def transform_post(html: str) -> str:
    html = fix_inline_math_tex(html)

    def repl(m: re.Match[str]) -> str:
        hdr = m.group("hdr")
        body = m.group("body").strip()
        lines = [ln.strip() for ln in re.split(r"<br\s*/?>", body) if ln.strip()]
        dev_lines = [to_devanagari_line(ln) for ln in lines]
        dev_block = (
            f'{hdr}<div class="sanskrit-text sanskrit-verse-lines">\n  '
            + "<br />\n  ".join(dev_lines)
            + "\n</div>\n<details class=\"iast-details\"><summary>IAST transliteration</summary>\n"
            + '<div class="prose-text iast-verse-lines">\n  '
            + "\n  ".join(lines)
            + "\n</div>\n</details>"
        )
        return dev_block

    return VERSE_BLOCK.sub(repl, html)


def main() -> None:
    text = POST.read_text(encoding="utf-8")
    new = transform_post(text)
    if new == text:
        print("No changes (pattern miss?)")
        return
    POST.write_text(new, encoding="utf-8")
    print(f"Updated {POST.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

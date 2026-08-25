# -*- coding: utf-8 -*-
"""Gate blog posts for Pāṇinian purity and chandobaddha budgets. Exit 1 on fail."""
from __future__ import annotations
import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]  # repo root: .../.grok/skills/name/scripts
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
from meter import count_aksharas, line_body, purity_flags  # noqa: E402

POSTS = ROOT / "_posts"


def extract_verses(text: str):
    verses = []
    parts = re.split(r'<p class="verse-topic">', text)
    for part in parts[1:]:
        head = part.split("</p>", 1)[0]
        meter = "?"
        if "अनुष्टुभ्" in head:
            meter = "अनुष्टुभ्"
        elif "उपजाति" in head:
            meter = "उपजाति"
        block = re.search(r'<div class="sanskrit-text[^"]*"[^>]*>(.*?)</div>', part, re.S)
        if not block:
            continue
        lines = re.findall(r"<span[^>]*>([^<]+)</span>", block.group(1))
        lines = [re.sub(r"\s+", " ", ln).strip() for ln in lines if ln.strip()]
        lines = [ln for ln in lines if re.search(r"[\u0900-\u097Fa-zA-Z]", ln)]
        if lines:
            verses.append((meter, lines))
    return verses


def check_verse(meter, lines):
    pflags, cflags = [], []
    for ln in lines:
        pflags.extend(purity_flags(ln))
    counts = [count_aksharas(line_body(ln)) for ln in lines]
    if meter == "अनुष्टुभ्":
        if len(lines) == 2:
            a, b = counts
            if not (14 <= a <= 18 and 14 <= b <= 18):
                cflags.append(f"anu_lines_{a}+{b}")
            if a + b < 28 or a + b > 36:
                cflags.append(f"anu_total_{a+b}")
        elif len(lines) == 4:
            if not all(7 <= c <= 9 for c in counts):
                cflags.append(f"anu_4x_{counts}")
        else:
            cflags.append(f"anu_nlines_{len(lines)}")
        if any(c > 20 for c in counts):
            cflags.append("anu_overlong")
        if any(c < 6 for c in counts):
            cflags.append("anu_fragment")
    elif meter == "उपजाति":
        if len(lines) != 4:
            cflags.append(f"upa_nlines_{len(lines)}")
        elif not all(c == 11 for c in counts):
            cflags.append(f"upa_counts_{counts}")
    else:
        cflags.append("unknown_meter")
    return list(dict.fromkeys(pflags)), list(dict.fromkeys(cflags)), counts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dates", nargs="*", help="YYYY-MM-DD prefixes to check")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--strict-exit", action="store_true", default=True)
    args = ap.parse_args()
    paths = sorted(POSTS.glob("2026-*.md"))
    if args.dates:
        allow = set(args.dates)
        paths = [p for p in paths if p.name[:10] in allow]

    report = []
    n_p = n_c = n_e = 0
    for p in paths:
        t = p.read_text(encoding="utf-8")
        verses = extract_verses(t)
        bad_p = bad_c = 0
        detail = []
        if not verses:
            bad_p = bad_c = 1
            detail.append({"i": 0, "p": ["no_verses"], "c": ["no_verses"]})
        for i, (m, lines) in enumerate(verses, 1):
            pf, cf, counts = check_verse(m, lines)
            if pf:
                bad_p += 1
            if cf:
                bad_c += 1
            if pf or cf:
                detail.append({"i": i, "m": m, "counts": counts, "p": pf, "c": cf, "lines": lines})
        panini_fail = bad_p > 0
        chandas_fail = bad_c > 0
        if panini_fail:
            n_p += 1
        if chandas_fail:
            n_c += 1
        if panini_fail or chandas_fail:
            n_e += 1
        report.append(
            {
                "path": p.name,
                "date": p.name[:10],
                "n_verses": len(verses),
                "panini_fail": panini_fail,
                "chandas_fail": chandas_fail,
                "either": panini_fail or chandas_fail,
                "bad_p": bad_p,
                "bad_c": bad_c,
                "detail": detail[:5],
            }
        )

    N = len(report)
    summary = {
        "total": N,
        "not_paninian": n_p,
        "not_chandobaddha": n_c,
        "either": n_e,
        "both": sum(1 for r in report if r["panini_fail"] and r["chandas_fail"]),
        "ok": sum(1 for r in report if not r["either"]),
    }
    print(
        f"total={N} not_paninian={n_p} not_chandas={n_c} either={n_e} ok={summary['ok']}"
    )
    if args.json:
        out = POSTS.parent / "_gate_report.json"
        out.write_text(json.dumps({"summary": summary, "posts": report}, ensure_ascii=False, indent=2), encoding="utf-8")
        print("wrote", out)
    fails = [r for r in report if r["either"]]
    for r in fails[:20]:
        print(f"FAIL {r['date']} p={r['bad_p']} c={r['bad_c']} {r['path'][:60]}")
    if fails and len(fails) > 20:
        print(f"... +{len(fails)-20} more")
    sys.exit(1 if fails and args.strict_exit else 0)


if __name__ == "__main__":
    main()

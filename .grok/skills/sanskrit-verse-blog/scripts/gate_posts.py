# -*- coding: utf-8 -*-
"""Gate blog posts for purity, chandas, and (optional) Pāṇinian quality.

Default: purity + meter (legacy corpus-safe).
--quality: also require grammar maps, non-echo wfw, no stock formulas/calques.
Exit 1 on fail when --strict-exit (default).
"""
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]  # repo root
if str(Path(__file__).resolve().parent) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
from meter import count_aksharas, line_body, purity_flags  # noqa: E402
from grammar import extract_verse_blocks, verse_quality_flags  # noqa: E402

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


def check_post_quality(text: str):
    """Return list of {i, flags, lines} for quality failures."""
    fails = []
    blocks = extract_verse_blocks(text)
    if len(blocks) != 12:
        fails.append({"i": 0, "flags": [f"verse_count_{len(blocks)}_want_12"], "lines": []})
    for i, b in enumerate(blocks, 1):
        qf = verse_quality_flags(b["meter"], b["lines"], b["details"])
        if qf:
            fails.append({"i": i, "flags": qf, "lines": b["lines"][:2]})
    # post-level: no em/en dash
    if "\u2014" in text or "\u2013" in text:
        fails.append({"i": 0, "flags": ["em_or_en_dash"], "lines": []})
    return fails


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dates", nargs="*", help="YYYY-MM-DD prefixes to check")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--strict-exit", action="store_true", default=True)
    ap.add_argument(
        "--quality",
        action="store_true",
        help="Pāṇinian quality bar: grammar maps, non-echo wfw, no stock formulas",
    )
    ap.add_argument(
        "--paths",
        nargs="*",
        help="Explicit post paths relative to repo or absolute",
    )
    args = ap.parse_args()
    if args.paths:
        paths = []
        for raw in args.paths:
            p = Path(raw)
            if not p.is_absolute():
                p = ROOT / p
            paths.append(p)
        paths = sorted(paths)
    else:
        paths = sorted(POSTS.glob("2026-*.md")) + sorted(POSTS.glob("2027-*.md"))
        if args.dates:
            allow = set(args.dates)
            paths = [p for p in paths if p.name[:10] in allow]

    report = []
    n_p = n_c = n_q = n_e = 0
    for p in paths:
        t = p.read_text(encoding="utf-8")
        verses = extract_verses(t)
        bad_p = bad_c = bad_q = 0
        detail = []
        if not verses:
            bad_p = bad_c = 1
            detail.append({"i": 0, "p": ["no_verses"], "c": ["no_verses"], "q": []})
        for i, (m, lines) in enumerate(verses, 1):
            pf, cf, counts = check_verse(m, lines)
            if pf:
                bad_p += 1
            if cf:
                bad_c += 1
            if pf or cf:
                detail.append(
                    {"i": i, "m": m, "counts": counts, "p": pf, "c": cf, "q": [], "lines": lines}
                )
        q_detail = []
        if args.quality:
            q_detail = check_post_quality(t)
            bad_q = len([x for x in q_detail if x["flags"]])
            for qd in q_detail[:8]:
                detail.append(
                    {
                        "i": qd["i"],
                        "q": qd["flags"],
                        "p": [],
                        "c": [],
                        "lines": qd.get("lines", []),
                    }
                )

        panini_fail = bad_p > 0
        chandas_fail = bad_c > 0
        quality_fail = bad_q > 0
        either = panini_fail or chandas_fail or quality_fail
        if panini_fail:
            n_p += 1
        if chandas_fail:
            n_c += 1
        if quality_fail:
            n_q += 1
        if either:
            n_e += 1
        report.append(
            {
                "path": p.name,
                "date": p.name[:10],
                "n_verses": len(verses),
                "panini_fail": panini_fail,
                "chandas_fail": chandas_fail,
                "quality_fail": quality_fail,
                "either": either,
                "bad_p": bad_p,
                "bad_c": bad_c,
                "bad_q": bad_q,
                "detail": detail[:12],
            }
        )

    N = len(report)
    summary = {
        "total": N,
        "not_paninian": n_p,
        "not_chandobaddha": n_c,
        "not_quality": n_q,
        "either": n_e,
        "ok": sum(1 for r in report if not r["either"]),
        "quality_mode": bool(args.quality),
    }
    print(
        f"total={N} not_paninian={n_p} not_chandas={n_c} not_quality={n_q} "
        f"either={n_e} ok={summary['ok']} quality_mode={args.quality}"
    )
    if args.json:
        out = POSTS.parent / "_gate_report.json"
        out.write_text(
            json.dumps({"summary": summary, "posts": report}, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print("wrote", out)
    fails = [r for r in report if r["either"]]
    for r in fails[:30]:
        qs = f" q={r['bad_q']}" if args.quality else ""
        print(f"FAIL {r['date']} p={r['bad_p']} c={r['bad_c']}{qs} {r['path'][:70]}")
        if args.quality:
            for d in r["detail"]:
                if d.get("q"):
                    print(f"   v{d['i']}: {', '.join(d['q'])}")
    if fails and len(fails) > 30:
        print(f"... +{len(fails)-30} more")
    sys.exit(1 if fails and args.strict_exit else 0)


if __name__ == "__main__":
    main()

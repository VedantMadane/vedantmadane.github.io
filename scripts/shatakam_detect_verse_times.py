#!/usr/bin/env python3
"""
Estimate verse start/end times from one long chant WAV using RMS energy valleys.

Outputs CSV: verse,start_sec,end_sec

Multi-part recordings (e.g. shatakam1.wav = only verses 1-N):
  - Set --verses to how many verses are IN THIS FILE (not always 100).
  - Set --first-verse to the first verse number in this file (default 1).
  - After you concatenate parts into one master MP3, add --global-time-offset for
    part 2+ so times match the full timeline (offset = sum of prior parts' durations).

Example part 1 (verses 1-40 in file):
  python scripts/shatakam_detect_verse_times.py shatakam1.wav -o part1.csv --verses 40 --first-verse 1 --plot p1.png

Example part 2 (verses 41-80), times shifted when master is part1+part2 concatenated:
  python scripts/shatakam_detect_verse_times.py shatakam2.wav -o part2.csv --verses 40 --first-verse 41 --global-time-offset 538.61 --plot p2.png
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import numpy as np
import soundfile as sf


def block_rms_mono(path: Path, hop: int | None = None) -> tuple[np.ndarray, np.ndarray, int]:
    """
    Load WAV as mono, compute RMS in non-overlapping blocks of `hop` samples.
    Returns rms (per block), time center of each block (sec), sample rate.
    """
    info = sf.info(str(path))
    sr = info.samplerate
    if hop is None:
        hop = max(sr // 50, 1)  # ~50 Hz frame rate

    y, _sr = sf.read(str(path), dtype="float32", always_2d=True)
    if y.ndim == 2 and y.shape[1] > 1:
        y = y.mean(axis=1)
    else:
        y = y.ravel()

    n_blk = len(y) // hop
    if n_blk < 2:
        rms = np.array([float(np.sqrt(np.mean(y**2)))])
        t = np.array([0.0])
        return rms, t, sr

    y = y[: n_blk * hop].reshape(n_blk, hop)
    rms = np.sqrt(np.mean(y * y, axis=1))
    t = (np.arange(n_blk) + 0.5) * hop / sr
    return rms, t, sr


def find_verse_starts(
    rms: np.ndarray,
    times: np.ndarray,
    n_verses: int,
    threshold_factor: float,
    min_gap_sec: float,
    duration: float,
) -> np.ndarray:
    k = min(7, len(rms) // 10 or 1)
    if k < 1:
        k = 1
    pad = np.pad(rms, (k, k), mode="edge")
    smooth = np.convolve(pad, np.ones(2 * k + 1) / (2 * k + 1), mode="valid")

    thr = float(np.percentile(smooth, 20) * threshold_factor)
    valley_idx: list[int] = []
    for i in range(1, len(smooth) - 1):
        if smooth[i] <= smooth[i - 1] and smooth[i] <= smooth[i + 1] and smooth[i] < thr:
            valley_idx.append(i)

    starts: list[float] = [0.0]
    for i in valley_idx:
        t = float(times[i])
        if t - starts[-1] >= min_gap_sec:
            starts.append(t)
        if len(starts) >= n_verses:
            break

    if len(starts) < n_verses:
        starts = np.linspace(0.0, max(duration * 0.999, 0.01), n_verses).tolist()
    else:
        starts = starts[:n_verses]

    return np.array(starts, dtype=np.float64)


def main() -> None:
    ap = argparse.ArgumentParser(description="Rough verse timestamps from chant WAV (RMS valleys).")
    ap.add_argument("wav", type=Path, help="Input WAV path")
    ap.add_argument("-o", "--csv", type=Path, default=Path("verse_times.csv"))
    ap.add_argument(
        "--verses",
        type=int,
        default=100,
        help="Number of verses in THIS file only (use <100 for a partial recording)",
    )
    ap.add_argument(
        "--first-verse",
        type=int,
        default=1,
        help="Verse number of the first row in CSV (use 41 if this file starts at verse 41)",
    )
    ap.add_argument(
        "--global-time-offset",
        type=float,
        default=0.0,
        help="Add this many seconds to every start_sec/end_sec (use when merging parts on one timeline)",
    )
    ap.add_argument(
        "--threshold-factor",
        type=float,
        default=1.4,
        help="Multiply 20th-percentile RMS; lower = more valleys pass",
    )
    ap.add_argument(
        "--min-gap",
        type=float,
        default=None,
        help="Min seconds between verse starts (default: duration / verses * 0.55)",
    )
    ap.add_argument("--hop-ms", type=float, default=None, help="Block size in ms (default ~20 ms)")
    ap.add_argument("--plot", type=Path, default=None, help="Save debug PNG")
    args = ap.parse_args()
    if args.first_verse < 1:
        ap.error("--first-verse must be >= 1")

    duration = float(sf.info(str(args.wav)).duration)
    min_gap = args.min_gap
    if min_gap is None:
        min_gap = max(duration / args.verses * 0.55, 1.5)

    hop = None
    if args.hop_ms is not None:
        hop = max(int(sf.info(str(args.wav)).samplerate * args.hop_ms / 1000.0), 1)

    print(f"Loading {args.wav.name} (~{duration:.1f}s)...")
    rms, times, sr = block_rms_mono(args.wav, hop=hop)

    starts = find_verse_starts(
        rms,
        times,
        args.verses,
        args.threshold_factor,
        min_gap,
        duration,
    )

    ends = np.append(starts[1:], duration)
    off = float(args.global_time_offset)
    first = int(args.first_verse)
    rows = []
    for i in range(args.verses):
        rows.append(
            {
                "verse": first + i,
                "start_sec": round(float(starts[i]) + off, 3),
                "end_sec": round(float(ends[i]) + off, 3),
            }
        )

    args.csv.parent.mkdir(parents=True, exist_ok=True)
    with args.csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["verse", "start_sec", "end_sec"])
        w.writeheader()
        w.writerows(rows)
    print(
        f"Wrote {args.csv.resolve()} (verses {first}-{first + args.verses - 1}, "
        f"{args.verses} rows). min_gap={min_gap:.2f}s offset={off}s"
    )

    if args.plot:
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots(figsize=(14, 4))
        ax.plot(times, rms, color="steelblue", lw=0.6, label="RMS")
        for s in starts:
            ax.axvline(s, color="coral", lw=0.7, alpha=0.75)
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("RMS")
        ax.set_title(
            f"{args.wav.name} - verse starts (adjust --min-gap, --threshold-factor, --verses if wrong)"
        )
        ax.legend()
        plt.tight_layout()
        args.plot.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(args.plot, dpi=140)
        print(f"Saved {args.plot.resolve()}")


if __name__ == "__main__":
    main()

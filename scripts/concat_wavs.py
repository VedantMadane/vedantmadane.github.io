#!/usr/bin/env python3
"""
Concatenate WAV files in order and write a single output WAV.
Also emits a verse_times.csv with cumulative offsets (one row per input file = one verse chunk).

Usage:
  python scripts/concat_wavs.py file1.wav file2.wav ... -o master.wav --csv verse_times.csv
  python scripts/concat_wavs.py --folder "C:/path/to/wavs" --pattern "shatakam*.wav" -o master.wav

If inputs have different sample rates, all are resampled to match the first file.
"""

from __future__ import annotations

import argparse
import csv
import glob
from pathlib import Path

import numpy as np
import soundfile as sf


def load_mono(path: Path, target_sr: int | None = None) -> tuple[np.ndarray, int]:
    y, sr = sf.read(str(path), dtype="float32", always_2d=True)
    if y.ndim == 2 and y.shape[1] > 1:
        y = y.mean(axis=1)
    else:
        y = y.ravel()
    if target_sr is not None and sr != target_sr:
        ratio = target_sr / sr
        n_out = int(len(y) * ratio)
        indices = np.linspace(0, len(y) - 1, n_out)
        y = np.interp(indices, np.arange(len(y)), y).astype(np.float32)
        sr = target_sr
    return y, sr


def main() -> None:
    ap = argparse.ArgumentParser(description="Concatenate WAV files into one master WAV + timing CSV.")
    ap.add_argument("files", nargs="*", type=Path, help="WAV files in order")
    ap.add_argument("--folder", type=Path, default=None, help="Folder to scan for WAVs")
    ap.add_argument("--pattern", type=str, default="*.wav", help="Glob pattern inside --folder")
    ap.add_argument("-o", "--output", type=Path, required=True, help="Output WAV path")
    ap.add_argument("--csv", type=Path, default=None, help="Write verse_times.csv with cumulative offsets")
    ap.add_argument("--first-verse", type=int, default=1, help="Starting verse number")
    args = ap.parse_args()

    wav_files: list[Path] = list(args.files)
    if args.folder:
        found = sorted(Path(p) for p in glob.glob(str(args.folder / args.pattern)))
        wav_files.extend(found)

    if not wav_files:
        ap.error("No WAV files provided. Pass paths directly or use --folder + --pattern.")

    print(f"Concatenating {len(wav_files)} files...")

    segments: list[np.ndarray] = []
    durations: list[float] = []
    target_sr: int | None = None

    for p in wav_files:
        y, sr = load_mono(p, target_sr=target_sr)
        if target_sr is None:
            target_sr = sr
        dur = len(y) / sr
        segments.append(y)
        durations.append(dur)
        print(f"  {p.name:40s}  {dur:8.2f}s  ({len(y)} samples @ {sr} Hz)")

    master = np.concatenate(segments)
    total_dur = len(master) / target_sr

    args.output.parent.mkdir(parents=True, exist_ok=True)
    sf.write(str(args.output), master, target_sr, subtype="PCM_16")
    size_mb = args.output.stat().st_size / 1e6
    print(f"\nWrote {args.output} ({total_dur:.2f}s, {size_mb:.1f} MB)")

    if args.csv:
        offset = 0.0
        rows = []
        for i, dur in enumerate(durations):
            rows.append(
                {
                    "verse": args.first_verse + i,
                    "start_sec": round(offset, 3),
                    "end_sec": round(offset + dur, 3),
                }
            )
            offset += dur
        args.csv.parent.mkdir(parents=True, exist_ok=True)
        with args.csv.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=["verse", "start_sec", "end_sec"])
            w.writeheader()
            w.writerows(rows)
        print(f"Wrote {args.csv} ({len(rows)} rows)")


if __name__ == "__main__":
    main()

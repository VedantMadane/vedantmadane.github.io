#!/usr/bin/env python3
"""
Plot waveform, mel spectrogram, RMS envelope, and onset strength for rhythmic chant
(e.g. śloka in fixed meter). No music required: energy dips often mark pāda/verse gaps;
onset strength can reflect syllable-level pulses.

Usage:
  pip install -r scripts/requirements-audio.txt
  python scripts/plot_chant_spectra.py path/to/recitation.mp3 -o chant_plots.png
"""

from __future__ import annotations

import argparse
from pathlib import Path

import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    ap = argparse.ArgumentParser(
        description=(
            "Spectra and energy plots for metered chant (e.g. Sardula-vikridita sloka)."
        )
    )
    ap.add_argument("audio", type=Path, help="Audio file (wav, mp3, flac, etc.)")
    ap.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Write PNG instead of opening a window",
    )
    ap.add_argument(
        "--sr",
        type=int,
        default=22_050,
        help="Sample rate for analysis (default 22050; use 0 or negative for native)",
    )
    ap.add_argument(
        "--hop",
        type=int,
        default=512,
        help="STFT hop length in samples (smaller = finer time resolution)",
    )
    ap.add_argument(
        "--n-fft",
        type=int,
        default=2048,
        dest="n_fft",
        help="FFT window size",
    )
    ap.add_argument(
        "--n-mels",
        type=int,
        default=128,
        dest="n_mels",
        help="Number of mel bands",
    )
    args = ap.parse_args()

    sr = None if args.sr <= 0 else args.sr
    y, sr = librosa.load(args.audio, sr=sr, mono=True)
    duration = float(librosa.get_duration(y=y, sr=sr))

    hop = args.hop
    n_fft = args.n_fft

    # Short-time energy (smooth RMS): useful for gaps between pādas / verses
    rms = librosa.feature.rms(y=y, frame_length=n_fft, hop_length=hop)[0]
    t_rms = librosa.times_like(rms, sr=sr, hop_length=hop)

    # Onset strength ~ syllable / stress pulses in chant
    onset = librosa.onset.onset_strength(y=y, sr=sr, hop_length=hop)
    t_onset = librosa.times_like(onset, sr=sr, hop_length=hop)

    # Mel spectrogram: shows how spectral energy evolves (voicing, breath noise)
    mel = librosa.feature.melspectrogram(
        y=y, sr=sr, n_fft=n_fft, hop_length=hop, n_mels=args.n_mels
    )
    mel_db = librosa.power_to_db(mel, ref=np.max)

    fig, axes = plt.subplots(
        4,
        1,
        figsize=(14, 11),
        sharex=True,
        gridspec_kw={"height_ratios": [1.0, 2.2, 0.9, 0.9], "hspace": 0.12},
    )

    librosa.display.waveshow(y, sr=sr, ax=axes[0], color="#2c5282")
    axes[0].set_ylabel("Waveform")
    axes[0].set_title(
        f"{args.audio.name} - {duration:.1f}s @ {sr} Hz (chant / metered speech)"
    )

    img = librosa.display.specshow(
        mel_db,
        sr=sr,
        hop_length=hop,
        x_axis="time",
        y_axis="mel",
        ax=axes[1],
        cmap="magma",
    )
    axes[1].set_ylabel("Mel")
    fig.colorbar(img, ax=axes[1], format="%+2.0f dB", pad=0.01)

    axes[2].fill_between(t_rms, rms, alpha=0.35, color="#276749")
    axes[2].plot(t_rms, rms, color="#22543d", lw=0.8)
    axes[2].set_ylabel("RMS")
    axes[2].set_title("RMS envelope (look for dips at pāda / verse boundaries)")

    axes[3].plot(t_onset, onset, color="#c05621", lw=0.7)
    axes[3].set_ylabel("Onset")
    axes[3].set_xlabel("Time (s)")
    axes[3].set_title("Onset strength (syllable-level emphasis)")

    plt.tight_layout()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(args.output, dpi=160, bbox_inches="tight")
        print(f"Saved {args.output.resolve()}")
    else:
        plt.show()


if __name__ == "__main__":
    main()

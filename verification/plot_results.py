#!/usr/bin/env python3
"""Generate the repository figure from the committed numerical record."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import tempfile

os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "qtp-matplotlib"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]


def generate(output: Path, preview: Path | None = None):
    record = json.loads((ROOT / "verification/data/filter_results.json").read_text())
    rows = record["quadrature"]
    n = np.array([r["N"] for r in rows])
    fano = np.array([r["F"] for r in rows])
    current = np.array([r["current_at_unit_contact_rate"] for r in rows])
    dense_n = np.geomspace(1, n.max(), 400)
    b = 4 / ((dense_n + 1) * (dense_n + 2))
    lower = 1 / (18 * dense_n**2 + 2)
    upper = (b + (np.pi + 2) / (dense_n * (dense_n + 3))) / (2 - b)
    plt.rcParams.update({
        "font.size": 10, "axes.titlesize": 12, "axes.labelsize": 11,
        "axes.spines.top": False, "axes.spines.right": False,
        "svg.hashsalt": "quantum-transport-precision-v1",
        "font.family": "DejaVu Sans",
    })
    fig, axes = plt.subplots(1, 2, figsize=(11.6, 4.6), layout="constrained")
    blue, orange, green, gray = "#1764A3", "#B35618", "#39816B", "#677480"
    ax = axes[0]
    ax.fill_between(dense_n, lower, upper, color="#D8DEE4", alpha=0.65,
                    label="Bounds on optimal F")
    ax.loglog(dense_n, 1 / (2 * dense_n), color=orange, linestyle="--",
              linewidth=1.8, label="Butterworth chain")
    ax.loglog(n, fano, "o-", color=blue, markersize=4.5, linewidth=2,
              label="Constructed chain")
    ax.set(xlabel="Number of serial sites N", ylabel="Count Fano factor F",
           title="A. Optimal inverse-square order", xlim=(1, n.max()))
    ax.grid(True, which="major", alpha=0.22)
    ax.legend(loc="lower left", frameon=False, fontsize=9)

    ax = axes[1]
    bound = (1 - fano) / np.log(1 / fano)
    ax.semilogx(n, bound, "--", color=orange, linewidth=1.8,
                label="Contact bound at the constructed F")
    ax.semilogx(n, current, "o-", color=blue, markersize=4.5, linewidth=2,
                label="Constructed current")
    asym_n = np.geomspace(2, n.max(), 250)
    ax.semilogx(asym_n, 1 / (3 * np.log(asym_n)), ":", color=green,
                linewidth=2, label="1 / (3 log N), asymptotic")
    ax.set(xlabel="Number of serial sites N", ylabel="Current / contact rate, J / Γ",
           title="B. Logarithmic throughput cost", xlim=(1, n.max()), ylim=(0, 0.78))
    ax.grid(True, which="major", alpha=0.22)
    ax.legend(loc="upper right", frameon=False, fontsize=9)
    for ax in axes:
        ax.set_xticks([1, 2, 4, 8, 16, 32, 64, 128])
        ax.set_xticklabels(["1", "2", "4", "8", "16", "32", "64", "128"])
        ax.tick_params(axis="both", labelsize=9)
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, metadata={"Date": None, "Creator": "verification/plot_results.py"})
    if preview:
        preview.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(preview, dpi=160)
    plt.close(fig)
    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path,
                        default=ROOT / "science/figures/precision_throughput.svg")
    parser.add_argument("--preview", type=Path)
    args = parser.parse_args()
    print(generate(args.output, args.preview))


"""
Run all P2P compare scripts in parallel.
By default saves figures to figures/P2P/ in the project root.
Pass --show to open interactive plot windows instead.

Usage:
    python scripts/P2P/compare/run_all.py [--runtimes N] [--no-save] [--db PATH]
                                          [--output-dir PATH] [--show]
"""

import argparse
import subprocess
import sys
import os

SCRIPTS = [
    "length.py",
    "loss.py",
    "efficiency.py",
    "dark_count.py",
    "node_loss.py",
    "source_err.py",
    "dephasing.py",
    "basis_bias.py",
    "bs_eff.py",
    "charlie_pos.py",
]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--runtimes",   type=int,  default=100)
    parser.add_argument("--no-save",    action="store_true", help="Skip saving results to DB")
    parser.add_argument("--db",         type=str,  default=None, help="Path to results SQLite DB")
    parser.add_argument("--error",      choices=["bars", "shade", "sigma", "iqr", "sem"], default="bars",
                        help="Error display: bars=min/max whiskers (default), shade=±1σ log-space band, "
                             "sigma=±1σ whiskers, iqr=IQR 25–75th percentile, sem=±1 SEM")
    parser.add_argument("--output-dir", type=str,  default=None,
                        help="Directory to write figures (default: <project_root>/figures/P2P)")
    parser.add_argument("--show",       action="store_true",
                        help="Open interactive plot windows instead of saving to disk")
    args = parser.parse_args()

    here         = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(here)))

    if not args.show:
        output_dir = args.output_dir or os.path.join(project_root, "figures", "P2P")
        os.makedirs(output_dir, exist_ok=True)
        print(f"Figures will be saved to: {output_dir}")
    else:
        output_dir = None

    processes = []
    for i, script in enumerate(SCRIPTS, 1):
        cmd = [sys.executable, os.path.join(here, script), "--runtimes", str(args.runtimes)]
        if args.no_save:
            cmd.append("--no-save")
        if args.db is not None:
            cmd += ["--db", args.db]
        cmd += ["--error", args.error]
        if output_dir is not None:
            cmd += ["--output-dir", output_dir]
        print(f"[{i}/{len(SCRIPTS)}] Starting {script}  (runtimes={args.runtimes})")
        p = subprocess.Popen(cmd)
        processes.append(p)

    print(f"\nAll {len(SCRIPTS)} scripts running...")
    for p in processes:
        p.wait()

    if output_dir:
        print(f"All done. Figures saved to {output_dir}")
    else:
        print("All done.")

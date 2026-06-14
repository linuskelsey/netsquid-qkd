"""
Run all P2P compare scripts in parallel.
All plot windows open simultaneously — close them in any order.

Usage:
    python scripts/P2P/compare/run_all.py [--runtimes N]
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
]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--runtimes", type=int, default=100)
    args = parser.parse_args()

    here = os.path.dirname(os.path.abspath(__file__))

    processes = []
    for i, script in enumerate(SCRIPTS, 1):
        print(f"[{i}/{len(SCRIPTS)}] Starting {script}  (runtimes={args.runtimes})")
        p = subprocess.Popen(
            [sys.executable, os.path.join(here, script), "--runtimes", str(args.runtimes)]
        )
        processes.append(p)

    print(f"\nAll {len(SCRIPTS)} scripts running — close windows when done.")
    for p in processes:
        p.wait()

    print("All done.")

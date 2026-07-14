"""
Run all P2P parameter comparison scripts in parallel.

Figures are saved to a timestamped directory under docs/figures/ by default:

    docs/figures/<Month>/<YYYYMMDD> - P2P parameters/all parameters/<script>.png

The month folder is created if it does not exist. The day folder is created if it
does not exist. A fresh 'all parameters' subfolder is created inside the day folder.
Pass --output-dir to override the save location, or --show to display interactively.

Usage:
    python scripts/P2P/compare/run_all.py [options]

Options:
    --runtimes INT   Monte Carlo runs per sweep point (default: 100)
    --workers INT    Worker processes per script (default: 80% of CPU cores)
    --error STR      Error display style: bars (default), shade, sigma, iqr, sem
    --output-dir PATH  Override save directory (disables auto timestamped path)
    --show           Open interactive plot windows instead of saving to disk
    --config PATH    JSON config preset passed to every script
    --compare-configs PATH [PATH ...]
                     2–4 config paths; each script runs in compare-configs mode,
                     overlaying all configs on one figure per sweep

Sweeps run:
    length.py       Key rate vs distance (1-100 km)
    loss.py         Key rate vs fibre attenuation (0-0.3 dB/km)
    efficiency.py   Key rate vs detector efficiency (1.0->0.15)
    dark_count.py   Key rate vs dark count rate (0-250 cps)
    node_loss.py    Key rate vs node/connector loss (0-6 dB)
    source_err.py   Key rate vs source error rate (0-4%)
    dephasing.py    Key rate vs fibre dephasing rate (0-0.003 /km)
    basis_bias.py   Key rate vs X-basis detector bias (1.0->0.5)
    bs_eff.py       Key rate vs beam splitter efficiency (1.0->0.8)
    charlie_pos.py  MDI key rate vs Charlie position (0.1-0.9)

Examples:
    python scripts/P2P/compare/run_all.py
    python scripts/P2P/compare/run_all.py --runtimes 20 --workers 7
    python scripts/P2P/compare/run_all.py --error shade --config configs/layer5_realistic.json
    python scripts/P2P/compare/run_all.py --output-dir results/p2p --runtimes 50
    python scripts/P2P/compare/run_all.py --show
"""

import argparse
import subprocess
import sys
import os
from datetime import datetime

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
    parser = argparse.ArgumentParser(description="Run all P2P parameter comparison scripts")
    parser.add_argument("--runtimes",   type=int,  default=100)
    parser.add_argument("--workers",    type=int,  default=None, help="Worker processes per script (default: 80%% of CPU cores)")
    parser.add_argument("--error",      choices=["bars", "shade", "sigma", "iqr", "sem"], default="bars")
    parser.add_argument("--output-dir", type=str,  default=None, help="Override save directory")
    parser.add_argument("--show",       action="store_true", help="Display plots interactively instead of saving")
    parser.add_argument("--config",     type=str,  default=None, help="JSON config preset")
    parser.add_argument("--no-db",          action="store_true", help="Disable DB writing")
    parser.add_argument("--compare-configs", nargs="+", metavar="PATH", dest="compare_configs",
                        help="2–4 config paths; run every script in compare-configs mode")
    args = parser.parse_args()

    if args.compare_configs and not (2 <= len(args.compare_configs) <= 4):
        parser.error("--compare-configs requires 2–4 paths")

    here         = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(here)))

    if not args.show:
        if args.output_dir:
            output_dir = args.output_dir
        else:
            now       = datetime.now()
            month_dir = os.path.join(project_root, "docs", "figures", now.strftime("%B"))
            day_dir   = os.path.join(month_dir, f"{now.strftime('%Y%m%d')} - P2P parameters")
            subfolder = "config comparison" if args.compare_configs else "all parameters"
            output_dir = os.path.join(day_dir, subfolder)
        os.makedirs(output_dir, exist_ok=True)
        print(f"Figures will be saved to: {output_dir}")
    else:
        output_dir = None

    processes = []
    for i, script in enumerate(SCRIPTS, 1):
        cmd = [sys.executable, os.path.join(here, script), "--runtimes", str(args.runtimes)]
        if args.workers is not None:
            cmd += ["--workers", str(args.workers)]
        cmd += ["--error", args.error]
        if args.compare_configs:
            cmd += ["--compare-configs"] + args.compare_configs
        elif args.config is not None:
            cmd += ["--config", args.config]
        if output_dir is not None:
            cmd += ["--output-dir", output_dir]
        if args.no_db:
            cmd += ["--no-db"]
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

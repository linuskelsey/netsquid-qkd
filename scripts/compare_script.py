"""
QKD Simulation Comparison
============================
Executes both the BB84 and the MDI-QKD netsquid simulations and prints comparative performance metrics.

Usage:
    python scripts/compare_script.py [--runtimes N] [--photons N] [--fibre F] [--freq F] [--speed S]

Defaults:
    runtimes    10
    photons     1024
    fibre       1       (km)
    freq        1e7     (Hz)
    speed       0.8     (fraction of c)
"""

import argparse
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("BB84/") # For BB84 protocols
sys.path.append("MDI/") # For MDI protocols
from BB84.BB84_run import run_BB84_sims
from MDI.mdiRun import run_mdi_sims

import matplotlib.pyplot as plt



def qber(keyA, keyB):
    """Compute QBER between two key lists."""
    if not keyA or not keyB:
        return None
    length = min(len(keyA), len(keyB))
    if length == 0:
        return None
    errors = sum(a != b for a, b in zip(keyA[:length], keyB[:length]))
    return errors / length


def print_run_summary(run_idx, keyA, keyB, keyRate, protocol):
    """Print per-run metrics."""
    if keyA != "nan":
        q = qber(keyA, keyB)
        q_str = f"{q*100:.2f}%" if q is not None else "N/A"
        print(f"  {protocol} run {run_idx+1:>3}:  key_len={len(keyA):>5} | QBER={q_str:>7} | key_rate={keyRate:.4f}")
    else:
        print(f"  {protocol} run {run_idx+1:>3}:  did not complete")


def aggregate_summary(KeyListA, KeyListB, KeyRateList, protocol):
    """Print aggregate metrics across all runs."""
    qbers       = []
    key_rates   = []
    key_lengths = []

    for i, (keyA, keyB) in enumerate(zip(KeyListA, KeyListB)):
        q = qber(keyA, keyB)
        if q is not None and keyA != "nan":
            qbers.append(q)
            key_rates.append(KeyRateList[i])
            key_lengths.append(min(len(keyA), len(keyB)))

    avg_qber     = sum(qbers) / len(qbers) if qbers else float('nan')
    avg_kr       = sum(key_rates) / len(key_rates) if key_rates else float('nan')
    avg_key_len  = sum(key_lengths) / len(key_lengths) if key_lengths else float('nan')
    
    return len(qbers), avg_key_len, avg_qber, avg_kr


def comparative_stats(stats1, stats2):
    print()
    print("=" * 65)
    print(f" Aggregate Results     |    BB84    |     MDI    |")
    print("=" * 65)
    print(f"  Runs completed       |    {stats1[0]:>3}     |    {stats2[0]:>3}     |")
    print(f"  Avg key length       |   {stats1[1]:.2f}   |   {stats2[1]:.2f}   |")
    print(f"  Avg QBER             |    {stats1[2]*100:.2f}%   |    {stats2[2]*100:.2f}%   |")
    print(f"  Avg key rate (kbps)  |   {stats1[3]/1000:.2f}  |   {stats2[3]/1000:.2f}  |")
    return


def main(runtimes=10, photons=1024, fibre=100, freq=1e7, speed=0.8):
    # Parameter setup ===========================================
    # print()
    # print("=" * 65)
    # print("  QKD Simulations")
    # print("=" * 65)
    # print(f"  Runtimes   : {runtimes}")
    # print(f"  Photons    : {photons}")
    # print(f"  Fibre      : {fibre} km")
    # print(f"  Frequency  : {freq:.2e} Hz")
    # print(f"  Speed      : {speed}c")
    # print("=" * 65)
    # print()

    # BB84 run ==================================================
    KeyListA_bb84, KeyListB_bb84, KeyRateList_bb84 = run_BB84_sims(
        runtimes    = runtimes,
        fibreLen    = fibre,
        photonCount = photons,
        sourceFreq  = freq,
        qSpeed      = speed
    )

    # MDI run ===================================================
    KeyListA_mdi, KeyListB_mdi, KeyRateList_mdi = run_mdi_sims(
        runtimes    = runtimes,
        fibreLen    = fibre,
        photonCount = photons,
        sourceFreq  = freq,
        qSpeed      = speed
    )

    # Individual runs ===========================================
    # print("\n  Per-run results:")
    # print("-" * 65)
    # for i in range(runtimes):
        # print_run_summary(i, KeyListA_bb84[i], KeyListB_bb84[i], KeyRateList_bb84[i], "BB84")
        # print_run_summary(i, KeyListA_mdi[i], KeyListB_mdi[i], KeyRateList_mdi[i], "MDI ")

    # Aggregate stats ===========================================
    bb84_stats = aggregate_summary(KeyListA_bb84, KeyListB_bb84, KeyRateList_bb84, "BB84")
    mdi_stats = aggregate_summary(KeyListA_mdi, KeyListB_mdi, KeyRateList_mdi, "MDI")
    # NO PRINT -- comparative_stats(bb84_stats, mdi_stats)

    return bb84_stats, mdi_stats

if __name__ == "__main__":
    Dx = [1,10,25,50,100]

    lengths_bb84 = []
    lengths_mdi = []
    qbers_bb84 = []
    qbers_mdi = []
    rates_bb84 = []
    rates_mdi = []

    for d in Dx:
        bb84, mdi = main(fibre=d)

        lengths_bb84.append(bb84[1])
        qbers_bb84.append(bb84[2])
        rates_bb84.append(bb84[3])

        lengths_mdi.append(mdi[1])
        qbers_mdi.append(mdi[2])
        rates_mdi.append(mdi[3])

    base = rates_bb84[0]
    rates_bb84 = [r / base for r in rates_bb84]
    rates_mdi = [r / base for r in rates_mdi]

    plt.figure()
    plt.plot(Dx, rates_bb84, 'o-', label="BB84")
    plt.plot(Dx, rates_mdi, 's-', label="MDI")

    plt.xlabel("Node separation in kilometres")
    plt.ylabel("Relative secure key rate")
    plt.title("Relative performance: BB84 and MDI-QKD")
    plt.legend()
    plt.grid(True, alpha=0.3)

    ax = plt.gca()
    ax.set_ylim([0,1.1])
    
    plt.show()
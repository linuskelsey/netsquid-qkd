#!/usr/bin/env bash
# Overnight data collection run — surrogate, adaptive MC, timing (users + area).
# Run from repo root: bash scripts/overnight.sh

set -euo pipefail

# ── Parameters ────────────────────────────────────────────────────────────────
WORKERS=8
FIGURES=docs/figures/July/17Jul26-overnight
GRIDS=data/surrogate_grids

SURROGATE_GRID=16        # 16×16 = 256 training points
SURROGATE_RUNTIMES=500

ADAPTIVE_MAX_RUNS=1000
ADAPTIVE_BATCH=100
ADAPTIVE_MIN_RUNS=100

TIMING_N_MIN=10
TIMING_N_MAX=20
TIMING_N_STEP=1
TIMING_RUNTIMES=50
TIMING_SEEDS=10
TIMING_AREA=25

AREA_N=10
AREA_K=3
AREA_MIN=5
AREA_MAX=50
AREA_STEP=5
AREA_RUNTIMES=50
AREA_SEEDS=10

# ── Setup ─────────────────────────────────────────────────────────────────────
mkdir -p "$FIGURES" "$GRIDS"
echo "======================================================"
echo "  Overnight run started: $(date)"
echo "======================================================"

# ── 1. GP Surrogate ───────────────────────────────────────────────────────────
echo ""
echo "[ 1/3 ] GP Surrogate  (${SURROGATE_GRID}×${SURROGATE_GRID} grid, ${SURROGATE_RUNTIMES} runs/pt)"
python scripts/P2P/time/surrogate.py \
    --grid-size   "$SURROGATE_GRID" \
    --runtimes    "$SURROGATE_RUNTIMES" \
    --workers     "$WORKERS" \
    --protocol    both \
    --save-grid   "$GRIDS" \
    --output-dir  "$FIGURES"

# ── 2. Adaptive MC ────────────────────────────────────────────────────────────
echo ""
echo "[ 2/3 ] Adaptive MC  (max=${ADAPTIVE_MAX_RUNS}, batch=${ADAPTIVE_BATCH})"
python scripts/P2P/time/adaptive_mc.py \
    --max-runs    "$ADAPTIVE_MAX_RUNS" \
    --batch       "$ADAPTIVE_BATCH" \
    --min-runs    "$ADAPTIVE_MIN_RUNS" \
    --workers     "$WORKERS" \
    --protocol    both \
    --output-dir  "$FIGURES"

# ── 3. Timing ─────────────────────────────────────────────────────────────────
echo ""
echo "[ 3/4 ] Timing vs users  (N=${TIMING_N_MIN}–${TIMING_N_MAX}, ${TIMING_SEEDS} seeds, ${TIMING_RUNTIMES} runtimes)"
python scripts/network/time/time_vs_users.py \
    --n-min    "$TIMING_N_MIN" \
    --n-max    "$TIMING_N_MAX" \
    --n-step   "$TIMING_N_STEP" \
    --runtimes "$TIMING_RUNTIMES" \
    --seeds    "$TIMING_SEEDS" \
    --area     "$TIMING_AREA" \
    --workers  "$WORKERS" \
    --save     "$FIGURES/time_vs_users.png"

# ── 4. Timing vs area ─────────────────────────────────────────────────────────
echo ""
echo "[ 4/4 ] Timing vs area  (N=${AREA_N}, area=${AREA_MIN}–${AREA_MAX}km, ${AREA_SEEDS} seeds)"
python scripts/network/time/time_vs_area.py \
    --n         "$AREA_N" \
    --k         "$AREA_K" \
    --area-min  "$AREA_MIN" \
    --area-max  "$AREA_MAX" \
    --area-step "$AREA_STEP" \
    --runtimes  "$AREA_RUNTIMES" \
    --seeds     "$AREA_SEEDS" \
    --workers   "$WORKERS" \
    --save      "$FIGURES/time_vs_area.png"

echo ""
echo "======================================================"
echo "  Overnight run complete: $(date)"
echo "======================================================"

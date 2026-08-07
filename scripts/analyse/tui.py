"""
Interactive TUI for reconstructing QKD simulation figures from results.db.

Usage:
    python scripts/analyse/tui.py [--output-dir DIR]

--output-dir DIR: when set, every Plot click saves a figure bundle
{plot.png, plot.tex, assumptions.md} into DIR instead of opening a window
(named p2p_<sweep> or network_<x>_<y>; topology figures save alongside as
network_topology.png, not part of the 3-file bundle). Omit to keep the
default interactive-window behaviour described below.

P2P tab
    Select a sweep axis (x-axis), adjust the 9 fixed parameter values, pick
    one or both protocols and an error display mode, then click Plot. The
    status bar debounces 300 ms after every control change and fires a fast
    COUNT(*) query so you can see how many rows match before plotting.

Network tab
    Select x-axis (n_users / k_relays) and y-axis. Fixed params are chosen
    from dropdowns populated with values actually present in the DB. Seed
    blank = aggregate all seeds. If a specific seed is selected, Plot also
    produces a second MDI topology figure for that seed.

Plot windows
    Each Plot click spawns a separate Python process for matplotlib so the
    TUI stays live. Multiple windows can be open simultaneously. Save via
    the matplotlib toolbar.

Error modes (same logic as compare scripts):
    bars  — min/max whiskers
    shade — log-space ±1σ fill band
    sigma — log-space ±1σ error bars
    iqr   — Q25/Q75 whiskers
    sem   — standard error of mean bars

Key bindings:
    q / ctrl+c — quit
"""
import argparse
import math
import multiprocessing as mp
import os
import sys
import time
import traceback
from typing import Dict, List, Optional

import matplotlib.pyplot as plt

_ROOT    = os.path.join(os.path.dirname(__file__), "../..")
_NET_DIR = os.path.join(_ROOT, "network")
sys.path.insert(0, _ROOT)
sys.path.insert(0, _NET_DIR)          # so topology.py is importable in child processes
sys.path.insert(0, os.path.dirname(__file__))

from lib.plotting import apply_thesis_style, save_bundle

apply_thesis_style()

from textual.app import App, ComposeResult
from textual.containers import Horizontal, ScrollableContainer, Vertical
from textual.widgets import (
    Button, Checkbox, Header, Input, Label,
    RadioButton, RadioSet, Select, Static, TabbedContent, TabPane,
)
from textual import on

from db import (
    COL_DEFAULTS, ERROR_MODES, NET_X_COLS, NET_Y_COLS, NET_Y_LABELS,
    SWEEP_COLS, count_p2p, list_distinct, query_network, query_p2p,
)

_MARKERS = {"BB84": "o-", "MDI": "s-"}
_COLOURS = {"BB84": "tab:blue", "MDI": "tab:orange"}
_TOPO_COLOURS = [
    "#e41a1c", "#377eb8", "#4daf4a", "#984ea3",
    "#ff7f00", "#a65628", "#f781bf", "#999999",
]


# ── topology drawing (inlined — visualise_network.py has a broken import) ─────

def _draw_mdi_topo(ax, topo) -> None:
    """Draw MDI-QKD topology onto ax using matplotlib only (no networkx)."""
    def _col(k):
        return _TOPO_COLOURS[k % len(_TOPO_COLOURS)]

    for i in range(topo.N):
        r = int(topo.user_relay[i])
        ax.plot(
            [topo.user_pos[i][0], topo.relay_pos[r][0]],
            [topo.user_pos[i][1], topo.relay_pos[r][1]],
            color=_col(r), lw=0.8, alpha=0.6,
        )
    for k1 in range(topo.K):
        for k2 in range(k1 + 1, topo.K):
            ax.plot(
                [topo.relay_pos[k1][0], topo.relay_pos[k2][0]],
                [topo.relay_pos[k1][1], topo.relay_pos[k2][1]],
                "k--", lw=0.8, alpha=0.4,
            )
    for i in range(topo.N):
        ax.scatter(*topo.user_pos[i], color=_col(int(topo.user_relay[i])), s=60, zorder=3)
    for k in range(topo.K):
        ax.scatter(*topo.relay_pos[k], marker="s", s=100, color=_col(k), zorder=4)

    ax.scatter([], [], marker="o", color="grey", s=60, label="User")
    ax.scatter([], [], marker="s", color="grey", s=100, label="Relay")
    ax.set_xlabel("x (km)")
    ax.set_ylabel("y (km)")
    ax.legend(loc="upper right", fontsize=8)
    ax.set_aspect("equal")


# ── plot helpers ──────────────────────────────────────────────────────────────

def _sim_count_label(ns: List[int]) -> str:
    if not ns:
        return ""
    lo, hi = min(ns), max(ns)
    return f"n={lo} sims/point" if lo == hi else f"n={lo}–{hi} sims/point"


def _errorbar_p2p(ax, d: dict, error_mode: str, proto: str) -> None:
    """
    Plot one P2P protocol series using log-space statistics (bps → kbps).
    Mirrors error-mode logic in scripts/P2P/compare/*.py exactly.
    """
    x      = d["x"]
    y      = [v / 1000 for v in d["mean"]]
    s      = d["std_log"]
    colour = _COLOURS[proto]
    fmt    = _MARKERS[proto]

    if error_mode == "bars":
        lo = [max(y[i] - d["min"][i] / 1000, 0) for i in range(len(x))]
        hi = [max(d["max"][i] / 1000 - y[i], 0) for i in range(len(x))]
        ax.errorbar(x, y, yerr=[lo, hi], fmt=fmt, color=colour, label=proto, capsize=3)
    elif error_mode == "sigma":
        lo = [y[i] * (1 - math.exp(-s[i])) for i in range(len(x))]
        hi = [y[i] * (math.exp(s[i]) - 1)  for i in range(len(x))]
        ax.errorbar(x, y, yerr=[lo, hi], fmt=fmt, color=colour, label=proto, capsize=3)
    elif error_mode == "iqr":
        lo = [max(y[i] - d["q25"][i] / 1000, 0) for i in range(len(x))]
        hi = [max(d["q75"][i] / 1000 - y[i], 0) for i in range(len(x))]
        ax.errorbar(x, y, yerr=[lo, hi], fmt=fmt, color=colour, label=proto, capsize=3)
    elif error_mode == "sem":
        sem = [v / 1000 for v in d["sem"]]
        ax.errorbar(x, y, yerr=[sem, sem], fmt=fmt, color=colour, label=proto, capsize=3)
    else:  # shade
        line, = ax.plot(x, y, fmt, color=colour, label=proto)
        lo = [y[i] * math.exp(-s[i]) for i in range(len(x))]
        hi = [y[i] * math.exp(+s[i]) for i in range(len(x))]
        ax.fill_between(x, lo, hi, alpha=0.15, color=line.get_color())


def _plot_p2p_thread(
    sweep_col: str, sweep_label: str,
    fixed_dict: dict, protocols: List[str], error_mode: str,
    output_dir: Optional[str] = None,
) -> None:
    """Blocking — runs in a separate process via mp.Process."""
    try:
        data = query_p2p(sweep_col, fixed_dict, protocols)
        if not any(d["x"] for d in data.values()):
            print("[analyse] No P2P data matches current filter.")
            return

        fig, ax = plt.subplots(figsize=(8, 5))
        all_ns: List[int] = []
        for proto, d in data.items():
            if not d["x"]:
                continue
            _errorbar_p2p(ax, d, error_mode, proto)
            all_ns.extend(d["n"])

        ax.set_xlabel(sweep_label)
        ax.set_ylabel("Secure key rate (kbps)")
        ax.set_yscale("log")
        ax.grid(True, alpha=0.3)
        ax.legend()
        short_title = f"Key Rate vs {sweep_label.split(' (')[0]}"
        plt.title(short_title)
        plt.tight_layout()

        if output_dir:
            save_bundle(
                fig, output_dir, f"p2p_{sweep_col}",
                title=short_title,
                assumptions={**fixed_dict, "Sweep column": sweep_col,
                             "Protocols": protocols, "Error display": error_mode,
                             "MC runs per point": _sim_count_label(all_ns)},
                notes=["Reconstructed from results.db via the analyse TUI."],
            )
            print(f"[analyse] saved to {os.path.join(output_dir, f'p2p_{sweep_col}')}")
        else:
            plt.show()
    except Exception:
        traceback.print_exc()


def _errorbar_net(ax, d: dict, error_mode: str, proto: str, is_rate: bool) -> None:
    """
    Plot one network protocol series.
    is_rate: True → convert bps→kbps and use log-space std for sigma/shade.
             False → raw values, linear std (success_rate is [0,1]).
    """
    x      = d["x"]
    sc     = 1000 if is_rate else 1
    y      = [v / sc for v in d["mean"]]
    colour = _COLOURS[proto]
    fmt    = _MARKERS[proto]

    if error_mode == "bars":
        lo = [max(y[i] - d["min"][i] / sc, 0) for i in range(len(x))]
        hi = [max(d["max"][i] / sc - y[i], 0) for i in range(len(x))]
        ax.errorbar(x, y, yerr=[lo, hi], fmt=fmt, color=colour, label=proto, capsize=3)
    elif error_mode in ("sigma", "shade"):
        if is_rate:
            s  = d["std_log"]
            lo = [y[i] * (1 - math.exp(-s[i])) for i in range(len(x))]
            hi = [y[i] * (math.exp(s[i]) - 1)  for i in range(len(x))]
        else:
            std = [v / sc for v in d["std"]]
            lo  = [max(y[i] - std[i], 0) for i in range(len(x))]
            hi  = [y[i] + std[i] for i in range(len(x))]
        if error_mode == "sigma":
            ax.errorbar(x, y, yerr=[lo, hi], fmt=fmt, color=colour, label=proto, capsize=3)
        else:
            line, = ax.plot(x, y, fmt, color=colour, label=proto)
            ax.fill_between(x, lo, hi, alpha=0.15, color=line.get_color())
    elif error_mode == "iqr":
        lo = [max(y[i] - d["q25"][i] / sc, 0) for i in range(len(x))]
        hi = [max(d["q75"][i] / sc - y[i], 0) for i in range(len(x))]
        ax.errorbar(x, y, yerr=[lo, hi], fmt=fmt, color=colour, label=proto, capsize=3)
    elif error_mode == "sem":
        sem = [v / sc for v in d["sem"]]
        ax.errorbar(x, y, yerr=[sem, sem], fmt=fmt, color=colour, label=proto, capsize=3)


_SHORT_Y = {
    "avg_key_rate": "Avg Key Rate",
    "success_rate": "Success Rate",
    "min_key_rate": "Min Key Rate",
    "max_key_rate": "Max Key Rate",
}


def _plot_network_thread(
    x_col: str, y_col: str,
    fixed_dict: dict, protocols: List[str], error_mode: str,
    output_dir: Optional[str] = None,
) -> None:
    """
    Blocking — runs in a separate process via mp.Process.
    If a specific seed is selected, also produces an MDI topology figure
    using topology.py (numpy/sklearn — no netsquid required).
    Both figures are shown together via a single plt.show() call.
    """
    try:
        data    = query_network(x_col, y_col, fixed_dict, protocols)
        is_rate = y_col != "success_rate"
        if not any(d["x"] for d in data.values()):
            print("[analyse] No network data matches current filter.")
            return

        # Key rate figure
        fig1, ax1 = plt.subplots(figsize=(8, 5))
        all_ns: List[int] = []
        for proto, d in data.items():
            if not d["x"]:
                continue
            _errorbar_net(ax1, d, error_mode, proto, is_rate)
            all_ns.extend(d["n"])

        ax1.set_xlabel(x_col.replace("_", " "))
        ax1.set_ylabel(NET_Y_LABELS[y_col])
        if is_rate:
            ax1.set_yscale("log")
        ax1.grid(True, alpha=0.3)
        ax1.legend()
        x_label_short = "User Count" if x_col == "n_users" else "Relay Count"
        short_title = f"{_SHORT_Y[y_col]} vs {x_label_short}"
        fig1.suptitle(short_title)
        fig1.tight_layout()

        # Topology figure — only when a specific seed is selected
        seed = fixed_dict.get("seed")
        if seed is not None:
            _try_topology_fig(x_col, data, fixed_dict, int(seed), output_dir)

        if output_dir:
            save_bundle(
                fig1, output_dir, f"network_{x_col}_{y_col}",
                title=short_title,
                assumptions={**fixed_dict, "X axis": x_col, "Y axis": y_col,
                             "Protocols": protocols, "Error display": error_mode,
                             "MC runs per point": _sim_count_label(all_ns)},
                notes=["Reconstructed from results.db via the analyse TUI."],
            )
            print(f"[analyse] saved to {os.path.join(output_dir, f'network_{x_col}_{y_col}')}")
        else:
            plt.show()
    except Exception:
        traceback.print_exc()


def _try_topology_fig(x_col: str, data: dict, fixed_dict: dict, seed: int,
                      output_dir: Optional[str] = None) -> None:
    """
    Attempt to produce an MDI topology figure for the given seed.
    Silently skips if required params are unavailable or topology import fails.
    n_users / k_relays are taken from fixed_dict; if one is the x-axis
    (and therefore absent), the median x-value from the query results is used.
    """
    try:
        from topology import place_users, optimise_relays, Topology  # type: ignore

        # Determine topology params
        all_x = sorted({xv for d in data.values() for xv in d["x"]})
        mid_x = int(all_x[len(all_x) // 2]) if all_x else None

        if x_col == "n_users":
            topo_n = mid_x
            topo_k = fixed_dict.get("k_relays")
        else:
            topo_n = fixed_dict.get("n_users")
            topo_k = mid_x

        if topo_n is None or topo_k is None:
            print("[analyse] Cannot determine n_users / k_relays for topology — skipping.")
            return

        area = fixed_dict.get("area_km") or 25.0
        user_pos  = place_users(int(topo_n), area_km=area, seed=seed)
        relay_pos = optimise_relays(user_pos, int(topo_k), seed=seed)
        topo      = Topology(user_pos, relay_pos)

        fig2, ax2 = plt.subplots(figsize=(6, 6))
        _draw_mdi_topo(ax2, topo)
        fig2.suptitle(f"MDI-QKD Topology (N={topo_n}, K={topo_k})")
        fig2.tight_layout()

        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
            topo_path = os.path.join(output_dir, "network_topology.png")
            fig2.savefig(topo_path, dpi=150)
            print(f"[analyse] topology saved to {topo_path}")

    except ImportError:
        print("[analyse] topology.py not importable — skipping topology figure.")
    except Exception:
        traceback.print_exc()


# ── TUI ───────────────────────────────────────────────────────────────────────

class AnalyseTUI(App):
    CSS = """
    Screen { background: $surface; }
    TabbedContent { height: 1fr; }
    ContentSwitcher { height: 1fr; }
    TabPane { height: 1fr; padding: 0; }
    .tab-h { height: 1fr; }
    .tab-left {
        width: 30; padding: 1 2;
        border-right: solid $primary-darken-2;
    }
    .tab-right { width: 1fr; padding: 1 2; height: 1fr; }
    .tab-right ScrollableContainer { height: auto; max-height: 60%; }
    .net-right ScrollableContainer { height: 1fr; }
    .sec { color: $text-muted; text-style: bold; margin-top: 1; margin-bottom: 0; }
    .row { height: auto; align: left middle; }
    .plbl { width: 22; }
    Input  { width: 13; height: 3; }
    Select { width: 20; }
    Button { margin-top: 1; margin-right: 1; }
    #status { height: 1; background: $primary-darken-3; padding: 0 2; dock: bottom; }
    """
    BINDINGS = [("q", "quit", "Quit")]

    def __init__(self, output_dir: Optional[str] = None) -> None:
        super().__init__()
        self._output_dir = output_dir
        self._p2p_sweep_idx: int = 0
        self._p2p_error_idx: int = 0
        self._net_x_idx: int = 0
        self._net_y_idx: int = 0
        self._net_error_idx: int = 0
        self._debounce_timer = None

        # Pre-fetch distinct network values for Select dropdowns
        try:
            self._net_n_users  = [int(v)   for v in list_distinct("n_users",  "network_results")]
            self._net_k_relays = [int(v)   for v in list_distinct("k_relays", "network_results") if v is not None]
            self._net_areas    = [float(v) for v in list_distinct("area_km",  "network_results")]
            self._net_seeds    = [int(v)   for v in list_distinct("seed",     "network_results")]
        except Exception:
            self._net_n_users  = list(range(2, 21))
            self._net_k_relays = [1, 2, 3, 4, 5]
            self._net_areas    = [10.0, 25.0, 50.0]
            self._net_seeds    = []

    # ── compose ───────────────────────────────────────────────────────────────

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with TabbedContent():

            with TabPane("P2P", id="tab-p2p"):
                with Horizontal(classes="tab-h"):
                    with Vertical(classes="tab-left"):
                        yield Label("SWEEP", classes="sec")
                        with RadioSet(id="p2p-sweep"):
                            for _, label, _ in SWEEP_COLS:
                                yield RadioButton(label)
                        yield Label("PROTOCOL", classes="sec")
                        yield Checkbox("BB84", id="p2p-bb84", value=True)
                        yield Checkbox("MDI",  id="p2p-mdi",  value=True)
                    with Vertical(classes="tab-right"):
                        with ScrollableContainer():
                            yield Label("FIXED PARAMS", classes="sec")
                            for col, label, default in SWEEP_COLS:
                                with Horizontal(classes="row"):
                                    yield Label(label, classes="plbl")
                                    yield Input(str(default), id=f"fp-{col}")
                        yield Label("ERROR MODE", classes="sec")
                        with RadioSet(id="p2p-error"):
                            for mode in ERROR_MODES:
                                yield RadioButton(mode)
                        with Horizontal():
                            yield Button("Reset defaults", id="p2p-reset", variant="default")
                            yield Button("Plot",           id="p2p-plot",  variant="primary")

            with TabPane("Network", id="tab-net"):
                with Horizontal(classes="tab-h"):
                    with Vertical(classes="tab-left"):
                        yield Label("X AXIS", classes="sec")
                        with RadioSet(id="net-x"):
                            for col in NET_X_COLS:
                                yield RadioButton(col.replace("_", " "))
                        yield Label("Y AXIS", classes="sec")
                        with RadioSet(id="net-y"):
                            for col in NET_Y_COLS:
                                yield RadioButton(col.replace("_", " "))
                        yield Label("PROTOCOL", classes="sec")
                        yield Checkbox("BB84", id="net-bb84", value=True)
                        yield Checkbox("MDI",  id="net-mdi",  value=True)
                    with Vertical(classes="tab-right net-right"):
                        with ScrollableContainer():
                            yield Label("FIXED PARAMS", classes="sec")
                            with Horizontal(classes="row"):
                                yield Label("n users", classes="plbl")
                                yield Select(
                                    [(str(n), n) for n in self._net_n_users],
                                    allow_blank=False,
                                    id="nfp-n_users",
                                )
                            with Horizontal(classes="row"):
                                yield Label("k relays", classes="plbl")
                                yield Select(
                                    [(str(k), k) for k in self._net_k_relays],
                                    allow_blank=False,
                                    id="nfp-k_relays",
                                )
                            with Horizontal(classes="row"):
                                yield Label("area km", classes="plbl")
                                yield Select(
                                    [(str(a), a) for a in self._net_areas],
                                    allow_blank=False,
                                    id="nfp-area_km",
                                )
                            with Horizontal(classes="row"):
                                yield Label("seed (blank=all)", classes="plbl")
                                yield Select(
                                    [(str(s), s) for s in self._net_seeds],
                                    prompt="All seeds",
                                    id="nfp-seed",
                                )
                            yield Label("ERROR MODE", classes="sec")
                            with RadioSet(id="net-error"):
                                for mode in ERROR_MODES:
                                    yield RadioButton(mode)
                        yield Button("Plot", id="net-plot", variant="primary")

        yield Static("filtered: —", id="status")

    def on_mount(self) -> None:
        self._update_p2p_states()
        self._update_net_states()
        self._schedule_count()

    # ── event handlers ────────────────────────────────────────────────────────

    @on(RadioSet.Changed, "#p2p-sweep")
    def _p2p_sweep_changed(self, event: RadioSet.Changed) -> None:
        self._p2p_sweep_idx = event.index
        self._update_p2p_states()
        self._schedule_count()

    @on(RadioSet.Changed, "#p2p-error")
    def _p2p_error_changed(self, event: RadioSet.Changed) -> None:
        self._p2p_error_idx = event.index

    @on(RadioSet.Changed, "#net-x")
    def _net_x_changed(self, event: RadioSet.Changed) -> None:
        self._net_x_idx = event.index
        self._update_net_states()
        self._schedule_count()

    @on(RadioSet.Changed, "#net-y")
    def _net_y_changed(self, event: RadioSet.Changed) -> None:
        self._net_y_idx = event.index

    @on(RadioSet.Changed, "#net-error")
    def _net_error_changed(self, event: RadioSet.Changed) -> None:
        self._net_error_idx = event.index

    @on(Input.Changed)
    def _input_changed(self) -> None:
        self._schedule_count()

    @on(Select.Changed)
    def _select_changed(self) -> None:
        self._schedule_count()

    @on(Checkbox.Changed)
    def _checkbox_changed(self) -> None:
        self._schedule_count()

    @on(Button.Pressed, "#p2p-plot")
    def _p2p_plot(self) -> None:
        col, label, _ = SWEEP_COLS[self._p2p_sweep_idx]
        protos = self._get_protocols("p2p")
        if not protos:
            return
        mp.Process(
            target=_plot_p2p_thread,
            args=(col, label, self._get_p2p_fixed(), protos, ERROR_MODES[self._p2p_error_idx],
                  self._output_dir),
        ).start()

    @on(Button.Pressed, "#p2p-reset")
    def _p2p_reset(self) -> None:
        for col, _, default in SWEEP_COLS:
            self.query_one(f"#fp-{col}", Input).value = str(default)
        self._schedule_count()

    @on(Button.Pressed, "#net-plot")
    def _net_plot(self) -> None:
        protos = self._get_protocols("net")
        if not protos:
            return
        mp.Process(
            target=_plot_network_thread,
            args=(
                NET_X_COLS[self._net_x_idx],
                NET_Y_COLS[self._net_y_idx],
                self._get_net_fixed(),
                protos,
                ERROR_MODES[self._net_error_idx],
                self._output_dir,
            ),
        ).start()

    # ── state helpers ─────────────────────────────────────────────────────────

    def _get_p2p_fixed(self) -> Dict[str, float]:
        fixed = {}
        for col, _, _ in SWEEP_COLS:
            try:
                fixed[col] = float(self.query_one(f"#fp-{col}", Input).value)
            except ValueError:
                fixed[col] = COL_DEFAULTS[col]
        return fixed

    def _get_net_fixed(self) -> Dict:
        fixed: Dict = {}
        for col in ("n_users", "k_relays", "area_km"):
            val = self.query_one(f"#nfp-{col}", Select).value
            fixed[col] = None if val is Select.NULL else val
        seed_val = self.query_one("#nfp-seed", Select).value
        fixed["seed"] = None if seed_val is Select.NULL else int(seed_val)
        return fixed

    def _get_protocols(self, prefix: str) -> List[str]:
        protos = []
        if self.query_one(f"#{prefix}-bb84", Checkbox).value:
            protos.append("BB84")
        if self.query_one(f"#{prefix}-mdi", Checkbox).value:
            protos.append("MDI")
        return protos

    def _update_p2p_states(self) -> None:
        """Disable the fixed-param input matching the current sweep axis."""
        sweep_col = SWEEP_COLS[self._p2p_sweep_idx][0]
        for col, _, _ in SWEEP_COLS:
            self.query_one(f"#fp-{col}", Input).disabled = (col == sweep_col)

    def _update_net_states(self) -> None:
        """Disable the fixed-param Select matching the current x-axis."""
        x_col = NET_X_COLS[self._net_x_idx]
        for col in ("n_users", "k_relays"):
            self.query_one(f"#nfp-{col}", Select).disabled = (col == x_col)

    def _schedule_count(self) -> None:
        if self._debounce_timer is not None:
            self._debounce_timer.stop()
        self._debounce_timer = self.set_timer(0.3, self._refresh_count)

    def _refresh_count(self) -> None:
        t0     = time.time()
        sweep  = SWEEP_COLS[self._p2p_sweep_idx][0]
        fixed  = self._get_p2p_fixed()
        protos = self._get_protocols("p2p")
        n      = count_p2p(sweep, fixed, protos) if protos else 0
        dt     = time.time() - t0
        self.query_one("#status", Static).update(
            f"filtered: {n:,} rows   Q: {dt:.2f}s   (sweep: {sweep})"
        )


if __name__ == "__main__":
    _parser = argparse.ArgumentParser(description="Interactive TUI for reconstructing QKD figures from results.db")
    _parser.add_argument("--output-dir", metavar="DIR", default=None,
                         help="Save each Plot click as a figure bundle to this directory instead of opening a window")
    _args = _parser.parse_args()
    AnalyseTUI(output_dir=_args.output_dir).run()

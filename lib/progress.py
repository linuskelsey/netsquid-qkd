import sys
import time
import threading

_FRAMES = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]


class Progress:
    """Animated in-place spinner with percentage and elapsed time.

    Background thread redraws every 100ms so the spinner animates
    continuously regardless of how long each simulation step takes.

    Usage:
        prog = Progress(total=n)
        prog.update(step, "label")   # update step count and label
        prog.done()                  # stop spinner, print completion line
    """

    def __init__(self, total):
        self.total       = total
        self._start      = time.time()
        self._frame      = 0
        self._step       = 0
        self._label      = ""
        self._active     = False
        self._lock       = threading.Lock()
        self._stop       = threading.Event()
        self._thread     = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()

    def _render(self):
        pct    = int(100 * self._step / self.total) if self.total else 0
        elapsed = int(time.time() - self._start)
        m, s   = divmod(elapsed, 60)
        t      = f"{m}m {s:02d}s" if m else f"{s}s"
        frame  = _FRAMES[self._frame % len(_FRAMES)]
        self._frame += 1
        sys.stdout.write(f"\r{frame} {pct:3d}%  {self._label}  {t}\033[K")
        sys.stdout.flush()

    def _loop(self):
        while not self._stop.is_set():
            with self._lock:
                if self._active:
                    self._render()
            time.sleep(0.1)

    def print(self, *args, **kwargs):
        """Clear spinner line, print a normal line, spinner resumes."""
        with self._lock:
            sys.stdout.write("\r\033[K")
            sys.stdout.flush()
        print(*args, **kwargs)

    def update(self, step, label=""):
        with self._lock:
            self._step   = step
            self._label  = label
            self._active = True
            self._render()

    def stop(self):
        """Stop the spinner thread silently (no output)."""
        self._stop.set()
        self._thread.join()
        sys.stdout.write("\r\033[K")
        sys.stdout.flush()
        self._active = False

    def done(self):
        self._stop.set()
        self._thread.join()
        elapsed = int(time.time() - self._start)
        m, s = divmod(elapsed, 60)
        t = f"{m}m {s:02d}s" if m else f"{s}s"
        sys.stdout.write(f"\r\033[K✓ complete  total {t}\n")
        sys.stdout.flush()

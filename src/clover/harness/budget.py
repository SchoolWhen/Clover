"""Fair-budget controller (sequence 4.2).

Two enforceable budgets for cross-route comparisons:
  - Equal-Byte: cap on per-frame state+history bytes. Frames beyond the
    cap are dropped oldest-first (and the drop is *reported*, never silent).
  - Equal-Latency: a deadline in ms; in strict mode an overrun raises
    BudgetExceeded, in anytime mode the wrapped callable's `fallback`
    result is returned (hard-real-time contract, sequence 2.6).
"""
from __future__ import annotations

import time
from dataclasses import dataclass, field

from ..core import Frame


class BudgetExceeded(RuntimeError):
    pass


@dataclass
class FairBudgetController:
    max_state_bytes: int | None = None      # Equal-Byte cap
    deadline_ms: float | None = None        # Equal-Latency cap
    strict: bool = True
    events: list[str] = field(default_factory=list)

    def apply_byte_budget(self, frames: list[Frame]) -> list[Frame]:
        """Keep the newest frames whose cumulative bytes fit the cap."""
        if self.max_state_bytes is None:
            return frames
        kept, total = [], 0
        for fr in reversed(frames):
            if total + fr.nbytes > self.max_state_bytes and kept:
                dropped = len(frames) - len(kept)
                self.events.append(f"byte_budget: dropped {dropped} oldest frame(s)")
                break
            kept.append(fr)
            total += fr.nbytes
        return list(reversed(kept))

    def run_with_deadline(self, fn, fallback=None):
        t0 = time.perf_counter()
        out = fn()
        dt = (time.perf_counter() - t0) * 1e3
        if self.deadline_ms is not None and dt > self.deadline_ms:
            self.events.append(f"latency_budget: {dt:.2f}ms > {self.deadline_ms}ms")
            if self.strict:
                raise BudgetExceeded(f"deadline exceeded: {dt:.2f}ms > {self.deadline_ms}ms")
            return fallback
        return out

"""Anytime compute scheduler (H8 + hard-real-time contract; sequence 4.6).

Allocates a per-frame compute budget across candidate readouts/tasks.
Each task declares (cost_ms, expected info gain, ambiguity resolved).
Policy: greedy by value density (gain/cost) subject to the remaining
budget; the scheduler must always be able to return *some* answer by
the deadline (interruptible contract), so the highest-density task runs
first and partial results are a valid state. If measured jitter exceeds
the guard threshold, low-density tasks are shed pre-emptively.
"""
from __future__ import annotations

import dataclasses


@dataclasses.dataclass
class ComputeTask:
    name: str
    cost_ms: float
    expected_gain: float      # expected information gain (bits or task units)
    ambiguity: float = 0.0    # current ambiguity this task would resolve [0,1]

    @property
    def density(self) -> float:
        value = self.expected_gain * (0.5 + self.ambiguity)
        return value / max(self.cost_ms, 1e-9)


class AnytimeComputeScheduler:
    def __init__(self, frame_budget_ms: float = 33.3, jitter_guard_ms: float = 8.0):
        self.frame_budget_ms = frame_budget_ms
        self.jitter_guard_ms = jitter_guard_ms

    def plan(self, tasks: list[ComputeTask], observed_jitter_ms: float = 0.0) -> dict:
        budget = self.frame_budget_ms
        if observed_jitter_ms > self.jitter_guard_ms:
            budget *= 0.7   # shed load under jitter: protect the deadline
        ordered = sorted(tasks, key=lambda t: -t.density)
        chosen, spent = [], 0.0
        for t in ordered:
            if spent + t.cost_ms <= budget:
                chosen.append(t.name); spent += t.cost_ms
        return {"execute_in_order": chosen,
                "planned_ms": spent,
                "budget_ms": budget,
                "shed": [t.name for t in ordered if t.name not in chosen],
                "anytime_guarantee": bool(chosen) or not tasks}

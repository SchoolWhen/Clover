"""Transition-affordance compatibility (H12/H14; sequence 4.6).

An affordance is a learnable transition-compatibility -- not a label.
Given distributions over outcomes for (a) applying a candidate tool
transition and (b) the goal-satisfying transition family, compatibility
is the (negative) divergence between them; goal-change (Delta W_goal)
measures progress in world state, tool-change (Delta W_tool) measures
mere contact/manipulation motion. H14's active-evidence policy picks
the action maximising expected information gain per unit cost.
"""
from __future__ import annotations

import numpy as np


def _kl(p: np.ndarray, q: np.ndarray) -> float:
    p = np.asarray(p, float); q = np.asarray(q, float)
    p = p / p.sum(); q = q / (q.sum() + 1e-12) + 1e-12
    return float((p * np.log(p / q)).sum())


class TransitionAffordance:
    def compatibility(self, tool_outcome_dist: np.ndarray,
                      goal_outcome_dist: np.ndarray) -> float:
        """Higher = more compatible (negative symmetric divergence)."""
        return -0.5 * (_kl(tool_outcome_dist, goal_outcome_dist)
                       + _kl(goal_outcome_dist, tool_outcome_dist))

    def delta_w(self, before: dict[str, float], after: dict[str, float],
                goal_keys: set[str]) -> dict:
        """Split a world-state change into goal-progress vs tool-motion."""
        dg = sum(abs(after.get(k, 0.0) - before.get(k, 0.0)) for k in goal_keys)
        dt_ = sum(abs(after.get(k, 0.0) - before.get(k, 0.0))
                  for k in set(before) | set(after) if k not in goal_keys)
        return {"delta_w_goal": dg, "delta_w_tool": dt_,
                "goal_fraction": dg / max(dg + dt_, 1e-12)}


def select_evidence_action(candidates: list[dict]) -> dict | None:
    """candidates: {name, expected_gain, cost, irreversible}.
    H14/H13 policy: irreversible actions are never selected for mere
    evidence-gathering (they require a licence, not a probe)."""
    feasible = [c for c in candidates if not c.get("irreversible", False)]
    if not feasible:
        return None
    return max(feasible, key=lambda c: c["expected_gain"] / max(c["cost"], 1e-9))

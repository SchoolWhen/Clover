"""Epistemic occlusion battery — slots U9-U12 (sequence 4.5).

Streaming episodes with three trap types:
  - long_occlusion: object leaves the field of view; later queries must
    answer from memory (identity/position) or mark uncertainty;
  - swap_during_occlusion: while occluded, the object is secretly moved
    or replaced; stale beliefs must be revised on re-observation, and
    the battery penalises high-confidence false-positive write-back;
  - unknown_vs_unobserved: a region was never observed; the correct
    label is UNOBSERVED, not 'absent/empty'.
Episodes are structured event streams rendered as simple blob frames;
the scorer consumes a model's per-query epistemic labels (core protocol)
and returns per-trap accuracy plus the FP-writeback contamination rate.
"""
from __future__ import annotations

import dataclasses

import numpy as np

from ..core import EpistemicLabel

TRAPS = ("long_occlusion", "swap_during_occlusion", "unknown_vs_unobserved")


@dataclasses.dataclass
class Episode:
    trap: str
    frames: np.ndarray                     # T x H x W x 3
    queries: list[dict]                    # {t, subject, expected_label, note}


def _canvas(T=40, size=48):
    return np.zeros((T, size, size, 3), dtype=np.uint8)


def _draw(frames, t, x, y, color, r=4):
    yy, xx = np.mgrid[0:frames.shape[1], 0:frames.shape[2]]
    frames[t][(xx - x) ** 2 + (yy - y) ** 2 <= r * r] = color


def make_episode(trap: str, seed: int = 0) -> Episode:
    if trap not in TRAPS:
        raise ValueError(f"trap must be one of {TRAPS}")
    rng = np.random.default_rng(seed)
    frames = _canvas()
    color = (60, 200, 90)
    queries: list[dict] = []
    if trap == "long_occlusion":
        for t in range(15):
            _draw(frames, t, 6 + t, 24, color)
        # frames 15..34: object out of view (blank); reappears at 35
        for t in range(35, 40):
            _draw(frames, t, 41, 24, color)
        queries = [
            {"t": 20, "subject": "target", "expected_label": EpistemicLabel.UNOBSERVED,
             "note": "currently out of view: not 'absent'"},
            {"t": 36, "subject": "target", "expected_label": EpistemicLabel.OBSERVED,
             "note": "reappeared, identity from memory must be re-verified"},
        ]
    elif trap == "swap_during_occlusion":
        for t in range(15):
            _draw(frames, t, 6 + t, 24, color)
        # occluded 15..29; meanwhile moved to y=10 (secret change)
        for t in range(30, 40):
            _draw(frames, t, 21, 10, color)
        queries = [
            {"t": 31, "subject": "target.position", "expected_label": EpistemicLabel.OBSERVED,
             "note": "position is the NEW one; answering the stale position = FP write-back"},
            {"t": 31, "subject": "target.old_position_belief", "expected_label": EpistemicLabel.REFUTED,
             "note": "the pre-occlusion belief must be marked refuted after re-observation"},
        ]
    else:  # unknown_vs_unobserved
        for t in range(40):
            _draw(frames, t, 10, 10, color)   # only the top-left region is ever shown lit
        queries = [
            {"t": 39, "subject": "bottom_right_region", "expected_label": EpistemicLabel.UNOBSERVED,
             "note": "never observed: 'empty' would be an unjustified claim"},
            {"t": 39, "subject": "target", "expected_label": EpistemicLabel.OBSERVED, "note": "control query"},
        ]
    return Episode(trap, frames, queries)


def score_episode(ep: Episode, answers: dict[str, EpistemicLabel],
                  confidences: dict[str, float] | None = None) -> dict:
    """answers keyed by query subject. FP write-back = answered OBSERVED
    with confidence >= 0.8 where the expected label was not OBSERVED."""
    confidences = confidences or {}
    correct, fp_writeback, total = 0, 0, 0
    for q in ep.queries:
        total += 1
        got = answers.get(q["subject"])
        if got == q["expected_label"]:
            correct += 1
        if (got == EpistemicLabel.OBSERVED and q["expected_label"] != EpistemicLabel.OBSERVED
                and confidences.get(q["subject"], 0.0) >= 0.8):
            fp_writeback += 1
    return {"trap": ep.trap, "accuracy": correct / max(total, 1),
            "fp_writeback_count": fp_writeback, "n_queries": total}

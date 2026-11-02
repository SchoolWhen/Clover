"""Sparse event intermediate representation (H9/H2; sequence 4.6).

Converts dense frame streams into a sparse event stream: an event is
emitted when (a) appearance change exceeds theta (change event), or
(b) prediction residual exceeds theta (surprise event). Unchanged,
predicted content produces no tokens -- the IR's capacity scales with
events, not pixels. A trivial constant-velocity predictor is built in;
the residual channel is where a learned predictor would plug in.
"""
from __future__ import annotations

import dataclasses

import numpy as np


@dataclasses.dataclass
class Event:
    t: int
    kind: str                 # 'appearance_change' | 'prediction_surprise' | 'keyframe'
    magnitude: float
    location: tuple[int, int]  # centroid (y, x) of the changed region


class SparseEventIR:
    def __init__(self, theta_change: float = 12.0, theta_surprise: float = 18.0):
        self.theta_change = theta_change
        self.theta_surprise = theta_surprise

    def encode(self, frames: np.ndarray) -> dict:
        """frames: T x H x W x 3 uint8 -> {events, stats}."""
        gray = frames.astype(float).mean(axis=3)
        events: list[Event] = [Event(0, "keyframe", 0.0, (0, 0))]
        prev_velocity = np.zeros_like(gray[0])
        for t in range(1, len(frames)):
            diff = np.abs(gray[t] - gray[t - 1])
            predicted = gray[t - 1] + prev_velocity
            residual = np.abs(gray[t] - predicted)
            prev_velocity = gray[t] - gray[t - 1]
            for kind, field, theta in (("appearance_change", diff, self.theta_change),
                                       ("prediction_surprise", residual, self.theta_surprise)):
                mask = field > theta
                if mask.any():
                    ys, xs = np.nonzero(mask)
                    events.append(Event(t, kind, float(field[mask].mean()),
                                        (int(ys.mean()), int(xs.mean()))))
        dense_tokens = int(np.prod(frames.shape[:3]))
        return {"events": events,
                "stats": {"n_events": len(events), "dense_pixel_frames": dense_tokens,
                          "sparsity_ratio": len(events) / max(dense_tokens, 1)}}

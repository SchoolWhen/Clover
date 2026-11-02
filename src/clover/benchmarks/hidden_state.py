"""B15 hidden-state minimal pairs (sequence 4.5).

NOTE on naming: the task text calls this 'U15 hidden state'; per the
sequence-1.2 namespace fix, the hidden-state identifiability family is
B15 (slot U15 is the long-horizon household task). This module is B15.

Generator: pairs of synthetic videos whose pre-contact kinematics are
pixel-identical; the pair differs only in a hidden physical parameter
(eccentric mass distribution, friction-coefficient boundary, internal
cavity). The trajectories fork only after contact. A model that scores
well must use post-contact evidence -- or refuse before it exists.

Physics is analytic 1-D/2-D (slide with friction switch at a boundary;
drop with restitution). 'Rendering' draws the moving body as a filled
disc on a plain background; appearance (size/color) is decorrelated
from the hidden parameter by construction.
"""
from __future__ import annotations

import dataclasses

import numpy as np

HIDDEN_KINDS = ("friction_boundary", "restitution_cavity", "mass_eccentricity")


@dataclasses.dataclass
class MinimalPair:
    kind: str
    frames_a: np.ndarray          # T x H x W x 3 uint8
    frames_b: np.ndarray
    contact_index: int            # first frame where trajectories may differ
    hidden_a: float
    hidden_b: float
    appearance: dict              # decorrelated appearance parameters (same for both)
    outcome_a: float              # observable post-contact quantity (e.g. stop position)
    outcome_b: float


def _render(positions: np.ndarray, size: int = 48, radius: int = 4,
            color=(200, 60, 60)) -> np.ndarray:
    T = len(positions)
    frames = np.zeros((T, size, size, 3), dtype=np.uint8)
    yy, xx = np.mgrid[0:size, 0:size]
    for t, (x, y) in enumerate(positions):
        mask = (xx - x) ** 2 + (yy - y) ** 2 <= radius ** 2
        frames[t][mask] = color
    return frames


def _slide(mu_before: float, mu_after: float, v0: float = 30.0, dt: float = 0.05,
           boundary: float = 24.0, steps: int = 60, g: float = 60.0):
    """Slide on a surface whose friction coefficient changes at `boundary`."""
    x, v = 2.0, v0
    xs, contact = [], None
    for t in range(steps):
        mu = mu_before if x < boundary else mu_after
        if contact is None and x >= boundary:
            contact = t
        a = -mu * g
        v = max(v + a * dt, 0.0)
        x = x + v * dt
        xs.append(x)
        if v == 0.0 and t > 5:
            xs.extend([x] * (steps - len(xs)))
            break
    pos = np.array([[min(xx, 45.0), 24.0] for xx in xs])
    return pos, (contact if contact is not None else steps), float(xs[-1])


def make_pair(kind: str, seed: int = 0) -> MinimalPair:
    if kind not in HIDDEN_KINDS:
        raise ValueError(f"kind must be one of {HIDDEN_KINDS}")
    rng = np.random.default_rng(seed)
    # decorrelated appearance: color/size carry no information about hidden values
    color = tuple(int(c) for c in rng.integers(40, 230, size=3))
    radius = int(rng.integers(3, 6))
    appearance = {"color": color, "radius": radius}
    if kind == "friction_boundary":
        mu_a, mu_b = 0.05, 0.45     # same pre-boundary friction, different after
        pa, ca, oa = _slide(0.10, mu_a)
        pb, cb, ob = _slide(0.10, mu_b)
        contact = max(ca, cb)
        ha, hb = mu_a, mu_b
    elif kind == "restitution_cavity":
        # drop: identical fall; bounce height differs (hollow vs solid core)
        def drop(e):
            y, v, ys = 4.0, 0.0, []
            dt, g, floor = 0.05, 60.0, 42.0
            bounced = None
            for t in range(60):
                v += g * dt; y += v * dt
                if y >= floor:
                    y = floor; v = -v * e
                    if bounced is None:
                        bounced = t
                ys.append(y)
            return np.array([[24.0, yy] for yy in ys]), bounced, float(min(ys[-20:]))
        pa, ca, oa = drop(0.25); pb, cb, ob = drop(0.65)
        contact = max(ca, cb); ha, hb = 0.25, 0.65
    else:  # mass_eccentricity: slide + rotation onset after boundary differs
        pa, ca, oa = _slide(0.10, 0.20)
        pb, cb, ob = _slide(0.10, 0.20)
        # eccentric mass: after contact the body also drifts vertically (wobble)
        pb2 = pb.copy(); pb2[ca:, 1] = 24.0 + np.cumsum(np.full(60 - ca, 0.12))[: 60 - ca]
        pb = pb2
        contact = ca; ha, hb = 0.0, 1.0
    fa = _render(pa, radius=radius, color=color)
    fb = _render(pb, radius=radius, color=color)
    # enforce the minimal-pair contract: identical before contact
    assert np.array_equal(fa[:contact], fb[:contact]), "pre-contact frames must be identical"
    return MinimalPair(kind, fa, fb, contact, ha, hb, appearance, oa, ob)


def score_predictions(pair: MinimalPair, pred_a: float | None, pred_b: float | None) -> dict:
    """pred None = refusal (correct before contact evidence exists is judged
    by the caller using only pre-contact frames; here we score full-video
    predictions on ranking + refusal behaviour)."""
    if pred_a is None or pred_b is None:
        return {"ranking_correct": None, "refused": True}
    true_order = np.sign(pair.hidden_b - pair.hidden_a)
    pred_order = np.sign(pred_b - pred_a)
    return {"ranking_correct": bool(true_order == pred_order and true_order != 0),
            "refused": False}

"""Anti-shortcut perturbation suite (sequence 4.5).

Given a frame-sequence classifier `predict(frames) -> label` and labelled
sequences, measures how much of its score survives four probes:
  - static_frame: every frame replaced by the first frame;
  - time_shuffle: frame order permuted (temporal information destroyed);
  - background_only: the central object region is masked out;
  - language_only: for language-conditioned models, the caller supplies
    a no-vision baseline score; a model whose margin over it vanishes
    under the vision probes is flagged.
A large clean-vs-probe gap on static/time probes indicates temporal
shortcutting in reverse (good); a *small* drop where temporal structure
is task-essential indicates the model never used time. Interpretation
is per-task and reported, not auto-judged.
"""
from __future__ import annotations

import numpy as np


def _static(frames: np.ndarray) -> np.ndarray:
    return np.repeat(frames[:1], len(frames), axis=0)


def _shuffle(frames: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    return frames[rng.permutation(len(frames))]


def _background_only(frames: np.ndarray) -> np.ndarray:
    out = frames.copy()
    h, w = frames.shape[1], frames.shape[2]
    out[:, h // 4: 3 * h // 4, w // 4: 3 * w // 4] = 0
    return out


PROBES = {"static_frame": _static, "background_only": _background_only}


def run_suite(predict, dataset: list[tuple[np.ndarray, int]], seed: int = 0,
              language_only_score: float | None = None) -> dict:
    rng = np.random.default_rng(seed)

    def acc(fn):
        ok = sum(int(predict(fn(fr)) == y) for fr, y in dataset)
        return ok / max(len(dataset), 1)

    clean = acc(lambda fr: fr)
    results = {"clean": clean}
    for name, fn in PROBES.items():
        results[name] = acc(fn)
    results["time_shuffle"] = acc(lambda fr: _shuffle(fr, rng))
    if language_only_score is not None:
        results["language_only_baseline"] = language_only_score
        results["margin_over_language_only"] = clean - language_only_score
    results["drops"] = {k: clean - v for k, v in results.items()
                        if k not in ("clean", "drops", "language_only_baseline",
                                     "margin_over_language_only")}
    return results

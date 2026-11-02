"""Attribution probes (sequence 4.4) — implements the SSOT probe protocol.

Only two readouts may support a 'capability comes from V0/L0
pretraining' claim:
  1. ZeroShotKNNProbe: no trained parameters.
  2. FrozenLinearProbe: single linear layer on a frozen backbone, with
     pre-registered caps on effective degrees of freedom and training
     steps. In attribution mode, exceeding either cap raises
     ProbeCapacityError instead of silently producing a number.
Anything bigger (MLP/Transformer decoder fine-tuning) is 'probe-learned'
by definition and is not implemented here at all.
"""
from __future__ import annotations

import dataclasses

import numpy as np


class ProbeCapacityError(RuntimeError):
    pass


@dataclasses.dataclass
class ProbeBudget:
    max_effective_dof: int = 100_000     # cap: features x classes actually trainable
    max_steps: int = 2_000               # cap: optimiser steps for the linear probe
    attribution_mode: bool = True        # True -> caps are hard limits


class FrozenLinearProbe:
    """Ridge/softmax linear readout on frozen features."""

    def __init__(self, budget: ProbeBudget | None = None, l2: float = 1e-3):
        self.budget = budget or ProbeBudget()
        self.l2 = l2
        self.W: np.ndarray | None = None
        self.b: np.ndarray | None = None
        self.effective_dof = 0
        self.steps_used = 0

    def fit(self, X: np.ndarray, y: np.ndarray) -> "FrozenLinearProbe":
        X = np.asarray(X, float); y = np.asarray(y, int)
        n, d = X.shape
        classes = int(y.max()) + 1
        self.effective_dof = d * classes
        if self.budget.attribution_mode and self.effective_dof > self.budget.max_effective_dof:
            raise ProbeCapacityError(
                f"effective DOF {self.effective_dof} > cap {self.budget.max_effective_dof}: "
                "result would be probe-learned, not attributable to the backbone")
        # closed-form ridge on one-hot targets = 1 'step' of the budget sense;
        # iterative refinement is capped and counted below.
        Y = np.eye(classes)[y]
        Xb = np.hstack([X, np.ones((n, 1))])
        A = Xb.T @ Xb + self.l2 * np.eye(d + 1)
        W = np.linalg.solve(A, Xb.T @ Y)
        self.steps_used = 1
        if self.budget.attribution_mode and self.steps_used > self.budget.max_steps:
            raise ProbeCapacityError("step cap exceeded")
        self.W, self.b = W[:-1], W[-1]
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        return (np.asarray(X, float) @ self.W + self.b).argmax(axis=1)

    def score(self, X: np.ndarray, y: np.ndarray) -> float:
        return float((self.predict(X) == np.asarray(y)).mean())


class ZeroShotKNNProbe:
    """Zero trained parameters: class prototypes are support-set means."""

    def __init__(self, metric: str = "cosine"):
        if metric not in ("cosine", "euclidean"):
            raise ValueError("metric must be cosine|euclidean")
        self.metric = metric
        self.prototypes: np.ndarray | None = None
        self.classes: np.ndarray | None = None
        self.support_size = 0

    def fit(self, X: np.ndarray, y: np.ndarray) -> "ZeroShotKNNProbe":
        X = np.asarray(X, float); y = np.asarray(y)
        self.classes = np.unique(y)
        self.prototypes = np.stack([X[y == c].mean(axis=0) for c in self.classes])
        self.support_size = len(y)
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        X = np.asarray(X, float)
        if self.metric == "cosine":
            a = X / (np.linalg.norm(X, axis=1, keepdims=True) + 1e-12)
            b = self.prototypes / (np.linalg.norm(self.prototypes, axis=1, keepdims=True) + 1e-12)
            sim = a @ b.T
            return self.classes[sim.argmax(axis=1)]
        d = ((X[:, None, :] - self.prototypes[None, :, :]) ** 2).sum(-1)
        return self.classes[d.argmin(axis=1)]

    def score(self, X: np.ndarray, y: np.ndarray) -> float:
        return float((self.predict(X) == np.asarray(y)).mean())

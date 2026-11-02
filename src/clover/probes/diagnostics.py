"""State-sufficiency diagnostics (sequence 4.4).

Implements the three diagnostics named in representation-and-memory.md:
  1. NonMarkovianityDetector -- conditional-mutual-information leak
     I(y_{t+1}; history | z_t, a_t) > eps means z is not a sufficient state.
  2. StateAliasingAuditor -- for alias pairs (visually equivalent,
     physically different; classes A1-A6), the rate at which their latent
     distance collapses below the median same-class distance.
  3. ReversibilityProbe -- can a *linear* decoder recover held-out query
     features that were never declared at compression time? (H3 test.)
Estimators are deliberately simple (histogram CMI, linear R^2): they are
diagnostics with stated bias, not oracles.
"""
from __future__ import annotations

import numpy as np


def _discretize(x: np.ndarray, bins: int) -> np.ndarray:
    x = np.asarray(x, float)
    if x.ndim == 1:
        x = x[:, None]
    out = np.zeros(x.shape[0], dtype=int)
    mult = 1
    for j in range(x.shape[1]):
        col = x[:, j]
        edges = np.quantile(col, np.linspace(0, 1, bins + 1)[1:-1])
        out += np.digitize(col, edges) * mult
        mult *= bins
    return out


def _entropy(labels: np.ndarray) -> float:
    _, counts = np.unique(labels, return_counts=True)
    p = counts / counts.sum()
    return float(-(p * np.log2(p)).sum())


def _cmi(x: np.ndarray, y: np.ndarray, z: np.ndarray, bins: int = 4) -> float:
    """I(X;Y|Z) in bits via plug-in histogram estimator."""
    xd, yd, zd = _discretize(x, bins), _discretize(y, bins), _discretize(z, bins)
    total = 0.0
    for zv in np.unique(zd):
        m = zd == zv
        if m.sum() < 8:
            continue
        pz = m.mean()
        h_y_given_z = _entropy(yd[m])
        # H(Y|Z=z) - H(Y|X,Z=z)
        h = h_y_given_z
        for xv in np.unique(xd[m]):
            mx = m & (xd == xv)
            h -= (mx.sum() / m.sum()) * _entropy(yd[mx])
        total += pz * h
    return float(max(total, 0.0))


class NonMarkovianityDetector:
    def __init__(self, eps_bits: float = 0.05, bins: int = 4):
        self.eps = eps_bits
        self.bins = bins

    def leak(self, z: np.ndarray, a: np.ndarray, history: np.ndarray,
             y_next: np.ndarray) -> dict:
        """z, a: current state/action; history: past window features to test."""
        cond = np.hstack([np.asarray(z, float), np.asarray(a, float).reshape(len(z), -1)])
        val = _cmi(np.asarray(history, float), np.asarray(y_next, float), cond, self.bins)
        return {"cmi_bits": val, "leak_detected": bool(val > self.eps), "eps_bits": self.eps}


ALIAS_CLASSES = ("A1", "A2", "A3", "A4", "A5", "A6")


class StateAliasingAuditor:
    """pairs: list of (z_i, z_j, alias_class) with visually-equivalent but
    physically different states; reference: same-physical-state pair distances."""

    def audit(self, alias_pairs: list[tuple[np.ndarray, np.ndarray, str]],
              reference_distances: np.ndarray) -> dict:
        ref_med = float(np.median(reference_distances))
        per_class: dict[str, list[float]] = {}
        collapsed = 0
        for zi, zj, cls in alias_pairs:
            if cls not in ALIAS_CLASSES:
                raise ValueError(f"alias class must be one of {ALIAS_CLASSES}")
            d = float(np.linalg.norm(np.asarray(zi) - np.asarray(zj)))
            per_class.setdefault(cls, []).append(d)
            collapsed += int(d < ref_med)
        return {
            "reference_median_distance": ref_med,
            "collapse_rate": collapsed / max(len(alias_pairs), 1),
            "per_class_mean_distance": {k: float(np.mean(v)) for k, v in per_class.items()},
        }


class ReversibilityProbe:
    """Linear recovery of held-out query features from compressed state."""

    def __init__(self, l2: float = 1e-3):
        self.l2 = l2

    def recoverability(self, Z: np.ndarray, Q: np.ndarray) -> dict:
        Z = np.asarray(Z, float); Q = np.asarray(Q, float)
        if Q.ndim == 1:
            Q = Q[:, None]
        Zb = np.hstack([Z, np.ones((len(Z), 1))])
        W = np.linalg.solve(Zb.T @ Zb + self.l2 * np.eye(Zb.shape[1]), Zb.T @ Q)
        pred = Zb @ W
        ss_res = ((Q - pred) ** 2).sum(axis=0)
        ss_tot = ((Q - Q.mean(axis=0)) ** 2).sum(axis=0) + 1e-12
        r2 = 1.0 - ss_res / ss_tot
        return {"r2_per_feature": [float(v) for v in r2],
                "r2_mean": float(r2.mean()),
                "irrecoverable_features": [int(i) for i, v in enumerate(r2) if v < 0.5]}

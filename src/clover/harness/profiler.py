"""End-to-end wall-clock profiler (sequence 4.2).

Segments follow foundation-models-and-systems.md: the complete path
raw_bytes_input -> decode -> preprocess/resize -> visual_tokenization ->
forward -> postprocess -> actionable_output must be measured, never a
single model's forward time. Reports P50/P95/P99 and latency jitter
(max - P50 and P99 - P50), per the sequence-2.6 hard-real-time contract.
"""
from __future__ import annotations

import time
from contextlib import contextmanager

import numpy as np

SEGMENTS = ("decode", "preprocess", "tokenize", "forward", "postprocess", "output")


class EndToEndProfiler:
    def __init__(self):
        self._samples: dict[str, list[float]] = {s: [] for s in ("total",) + SEGMENTS}
        self._t0: float | None = None
        self._seg_t: float | None = None
        self._seg_name: str | None = None

    @contextmanager
    def run(self):
        """Wrap one end-to-end frame pass; use `segment()` inside."""
        self._t0 = time.perf_counter()
        try:
            yield self
        finally:
            self._samples["total"].append((time.perf_counter() - self._t0) * 1e3)
            self._t0 = None

    @contextmanager
    def segment(self, name: str):
        if name not in SEGMENTS:
            raise ValueError(f"unknown segment {name}; expected one of {SEGMENTS}")
        start = time.perf_counter()
        try:
            yield
        finally:
            self._samples[name].append((time.perf_counter() - start) * 1e3)

    def report(self) -> dict:
        out = {}
        for name, vals in self._samples.items():
            if not vals:
                continue
            a = np.asarray(vals)
            p50, p95, p99 = (float(np.percentile(a, q)) for q in (50, 95, 99))
            out[name] = {
                "n": len(vals), "p50_ms": p50, "p95_ms": p95, "p99_ms": p99,
                "max_ms": float(a.max()), "mean_ms": float(a.mean()),
                "jitter_p99_minus_p50_ms": p99 - p50,
                "jitter_max_minus_p50_ms": float(a.max()) - p50,
            }
        return out

    def deadline_miss_rate(self, deadline_ms: float) -> float:
        a = np.asarray(self._samples["total"])
        if len(a) == 0:
            return 0.0
        return float((a > deadline_ms).mean())

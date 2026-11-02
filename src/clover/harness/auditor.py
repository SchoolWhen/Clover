"""Resource auditor (sequence 4.2).

Records: model weight hashes (sha256), peak RAM (ru_maxrss), per-frame
state/memory bytes, and energy. Energy is only reported when a real
sampler exists (NVML via pynvml, or macOS powermetrics): otherwise the
field is the string 'UNAVAILABLE' -- this codebase never fabricates
Joule numbers (sequence 2.6 energy ledger discipline).
"""
from __future__ import annotations

import hashlib
import pathlib
import resource

import numpy as np


def file_sha256(path: str | pathlib.Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def peak_ram_bytes() -> int:
    # ru_maxrss is KiB on Linux, bytes on macOS.
    import sys
    v = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(v * 1024) if sys.platform.startswith("linux") else int(v)


class ResourceAuditor:
    def __init__(self):
        self.weight_hashes: dict[str, str] = {}
        self.state_bytes_per_frame: list[int] = []

    def register_weights(self, name: str, path: str | pathlib.Path) -> str:
        digest = file_sha256(path)
        self.weight_hashes[name] = digest
        return digest

    def record_state_bytes(self, nbytes: int) -> None:
        self.state_bytes_per_frame.append(int(nbytes))

    def joule_per_frame(self, power_samples_w: list[float] | None = None,
                         frame_times_s: list[float] | None = None):
        """Mean J/frame from externally sampled power, or 'UNAVAILABLE'.

        The caller must supply real power samples (NVML/powermetrics);
        without them this returns the UNAVAILABLE marker by design.
        """
        if not power_samples_w or not frame_times_s:
            return "UNAVAILABLE"
        energy_j = float(np.mean(power_samples_w)) * float(np.sum(frame_times_s))
        return energy_j / len(frame_times_s)

    def report(self) -> dict:
        sb = np.asarray(self.state_bytes_per_frame) if self.state_bytes_per_frame else np.array([0])
        return {
            "weight_hashes": dict(self.weight_hashes),
            "peak_ram_bytes": peak_ram_bytes(),
            "state_bytes_per_frame_mean": float(sb.mean()),
            "state_bytes_per_frame_max": int(sb.max()),
        }

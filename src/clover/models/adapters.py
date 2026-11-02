"""Phase A model-family adapters (sequence 4.3).

One unified loading/inference interface over the Phase A families.
Design rules from the repository's own audit discipline:
  - backends (torch/ultralytics/transformers) are OPTIONAL and lazily
    imported; on this dev machine (no GPU, no weights) load() fails
    closed with ModelUnavailable stating exactly what is missing --
    it never pretends to run a model;
  - every adapter carries its registry metadata (weights source,
    license, parameter count) from registry/artifacts.yaml records;
  - precision switching (fp16/int8) is a declared config, validated
    against what the family's official export paths support;
  - `dry_run_infer` exists ONLY to exercise the harness plumbing and
    returns outputs explicitly stamped SYNTHETIC_DRY_RUN.
"""
from __future__ import annotations

import abc
import dataclasses
from typing import Any

from ..core import Frame


class ModelUnavailable(RuntimeError):
    """Raised when a backend or weights are absent. Fail-closed by design."""


@dataclasses.dataclass
class AdapterMeta:
    family: str
    group: str
    weights_source: str
    license: str
    params: str
    output_kinds: tuple[str, ...]
    backend_module: str           # python module providing the real backend
    supports_int8: bool = False


class ModelAdapter(abc.ABC):
    meta: AdapterMeta

    def __init__(self, precision: str = "fp16", checkpoint: str | None = None):
        if precision not in ("fp32", "fp16", "int8"):
            raise ValueError("precision must be fp32|fp16|int8")
        if precision == "int8" and not self.meta.supports_int8:
            raise ValueError(f"{self.meta.family}: INT8 path not in official export record")
        self.precision = precision
        self.checkpoint = checkpoint
        self._backend = None

    def load(self):
        """Import the real backend; fail closed if unavailable."""
        import importlib
        try:
            self._backend = importlib.import_module(self.meta.backend_module)
        except ImportError as e:
            raise ModelUnavailable(
                f"{self.meta.family}: backend '{self.meta.backend_module}' not installed "
                f"and/or weights '{self.checkpoint or self.meta.weights_source}' not present. "
                f"Install the [models] extra and download official weights to run for real."
            ) from e
        return self

    @property
    def loaded(self) -> bool:
        return self._backend is not None

    def dry_run_infer(self, frames: list[Frame]) -> dict[str, Any]:
        """Plumbing test ONLY. Not a model result."""
        return {
            "family": self.meta.family,
            "mode": "SYNTHETIC_DRY_RUN",
            "n_frames": len(frames),
            "outputs": {k: None for k in self.meta.output_kinds},
            "note": "No weights were loaded; values are placeholders for harness integration tests.",
        }

    def infer(self, frames: list[Frame]) -> dict[str, Any]:
        if not self.loaded:
            raise ModelUnavailable(f"{self.meta.family}: call load() first (fails closed without backend/weights)")
        raise NotImplementedError(
            f"{self.meta.family}: backend present but the real inference binding is "
            "hardware-gated (no GPU/weights on the dev machine); see 06-evaluation evidence log."
        )


def _mk(name, **kw):
    return type(name, (ModelAdapter,), {"meta": AdapterMeta(**kw)})


YOLO26n = _mk("YOLO26n", family="YOLO26n", group="detection",
              weights_source="ultralytics yolo26n.pt (640)",
              license="AGPL-3.0 or Enterprise", params="2.4M",
              output_kinds=("boxes", "classes", "scores"),
              backend_module="ultralytics", supports_int8=True)

RFDETRNano = _mk("RFDETRNano", family="RF-DETR-Nano", group="detection",
                 weights_source="roboflow/rf-detr (Nano, 384)",
                 license="Apache-2.0 (open base)", params="30.5M",
                 output_kinds=("boxes", "classes", "scores"),
                 backend_module="rfdetr", supports_int8=True)

SAM3 = _mk("SAM3", family="SAM 3", group="promptable segmentation/tracking",
           weights_source="facebook/sam3@3c879f3",
           license="SAM License (custom)", params="~850M",
           output_kinds=("masks", "boxes", "track_ids"),
           backend_module="transformers", supports_int8=False)

CoTracker3 = _mk("CoTracker3", family="CoTracker3", group="point tracking",
                 weights_source="facebookresearch/co-tracker (CoTracker3)",
                 license="see upstream repo (registry: unknown)",
                 params="see upstream repo",
                 output_kinds=("tracks", "visibility"),
                 backend_module="cotracker", supports_int8=False)

TAPNext = _mk("TAPNext", family="TAPNext", group="point tracking",
              weights_source="google-deepmind/tapnet (TAPNext)",
              license="see upstream repo (registry: unknown)",
              params="see upstream repo",
              output_kinds=("tracks", "occlusion"),
              backend_module="tapnet", supports_int8=False)

DA3Small = _mk("DA3Small", family="Depth Anything 3 (DA3-SMALL)", group="monocular geometry",
               weights_source="depth-anything/DA3-SMALL",
               license="see HF card (family GIANT is CC BY-NC 4.0)",
               params="34.3M (official page)",
               output_kinds=("depth", "camera_pose"),
               backend_module="transformers", supports_int8=False)

VGGT = _mk("VGGT", family="VGGT", group="3D reconstruction",
           weights_source="facebookresearch/vggt",
           license="see upstream repo", params="see upstream repo",
           output_kinds=("point_map", "camera_pose", "depth"),
           backend_module="vggt", supports_int8=False)

PaddleOCRVL = _mk("PaddleOCRVL", family="PaddleOCR-VL-1.6", group="document parsing",
                  weights_source="PaddlePaddle/PaddleOCR-VL-1.6@c5630ab",
                  license="Apache-2.0", params="958.6M",
                  output_kinds=("text", "layout", "reading_order"),
                  backend_module="transformers", supports_int8=False)

DINOv3 = _mk("DINOv3", family="DINOv3", group="self-supervised representation",
             weights_source="facebookresearch/dinov3",
             license="see upstream repo", params="21M..6.716B by variant",
             output_kinds=("features",),
             backend_module="torch", supports_int8=False)

VJEPA2 = _mk("VJEPA2", family="V-JEPA 2", group="latent world model",
             weights_source="facebookresearch/jepa (V-JEPA 2)",
             license="see upstream repo", params="see upstream repo",
             output_kinds=("latent_state", "predicted_latent"),
             backend_module="torch", supports_int8=False)

PHASE_A = {c.meta.family: c for c in
           (YOLO26n, RFDETRNano, SAM3, CoTracker3, TAPNext, DA3Small, VGGT,
            PaddleOCRVL, DINOv3, VJEPA2)}

"""Unified data protocol for Clover (sequence 4.1).

Defines the contracts every module shares:
  - Frame / FrameStream: timestamped RGB frames with provenance.
  - CameraIntrinsics (V1) and MultiViewCalibration (V2).
  - Action interface (V3): embodied actions that determine future views.
  - EpistemicLabel: the eight-state epistemic label set. Every world
    assertion must carry one; OBSERVED is the only label that may be
    written to persistent memory under the asymmetric gating rule
    (01-research/representation-and-memory.md, sequence 2.3).
  - Assertion: a world claim with label, confidence, evidence refs and
    provenance (V/L accounting), i.e. the H6 proof-carrying shape.
"""
from __future__ import annotations

import enum
import time
from dataclasses import dataclass, field
from typing import Any, Iterator, Optional, Sequence

import numpy as np


class EpistemicLabel(enum.Enum):
    OBSERVED = "OBSERVED"                    # directly supported by current/replayed visual evidence
    INFERRED = "INFERRED"                    # derived from observations by a stated rule/model
    PREDICTED = "PREDICTED"                  # about a future/unobserved state, from a model
    ASSUMED = "ASSUMED"                      # completion/prior filling a gap; not evidence
    AMBIGUOUS = "AMBIGUOUS"                  # evidence supports >=2 incompatible values
    UNOBSERVED = "UNOBSERVED"                # region/state never observed (not 'absent')
    REFUTED = "REFUTED"                      # contradicted by later evidence
    MODEL_INCOMPLETE = "MODEL_INCOMPLETE"    # the state space cannot express the truth

    @property
    def persistable(self) -> bool:
        """Only OBSERVED assertions may cross the persistent-memory gate."""
        return self is EpistemicLabel.OBSERVED


class ObservationProtocol(enum.Enum):
    V0 = "V0"  # monocular RGB + temporal order
    V1 = "V1"  # RGB + camera calibration
    V2 = "V2"  # calibrated multi-camera RGB
    V3 = "V3"  # embodied active vision (actions determine future views)


class LearningProvenance(enum.Enum):
    L0 = "L0"  # vision-only self-supervision
    L1 = "L1"  # human labels / demonstrations
    L2 = "L2"  # language / teacher supervision
    L3 = "L3"  # synthetic / simulator supervision
    L4 = "L4"  # privileged state (depth/pose/force/tactile/sim state) supervision


@dataclass
class CameraIntrinsics:  # V1
    fx: float
    fy: float
    cx: float
    cy: float
    distortion: tuple[float, ...] = ()

    def matrix(self) -> np.ndarray:
        return np.array([[self.fx, 0.0, self.cx],
                         [0.0, self.fy, self.cy],
                         [0.0, 0.0, 1.0]])


@dataclass
class MultiViewCalibration:  # V2
    intrinsics: list[CameraIntrinsics]
    extrinsics: list[np.ndarray]  # 4x4 camera->world per view

    def __post_init__(self):
        if len(self.intrinsics) != len(self.extrinsics):
            raise ValueError("intrinsics/extrinsics length mismatch")


@dataclass
class Frame:
    image: np.ndarray                 # HxWx3 uint8 RGB
    timestamp_s: float
    view_id: int = 0
    intrinsics: Optional[CameraIntrinsics] = None
    source: str = "synthetic"         # provenance of the pixels themselves

    def __post_init__(self):
        if self.image.ndim != 3 or self.image.shape[2] != 3:
            raise ValueError("Frame.image must be HxWx3 RGB")

    @property
    def nbytes(self) -> int:
        return int(self.image.nbytes)


class FrameStream:
    """Ordered frames; iteration yields (frame) in timestamp order."""

    def __init__(self, frames: Sequence[Frame]):
        self._frames = sorted(frames, key=lambda f: f.timestamp_s)

    def __iter__(self) -> Iterator[Frame]:
        return iter(self._frames)

    def __len__(self) -> int:
        return len(self._frames)

    def __getitem__(self, i):
        return self._frames[i]


@dataclass
class Action:  # V3
    """An embodied action that will determine future views."""
    kind: str                          # e.g. 'move_view', 'push', 'illuminate'
    params: dict[str, Any] = field(default_factory=dict)
    irreversible: bool = False

    def requires_licence(self) -> bool:
        return self.irreversible


@dataclass
class Assertion:
    """A world claim in H6 proof-carrying shape."""
    subject: str
    predicate: str
    value: Any
    label: EpistemicLabel
    confidence: float                  # calibrated [0,1]; not evidence by itself
    evidence_refs: list[str] = field(default_factory=list)
    protocol: ObservationProtocol = ObservationProtocol.V0
    provenance: LearningProvenance = LearningProvenance.L0
    created_s: float = field(default_factory=time.time)
    depends_on: list[str] = field(default_factory=list)  # assertion ids (rollback graph)

    def __post_init__(self):
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be in [0,1]")

    @property
    def persistable(self) -> bool:
        return self.label.persistable

    @property
    def id(self) -> str:
        return f"{self.subject}|{self.predicate}|{self.created_s:.6f}"

    def downgrade(self, new_label: EpistemicLabel) -> "Assertion":
        """Return a copy with a weaker label (used by refutation cascades)."""
        return Assertion(self.subject, self.predicate, self.value, new_label,
                         self.confidence, list(self.evidence_refs), self.protocol,
                         self.provenance, self.created_s, list(self.depends_on))

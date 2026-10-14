# Classical Computer Vision and Geometry

## Why Clover must study this seriously

Before deep learning, computer vision developed explicit mathematical machinery for recovering structure and motion from images. Clover should not force a learned model to rediscover every well-understood invariant merely to appear end-to-end.

The important question is:

> **Which parts of visual world understanding already have reliable mathematical structure, and where do those methods stop?**

## Core bodies of prior work

### Projective and multi-view geometry

Provides explicit relationships among camera projection, epipolar constraints, triangulation, pose and 3D structure.

### Structure from Motion / Bundle Adjustment

Jointly estimates camera states and 3D landmarks by minimizing geometric reprojection errors.

### Visual odometry and SLAM

Maintains a spatial estimate while a camera moves through a scene. Modern SLAM systems add loop closure, relocalization and multi-map operation.

### Optical flow

Estimates image-plane motion. Flow is not itself world motion, but it is a key observable for temporal geometry.

### Tracking and filtering

Kalman filters, particle filters and data association formalize uncertainty, temporal prediction and observation updates.

### Occupancy / mapping

Explicitly distinguishes observed free space, occupied space and often unknown space — a distinction directly relevant to Clover's observability semantics.

## ORB-SLAM3

ORB-SLAM3 is an open-source real-time system supporting visual, visual-inertial and multi-map SLAM across monocular, stereo and RGB-D configurations.

Primary source:

- https://github.com/UZ-SLAMLab/ORB_SLAM3

Clover should use it as an intellectual baseline for explicit persistent geometry, not as a module to import blindly.

## RAFT

RAFT is a learned optical-flow model built around recurrent all-pairs field transforms.

Primary source:

- https://github.com/princeton-vl/RAFT

It is useful as a reminder that the boundary between 'classical variable' and 'learned estimator' is already porous: the variable can remain explicit while the estimator is learned.

## What classical approaches solve well

- camera geometry under stated assumptions;
- metric/relative structure from multiple views;
- explicit state estimation and uncertainty propagation;
- loop closure/relocalization in structured environments;
- interpretable failure modes tied to observability and geometry.

## What they do not solve by themselves

- open-ended semantic abstraction;
- general object type formation;
- high-level physical common sense;
- causal understanding;
- broad transfer from large visual experience;
- deformable/non-rigid everyday worlds at general scope;
- task relevance and language-level goals.

## Clover research tension

The modern question is not classical **or** learning. A more useful decomposition is:

> **Which invariants should be structural, which estimators should be learned, and which abstractions must emerge from experience?**

This is likely more productive than rebuilding a purely hand-engineered or purely learned stack.

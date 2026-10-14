# Research Question

> **How can a machine understand the real world through vision alone?**

This is Clover's highest SSOT.

## Machine

The target is an embodied computational system that can maintain and use knowledge across time, not a one-shot visual classifier.

## Understand

`Understand` is intentionally not defined as a single benchmark score. The current technical working definition requires a world representation that supports persistent state, identity, space/time structure, dynamics, causal and counterfactual reasoning, uncertainty, memory, revision, generalization and downstream decision usefulness.

See [`what-is-understanding.md`](what-is-understanding.md).

## Real world

The target domain contains:

- persistent entities independent of the camera view;
- occlusion and incomplete observation;
- continuous time and changing relations;
- physical constraints and interactions;
- novel objects and environments;
- consequences of action.

Synthetic environments can isolate mechanisms, but the scientific target is not confined to synthetic data.

## Vision alone

The phrase must be made explicit in each experiment. Clover currently distinguishes:

- **V0 — strict monocular vision:** RGB frames + temporal order/timestamps only;
- **V1 — calibrated vision:** V0 + known camera intrinsics;
- **V2 — multi-camera vision:** multiple calibrated RGB streams;
- **V3 — embodied active vision:** the agent may move to acquire new visual evidence while sensory evidence remains visual.

Depth, LiDAR, tactile, force, IMU, privileged simulator state and ground-truth object identity are not silently counted as vision.

## Research consequence

The question is stable. CPU/GPU preference, field formulations, explicit state, latent learning, object-centric models, geometry, Transformers and current Clover code are all candidate answers or tools, not part of the question itself.

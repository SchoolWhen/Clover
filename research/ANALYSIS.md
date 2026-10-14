# Stage 2 — Analysis
## Method Reports and Mechanism Decomposition

Last updated: 2026-10-14

**Status:** DEFINED, NOT YET THE PRIMARY ACTIVE STAGE.

Analysis begins after Stage 1 Research has collected sufficiently broad material. Its job is to understand individual methods deeply rather than adding more names to the inventory.

## One method = one small report

For every important method, use this template:

```text
Method / paper:
Version / date:
Research family:
Primary paper:
Official project:
Official code:
Evidence level:

Problem solved:
Input observations:
Training data / supervision:
V0–V3 observation protocol:
L0–L4 learning provenance:

Core representation:
Core mechanism:
Learning objective:
Temporal mechanism:
Memory mechanism:
Geometry assumptions:
Object/entity assumptions:
Physics assumptions:
Causal assumptions:
Action interface:

Datasets:
Benchmarks:
Reported result:
Reproduced result:

Strengths:
Weaknesses:
Confounds:
Failure modes:
Compute / scale requirements:
Reproducibility:

What this method actually demonstrates:
What it does NOT demonstrate:
Which Clover question it constrains:
What experiment would distinguish it from competing methods:
```

## Analysis dimensions

Every report should try to answer the same dimensions so later Synthesis is possible:

1. **Representation** — pixels, features, point maps, slots, tokens, graphs, latent state, explicit state, simulator, policy hidden state, etc.
2. **Time** — frame-local, short history, streaming, recurrent, persistent, episodic, future prediction.
3. **Space** — 2D, projective 3D, metric 3D, 4D, topological, semantic, relational.
4. **Identity** — visible association, persistent entity, object permanence, re-identification.
5. **Physics** — none, qualitative, relational, quantitative, hard constraint, learned dynamics.
6. **Causality** — correlation, prediction, action-conditioned transition, intervention, counterfactual.
7. **Uncertainty** — confidence only, calibrated uncertainty, belief state, explicit unknown / refusal.
8. **Memory** — context window, recurrent state, external store, episodic retrieval, map, replay.
9. **Action** — no action, downstream policy, action conditioning, planner, joint world/action model.
10. **Generalization** — object, scene, camera, dynamics, embodiment, real-world shift.
11. **Learning evidence** — image/video only, labels, language, robot actions, proprioception, simulation privilege.
12. **Evaluation** — what the benchmark truly measures and what shortcuts remain.

## Rule

Do not write “better” or “worse” without specifying the dimension, protocol and evidence.

Do not import the method into Clover during Analysis. Analysis produces understanding, not architecture.

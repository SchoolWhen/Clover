# Stage 1 — Research Frontier Watch
## Current Primary Sources Worth Deeper Analysis

Last updated: 2026-10-14

This file is a thin companion to [`RESEARCH.md`](RESEARCH.md).

`RESEARCH.md` is the stable broad inventory. This file tracks current primary sources that materially expand or challenge that inventory and should later receive Stage 2 method reports.

A frontier entry is **not** a Clover design decision.

---

## 1. Executability is a separate world-model capability

### RoboWM-Bench

Primary paper: https://arxiv.org/abs/2604.19092

Research role:

```text
video-world-model realism
vs
physical plausibility
vs
robot-executable behavior
```

Why it matters:

RoboWM-Bench converts generated human/robot manipulation behavior into embodied action sequences and tests whether execution actually completes the task. It reports recurring failures in spatial reasoning, contact prediction and deformation even when generated videos appear plausible.

What it does **not** establish:

- that video generation is the right world representation;
- that one particular explicit/latent state solves executability;
- generality beyond the evaluated manipulation settings.

Stage-2 question:

> What information is missing when visual prediction is perceptually strong but action extraction remains physically invalid?

---

### RoboTrustBench

Primary paper: https://arxiv.org/abs/2606.01600

Research role:

Tests video world models under:

- normal instructions;
- constraint-sensitive cases;
- counterfactual cases;
- adversarial/unsafe instructions.

Why it matters:

It separates ordinary visual coherence from constraint reasoning, counterfactual grounding, physical interaction and safe refusal.

Stage-2 question:

> Should world-model evaluation include refusal, impossibility and constraint awareness rather than only next-video quality?

---

## 2. Contact and deformable-object dynamics may require their own state

### WorldContact

Primary paper: https://arxiv.org/abs/2609.19600

Research role:

Contact-centric world modeling for deformable-object manipulation.

Why it matters:

Rigid-object geometry is not enough for bags, cloth and other deformables. Contact topology, deformation and action-response dynamics can dominate task success.

The reported system predicts deformable-object dynamics at larger time steps than its source numerical simulator and uses generated trajectories to expand policy-training data.

What it does **not** establish:

- that contact-centric state is a universal world representation;
- that RGB alone uniquely identifies contact force/material parameters;
- that simulator-trained contact dynamics generalize without qualification to arbitrary real materials.

Stage-2 question:

> Which contact/deformation state is visually identifiable, which must be inferred through action, and which requires non-visual evidence?

---

## 3. Functional correctness can diverge from visual fidelity

### Video2World

Primary paper: https://arxiv.org/abs/2610.04432

Research role:

Autonomous video-to-simulation reconstruction from embodied videos.

Evaluation dimensions include:

- geometric fidelity;
- dynamic fidelity;
- functional correctness.

Why it matters:

The benchmark reports that worlds which look better can function worse. This reinforces a central distinction for Clover:

```text
visual resemblance
≠
correct physical state
≠
executable world model
```

Stage-2 question:

> What representation makes a reconstructed world functionally equivalent rather than merely visually similar?

---

## 4. Individual capabilities do not automatically compose into a working robot

### RobotWorld

Primary paper: https://arxiv.org/abs/2610.10409

Research role:

Benchmarking multimodal agents across 84 physical tasks spanning manipulation, mobile manipulation, locomotion, driving and aerial control.

Why it matters:

The reported agents can construct useful perception/control subroutines such as segmentation, camera calibration, spatial estimation and dynamics computation, but still fail to compose them reliably into successful behavior. Reported failures include losing task-relevant object state, ineffective recovery and incorrect completion judgments.

Stage-2 question:

> Is the missing capability a better component, a persistent task/world state, a better interface contract, or closed-loop verification?

This source is particularly relevant to Stage 3 systems-level Synthesis because it warns that strong isolated capabilities can fail through composition.

---

## 5. Persistent semantic maps are a world-memory baseline

### PerSeM

Primary paper: https://arxiv.org/abs/2609.19542

Research role:

Training-free persistent semantic memory for long-horizon open-vocabulary mapping.

Why it matters:

It associates frame-wise semantics with persistent world-space voxels and uses history-preserving refinement, replay and verification. This makes it a useful comparator for the question:

```text
frame-wise semantics
vs
persistent semantic world memory
```

What it does **not** establish:

- general object permanence under arbitrary world change;
- causal or physical understanding;
- that voxel memory is the best general-purpose representation.

Stage-2 question:

> How much long-horizon stability can be obtained by persistent aggregation alone before a richer world model is needed?

---

## 6. Amodal perception must be separated from ordinary tracking

### TAO-Amodal

Primary paper: https://arxiv.org/abs/2312.12433

Research role:

A benchmark for tracking objects through partial/full occlusion and out-of-frame states with amodal annotations.

Why it remains relevant:

Modern video segmentation/tracking can maintain visible masks, but world understanding requires reasoning about entities when the visible support disappears.

Stage-2 question:

> How should we distinguish visible tracking, amodal completion, re-identification and true object permanence?

TAO-Amodal is older than the current 2026 frontier but remains a useful diagnostic anchor.

---

## 7. Video-to-control should be studied as an interface problem

### From Video to Control: A Survey of Learning Manipulation Interfaces from Temporal Visual Data

Primary paper: https://arxiv.org/abs/2604.04974

Research role:

Organizes video-to-control approaches into:

- direct video→action policies;
- latent-action interfaces;
- explicit visual interfaces.

Why it matters:

The difficult problem may not be “video representation” alone but the interface between video-derived world information and closed-loop robot control.

Stage-2 question:

> Which world information must be exposed to control for verification, correction and safe execution?

---

## 8. Social/multi-agent reasoning is another real-world dimension

### SocialGrid

Primary paper: https://arxiv.org/abs/2604.16022

Research role:

Embodied multi-agent planning and social reasoning benchmark.

Why it matters:

The physical world contains other agents whose future behavior may depend on hidden goals, communication, deception and interaction history. World understanding may eventually require maintaining beliefs about agent state in addition to object/geometry state.

What it does **not** establish:

- that social reasoning must be part of Clover's first visual-world algorithm;
- that language-agent game environments directly transfer to real robotics.

Stage-1 implication:

Keep **multi-agent / social world modeling** visible in the inventory so the project does not silently equate “real world” with only rigid objects and static environments.

---

## 9. Immediate frontier-analysis queue

High-priority future Stage-2 reports from this watch:

```text
RoboWM-Bench
RoboTrustBench
WorldContact
Video2World
RobotWorld
PerSeM
TAO-Amodal
Video-to-Control survey
```

Suggested comparison axes:

```text
visual fidelity
geometry fidelity
dynamics fidelity
contact correctness
persistent state
functional correctness
executability
constraint awareness
counterfactual behavior
recovery
uncertainty / refusal
```

---

## 10. Frontier-watch rule

Add a source here when it is current and materially changes what Stage 1 should know.

Promote stable concepts into [`RESEARCH.md`](RESEARCH.md) and deeper source maps once their role is clear.

Do not promote a frontier mechanism directly into Clover Innovation.

# R-B — Geometry: What Is Already Solved?

Last updated: 2026-10-14  
Status: **BACKGROUND_RESEARCH**

## 1. Fundamental question

> **Which parts of real-world visual understanding already have strong geometric formulations, and where do learned representations add genuinely new capability?**

Clover should not force a neural architecture to rediscover mature projective geometry if an explicit solution is already stronger, more interpretable and more reliable. Conversely, classical geometry should not be treated as sufficient for semantics, persistence, physics or causality.

## 2. Canonical foundations

### Multiple View Geometry

- Hartley & Zisserman: https://www.robots.ox.ac.uk/~vgg/hzbook/

Key structures include:

```text
camera projection
homography
epipolar geometry
triangulation
multi-view reconstruction
bundle adjustment
```

These define exact geometric relationships independent of current deep-learning fashion.

### Probabilistic state estimation

- Probabilistic Robotics: https://mitpress.mit.edu/9780262201629/probabilistic-robotics/

Geometry in a robot is not only reconstruction; it also involves state uncertainty, data association and sequential estimation.

## 3. Classical explicit baselines

### ORB-SLAM3

- Paper: https://arxiv.org/abs/2007.11898
- Code: https://github.com/UZ-SLAMLab/ORB_SLAM3

**Demonstrates:** explicit camera trajectory, mapping, relocalization and multi-map reuse can be highly effective with engineered geometric structure.

**Does not establish:** semantic object identity, open-world category understanding, intuitive physics, hidden-state persistence or causality.

### RAFT

- Paper: https://arxiv.org/abs/2003.12039
- Code: https://github.com/princeton-vl/RAFT

**Demonstrates:** dense temporal correspondence / optical flow is a strong motion primitive.

**Does not establish:** that a tracked pixel correspondence is a persistent entity or causal object.

## 4. Learned geometry changes the boundary

### DUSt3R

- Paper: https://arxiv.org/abs/2312.14132

DUSt3R predicts point maps directly from image pairs and reduces dependence on a long classical correspondence→pose→triangulation pipeline.

**Research significance:** the useful question is no longer `classical geometry or learning?`; it is where explicit constraints and learned priors should divide labor.

### VGGT

- Paper: https://arxiv.org/abs/2503.11651
- Code: https://github.com/facebookresearch/vggt

VGGT predicts multiple geometric quantities from images, including camera parameters, depth, point maps and tracks.

**Demonstrates:** a foundation model can serve as a broad learned geometry estimator rather than a task-specific depth or pose model.

**Does not establish:** persistent world memory, physical dynamics, causal state or action usefulness by itself.

### VGGT-Ω

- Paper: https://arxiv.org/abs/2605.15195
- Project: https://vggt-omega.github.io/
- Code: https://github.com/facebookresearch/vggt-omega

VGGT-Ω extends the learned-geometry direction toward static and dynamic scene reconstruction and representation useful to downstream embodied systems.

**Key hypothesis to test:** reconstruction may be a scalable proxy for spatial understanding.

**Counter-question:** how far does reconstruction remain correct or useful once an object leaves the field of view, undergoes state change, or requires causal reasoning?

## 5. Geometry is not world understanding

A strong geometry system may correctly estimate:

```text
camera pose
depth
point correspondence
surface / point-map structure
motion
```

while still failing:

```text
same object after long occlusion?
object still exists outside view?
what is unknown versus empty?
what physical property caused an outcome?
what will an intervention change?
which geometry matters to a task?
```

This boundary must be measured rather than assumed.

## 6. Geometry and visible entities

### SAM 3.1

- Official overview: https://ai.meta.com/blog/segment-anything-model-3/
- Code: https://github.com/facebookresearch/sam3
- Release notes: https://github.com/facebookresearch/sam3/blob/main/RELEASE_SAM3p1.md

SAM 3.1 improves efficient multi-object video detection/segmentation/tracking through shared-memory object multiplexing.

**Use for Clover:** a strong contemporary baseline for visible entity tracking.

**Important limit:**

```text
visible tracking
≠ object permanence
≠ persistent world state
```

A system that tracks an object while visible has not yet shown it can represent that object correctly after it leaves the field of view.

## 7. Geometry under missing views

### Vantage

- Paper: https://arxiv.org/abs/2610.11810
- Code: https://github.com/q1xiangchen/Vantage

Vantage plans a question-relevant view and then uses geometry-grounded evidence to improve multi-view spatial reasoning.

**Demonstrates:** failure can come from missing evidence, not just weak reasoning; viewpoint selection changes the observable geometry.

**Clover implication:** geometry and active perception should be linked in V3 experiments rather than treated as independent modules.

## 8. Operational research questions

1. Which geometric quantities are reliable enough to remain explicit?
2. Which quantities are better estimated by learned geometry foundation models?
3. Does learned geometry improve robustness mainly through priors, or does it encode task-relevant world structure absent from classical pipelines?
4. How should dynamic objects and camera motion be separated?
5. Can geometric state persist through long occlusion without a separate memory mechanism?
6. Does metric 3D reconstruction improve planning, generalization or recovery compared with a strong direct policy?
7. When geometry is uncertain, how should that uncertainty propagate into downstream decisions?

## 9. Best baseline matrix

| Family | Baseline | Isolates |
|---|---|---|
| Classical geometry | ORB-SLAM3 | explicit camera/map state |
| Dense motion | RAFT | short-term correspondence |
| Learned pairwise geometry | DUSt3R | learned point-map estimation |
| Geometry foundation model | VGGT | broad learned spatial state |
| Dynamic learned geometry | VGGT-Ω | dynamic reconstruction / global spatial representation |
| Visible entity tracking | SAM 3.1 | detection/segmentation/tracking while visible |

## 10. Discriminating experiments

### T-B-01 — Geometry-only capability boundary

Use the same V0/V1 video and compare:

```text
ORB-SLAM3
RAFT
VGGT / VGGT-Ω
```

Queries:

```text
Where is the camera?
What moved?
Which points correspond?
What is behind / in front?
Same object after occlusion?
Still exists outside view?
What changed causally?
```

The purpose is to identify exactly where geometry stops being sufficient.

### T-B-02 — Reconstruction vs persistence

Evaluate a reconstruction model before, during and after long out-of-FOV intervals using PersistBench-style ground truth.

Measure:

- geometric continuity;
- object identity continuity;
- appearance preservation;
- stale hallucinated geometry;
- uncertainty when evidence is absent.

### T-B-03 — Geometry value for action

Matched comparison:

```text
strong policy
vs
same policy + explicit / learned geometry state
```

Measure unseen-scene success, planning cost, collision/reachability error and recovery.

### T-B-04 — Camera shift

Hold world/task constant while changing intrinsics, viewpoint and trajectory.

This separates a genuinely geometric representation from camera-specific visual shortcuts.

## 11. Kill conditions

A geometry pathway should not be preserved as a privileged world representation if it adds no measurable benefit to:

- spatial correctness;
- generalization under camera shift;
- long-horizon persistence;
- planning/search cost;
- recovery;
- task success.

Likewise, a learned geometry model should not replace exact classical structure merely because it is newer if it is less reliable or less observable in the relevant regime.

## 12. Clover landing

Current conclusion:

> **Geometry is a solved-to-strongly-solved subproblem in several regimes, not a solved world-understanding problem. The next Clover representation must treat geometry as prior art to beat or reuse, then demonstrate what additional state is required for identity, memory, physics, causality and action.**

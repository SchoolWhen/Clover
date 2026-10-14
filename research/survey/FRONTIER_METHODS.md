# Frontier Methods

Last updated: 2026-10-14

This document compares method families that materially constrain the Clover research question.

> **How can a machine understand the real world through vision alone, then use that understanding to decide and act?**

The purpose is not to assemble a stack. Each route is treated as a competing explanation of what internal state is sufficient.

For the source/claim/landing map, see [`SOURCE_MAP.md`](SOURCE_MAP.md). For the broader synthesis, see [`BACKGROUND_RESEARCH.md`](BACKGROUND_RESEARCH.md).

---

## 1. Classical geometry and state estimation

**ORB-SLAM3**  
Paper: https://arxiv.org/abs/2007.11898  
Code: https://github.com/UZ-SLAMLab/ORB_SLAM3

Explicit pose/map/trajectory state demonstrates that some physical-world variables already have strong mathematical formulations. It provides localization, relocalization and map reuse, but not open-world semantics, general object permanence or causal reasoning.

**RAFT**  
Paper: https://arxiv.org/abs/2003.12039  
Code: https://github.com/princeton-vl/RAFT

Dense temporal correspondence baseline. Flow is valuable motion evidence, but flow is not object identity, persistence or causality.

**Research contradiction:** which variables should remain explicit geometric invariants, and which should be learned?

---

## 2. Static self-supervised visual representation

**DINOv3**  
Research: https://ai.meta.com/research/publications/dinov3/  
Paper: https://arxiv.org/abs/2508.10104  
Code: https://github.com/facebookresearch/dinov3

DINOv3 is now the primary current static SSL comparator. It scales label-free image learning to very large data/model regimes and produces strong frozen dense features for detection, segmentation, depth and tracking-related tasks.

**DINOv2**  
Paper: https://arxiv.org/abs/2304.07193  
Code: https://github.com/facebookresearch/dinov2

Retained as a historical/currently reproducible predecessor, but no longer the only or strongest static SSL reference in the Survey.

**Research contradiction:** if an image backbone already contains strong dense object/part/depth information, which world-understanding capabilities require persistent temporal state rather than better static representation?

---

## 3. Predictive video representation

**V-JEPA 2**  
Research: https://ai.meta.com/research/publications/v-jepa-2-self-supervised-video-models-enable-understanding-prediction-and-planning/  
Paper: https://arxiv.org/abs/2506.09985  
Code: https://github.com/facebookresearch/vjepa2

Connects internet-scale action-free video learning to motion/anticipation and action-conditioned robot planning. It is a major competitor to an explicitly factorized Clover world state.

**V-JEPA 2.1**  
Paper: https://arxiv.org/abs/2603.14482

Dense predictive learning and deep self-supervision produce spatially structured, semantically coherent and temporally consistent features, while also reporting downstream robot improvements.

**Interpreting Physics in Video World Models**  
Meta: https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/

Reports that speed, acceleration and motion direction emerge inside large video encoders; direction behaves as a high-dimensional population code. This is direct counter-evidence to assuming all useful physical variables must be compact explicit state.

**Research contradiction:**

```text
explicit factorized state
vs
distributed predictive latent
vs
hybrid/identifiable latent
```

---

## 4. Learned geometry / spatial reconstruction

**DUSt3R** — https://arxiv.org/abs/2312.14132  
Learned point-map geometry bridges classical pipelines and foundation models.

**VGGT**  
Paper: https://arxiv.org/abs/2503.11651  
Code: https://github.com/facebookresearch/vggt

Predicts cameras, depth, point maps and tracks from one or more images.

**VGGT-Ω**  
Paper: https://arxiv.org/abs/2605.15195  
Project: https://vggt-omega.github.io/  
Code: https://github.com/facebookresearch/vggt-omega

Extends learned geometry to larger-scale static/dynamic reconstruction. Its learned registers also improve VLA and language-alignment results, motivating the hypothesis that reconstruction can be a scalable proxy for spatial understanding.

**World Labs Atlas** — https://www.worldlabs.ai/blog/atlas  
Atlas combines reconstruction with generation and space-time simulation, but a generated hidden surface is not the same epistemic object as an observed surface.

**Research contradiction:**

```text
reconstruction quality
vs
persistent world state
vs
action-useful state
```

---

## 5. Object-centric representation and visible entity tracking

**Slot Attention** — https://proceedings.neurips.cc/paper/2020/hash/8511df98c02ab60aea1b2356c013bc0f-Abstract.html  
Object-like exchangeable slots provide a compositional representation route.

**PLATO** — https://www.nature.com/articles/s41562-022-01394-8  
Object-centric inductive structure has shown value for learning intuitive-physics expectations in controlled settings.

**SAM 3 / SAM 3.1**  
Research: https://ai.meta.com/research/publications/sam-3-segment-anything-with-concepts/  
Code: https://github.com/facebookresearch/sam3  
SAM 3.1 notes: https://github.com/facebookresearch/sam3/blob/main/RELEASE_SAM3p1.md

SAM 3.1 is the current open-vocabulary image/video detection, segmentation and tracking baseline in this Survey. It supersedes SAM 2 as the primary contemporary comparator for visible entity persistence, while SAM 2 remains historically important.

**Critical distinction:**

```text
visible tracking ≠ object permanence
```

---

## 6. Persistent visual and episodic memory

**PersistBench**  
Paper: https://arxiv.org/abs/2609.20819  
Project/code: https://guangzhaohe.com/persistbench

Uses 360° reference video to measure object permanence, motion continuity and appearance preservation after objects leave normal view. Current 4D/world models show strong short-term perception but degraded memory outside the field of view.

**S-EMBER**  
Meta: https://ai.meta.com/research/publications/s-ember-a-large-scale-benchmark-for-streaming-egocentric-memory-retrieval/  
Paper: https://arxiv.org/abs/2607.02689

Streaming egocentric retrieval benchmark. It separates semantic answering from precise temporal grounding and shows that more model scale/frame density does not automatically solve grounded recall.

**VISTA** — https://arxiv.org/abs/2610.02200  
Separates model weights from lossless visual memory, active retrieval and evidence organization, making the memory harness itself an explicit research variable.

**Research contradiction:**

```text
long context / recurrent latent
vs
persistent world state
vs
raw/selective evidence replay
vs
episodic memory
```

Evidence Replay remains one Clover hypothesis, not the default answer.

---

## 7. Intuitive physics and physical consistency

**IntPhys 2**  
Research: https://ai.meta.com/research/publications/intphys-2-benchmarking-intuitive-physics-understanding-in-complex-synthetic-environments/  
Code: https://github.com/facebookresearch/IntPhys2

Measures permanence, immutability, spatiotemporal continuity and solidity through controlled violation-of-expectation tests.

**MVP / Minimal Video Pairs**  
Research: https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/

Tests whether physical-reasoning scores survive minimally changed paired videos with identical questions and opposite answers.

**Principia** — https://arxiv.org/abs/2609.04200  
Tests relational Newtonian consistency in real controlled scenes using calibration-independent relationships between objects.

**Interpreting Physics in Video World Models**  
https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/

Shows that learned video features can encode physical variables without a compact symbolic state.

**Research contradiction:** visual plausibility, learned physical regularity, quantitative physical state and action-relevant physical knowledge are not the same capability.

---

## 8. Causal and counterfactual reasoning

**CausalVQA**  
https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/

Real-video questions probe counterfactual, hypothetical, anticipation and planning reasoning.

**General identifiability and achievability for CRL**  
https://proceedings.mlr.press/v238/varici24a.html

**Multi-node interventional CRL**  
https://proceedings.mlr.press/v236/bing24a

These causal-representation results are important background because causal variables can be underdetermined from observational data unless additional assumptions or interventional environments provide identifiability.

**Research contradiction:**

```text
predictive correlation
vs
intervention-sensitive dependency
vs
counterfactual world model
```

Historical Counter-Witness First Causality remains a candidate hypothesis to test against these baselines.

---

## 9. Active perception / information-seeking vision

**Bajcsy, Active Perception** — https://ieeexplore.ieee.org/abstract/document/5968  
Foundational view that perception includes selecting sensing actions.

**Vantage**  
Paper: https://arxiv.org/abs/2610.11810  
Code: https://github.com/q1xiangchen/Vantage

View planning + geometry-grounded evidence gathering + VLM reasoning. Shows evidence acquisition can be a bottleneck independent of raw model scale.

**SpatialCORE**  
Paper: https://arxiv.org/abs/2609.38716  
Code: https://github.com/rafiibnsultan/SpatialCORE

Spatial-grounding confidence can guide learning/compute; confidence is not automatically truth.

**Research contradiction:** can a system represent missing information well enough to decide what visual action should be taken next?

---

## 10. Generative spatial/world models

**World Labs Atlas** — https://www.worldlabs.ai/blog/atlas  
**World-model taxonomy** — https://www.worldlabs.ai/blog/taxonomy-of-world-models

Atlas unifies reconstruction, generation and space-time simulation in a spatially grounded multimodal architecture.

**Cosmos 3**  
Project: https://research.nvidia.com/labs/cosmos-lab/cosmos3/  
Report: https://arxiv.org/abs/2606.02800  
Code: https://github.com/nvidia/cosmos

Cosmos 3 jointly handles language, image, video, audio and action and explicitly merges VLM, generator, simulator and world-action roles.

**EVEWorld** — https://arxiv.org/abs/2610.03374  
Targets visually plausible but process-inconsistent rollout behavior.

**DR-WM / From Pixels to Executable Physics** — https://arxiv.org/abs/2610.17630  
Connects visual geometry with action-response-derived terrain/contact priors.

**Critical distinction:**

```text
plausible completion ≠ observed fact ≠ evidence-supported belief
```

---

## 11. VLA / embodied reasoning / robot foundation systems

**RT-2** — https://arxiv.org/abs/2307.15818  
Action-first route transferring web vision/language knowledge into robot actions.

**OpenVLA**  
Paper: https://arxiv.org/abs/2406.09246  
Code: https://github.com/openvla/openvla

Primary open VLA comparator.

**π0.5**  
Paper: https://arxiv.org/abs/2504.16054  
Project: https://www.pi.website/blog/pi05

Strong open-world-generalization counterexample to assuming an explicit exposed world state is obviously required.

**Gemini Robotics ER 2**  
Overview: https://deepmind.google/models/gemini-robotics/embodied-reasoning/  
Model card: https://deepmind.google/models/model-cards/gemini-robotics-er-2/

High-level robot reasoning route built on a large multimodal VLM; motor execution is delegated to a lower-level VLA. Important confound: physical reasoning can mix visual evidence with language/world priors.

**Gemini Robotics 2** — https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/  
Whole-body VLA/control reference.

**Figure Helix 2.5** — https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization — `OFFICIAL_REPORTED_RESULT`  
Reports whole-body long-horizon zero-shot behavior in 30 unseen homes and a controlled human-experience pretraining ablation.

**Skild S1** — https://www.skild.ai/blogs/s1 — `OFFICIAL_REPORTED_RESULT`  
Reports in-context robot task learning from video demonstrations and long-horizon unseen behavior.

**Skild general-purpose robot brain** — https://skild.ai/blogs/building-the-general-purpose-robotic-brain  
Embodiment-invariant/omni-bodied foundation-policy thesis.

**Core falsifier for explicit-worldview research:**

```text
strong matched policy
vs
strong matched policy + persistent world representation
```

The world representation must improve action, recovery, generalization, sample efficiency, planning/search cost or unjustified-action rate.

---

## 12. World-action models

**World-Action Models survey**  
Paper: https://arxiv.org/abs/2609.16074  
Resource page: https://rcl-robotics.github.io/Awesome-World-Action-Models

WAMs couple future world prediction with executable action generation.

**ReWAM** — https://arxiv.org/abs/2609.38163  
Reconstruction fidelity and generic perceptual features alone do not guarantee policy-useful state.

**HWAM** — https://arxiv.org/abs/2610.12026  
Reference action, executed motion and realized state must be distinguished.

**Being-H0.7** — https://arxiv.org/abs/2605.00078  
Future-aware latent reasoning without future-pixel rollout at inference.

**Being-M0.7** — https://arxiv.org/abs/2610.11283  
Large human video/motion pretraining before humanoid adaptation.

**H-WM** — https://arxiv.org/abs/2602.11291  
Combines high-level logical transitions with low-level visual transitions.

**Research contradiction:** which future information is sufficient for control: pixels, geometry, latent state, explicit task state or some hybrid?

---

## 13. Identifiable / hybrid state

**Identifiable World Models** — https://arxiv.org/abs/2610.07028

Promising middle route: retain powerful distributed representation while learning coordinates that align with identifiable world variables.

This is important because the strongest answer may not be “explicit or latent,” but a layered or partially identifiable representation.

---

## 14. Model-based control

**DreamerV3** — https://arxiv.org/abs/2301.04104  
**TD-MPC2** — https://arxiv.org/abs/2310.16828

Important counterexamples to the belief that useful planning state must be human-interpretable.

---

## 15. State/action-grounded world-model evaluation

**RoboPhys-3D** — https://arxiv.org/abs/2608.28718

Evaluates world-model outputs through pixel fidelity, 3D geometry, state-level understanding and task-level completeness. It is especially relevant because state/execution-grounded metrics expose failures that perceptual or generic VLM judgments may miss.

---

## 16. Sparse / event-like computation

**Motion-aware Event Suppression** — https://arxiv.org/abs/2602.23204

Shows that sparse visual change can reduce downstream compute. The Clover lesson is to test sparse visual evidence as a representation/computation hypothesis without making event-camera hardware a scientific requirement.

---

## Provisional constraints from the frontier

Current evidence supports constraints, not a final architecture:

1. scalable open-world abstraction strongly benefits from learned representation;
2. explicit geometry remains valuable where variables and invariants are well-defined;
3. static SSL is stronger than older Clover baselines assumed — DINOv3 is now a key comparator;
4. predictive video representations learn substantial distributed physical structure;
5. reconstruction gives strong spatial state but does not automatically provide persistence, causality or action utility;
6. visible segmentation/tracking is not object permanence;
7. streaming/persistent memory is an independent capability, not simply “more context”;
8. plausible generation is not authoritative truth;
9. strong policies can act without exposed explicit state;
10. interaction adds controllability and interventional evidence;
11. active perception can create evidence unavailable in the current view;
12. physical variables can be distributed rather than compactly factorized;
13. control-oriented future prediction is increasingly moving toward task-relevant latent/state prediction rather than full pixel rollout;
14. state/process consistency and execution consequences matter more than video quality alone;
15. any explicit Clover worldview must prove measurable value for action, recovery, generalization or efficiency.

The next Clover architecture must be derived from baseline + battery + failure-map evidence, not attachment to an older mechanism.

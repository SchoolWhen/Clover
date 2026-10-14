# Frontier Methods

Last updated: 2026-10-14

This document surveys method families that materially constrain the Clover research question.

The goal is not to collect every new model. The goal is to understand the strongest competing answers to:

> **What internal machinery is sufficient for a machine to understand the real world through vision and use that understanding for action?**

## 1. Classical geometry, estimation and persistent state

### ORB-SLAM3
- Paper: https://arxiv.org/abs/2007.11898
- Code: https://github.com/UZ-SLAMLab/ORB_SLAM3

Explicit pose/map/trajectory state shows that some parts of “world state” are already well formalized. It gives observability, map reuse and localization but not open-world semantics, physical causality or broad learned abstraction.

### RAFT
- Paper: https://arxiv.org/abs/2003.12039
- Code: https://github.com/princeton-vl/RAFT

Dense correspondence is useful, but flow is not identity, permanence or causality.

**Clover question:** which geometric variables should remain explicit invariants, and which should be learned?

## 2. Static self-supervised representation

### DINOv2
- Paper: https://arxiv.org/abs/2304.07193
- Code: https://github.com/facebookresearch/dinov2

Demonstrates scalable label-free visual representation and emergent object/part structure. Static features alone do not provide persistent identity, dynamics or long-horizon world memory.

## 3. Predictive video representation

### V-JEPA 2
- Paper: https://arxiv.org/abs/2506.09985
- Official: https://ai.meta.com/vjepa/
- Code: https://github.com/facebookresearch/vjepa2

Connects large-scale action-free video learning to motion/anticipation and then to action-conditioned robot planning. It is a major competing answer to the idea that world variables must first be explicitly factorized.

Open questions: persistent identity, long occlusion, distributed vs explicit physics, and what robot interaction adds beyond passive video.

### V-JEPA 2.1
- Paper: https://arxiv.org/abs/2603.14482
- Code: https://github.com/facebookresearch/vjepa2

Adds dense predictive learning and deeper self-supervision, strengthening the possibility that semantics, dense space and time can coexist in one learned representation.

### Interpreting Physics in Video World Models
- Paper: https://arxiv.org/abs/2602.07050
- Official: https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/

Reports a “Physics Emergence Zone” and distributed/high-dimensional encoding of some physical variables. This is direct counter-evidence to assuming that useful physical state must always be a compact explicit vector.

## 4. Learned geometry / spatial intelligence

### DUSt3R
- Paper: https://arxiv.org/abs/2312.14132

Learned point-map geometry collapses parts of a classical multi-stage reconstruction pipeline into a trainable system.

### VGGT
- Paper: https://arxiv.org/abs/2503.11651
- Code: https://github.com/facebookresearch/vggt

Predicts camera parameters, depth, point maps and tracks from one or more images. It is a strong learned explicit-spatial substrate.

### VGGT-Ω
- Paper: https://arxiv.org/abs/2605.15195
- Project: https://vggt-omega.github.io/
- Code: https://github.com/facebookresearch/vggt-omega

Pushes learned geometry toward larger-scale and dynamic reconstruction.

### World Labs Atlas
- Official: https://www.worldlabs.ai/blog/atlas

Combines reconstruction, generation, simulation and robotics workflows in a spatial world model. Crucial Clover distinction: plausible hidden completion is not the same thing as observed/justified world state.

## 5. Object-centric / persistent entities

### Slot Attention
- Paper: https://arxiv.org/abs/2006.15055

Formalizes object-like slots and the hypothesis that entity decomposition supports compositional reasoning.

### SAM 2
- Paper: https://arxiv.org/abs/2408.00714
- Code: https://github.com/facebookresearch/sam2

Strong video segmentation/mask tracking baseline. Clover should not attribute ordinary visible entity continuity to a world model if a perception foundation model already provides it.

## 6. Visual memory / evidence organization

### VISTA
- Paper: https://arxiv.org/abs/2610.02200

Separates base model from lossless visual memory, active retrieval and evidence reorganization. This makes “memory architecture vs learned world state” a first-class research question.

## 7. Active evidence selection / spatial reasoning

### Vantage
- Paper: https://arxiv.org/abs/2610.11810
- Code: https://github.com/q1xiangchen/Vantage

Training-free view planning + geometry-grounded evidence gathering + VLM reasoning. Shows that evidence/view selection can be a bottleneck independent of base-model capacity.

### SpatialCORE
- Paper: https://arxiv.org/abs/2609.38716
- Code: https://github.com/rafiibnsultan/SpatialCORE

Uses confidence in generated spatial grounding as a training signal. Clover lesson: confidence can guide learning/compute, but confidence is not truth.

## 8. Vision-language-action / world-action models

### RT-2
- Paper: https://arxiv.org/abs/2307.15818
- PMLR: https://proceedings.mlr.press/v229/zitkovich23a.html

Action-first route: web-scale vision/language knowledge transferred into action tokens.

### OpenVLA
- Paper: https://arxiv.org/abs/2406.09246
- Code: https://github.com/openvla/openvla

Important open VLA baseline and eventual comparator.

### π0.5
- Paper: https://arxiv.org/abs/2504.16054
- Official: https://www.pi.website/blog/pi05

Open-world robot generalization from heterogeneous multimodal/robot supervision. Strong falsifier for claims that explicit persistent world state is obviously necessary.

### ReWAM
- Paper: https://arxiv.org/abs/2609.38163

Argues that neither reconstruction fidelity nor generic perceptual features alone guarantee a policy-useful representation. Introduces action-grounded representation shaping.

### HWAM
- Paper: https://arxiv.org/abs/2610.12026

Separates reference action from realized physical state by jointly modeling state/action. Critical lesson: intended action, executed action and observed consequence are distinct.

### Being-H0.7
- Paper: https://arxiv.org/abs/2605.00078

Uses latent future-aware reasoning with a training-only future branch and no future-pixel rollout at inference.

### Being-M0.7
- Paper: https://arxiv.org/abs/2610.11283

Uses >10,000 hours of mixed human video/motion data to learn visual-motion priors before robot adaptation. Shows a route from non-robot experience to humanoid world-action priors.

### H-WM
- Paper: https://arxiv.org/abs/2602.11291

Combines high-level logical transitions and low-level visual transitions to address long-horizon drift vs perceptual grounding.

### World-Action Models survey
- Paper: https://arxiv.org/abs/2609.16074
- Project: https://rcl-robotics.github.io/Awesome-World-Action-Models

Useful current taxonomy for representations, transitions, action interfaces, data modalities and long-horizon challenges.

## 9. Embodied reasoning / high-level robot brain

### Gemini Robotics ER 2
- Model card: https://deepmind.google/models/model-cards/gemini-robotics-er-2/
- Product: https://deepmind.google/models/gemini-robotics/embodied-reasoning/

Official high-level robot reasoning route built on a large multimodal VLM. Central confound: physical behavior may combine visual evidence with extensive language/world priors.

## 10. Robot foundation models / experience scaling

### Figure Helix 2.5
- Official: https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization
- Evidence: `OFFICIAL_REPORTED_RESULT`

Reported whole-body long-horizon behavior in 30 unseen homes, with substantial gain from human-experience pretraining.

### Skild S1
- Official: https://skild.ai/blogs/s1
- Evidence: `OFFICIAL_REPORTED_RESULT`

Reported in-context robot task learning from video demonstration and unseen long-horizon tasks.

### Physical Self-Play
- Official: https://skild.ai/blogs/physical-self-play

Suggests physical intelligence may need observation + imitation + interaction + self-generated experience.

## 11. Generative physical world models

### Cosmos 3
- Paper: https://arxiv.org/abs/2606.02800
- Code: https://github.com/nvidia/cosmos
- Official: https://www.nvidia.com/en-us/ai/cosmos/

Represents the world-foundation-model direction where reasoning, generation and action interfaces increasingly converge.

### EVEWorld
- Paper: https://arxiv.org/abs/2610.03374

Targets “model laziness”: visually plausible world-model rollouts that fail to model consistent object evolution. This is important evidence that video fidelity and physical process correctness differ.

### DR-WM / From Pixels to Executable Physics
- Paper: https://arxiv.org/abs/2610.17630

Combines visual geometry with terrain/contact priors calibrated from action-response data to predict robot consequences. Strong evidence that some action-relevant physical state may require interaction, not appearance alone.

## 12. Identifiable / hybrid representation

### Identifiable World Models
- Paper: https://arxiv.org/abs/2610.07028

Suggests a middle route: powerful distributed world representation + small identifiable coordinate layer, rather than fully explicit vs fully latent.

## 13. Sparse / event-based computation

### Motion-aware Event Suppression
- Paper: https://arxiv.org/abs/2602.23204

Useful lesson: physical visual change is sparse and computation may exploit that. This does not imply Clover must depend on event-camera hardware.

## 14. Model-based control

### DreamerV3
- Paper: https://arxiv.org/abs/2301.04104

### TD-MPC2
- Paper: https://arxiv.org/abs/2310.16828

These are important counterexamples to the belief that a world representation must be human-interpretable to be useful for control.

## 15. Provisional constraints from the frontier

The current evidence supports constraints, not a final architecture:

1. scalable open-world abstraction needs learned representation;
2. explicit geometry remains valuable where variables/invariants are well-defined;
3. predictive video representations can learn substantial physical structure;
4. reconstruction is powerful for space but not automatically for causality/action;
5. plausible generation is not authoritative truth;
6. direct policies/robot foundation models can be strong without exposed explicit state;
7. interaction contributes controllability/action-consequence information;
8. memory/evidence organization can change capability without changing weights;
9. physical variables can be distributed rather than compactly factorized;
10. future-world prediction for control is increasingly moving into compact latent state rather than pixel rollout;
11. process/state consistency and execution consequences matter more than visual quality alone;
12. any explicit Clover worldview must prove measurable benefit for action, recovery, generalization or efficiency.

The next Clover architecture should be derived from these contradictions rather than attachment to an older mechanism.

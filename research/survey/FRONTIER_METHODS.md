# Frontier Methods

Last updated: 2026-10-14

This document surveys method families that materially constrain the Clover research question.

> **What internal machinery is sufficient for a machine to understand the real world through vision and use that understanding for action?**

## Classical geometry and state estimation

**ORB-SLAM3** — https://arxiv.org/abs/2007.11898 · https://github.com/UZ-SLAMLab/ORB_SLAM3  
Explicit pose/map/trajectory state shows that some world variables are already well formalized. It gives observability, map reuse and localization but not open-world semantics or causality.

**RAFT** — https://arxiv.org/abs/2003.12039 · https://github.com/princeton-vl/RAFT  
Dense temporal correspondence baseline; flow is not identity, permanence or causality.

Research question: which geometric variables should remain explicit invariants, and which should be learned?

## Static self-supervised representation

**DINOv2** — https://arxiv.org/abs/2304.07193 · https://github.com/facebookresearch/dinov2  
Scalable label-free visual features and emergent object/part structure. Static features alone do not solve persistent identity, dynamics or long-horizon memory.

## Predictive video representation

**V-JEPA 2** — https://arxiv.org/abs/2506.09985 · https://ai.meta.com/vjepa/ · https://github.com/facebookresearch/vjepa2  
Connects large-scale action-free video learning to motion/anticipation and action-conditioned robot planning. Major competitor to explicit factorized world state.

**V-JEPA 2.1** — https://arxiv.org/abs/2603.14482  
Dense predictive learning and deep self-supervision strengthen the possibility of one distributed representation covering semantics, dense space and time.

**Interpreting Physics in Video World Models** — https://arxiv.org/abs/2602.07050 · https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/  
Reports distributed/high-dimensional physical representations. Direct counter-evidence to assuming all useful physical variables must be compact explicit state.

## Learned geometry / spatial intelligence

**DUSt3R** — https://arxiv.org/abs/2312.14132  
Learned point-map geometry bridges classical pipelines and foundation models.

**VGGT** — https://arxiv.org/abs/2503.11651 · https://github.com/facebookresearch/vggt  
Predicts cameras, depth, point maps and tracks from one or more images.

**VGGT-Ω** — https://arxiv.org/abs/2605.15195 · https://vggt-omega.github.io/ · https://github.com/facebookresearch/vggt-omega  
Extends learned geometry toward larger-scale and dynamic reconstruction.

**World Labs Atlas** — https://www.worldlabs.ai/blog/atlas  
Combines reconstruction, generation, simulation and robotics workflows. Critical distinction: plausible hidden completion is not evidence-supported truth.

## Object-centric / entity representation

**Slot Attention** — https://arxiv.org/abs/2006.15055  
Formalizes object-like slots and compositional entity representation.

**SAM 2** — https://arxiv.org/abs/2408.00714 · https://github.com/facebookresearch/sam2  
Strong visible video entity/segmentation baseline. Clover should not call ordinary mask persistence “world understanding” if perception models already provide it.

## Memory and evidence organization

**VISTA** — https://arxiv.org/abs/2610.02200  
Separates base-model weights from lossless visual memory, active retrieval and evidence organization. Makes memory architecture itself a first-class research variable.

## Active evidence / spatial reasoning

**Vantage** — https://arxiv.org/abs/2610.11810 · https://github.com/q1xiangchen/Vantage  
View planning + geometry-grounded evidence gathering + VLM reasoning. Shows evidence selection can be a bottleneck independent of model size.

**SpatialCORE** — https://arxiv.org/abs/2609.38716 · https://github.com/rafiibnsultan/SpatialCORE  
Uses spatial-grounding confidence in post-training. Lesson: confidence can guide learning/compute; it is not automatically truth.

## Vision-language-action / world-action models

**RT-2** — https://arxiv.org/abs/2307.15818  
Action-first alternative: transfer web vision/language knowledge into robot actions.

**OpenVLA** — https://arxiv.org/abs/2406.09246 · https://github.com/openvla/openvla  
Important open VLA comparator.

**π0.5** — https://arxiv.org/abs/2504.16054 · https://www.pi.website/blog/pi05  
Open-world robot generalization with heterogeneous multimodal/robot training. Serious falsifier for “explicit persistent world state is obviously necessary.”

**ReWAM** — https://arxiv.org/abs/2609.38163  
Reconstruction fidelity and generic perceptual features alone do not guarantee policy-useful state; action-grounded representation shaping matters.

**HWAM** — https://arxiv.org/abs/2610.12026  
Reference action, executed motion and realized state must be distinguished.

**Being-H0.7** — https://arxiv.org/abs/2605.00078  
Latent future-aware reasoning with a training-only future branch; no future-pixel rollout at inference.

**Being-M0.7** — https://arxiv.org/abs/2610.11283  
Uses large mixed human video/motion data to learn future-aware visual-motion priors before humanoid adaptation.

**H-WM** — https://arxiv.org/abs/2602.11291  
Combines high-level logical transitions and low-level visual transitions for long-horizon planning/grounding.

**World-Action Models survey** — https://arxiv.org/abs/2609.16074 · https://rcl-robotics.github.io/Awesome-World-Action-Models  
Current taxonomy for representation, transitions, action interfaces, data and evaluation.

## Embodied reasoning / robot-brain systems

**Gemini Robotics ER 2** — https://deepmind.google/models/model-cards/gemini-robotics-er-2/ · https://deepmind.google/models/gemini-robotics/embodied-reasoning/  
High-level robot reasoning route built on a large multimodal VLM. Key confound: physical reasoning may combine visual evidence with extensive language/world priors.

## Robot foundation models / experience scaling

**Figure Helix 2.5** — https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization — `OFFICIAL_REPORTED_RESULT`  
Reported whole-body long-horizon behavior in unseen homes with large gains from human-experience pretraining.

**Skild S1** — https://skild.ai/blogs/s1 — `OFFICIAL_REPORTED_RESULT`  
Reported in-context robot task learning from video demonstrations and long-horizon unseen behavior.

**Physical Self-Play** — https://skild.ai/blogs/physical-self-play  
Suggests physical intelligence may require passive observation + imitation + interaction + self-generated experience.

## Generative physical world models

**Cosmos 3** — https://arxiv.org/abs/2606.02800 · https://github.com/nvidia/cosmos  
World-foundation-model direction where reasoning, generation and action interfaces converge.

**EVEWorld** — https://arxiv.org/abs/2610.03374  
Targets “model laziness”: visually plausible rollouts with weak instance/evolution consistency. Evidence that visual fidelity and physical process correctness differ.

**DR-WM / From Pixels to Executable Physics** — https://arxiv.org/abs/2610.17630  
Combines visual geometry with terrain/contact priors calibrated from action-response data. Suggests some action-relevant physical state requires interaction, not appearance alone.

## Identifiable / hybrid state

**Identifiable World Models** — https://arxiv.org/abs/2610.07028  
Promising middle route: powerful distributed representation + identifiable explicit coordinates.

## Sparse / event-like computation

**Motion-aware Event Suppression** — https://arxiv.org/abs/2602.23204  
Shows high-rate sparse visual processing and downstream compute reduction. Clover lesson: exploit informative visual change, without necessarily requiring event-camera hardware.

## Model-based control

**DreamerV3** — https://arxiv.org/abs/2301.04104  
**TD-MPC2** — https://arxiv.org/abs/2310.16828

Important counterexamples to the belief that a world state must be human-interpretable to be useful for control.

## Provisional constraints from the frontier

Current evidence supports constraints, not a final architecture:

1. scalable open-world abstraction needs learned representation;
2. explicit geometry remains valuable where variables/invariants are well-defined;
3. predictive video representations learn substantial physical structure;
4. reconstruction gives strong spatial state but not automatically causality/action;
5. plausible generation is not authoritative truth;
6. strong policies can act without exposed explicit state;
7. interaction adds controllability/action-consequence information;
8. memory/evidence organization can change capability without changing weights;
9. physical variables can be distributed rather than compactly factorized;
10. control-oriented future prediction is increasingly moving into compact latent state rather than pixel rollout;
11. state/process consistency and execution consequences matter more than video quality alone;
12. any explicit Clover worldview must prove measurable value for action, recovery, generalization or efficiency.

The next Clover architecture should be derived from these contradictions, not attachment to an older mechanism.

# Clover Research Map

Last updated: 2026-10-14

This map exists to answer one question:

> **What does prior research already tell us about how a machine might understand the real world through vision alone?**

The map is not a shopping list of modules to add to Clover. Each area is studied for the problem it solves, the representation it assumes, the evidence it has produced, and the questions it leaves unresolved.

## Research axes

We track every research route along the same axes:

1. **Representation** — what internal state exists?
2. **Learning signal** — reconstruction, prediction, contrast, imitation, language, interaction, control reward, or hand-designed geometry?
3. **Time** — frames, tracks, recurrent memory, latent dynamics, or persistent world state?
4. **Space** — image-plane, metric 3D, topological, object-centric, field, or distributed latent?
5. **Physics** — explicit constraints, learned regularities, generative prediction, or none?
6. **Uncertainty / observability** — can the method distinguish unknown, unobserved and false?
7. **Memory** — what persists when evidence leaves the field of view?
8. **Causality** — correlation, prediction, intervention, or counterfactual support?
9. **Action connection** — is world knowledge useful for planning and control?
10. **Generalization** — new object, scene, composition, embodiment or task?
11. **Compute structure** — dense, sparse, recurrent, graph, geometric optimization, transformer, diffusion, etc.?
12. **Evidence strength** — paper benchmark, public reproduction, real robot study, or vendor report?

## Major research families

| Family | Main question | Representative work | Primary Clover tension |
|---|---|---|---|
| [Classical vision & geometry](classical-vision.md) | What can be recovered from vision with explicit geometry? | SfM, SLAM, ORB-SLAM3, optical flow | Which variables should not need to be relearned? |
| [Learned visual representations](learned-visual-representations.md) | What useful structure emerges without labels? | DINOv2 | How much world structure exists in static visual features? |
| [Video world models](video-world-models.md) | Can prediction from passive video produce physical understanding? | V-JEPA 2 / 2.1 | Is a distributed latent sufficient for world understanding? |
| [Spatial intelligence](spatial-intelligence.md) | Can learned reconstruction become a scalable spatial substrate? | VGGT, VGGT-Ω, DUSt3R, Atlas | Is reconstruction a proxy for understanding or only geometry? |
| [Object-centric representation](object-centric-representation.md) | Should the world decompose into persistent entities? | Slot Attention, segmentation/tracking | Are objects primitive or emergent? |
| [Embodied reasoning](embodied-reasoning.md) | Can multimodal reasoning serve as a high-level robot brain? | Gemini Robotics ER 2 | Is apparent physical reasoning visual or language-mediated? |
| [Vision-language-action](vla.md) | How far can direct perception-to-action scale? | RT-2, OpenVLA, π0.5 | Is an explicit world state necessary for strong behavior? |
| [Robot foundation models](robot-foundation-models.md) | Can broad physical experience produce general robot capability? | Helix 2.5, Skild S1 | Does large-scale pretraining make explicit world models unnecessary? |
| [Model-based robotics](model-based-robotics.md) | How should belief, state, planning and control interact? | POMDP, MPC, belief-space planning | Which old robotics distinctions should Clover preserve? |
| [Active perception](active-perception.md) | What should a robot look at next? | active vision, belief-space exploration | Can uncertainty become a visual information-seeking action? |
| [Causality](causality.md) | What must be represented to understand interventions? | causal reasoning, action-conditioned models | Prediction is not yet causality. |
| [Lifelong learning](lifelong-learning.md) | How does a world model revise itself over time? | continual learning, LIBERO | How can the robot grow without freezing or catastrophic forgetting? |

## A useful non-answer

The current map does **not** support a conclusion such as:

- explicit state > latent state;
- field > objects;
- prediction > reconstruction;
- VLA > modular robot brain;
- CPU > GPU;
- Transformer > non-Transformer.

Those are empirical research questions.

## Current high-value tensions

### 1. Explicit vs distributed world representation

Meta's mechanistic work on video world models reports that some physical variables become linearly accessible with depth while others, such as motion direction, can be encoded by distributed high-dimensional population codes. This is direct counter-pressure against assuming that useful world variables must always be compact explicit state.

### 2. Prediction vs reconstruction

V-JEPA 2 emphasizes predictive latent learning; VGGT/VGGT-Ω emphasize geometric reconstruction; Atlas combines reconstruction, generation and simulation. We do not yet know which objective yields the best substrate for persistent robot world understanding.

### 3. Observation vs interaction

V-JEPA 2 learns broadly from action-free video and adds a comparatively small amount of robot interaction for action-conditioned planning. Robot foundation models increasingly combine human video, simulation, teleoperation and robot data. The unresolved question is what interaction contributes that observation cannot.

### 4. World state vs direct policy

Gemini Robotics ER 2 explicitly separates high-level embodied reasoning from lower-level VLA control, while π0.5 and other VLA systems demonstrate long-horizon generalization with much more end-to-end learning. Clover must eventually show whether an explicit persistent worldview provides measurable value beyond a strong reactive or hierarchical policy.

## Source policy

Prefer, in order:

1. primary paper / model card;
2. official project page or repository;
3. official benchmark code;
4. company technical report for closed systems;
5. third-party summary only when primary evidence is unavailable.

Closed-system claims are recorded as **reported results**, not independently reproduced facts.

## Next step

Continue filling this map before committing to a new Clover representation. Reproduction and benchmark comparison come later, after the research landscape is sufficiently clear.

# Frontier Methods

Last updated: 2026-10-14

This document surveys method families that materially constrain the Clover research question.

The goal is not to collect every new model. The goal is to understand the strongest competing answers to:

> **What internal machinery is sufficient for a machine to understand the real world through vision and use that understanding for action?**

---

# 1. Classical geometry, estimation and persistent state

## 1.1 Multi-view geometry / SfM / SLAM

### Core idea

Recover geometric state explicitly from image formation constraints.

Typical state:

```text
camera pose
landmarks / map
depth / geometry
trajectory
uncertainty
```

Representative system:

### ORB-SLAM3

- **Type:** explicit geometric state estimation.
- **Paper:** https://arxiv.org/abs/2007.11898
- **Code:** https://github.com/UZ-SLAMLab/ORB_SLAM3

Why it matters:

- demonstrates that camera motion, map structure and long-term localization do not need to be treated as vague latent semantics;
- makes observability and estimation error explicit;
- provides a mature notion of persistent state.

What it does not solve:

- open-world object semantics;
- causal physical understanding;
- general task abstraction;
- broad learning from visual experience.

### Clover question

> Which geometric variables are already sufficiently well-defined that relearning them end-to-end is unnecessary, and which variables require learned representation?

---

## 1.2 Optical flow / motion correspondence

### RAFT

- **Paper:** https://arxiv.org/abs/2003.12039
- **Code:** https://github.com/princeton-vl/RAFT

Core contribution:

- learned dense correspondence across frames;
- iterative refinement over a correlation volume.

Clover relevance:

Motion correspondence is a useful diagnostic primitive, but:

```text
flow
≠
identity
≠
object permanence
≠
causality
```

A world model must explain when correspondence is sufficient and when it fails.

---

# 2. Self-supervised static visual representation

## 2.1 DINOv2

- **Paper:** https://arxiv.org/abs/2304.07193
- **Code:** https://github.com/facebookresearch/dinov2

### Core idea

Learn general-purpose visual features without task labels at internet scale.

### Why it matters

DINO-like representations demonstrate that:

- object/part structure can emerge without explicit category supervision;
- a reusable visual representation can support many downstream tasks;
- human-designed descriptors are not the only path to invariance.

### Limitation for the Clover question

Static representation alone does not specify:

- persistent identity across long occlusion;
- dynamics;
- intervention;
- causal state transition;
- long-term world memory.

### Research tension

> Is a strong static visual foundation sufficient when combined with memory/dynamics, or does the representation itself need to be temporal from the start?

---

# 3. Predictive video representation and world models

## 3.1 V-JEPA 2

- **Paper:** https://arxiv.org/abs/2506.09985
- **Official page:** https://ai.meta.com/vjepa/
- **Code:** https://github.com/facebookresearch/vjepa2

### Core idea

Learn video representations by predicting in latent embedding space rather than generating raw future pixels.

The paper reports:

- more than one million hours of internet video/image pretraining;
- strong motion understanding and anticipation;
- an action-conditioned post-training stage using less than 62 hours of DROID robot video;
- zero-shot image-goal planning on Franka arms in unseen lab environments.

### Why this is central to Clover

V-JEPA 2 is one of the clearest modern attempts to connect:

```text
observation
→ world representation
→ future prediction
→ robot planning
```

without requiring full future video generation.

### What remains unresolved

- whether a persistent world state exists internally;
- whether identity survives long occlusion without context replay;
- whether physical state variables are explicit or distributed;
- whether planning gains come from "understanding" or from a useful predictive embedding;
- what the interaction data adds beyond passive video.

---

## 3.2 V-JEPA 2.1

- **Paper:** https://arxiv.org/abs/2603.14482
- **Code:** https://github.com/facebookresearch/vjepa2

### Core additions

The paper emphasizes:

- dense predictive loss;
- deep self-supervision across intermediate layers;
- image/video tokenizers;
- dense spatial-temporal features;
- temporal consistency.

### Clover relevance

V-JEPA 2.1 strengthens the case that one representation can combine:

```text
global semantics
+
dense spatial grounding
+
temporal structure
```

This is direct competition for any claim that Clover needs a completely separate explicit primitive hierarchy to obtain the same abilities.

---

## 3.3 Interpreting Physics in Video World Models

- **Paper:** https://arxiv.org/abs/2602.07050
- **Official Meta page:** https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/

### Key result

The study reports a "Physics Emergence Zone" in intermediate video-model layers and finds:

- speed and acceleration can become linearly accessible;
- motion direction emerges later;
- direction may be encoded as a high-dimensional population code rather than a small set of compact physical variables.

### Why this is scientifically dangerous and useful for Clover

Historical Clover often preferred explicit machine-readable world variables.

This paper gives a competing possibility:

> **A distributed representation can encode physically useful structure without factorizing it into classical variables.**

Clover must therefore prove the benefit of explicit state rather than assuming it.

---

# 4. Learned geometry / spatial intelligence

## 4.1 DUSt3R

- **Paper:** https://arxiv.org/abs/2312.14132

### Core idea

Move beyond the traditional hand-built multi-view pipeline by predicting dense 3D structure directly from image pairs.

### Clover relevance

DUSt3R is a bridge between:

```text
explicit geometry
and
learned representation
```

It weakens the false dichotomy:

```text
classical geometry
vs
neural latent
```

Modern systems can learn to emit explicit geometric structure.

---

## 4.2 VGGT

- **Paper:** https://arxiv.org/abs/2503.11651
- **CVPR page:** https://openaccess.thecvf.com/content/CVPR2025/html/Wang_VGGT_Visual_Geometry_Grounded_Transformer_CVPR_2025_paper.html
- **Code:** https://github.com/facebookresearch/vggt

### Core output

From one or more images, VGGT predicts:

- camera parameters;
- depth;
- point maps;
- 3D tracks.

### Research question

> If large-scale learned reconstruction already provides a unified spatial substrate, what additional state does world understanding require?

A plausible answer is:

```text
geometry
+
identity
+
observability
+
dynamics
+
causality
+
memory
```

But this must be demonstrated, not assumed.

---

## 4.3 VGGT-Ω

- **Paper:** https://arxiv.org/abs/2605.15195
- **Project:** https://vggt-omega.github.io/
- **Code:** https://github.com/facebookresearch/vggt-omega

### Why it matters

The 2026 line pushes geometry foundation models toward:

- larger-scale reconstruction;
- dynamic scenes;
- reusable geometric representation;
- stronger downstream alignment.

### Clover tension

> Could reconstruction be a scalable proxy objective for spatial understanding?

If yes, old Clover field-based geometry may be unnecessary or only useful as a higher-level state layer.

---

## 4.4 World Labs Atlas

- **Official report:** https://www.worldlabs.ai/blog/atlas

### Core idea

Atlas is described as an omni world model operating on text, images, video and 3D with a shared spatial context.

Reported capabilities include:

- camera-controlled generation;
- sparse-view reconstruction;
- explicit 3D output;
- space-time simulation;
- real-to-sim robotics workflows.

### Scientific importance

Atlas represents a competing thesis:

> A sufficiently strong generative spatial model may combine reconstruction, completion and simulation in one learned system.

### Important caution

When input views do not determine hidden parts of the world, Atlas can **imagine** plausible completion.

For Clover:

```text
plausible completion
≠
observed truth
```

This is a central observability problem.

---

# 5. Object-centric and persistent entity representations

## 5.1 Slot Attention

- **Paper:** https://arxiv.org/abs/2006.15055

### Core idea

Map visual features into a set of exchangeable object-like slots.

### Why it matters

It formalizes a long-running hypothesis:

> the world may become easier to reason about if representation decomposes into entity-like units.

### Clover question

Historical CSP/entity ideas must be compared with object-centric learning:

- are objects primitive?
- emergent?
- task-conditioned?
- continuous fields with object-like attractors?
- distributed latent clusters?

The answer is open.

---

## 5.2 SAM 2 as a perception baseline

- **Paper:** https://arxiv.org/abs/2408.00714
- **Code:** https://github.com/facebookresearch/sam2

SAM 2 is not a world model.

Its relevance is narrower:

> How strong can modern video segmentation / mask tracking become before any world-model machinery is added?

Clover should not claim identity continuity if a perception foundation model already provides the same observable behavior.

---

# 6. Memory and visual reasoning harnesses

## 6.1 VISTA

- **Paper:** https://arxiv.org/abs/2610.02200

### Core idea

Keep past visual observations in lossless form and let the underlying multimodal model retrieve/reorganize them during long-horizon reasoning.

The paper reports a major gain on ARC-AGI-3 using the same underlying multimodal model.

### Why it matters

VISTA separates:

```text
model weights
from
visual memory / retrieval / evidence organization
```

This is directly relevant to Clover's historical distinction between:

- current world state;
- raw visual evidence;
- replay/revision.

### Open question

> Should a robot world model compress old visual evidence into state, keep lossless evidence, or maintain both with different retention rules?

---

# 7. Spatial reasoning with explicit evidence organization

## 7.1 Vantage

- **Paper:** https://arxiv.org/abs/2610.11810
- **Code:** https://github.com/q1xiangchen/Vantage

### Core idea

A training-free multi-view spatial reasoning framework:

```text
question
→ view planning
→ geometry-grounded evidence gathering
→ VLM reasoning
```

### Clover lesson

Sometimes the bottleneck is not model capacity.

It can be:

> **which evidence is made available, from which viewpoint, and how it is organized.**

This supports active perception and evidence-management research.

---

## 7.2 SpatialCORE

- **Paper:** https://arxiv.org/abs/2609.38716
- **Code:** https://github.com/rafiibnsultan/SpatialCORE

### Core idea

Use the model's confidence in generated spatial grounding as part of the post-training reward.

### Clover lesson

This is evidence that confidence can guide learning.

It does **not** imply:

```text
confidence = truth
```

For Clover, uncertainty/confidence can help allocate compute or prioritize re-observation without becoming world authority by itself.

---

# 8. World-action and VLA methods

## 8.1 RT-2

- **Paper:** https://arxiv.org/abs/2307.15818
- **PMLR:** https://proceedings.mlr.press/v229/zitkovich23a.html

### Core idea

Encode robot actions as tokens and transfer web-scale vision-language knowledge into robotic control.

### Clover challenge

RT-2 introduced a strong alternative to explicit world modeling:

```text
vision + language
→ action
```

If direct action policies continue to improve, Clover must show what persistent world representation adds.

---

## 8.2 OpenVLA

- **Paper:** https://arxiv.org/abs/2406.09246
- **Code:** https://github.com/openvla/openvla

### Why it matters

OpenVLA is an important open baseline for:

- VLA architecture;
- action tokenization / prediction;
- robot data scaling;
- LIBERO-style evaluation.

For Clover it is an eventual comparator, not a component to import.

---

## 8.3 π0.5

- **Paper:** https://arxiv.org/abs/2504.16054
- **Official page:** https://www.pi.website/blog/pi05

### Core idea

Open-world generalization using heterogeneous training across:

- visual observations;
- language;
- semantic subtasks;
- object-related information;
- robot actions.

### Clover question

> Can broad multimodal and robot pretraining produce enough implicit world understanding that a separate persistent world state becomes unnecessary?

This is a critical falsifier for explicit-worldview claims.

---

## 8.4 ReWAM

- **Paper:** https://arxiv.org/abs/2609.38163

### Core finding

The paper argues that:

- reconstruction fidelity alone does not guarantee useful control representation;
- pretrained perceptual features alone do not guarantee useful control representation.

ReWAM introduces:

- Feature Calibration;
- Temporal Representation Bottleneck;
- Action-Grounded Representation Shaping.

### Why this matters

This directly reframes the Clover question:

> The best world representation may not be the one that reconstructs reality most faithfully. It may be the one that preserves the state variables most relevant to controllable change.

---

## 8.5 HWAM

- **Paper:** https://arxiv.org/abs/2610.12026

### Core contradiction

A high-level action command is not identical to the action physically realized by the robot.

HWAM explicitly predicts post-execution body state together with reference action.

### Clover lesson

Any robot brain needs to distinguish:

```text
intended action
executed action
observed consequence
```

This is broader than a VLA detail. It is a world-model state transition issue.

---

## 8.6 H-WM

- **Paper:** https://arxiv.org/abs/2602.11291

### Core idea

Combine:

- high-level logical world transitions;
- low-level visual world transitions.

### Clover relevance

H-WM is a direct competing answer to a long-horizon problem:

> purely visual prediction compounds errors, while purely symbolic planning loses perceptual grounding.

Clover should study this contradiction without copying the architecture.

---

# 9. Embodied reasoning models

## 9.1 Gemini Robotics ER 2

- **Model card:** https://deepmind.google/models/model-cards/gemini-robotics-er-2/
- **Product page:** https://deepmind.google/models/gemini-robotics/embodied-reasoning/

### Official description

Gemini Robotics ER 2 is a VLM derived from Gemini 3.5 Flash and enhanced for:

- spatial reasoning;
- temporal reasoning;
- physical reasoning;
- embodied planning.

### Why it is especially important

It is one of the clearest industrial formulations of a high-level robot "brain" distinct from low-level motor execution.

### Central confound for Clover

Because it inherits large-scale language and multimodal pretraining:

> apparent physical reasoning may combine visual evidence with non-visual prior knowledge.

Clover's strict vision-only protocol should keep this distinction explicit.

---

# 10. Robot foundation models and experience scaling

## 10.1 Figure Helix 2.5

- **Official result:** https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization

Figure reports:

- whole-body autonomy in 30 unseen homes;
- no environment-specific data collection/fine-tuning in those homes;
- three long-horizon household behaviors;
- zero-shot success rising from 9% to 56% with Index pretraining.

### Why it matters

The key evidence is not merely "56%".

It is:

> broad human-experience pretraining can materially improve zero-shot transfer to unfamiliar physical environments.

### Evidence label

`OFFICIAL_REPORTED_RESULT`

This is not treated as independent reproduction.

---

## 10.2 Skild S1

- **Official report:** https://skild.ai/blogs/s1

S1 is presented as an in-context robot learner:

```text
video demonstration
→ infer task intent / correspondence
→ execute on robot
```

The company reports long-horizon unseen tasks up to roughly ten minutes without post-training for the new task.

### Clover relevance

This attacks a central assumption:

> maybe a persistent explicit world model is not required if a sufficiently broad policy can infer task/world structure in context.

Again, this is a hypothesis that Clover must test, not dismiss.

---

## 10.3 Physical Self-Play

- **Official report:** https://skild.ai/blogs/physical-self-play

The approach adds self-play/RL after broad pretraining.

### Research implication

A complete physical intelligence learning story may involve:

```text
observation
+
demonstration
+
interaction
+
self-generated experience
```

not one data source.

---

# 11. Generative physical world models

## 11.1 Cosmos 3

- **Paper:** https://arxiv.org/abs/2606.02800
- **Code/ecosystem:** https://github.com/nvidia/cosmos
- **Official:** https://www.nvidia.com/en-us/ai/cosmos/

### Why it matters

Cosmos represents the "world foundation model" direction in physical AI:

- world generation;
- reasoning;
- action-related generation;
- data engine / simulation roles.

### Clover caution

A generative model can be excellent for:

```text
possible future sampling
synthetic data
simulation
```

while still lacking a uniquely authoritative state estimate.

That distinction should remain explicit.

---

# 12. Identifiability and interpretable coordinates

## 12.1 Identifiable World Models from Pretrained Diffusion Representations

- **Paper:** https://arxiv.org/abs/2610.07028

### Core question

Predictive accuracy does not imply that latent coordinates correspond to underlying state variables.

The paper studies whether identifiable coordinates can be recovered on top of frozen diffusion latents.

### Clover relevance

This suggests a possible middle ground:

```text
distributed learned world representation
+
small identifiable state layer
```

rather than choosing between fully explicit and fully latent representation.

This is an important candidate family to investigate.

---

# 13. Event-based / sparse computation

## 13.1 Motion-aware Event Suppression

- **Paper:** https://arxiv.org/abs/2602.23204

Reported properties include:

- event-stream motion filtering;
- 173 Hz inference on consumer GPU;
- less than 1 GB memory;
- downstream acceleration through token pruning.

### Clover relevance

The useful lesson is not "use event cameras".

It is:

> physical visual change is sparse, and representation/compute can exploit that sparsity.

A Clover-native implementation could derive event-like internal evidence from standard video if it proves information-preserving.

---

# 14. Model-based control and planning

## 14.1 DreamerV3

- **Paper:** https://arxiv.org/abs/2301.04104

Dreamer demonstrates broad behavior learning by acting through a learned latent dynamics model.

## 14.2 TD-MPC2

- **Paper:** https://arxiv.org/abs/2310.16828

TD-MPC2 combines learned latent dynamics with planning/control.

### Clover relevance

These lines are essential because they ask:

> What must a learned world model contain to be useful for control, even if it is not human-interpretable?

Clover must compare its notion of "understanding" with control-sufficient latent state.

---

# 15. Provisional synthesis

The strongest current evidence does **not** support one simple conclusion.

It supports a set of constraints:

1. learned representation is necessary for scalable open-world abstraction;
2. explicit geometry remains unusually valuable where the variables are well-defined;
3. temporal prediction helps, but prediction alone is not persistent world state;
4. reconstruction gives spatial structure, but not automatically causality;
5. generation provides possible-world simulation, but can hallucinate unobserved state;
6. direct policies can achieve strong real behavior without exposing explicit state;
7. large-scale experience strongly improves transfer;
8. interaction adds information about controllability and consequences;
9. memory/evidence organization can unlock capability without changing model weights;
10. distributed physical representations are a serious competitor to explicit state;
11. action usefulness should eventually discriminate representations;
12. the next Clover architecture should be derived from these contradictions, not from attachment to an old mechanism.

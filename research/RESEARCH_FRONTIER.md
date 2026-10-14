# Stage 1 — Research Frontier Watch
## Current Primary / Official Sources Worth Deeper Analysis

Last updated: 2026-10-14  
Freshness cutoff checked through: **2026-10-14**

This file is a thin companion to [`RESEARCH.md`](RESEARCH.md).

`RESEARCH.md` is the stable broad inventory. This file tracks current primary or official sources that materially expand, challenge, or refresh that inventory and should later receive Stage 2 method reports.

A frontier entry is **not** a Clover design decision.

Evidence labels used here:

- `PRIMARY_PAPER`
- `OFFICIAL_PROJECT`
- `OPEN_SOURCE`
- `OFFICIAL_REPORTED_RESULT`

---

## 1. Executability is a separate world-model capability

### RoboWM-Bench

Primary paper: https://arxiv.org/abs/2604.19092  
Evidence: `PRIMARY_PAPER`

Research role:

```text
video-world-model realism
vs
physical plausibility
vs
robot-executable behavior
```

RoboWM-Bench converts generated human/robot manipulation behavior into embodied action sequences and tests whether execution actually completes the task. It reports recurring failures in spatial reasoning, contact prediction and deformation even when generated videos appear plausible.

What it does **not** establish:

- that video generation is the right world representation;
- that one particular explicit/latent state solves executability;
- generality beyond the evaluated manipulation settings.

Stage-2 question:

> What information is missing when visual prediction is perceptually strong but action extraction remains physically invalid?

### RoboTrustBench

Primary paper: https://arxiv.org/abs/2606.01600  
Evidence: `PRIMARY_PAPER`

Tests video world models under normal, constraint-sensitive, counterfactual and adversarial/unsafe instructions.

Stage-2 question:

> Should world-model evaluation include refusal, impossibility and constraint awareness rather than only next-video quality?

---

## 2. Contact and deformable-object dynamics may require their own state

### WorldContact

Primary paper: https://arxiv.org/abs/2609.19600  
Evidence: `PRIMARY_PAPER`

Contact-centric world modeling for deformable-object manipulation.

Rigid-object geometry is not enough for bags, cloth and other deformables. Contact topology, deformation and action-response dynamics can dominate task success.

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
Submitted: 2026-10-03; revised through 2026-10-09  
Evidence: `PRIMARY_PAPER`

Autonomous video-to-simulation reconstruction from embodied videos, evaluated by geometric fidelity, dynamic fidelity and functional correctness.

Central distinction:

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
Submitted: 2026-10-07  
Evidence: `PRIMARY_PAPER`

Benchmarks multimodal agents across 84 physical tasks spanning manipulation, mobile manipulation, locomotion, driving and aerial control. Reported failures include loss of task-relevant object state, ineffective recovery and incorrect completion judgments even when useful perception/control subroutines can be constructed.

Stage-2 question:

> Is the missing capability a better component, a persistent task/world state, a better interface contract, or closed-loop verification?

---

## 5. Persistent semantic maps are a world-memory baseline

### PerSeM

Primary paper: https://arxiv.org/abs/2609.19542  
Evidence: `PRIMARY_PAPER`

Associates frame-wise semantics with persistent world-space voxels and uses history-preserving refinement, replay and verification.

Research contrast:

```text
frame-wise semantics
vs
persistent semantic world memory
```

What it does **not** establish:

- general object permanence under arbitrary world change;
- causal or physical understanding;
- that voxel memory is the best general-purpose representation.

---

## 6. Amodal perception must be separated from ordinary tracking

### TAO-Amodal

Primary paper: https://arxiv.org/abs/2312.12433  
Evidence: `PRIMARY_PAPER`

A benchmark for tracking objects through partial/full occlusion and out-of-frame states with amodal annotations.

Required distinction:

```text
visible detection
→ visible tracking
→ amodal completion
→ re-identification
→ object permanence
→ persistent world entity
```

These are different capabilities.

---

## 7. Video-to-control should be studied as an interface problem

### From Video to Control: A Survey of Learning Manipulation Interfaces from Temporal Visual Data

Primary paper: https://arxiv.org/abs/2604.04974  
Evidence: `PRIMARY_PAPER`

Organizes video-to-control approaches into direct video→action policies, latent-action interfaces and explicit visual interfaces.

Stage-2 question:

> Which world information must be exposed to control for verification, correction and safe execution?

---

## 8. Social/multi-agent reasoning is another real-world dimension

### SocialGrid

Primary paper: https://arxiv.org/abs/2604.16022  
Evidence: `PRIMARY_PAPER`

Embodied multi-agent planning and social reasoning benchmark.

Stage-1 implication:

Keep **multi-agent / social world modeling** visible so the project does not silently equate “real world” with only rigid objects and static environments.

---

## 9. 2026-10-13: behavior-grounded physical parameters enter the world-model loop

### DR-WM — From Pixels to Executable Physics

Primary paper: https://arxiv.org/abs/2610.17630  
Submitted: **2026-10-13**  
Evidence: `PRIMARY_PAPER`

Research role:

```text
RGB scene geometry
+ real action-response evidence
+ inferred spatial contact properties
→ executable consequence prediction
```

DR-WM reconstructs geometry from an initial RGB image and augments it with spatially varying terrain/contact priors calibrated from real action-response data. Candidate robot actions are then simulated to predict future embodied consequences.

Why it matters:

It makes a hard distinction between **what pixels reveal geometrically** and **what physical parameters become learnable from interaction**. Friction/contact behavior is not assumed to be visually obvious.

What it does **not** establish:

- that its terrain representation is a general world representation;
- that passive RGB can identify friction or contact properties;
- a pure `V0/L0` route: it explicitly uses action/state experience;
- general manipulation/contact reasoning beyond the evaluated terrain setting.

Stage-2 questions:

> Which hidden physical variables are identifiable from passive video, which become identifiable from action-response, and which remain impossible without non-visual evidence?

> Can a learned representation discover action-relevant physical variables without imposing the simulator's parameterization?

---

## 10. 2026-10-13: a general multimodal reasoner is becoming a robotics baseline

### Gemini 4 Argon for Robotics

Official report: https://developers.googleblog.com/gemini-4-argon-for-robotics/  
Published: **2026-10-13**  
Evidence: `OFFICIAL_REPORTED_RESULT`

Associated ERQA benchmark/code: https://github.com/embodiedreasoning/ERQA  
Evidence: `OPEN_SOURCE`

Google reports Argon across embodied/physical reasoning, zero-shot closed-loop robot control through tools/primitives, Real2Sim reconstruction/calibration, video-world-model steering, hindsight labeling/progress estimation, simulation-generated robot training data and iterative self-improvement.

The official report states an **87%** pure-reasoning score on ERQA. Treat it as an official reported result until independently reproduced.

Important provenance boundary:

The robotics workflows mix RGB/video with calibrated geometry, code/tools, simulation, robot state/proprioception and in some examples tactile/contact telemetry. They are therefore **not** evidence that the demonstrated capabilities were learned from vision alone.

Stage-2 questions:

> Which Argon capabilities come from visual evidence, which from language/world priors, and which from tools/simulation/state access?

> Does persistent world state add measurable value beyond a strong general reasoner with an external visual/tool harness?

---

## 11. ERQA enters the embodied-reasoning benchmark inventory

### Embodied Reasoning Question Answer (ERQA)

Official repository/data/eval harness: https://github.com/embodiedreasoning/ERQA  
Evidence: `OPEN_SOURCE`

The repository exposes a 400-example multimodal benchmark of interleaved images and text focused on real-world spatial/world-knowledge reasoning in robotics contexts.

Useful for cheap comparison of public models before real-robot evaluation.

Does **not** measure by itself:

- persistent visual memory;
- world change / belief revision;
- causal intervention;
- long-horizon execution;
- whether an answer came from visual evidence versus pretrained language/world knowledge.

---

## 12. Current open VLA baseline refresh: GR00T N1.7

Official code: https://github.com/NVIDIA/Isaac-GR00T  
Model: https://huggingface.co/nvidia/GR00T-N1.7-3B  
Official technical overview: https://developer.nvidia.com/blog/develop-humanoid-robot-policies-end-to-end-with-nvidia-isaac-gr00t/  
Evidence: `OPEN_SOURCE` / `OFFICIAL_PROJECT`

GR00T N1.7 is a current NVIDIA open VLA release for generalized humanoid skills, with a Cosmos-Reason2-2B / Qwen3-VL-based VLM backbone, relative end-effector action representation, robot demonstrations and large-scale human egocentric-video pretraining.

For Clover, it is a **reproducible direct-policy baseline**, not a proposed component.

Stage-2 question:

> What task-relevant state can be decoded from GR00T's internal representations, and which world-understanding failures persist despite human-video/cross-embodiment pretraining?

---

## 13. Current world-action frontier splits into different state strategies

### Being-M0.7

Primary paper: https://arxiv.org/abs/2610.11283  
Submitted: 2026-10-08  
Evidence: `PRIMARY_PAPER`

Transfers large-scale human visual-motion priors into humanoid control through a latent world-action model.

### HWAM

Primary paper: https://arxiv.org/abs/2610.12026  
Submitted: 2026-10-08  
Evidence: `PRIMARY_PAPER`

Explicitly predicts post-execution body state together with reference actions to model the gap between commanded and physically realized motion.

Research split:

```text
large latent visual-motion prior
vs
explicit post-execution state target
```

Stage-2 questions:

> When does explicit realized-state prediction improve control over a latent future model?

> Which benefits come from representation choice versus data scale, embodiment-specific supervision or training objective?

---

## 14. Identifiable world coordinates are now a serious hybrid alternative

### Identifiable World Models from Pretrained Diffusion Representations

Primary paper: https://arxiv.org/abs/2610.07028  
Submitted: 2026-10-04  
Evidence: `PRIMARY_PAPER`

Studies whether frozen pretrained diffusion representations can be aligned to coordinates that recover latent dynamical states under explicit identifiability assumptions.

Hybrid hypothesis:

```text
powerful distributed representation
+
partially identifiable / intervention-relevant coordinates
```

What it does **not** establish:

- open-world real-video identifiability;
- that theoretical assumptions hold for arbitrary real scenes;
- that identified variables are sufficient for planning or persistent memory.

---

## 15. Evidence acquisition is becoming agentic even inside video understanding

### Agentic Video Understanding with Gemini

Official report: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/  
Published: 2026-09-01  
Evidence: `OFFICIAL_REPORTED_RESULT`

The system dynamically searches, scans, re-watches and changes sampling density over long videos instead of ingesting all frames at one fixed rate.

Why it matters:

It makes **evidence-acquisition policy** a separate research variable from base representation quality.

Important limitation:

The public mode can use frames, audio and transcripts; it is not automatically a vision-only protocol and does not create a persistent physical world model.

---

## 16. 2026-10-13: active semantic exploration remains a strong structured alternative

### Mobility-Budget-Constrained Submodular Maximization for Distributed Semantic Multi-Robot Exploration

Primary paper: https://arxiv.org/abs/2610.17562  
Submitted: **2026-10-13**  
Evidence: `PRIMARY_PAPER`

Combines semantic mapping, Dirichlet uncertainty, information-gain objectives and mobility-aware trajectory selection under communication constraints.

Why it matters:

Active perception need not start from a large learned world model. Explicit uncertainty and information gain remain structured baselines for deciding **where to look next**.

---

## 17. 2026-10-12: articulated assets expose mass/material/function as first-class evaluation targets

### Artisan — Towards Physically Grounded Articulated 3D Assets

Primary paper: https://arxiv.org/abs/2610.13947  
Project: https://physicalvision.github.io  
Submitted: 2026-10-09; revised **2026-10-12**  
Evidence: `PRIMARY_PAPER`

Artisan moves articulated 3D generation from reproducing appearance toward reproducing how objects **move and function**. Its pipeline uses physical-simulation feedback and evaluates more than geometry/appearance/articulation, including collision-free motion, stability under gravity, mass/material properties and downstream task behavior.

Its benchmark includes 100 reference assets, 50 stability prompts and 50 objects with reference masses, and evaluates more than 10 representative models.

Why it matters:

This adds a missing Stage-1 dimension:

```text
visual/spatial asset quality
≠
articulation correctness
≠
physical stability
≠
material/mass correctness
≠
functional usability
```

What it does **not** establish:

- that mass/material properties can be inferred correctly from passive RGB;
- that simulation feedback matches arbitrary real materials;
- a universal world representation for robotics.

Stage-2 question:

> Which functional/physical object properties can be inferred visually, which require interaction, and which should remain uncertain rather than hallucinated?

---

## 18. Unified causal World-Action Modeling is scaling rapidly

### Riemann-1.0

Primary paper: https://arxiv.org/abs/2608.27033  
Evidence: `PRIMARY_PAPER`

Riemann-1.0 jointly models multi-view visual observations, robot states and embodiment-specific actions as one causal autoregressive sequence. The paper reports progressive embodied pretraining over more than 200K hours of heterogeneous interaction experience spanning human egocentric video, handheld-gripper demonstrations and robot trajectories.

Why it matters:

It is a strong counter-hypothesis to a separate explicit world-model architecture:

```text
world evolution + robot state + action
inside one causal sequence model
```

What it does **not** establish:

- that one autoregressive sequence is the best representation of real-world belief;
- vision-only learning provenance;
- explicit uncertainty/object permanence/causal identifiability outside the trained objective.

Stage-2 question:

> What world state emerges inside a unified causal WAM, and what failures remain when representation boundaries are removed rather than made explicit?

---

## 19. Language can itself become the action/world-model interface

### Qwen-RobotWorld

Primary technical report: https://arxiv.org/abs/2606.17030  
Evidence: `PRIMARY_PAPER`

Qwen-RobotWorld uses natural language as a unified action interface and predicts future visual trajectories across manipulation, autonomous driving, navigation and human-to-robot transfer. Its training corpus combines millions of video-text examples across many embodiments/action categories.

Why it matters:

It offers a different hypothesis from action tokens or robot-state-conditioned dynamics:

```text
language action abstraction
→ future visual trajectory
→ data / evaluation / planning signal
```

What it does **not** establish:

- that language is a sufficient machine-native action representation;
- that physical state is identifiable from generated pixels;
- that language-conditioned prediction avoids language-prior shortcuts.

Stage-2 question:

> What physical precision is lost or gained when language becomes the shared action interface across embodiments?

---

## 20. Foundation world models are becoming data engines, not only simulators

### Xiaomi-Robotics-U0

Primary paper: https://arxiv.org/abs/2607.11643  
Official project/code/checkpoints: https://robotics.xiaomi.com/xiaomi-robotics-u0.html  
Evidence: `PRIMARY_PAPER` / `OPEN_SOURCE`

Xiaomi-Robotics-U0 is a 38B multimodal autoregressive world foundation model that unifies image/video generation, embodied scene generation, multi-view transfer and embodied video generation. The paper reports using the generated/edited embodied data to improve downstream manipulation generalization.

Why it matters:

Stage 1 should distinguish at least three world-model roles:

```text
world representation for belief
world simulator for prediction/evaluation
world data engine for policy training
```

A model can be useful in the third role without being a faithful internal world representation.

Stage-2 question:

> How should Clover separately evaluate a world model's epistemic fidelity, simulator fidelity and usefulness as a data generator?

---

## 21. Immediate frontier-analysis queue

Highest-priority future Stage-2 reports after the 2026-10-14 refresh:

```text
Gemini 4 Argon for Robotics + ERQA
DR-WM / From Pixels to Executable Physics
GR00T N1.7
Riemann-1.0
Qwen-RobotWorld
Xiaomi-Robotics-U0
Being-M0.7
HWAM
Identifiable World Models
Artisan
Vantage / Seek-and-View
Agentic Video Understanding
Video2World
RobotWorld
RoboWM-Bench
RoboTrustBench
WorldContact
PerSeM
TAO-Amodal
```

Suggested comparison axes:

```text
visual protocol
learning provenance
representation/state type
visual fidelity
geometry fidelity
state identifiability
dynamics fidelity
contact / friction / deformation correctness
mass / material / articulation correctness
persistent state
memory / evidence retrieval
functional correctness
executability
action-execution gap
constraint awareness
counterfactual behavior
active evidence acquisition
recovery
uncertainty / refusal
open-world generalization
world-model role: belief / simulator / data engine
reproducibility
```

---

## 22. Frontier-watch rule

Add a source here when it is current and materially changes what Stage 1 should know.

For every frontier source, record at least:

```text
date
exact URL
evidence level
what it demonstrates
what it does not demonstrate
visual / training provenance when material
why it changes the Stage-1 map
Stage-2 question
```

Promote stable concepts into [`RESEARCH.md`](RESEARCH.md) and deeper source maps once their role is clear.

Do not promote a frontier mechanism directly into Clover Innovation.

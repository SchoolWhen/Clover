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
Evidence: `PRIMARY_PAPER`

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
Evidence: `PRIMARY_PAPER`

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
Submitted: 2026-10-03; revised through 2026-10-09  
Evidence: `PRIMARY_PAPER`

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
Submitted: 2026-10-07  
Evidence: `PRIMARY_PAPER`

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
Evidence: `PRIMARY_PAPER`

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
Evidence: `PRIMARY_PAPER`

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
Evidence: `PRIMARY_PAPER`

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
Evidence: `PRIMARY_PAPER`

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

This is unusually relevant to the central Clover question because it makes a hard distinction between **what pixels reveal geometrically** and **what physical parameters become learnable from interaction**. Friction/contact behavior is not treated as something that must be visually obvious.

What it does **not** establish:

- that its terrain representation is a general world representation;
- that passive RGB can identify friction or contact properties;
- a pure `V0/L0` route: the method explicitly uses action/state experience to calibrate physical behavior;
- general manipulation/contact reasoning beyond the evaluated quadruped-terrain setting.

Stage-2 questions:

> Which hidden physical variables are identifiable from passive video, which become identifiable from action-response, and which remain impossible without non-visual evidence?

> Can a learned representation discover the same action-relevant parameters without imposing the simulator's physical parameterization?

---

## 10. 2026-10-13: a general multimodal reasoner is becoming a robotics baseline

### Gemini 4 Argon for Robotics

Official report: https://developers.googleblog.com/gemini-4-argon-for-robotics/  
Published: **2026-10-13**  
Evidence: `OFFICIAL_REPORTED_RESULT`

Associated ERQA benchmark/code: https://github.com/embodiedreasoning/ERQA  
Evidence: `OPEN_SOURCE`

Google reports Gemini 4 Argon as a general-purpose model used across:

- embodied/physical reasoning;
- zero-shot closed-loop robot control through tools/primitives;
- Real2Sim reconstruction and calibration;
- video-world-model steering;
- hindsight labeling / progress estimation;
- simulation-generated robot training data;
- iterative robot self-improvement.

The official report states an **87%** pure-reasoning score on ERQA. Treat that score as an official reported result until independently reproduced.

Why it matters:

Argon is a strong counter-hypothesis to a narrow view that robotic world understanding must live inside a purpose-built robot architecture. A powerful general multimodal model plus visual/geometry/simulation/tool harnesses can already perform substantial physical workflows.

Important provenance boundary:

Argon's robotics workflows use mixtures of RGB/video, calibrated geometry, code/tools, simulation, robot state/proprioception and in some examples tactile/contact telemetry. It is therefore **not** evidence that the demonstrated robotics capabilities were learned from vision alone.

What it does **not** establish:

- a persistent evidence-grounded world state;
- that its internal representation is physically identifiable;
- that general reasoning eliminates the need for robot-specific state/memory;
- independent scientific reproduction of the reported robotics demonstrations.

Stage-2 questions:

> Which Argon capabilities come from visual evidence, which from language/world priors, and which from tools/simulation/state access?

> Does an explicit persistent world representation add measurable value beyond a strong general reasoner with an external visual/tool harness?

---

## 11. ERQA should enter the embodied-reasoning benchmark inventory

### Embodied Reasoning Question Answer (ERQA)

Official repository/data/eval harness: https://github.com/embodiedreasoning/ERQA  
Evidence: `OPEN_SOURCE`

The repository exposes a 400-example multimodal benchmark of interleaved images and text focused on real-world spatial/world-knowledge reasoning in robotics contexts.

Why it matters:

ERQA provides a reproducible reference point for the rapidly improving class of general multimodal physical reasoners. It is especially useful for comparing public APIs/models before expensive real-robot evaluation.

What it does **not** measure by itself:

- persistent visual memory;
- world change / belief revision;
- causal intervention;
- long-horizon action execution;
- whether an answer was derived from visual evidence rather than pretrained language/world knowledge.

Stage-1 action:

Add ERQA to the benchmark inventory with a warning that it is an **embodied-reasoning diagnostic**, not a definition of real-world understanding.

---

## 12. Current open VLA baseline refresh: GR00T N1.7

Official code: https://github.com/NVIDIA/Isaac-GR00T  
Model: https://huggingface.co/nvidia/GR00T-N1.7-3B  
Official technical overview: https://developer.nvidia.com/blog/develop-humanoid-robot-policies-end-to-end-with-nvidia-isaac-gr00t/  
Evidence: `OPEN_SOURCE` / `OFFICIAL_PROJECT`

GR00T N1.7 is the current NVIDIA open VLA release for generalized humanoid skills. The public repository describes a Cosmos-Reason2-2B / Qwen3-VL-based VLM backbone, relative end-effector action representation, robot demonstrations and large-scale human egocentric-video pretraining.

Why it matters:

For Clover, GR00T N1.7 is important less as a proposed component than as a **reproducible direct-policy baseline**. Any claim that a persistent/world-state representation is necessary for general robot behavior should eventually survive comparison against strong open end-to-end policies of this class.

What it does **not** establish:

- that direct VLA policies have a stable persistent world model;
- that human-video pretraining isolates visual knowledge from language/action priors;
- that good manipulation performance answers the observability, permanence, causality or epistemic-state questions.

Stage-2 question:

> What task-relevant state can be decoded from GR00T's internal representations, and which failure modes persist despite cross-embodiment human-video pretraining?

---

## 13. Current world-action frontier splits into two different state strategies

### Being-M0.7

Primary paper: https://arxiv.org/abs/2610.11283  
Submitted: 2026-10-08  
Evidence: `PRIMARY_PAPER`

Being-M0.7 transfers visual-motion priors from a large mixture of human video/motion data into humanoid control through a latent world-action model.

### HWAM

Primary paper: https://arxiv.org/abs/2610.12026  
Submitted: 2026-10-08  
Evidence: `PRIMARY_PAPER`

HWAM explicitly predicts the robot's post-execution body state together with reference actions to address the gap between commanded and physically realized motion.

Why the pair matters:

These two contemporary WAMs expose an important split:

```text
large latent visual-motion prior
vs
explicit post-execution state target
```

Neither result settles the general representation question, but together they create a useful Stage-2 comparison for **what action-relevant state must be represented explicitly**.

Stage-2 questions:

> When does explicit realized-state prediction improve control over a latent future model?

> Which benefits come from representation choice versus data scale, humanoid-specific supervision or training objective?

---

## 14. Identifiable world coordinates are now a serious hybrid alternative

### Identifiable World Models from Pretrained Diffusion Representations

Primary paper: https://arxiv.org/abs/2610.07028  
Submitted: 2026-10-04  
Evidence: `PRIMARY_PAPER`

The paper studies whether frozen pretrained diffusion representations can be aligned to coordinates that recover latent dynamical states under explicit identifiability assumptions, rather than forcing a choice between fully opaque distributed latents and fully hand-designed symbolic state.

Why it matters:

This strengthens the hybrid hypothesis:

```text
powerful distributed representation
+
partially identifiable / intervention-relevant coordinates
```

What it does **not** establish:

- open-world real-video identifiability;
- that the required theoretical assumptions hold for arbitrary real scenes;
- that identified variables are sufficient for robot planning or persistent memory.

Stage-2 question:

> Can useful world coordinates be discovered on top of large visual representations while retaining the representation's open-world capacity?

---

## 15. Evidence acquisition is becoming agentic even inside video understanding

### Agentic Video Understanding with Gemini

Official report: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/  
Published: 2026-09-01  
Evidence: `OFFICIAL_REPORTED_RESULT`

The system dynamically searches, scans, re-watches and changes sampling density over long videos instead of ingesting all frames at one fixed rate.

Why it matters:

This is a useful non-robot counterexample showing that **active evidence selection** can improve both efficiency and answer quality without changing the base model. It supports treating evidence acquisition policy as a separate research variable from representation quality.

Important limitation:

The public product mode can use frames, audio and transcripts; it is not automatically a vision-only protocol. It also does not create a persistent physical world model.

Stage-2 question:

> How much of apparent long-video understanding comes from better evidence acquisition rather than a better internal world representation?

---

## 16. 2026-10-13: active semantic exploration is still a live classical/structured alternative

### Mobility-Budget-Constrained Submodular Maximization for Distributed Semantic Multi-Robot Exploration

Primary paper: https://arxiv.org/abs/2610.17562  
Submitted: **2026-10-13**  
Evidence: `PRIMARY_PAPER`

The method combines semantic mapping, Dirichlet uncertainty, information-gain objectives and mobility-aware trajectory selection under communication constraints.

Why it matters:

It is a reminder that active perception need not start from a large learned world model. Explicit uncertainty and information gain remain strong structured baselines for deciding **where to look next**.

What it does **not** establish:

- general open-world semantic understanding;
- learned active perception from raw RGB alone;
- real-world performance beyond the reported simulation settings.

Stage-2 question:

> When does an explicit uncertainty/information-gain controller outperform learned active-view selection, and can the two be compared under the same observation budget?

---

## 17. Immediate frontier-analysis queue

Highest-priority future Stage-2 reports after the 2026-10-14 refresh:

```text
Gemini 4 Argon for Robotics + ERQA
DR-WM / From Pixels to Executable Physics
GR00T N1.7
Being-M0.7
HWAM
Identifiable World Models
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
visual fidelity
geometry fidelity
state identifiability
dynamics fidelity
contact / friction / deformation correctness
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
reproducibility
```

---

## 18. Frontier-watch rule

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

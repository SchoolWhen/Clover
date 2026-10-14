# Clover Status

Last updated: 2026-10-14

## Research question

> **How can a machine understand the real world through vision alone?**

## Product goal

> **Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.**

## Current stage

> **Stage 1 — Research / Survey & Evidence Collection — ACTIVE**

The repository follows:

```text
1 Research
→ 2 Analysis
→ 3 Synthesis
→ 4 Innovation
→ 5 Implementation
→ 6 Evaluation
→ 7 Reflection
```

The immediate priority is breadth, traceability and coverage. We are collecting the full research landscape before making a new Clover algorithmic commitment.

Stage-1 freshness has been checked through **2026-10-14**.

Start with:

1. [`SSOT.md`](SSOT.md)
2. [`research/PIPELINE.md`](research/PIPELINE.md)
3. [`research/RESEARCH.md`](research/RESEARCH.md)
4. [`research/RESEARCH_FRONTIER.md`](research/RESEARCH_FRONTIER.md)
5. [`research/README.md`](research/README.md)

## Stage-1 foundation — active / expanding

The current inventory explicitly tracks directions including:

- epistemology, inverse problems and partial observability;
- human/developmental visual cognition;
- classical geometry, SfM, VO and SLAM;
- optical flow, correspondence and tracking;
- static self-supervised representation;
- predictive video representation;
- learned geometry;
- NeRF / Gaussian Splatting / 4D reconstruction;
- object-centric representation;
- scene graphs and semantic mapping;
- persistent / episodic memory;
- belief revision and forgetting;
- intuitive, relational and quantitative physics;
- physics-structured / differentiable world models;
- contact, friction, articulation and deformable-object dynamics;
- mass/material/function grounding;
- causal representation learning;
- counterfactual visual reasoning;
- active perception and next-best-view;
- system identification and action consequences;
- generative world models;
- world-action models;
- world models as belief state, simulator and data engine;
- VLA and direct policy;
- hierarchical embodied reasoning;
- robot foundation models;
- human / egocentric video transfer;
- affordance learning;
- model-based control and belief-space planning;
- semantic memory;
- uncertainty and calibration;
- open-world / OOD recognition;
- continual / lifelong learning;
- simulation, Real2Sim and synthetic data;
- large robot datasets;
- benchmark design and shortcut auditing;
- systems integration and compounded failure;
- multi-agent / social world modeling;
- unified physical-AI surveys.

This list is intentionally expandable. If a direction materially constrains the mother question, Stage 1 should collect it.

## 2026-10-14 frontier refresh

The current edge includes several references that materially change the comparison space:

- **Gemini 4 Argon for Robotics** — https://developers.googleblog.com/gemini-4-argon-for-robotics/ — `OFFICIAL_REPORTED_RESULT`; current general multimodal physical-reasoning / Real2Sim / robot-tool-use counter-hypothesis.
- **ERQA** — https://github.com/embodiedreasoning/ERQA — `OPEN_SOURCE`; embodied/spatial reasoning benchmark and evaluation harness.
- **DR-WM / From Pixels to Executable Physics** — https://arxiv.org/abs/2610.17630 — `PRIMARY_PAPER`, submitted 2026-10-13; separates visual geometry from contact/friction properties calibrated through action-response evidence.
- **GR00T N1.7** — https://github.com/NVIDIA/Isaac-GR00T — `OPEN_SOURCE`; current strong open VLA/direct-policy reference with human-video pretraining and cross-embodiment action representation.
- **Riemann-1.0** — https://arxiv.org/abs/2608.27033 — `PRIMARY_PAPER`; unified causal WAM jointly modeling observations, robot state and action over large heterogeneous embodied experience.
- **Qwen-RobotWorld** — https://arxiv.org/abs/2606.17030 — `PRIMARY_PAPER`; language-conditioned video world modeling across multiple embodied domains.
- **Xiaomi-Robotics-U0** — https://arxiv.org/abs/2607.11643 — `PRIMARY_PAPER`; world foundation model functioning as embodied generator, transfer mechanism and data engine.
- **Being-M0.7** — https://arxiv.org/abs/2610.11283 — `PRIMARY_PAPER`; latent visual-motion world-action route for humanoid control.
- **HWAM** — https://arxiv.org/abs/2610.12026 — `PRIMARY_PAPER`; explicitly predicts post-execution body state to model the action-execution gap.
- **Identifiable World Models** — https://arxiv.org/abs/2610.07028 — `PRIMARY_PAPER`; hybrid route combining distributed pretrained representations with identifiable dynamical coordinates under explicit assumptions.
- **Artisan** — https://arxiv.org/abs/2610.13947 — `PRIMARY_PAPER`; adds collision, gravity stability, mass/material properties and functional task behavior to articulated-asset evaluation.
- **Vantage / Seek-and-View** — https://arxiv.org/abs/2610.11810 — `PRIMARY_PAPER`; question-conditioned viewpoint/evidence acquisition for multi-view spatial reasoning.
- **Agentic Video Understanding** — https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/ — `OFFICIAL_REPORTED_RESULT`; evidence-acquisition policy as a variable separate from base representation.
- **RobotWorld** — https://arxiv.org/abs/2610.10409 — `PRIMARY_PAPER`; exposes composition, retained task-state, recovery and completion-verification failures across diverse physical tasks.
- **Video2World** — https://arxiv.org/abs/2610.04432 — `PRIMARY_PAPER`; evaluates reconstructed worlds by geometry, dynamics and functional correctness rather than visual similarity alone.

These are **research materials and comparators**, not Clover components.

## Current method references

Important tracked references now span:

```text
classical geometry / tracking
ORB-SLAM3 · RAFT

static / video representation
DINOv3 · V-JEPA 2 / 2.1

learned 3D / 4D world structure
DUSt3R · VGGT / VGGT-Ω · NeRF / 3DGS / 4D reconstruction

entities / memory
SAM 3.1 · Slot Attention · PLATO · PersistBench · S-EMBER · VISTA · PerSeM · TAO-Amodal

physical / causal understanding
IntPhys 2 · Minimal Video Pairs · Principia · RoboPhys-3D · CausalVQA · DR-WM · Artisan · WorldContact

active evidence
Vantage · agentic video understanding · semantic information-gain exploration

generative / world models
Atlas · Cosmos 3 · Video2World · Qwen-RobotWorld · Xiaomi-Robotics-U0

VLA / direct policy / robot foundation systems
OpenVLA · π0.5 · GR00T N1.7 · Gemini Robotics · Gemini 4 Argon · Helix · Skild

world-action models
ReWAM · Riemann-1.0 · Being-M0.7 · HWAM · related WAMs

hybrid state
Identifiable World Models
```

## Dataset / benchmark collection

Tracked resources include:

- Ego4D;
- Perception Test;
- DROID;
- Open X-Embodiment;
- LIBERO;
- CALVIN;
- RoboCasa;
- ManiSkill;
- ERQA;
- RobotWorld;
- Video2World;
- RoboWM-Bench;
- RoboTrustBench;
- TAO-Amodal;
- IntPhys 2;
- Minimal Video Pairs;
- CausalVQA;
- PersistBench;
- S-EMBER;
- Principia;
- RoboPhys-3D;
- EmbodimentSemantic;
- Artisan physical/articulated-asset benchmark resources.

Stage 1 records what each dataset/benchmark actually measures, its inputs, hidden ground truth, shortcuts, licensing and reproducibility.

## Boundary distinctions strengthened by current evidence

```text
visual geometry
≠
hidden physical parameters

plausible prediction
≠
physically executable consequence

reference action
≠
realized robot state

visible tracking
≠
amodal completion
≠
object permanence

appearance / reconstruction quality
≠
articulation / mass / material / function

long context
≠
active evidence acquisition

strong multimodal reasoner + tools
≠
proof of vision-only world understanding

world model for belief
≠
world simulator
≠
world data engine
```

## Existing Clover prototype

Pre-reset Clover mechanisms remain `INTERNAL_HYPOTHESIS` material. They conceptually belong to Stage 4 Innovation until evidence promotes, transforms or rejects them.

No historical mechanism is protected.

## Current non-goals

We are not currently:

- freezing a final representation;
- implementing a new Clover core architecture;
- optimizing leaderboard scores;
- claiming explicit state is superior to latent state;
- claiming a direct policy is sufficient;
- claiming a generative world model is sufficient;
- choosing hardware before the scientific mechanism;
- treating one benchmark as the definition of understanding.

## Next transition

Stage 2 Analysis becomes the primary activity only when Stage 1 coverage is broad enough that method selection for deeper reports is not distorted by obvious missing fields.

Analysis will then produce one-method-one-report mechanism breakdowns; Stage 3 Synthesis will compare their strengths, weaknesses and common gaps; only Stage 4 Innovation will formalize Clover-original algorithms.

## Not yet demonstrated

Clover has not yet publicly demonstrated general real-world visual world understanding, a final world representation, comprehensive positive-result SOTA, robust open-world generalization, general causal understanding, persistent long-horizon real-robot world state, a validated original algorithm, or a final hardware mapping.

These remain research targets.

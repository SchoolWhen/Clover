# Clover Status

Last updated: 2026-10-14

## Research question

> **How can a machine understand the real world through vision alone?**

## Product goal

> **Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.**

## Current stage

> **Stage 1 — Research / Survey & Evidence Collection — ACTIVE**

The repository now follows:

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

The current inventory covers more than the original eight deep domains. It now explicitly tracks directions including:

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
- contact, friction and deformable-object dynamics;
- causal representation learning;
- counterfactual visual reasoning;
- active perception and next-best-view;
- system identification and action consequences;
- generative world models;
- world-action models;
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

The current edge now includes several references that materially change the comparison space:

- **Gemini 4 Argon for Robotics** — https://developers.googleblog.com/gemini-4-argon-for-robotics/ — `OFFICIAL_REPORTED_RESULT`; current general multimodal physical-reasoning / Real2Sim / robot-tool-use counter-hypothesis.
- **ERQA** — https://github.com/embodiedreasoning/ERQA — `OPEN_SOURCE`; embodied/spatial reasoning benchmark and evaluation harness.
- **DR-WM / From Pixels to Executable Physics** — https://arxiv.org/abs/2610.17630 — `PRIMARY_PAPER`, submitted 2026-10-13; separates visual geometry from contact/friction properties calibrated through action-response evidence.
- **GR00T N1.7** — https://github.com/NVIDIA/Isaac-GR00T — `OPEN_SOURCE`; current strong open VLA/direct-policy baseline with human-video pretraining and cross-embodiment action representation.
- **Being-M0.7** — https://arxiv.org/abs/2610.11283 — `PRIMARY_PAPER`; latent visual-motion world-action route for humanoid control.
- **HWAM** — https://arxiv.org/abs/2610.12026 — `PRIMARY_PAPER`; explicitly predicts post-execution body state to model the action-execution gap.
- **Identifiable World Models** — https://arxiv.org/abs/2610.07028 — `PRIMARY_PAPER`; hybrid route combining distributed pretrained representations with identifiable dynamical coordinates under explicit assumptions.
- **Vantage / Seek-and-View** — https://arxiv.org/abs/2610.11810 — `PRIMARY_PAPER`; question-conditioned viewpoint/evidence acquisition for multi-view spatial reasoning.
- **Agentic Video Understanding** — https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/ — `OFFICIAL_REPORTED_RESULT`; evidence-acquisition policy as a variable separate from the base representation.
- **RobotWorld** — https://arxiv.org/abs/2610.10409 — `PRIMARY_PAPER`; exposes composition, task-state retention, recovery and completion-verification failures across diverse robot-use tasks.
- **Video2World** — https://arxiv.org/abs/2610.04432 — `PRIMARY_PAPER`; evaluates reconstructed worlds by geometry, dynamics and functional correctness rather than visual similarity alone.

These are **research materials and comparators**, not Clover components.

## Current method references

Important references already tracked include ORB-SLAM3, RAFT, DINOv3, V-JEPA 2 / 2.1, DUSt3R, VGGT / VGGT-Ω, SAM 3 / 3.1, Slot Attention, PLATO, NeRF / 3DGS / 4D reconstruction, PersistBench, S-EMBER, VISTA, IntPhys 2, Minimal Video Pairs, Principia, RoboPhys-3D, CausalVQA, causal representation learning, Vantage, Atlas, Cosmos 3, OpenVLA, π0.5, GR00T N1.7, Gemini Robotics, Gemini 4 Argon, Helix, Skild, ReWAM, Being-M0.7, HWAM, HumanEgo, DreamerV3, TD-MPC2, DR-WM and related work.

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
- IntPhys 2;
- Minimal Video Pairs;
- CausalVQA;
- PersistBench;
- S-EMBER;
- Principia;
- RoboPhys-3D;
- TAO-Amodal;
- EmbodimentSemantic.

Stage 1 records what each dataset/benchmark actually measures, its inputs, hidden ground truth, shortcuts, licensing and reproducibility.

## New boundary distinctions strengthened by current evidence

The latest material makes these distinctions increasingly important:

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

long context
≠
active evidence acquisition

strong multimodal reasoner + tools
≠
proof of vision-only world understanding
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

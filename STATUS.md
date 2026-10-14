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

Start with:

1. [`SSOT.md`](SSOT.md)
2. [`research/PIPELINE.md`](research/PIPELINE.md)
3. [`research/RESEARCH.md`](research/RESEARCH.md)
4. [`research/README.md`](research/README.md)

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
- causal representation learning;
- counterfactual visual reasoning;
- active perception;
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
- simulation and synthetic data;
- large robot datasets;
- benchmark design and shortcut auditing;
- systems integration and compounded failure;
- unified physical-AI surveys.

This list is intentionally expandable. If a direction materially constrains the mother question, Stage 1 should collect it.

## Current method references

Important references already tracked include ORB-SLAM3, RAFT, DINOv3, V-JEPA 2 / 2.1, DUSt3R, VGGT / VGGT-Ω, SAM 3 / 3.1, Slot Attention, PLATO, NeRF / 3DGS / 4D reconstruction, PersistBench, S-EMBER, VISTA, IntPhys 2, Minimal Video Pairs, Principia, RoboPhys-3D, CausalVQA, causal representation learning, Vantage, Atlas, Cosmos 3, OpenVLA, π0.5, Gemini Robotics, Helix, Skild, ReWAM, Being-M0.7, HWAM, HumanEgo, DreamerV3, TD-MPC2 and related work.

These are **research materials and comparators**, not Clover components.

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
- IntPhys 2;
- Minimal Video Pairs;
- CausalVQA;
- PersistBench;
- S-EMBER;
- Principia;
- RoboPhys-3D;
- EmbodimentSemantic.

Stage 1 records what each dataset/benchmark actually measures, its inputs, hidden ground truth, shortcuts, licensing and reproducibility.

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

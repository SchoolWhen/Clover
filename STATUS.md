# Clover Status

Last updated: 2026-10-14

## Research Question

> **How can a machine understand the real world through vision alone?**

## Product Goal

> **Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.**

## Current Phase

**Background Research / Problem Reconstruction — ACTIVE.**

The immediate priority is to build a sufficiently complete, primary-source-backed understanding of the problem before freezing a new Clover representation or architecture.

Current order:

```text
Background Research / Research Map
→ Baseline Setup
→ Understanding Battery
→ Failure Matrix
→ Representation Hypothesis
```

Start with [`SSOT.md`](SSOT.md), then [`research/survey/BACKGROUND_RESEARCH.md`](research/survey/BACKGROUND_RESEARCH.md) and [`research/survey/SOURCE_MAP.md`](research/survey/SOURCE_MAP.md).

## Background Research Foundation — ACTIVE / EXPANDING

The repository now organizes the problem into explicit research domains:

- partial observability, uncertainty and active perception;
- classical geometry and state estimation;
- static self-supervised visual representation;
- predictive video representation;
- learned geometry and spatial reconstruction;
- object-centric representation and visible tracking;
- persistent visual/episodic memory;
- intuitive physics and quantitative physical reasoning;
- causality and intervention;
- generative world models;
- embodied VLM/VLA/world-action models;
- robot foundation models and real-world generalization;
- state/action-grounded evaluation.

Every durable external claim should map to a primary paper, official technical source or open repository, plus a statement of what the source does **not** establish.

## Current Research Baseline Updates

The Survey now treats these as important current references:

- DINOv3 for static self-supervised visual representation;
- V-JEPA 2 / 2.1 for predictive video representation;
- VGGT / VGGT-Ω for learned geometry;
- SAM 3 / 3.1 for visible open-vocabulary entity detection/segmentation/tracking;
- PersistBench and S-EMBER for persistent/streaming visual memory;
- IntPhys 2, MVP, Principia and CausalVQA for physical/causal diagnostics;
- OpenVLA / π0.5 / Gemini Robotics / Helix 2.5 / Skild S1 as embodied policy/reasoning counter-hypotheses;
- Atlas and Cosmos 3 as generative/general world-model counter-hypotheses.

These are **comparators and evidence**, not components automatically adopted into Clover.

## Existing Clover Prototype — RESEARCH_PROTOTYPE

A substantial pre-reset Research Prototype 1 exists outside the current public codebase, exploring field-based visual evidence, persistent entities/spacetime support, typed world queries, epistemic licences, decision, tool-use and execution loops.

Those mechanisms are **candidate hypotheses**, not architectural commitments. Public code migration and the naming/versioning scheme for future code generations remain downstream of the background research and representation decision process.

## Active Research Questions — OPEN

The current Survey explicitly investigates, among others:

- what a world representation must contain;
- explicit vs distributed vs hybrid state;
- geometry vs learned representation;
- prediction vs reconstruction vs generation;
- what vision can directly observe vs only infer;
- passive observation vs interaction;
- object-centric vs dense/field representation;
- persistent memory and evidence retention;
- belief revision and contradiction handling;
- intuitive physics and quantitative physical state;
- causal identifiability and counterfactual reasoning;
- language/world-knowledge confounds;
- active perception;
- whether a persistent worldview measurably improves action;
- embodiment-invariant abstractions;
- hardware/software co-design only after scientific structure is known.

## Evaluation — BEING REFRAMED AS A BATTERY

Public benchmarks and robot tasks remain measurement instruments rather than project goals.

The evidence hierarchy is:

1. controlled cognitive/physical diagnostics;
2. shortcut-resistant paired tests;
3. persistent/streaming memory diagnostics;
4. causal/interventional tests;
5. geometry/world-state diagnostics;
6. real-video transfer;
7. active-perception tasks;
8. long-horizon embodied tasks in unfamiliar environments;
9. action usefulness and recovery;
10. efficiency and hardware co-design once capability is established.

## Not Yet Demonstrated

Clover has not yet publicly demonstrated:

- general real-world visual world understanding;
- a final world representation;
- superiority of explicit state over distributed latent state;
- superiority of historical Clover field/CSP/licence mechanisms;
- comprehensive positive-result SOTA;
- robust open-world generalization;
- persistent long-horizon real-robot world state;
- general causal understanding;
- long-horizon autonomous robot-brain capability;
- an empirically established memory architecture;
- a final CPU/GPU/Metal allocation.

These are research targets or open hypotheses. They do not justify lowering the research question.

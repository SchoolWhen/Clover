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

Start with [`SSOT.md`](SSOT.md), then [`research/survey/RESEARCH_OVERVIEW.md`](research/survey/RESEARCH_OVERVIEW.md), [`research/survey/BACKGROUND_RESEARCH.md`](research/survey/BACKGROUND_RESEARCH.md), [`research/dossiers/README.md`](research/dossiers/README.md) and [`research/survey/SOURCE_MAP.md`](research/survey/SOURCE_MAP.md).

## Background Research Foundation — ACTIVE / EXPANDING

The repository now has two complementary research layers:

1. a broad Survey that maps the full problem, sources, methods, benchmarks and unresolved questions;
2. eight deep research dossiers that push each domain from literature summary toward explicit baselines, discriminating experiments and kill conditions.

Current dossiers:

- `R-A` observability / epistemology;
- `R-B` geometry;
- `R-C` representation;
- `R-D` memory / persistence;
- `R-E` physics;
- `R-F` causality / interaction;
- `R-G` world model ↔ action;
- `R-H` active perception / lifelong learning.

The compact visual map is [`research/survey/RESEARCH_OVERVIEW.md`](research/survey/RESEARCH_OVERVIEW.md).

Every durable external claim should map to a primary paper, official technical source or open repository, plus a statement of what the source does **not** establish.

## Current Primary Contradictions

The current research map is organized around six competing questions rather than historical Clover module names:

```text
C1 explicit state vs distributed latent vs hybrid / identifiable state
C2 reconstruction vs prediction vs generation
C3 object-centric vs dense scene representation
C4 passive observation vs interaction
C5 persistent world state vs long context / direct policy
C6 evidence-grounded belief vs plausible generative completion
```

These contradictions will determine which baselines and diagnostic experiments are needed before a representation hypothesis is promoted.

## Current Research Baseline Updates

The Survey now treats these as important current references:

- DINOv3 for static self-supervised visual representation;
- V-JEPA 2 / 2.1 for predictive video representation;
- VGGT / VGGT-Ω for learned geometry;
- SAM 3 / 3.1 for visible open-vocabulary entity detection/segmentation/tracking;
- PersistBench, S-EMBER and VISTA-style comparisons for persistent/streaming visual memory;
- IntPhys 2, Minimal Video Pairs, QuantiPhy, Principia and CausalVQA for physical/causal diagnostics;
- RoboPhys-3D for state/action-grounded world-model evaluation;
- OpenVLA / π0.5 / Gemini Robotics / Helix 2.5 / Skild S1 as embodied policy/reasoning counter-hypotheses;
- WAM / ReWAM / Being-M0.7-class systems as world-action comparators;
- Atlas and Cosmos 3 as generative/general world-model counter-hypotheses;
- causal representation learning and active-perception literature as theoretical constraints on what passive observation can identify.

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
- intuitive, quantitative and relational physics;
- causal identifiability and counterfactual reasoning;
- language/world-knowledge confounds;
- active perception;
- continual visual learning and forgetting;
- whether a persistent worldview measurably improves action;
- embodiment-invariant abstractions;
- hardware/software co-design only after scientific structure is known.

## Evaluation — BEING REFRAMED AS A BATTERY

Public benchmarks and robot tasks remain measurement instruments rather than project goals.

The evidence hierarchy is:

1. controlled cognitive/physical diagnostics;
2. shortcut-resistant paired tests;
3. persistent/streaming memory diagnostics;
4. quantitative and relational physics tests;
5. causal/interventional tests;
6. geometry/world-state diagnostics;
7. real-video transfer;
8. active-perception tasks;
9. long-horizon embodied tasks in unfamiliar environments;
10. action usefulness and recovery;
11. efficiency and hardware co-design once capability is established.

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

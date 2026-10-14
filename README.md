# Clover

**Open research on how machines can understand the real world through vision alone.**

> **Research question:** How can a machine understand the real world through vision alone?
>
> **Long-term goal:** Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.

Clover is a long-term open research project. **The question is fixed; the answer is open.**

[中文说明](README.zh-CN.md)

## Start here

For a new agent, researcher or contributor:

1. [`SSOT.md`](SSOT.md) — fixed research question, product goal and scientific stance.
2. [`research/PIPELINE.md`](research/PIPELINE.md) — the seven-stage research lifecycle.
3. [`research/RESEARCH.md`](research/RESEARCH.md) — the active broad research inventory.
4. [`research/RESEARCH_STATE_VARIABLES.md`](research/RESEARCH_STATE_VARIABLES.md) — what kinds of world variables matter and what evidence constrains them.
5. [`research/RESEARCH_IDENTIFIABILITY.md`](research/RESEARCH_IDENTIFIABILITY.md) — predictability vs observability vs identifiability, partial observability and intervention.
6. [`research/RESEARCH_FRONTIER.md`](research/RESEARCH_FRONTIER.md) — current frontier sources checked through the latest Stage-1 refresh.
7. [`AGENTS.md`](AGENTS.md) — operating rules for research and coding agents.
8. [`STATUS.md`](STATUS.md) — current stage and non-goals.
9. [`research/README.md`](research/README.md) — flat research navigation.

## Current stage — 1 Research

Clover uses:

```text
1 Research
→ 2 Analysis
→ 3 Synthesis
→ 4 Innovation
→ 5 Implementation
→ 6 Evaluation
→ 7 Reflection
↺ next cycle
```

**Stage 1 Research is active.**

The current job is to collect the problem space broadly before deciding what Clover itself should invent.

We are collecting:

- research directions;
- foundational theories;
- latest strong methods;
- primary papers;
- official project pages;
- open code and checkpoints;
- datasets;
- benchmarks;
- labs/projects worth monitoring;
- training/evidence provenance;
- known limitations;
- open questions.

The active inventory is [`research/RESEARCH.md`](research/RESEARCH.md).

## Stage-1 structure

The current flat research entry has four complementary surfaces:

```text
RESEARCH.md
    what directions / methods / datasets exist?

RESEARCH_STATE_VARIABLES.md
    what does “world state” actually contain?

RESEARCH_IDENTIFIABILITY.md
    which variables are determined by which evidence, under what assumptions?

RESEARCH_FRONTIER.md
    what new primary/official work materially changes the map right now?
```

This separation is intentional. It prevents the repository from treating a new model, a latent variable and an information-theoretic limitation as the same kind of research object.

## What Stage 1 currently covers

The inventory is intentionally wider than “world models” or “VLA.” It includes:

- inverse problems, observability, identifiability, uncertainty and POMDPs;
- human/developmental visual cognition;
- classical geometry, SfM, VO and SLAM;
- optical flow and tracking;
- static self-supervised visual representation;
- predictive video representation;
- learned geometry;
- neural scene representations, NeRF, 3DGS and 4D reconstruction;
- object-centric representation;
- scene graphs and semantic mapping;
- persistent and episodic memory;
- world change, multi-session maps and belief revision;
- intuitive, relational and quantitative physics;
- mass, density, inertia, friction, stiffness and material-property inference;
- articulated, deformable, soft-body, contact and liquid dynamics;
- structured / physics-informed world models;
- causal representation learning and counterfactual reasoning;
- active perception, intervention and system identification;
- generative world models;
- world-action models;
- VLA and direct policies;
- embodied reasoning and robot foundation models;
- human / egocentric video learning;
- affordance and functional-object learning;
- model-based control;
- semantic memory;
- uncertainty calibration and OOD;
- continual learning;
- simulation / synthetic data;
- robot datasets;
- benchmark methodology;
- systems integration and compounded failure;
- multi-agent / social world modeling.

If another direction materially constrains the mother question, it should be added even if it does not fit an existing category.

## A central Stage-1 distinction

Current evidence increasingly requires Clover to keep this distinction explicit:

```text
statistically predictable from pixels
≠
physically identifiable from pixels
```

A model can estimate mass, material or future motion using strong learned priors without proving that the visual evidence uniquely determines those variables.

Therefore Stage 1 now asks, per variable:

```text
What is directly observed?
What is inferred from passive temporal evidence?
What becomes clearer from active viewpoints?
What requires action-response / system identification?
What currently relies on non-visual or privileged state?
What uncertainty remains after all allowed evidence?
```

See [`research/RESEARCH_STATE_VARIABLES.md`](research/RESEARCH_STATE_VARIABLES.md) and [`research/RESEARCH_IDENTIFIABILITY.md`](research/RESEARCH_IDENTIFIABILITY.md).

## What happens later

### 2 Analysis

One important method → one small mechanism report:

```text
problem
inputs / supervision
representation
mechanism
objective
memory / time
geometry / physics / causality assumptions
datasets / benchmarks
results
strengths / weaknesses
confounds / failure modes
identifiability assumptions
evidence budget
```

### 3 Synthesis

Compare methods across common dimensions and summarize:

```text
advantages
limitations
trade-offs
common failures
capability matrix
Failure Matrix
research gaps
```

### 4 Innovation

Only after the gap is well supported do Clover-original ideas become serious hypotheses:

```text
gap
→ original hypothesis
→ mathematical / algorithmic form
→ prediction
→ falsifier
```

### 5 Implementation

Build reproducible code.

### 6 Evaluation

Run experiments and record Results.

### 7 Reflection

Interpret failures, reject bad assumptions and begin the next research cycle.

## Detailed Stage-1 material

The flat stage files are the main navigation. Deeper research assets remain available:

- [World-State Variables & Observability](research/RESEARCH_STATE_VARIABLES.md)
- [Identifiability & Information Limits](research/RESEARCH_IDENTIFIABILITY.md)
- [Current Frontier Watch](research/RESEARCH_FRONTIER.md)
- [Source Map](research/survey/SOURCE_MAP.md)
- [Background Research](research/survey/BACKGROUND_RESEARCH.md)
- [Research Overview](research/survey/RESEARCH_OVERVIEW.md)
- [Frontier Methods](research/survey/FRONTIER_METHODS.md)
- [Papers & Primary Sources](research/survey/PAPERS.md)
- [Benchmarks & Tasks](research/survey/BENCHMARKS_TASKS.md)
- [Datasets & Code](research/survey/DATASETS_CODE.md)
- [Deep dossiers](research/dossiers/README.md)

These are supporting research records, not separate top-level project stages.

## “Vision alone” protocol

Observation protocol:

- `V0` — monocular RGB + temporal order;
- `V1` — V0 + camera intrinsics;
- `V2` — calibrated multi-camera RGB;
- `V3` — active embodied vision where action changes future visual evidence.

Learning provenance:

- `L0` — visual self-supervision;
- `L1` — visual labels/annotations;
- `L2` — language/world-knowledge supervision;
- `L3` — action-conditioned demonstrations/experience;
- `L4` — non-visual or privileged physical evidence.

This prevents “RGB at deployment” from being confused with “learned only from vision.”

## What we do not assume

Clover does **not** assume that CPU or GPU is scientifically superior, that explicit state must beat distributed latent state, that field/object/geometry/token must be the final primitive, that Transformer or non-Transformer is the answer, that prediction/reconstruction/generation is necessarily sufficient, or that one benchmark defines understanding.

Historical Clover mechanisms remain ideas until the research process supports or rejects them.

## Long-term product loop

```text
Vision
  ↓
World understanding
  ↓
Decision
  ↓
Tool / capability selection
  ↓
Execution
  ↓
new visual evidence
  └──────────────→ updated understanding
```

## Project definition

- [SSOT](SSOT.md)
- [Principles](PRINCIPLES.md)
- [Status](STATUS.md)
- [Roadmap](ROADMAP.md)
- [Research lifecycle](research/PIPELINE.md)
- [Active research inventory](research/RESEARCH.md)

---

**Research broadly. Analyze deeply. Synthesize comparatively. Innovate only from demonstrated gaps.**

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
4. [`research/RESEARCH_STATE_VARIABLES.md`](research/RESEARCH_STATE_VARIABLES.md) — what kinds of world state may matter.
5. [`research/RESEARCH_IDENTIFIABILITY.md`](research/RESEARCH_IDENTIFIABILITY.md) — what evidence can actually constrain hidden state.
6. [`research/RESEARCH_OBSERVATION_PHYSICS.md`](research/RESEARCH_OBSERVATION_PHYSICS.md) — how the world becomes RGB and where image formation destroys/aliases information.
7. [`research/RESEARCH_PHYSICAL_PROPERTIES.md`](research/RESEARCH_PHYSICAL_PROPERTIES.md) — hidden physical properties, contact/deformation, irreversible change and intervention datasets.
8. [`research/RESEARCH_SUFFICIENT_STATE.md`](research/RESEARCH_SUFFICIENT_STATE.md) — what an internal world state must preserve for different capabilities.
9. [`research/RESEARCH_STATE_ALIASING.md`](research/RESEARCH_STATE_ALIASING.md) — when different worlds/histories collapse into the same representation.
10. [`research/RESEARCH_ADAPTIVE_ABSTRACTION.md`](research/RESEARCH_ADAPTIVE_ABSTRACTION.md) — state granularity, hierarchy, timescale and task-conditioned abstraction.
11. [`research/RESEARCH_VALUE_OF_INFORMATION.md`](research/RESEARCH_VALUE_OF_INFORMATION.md) — active evidence acquisition, probing actions and information value.
12. [`research/RESEARCH_FRONTIER.md`](research/RESEARCH_FRONTIER.md) — current research edge through 2026-10-14.
13. [`AGENTS.md`](AGENTS.md) — operating rules for research and coding agents.
14. [`STATUS.md`](STATUS.md) — current stage and non-goals.
15. [`research/README.md`](research/README.md) — flat research navigation.

## Current stage — 1 Research

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

The current job is to collect and structure the problem space broadly before deciding what Clover itself should invent.

## Stage-1 question chain

The current foundation is organized around this chain:

```text
What relevant research exists?
        ↓
What state exists in the real world?
        ↓
How does that state become RGB evidence?
        ↓
What hidden state is identifiable from that evidence?
        ↓
Which physical properties require history, active views, interaction or non-visual sensing?
        ↓
What information must an internal state preserve?
        ↓
When has the representation aliased distinct worlds/histories?
        ↓
At what granularity / timescale should state be represented?
        ↓
When evidence is insufficient, what view / probe / action is worth taking next?
        ↓
Which current methods and benchmarks can discriminate competing answers?
```

This is a research map, not a proposed Clover architecture.

## Core Stage-1 distinctions

```text
pixels
≠
world state

statistically predictable from pixels
≠
physically identifiable from pixels

vision alone
≠
passive vision only

observationally indistinguishable worlds
≠
representation failure

information available but discarded
=
potential representation failure

complete physical description
≠
minimal predictive state
≠
minimal control-sufficient state
≠
general-purpose world state

one-task sufficiency
≠
future-task optionality

minimal state
≠
best state at every timescale

most informative action
≠
best action after accounting for cost / risk / irreversibility
```

## What Stage 1 currently covers

The inventory is intentionally wider than “world models” or “VLA.” It includes:

- inverse problems, observability, identifiability, uncertainty and POMDPs;
- human/developmental visual cognition;
- image formation / inverse rendering / camera acquisition;
- transparency, reflection, refraction, blur, rolling shutter and adverse visual conditions;
- classical geometry, SfM, VO and SLAM;
- optical flow, correspondence and tracking;
- static/video self-supervised representation;
- learned geometry, NeRF/3DGS/4D reconstruction;
- object-centric representation, scene graphs and semantic mapping;
- persistent/episodic memory and world change;
- hidden physical properties: mass, inertia, friction, stiffness, temperature, viscosity and material state;
- rigid, articulated, deformable, fluid and granular dynamics;
- irreversible topology change: cutting, splitting, merging and breakage;
- intuitive/quantitative/causal physical reasoning;
- active perception, active system identification and intervention;
- generative world models, world-action models and VLA/direct policies;
- belief state, predictive state, information state and representation sufficiency;
- state aliasing and Markov-state diagnostics;
- state abstraction, bisimulation, hierarchical / multi-timescale state;
- structured/equivariant memory;
- value of information, epistemic actions and probing-action safety;
- open-world hypothesis generation and non-stationarity;
- self/embodiment model mismatch;
- uncertainty calibration, OOD and continual/test-time adaptation;
- simulation/data engines, datasets, benchmarks and systems integration.

If another direction materially constrains the mother question, it should be added even if it does not fit an existing category.

## Later stages

### 2 Analysis

One important method → one small mechanism report.

### 3 Synthesis

Compare methods across common dimensions, strengths, weaknesses, trade-offs and failure modes.

### 4 Innovation

Only after a gap is well supported do Clover-original hypotheses become serious candidates.

### 5 Implementation

Build reproducible code.

### 6 Evaluation

Run experiments, ablations and real-world tests.

### 7 Reflection

Interpret failures, reject bad assumptions and begin the next research cycle.

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

Clover does **not** assume that CPU/GPU choice determines the science, that explicit state must beat distributed latent state, that field/object/geometry/token must be the final primitive, that hierarchy is automatically superior to flat state, that information gain is itself the final algorithm, that prediction/reconstruction/generation is necessarily sufficient, or that one benchmark defines understanding.

Historical Clover mechanisms remain ideas until the research process supports or rejects them.

## Project definition

- [SSOT](SSOT.md)
- [Principles](PRINCIPLES.md)
- [Status](STATUS.md)
- [Roadmap](ROADMAP.md)
- [Research lifecycle](research/PIPELINE.md)
- [Flat Stage-1 navigation](research/README.md)

---

**Research broadly. Analyze deeply. Synthesize comparatively. Innovate only from demonstrated gaps.**

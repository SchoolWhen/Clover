# Research

> **Research question:** How can a machine understand the real world through vision alone?
>
> **Long-term goal:** Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.

## Lifecycle

```text
1 Research
→ 2 Analysis
→ 3 Synthesis
→ 4 Innovation
→ 5 Implementation
→ 6 Evaluation
→ 7 Reflection
↺ next research cycle
```

**Current stage: 1 — Research.**  
Freshness checked through: **2026-10-14**.

## Stage-1 reading order

A new agent should read this chain before proposing architecture:

```text
PIPELINE.md
↓
RESEARCH.md
↓
RESEARCH_STATE_VARIABLES.md
↓
RESEARCH_IDENTIFIABILITY.md
↓
RESEARCH_OBSERVATION_PHYSICS.md
↓
RESEARCH_PHYSICAL_PROPERTIES.md
↓
RESEARCH_SUFFICIENT_STATE.md
↓
RESEARCH_FRONTIER.md
```

| File | Question it answers |
|---|---|
| [`PIPELINE.md`](PIPELINE.md) | What research stage are we in and what comes later? |
| [`RESEARCH.md`](RESEARCH.md) | What research directions, methods, datasets and benchmarks exist? |
| [`RESEARCH_STATE_VARIABLES.md`](RESEARCH_STATE_VARIABLES.md) | What kinds of state may exist in the real world? |
| [`RESEARCH_IDENTIFIABILITY.md`](RESEARCH_IDENTIFIABILITY.md) | What can be observed, predicted or identified from which evidence? |
| [`RESEARCH_OBSERVATION_PHYSICS.md`](RESEARCH_OBSERVATION_PHYSICS.md) | How do light transport, material, viewpoint, motion and camera acquisition distort or erase evidence before learning begins? |
| [`RESEARCH_PHYSICAL_PROPERTIES.md`](RESEARCH_PHYSICAL_PROPERTIES.md) | Which hidden physical properties and irreversible changes require history, interaction or non-visual evidence? |
| [`RESEARCH_SUFFICIENT_STATE.md`](RESEARCH_SUFFICIENT_STATE.md) | What information must an internal state preserve for prediction, control, planning, memory, causality and future tasks? |
| [`RESEARCH_FRONTIER.md`](RESEARCH_FRONTIER.md) | Which current primary/official sources materially change the research edge? |

## Current Stage-1 logic

```text
What exists in the literature?
        ↓
What state exists in the world?
        ↓
How does the world become an RGB observation?
        ↓
What evidence actually constrains hidden state?
        ↓
Which properties require interaction or stronger sensing?
        ↓
What information must a machine retain?
        ↓
Which current methods test competing answers?
```

## Non-negotiable distinctions

```text
pixels
≠
world state

world-state ambiguity
≠
image-formation ambiguity
≠
sensor/acquisition corruption

statistically predictable from pixels
≠
physically identifiable from pixels

passive observation
≠
active visual evidence
≠
physical intervention

plausible reconstruction
≠
true physical decomposition

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
```

## Evidence and protocol discipline

Observation protocol:

- `V0` — monocular RGB + temporal ordering;
- `V1` — V0 + camera intrinsics;
- `V2` — calibrated multi-camera RGB;
- `V3` — active embodied vision where action changes future visual evidence.

Learning provenance:

- `L0` — visual self-supervision;
- `L1` — visual labels/annotations;
- `L2` — language/world-knowledge supervision;
- `L3` — action-conditioned demonstrations/experience;
- `L4` — non-visual or privileged physical evidence.

Evidence levels:

```text
PRIMARY_PAPER
OFFICIAL_PROJECT
OPEN_SOURCE
OFFICIAL_REPORTED_RESULT
BACKGROUND_REFERENCE
SURVEY_SIGNAL
INTERNAL_HYPOTHESIS
OPEN
SUPERSEDED
```

Do not call a result vision-only merely because deployment uses RGB.

## Sufficiency annotation

When a source claims a compact state or representation, record what it is intended to preserve:

```text
S-PRED   prediction
S-CTRL   control
S-PLAN   planning
S-MEM    long-horizon memory / revision
S-CAUSE  intervention / counterfactuals
S-EPI    uncertainty / belief
S-OPEN   open-world / future-task optionality
```

A state sufficient for one fixed task is not automatically a general world representation.

## Current high-value foundations

Theory / state:

- POMDP robotics survey — https://arxiv.org/abs/2209.10342
- Predictive Representations of State — https://papers.nips.cc/paper_files/paper/2001/hash/1e4d36177d71bbb3558e43af9577d70e-Abstract.html
- Approximate Information State — https://www.jmlr.org/beta/papers/v23/20-1165.html
- Lambda Discrepancy — https://proceedings.neurips.cc/paper_files/paper/2024/hash/73073ccb3bc559fd001e66b9079d6d5e-Abstract-Conference.html
- Latent State Design under Sufficiency Constraints — https://arxiv.org/abs/2605.01694
- DELE-w0.5 — https://arxiv.org/abs/2608.22067
- Representation World Model — https://arxiv.org/abs/2609.29171

Observation physics:

- Recent Trends in Inverse Rendering — https://onlinelibrary.wiley.com/doi/full/10.1111/cgf.70592
- inverse-rendering ambiguity analysis — https://arxiv.org/abs/2404.12819
- Trans2Occ — https://arxiv.org/abs/2606.01777
- UnReflectAnything — https://arxiv.org/abs/2512.09583
- motion-blur VPR benchmark — https://arxiv.org/abs/2412.07751
- EvSLAM — https://arxiv.org/abs/2604.24033

Hidden physics / intervention:

- visual mass estimation — https://arxiv.org/abs/2601.20303
- ViTacPhys — https://arxiv.org/abs/2608.21355
- HEARTH — https://arxiv.org/abs/2609.23418
- DR-WM — https://arxiv.org/abs/2610.17630
- PointCast — https://arxiv.org/abs/2609.28393
- What-If World — https://arxiv.org/abs/2605.27589
- CRONOS — https://arxiv.org/abs/2605.23699
- CG-World — https://arxiv.org/abs/2607.26452

These are research materials, not Clover components.

## Supporting Stage-1 assets

Use these when deeper detail is needed:

- [`survey/SOURCE_MAP.md`](survey/SOURCE_MAP.md) — source → evidence → claim → limitation.
- [`survey/BACKGROUND_RESEARCH.md`](survey/BACKGROUND_RESEARCH.md) — broad background synthesis.
- [`survey/RESEARCH_OVERVIEW.md`](survey/RESEARCH_OVERVIEW.md) — visual map.
- [`survey/FRONTIER_METHODS.md`](survey/FRONTIER_METHODS.md) — method-family references.
- [`survey/PAPERS.md`](survey/PAPERS.md) — paper/project/code index.
- [`survey/BENCHMARKS_TASKS.md`](survey/BENCHMARKS_TASKS.md) — benchmark/task inventory.
- [`survey/DATASETS_CODE.md`](survey/DATASETS_CODE.md) — datasets and reproducibility resources.
- [`dossiers/`](dossiers/) — deeper topic notes, not separate project phases.

## Current rule

Do not promote Stage-1 material directly into Innovation.

```text
collect broadly
→ analyze methods one by one
→ synthesize trade-offs and common gaps
→ propose original hypotheses
→ implement
→ evaluate
→ reflect
```

**Research broadly first. Protect the question, not the current answer.**

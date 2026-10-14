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
RESEARCH_STATE_ALIASING.md
↓
RESEARCH_ADAPTIVE_ABSTRACTION.md
↓
RESEARCH_VALUE_OF_INFORMATION.md
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
| [`RESEARCH_STATE_ALIASING.md`](RESEARCH_STATE_ALIASING.md) | When do different worlds/histories collapse into the same internal state, and how can that failure be detected? |
| [`RESEARCH_ADAPTIVE_ABSTRACTION.md`](RESEARCH_ADAPTIVE_ABSTRACTION.md) | Should state granularity vary by task, timescale, event, uncertainty, space or embodiment? |
| [`RESEARCH_VALUE_OF_INFORMATION.md`](RESEARCH_VALUE_OF_INFORMATION.md) | When current evidence is insufficient, what view/probe/action is worth taking next to gain information? |
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
When has compression aliased distinct worlds?
        ↓
At what granularity / timescale should state be represented?
        ↓
What observation or intervention is worth acquiring next?
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

observationally indistinguishable states
≠
representation failure

information available but discarded
=
potential representation failure

minimal state
≠
best state at every timescale

most informative action
≠
best action after accounting for cost / risk / irreversibility
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

## Stage-1 abstraction / information annotations

When relevant, also record:

### Aliasing target

```text
A1 perceptual aliasing
A2 history aliasing
A3 representation aliasing
A4 action/embodiment aliasing
A5 causal aliasing
A6 task-conditioned aliasing
```

### Granularity mode

```text
G1 task-conditioned
G2 temporal / multi-timescale
G3 event-conditioned
G4 spatial coarse-to-fine
G5 entity / relation / role
G6 uncertainty-conditioned
G7 embodiment-conditioned
G8 open-world reserve / recoverability
```

### Information target

```text
V1 latent-state information
V2 parameter information
V3 mechanism information
V4 causal-structure information
V5 task-interpretation information
```

These are research bookkeeping labels, not Clover architecture primitives.

## Current high-value foundations

Theory / state:

- POMDP robotics survey — https://arxiv.org/abs/2209.10342
- Predictive Representations of State — https://papers.nips.cc/paper_files/paper/2001/hash/1e4d36177d71bbb3558e43af9577d70e-Abstract.html
- Approximate Information State — https://www.jmlr.org/beta/papers/v23/20-1165.html
- Lambda Discrepancy — https://proceedings.neurips.cc/paper_files/paper/2024/hash/73073ccb3bc559fd001e66b9079d6d5e-Abstract-Conference.html
- Compositional Behavioral Semantics for State Abstraction — https://proceedings.mlr.press/v306/zhang26dy.html
- PAMD visual bisimulation metrics — https://proceedings.mlr.press/v306/roh26a.html
- Latent State Design under Sufficiency Constraints — https://arxiv.org/abs/2605.01694
- DELE-w0.5 — https://arxiv.org/abs/2608.22067
- Representation World Model — https://arxiv.org/abs/2609.29171
- Observable quotient world models — https://doi.org/10.1016/j.knosys.2026.116768

Hierarchy / memory / granularity:

- Flow Equivariant World Models — https://proceedings.mlr.press/v306/lillemark26a.html
- HiMe — https://proceedings.mlr.press/v306/ji26k.html
- H-WM — https://arxiv.org/abs/2602.11291
- S2-HWM — https://arxiv.org/abs/2608.13103
- ViGAR — https://arxiv.org/abs/2610.02368
- Causal Bisimulation Modeling — https://ojs.aaai.org/index.php/AAAI/article/view/29507

Value of information / active evidence:

- Active inference and artificial reasoning — https://www.nature.com/articles/s41467-026-77209-5
- Active Perception for Embodied Disambiguation — https://arxiv.org/abs/2608.13605
- Vantage / Seek-and-View — https://arxiv.org/abs/2610.11810
- Sampling-based SysID with Active Exploration — https://proceedings.mlr.press/v305/sobanbabu25a.html
- DR-WM — https://arxiv.org/abs/2610.17630

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
- PointCast — https://arxiv.org/abs/2609.28393
- What-If World — https://arxiv.org/abs/2605.27589
- CRONOS — https://arxiv.org/abs/2605.23699
- CG-World — https://arxiv.org/abs/2607.26452

These are research materials, not Clover components.

## Additional Stage-1 coverage gaps discovered

Do not create a new top-level stage for these. Keep them visible in the Research backlog and promote them only when primary evidence is strong enough.

```text
open-world hypothesis generation
— detect when none of the current world-model hypotheses explain the evidence

non-stationarity / change-point detection
— detect when dynamics, embodiment, environment or task rules have changed

self / embodiment model
— distinguish external world dynamics from robot-body/controller/camera dynamics

representation reversibility
— after compression, can omitted distinctions be recovered from retained evidence/provenance?

multi-timescale / event-time state
— continuous fast dynamics vs sparse meaningful state transitions

structured / equivariant memory
— preserve out-of-view state under self-motion without brute-force history storage

epistemic-action safety
— information-gathering actions can be costly, destructive or unsafe

model-structure uncertainty
— uncertainty about which dynamics/causal model applies, not only uncertainty inside one model

meta-reasoning
— decide whether to think, look, move, probe, ask, wait or act
```

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

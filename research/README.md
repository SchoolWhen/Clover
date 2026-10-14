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
RESEARCH_OPEN_WORLD_EPISTEMICS.md
↓
RESEARCH_FRONTIER.md
```

| File | Question |
|---|---|
| [`RESEARCH.md`](RESEARCH.md) | What relevant research directions, methods, datasets and benchmarks exist? |
| [`RESEARCH_STATE_VARIABLES.md`](RESEARCH_STATE_VARIABLES.md) | What kinds of state may exist in the real world? |
| [`RESEARCH_IDENTIFIABILITY.md`](RESEARCH_IDENTIFIABILITY.md) | What can actually be observed or identified from which evidence? |
| [`RESEARCH_OBSERVATION_PHYSICS.md`](RESEARCH_OBSERVATION_PHYSICS.md) | How does image formation/camera acquisition distort or erase evidence before learning begins? |
| [`RESEARCH_PHYSICAL_PROPERTIES.md`](RESEARCH_PHYSICAL_PROPERTIES.md) | Which hidden physical properties and irreversible changes require history, interaction or non-visual evidence? |
| [`RESEARCH_SUFFICIENT_STATE.md`](RESEARCH_SUFFICIENT_STATE.md) | What information must state preserve for prediction, control, planning, memory, causality and future tasks? |
| [`RESEARCH_STATE_ALIASING.md`](RESEARCH_STATE_ALIASING.md) | When do different worlds/histories collapse into the same internal state? |
| [`RESEARCH_ADAPTIVE_ABSTRACTION.md`](RESEARCH_ADAPTIVE_ABSTRACTION.md) | At what task/time/space/uncertainty/embodiment granularity should state be maintained? |
| [`RESEARCH_VALUE_OF_INFORMATION.md`](RESEARCH_VALUE_OF_INFORMATION.md) | Which view, probe or intervention is worth acquiring next? |
| [`RESEARCH_OPEN_WORLD_EPISTEMICS.md`](RESEARCH_OPEN_WORLD_EPISTEMICS.md) | What if the hypothesis set is incomplete, the model is wrong/outdated, probing is unsafe, or another agent has hidden state? |
| [`RESEARCH_FRONTIER.md`](RESEARCH_FRONTIER.md) | Which current primary/official sources materially change the frontier? |

## Stage-1 logic

```text
literature / methods
↓
world variables
↓
observation process
↓
identifiability
↓
hidden physics / intervention
↓
sufficient state
↓
aliasing
↓
adaptive granularity
↓
value of information
↓
open-world model expansion / falsification / safety
↓
current frontier
```

## Non-negotiable distinctions

```text
pixels ≠ world state

world-state ambiguity
≠ image-formation ambiguity
≠ sensor/acquisition corruption

statistical predictability
≠ physical identifiability

passive observation
≠ active visual evidence
≠ physical intervention

complete physical description
≠ minimal predictive state
≠ minimal control-sufficient state
≠ general-purpose world state

observational indistinguishability
≠ representation failure

minimum state
≠ best state at every timescale

maximum information gain
≠ best safe action

uncertainty inside a known hypothesis set
≠ correct hypothesis missing from the set

uncertain current state
≠ current world model has become invalid

external-world state
≠ robot/self/embodiment state
```

## Protocol discipline

Observation protocol:

- `V0` — monocular RGB + temporal ordering;
- `V1` — V0 + camera intrinsics;
- `V2` — calibrated multi-camera RGB;
- `V3` — embodied active vision where action changes future visual evidence.

Learning provenance:

- `L0` — visual self-supervision;
- `L1` — visual labels/annotations;
- `L2` — language/world-knowledge supervision;
- `L3` — action-conditioned demonstrations/experience;
- `L4` — non-visual or privileged physical evidence.

Evidence labels:

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

Do not call a system vision-only merely because deployment input is RGB.

## State / uncertainty annotations

When useful, annotate claims with these research labels.

### Sufficiency

```text
S-PRED prediction
S-CTRL control
S-PLAN planning
S-MEM memory / revision
S-CAUSE intervention / counterfactuals
S-EPI uncertainty / belief
S-OPEN open-world / future-task optionality
```

### Aliasing

```text
A1 perceptual
A2 history
A3 representation
A4 action / embodiment
A5 causal
A6 task-conditioned
```

### Granularity

```text
G1 task-conditioned
G2 temporal / multi-timescale
G3 event-conditioned
G4 spatial coarse-to-fine
G5 entity / relation / role
G6 uncertainty-conditioned
G7 embodiment-conditioned
G8 open-world reserve / recoverability
G9 regime-conditioned
```

### Information target

```text
V1 latent-state information
V2 parameter information
V3 mechanism information
V4 causal-structure information
V5 task-interpretation information
```

### Open-world epistemic failure

```text
E1 observation uncertainty
E2 state uncertainty
E3 parameter uncertainty
E4 model-structure uncertainty
E5 hypothesis-set incompleteness
E6 regime change / model invalidation
E7 social / intentional uncertainty
E8 epistemic-action safety
```

These are bookkeeping labels for Research/Analysis, not Clover architecture primitives.

## High-value current references

State / abstraction:

- POMDP robotics survey — https://arxiv.org/abs/2209.10342
- Predictive Representations of State — https://papers.nips.cc/paper_files/paper/2001/hash/1e4d36177d71bbb3558e43af9577d70e-Abstract.html
- Approximate Information State — https://www.jmlr.org/beta/papers/v23/20-1165.html
- Lambda Discrepancy — https://proceedings.neurips.cc/paper_files/paper/2024/hash/73073ccb3bc559fd001e66b9079d6d5e-Abstract-Conference.html
- Compositional Behavioral Semantics — https://proceedings.mlr.press/v306/zhang26dy.html
- Latent State Design under Sufficiency Constraints — https://arxiv.org/abs/2605.01694
- DELE-w0.5 — https://arxiv.org/abs/2608.22067
- Representation World Model — https://arxiv.org/abs/2609.29171

Active evidence / safety:

- Active inference and artificial reasoning — https://www.nature.com/articles/s41467-026-77209-5
- Vantage — https://arxiv.org/abs/2610.11810
- DR-WM — https://arxiv.org/abs/2610.17630
- Splat-CBF — https://arxiv.org/abs/2609.23100
- ATOM-CBF — https://proceedings.mlr.press/v331/yun26a.html

Open-world epistemics / model mismatch:

- HUME — https://arxiv.org/abs/2607.06501 · https://open-world-planning.github.io/
- Changepoint-Aware World Models — https://arxiv.org/abs/2609.18950
- Feedback World Model — https://arxiv.org/abs/2605.15705
- Sirius-Fleet — https://proceedings.mlr.press/v270/liu25g.html
- Diffusion-Based Body Schema — https://arxiv.org/abs/2608.01029
- Embodiment Gap survey — https://arxiv.org/abs/2608.18433
- hidden-goal human–robot coordination — https://arxiv.org/abs/2608.04309

Observation / hidden physics:

- inverse rendering survey — https://onlinelibrary.wiley.com/doi/full/10.1111/cgf.70592
- Trans2Occ — https://arxiv.org/abs/2606.01777
- visual mass estimation — https://arxiv.org/abs/2601.20303
- ViTacPhys — https://arxiv.org/abs/2608.21355
- HEARTH — https://arxiv.org/abs/2609.23418
- PointCast — https://arxiv.org/abs/2609.28393
- What-If World — https://arxiv.org/abs/2605.27589
- CG-World — https://arxiv.org/abs/2607.26452

These are research materials and comparators, not Clover components.

## Remaining Stage-1 collection gaps

Keep collecting primary evidence for:

```text
unknown-unknown detection / open-set mechanism discovery
model-class selection / nonparametric world models
persistent provenance for hypotheses and refutations
scientific experiment design / falsification
self-model ↔ external-world-model coupling
representation reversibility after aggressive compression
safe exploration under irreversible actions
human-query / escalation cost models
social permission / consent for probing actions
multi-agent belief recursion
correlated uncertainty / model-ensemble collapse
long-horizon model drift and slow non-stationarity
```

Do not create a new top-level project stage for each gap.

## Supporting material

- [`survey/SOURCE_MAP.md`](survey/SOURCE_MAP.md)
- [`survey/BACKGROUND_RESEARCH.md`](survey/BACKGROUND_RESEARCH.md)
- [`survey/RESEARCH_OVERVIEW.md`](survey/RESEARCH_OVERVIEW.md)
- [`survey/FRONTIER_METHODS.md`](survey/FRONTIER_METHODS.md)
- [`survey/PAPERS.md`](survey/PAPERS.md)
- [`survey/BENCHMARKS_TASKS.md`](survey/BENCHMARKS_TASKS.md)
- [`survey/DATASETS_CODE.md`](survey/DATASETS_CODE.md)
- [`dossiers/`](dossiers/)

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

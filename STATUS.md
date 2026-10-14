# Clover Status

Last updated: 2026-10-14  
Stage-1 freshness checked through: **2026-10-14**

## Research question

> **How can a machine understand the real world through vision alone?**

## Long-term goal

> **Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.**

## Current stage

> **Stage 1 — Research / Survey & Evidence Collection — ACTIVE**

Lifecycle:

```text
1 Research
→ 2 Analysis
→ 3 Synthesis
→ 4 Innovation
→ 5 Implementation
→ 6 Evaluation
→ 7 Reflection
```

The immediate objective is **coverage before commitment**. No new Clover core representation or algorithm is currently frozen.

## Read first

1. [`SSOT.md`](SSOT.md)
2. [`research/PIPELINE.md`](research/PIPELINE.md)
3. [`research/RESEARCH.md`](research/RESEARCH.md)
4. [`research/RESEARCH_STATE_VARIABLES.md`](research/RESEARCH_STATE_VARIABLES.md)
5. [`research/RESEARCH_IDENTIFIABILITY.md`](research/RESEARCH_IDENTIFIABILITY.md)
6. [`research/RESEARCH_OBSERVATION_PHYSICS.md`](research/RESEARCH_OBSERVATION_PHYSICS.md)
7. [`research/RESEARCH_PHYSICAL_PROPERTIES.md`](research/RESEARCH_PHYSICAL_PROPERTIES.md)
8. [`research/RESEARCH_SUFFICIENT_STATE.md`](research/RESEARCH_SUFFICIENT_STATE.md)
9. [`research/RESEARCH_STATE_ALIASING.md`](research/RESEARCH_STATE_ALIASING.md)
10. [`research/RESEARCH_ADAPTIVE_ABSTRACTION.md`](research/RESEARCH_ADAPTIVE_ABSTRACTION.md)
11. [`research/RESEARCH_VALUE_OF_INFORMATION.md`](research/RESEARCH_VALUE_OF_INFORMATION.md)
12. [`research/RESEARCH_FRONTIER.md`](research/RESEARCH_FRONTIER.md)
13. [`research/README.md`](research/README.md)

## Current Stage-1 research surfaces

### 1. Broad research inventory

[`research/RESEARCH.md`](research/RESEARCH.md)

Collects methods, theories, datasets, benchmarks, projects and open directions across geometry, video representation, memory, physics, causality, active perception, world models, WAM/VLA, robot learning, uncertainty, continual learning and related areas.

### 2. World-state variables

[`research/RESEARCH_STATE_VARIABLES.md`](research/RESEARCH_STATE_VARIABLES.md)

Tracks candidate world-state dimensions such as geometry, identity/permanence, articulation, inertial/material/contact state, function, causal/controllability state and epistemic state, together with the evidence route used to constrain them.

### 3. Identifiability and information limits

[`research/RESEARCH_IDENTIFIABILITY.md`](research/RESEARCH_IDENTIFIABILITY.md)

Separates predictability, observability, identifiability, calibration and action sufficiency.

Central rule:

```text
statistically predictable from pixels
≠
physically identifiable from pixels
```

### 4. Observation physics

[`research/RESEARCH_OBSERVATION_PHYSICS.md`](research/RESEARCH_OBSERVATION_PHYSICS.md)

Studies how geometry/material/light/motion/camera acquisition create RGB evidence and ambiguity.

Central rule:

```text
world-state ambiguity
≠
image-formation ambiguity
≠
sensor/acquisition corruption
```

### 5. Hidden physical properties and irreversible change

[`research/RESEARCH_PHYSICAL_PROPERTIES.md`](research/RESEARCH_PHYSICAL_PROPERTIES.md)

Covers mass/inertia, friction, stiffness, temperature, fluids, granular media, contact/deformation, cutting/splitting/merging/breakage and intervention/counterfactual datasets.

Central rule:

```text
property useful for action
≠
property learned from vision alone
```

### 6. Minimum sufficient world state

[`research/RESEARCH_SUFFICIENT_STATE.md`](research/RESEARCH_SUFFICIENT_STATE.md)

Compares belief state, predictive state, information state, state abstraction/bisimulation and modern compact future-state/world-model representations.

Central rule:

```text
complete physical description
≠
minimal predictive state
≠
minimal control-sufficient state
≠
general-purpose world state
```

### 7. State aliasing and representation failure

[`research/RESEARCH_STATE_ALIASING.md`](research/RESEARCH_STATE_ALIASING.md)

Studies when different worlds or histories collapse into the same internal state even though they require different prediction, belief or action.

Important references include:

- perceptual aliasing / active perception — https://doi.org/10.1023/A:1022619109594
- λ-discrepancy — https://papers.nips.cc/paper_files/paper/2024/hash/73073ccb3bc559fd001e66b9079d6d5e-Abstract-Conference.html
- PO-PDDL — https://arxiv.org/abs/2606.15654
- Observable quotient world models — https://doi.org/10.1016/j.knosys.2026.116768
- Compositional Behavioral Semantics — https://proceedings.mlr.press/v306/zhang26dy.html

Central distinction:

```text
states indistinguishable from available evidence
≠
representation failure

necessary evidence existed but encoder discarded it
=
potential representation failure
```

### 8. Adaptive abstraction and state granularity

[`research/RESEARCH_ADAPTIVE_ABSTRACTION.md`](research/RESEARCH_ADAPTIVE_ABSTRACTION.md)

Studies task-conditioned, temporal, event-conditioned, spatial, entity/relation, uncertainty-conditioned and embodiment-conditioned abstraction.

Current references include:

- Causal Bisimulation Modeling — https://ojs.aaai.org/index.php/AAAI/article/view/29507
- Compositional Behavioral Semantics — https://proceedings.mlr.press/v306/zhang26dy.html
- H-WM — https://arxiv.org/abs/2602.11291
- S2-HWM — https://arxiv.org/abs/2608.13103
- HiMe — https://proceedings.mlr.press/v306/ji26k.html
- Flow Equivariant World Models — https://proceedings.mlr.press/v306/lillemark26a.html
- ViGAR — https://arxiv.org/abs/2610.02368

Central question:

```text
what should be represented
at what granularity
at what timescale
for which capability?
```

### 9. Value of information and probing actions

[`research/RESEARCH_VALUE_OF_INFORMATION.md`](research/RESEARCH_VALUE_OF_INFORMATION.md)

Studies information-seeking actions, active perception, Bayesian/epistemic experiment design, active system identification and safe probing.

Current references include:

- Active inference and artificial reasoning — https://www.nature.com/articles/s41467-026-77209-5
- Active Perception for Embodied Disambiguation — https://arxiv.org/abs/2608.13605
- Vantage — https://arxiv.org/abs/2610.11810
- Sampling-based SysID with Active Exploration — https://proceedings.mlr.press/v305/sobanbabu25a.html
- DR-WM — https://arxiv.org/abs/2610.17630

Central distinction:

```text
best task action
≠
most informative action
≠
best action after information value, cost, risk and irreversibility are combined
```

### 10. Current frontier

[`research/RESEARCH_FRONTIER.md`](research/RESEARCH_FRONTIER.md)

Tracks current primary/official work that materially changes the comparison space.

## Newly explicit Stage-1 coverage gaps

The current scan also keeps the following adjacent problems visible without creating new top-level phases:

```text
open-world hypothesis generation
— detect when none of the current hypotheses explain the evidence

non-stationarity / change-point detection
— detect changed dynamics, environment rules, embodiment or task distribution

self / embodiment model
— separate robot-body/controller/camera dynamics from external-world dynamics

representation reversibility
— recover previously omitted distinctions from retained evidence/provenance when a new task demands them

multi-timescale / event-time state
— distinguish continuous fast dynamics from sparse meaningful state transitions

structured / equivariant memory
— preserve state under self-motion/world motion without brute-force history

epistemic-action safety
— information-gathering actions may be costly, destructive or unsafe

model-structure uncertainty
— uncertainty over which model/causal mechanism applies, not only state uncertainty inside one model

meta-reasoning
— choose whether to think, look, move, probe, ask, wait or act
```

## Current non-goals

We are not currently:

- freezing a final representation;
- implementing a new Clover core architecture;
- optimizing leaderboard scores;
- claiming explicit state is superior to latent state;
- claiming compact state is automatically better than rich state;
- claiming hierarchy is automatically better than a flat state;
- claiming an information-gain objective is itself the Clover solution;
- claiming a direct policy is sufficient;
- claiming a generative world model is sufficient;
- treating photometric reconstruction as proof of physical-state recovery;
- treating dataset predictability as proof of physical identifiability;
- choosing hardware before the scientific mechanism;
- treating one benchmark as the definition of understanding.

## Stage-1 exit condition

Stage 2 Analysis becomes primary only when the research inventory is broad enough that a new agent can identify:

1. major competing research directions;
2. strongest representative methods and primary sources;
3. what evidence each method actually uses;
4. what its observation/image-formation assumptions are;
5. what world variables it attempts to represent;
6. what its representation is sufficient for;
7. how state aliasing could expose missing information;
8. what abstraction/granularity/timescale assumptions it makes;
9. whether it actively acquires information and what uncertainty that targets;
10. what datasets/benchmarks can discriminate its claims;
11. which capabilities remain unmeasured or under-specified;
12. which methods deserve one-method-one-report analysis.

## Not yet demonstrated

Clover has not yet publicly demonstrated a validated general real-world visual world model, a final representation, robust open-world generalization, general causal understanding, persistent long-horizon real-robot world state, a validated original algorithm, or a final hardware mapping.

These remain research targets.

# AGENTS.md — Clover Project Instructions

This file is mandatory reading for AI agents, coding agents, research agents and contributors.

## 1. Highest SSOT

> **Research question:** How can a machine understand the real world through vision alone?
>
> **Long-term product goal:** Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.

The question is fixed. The answer is open.

## 2. Mandatory reading order

Before proposing architecture, code, experiments or conclusions, read:

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
12. [`research/RESEARCH_OPEN_WORLD_EPISTEMICS.md`](research/RESEARCH_OPEN_WORLD_EPISTEMICS.md)
13. [`research/RESEARCH_MODEL_DISCOVERY.md`](research/RESEARCH_MODEL_DISCOVERY.md)
14. [`research/RESEARCH_FRONTIER.md`](research/RESEARCH_FRONTIER.md)
15. [`PRINCIPLES.md`](PRINCIPLES.md)
16. [`STATUS.md`](STATUS.md)
17. [`research/README.md`](research/README.md)
18. [`research/survey/SOURCE_MAP.md`](research/survey/SOURCE_MAP.md)
19. deeper survey/dossier files only as needed.

Historical/news files are evidence signals, not SSOT.

## 3. Lifecycle

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

**Current active stage: Stage 1 — Research.**

Do not prematurely freeze a Clover representation or core algorithm.

## 4. Research rules

### 4.1 Protect the question, not an old answer

CPU/GPU choices, field crystallization, visual charge, CSP, SEP, epistemic licences, LCPS/GCPS, Visual World Compiler, Evidence Replay, explicit state, latent state, object-centric state, Transformer/non-Transformer and historical Clover mechanisms are hypotheses or engineering choices, not axioms.

### 4.2 Research before Innovation

```text
broad Research
→ method Analysis
→ comparative Synthesis
→ demonstrated unresolved gap
→ Innovation hypothesis
→ Implementation
→ Evaluation
→ Reflection
```

Do not choose a preferred representation first and search for justification afterward.

### 4.3 Benchmarks are instruments

A benchmark score is evidence about a capability, not the definition of understanding.

### 4.4 No framework stacking

For every external method, record:

```text
problem
what it actually demonstrates
what it does not demonstrate
representation / mechanism
input / learning provenance
observation assumptions
code / dataset / benchmark
competing method / counter-hypothesis
```

Do not import a method into Clover merely because it is strong.

### 4.5 Source traceability

Use and preserve:

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

Preserve exact URLs. Company reports and news do not become scientific fact silently.

## 5. Vision-only discipline

Observation protocol:

- `V0`: monocular RGB + temporal order;
- `V1`: V0 + camera intrinsics;
- `V2`: calibrated multi-camera RGB;
- `V3`: active embodied vision where action changes future visual evidence.

Learning provenance:

- `L0`: visual self-supervision;
- `L1`: visual labels/annotations;
- `L2`: language/world-knowledge supervision;
- `L3`: action-conditioned demonstrations/experience;
- `L4`: non-visual / privileged physical evidence.

Do not call a system “learned from vision alone” just because deployment input is RGB.

## 6. Observation is not world state

Record camera/image-formation assumptions when material:

```text
camera model
viewpoint / calibration
illumination
reflectance / material
transparency / refraction
specular reflection
occlusion
motion blur
rolling shutter
exposure / dynamic range
sensor noise / compression
```

Keep distinct:

```text
world-state ambiguity
≠ image-formation ambiguity
≠ sensor/acquisition corruption
```

Photometric reconstruction is not proof of true physical decomposition.

## 7. Predictability is not identifiability

A model predicting mass, material, friction, temperature or another hidden variable does not prove that the variable is uniquely determined by visual evidence.

Record dependence on priors, scale, temporal history, active viewpoints, interventions, language knowledge, non-visual sensing and privileged simulator state.

When several worlds remain compatible with the evidence, uncertainty can be the correct output.

## 8. State sufficiency must be named

```text
S-PRED prediction
S-CTRL control
S-PLAN planning
S-MEM memory / revision
S-CAUSE intervention / counterfactuals
S-EPI uncertainty / belief
S-OPEN open-world / future-task optionality
```

Task sufficiency is not automatically general world understanding.

## 9. Diagnose aliasing

```text
A1 perceptual
A2 history
A3 representation
A4 action / embodiment
A5 causal
A6 task-conditioned
```

If evidence itself cannot distinguish two worlds, do not call that a representation failure. If discriminating evidence existed but was discarded, it may be one.

## 10. Abstraction must state what it preserves

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

Minimal state is not automatically better; maximal detail is not automatically better.

## 11. Information-gathering actions are first-class

Distinguish information about:

```text
V1 latent state
V2 parameters
V3 mechanism
V4 causal structure
V5 task interpretation
```

Record time, energy, risk, irreversibility, world disturbance, safety and social/permission cost.

The most informative action is not automatically the best action.

## 12. Open-world epistemic failure must remain possible

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

A credible agent must be allowed to represent:

```text
none of my current hypotheses explain this
my model may be wrong
my model used to work but the world changed
I need more evidence
that experiment is unsafe or impermissible
I should ask for help / abstain
```

Do not force probability mass onto a known-wrong model set.

## 13. Scientific model discovery is distinct from state estimation

Keep separate:

```text
state estimation
parameter estimation
model selection
mechanism / causal-structure discovery
open-world hypothesis generation
falsification
model expansion
```

When a source claims discovery, record:

```text
candidate hypothesis class
assumptions that make identification possible
which intervention/evidence discriminates hypotheses
what remains observationally equivalent
how rejected hypotheses are recorded
whether new hypotheses can be introduced
```

Reflection is not falsification. A new explanation is not established until it survives evidence that could have rejected it.

## 14. Experiment design must account for misspecification

Expected information gain alone is not automatically a correct probing objective when the model class is wrong.

When relevant record:

```text
informativeness
representativeness
model-misspecification sensitivity
safety / physical constraints
cost / budget
irreversibility
social permission
```

An experiment can be highly informative under the assumed model and still make the system confidently more wrong.

## 15. Preserve hypothesis provenance and refutation history

For scientific/model-discovery claims, record when possible:

```text
hypothesis statement
scope / assumptions
provenance
supporting evidence
counterevidence
predictions made before outcomes
experiments/interventions performed
reason for rejection / supersession
regime in which it may still apply
```

Do not silently resurrect a falsified hypothesis without new evidence or a documented regime change.

## 16. Self / embodiment is part of state

Do not assume the robot body, controller, camera mounting or actuator response is fixed forever.

Distinguish external-world change from body/controller/camera/action-semantics change.

## 17. Social hidden state is not directly observed

Keep distinct:

```text
visible action
short-term intention
goal
belief
belief about another belief
preference
permission / ownership / social norm
```

Do not turn a Theory-of-Mind inference into an observed fact. Recursive belief depth is a modeling cost/necessity question, not something to maximize automatically.

## 18. Plausible generation is not world truth

Keep distinct:

```text
observed
inferred
predicted
hypothetical / generated
ambiguous
unobserved
contradicted
refuted
model-incomplete
```

## 19. Stage-1 contribution template

Record as much as known:

- direction;
- name/version/date;
- primary paper URL;
- official project/code/checkpoint;
- dataset/benchmark;
- evidence level;
- input/training provenance;
- observation/image-formation assumptions;
- world variables represented;
- sufficiency target;
- aliasing failure addressed/introduced;
- abstraction/granularity assumption;
- information-gathering mechanism and cost;
- open-world epistemic failure type (`E1–E8`);
- hypothesis class / identifiability assumptions when relevant;
- experiment/falsification mechanism when relevant;
- hypothesis provenance/refutation handling when relevant;
- demonstrated capability;
- limitation/open question.

Do not turn a collection record into an architecture decision.

## 20. Coding agents

Do not rewrite research claims to match current code. Small diagnostic code is allowed before Stage 5 only when genuinely needed to answer a research question. Core algorithm implementation belongs downstream of Innovation.

## 21. Research agents

During Stage 1:

1. search broadly, including outside current categories;
2. upgrade discovery signals to primary/official sources;
3. preserve exact URLs;
4. record code/datasets/benchmarks;
5. summarize claims conservatively;
6. distinguish learning/evidence provenance from deployment input;
7. record observation assumptions;
8. state representation sufficiency target;
9. test for aliasing / discarded information;
10. record granularity/timescale assumptions;
11. record active evidence acquisition and its risk/cost;
12. ask whether the model/hypothesis set can itself be wrong or incomplete;
13. record the assumptions required for causal/mechanism identification;
14. preserve hypothesis/refutation provenance when available;
15. keep self/embodiment and social hidden state visible;
16. record missing research areas explicitly;
17. do not import external mechanisms into Clover by default.

## Final rule

> **Research broadly. Analyze deeply. Synthesize comparatively. Innovate only from demonstrated gaps.**
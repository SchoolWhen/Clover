# AGENTS.md — Clover Project Instructions

This file is mandatory reading for AI agents, coding agents, research agents and contributors.

## 1. Highest SSOT

> **Research question:** How can a machine understand the real world through vision alone?
>
> **Long-term product goal:** Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.

The question is fixed. The answer is open.

## 2. Mandatory reading order and document ownership

1. [SSOT.md](SSOT.md#topic-ssot) — fixed question and scientific contract.
2. [STATUS.md](STATUS.md) — the only current progress and stage authority.
3. [RESEARCH.md](RESEARCH.md) — breadth, competing fields and coverage.
4. [PROCESS.md](PROCESS.md) — lifecycle and contribution templates.
5. Read the relevant canonical topic: [questions](QUESTIONS.md), [perception](PERCEPTION.md), [representation](REPRESENTATION.md), [action](ACTION.md), [learning](LEARNING.md), [systems](SYSTEMS.md), [evaluation](EVALUATION.md), [sources](SOURCES.md), [hypotheses](HYPOTHESES.md).

Maintain each topic in place. One method means one structured section, not one new file. Do not create dated research supplements, patch reports, per-question progress files, duplicate indexes, archive trees or news editions. Fold verified discoveries into the topic and SOURCES.md; update STATUS.md for material progress. Preserve exact evidence URLs, reading depth, assumptions, counterevidence and refutation history. Git commits preserve prior versions. Add a file only when an existing topic genuinely cannot own its content.

Source record dates are not the document maintenance date. A merge or cleanup never upgrades an inherited source to newly verified evidence. Dated audit recommendations remain historical; STATUS.md governs the current stage. The former timestamped news-publication rule is retired by the 2026-10-25 repository simplification.

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

Do not prematurely freeze a Clover representation, foundation backbone or core algorithm.

## 4. Research rules

### 4.1 Protect the question, not an old answer

CPU/GPU choices, DeepSeek/Qwen/other vendor backbones, field crystallization, visual charge, CSP, SEP, epistemic licences, LCPS/GCPS, Visual World Compiler, Evidence Replay, explicit state, latent state, object-centric state, Transformer/non-Transformer and historical Clover mechanisms are hypotheses or engineering choices, not axioms.

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

Do not choose a preferred representation/backbone first and search for justification afterward.

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

When a source claims discovery, record candidate hypothesis class, identifiability assumptions, discriminating evidence/interventions, remaining equivalence classes, refutation handling and whether new hypotheses can be introduced.

Reflection is not falsification.

## 14. Experiment design must account for misspecification

Expected information gain alone is not automatically a correct probing objective when the model class is wrong.

Record informativeness, representativeness, misspecification sensitivity, safety/physical constraints, cost/budget, irreversibility and social permission.

## 15. Preserve hypothesis provenance and refutation history

For scientific/model-discovery claims, preserve when possible:

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

Keep distinct visible action, short-term intention, goal, belief, recursive belief, preference, permission/ownership and social norm.

Do not turn a Theory-of-Mind inference into an observed fact.

## 18. Foundation-model systems provenance is mandatory

When a method depends on an LLM/VLM/foundation backbone, do not record only the family name.

Record when material:

```text
exact backbone + version / checkpoint / API model
open weights vs hosted/API artifact
license
modalities in the exact artifact
total parameters
active parameters per token
attention / sequence architecture
MoE routing / expert count if relevant
visual/video tokenizer
image resolution / patch / token budget
video frame sampling / timestamp representation
multimodal fusion
native / extended context length
KV/cache precision + memory cost
training-data provenance / mixture / alignment
post-training method
precision / quantization
runtime / compiler / custom kernels
parallelism / expert communication
harness / tools / external memory
reasoning-effort setting
local Mac-M4 feasibility
```

Keep explicit:

```text
scientific world-state hypothesis
≠ backbone architecture
≠ training recipe
≠ runtime
≠ harness
```

Also:

```text
long context ≠ persistent grounded memory
serving KV cache ≠ epistemic world memory
base model ≠ model + harness ≠ model + tools/memory
hosted product ≠ open-weight checkpoint unless verified
total params ≠ active params ≠ memory ≠ communication cost
```

DeepSeek/Qwen are current high-value systems references, not default Clover choices. See [`SYSTEMS.md`](SYSTEMS.md#topic-research-foundation_models-deepseek_qwen).

## 19. Data/training gains must be separated from architecture gains

For foundation/embodied models, track:

```text
data source + hours/tokens/examples
robot vs human vs synthetic
cross-embodiment alignment
coordinate/action normalization
temporal synchronization
filtering / deduplication
curriculum
SFT / RL / preference / distillation
deployment-rollout reuse
```

Do not attribute a gain to architecture if data scale/alignment/post-training changed simultaneously.

Synthetic data is not observed physical evidence; preserve its provenance.

## 20. Visual tokenization is part of the observation bottleneck

For multimodal backbones, image/video preprocessing can discard evidence before world-state reasoning starts.

Later comparisons should test:

```text
resolution / patch size
pixel-unshuffle / pooling
token pruning / merging
frame rate / sampling
multi-view synchronization
visual cache reuse
```

against physical/spatial/permanence capability under matched memory/latency budgets.

## 21. Agent harness contribution must be measured

Modern agent benchmarks often measure a system rather than a base model.

Preserve:

```text
harness name/version
prompt/protocol
tools/plugins/MCP
external VLM/perception helpers
retrieval/memory subsystem
retry policy
parallel-tool policy
sandbox/browser/shell
reasoning effort
```

A DeepSeek/Qwen/vendor result that includes an agent harness must not be compared directly to a bare model without marking the difference.

## 22. Engineering feasibility is part of the evidence chain

Current local development reference:

```text
Mac mini with Apple M4
```

Treat it as a measured reference environment, not a scientific constraint and not the assumed final robot computer.

Keep distinct:

```text
current development machine
≠ final edge computer
≠ scientific representation hypothesis
```

For performance claims record hardware/RAM, OS/runtime/backend, precision/quantization, input resolution/context, cold load, first inference, warm p50/p95/p99, peak memory and sustained/thermal behavior.

When relevant measure full camera→state→decision→action latency, not only isolated model inference.

## 23. Simulation evidence must be tiered

Use this validation ladder when applicable:

```text
EV0 mathematical / synthetic diagnostic
EV1 controlled single-simulator test
EV2 randomized in-simulator robustness
EV3 sim-to-sim transfer
EV4 offline real-data validation
EV5 real-to-sim / digital-twin validation
EV6 deployment-runtime / compute hardware in the loop
EV7 proxy physical hardware
EV8 target real robot
```

Do not call EV0–EV6 “sim2real success.”

Current absence of a target real robot is a constraint on claim strength, not a reason to postpone validation.

### Simulation-specific provenance

Record simulator/version, physics engine/solver, physics timestep, renderer, assets/hashes, camera settings, control frequency, latency/noise models, collision/contact/friction parameters, randomization distributions and privileged simulator state used.

### Failure attribution

Distinguish scenario/configuration bug, simulator/solver artifact, synthetic visual shortcut, actuator/controller mismatch, simulator overfit, genuine algorithmic failure and reality-gap failure.

## 24. Hardware-aware optimization must preserve capability

Quantization, pruning, state compression, lower resolution, shorter context, batching and asynchronous execution may change scientific behavior.

Later ablations should ask:

```text
Does visual-token reduction damage physical-state retention?
Does KV/cache quantization damage uncertainty calibration?
Does memory pruning damage object permanence or revision?
Does shorter history introduce state aliasing?
Does batching/remote execution violate deadlines?
Does async execution make belief stale?
Does a custom kernel/backend change state numerically over long horizons?
```

Speed alone is not a sufficient optimization metric.

## 25. Plausible generation is not world truth

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

## 26. Stage-1 contribution template

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
- hypothesis provenance/refutation handling;
- exact foundation backbone/artifact when relevant;
- total/active parameters, attention, visual-token/context/cache assumptions when relevant;
- data mixture/alignment/post-training when relevant;
- runtime/kernel/harness/tool assumptions when relevant;
- deployment/runtime assumptions;
- validation-evidence level (`EV0–EV8`);
- simulator/runtime/hardware provenance;
- demonstrated capability;
- limitation/open question.

Do not turn a collection record into an architecture decision.

## 27. Coding agents

Do not rewrite research claims to match current code. Small diagnostic code is allowed before Stage 5 only when genuinely needed to answer a research question. Core algorithm implementation belongs downstream of Innovation.

## 28. Research agents

During Stage 1:

1. search broadly, including outside current categories;
2. upgrade discovery signals to primary/official sources;
3. preserve exact URLs and exact model artifacts;
4. record code/datasets/benchmarks;
5. summarize claims conservatively;
6. distinguish learning/evidence provenance from deployment input;
7. record observation assumptions;
8. state representation sufficiency target;
9. test for aliasing/discarded information;
10. record granularity/timescale assumptions;
11. record active evidence acquisition and risk/cost;
12. ask whether the model/hypothesis set can be wrong/incomplete;
13. record causal/mechanism-identification assumptions;
14. preserve hypothesis/refutation provenance;
15. keep self/embodiment and social hidden state visible;
16. separate architecture gains from data/post-training gains;
17. separate base-model capability from harness/tool/memory capability;
18. record total vs active parameters and visual/context/cache budgets when material;
19. record runtime/kernel/hardware dependencies when they affect claimed efficiency;
20. record local-M4 feasibility vs remote/frontier-only comparison;
21. classify simulation/real-world evidence conservatively;
22. record missing research areas explicitly;
23. do not import external mechanisms into Clover by default.

## Final rule

> **Research broadly. Analyze deeply. Synthesize comparatively. Innovate only from demonstrated gaps.**

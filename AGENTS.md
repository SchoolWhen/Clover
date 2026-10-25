# AGENTS.md — Clover Project Instructions

This file is mandatory reading for AI agents, coding agents, research agents and contributors.

## 1. Highest SSOT

> **Research question:** How can a machine understand the real world through vision alone?
>
> **Long-term product goal:** Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.

The question is fixed. The answer is open.

**Model objective:** pure-vision AGI with natively ultrafast computation and broad visual understanding. Core computer-vision functions—recognition, detection, segmentation, tracking, correspondence, pose, counting and visual reading—are mandatory research/capability dimensions alongside memory, spatial/physical/causal reasoning and action usefulness. A robotic brain is a long-term application; do not reduce the model's scope to robotics, video generation or a single world-state task. These are targets, not demonstrated Clover results. Read the full scope and speed contract in SSOT.md.

## 2. Mandatory reading order and document ownership

1. [`SSOT.md`](SSOT.md) — the fixed research question and scientific contract, binding on every stage.
2. [`PROCESS.md`](PROCESS.md) — the common lifecycle, stage boundaries, contribution and evidence rules.
3. [`STATUS.md`](STATUS.md) — the only current project-progress and active-stage authority.
4. Read the owning stage's README and then the relevant direction document. The current research entry is [Stage 1](01-research/README.md).

Root scope is shared across stages: research contract, agent rules, process, global status and the bilingual homepage. Stage-specific material belongs under `01-research/` through `07-reflection/`. Within a stage, prefer one file per direction and structured sections per method/question. Do not add date-named supplements, per-question update files, duplicate indexes or news editions. Introduce a direction file only when its content has a distinct continuing owner.

Update the existing direction document in place. Fold Stage-1 verified discoveries into its topic and source map; register method analysis in Stage 2, comparative synthesis in Stage 3, candidate innovation in Stage 4, implementation in Stage 5, experiments/results in Stage 6 and interpretation in Stage 7. A benchmark survey is Stage 1; an executed benchmark result is Stage 6. A historical hypothesis may be housed in Stage 4 without being adopted or making that stage active.

Preserve exact source URLs, reading depth, assumptions, counterevidence, falsifiers and refutation history. Source dates are not maintenance dates. Moves, merges and directory creation never upgrade evidence or imply stage completion. Git commits preserve prior versions; do not retain obsolete path shells or archive trees. STATUS.md alone governs the current stage.

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

The active stage is recorded only in [`STATUS.md`](STATUS.md); the same scientific controls apply to every stage.

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

DeepSeek/Qwen are current high-value systems references, not default Clover choices. See [`01-research/foundation-models-and-systems.md`](01-research/foundation-models-and-systems.md#topic-research-foundation_models-deepseek_qwen).

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

## 26. Stage-specific contribution templates

The Stage-1 source template and collection rules live in [`01-research/README.md`](01-research/README.md). Each later stage owns its template in its README; all remain subordinate to this file and SSOT.md.

## 27. Coding agents

Do not rewrite research claims to match current code. Small diagnostic code is allowed before Stage 5 only when genuinely needed to answer a research question. Core algorithm implementation belongs downstream of Innovation.

## 28. Research agents

During Stage 1, follow the collection rules in [`01-research/README.md`](01-research/README.md). Research outputs stay with their direction; do not route a source record into a later stage solely because it mentions training, evaluation or innovation.

## Final rule

> **Research broadly. Analyze deeply. Synthesize comparatively. Innovate only from demonstrated gaps.**

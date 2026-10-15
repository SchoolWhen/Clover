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
Freshness checked through: **2026-10-15**.

## Stage-1 reading order

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
RESEARCH_MODEL_DISCOVERY.md
↓
RESEARCH_FOUNDATION_MODEL_SYSTEMS.md
↓
RESEARCH_TRAINING_POSTTRAINING.md
↓
RESEARCH_ENGINEERING_VALIDATION.md
↓
RESEARCH_FRONTIER.md
```

| File | Question |
|---|---|
| [`RESEARCH.md`](RESEARCH.md) | What relevant directions, methods, datasets and benchmarks exist? |
| [`RESEARCH_STATE_VARIABLES.md`](RESEARCH_STATE_VARIABLES.md) | What kinds of state may exist in the real world? |
| [`RESEARCH_IDENTIFIABILITY.md`](RESEARCH_IDENTIFIABILITY.md) | What can actually be observed or identified from which evidence? |
| [`RESEARCH_OBSERVATION_PHYSICS.md`](RESEARCH_OBSERVATION_PHYSICS.md) | How does image formation/camera acquisition distort or erase evidence? |
| [`RESEARCH_PHYSICAL_PROPERTIES.md`](RESEARCH_PHYSICAL_PROPERTIES.md) | Which hidden physical properties and irreversible changes require history, interaction or stronger sensing? |
| [`RESEARCH_SUFFICIENT_STATE.md`](RESEARCH_SUFFICIENT_STATE.md) | What information must state preserve for prediction, control, planning, memory, causality and future tasks? |
| [`RESEARCH_STATE_ALIASING.md`](RESEARCH_STATE_ALIASING.md) | When do different worlds/histories collapse into the same internal state? |
| [`RESEARCH_ADAPTIVE_ABSTRACTION.md`](RESEARCH_ADAPTIVE_ABSTRACTION.md) | At what task/time/space/uncertainty/embodiment granularity should state be maintained? |
| [`RESEARCH_VALUE_OF_INFORMATION.md`](RESEARCH_VALUE_OF_INFORMATION.md) | Which view, probe or intervention is worth acquiring next? |
| [`RESEARCH_OPEN_WORLD_EPISTEMICS.md`](RESEARCH_OPEN_WORLD_EPISTEMICS.md) | What if the hypothesis set is incomplete, the model is wrong/outdated, probing is unsafe, or another agent has hidden state? |
| [`RESEARCH_MODEL_DISCOVERY.md`](RESEARCH_MODEL_DISCOVERY.md) | How should hypotheses, mechanisms, experiments, falsification and provenance be managed when the model class itself may be wrong? |
| [`RESEARCH_FOUNDATION_MODEL_SYSTEMS.md`](RESEARCH_FOUNDATION_MODEL_SYSTEMS.md) | How do backbone architecture, multimodal tokenization, data, MoE/attention, context/cache, kernels and agent harness alter what is scientifically and operationally possible? |
| [`RESEARCH_TRAINING_POSTTRAINING.md`](RESEARCH_TRAINING_POSTTRAINING.md) | How do pretraining, co-training, SFT/behavior cloning, distillation, RL, simulated training and deployment learning alter representation, generalization and robot behavior? |
| [`RESEARCH_ENGINEERING_VALIDATION.md`](RESEARCH_ENGINEERING_VALIDATION.md) | Can candidate models run under realistic edge constraints, and how should evidence graduate from simulation toward real-robot validation? |
| [`RESEARCH_FRONTIER.md`](RESEARCH_FRONTIER.md) | Which current primary/official sources materially change the comparison space? |

Supporting material:

- [`foundation_models/`](foundation_models/) — DeepSeek/Qwen and foundation-model systems watches/matrices;
- [`training/`](training/) — controlled training variables and high-risk post-training boundary questions;
- [`engineering/`](engineering/) — deployment lifecycle, fault injection, runtime reliability and validation resources;
- [`emerging/`](emerging/) — dated audits for fast-moving cross-boundary clusters; current audit covers embodied JEPA, RSI, VLA test-time scaling, WAM runtime acceleration and generative-video perception;
- [`survey/`](survey/) / [`dossiers/`](dossiers/) — source maps, datasets, benchmarks and deeper topic notes.

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
open-world uncertainty / model mismatch
↓
model discovery / experiment / falsification
↓
foundation-model architecture / data / runtime / harness
↓
training / post-training / embodied learning regime
↓
engineering feasibility / simulation / validation ladder
↓
current frontier / emerging cross-boundaries
```

## Non-negotiable distinctions

```text
pixels ≠ world state
statistical predictability ≠ physical identifiability
passive observation ≠ active visual evidence ≠ physical intervention
observational indistinguishability ≠ representation failure
complete physical description ≠ predictive/control/general-purpose sufficient state
long context ≠ persistent grounded world memory
serving KV cache ≠ epistemic world memory
base model ≠ model + harness ≠ model + harness + external tools
base policy ≠ policy + verifier/search/test-time compute
hosted product ≠ open-weight checkpoint unless exact artifact is verified
total parameters ≠ active parameters ≠ memory footprint ≠ communication cost
architecture efficiency on paper ≠ realized efficiency on available kernels/hardware
architecture ≠ training recipe ≠ data mixture ≠ post-training objective
supervised task success ≠ on-policy robustness
LLM post-training ≠ robot post-training
more heterogeneous robot data ≠ better transfer without alignment
cross-embodiment state alignment ≠ cross-embodiment action alignment
reasoning improvement ≠ perception preservation
minimum state ≠ best state at every timescale
maximum information gain ≠ best safe / permitted experiment
uncertainty inside a known hypothesis set ≠ correct hypothesis missing from the set
uncertain current state ≠ current world model has become invalid
parameter estimation ≠ model selection ≠ mechanism discovery ≠ open-world model expansion
reused inference state ≠ valid inference state
self-evolution ≠ demonstrated self-improvement
RSI evolve-set gain ≠ held-out / OOD gain
current development machine ≠ final robot edge computer ≠ scientific hypothesis
model latency ≠ end-to-end closed-loop latency
same-simulator success ≠ sim2sim robustness ≠ sim2real transfer ≠ real-world validation
benchmark success ≠ runtime reliability
model accuracy ≠ hardware-setup robustness
reflection ≠ falsification
current best hypothesis ≠ permanent truth
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

Do not call a system vision-only merely because deployment input is RGB.

## Research bookkeeping labels

### Sufficiency
`S-PRED` prediction · `S-CTRL` control · `S-PLAN` planning · `S-MEM` memory/revision · `S-CAUSE` intervention/counterfactual · `S-EPI` uncertainty/belief · `S-OPEN` future-task/open-world optionality.

### Aliasing
`A1` perceptual · `A2` history · `A3` representation · `A4` action/embodiment · `A5` causal · `A6` task-conditioned.

### Granularity
`G1` task · `G2` temporal · `G3` event · `G4` spatial · `G5` entity/relation/role · `G6` uncertainty · `G7` embodiment · `G8` recoverability · `G9` regime.

### Information target
`V1` latent state · `V2` parameters · `V3` mechanism · `V4` causal structure · `V5` task interpretation.

### Open-world epistemic failure
`E1` observation · `E2` state · `E3` parameter · `E4` model structure · `E5` hypothesis-set incompleteness · `E6` regime/model invalidation · `E7` social/intentional · `E8` epistemic-action safety.

### Training regime

```text
TR0  base pretraining
TR1  continued/domain pretraining
TR2  SFT / behavior cloning
TR3  co-training / auxiliary objectives
TR4  preference / conservative offline alignment
TR5  verifier/reward RL
TR6  online embodied RL
TR7  on-policy distillation
TR8  strong-to-weak distillation
TR9  simulated/world-model post-training
TR10 deployment-rollout/self-improvement
TR11 continual/test-time adaptation
```

### Validation evidence ladder
`EV0` synthetic/math · `EV1` controlled sim · `EV2` randomized sim · `EV3` sim2sim · `EV4` offline real data · `EV5` real2sim/digital twin · `EV6` deployment-runtime HIL · `EV7` proxy hardware · `EV8` target robot.

These are Research/Analysis labels, not Clover architecture primitives.

## Foundation-model systems fields

For methods built on frontier LLM/VLM backbones, record when relevant:

```text
backbone + exact version / artifact
open weights vs API/hosted only
license
modalities
total params / active params
attention / sequence architecture
visual/video tokenizer + token budget
context length + KV/cache cost
multimodal fusion
training-data provenance / mixture / alignment
pretraining + post-training stages
on/off-policy interaction
reward / verifier / teacher source
which modules are frozen / updated
precision / quantization
runtime / kernels / parallelism
harness / tools / external memory
reasoning-effort setting
test-time sampling / verifier / search budget
inference-state reuse + refresh criterion
local Mac-M4 feasibility
```

For self-improving systems additionally record:

```text
editable surface: model / data / harness / code / memory
immutable evaluator / safety boundary
evolve-set vs held-out evaluation
accepted-change inheritance
lineage / rollback
research / training budget
whether improvements persist across later cycles
```

DeepSeek/Qwen current watch: [`foundation_models/DEEPSEEK_QWEN.md`](foundation_models/DEEPSEEK_QWEN.md).

Training/post-training map: [`RESEARCH_TRAINING_POSTTRAINING.md`](RESEARCH_TRAINING_POSTTRAINING.md).

Latest emerging cross-boundary audit: [`emerging/JEPA_RSI_RUNTIME_2026-10-15.md`](emerging/JEPA_RSI_RUNTIME_2026-10-15.md).

## Current practical development constraint

The present local reference machine is a **Mac mini with Apple M4**. Treat it as a measured development/deployment reference, not a scientific constraint.

Useful local paths:

- MLX — https://github.com/ml-explore/mlx
- Apple Core AI / Core ML — https://developer.apple.com/core-ai/ · https://developer.apple.com/documentation/coreml
- ExecuTorch Core ML / MLX backends
- MuJoCo — https://github.com/google-deepmind/mujoco
- small/medium open multimodal backbones for proxy studies

Use remote/cloud/API comparators when the research question genuinely requires frontier-scale DeepSeek/Qwen or Linux/NVIDIA-only infrastructure. Do not make those stacks local prerequisites.

## Remaining Stage-1 collection gaps

The map is now broad. Remaining gaps should be filled only when strong primary evidence appears:

```text
unknown-unknown diagnostics with real embodied evidence
representation reversibility after compression
self-model ↔ external-world-model coupling
safe irreversible exploration / social permission
correlated uncertainty / ensemble collapse
visual-token budget vs physical-state retention
video frame-rate/token sampling vs fast dynamics
byte-matched long-context vs explicit-memory comparison
KV precision vs epistemic calibration
MoE expert specialization for spatial/physical variables
small-proxy → frontier scaling validity
frozen-backbone vs partial/full adaptation trade-offs
post-training effects on uncertainty / memory / physical reasoning
reward design for partial success / safety / epistemic quality
failure/recovery trajectory sampling
human-video / robot / sim mixture attribution
language-prior contamination in physical reasoning
streaming multimodal prefill / incremental visual encoding
fast controller + slow reasoner synchronization
test-time verifier/search scaling under matched latency and energy
inference-state staleness under asynchronous / cached WAM execution
embodied-JEPA scaling vs physical-variable retention
RSI evaluator validity / hidden-eval leakage / reward hacking
RSI process-level retention and OOD transfer
harness contribution to benchmark scores
runtime/kernel version drift and cross-hardware numerical divergence
API/hosted vs open-weight artifact equivalence
training-data alignment vs architecture gains
quantization effects on uncertainty / permanence / memory
sim2sim → sim2real predictive correlation
formal persistent-state rollback and world-state poisoning benchmarks
```

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
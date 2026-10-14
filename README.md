# Clover

**Open research on how machines can understand the real world through vision alone.**

> **Research question:** How can a machine understand the real world through vision alone?
>
> **Long-term goal:** Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.

Clover is a long-term open research project. **The question is fixed; the answer is open.**

[中文说明](README.zh-CN.md)

## Start here

For a new agent, researcher or contributor:

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
14. [`research/RESEARCH_FOUNDATION_MODEL_SYSTEMS.md`](research/RESEARCH_FOUNDATION_MODEL_SYSTEMS.md)
15. [`research/RESEARCH_TRAINING_POSTTRAINING.md`](research/RESEARCH_TRAINING_POSTTRAINING.md)
16. [`research/RESEARCH_ENGINEERING_VALIDATION.md`](research/RESEARCH_ENGINEERING_VALIDATION.md)
17. [`research/RESEARCH_FRONTIER.md`](research/RESEARCH_FRONTIER.md)
18. [`AGENTS.md`](AGENTS.md)
19. [`STATUS.md`](STATUS.md)
20. [`research/README.md`](research/README.md)

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

**Stage 1 Research is active.** The current job is to collect and structure the problem space broadly before deciding what Clover itself should invent.

## Stage-1 question chain

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
What view / probe / action is worth acquiring next?
↓
What if the current hypothesis set is incomplete, stale, unsafe to test, or socially constrained?
↓
How should hypotheses, mechanisms, experiments, falsification and provenance be managed?
↓
How do foundation-model architecture, multimodal tokenization, data, context/cache, kernels and harness affect the result?
↓
How did pretraining / co-training / SFT / BC / RL / distillation / deployment learning create the observed capability?
↓
Can the candidate run under realistic edge/closed-loop constraints, and how strong is its simulation-to-real evidence?
↓
Which current methods and benchmarks discriminate competing answers?
```

This is a research map, not a proposed Clover architecture.

## Core Stage-1 distinctions

```text
pixels ≠ world state
statistical predictability ≠ physical identifiability
vision alone ≠ passive vision only
observational indistinguishability ≠ representation failure
complete physical description ≠ minimal predictive/control/general-purpose state
long context ≠ persistent grounded world memory
serving KV cache ≠ epistemic world memory
base model ≠ model + harness ≠ model + harness + tools/memory
hosted product ≠ open-weight checkpoint unless exact artifact is verified
total parameters ≠ active parameters ≠ runtime memory ≠ communication cost
architecture efficiency on paper ≠ realized efficiency on available kernels/hardware
architecture ≠ training recipe ≠ data mixture ≠ post-training objective
supervised task success ≠ on-policy robustness
LLM post-training ≠ robot post-training
more heterogeneous robot data ≠ better transfer without alignment
reasoning improvement ≠ perception preservation
minimum state ≠ best state at every timescale
maximum information gain ≠ best safe / permitted experiment
uncertainty over known hypotheses ≠ correct hypothesis missing entirely
uncertain state ≠ stale / wrong world model
parameter estimation ≠ model selection ≠ mechanism discovery ≠ open-world model expansion
current development machine ≠ final edge computer ≠ scientific hypothesis
model inference latency ≠ camera-to-action closed-loop latency
single-simulator success ≠ sim2sim robustness ≠ sim2real transfer ≠ target-robot validation
reflection ≠ falsification
current best hypothesis ≠ permanent truth
external-world state ≠ self / embodiment state
visible behavior of another agent ≠ its hidden goal / belief
```

## What Stage 1 currently covers

The inventory is intentionally wider than “world models” or “VLA.” It includes:

- inverse problems, observability, identifiability, uncertainty and POMDPs;
- human/developmental visual cognition;
- image formation, camera acquisition and adverse visual conditions;
- geometry, SfM, VO, SLAM, tracking and learned 3D/4D reconstruction;
- static/video self-supervised representation;
- object-centric representation, scene graphs and semantic mapping;
- persistent/episodic memory, world change and belief revision;
- hidden physical properties and rigid/articulated/deformable/fluid/granular dynamics;
- irreversible topology change;
- intuitive/quantitative/causal physical reasoning;
- active perception, system identification, intervention and value of information;
- generative world models, WAMs, VLA/direct policies and embodied reasoning;
- sufficient state, aliasing, abstraction and multi-timescale state;
- open-world hypothesis generation, mechanism discovery and falsification;
- self/body schema, social hidden state, help-seeking and permission constraints;
- foundation-model systems: dense/MoE, sparse/linear/full attention, multimodal fusion, visual/video tokenization, long context, KV/cache hierarchy, kernels, distributed runtime and agent harness;
- **training / post-training:** continued pretraining, instruction SFT, behavior cloning, VLM/VLA co-training, preference/offline alignment, RL, on-policy distillation, strong-to-weak distillation, simulation/world-model post-training, deployment self-improvement and continual adaptation;
- robot-data alignment across embodiments, human videos, synthetic data, real demonstrations and failure/recovery trajectories;
- edge inference, memory/latency/power constraints and hardware-aware profiling;
- simulation fidelity, domain randomization, sim2sim, sim2real, real2sim and digital twins;
- hardware-in-the-loop / proxy-hardware validation, runtime monitoring, regression and rollback;
- datasets, benchmarks, reproducibility and systems integration.

## DeepSeek / Qwen and training-system watch

Stage 1 tracks DeepSeek and Qwen as **foundation-model systems references**, not default Clover dependencies.

- [`research/RESEARCH_FOUNDATION_MODEL_SYSTEMS.md`](research/RESEARCH_FOUNDATION_MODEL_SYSTEMS.md)
- [`research/foundation_models/DEEPSEEK_QWEN.md`](research/foundation_models/DEEPSEEK_QWEN.md)
- [`research/RESEARCH_TRAINING_POSTTRAINING.md`](research/RESEARCH_TRAINING_POSTTRAINING.md)

Current questions include:

```text
visual token budget vs physical-state retention
long raw context vs explicit grounded memory under equal bytes/latency
MoE active compute vs storage/communication
FP4/FP8/INT quantization vs uncertainty and long-horizon state
streaming visual encoding vs repeated long-context prefill
frozen backbone vs adapters vs partial/full adaptation
training-data alignment vs architecture gain
SFT/BC vs RL vs distillation vs deployment learning
base model vs harness/tool/memory contribution
small proxy model vs frontier-scale mechanism validity
```

## Why robot training is not just LLM post-training

Robot policies act on the world. Their outputs change future observations and reachable states.

Therefore robot adaptation must additionally handle:

```text
covariate shift
continuous / multimodal actions
control frequency / latency
embodiment-specific action semantics
costly real-world resets
sparse / delayed rewards
contact and hardware dynamics
safety / irreversible actions
sim2real mismatch
operator / demonstration quality
```

The high-level pattern `pretrain → specialize → feedback` is shared; the optimization problem is not.

## Current practical environment

The current local development reference is a **Mac mini with Apple M4**.

Use it for:

```text
small/medium open multimodal baselines
frozen-backbone + state/action heads
LoRA / adapter experiments
MLX / Core AI / Core ML experiments
visual-token/context/memory ablations
behavior cloning / flow-diffusion heads
small MuJoCo RL
teacher distillation
quantization / compression
streaming state prototypes
runtime profiling
```

It is **not** the final robot computer and does not determine the scientific representation. Frontier-scale DeepSeek/Qwen models and Linux/NVIDIA-only simulation/runtime stacks should be remote comparators only when the research question requires them.

## No-real-robot validation policy

```text
EV0 mathematical / synthetic diagnostic
EV1 controlled single simulator
EV2 randomized simulator robustness
EV3 sim-to-sim transfer
EV4 offline real-data / policy evaluation
EV5 real-to-sim / digital-twin validation
EV6 deployment-runtime / compute HIL
EV7 proxy physical hardware
EV8 target real robot
```

Do not describe EV0–EV6 as demonstrated sim2real success.

## Current frontier

The thin current-edge index is [`research/RESEARCH_FRONTIER.md`](research/RESEARCH_FRONTIER.md), freshness checked through **2026-10-15**. Recent high-value additions include WorldOracle, RoboSimStudio, LIBERO-RIG, LoopWAM, ForceWAM, RoboFQE, LADDER, GreenWAM, DR-WM, SpecWM and other sources that materially change the comparison space.

The training surface additionally tracks DeepSeek-R1/V4.1, Qwen3/Qwen3-VL, π0/π0.5, OpenVLA-OFT, Qwen-RobotManip, GR00T N1.7, VLAFlow, VLA-OPD, TEMPO, RehearseVLA and deployment-learning approaches.

## Later stages

### 2 Analysis
One important method → one mechanism report.

### 3 Synthesis
Compare methods across common dimensions, strengths, weaknesses, trade-offs and failure modes.

### 4 Innovation
Only after a gap is well supported do Clover-original hypotheses become serious candidates.

### 5 Implementation
Build reproducible code.

### 6 Evaluation
Run experiments, ablations, cross-simulator tests and eventual real-world tests.

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

## What we do not assume

Clover does **not** assume that DeepSeek/Qwen/another foundation model is the answer, that one training recipe is universally best, that CPU/GPU/NPU choice determines the science, that the Mac mini M4 is the final target hardware, that long context equals memory, that one simulator is reality, that sim-only success proves transfer, that explicit state must beat distributed latent state, that hierarchy is automatically superior, or that one benchmark defines understanding.

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
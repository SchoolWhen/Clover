# Clover Status

Last updated: **2026-10-15**  
Stage-1 freshness checked through: **2026-10-15**

## Research question

> **How can a machine understand the real world through vision alone?**

## Long-term goal

> **Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.**

## Current stage

> **Stage 1 — Research / Survey & Evidence Collection — ACTIVE**

```text
1 Research
→ 2 Analysis
→ 3 Synthesis
→ 4 Innovation
→ 5 Implementation
→ 6 Evaluation
→ 7 Reflection
```

Immediate objective: **coverage before commitment**. No Clover core representation or algorithm is frozen.

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
12. [`research/RESEARCH_OPEN_WORLD_EPISTEMICS.md`](research/RESEARCH_OPEN_WORLD_EPISTEMICS.md)
13. [`research/RESEARCH_MODEL_DISCOVERY.md`](research/RESEARCH_MODEL_DISCOVERY.md)
14. [`research/RESEARCH_FOUNDATION_MODEL_SYSTEMS.md`](research/RESEARCH_FOUNDATION_MODEL_SYSTEMS.md)
15. [`research/RESEARCH_ENGINEERING_VALIDATION.md`](research/RESEARCH_ENGINEERING_VALIDATION.md)
16. [`research/RESEARCH_FRONTIER.md`](research/RESEARCH_FRONTIER.md)
17. [`research/README.md`](research/README.md)

Supporting watches:

- [`research/foundation_models/DEEPSEEK_QWEN.md`](research/foundation_models/DEEPSEEK_QWEN.md)
- [`research/engineering/DEPLOYMENT_LIFECYCLE.md`](research/engineering/DEPLOYMENT_LIFECYCLE.md)
- [`research/engineering/VALIDATION_RESOURCES.md`](research/engineering/VALIDATION_RESOURCES.md)

## Current Stage-1 surfaces

```text
1  broad research inventory
2  world-state variables
3  identifiability / information limits
4  observation physics
5  hidden physical properties / irreversible change
6  minimum sufficient world state
7  state aliasing / representation failure
8  adaptive abstraction / state granularity
9  value of information / probing actions
10 open-world epistemics / model mismatch / epistemic safety
11 model discovery / experiment design / falsification / provenance
12 foundation-model architecture / multimodal / data / inference systems
13 engineering / edge deployment / simulation / validation
14 current frontier
```

## Newly added surface: foundation-model systems

[`research/RESEARCH_FOUNDATION_MODEL_SYSTEMS.md`](research/RESEARCH_FOUNDATION_MODEL_SYSTEMS.md) closes a major Stage-1 gap exposed by the DeepSeek/Qwen review.

It studies:

```text
dense vs MoE / total vs active parameters
full / sparse / linear / hybrid attention
multimodal fusion
visual/video tokenization
long context and KV/cache hierarchy
streaming perception
training-data mixture / alignment / curriculum
synthetic-data provenance
SFT / RL / distillation / deployment learning
precision / quantization
kernel/compiler/runtime co-design
parallelism and expert communication
agent harness / tools / external memory
backbone reuse vs training from scratch
small-proxy → frontier scaling validity
```

Critical distinctions:

```text
scientific world-state hypothesis
≠ foundation-model backbone
≠ training recipe
≠ inference runtime
≠ agent harness

long context
≠ persistent grounded world memory

serving KV cache
≠ epistemic world memory

base model
≠ model + harness
≠ model + harness + external tools

hosted product
≠ open-weight checkpoint
unless the exact artifact is verified

total parameters
≠ active parameters
≠ runtime memory
≠ communication cost
```

## DeepSeek / Qwen watch — 2026-10-15

Detailed record: [`research/foundation_models/DEEPSEEK_QWEN.md`](research/foundation_models/DEEPSEEK_QWEN.md).

### DeepSeek signals

Current tracked items include:

- **DeepSeek-V4.1-Flash** — native multimodal 552B MoE, asymmetric Causal Encoder–Decoder with 8B active input / 16B active output, 1M context and large KV-cache reduction;
- sparse/compressed attention and cache design;
- FlashMLA / DeepSelect / DeepGEMM / DeepEP / TileKernels;
- speculative decoding / conditional sparse memory;
- DeepSeek Harness and model-vs-harness attribution;
- Janus as a historical decoupled visual-understanding/generation reference.

Research lesson:

```text
model architecture
+
cache
+
kernels
+
communication
+
post-training data
+
harness
```

must be disentangled when attributing capability.

### Qwen signals

Current tracked items include:

- **Qwen3.8-Max** — 2.4T total / 95B active long-horizon agent reference;
- **Qwen3.8-Omni / Realtime** — continuous multimodal agent/runtime reference;
- **Qwen3.5** — native multimodal hybrid linear/full-attention sparse-MoE family, including small open models useful for proxy experiments;
- **Qwen3-VL** — modern dense/MoE multimodal family for local and remote probing;
- **FlashQLA**, Qwen-MM-Plugins and Qwen-Live-Harness;
- **Qwen-RobotWorld**, **Qwen-RobotManip**, **Qwen-VLA** and **Qwen-Drive** as competing Physical-AI designs.

Especially important data lesson from Qwen-RobotManip:

```text
heterogeneous robot-data scale
without representation / motion / behavior alignment
can create conflict rather than useful scaling.
```

## Current practical development reference

```text
Mac mini with Apple M4
```

Use it for measured proxy work:

```text
small/medium open multimodal models
MLX / MLX-VLM
Core AI / Core ML
visual-token / frame-rate ablations
context vs explicit-memory experiments
quantization / cache experiments
streaming state prototypes
MuJoCo integration
```

Do **not** treat a 552B DeepSeek or 2.4T Qwen model as a local-M4 target. Use remote/cloud/API comparisons only when they answer a concrete research question.

## 2026-10-15 latest validation sweep

Stage 1 also tracks:

- WorldOracle — https://arxiv.org/abs/2610.18826
- RoboSimStudio — https://arxiv.org/abs/2610.18835
- LIBERO-RIG — https://arxiv.org/abs/2610.18843
- LoopWAM — https://arxiv.org/abs/2610.18873
- ForceWAM — https://arxiv.org/abs/2610.18852
- RoboFQE — https://arxiv.org/abs/2610.18699
- Grid or Nodes? — https://arxiv.org/abs/2610.18637
- LADDER — https://arxiv.org/abs/2610.18053
- GreenWAM — https://arxiv.org/abs/2610.18774

These extend the evidence map toward real execution, Real2Sim, hardware perturbation, offline evaluation, long-horizon failure, deployment learning and edge-memory trade-offs.

## Validation evidence ladder while no target robot exists

```text
EV0 mathematical / synthetic diagnostic
EV1 controlled single-simulator test
EV2 randomized in-simulator robustness
EV3 sim-to-sim transfer
EV4 offline real-data / offline policy evaluation
EV5 real-to-sim / digital-twin validation
EV6 deployment-runtime / compute hardware in the loop
EV7 proxy physical hardware
EV8 target real robot
```

## Current benchmark expansion

[`research/survey/BENCHMARKS_TASKS.md`](research/survey/BENCHMARKS_TASKS.md) currently extends the candidate Understanding Battery through `U20`, including:

```text
U16 WorldOracle      real-execution world-model fidelity
U17 LIBERO-RIG       hardware/setup robustness
U18 LADDER           long-horizon compounding failure
U19 RoboFQE          rollout-free offline policy evaluation
U20 Grid-or-Nodes    memory efficiency / inductive-bias diagnostic
```

## Current non-goals

We are not currently:

- freezing a final representation or foundation-model backbone;
- choosing DeepSeek or Qwen as Clover architecture by default;
- implementing a new Clover core algorithm;
- assuming long context replaces explicit/persistent memory;
- assuming MoE/sparse/linear attention is intrinsically superior for world modeling;
- attributing hosted-agent performance entirely to the base model;
- treating synthetic data as observed physical evidence;
- designing the science around Mac mini M4;
- claiming sim2real success without real hardware;
- making NVIDIA/Isaac mandatory;
- treating one benchmark as the definition of understanding.

## Remaining collection gaps after the DeepSeek/Qwen audit

The remaining gaps are now narrower:

```text
visual-token budget vs physical-state retention
video frame-rate / token sampling vs fast dynamics
byte-matched long-context vs explicit-memory comparison
KV-cache precision vs uncertainty / epistemic calibration
MoE expert specialization for spatial / physical variables
small-proxy → frontier-model scaling validity
frozen-backbone vs adapter vs partial/full adaptation
language-prior contamination in physical reasoning
streaming multimodal prefill / incremental visual encoding
fast controller + slow reasoner synchronization
harness / tool / external-memory contribution to benchmark scores
runtime/kernel version drift
cross-hardware numerical divergence for stateful models
API/hosted vs open-weight artifact equivalence
training-data alignment vs architecture gains
synthetic-data error amplification
representation reversibility after compression
safe irreversible exploration / social permission
sim2sim → sim2real predictive correlation
formal persistent-state rollback / world-state poisoning benchmarks
```

## Stage-1 exit condition

Stage 2 Analysis becomes primary when a new agent can identify:

1. major competing scientific directions and strongest representatives;
2. source/evidence and learning provenance;
3. observation assumptions and world variables represented;
4. identifiability and sufficiency assumptions;
5. likely state-aliasing and abstraction failures;
6. information-gathering / open-world epistemic behavior;
7. hypothesis/model-class and falsification assumptions;
8. exact foundation backbone/artifact when used;
9. total/active parameters, attention, visual-token and context/cache assumptions where material;
10. training-data / post-training provenance;
11. runtime/kernel/harness/tool assumptions;
12. deployment/runtime hardware constraints;
13. validation evidence level (`EV0–EV8`);
14. datasets/benchmarks that discriminate claims;
15. methods deserving one-method-one-report Analysis.

## Not yet demonstrated

Clover has not yet publicly demonstrated a validated general real-world visual world model, final representation, final foundation-model backbone, robust open-world generalization, general causal understanding, persistent long-horizon real-robot world state, validated sim2real transfer, validated original algorithm, or final hardware mapping.

These remain research targets.

<a id="top"></a>

# 调研方向：基础模型架构、运行时与工程条件

Maintained: **2026-10-25** · Document stage: **1 — Research** ([status](../STATUS.md)).

Exact model artifacts, engineering constraints and validation resources. Artifact-specific records retain their original check dates; inherited vendor claims are not reverified by this consolidation.

This is the canonical topic document. Update it in place; source-level dates and reading-depth labels below qualify the evidence, not the maintenance date.

<!-- BEGIN current-model-artifacts -->
<a id="current-model-artifacts"></a>

## 当前精确模型 artifact 核验

核验日：**2026-10-25**。本次读取以下官方权重仓库的精确 revision、模型卡和配置，没有加载模型、运行推理或验证本机可行性。后面保留的 2026-10-15 记录须与这里的新核验区分。

| 精确 artifact | 固定 revision | 配置/卡片中实际可见的模态与结构 | 许可元数据 |
|---|---|---|---|
| [deepseek-ai/DeepSeek-V4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017/tree/1bae0e1088993b9b82de08f59de5be5a34e42170) | `1bae0e1088993b9b82de08f59de5be5a34e42170` | `DeepseekV41ForCausalLM` + `vision_config`；文本配置最大位置 1,048,576；视觉 patch=14、downsample_ratio=3、max_image_tokens=1024。 [固定配置](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017/blob/1bae0e1088993b9b82de08f59de5be5a34e42170/config.json) | MIT |
| [Qwen/Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next/tree/de4b8e4d43b917e7706784d8bb445c9af86a3540) | `de4b8e4d43b917e7706784d8bb445c9af86a3540` | `Qwen4ExpForConditionalGeneration` + `vision_config`；配置 model_type=`qwen4_exp`；文本最大位置 262,144；线性/完整注意力混合。品牌名不能替代配置。 [固定配置](https://huggingface.co/Qwen/Qwen3.8-Flash-Next/blob/de4b8e4d43b917e7706784d8bb445c9af86a3540/config.json) | `other` / `qwen-community-1.0` |
| [Qwen/Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/tree/207bd685a7e3696cfaff12ded7c6a7ea0f88c996) | `207bd685a7e3696cfaff12ded7c6a7ea0f88c996` | 卡片 pipeline=`text-generation`；`Qwen3_5MoeForCausalLM`；公开配置未含 `vision_config`；最大位置 262,144。 [固定配置](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/blob/207bd685a7e3696cfaff12ded7c6a7ea0f88c996/config.json) | `other` / `qwen3.8-max` |
| [Qwen/Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B/tree/1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0) | `1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0` | `Qwen3_5ForConditionalGeneration` + `vision_config`；卡片为 image-text-to-text；文本最大位置 262,144。 [固定配置](https://huggingface.co/Qwen/Qwen3.8-27B/blob/1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0/config.json) | Apache-2.0 |

**已解决的混淆：** `Qwen3.8-2.4T-A95B` 模型卡明确把托管 `Qwen3.8-Max` 的视觉输入、非思考模式、默认 1M 上下文和内置工具列为更多服务特性；不能把这些能力直接赋给这个公开文本权重。Flash-Next/27B 的公开多模态配置也不能代表相同托管产品的全部工具和运行策略。配置位置上限不是本机实测可用上下文，许可名称也不能按家族统一假定。

**仍待核验：** 全部厂商条目的现行 API 路由、推理默认值、精确训练混合、总/激活参数的独立计数、实际 runtime/kernel、视觉预处理、量化与端到端质量/内存/时延。以上四个 artifact 的当前元数据不替代这些实验或其余旧条目的刷新。DeepSeek-1017 的卡片是对原 Flash 的更新，相关 benchmark 仍按官方报告对待。
<!-- END current-model-artifacts -->

<!-- BEGIN current-cross-domain-evidence -->
<a id="current-cross-domain-evidence"></a>

## 当前跨领域与前沿证据：运行系统、在线监控与精确 artifact

检索/核验：**2026-10-25（Asia/Shanghai）**。下表是外部研究记录，不是 Clover 的实验结果或架构决定。

缓存路由、进度探针和核不确定性头改变的是计算/监控接口，不自动构成世界记忆、可识别状态或安全保证。所有效率结果要连同计算阶段、硬件、输入/历史预算和质量条件记录。厂商旧发布计划不能替代当前可访问的模型 artifact。

### Qwen3.8-Next 架构研究

- **来源/版本：** [原论文](https://arxiv.org/abs/2608.30320v1)；初始提交 2026-08-31；本次返回版本更新于 2026-08-31。`PRIMARY_PAPER`。
- **问题与机制：** Qwen3.8-Next 的架构研究把效率、效果和训练稳定性放在一起比较。
- **输入/学习来源：** 基础模型数据与后训练来源不能省略；具体开放 artifact 另以官方模型卡/配置为准。
- **实际证据：** 是系统和骨干设计的外部参照，不是 Clover 的视觉状态方案。
- **不能推出 / 待区分：** 不能只凭模型家族名迁移总参数、激活参数、模态、缓存成本或某个硬件上的速度。
- **本次阅读深度：** 摘要与书目核验。

### Velox

- **来源/版本：** [原论文](https://arxiv.org/abs/2610.22311v1)；初始提交 2026-10-15；本次返回版本更新于 2026-10-15。`PRIMARY_PAPER`。 [作者提供的项目/代码入口](https://velox-world.com/velox/)（未运行复现）。
- **问题与机制：** Velox 用流式几何和相机视锥对应选择历史注意力块，限制随 rollout 增长的成本。
- **输入/学习来源：** 基于既有视频世界模型；几何与模型路由来源分别记录。
- **实际证据：** H200 上的 attention/denoising 与 WBench 导航质量比较。
- **不能推出 / 待区分：** 分阶段加速不是端到端机器人速度；生成历史的几何覆盖不等于真实相机证据的新鲜度。
- **本次阅读深度：** 摘要与书目核验。

### Progress Probes P²

- **来源/版本：** [原论文](https://arxiv.org/abs/2610.31613v1)；初始提交 2026-10-22；本次返回版本更新于 2026-10-22。`PRIMARY_PAPER`。
- **问题与机制：** Progress Probes P² 用 VLA 内部激活上的线性进度探针监测执行偏离。
- **输入/学习来源：** 示范进度监督与原 VLA 知识链保留；不需要外部监控 VLM 不等于不需监督。
- **实际证据：** π0.5 的模拟/真实执行失败检测。
- **不能推出 / 待区分：** 进度下降可作为监控信号，但不是世界状态正确、校准或形式安全证书。
- **本次阅读深度：** 摘要与书目核验。

### Post-hoc Kernel-variance Heads

- **来源/版本：** [原论文](https://arxiv.org/abs/2610.29730v1)；初始提交 2026-10-21；本次返回版本更新于 2026-10-21。`PRIMARY_PAPER`。
- **问题与机制：** Kernel-variance heads 从单策略示范嵌入估计不熟悉度，比较 ensemble、主动采样和转交。
- **输入/学习来源：** 训练示范 support、具体 SmolVLA 特征/核与 supervisor proxy 是条件。
- **实际证据：** LIBERO-10 和受控模态扰动；正文区分跨任务覆盖与任务内排序。
- **不能推出 / 待区分：** 不熟悉不必失败，低不熟悉也不保证安全；转交代理不是人的许可或实际风险覆盖保证。
- **本次阅读深度：** 正文选读：方法、监督或局限段；未复核全部实验/证明。
<!-- END current-cross-domain-evidence -->

## Contents

- [Foundation-Model Architecture, Training and Runtime Systems](#topic-research-research_foundation_model_systems)
- [Engineering, Deployment and Validation Constraints](#topic-research-research_engineering_validation)
- [DeepSeek and Qwen source records (checked 2026-10-15)](#topic-research-foundation_models-deepseek_qwen)
- [Foundation-Model Cross-Boundary Research Matrix](#topic-research-foundation_models-cross_boundaries)
- [Stage-1 Supporting Research — Deployment Lifecycle, Fault Injection and Runtime Reliability](#topic-research-engineering-deployment_lifecycle)
- [Engineering / Validation Resources — Current Snapshot](#topic-research-engineering-validation_resources)
- [Stage-1 Emerging Audit — Remaining CV, Embodiment and Serving Boundaries](#topic-research-emerging-cv_embodiment_systems_2026-10-15)
- [Stage-1 Emerging Cross-Boundary Audit — Embodied JEPA, RSI, Runtime and Physical-AI Systems](#topic-research-emerging-jepa_rsi_runtime_2026-10-15)
- [Stage-1 Emerging Audit — Physical Security, Whole-Body State and Multi-Agent World Models](#topic-research-emerging-security_wholebody_multiagent_2026-10-15)

<a id="topic-research-research_foundation_model_systems"></a>

## Foundation-Model Architecture, Training and Runtime Systems

Source record updated: **2026-10-15**
Source intake checked through: **2026-10-15**

> **Research question:** How can a machine understand the real world through vision alone?

This is a Stage-1 research document. It does **not** choose a Clover architecture, vendor, foundation model, accelerator or training stack.

Its purpose is to cover a gap that became visible after reviewing DeepSeek and Qwen: modern frontier models are no longer separable into “architecture” and “systems” cleanly. Capability, context length, multimodal representation, data mixture, post-training, cache design, kernels, communication, serving runtime and agent harness increasingly co-determine what the model can do in practice.

For Clover, these are constraints and competing research hypotheses, not answers.

---

### 1. Why this surface is necessary

The existing Stage-1 map studies what world state exists, what vision can identify, what representation may be sufficient, how agents acquire evidence and how models are deployed.

It still needs a bridge between those scientific questions and the actual design space of frontier multimodal foundation models.

Keep distinct:

```text
scientific world-state hypothesis
≠ foundation-model backbone architecture
≠ training recipe
≠ inference runtime
≠ agent harness
≠ edge deployment stack
```

A poor runtime can make a scientifically useful state representation unusable.

A powerful harness can make a weak base model appear stronger.

A large context window can reduce retrieval pressure without creating persistent grounded memory.

A visually capable VLM can provide strong priors without learning those priors from vision alone.

---

### 2. Foundation-model architecture axes to track

#### F1 — Dense vs sparse / Mixture-of-Experts

Record:

```text
total parameters
activated parameters per token
number of experts
experts selected per token
shared experts
router / load-balancing design
expert-parallel communication cost
```

Important distinction:

```text
total parameter count
≠ active compute per token
≠ memory footprint
≠ communication cost
```

MoE can reduce active FLOPs while increasing weight storage, routing, network and kernel complexity.

#### F2 — Attention / sequence-state architecture

Track:

```text
full attention
sliding-window attention
sparse attention
compressed / latent attention
linear attention
state-space / recurrent alternatives
hybrid linear + full attention
cross-layer KV reuse
hierarchical indexing
```

Long-video robotics creates input-heavy workloads. Prefill and streaming-update cost can matter more than ordinary chatbot decode cost.

#### F3 — Residual / information-flow architecture

Track mechanisms such as:

```text
standard residual
hyper-connections
manifold-constrained mixing
gating
normalization choices
```

These are training/stability mechanisms unless evidence shows a direct world-representation effect.

#### F4 — Multimodal fusion topology

Compare:

```text
frozen vision encoder + projector
joint early vision-language pretraining
multi-level vision feature injection
late fusion
cross-attention bridges
separate understanding / generation encoders
shared backbone with modality-specific heads
```

Do not assume “native multimodal” implies a particular representation quality for geometry, physics or persistence.

#### F5 — Visual / video tokenization

Track:

```text
image resizing / dynamic resolution
patch size
pixel-unshuffle / pooling
visual-token count
frame sampling rate
video temporal alignment
multi-view synchronization
token pruning / merging
vision-cache reuse
```

This is scientifically relevant because the tokenizer is part of the observation bottleneck.

```text
world evidence lost before the backbone
cannot be recovered by a better world-state head later.
```

Visual-token compression can therefore create state aliasing.

#### F6 — Long context

Record:

```text
native context length
extended context length
attention mode used at each length
KV bytes per token
prefill cost
decode cost
host / SSD spill
context-parallel requirements
```

Keep explicit:

```text
long context
≠ persistent world memory
≠ belief revision
≠ evidence provenance
```

Long context is a computational resource, not a proof of memory semantics.

#### F7 — Adaptive / test-time compute

Track:

```text
reasoning effort
thinking / non-thinking modes
adaptive tool use
multi-pass reasoning
speculative decoding
multi-token prediction
fast / slow model paths
```

For robotics, a key question is whether the system can allocate compute according to deadline and uncertainty:

```text
fast control loop
+
slower reflective / planning loop
```

without producing stale world state.

---

### 3. Training-data and curriculum axes

#### D1 — Pretraining provenance

Record separately:

```text
web text
images
video
egocentric video
robot demonstrations
synthetic robot data
simulation
language descriptions
action labels
privileged physical state
human feedback / preferences
```

A VLM may perform physical reasoning because of language/world priors rather than direct visual evidence.

This must remain compatible with Clover's `L0–L4` provenance labels.

#### D2 — Data mixture and alignment

Track:

```text
sampling ratios
modality balance
robot / human balance
cross-embodiment alignment
temporal synchronization
state-action consistency
instruction-video consistency
filtering and deduplication
```

More data is not automatically better if heterogeneous coordinate systems and action semantics conflict.

#### D3 — Curriculum

Track:

```text
general → specialist
short → long horizon
static image → video → interaction
single embodiment → cross embodiment
clean → randomized / OOD
passive → active / interventional
```

#### D4 — Synthetic-data loops

Study:

```text
teacher-generated instructions
synthetic agent environments
human→robot retargeting
simulation rendering
world-model-generated training data
self-generated failure/recovery data
```

Synthetic data must preserve provenance. It is not observed physical evidence.

#### D5 — Post-training

Record separately:

```text
SFT
RL
RLVR / environment rewards
on-policy distillation
DPO / preference alignment
action-policy fine-tuning
continual deployment learning
```

Do not attribute a post-training gain to the base representation without ablation.

---

### 4. Runtime / systems axes

#### S1 — Precision

Track:

```text
BF16 / FP16
FP8 weights / activations
FP4 weights / KV
INT8 / INT4
mixed precision
```

For Clover, evaluate not only accuracy but:

```text
uncertainty calibration
rare-event sensitivity
object permanence
state aliasing
belief revision
long-horizon drift
```

#### S2 — KV / cache hierarchy

Track:

```text
HBM / unified memory
host RAM
SSD persistence
cross-layer reuse
paged cache
replay / reconstruction
```

Critical distinction:

```text
serving KV cache
≠ epistemic world memory
```

A serving cache stores model-computation state. A world model must additionally encode what is believed, why, with what uncertainty and from which evidence.

#### S3 — Parallelism

Track:

```text
tensor parallel
pipeline parallel
expert parallel
context parallel
data parallel
sequence parallel
```

For MoE, communication can dominate active compute.

#### S4 — Kernel / compiler co-design

Record:

```text
fused operators
attention kernels
Top-K kernels
GEMM kernels
MoE dispatch / combine
quantization kernels
compiler / JIT dependency
hardware-specific paths
```

This matters because an architecture can be efficient on paper but slow on the project's actual hardware.

#### S5 — Storage / I/O

Study:

```text
checkpoint size
load time
weight streaming
KV persistence
training-data I/O
trajectory / video storage
failure replay storage
```

#### S6 — Speculative / multi-token generation

Track acceptance rate, draft cost, verification cost and quality changes.

Robotics may benefit only if speculative generation reduces end-to-end control latency rather than benchmark decode latency alone.

---

### 5. Agent harness and tool-runtime effects

Modern agent evaluations often measure a **system**, not just a model.

Record:

```text
base model
prompt / protocol
harness name + version
tool set
memory subsystem
retrieval subsystem
visual helper / external VLM
MCP / plugin layer
retry policy
parallel-tool policy
sandbox / browser / shell
reasoning-effort setting
```

Keep explicit:

```text
base-model capability
≠ model + harness capability
≠ model + harness + external tools capability
```

This is particularly important for vendor agentic benchmarks.

---

### 6. Backbone reuse vs training from scratch

Clover should explicitly research at least five paths:

```text
B0 train full model from scratch
B1 reuse frozen visual / multimodal backbone
B2 partial fine-tuning / adapters
B3 frozen backbone + new world-state / action head
B4 teacher → smaller student / distillation
```

Questions:

```text
Which world-state variables are already linearly/probe-recoverable?
Which require backbone adaptation?
Which are lost by the original visual tokenizer?
Which capabilities come from language priors rather than vision?
Does freezing the backbone preserve OOD robustness?
Can a new Clover algorithm be tested without frontier-scale pretraining?
```

A scientifically original algorithm does not require training a frontier foundation model from zero.

---

### 7. Proxy-model and scaling validity

Current project hardware cannot train or serve trillion-parameter frontier models locally.

Therefore Stage 1 must research **proxy validity**:

```text
small model demonstrates mechanism
↓
medium model reproduces mechanism
↓
large / remote comparator checks scaling behavior
```

Measure whether conclusions survive changes in:

```text
parameter count
active parameter count
context length
vision resolution
video length
training-data volume
precision
runtime backend
```

A mechanism that works only at 2B or only at 2T parameters is a different scientific claim.

---

### 8. Streaming perception as a first-class workload

Robotic vision is not a sequence of independent chat requests.

A future Clover system may receive an effectively unbounded stream:

```text
camera frame
→ state update
→ camera frame
→ state update
→ ...
```

Research:

```text
incremental vision encoding
frame reuse
visual cache invalidation
temporal token pruning
bounded-history recurrence
periodic global refresh
fast/slow path scheduling
stream interruption / resume
```

Important distinction:

```text
re-encoding a 1M-token history every step
≠ efficient streaming world-state maintenance.
```

---

### 9. Current DeepSeek lessons

Detailed current-source watch: [`foundation-models-and-systems.md`](#topic-research-foundation_models-deepseek_qwen).

High-value DeepSeek research signals include:

```text
DeepSeek-V4 / V4.1
MoE with low active parameters
million-token context
compressed / sparse attention
Causal Encoder-Decoder prefill/decode asymmetry
cross-layer KV reuse
FP4 KV caching
conditional sparse memory
speculative decoding
hardware-specific optimized kernels
expert-parallel communication
agent harness / protocol tooling
```

These demonstrate model-systems co-design. They do **not** demonstrate a sufficient physical world representation.

---

### 10. Current Qwen lessons

High-value Qwen research signals include:

```text
Qwen3-Next / Qwen3.5 hybrid linear + full attention
high-sparsity MoE
native multimodal early fusion
Qwen3-VL dynamic multimodal / video representation
Qwen3.8 long-horizon agent scaling
Qwen3.8 Omni real-time multimodal runtime
FlashQLA kernel co-design
Qwen-MM-Plugins / Qwen-Live-Harness
Qwen-RobotManip alignment-before-scale
Qwen-RobotWorld language-conditioned world modeling
Qwen-Drive explicit 3D probe + planning expert
```

These are valuable counter-hypotheses about architecture, data alignment, multimodal agents and embodied adaptation. They do **not** establish that language is a sufficient physical state or that a VLM backbone itself is a grounded world model.

---

### 11. Mac mini M4 implications

Current project reference hardware:

```text
Mac mini / Apple M4
```

Do not attempt to use this machine as evidence that 552B or multi-trillion-parameter models are locally deployable.

Use the M4 for:

```text
small / medium open VLM baselines
MLX / MLX-VLM experiments
visual-token / context / memory ablations
quantization studies
streaming prototypes
custom Metal / MLX kernels if justified
MuJoCo + model-loop integration
profiling unified-memory behavior
```

Use remote/cloud/API comparators for frontier-scale DeepSeek/Qwen models when necessary.

Good local research candidates from the Qwen family include small dense Qwen3-VL and Qwen3.5 checkpoints because they preserve important architectural ideas at tractable scale.

DeepSeek-V4.1-Flash should primarily be treated as a **remote / distributed systems reference**, not a local M4 baseline.

---

### 12. New reporting fields for Stage 1 / Stage 2

For foundation-model-based methods, record when relevant:

```text
backbone + exact version
open weights / API only
license
modalities
native vs external multimodality
total params
active params
attention / sequence architecture
context length
visual tokenizer / token budget
video frame sampling
multimodal fusion method
training-data provenance
post-training method
precision
KV bytes / token if known
runtime / kernels
parallelism
hardware requirement
harness / tools / memory
reasoning-effort setting
local M4 feasibility
```

---

### 13. Stage-1 gaps exposed by this review

These now deserve explicit follow-up:

```text
visual-token budget vs physical-state retention
video frame-rate / token sampling vs fast dynamics
byte-matched long-context vs explicit-memory comparison
KV precision vs epistemic calibration
MoE expert specialization for physical / spatial variables
small-proxy → frontier scaling validity
frozen-backbone vs backbone-adaptation trade-offs
foundation-model language-prior contamination
streaming multimodal prefill cost
incremental visual encoding
fast controller + slow reasoner synchronization
harness contribution to benchmark scores
runtime/kernel version drift
cross-hardware numerical divergence
API model vs open-weight model equivalence
training-data alignment vs architecture gains
synthetic-data provenance and error amplification
```

---

### Current rule

Do not choose DeepSeek or Qwen as Clover's architecture by default.

Do use them as unusually informative current examples of **model × data × runtime × hardware × harness co-design**.

The target is to understand which of those design choices matter for a vision-grounded robotic world model, which are generic LLM systems optimizations, and which can be tested at tractable scale before Clover enters Innovation.

---

<a id="topic-research-research_engineering_validation"></a>

## Engineering, Deployment and Validation Constraints

Source record updated: 2026-10-14
Source intake checked through: **2026-10-14**

> **Research question:** How can a machine understand the real world through vision alone?

This is a Stage-1 research document. It does **not** constrain Clover to one hardware platform, one simulator, one runtime, or one robot.

Its purpose is to make the downstream engineering and validation problem explicit **before** an algorithm is frozen.

The central questions are:

```text
Can the model run fast enough where the robot actually runs?
What is the real end-to-end latency from camera frame to action/state update?
How much memory, bandwidth, storage and power does it consume?
What accuracy/capability is lost under quantization or compression?
Which operators prevent hardware acceleration?
How do we test without a real robot?
What does simulation prove, and what does it not prove?
How do we distinguish simulator bugs, physics mismatch and model failures?
How should sim-only evidence graduate toward real-world evidence?
```

---

### 1. Hardware is a constraint and research variable — not the scientific answer

Current local development reference for this project:

```text
Mac mini with Apple M4
```

The exact installed RAM/storage configuration should be recorded when performance experiments are run rather than assumed here.

Important distinction:

```text
current development machine
≠
final robot edge computer
≠
scientific hypothesis
```

Clover should remain scientifically portable across CPU/GPU/NPU/ANE-class hardware.

However, deployment constraints can expose scientifically relevant trade-offs:

```text
rich state vs memory
long history vs latency
high-resolution vision vs bandwidth
large world model vs control frequency
generative rollout vs deadline
persistent evidence vs storage
active perception vs energy
```

A representation that cannot satisfy a realistic closed-loop deadline may be scientifically interesting but operationally insufficient for robotics.

---

### 2. Apple-Silicon development / deployment research path

#### MLX

Official project: https://github.com/ml-explore/mlx
Documentation: https://github.com/ml-explore/mlx/blob/main/docs/src/index.rst
Evidence: `OPEN_SOURCE` / `OFFICIAL_PROJECT`

MLX is designed for Apple silicon and uses unified memory shared between CPU/GPU execution. It supports autodiff, compilation, training/inference and distributed communication.

Relevant Stage-1 questions:

```text
Which Clover operations map efficiently to MLX?
Does persistent state benefit from unified memory?
What becomes bandwidth-bound rather than compute-bound?
Which custom operations require Metal kernels?
How much host↔device orchestration remains?
```

Current distributed reference:
https://github.com/ml-explore/mlx/blob/main/docs/src/usage/distributed.rst

Do not assume distributed Mac execution is required; keep it as a future scaling path.

#### Core AI / Core ML

Apple Core AI overview: https://developer.apple.com/core-ai/
Core ML: https://developer.apple.com/documentation/coreml

Current Apple tooling supports hardware-aware model authoring/profiling, conversion and execution across CPU/GPU/Neural Engine where operations are supported.

Relevant optimization topics:

```text
operator compatibility
compute-unit placement
quantization
palettization
model specialization
cold load / warm load
memory footprint
custom Metal kernels
```

Core AI optimization explicitly supports quantization/palettization:
https://developer.apple.com/core-ai/

Core AI / Core ML profiling:
https://developer.apple.com/documentation/coreai/inspecting-debugging-and-profiling-core-ai-models
https://developer.apple.com/documentation/coreml/analyzing-a-core-ml-models-performance-in-xcode

Important rule:

```text
model FLOPs
≠
actual device latency
```

because unsupported operations, memory traffic, shape specialization, graph partitions and CPU/GPU/ANE placement can dominate runtime.

#### ExecuTorch on Apple platforms

Core ML backend:
https://docs.pytorch.org/executorch/stable/backends/coreml/coreml-overview.html

MLX backend:
https://docs.pytorch.org/executorch/stable/backends/mlx/mlx-overview.html

Current MLX delegate status should be treated as evolving/experimental where documented.

Use these as deployment comparators, not assumptions about the final Clover runtime.

---

### 3. Edge-deployment metrics Clover should eventually report

Do not report only average FPS.

For each serious deployment configuration, record:

```text
model / commit
input resolution / context length
precision / quantization
runtime/backend
hardware + RAM
OS/runtime versions
```

#### Latency

```text
cold model load
first inference
warm p50 latency
p95 latency
p99 latency
state-update latency
camera→state latency
camera→decision latency
camera→action-command latency
```

Robotics often cares more about worst-tail latency and deadline misses than peak throughput.

#### Throughput

```text
frames/s
tokens/s if language/model reasoning is used
simulated worlds/s
state updates/s
planning rollouts/s
```

#### Memory

```text
model weights
peak resident memory
persistent world-state memory
KV/cache/history memory
working buffers
raw-evidence storage growth
```

On unified-memory machines, total memory pressure matters even when explicit CPU↔GPU copies are reduced.

#### Compression quality

For FP16 / INT8 / INT4 / palettized or pruned variants, report:

```text
memory reduction
latency change
energy/power change where measurable
capability degradation
calibration degradation
state-aliasing increase
rare-event / unknown-state degradation
```

A compressed model that keeps benchmark accuracy but loses uncertainty calibration or persistence is not equivalent.

#### Sustained behavior

Benchmark not only short bursts but prolonged runtime:

```text
thermal state
sustained latency
memory growth / leak
cache growth
state drift
long-horizon degradation
```

Apple profiling references:

- Xcode/Core ML performance reports — https://developer.apple.com/documentation/coreml/analyzing-a-core-ml-models-performance-in-xcode
- memory profiling — https://developer.apple.com/documentation/xcode/gathering-information-about-memory-use
- Instruments / performance — https://developer.apple.com/documentation/xcode/performance-and-metrics

---

### 4. Real-time robotics is an end-to-end systems problem

Model inference is only one component.

A future robot loop may include:

```text
camera exposure / sensor readout
→ frame transfer
→ preprocessing
→ perception / representation update
→ memory retrieval
→ world-state update
→ planning / reasoning
→ policy / controller
→ command serialization
→ actuator/controller delay
→ physical response
→ next camera observation
```

Therefore:

```text
model latency
≠
closed-loop latency
```

Eventually measure the full perception-to-action cycle and timing jitter.

Important future systems topics:

- asynchronous sensing and control;
- dropped/late frames;
- timestamp alignment;
- camera/control clock drift;
- state update races;
- stale plans;
- interrupted inference;
- watchdog/failsafe behavior;
- degraded-mode execution;
- logging without blocking the control loop.

These are downstream engineering concerns but can invalidate scientific conclusions if ignored.

---

### 5. We currently do not have a real robot — validation must use a ladder

The absence of a target robot does **not** mean evaluation should be postponed.

It means claims must be tiered by evidence strength.

Suggested research validation ladder:

#### EV0 — mathematical / unit / synthetic diagnostic

Test equations, invariances, state-update logic and falsifiers on controlled synthetic examples.

Proves only local mechanism behavior.

#### EV1 — single-simulator controlled tasks

Use deterministic scenarios with privileged ground truth.

Useful for:

```text
state identifiability tests
aliasing tests
controlled interventions
counterfactual branches
memory/world-change tests
```

Does not prove transfer.

#### EV2 — randomized in-simulator robustness

Randomize:

```text
textures / lighting / camera
mass / friction / damping
geometry / object pose
sensor noise / latency
action noise / controller parameters
```

Purpose: expose brittle simulator-specific solutions.

Domain randomization is a robustness tool, not evidence that the real distribution is covered.

#### EV3 — sim-to-sim transfer

Train/calibrate in simulator A, evaluate in simulator B with matched task semantics.

Possible mismatch sources:

```text
contact solver
integration scheme
friction model
collision geometry
rendering / camera pipeline
actuator model
controller timing
```

Cross-simulator survival is stronger than same-simulator generalization because it removes some engine-specific shortcuts.

NVIDIA currently documents sim-to-sim system-identification recovery and explicitly separates parameter recovery from solver parity:
https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup_tutorials/tutorial_system_identification_simsim.html

#### EV4 — offline real-data validation

Before owning a robot, use recorded real-world datasets/video to test:

```text
perception
persistence
world change
physical reasoning
uncertainty
OOD
state reconstruction
```

But offline real video does not validate action consequences or closed-loop control.

#### EV5 — real-to-sim / digital-twin validation when any real telemetry becomes available

Use recorded trajectories or measurements to calibrate simulator parameters and hold out trajectories for validation.

System-identification reference:
https://docs.isaacsim.omniverse.nvidia.com/latest/robot_setup/ext_isaacsim_robot_setup_sysid.html

Real-is-Sim reference:
https://arxiv.org/abs/2504.03597

Important distinction:

```text
fitting simulation to one trajectory
≠
validated digital twin
```

Use held-out trajectories, interventions and task outcomes.

#### EV6 — software / compute hardware in the loop

Before a robot is available, run the real deployment runtime on the intended or proxy edge computer while physics/sensors remain simulated.

This can validate:

```text
runtime latency
serialization
ROS / message interfaces
frame timing
memory
watchdogs
real-time scheduling assumptions
```

It does **not** validate real actuator/contact physics.

#### EV7 — proxy physical hardware

A low-cost arm/mobile base/camera rig can later provide limited reality-gap measurements before target hardware exists.

Claims must state that embodiment differs from the target.

#### EV8 — target real robot

Final transfer / closed-loop real-world evaluation.

Only this tier can support strong target-robot execution claims.

---

### 6. Sim2Sim should be a first-class test, not an afterthought

Why sim2sim matters:

A model can overfit not only a dataset but a **physics engine**.

If a policy/world model fails when the same scenario is moved from one simulator to another, likely causes include:

```text
solver-specific contact
incorrect friction assumptions
rendering shortcuts
state-coordinate assumptions
actuator semantics
hidden simulator metadata
```

A useful protocol is:

```text
same semantic task
same nominal geometry
same initial conditions where possible
same observation protocol
↓
engine A
engine B
↓
compare state/action/outcome divergence
```

Do not require numerical trajectory equality; compare task-relevant and physically meaningful invariants.

Reference example using Isaac Sim → Gazebo → real ROS 2 robot:
https://arxiv.org/abs/2501.02902

---

### 7. Sim2Real, Real2Sim and Real2Sim2Real solve different problems

#### Sim2Real

```text
simulation training/testing
→ real deployment
```

Tools include:

```text
domain randomization
domain adaptation
robust policies
system identification
state/action abstraction
sim-real co-training
```

Reality-gap survey:
https://arxiv.org/abs/2510.20808

#### Real2Sim

```text
real observations / telemetry
→ calibrated digital/simulation model
```

Useful for identifying where simulator parameters or geometry are wrong.

#### Real2Sim2Real

```text
real evidence
→ calibrated/randomized simulator
→ training / analysis
→ real deployment
→ new evidence
→ recalibration
```

This is likely the more realistic long-term workflow for a general robot because the simulator itself should remain revisable.

However:

```text
better simulator fit
≠
correct world model
```

because multiple physical parameter sets can explain the same trajectories.

Keep identifiability analysis from earlier Stage-1 research active here.

---

### 8. Simulator choice under the current Mac mini M4 constraint

#### MuJoCo — strong local baseline

Official repository: https://github.com/google-deepmind/mujoco

Current releases provide universal macOS binaries and native Python bindings.

Good local uses:

```text
rigid/contact dynamics
controlled state variables
system identification experiments
model-based control
fast deterministic diagnostics
cross-solver comparison
```

Do not treat MuJoCo rendering/physics as reality.

#### ManiSkill — limited Mac path

Official repository: https://github.com/haosulab/ManiSkill
Documentation: https://maniskill.readthedocs.io/

Current documentation emphasizes Linux/NVIDIA for full GPU simulation. Mac support is limited and GPU simulation is not available in the documented support matrix.

Use cloud/Linux GPU environments for serious large-scale ManiSkill experiments if needed.

#### NVIDIA Isaac Sim / Isaac Lab — remote/Linux-NVIDIA path

Official requirements:
https://docs.isaacsim.omniverse.nvidia.com/6.0.0/installation/requirements.html

Current Isaac Sim does not support macOS/non-NVIDIA hardware for its standard workstation/library path.

Therefore do **not** make local Isaac Sim a project prerequisite.

Possible research workflow:

```text
Mac M4
  local model development
  local MuJoCo / synthetic diagnostics
  Apple deployment profiling
       ↓
remote/cloud Linux + NVIDIA only when needed
  Isaac Sim / Isaac Lab
  large-scale GPU simulation
  photorealistic sensor generation
       ↓
cross-simulator evaluation
```

This keeps current hardware from blocking research while avoiding premature infrastructure cost.

---

### 9. Simulation failure taxonomy

When an experiment fails in simulation, classify the failure before blaming the algorithm.

#### SF1 — scenario/modeling bug

Wrong units, transforms, collision mesh, camera intrinsics, reset logic, asset scale, etc.

#### SF2 — simulator numerical/solver artifact

Timestep, contact solver, penetration, friction discretization, integration instability.

#### SF3 — synthetic perception shortcut

Textures, perfect segmentation, deterministic camera, unrealistic lighting, metadata leakage.

#### SF4 — actuator/controller mismatch

Command semantics, latency, stiffness/damping, saturation, gear/backlash model.

#### SF5 — policy/model overfitting to simulator

Uses engine-specific dynamics or rendering regularities.

#### SF6 — genuine algorithmic failure

Failure persists across controlled simulator variations and alternative engines.

#### SF7 — reality-gap failure

Works across simulation tests but fails on real data/hardware.

This taxonomy should be used later in Reflection.

---

### 10. Validation should be vector-valued

A future Clover model should not be validated with one scalar score.

Track at least:

```text
scientific capability
prediction / belief quality
uncertainty calibration
state persistence / revision
causal/intervention correctness
closed-loop task success
simulator robustness
sim2sim transfer
real-data generalization
real-time latency
memory footprint
compute utilization
power/thermal behavior
recovery / failure detection
reproducibility
```

This mirrors the Stage-1 principle that benchmarks are instruments, not the definition of understanding.

---

### 11. Reproducibility / systems metadata

Every later experiment should preserve:

```text
Git commit
model checkpoint hash
runtime/backend version
OS version
hardware and memory
simulator version
physics timestep
renderer settings
random seed
assets/version/hash
camera parameters
control frequency
observation/action delay
precision / quantization
benchmark dataset version
```

For simulation experiments additionally preserve:

```text
physics engine
solver settings
collision settings
friction/contact parameters
domain-randomization distributions
privileged simulator state used during training/evaluation
```

Without this metadata, sim2sim and sim2real comparisons can become irreproducible.

---

### 12. Future deployment-ablation matrix

For important Clover candidates, later compare:

```text
full precision vs quantized
full state vs compressed state
all history vs summarized history
CPU vs GPU vs NPU/ANE-capable path
local edge vs remote compute
single-frame vs streaming
cold start vs sustained loop
single simulator vs cross simulator
nominal sim vs randomized sim
sim-only vs offline real data
```

Crucially, do not optimize only speed.

Measure whether acceleration changes the **science**:

```text
Does quantization increase state aliasing?
Does memory pruning damage permanence?
Does lower resolution damage physical identifiability?
Does shorter context break world-change detection?
Does batching increase control latency?
Does asynchronous execution make belief stale?
```

---

### 13. Stage-1 engineering gaps still worth collecting

```text
robot-edge runtime benchmarks for multimodal/world models
ANE/NPU operator-compatibility studies for streaming models
quantization effects on uncertainty/calibration/memory
stateful streaming inference on edge devices
memory-bandwidth-aware world representation
low-power active perception
real-time scheduling for learned world models
cross-simulator benchmark standardization
simulator uncertainty / solver disagreement
sim2sim-to-sim2real correlation
reality-gap metrics for world models rather than only policies
hardware-in-the-loop benchmarks for learned robot world models
low-cost proxy-robot validation protocols
automatic real2sim system identification
sensor/actuator latency randomization
fault injection / degraded hardware testing
reproducible end-to-end camera→action profiling
```

---

### Current rule

Do not design Clover around the Mac mini M4.

Do use the Mac mini M4 as a **measured reference deployment/development environment** now.

Do not claim sim2real success without real hardware.

Do build a validation ladder so that each stage provides stronger evidence than the previous one.

The target is:

```text
scientific mechanism
+
measured runtime feasibility
+
simulation robustness
+
cross-simulator robustness
+
real-data evidence
+
eventual real-robot evidence
```

not any one of those alone.

---

<a id="topic-research-foundation_models-deepseek_qwen_current_2026-10-15"></a>
<a id="topic-research-foundation_models-deepseek_qwen"></a>

## DeepSeek and Qwen source records

Source checked: **2026-10-15**. These inherited artifact records were consolidated on 2026-10-25; the vendors’ model, API and release status was not reverified during consolidation.

> Systems comparators for [foundation-model architecture and runtime](#topic-research-research_foundation_model_systems).

The records below track the architecture, multimodal design, training, inference kernels, runtime and embodied extensions described in the sources checked on that date. They do not establish present API availability or equivalence between hosted products and open checkpoints.

They are **comparators and engineering references**, not default Clover components. For deployment-status claims, the latest applicable official changelog/status supersedes an older launch plan; record the check date and exact artifact rather than carrying an announcement forward as an immutable fact.

---

### DeepSeek

#### DeepSeek-V4.1-Flash

Official release: https://www.deepseek.com/en/news/deepseek-v4-1-flash/
Technical report / weights: https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash
Paper: https://arxiv.org/abs/2609.19969
Evidence: `PRIMARY_PAPER` / `OFFICIAL_PROJECT` / `OPEN_SOURCE`

Architecture reported in the checked source:

```text
552B backbone parameters
8B active per token during prefill
16B active per token during decode
1M-token context
native image + text input
text autoregressive output
```

##### Causal Encoder-Decoder

The 40-layer model is organized as a 20-layer causal encoder followed by a 20-layer decoder.

The design explicitly targets input-heavy agent workloads:

```text
prefill compute
≠ decode compute
```

This is relevant to robotic perception because continuous visual input can make repeated prefill/state-update cost dominant.

##### Compressed Sparse Attention 2

The report describes Full / Reindex / Reuse attention-layer modes, hierarchical sparse indexing, cross-layer reuse and FP4 main-KV caching.

Reported global KV footprint:

```text
~890 bytes / token
≈ 1/4 DeepSeek-V4-Flash
```

Persistent KV footprint is reported at roughly 1/8 of V4-Flash through SWA Bounded Replay.

Stage-1 question:

> If long visual history becomes dramatically cheaper, does explicit grounded memory still outperform context-only approaches under equal bytes and latency?

##### MoE

The checked model description states:

```text
1 shared expert
384 routed experts / layer
6 routed experts active / token
```

Track total weight storage and expert-parallel communication separately from active FLOPs.

##### Multimodal path

The released model card describes:

```text
DeepSeek-ViT
2D-RoPE
3×3 pixel-unshuffle downsampling
2-layer MLP projector
joint image/text processing from LM pretraining
```

Stage-1 question:

> Which physical evidence is lost by visual downsampling before world-state inference begins?

##### Data

Reported pretraining:

```text
45T multimodal tokens
sparse attention trained at 64K sequence length
context extension to 1M during pretraining
```

Post-training is described as:

```text
SFT
→ RL
→ on-policy distillation
```

with major changes concentrated in large-scale automatic synthesis of agent tasks/environments and progressive scaling of tasks/rollouts.

This is important evidence for:

```text
data / environment design can produce major capability changes
without inventing a new RL algorithm.
```

##### Conditional memory / speculative decoding

The checked architecture also exposes:

- Engram conditional sparse memory;
- DSpark speculative decoding;
- Single-Pass mHC / Mega-mHC.

These are systems/architecture comparators. Do not map them directly to Clover persistent world memory without evidence.

---

##### API-status correction recorded on 2026-10-15

The Sept-10 launch post said DeepSeek planned to route `deepseek-v4-pro` requests to V4.1-Flash after Sept 14 while phasing out V4 Pro. The later API changelog checked on 2026-10-15 instead stated that **V4 Pro service would continue after Sept 14 with unchanged billing**. Preserve this correction to the launch plan; it is not a claim that the same routing remains in force today.

Sources: API changelog https://api-docs.deepseek.com/updates/ · official news index https://www.deepseek.com/en/news/ · launch https://www.deepseek.com/en/news/deepseek-v4-1-flash/

---

#### DeepSeek-V4

Official release: https://www.deepseek.com/en/news/v4-preview/
Technical report: https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek_V4.pdf
ArXiv id listed by official model repository: `2606.19348`

Released sizes:

```text
V4-Pro   1.6T total / 49B active
V4-Flash 284B total / 13B active
1M context
```

Key systems ideas:

- hybrid Compressed Sparse Attention + Heavily Compressed Attention;
- mHC residual architecture;
- Muon optimizer;
- sparse MoE;
- long-context cache reduction.

Reported at 1M context, V4-Pro requires substantially lower single-token FLOPs and KV cache than V3.2.

Research role: strong reference for **long-context efficiency as architecture/runtime co-design**.

---

#### DeepSeek infrastructure stack

##### FlashMLA

https://github.com/deepseek-ai/FlashMLA

Role described at the source check:

```text
optimized sparse / latent attention kernels
FP8 / FP4 KV cache
prefill + decode
NVIDIA GPU + Huawei Ascend NPU paths
```

Important deployment lesson:

The 2026-09-30 release changed cache format and dropped support for earlier models/Hopper in the current main path.

Therefore:

```text
model version
+
kernel version
+
cache format
+
hardware generation
```

must be preserved in experiment provenance.

##### DeepSelect

https://github.com/deepseek-ai/DeepSelect

High-performance Top-K kernels for DeepSeek Sparse Attention and sampling.

Official repo reports approximately 2–20× speedup over vanilla `torch.topk` for supported workloads and includes CUDA + Ascend paths.

Research lesson:

> A sparse-attention architecture may depend on a custom selection kernel to realize its theoretical benefit.

##### DeepGEMM

https://github.com/deepseek-ai/DeepGEMM

Unified high-performance kernels covering FP8/FP4/BF16 GEMM, MoE-related paths, HyperConnection and other primitives.

##### DeepEP

https://github.com/deepseek-ai/DeepEP

Expert-parallel communication library with high-throughput and low-latency dispatch/combine, FP8 dispatch, NVLink/RDMA and additional distributed primitives.

Research lesson:

```text
MoE active FLOPs ↓
can still mean
network / dispatch complexity ↑
```

##### TileKernels

https://github.com/deepseek-ai/TileKernels

The checked project describes MoE routing, quantization, Engram and mHC kernels, with NVIDIA and Ascend backends.

##### DeepSpec / DSpark

https://github.com/deepseek-ai/DeepSpec

Full-stack speculative-decoding research code, including training and evaluation of draft models.

##### 3FS

https://github.com/deepseek-ai/3FS

Distributed filesystem designed for AI training/inference I/O workloads.

This is relevant if future Clover research moves from local experiments to large-scale video/trajectory training.

---

#### DeepSeek Harness

https://github.com/deepseek-ai/deepseek-harness

At the source check, DeepSeek's open agent harness described an “everything is a plugin” architecture and developer-preview status.

Stage-1 lesson:

```text
DeepSeek model benchmark
≠ DeepSeek model + dsh + tools + plugins benchmark
```

When reproducing agentic claims, capture exact model, effort mode, harness/version, tools/plugins, runtime/kernel version and hardware. A model-only score and a model-plus-harness score require separate attribution.

---

#### Janus-series — historical but still conceptually useful

https://github.com/deepseek-ai/Janus

Janus explicitly decouples visual encoding for multimodal understanding and image generation while sharing a unified Transformer.

This is useful as a representation-design counterexample:

```text
one visual encoder for every objective
is not automatically optimal.
```

Janus-Pro is an older family in this inventory and should not be confused with V4.1.

For Mac/local research it can still be a smaller historical multimodal baseline if runtime support is practical.

---

### Qwen

#### Qwen3.8-Max

Official release: https://qwen.ai/blog?id=qwen3.8
Official repository: https://github.com/QwenLM/Qwen3.8
Open model: https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B
Evidence: `OFFICIAL_PROJECT` / `OPEN_SOURCE`

Scale reported in the checked source:

```text
2.4T total parameters
95B active
built on Qwen3.5 architectural foundation
long-horizon / agent focus
```

Important reproducibility caution:

The released Hugging Face checkpoint is exposed as a text causal-LM architecture, while hosted integrations may expose image-capable agent workflows.

Therefore:

```text
hosted product modality
≠ open-weight checkpoint modality
```

unless the exact model artifact is verified.

The checked hosted API describes `reasoning_effort` control. A score obtained with `xhigh` reasoning should not be compared to a low-effort local checkpoint as if only architecture differed.

Qwen3.8 is a comparator for long-horizon agent RL, harness effects and adaptive reasoning effort, rather than a local M4 baseline. Exact hosted/open artifact equivalence and modality must be verified for the comparison.

---

#### Qwen3.8-Omni-Flash / Realtime

Official release: https://qwen.ai/blog?id=qwen3.8-omni-flash
Release date recorded by the source check: **2026-09-18**.

Reported capabilities:

```text
text + image + audio + video input
1M-token context
agent/tool workflows
Realtime API for continuous audio-visual interaction
```

Official production measurements report text-output throughput and time-to-first-token / first-audio-packet under streaming audio and audio-visual inputs.

Research role:

```text
continuous multimodal stream
+
low-latency response
+
agent harness
```

is a useful systems comparator for future robot streaming, even though audio violates strict Clover vision-only sensing and therefore must not be treated as a V0–V3 result.

---

#### Qwen3.5 — native multimodal foundation

Official release: https://qwen.ai/blog?id=qwen3.5

Initial open flagship:

```text
397B total / 17B active
native vision-language
hybrid linear + full attention
sparse MoE
```

Architectural lineage:

```text
Gated DeltaNet
+
Gated / standard attention
+
high-sparsity MoE
+
multi-token prediction
```

Officially reported system observations include strong long-context decode-throughput gains versus earlier Qwen families.

##### Early vision-language fusion

Qwen3.5 is described as natively multimodal with early text-vision fusion and large multimodal pretraining.

Stage-1 question:

> Does early fusion improve physical/spatial state retention, or primarily improve semantic alignment and agent usability?

##### Small open models

The Qwen3.5 family includes smaller models such as 0.8B / 2B / 4B / 9B class releases, making it especially useful for local proxy experiments.

These are practical candidates for Mac M4 proxy studies of sequence mechanisms, long context versus explicit memory, and multimodal adaptation without training from scratch. They do not establish that a small-checkpoint result transfers to frontier Max models.

---

#### Qwen3-Next — efficiency foundation

Official release: https://qwen.ai/blog?id=qwen3-next

Key architecture:

```text
80B total / ~3B active
Gated DeltaNet + full attention hybrid
75% linear-attention layers / 25% standard attention
ultra-sparse MoE
multi-token prediction
```

Qwen explicitly reports the trade-off:

```text
linear attention = efficient but weaker recall
full attention = stronger recall but expensive
```

This is highly relevant to Clover's long-stream memory question.

---

#### Qwen3-VL

Technical report: https://arxiv.org/abs/2511.21631
Code: https://github.com/QwenLM/Qwen3-VL

The checked family inventory includes:

```text
dense 2B / 4B / 8B / 32B
MoE 30B-A3B / 235B-A22B
256K native interleaved multimodal context
```

Key architecture signals:

- enhanced interleaved-MRoPE for spatial-temporal modeling;
- DeepStack multi-level ViT feature integration;
- text-based timestamp alignment for video;
- dense and MoE variants for different latency/quality trade-offs.

Research role:

Qwen3-VL small dense models are strong candidates for local baseline/probing because they preserve modern multimodal design at tractable scale.

---

#### Qwen visual tokenization lineage

Earlier Qwen2-VL introduced native dynamic resolution and M-ROPE; Qwen3-VL extends temporal/spatial treatment. The Qwen2.5-VL lineage adds dynamic visual resolution, dynamic-FPS training and absolute-time treatment of video, directly relevant to fast dynamics and frame-sampling studies.

Official Qwen2.5-VL description: https://qwen.ai/blog?from=research.research-list&id=c5e7415d9a9e89adc18c59d9e466e5a1a459b8f4

Research question:

```text
more visual tokens
→ more evidence
but also
→ more prefill cost / memory / latency
```

For Clover, compare physical-state retention under a fixed **byte / latency budget**, not only maximum-resolution accuracy.

---

#### FlashQLA

https://github.com/QwenLM/FlashQLA

High-performance Gated-Delta/linear-attention kernels built on TileLang.

The checked project reports:

```text
~2–3× forward speedup
~2× backward speedup
```

versus the referenced FLA Triton kernel across supported Hopper/Blackwell scenarios, with context-parallel support added in 2026.

Research lesson:

Hybrid attention efficiency depends on real kernel support; theoretical sequence complexity is not enough.

---

#### Qwen-MM-Plugins

https://github.com/QwenLM/Qwen-MM-Plugins

The checked project describes native image/video/file inspection, long-video memory, 3D spatial reasoning, physical-hardware operation plugins and demonstration-video → reusable-skill workflows.

This is important because it externalizes significant capabilities from the base model.

Keep explicit:

```text
Qwen model
≠ Qwen model + MM Plugins
```

---

#### Qwen-Live-Harness

https://github.com/QwenLM/Qwen-Live-Harness

Realtime audio/video harness with background task delegation, proactive interaction and long-term memory.

The memory subsystem is separately configurable; visual memory can periodically observe a screen/camera and save textual descriptions.

Research role:

This is a concrete example of:

```text
base model
+
external persistent memory
+
visual observer
+
agent runtime
```

which should be compared against end-to-end recurrent/persistent world models rather than conflated with them.

---

#### Qwen Physical-AI suite

##### Qwen-RobotWorld

Paper: https://arxiv.org/abs/2606.17030
Official: https://qwen.ai/blog?email_hash=23463b99b62a72f26ed677cc556c44e8&id=qwen-robotworld

Design reported in the checked source:

```text
language-conditioned video world model
Double-Stream MMDiT
frozen Qwen2.5-VL semantic/action encoder
8.6M video-text pairs
200M+ frames
20+ embodiments
500+ action categories
```

It treats language as a universal action abstraction.

The recorded general-to-expert curriculum combines general image/video priors, human-interaction video, single-view embodied SFT, multi-view expansion, cross-view consistency, and complex cross-domain / long-horizon data. Curriculum order and data mixture are part of the method, not implementation trivia.

Critical Clover distinction:

```text
language action abstraction useful for scaling
≠ language is a physically sufficient action representation.
```

---

##### Qwen-RobotManip

Official: https://qwen.ai/blog?id=qwen-robotmanip
Repository: https://github.com/QwenLM/Qwen-RobotManip
Paper: https://arxiv.org/abs/2606.17846

Architecture:

```text
Qwen3.5-4B vision-language backbone
+
flow-matching DiT action expert
```

Important alignment mechanisms:

```text
80D canonical state-action representation
camera-frame delta end-effector pose
camera intrinsics/extrinsics conditioning
structured embodiment prompt
in-context policy adaptation
```

Reported pretraining corpus:

```text
~38,100 h total
~11,420 h robot data
~1,933 h egocentric human video
~24,808 h synthesized human→robot demos
15 embodiments
```

The recorded pretraining uses a VLA:VLM stream ratio of approximately 9:1. Demonstration SFT retains VL+VLA co-training during post-training. The reported curation includes state/action filtering and cross-modal consistency checks. These ratios describe one training design, not universal constants or a scaling law.

This is a particularly important Stage-1 data-engine lesson:

```text
scaling heterogeneous robot data
requires semantic / coordinate / motion alignment.
```

At the source check, the official repository stated there was no plan to release RobotManip/RobotNav model weights, limiting reproducibility relative to open-weight baselines. This release-status statement requires a fresh check before use.

---

##### Qwen-VLA

Official: https://qwen.ai/blog?id=qwenvla
Paper id: https://arxiv.org/abs/2605.30280

Qwen-VLA combines robot, egocentric, synthetic simulation and general vision-language data across manipulation/navigation/cross-embodiment control.

The recorded staged training is:

```text
Stage I   text-to-action pretraining, VLM frozen
Stage II  continual multimodal pretraining, VLM + action decoder updated
Stage III SFT for multitask / real-robot specialization
Stage IV  PPO RL in simulation
```

Each stage changes the learning signal and updated parameter subset; final policy behavior cannot be attributed to backbone architecture alone.

Research role: broad direct-policy counter-hypothesis to persistent explicit world-state approaches.

---

##### Qwen-Drive 1.0

Official: https://qwen.ai/blog?id=qwen-drive-1.0
Paper: https://arxiv.org/abs/2609.00111

Built on native multimodal Qwen3.5-4B while keeping the pretrained VLM architecture untouched and adding:

```text
explicit BEV perception head
3D object detection
semantic occupancy
BEV map segmentation
flow-matching planning expert
```

Research role:

Strong counterexample to the idea that all state must remain implicit inside the foundation backbone.

```text
native multimodal VLM architecture (weight-freezing scope not verified in this intake)
+
explicit inspectable 3D probe
+
planning head
```

is a distinct design family Clover should compare. Architecture preservation does not establish that pretrained weights were frozen; the update scope requires source-level verification.

---

#### Qwen-AgentWorld — adjacent digital-world reference

Official: https://qwen.ai/blog?id=qwen-agentworld

A language world model trained natively to simulate agent environments across seven digital domains, with paired ground-truth observations from real environments.

It is not a physical-world/vision-only result, but it is useful for studying world-model training objectives, environment simulation and evaluator design.

---

### Research contrasts at the source check

| Axis | DeepSeek source record | Qwen source record | Clover question |
|---|---|---|---|
| Long context | compressed/sparse KV-centric design | hybrid linear/full attention + 1M hosted contexts | context vs explicit memory under equal budget |
| MoE | very large sparse MoE + heavy expert-parallel systems | ultra-sparse MoE across multiple scales | active compute vs communication/storage |
| Vision | DeepSeek-ViT + projector; joint multimodal pretraining | native multimodal/early fusion; Qwen3-VL DeepStack | which fusion preserves physical evidence? |
| Streaming | input-heavy CED optimization | Omni Realtime + harness | incremental robot perception architecture |
| Kernels | FlashMLA / DeepSelect / DeepGEMM / DeepEP | FlashQLA | hardware co-design and portability |
| Agent runtime | DeepSeek Harness | Qwen-MM-Plugins / Live Harness | model vs harness capability |
| Physical AI | general multimodal/agent focus in these records | RobotWorld / RobotManip / VLA / Drive | backbone reuse vs embodied specialization |
| Data | 45T multimodal + synthetic agent task pipeline | multimodal scaling + large cross-embodiment robot synthesis | data alignment vs architecture |
| Post-training | SFT/RL/on-policy distillation + synthetic agent environments | multi-stage reasoning and robot curricula | separate training-recipe gains from backbone gains |
| Small local models | fewer frontier analogues in these records | strong 2B–9B multimodal family | Mac M4 proxy research |

---

### Required attribution for method analysis

For every claim, preserve the exact check date, model identifier, hosted/API versus open-checkpoint identity, modalities of that artifact, reasoning-effort/thinking mode, harness/tools, runtime/kernel, quantization/cache format and API-routing status. An older release page cannot override a later applicable changelog.

For DeepSeek/Qwen-derived comparisons, always ask:

```text
1. Is the result base-model, harness, or full-system performance?
2. Is multimodality native in the exact artifact being tested?
3. What is total vs active parameter count?
4. What is the visual/video token budget?
5. How is time represented?
6. What is the actual context/KV memory cost?
7. Is long context replacing an explicit memory subsystem?
8. What data/provenance created the physical prior?
9. Which model parts are frozen vs adapted?
10. Which custom kernels/runtime are required for claimed efficiency?
11. Does the open checkpoint reproduce the hosted product?
12. Can the mechanism be evaluated on M4-scale proxy models?
13. What happens after quantization / lower resolution / shorter history?
14. Which world-understanding property is actually demonstrated?
```

---

### Candidate controlled experiments

Stage 1 should collect enough evidence to later support controlled experiments such as:

#### E-FM1 — visual token budget

```text
same model
same video
vary image resolution / token count / frame rate
→ physical / spatial / permanence diagnostics
```

#### E-FM2 — context vs memory under equal bytes

```text
long raw context
vs
compact persistent state + evidence retrieval
```

Match total memory footprint and latency.

#### E-FM3 — precision vs epistemics

```text
BF16
FP8
INT8 / INT4
```

Compare calibration, unknown-state behavior and long-horizon state consistency, not only task accuracy.

#### E-FM4 — harness ablation

```text
base model
+ tools
+ memory
+ visual plugins
+ retries
```

Measure incremental contribution of each layer.

#### E-FM5 — frozen backbone vs adaptation

Use tractable Qwen small models to compare:

```text
frozen VLM + new state head
adapter / LoRA
partial backbone tuning
full tuning where feasible
```

#### E-FM6 — streaming fast/slow loop

Compare:

```text
fast local state updater
+
slower reasoner/planner
```

against synchronous monolithic inference under identical deadlines.

---

### Research implication

DeepSeek and Qwen expose a major Stage-1 lesson:

> **Modern model capability is increasingly produced by a coupled stack of representation, data, sparse compute, memory/cache, kernels, distributed systems, post-training and agent runtime.**

For Clover, the correct response is not to imitate either stack wholesale.

The research task is to identify which pieces are generic foundation-model engineering, which pieces materially change visual world-state quality, and which can be tested with small reproducible models before large-scale Innovation.

---

<a id="topic-research-foundation_models-cross_boundaries"></a>

## Foundation-Model Cross-Boundary Research Matrix

Source record updated: **2026-10-15**
Source intake checked through: **2026-10-15**

> Supporting material for [`foundation-models-and-systems.md`](#topic-research-research_foundation_model_systems) and [`learning-and-data.md`](learning-and-data.md#topic-research-research_training_posttraining).

This document closes the remaining cross-boundary gaps between computer vision, multimodal foundation models, embodied learning, runtime systems and edge deployment. It is **not** a Clover architecture decision.

Core rule:

```text
scientific capability
must be separated from
input compression + training recipe + runtime + harness + deployment artifact
```

---

### P0 — must understand before serious architecture selection

### P0.1 Visual tokenizer / video sampling is part of the sensor

A robot does not feed raw reality to a foundation model.

```text
world
→ optics / camera
→ RGB frames
→ resize / crop / normalization
→ frame sampler
→ patch / pixel-unshuffle / pooling
→ token pruning / merging
→ visual tokens
→ backbone
→ state
```

Therefore the visual tokenizer belongs inside the effective observation operator.

Track:

```text
input resolution
patch size / stride
pixel-unshuffle factor
visual tokens / frame
frames / second presented to model
frame-selection policy
multi-view synchronization
token pruning / merging stage
visual cache reuse
```

Current evidence:

- DeepSeek-V4.1-Flash uses native visual input with a dedicated visual front end; its released model material makes visual downsampling/tokenization part of the architecture: https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash
- Qwen3.5 is natively multimodal: https://qwen.ai/blog?id=qwen3.5
- Qwen3-VL provides tractable open multimodal checkpoints for controlled tokenizer experiments: https://github.com/QwenLM/Qwen3-VL
- VLA-Pruner shows that token importance for action can differ from semantic salience and explicitly uses temporal/action-aware pruning: https://arxiv.org/abs/2511.16449 · https://github.com/MINT-SJTU/VLA-Pruner

Required Clover experiment family:

```text
same checkpoint
same raw video
vary:
  resolution
  FPS
  token budget
  pruning policy
  temporal sampling

measure:
  geometry
  fast motion
  contact events
  object permanence
  hidden-state inference
  uncertainty
  task success
  latency / memory
```

Do not conclude that a model lacks physical understanding until verifying that the discriminating visual evidence survived tokenization.

---

### P0.2 Streaming foundation model, not repeated giant prompts

Robotic perception is a continuous stream, not a sequence of independent chat requests.

Research:

```text
incremental visual encoding
frame-to-frame feature reuse
bounded cache update
cache invalidation
selective global refresh
stream interruption / resume
asynchronous perception / reasoning
fast state updater + slow reasoner
```

Current evidence:

- Long-WAM treats history length and real-time processing as a joint model-system problem and studies optimized long-context World-Action Models: https://arxiv.org/abs/2610.10528
- Qwen-Live-Harness exposes a concrete continuous audio/video agent runtime with configurable visual FPS, background perception and memory: https://github.com/QwenLM/Qwen-Live-Harness
- DeepSeek-V4.1-Flash explicitly separates input-heavy and output-heavy compute with an asymmetric Causal Encoder–Decoder: https://www.deepseek.com/en/news/deepseek-v4-1-flash/

Required measurements:

```text
incremental update latency
full-refresh latency
state staleness
frame backlog
cache growth
memory leak / fragmentation
deadline miss rate
belief error after dropped / reordered frames
```

A million-token context model that must repeatedly rebuild a huge prefix is not automatically a viable streaming world model.

---

### P0.3 Long context vs persistent world memory

Long history availability and useful world memory are different claims.

Current evidence:

- Long-WAM reports that access to longer history pays off much more when the visual foundation is pretrained to use causal history: https://arxiv.org/abs/2610.10528
- ReCAP finds that keeping all stale generated history can hurt long-horizon robot world prediction; retaining an anchor plus recent complete visual-action blocks improves prediction and bounds context growth: https://arxiv.org/abs/2610.14583
- RM-WAM treats history as conditionally useful and learns to gate short-term visual memory plus latent event memory rather than injecting all history: https://arxiv.org/abs/2610.15305
- WorldMemArena directly compares long-context, external-memory/RAG and harness-managed multimodal memory under evolving world state: https://arxiv.org/abs/2605.29341 · https://github.com/UCSB-AI/WorldMemArena

Required comparison:

```text
A long raw context
B short context + explicit persistent state
C short context + evidence retrieval
D hybrid state + evidence + bounded recent context
```

Match as far as possible:

```text
total bytes
peak memory
camera→decision latency
compute budget
```

Then measure permanence, revision, contradiction, causal history, uncertainty and OOD task reuse.

---

### P0.4 Foundation-backbone adaptation

Clover does not need frontier-scale pretraining from scratch to test an original world-state mechanism.

Compare:

```text
B1 frozen VLM + Clover state head
B2 head + LoRA / adapter
B3 selective vision / language block tuning
B4 partial backbone tuning
B5 full fine-tuning where feasible
B6 teacher → smaller student / distillation
```

Current evidence:

- Qwen-Drive 1.0 keeps the native multimodal backbone architecture and adds explicit BEV perception / 3D state / planning components: https://qwen.ai/blog?id=qwen-drive-1.0
- A 2026 π0 LoRA/FFT study finds some LoRA configurations match FFT, while freezing too much of the visual/semantic path can hurt embodiment adaptation: https://arxiv.org/abs/2607.10172
- Adaptive Capacity Allocation reports that robotics adaptation can require substantially higher/task-varying rank than common language LoRA recipes and evaluates π0 and SmolVLA on a real robot: https://arxiv.org/abs/2603.07404
- Actions as Language shows robot fine-tuning can catastrophically damage foundational VLM capabilities and explicitly evaluates preservation: https://arxiv.org/abs/2509.22195

Required preservation vector:

```text
task success
OOD visual generalization
geometry / spatial probes
physical reasoning
uncertainty calibration
memory / permanence
language prior sensitivity
catastrophic forgetting
latency / memory
```

A tuned model can improve robot success while damaging general visual/world capabilities.

---

### P1 — high-value research variables

### P1.1 Data science is a first-class model variable

Record separately:

```text
raw hours / tokens / trajectories
unique environments
unique objects
unique tasks
embodiments
operators
camera setups
success / failure / recovery fraction
real robot / human / sim / generated fraction
deduplication
near-duplicate leakage
retargeting method
state/action alignment
temporal synchronization
instruction alignment
filtering / quality score
curriculum / sampling ratio
```

Current evidence:

- Qwen-RobotManip reports a large heterogeneous corpus but emphasizes representation / motion / behavior alignment rather than naive pooling: https://qwen.ai/blog?id=qwen-robotmanip · https://arxiv.org/abs/2606.17846
- Rethinking VLA Scaling reports that naive heterogeneous embodiment pooling can induce negative transfer and that physical action alignment materially changes transfer: https://arxiv.org/abs/2602.09722
- Manipulation data-scaling work reports that environment/object diversity can matter more than repeatedly adding demonstrations in the same condition: https://arxiv.org/abs/2410.18647

Research questions:

```text
Does deduplication remove useful repeated physical evidence?
Does synthetic retargeting preserve contact / timing / kinematics?
Does language annotation inject priors absent from vision?
Does curriculum change what the representation preserves?
Does the best real/human/sim mixture change with model scale?
```

Data quantity is not a sufficient description of training evidence.

---

### P1.2 Quantization must be evaluated as a capability intervention

Quantization can alter multimodal tokens, action experts, KV state and rare-event behavior differently.

Current evidence:

- QuantVLA studies post-training low-bit quantization of both VLM and DiT action components: https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_QuantVLA_Scale-Calibrated_Post-Training_Quantization_for_Vision-Language-Action_Models_CVPR_2026_paper.html
- FoldQuantVLA evaluates native W4A4 inference on GR00T / π0.5 and shows that selectively retaining higher precision can materially change real-robot success: https://arxiv.org/abs/2609.24433
- Quantization-Conditioned RL finds PTQ/QAT gaps become especially visible on long-horizon / shifted robot tasks and uses rollout outcomes and partial completion to recover low-bit policies: https://arxiv.org/abs/2610.15675
- DeepSeek-V4.1 exposes FP8/FP4 KV-cache kernel paths in its official inference stack: https://github.com/deepseek-ai/FlashMLA

Required Clover measurements:

```text
nominal task success
OOD success
uncertainty calibration
unknown/refusal behavior
rare physical event sensitivity
object identity / permanence
belief revision
long-horizon state drift
action smoothness / contact stability
latency / memory / energy
```

Keep distinct:

```text
PTQ
≠ QAT
≠ quantization-conditioned post-training / RL
```

---

### P1.3 Small-proxy → frontier scaling validity

The current Mac-M4 workflow will rely heavily on 2B/4B/8B-scale proxy models. Every mechanism claim should therefore state its scale domain.

Evidence:

- Robotics scaling work shows model/data/compute scale changes downstream behavior, but does not prove every local mechanism scales monotonically: https://arxiv.org/abs/2405.14005
- Rethinking VLA Scaling shows that some intuitive regularization/data recipes do not remain beneficial at scale: https://arxiv.org/abs/2602.09722
- DeepSeek historical scaling work treats training hyperparameters as scale-dependent rather than assuming one small-model recipe transfers unchanged: https://arxiv.org/abs/2401.02954
- Qwen spans small dense multimodal checkpoints through large sparse-MoE systems, making family-level proxy checks possible when exact artifacts are comparable.

Required protocol:

```text
small model discovers effect
→ medium model replication
→ large / remote model counter-check
```

Track sign/magnitude/failure changes with parameter scale, active parameters, context, visual-token budget, data scale, precision and backend.

A 4B result is not automatically a MoE/frontier result.

---

### P1.4 Harness attribution

Modern agent performance belongs to a **model-harness configuration**, not necessarily the base model.

Current evidence:

- WorldMemArena compares long-context, manual external memory and harness-managed memory: https://arxiv.org/abs/2605.29341
- Qwen-MM-Plugins adds image/video processing, multimodal memory and specialized visual tools: https://github.com/QwenLM/Qwen-MM-Plugins
- Qwen-Live-Harness adds realtime multimodal interaction and long-term memory: https://github.com/QwenLM/Qwen-Live-Harness
- DeepSeek Harness uses an everything-is-a-plugin execution architecture: https://github.com/deepseek-ai/deepseek-harness

Required ablation ladder:

```text
base model
+ system prompt / protocol
+ external memory
+ perception helper
+ tools
+ retries / recovery
+ full harness
```

Record accuracy/capability, token cost, wall-clock latency and memory at every rung.

---

### P2 — understand now, but do not let these dominate Clover science

### P2.1 Distributed training / storage / network

Track enough to know whether a claimed architecture is operationally realistic:

```text
data / tensor / pipeline / expert / context parallelism
all-to-all / dispatch cost
checkpoint / optimizer-state size
video/trajectory I/O
network topology
storage bandwidth
fault recovery
```

Current DeepSeek references:

- DeepEP — expert-parallel communication: https://github.com/deepseek-ai/DeepEP
- 3FS — AI-oriented distributed filesystem: https://github.com/deepseek-ai/3FS
- DeepGEMM — low-precision / MoE kernels: https://github.com/deepseek-ai/DeepGEMM
- DeepSelect — sparse-attention/sampling Top-K kernels: https://github.com/deepseek-ai/DeepSelect

These are feasibility and scaling references. They are not evidence that a particular world representation is scientifically superior.

### P2.2 Optimizer / residual / speculative-decoding details

Track mechanisms such as:

```text
Muon / AdamW variants
mHC / hyper-connections
multi-token prediction
speculative decoding
custom low-precision training recipes
```

Only promote one of these into a Clover scientific variable if an ablation shows it changes a world-understanding property rather than only training stability, throughput or decoding latency.

---

### Additional cross-boundaries exposed by the final audit

These should remain visible even though they do not need new top-level documents:

```text
reward / verifier quality and reward hacking
action chunk / control-rate / replanning frequency
fast control loop vs slow semantic reasoner
training/evaluation data contamination
hosted API model drift and silent routing
checkpoint/runtime/kernel version drift
quantization before vs after post-training
post-training preservation of uncertainty / memory / causal probes
model rollback vs persistent-memory rollback
fleet update admission / poisoned or broken-robot experience
```

See [`learning-and-data.md`](learning-and-data.md#topic-research-training-high_risk_boundaries) for the training-specific matrix.

---

### Current conclusion

The remaining foundation-model issues are no longer missing broad fields. They are **controlled-variable problems**.

For Stage 2 and later experiments, the unit of comparison should increasingly become:

```text
raw observation
+ tokenizer/sampling
+ exact checkpoint
+ adaptation recipe
+ runtime/precision
+ memory/harness
+ hardware
```

not simply a model-family name.

---

<a id="topic-research-engineering-deployment_lifecycle"></a>

## Stage-1 Supporting Research — Deployment Lifecycle, Fault Injection and Runtime Reliability

Source record updated: 2026-10-14
Source intake checked through: **2026-10-14**

> Companion to [`foundation-models-and-systems.md`](#topic-research-research_engineering_validation).

This file studies what happens after a model is scientifically interesting but before it can be trusted as a robot subsystem.

It does **not** propose a Clover architecture.

---

### 1. Deployment profiles should be explicit

Do not report one latency number without saying **where the model is expected to run**.

#### DP0 — local research workstation

Current Clover reference:

```text
Mac mini / Apple M4
```

Primary roles:

```text
model development
MLX / Core AI / Core ML profiling
local MuJoCo diagnostics
offline real-video evaluation
quantization / compression studies
stateful streaming prototypes
```

Apple references:

- Core AI — https://developer.apple.com/core-ai/
- Core AI profiling/debugging — https://developer.apple.com/documentation/coreai/inspecting-debugging-and-profiling-core-ai-models
- Core ML Xcode performance report — https://developer.apple.com/documentation/coreml/analyzing-a-core-ml-model-s-performance-in-xcode

Apple's performance tooling can report load/prediction timing and operation placement across CPU/GPU/Neural Engine. Memory and power require separate measurement.

#### DP1 — proxy edge compute

Examples:

```text
Apple-silicon device
Jetson Orin-class device
other CPU/GPU/NPU embedded target
```

NVIDIA Orin reference:
https://developer.nvidia.com/sites/default/files/akamai/Jetson_AGX_Orin_Developer_Kit_RG_0.pdf

The purpose is not to choose NVIDIA now. The purpose is to expose portability issues:

```text
unsupported operators
memory-bandwidth dependence
precision dependence
runtime-specific graph partitioning
thermal throttling
power envelope
camera / middleware integration
```

#### DP2 — target robot compute

This profile only exists once the actual robot, cameras, controller and compute budget are known.

Rule:

```text
performance on DP0
≠
performance on DP1
≠
performance on DP2
```

---

### 2. Edge feasibility is an end-to-end timing question

A model can be fast in isolation and still be too slow for closed-loop robotics.

Measure:

```text
sensor exposure / readout
capture → memory transfer
preprocessing
representation update
memory retrieval
world-state update
planning / policy
message serialization
controller / actuator delay
```

Report:

```text
p50
p95
p99
maximum / deadline miss rate
jitter
cold start
first inference
sustained latency
```

Do not hide batching delay behind throughput.

#### Deployment-oriented edge comparator

**LiteVLA-Edge**
Primary paper: https://arxiv.org/abs/2603.03380
Evidence: `PRIMARY_PAPER`

The work targets fully on-device VLA inference on Jetson Orin-class hardware and reports a ROS 2 integrated perception→reasoning→action pipeline. Its importance for Clover is not the specific VLA architecture, but the systems lesson:

```text
model compression
+
runtime choice
+
middleware
+
full-loop timing
```

must be measured together.

It does **not** establish that its latency is sufficient for every robot or that 4-bit quantization preserves persistent-world-model properties.

---

### 3. Fault injection should be part of validation, not an emergency-only test

A later Clover candidate should be evaluated under controlled deployment perturbations.

#### FI1 — camera-stream faults

```text
frame drop
bursty frame loss
stale frame reuse
partial image loss
camera disconnect / reconnect
```

#### FI2 — image-quality / observation degradation

```text
motion blur
exposure shift
occlusion
compression artifacts
lighting shift
reflection / transparency
```

#### FI3 — calibration / rig drift

```text
camera bump
camera remount
intrinsic drift
camera↔robot extrinsic error
base pose change
table / scene geometry offset
```

#### FI4 — compute perturbation

```text
inference delay
jitter
CPU/GPU contention
memory pressure
thermal throttling
background process load
```

#### FI5 — state / timing faults

```text
out-of-order timestamp
clock drift
stale world state
late memory retrieval
dropped control message
```

#### FI6 — actuator / controller perturbation

```text
actuation gain shift
control-rate shift
latency
saturation
backlash / wear
joint / gripper degradation
```

#### FI7 — persistent-state corruption

```text
wrong memory write
stale fact retained
incorrect identity merge
malicious / poisoned memory
world-state provenance lost
```

#### Current benchmark anchors

**LIBERO-RIG**
Primary paper: https://arxiv.org/abs/2610.18843
Evidence: `PRIMARY_PAPER`

This 2026-10-13 benchmark holds LIBERO tasks fixed while perturbing the **hardware/setup** across axes including camera geometry/calibration, actuation gain, control rate, proprioception, base pose, table height and gripper configuration.

Stage-1 lesson:

```text
scene/task generalization
≠
hardware-setup robustness.
```

A model may tolerate visual augmentation while still fail under faults that do not look like image corruptions.

**Bench2Drive-Robust**
Primary paper: https://arxiv.org/abs/2605.18059
Open code: https://github.com/Thinklab-SJTU/Bench2Drive-Robust
Evidence: `PRIMARY_PAPER` / `OPEN_SOURCE`

The benchmark injects camera-stream failures, ego-state errors and compute/control delay in a closed loop. It is automotive rather than manipulation, but it is an excellent methodological reference for **deployment perturbation testing**.

**When Sensors Fail**
Primary paper: https://arxiv.org/abs/2603.04648
Evidence: `PRIMARY_PAPER`

Studies temporally persistent sensor dropout and observation drift in control. It is useful evidence that robustness to transient image corruptions is not enough when observation failures persist over time.

---

### 4. Runtime monitoring is different from offline evaluation

A system can pass a benchmark and still need a runtime mechanism that detects impending failure.

#### Deployment-Time Reliability of Learned Robot Policies

Primary source: https://arxiv.org/abs/2603.11400
Evidence: `PRIMARY_PAPER`

The work organizes deployment reliability around:

```text
runtime failure monitoring
training-data attribution for diagnosis
long-horizon policy coordination / feasibility
```

Stage-1 implication:

A future Clover deployment should not only predict the world; it should expose signals that allow the system to recognize:

```text
my predicted progress disagrees with observed progress
my action is not producing the expected consequence
I am entering an unfamiliar / failure-prone region
```

#### Runtime monitoring questions

Later measure:

```text
failure-detection recall
false alarm rate
detection lead time
recovery success
human-escalation rate
cost of unnecessary stops
```

A monitor that fires only after a collision is not an adequate early-warning system.

---

### 5. Regression testing must include capability regression, not only software correctness

Every new checkpoint can improve one score and silently damage another capability.

A later regression suite should cover:

```text
perception
persistence
belief revision
unknown / abstention
causal intervention
active perception
latency
memory
calibration
sim2sim transfer
recovery
security / provenance
```

For each release candidate preserve:

```text
previous checkpoint
new checkpoint
dataset delta
code delta
runtime delta
simulator delta
hardware delta
metric vector delta
```

#### Release statuses worth considering later

```text
research-only
simulation-qualified
real-data-qualified
proxy-hardware-qualified
target-hardware candidate
target-hardware qualified
```

These labels should indicate evidence strength, not marketing maturity.

---

### 6. Rollback should be planned before online adaptation is enabled

Continual/test-time adaptation creates a new risk:

```text
model update improves current regime
but corrupts previously valid capability
```

Before allowing an online model update, a deployment system should eventually define:

```text
update trigger
validation gate
protected capability set
rollback checkpoint
rollback trigger
state / memory migration rule
```

Important research question:

```text
If model weights roll back,
what happens to world memory learned under the newer model?
```

Weight rollback and belief/memory rollback are not automatically the same operation.

---

### 7. Data / checkpoint / experiment provenance should be first-class

A result should be traceable from robot behavior back to the exact evidence and software that produced it.

Preserve where possible:

```text
Git commit
checkpoint hash
training-data manifest + version
preprocessing version
calibration file
simulator + asset versions
randomization distributions
runtime/backend
hardware / firmware
camera configuration
controller parameters
experiment seed
raw episode / video IDs
```

#### Generalization should be grounded relative to training data

**RADAR — Grounding Robot Generalization in Training Data via Retrieval-Augmented VLMs**
Primary paper: https://arxiv.org/abs/2603.11426
Evidence: `PRIMARY_PAPER`

The paper compares evaluation settings directly with training examples to characterize what kind of generalization is actually being tested.

Stage-1 lesson:

```text
unseen benchmark episode
≠
necessarily meaningfully novel experience.
```

A later Clover evaluation should report what is actually novel relative to its training/evidence distribution.

---

### 8. Security and world-state integrity belong in deployment validation

A persistent world model creates attack surfaces that ordinary stateless perception does not have.

#### Security of Foundation-Model-Powered Embodied Agents

Primary survey: https://arxiv.org/abs/2608.16843
Evidence: `PRIMARY_PAPER`

The survey identifies attack surfaces spanning:

```text
model supply chain
user instruction
context / memory
physical semantic environment
multimodal perception
world state
reasoning / planning
action interfaces
middleware
multi-agent communication
execution control
```

It specifically highlights long-term memory, middleware/networking, world-state integrity and multi-agent trust as comparatively underexplored.

#### Security of World-Model-Based Embodied AI

Primary survey: https://arxiv.org/abs/2607.28226
Evidence: `PRIMARY_PAPER`

Important Stage-1 distinction:

```text
world model as safety shield
≠
world model is trustworthy.
```

A corrupted predictive model can create **predictive safety illusions**.

#### Persistent-memory poisoning reference

MemSentry: https://arxiv.org/abs/2609.08747

This is not a robotics result, but it is a useful warning that a malicious or low-quality persistent-memory write can affect behavior long after the original observation disappears.

Future Clover security tests should therefore include:

```text
memory-write provenance
state-update authorization
contradictory evidence handling
poisoned observation persistence
rollback / quarantine of suspect memory
```

---

### 9. No real robot yet: use existing robot ecosystems before buying expensive hardware

The absence of hardware should not block data/model experimentation.

#### LeRobot

Official documentation: https://huggingface.co/docs/lerobot/index

LeRobot explicitly supports a no-hardware workflow using public robot datasets and simulation benchmarks, while retaining a path to real hardware later.

#### SO-101 as a future EV7 proxy option

Official guide: https://huggingface.co/docs/lerobot/en/so101

This low-cost arm is not a final Clover embodiment, but it could later provide:

```text
real camera timing
calibration drift
servo latency
contact / execution instability
real dataset collection
failure/recovery traces
```

without committing to an expensive target robot.

#### Existing SO-101 evaluation reference

**Benchmarking Vision-Language-Action Models on SO-101: Failure and Recovery Analysis**
Primary paper: https://arxiv.org/abs/2606.08881
Evidence: `PRIMARY_PAPER`

Its useful methodological contribution is failure/recovery analysis on affordable real hardware, not proof that SO-101 should be Clover's target platform.

---

### 10. Hardware robustness and model robustness should not be conflated

A later evaluation matrix should separate:

```text
new scene
new object
new task
new lighting
new camera
new calibration
new controller gain
new control rate
new gripper / wear
new robot embodiment
new runtime/backend
```

These are different generalization axes.

The latest LIBERO-RIG evidence is particularly important because it shows why visual robustness alone cannot cover perturbations that do not manifest as ordinary image changes.

---

### 11. Suggested future Clover deployment test suite

#### DT1 — device portability

Run the same frozen model on:

```text
Mac M4 reference
another backend / hardware class
```

Compare numerical behavior, latency and capability vector.

#### DT2 — quantization stress

```text
full precision
FP16
INT8
INT4 / palettized where supported
```

Measure not just task score but calibration, persistence and aliasing.

#### DT3 — latency injection

Inject controlled:

```text
fixed delay
random jitter
bursty delay
```

into the closed loop.

#### DT4 — camera fault suite

Frame drops, camera shifts, calibration error, blur and stale frames.

#### DT5 — actuator / controller fault suite

Gain, rate, delay, saturation and unavailable joint/gripper conditions.

#### DT6 — world-state integrity

Inject false/stale/poisoned persistent facts and test evidence-based correction.

#### DT7 — restart / recovery

Kill/restart runtime processes while preserving or restoring state deliberately. Measure whether the system resumes with valid belief rather than silently stale memory.

#### DT8 — checkpoint regression

Run the same fixed episode battery across every serious checkpoint.

#### DT9 — cross-simulator / cross-runtime

Move the same task/state definition across simulators or runtimes and identify which failures come from representation versus infrastructure.

---

### 12. Current research gaps

Still worth collecting:

```text
standard robotics fault-injection suites beyond driving
world-model-specific edge benchmarks
persistent-memory corruption benchmarks for embodied systems
robot-model canary/shadow deployment protocols
formal rollback semantics for stateful learned world models
power/energy measurement standards across heterogeneous edge devices
runtime deadline guarantees for learned world models
correlation between sim2sim robustness and eventual sim2real performance
security evaluation with physically realizable long-horizon attacks
hardware-setup robustness across non-manipulation embodiments
```

---

### Current rule

Do not wait for a target robot to begin deployment validation.

Do not interpret simulation as real-world proof.

Do not interpret benchmark success as runtime reliability.

Do not interpret model accuracy as hardware robustness.

A credible future Clover claim should carry both:

```text
scientific evidence level
+
deployment / validation evidence level
```

---

<a id="topic-research-engineering-validation_resources"></a>

## Engineering / Validation Resources — Current Snapshot

Source record updated: **2026-10-15**
Source intake checked through: **2026-10-15**

Companion to [`foundation-models-and-systems.md`](#topic-research-research_engineering_validation).

This file is a compact resource table for downstream validation. It is not a Clover architecture proposal.

### Current high-value resources

| Resource | Primary/official URL | What it is useful for | Current quantitative / structural signal | Does **not** establish |
|---|---|---|---|---|
| WorldOracle | https://arxiv.org/abs/2610.18826 | action-conditioned world-model evaluation against paired real executions | evaluates physical-state correctness, spatial interaction alignment, key interaction areas and multi-view coherence over long successful/failed executions | policy quality, universal physical correctness, vision-only learning |
| RoboSimStudio | https://arxiv.org/abs/2610.18835 · https://robosimstudio.github.io | interactive Real2Sim / Real2Sim2Real; explicit solver/contact/parameter hypotheses | supports visual, force-feedback and agentic Real2Sim2Real refinement using an editable physics stack | one calibrated simulator is uniquely correct |
| LIBERO-RIG | https://arxiv.org/abs/2610.18843 | hardware/setup robustness with task semantics held fixed | 11 perturbation axes × 5 severity levels; 210 conditions; pooled success 0.932 nominal → 0.767 mid → 0.509 highest severity across nine VLAs | target-hardware reliability or complete embodiment robustness |
| RoboFQE | https://arxiv.org/abs/2610.18699 | rollout-free offline policy evaluation when new robot/simulator rollouts are costly | preserves policy rankings in reported simulated/real manipulation studies, including long horizons where autoregressive video evaluators degrade | closed-loop safety, real-world transfer, causal validity |
| LADDER | https://arxiv.org/abs/2610.18053 · https://ladder.insait.ai | long-horizon manipulation scaling and compounding-error analysis | 1–10 subgoals; 145 tasks; 8 categories; 2 embodiments; 2,024 simulated episodes/system; low-level success 85.4% at one subgoal → near zero on extended tasks | orchestration alone solves physical execution |
| LoopWAM | https://arxiv.org/abs/2610.18873 · https://loop-wam.github.io | deployment-rollout learning from successful, suboptimal and failed experience | RoboChallenge Table30-V2 success reported 23.67% → 43.33% after three deployment/training rounds; shirt folding 13.20% → 55.56% after two rounds | monotonic/safe self-improvement or immunity to feedback-loop bias |
| ForceWAM | https://arxiv.org/abs/2610.18852 · https://force-wam.github.io | contact-rich WAM with future video + six-axis force/torque prediction and play-data response learning | reported 85–95% mean success on evaluated real tasks; play data adds 15–45 percentage points | RGB-only force/contact identifiability |
| Grid or Nodes? | https://arxiv.org/abs/2610.18637 | memory representation / edge-memory diagnostic under partial observability | reported out-of-view comparison: node memory 14 KB vs FloWM grid 5.6 MB; diagonal-motion detection 93% tracker vs 11% FloWM | oracle node memory is a deployable learned solution |
| GreenWAM | https://arxiv.org/abs/2610.18774 · https://greenvla.github.io | joint world-model/policy role, cross-embodiment action representation and real-time distillation | reports real-humanoid adaptation and a distilled single-step policy for real-time control | distillation preserves all world-model capabilities or one anatomical action space is universal |
| FreeBar | https://arxiv.org/abs/2610.14997 | asynchronous VLA action-chunk alignment under real-time execution | reports +10–15% average success over naive asynchronous execution and >45% lower per-chunk latency than RTC in the evaluated settings | asynchronous execution is solved generally or safety follows from chunk consistency |
| REACT | https://arxiv.org/abs/2610.12007 | rolling denoising and decoupled sensing/encoding/action streaming | reports improved reactivity and smoother execution across RoboTwin 2.0 and multiple real platforms | one streaming schedule is universally optimal |

### How to use these resources with the EV ladder

```text
EV0–EV2
controlled mechanism / simulation robustness

EV3
cross-simulator transfer

EV4
RoboFQE + offline real-data evaluation

EV5
RoboSimStudio / Real2Sim calibration + held-out trajectories

EV6
deployment runtime on Mac M4 or proxy edge compute
+ FreeBar/REACT-style timing stress tests where relevant

EV7
low-cost proxy hardware
+ LIBERO-RIG-inspired setup perturbations

EV8
target robot
+ WorldOracle-style predicted-vs-real consequence comparison
```

### Required claim discipline

Keep these distinctions explicit:

```text
offline policy ranking
≠ closed-loop validation

real2sim fit
≠ uniquely identified real physics

world-model visual quality
≠ real-execution consequence fidelity

one-step / short-horizon success
≠ long-horizon reliability

scene robustness
≠ hardware/setup robustness

real-time distillation
≠ preserved epistemic / memory / causal capability

successful deployment self-training
≠ safe monotonic improvement
```

### Current Mac mini M4 relevance

The present Mac mini M4 can already support meaningful validation work before a target robot exists:

```text
MLX / Core ML profiling
quantization / memory studies
stateful streaming prototypes
MuJoCo diagnostics
fault / latency injection
offline real-video evaluation
RoboFQE-style offline evaluation if the required trajectories are available
```

Remote Linux/NVIDIA compute should be introduced only when a chosen experiment specifically requires Isaac Sim/Isaac Lab or large-scale GPU simulation.

### Remaining validation gaps

Still weakly covered by current literature:

```text
world-model-specific edge benchmark on Apple / NPU-class devices
quantization effects on uncertainty / persistence / state aliasing
standardized sim2sim → sim2real predictive correlation
formal persistent-state rollback after model rollback
world-state / memory poisoning benchmark
shadow/canary deployment protocols for robot world models
standard manipulation fault-injection suite spanning sensor + compute + actuation
energy-aware active perception under real edge power budgets
numerical divergence of stateful world models across hardware backends
```

---

<a id="topic-research-emerging-cv_embodiment_systems_2026-10-15"></a>

## Stage-1 Emerging Audit — Remaining CV, Embodiment and Serving Boundaries

Source record updated: **2026-10-15**
Source intake checked through: **2026-10-15**

> Mother question: **How can a machine understand the real world through vision alone?**

This audit follows [`foundation-models-and-systems.md`](#topic-research-emerging-jepa_rsi_runtime_2026-10-15) and asks whether the latest arXiv/GitHub sweep exposes any remaining boundary that the stable Stage-1 map still underweights.

Conclusion: no new top-level lifecycle stage is needed, but the following cross-boundaries should be explicit.

---

### 1. Frame RGB is a design choice, not the definition of all visual sensing

Clover's current scientific protocols `V0–V3` deliberately use RGB. Keep that constraint stable when making Clover claims.

However, adjacent **visual-only sensor families** are useful counterfactuals because they reveal information that frame RGB may discard before learning begins.

### EventCV / event-based robotic vision

Paper: https://arxiv.org/abs/2609.21330
Project: https://eventcv.net
Evidence: `PRIMARY_PAPER` / `OFFICIAL_PROJECT`

Event cameras provide asynchronous per-pixel brightness-change events at microsecond-scale temporal resolution, with high dynamic range and low power characteristics. EventCV provides a robotics-oriented library with denoising, geometry, feature learning, motion estimation, video-to-event simulation and ONNX inference, and reports Jetson Orin AGX case studies.

Stage-1 role:

```text
frame RGB
vs
event vision
```

is **not** a Clover baseline contest. It is a sensor-information diagnostic.

Questions:

```text
Which fast contact/slip/impact/motion evidence is aliased by ordinary frame sampling?
How much can higher RGB frame rate recover?
What is lost because of exposure / motion blur rather than model architecture?
What information requires a different optical sensor?
```

Important rule:

```text
event-camera result
≠ V0–V3 RGB result
```

Do not silently broaden “vision alone” from RGB to arbitrary visual sensors in Clover claims.

---

### 2. World models can be hardware-locked because body morphology changes dynamics

### Morphology-conditioned quadrupedal world models

Paper: https://arxiv.org/abs/2604.08780
Evidence: `PRIMARY_PAPER`

The paper studies world models conditioned explicitly on engineering morphology specifications instead of forcing the model to infer static properties such as limb length/mass only from motion history.

It motivates a distinction already implicit in Clover but worth making explicit:

```text
environment dynamics
≠
robot morphology
≠
actuator/controller dynamics
```

and:

```text
world model generalization
≠
embodiment generalization
≠
morphology generalization
```

The authors themselves characterize the method as distribution-bounded within the studied quadruped family, not a universal physics engine.

Stage-1 landing:

- self/body schema;
- embodiment-conditioned state/action semantics;
- adaptive abstraction;
- engineering/hardware robustness;
- system identification.

Future Clover experiment:

> Hold scene/task fixed while changing body geometry or actuator parameters; test whether the world-state representation separates external-world change from embodiment change.

---

### 3. Affordance is becoming a foundation-model target rather than only an auxiliary head

### AFUN — affordance foundation model

Paper: https://arxiv.org/abs/2606.02551
Project: https://www.zhaoningwang.com/AFUN
Evidence: `PRIMARY_PAPER` / `OFFICIAL_PROJECT`

AFUN predicts both:

```text
where to interact
+
how the object should move after contact
```

from task-conditioned RGB-D input, and aligns heterogeneous robot/human/simulation/scan data into a standardized affordance schema.

Why it matters:

```text
object identity
≠
object geometry
≠
functional affordance
```

and affordance may depend jointly on:

```text
world state
× task
× embodiment
```

rather than being a fixed intrinsic label.

Boundary:

- RGB-D means this is not a strict V0 result;
- language/task conditioning injects semantic priors;
- strong affordance prediction does not prove complete object physics.

This should strengthen Stage-2 analysis of R26 affordance/action-relevant perception.

---

### 4. Test-time adaptation is broader than verifier-guided Best-of-N

### RoboTTT — context compressed into fast weights

Paper: https://arxiv.org/abs/2607.15275
Project: https://research.nvidia.com/labs/gear/robottt/
Evidence: `PRIMARY_PAPER` / `OFFICIAL_PROJECT`

RoboTTT introduces another answer to the long-context problem:

```text
raw token / KV history
vs
explicit persistent memory
vs
history compressed into adaptive fast weights
```

Its recurrent state is partly represented by model parameters updated through gradient descent during training and inference. The paper reports context scaling to 8K robot timesteps without inference latency growing with context length in its design.

Required Clover questions:

```text
What facts are retained in fast weights?
Can a fact be revised selectively?
How is provenance represented?
Can updates contaminate unrelated skills?
What is rollback semantics?
How does fast-weight memory compare under equal bytes/latency with explicit state + evidence retrieval?
```

This belongs simultaneously to:

- long context vs memory;
- test-time adaptation;
- continual learning;
- stateful rollback;
- post-training / deployment learning.

### RA-VLA — retrieval-augmented test-time adaptation

Paper: https://arxiv.org/abs/2608.25585
Evidence: `PRIMARY_PAPER`

RA-VLA is a useful counter-hypothesis in which expert context is retrieved and grounded at test time without changing the base policy through conventional fine-tuning.

Keep distinct:

```text
retrieval-conditioned adaptation
≠
fast-weight adaptation
≠
verifier/search scaling
≠
online gradient fine-tuning
```

These methods should not all be reported under the vague label `test-time improvement`.

---

### 5. JEPA/WAM naming itself now requires artifact-level disambiguation

Two different papers submitted on 2026-10-08 use the name **LeWAM**.

### LeWAM A — End-to-End World and Action Modeling with JEPAs

Paper: https://arxiv.org/abs/2610.12818

Core idea:

```text
joint next-latent prediction
+
action flow matching
+
latent-distribution constraint
```

with one model supporting both direct policy execution and sampled-action planning.

### LeWAM B — A JEPA World Action Model with Diffusion-Steering-Based MPC

Paper: https://arxiv.org/abs/2610.12407

Core idea:

```text
bidirectional JEPA dynamics/policy model
+
forward/backward/inverse/policy modes
+
planning in policy-noise space to reduce model exploitation
```

These are scientifically distinct methods despite the shared acronym/name.

Repository rule:

```text
method name alone is never a stable identifier.
```

For every fast-moving method preserve:

```text
exact title
arXiv / DOI id
authors
version/date
code repository
checkpoint/config if relevant
```

This rule is especially important for WAM/VLA/RSI literature where naming collisions and version drift are common.

---

### 6. Video-model continued pretraining is becoming part of WAM design

### Video Prediction Policy 2 (VPP2)

Paper: https://arxiv.org/abs/2610.10270
Evidence: `PRIMARY_PAPER`

VPP2 attributes WAM failures partly to a base video model not being specialized for manipulation. Its recipe includes:

```text
large-scale manipulation-video continued pretraining
+
event-level video pretraining
+
post-training/distillation into a single-step visual planner
+
Mixture-of-Transformers action module
```

Stage-1 implication:

> The quality of a WAM is not only a function of the action head or world-action objective. The **video foundation model's domain curriculum** can materially determine downstream physical prediction/action quality.

This reinforces Clover's training rule:

```text
backbone architecture
≠
backbone pretraining domain
≠
continued pretraining
≠
action post-training
```

---

### 7. Multi-robot serving / edge-cloud scheduling is different from single-model latency

### Robion — efficient VLA management and serving for robot factories

Paper: https://arxiv.org/abs/2609.12075
Evidence: `PRIMARY_PAPER`

Robion treats VLA serving under multiple robots/models and safety-relevant service-level objectives (SLOs) as a systems problem. It co-schedules VLM and action-diffusion stages, manages GPU placement and prioritizes requests by remaining SLO budget.

Why this matters for Clover later:

```text
single-robot local latency
≠
shared edge-server latency
≠
fleet SLO reliability
```

A future deployment may choose among:

```text
fully onboard
onboard fast path + remote slow path
shared edge inference
cloud frontier comparator
```

Required metrics:

```text
p50 / p95 / p99 camera→action latency
deadline miss rate
queueing delay
network delay
robot concurrency
model-switch/load cost
fairness / starvation
fallback behavior when server/network is unavailable
```

Throughput alone is insufficient for embodied control.

---

### 8. New boundary taxonomy from this audit

Add these as comparison axes, not lifecycle stages:

```text
B-SENSOR  frame RGB vs adjacent visual sensor evidence
B-BODY    external world vs morphology/body dynamics
B-AFF     object state vs embodiment/task-relative affordance
B-TTA     retrieval vs fast-weight vs verifier/search vs gradient test-time adaptation
B-ID      artifact identity / naming / version disambiguation
B-CURR    generic video pretraining vs manipulation-specialized continued pretraining
B-SERVE   local single-robot vs shared edge/fleet serving
```

---

### 9. Does this reveal a missing foundational domain?

No.

These findings fit existing Stage-1 surfaces:

```text
Observation Physics
State Variables
Adaptive Abstraction / Embodiment
Affordance / Action-Relevant Perception
Foundation Model Systems
Training / Post-Training
Engineering / Deployment
Frontier
```

The important change is analytical discipline: future Stage-2 reports must distinguish sensor information, body morphology, memory mechanism, test-time adaptation type, training curriculum and serving topology instead of attributing all gains to “the model.”

---

<a id="topic-research-emerging-jepa_rsi_runtime_2026-10-15"></a>

## Stage-1 Emerging Cross-Boundary Audit — Embodied JEPA, RSI, Runtime and Physical-AI Systems

Source record updated: **2026-10-15**
Source intake checked through: **2026-10-15**

> Mother question: **How can a machine understand the real world through vision alone?**

This is supporting Stage-1 material. It does **not** add a new project stage and it does **not** promote any current mechanism into Clover Innovation.

The purpose of this audit is to cover several fast-moving 2026 clusters that cut across the existing research map:

```text
latent predictive world modeling / JEPA
cross-embodiment latent action spaces
inference-time policy scaling / verifiers
world-action-model acceleration
recursive self-improvement of agents / harnesses / research systems
embodied recursive improvement
open-source local embodied experimentation
video-foundation-model features used for perception
multi-view / multimodal world-state unification
```

Keep evidence types explicit:

```text
PRIMARY_PAPER
OFFICIAL_PROJECT
OPEN_SOURCE
OPEN_SOURCE_PROJECT / ENGINEERING_REFERENCE
COMMUNITY_RESEARCH_REPOSITORY
```

A GitHub project or research workspace is not automatically primary scientific evidence.

---

### 1. Embodied JEPA / latent predictive control is now a distinct method cluster

The earlier Stage-1 map already tracked V-JEPA and predictive latent world models. The 2026 robot literature now justifies treating **action-conditioned JEPA / latent predictive control** as a concrete method family rather than only a generic video-prediction idea.

### 1.1 RoboJEPA — scaling robotic latent world models

Paper: https://arxiv.org/abs/2610.10515
Official code: https://github.com/facebookresearch/robo_jepa
Evidence: `PRIMARY_PAPER` / `OPEN_SOURCE`

Key reported design:

```text
frozen V-JEPA 2.1 visual encoder
+
action-conditioned latent predictor
+
robot data from 12 embodiments
+
22M → 8B predictor scaling
+
CEM / MPC planning in latent space
```

The official repository releases multiple predictor sizes/checkpoints and deployment code.

Reported scientific signals:

- latent rollout / imagination error follows a compute scaling law in the reported regime;
- downstream planning improves predictably with compute;
- imagination error correlates with planning performance;
- zero-shot goal-image planning is demonstrated in RoboCasa and on a real Franka;
- future video decoding is optional rather than required for control.

What it does **not** establish:

```text
JEPA latent state is open-world sufficient
imagination error is a universal proxy for robot success
frozen V-JEPA preserves every physical variable
12 embodiments solve embodiment generalization generally
scaling to 8B removes state aliasing / uncertainty / causal limitations
```

High-priority Stage-2 question:

> Which information becomes better with predictor scale, and which information is irreversibly absent because the frozen visual representation never encoded it?

---

### 1.2 ThinkJEPA — dense dynamics + slow semantic thinker

Paper: https://arxiv.org/abs/2603.22281
Code: https://github.com/Hai-chao-Zhang/ThinkJEPA
Evidence: `PRIMARY_PAPER` / `OPEN_SOURCE`

ThinkJEPA explicitly combines:

```text
fast / dense JEPA dynamics pathway
+
slower sparsely sampled VLM semantic pathway
```

This is a direct scientific comparator for Clover's existing fast-state-updater / slow-reasoner question.

Important boundary:

```text
semantic guidance
≠
physical state evidence
```

The VLM branch can inject language/world priors not learned from vision-only physical interaction.

---

### 1.3 Demo-JEPA — demonstration intent as future latent trajectory

Paper: https://arxiv.org/abs/2605.20811
Evidence: `PRIMARY_PAPER`

Core counter-hypothesis:

```text
cross-embodiment imitation
need not align source actions directly;
visual demonstration can specify a target-compatible future latent trajectory.
```

This is relevant to human-video transfer, sufficient state and cross-embodiment learning.

It does not prove that latent future trajectories capture all contact / force / material constraints required for execution.

---

### 1.4 LeapBot-WA — JEPA as a world anchor

Paper: https://arxiv.org/abs/2607.23969
Code: https://github.com/LeapWM/leapbot-wa
Evidence: `PRIMARY_PAPER` / `OPEN_SOURCE`

LeapBot-WA moves WAM training away from pixel-level future reconstruction toward predictive latent alignment and prunes the heavy dynamics anchor branch at inference.

This is a useful comparator for:

```text
pixel future generation
vs
latent future prediction
vs
future-state action inference
```

and for the question of whether training-time privileged dynamics structure can be removed without losing action-relevant information at deployment.

---

### 1.5 SkyJEPA — interpretable probes + embedded real-time control

Paper: https://arxiv.org/abs/2606.23444
Evidence: `PRIMARY_PAPER`

SkyJEPA combines a latent dynamics model with a physics-inspired prober that maps frozen latent state into interpretable physical quantities, then uses sampling-based optimal control for quadrotor control and reports zero-shot sim-to-real experiments.

Research role:

```text
distributed latent
+
interpretable physical probe
+
model-based control
```

is another hybrid route between opaque latent state and fully explicit state.

---

### 1.6 Vision-Predictor-Action (VPA) — small predictive control on Apple M4

Paper: https://arxiv.org/abs/2610.15556
Code: https://github.com/ylee-sling/Vision-Predictor-Action
Evidence: `PRIMARY_PAPER` / `OPEN_SOURCE`

Reported proof-of-concept configuration:

```text
shared vision encoder
frozen text encoder
JEPA next-latent predictor
skill selector
flow-matching action chunk
<20M trainable parameters
```

The paper reports roughly 10–14 ms per decision step on an Apple M4 for its single-camera reference configuration and 40% success over 200 LIBERO-10 episodes for the reported two-camera policy.

Treat this as **preliminary**, not as evidence that a small JEPA controller already solves general embodied intelligence.

It is nevertheless highly relevant to Clover's Mac-M4 proxy experiments because it demonstrates a tractable low-latency JEPA/action architecture on the project's hardware class.

---

### 2. Cross-embodiment action representation is becoming a first-class world-model variable

### LAC-WM

Paper: https://arxiv.org/abs/2610.10846
Project: https://lacwm.github.io/
Evidence: `PRIMARY_PAPER`

LAC-WM learns a shared latent action space across embodiments and compares it against explicit action-conditioned world modeling.

Reported result: explicit action conditioning forms more disjoint representations across embodiments, whereas the learned latent action space improves adaptation to unseen embodiments in the evaluated settings.

Stage-1 implication:

```text
state alignment
and
action alignment
are separate problems.
```

A universal world representation can still fail if action semantics fragment by embodiment.

Do not conclude that one latent action space is universally physically sufficient.

---

### 3. Test-time policy scaling must be separated from base-policy capability

### DiVeR

Paper: https://arxiv.org/abs/2610.04933
Evidence: `PRIMARY_PAPER`

DiVeR treats a frozen VLA as a stochastic action proposer and trains a lightweight verifier, focusing supervision on sparse decision-critical states identified by dispersion in action-expert representations.

This adds an important system decomposition:

```text
base policy
+
number of sampled action candidates N
+
verifier
+
selection rule
+
inference budget
→ deployed behavior
```

Therefore future Clover evaluations must record test-time sampling / search / verifier budget separately from model weights.

New comparison axis:

```text
training-time scaling
vs
test-time action scaling
```

and:

```text
base-policy success
≠
policy + verifier + Best-of-N success.
```

---

### 4. WAM performance optimization now requires state-staleness semantics

### 4.1 MARS

Paper: https://arxiv.org/abs/2610.17141
Code: https://github.com/PKU-VaLuE-Lab/MARS
Evidence: `PRIMARY_PAPER` / `OPEN_SOURCE`

MARS profiles and accelerates WAM inference across three sources of redundancy:

```text
attention computation
diffusion / flow denoising
cross-query future-visual representation reuse
```

It uses online verification before speculative reuse.

Stage-1 implication:

> An inference cache is not merely a systems optimization; in closed-loop robotics it has a **validity / staleness condition** tied to new observations and actions.

---

### 4.2 Δ Flow Matching

Paper: https://arxiv.org/abs/2610.15794
Evidence: `PRIMARY_PAPER`

Instead of generating actions/future states from a fixed Gaussian source, Δ-flow starts from recent history plus mild noise and learns a smaller residual transport.

Reported experiments integrate it into π0.5, ImageWAM and Fast-WAM and show faster training / single-step inference in the evaluated settings.

Research implication:

```text
generative prior / source distribution
```

is a first-class training and inference variable for robot foundation models, not just an implementation detail.

---

### 4.3 WAMachine

Paper: https://arxiv.org/abs/2609.34608
Evidence: `PRIMARY_PAPER`

WAMachine preserves/adapts intermediate computation across:

```text
closed-loop replans
denoising steps
Transformer layers
```

using trajectory remapping, observation rebinding and residual rescaling, with consistency/probe checks to decide when state must be refreshed.

Important Clover distinction:

```text
reusable inference state
≠
valid inference state
```

Cross-hardware / quantized / asynchronous implementations should measure stale-state failure, not only speed.

---

### 4.4 AsyncVLA and real-time WAM execution

AsyncVLA: https://arxiv.org/abs/2602.13476
World Action Models in Real Time: https://arxiv.org/abs/2608.01880
Evidence: `PRIMARY_PAPER`

AsyncVLA explicitly separates a remote >8B semantic policy from a lightweight onboard 76M Edge Adapter and evaluates dynamic communication delays up to six seconds.

The real-time WAM study shows that temporal alignment between observation, predicted chunk and executed action is fundamental; asynchronous execution can fail even when the underlying policy is strong.

Stage-1 implication:

```text
fast model + slow model
```

requires a synchronization / timestamp / stale-guidance model, not only two inference loops.

---

### 5. Recursive self-improvement needs a strict taxonomy

The 2026 RSI literature is growing quickly. Clover should not use “self-improvement” as a single undifferentiated label.

Use at least:

```text
RSI-A  artifact / memory / skill self-evolution
RSI-H  harness / prompt / tools / control-flow self-evolution
RSI-D  data / curriculum / training-recipe self-improvement
RSI-M  model-weight improvement
RSI-R  research-agent / experiment-process improvement
RSI-E  embodied deployment / policy improvement
RSI-J  joint model + harness + data co-evolution
```

Also record:

```text
editable surface
immutable evaluator
train/evolve tasks
hidden held-out tasks
resource budget
accepted-change lineage
rollback mechanism
whether the next cycle actually inherits the accepted change
```

A system is not demonstrated recursively self-improving merely because an agent writes a new prompt once.

---

### 6. Primary RSI references that materially change the map

### 6.1 AIDE² — research agent edits its own code

Paper: https://arxiv.org/abs/2609.26457
Evidence: `PRIMARY_PAPER`

AIDE² proposes modifications to its own research-agent implementation, evaluates them, and carries accepted rewrites into the next improvement generation. The paper reports an autonomous eight-day run with seven successive improvements and held-out transfer across multiple AI-R&D domains.

High-value methodological lesson:

```text
self-improvement claim
requires
hidden / held-out evaluation
+
accepted-change inheritance
+
lineage
```

---

### 6.2 RRSI — regularize harness evolution against overfitting

Paper: https://arxiv.org/abs/2609.24972
Code: https://github.com/google-research/rrsi
Evidence: `PRIMARY_PAPER` / `OPEN_SOURCE`

RRSI evolves prompts, control flow, tools, memory and context management around a frozen model while regularizing proposal/selection to reduce benchmark-specific overfitting.

Critical lesson:

```text
ID improvement under evolution tasks
≠
OOD improvement
```

RSI itself needs regularization and held-out generalization tests.

---

### 6.3 RSI-Master — structured autonomous post-training research

Paper: https://arxiv.org/abs/2609.35561
Evidence: `PRIMARY_PAPER`

RSI-Master provides an Experiment OS plus Worker/Reviewer research DAG to reduce action hacking and strategy lock-in during autonomous post-training research.

Clover relevance is methodological:

```text
experiment traceability
alternative-hypothesis exploration
reviewer/worker separation
persistent research records
```

not evidence for a physical world representation.

---

### 6.4 RSI-Forge — research environment generation is itself a bottleneck

Paper: https://arxiv.org/abs/2610.09426
Evidence: `PRIMARY_PAPER`

RSI-Forge turns published papers into executable improvement environments. It reports 210 environments over 18 fields, with 90 independently reviewed by domain experts.

Experts are more critical than agent judges about shortcut resistance and source-paper faithfulness.

Stage-1 lesson:

> Self-improvement quality is bounded by the quality of the evaluator/environment; automated judges can overestimate evaluator validity.

---

### 6.5 RSIGym — Data / Harness / Joint improvement tracks

Paper: https://arxiv.org/abs/2610.10310
Evidence: `PRIMARY_PAPER`

RSIGym exposes training, inference, rollout, evaluation and sandbox services under shared budget/permission controls and explicitly separates:

```text
Data improvement
Harness improvement
Joint improvement
```

This is a useful systems reference for future autonomous Clover experimentation.

---

### 6.6 HELIX — model / harness / data co-evolution

Paper: https://arxiv.org/abs/2608.13951
Code: https://github.com/HKUDS/HELIX
Evidence: `PRIMARY_PAPER` / `OPEN_SOURCE`

HELIX treats harness evolution as both immediate execution improvement and a source of verified successes, regressions, near misses and alternatives for subsequent model training.

Important loop:

```text
harness change
→ trajectories
→ verified training data
→ model update
→ new harness search
```

This should be kept separate from pure weight-only RSI.

---

### 6.7 Harmony Harness / Harness² — compositional and open-world harness evolution

Harmony Harness: https://arxiv.org/abs/2610.15150
Harness²: https://arxiv.org/abs/2610.14224
Evidence: `PRIMARY_PAPER`

Harmony Harness treats harness evolution as multi-objective optimization and separates reusable mechanisms from benchmark-specific adaptations.

Harness² studies recursive harness refinement when open-world tasks lack ground-truth online verifiers and adds a second recursion level that transfers experience from task-specific refinements into a continual improvement harness.

Stage-1 question:

> How should a self-improving system improve under incomplete evaluators without gradually optimizing the evaluator's blind spots?

---

### 6.8 AReaL-RSI — scaling recursive improvement is a resource-allocation problem

Paper: https://arxiv.org/abs/2610.18083
Evidence: `PRIMARY_PAPER`

Submitted 2026-10-13.

AReaL-RSI organizes a persistent team of research agents, with role specialization, adaptive research orientations, conditional memory sharing and evidence-based review across campaigns.

New Stage-1 axis:

```text
RSI quality
is a function of
search budget + role allocation + memory sharing + evidence validity
```

not merely whether one agent can edit itself.

---

### 6.9 Process-level evaluation of self-evolution

Generalized Agent Iteration: https://arxiv.org/abs/2609.13406
EvoPathBench / process-level evaluation: https://arxiv.org/abs/2609.24663
Evidence: `PRIMARY_PAPER`

These works provide useful conceptual/evaluation constraints:

- distinguish whether the improvement mechanism belongs inside the agent;
- distinguish externally grounded evaluation from self-referential evaluation;
- evaluate successive evolution checkpoints, not only final endpoint performance;
- measure retention, OOD transfer and adaptation after unrelated updates.

---

### 7. Embodied RSI is now a real robot-learning subdirection

### 7.1 EmbodiRSI

Paper: https://arxiv.org/abs/2609.38905
Evidence: `PRIMARY_PAPER`

EmbodiRSI closes a deployment-specific loop:

```text
real deployment scene
→ task-specific simulation
→ policy rollout / failure
→ corrective trajectories + adaptive data collection
→ policy update
→ real refinement
→ next cycle
```

The paper reports two recursive updates improving its scene-balanced simulation success and reports a data-efficient real-world adaptation result in the studied tabletop settings.

This directly links Clover's existing:

```text
Real2Sim2Real
+
failure / recovery data
+
post-training
+
model discovery
+
deployment adaptation
```

Do not generalize its reported gains into a claim that embodied RSI is safe, monotonic or universally data-efficient.

---

### 7.2 RegenHarness — evidence-gated embodied harness changes

Paper: https://arxiv.org/abs/2609.27612
Evidence: `PRIMARY_PAPER`

RegenHarness separates proposal, execution, verification, commitment and bounded recovery, and allows versioned modifications to context rules, task templates, routing and recovery policies while preventing the agent from weakening its trusted commit gate.

This is a useful embodied reference for:

```text
self-improvement
+
immutable safety / verification boundary
+
versioned rollout / rollback
```

---

### 7.3 Embodied Turing Machines / COAP

Paper: https://arxiv.org/abs/2610.12369
Evidence: `PRIMARY_PAPER`

This is a strong counter-hypothesis to always keeping a large learned model in the control loop.

COAP proposes:

```text
camera / proprioceptive evidence
→ explicit state
→ reusable code policy
```

and lets coding agents improve the shared code library across tasks.

The reported RoboDojo result is evidence for the evaluated system, not proof that explicit code/state dominates VLA/WAM generally.

Important Clover question:

> Which parts of embodied intelligence should remain learned, and which can be compiled into inspectable stateful code once the relevant state is reliably estimated?

---

### 8. AgentRSI GitHub repository — classify correctly

Repository: https://github.com/heng526/AgentRSI
Evidence: `COMMUNITY_RESEARCH_REPOSITORY`

The repository describes itself as the canonical P0 repository for a CVPR-RSI research project and contains:

```text
paper translations / extracts
reproduction code and configurations
literature-search records
reading notes
robot scoring reports
ResearchOps protocol
```

Its ResearchOps layer uses append-only outbox records and reducer-owned state / ledgers.

Useful Clover lesson:

```text
research-agent actions
should produce immutable / auditable evidence records
```

But the repository itself is **not** evidence that a particular RSI scientific claim is valid. Use linked primary papers for method claims.

---

### 9. EmbodiedJev / 行知 — useful engineering reference, not a new scientific method

Repository: https://github.com/FBddcz/embodied-jev
Evidence: `OPEN_SOURCE_PROJECT / ENGINEERING_REFERENCE`

Current repository capabilities include:

```text
MuJoCo + Franka Panda
rule baseline
local MiniCPM5-2B
cloud/API model adapters
structured state / RGB-D / direct RGB options
external and wrist cameras
short-step and hierarchical action modes
same-task / same-seed multi-model comparison
trajectory replay / JSON export
pre-execution simulation checks
macOS / Linux workflow
```

The project itself explicitly distinguishes controller-generated geometry / candidate logic / safety checks from learned model capability.

Clover use:

```text
EV1 controlled simulation
EV6 local runtime / software HIL
Mac-M4 model comparison
trajectory / experiment provenance
fault / disturbance experiments
candidate-action preflight
```

Do **not** use EmbodiedJev results as evidence that:

```text
a model understands the real world
MuJoCo success transfers to real hardware
controller-provided structure was learned by the model
vendor APIs are comparable without pinning model/runtime/settings
```

It is a useful workbench/reference architecture, not a Clover baseline by default.

---

### 10. Computer-vision boundary: generative video backbones are becoming perception backbones

### RLHND

Paper: https://arxiv.org/abs/2610.09455
Evidence: `PRIMARY_PAPER`

RLHND repurposes a pretrained Cosmos 3 video diffusion backbone as a deterministic clip-level representation for egocentric hand tracking, then adds a tactile expert for contact/force prediction.

Stage-1 implication:

```text
generative video foundation model
≠ only a generator;
it may also act as a strong motion / interaction representation.
```

But contact/force supervision is not RGB-only physical evidence; preserve provenance.

This suggests an Analysis comparison among:

```text
DINO-style static visual backbone
V-JEPA predictive backbone
video-diffusion backbone used as features
learned geometry backbone
```

under the same physical-state probes.

---

### 11. Multi-view / multimodal world models expose another representation boundary

### Thinker-WM

Paper: https://arxiv.org/abs/2610.18447
Project: https://thinkercosmos.ubtrobot.com
Evidence: `PRIMARY_PAPER` / `OFFICIAL_PROJECT`

Submitted 2026-10-13 and revised 2026-10-14.

Thinker-WM jointly models:

```text
RGB
metric depth
action
```

through a shared intermediate dynamics Transformer with modality-specific encoders/decoders.

Reported training corpus:

```text
~20K h egocentric video
~10K h real robot
~1K h simulation
~4K h real robot with aligned depth supervision
```

This is a strong counter-hypothesis that geometry, appearance and action should share dynamics parameters.

It does **not** demonstrate L0/L1 vision-only learning because depth and action supervision materially contribute to training.

### PAIWorld

Paper: https://arxiv.org/abs/2606.18375
Evidence: `PRIMARY_PAPER`

PAIWorld explicitly adds cross-view communication and 3D geometric priors to multi-view world modeling.

Stage-1 implication:

```text
concatenating multiple camera tokens
≠
3D-consistent multi-view world state.
```

This should be tested explicitly under Clover's `V2` protocol.

---

### 12. Physical-process supervision: not only endpoint visual quality

### EVEWorld

Paper: https://arxiv.org/abs/2610.03374
Evidence: `PRIMARY_PAPER`

EVEWorld argues that world models can exhibit “model laziness”: producing visually plausible output while violating instance-level physical evolution across time.

It introduces process-level temporal/instance supervision and a Model Laziness Rate diagnostic.

Clover relevance:

```text
endpoint appearance
≠
correct physical process
```

This complements WorldOracle / RoboWM-Bench / What-If World and should enter the world-model evaluation cluster.

---

### 13. What this audit adds to Stage 1

No new top-level project stage is needed. The stable Stage-1 map should absorb these as cross-boundary research clusters:

```text
C1 embodied JEPA / latent predictive control
C2 unified latent actions across embodiments
C3 test-time VLA scaling / verifier-guided action selection
C4 inference-state reuse with staleness / verification semantics
C5 recursive model / harness / data / research-system improvement
C6 embodied RSI / Real2Sim2Real self-improvement
C7 process-level self-evolution evaluation
C8 generative video backbones as perception representations
C9 explicit multi-view geometric consistency
C10 stateful code as a counter-hypothesis to always-on foundation models
```

These map into existing Stage-1 surfaces rather than becoming separate lifecycle stages.

---

### 14. New mandatory comparison fields for Stage 2

For relevant methods, record:

```text
predictive target: pixels / latent / geometry / action / multimodal
frozen or adapted visual backbone
latent scale / predictor scale
planning method: direct policy / CEM / MPC / search / verifier
cross-embodiment action representation
inference-time candidate count / verifier budget
inference-state reuse and refresh criterion
stale-state detection
fast/slow path synchronization
editable RSI surface
immutable evaluator / safety boundary
hidden / held-out evaluation
accepted-change inheritance
rollback / lineage
research / training compute budget
whether improvement persists across later cycles
whether model weights, harness, data, or code changed
```

---

### 15. Immediate Stage-2 additions from this audit

High-value clusters:

```text
RoboJEPA
vs ThinkJEPA
vs LeapBot-WA
vs Demo-JEPA
vs V-JEPA 2/2.1

LAC-WM
vs explicit cross-embodiment action conditioning

DiVeR
vs base VLA
vs policy + verifier / Best-of-N

MARS
vs WAMachine
vs Δ-flow
vs asynchronous WAM execution

AIDE²
RRSI
RSI-Master
RSI-Forge
RSIGym
HELIX
Harmony Harness / Harness²
AReaL-RSI

EmbodiRSI
RegenHarness
Embodied Turing Machines / COAP

Thinker-WM
PAIWorld
RLHND
EVEWorld
```

The goal is not to choose winners. The goal is to identify which mechanisms improve:

```text
world-state quality
physical correctness
open-world robustness
real-time execution
adaptation efficiency
research efficiency
```

and which gains come mainly from harness, evaluator, compute budget, privileged evidence or deployment engineering.

---

### Current conclusion

The latest arXiv/GitHub sweep does **not** reveal a missing foundational domain comparable to geometry, causality, memory or deployment.

It does reveal several fast-growing cross-boundary method families that materially change how Clover should analyze modern systems:

> **latent predictive control, test-time verification, stateful inference reuse, recursive improvement, and process-level evaluation now deserve first-class comparison axes.**

Continue Stage-1 freshness updates for these clusters, but keep the primary work moving toward method-by-method Stage-2 Analysis.

---

<a id="topic-research-emerging-security_wholebody_multiagent_2026-10-15"></a>

## Stage-1 Emerging Audit — Physical Security, Whole-Body State and Multi-Agent World Models

Source record updated: **2026-10-15**
Source intake checked through: **2026-10-15**

> Mother question: **How can a machine understand the real world through vision alone?**

This is supporting Stage-1 material. It does not create a new Clover lifecycle stage or promote any current method into Innovation.

This audit covers four cross-boundaries that remained underweighted after the Embodied-JEPA / RSI re-audit:

```text
physical-world adversarial robustness / visual prompt injection
whole-body humanoid predictive state and balance-aware control
multi-robot / shared-intention world models
action competence that can arise from non-visual priors
```

---

### 1. Physical-world adversarial robustness is a first-class embodied failure mode

#### Universal Adversarial Objects for VLA policies

Paper: https://arxiv.org/abs/2609.39178
Evidence: `PRIMARY_PAPER`

The work optimizes the texture of a physical object placed inside the robot's field of view and reports large task-success degradation for evaluated VLA policies in simulation and real-world settings.

Stage-1 implication:

```text
ordinary visual OOD
≠
adversarially chosen visual evidence
```

and:

```text
clean-scene robustness
≠
physical-world adversarial robustness
```

A persistent world model may amplify the risk if one poisoned observation is converted into a long-lived state or memory.

#### Physical prompt injection through visible text

Paper: https://arxiv.org/abs/2608.05715
Evidence: `PRIMARY_PAPER`

This work studies human-readable adversarial text physically placed in the robot scene. The attack targets the VLM planner through the visual channel rather than through the user's explicit instruction channel.

Important distinction:

```text
scene text as world evidence
≠
scene text as trusted instruction
```

For Clover, any future visual-language interface should preserve provenance:

```text
user instruction
observed scene text
retrieved memory
system policy
```

must not collapse into one undifferentiated prompt stream.

#### Additional security references

- Partially Observable Adversarial Patch Attacks on VLAs — https://arxiv.org/abs/2606.03556
- TrustVLA — https://arxiv.org/abs/2607.12571
- Hidden in Plain Sight / DURA — https://arxiv.org/abs/2608.10393
- Trajectory-Level Redirection Attacks — https://arxiv.org/abs/2606.12978
- VLA Safety survey — https://arxiv.org/abs/2604.23775

Research questions:

```text
Can visual attacks poison persistent world state after the trigger disappears?
Can contradiction/evidence revision remove poisoned beliefs?
Can runtime monitors distinguish adversarial evidence from ordinary scene change?
Does quantization/token pruning make attack sensitivity better or worse?
Can a safety layer remain effective if the world-state representation is already compromised?
```

---

### 2. Whole-body humanoid control makes body state impossible to treat as a side channel

#### World-Model-Augmented Visual Locomotion

Paper: https://arxiv.org/abs/2609.02542
Evidence: `PRIMARY_PAPER`

The reported system combines a recurrent predictive feature with PPO for humanoid foothold-constrained locomotion and deploys on a physical Unitree G1.

Its provenance is important:

```text
onboard depth
+
proprioception
+
learned recurrent world model
```

so it is **not** a V0 vision-only result.

Scientific lesson:

```text
external terrain state
+
body configuration / momentum / balance state
```

must be jointly sufficient for whole-body action.

#### ω-0 — latent predictive whole-body WAM

Paper: https://arxiv.org/abs/2608.06375
Evidence: `PRIMARY_PAPER`

ω-0 couples compact future observation embeddings with whole-body action latents for concurrent locomotion and manipulation.

Stage-1 relevance:

```text
arm manipulation state
≠
whole-body loco-manipulation state
```

because balance, base motion, posture and contact transitions can make the same object-level plan executable or impossible.

#### MetaWorld-X

Paper: https://arxiv.org/abs/2603.08572
Evidence: `PRIMARY_PAPER`

This provides a hierarchical counter-hypothesis in which VLM-level orchestration coordinates specialized whole-body experts instead of relying on one monolithic end-to-end controller.

Future comparison axis:

```text
single unified whole-body policy
vs
predictive whole-body world/action model
vs
hierarchical expert orchestration
```

---

### 3. Multi-robot systems add shared-intention state and communication assumptions

#### Sequential World Model for multi-robot cooperation

Paper: https://arxiv.org/abs/2509.13095
ICLR 2026 paper page: https://proceedings.iclr.cc/paper_files/paper/2026/hash/16415eed5a0a121bfce79924db05d3fe-Abstract-Conference.html
Code: https://github.com/zhaozijie2022/seqwm
Evidence: `PRIMARY_PAPER` / `OPEN_SOURCE`

SeqWM models agents sequentially and shares predicted intentions across agents instead of building one monolithic joint-dynamics model.

This exposes a new decomposition:

```text
private local state
shared world state
predicted teammate intention
communication channel
communication delay / loss
```

Multi-agent success therefore does not only test world representation; it also tests what state is communicated, when it becomes stale and whether other agents' intentions are modeled correctly.

Do not infer that multi-robot intent is visually identifiable. The evaluated systems use explicit coordination information and robot state beyond passive RGB.

Future Clover question:

> If multiple robots share one persistent world model, what evidence is local, what belief is shared, and how are contradictions/provenance resolved across agents?

---

### 4. Action competence can come from non-visual priors

#### LA4VLA — language-action pretraining without vision

Paper: https://arxiv.org/abs/2606.27295
Evidence: `PRIMARY_PAPER`

LA4VLA deliberately learns language-conditioned action priors without visual observations before visual robot fine-tuning.

This is a useful attribution counterexample:

```text
robot succeeds from RGB at deployment
≠
robot learned the relevant behavior from visual evidence
```

Action competence can be injected through:

```text
language-action pretraining
robot demonstrations
human priors
simulator state
teacher policy / distillation
```

Therefore Stage-2 reports must preserve the learning-provenance labels `L0–L4` and must not use deployment modality alone to infer where knowledge originated.

---

### 5. New comparison axes

Add as cross-boundary axes, not lifecycle stages:

```text
B-ADV    natural OOD vs adversarial visual evidence / prompt injection
B-BELIEF clean current frame vs persistent poisoned state
B-WHOLE  external object state vs whole-body balance/contact state
B-MULTI  private belief vs shared belief vs teammate-intention model
B-COMM   local inference vs communication-dependent coordination
B-ATTR   deployment input modality vs training-origin of competence
```

---

### 6. Does this reveal a missing foundational domain?

No new top-level Stage-1 surface is required.

These findings land in existing surfaces:

```text
Observation Physics / visual evidence integrity
Open-World Epistemics / uncertainty / belief revision
State Variables / self-body schema
Adaptive Abstraction / embodiment
Training / Post-Training provenance
Engineering / runtime safety
Social / multi-agent hidden state
Frontier
```

But they tighten future evaluation requirements:

```text
clean success
adversarial success
whole-body stability
communication robustness
provenance-correct attribution
persistent-state recovery after corruption
```

should be reported separately when relevant.

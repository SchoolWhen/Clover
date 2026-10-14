# Stage 1 — Foundation-Model Architecture, Training and Runtime Systems

Last updated: **2026-10-15**  
Freshness cutoff checked through: **2026-10-15**

> **Research question:** How can a machine understand the real world through vision alone?

This is a Stage-1 research document. It does **not** choose a Clover architecture, vendor, foundation model, accelerator or training stack.

Its purpose is to cover a gap that became visible after reviewing DeepSeek and Qwen: modern frontier models are no longer separable into “architecture” and “systems” cleanly. Capability, context length, multimodal representation, data mixture, post-training, cache design, kernels, communication, serving runtime and agent harness increasingly co-determine what the model can do in practice.

For Clover, these are constraints and competing research hypotheses, not answers.

---

## 1. Why this surface is necessary

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

## 2. Foundation-model architecture axes to track

### F1 — Dense vs sparse / Mixture-of-Experts

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

### F2 — Attention / sequence-state architecture

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

### F3 — Residual / information-flow architecture

Track mechanisms such as:

```text
standard residual
hyper-connections
manifold-constrained mixing
gating
normalization choices
```

These are training/stability mechanisms unless evidence shows a direct world-representation effect.

### F4 — Multimodal fusion topology

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

### F5 — Visual / video tokenization

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

### F6 — Long context

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

### F7 — Adaptive / test-time compute

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

## 3. Training-data and curriculum axes

### D1 — Pretraining provenance

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

### D2 — Data mixture and alignment

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

### D3 — Curriculum

Track:

```text
general → specialist
short → long horizon
static image → video → interaction
single embodiment → cross embodiment
clean → randomized / OOD
passive → active / interventional
```

### D4 — Synthetic-data loops

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

### D5 — Post-training

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

## 4. Runtime / systems axes

### S1 — Precision

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

### S2 — KV / cache hierarchy

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

### S3 — Parallelism

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

### S4 — Kernel / compiler co-design

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

### S5 — Storage / I/O

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

### S6 — Speculative / multi-token generation

Track acceptance rate, draft cost, verification cost and quality changes.

Robotics may benefit only if speculative generation reduces end-to-end control latency rather than benchmark decode latency alone.

---

## 5. Agent harness and tool-runtime effects

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

## 6. Backbone reuse vs training from scratch

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

## 7. Proxy-model and scaling validity

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

## 8. Streaming perception as a first-class workload

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

## 9. Current DeepSeek lessons

Detailed current-source watch: [`foundation_models/DEEPSEEK_QWEN.md`](foundation_models/DEEPSEEK_QWEN.md).

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

## 10. Current Qwen lessons

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

## 11. Mac mini M4 implications

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

## 12. New reporting fields for Stage 1 / Stage 2

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

## 13. Stage-1 gaps exposed by this review

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

## Current rule

Do not choose DeepSeek or Qwen as Clover's architecture by default.

Do use them as unusually informative current examples of **model × data × runtime × hardware × harness co-design**.

The target is to understand which of those design choices matter for a vision-grounded robotic world model, which are generic LLM systems optimizations, and which can be tested at tractable scale before Clover enters Innovation.
# DeepSeek / Qwen Foundation-Model Systems Watch

Last updated: **2026-10-15**  
Freshness cutoff checked through: **2026-10-15**

> Supporting material for [`../RESEARCH_FOUNDATION_MODEL_SYSTEMS.md`](../RESEARCH_FOUNDATION_MODEL_SYSTEMS.md).

This file tracks DeepSeek and Qwen because they currently expose unusually rich information about model architecture, multimodal design, agent training, inference kernels, runtime systems and embodied extensions.

They are **comparators and engineering references**, not default Clover components.

---

# 1. DeepSeek — current map

## DeepSeek-V4.1-Flash

Official release: https://www.deepseek.com/en/news/deepseek-v4-1-flash/  
Technical report / weights: https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash  
Paper: https://arxiv.org/abs/2609.19969  
Evidence: `PRIMARY_PAPER` / `OFFICIAL_PROJECT` / `OPEN_SOURCE`

Current reported architecture:

```text
552B backbone parameters
8B active per token during prefill
16B active per token during decode
1M-token context
native image + text input
text autoregressive output
```

### Causal Encoder-Decoder

The 40-layer model is organized as a 20-layer causal encoder followed by a 20-layer decoder.

The design explicitly targets input-heavy agent workloads:

```text
prefill compute
≠ decode compute
```

This is relevant to robotic perception because continuous visual input can make repeated prefill/state-update cost dominant.

### Compressed Sparse Attention 2

The report describes Full / Reindex / Reuse attention-layer modes, hierarchical sparse indexing, cross-layer reuse and FP4 main-KV caching.

Reported global KV footprint:

```text
~890 bytes / token
≈ 1/4 DeepSeek-V4-Flash
```

Persistent KV footprint is reported at roughly 1/8 of V4-Flash through SWA Bounded Replay.

Stage-1 question:

> If long visual history becomes dramatically cheaper, does explicit grounded memory still outperform context-only approaches under equal bytes and latency?

### MoE

The current released description states:

```text
1 shared expert
384 routed experts / layer
6 routed experts active / token
```

Track total weight storage and expert-parallel communication separately from active FLOPs.

### Multimodal path

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

### Data

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

### Conditional memory / speculative decoding

Current released architecture also exposes:

- Engram conditional sparse memory;
- DSpark speculative decoding;
- Single-Pass mHC / Mega-mHC.

These are systems/architecture comparators. Do not map them directly to Clover persistent world memory without evidence.

---

## DeepSeek-V4

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

## DeepSeek infrastructure stack

### FlashMLA

https://github.com/deepseek-ai/FlashMLA

Current role:

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

### DeepSelect

https://github.com/deepseek-ai/DeepSelect

High-performance Top-K kernels for DeepSeek Sparse Attention and sampling.

Official repo reports approximately 2–20× speedup over vanilla `torch.topk` for supported workloads and includes CUDA + Ascend paths.

Research lesson:

> A sparse-attention architecture may depend on a custom selection kernel to realize its theoretical benefit.

### DeepGEMM

https://github.com/deepseek-ai/DeepGEMM

Unified high-performance kernels covering FP8/FP4/BF16 GEMM, MoE-related paths, HyperConnection and other primitives.

### DeepEP

https://github.com/deepseek-ai/DeepEP

Expert-parallel communication library with high-throughput and low-latency dispatch/combine, FP8 dispatch, NVLink/RDMA and additional distributed primitives.

Research lesson:

```text
MoE active FLOPs ↓
can still mean
network / dispatch complexity ↑
```

### TileKernels

https://github.com/deepseek-ai/TileKernels

Current features include MoE routing, quantization, Engram and mHC kernels, with NVIDIA and Ascend backends.

### DeepSpec / DSpark

https://github.com/deepseek-ai/DeepSpec

Full-stack speculative-decoding research code, including training and evaluation of draft models.

### 3FS

https://github.com/deepseek-ai/3FS

Distributed filesystem designed for AI training/inference I/O workloads.

This is relevant if future Clover research moves from local experiments to large-scale video/trajectory training.

---

## DeepSeek Harness

https://github.com/deepseek-ai/deepseek-harness

DeepSeek's open agent harness uses an “everything is a plugin” architecture and is currently developer preview.

Stage-1 lesson:

```text
DeepSeek model benchmark
≠ DeepSeek model + dsh + tools + plugins benchmark
```

When reproducing agentic claims, capture harness/version/tool configuration.

---

## Janus-series — historical but still conceptually useful

https://github.com/deepseek-ai/Janus

Janus explicitly decouples visual encoding for multimodal understanding and image generation while sharing a unified Transformer.

This is useful as a representation-design counterexample:

```text
one visual encoder for every objective
is not automatically optimal.
```

Janus-Pro is not the current DeepSeek frontier and should not be confused with V4.1.

For Mac/local research it can still be a smaller historical multimodal baseline if runtime support is practical.

---

# 2. Qwen — current map

## Qwen3.8-Max

Official release: https://qwen.ai/blog?id=qwen3.8  
Official repository: https://github.com/QwenLM/Qwen3.8  
Open model: https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B  
Evidence: `OFFICIAL_PROJECT` / `OPEN_SOURCE`

Current headline scale:

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

Qwen3.8 is especially useful for studying long-horizon agent RL, harness effects and adaptive reasoning effort, not as a local M4 baseline.

---

## Qwen3.8-Omni-Flash / Realtime

Official release: https://qwen.ai/blog?id=qwen3.8-omni-flash

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

## Qwen3.5 — native multimodal foundation

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

### Early vision-language fusion

Qwen3.5 is described as natively multimodal with early text-vision fusion and large multimodal pretraining.

Stage-1 question:

> Does early fusion improve physical/spatial state retention, or primarily improve semantic alignment and agent usability?

### Small open models

The Qwen3.5 family includes smaller models such as 0.8B / 2B / 4B / 9B class releases, making it especially useful for local proxy experiments.

These are stronger practical candidates for Mac M4 architecture experiments than frontier Max models.

---

## Qwen3-Next — efficiency foundation

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

## Qwen3-VL

Technical report: https://arxiv.org/abs/2511.21631  
Code: https://github.com/QwenLM/Qwen3-VL

Current family includes:

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

## Qwen visual tokenization lineage

Earlier Qwen2-VL introduced native dynamic resolution and M-ROPE; Qwen3-VL extends temporal/spatial treatment.

Research question:

```text
more visual tokens
→ more evidence
but also
→ more prefill cost / memory / latency
```

For Clover, compare physical-state retention under a fixed **byte / latency budget**, not only maximum-resolution accuracy.

---

## FlashQLA

https://github.com/QwenLM/FlashQLA

High-performance Gated-Delta/linear-attention kernels built on TileLang.

Current project reports:

```text
~2–3× forward speedup
~2× backward speedup
```

versus the referenced FLA Triton kernel across supported Hopper/Blackwell scenarios, with context-parallel support added in 2026.

Research lesson:

Hybrid attention efficiency depends on real kernel support; theoretical sequence complexity is not enough.

---

## Qwen-MM-Plugins

https://github.com/QwenLM/Qwen-MM-Plugins

Current capabilities include native image/video/file inspection, long-video memory, 3D spatial reasoning, physical-hardware operation plugins and demonstration-video → reusable-skill workflows.

This is important because it externalizes significant capabilities from the base model.

Keep explicit:

```text
Qwen model
≠ Qwen model + MM Plugins
```

---

## Qwen-Live-Harness

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

# 3. Qwen Physical-AI suite

## Qwen-RobotWorld

Paper: https://arxiv.org/abs/2606.17030  
Official: https://qwen.ai/blog?email_hash=23463b99b62a72f26ed677cc556c44e8&id=qwen-robotworld

Current reported design:

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

Critical Clover distinction:

```text
language action abstraction useful for scaling
≠ language is a physically sufficient action representation.
```

---

## Qwen-RobotManip

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

This is a particularly important Stage-1 data-engine lesson:

```text
scaling heterogeneous robot data
requires semantic / coordinate / motion alignment.
```

The official repository currently states there is no plan to release RobotManip/RobotNav model weights, so reproducibility is limited relative to open-weight baselines.

---

## Qwen-VLA

Official: https://qwen.ai/blog?id=qwenvla  
Paper id: https://arxiv.org/abs/2605.30280

Qwen-VLA combines robot, egocentric, synthetic simulation and general vision-language data across manipulation/navigation/cross-embodiment control.

Research role: broad direct-policy counter-hypothesis to persistent explicit world-state approaches.

---

## Qwen-Drive 1.0

Official: https://qwen.ai/blog?id=qwen-drive-1.0

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
frozen VLM
+
explicit inspectable 3D probe
+
planning head
```

is a distinct design family Clover should compare.

---

## Qwen-AgentWorld — adjacent digital-world reference

Official: https://qwen.ai/blog?id=qwen-agentworld

A language world model trained natively to simulate agent environments across seven digital domains, with paired ground-truth observations from real environments.

It is not a physical-world/vision-only result, but it is useful for studying world-model training objectives, environment simulation and evaluator design.

---

# 4. DeepSeek vs Qwen — high-value contrasts

| Axis | DeepSeek current signal | Qwen current signal | Clover question |
|---|---|---|---|
| Long context | compressed/sparse KV-centric design | hybrid linear/full attention + 1M hosted contexts | context vs explicit memory under equal budget |
| MoE | very large sparse MoE + heavy expert-parallel systems | ultra-sparse MoE across multiple scales | active compute vs communication/storage |
| Vision | DeepSeek-ViT + projector; joint multimodal pretraining | native multimodal/early fusion; Qwen3-VL DeepStack | which fusion preserves physical evidence? |
| Streaming | input-heavy CED optimization | Omni Realtime + harness | incremental robot perception architecture |
| Kernels | FlashMLA / DeepSelect / DeepGEMM / DeepEP | FlashQLA | hardware co-design and portability |
| Agent runtime | DeepSeek Harness | Qwen-MM-Plugins / Live Harness | model vs harness capability |
| Physical AI | currently more general multimodal/agent focus | RobotWorld / RobotManip / VLA / Drive | backbone reuse vs embodied specialization |
| Data | 45T multimodal + synthetic agent task pipeline | multimodal scaling + large cross-embodiment robot synthesis | data alignment vs architecture |
| Small local models | fewer current frontier analogues | strong 2B–9B multimodal family | Mac M4 proxy research |

---

# 5. What Clover should add to Stage-2 method reports

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

# 6. Priority experiments suggested by this watch

Stage 1 should collect enough evidence to later support controlled experiments such as:

### E-FM1 — visual token budget

```text
same model
same video
vary image resolution / token count / frame rate
→ physical / spatial / permanence diagnostics
```

### E-FM2 — context vs memory under equal bytes

```text
long raw context
vs
compact persistent state + evidence retrieval
```

Match total memory footprint and latency.

### E-FM3 — precision vs epistemics

```text
BF16
FP8
INT8 / INT4
```

Compare calibration, unknown-state behavior and long-horizon state consistency, not only task accuracy.

### E-FM4 — harness ablation

```text
base model
+ tools
+ memory
+ visual plugins
+ retries
```

Measure incremental contribution of each layer.

### E-FM5 — frozen backbone vs adaptation

Use tractable Qwen small models to compare:

```text
frozen VLM + new state head
adapter / LoRA
partial backbone tuning
full tuning where feasible
```

### E-FM6 — streaming fast/slow loop

Compare:

```text
fast local state updater
+
slower reasoner/planner
```

against synchronous monolithic inference under identical deadlines.

---

# Current conclusion

DeepSeek and Qwen expose a major Stage-1 lesson:

> **Modern model capability is increasingly produced by a coupled stack of representation, data, sparse compute, memory/cache, kernels, distributed systems, post-training and agent runtime.**

For Clover, the correct response is not to imitate either stack wholesale.

The research task is to identify which pieces are generic foundation-model engineering, which pieces materially change visual world-state quality, and which can be tested with small reproducible models before large-scale Innovation.
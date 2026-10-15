# Foundation-Model Systems — Supporting Stage-1 Index

This directory supports [`../RESEARCH_FOUNDATION_MODEL_SYSTEMS.md`](../RESEARCH_FOUNDATION_MODEL_SYSTEMS.md) and the cross-cutting training surface [`../RESEARCH_TRAINING_POSTTRAINING.md`](../RESEARCH_TRAINING_POSTTRAINING.md).

It is **not** a vendor-selection layer and does not make DeepSeek, Qwen, or any other model family a Clover dependency.

## Current watches / matrices

- [`DEEPSEEK_QWEN.md`](DEEPSEEK_QWEN.md) — DeepSeek/Qwen architecture, multimodal, data, inference-kernel, harness and Physical-AI watch.
- [`DEEPSEEK_QWEN_CURRENT_2026-10-15.md`](DEEPSEEK_QWEN_CURRENT_2026-10-15.md) — current official-state snapshot, including API/hosted/open-artifact distinctions and later changelog corrections.
- [`CROSS_BOUNDARIES.md`](CROSS_BOUNDARIES.md) — P0/P1/P2 cross-boundary matrix: visual tokenizer/video sampling, streaming foundation models, long context vs world memory, backbone adaptation, data science, quantization, proxy→frontier scaling, harness attribution, distributed systems and optimizer/runtime boundaries.
- [`../RESEARCH_TRAINING_POSTTRAINING.md`](../RESEARCH_TRAINING_POSTTRAINING.md) — pretraining, SFT/behavior cloning, co-training, distillation, RL, simulated post-training, deployment learning and continual adaptation across LLM/VLM/VLA/world-model systems.
- [`../training/README.md`](../training/README.md) — controlled training-variable matrix covering data diversity/quality, alignment, action representation, horizon, update scope, reward/teacher, failure data, simulator trust and checkpoint selection.
- [`../training/HIGH_RISK_BOUNDARIES.md`](../training/HIGH_RISK_BOUNDARIES.md) — partial-success rewards, epistemic reward, failure/recovery ratios, world-model trust, module adaptation timescales, uncertainty regression, distillation loss, scale transfer, fleet contamination and stateful rollback.
- [`../emerging/JEPA_RSI_RUNTIME_2026-10-15.md`](../emerging/JEPA_RSI_RUNTIME_2026-10-15.md) — current cross-boundary audit of embodied JEPA, latent-action world models, test-time VLA verification, WAM inference-state acceleration, recursive self-improvement, embodied RSI, and generative-video perception.
- [`../STAGE1_FINAL_AUDIT_2026-10-15.md`](../STAGE1_FINAL_AUDIT_2026-10-15.md) — Stage-1 coverage audit and cross-boundary priorities through 2026-10-15.

## Why it exists

Modern frontier capability is increasingly produced by a coupled stack:

```text
representation
+
visual / multimodal tokenization
+
data mixture / alignment
+
pretraining / post-training
+
attention / MoE
+
context / cache
+
kernels / compiler / distributed runtime
+
agent harness / tools / memory
```

For Clover, these factors must be separated experimentally rather than attributed to “the model” as one opaque object.

Training must also be decomposed:

```text
architecture
× data
× objective
× update scope
× on/off-policy interaction
× teacher/reward source
→ observed capability
```

Self-improving systems require another decomposition:

```text
model-weight change
≠ harness change
≠ data/curriculum change
≠ memory/skill artifact change
≠ embodied deployment adaptation
```

For RSI claims, also preserve the immutable evaluator, held-out split, resource budget, accepted-change lineage and rollback mechanism.

## Current rule

For every vendor/model/system result, preserve the exact artifact and distinguish:

```text
base model
hosted product
open-weight checkpoint
training / post-training recipe
runtime/kernel stack
agent harness
external tools / memory
test-time verifier / search budget
```

A benchmark result from one configuration does not automatically transfer to the others.
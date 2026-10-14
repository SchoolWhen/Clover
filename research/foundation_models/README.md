# Foundation-Model Systems — Supporting Stage-1 Index

This directory supports [`../RESEARCH_FOUNDATION_MODEL_SYSTEMS.md`](../RESEARCH_FOUNDATION_MODEL_SYSTEMS.md) and the cross-cutting training surface [`../RESEARCH_TRAINING_POSTTRAINING.md`](../RESEARCH_TRAINING_POSTTRAINING.md).

It is **not** a vendor-selection layer and does not make DeepSeek, Qwen, or any other model family a Clover dependency.

## Current watch

- [`DEEPSEEK_QWEN.md`](DEEPSEEK_QWEN.md) — current DeepSeek/Qwen architecture, multimodal, data, inference-kernel, harness and Physical-AI signals checked through 2026-10-15.
- [`../RESEARCH_TRAINING_POSTTRAINING.md`](../RESEARCH_TRAINING_POSTTRAINING.md) — pretraining, SFT/behavior cloning, co-training, distillation, RL, simulated post-training, deployment learning and continual adaptation across LLM/VLM/VLA/world-model systems.

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

## Current rule

For every vendor/model result, preserve the exact artifact and distinguish:

```text
base model
hosted product
open-weight checkpoint
training / post-training recipe
runtime/kernel stack
agent harness
external tools / memory
```

A benchmark result from one of these configurations does not automatically transfer to the others.
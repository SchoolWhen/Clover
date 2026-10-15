# DeepSeek / Qwen — Verified Current Snapshot

Last checked: **2026-10-15**

This file is a freshness snapshot supporting [`DEEPSEEK_QWEN.md`](DEEPSEEK_QWEN.md).

It exists because vendor release plans, API routing and hosted/open artifacts can change after launch.

Use this rule:

```text
latest official changelog/status
supersedes
older launch-plan wording
```

Do not silently treat a hosted API product and an open-weight checkpoint as the same artifact.

---

# 1. DeepSeek — current verified state

## DeepSeek-V4.1-Flash

Official launch: https://www.deepseek.com/en/news/deepseek-v4-1-flash/
API changelog: https://api-docs.deepseek.com/updates/
Official news index: https://www.deepseek.com/en/news/

Current official headline architecture:

```text
552B MoE
8B active for input/prefill
16B active for output/decode
native visual understanding
1M context family direction
```

The release emphasizes:

```text
Causal Encoder–Decoder asymmetry
large KV-cache reduction
new pretraining methods
larger-scale RL post-training
```

Research relevance for Clover:

```text
continuous vision is input-heavy
therefore prefill/state-update cost can dominate
```

This is a systems reference, not evidence for a sufficient physical world representation.

### API-status correction

The Sept-10 launch post said DeepSeek planned to route `deepseek-v4-pro` requests to V4.1-Flash after Sept 14 while phasing out V4 Pro.

The later DeepSeek API changelog states that, in response to user demand, **V4 Pro API service would continue after Sept 14 with unchanged billing**.

Therefore the current record must not repeat the original routing plan as present fact.

This is a useful general lesson:

```text
launch announcement
≠ immutable deployment state
```

Capture the date/source of every API-routing claim.

---

## DeepSeek model + harness distinction

DeepSeek agent benchmark results can depend on DeepSeek Harness configuration and reasoning effort.

Current resources:

- DeepSeek Harness — https://github.com/deepseek-ai/deepseek-harness
- FlashMLA — https://github.com/deepseek-ai/FlashMLA
- DeepSelect — https://github.com/deepseek-ai/DeepSelect
- DeepGEMM — https://github.com/deepseek-ai/DeepGEMM
- DeepEP — https://github.com/deepseek-ai/DeepEP
- 3FS — https://github.com/deepseek-ai/3FS

Required attribution:

```text
exact model
+
exact effort mode
+
exact harness
+
exact tools/plugins
+
runtime/kernel version
+
hardware
```

---

# 2. Qwen — current verified state

## Qwen3.8-Max

Official: https://qwen.ai/blog?id=qwen3.8

Current official headline:

```text
2.4T total parameters
95B active
long-horizon / coding / work / research focus
reasoning_effort control in hosted API
```

Qwen's official post states that Max-class open weights were planned/released around the launch period; exact hosted/open artifact equivalence must still be verified before benchmark comparison.

Research relevance:

```text
reasoning effort is a runtime variable
```

A benchmark score obtained with `xhigh` reasoning should not be compared to a low-effort local checkpoint as if only architecture differed.

---

## Qwen3.8-Omni-Flash

Official: https://qwen.ai/blog?id=qwen3.8-omni-flash

Released 2026-09-18.

Officially described as:

```text
text + image + audio + video input
1M context
agent/tool workflows
Realtime API
```

For Clover it is a **streaming-systems comparator**, not a strict vision-only result because audio input lies outside V0–V3.

---

## Qwen3.5

Official: https://qwen.ai/blog?id=qwen3.5

Current high-value architecture signal:

```text
native vision-language
hybrid linear + full attention
sparse MoE
397B total / 17B active flagship
small open models also available
```

Research relevance:

- linear/recurrent-style sequence mechanisms vs full attention;
- local proxy experiments on small checkpoints;
- long-context vs explicit-memory comparison;
- multimodal adaptation without training from scratch.

---

## Qwen3-VL

Technical report: https://arxiv.org/abs/2511.21631
Code: https://github.com/QwenLM/Qwen3-VL

Useful for tractable local/remote experiments because the family spans smaller dense checkpoints and larger MoE checkpoints.

Important historical visual-tokenization lineage from Qwen2.5-VL:

- dynamic visual resolution;
- dynamic FPS training;
- absolute-time treatment for video.

Official Qwen2.5-VL description: https://qwen.ai/blog?from=research.research-list&id=c5e7415d9a9e89adc18c59d9e466e5a1a459b8f4

This is directly relevant to Clover's fast-dynamics / frame-sampling studies.

---

# 3. Qwen Physical-AI training signals

## Qwen-VLA

Official: https://qwen.ai/blog?id=qwenvla
Paper: https://arxiv.org/abs/2605.30280

Official staged training:

```text
Stage I   text-to-action pretraining, VLM frozen
Stage II  continual multimodal pretraining, VLM + action decoder updated
Stage III SFT for multitask / real-robot specialization
Stage IV  PPO RL in simulation
```

Research lesson:

```text
final policy behavior
cannot be attributed to backbone architecture alone
```

Each stage changes the learning signal and updated parameter subset.

---

## Qwen-RobotManip

Official: https://qwen.ai/blog?id=qwen-robotmanip
Paper: https://arxiv.org/abs/2606.17846

Current reported design:

```text
Qwen3.5-4B VLM
+
flow-matching DiT action head
```

Training/data highlights:

```text
~38.1K h total corpus
~11.4K h robot data
~1.9K h egocentric human video
~24.8K h synthesized human→robot data
15 embodiments
pretraining VLA:VLM stream ≈ 9:1
post-training uses demonstration SFT
VL+VLA co-training is retained during post-training
```

Official data curation includes multiple state/action filtering and cross-modal consistency checks.

Central lesson:

```text
heterogeneous data scale
requires
representation + motion + behavior alignment
```

Do not copy the mixture ratios as universal constants. They are one training design, not a scaling law.

---

## Qwen-RobotWorld

Official: https://qwen.ai/blog?email_hash=23463b99b62a72f26ed677cc556c44e8&id=qwen-robotworld
Paper: https://arxiv.org/abs/2606.17030

Official curriculum is general→expert and combines:

```text
general image/video priors
human-interaction video
single-view embodied SFT
multi-view expansion
cross-view consistency
complex cross-domain / long-horizon data
```

Research lesson:

> Curriculum order and data mixture are part of the method, not implementation trivia.

---

## Qwen-Drive 1.0

Official: https://qwen.ai/blog?id=qwen-drive-1.0
Paper: https://arxiv.org/abs/2609.00111

Important design family:

```text
pretrained Qwen3.5-4B architecture retained
+
explicit BEV perception head
+
3D object / occupancy / map outputs
+
flow-matching planning expert
```

This is a strong counterexample to the assumption that all useful state must remain implicit inside one monolithic VLM latent.

---

# 4. DeepSeek vs Qwen — current research role for Clover

| Question | DeepSeek signal | Qwen signal |
|---|---|---|
| input-heavy compute | Causal Encoder–Decoder asymmetry | Omni realtime / visual-stream systems |
| long context | aggressive KV compression | hybrid linear/full attention + large hosted contexts |
| sparse compute | large MoE + expert systems | sparse MoE across multiple scales |
| visual tokenization | native visual front end / downsampling | dynamic resolution/FPS, Qwen3-VL |
| post-training | SFT/RL/on-policy distillation + synthetic agent environments | multi-stage reasoning and robot curricula |
| physical AI | mainly general multimodal/agent systems | RobotManip/RobotWorld/VLA/Drive suite |
| local M4 proxies | limited frontier analogy | strong small Qwen multimodal checkpoints |
| harness attribution | DeepSeek Harness | MM-Plugins / Live-Harness / hosted tools |

---

# 5. Artifact-provenance rule

For every DeepSeek/Qwen claim preserve:

```text
exact date
exact model identifier
hosted vs open checkpoint
modalities of the exact artifact
reasoning-effort / thinking mode
harness/tools
runtime/kernel
quantization/cache format
API routing status
```

Do not carry forward a vendor claim from an older release page after the vendor's newer changelog/status contradicts it.

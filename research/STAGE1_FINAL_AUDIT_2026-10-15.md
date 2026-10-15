# Stage 1 Final Audit — 2026-10-15

> Research question: **How can a machine understand the real world through vision alone?**

This audit checks whether Stage 1 still has missing *major domains* after expanding from visual world modeling into identifiability, memory, causality, model discovery, foundation-model systems, training/post-training, deployment and validation.

## Audit conclusion

**No obvious major research domain is currently missing.**

The remaining work is dominated by **cross-boundary controlled-variable problems** rather than new top-level categories.

The important implication is:

```text
Stage 1 should remain open to freshness updates,
but Stage 2 can become the primary mode once these boundaries are recorded.
```

Do not interpret this as “research is complete forever.” It means the broad problem map is sufficiently complete that continued collection should be selective and evidence-driven.

---

# 1. Cross-boundary priorities

## P0 — must be understood before serious architecture selection

### P0.1 Visual tokenizer / video sampling

The effective observation path is:

```text
world
→ optics / camera
→ RGB
→ resize / crop / ISP
→ frame sampling
→ visual tokenizer / patching / pixel-unshuffle / pooling
→ token pruning / merging
→ backbone
→ internal state
```

The tokenizer is therefore part of the sensing pipeline, not merely an implementation detail.

Current evidence to track:

- Qwen2.5-VL dynamic FPS + absolute-time encoding: https://qwen.ai/blog?from=research.research-list&id=c5e7415d9a9e89adc18c59d9e466e5a1a459b8f4
- Qwen3-VL: https://github.com/QwenLM/Qwen3-VL
- SAPrune / stage-aware VLA token pruning: https://arxiv.org/abs/2610.05273
- VLA-ACL / action-consistent token pruning: https://arxiv.org/abs/2610.08133
- adaptive two-stage video token pruning: https://arxiv.org/abs/2608.03112

Required future experiment:

```text
same raw video
same checkpoint
vary resolution / FPS / token count / pruning policy
```

Measure geometry, fast contact, permanence, uncertainty, OOD behavior, action stability, latency and memory.

A model must not be blamed for missing evidence that the tokenizer already discarded.

---

### P0.2 Streaming foundation models

A robot receives an unbounded stream; it should not be modeled as repeated independent chat prompts.

Study:

```text
incremental visual encoding
frame reuse
cache invalidation
bounded history
periodic global refresh
fast local state update
slow semantic/planning update
stream interruption / resume
```

DeepSeek-V4.1-Flash is relevant because its Causal Encoder–Decoder explicitly separates input-heavy and output-heavy compute: https://www.deepseek.com/en/news/deepseek-v4-1-flash/

Qwen3.8-Omni-Flash and Qwen-Live-Harness are useful runtime comparators for continuous multimodal streams, although audio is outside strict Clover V0–V3 sensing: https://qwen.ai/blog?id=qwen3.8-omni-flash · https://github.com/QwenLM/Qwen-Live-Harness

Required metrics:

```text
incremental latency
full-refresh latency
state staleness
frame backlog
dropped/reordered frame robustness
cache growth
memory leak
p95/p99 camera→action deadline
```

---

### P0.3 Long context vs grounded world memory

Long context is a computational resource. It is not automatically:

```text
persistent world belief
belief revision
evidence provenance
identity memory
```

Current multimodal memory evidence:

- M3Exam shows persistent gaps and efficiency costs in multimodal long-context memory, while query-conditioned memory can reduce retrieved tokens: https://arxiv.org/abs/2606.07402
- ICM-Bench isolates long-term identity memory rather than generic event recall: https://arxiv.org/abs/2609.04438

Required equal-budget comparison:

```text
A raw long context
B persistent state
C evidence retrieval
D hybrid state + evidence + bounded recent context
```

Match bytes, peak memory and latency as far as possible.

---

### P0.4 Backbone adaptation

Compare under matched data/compute:

```text
frozen backbone + state/action head
LoRA / adapter
selective visual-language adaptation
partial fine-tuning
full fine-tuning
teacher→student distillation
```

Current controlled evidence:

- π0 LoRA vs full fine-tuning study: https://arxiv.org/abs/2607.10172
  - some LoRA settings match full tuning on the evaluated industrial tasks;
  - over-freezing the VLM/vision path can hurt embodiment adaptation.
- Qwen-Drive demonstrates another design family: keep the pretrained Qwen3.5-4B VLM architecture and add explicit BEV/perception/planning modules: https://qwen.ai/blog?id=qwen-drive-1.0

Future selection must jointly consider adaptation quality, catastrophic forgetting, calibration, memory, OOD vision and deployment cost.

---

# 2. P1 research variables

## P1.1 Data science / data alignment

Do not summarize robot data by `hours` alone.

Record:

```text
unique scenes
objects
tasks
embodiments
operators
camera setups
success/failure/recovery distribution
real/human/sim/generated fractions
alignment method
retargeting error
temporal synchronization
deduplication / leakage
curriculum / sampling ratio
```

High-value current evidence:

- Qwen-RobotManip uses ~38.1K hours across robot, egocentric human and synthesized human→robot data, but emphasizes representation/motion/behavior alignment before scale: https://qwen.ai/blog?id=qwen-robotmanip
- Rethinking VLA Scaling finds naive heterogeneous robot pooling can cause negative transfer: https://arxiv.org/abs/2602.09722

Open question:

> Does the best robot/human/sim/generated mixture change with model scale and representation capacity?

No universal mixture is currently justified.

---

## P1.2 Quantization as a capability intervention

Low-bit inference should not be evaluated only by average task success.

Current evidence:

- FoldQuantVLA: https://arxiv.org/abs/2609.24433
- LiteVLA-Edge: https://arxiv.org/abs/2603.03380

Required measurements:

```text
nominal success
OOD success
uncertainty calibration
unknown/refusal
rare-event sensitivity
object identity/permanence
belief revision
long-horizon drift
action smoothness/contact stability
latency/memory/energy
```

Keep distinct:

```text
PTQ
QAT
quantization-aware / quantization-conditioned post-training
```

A quantized model may need additional post-training; that gain must not be attributed to quantization alone.

---

## P1.3 Small→large scaling validity

Mac-M4 experiments will often use 2B/4B/8B proxies.

Required protocol:

```text
small-model discovery
→ medium replication
→ large/frontier counter-check
```

Track whether the effect changes with:

```text
parameter count
active parameters
MoE routing
context length
visual-token budget
data mixture
precision
runtime backend
```

A 4B result is not a 30B/MoE result by default.

---

## P1.4 Harness attribution

Modern benchmarks can measure a full system rather than the base model.

Ablate:

```text
base model
+ prompt/protocol
+ external memory
+ visual/perception helper
+ tools/MCP
+ retry/recovery
+ full harness
```

Track token cost, latency and memory together with capability.

DeepSeek and Qwen make this particularly important because both expose explicit harness/runtime layers.

---

# 3. P2 — understand but do not let systems detail dominate science

Track enough of the following to reproduce feasibility claims:

```text
data/tensor/pipeline/expert/context parallelism
network topology
all-to-all / expert communication
storage bandwidth
checkpoint/optimizer size
custom kernels
Muon/AdamW variants
mHC/hyper-connections
speculative decoding
multi-token prediction
```

DeepSeek references:

- DeepEP — https://github.com/deepseek-ai/DeepEP
- DeepGEMM — https://github.com/deepseek-ai/DeepGEMM
- DeepSelect — https://github.com/deepseek-ai/DeepSelect
- 3FS — https://github.com/deepseek-ai/3FS

These affect feasibility and scaling. They are not evidence that a world-state representation is scientifically superior.

---

# 4. Training/post-training high-risk boundaries

The detailed matrix is in [`training/HIGH_RISK_BOUNDARIES.md`](training/HIGH_RISK_BOUNDARIES.md).

Stage 1 now explicitly requires research on:

```text
partial-success reward
reward for epistemic correctness
failure/recovery sampling ratio
recovery-vs-nominal interference
world-model trust controlling imagined rollout
human/sim/robot mixture × model scale
frozen vs LoRA vs partial vs full tuning
module-specific learning rates/update frequencies
slow semantic vs fast motor adaptation
post-training calibration degradation
world-capability regression despite task success
capability loss under distillation
4B→MoE recipe transfer
fleet contamination / update admission
model rollback ↔ persistent-memory compatibility
```

Important current reward evidence:

- RoboReward constructs calibrated negatives, near-misses and partial-progress outcomes for robotics reward modeling: https://arxiv.org/abs/2601.00675
- SARM2 uses stage-aware dense reward for long-horizon robot policy improvement: https://arxiv.org/abs/2606.10305
- TOPReward extracts temporal task-progress signals from VLM token probabilities: https://arxiv.org/abs/2602.19313
- MERL uses simulator trust to control imagined-data ratio and rollout horizon: https://arxiv.org/abs/2610.16517

No universal failure-data percentage, recovery ratio, real/human/sim mixture or tuning method is currently justified.

---

# 5. Training curriculum itself is part of the scientific comparison

Current Qwen robot systems make this especially visible.

## Qwen-VLA

Official description uses four stages:

```text
T2A pretraining
→ continual pretraining
→ SFT
→ PPO RL in simulation
```

Source: https://qwen.ai/blog?id=qwenvla

This means final behavior cannot be attributed to the backbone alone.

## Qwen-RobotManip

Official training uses:

```text
VLA/VLM dual-stream pretraining at ~9:1
→ benchmark/generalist SFT
→ continued VLA+VL co-training during post-training
```

Source: https://qwen.ai/blog?id=qwen-robotmanip

## Qwen-RobotWorld

Uses a general→expert curriculum combining general image/video priors, human-interaction data and progressive embodied SFT stages including multi-view and cross-domain training.

Source: https://qwen.ai/blog?email_hash=23463b99b62a72f26ed677cc556c44e8&id=qwen-robotworld

Central rule:

```text
architecture result
≠ training-curriculum result
```

---

# 6. Final audit additions beyond the original P0/P1/P2 list

These are not new project stages. They are cross-cutting constraints that should remain visible.

## A. Runtime safety / formal safety interface

Task success can coexist with unsafe behavior.

Track:

```text
unsafe-success
risk exposure time
constraint violations
collision/force/workspace limits
safety-layer intervention rate
recovery after intervention
```

Current sources:

- VLA safety survey: https://arxiv.org/abs/2604.23775
- AEGIS / plug-and-play CBF safety layer: https://arxiv.org/abs/2512.11891
- FEARL / verifiable modular safety: https://arxiv.org/abs/2606.23754
- ForesightSafety-VLA: https://arxiv.org/abs/2606.27079

A safety filter is not proof that the underlying world model is safe or correct; but deployment evidence without a safety analysis is incomplete.

---

## B. Statistical / reproducibility discipline for real robots

Real-robot evaluation is expensive and noisy.

Required metadata:

```text
number of trials
number of seeds/checkpoints
operator identity / blinding
initial-state randomization
hardware/calibration version
confidence intervals / variance
failure taxonomy
selection criterion
```

Rethinking VLA Scaling introduces a grouped blind ensemble protocol to reduce operator/model-identity bias during real evaluation: https://arxiv.org/abs/2602.09722

One impressive video or one lucky checkpoint is not sufficient evidence.

---

## C. Reward/verifier reliability

A learned reward can itself hallucinate progress or be exploited.

Reward-model evaluation should be independent from policy evaluation and include:

```text
false-positive success
near-miss ranking
stage ordering
OOD task transfer
reward hacking
reward uncertainty
human agreement
```

Reward-model improvement and policy improvement are distinct claims.

---

## D. Artifact drift / API routing / benchmark contamination

Preserve exact:

```text
model/checkpoint/API version
release date
API route
harness version
runtime/kernel version
benchmark snapshot
training-data cutoff/provenance if known
```

Vendor release plans can change after publication. Current-state claims should prefer the latest official changelog/status page over an older launch announcement.

Example: DeepSeek's 2026-09-10 launch post initially said V4-Pro requests would be routed to V4.1-Flash after Sept 14, while the later API changelog states V4 Pro would continue to be served. Current record must preserve the later status.

DeepSeek launch: https://www.deepseek.com/en/news/deepseek-v4-1-flash/
DeepSeek API changelog: https://api-docs.deepseek.com/updates/

---

# 7. Stage-1 readiness judgment

The broad map now covers:

```text
world / observation / identifiability
representation / state / memory / causality
active evidence / model discovery
foundation-model architecture / tokenizer / context / runtime
training / post-training / data / reward
edge deployment / simulation / sim2real / validation
runtime safety / monitoring / rollback
```

Therefore the recommended project mode is now:

```text
Stage 1 = incremental freshness + gap maintenance
Stage 2 = primary method-by-method analysis
```

Stage 1 should reopen a major category only if new evidence shows that an entire capability class is absent from the map.

Otherwise new work should be attached to an existing surface and tested as a controlled variable.

---

# 8. Highest-priority Stage-2 experiments implied by this audit

1. **Visual-token / FPS ablation** on a tractable open Qwen VLM/VLA proxy.
2. **Equal-byte long-context vs persistent-memory comparison**.
3. **Frozen vs LoRA vs partial tuning** under matched robot data.
4. **BC vs co-training vs future-latent auxiliary vs on-policy distillation**.
5. **Post-training preservation battery**: task success + permanence + memory revision + causal probes + calibration.
6. **Quantization before/after post-training** and capability regression.
7. **Failure/recovery ratio sweep** under fixed total data budget.
8. **World-model trust vs imagined rollout horizon**.
9. **Small dense proxy → larger dense/MoE replication**.
10. **Base model vs harness/memory/tools ablation**.

These experiments are downstream candidates, not Stage-1 conclusions.

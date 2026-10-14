# Foundation-Model Cross-Boundary Research Matrix

Last updated: **2026-10-15**  
Freshness cutoff checked through: **2026-10-15**

> Supporting material for [`../RESEARCH_FOUNDATION_MODEL_SYSTEMS.md`](../RESEARCH_FOUNDATION_MODEL_SYSTEMS.md) and [`../RESEARCH_TRAINING_POSTTRAINING.md`](../RESEARCH_TRAINING_POSTTRAINING.md).

This document closes the remaining cross-boundary gaps between computer vision, multimodal foundation models, embodied learning, runtime systems and edge deployment. It is **not** a Clover architecture decision.

Core rule:

```text
scientific capability
must be separated from
input compression + training recipe + runtime + harness + deployment artifact
```

---

# P0 — must understand before serious architecture selection

## P0.1 Visual tokenizer / video sampling is part of the sensor

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

## P0.2 Streaming foundation model, not repeated giant prompts

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

## P0.3 Long context vs persistent world memory

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

## P0.4 Foundation-backbone adaptation

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

# P1 — high-value research variables

## P1.1 Data science is a first-class model variable

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

## P1.2 Quantization must be evaluated as a capability intervention

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

## P1.3 Small-proxy → frontier scaling validity

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

## P1.4 Harness attribution

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

# P2 — understand now, but do not let these dominate Clover science

## P2.1 Distributed training / storage / network

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

## P2.2 Optimizer / residual / speculative-decoding details

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

# Additional cross-boundaries exposed by the final audit

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

See [`../training/HIGH_RISK_BOUNDARIES.md`](../training/HIGH_RISK_BOUNDARIES.md) for the training-specific matrix.

---

# Current conclusion

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

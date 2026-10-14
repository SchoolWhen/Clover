# Training / Post-Training — Supporting Stage-1 Matrix

Last updated: **2026-10-15**  
Freshness cutoff checked through: **2026-10-15**

> Supporting material for [`../RESEARCH_TRAINING_POSTTRAINING.md`](../RESEARCH_TRAINING_POSTTRAINING.md).

This file is **not** a Clover training recipe. It records variables that must be controlled before attributing a capability gain to architecture or representation.

High-risk cross-boundary questions live in [`HIGH_RISK_BOUNDARIES.md`](HIGH_RISK_BOUNDARIES.md), including partial-success rewards, epistemic calibration, failure/recovery ratios, simulator trust, module adaptation timescales, uncertainty regression, distillation, scaling, fleet-update contamination and model/memory rollback consistency.

---

## 1. Training variables that must be separated

| Axis | Examples | Why it matters |
|---|---|---|
| Data quantity | hours, episodes, tokens, trajectories | scale can help, but repeated homogeneous data may saturate |
| Data diversity | objects, scenes, tasks, embodiments, operators | often more important for OOD generalization than repetition |
| Data quality | expert, suboptimal, failed, noisy, mis-synchronized | equal weighting can create negative transfer |
| Data provenance | real robot, human video, sim, generated/retargeted | determines evidence strength and sim/human→robot bias |
| Alignment | coordinate frames, action space, camera semantics, temporal units | heterogeneous data can conflict without alignment |
| Curriculum | general→expert, easy→hard, short→long, sim→real | stage order changes what is retained/overwritten |
| Objective | action BC, language co-training, future latent, value/reward, world prediction | objective shapes representation and transfer |
| Update scope | frozen backbone, adapter, projector/head, partial/full model | controls specialization vs forgetting |
| Policy distribution | offline/off-policy vs self-generated/on-policy | determines whether recovery/deployment states are covered |
| Teacher/reward source | expert policy, verifier, VLM, learned reward, environment | errors/biases become learning signals |
| Action representation | discrete, regression, diffusion, flow, latent action | changes multimodality, precision and inference cost |
| Temporal abstraction | per-step action, fixed chunk, adaptive horizon, high-level subtask | affects feedback frequency and long/short-horizon trade-offs |
| Replay / failure mining | success only, failure, recovery, prioritized replay | determines whether the policy learns to recover |
| Simulator trust | imagined ratio, rollout horizon, sysid quality | model-based RL can exploit simulator/world-model error |
| Checkpoint selection | BC validation loss, offline FQE, real rollout | proxy metrics can select the wrong policy |
| Continual update | periodic batch, online, fleet aggregation | creates drift/forgetting/rollback/state-compatibility issues |

---

## 2. Data scale is not one scalar

### Data Scaling Laws in Imitation Learning for Robotic Manipulation

Paper: https://arxiv.org/abs/2410.18647

The study collects more than 40K demonstrations and reports more than 15K real-robot rollouts. Its main Stage-1 signal is that diversity in environments/objects can matter more for generalization than repeatedly collecting more demonstrations for the same environment/object once a threshold is reached.

Therefore record separately:

```text
number of trajectories
number of unique scenes
number of unique objects
task diversity
operator diversity
embodiment diversity
```

Do not use `hours` as the only robot-data scale variable.

### Qwen-RobotManip

Paper: https://arxiv.org/abs/2606.17846  
Official overview: https://qwen.ai/blog?id=qwen-robotmanip

Its central training claim is that representation, motion and behavioral alignment make heterogeneous cross-embodiment scaling coherent.

Important distinction:

```text
data scale
≠ useful scale
```

if action/state semantics conflict.

---

## 3. Objective choice changes transfer under a fixed backbone

### VLAFlow

Paper: https://arxiv.org/abs/2607.01586

Controlled comparison under a shared π0-style architecture/backbone/action space:

```text
action-only
vs language co-training
vs future-latent alignment
vs language + future-latent
```

This is a high-value Stage-2 candidate because it isolates training signal better than comparing unrelated model families.

### VLAct — continued pretraining as representation learning

Project: https://starvla.github.io/VLAct/

Use as a current signal that robot continued pretraining can be framed as preserving/learning transferable visual-action representation rather than simply fitting action labels.

Treat project-reported results conservatively until primary-paper details are analyzed.

---

## 4. Action representation and action horizon are training variables

### OpenVLA-OFT

Paper: https://arxiv.org/abs/2502.19645

Shows that action decoding scheme, action chunking, continuous action representation and fine-tuning loss can materially change both policy performance and inference speed even with the same OpenVLA base.

### Mixture of Horizons

Paper: https://arxiv.org/abs/2511.19433

Reports an action-chunk trade-off:

```text
longer horizon
→ more foresight / less frequent replanning
→ weaker local precision / feedback

shorter horizon
→ stronger local correction
→ weaker long-range continuity / more inference
```

### GeoAAC

Paper: https://arxiv.org/abs/2609.20776

Adapts action horizon using flow-denoising geometry.

### ChunkTrust

Paper: https://arxiv.org/abs/2609.39754

Treats execution horizon as a latent variable inferred from action-expert evidence.

Research implication:

> `action chunk length` and `how many predicted actions are actually executed before replanning` must be recorded separately.

---

## 5. Data quality / weighting can matter more in post-training than pretraining

### Posterior-Transition Reweighting

Paper: https://arxiv.org/abs/2603.16542

Uses observed post-action consequences to reweight heterogeneous offline robot samples instead of trusting all demonstrations equally.

### RoboDrop

Paper: https://arxiv.org/abs/2609.10021

Studies post-training data curation under heterogeneous errors such as execution mistakes, sensor drift and timestamp misalignment.

### ATHENA

Paper: https://arxiv.org/abs/2606.16208

Uses scalable influence-style analysis for multitask VLA data curation.

Required future metadata:

```text
sample weighting
filtering / drop criteria
operator identity / quality
sensor synchronization checks
failure / recovery labels
synthetic-confidence score
```

---

## 6. Frozen vs updated components is a scientific variable

### TEMPO

Paper: https://arxiv.org/abs/2608.07314

Freezes the pretrained vision-language backbone while updating semantic projection and low-level action expert at different rates.

This is important because uniform full-model RL can destabilize semantic representations while trying to improve control.

### Learning Action Priors for Cross-embodiment Robot Manipulation

Paper: https://arxiv.org/abs/2606.26095

Pretrains an action module on unconditioned motion trajectories before VLA alignment, arguing that action modules otherwise learn physical temporal structure from scratch during cross-modal training.

Future Clover comparisons should include:

```text
frozen backbone
adapter / LoRA
projection + action head
partial backbone
full model
```

under matched data and compute.

---

## 7. Offline SFT, online RL and on-policy distillation cover different state distributions

### VLA-OPD

Paper: https://arxiv.org/abs/2603.26666

Frames the trade-off as:

```text
offline SFT
→ efficient
→ demonstration distribution
→ distribution-shift / forgetting risk

online RL
→ current-policy state distribution
→ sparse reward / expensive interaction

on-policy distillation
→ current-policy states
→ dense teacher supervision
```

This is a useful template for later controlled experiments.

### Online-RL references

- RL fine-tuning for diffusion navigation — https://arxiv.org/abs/2603.12868
- LaST-R1 — https://arxiv.org/abs/2604.28192
- PAC-ACT — https://arxiv.org/abs/2607.09590
- TEMPO — https://arxiv.org/abs/2608.07314
- VLA-Precision — https://arxiv.org/abs/2609.04355

For every online-RL result record:

```text
number of real/sim rollouts
reset procedure
reward source
safety constraints
exploration policy
reference-policy/KL constraint
which parameters update
human interventions
failed rollout retention
```

---

## 8. Simulated/world-model post-training requires explicit trust

### RehearseVLA

CVPR 2026: https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_RehearseVLA_Simulated_Post-Training_for_VLAs_with_Physically-Consistent_World_Model_CVPR_2026_paper.html

Uses a learned world-model simulator for RL-style VLA post-training when physical resets/interactions are expensive.

### MERL — Trust-Calibrated VLA Policy Post-Training with Evolving Imagination

Paper: https://arxiv.org/abs/2610.16517

Submitted 2026-10-12. It explicitly varies imagined-data ratio and rollout horizon according to simulator reliability and uses trust to weight replay/optimization.

This strengthens a Stage-1 rule:

```text
more imagined data
≠ better post-training
```

if the learned simulator is inaccurate.

Later tests should vary:

```text
simulator calibration error
imagined-data fraction
imagined rollout horizon
trust threshold
real/sim mixing ratio
```

---

## 9. Failure / recovery data are a separate distribution

Most demonstration datasets overrepresent successful expert trajectories.

Relevant references:

- LoopWAM — https://arxiv.org/abs/2610.18873
- OnEvoMemory — https://arxiv.org/abs/2608.08749
- FailSafe — https://arxiv.org/abs/2510.01642
- ReSYNC / Recover, Discover, Plan — https://arxiv.org/abs/2606.18328
- ENPIRE — https://arxiv.org/abs/2606.19980

Distinguish:

```text
expert success
suboptimal success
recoverable failure
irrecoverable failure
human correction
self-recovery
```

Training only on ideal demonstrations can produce strong nominal behavior but weak recovery.

---

## 10. Checkpoint selection / offline validation can mislead

### Critical Interval MSE

Paper: https://arxiv.org/abs/2606.29898

Motivation: ordinary validation loss on expert demonstrations can be poorly correlated with real rollout performance.

### RoboFQE

Paper: https://arxiv.org/abs/2610.18699

Provides rollout-free offline policy evaluation from offline trajectories.

Stage-1 implication:

```text
best validation-loss checkpoint
≠ best deployed robot policy
```

Record the selection metric and whether it was validated against closed-loop outcomes.

---

## 11. General LLM/VLM post-training also shows capability interference

### DeepSeek-R1

Paper: https://arxiv.org/abs/2501.12948

RL-only reasoning can emerge but behavior quality/readability can degrade; cold-start and staged training change the outcome.

### DeepSeek-V4.1-Flash

Official: https://www.deepseek.com/en/news/deepseek-v4-1-flash/  
Model: https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash

Released recipe:

```text
SFT → RL → on-policy distillation
```

with major emphasis on automated task/environment/rollout generation.

### Qwen3

Official: https://qwenlm.github.io/blog/qwen3/

Flagship stages:

```text
long-CoT cold start
→ reasoning RL
→ thinking/non-thinking fusion
→ general RL
```

### Text-Centric Post-Training for Omni-Modal Reasoning

Paper: https://arxiv.org/abs/2610.02819

Important boundary result: text-only reasoning post-training can improve multimodal reasoning while degrading perception; a later native multimodal refinement can recover perception.

This is direct evidence that:

```text
post-training improvement on one axis
≠ monotonic improvement on every axis
```

---

## 12. Proposed future Clover training ablation matrix

When implementation becomes appropriate, use a fixed small/medium backbone and matched data budget.

### Objective axis

```text
BC / SFT
action + language co-training
action + future latent
BC + world-state auxiliary
on-policy distillation
simulated RL
online RL
failure/recovery replay
```

### Update-scope axis

```text
frozen backbone
adapter / LoRA
projection/head only
partial backbone
full model
```

### Data axis

```text
expert-only
expert + suboptimal
expert + failure/recovery
robot only
robot + human video
robot + sim
robot + human + sim
```

### Temporal-control axis

```text
single action
fixed chunk
mixture of horizons
adaptive execution horizon
```

### Evaluation vector

```text
IID task success
OOD scene/object/task
cross-embodiment
recovery
physical consistency
uncertainty calibration
persistent memory / revision
state aliasing
long-horizon reliability
latency / memory / energy
catastrophic forgetting
```

Do not change all axes at once.

---

## 13. Remaining training-specific gaps

See [`HIGH_RISK_BOUNDARIES.md`](HIGH_RISK_BOUNDARIES.md) for the expanded evidence matrix. Remaining open questions include:

```text
robot post-training scaling laws under matched architecture/data quality
reward models that encode partial success + safety + epistemic correctness
human intervention / takeover as training signal
failure/recovery sampling without destabilizing nominal skills
weighting synthetic samples by simulator/world-model trust
pretraining-objective effects on later physical identifiability
continual fleet learning without propagating one robot's sensor/hardware fault
personalized embodiment adaptation vs global shared policy
rollback semantics when model weights and persistent memory co-evolve
optimizer / LR / batch-size effects on pretrained world-state representations
seed variance for real-robot post-training
checkpoint selection metrics that predict EV7/EV8 performance
joint world-model/policy training vs sequential training under matched compute
```

---

## Final rule

For every claimed training gain ask:

```text
what changed?
data?
objective?
update scope?
action representation?
on/off-policy distribution?
reward/teacher?
simulator trust?
checkpoint-selection metric?
runtime?
```

Until these are controlled, do not call the gain an architectural discovery.

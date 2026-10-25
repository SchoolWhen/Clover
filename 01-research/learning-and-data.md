<a id="top"></a>

# 调研方向：数据、训练与持续学习

Maintained: **2026-10-25** · Document stage: **1 — Research** ([status](../STATUS.md)).

Training, post-training, data provenance, continual learning and capability preservation under adaptation.

This is the canonical topic document. Update it in place; source-level dates and reading-depth labels below qualify the evidence, not the maintenance date.

## Contents

- [Training, Post-Training and Embodied Learning Regimes](#topic-research-research_training_posttraining)
- [Training / Post-Training — Supporting Stage-1 Matrix](#topic-research-training-readme)
- [Training / Post-Training — High-Risk Boundary Questions](#topic-research-training-high_risk_boundaries)
- [Data, Experience and Interaction](#topic-docs-research-map-data-and-experience)
- [Lifelong Learning and World Growth](#topic-docs-research-map-lifelong-learning)

<a id="topic-research-research_training_posttraining"></a>

## Training, Post-Training and Embodied Learning Regimes

Source record updated: **2026-10-15**
Source intake checked through: **2026-10-15**

> **Research question:** How can a machine understand the real world through vision alone?

This is a Stage-1 research document. It does **not** choose a Clover training recipe.

Its purpose is to make one missing variable explicit:

```text
same architecture
+ different data / objective / update scope / interaction regime
→ potentially very different capability
```

For modern foundation models and robot policies, training procedure is not merely an implementation detail. It can determine what information is preserved, what behavior is preferred, how well the model generalizes, whether old capabilities are forgotten, and whether the deployed policy survives its own state distribution.

---

### 1. Keep model architecture separate from training regime

Record separately:

```text
base architecture
pretraining objective
pretraining data mixture
continued pretraining
supervised fine-tuning / behavior cloning
preference optimization
reinforcement learning
on-policy / off-policy data
knowledge distillation
world-model / simulator post-training
deployment-rollout learning
continual / test-time adaptation
```

Do not conclude that an architectural component caused a gain if the compared systems also changed training data, objective, update scope, reward source or deployment interaction.

---

### 2. A useful training-regime taxonomy

#### TR0 — base pretraining

Examples:

```text
next-token prediction
masked / predictive representation learning
vision-language pretraining
video prediction
world-model prediction
```

Question: what broad prior is acquired before task-specific robot supervision?

#### TR1 — continued / domain-adaptive pretraining

Continue training on a narrower domain before task-specific adaptation.

Examples:

```text
robot video
human manipulation video
egocentric video
physical reasoning data
long-context / long-video data
```

Risk: domain specialization can improve downstream transfer while eroding unrelated capabilities.

#### TR2 — supervised post-training / behavior cloning

For LLM/VLM:

```text
instruction SFT
multimodal SFT
CoT cold start
```

For robots:

```text
observation + instruction + action demonstration
→ supervised action prediction
```

Robot behavior cloning is analogous to SFT only at a high level. Robot actions alter the future state distribution, so deployment can rapidly leave the demonstration distribution.

#### TR3 — co-training / auxiliary-objective training

Examples:

```text
VLM + VLA co-training
language supervision + actions
future latent prediction + actions
geometry / depth / pose auxiliaries
world-model + policy joint objectives
```

These signals can change representation quality even when architecture stays fixed.

#### TR4 — preference / conservative offline alignment

Examples include:

```text
preference optimization
sample reweighting
quality filtering
posterior / transition attribution
```

Useful when recorded data contain conflicting or suboptimal supervision.

#### TR5 — reinforcement learning with verifiable or learned rewards

For general models this may use:

```text
rule/verifier rewards
preference reward models
tool / environment outcomes
```

For robots it may use:

```text
task success
progress
collision / force / safety penalties
world-model or VLM-generated rewards
```

Reward design becomes part of the scientific claim.

#### TR6 — online embodied reinforcement learning

The current policy acts, changes the world, and learns from its own state distribution.

This can correct covariate shift but is expensive, safety-sensitive and reset-limited in the real world.

#### TR7 — on-policy distillation / teacher-guided self-generated trajectories

The student visits states induced by its own policy while a teacher supplies denser supervision.

This can bridge offline SFT and expensive sparse-reward RL, but teacher errors and epistemic uncertainty become part of the evidence chain.

#### TR8 — strong-to-weak / model distillation

Transfer capability from a larger teacher into a smaller model.

Important question for Clover:

```text
what survives distillation?
```

Measure not only task accuracy but memory, uncertainty, persistence, physical reasoning and rare-event behavior.

#### TR9 — simulated / world-model post-training

Use a simulator or learned world model for exploration, RL or rehearsal.

Important distinction:

```text
learning to exploit simulator/world-model errors
≠ learning correct real-world behavior
```

#### TR10 — deployment-rollout learning / self-improvement

Use successful, failed and suboptimal deployment trajectories for further training.

This includes failure mining, active data collection and repeated deployment→training cycles.

#### TR11 — continual / test-time adaptation

Update after deployment as environment, robot body, sensors or task distribution changes.

Must be evaluated together with forgetting, rollback and persistent-state compatibility.

These labels are bookkeeping tools, not a Clover training plan.

---

### 3. General LLM / VLM post-training: current lessons

#### DeepSeek-R1 — RL can create capability, but raw RL has behavioral failure modes

Primary paper: https://arxiv.org/abs/2501.12948
Official code: https://github.com/deepseek-ai/DeepSeek-R1

DeepSeek-R1-Zero applies large-scale RL directly to a base model without preliminary SFT and reports emergent reasoning behavior. The same line also reports practical problems such as repetition, poor readability and language mixing. DeepSeek-R1 introduces cold-start data and multi-stage training before/around RL.

Stage-1 lesson:

```text
RL can improve a target capability
without automatically producing desirable overall behavior.
```

The initialization / cold-start distribution matters.

#### DeepSeek-V4.1-Flash — data-pipeline changes can dominate algorithmic changes

Official release: https://www.deepseek.com/en/news/deepseek-v4-1-flash/
Model / technical material: https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash

The released description uses:

```text
SFT
→ RL
→ on-policy distillation
```

and states that substantive post-training changes are concentrated in large-scale automatic synthesis of agent tasks/environments plus progressive scaling of tasks and rollouts rather than a new RL algorithm.

Stage-1 lesson:

```text
post-training algorithm
≠ post-training data pipeline
```

Both must be reported.

#### Qwen3 — staged post-training deliberately installs different behavior modes

Official overview: https://qwenlm.github.io/blog/qwen3/
Technical report: https://arxiv.org/abs/2505.09388

The flagship Qwen3 pipeline uses four stages:

```text
long-CoT cold-start SFT
→ reasoning RL
→ thinking / non-thinking fusion
→ general-domain RL
```

Smaller models use strong-to-weak distillation to avoid reproducing the full expensive pipeline.

Stage-1 lesson:

> “post-training” is not one operation. Different stages can install reasoning style, combine behavioral modes, align preferences and transfer capability to smaller models.

#### Qwen3-VL — multimodal post-training must preserve perception while improving reasoning

Primary paper: https://arxiv.org/abs/2511.21631

The released post-training recipe includes supervised fine-tuning, strong-to-weak distillation and reinforcement learning across text and multimodal domains, including grounding and tool-integrated visual reasoning.

A useful 2026 boundary result is:

- Text-Centric Post-Training for Omni-Modal Reasoning — https://arxiv.org/abs/2610.02819

It reports that text-only reasoning post-training can substantially improve multimodal reasoning while degrading perception, and that a smaller native audio-visual RL refinement can recover perception while retaining most reasoning gains.

Stage-1 lesson:

```text
reasoning improvement
≠ perception preservation
```

A post-training objective can create cross-capability interference.

---

### 4. Robot training is only partially analogous to LLM post-training

Common high-level structure:

```text
large general prior
→ specialization
→ feedback / correction
→ deployment
```

But the learning problem is materially different.

#### Language-model output

```text
token
```

An incorrect token usually does not physically alter the next input distribution.

#### Robot-policy output

```text
continuous / discretized action
→ changes physical world
→ changes camera evidence
→ changes future reachable states
```

Therefore robot post-training must handle:

```text
covariate shift
continuous multimodal actions
control frequency / latency
embodiment-specific semantics
costly real-world resets
sparse / delayed reward
safety and irreversible actions
contact dynamics
hardware drift
human teleoperation quality
sim2real mismatch
```

So:

```text
LLM SFT → RL recipe
≠ directly reusable robot recipe
```

---

### 5. Major robot-policy training families

#### 5.1 Behavior cloning / imitation learning

Learn recorded expert actions from demonstrations.

Strengths:

```text
stable
simple
uses offline data
safe compared with online exploration
```

Weaknesses:

```text
policy-induced distribution shift
recovery states underrepresented
operator inconsistency
suboptimal demonstrations
```

Classical examples include ACT-style action chunking and Diffusion Policy.

Diffusion Policy: https://arxiv.org/abs/2303.04137

#### 5.2 Action representation and decoding objective are training variables

OpenVLA-OFT: https://arxiv.org/abs/2502.19645

Under an OpenVLA backbone, changing fine-tuning design — parallel decoding, action chunking, continuous actions and an L1 objective — materially changes both task success and inference speed.

Stage-1 lesson:

```text
backbone quality
≠ downstream policy quality
```

Action representation and decoding loss can dominate adaptation.

#### 5.3 Flow / diffusion action experts

π0 uses a pretrained VLM plus a continuous action expert trained with flow matching.

Official overview: https://www.physicalintelligence.company/blog/pi0
Paper: https://www.physicalintelligence.company/download/pi0.pdf

The system combines internet-scale visual-language pretraining, cross-embodiment robot data and later high-quality task post-training.

π0.5 adds a two-stage structure in which pretraining uses discrete-token tasks and post-training introduces a finer-grained action expert for mobile manipulation and efficient real-time control.

π0.5 paper: https://www.physicalintelligence.company/download/pi05.pdf

Important distinction:

```text
semantic pretraining
≠ motor post-training
```

#### 5.4 Cross-embodiment co-training requires alignment

Open X-Embodiment / RT-X: https://arxiv.org/abs/2310.08864

Qwen-RobotManip: https://arxiv.org/abs/2606.17846
Official overview: https://qwen.ai/blog?id=qwen-robotmanip

Qwen-RobotManip uses:

```text
Qwen3.5-4B VLM backbone
+
flow-matching DiT action head
```

with a canonical 80-dimensional state/action space, camera-frame delta poses, camera calibration information and in-context embodiment conditioning.

Reported training structure:

```text
pretraining:
VLA robot stream + VLM stream
≈ 9:1

post-training:
generalist supervised fine-tuning on demonstration data
+ VLM/VLA co-training
```

The work argues that representation, motion and behavior alignment are prerequisites for useful data scaling across embodiments.

Stage-1 lesson:

```text
more heterogeneous robot data
≠ automatically better
```

Data must have compatible state/action semantics.

#### 5.5 Human-video / latent-action pretraining

LAPA: https://arxiv.org/abs/2410.11758
ConLA: https://arxiv.org/abs/2602.00557
HARP-VLA: https://arxiv.org/abs/2605.31234
HuRo: https://arxiv.org/abs/2609.10706
JALA: https://openaccess.thecvf.com/content/CVPR2026/html/Luo_Joint-Aligned_Latent_Action_Towards_Scalable_VLA_Pretraining_in_the_Wild_CVPR_2026_paper.html

These approaches try to exploit large human-video corpora by learning latent actions, aligning human/robot representations, or converting human trajectories into robot-compatible observations/actions.

Main risks:

```text
human hand dynamics ≠ robot dynamics
visual similarity ≠ executable action equivalence
retargeted action ≠ measured robot action
synthetic robotization errors can become supervision
```

Record synthetic / inferred action provenance explicitly.

#### 5.6 Synthetic-data / simulation pretraining

NVIDIA GR00T N1 / N1.7 uses mixtures of human/egocentric, synthetic/simulation and real robot data.

Official training overview: https://developer.nvidia.com/blog/accelerate-generalist-humanoid-robot-development-with-nvidia-isaac-gr00t-n1/
N1.7 overview: https://developer.nvidia.com/blog/develop-humanoid-robot-policies-end-to-end-with-nvidia-isaac-gr00t/

N1.7 is reported as pretrained on roughly 32K hours of real demonstration/human egocentric data plus roughly 8K hours of simulated rollouts/demonstrations, followed by robot-specific post-training workflows.

Important question:

> Which gains come from data quantity, which from embodiment alignment, and which from simulator-specific structure?

#### 5.7 Offline post-training on heterogeneous robot data

Posterior-Transition Reweighting: https://arxiv.org/abs/2603.16542

This work treats recorded robot demonstrations as unequal supervision and reweights samples according to how attributable the observed post-action consequence is under the current representation.

Ambient Diffusion Policy: https://arxiv.org/abs/2606.12365

This work studies how suboptimal data should contribute differently at different diffusion noise levels.

Stage-1 lesson:

```text
all demonstrations equally weighted
```

is itself a training assumption.

#### 5.8 Online RL post-training

Robot RL can move a policy beyond demonstration behavior, but interaction is expensive and dangerous.

Examples:

- VLA navigation GRPO fine-tuning — https://arxiv.org/abs/2603.12868
- LaST-R1 — https://arxiv.org/abs/2604.28192
- PAC-ACT — https://arxiv.org/abs/2607.09590
- TEMPO — https://arxiv.org/abs/2608.07314
- VLA-Precision — https://arxiv.org/abs/2609.04355

TEMPO is especially useful conceptually because it updates semantic and low-level action components at different rates rather than treating the whole VLA as one homogeneous policy.

Stage-1 lesson:

```text
which parameters are updated
```

is a first-class post-training variable.

#### 5.9 On-policy distillation as a bridge between SFT and RL

VLA-OPD: https://arxiv.org/abs/2603.26666

The student visits states generated by its own policy while an expert teacher gives dense supervision. The paper explicitly frames the problem as a trade-off:

```text
offline SFT
→ efficient but distribution-shift / forgetting risk

online RL
→ on-policy but sparse-reward / sample-efficiency problems
```

On-policy distillation tries to combine on-policy state coverage with dense teacher signals.

#### 5.10 Simulated / world-model RL post-training

RehearseVLA: https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_RehearseVLA_Simulated_Post-Training_for_VLAs_with_Physically-Consistent_World_Model_CVPR_2026_paper.html

The method performs RL-style post-training inside a learned physical world simulator to avoid expensive/non-resettable real interaction.

Important danger:

```text
world-model bias
→ reward / exploration bias
→ policy learns simulator artifact
```

This must be followed by EV3–EV8 evidence rather than treated as real-world RL.

#### 5.11 Deployment self-improvement / failure learning

LoopWAM: https://arxiv.org/abs/2610.18873

RoboCat historical reference: https://deepmind.google/blog/robocat-a-self-improving-robotic-agent

ENPIRE: https://arxiv.org/abs/2606.19980

This family uses policy failures, suboptimal deployment rollouts, autonomous data collection or agent-guided training loops to improve subsequent models.

Important distinction:

```text
self-improvement
≠ safe improvement
≠ monotonic improvement
≠ unbiased data collection
```

---

### 6. Controlled evidence that training objective changes representation

#### VLAFlow

Paper: https://arxiv.org/abs/2607.01586

VLAFlow fixes a π0-style architecture, shared VLM backbone, action expert and 14-dimensional action space, then compares four training signals on the same heterogeneous robot corpus:

```text
action-only
language-supervised co-training
future-latent alignment
language + future-latent combination
```

Reported conclusion:

- action-only pretraining is sensitive to heterogeneous data;
- language supervision better preserves vision-language generalization;
- future latent alignment improves transition/action-outcome modeling;
- combining both provides the most stable overall transfer across the reported benchmarks.

This is especially valuable to Clover because it isolates **objective choice** more cleanly than comparing unrelated model families.

---

### 7. Post-training can improve one capability while damaging another

Track at least these failure modes:

#### PT-F1 — catastrophic forgetting

Task/robot fine-tuning erases broad pretrained semantic or physical capability.

#### PT-F2 — reward overoptimization / reward hacking

RL improves the training reward without improving the intended real-world capability.

#### PT-F3 — perception-reasoning interference

Reasoning tuning improves inference but weakens visual perception or grounding.

#### PT-F4 — action-mode collapse

Fine-tuning narrows a useful multimodal action distribution into one brittle strategy.

#### PT-F5 — unsafe exploration

Online RL visits dangerous or irreversible states.

#### PT-F6 — simulator exploitation

World-model/simulator post-training discovers artifacts rather than real physics.

#### PT-F7 — embodiment over-specialization

Target-robot fine-tuning reduces cross-embodiment transfer.

#### PT-F8 — calibration loss

Post-training produces more confident behavior without better epistemic calibration.

#### PT-F9 — memory / state regression

Task success improves while persistence, belief revision or long-horizon world state degrades.

#### PT-F10 — deployment-data feedback bias

Self-training increasingly samples states created by the current policy and can reinforce blind spots.

---

### 8. Required training provenance for future Clover comparisons

For every serious baseline or experiment record:

```text
base checkpoint
architecture revision
pretraining corpus / source classes
pretraining objective
continued-pretraining data
post-training stages and order
objective per stage
data per stage
real / synthetic / human-video / robot-data ratio
on-policy vs off-policy
reward source / verifier
teacher model if distilled
what parameters are frozen / updated
learning rate / update ratio where material
action representation
control frequency / chunk size
history/context supplied
simulator or real environment used for training
failure / recovery data included?
privileged state / force / depth / tactile used?
checkpoint selected by which metric?
```

Without this record, architecture comparisons are confounded.

---

### 9. A useful controlled training-ablation matrix for Clover

For a fixed backbone and matched data budget, later compare:

```text
A  supervised behavior cloning only
B  A + VLM co-training
C  A + future-state / world-model auxiliary
D  A + strong-to-weak distillation
E  A + on-policy teacher distillation
F  A + simulated RL
G  A + real/proxy online RL
H  A + deployment failure/recovery data
```

Also cross with update scope:

```text
freeze visual/VLM backbone
adapter / LoRA only
projection + action head
upper backbone + action head
full model
```

And measure a capability vector rather than success alone:

```text
task success
OOD scene/object/task transfer
cross-embodiment transfer
recovery
physical consistency
uncertainty calibration
persistent memory
state aliasing
long-horizon reliability
latency / memory
catastrophic forgetting
```

---

### 10. Mac mini M4 implication

The current machine is suitable for controlled small-model/post-training experiments such as:

```text
small Qwen/VLM backbone
frozen-backbone + action/state head
LoRA / adapter tuning
offline behavior cloning
flow/diffusion action-head experiments
small MuJoCo RL
teacher distillation experiments
objective / data-mixture ablations
quantized post-training inference tests
```

Do not use the inability to reproduce frontier-scale RL locally as a reason to skip training-regime research.

Use small controlled proxies first, then validate important effects on remote larger checkpoints when necessary.

Critical rule:

```text
effect observed on 4B proxy
≠ automatically valid on frontier MoE
```

Scaling validation remains required.

---

### 11. Current open questions

Continue collecting evidence for:

```text
Which post-training stages improve physical reasoning rather than linguistic reasoning only?
When should the VLM/world-state backbone be frozen during robot adaptation?
Can RL improve action robustness without corrupting semantic/world-state representations?
How should reward signals represent uncertainty, safety and partial success?
How should failed/recovery trajectories be sampled relative to expert successes?
What real/sim/human-video mixture best preserves OOD physical transfer?
Can on-policy distillation preserve uncertainty better than hard imitation?
When does future-state auxiliary training improve actual control?
How much world-model capability survives policy distillation?
How does quantization interact with post-trained behavior?
How should continual robot learning rollback persistent state when model weights roll back?
How should synthetic-data provenance affect sample weighting?
What training objectives preserve `S-OPEN` future-task optionality instead of only `S-CTRL`?
```

---

### 12. Stage-2 analysis priority created by this surface

When Stage 2 starts, explicitly compare these training-regime clusters:

```text
DeepSeek-R1 / V4.1 post-training
Qwen3 / Qwen3-VL post-training
π0 / π0.5
OpenVLA-OFT
Qwen-RobotManip
GR00T N1.7
VLAFlow
VLA-OPD
TEMPO / online RL variants
RehearseVLA
LoopWAM / deployment self-improvement
human-video latent-action pretraining: LAPA / HARP / HuRo / JALA
```

The objective is not to find one universally best recipe. The objective is to identify which learning regime preserves which capability under which evidence and deployment constraints.

---

### Final rule

```text
architecture
× data
× objective
× update scope
× interaction regime
× runtime
→ observed capability
```

Do not attribute the result to architecture alone.

---

<a id="topic-research-training-readme"></a>

## Training / Post-Training — Supporting Stage-1 Matrix

Source record updated: **2026-10-15**
Source intake checked through: **2026-10-15**

> Supporting material for [`learning-and-data.md`](#topic-research-research_training_posttraining).

This file is **not** a Clover training recipe. It records variables that must be controlled before attributing a capability gain to architecture or representation.

High-risk cross-boundary questions live in [`learning-and-data.md`](#topic-research-training-high_risk_boundaries), including partial-success rewards, epistemic calibration, failure/recovery ratios, simulator trust, module adaptation timescales, uncertainty regression, distillation, scaling, fleet-update contamination and model/memory rollback consistency.

---

### 1. Training variables that must be separated

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

### 2. Data scale is not one scalar

#### Data Scaling Laws in Imitation Learning for Robotic Manipulation

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

#### Qwen-RobotManip

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

### 3. Objective choice changes transfer under a fixed backbone

#### VLAFlow

Paper: https://arxiv.org/abs/2607.01586

Controlled comparison under a shared π0-style architecture/backbone/action space:

```text
action-only
vs language co-training
vs future-latent alignment
vs language + future-latent
```

This is a high-value Stage-2 candidate because it isolates training signal better than comparing unrelated model families.

#### VLAct — continued pretraining as representation learning

Project: https://starvla.github.io/VLAct/

Use as a current signal that robot continued pretraining can be framed as preserving/learning transferable visual-action representation rather than simply fitting action labels.

Treat project-reported results conservatively until primary-paper details are analyzed.

---

### 4. Action representation and action horizon are training variables

#### OpenVLA-OFT

Paper: https://arxiv.org/abs/2502.19645

Shows that action decoding scheme, action chunking, continuous action representation and fine-tuning loss can materially change both policy performance and inference speed even with the same OpenVLA base.

#### Mixture of Horizons

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

#### GeoAAC

Paper: https://arxiv.org/abs/2609.20776

Adapts action horizon using flow-denoising geometry.

#### ChunkTrust

Paper: https://arxiv.org/abs/2609.39754

Treats execution horizon as a latent variable inferred from action-expert evidence.

Research implication:

> `action chunk length` and `how many predicted actions are actually executed before replanning` must be recorded separately.

---

### 5. Data quality / weighting can matter more in post-training than pretraining

#### Posterior-Transition Reweighting

Paper: https://arxiv.org/abs/2603.16542

Uses observed post-action consequences to reweight heterogeneous offline robot samples instead of trusting all demonstrations equally.

#### RoboDrop

Paper: https://arxiv.org/abs/2609.10021

Studies post-training data curation under heterogeneous errors such as execution mistakes, sensor drift and timestamp misalignment.

#### ATHENA

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

### 6. Frozen vs updated components is a scientific variable

#### TEMPO

Paper: https://arxiv.org/abs/2608.07314

Freezes the pretrained vision-language backbone while updating semantic projection and low-level action expert at different rates.

This is important because uniform full-model RL can destabilize semantic representations while trying to improve control.

#### Learning Action Priors for Cross-embodiment Robot Manipulation

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

### 7. Offline SFT, online RL and on-policy distillation cover different state distributions

#### VLA-OPD

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

#### Online-RL references

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

### 8. Simulated/world-model post-training requires explicit trust

#### RehearseVLA

CVPR 2026: https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_RehearseVLA_Simulated_Post-Training_for_VLAs_with_Physically-Consistent_World_Model_CVPR_2026_paper.html

Uses a learned world-model simulator for RL-style VLA post-training when physical resets/interactions are expensive.

#### MERL — Trust-Calibrated VLA Policy Post-Training with Evolving Imagination

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

### 9. Failure / recovery data are a separate distribution

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

### 10. Checkpoint selection / offline validation can mislead

#### Critical Interval MSE

Paper: https://arxiv.org/abs/2606.29898

Motivation: ordinary validation loss on expert demonstrations can be poorly correlated with real rollout performance.

#### RoboFQE

Paper: https://arxiv.org/abs/2610.18699

Provides rollout-free offline policy evaluation from offline trajectories.

Stage-1 implication:

```text
best validation-loss checkpoint
≠ best deployed robot policy
```

Record the selection metric and whether it was validated against closed-loop outcomes.

---

### 11. General LLM/VLM post-training also shows capability interference

#### DeepSeek-R1

Paper: https://arxiv.org/abs/2501.12948

RL-only reasoning can emerge but behavior quality/readability can degrade; cold-start and staged training change the outcome.

#### DeepSeek-V4.1-Flash

Official: https://www.deepseek.com/en/news/deepseek-v4-1-flash/
Model: https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash

Released recipe:

```text
SFT → RL → on-policy distillation
```

with major emphasis on automated task/environment/rollout generation.

#### Qwen3

Official: https://qwenlm.github.io/blog/qwen3/

Flagship stages:

```text
long-CoT cold start
→ reasoning RL
→ thinking/non-thinking fusion
→ general RL
```

#### Text-Centric Post-Training for Omni-Modal Reasoning

Paper: https://arxiv.org/abs/2610.02819

Important boundary result: text-only reasoning post-training can improve multimodal reasoning while degrading perception; a later native multimodal refinement can recover perception.

This is direct evidence that:

```text
post-training improvement on one axis
≠ monotonic improvement on every axis
```

---

### 12. Proposed future Clover training ablation matrix

When implementation becomes appropriate, use a fixed small/medium backbone and matched data budget.

#### Objective axis

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

#### Update-scope axis

```text
frozen backbone
adapter / LoRA
projection/head only
partial backbone
full model
```

#### Data axis

```text
expert-only
expert + suboptimal
expert + failure/recovery
robot only
robot + human video
robot + sim
robot + human + sim
```

#### Temporal-control axis

```text
single action
fixed chunk
mixture of horizons
adaptive execution horizon
```

#### Evaluation vector

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

### 13. Remaining training-specific gaps

See [`learning-and-data.md`](#topic-research-training-high_risk_boundaries) for the expanded evidence matrix. Remaining open questions include:

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

### Final rule

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

---

<a id="topic-research-training-high_risk_boundaries"></a>

## Training / Post-Training — High-Risk Boundary Questions

Source record updated: **2026-10-15**
Source intake checked through: **2026-10-15**

> Supporting material for [`learning-and-data.md`](#topic-research-research_training_posttraining).

These questions are high-risk because optimizing one headline metric can silently damage other properties of a robotic world model or policy.

Current rule:

```text
task success ↑
does not imply
world understanding / calibration / memory / recovery / safety ↑
```

For every question below, the goal is to record what is known, what is still open, and what Clover should measure later.

---

### Q1 — How should a reward represent partial success?

Binary success/failure is too coarse for long-horizon robot learning.

Current evidence:

- DenseReward predicts dense frame-level progress and explicitly synthesizes physically realistic failure trajectories: https://arxiv.org/abs/2607.13033
- SARM2 uses multi-task stage-aware dense reward for long-horizon manipulation: https://arxiv.org/abs/2606.10305
- Z-1 uses completion-aware reward calibration during VLA RL post-training: https://arxiv.org/abs/2606.31846
- Quantization-Conditioned RL uses progress-scaled terminal penalties to distinguish partial completion in low-bit VLA policies: https://arxiv.org/abs/2610.15675

Do not collapse partial success into one arbitrary scalar without preserving decomposition.

A useful future reward record is:

```text
R_task          final task completion
R_progress      stage / subgoal progress
R_physics       physically valid interaction
R_safety        constraint violations / near misses
R_recovery      successful recovery after deviation
R_epistemic     calibrated belief / justified uncertainty
R_efficiency    time / energy / intervention cost
```

Whether these should be scalarized, lexicographically ordered or handled as constrained objectives remains open.

---

### Q2 — Should reward explicitly encourage epistemic correctness, not only task success?

**Yes, this must be researched; the exact objective is open.**

A policy can finish a task while holding a badly calibrated or factually wrong world belief.

Methodological evidence outside robotics is strong: ordinary reasoning RL can improve task accuracy while degrading calibration, while proper-scoring-rule rewards can preserve or improve calibrated confidence.

- RLCR / *Beyond Binary Rewards* — https://arxiv.org/abs/2507.16806

Embodied reward work already shows that reward must be multi-dimensional and verified rather than a simple success scalar:

- ReWorld rewards physical realism, task logic, embodiment plausibility and visual quality: https://arxiv.org/abs/2601.12428
- Reward as an Agent explicitly targets reward hacking / verification failures in embodied world-model RL: https://arxiv.org/abs/2606.19990

Future Clover research should test separate epistemic terms such as:

```text
calibration / proper scoring
unknown-state correctness
belief update after contradictory evidence
confidence in world-model rollout
refusal / ask-for-more-evidence behavior
```

Critical warning:

```text
rewarding “high confidence” is wrong.
```

The target should be **confidence justified by evidence/outcomes**, not confidence itself.

---

### Q3 — What fraction of training data should be failure trajectories?

**No universal ratio is supported by current evidence. Do not invent one.**

The correct fraction likely depends on:

```text
base-policy failure rate
failure diversity
severity / recoverability
nominal-state coverage
recovery objective
training stage
on-policy vs offline distribution
```

Current evidence:

- DenseReward argues diverse failure data is necessary for dense reward learning: https://arxiv.org/abs/2607.13033
- FAR exploits informative failure cases and successful retries for continual improvement: https://arxiv.org/abs/2607.01111
- FLARE adds retry/reset behavior because failure-free demonstrations leave policies unable to recover: https://arxiv.org/abs/2608.26645
- LoopWAM explicitly learns from successes, suboptimal behavior and failures: https://arxiv.org/abs/2610.18873

Required experiment:

```text
failure/recovery fraction sweep
0 / low / medium / high
with fixed total data budget
```

Evaluate both failure recovery **and nominal performance**.

---

### Q4 — Can recovery data damage the nominal policy?

**Yes in principle; current literature mostly demonstrates benefit but does not justify unlimited recovery mixing.**

Recovery states can be heavily off the nominal trajectory distribution. Oversampling them can distort the policy toward conservative/recovery behavior or weaken clean execution.

Useful references:

- FLARE separates ordinary Retry from state-breaking Reset behavior rather than forcing every failure mode into one undifferentiated nominal policy: https://arxiv.org/abs/2608.26645
- RecoverFly combines failure revisiting with reference-policy regularization specifically to improve adaptation while preserving acquired capability: https://arxiv.org/abs/2608.09467
- FAR uses failure-contrastive adaptation and then incorporates successful recovery trajectories: https://arxiv.org/abs/2607.01111

Future Clover experiment:

```text
nominal-only
vs nominal + recovery mixed uniformly
vs prioritized recovery
vs separate recovery module / gate
```

Measure:

```text
clean-task success
trajectory efficiency
unnecessary reset/retry frequency
recovery success
safety
OOD robustness
```

---

### Q5 — How should world-model confidence control imagined rollout length?

This is now an active 2026 research direction rather than a purely hypothetical idea.

- MERL explicitly lets simulator reliability control the imagined-data ratio and rollout horizon; chunk-level trust also controls replay selection and optimization weight: https://arxiv.org/abs/2610.16517
- RWM-U propagates epistemic uncertainty over world-model rollouts for offline model-based RL on physical robots: https://arxiv.org/abs/2504.16680
- WOMBET filters generated experience by return and epistemic uncertainty before transfer: https://proceedings.mlr.press/v331/kim26a.html
- WoVR focuses on preventing policy optimization from exploiting hallucinated imagined success: https://arxiv.org/abs/2602.13977

Future rule to test, not assume:

```text
high trust → longer imagination / more synthetic weight
low trust  → shorter rollout / lower weight / real-data fallback
```

Confidence must itself be calibrated against held-out real or high-trust transitions.

---

### Q6 — Does the optimal human-video / simulator / robot-data mixture depend on model scale?

**Very likely, but current evidence does not provide a universal scaling law.**

Qwen-RobotManip is a key current data-engine example:

- ~11.4K h robot data
- ~1.9K h egocentric human video
- ~24.8K h synthesized human→robot data
- 15 embodiments

Source: https://qwen.ai/blog?id=qwen-robotmanip · https://arxiv.org/abs/2606.17846

But its central lesson is alignment before pooling.

Rethinking VLA Scaling shows naive embodiment mixing can cause negative transfer: https://arxiv.org/abs/2602.09722

Required future matrix:

```text
model scale × data mixture

small / medium / large
×
robot / human / sim / generated ratios
```

Keep total optimizer steps / tokens controlled where possible.

Do not assume a mixture optimized for 4B remains optimal for a large MoE.

---

### Q7 — Frozen VLM vs LoRA vs partial tune vs full tune: when is each best?

Current evidence says there is **no universal winner**.

- A real-robot π0 study finds some LoRA configurations match FFT, while freezing the VLM or restricting adaptation too aggressively degrades embodiment transfer: https://arxiv.org/abs/2607.10172
- Adaptive Capacity Allocation reports robotics PEFT can require larger/task-varying effective rank and can match/exceed full tuning on evaluated real tasks: https://arxiv.org/abs/2603.07404
- VLM2VLA demonstrates that data/action alignment plus LoRA can preserve foundational VLM capabilities better than naive robot fine-tuning: https://arxiv.org/abs/2509.22195
- Qwen-Drive provides a strong explicit alternative: reuse a pretrained multimodal backbone and add task-specific state/planning modules: https://qwen.ai/blog?id=qwen-drive-1.0

Future selection criteria:

```text
new embodiment gap
new visual domain
new task semantics
available data
forgetting tolerance
compute / memory budget
need to preserve general VLM capability
```

---

### Q8 — Should different modules use different learning rates / update frequencies?

**Yes, this deserves explicit experimentation.**

TEMPO is a direct 2026 example:

- pretrained VLM backbone frozen;
- semantic projection updated infrequently;
- low-level action expert updated frequently.

Paper: https://arxiv.org/abs/2608.07314

Its motivation is functional:

```text
semantic representation changes slowly
motor correction needs fast feedback
```

This should be generalized into experiments over:

```text
vision encoder LR
language/semantic LR
state/memory module LR
action expert LR
reward/value LR
world-model LR
```

The right timescale may differ across deployment regimes.

---

### Q9 — Should semantic representation and motor representation adapt at different speeds?

This is closely related to Q8 but is conceptually broader than choosing learning rates.

Evidence:

- TEMPO explicitly uses a two-timescale semantic/action post-training architecture: https://arxiv.org/abs/2608.07314
- Actions as Language shows aggressive robot adaptation can destroy higher-level semantic/multimodal capability: https://arxiv.org/abs/2509.22195
- VLA-OPD frames catastrophic forgetting and policy-distribution shift as separate problems in post-training: https://arxiv.org/abs/2603.26666

Future Clover hypothesis space should include:

```text
slow semantic/world representation
+
fast motor/action adaptation
```

but this remains a hypothesis, not a default architecture.

---

### Q10 — Can post-training worsen uncertainty calibration?

**Yes. Strong evidence exists in reasoning models; robot-specific evidence remains insufficient and should be collected.**

RLCR finds ordinary correctness-reward RL can actively degrade calibration and shows proper-scoring-rule rewards can counteract it: https://arxiv.org/abs/2507.16806

For embodied systems this creates a concrete Stage-1 gap:

```text
before post-training
vs after SFT
vs after RL
vs after distillation
vs after quantization
```

measure:

```text
ECE / Brier where meaningful
selective prediction
unknown-state detection
failure prediction
world-model confidence vs realized error
```

Do not assume higher task reward means better epistemics.

---

### Q11 — Can task success improve while permanence / memory / causal reasoning degrade?

**Yes, this is a credible and partly demonstrated form of capability forgetting, but direct robot-world-state benchmarks are still missing.**

- VLM2VLA starts from the observation that robot fine-tuning can reduce foundational reasoning/multimodal understanding: https://arxiv.org/abs/2509.22195
- LifeLong-RFT explicitly targets continual VLA adaptation where ordinary SFT is prone to catastrophic forgetting: https://arxiv.org/abs/2602.10503
- *What Should World Models Forget?* argues continual world models require separate tests for invariant knowledge vs instance facts that should change: https://arxiv.org/abs/2610.03713

Clover must therefore carry a **capability regression battery** through every post-training stage:

```text
task success
geometry
object permanence
memory revision
causal/counterfactual probes
uncertainty
OOD visual semantics
```

---

### Q12 — What is lost when distilling to a smaller model?

Task success alone is insufficient to answer this.

Current positive evidence:

- VLA-AD distills OpenVLA-7B into a 158M student using semantic guidance and reports near-teacher LIBERO task performance: https://arxiv.org/abs/2605.16241
- RT-VLA distills a larger driving VLA into a real-time student while preserving evaluated driving/reasoning capability: https://arxiv.org/abs/2606.14010
- World-model feature distillation into compact robot policies is an emerging route: https://arxiv.org/abs/2609.24682

Open question:

```text
what disappears first?
```

Candidate losses:

```text
rare-event behavior
uncertainty calibration
fine spatial precision
long-horizon memory
open-world semantics
causal sensitivity
recovery diversity
```

Future distillation evaluation must use a capability vector, not only teacher/student success gap.

---

### Q13 — Does a recipe that works at 4B scale to a large sparse MoE?

**Unknown by default. Never assume yes.**

Evidence:

- Rethinking VLA Scaling reports several seemingly reasonable data/regularization strategies do not improve consistently at scale: https://arxiv.org/abs/2602.09722
- DeepSeek scaling-law work historically treats hyperparameters themselves as scale dependent: https://arxiv.org/abs/2401.02954
- Modern DeepSeek/Qwen MoE models additionally introduce routing, active-parameter, communication and kernel effects absent from small dense models.

Required Clover protocol:

```text
4B discovery
→ 8B / 30B replication
→ sparse-MoE / remote counter-check
```

Record if the effect changes sign, disappears or requires a different LR/data mixture/objective weight.

---

### Q14 — In continual fleet learning, can one broken robot contaminate the fleet?

**Yes in principle, and update admission must be treated as a safety problem.**

Potential bad-client causes include:

```text
sensor/calibration fault
actuator damage
wrong embodiment metadata
corrupted memory
adversarial data
local environment regime shift
bad reward / human annotation
```

Relevant evidence:

- A 2026 federated VLA study shows that physical cross-site heterogeneity is substantial and studies federated update scope / aggregation / personalization: https://arxiv.org/abs/2609.22973
- *When Validation Stops Learning* studies update-admission rules for continual embodied agents and shows overly conservative gates can reject all useful learning while weak gates risk harmful updates: https://arxiv.org/abs/2609.10873
- Earlier federated embodied-agent work demonstrates that poisoned clients/data can steer embodied policies, motivating robust aggregation and client trust mechanisms.

Future fleet protocol should preserve:

```text
robot identity / hardware state
calibration version
data provenance
failure regime
local validation delta
update confidence
quarantine status
```

A fleet update should not be accepted merely because it improves the originating robot.

---

### Q15 — After model rollback, what happens to memory learned by the newer model?

This is a genuine unresolved stateful-system problem.

Weights and persistent world memory have different histories.

Example:

```text
model v12
→ operates / writes memory M12
→ update to v13
→ writes M13 using different representation / policy
→ v13 regresses
→ rollback weights to v12
```

Questions:

```text
Can v12 read M13?
Was M13 derived through a behavior later judged unsafe?
Should raw evidence survive while derived beliefs are re-encoded?
Which memories depend on v13-specific latent semantics?
What should be quarantined or invalidated?
```

Adjacent 2026 agent-memory research provides useful mechanisms but not yet a robot-specific solution:

- ChronoMem introduces version control and semantic rollback for long-term agent memory: https://arxiv.org/abs/2607.27773
- TRACE studies admission of stale vs still-valid memory after system/world evolution: https://arxiv.org/abs/2609.33517
- Crab / Planarian study consistent checkpoint/restore of stateful agent environments and the hazards of rollback across external side effects: https://arxiv.org/abs/2604.28138 · https://arxiv.org/abs/2609.35366

A future Clover memory design should distinguish at least:

```text
raw evidence
versioned derived belief
model/checkpoint that created belief
belief dependencies
current validity status
```

Prefer re-deriving beliefs from preserved evidence after rollback over blindly restoring incompatible latent state.

---

### Required post-training report card

Every serious Clover post-training experiment should eventually produce a before/after vector:

```text
Task
Nominal
OOD
Partial progress
Failure recovery
Safety
Epistemic calibration
Unknown/refusal
Physical prediction
Object permanence
Memory revision
Causal/counterfactual
Long-horizon reliability
Latency
Memory
Energy
Forgetting / retained general capability
```

and record:

```text
exact checkpoint
training stages + order
data mixture + provenance
failure/recovery ratio
reward components
on/off-policy regime
world-model confidence usage
frozen / adapted modules
module learning rates / update frequencies
action horizon
precision / quantization
checkpoint-selection criterion
rollback / memory version
```

---

### Current conclusion

The remaining post-training questions are not mainly about inventing another optimizer.

They are about **credit assignment, evidence quality, distribution control, trust calibration, capability preservation and state lifecycle**.

That is the level at which Clover should compare robot post-training methods in Stage 2.

---

<a id="topic-docs-research-map-data-and-experience"></a>

## Data, Experience and Interaction

### Core question

> **What kinds of experience are actually required for a machine to build a world model from vision?**

The modern robotics literature suggests that data source is part of the algorithmic question, not merely an engineering detail.

### Passive video

Strengths:

- enormous diversity;
- natural human/object/environment interactions;
- cheap relative to robot data;
- useful for learning visual and temporal regularities.

Limitation:

The model often does not know the agent's exact action/intervention, so some causal variables are not identifiable.

V-JEPA 2 is an important case: large-scale action-free video pretraining is followed by comparatively small action-conditioned robot post-training.

### Human egocentric video

Strengths:

- first-person viewpoint;
- long natural task sequences;
- dense hand-object interactions;
- scalable collection.

Limitations:

- human morphology differs from robots;
- action/force/proprioceptive signals may be absent;
- language narration can introduce non-visual supervision.

Ego4D and recent robot-foundation-model efforts make this a major research direction.

### Robot demonstrations / teleoperation

Strengths:

- explicit actions and consequences;
- robot embodiment matched to deployment;
- direct control supervision.

Limitations:

- expensive;
- limited environment diversity;
- often biased toward successful demonstrations.

DROID and Open X-Embodiment are important public resources.

### Simulation

Strengths:

- unlimited interventions;
- exact world state;
- controlled counterfactuals;
- scalable self-play / exploration.

Limitations:

- sim-to-real gap;
- simulator assumptions can become hidden supervision;
- visual realism is not equivalent to physical realism.

### Self-generated interaction

Self-play and autonomous exploration add a different source of evidence: the model can choose interventions specifically to reveal dynamics or improve skills.

For Clover this may connect directly to active perception and causal identification.

### Working hypothesis

A general robot brain may eventually require a curriculum combining:

```text
passive visual observation
+ egocentric human experience
+ robot action/consequence data
+ simulation/intervention
+ autonomous exploration
```

This is a research hypothesis. The contribution of each source should be measured rather than assumed.

---

<a id="topic-docs-research-map-lifelong-learning"></a>

## Lifelong Learning and World Growth

### Core question

> **Can a robot's understanding of the world improve continuously from experience without periodically rebuilding the entire model?**

A general robot brain cannot remain permanently frozen after offline training. It must acquire new entities, dynamics, places and task regularities while correcting earlier beliefs.

### Relevant fields

- continual learning;
- catastrophic forgetting;
- experience replay;
- online adaptation;
- lifelong robot learning;
- memory consolidation;
- open-world recognition;
- ontology/type discovery.

### LIBERO

LIBERO is a benchmark for lifelong robot learning focused on knowledge transfer. Its purpose is not pure visual world understanding, but it provides a mature framework for asking whether previously learned skills and knowledge help or interfere with later tasks.

Primary source:

- https://libero-project.github.io/main.html

### Clover's stronger requirement

Skill retention alone is not enough. A persistent worldview should support:

```text
new evidence
→ revise belief
→ preserve unaffected knowledge
→ invalidate affected claims
→ consolidate stable structure
→ forget detail without losing provenance
```

### Types of growth to study

- **Add** — new entity/type/relation/model;
- **Merge** — previously separate concepts become equivalent;
- **Split** — one category separates into different dynamics/affordances;
- **Revise** — later evidence changes an earlier belief;
- **Retire** — obsolete hypothesis no longer influences current authority;
- **Forget** — remove unnecessary high-resolution history;
- **Consolidate** — replace repeated evidence with a stable reusable model.

These operations are research requirements, not claims that the current public repository already implements them.

### Open questions

1. What should remain plastic during deployment?
2. How can a system distinguish new knowledge from transient noise?
3. What memories must be retained to allow later reinterpretation?
4. Can a model grow its ontology without human category labels?
5. How do we prevent self-training errors from becoming authoritative world facts?
6. What does a 24-hour or 7-day persistent robot worldview look like computationally?

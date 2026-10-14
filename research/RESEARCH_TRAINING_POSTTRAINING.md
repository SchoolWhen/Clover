# Stage 1 — Training, Post-Training and Embodied Learning Regimes

Last updated: **2026-10-15**  
Freshness cutoff checked through: **2026-10-15**

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

## 1. Keep model architecture separate from training regime

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

## 2. A useful training-regime taxonomy

### TR0 — base pretraining

Examples:

```text
next-token prediction
masked / predictive representation learning
vision-language pretraining
video prediction
world-model prediction
```

Question: what broad prior is acquired before task-specific robot supervision?

### TR1 — continued / domain-adaptive pretraining

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

### TR2 — supervised post-training / behavior cloning

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

### TR3 — co-training / auxiliary-objective training

Examples:

```text
VLM + VLA co-training
language supervision + actions
future latent prediction + actions
geometry / depth / pose auxiliaries
world-model + policy joint objectives
```

These signals can change representation quality even when architecture stays fixed.

### TR4 — preference / conservative offline alignment

Examples include:

```text
preference optimization
sample reweighting
quality filtering
posterior / transition attribution
```

Useful when recorded data contain conflicting or suboptimal supervision.

### TR5 — reinforcement learning with verifiable or learned rewards

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

### TR6 — online embodied reinforcement learning

The current policy acts, changes the world, and learns from its own state distribution.

This can correct covariate shift but is expensive, safety-sensitive and reset-limited in the real world.

### TR7 — on-policy distillation / teacher-guided self-generated trajectories

The student visits states induced by its own policy while a teacher supplies denser supervision.

This can bridge offline SFT and expensive sparse-reward RL, but teacher errors and epistemic uncertainty become part of the evidence chain.

### TR8 — strong-to-weak / model distillation

Transfer capability from a larger teacher into a smaller model.

Important question for Clover:

```text
what survives distillation?
```

Measure not only task accuracy but memory, uncertainty, persistence, physical reasoning and rare-event behavior.

### TR9 — simulated / world-model post-training

Use a simulator or learned world model for exploration, RL or rehearsal.

Important distinction:

```text
learning to exploit simulator/world-model errors
≠ learning correct real-world behavior
```

### TR10 — deployment-rollout learning / self-improvement

Use successful, failed and suboptimal deployment trajectories for further training.

This includes failure mining, active data collection and repeated deployment→training cycles.

### TR11 — continual / test-time adaptation

Update after deployment as environment, robot body, sensors or task distribution changes.

Must be evaluated together with forgetting, rollback and persistent-state compatibility.

These labels are bookkeeping tools, not a Clover training plan.

---

## 3. General LLM / VLM post-training: current lessons

### DeepSeek-R1 — RL can create capability, but raw RL has behavioral failure modes

Primary paper: https://arxiv.org/abs/2501.12948  
Official code: https://github.com/deepseek-ai/DeepSeek-R1

DeepSeek-R1-Zero applies large-scale RL directly to a base model without preliminary SFT and reports emergent reasoning behavior. The same line also reports practical problems such as repetition, poor readability and language mixing. DeepSeek-R1 introduces cold-start data and multi-stage training before/around RL.

Stage-1 lesson:

```text
RL can improve a target capability
without automatically producing desirable overall behavior.
```

The initialization / cold-start distribution matters.

### DeepSeek-V4.1-Flash — data-pipeline changes can dominate algorithmic changes

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

### Qwen3 — staged post-training deliberately installs different behavior modes

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

### Qwen3-VL — multimodal post-training must preserve perception while improving reasoning

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

## 4. Robot training is only partially analogous to LLM post-training

Common high-level structure:

```text
large general prior
→ specialization
→ feedback / correction
→ deployment
```

But the learning problem is materially different.

### Language-model output

```text
token
```

An incorrect token usually does not physically alter the next input distribution.

### Robot-policy output

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

## 5. Major robot-policy training families

### 5.1 Behavior cloning / imitation learning

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

### 5.2 Action representation and decoding objective are training variables

OpenVLA-OFT: https://arxiv.org/abs/2502.19645

Under an OpenVLA backbone, changing fine-tuning design — parallel decoding, action chunking, continuous actions and an L1 objective — materially changes both task success and inference speed.

Stage-1 lesson:

```text
backbone quality
≠ downstream policy quality
```

Action representation and decoding loss can dominate adaptation.

### 5.3 Flow / diffusion action experts

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

### 5.4 Cross-embodiment co-training requires alignment

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

### 5.5 Human-video / latent-action pretraining

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

### 5.6 Synthetic-data / simulation pretraining

NVIDIA GR00T N1 / N1.7 uses mixtures of human/egocentric, synthetic/simulation and real robot data.

Official training overview: https://developer.nvidia.com/blog/accelerate-generalist-humanoid-robot-development-with-nvidia-isaac-gr00t-n1/  
N1.7 overview: https://developer.nvidia.com/blog/develop-humanoid-robot-policies-end-to-end-with-nvidia-isaac-gr00t/

N1.7 is reported as pretrained on roughly 32K hours of real demonstration/human egocentric data plus roughly 8K hours of simulated rollouts/demonstrations, followed by robot-specific post-training workflows.

Important question:

> Which gains come from data quantity, which from embodiment alignment, and which from simulator-specific structure?

### 5.7 Offline post-training on heterogeneous robot data

Posterior-Transition Reweighting: https://arxiv.org/abs/2603.16542

This work treats recorded robot demonstrations as unequal supervision and reweights samples according to how attributable the observed post-action consequence is under the current representation.

Ambient Diffusion Policy: https://arxiv.org/abs/2606.12365

This work studies how suboptimal data should contribute differently at different diffusion noise levels.

Stage-1 lesson:

```text
all demonstrations equally weighted
```

is itself a training assumption.

### 5.8 Online RL post-training

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

### 5.9 On-policy distillation as a bridge between SFT and RL

VLA-OPD: https://arxiv.org/abs/2603.26666

The student visits states generated by its own policy while an expert teacher gives dense supervision. The paper explicitly frames the problem as a trade-off:

```text
offline SFT
→ efficient but distribution-shift / forgetting risk

online RL
→ on-policy but sparse-reward / sample-efficiency problems
```

On-policy distillation tries to combine on-policy state coverage with dense teacher signals.

### 5.10 Simulated / world-model RL post-training

RehearseVLA: https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_RehearseVLA_Simulated_Post-Training_for_VLAs_with_Physically-Consistent_World_Model_CVPR_2026_paper.html

The method performs RL-style post-training inside a learned physical world simulator to avoid expensive/non-resettable real interaction.

Important danger:

```text
world-model bias
→ reward / exploration bias
→ policy learns simulator artifact
```

This must be followed by EV3–EV8 evidence rather than treated as real-world RL.

### 5.11 Deployment self-improvement / failure learning

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

## 6. Controlled evidence that training objective changes representation

### VLAFlow

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

## 7. Post-training can improve one capability while damaging another

Track at least these failure modes:

### PT-F1 — catastrophic forgetting

Task/robot fine-tuning erases broad pretrained semantic or physical capability.

### PT-F2 — reward overoptimization / reward hacking

RL improves the training reward without improving the intended real-world capability.

### PT-F3 — perception-reasoning interference

Reasoning tuning improves inference but weakens visual perception or grounding.

### PT-F4 — action-mode collapse

Fine-tuning narrows a useful multimodal action distribution into one brittle strategy.

### PT-F5 — unsafe exploration

Online RL visits dangerous or irreversible states.

### PT-F6 — simulator exploitation

World-model/simulator post-training discovers artifacts rather than real physics.

### PT-F7 — embodiment over-specialization

Target-robot fine-tuning reduces cross-embodiment transfer.

### PT-F8 — calibration loss

Post-training produces more confident behavior without better epistemic calibration.

### PT-F9 — memory / state regression

Task success improves while persistence, belief revision or long-horizon world state degrades.

### PT-F10 — deployment-data feedback bias

Self-training increasingly samples states created by the current policy and can reinforce blind spots.

---

## 8. Required training provenance for future Clover comparisons

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

## 9. A useful controlled training-ablation matrix for Clover

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

## 10. Mac mini M4 implication

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

## 11. Current open questions

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

## 12. Stage-2 analysis priority created by this surface

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

## Final rule

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
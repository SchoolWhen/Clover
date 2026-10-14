# Training / Post-Training — High-Risk Boundary Questions

Last updated: **2026-10-15**  
Freshness cutoff checked through: **2026-10-15**

> Supporting material for [`../RESEARCH_TRAINING_POSTTRAINING.md`](../RESEARCH_TRAINING_POSTTRAINING.md).

These questions are high-risk because optimizing one headline metric can silently damage other properties of a robotic world model or policy.

Current rule:

```text
task success ↑
does not imply
world understanding / calibration / memory / recovery / safety ↑
```

For every question below, the goal is to record what is known, what is still open, and what Clover should measure later.

---

## Q1 — How should a reward represent partial success?

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

## Q2 — Should reward explicitly encourage epistemic correctness, not only task success?

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

## Q3 — What fraction of training data should be failure trajectories?

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

## Q4 — Can recovery data damage the nominal policy?

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

## Q5 — How should world-model confidence control imagined rollout length?

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

## Q6 — Does the optimal human-video / simulator / robot-data mixture depend on model scale?

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

## Q7 — Frozen VLM vs LoRA vs partial tune vs full tune: when is each best?

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

## Q8 — Should different modules use different learning rates / update frequencies?

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

## Q9 — Should semantic representation and motor representation adapt at different speeds?

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

## Q10 — Can post-training worsen uncertainty calibration?

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

## Q11 — Can task success improve while permanence / memory / causal reasoning degrade?

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

## Q12 — What is lost when distilling to a smaller model?

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

## Q13 — Does a recipe that works at 4B scale to a large sparse MoE?

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

## Q14 — In continual fleet learning, can one broken robot contaminate the fleet?

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

## Q15 — After model rollback, what happens to memory learned by the newer model?

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

# Required post-training report card

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

# Current conclusion

The remaining post-training questions are not mainly about inventing another optimizer.

They are about **credit assignment, evidence quality, distribution control, trust calibration, capability preservation and state lifecycle**.

That is the level at which Clover should compare robot post-training methods in Stage 2.

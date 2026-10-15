# Stage-1 Emerging Audit — Physical Security, Whole-Body State and Multi-Agent World Models

Last updated: **2026-10-15**  
Freshness cutoff checked through: **2026-10-15**

> Mother question: **How can a machine understand the real world through vision alone?**

This is supporting Stage-1 material. It does not create a new Clover lifecycle stage or promote any current method into Innovation.

This audit covers four cross-boundaries that remained underweighted after the Embodied-JEPA / RSI re-audit:

```text
physical-world adversarial robustness / visual prompt injection
whole-body humanoid predictive state and balance-aware control
multi-robot / shared-intention world models
action competence that can arise from non-visual priors
```

---

## 1. Physical-world adversarial robustness is a first-class embodied failure mode

### Universal Adversarial Objects for VLA policies

Paper: https://arxiv.org/abs/2609.39178  
Evidence: `PRIMARY_PAPER`

The work optimizes the texture of a physical object placed inside the robot's field of view and reports large task-success degradation for evaluated VLA policies in simulation and real-world settings.

Stage-1 implication:

```text
ordinary visual OOD
≠
adversarially chosen visual evidence
```

and:

```text
clean-scene robustness
≠
physical-world adversarial robustness
```

A persistent world model may amplify the risk if one poisoned observation is converted into a long-lived state or memory.

### Physical prompt injection through visible text

Paper: https://arxiv.org/abs/2608.05715  
Evidence: `PRIMARY_PAPER`

This work studies human-readable adversarial text physically placed in the robot scene. The attack targets the VLM planner through the visual channel rather than through the user's explicit instruction channel.

Important distinction:

```text
scene text as world evidence
≠
scene text as trusted instruction
```

For Clover, any future visual-language interface should preserve provenance:

```text
user instruction
observed scene text
retrieved memory
system policy
```

must not collapse into one undifferentiated prompt stream.

### Additional security references

- Partially Observable Adversarial Patch Attacks on VLAs — https://arxiv.org/abs/2606.03556
- TrustVLA — https://arxiv.org/abs/2607.12571
- Hidden in Plain Sight / DURA — https://arxiv.org/abs/2608.10393
- Trajectory-Level Redirection Attacks — https://arxiv.org/abs/2606.12978
- VLA Safety survey — https://arxiv.org/abs/2604.23775

Research questions:

```text
Can visual attacks poison persistent world state after the trigger disappears?
Can contradiction/evidence revision remove poisoned beliefs?
Can runtime monitors distinguish adversarial evidence from ordinary scene change?
Does quantization/token pruning make attack sensitivity better or worse?
Can a safety layer remain effective if the world-state representation is already compromised?
```

---

## 2. Whole-body humanoid control makes body state impossible to treat as a side channel

### World-Model-Augmented Visual Locomotion

Paper: https://arxiv.org/abs/2609.02542  
Evidence: `PRIMARY_PAPER`

The reported system combines a recurrent predictive feature with PPO for humanoid foothold-constrained locomotion and deploys on a physical Unitree G1.

Its provenance is important:

```text
onboard depth
+
proprioception
+
learned recurrent world model
```

so it is **not** a V0 vision-only result.

Scientific lesson:

```text
external terrain state
+
body configuration / momentum / balance state
```

must be jointly sufficient for whole-body action.

### ω-0 — latent predictive whole-body WAM

Paper: https://arxiv.org/abs/2608.06375  
Evidence: `PRIMARY_PAPER`

ω-0 couples compact future observation embeddings with whole-body action latents for concurrent locomotion and manipulation.

Stage-1 relevance:

```text
arm manipulation state
≠
whole-body loco-manipulation state
```

because balance, base motion, posture and contact transitions can make the same object-level plan executable or impossible.

### MetaWorld-X

Paper: https://arxiv.org/abs/2603.08572  
Evidence: `PRIMARY_PAPER`

This provides a hierarchical counter-hypothesis in which VLM-level orchestration coordinates specialized whole-body experts instead of relying on one monolithic end-to-end controller.

Future comparison axis:

```text
single unified whole-body policy
vs
predictive whole-body world/action model
vs
hierarchical expert orchestration
```

---

## 3. Multi-robot systems add shared-intention state and communication assumptions

### Sequential World Model for multi-robot cooperation

Paper: https://arxiv.org/abs/2509.13095  
ICLR 2026 paper page: https://proceedings.iclr.cc/paper_files/paper/2026/hash/16415eed5a0a121bfce79924db05d3fe-Abstract-Conference.html  
Code: https://github.com/zhaozijie2022/seqwm  
Evidence: `PRIMARY_PAPER` / `OPEN_SOURCE`

SeqWM models agents sequentially and shares predicted intentions across agents instead of building one monolithic joint-dynamics model.

This exposes a new decomposition:

```text
private local state
shared world state
predicted teammate intention
communication channel
communication delay / loss
```

Multi-agent success therefore does not only test world representation; it also tests what state is communicated, when it becomes stale and whether other agents' intentions are modeled correctly.

Do not infer that multi-robot intent is visually identifiable. The evaluated systems use explicit coordination information and robot state beyond passive RGB.

Future Clover question:

> If multiple robots share one persistent world model, what evidence is local, what belief is shared, and how are contradictions/provenance resolved across agents?

---

## 4. Action competence can come from non-visual priors

### LA4VLA — language-action pretraining without vision

Paper: https://arxiv.org/abs/2606.27295  
Evidence: `PRIMARY_PAPER`

LA4VLA deliberately learns language-conditioned action priors without visual observations before visual robot fine-tuning.

This is a useful attribution counterexample:

```text
robot succeeds from RGB at deployment
≠
robot learned the relevant behavior from visual evidence
```

Action competence can be injected through:

```text
language-action pretraining
robot demonstrations
human priors
simulator state
teacher policy / distillation
```

Therefore Stage-2 reports must preserve the learning-provenance labels `L0–L4` and must not use deployment modality alone to infer where knowledge originated.

---

## 5. New comparison axes

Add as cross-boundary axes, not lifecycle stages:

```text
B-ADV    natural OOD vs adversarial visual evidence / prompt injection
B-BELIEF clean current frame vs persistent poisoned state
B-WHOLE  external object state vs whole-body balance/contact state
B-MULTI  private belief vs shared belief vs teammate-intention model
B-COMM   local inference vs communication-dependent coordination
B-ATTR   deployment input modality vs training-origin of competence
```

---

## 6. Does this reveal a missing foundational domain?

No new top-level Stage-1 surface is required.

These findings land in existing surfaces:

```text
Observation Physics / visual evidence integrity
Open-World Epistemics / uncertainty / belief revision
State Variables / self-body schema
Adaptive Abstraction / embodiment
Training / Post-Training provenance
Engineering / runtime safety
Social / multi-agent hidden state
Frontier
```

But they tighten future evaluation requirements:

```text
clean success
adversarial success
whole-body stability
communication robustness
provenance-correct attribution
persistent-state recovery after corruption
```

should be reported separately when relevant.

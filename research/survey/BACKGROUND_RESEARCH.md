# Background Research Foundation

Last updated: 2026-10-14  
Phase: **Background Research / Problem Reconstruction**

> **Research question:** How can a machine understand the real world through vision alone?
>
> **Long-term goal:** Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.

This document is the problem-space foundation for Clover after the 2026-10-14 Research Reset. It does **not** propose the next Clover architecture. It reconstructs what must be understood before a representation hypothesis is allowed to become a design commitment.

The operative sequence is:

```text
Background Research / Research Map
→ Baseline Setup
→ Understanding Battery
→ Failure Matrix
→ Representation Hypothesis
→ World Formation / Learning
→ Robot Brain
→ Real-world evaluation
→ Hardware co-design
```

Historical Clover mechanisms — field crystallization, CSP, SEP, licences, LCPS/GCPS, Visual World Compiler, CPU-first computation and related machinery — remain candidate hypotheses only.

---

## 1. Problem formulation

A camera does not observe the physical world state directly. It observes an image produced by the interaction of world state, viewpoint, visibility, lighting and sensor characteristics.

A useful abstraction is:

```text
hidden physical state S_t
+ camera/view state C_t
+ visibility/lighting/sensor process
→ visual observation O_t
```

A vision-based machine receives a history:

```text
O_1, O_2, ... O_t
```

and must construct some internal state `Z_t` that is sufficient for future queries and action.

The research problem is therefore not merely image recognition. It is:

> **What internal structure, learned or constructed from visual experience, is sufficient to support stable state estimation, identity, persistence, space, time, physics, causality, uncertainty, prediction, active evidence acquisition and action?**

This immediately makes the problem a partially observed inverse problem rather than a direct pixels→truth mapping.

Important background:

- POMDPs formalize decision-making when the real state is not directly observable: https://arxiv.org/abs/2209.10342
- Probabilistic Robotics formalizes state estimation, uncertainty, localization and mapping: https://mitpress.mit.edu/9780262201629/probabilistic-robotics/
- Active perception treats sensing as an action-selection problem rather than passive data intake: https://ieeexplore.ieee.org/abstract/document/5968

### Core implication

```text
pixels ≠ unique world state
```

A serious world-understanding system must therefore represent some combination of:

```text
observed
inferred
predicted
ambiguous
unobserved
contradicted
```

without silently treating plausible completion as measured fact.

---

## 2. “Vision alone” needs two independent labels

The existing V0–V3 protocol describes **what sensory evidence is available at inference/evaluation time**.

### Observation protocol

- **V0 — Strict monocular vision:** RGB + temporal order/timestamps only.
- **V1 — Calibrated monocular vision:** V0 + declared intrinsics.
- **V2 — Multi-camera vision:** calibrated RGB from multiple cameras.
- **V3 — Embodied active vision:** the agent may move to obtain new visual evidence; sensory evidence remains visual.

However, modern models may use language, robot demonstrations, proprioception or privileged simulator state during pretraining. Deployment-time visual input alone does not prove the representation was learned from vision alone.

Therefore background research should also annotate a second, orthogonal axis.

### Learning-evidence provenance (proposed research annotation)

- **L0 — visual self-supervision only:** images/video without semantic labels or non-visual supervision.
- **L1 — visual supervision:** human labels, masks, tracks, geometry labels or other annotations derived for vision tasks.
- **L2 — language/world-knowledge supervision:** captions, text corpora, VLM pretraining, semantic internet supervision.
- **L3 — action-conditioned experience:** robot demonstrations, action labels, teleoperation, action-conditioned video.
- **L4 — non-visual/privileged physical evidence:** proprioception, force/tactile, IMU, depth/LiDAR, simulator state or equivalent privileged variables.

These are annotations, not a hierarchy of quality. They prevent a major confound:

```text
visual input at deployment
≠
knowledge learned only from vision
```

A Clover result should report both axes when relevant, for example `V0/L0`, `V1/L3`, or `V3/L3`.

---

## 3. Research domain A — classical geometry and state estimation

Before asking a neural model to “understand space,” Clover must understand what projective geometry already solves exactly or approximately.

### Key sources

- Multiple-view geometry foundations: https://www.robots.ox.ac.uk/~vgg/hzbook/
- ORB-SLAM3 paper: https://arxiv.org/abs/2007.11898
- ORB-SLAM3 code: https://github.com/UZ-SLAMLab/ORB_SLAM3
- RAFT optical flow: https://arxiv.org/abs/2003.12039
- RAFT code: https://github.com/princeton-vl/RAFT

### What this route demonstrates

Classical/optimization-based vision can produce explicit, inspectable variables such as:

```text
camera pose
trajectory
correspondence
multi-view geometry
map structure
relocalization
uncertainty/state estimates
```

### What it does not establish

It does not by itself solve:

```text
open-world semantics
persistent object identity under arbitrary occlusion
physical dynamics
causal structure
counterfactual reasoning
long-horizon task state
```

### Clover question

> Which geometric invariants should remain explicit because mathematics already gives them strong structure, and which variables should instead be learned from data?

---

## 4. Research domain B — static self-supervised visual representation

The question here is what large-scale visual experience can provide before explicit temporal/world modeling is introduced.

### DINOv3

- Meta research page: https://ai.meta.com/research/publications/dinov3/
- Project page: https://ai.meta.com/research/dinov3/
- Paper: https://arxiv.org/abs/2508.10104
- Code: https://github.com/facebookresearch/dinov3

DINOv3 scales label-free image self-supervision to 7B-parameter models and 1.7B images and produces strong frozen dense features for detection, segmentation, depth and related tasks.

### Research significance

DINOv3 should replace DINOv2 as the primary current static SSL baseline in the Survey, while DINOv2 remains historically important.

### Clover question

> If a static visual representation already gives strong object/part/depth structure, what world-understanding capabilities specifically require persistent temporal state rather than a stronger image encoder?

---

## 5. Research domain C — predictive video representation

### V-JEPA 2

- Meta research page: https://ai.meta.com/research/publications/v-jepa-2-self-supervised-video-models-enable-understanding-prediction-and-planning/
- Paper: https://arxiv.org/abs/2506.09985
- Code: https://github.com/facebookresearch/vjepa2

V-JEPA 2 pretrains from more than one million hours of internet video and then uses less than 62 hours of robot video for action-conditioned post-training and zero-shot image-goal planning.

### V-JEPA 2.1

- Paper: https://arxiv.org/abs/2603.14482

V-JEPA 2.1 strengthens dense, spatially structured and temporally consistent features and reports gains in anticipation, navigation, depth and robot grasping.

### Mechanistic evidence

- Interpreting Physics in Video World Models: https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/

This work reports that speed, acceleration and direction become decodable across video-model depth, with motion direction represented as a high-dimensional population code rather than a tiny set of compact “physics neurons.”

### Clover implication

This is a direct counter-hypothesis to any claim that useful physical understanding must be represented as a compact hand-designed explicit variable set.

The correct comparison is empirical:

```text
explicit/factorized state
vs
distributed predictive latent
vs
hybrid/identifiable latent
```

---

## 6. Research domain D — learned geometry and spatial reconstruction

### VGGT / VGGT-Ω

- VGGT paper: https://arxiv.org/abs/2503.11651
- VGGT code: https://github.com/facebookresearch/vggt
- VGGT-Ω paper: https://arxiv.org/abs/2605.15195
- VGGT-Ω project: https://vggt-omega.github.io/
- VGGT-Ω code: https://github.com/facebookresearch/vggt-omega

VGGT-family models show that feed-forward learned reconstruction can recover cameras, depth, point maps and tracks at foundation-model scale. VGGT-Ω extends this toward larger-scale static and dynamic reconstruction and reports that learned scene registers can improve VLA models and language alignment.

### Central hypothesis to test

> **Can reconstruction be a scalable proxy task for spatial understanding?**

This is important but must not be silently upgraded to:

```text
reconstruction = world understanding
```

Spatial reconstruction still leaves open memory, observability, physics, causal structure and action relevance.

---

## 7. Research domain E — objects, entities and visible tracking

Object-centric representations are one possible answer to compositionality and identity, but not the only one.

### Key sources

- Slot Attention: https://proceedings.neurips.cc/paper/2020/hash/8511df98c02ab60aea1b2356c013bc0f-Abstract.html
- PLATO / object-centric intuitive physics: https://www.nature.com/articles/s41562-022-01394-8
- SAM 3 research: https://ai.meta.com/research/publications/sam-3-segment-anything-with-concepts/
- SAM 3 / 3.1 code: https://github.com/facebookresearch/sam3
- SAM 3.1 release notes: https://github.com/facebookresearch/sam3/blob/main/RELEASE_SAM3p1.md

SAM 3.1 is the current relevant open-vocabulary video detection/segmentation/tracking baseline. It should replace SAM 2 as the primary contemporary visible-entity baseline, while SAM 2 remains an architectural predecessor.

### Important distinction

```text
visible tracking
≠
object permanence
```

Tracking an object while it is observed does not prove the model maintains a world-state hypothesis after it leaves the field of view.

---

## 8. Research domain F — persistent visual memory

This domain must be first-class because world understanding requires maintaining facts beyond the current view.

### PersistBench

- Paper: https://arxiv.org/abs/2609.20819
- Project/code: https://guangzhaohe.com/persistbench

PersistBench uses 360° video as omniscient reference and evaluates object permanence, motion continuity and appearance preservation after objects leave the normal field of view. Current 4D/world models degrade substantially once objects disappear from view.

Its central lesson is:

> **Seeing is not remembering.**

### S-EMBER

- Meta research page: https://ai.meta.com/research/publications/s-ember-a-large-scale-benchmark-for-streaming-egocentric-memory-retrieval/
- Paper: https://arxiv.org/abs/2607.02689

S-EMBER evaluates grounded episodic retrieval in a causal streaming setting rather than giving the model an entire offline video file. It exposes a gap between semantic answer quality and precise temporal grounding.

### VISTA

- Paper: https://arxiv.org/abs/2610.02200

VISTA is relevant because it isolates memory/evidence organization from base-model weights, making the memory harness itself a research variable.

### Clover questions

```text
What must be remembered?
raw visual evidence?
compressed world state?
episodic events?
object state?
task state?
which information can be forgotten safely?
```

Evidence Replay remains one candidate answer, not a commitment.

---

## 9. Research domain G — intuitive physics and physical variables

Clover needs to distinguish at least three levels:

```text
visual plausibility
→ predictive physical regularity
→ quantitative/action-relevant physical state
```

### Core benchmarks and sources

- IntPhys 2: https://ai.meta.com/research/publications/intphys-2-benchmarking-intuitive-physics-understanding-in-complex-synthetic-environments/
- IntPhys 2 code: https://github.com/facebookresearch/IntPhys2
- MVP / Minimal Video Pairs: https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/
- Principia: https://arxiv.org/abs/2609.04200
- Interpreting Physics in Video World Models: https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/

IntPhys 2 evaluates permanence, immutability, spatiotemporal continuity and solidity. MVP tests whether apparent physical reasoning survives minimal-pair shortcut controls. Principia evaluates relational Newtonian consistency without requiring absolute camera calibration.

### Cognitive-science anchors

- Spelke et al., Origins of Knowledge: https://pubmed.ncbi.nlm.nih.gov/1454901/
- Review of early object/physics knowledge: https://pubmed.ncbi.nlm.nih.gov/26302470/

These sources motivate continuity, solidity, persistence and object structure as useful research dimensions, not as a requirement that Clover copy human infant representations.

### Epistemic boundary

Some quantities can be visually estimated from learned priors but are not directly measured by RGB. Exact force, friction, internal material parameters and hidden geometry should not automatically be treated as observations.

---

## 10. Research domain H — causality and counterfactuals

Prediction alone does not imply causal identification.

### Sources

- CausalVQA: https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/
- General identifiability and achievability for causal representation learning: https://proceedings.mlr.press/v238/varici24a.html
- Identifying linearly mixed causal representations from multi-node interventions: https://proceedings.mlr.press/v236/bing24a

Interventional causal-representation work shows why observational video alone may leave multiple causal explanations compatible with the same data unless additional structural assumptions or interventions are available.

### Clover implication

V3 active vision/action is scientifically important because action can create new visual evidence:

```text
current belief
→ action/intervention
→ changed world
→ new visual evidence
→ revised causal hypothesis
```

This still respects vision as the sensory evidence channel.

Counter-Witness First Causality remains a Clover hypothesis to compare against ordinary learned dynamics and causal-representation baselines.

---

## 11. Research domain I — generative world models

A different answer to “world model” is a model that can generate or simulate plausible futures rather than expose a persistent queryable state.

### World Labs Atlas

- Official technical overview: https://www.worldlabs.ai/blog/atlas
- Functional taxonomy of world models: https://www.worldlabs.ai/blog/taxonomy-of-world-models

Atlas unifies generation, reconstruction and space-time simulation inside a spatially grounded multimodal model.

### NVIDIA Cosmos 3

- Official project: https://research.nvidia.com/labs/cosmos-lab/cosmos3/
- Technical report: https://arxiv.org/abs/2606.02800
- Code: https://github.com/nvidia/cosmos

Cosmos 3 jointly processes/generates language, image, video, audio and action sequences and explicitly collapses boundaries between VLMs, video generators, simulators and world-action models.

### Fundamental Clover distinction

```text
plausible hidden completion
≠
observed fact
≠
evidence-supported belief
```

Atlas can intentionally imagine unseen parts of a world. That is useful for generation and simulation, but a robot world state needs to know which parts are observed, inferred or merely plausible.

---

## 12. Research domain J — VLM/VLA and robot foundation models

These systems are the strongest falsifiers of the claim that explicit persistent world state is obviously required.

### Open VLA baseline

- OpenVLA paper: https://arxiv.org/abs/2406.09246
- Code: https://github.com/openvla/openvla

### π0.5

- Paper: https://arxiv.org/abs/2504.16054
- Project/blog: https://www.pi.website/blog/pi05

π0.5 combines image observations, language, semantic subtasks, object detections and low-level actions and demonstrates long-horizon manipulation in unseen homes.

### Gemini Robotics ER 2 / Robotics 2

- ER 2 overview: https://deepmind.google/models/gemini-robotics/embodied-reasoning/
- ER 2 model card: https://deepmind.google/models/model-cards/gemini-robotics-er-2/
- Robotics 2 overview: https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/

Gemini Robotics ER 2 explicitly separates a high-level embodied reasoning model from lower-level VLA execution. This is evidence that hierarchical reasoning/action remains competitive; it does not establish that Clover's historical hierarchy is correct.

### Figure Helix 2.5

- Official report: https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization

Figure reports zero-shot whole-body autonomy across 30 unseen homes and a controlled pretraining comparison from 9% to 56% success. Treat this as `OFFICIAL_REPORTED_RESULT`, not independently reproduced science.

### Skild S1

- Official report: https://www.skild.ai/blogs/s1
- General-purpose brain overview: https://skild.ai/blogs/building-the-general-purpose-robotic-brain

Skild reports in-context robot task learning from video demonstrations and unseen long-horizon tasks. Also `OFFICIAL_REPORTED_RESULT` unless independently reproduced.

### Core experiment eventually required

```text
strong direct/implicit policy
vs
matched strong policy + persistent world representation
```

If the explicit worldview does not improve generalization, planning cost, recovery, sample efficiency, unjustified-action rate or long-horizon success, its necessity is not established.

---

## 13. Research domain K — world-action models

- World-Action Models survey: https://arxiv.org/abs/2609.16074
- Resource page: https://rcl-robotics.github.io/Awesome-World-Action-Models
- HWAM: https://arxiv.org/abs/2610.12026
- Being-M0.7: https://arxiv.org/abs/2610.11283
- ReWAM: https://arxiv.org/abs/2609.38163

WAMs explicitly couple future world prediction with action generation. They sharpen several questions Clover must answer:

```text
Should world and action be factorized?
Which future state is worth predicting?
Does pixel rollout help control more than latent/state prediction?
How is execution reality distinguished from commanded/reference action?
```

News-derived WAM ideas should remain research signals until their primary papers and evaluation protocols are understood.

---

## 14. Research domain L — active perception and information gathering

A robot cannot solve open-world uncertainty only by waiting for more frames. It may need to move to create the missing evidence.

### Foundational source

- Ruzena Bajcsy, Active Perception: https://ieeexplore.ieee.org/abstract/document/5968

### Contemporary source

- Vantage: https://arxiv.org/abs/2610.11810
- Code: https://github.com/q1xiangchen/Vantage

### Core loop

```text
ambiguity
→ estimate information need
→ select viewpoint/action
→ collect new RGB evidence
→ update world belief
```

This is a central bridge between “understanding through vision alone” and “robot brain that acts.”

---

## 15. Evaluation must be grounded in state and action, not appearance alone

### RoboPhys-3D

- Paper: https://arxiv.org/abs/2608.28718

RoboPhys-3D evaluates generated/world-model rollouts using pixel fidelity, 3D consistency, state-level understanding and task-level completeness. It reports that state/execution-grounded metrics expose failures missed by perceptual or generic VLM judgments.

### Required evaluation hierarchy

```text
controlled capability diagnostic
+ anti-shortcut test
+ persistent memory test
+ interventional/causal test
+ real video transfer
+ active-perception test
+ long-horizon embodied task
+ action usefulness
```

No single benchmark is allowed to define “understanding.”

---

## 16. The six primary contradictions to resolve

The next Clover representation should emerge from experiments that discriminate these competing explanations.

### C1 — explicit vs distributed state

```text
explicit geometry / entities / variables
vs
distributed latent
vs
hybrid identifiable latent
```

### C2 — reconstruction vs prediction vs generation

```text
recover current world
vs
predict relevant future
vs
generate/simulate possible worlds
```

### C3 — object-centric vs dense scene representation

```text
objects/entities
vs
dense feature/field
vs
mixed hierarchy
```

### C4 — passive observation vs interaction

```text
watching
vs
acting and observing consequences
```

### C5 — persistent world state vs long context/direct policy

```text
maintained world belief
vs
implicit context/policy memory
```

### C6 — evidence-grounded belief vs plausible completion

```text
what evidence supports
vs
what a generative prior can plausibly imagine
```

These contradictions are more fundamental than historical Clover module names.

---

## 17. Current background conclusions — constraints, not architecture

The present evidence supports the following research constraints:

1. **World understanding is partially observable.** Unknown/unobserved state must be represented rather than silently completed.
2. **Classical geometry already solves meaningful structure.** Learned systems should be compared against it, not reinvent it without evidence.
3. **Static SSL is stronger than the old Survey baseline implied.** DINOv3 is now a primary generic visual representation baseline.
4. **Distributed video representations contain real physical information.** Compact explicit variables are not automatically superior.
5. **Reconstruction is powerful but insufficient evidence for persistence, causality or action utility.**
6. **Visible tracking is not object permanence.** PersistBench makes this distinction measurable.
7. **Streaming memory is a separate capability.** S-EMBER shows that long-context scale does not automatically solve precise grounded recall.
8. **Generation and truth have different epistemic roles.** Plausible unseen completion must not be mislabeled observed state.
9. **Interaction can add causal/controllability information unavailable from passive observation alone.**
10. **Direct VLA/robot foundation models are serious counter-hypotheses.** Explicit world state must earn its complexity through measurable embodied value.
11. **Active perception is part of intelligence, not merely camera control.** The agent should know when it needs more evidence and obtain it.
12. **Hardware comes after scientific structure.** Apple M4 is a useful local platform, not a prior on the representation.

---

## 18. What Clover must not claim yet

The repository does **not** currently establish that:

```text
explicit > latent
object-centric > dense
field > transformer
reconstruction > prediction
auditability is necessary for intelligence
Evidence Replay is necessary
CSP/SEP/licence is the correct world language
CPU-first is superior
Clover > VLA/world model
```

Each may become supported, transformed or rejected after baseline, battery and failure-map evidence.

---

## 19. Immediate research deliverables

Before the next architecture proposal, complete and keep current:

1. `BACKGROUND_RESEARCH.md` — problem-space synthesis.
2. `SOURCE_MAP.md` — one-to-one source/evidence/landing map.
3. `FRONTIER_METHODS.md` — method-family comparison.
4. `PAPERS.md` — primary-source reading index.
5. `BENCHMARKS_TASKS.md` — capability measurement map.
6. `DATASETS_CODE.md` — reproducibility resources.
7. `RESEARCH_QUESTIONS.md` — unresolved contradictions.
8. baseline reconstruction notes/results when experiments begin.
9. Understanding Battery protocol.
10. Failure Matrix.

Only after these are strong enough should a new Clover representation hypothesis be frozen.

---

## 20. Final research posture

> **Protect the question, not the current answer.**

The fixed target is a machine that forms a useful understanding of the real world from visual experience and uses it to decide and act. Whether the best internal machinery is geometry, objects, predictive latents, fields, generative simulation, explicit belief state, a hybrid, or something not yet named remains an empirical research question.

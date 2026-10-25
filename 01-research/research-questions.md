<a id="top"></a>

# 调研方向：研究问题与可证伪边界

Maintained: **2026-10-25** · Document stage: **1 — Research** ([status](../STATUS.md)).

Unresolved questions and the evidence that could distinguish competing answers. These are questions, not adopted mechanisms.

This is the canonical topic document. Update it in place; source-level dates and reading-depth labels below qualify the evidence, not the maintenance date.

<!-- BEGIN cross-domain-research-bridges -->
<a id="cross-domain-research-bridges"></a>

## 交叉研究：可以检验的桥接问题

这些是文献提出的对照和条件，不是本项目采纳的模块列表。

| 交叉方向 | 原问题中的作用 | 已核实的参照 | 仍需解决的接口 |
|---|---|---|---|
| 多视图几何 × 循环状态 × SLAM | 多帧如何形成一致且可修正的状态 | CUT3R、MonST3R、HiP3R、Stream4D | 几何漂移、动态身份、隐藏态与物性不是同一误差 |
| 物理结构学习 × 系统辨识 | 什么先验允许从轨迹找到紧凑动力学 | HNN、LNN、Koopman、SINDy、GNS、FNO | 真状态/坐标/方程族是否被额外提供；相机逆问题在哪里解决 |
| 信息论 × 状态充分性 × 记忆 | 压缩究竟保留谁需要的信息 | Information Bottleneck、CADRE、WholeBodyMem | 指定任务充分与未知未来任务充分；可恢复/不可重看的证据 |
| 无监督技能 × 可达性几何 | 不靠单任务奖励学习可复用行为坐标 | METRA、HILP | 时间距离是否丢失身份、物性、不可逆事件或反事实区分 |
| 领域泛化 × 因果结构 | 区分外观捷径和物理机制外推 | IRM、DomainBed、WILDS、物性偏移世界模型 | 环境划分/模型选择是否泄漏；已知质量与视觉识别质量分开 |
| 成像物理 × 主动感知 | 真实获取哪些测量值得其时间/风险 | 采证式 CLOSER、照明检查、任务相关 NBV | depth/地图/机体状态来源；亮度、熵和任务风险的区别 |
| 生成视频 × 因果验证 × 评测 | 区分看似合理、执行正确、持久保持和行动有用 | MIST、PhysTrace、Dual Exam、Sensorimotor Alignment | 独立考官、生成证据地位和闭环校验 |
| 部分可观测控制 × 可变形/接触 | 近静态图像下哪些隐藏量会改变动作 | FlowVLA、CW-WAM、软衣物世界模型、DefFlow | 点云、力、动作和完整模拟状态带来的额外可识别性 |

当前材料仍不足以从任何一行推出完整的 Clover 解法。后续应按共同失败与可证伪预测比较，避免把这些方向直接堆成网络结构。
<!-- END cross-domain-research-bridges -->

<!-- BEGIN broad-vision-questions -->
<a id="broad-vision-questions"></a>

## 广义纯视觉 AGI 与原生 ultrafast：必须共同回答的问题

原母问题不变。研究范围包括基础视觉功能，也包括跨时间、跨任务、开放世界的理解；机器人控制是其中一个用途。一个任务成功不授予其他能力，列全任务也没有自动回答一般智能如何形成。

| 待区分问题 | 竞争解释/参照 | 后续能区分它们的证据 |
|---|---|---|
| 是否存在兼顾识别、定位、分割、追踪与阅读的共同表征？ | 专用模型、统一架构分别训练、单权重多任务、持续共享状态 | 配平数据/骨干/计算后，基本功能、跨任务迁移和负迁移分项报告 |
| 共享“身份”究竟对应点、外观、语义实例还是物理实体？ | 点轨迹、框关联、掩码记忆、显式/分布式实体状态 | 遮挡/重现、相近实例、分裂合并、外观/功能改变与反证后修正 |
| 开放词汇识别来自视觉经验还是语言/教师知识？ | 视觉 SSL、视觉监督、图文预训练、标签/知识图驱动数据引擎 | V/L 来源匹配；新类别/属性/关系组合与无关文字/背景替换 |
| 多任务接口带来一般能力还是任务 token 路由？ | Pix2Seq/Florence/OneFormer/WeVisOne 等不同统一方式 | 新任务或新组合的学习、输出接口改变和共同状态贡献；不把 API 数量当 AGI |
| 视觉阅读如何与世界理解共存？ | 转写/布局专用器、图文解析器、视觉推理状态 | 小字/密集文档与自然视频同时覆盖；像素所见、语言先验和推断错误分开 |
| 原生计算机制能否同时保持全部关键视觉证据？ | 直接密集预测、序列解码、循环/SSM、稀疏/自适应与混合计算 | 相同完整工作负载的结果完成时间、证据年龄、长时内存及小物体/边界/运动/记忆保持 |
| 物理/因果识别是否依赖不可见的结构先验？ | 像素预测、已知 ODE、单父解码、局部稀疏/干预图等理论 | 在明示假设内外对照；报告未识别等价类/近似界，不用自信度补成真值 |
| 部署任务外的证据是否仍可恢复？ | 任务充分压缩、共享世界状态、原始证据/可恢复记忆 | 在采集后才公布的新查询/新任务与反例；区分当时不存在和后来被丢弃的信息 |

[完整能力地图](perception-and-identifiability.md#broad-visual-capabilities)、[学习来源](learning-and-data.md#broad-visual-learning)、[计算维度](foundation-models-and-systems.md#native-ultrafast-research)与[验收地图](evaluation-and-benchmarks.md#broad-visual-evaluation)共同维护这些问题。它们约束调研/分析，当前没有选定 Clover 的答案或宣布实验通过。
<!-- END broad-vision-questions -->

## Contents

- [Research Questions](#topic-research-survey-research_questions)
- [01 — What Is a World Representation?](#topic-docs-research-questions-01-world-representation)
- [02 — Explicit vs Distributed Representation](#topic-docs-research-questions-02-explicit-vs-distributed)
- [03 — Prediction vs Reconstruction vs Generation](#topic-docs-research-questions-03-prediction-reconstruction-generation)
- [04 — What Can Vision Alone Identify?](#topic-docs-research-questions-04-what-can-vision-alone-identify)
- [05 — What Requires Interaction?](#topic-docs-research-questions-05-observation-vs-interaction)
- [06 — Memory and World Persistence](#topic-docs-research-questions-06-memory-and-world-persistence)
- [07 — Objects vs Fields vs Geometry](#topic-docs-research-questions-07-objects-fields-geometry)
- [08 — What Is Physical Understanding?](#topic-docs-research-questions-08-physical-understanding)
- [09 — What Is Causal Understanding?](#topic-docs-research-questions-09-causal-understanding)
- [10 — Why Should a Worldview Help Action?](#topic-docs-research-questions-10-world-model-to-action)
- [11 — Language and the Vision-Only Question](#topic-docs-research-questions-11-language-and-vision-only)
- [12 — Why Did Classical Computer Vision Not Naturally Scale Into World Understanding?](#topic-docs-research-questions-12-why-classical-cv-did-not-scale-to-world-understanding)
- [Open Research Questions](#topic-docs-open-questions)

<a id="topic-research-survey-research_questions"></a>

## Research Questions

Source record updated: 2026-10-14

Synthesis layer of the Clover Survey. These questions must be understood before the next Clover representation is frozen.

> **SSOT:** How can a machine understand the real world through vision alone?

> **Long-term goal:** Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.

---

### 1. What exactly is hidden, and what is actually observed?

A camera observes images, not the world state itself. The underlying problem is partially observable.

Useful background:

- POMDPs in Robotics — https://arxiv.org/abs/2209.10342
- Probabilistic Robotics — https://mitpress.mit.edu/9780262201629/probabilistic-robotics/

Clover must distinguish at least:

```text
observed
inferred
predicted
ambiguous
unobserved
contradicted
```

**Status: OPEN.**

### 2. What is a world representation?

A SLAM map, 3D reconstruction, object graph, predictive latent, video generator, policy hidden state and simulator are all called “world models” but are not interchangeable.

Candidate families:

```text
explicit geometry
object/entity state
distributed predictive latent
continuous field
episodic/persistent memory
generative simulator
hybrid/identifiable latent
```

**Status: OPEN.**

### 3. Must understanding be explicit?

Explicit state supports direct queries, revision, verification and planning. Distributed representations remain serious counter-hypotheses.

- Interpreting Physics in Video World Models — https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/
- Identifiable World Models — https://arxiv.org/abs/2610.07028

The question is not “can we name variables?” but whether explicit state produces capabilities that distributed state cannot match at comparable data/compute.

### 4. Which parts of geometry should be learned?

Projective geometry, camera projection, visibility and bundle adjustment have strong mathematical formulations. DUSt3R/VGGT show learned estimators can recover geometry robustly.

- ORB-SLAM3 — https://arxiv.org/abs/2007.11898
- DUSt3R — https://arxiv.org/abs/2312.14132
- VGGT — https://arxiv.org/abs/2503.11651
- VGGT-Ω — https://arxiv.org/abs/2605.15195

Research target: identify the division of labor between exact structure and learned priors.

### 5. What does static visual SSL already solve?

DINOv3 now provides a stronger static baseline than the previous Survey assumed.

- DINOv3 — https://ai.meta.com/research/publications/dinov3/
- Code — https://github.com/facebookresearch/dinov3

Question:

> Which claimed world-understanding capabilities disappear when the comparator is a very strong frozen image representation rather than an older encoder?

### 6. Prediction, reconstruction or generation?

These objectives preserve different information:

- V-JEPA predicts in latent space — https://arxiv.org/abs/2506.09985
- VGGT/Ω reconstruct geometry — https://arxiv.org/abs/2605.15195
- Atlas/Cosmos generate/simulate — https://www.worldlabs.ai/blog/atlas · https://arxiv.org/abs/2606.02800
- ReWAM challenges reconstruction-only control state — https://arxiv.org/abs/2609.38163

Which objective produces the most useful state for persistence, prediction, causality and action?

### 7. Is reconstruction a sufficient proxy for spatial understanding?

VGGT-Ω provides direct evidence that reconstruction features can help VLA and language alignment.

- https://arxiv.org/abs/2605.15195

But spatial reconstruction does not automatically establish memory, causality or action utility.

Required comparison:

```text
reconstruction accuracy
vs
world-query accuracy
vs
persistent memory
vs
action improvement
```

### 8. What can vision alone identify?

Visible boundary, motion, texture and appearance are visual evidence. 3D shape, identity, support and persistence require temporal evidence and assumptions. Exact force, friction, mass or hidden geometry may be underdetermined.

The system must not silently convert learned priors into observations.

### 9. What does “vision alone” mean for training, not just deployment?

Existing V0–V3 labels describe observation at inference. Modern VLM/VLA systems may also learn from language, actions, proprioception or privileged simulator state.

Background Research proposes a second provenance annotation:

```text
L0 visual self-supervision
L1 visual labels
L2 language/world knowledge
L3 action-conditioned experience
L4 non-visual / privileged physical evidence
```

Question: how much capability is attributable to visual experience itself?

### 10. Objects, fields, geometry, or combinations?

Objects help identity/composition; dense features scale well; geometry supplies metric constraints; fields may support local continuous computation.

Relevant evidence:

- Slot Attention — https://proceedings.neurips.cc/paper/2020/hash/8511df98c02ab60aea1b2356c013bc0f-Abstract.html
- PLATO — https://www.nature.com/articles/s41562-022-01394-8
- DINOv3 — https://arxiv.org/abs/2508.10104
- VGGT-Ω — https://arxiv.org/abs/2605.15195

Historical Clover must re-test its field/entity hierarchy rather than preserve it.

### 11. What is the difference between visible tracking and object permanence?

SAM 3.1 is a strong contemporary visible-entity baseline:

- research — https://ai.meta.com/research/publications/sam-3-segment-anything-with-concepts/
- code — https://github.com/facebookresearch/sam3

PersistBench explicitly evaluates what happens after the object leaves view:

- https://arxiv.org/abs/2609.20819

Question: what internal mechanism maintains identity/existence when perception no longer supplies the object?

### 12. What is persistent memory?

Possible memories:

```text
raw visual evidence
compressed world state
episodic events
object state
task state
semantic concepts
hybrids
```

Relevant sources:

- PersistBench — https://arxiv.org/abs/2609.20819
- S-EMBER — https://arxiv.org/abs/2607.02689
- VISTA — https://arxiv.org/abs/2610.02200

**Status: OPEN.** Evidence Replay is one candidate, not the default answer.

### 13. Which information may be forgotten safely?

A world model cannot retain all pixels indefinitely at high resolution.

The real problem is query/task sufficiency:

> What distinctions must survive compression for the family of world queries and actions the system claims to support?

Compare:

```text
fixed context
recurrent latent
hierarchical memory
query-conditioned retention
selective replay
```

### 14. How should memory revise itself?

```text
new evidence
→ contradiction
→ affected state
→ revision
→ downstream update
```

Measure stale detection, correction latency, update locality and downstream action recovery.

Historical belief-revision and proof/provenance machinery should only survive if they improve these outcomes.

### 15. What is physical understanding?

Suggested ladder:

```text
visual continuation
→ physical plausibility
→ relational/invariant consistency
→ task-relevant state transition
→ intervention-sensitive prediction
→ quantitative state when identifiable
→ improved action/recovery
```

Relevant instruments:

- IntPhys 2 — https://ai.meta.com/research/publications/intphys-2-benchmarking-intuitive-physics-understanding-in-complex-synthetic-environments/
- MVP — https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/
- Principia — https://arxiv.org/abs/2609.04200
- RoboPhys-3D — https://arxiv.org/abs/2608.28718

### 16. Do useful physical variables need compact coordinates?

Meta's mechanistic study reports distributed high-dimensional motion representations:

- https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/

Question:

```text
compact interpretable state
vs
distributed decodable state
vs
identifiable hybrid
```

Which representation best supports generalization, intervention and action at matched cost?

### 17. What is causal understanding?

```text
correlation
→ predictive dependency
→ intervention-sensitive dependency
→ counterfactual model
```

Relevant sources:

- CausalVQA — https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/
- CRL identifiability — https://proceedings.mlr.press/v238/varici24a.html
- multi-node interventions — https://proceedings.mlr.press/v236/bing24a

Historical Counter-Witness causality is a candidate linking prediction error and revision; it must show intervention/counterfactual gains over learned dynamics.

### 18. What does interaction add?

Passive video can learn broad statistical dynamics. Interaction adds:

```text
controllability
intervention
action consequence
affordance
active information acquisition
```

V-JEPA 2 provides a concrete passive-video → action-conditioned example:

- https://arxiv.org/abs/2506.09985

Causal-representation theory also motivates interventions as information sources.

### 19. Do we need active perception?

Can the system represent uncertainty well enough to decide the next visual action?

- Bajcsy — https://ieeexplore.ieee.org/abstract/document/5968
- Vantage — https://arxiv.org/abs/2610.11810

Core loop:

```text
ambiguity
→ information need
→ look/move/inspect
→ new RGB evidence
→ belief update
```

### 20. How should uncertainty and observability be represented?

```text
not visible ≠ empty
unobserved ≠ absent
unknown type ≠ nonexistent
low confidence ≠ false
confidence ≠ authority
plausible completion ≠ observed fact
```

Bayesian state estimation and POMDP belief state are important prior art. Historical Clover epistemic/licence semantics are one possible implementation, not the definition of the problem.

### 21. When is generative completion useful, and when is it dangerous?

Atlas/Cosmos demonstrate strong generation/simulation routes:

- Atlas — https://www.worldlabs.ai/blog/atlas
- Cosmos 3 — https://arxiv.org/abs/2606.02800

Question: can a model exploit plausible hidden completion for planning while retaining explicit knowledge that the completion is hypothetical rather than observed?

### 22. What role should language play?

Language injects semantics, world knowledge and task concepts.

Gemini ER 2, π0.5, OpenVLA and related systems mix visual evidence with language/action priors:

- Gemini ER 2 — https://deepmind.google/models/gemini-robotics/embodied-reasoning/
- π0.5 — https://arxiv.org/abs/2504.16054
- OpenVLA — https://arxiv.org/abs/2406.09246

Vision-only evaluation must distinguish visual inference from language-prior recall.

### 23. Is a persistent world state actually necessary for strong robot behavior?

Direct and implicit policies are serious falsifiers:

- π0.5 — https://arxiv.org/abs/2504.16054
- Figure Helix 2.5 — https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization
- Skild S1 — https://www.skild.ai/blogs/s1

Critical eventual comparison:

```text
strong matched policy
vs
strong matched policy + persistent world representation
```

A worldview must improve measurable embodied outcomes to justify itself.

### 24. What should the world↔action relationship be?

Competing structures:

```text
direct policy
hierarchical reasoner + VLA
explicit world + planner
world-action model
generative simulator + planner
```

Relevant evidence:

- Gemini ER 2 — https://deepmind.google/models/gemini-robotics/embodied-reasoning/
- WAM survey — https://arxiv.org/abs/2609.16074
- HWAM — https://arxiv.org/abs/2610.12026

### 25. What does “type” mean for a machine?

Possible type systems:

```text
semantic category
geometry class
dynamical equivalence
affordance/effect equivalence
learned transformation class
```

Evaluate by transfer to novel objects/actions rather than human-label agreement alone.

### 26. What should remain invariant across embodiments?

Candidate separation:

```text
embodiment-independent world structure
+
embodiment-specific controllability/effect model
```

Relevant sources:

- Open X-Embodiment — https://github.com/google-deepmind/open_x_embodiment
- Skild omni-bodied thesis — https://skild.ai/blogs/building-the-general-purpose-robotic-brain

### 27. How should real-world understanding be evaluated?

Combine:

```text
controlled physics
shortcut-resistant pairs
persistent memory
streaming recall
real video
intervention
active perception
world change/revision
long-horizon tasks
unseen environments
action usefulness
```

RoboPhys-3D is especially relevant to state/action-grounded evaluation:

- https://arxiv.org/abs/2608.28718

### 28. What should a Failure Matrix record?

At minimum:

```text
geometry
identity
permanence
temporal consistency
observability
memory/retrieval
physics
causality
counterfactuals
OOD/generalization
camera shift
revision/recovery
long horizon
action utility
compute
```

This matrix should exist before a new representation decision.

### 29. When should hardware influence theory?

Hardware should not select the scientific representation.

The order remains:

```text
science problem
→ representation
→ algorithm
→ compute structure
→ CPU/GPU/Metal/other mapping
```

M4 suitability is an engineering property, not scientific correctness.

### 30. Why did CPU-era classical vision not become general world understanding?

Not simply speed. Important limits included handcrafted/task-specific representations, fragmented pipelines, limited data scaling and weak learned abstraction.

Historical anchors:

- SIFT — https://www.cs.ubc.ca/~lowe/papers/ijcv04.pdf
- AlexNet — https://papers.nips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf
- ResNet — https://arxiv.org/abs/1512.03385
- ViT — https://arxiv.org/abs/2010.11929
- CLIP — https://arxiv.org/abs/2103.00020

### 31. What should the next Clover architecture decision look like?

Not:

```text
interesting paper
→ add mechanism
```

Not:

```text
historical Clover idea
→ search for supporting evidence
```

Required chain:

```text
Background Research
→ strong baseline setup
→ Understanding Battery
→ Failure Matrix
→ unresolved cross-family contradiction
→ candidate representations
→ discriminating experiment
→ falsifier
→ architecture decision
→ implementation
```

A next-generation Clover proposal must state what observed failure it solves, what evidence supports it, what would kill it and what remains open.

---

<a id="topic-docs-research-questions-01-world-representation"></a>

## 01 — What Is a World Representation?

### Question

What internal state must a machine maintain so that visual observations become a usable model of a persistent world rather than a stream of unrelated frames?

### Major prior answers

#### Explicit geometric state

Classical SfM/SLAM represents cameras, landmarks and geometric constraints explicitly. ORB-SLAM3 demonstrates that a system can maintain and merge maps over long time spans and across revisits.

Strength: variables are interpretable and directly usable for localization and geometry.

Limit: geometry alone does not provide object identity, affordance, semantics, causal structure or broad open-world abstraction.

#### Learned distributed state

DINOv2 and V-JEPA-style encoders learn feature spaces rather than hand-written geometric state. V-JEPA 2 extends this to video and shows that large-scale self-supervised video learning supports motion understanding, action anticipation and, after action-conditioned post-training, robot planning.

Strength: broad abstraction can emerge without manually defining every variable.

Limit: what constitutes the persistent world state is less explicit, and updating/revising a long-lived world model remains a separate question.

#### Learned geometric state

VGGT directly predicts cameras, depth, point maps and 3D tracks with a feed-forward model. VGGT-Ω pushes this direction toward larger-scale, dynamic reconstruction and more transferable geometry-aware representations.

Strength: combines learned priors with explicit geometric outputs.

Limit: accurate reconstruction is not equivalent to physical, causal or task-level understanding.

#### Generative/spatial world models

World Labs Atlas and NVIDIA Cosmos 3 represent another answer: train a large model to generate/reconstruct/simulate coherent worlds across modalities. These systems suggest that a world representation may be best judged by what coherent futures or spatial continuations it can generate.

Limit: generation quality can hide state inconsistency; persistent identity, observability and intervention structure require separate measurement.

### Current synthesis

A useful world representation likely needs to support at least four functions:

1. **state** — what currently exists and where;
2. **persistence** — what remains true when not currently visible;
3. **transition** — how the world can change;
4. **query/action interface** — what downstream decisions can reliably read.

No current route establishes that one representation family is sufficient for all four.

### Clover implication

Clover should not choose `field`, `object graph`, `3D map`, or `latent` by preference. The next representation hypothesis should be selected by whether it jointly supports persistence, revision, dynamics, queryability and action utility.

### Primary sources

- ORB-SLAM3 paper: https://arxiv.org/abs/2007.11898
- ORB-SLAM3 code: https://github.com/UZ-SLAMLab/ORB_SLAM3
- DINOv2 paper: https://arxiv.org/abs/2304.07193
- V-JEPA 2 paper: https://arxiv.org/abs/2506.09985
- V-JEPA 2 official code: https://github.com/facebookresearch/vjepa2
- VGGT paper: https://arxiv.org/abs/2503.11651
- VGGT code: https://github.com/facebookresearch/vggt
- VGGT-Ω paper: https://arxiv.org/abs/2605.15195
- VGGT-Ω code: https://github.com/facebookresearch/vggt-omega
- World Labs Atlas: https://www.worldlabs.ai/blog/atlas
- Cosmos 3 paper: https://arxiv.org/abs/2606.02800

---

<a id="topic-docs-research-questions-02-explicit-vs-distributed"></a>

## 02 — Explicit vs Distributed Representation

### Question

Must world understanding be stored in compact explicit variables, or can a high-dimensional distributed representation be the better substrate?

### Why this matters

Old Clover prototypes lean toward explicit machine-native state. Modern representation learning provides a serious counter-hypothesis: useful physical information may be distributed across large feature spaces and only become readable when needed.

### Evidence for distributed representations

DINOv2 shows that self-supervised training at scale can produce generic visual features transferable across many tasks.

V-JEPA 2/2.1 shows that predictive self-supervision can produce strong global and dense video features. V-JEPA 2.1 specifically adds dense predictive loss and deep self-supervision to improve spatially and temporally grounded features.

Meta's mechanistic work on physics in video world models reports that some physical variables become increasingly linearly accessible across network depth while other quantities can be represented by distributed population codes rather than a small set of dedicated units.

### Evidence for explicit outputs

Classical geometry remains compelling when the variable has a well-defined mathematical meaning: camera pose, projection, depth constraints and multi-view consistency are not arbitrary labels.

VGGT is important because it combines a learned network with explicit geometric outputs: camera parameters, depth, point maps and tracks.

### The real comparison

The right question is not `explicit vs neural`.

It is:

> Which information should remain distributed for flexibility, and which information should be materialized as explicit state because downstream reasoning, revision or control needs stable semantics?

A plausible hybrid is:

```text
learned distributed visual representation
        ↓
selective explicit state materialization
        ↓
planning / verification / interaction
```

But this remains a hypothesis.

### Clover implication

Clover should test whether explicit variables add value in:

- long-horizon persistence;
- belief revision;
- causal intervention;
- efficient planning;
- failure diagnosis;
- cross-task reuse.

If explicit state does not improve these, explicitness alone is not a contribution.

### Primary sources

- DINOv2: https://arxiv.org/abs/2304.07193
- V-JEPA 2: https://arxiv.org/abs/2506.09985
- V-JEPA 2.1: https://arxiv.org/abs/2603.14482
- V-JEPA 2/2.1 code: https://github.com/facebookresearch/vjepa2
- VGGT: https://arxiv.org/abs/2503.11651
- VGGT-Ω: https://arxiv.org/abs/2605.15195
- Slot Attention: https://arxiv.org/abs/2006.15055
- Meta — Interpreting Physics in Video World Models: https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/

---

<a id="topic-docs-research-questions-03-prediction-reconstruction-generation"></a>

## 03 — Prediction vs Reconstruction vs Generation

### Question

Which learning objective best creates a representation useful for understanding a persistent physical world?

### Reconstruction

Classical multi-view geometry and modern models such as DUSt3R, VGGT and VGGT-Ω ask the system to recover spatial structure from visual observations.

Reconstruction strongly constrains geometry because multiple views must agree on cameras, depth or point structure.

What it does not guarantee: understanding dynamics, causality, object purpose or task relevance.

### Prediction

V-JEPA 2 predicts in representation space rather than directly generating pixels. The key idea is that useful latent structure can be learned by predicting missing/future representations while avoiding the burden of modeling every pixel detail.

V-JEPA 2.1 strengthens dense and temporal grounding with dense predictive loss, deep self-supervision and unified image/video training.

Prediction provides a natural test of temporal regularity, but prediction accuracy alone does not establish causal understanding.

### Generation / simulation

NeRF and 3D Gaussian Splatting show how visual observations can parameterize scenes for novel-view rendering. Atlas and Cosmos 3 go further toward learned world generation and simulation.

Generation can demonstrate rich spatial/temporal coherence, but photorealistic output can still be wrong at the state or action level.

### Planning-oriented latent world models

PlaNet, DreamerV3 and TD-MPC2 demonstrate another criterion: a world model can be useful even if it is optimized primarily to support control in latent space rather than reconstructing a human-readable world.

This creates a central Clover tension:

> Is the best representation the one that reconstructs reality most faithfully, predicts future representations most accurately, or supports decisions most efficiently?

### Current synthesis

These objectives supervise different invariants:

- reconstruction → spatial consistency;
- prediction → temporal/statistical consistency;
- generation → distributional/world continuation;
- control/world-action learning → action-relevant dynamics.

A future Clover objective may need a combination, but combining losses without a principled reason would be framework stacking. The research task is to identify which invariant is necessary for which capability.

### Primary sources

- DUSt3R: https://arxiv.org/abs/2312.14132
- VGGT: https://arxiv.org/abs/2503.11651
- VGGT-Ω: https://arxiv.org/abs/2605.15195
- V-JEPA 2: https://arxiv.org/abs/2506.09985
- V-JEPA 2.1: https://arxiv.org/abs/2603.14482
- NeRF: https://arxiv.org/abs/2003.08934
- World Labs Atlas: https://www.worldlabs.ai/blog/atlas
- Cosmos 3: https://arxiv.org/abs/2606.02800
- DreamerV3: https://arxiv.org/abs/2301.04104
- TD-MPC2: https://arxiv.org/abs/2310.16828

---

<a id="topic-docs-research-questions-04-what-can-vision-alone-identify"></a>

## 04 — What Can Vision Alone Identify?

### Question

Before designing a world model, we must separate what is identifiable from visual evidence from what remains fundamentally ambiguous without assumptions, motion or intervention.

### Geometry already teaches an important lesson

A single image does not uniquely specify the physical world. Projection discards information. Monocular geometry has scale and depth ambiguities; textureless regions, occlusion and repeated structure create additional uncertainty.

Multi-view motion changes the problem because viewpoint variation creates constraints. SfM/SLAM exploits exactly this: geometry becomes better identified from multiple observations and camera motion.

### Learned priors change inference, not observability

Modern models can infer plausible depth, object category or motion from a single view using learned regularities. This is valuable, but a learned prior is not the same as direct observation.

For Clover this distinction matters:

```text
observed evidence
learned prior
inferred state
unobserved region
```

should not be silently collapsed.

### Active vision changes what is knowable

A robot is not a passive camera. If two world hypotheses are visually indistinguishable, the system can move, change viewpoint or manipulate the scene to acquire discriminating evidence.

This makes `vision alone` compatible with information-seeking action: the sensory channel stays visual even though action changes the future observations.

### Research consequence

A world-understanding system should represent not only a best estimate but also which aspects are underdetermined by current visual evidence.

This is more fundamental than a confidence score. The machine should know *what observation would resolve the ambiguity*.

### Clover implication

The future Clover state should distinguish at least conceptually:

- directly observed;
- geometrically constrained;
- prior-inferred;
- currently unobserved;
- ambiguous among multiple hypotheses.

Whether these become explicit fields or remain distributed is still open.

### Primary sources

- ORB-SLAM3: https://arxiv.org/abs/2007.11898
- VGGT: https://arxiv.org/abs/2503.11651
- VGGT-Ω: https://arxiv.org/abs/2605.15195
- DUSt3R: https://arxiv.org/abs/2312.14132
- Active Perception overview roots: Ruzena Bajcsy, "Active Perception" (1988), DOI landing page: https://doi.org/10.1109/34.8800

---

<a id="topic-docs-research-questions-05-observation-vs-interaction"></a>

## 05 — What Requires Interaction?

### Question

How much world understanding can be learned from passive visual observation, and what knowledge requires acting in the world?

### Evidence from passive video

V-JEPA 2 is a major data point. It pretrains on more than one million hours of image/video data without actions and obtains strong motion/action understanding. This shows that a large amount of physical regularity is available from observation alone.

But robot planning is introduced by post-training an action-conditioned model with robot trajectory videos. That separation is scientifically useful: it suggests passive observation can build a broad visual prior while interaction teaches controllable transitions.

### Evidence from robot foundation models

π0.5 combines robot trajectories with web/multimodal knowledge, object detections and hierarchical semantic targets. Figure Helix 2.5 reports improved unseen-home generalization after pretraining on large-scale human behavior data. Skild reports combining human video, robot data, simulation and other physical experience.

These systems do not isolate a single causal factor, but collectively they suggest that broad physical competence benefits from heterogeneous experience.

### What interaction uniquely provides

Observation can reveal correlation and natural dynamics. Intervention gives stronger information about:

- controllability;
- action-conditioned transitions;
- object affordance;
- latent physical properties exposed by contact;
- causal direction under deliberate perturbation.

### Clover implication

The scientific question should be split:

1. What world structure can be acquired from vision-only observation?
2. What additional structure becomes identifiable when the agent acts but still receives only visual sensory evidence?

This preserves the vision-only SSOT while allowing embodied learning.

### Primary sources

- V-JEPA 2 paper: https://arxiv.org/abs/2506.09985
- V-JEPA 2 project/code: https://github.com/facebookresearch/vjepa2
- π0.5 paper: https://arxiv.org/abs/2504.16054
- π0.5 project: https://www.pi.website/blog/pi05
- Figure Helix 2.5 official report: https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization
- Skild S1 official report: https://www.skild.ai/blogs/s1
- Skild Physical Self-Play: https://skild.ai/blogs/physical-self-play

---

<a id="topic-docs-research-questions-06-memory-and-world-persistence"></a>

## 06 — Memory and World Persistence

### Question

If the visual field changes every moment, what should persist inside the machine, for how long, and in what form?

### Different traditions answer differently

#### SLAM

Persistent maps and keyframes preserve geometric information across time and revisits. ORB-SLAM3 is a strong example of reusing older map information and merging maps after tracking loss.

#### Video models

Transformers and video encoders maintain temporal context inside a finite computation window. V-JEPA 2.1 targets temporally consistent dense features, but a feature's temporal stability is not yet equivalent to an indefinitely persistent world memory.

#### Video segmentation

SAM 2 uses streaming memory for video segmentation, showing a practical architecture for carrying object-mask information through time.

#### Robot policies

Long-horizon policies may use context, recurrence or hierarchical subtask structure without exposing a persistent external world state.

### Three memory problems must be separated

1. **perceptual continuity** — keep identity over nearby frames;
2. **world persistence** — retain facts while they are out of view;
3. **lifelong consolidation** — retain useful knowledge across long periods without storing all raw observations.

Treating all three as one `memory module` hides the real research problem.

### Belief revision is the hard test

Memory is not useful if it only accumulates. A world model must support:

```text
old belief
+ new contradictory visual evidence
→ corrected world state
```

The important capability is selective persistence plus revision.

### Clover implication

Future Clover work should measure memory by world-query stability and correction, not by context length alone.

### Primary sources

- ORB-SLAM3: https://arxiv.org/abs/2007.11898
- SAM 2: https://arxiv.org/abs/2408.00714
- V-JEPA 2.1: https://arxiv.org/abs/2603.14482
- Ego4D dataset: https://ego4d-data.org/
- LIBERO lifelong robot learning benchmark: https://libero-project.github.io/main.html

---

<a id="topic-docs-research-questions-07-objects-fields-geometry"></a>

## 07 — Objects vs Fields vs Geometry

### Question

What are the basic units of a machine's world model: objects, continuous fields, geometric primitives, or something else?

### Object-centric view

Slot Attention argues that a scene can be decomposed into exchangeable slots that bind to entities and support compositional generalization.

SAM 2 demonstrates that object-like visual regions can be maintained over video with streaming memory.

Object representations are attractive for identity, relation and manipulation, but object boundaries can be ambiguous for fluids, articulated structures, crowds, shadows or changing topology.

### Geometric view

SLAM, DUSt3R and VGGT represent structure through cameras, points, depth and tracks. Geometry is strong for where things are and how views relate.

But pure geometry says little about which structure should count as an entity, what it can do, or why a change matters.

### Field/continuous view

NeRF represents a scene as a continuous radiance/density function. 3D Gaussian-style representations and generative spatial models offer other continuous or distributed scene substrates.

Old Clover field-crystallization hypotheses belong here, but they must be compared against these established continuous representations rather than treated as a unique category by default.

### Current synthesis

The world may require multiple scales of description:

```text
continuous spatial support
→ persistent structures
→ entities
→ relations / task abstractions
```

The research question is whether these need separate ontologies or can emerge from one representation family.

### Clover implication

The next Clover representation proposal should explain what happens in edge cases where `object` is not cleanly defined, while still making object-level action efficient when object structure is useful.

### Primary sources

- Slot Attention: https://arxiv.org/abs/2006.15055
- SAM 2: https://arxiv.org/abs/2408.00714
- DUSt3R: https://arxiv.org/abs/2312.14132
- VGGT: https://arxiv.org/abs/2503.11651
- NeRF: https://arxiv.org/abs/2003.08934

---

<a id="topic-docs-research-questions-08-physical-understanding"></a>

## 08 — What Is Physical Understanding?

### Question

What evidence is sufficient to say a machine understands physical behavior rather than recognizing visual patterns correlated with it?

### Levels of evidence

#### Level 1 — visual regularity

The model distinguishes common from unusual motion or appearance.

#### Level 2 — violation of expectation

Benchmarks such as IntPhys 2 test principles including permanence, immutability, spatiotemporal continuity and solidity.

#### Level 3 — state-variable accessibility

A representation makes quantities such as motion, depth or trajectories reliably decodable.

#### Level 4 — intervention stability

The model predicts how outcomes change under controlled interventions.

#### Level 5 — action usefulness

Physical knowledge improves planning and recovery in real or simulated interaction.

The higher levels are stronger evidence than benchmark recognition alone.

### Why shortcut controls matter

MVPBench uses minimal video pairs to reduce the chance that a model succeeds from superficial cues. This experimental idea is important for Clover: if the intended physical distinction can be solved by background or static-frame shortcuts, the result is weak evidence of understanding.

### Modern world models

V-JEPA 2 reports strong motion/action understanding and planning after action-conditioned post-training. Cosmos 3 combines multimodal understanding, world generation and action generation. New embodied-world-model evaluations such as RoboPhys-3D explicitly argue that perceptual realism can disagree with state- and execution-grounded correctness.

### Clover implication

Clover should eventually claim physical understanding only when evidence spans controlled diagnostics, counterfactual/intervention tests and downstream action.

### Primary sources

- IntPhys 2 official page: https://ai.meta.com/research/publications/intphys-2-benchmarking-intuitive-physics-understanding-in-complex-synthetic-environments/
- MVPBench official page: https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/
- V-JEPA 2: https://arxiv.org/abs/2506.09985
- Cosmos 3: https://arxiv.org/abs/2606.02800
- RoboPhys-3D: https://arxiv.org/abs/2608.28718

---

<a id="topic-docs-research-questions-09-causal-understanding"></a>

## 09 — What Is Causal Understanding?

### Question

When does a model move from predicting correlation to understanding how interventions change the world?

### Prediction is not yet causation

A video model can predict likely futures from observational regularities. This is valuable but does not by itself identify what variable caused the transition or what intervention would change the outcome.

### Causal evidence becomes stronger with interventions

For a robot, action provides natural interventions:

```text
observe state
→ apply controlled action
→ observe visual consequence
```

Repeated interventions can expose action-conditioned dynamics and affordances that passive video cannot uniquely identify.

### Counterfactual reasoning

A stronger world model should answer questions of the form:

- What if the support were removed?
- What if the object were pushed in another direction?
- Which action would make a desired state occur?

CausalVQA provides a useful video-reasoning diagnostic, but language QA is weaker evidence than interaction-grounded intervention prediction.

### Planning-oriented world models

PlaNet, DreamerV3, TD-MPC2 and V-JEPA 2-AC all use learned dynamics to support action selection. They show that predictive dynamics can be operationally useful without necessarily exposing a human-readable causal graph.

This is another Clover tension: explicit causal structure may aid revision and transfer, but it must demonstrate value beyond a strong latent dynamics model.

### Clover implication

Future causal claims should be tied to intervention-sensitive tests, not just next-frame or next-state accuracy.

### Primary sources

- CausalVQA official page: https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/
- V-JEPA 2 / V-JEPA 2-AC: https://arxiv.org/abs/2506.09985
- DreamerV3: https://arxiv.org/abs/2301.04104
- TD-MPC2: https://arxiv.org/abs/2310.16828

---

<a id="topic-docs-research-questions-10-world-model-to-action"></a>

## 10 — Why Should a Worldview Help Action?

### Question

If a direct policy can act successfully from vision, what additional value must a persistent world model provide?

### Direct-policy evidence

RT-2 established the modern VLA framing by representing robot actions in the same token space as language outputs and transferring web-scale vision-language knowledge into control.

OpenVLA provides an open-source VLA baseline trained on large-scale robot demonstrations.

π0.5 demonstrates that heterogeneous co-training can produce long-horizon behavior and meaningful generalization to new homes.

Figure Helix 2.5 and Skild S1 provide further vendor-reported evidence that broad pretraining can yield strong real-world robot behavior without exposing a classical explicit world state.

### Hierarchical reasoning evidence

Gemini Robotics ER 2 takes a more separated approach: a high-level embodied reasoning VLM handles spatial/temporal/physical reasoning, tool orchestration and success detection, while lower-level robotic models perform control.

This resembles the motivation behind Clover's Worldview → Decision → Tool Use → Execution decomposition, but similarity of decomposition is not evidence that Clover's specific internal representation is useful.

### What an explicit worldview must earn

A persistent worldview should provide measurable gains in at least some of:

- fewer unnecessary actions;
- better recovery after unexpected world change;
- longer-horizon consistency;
- safer refusal when evidence is insufficient;
- lower planning/search cost;
- transfer across tasks without retraining perception;
- better debugging or verification.

If it does not, direct/hierarchical policy learning remains the stronger engineering answer.

### Clover implication

The final paper should not argue for Worldview philosophically. It should demonstrate that the representation improves embodied performance under controlled comparisons.

### Primary sources

- RT-2 paper: https://arxiv.org/abs/2307.15818
- RT-2 PMLR publication: https://proceedings.mlr.press/v229/zitkovich23a.html
- OpenVLA paper: https://arxiv.org/abs/2406.09246
- OpenVLA code: https://github.com/openvla/openvla
- π0.5 paper: https://arxiv.org/abs/2504.16054
- π0.5 project: https://www.pi.website/blog/pi05
- Gemini Robotics ER 2 model card: https://deepmind.google/models/model-cards/gemini-robotics-er-2/
- Figure Helix 2.5: https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization
- Skild S1: https://www.skild.ai/blogs/s1

---

<a id="topic-docs-research-questions-11-language-and-vision-only"></a>

## 11 — Language and the Vision-Only Question

### Question

How should Clover study systems that use language pretraining when the SSOT asks what can be understood through vision alone?

### Why the distinction matters

Modern embodied models often inherit enormous amounts of semantic and commonsense knowledge from language or vision-language pretraining. This can dramatically improve task generalization, but it complicates claims about what was learned from visual evidence.

RT-2 explicitly transfers web-scale vision-language knowledge into robot control. π0.5 mixes image observations, language, object detections, semantic subtasks, web data and robot actions. Gemini Robotics ER 2 is a vision-language model based on Gemini 3.5 Flash.

These systems are important capability references, but they are not pure tests of visual world formation.

### Proposed research separation

Clover should distinguish:

#### Vision-only formation

What world structure can be learned from visual observations and visually observed interaction without language supervision?

#### Language alignment

Once a world representation exists, can language efficiently name, query and compose the learned structures?

#### Language prior

How much performance comes from knowledge imported through text rather than discovered from visual experience?

### Why this does not mean rejecting language

A general-purpose robot brain will likely need language. The research constraint is about causal attribution of capability, not banning useful interfaces.

Language can be a communication and task-specification channel while the scientific question remains: what world knowledge did vision itself provide?

### Clover implication

Future experiments should include vision-only and vision+language conditions when language knowledge could otherwise confound the central claim.

### Primary sources

- RT-2: https://arxiv.org/abs/2307.15818
- OpenVLA: https://arxiv.org/abs/2406.09246
- π0.5: https://arxiv.org/abs/2504.16054
- Gemini Robotics ER 2 model card: https://deepmind.google/models/model-cards/gemini-robotics-er-2/
- V-JEPA 2: https://arxiv.org/abs/2506.09985

---

<a id="topic-docs-research-questions-12-why-classical-cv-did-not-scale-to-world-understanding"></a>

## 12 — Why Did Classical Computer Vision Not Naturally Scale Into World Understanding?

### Question

Why did decades of CPU-era computer vision produce strong geometry, features and task-specific systems without naturally turning into the kind of broad visual intelligence now associated with large learned models?

This question matters because Clover originally treated CPU-first computation as a major prior. Hardware history alone does not explain the scientific transition.

### 1. Classical vision solved important invariance and geometry problems

SIFT engineered local features robust to scale, rotation and a meaningful range of viewpoint/illumination change. HOG engineered gradient statistics that were highly effective for human detection. SfM/SLAM developed explicit geometric estimation for cameras, maps and motion.

These methods were not primitive failures. Many remain mathematically strong baselines.

The limitation was usually the *scope of representation*: the designer chose what information should be represented and which task it should solve.

### 2. The deep-learning transition changed representation learning

AlexNet's 2012 ImageNet result is historically important for two linked reasons:

- a deep CNN learned hierarchical visual features from large labeled data rather than relying primarily on hand-designed descriptors;
- GPU implementation made training a 60M-parameter convolutional model on ImageNet practical enough to demonstrate the scaling advantage.

The scientific shift was therefore not simply `GPU > CPU`. It was:

```text
learned hierarchical representation
+ large data
+ scalable optimization
+ hardware able to execute the training
```

### 3. Architecture made scale usable

ResNet addressed optimization barriers that made very deep networks difficult to train. Vision Transformers later showed that, with large-scale pretraining, a comparatively generic attention architecture could compete with or exceed convolution-specific inductive biases.

The trend is important for Clover: architectures that look inefficient or under-constrained at small scale can become powerful once data, optimization and compute expose a better scaling regime.

### 4. Supervision broadened

ImageNet classification still learned a fixed label space. Later systems broadened supervision:

- CLIP used hundreds of millions of image-text pairs to create transferable visual-language representations;
- DINOv2 demonstrated strong transferable image features with self-supervision;
- V-JEPA 2/2.1 moves the learning signal into video prediction and temporal structure.

This progression reduces dependence on manually enumerated visual concepts.

### 5. What classical methods still do better conceptually

Modern learned systems do not invalidate classical insights. Geometry provides exact structure and identifiable variables when its assumptions hold. Bayesian filtering and POMDP theory distinguish state, belief, observation and action more clearly than many end-to-end networks. These distinctions may still be necessary in a general robot brain.

The research opportunity is therefore not to return to old CPU CV or to accept end-to-end scaling uncritically.

It is to ask:

> **Which structures should remain explicit because mathematics already characterizes them, and which structures should be learned because hand-designed representations fail to scale to open-ended visual experience?**

### 6. Hardware should follow the computation

The history suggests a co-design conclusion:

- GPUs won many deep-learning workloads because dense tensor operations parallelize extremely well;
- CPUs remain strong for irregular, sparse, branching and control-heavy computation;
- Apple Silicon unified memory makes heterogeneous CPU/GPU execution especially interesting for a future Clover implementation;
- but none of these hardware facts decide the representation scientifically.

### Clover implication

Clover should avoid two symmetric mistakes:

1. **nostalgia error** — assuming classical/CPU methods are more principled and therefore sufficient;
2. **scaling error** — assuming larger learned models automatically constitute world understanding.

The next Clover architecture should inherit mathematical structure where it is genuinely known and use learning where the world is too open-ended to hand-code.

### Primary sources

- SIFT — David Lowe, *Distinctive Image Features from Scale-Invariant Keypoints* (IJCV 2004): https://doi.org/10.1023/B:VISI.0000029664.99615.94
- SIFT author-hosted PDF: https://www-inst.eecs.berkeley.edu/~ee225b/sp11/readings/sift-lowe.pdf
- HOG — Dalal & Triggs, CVPR 2005: https://doi.org/10.1109/CVPR.2005.177
- AlexNet — Krizhevsky, Sutskever & Hinton, NeurIPS 2012: https://proceedings.neurips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html
- AlexNet PDF: https://papers.nips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf
- ResNet: https://arxiv.org/abs/1512.03385
- Vision Transformer: https://arxiv.org/abs/2010.11929
- CLIP: https://arxiv.org/abs/2103.00020
- DINOv2: https://arxiv.org/abs/2304.07193
- V-JEPA 2: https://arxiv.org/abs/2506.09985
- V-JEPA 2.1: https://arxiv.org/abs/2603.14482

---

<a id="topic-docs-open-questions"></a>

## Open Research Questions

These questions are first-class project assets. They are not placeholders for missing documentation.

### Representation

1. What internal representation is sufficient for world understanding?
2. Does useful understanding require explicit state?
3. Can distributed latent representations be sufficient and still support persistence, intervention and planning?
4. Should objects be primitives or emergent structures?
5. Are fields, objects and geometry competing representations or different views of one world state?

### Geometry and learning

6. Which properties should be guaranteed by geometry rather than learned?
7. Which abstractions are difficult or inefficient to hand-design?
8. Can a learned geometry foundation model replace or complement classical state estimation?

### Time and memory

9. What representation best preserves identity through occlusion and long time gaps?
10. How should multiple temporal scales coexist?
11. What should be forgotten, consolidated or replayed?

### Physics and causality

12. How much physical understanding can be learned from passive video?
13. What requires interaction?
14. How should causal structure be distinguished from predictive correlation?
15. What internal representation best supports counterfactual reasoning?

### Epistemics

16. How should unknown, unobserved, contradicted and stale information be represented?
17. What role, if any, should Clover's licence mechanism play in a final architecture?

### Embodiment

18. Does language improve world understanding or mainly inject external knowledge?
19. How should active perception emerge from world uncertainty?
20. What makes a world representation materially useful for robot decision-making?
21. Can a persistent worldview outperform a direct VLA on long-horizon recovery and intervention tasks?

### Evaluation

22. Which benchmark combinations actually discriminate understanding from shortcut exploitation?
23. What real tasks should define the final embodied result?
24. How should correctness, coverage, uncertainty and task utility be measured together?

### Hardware

25. Which components are naturally CPU, GPU or accelerator workloads once the scientific mechanism is known?
26. Can unified-memory systems such as Apple Silicon provide a useful prototype platform for mixed sparse/dense computation?

<a id="top"></a>

# 调研方向：评测方法、基准与证据

Maintained: **2026-10-25** · Document stage: **1 — Research** ([status](../STATUS.md)).

This Stage-1 direction surveys benchmarks, capability batteries, protocol controls and the evidence ladder. Designs and external results are not Clover measurements. Registered experiments and results belong to [Stage 6](../06-evaluation/README.md).

This is the canonical topic document. Update it in place; source-level dates and reading-depth labels below qualify the evidence, not the maintenance date.

<a id="evidence-retention-diagnostics"></a>

## 2026-10-25 当前补充：压缩与证据保留的区分条件

**下一步应区分的资料与诊断问题：**

| 问题 | 必须保留的对照 | 不能用来替代的指标 |
|---|---|---|
| 压缩是否删掉了当前任务证据 | 同一骨干、同一采样视频、原 tokens / 压缩 tokens | 仅 FLOPs 或吞吐 |
| 当未来任务改变，历史细节是否还可用 | 压缩前不透露后续 query；同字节预算的状态、显式记忆、可检索原证据对照 | 同一问题上的平均 QA 分数 |
| 失败来自采样还是表示 | 原始视频、采样帧、视觉编码、合并/裁剪逐层对照 | 把低帧率错漏全部归罪于推理 |
| 再观察能否补回缺失信息 | 可再观察 / 事件已消失或动作不可逆 | 假定每次都能安全重看 |
| 效率是否满足具身循环 | 含解码、编码、检索、状态更新的端到端 P50/P95 与峰值内存 | 已缓存编码、LLM 子阶段加速或外部 GPU 比例 |

这是后续分析与证据登记的区分表，不是要求 Stage 1 立即实施一套架构。物体永久性和未知任务的证据保留问题仍开放；当前两项压缩工作只是强效率参照。

<!-- BEGIN current-cross-domain-evidence -->
<a id="current-cross-domain-evidence"></a>

## 当前跨领域与前沿证据：评估必须区分的失败来源

检索/核验：**2026-10-25（Asia/Shanghai）**。下表是外部研究记录，不是 Clover 的实验结果或架构决定。

当前新增评估文献强调：变化未执行不能记为遗忘；离线代理相关性不能替代闭环结果；语言考官可能带入先验；总体分数可能掩盖任务内排序和少数危险条件。跨域方法的模型选择策略也是被比较系统的一部分。

### DomainBed

- **来源/版本：** [原论文](https://arxiv.org/abs/2007.01434v1)；初始提交 2020-07-02；本次返回版本更新于 2020-07-02。`PRIMARY_PAPER`。
- **问题与机制：** DomainBed 将数据、架构、训练与模型选择策略放到同一评估协议中。
- **输入/学习来源：** 监督式跨域数据；属于评估方法参照，不是机器人 V0/L0 成果。
- **实际证据：** 原论文协议下，充分实现的 ERM 是必须保留的强对照。
- **不能推出 / 待区分：** 不能把当时 ERM 的结果写成所有后来 DG 方法无效；也不能偷看测试域选模型再宣称 OOD 泛化。
- **本次阅读深度：** 正文选读：方法、监督或局限段；未复核全部实验/证明。

### WILDS

- **来源/版本：** [原论文](https://arxiv.org/abs/2012.07421v3)；初始提交 2020-12-14；本次返回版本更新于 2021-07-16。`PRIMARY_PAPER`。 [作者提供的项目/代码入口](https://wilds.stanford.edu/)（未运行复现）。
- **问题与机制：** WILDS 提供现实分布偏移数据与统一评估工具。
- **输入/学习来源：** 多个应用/模态和标签来源，并非统一机器人视觉协议。
- **实际证据：** 十组现实偏移任务；覆盖域与分组表现而非只报总体均值。
- **不能推出 / 待区分：** 其数据不直接证明机器人闭环迁移；借鉴分组、时间/地点划分与最差组报告时，应保留任务差异。
- **本次阅读深度：** 正文选读：方法、监督或局限段；未复核全部实验/证明。

### Simplicity Bias

- **来源/版本：** [原论文](https://arxiv.org/abs/2006.07710v2)；初始提交 2020-06-13；本次返回版本更新于 2020-10-28。`PRIMARY_PAPER`。
- **问题与机制：** Simplicity Bias 研究构造可控简单/复杂特征，检验优化器选择捷径。
- **输入/学习来源：** 理论与定制数据实验，条件比自然机器人场景窄。
- **实际证据：** 展示训练可能只依赖简单但脆弱的特征，集成/对抗训练也不必消除问题。
- **不能推出 / 待区分：** 不能把构造性结果扩大成所有网络都无法学习物理；应设计使外观捷径与真实机制预测相反的配对测试。
- **本次阅读深度：** 摘要与书目核验。

### WAM 表征先验与 nuisance 几何

- **来源/版本：** [原论文](https://arxiv.org/abs/2610.29168v1)；初始提交 2026-10-21；本次返回版本更新于 2026-10-21。`PRIMARY_PAPER`。
- **问题与机制：** WAM 泛化研究以 nuisance orthogonality 和训练后的 nuisance suppression 分析表征。
- **输入/学习来源：** 给定外观扰动、经验训练流形及既有预训练骨干。
- **实际证据：** 多骨干的视觉扰动与机器人策略表现关联。
- **不能推出 / 待区分：** 表征几何指标与成功率相关不证明因果充分；需留出新干扰类型、任务和机体做外推。
- **本次阅读深度：** 摘要与书目核验。

### Sensorimotor Alignment

- **来源/版本：** [原论文](https://arxiv.org/abs/2610.31670v1)；初始提交 2026-10-22；本次返回版本更新于 2026-10-22。`PRIMARY_PAPER`。
- **问题与机制：** Sensorimotor Alignment 用感知特征与运动轨迹几何的一致性，作闭环评估前的廉价模型筛选。
- **输入/学习来源：** 需要运动轨迹及评估数据；不能把离线 proxy 称为模型只用视觉。
- **实际证据：** 跨具身模型/骨干的相关性与模型筛选。
- **不能推出 / 待区分：** 代理分数不能替代闭环结果；应检验选择偏差、轨迹泄漏和跨任务外推，而非宣布“柏拉图式世界真值”。
- **本次阅读深度：** 摘要与书目核验。

### MIST / Execution Before Memory

- **来源/版本：** [原论文](https://arxiv.org/abs/2610.23542v1)；初始提交 2026-10-16；本次返回版本更新于 2026-10-16。`PRIMARY_PAPER`。
- **问题与机制：** MIST 先检查指定变化是否真的执行，再考察遮挡后 reveal 是否保持。
- **输入/学习来源：** 生成视频的设定/指令执行与隐藏转移分开，控制提前泄漏。
- **实际证据：** 诊断生成世界模型的执行失败与记忆失败。
- **不能推出 / 待区分：** 没有执行的变化不能拿来算遗忘；生成 reveal 保持也不等于真实物体持久态。
- **本次阅读深度：** 摘要与书目核验。

### PhysTrace / IntPhys2-Timing

- **来源/版本：** [原论文](https://arxiv.org/abs/2610.31429v1)；初始提交 2026-10-22；本次返回版本更新于 2026-10-22。`PRIMARY_PAPER`。 [作者提供的项目/代码入口](https://github.com/PhysTrace/PhysTrace)（未运行复现）。
- **问题与机制：** PhysTrace 将历史条件物理预期与视频窗口对齐，并增加 IntPhys2-Timing 的违规时段。
- **输入/学习来源：** 评估依赖 MLLM 生成的预期/判断；考官的语言先验必须独立登记。
- **实际证据：** 物理违例定位和 possible/impossible 区分。
- **不能推出 / 待区分：** 可解释描述仍可能判错，需用独立标注校验；不能把 MLLM 判词当物理真值。
- **本次阅读深度：** 摘要与书目核验。

### Dual Exam

- **来源/版本：** [原论文](https://arxiv.org/abs/2610.31066v1)；初始提交 2026-10-22；本次返回版本更新于 2026-10-22。`PRIMARY_PAPER`。
- **问题与机制：** Dual Exam 固定环境响应测试 agent，固定动作干预测试 world model，分开选择与演化。
- **输入/学习来源：** 物理、数字、社会、科学任务各有协议；并非单一视觉机器人 benchmark。
- **实际证据：** 两个分轨与一次耦合 pilot，用于分解组件失败。
- **不能推出 / 待区分：** 两轨任务/指标不同不可横比总分；分轨表现能否预测持续耦合收益仍开放。
- **本次阅读深度：** 摘要与书目核验。

### ProactEgoMem

- **来源/版本：** [原论文](https://arxiv.org/abs/2610.30089v1)；初始提交 2026-10-21；本次返回版本更新于 2026-10-21。`PRIMARY_PAPER`。
- **问题与机制：** ProactEgoMem 检验流式自我中心视频中主动捕获、状态追踪、位置追踪和记忆维护。
- **输入/学习来源：** 用户意图、视频与工具生命周期构成系统输入，学习来源随骨干而变。
- **实际证据：** 日常/科学视频以及通知/干预两级任务。
- **不能推出 / 待区分：** 有意图提示的主动记忆不等于任意未来任务记忆；考官应分离及时性、保真度与工具执行。
- **本次阅读深度：** 摘要与书目核验。
<!-- END current-cross-domain-evidence -->

<!-- BEGIN broad-vision-primary-evidence -->
<a id="broad-vision-primary-evidence"></a>

## 广义视觉理解的一手比较证据

核验日：2026-10-25。以下是外部方法与反例，覆盖经典接口、当前基础视觉与跨领域条件；未被采纳为 Clover 架构。

### 可识别性评测反例

- **一手来源：** [正式会议记录](https://proceedings.mlr.press/v337/joshi26a.html) · [论文](https://raw.githubusercontent.com/mlresearch/v337/main/assets/joshi26a/joshi26a.pdf)。
- **机制：** 用受控编码器分离数据生成条件和编码器几何，压力测试 MCC、R²、DCI 等指标。
- **输入与学习来源：** 已知真值的合成因子/编码器，是评测诊断 EV0。
- **实际证据：** 因子相关、丢失、过完备与空编码器条件下的指标误判。
- **边界与反假设：** 高指标不必然意味着定理等价类恢复；该分类也未覆盖随机编码器/离散因子或所有训练出的视觉编码器。
- **阅读深度：** 正文指标反例、分类及局限选读；未运行复现。

### 信念空间覆盖与离线评估

- **一手来源：** [正式会议记录](https://proceedings.mlr.press/v300/zhu26a.html) · [论文](https://raw.githubusercontent.com/mlresearch/v300/main/assets/zhu26a/zhu26a.pdf)。
- **机制：** 按信念空间度量覆盖而非完整历史计数，分析部分可观测离线策略评估。
- **输入与学习来源：** 离线行为数据、POMDP/策略稳定性与覆盖等假设。
- **实际证据：** 缓解某些样本误差界的历史/记忆指数依赖。
- **边界与反假设：** 信念相近须由目标策略/值稳定性支持；不能据此删除任意未来任务所需历史，或宣布长视觉流无需记忆。
- **阅读深度：** 正文问题设定、稳定性与覆盖条件选读；未复核全部证明；未运行复现。
<!-- END broad-vision-primary-evidence -->

<!-- BEGIN broad-visual-evaluation -->
<a id="broad-visual-evaluation"></a>

## 基础视觉、广义理解与原生速度的联合验收地图

以下是评测文献与协议候选，仍属 Stage 1；没有运行 Clover 实验。核心 CV 功能、一般理解、知识来源与原生速度都必须有独立证据，单一总分不能掩盖缺失功能。

| 能力 | 候选仪器/参照 | 应报告什么 | 最小区分条件 |
|---|---|---|---|
| 分类/属性/场景/实例 | [ImageNet](https://www.image-net.org/)、长尾/分布偏移和实例匹配 | 类别/属性准确率、分组表现、未知拒答和校准 | 背景替换、相近实例、罕见属性、未见组合；图文预训练与图像 SSL 对照 |
| 检测/点定位/计数 | [COCO](https://cocodataset.org/)、开放词汇/长尾与目标缺席集 | AP/召回、大小/遮挡分组、点/框误差、计数误差与误报 | 检测到但类别错、类别对但位置错分开；置信阈值和提示协议配平 |
| 语义/实例/全景/抠图 | [ADE20K](https://ade20k.csail.mit.edu/)、COCO、提示分割/抠图 | mIoU、mask AP、PQ、边界及 alpha 误差各自登记 | 真值框/点提示与自动目标发现分开；一个权重与分别训练模型分开 |
| 点追踪/光流 | [TAP-Vid](https://tapvid.github.io/)、[TAPVid-3D](https://tapvid3d.github.io/)、TAPNext++ 重检测 | 位置/可见性、AJ 与 AJ_RD、遮挡长度/重现条件、轨迹漂移 | 严格只用≤t帧；离线未来帧基线另列；查询点初始化、点数与分辨率一致 |
| 多目标追踪/再识别 | MOT 类数据、体育/拥挤/移动相机，HOTA/IDF1 等指标研究 | 检测与关联分项、身份切换、重现后的身份、完整管线时延 | 相同检测输入隔离关联收益；再比较完整感知；短暂遮挡与长时离场分别测 |
| OCR/文档/图表 | [OmniDocBench 官方资源](https://github.com/opendatalab/OmniDocBench)、场景文本和图表理解 | 转写误差、区域定位、阅读顺序、表/公式结构、细字召回和完整页耗时 | 看清文本、理解图表、利用外部语言知识分别测；精确数据版本/评价脚本保持一致 |
| 姿态/几何/空间关系 | 关键点、深度/姿态/重建与关系仪器 | 2D/3D误差、遮挡分组、尺度/相机校准、接触/支撑/包含判断 | 不把度量真值/深度/姿态标签藏入 RGB 输入；关系真值与图像接近分开 |
| 视频事件/推理/抽象 | 时间边界、关系组合、规则迁移、跨视频问题 | 事件定位、前后顺序、组成泛化、证据引用与反例敏感性 | 单帧、静态纹理、语言模板和预训练泄漏基线；未见组合和失败事件 |
| 持续状态/物理/因果/行动 | 本文既有 permanence、物理、干预、主动视觉与闭环仪器 | 身份/记忆/修正、条件预测、等价类/不确定性、决策价值 | 与上述基本功能共同报告；不能以机器人成功率代替识别/追踪/阅读能力 |
| 共同模型/原生 ultrafast | 固定视觉工作负载与[完整时延协议](foundation-models-and-systems.md#native-ultrafast-research) | 全量结果 P50/P95/P99、证据年龄、违约/丢帧、长期内存及各项能力 | 同权重、同输入/硬件/精度、单/多功能、冷/暖/长时；外部组件成本全部计入 |

OmniDocBench 官方更新记录已在 2026-04-30 从 v1.6 转为 v1.7；历史模型在 v1.6 的成绩须保留原版本，不能当成同协议的当前比较。

数据和指标的当前入口已核对到官方站点/作者项目；各数据许可、下载条件、split/hash 与脚本 revision 在实际注册实验时继续锁定，不把站点可访问当成数据已经获取。MOT 网站本次访问返回 410，不能据此使用未经核对的镜像数据；既有算法论文与官方评价资源仍可作为定位线索。TAPNext++ 项目提供的重检测指标不能与所有帧 AJ 混为一个数字。

后续比较需明确：任务专用最强参照、统一模型、受限视觉证据模型、额外教师/语言/几何模型和资源预算；它们回答不同问题。AGI 是跨任务学习、组合、迁移、修正和开放世界能力的目标，当前没有哪张表或某个 benchmark 自动授予这一结论。
<!-- END broad-visual-evaluation -->

## Contents

- [Evaluation Principles](#topic-docs-evaluation-evaluation-principles)
- [Clover Understanding Battery — Working Design](#topic-docs-evaluation-understanding-battery)
- [Evaluation & Benchmark Map](#topic-docs-evaluation-benchmark-map)
- [Benchmarks and Tasks](#topic-research-survey-benchmarks_tasks)

<a id="topic-docs-evaluation-evaluation-principles"></a>

## Evaluation Principles

### 1. Benchmarks are instruments

A benchmark answers a narrow measurement question. It does not define Clover's research problem.

### 2. Capability before leaderboard position

Before asking whether Clover is first on a leaderboard, ask whether the protocol measures a capability required by a general-purpose visual robot brain.

### 3. Use real tasks at the top of the evidence hierarchy

Controlled benchmarks are essential for diagnosis, but the eventual claim must survive unfamiliar physical environments and embodied tasks.

### 4. Separate perception success from world-model success

Detection, segmentation, depth, flow, reconstruction and tracking can each be excellent while the system still lacks a persistent, revisable world model.

### 5. Separate prediction from causality

Future prediction is evidence of useful dynamics, not automatically causal understanding. Strong causal claims require intervention-sensitive or counterfactual protocols.

### 6. Separate answer accuracy from coverage

If a system can refuse or return Unknown, report at minimum:

- coverage;
- correctness conditional on answering;
- unjustified assertion rate;
- refusal/unknown rate.

A system cannot obtain an apparent scientific win by refusing almost everything.

### 7. Track privileged information

Every evaluation should document what enters the model:

- RGB only?
- camera calibration?
- multiple cameras?
- depth?
- language?
- actions/proprioception?
- ground-truth state?

Examiner truth must not leak into the model path.

### 8. Attack shortcuts

Where possible use minimal pairs, scene/background probes, temporal shuffle, crop-only and language-only controls.

### 9. Compare representations on downstream consequences

Representation quality should eventually be judged by what it enables:

- better generalization;
- more reliable world queries;
- faster recovery;
- less data;
- better planning;
- lower compute;
- more stable long-horizon behavior.

### 10. Report evidence provenance

Distinguish:

- independently reproduced result;
- peer-reviewed/public benchmark result;
- official project result;
- vendor-reported closed-system result;
- Clover internal result.

Do not present these as equivalent evidence.

---

<a id="topic-docs-evaluation-understanding-battery"></a>

## Clover Understanding Battery — Working Design

**Status:** OPEN / design document
**Purpose:** define what a future comprehensive evaluation would need to measure without turning any one benchmark into the project objective.

### 1. Principle

The battery must answer:

> **Does the system form and use a coherent world understanding from visual evidence?**

A future scientific result should combine controlled diagnostics, open-world visual data and embodied tasks.

### 2. Capability families

#### U1 — Existence and observability

Questions:

- Is something present?
- Was it observed?
- Is it currently unobserved rather than absent?
- Is free space actually established or merely unseen?

Failure to distinguish these states is a fundamental worldview error.

#### U2 — Identity and permanence

Questions:

- Is this the same entity after viewpoint change?
- Does the entity persist through occlusion?
- Can it reappear after leaving the field of view?
- Can the system handle split/merge/deformation without arbitrary ID continuity?

Potential instruments: EgoTracks, SAM 2-style tracking baselines, custom occlusion/reappearance sequences.

#### U3 — Spatial structure

Questions:

- Where is an entity relative to the camera/world/other entities?
- Is A inside/on/behind/near B?
- What space is traversable?
- Does geometry remain coherent across views?

Potential instruments: geometry/reconstruction benchmarks, controlled multi-view tasks.

#### U4 — Temporal structure and dynamics

Questions:

- What changed?
- What is moving, and how?
- Which state is stable?
- What happens next?

Potential instruments: Perception Test, Something-Something V2, controlled trajectory tasks.

#### U5 — Intuitive physics

Questions:

- Can an object disappear without cause?
- Can solids interpenetrate?
- Is a trajectory physically continuous?
- Which events are possible/impossible?

Potential instrument: IntPhys 2.

#### U6 — Causality and counterfactuals

Questions:

- Why did the state change?
- What would happen under a different intervention?
- What action would produce a requested world-state change?

Potential instruments: CausalVQA plus future intervention twins in simulation/robotics.

#### U7 — Memory and revision

Questions:

- Can a fact survive outside the current context window?
- Can later evidence correct an earlier world belief?
- Can stable knowledge be consolidated without retaining every frame?

Potential instruments: Ego4D long-history subsets + custom long-duration visual tasks.

#### U8 — Generalization

Hold out:

- objects;
- scenes;
- compositions;
- viewpoints;
- dynamics;
- robot environments.

The key is not only OOD accuracy but whether the system knows when the new case invalidates an existing assumption.

#### U9 — Active perception

Task form:

Two or more world hypotheses remain indistinguishable from the current view. The robot must choose a visual action that resolves the ambiguity before committing to a downstream action.

This directly tests whether uncertainty can drive information-seeking behavior.

#### U10 — Decision usefulness

Compare downstream agents with and without the candidate worldview while controlling the rest of the stack as much as possible.

Measure:

- task success;
- unnecessary actions;
- replanning;
- recovery from world changes;
- search/compute cost;
- unsafe/unjustified commitments.

### 3. Anti-shortcut requirements

Every core diagnostic should consider:

- minimal pairs;
- background-only probe;
- static-frame probe;
- temporal shuffle;
- crop/scene-ID leakage;
- near-duplicate audit;
- language-only baseline when language is involved.

### 4. Pure-vision protocol labels

Results should identify the sensory protocol explicitly:

- **V0:** monocular RGB + temporal ordering;
- **V1:** RGB + camera calibration;
- **V2:** calibrated multi-camera RGB;
- **V3:** embodied active vision where actions determine future views.

Do not collapse these into one 'vision-only' number.

### 5. Evidence levels

A claim can have different evidence levels:

1. **unit/mechanism evidence**;
2. **controlled scientific diagnostic**;
3. **public benchmark evidence**;
4. **real-world visual transfer**;
5. **embodied task evidence**;
6. **unseen real-environment evidence**.

A high score at a lower level does not imply the higher levels.

### 6. Current status

This battery is a map for future evaluation. The current project phase is not yet running the complete battery. Its immediate purpose is to stop research from collapsing onto one convenient metric.

---

<a id="topic-docs-evaluation-benchmark-map"></a>

## Evaluation & Benchmark Map

Source record updated: 2026-10-14

Benchmarks are measurement instruments. This map records what each instrument is capable of measuring, what it cannot establish, and how it may eventually contribute to a broader Clover evaluation.

### 1. Intuitive physics

#### IntPhys 2

**Primary source:** https://ai.meta.com/research/publications/intphys-2-benchmarking-intuitive-physics-understanding-in-complex-synthetic-environments/

**Measures:** violation-of-expectation judgments around four macroscopic principles:

- Permanence
- Immutability
- Spatio-Temporal Continuity
- Solidity

**Strengths:** controlled synthetic environment, clean possible/impossible contrast, human reference performance.

**Known limitation for Clover:** success is still a narrow judgment task. A model could distinguish violations without constructing a persistent general-purpose world state useful for robotics.

**Role:** physics diagnostic, not project objective.

---

### 2. Shortcut resistance

#### Minimal Video Pairs (MVPBench)

**Primary source:** https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/

**Scale reported by authors:** 55K multiple-choice video QA examples.

**Core design:** each example has a visually similar minimal-change pair with the same question and opposing answer; credit requires the pair to be answered consistently.

**Strength:** explicitly attacks superficial visual/textual shortcuts.

**Role for Clover:** not only a benchmark; its minimal-pair philosophy should influence our own scientific tests.

---

### 3. Causal and counterfactual video reasoning

#### CausalVQA

**Primary source:** https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/

**Question families:**

- counterfactual;
- hypothetical;
- anticipation;
- planning;
- descriptive.

**Strength:** real-world video rather than only narrow simulation.

**Limitation:** QA correctness does not prove that the model maintains a causal world representation; language priors can contribute.

**Role:** causal reasoning diagnostic paired later with intervention-based robot/simulation experiments.

---

### 4. General video perception and reasoning

#### Perception Test

**Primary source:** https://github.com/google-deepmind/perception_test

Tasks include:

- multiple-choice video QA;
- object tracking;
- action localization;
- point tracking;
- sound localization;
- grounded video QA.

The dataset was designed around memory, abstract patterns, physics and semantics. Clover should restrict itself to compatible visual-only tasks when evaluating the SSOT.

**Role:** broad diagnostic battery, especially tracking/memory/physics subsets.

#### Something-Something V2

**Role:** motion/action representation diagnostic. Useful for measuring temporal representations, but task recognition is not world understanding by itself.

---

### 5. Egocentric visual experience

#### Ego4D

**Primary source:** https://ego4d-data.org/docs/

Ego4D documents roughly 3,600+ hours of in-the-wild egocentric video from many everyday settings, together with benchmark tasks and annotations.

Especially relevant components:

- episodic memory;
- long-term object tracking / EgoTracks;
- forecasting;
- hand-object interactions;
- object state changes.

**Role for Clover:** real visual-history research: persistence, long-term memory, anticipation and human-object interaction.

**Caution:** some Ego4D modalities include audio, gaze, stereo or 3D data. A strict Clover visual protocol must explicitly select permitted inputs.

---

### 6. Robot interaction data

#### DROID

**Primary source:** https://droid-dataset.github.io/

DROID reports 76K demonstration trajectories / 350 hours of interaction across 564 scenes and 86 tasks.

**Role for Clover:** study what action-conditioned interaction adds beyond passive video; not an immediate benchmark target.

#### Open X-Embodiment

**Primary sources:**

- https://github.com/google-deepmind/open_x_embodiment
- https://deepmind.google/blog/scaling-up-learning-across-many-different-robot-types/

Google DeepMind reports pooled data across 22 robot embodiments, more than 500 skills, about 150,000 tasks and more than one million episodes.

**Role:** cross-embodiment generalization and the question of whether diversity forces more abstract physical representations.

---

### 7. Lifelong and long-horizon robot learning

#### LIBERO

**Primary source:** https://libero-project.github.io/main.html

Focus: knowledge transfer in lifelong robot learning.

**Role:** future measurement of whether world knowledge transfers rather than catastrophically interfering across tasks.

#### CALVIN

**Primary source:** https://github.com/mees/calvin

Open benchmark for language-conditioned long-horizon manipulation and multi-step task sequences.

**Role:** future downstream test of persistent world-state usefulness. Because CALVIN is language-conditioned, it cannot by itself isolate vision-only understanding.

#### RoboCasa365

**Primary source:** https://robocasa.ai/

The 2026 release reports 365 tasks, 2,500+ kitchen scenes and 2,200+ hours of robot demonstrations, with composite/long-horizon settings and an open leaderboard.

**Role:** future generalist-robot evaluation, especially unseen compositional tasks.

---

### 8. What is still missing

No single benchmark above measures the full Clover goal:

```text
persistent visual world formation
+ open-world observability
+ physical prediction
+ causal revision
+ active perception
+ long-horizon memory
+ decision usefulness
+ real robot generalization
```

The eventual evaluation therefore needs a **battery**, not a single score.

### 9. Current policy

During the present research-mapping phase:

- catalog benchmarks;
- understand protocol and failure modes;
- do not optimize Clover around them;
- do not infer world understanding from benchmark success alone;
- defer large-scale reproduction/comparison until a new representation hypothesis is ready.

---

<a id="topic-research-survey-benchmarks_tasks"></a>

## Benchmarks and Tasks

Source record updated: 2026-10-15

Clover does not use a single benchmark as the definition of “understanding.” Benchmarks are instruments for discriminating representation hypotheses.

The current evaluation design follows:

```text
controlled capability diagnostic
+ anti-shortcut test
+ persistent/streaming memory test
+ causal/interventional test
+ real visual transfer
+ active perception
+ embodied long-horizon task
+ action usefulness
+ real-execution world-model fidelity
+ hardware/setup robustness
+ offline policy-evaluation sanity checks
```

---

### 1. Evaluation hierarchy

#### Level 1 — Cognitive / world-understanding diagnostics

Does the representation contain the structure needed to answer controlled questions about existence, identity, permanence, space, time, observability, physics, causality and counterfactuals?

#### Level 2 — Persistent world-model capability

Can the model maintain, predict, reconstruct, revise or retrieve world state across time?

#### Level 3 — Active evidence acquisition

Can the system recognize that current evidence is insufficient and deliberately obtain a better view or discriminating interaction?

#### Level 4 — Embodied brain capability

Can a robot use its world understanding to complete unfamiliar physical tasks over long horizons, recover when the world changes and avoid unjustified action?

#### Level 5 — Deployment / evidence robustness

Does the result survive:

```text
real-world execution comparison
hardware/calibration/control-loop changes
cross-simulator variation
offline-vs-rollout evaluation differences
latency / memory / runtime constraints
```

A final Clover result must eventually span all five levels.

---

### 2. Vision and learning-evidence protocol

#### Observation protocol

- **V0:** monocular RGB + temporal order/timestamp; no depth/LiDAR/tactile/force/IMU/GT pose/GT identity.
- **V1:** V0 + camera intrinsics.
- **V2:** calibrated multi-camera RGB.
- **V3:** embodied active vision; action changes future visual evidence.

#### Learning-evidence provenance

- `L0` visual self-supervision only;
- `L1` visual labels/annotations;
- `L2` language/world knowledge;
- `L3` action-conditioned demonstrations/experience;
- `L4` non-visual or privileged physical evidence.

Do not compare protocols as if they have the same information budget.

---

### 3. U1 — intuitive physics: IntPhys 2

- Official: https://ai.meta.com/research/publications/intphys-2-benchmarking-intuitive-physics-understanding-in-complex-synthetic-environments/
- Code: https://github.com/facebookresearch/IntPhys2

Use for controlled permanence, immutability, continuity and solidity diagnostics.

---

### 4. U2 — anti-shortcut physical reasoning: MVP / Minimal Video Pairs

- Official: https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/

Use minimal-change paired videos to test whether physical-understanding gains survive counterexamples.

---

### 5. U3 — causal/counterfactual video reasoning: CausalVQA

- Official: https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/

Use language-only/question-only controls because language priors are a confound.

---

### 6. U4 — general visual/video diagnostics: Perception Test

- Code/data: https://github.com/google-deepmind/perception_test

Prefer visual subsets for tracking, memory, physics, temporal relations and grounded evidence.

---

### 7. U5 — persistent world memory: PersistBench

- Paper: https://arxiv.org/abs/2609.20819
- Project/code: https://guangzhaohe.com/persistbench

Use for object permanence, motion continuity and appearance preservation after objects leave the field of view.

---

### 8. U6 — streaming episodic memory: S-EMBER

- Official: https://ai.meta.com/research/publications/s-ember-a-large-scale-benchmark-for-streaming-egocentric-memory-retrieval/
- Paper: https://arxiv.org/abs/2607.02689

Use for grounded streaming recall and temporal evidence localization.

---

### 9. U7 — relational / calibration-independent physics: Principia

- Paper: https://arxiv.org/abs/2609.04200

Use for relational physical-law consistency beyond video appearance quality.

---

### 10. U8 — 3D/state/action-grounded world-model evaluation: RoboPhys-3D

- Paper: https://arxiv.org/abs/2608.28718

Keep distinct:

```text
plausible video
≠ correct 3D/state
≠ correct executable consequence
```

---

### 11. U9 — custom object permanence / occlusion battery

Test visible→occluded→visible, leave/re-enter FOV, similar-object swaps, camera motion, hidden external movement/removal.

Measure identity continuity, false persistence/absence, uncertainty, correction latency and memory cost.

---

### 12. U10 — unknown vs unobserved

Require the system not to treat missing evidence as absence.

Measure unjustified assertion, refusal/coverage, calibration and downstream action consequences.

---

### 13. U11 — world change and belief revision

```text
world hypothesis
→ hidden/external change
→ partial new evidence
→ stale-state detection
→ revision
→ downstream query/replan
```

Measure stale detection, incorrect persistence, update locality, recovery and recompute cost.

---

### 14. U12 — intervention twins

Use same/near-same visual prefixes with controlled different interventions and different valid consequences.

Measure consequence accuracy, affected-variable localization, false causal attribution and counterfactual consistency.

---

### 15. U13 — active perception

Relevant sources:

- Bajcsy Active Perception — https://ieeexplore.ieee.org/abstract/document/5968
- Vantage — https://arxiv.org/abs/2610.11810 · https://github.com/q1xiangchen/Vantage

Measure correctness, views/actions requested, information gain, avoidable motion, latency and unnecessary evidence collection.

---

### 16. U14 — novel object dynamics

Use objects/types absent from training labels where possible. Measure dynamic prediction, adaptation, transfer and language-prior sensitivity.

---

### 17. U15 — long-horizon household task

Use multi-step find→inspect→retrieve→transport→place tasks with hidden change/recovery. Record per-step world state, decision premise, action, execution effect, memory, recovery and latency.

Relevant suites:

- LIBERO — https://libero-project.github.io/main.html · https://github.com/Lifelong-Robot-Learning/LIBERO
- CALVIN — https://github.com/mees/calvin
- RoboCasa — https://robocasa.ai/
- ManiSkill — https://github.com/haosulab/ManiSkill

---

### 18. U16 — real-execution world-model fidelity: WorldOracle

- Paper — https://arxiv.org/abs/2610.18826

WorldOracle gives an action-conditioned world model the **same initial observation and low-level action sequence** as a real execution, then compares predicted and actual outcomes.

It evaluates:

```text
physical state correctness
interaction spatial alignment
key interaction area fidelity
multi-view action coherence
```

The evaluation suite includes long multi-segment successful and failed real executions across multiple dynamics/embodiments.

Use for:

> whether a predicted world rollout matches what actually happened, not merely whether it looks plausible.

Do not infer policy quality or complete world understanding from this benchmark alone.

---

### 19. U17 — hardware/setup robustness: LIBERO-RIG

- Paper — https://arxiv.org/abs/2610.18843

LIBERO-RIG holds tasks fixed while perturbing eleven hardware/setup axes, including camera mounting/optics, camera-arm calibration, actuation gain, control rate, proprioceptive noise, base pose, table height and gripper pads. Each axis has five severity levels, totaling 210 conditions across four LIBERO suites.

Reported pooled VLA success:

```text
nominal       0.932
mid severity  0.767
highest       0.509
```

Use for distinguishing:

```text
scene/task generalization
≠ hardware/calibration/control-loop robustness
```

---

### 20. U18 — long-horizon scaling: LADDER

- Paper — https://arxiv.org/abs/2610.18053
- Project — https://ladder.insait.ai

LADDER scales from 1 to 10 subgoals within controlled task families: 145 tasks, eight categories, two embodiments and 2,024 simulated episodes per evaluated system.

Reported signal:

```text
low-level policy: 85.4% at one subgoal
→ near zero on extended tasks
```

Orchestration improves performance but remains bounded by physical execution errors; a GPT-6 Astra tool-selection setup is reported around 62% with substantial time/cost.

Use for separating planning/orchestration failures from low-level execution compounding.

---

### 21. U19 — rollout-free offline policy evaluation: RoboFQE

- Paper — https://arxiv.org/abs/2610.18699

RoboFQE estimates target-policy return from offline robot trajectories without running new simulator, learned-world-model or real-world rollouts.

Use as an **EV4/offline sanity-check instrument** for policy ranking when real robot rollouts are unavailable or expensive.

Important boundary:

```text
offline policy evaluation
≠ closed-loop deployment validation
```

Its value is especially relevant when autoregressive video evaluators accumulate long-horizon prediction error.

---

### 22. U20 — partial-observability memory representation: Grid or Nodes?

- Paper — https://arxiv.org/abs/2610.18637

This controlled FloWM study compares a dense grid memory to an oracle-fed node/Kalman representation under partial observability.

Reported diagnostic signals include:

```text
out-of-view node memory: 14 KB
FloWM grid:             5.6 MB

diagonal OOD motion:
FloWM detection         11%
unchanged tracker       93%
```

The oracle node memory is not a deployable learned baseline. Use this study to motivate measurements of:

```text
memory bytes
representation inductive bias
out-of-distribution motion
probe/readout dependence
```

---

### 23. Supporting validation resources — not standalone “understanding” benchmarks

#### RoboSimStudio

- Paper — https://arxiv.org/abs/2610.18835
- Project — https://robosimstudio.github.io

Use for explicit Real2Sim experiments where solver/contact model/physical parameters are editable and simulator hypotheses can be compared against observed behavior.

#### RoboWM-Bench

- Paper — https://arxiv.org/abs/2604.19092

Use for visual-plausibility vs executable-behavior distinction.

#### RoboTrustBench

- Paper — https://arxiv.org/abs/2606.01600

Use for constraint-sensitive, counterfactual and adversarial world-model evaluation.

#### Video2World

- Paper — https://arxiv.org/abs/2610.04432

Use for geometric/dynamic/functional correctness of reconstructed simulation worlds.

---

### 24. Required reporting dimensions

Every serious architecture/baseline comparison should report a vector rather than one scalar.

At minimum:

```text
in-domain
held-out scene
held-out object/composition
held-out dynamics
camera shift
hardware/setup shift
real-world transfer
real-execution rollout fidelity
task/query correctness
coverage / answer rate
unjustified assertion rate
unknown/refusal quality
memory/persistence
recovery
latency p50/p95/p99
memory bytes
energy when measurable
```

Where relevant also include physical consistency, intervention accuracy, temporal evidence localization, update locality, planning/search cost, offline-evaluation uncertainty and task success.

Use Pareto analysis rather than hiding trade-offs inside one weighted score.

---

### 25. Anti-shortcut / robustness audit

Challenge results with:

```text
background-only
foreground-only
single-frame
temporal shuffle
reversed video
crop
camera metadata
scene ID
duplicate / near-duplicate
language-only
question-only
minimal-change paired video
camera calibration perturbation
control-rate perturbation
latency / frame-drop injection
cross-simulator replay
```

If a shortcut reproduces the score, the original result is weak evidence for world understanding.

---

### 26. First Understanding Battery candidate — expanded

```text
U1  IntPhys 2                         intuitive physics
U2  MVP                               anti-shortcut physical understanding
U3  CausalVQA                         causal/counterfactual video reasoning
U4  Perception Test visual subsets    tracking/memory/real-video perception
U5  PersistBench                      object permanence outside FOV
U6  S-EMBER                           streaming episodic memory
U7  Principia                         relational physical consistency
U8  RoboPhys-3D                       state/action-grounded world-model quality
U9  custom occlusion/reappearance     identity/permanence
U10 custom unknown/unobserved         epistemic correctness
U11 custom world change/revision      stale detection/belief revision
U12 custom intervention twins         intervention sensitivity
U13 custom active perception          information-seeking vision
U14 custom novel dynamics             open-world physical transfer
U15 long-horizon embodied task        action usefulness/recovery
U16 WorldOracle                       predicted-vs-real action-conditioned futures
U17 LIBERO-RIG                        hardware/setup robustness
U18 LADDER                            horizon scaling / compounding execution
U19 RoboFQE                           rollout-free offline policy evaluation
U20 Grid-or-Nodes diagnostic          memory efficiency / inductive bias
```

This battery is intentionally heterogeneous. U19 and U20 are supporting diagnostics, not replacements for real closed-loop evaluation.

---

### Evaluation principle

```text
benchmark battery
+ shortcut resistance
+ persistent memory
+ causal intervention
+ real visual transfer
+ active evidence gathering
+ embodied long-horizon tasks
+ action usefulness
+ real-execution grounding
+ hardware/setup perturbation
+ validation-evidence tier
```

not:

```text
one benchmark → “understanding solved”
```

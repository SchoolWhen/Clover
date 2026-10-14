# Clover

**开放研究：机器如何仅通过视觉理解真实世界？**

> **最高研究问题：** How can a machine understand the real world through vision alone?
>
> **长期成果目标：** 构造一个仅通过视觉形成真实世界理解，并能据此决策和行动的通用机器人大脑。

Clover 是一个长期公开研究项目。**问题保持稳定，答案保持开放。** 仓库会分别记录事实、外部证据、研究假设、研究决策、评测与未来实现，使项目能够随着证据更新而改变答案，而不改变最高问题。

## 当前阶段：背景研究 / 问题重建

2026-10-14 的 Research Reset 将 Clover 从“证明既有架构”转为“先把问题和已有答案研究清楚，再决定下一代表示”。

当前严格顺序是：

```text
Background Research / Research Map
→ Baseline Setup
→ Understanding Battery
→ Failure Matrix
→ Representation Hypothesis
→ World Formation / Learning
→ Robot Brain
→ Real-world Evaluation
→ Hardware Co-design
```

因此当前**不冻结新的 Clover 核心表示，也不默认 field、CSP、SEP、licence、Evidence Replay、显式 state、latent state 或某一种神经网络架构是答案**。

## 推荐阅读顺序

1. [SSOT.md](SSOT.md) — 最高研究问题、长期目标和当前科学立场。
2. [RESEARCH_OVERVIEW.md](research/survey/RESEARCH_OVERVIEW.md) — 研究问题 → 8 大领域 → 6 个核心矛盾 → baseline → battery → Failure Matrix 的总览图。
3. [BACKGROUND_RESEARCH.md](research/survey/BACKGROUND_RESEARCH.md) — 对整个问题空间的系统背景研究。
4. [Research Dossiers](research/dossiers/README.md) — 8 个领域的纵向深度调研。
5. [SOURCE_MAP.md](research/survey/SOURCE_MAP.md) — 每一项外部证据对应的准确网址、证据等级、已证明能力、未证明边界与 Clover 落点。
6. [Survey README](research/survey/README.md) — 当前研究导航。
7. [FRONTIER_METHODS.md](research/survey/FRONTIER_METHODS.md) — 主要路线的竞争性比较。
8. [RESEARCH_QUESTIONS.md](research/survey/RESEARCH_QUESTIONS.md) — 下一代架构冻结前必须回答的问题。
9. [PAPERS.md](research/survey/PAPERS.md) — 论文、官方页面、代码索引。
10. [BENCHMARKS_TASKS.md](research/survey/BENCHMARKS_TASKS.md) — Understanding Battery 与任务地图。
11. [DATASETS_CODE.md](research/survey/DATASETS_CODE.md) — 数据、代码、checkpoint 与复现资源。

## 八个纵向研究领域

当前背景研究已经拆成 8 个可独立持续扩展的 dossier：

- [R-A — Observability / Epistemology](research/dossiers/R-A-observability-epistemology.md)：partial observability、未知/不可观测、belief state、视觉可辨识性。
- [R-B — Geometry](research/dossiers/R-B-geometry.md)：经典几何、optical flow、SLAM、learned geometry，明确“几何已经解决了什么”。
- [R-C — Representation](research/dossiers/R-C-representation.md)：explicit / latent / object-centric / dense / hybrid representation 的竞争。
- [R-D — Memory / Persistence](research/dossiers/R-D-memory-persistence.md)：object permanence、episodic memory、evidence retention、belief revision、forgetting。
- [R-E — Physics](research/dossiers/R-E-physics.md)：intuitive / quantitative / relational / intervention / execution-grounded physics。
- [R-F — Causality / Interaction](research/dossiers/R-F-causality-interaction.md)：causal identifiability、intervention、counterfactual、interaction data。
- [R-G — World Model ↔ Action](research/dossiers/R-G-world-action.md)：VLA、WAM、planner，以及 persistent worldview 是否真的比 direct policy 有价值。
- [R-H — Active Perception / Lifelong](research/dossiers/R-H-active-perception-lifelong.md)：主动获取视觉证据、continual learning、self-play、长期世界形成。

每个 dossier 都按同一模板组织：

```text
fundamental question
→ canonical foundations
→ current frontier
→ exact URL
→ demonstrated capability
→ limitation / confound
→ unresolved contradiction
→ baseline
→ discriminating experiment
→ kill condition
→ Clover implication
```

## 我们真正研究什么

Clover 不以某一个 benchmark、CPU 路线、Transformer 对立面或某一种既有架构为目标。

真正的问题是：

> **机器仅凭视觉经验，需要形成什么内部结构，才能对真实世界产生稳定、可迁移、可预测、能处理未知与变化、并真正帮助决策和行动的理解？**

核心能力至少包括：

- existence / observability；
- identity / object permanence；
- 空间与时间结构；
- dynamics / intuitive physics；
- uncertainty / unknown / unobserved；
- causality / intervention / counterfactual；
- persistent memory / belief revision；
- active perception；
- open-world generalization；
- 对 planning / action / recovery 的实际价值。

## 当前六个核心竞争性矛盾

```text
C1 explicit state vs distributed latent vs hybrid / identifiable state
C2 reconstruction vs prediction vs generation
C3 object-centric vs dense scene representation
C4 passive observation vs interaction
C5 persistent world state vs long context / direct policy
C6 evidence-grounded belief vs plausible generative completion
```

这些问题比旧 Clover 的模块名称更基础。下一代 Clover 应当由这些矛盾的实验结果推导出来，而不是从旧机制出发寻找支持材料。

## “Vision alone”需要双轴描述

### 观测协议

- `V0`：单目 RGB + 时间顺序；
- `V1`：V0 + 相机内参；
- `V2`：标定后的多相机 RGB；
- `V3`：机器人可以主动移动来获得新的视觉证据。

### 学习证据来源

背景研究进一步记录：

- `L0`：纯视觉自监督；
- `L1`：视觉标签/标注；
- `L2`：语言/世界知识监督；
- `L3`：带动作的演示/交互经验；
- `L4`：非视觉或 privileged physical evidence，例如 proprioception、force/tactile、IMU、depth/LiDAR、simulator state。

这能避免把“部署时只输入 RGB”误写成“这个系统只从视觉学到了知识”。

## 外部资料如何进入仓库

新的论文、技术报告或产业信号必须经过：

```text
外部来源
→ 精确网址
→ 证据等级
→ 它真正证明了什么
→ 它没有证明什么
→ 它解决了哪个研究矛盾
→ 对应的 Clover 研究落点
```

优先级：

```text
primary paper / preprint
→ official technical/model page
→ official open-source repository
→ official reported result
→ secondary news / signal
```

新闻归档只用于发现线索；能进入核心 Survey 的长期结论必须尽量回到 primary / official source。

## 我们不预设

Clover 不预设：

- CPU 一定优于 GPU；
- 显式表示一定优于 latent；
- field / object / geometry / token 中某一个一定是最终 primitive；
- Transformer 天然不适合理解世界；
- reconstruction、prediction 或 generation 中某一个一定正确；
- persistent explicit worldview 一定比 direct policy 强；
- 一个 benchmark 可以定义“理解”；
- 当前 Clover Research Prototype 就是最终答案。

## 最终落点

```text
视觉经验
 ↓
世界理解
 ↓
决策
 ↓
工具 / capability 选择
 ↓
执行
 ↓
新的视觉经验
 └──────────────→ 更新世界理解
```

这只是长期产品目标，不代表内部表示已经冻结。

更多内容见：

- [RESEARCH_OVERVIEW.md](research/survey/RESEARCH_OVERVIEW.md)
- [research/dossiers/README.md](research/dossiers/README.md)
- [PRINCIPLES.md](PRINCIPLES.md)
- [STATUS.md](STATUS.md)
- [ROADMAP.md](ROADMAP.md)
- [BACKGROUND_RESEARCH.md](research/survey/BACKGROUND_RESEARCH.md)
- [SOURCE_MAP.md](research/survey/SOURCE_MAP.md)
- [Survey README](research/survey/README.md)

**保护问题，不保护当前答案。**

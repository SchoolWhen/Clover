# Clover

**开放研究：机器如何仅通过视觉理解真实世界？**

> **最高研究问题：** How can a machine understand the real world through vision alone?
>
> **长期目标：** 构造一个仅通过视觉形成真实世界理解，并能据此决策和行动的通用机器人大脑。

Clover 是一个长期公开研究项目。**问题固定，答案开放。**

## 当前最重要的事情

目前只激活第一阶段：**Research / 调研**。

完整科研流程统一为：

```text
1 Research 调研
→ 2 Analysis 分析
→ 3 Synthesis 总结 / 综合
→ 4 Innovation 创新 / 原创算法假设
→ 5 Implementation 实现
→ 6 Evaluation 实验与 Results
→ 7 Reflection 反思 / 复盘
↺ 下一轮研究
```

这套顺序描述的是“我们对问题了解到了什么程度”，不是软件版本号。

## 新 Agent 推荐阅读顺序

1. [SSOT.md](SSOT.md) — 最高问题、长期目标、科学边界。
2. [research/PIPELINE.md](research/PIPELINE.md) — 七阶段科研流程。
3. [research/RESEARCH.md](research/RESEARCH.md) — 当前最重要的全量调研目录。
4. [AGENTS.md](AGENTS.md) — agent 工作规则。
5. [STATUS.md](STATUS.md) — 当前状态与非目标。
6. [research/README.md](research/README.md) — 扁平化研究导航。

## Stage 1 — Research / 调研

当前阶段优先做“材料覆盖”，暂时不急着提出下一代 Clover 算法。

需要尽可能收集：

```text
涉及哪些研究方向
经典理论是什么
最新强方法是什么
primary paper 在哪里
official project 在哪里
代码 / checkpoint 在哪里
dataset 在哪里
benchmark 在哪里
哪些团队正在持续做
方法真正证明了什么
方法还没有证明什么
训练时到底用了什么信息
还有哪些明显缺口没有调查
```

当前主入口：[research/RESEARCH.md](research/RESEARCH.md)。

它已经把问题扩展到 30+ 个相关方向，包括但不限于：

- inverse problem / observability / uncertainty / POMDP；
- 人类视觉与 developmental cognition；
- classical geometry / SfM / VO / SLAM；
- optical flow / correspondence / tracking；
- static SSL；
- predictive video representation；
- learned geometry；
- NeRF / 3DGS / 4D reconstruction；
- object-centric representation；
- scene graph / semantic mapping；
- persistent / episodic memory；
- belief revision / forgetting；
- intuitive / quantitative / relational physics；
- physics-informed / structured world model；
- causal representation learning；
- counterfactual reasoning；
- active perception；
- system identification；
- generative world model；
- world-action model；
- VLA / direct policy；
- embodied reasoning；
- robot foundation model；
- human / egocentric video learning；
- affordance learning；
- model-based control；
- semantic memory；
- uncertainty calibration / OOD；
- continual learning；
- simulation / synthetic data；
- robot datasets；
- benchmark / anti-shortcut methodology；
- systems integration / compounded failure。

如果以后发现任何新方向会实质影响母问题，即使它不属于现有分类，也应该直接加入 Research。

## Stage 2 — Analysis / 分析

调研材料足够广以后，再对真正重要的方法逐个做小报告。

每个方法至少分析：

```text
它解决什么问题
输入是什么
训练监督是什么
内部 representation 是什么
核心机制是什么
objective 是什么
如何处理时间 / memory
如何处理 geometry / object / physics / causality
如何接 action
dataset / benchmark 是什么
reported result 是什么
优点是什么
缺点是什么
confound 是什么
failure mode 是什么
能不能复现
```

模板见 [research/ANALYSIS.md](research/ANALYSIS.md)。

## Stage 3 — Synthesis / 总结综合

把逐方法分析放在同一坐标系里比较：

```text
优点
缺点
trade-off
capability matrix
Failure Matrix
共同瓶颈
哪些问题已经基本解决
哪些问题一直解决不了
哪里值得提出新算法
```

模板见 [research/SYNTHESIS.md](research/SYNTHESIS.md)。

## Stage 4 — Innovation / 创新

这才是“我们自己的东西”正式出现的阶段。

Innovation 可以包含：

- 原创 representation hypothesis；
- 新变量 / 新数学形式；
- 新 learning principle；
- 新 memory / update mechanism；
- 新 causal / active perception mechanism；
- 新 algorithm。

但必须从已经确认的 gap 出发：

```text
field gap
→ 为什么现有方法不够
→ Clover-original hypothesis
→ 数学 / 算法定义
→ prediction
→ falsifier
→ experiment
```

模板见 [research/INNOVATION.md](research/INNOVATION.md)。

## Stage 5–7

- [Implementation](research/IMPLEMENTATION.md) — 具体代码和可复现实验实现。
- [Evaluation](research/EVALUATION.md) — experiments / Results / ablation / real-world tests。
- [Reflection](research/REFLECTION.md) — 解释结果、复盘失败、删除错误假设、开始下一轮。

## 深度材料仍然保留

扁平 stage 文件是第一入口；详细资料继续作为支撑层：

- [Source Map](research/survey/SOURCE_MAP.md)
- [Background Research](research/survey/BACKGROUND_RESEARCH.md)
- [Research Overview](research/survey/RESEARCH_OVERVIEW.md)
- [Frontier Methods](research/survey/FRONTIER_METHODS.md)
- [Papers](research/survey/PAPERS.md)
- [Benchmarks & Tasks](research/survey/BENCHMARKS_TASKS.md)
- [Datasets & Code](research/survey/DATASETS_CODE.md)
- [Deep Dossiers](research/dossiers/README.md)

它们是 Research / Analysis 的材料库，不是另外一套阶段体系。

## Vision alone 的双轴说明

### 观测协议

- `V0`：单目 RGB + 时间顺序；
- `V1`：V0 + 相机内参；
- `V2`：标定多相机 RGB；
- `V3`：机器人主动移动来取得新的视觉证据。

### 学习证据来源

- `L0`：视觉自监督；
- `L1`：视觉标签 / annotation；
- `L2`：语言 / world knowledge；
- `L3`：带动作的 demonstration / interaction；
- `L4`：非视觉或 privileged physical evidence。

这可以避免把“部署只输入 RGB”误认为“所有世界知识都来自视觉”。

## 当前不做什么

现在不冻结 field、CSP、licence、explicit state、latent state、Transformer 或任何新 Clover core algorithm。

旧 Clover 机制统一作为未来 Innovation 阶段的候选 idea；是否保留要由后续 Analysis、Synthesis 和 Evaluation 决定。

## 长期产品闭环

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

---

**先把世界调研完整，再分析；先把分析总结清楚，再创新。**

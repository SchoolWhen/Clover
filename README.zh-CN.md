# Clover

**开放研究：机器如何仅通过视觉理解真实世界？**

> **最高研究问题：** How can a machine understand the real world through vision alone?
>
> **长期目标：** 构造一个仅通过视觉形成真实世界理解，并能据此决策和行动的通用机器人大脑。

Clover 是一个长期公开研究项目。**问题固定，答案开放。**

## 当前阶段

目前只激活：**Stage 1 — Research / 调研**。

```text
1 Research 调研
→ 2 Analysis 分析
→ 3 Synthesis 综合总结
→ 4 Innovation 原创假设 / 算法
→ 5 Implementation 实现
→ 6 Evaluation 实验与结果
→ 7 Reflection 反思 / 复盘
↺ 下一轮
```

当前原则：**coverage before commitment**。先把问题空间调查完整，再决定 Clover 自己应该发明什么。

## 新 Agent 推荐阅读顺序

1. [SSOT.md](SSOT.md)
2. [research/PIPELINE.md](research/PIPELINE.md)
3. [research/RESEARCH.md](research/RESEARCH.md)
4. [research/RESEARCH_STATE_VARIABLES.md](research/RESEARCH_STATE_VARIABLES.md)
5. [research/RESEARCH_IDENTIFIABILITY.md](research/RESEARCH_IDENTIFIABILITY.md)
6. [research/RESEARCH_OBSERVATION_PHYSICS.md](research/RESEARCH_OBSERVATION_PHYSICS.md)
7. [research/RESEARCH_PHYSICAL_PROPERTIES.md](research/RESEARCH_PHYSICAL_PROPERTIES.md)
8. [research/RESEARCH_SUFFICIENT_STATE.md](research/RESEARCH_SUFFICIENT_STATE.md)
9. [research/RESEARCH_STATE_ALIASING.md](research/RESEARCH_STATE_ALIASING.md)
10. [research/RESEARCH_ADAPTIVE_ABSTRACTION.md](research/RESEARCH_ADAPTIVE_ABSTRACTION.md)
11. [research/RESEARCH_VALUE_OF_INFORMATION.md](research/RESEARCH_VALUE_OF_INFORMATION.md)
12. [research/RESEARCH_OPEN_WORLD_EPISTEMICS.md](research/RESEARCH_OPEN_WORLD_EPISTEMICS.md)
13. [research/RESEARCH_MODEL_DISCOVERY.md](research/RESEARCH_MODEL_DISCOVERY.md)
14. [research/RESEARCH_FRONTIER.md](research/RESEARCH_FRONTIER.md)
15. [AGENTS.md](AGENTS.md)
16. [STATUS.md](STATUS.md)
17. [research/README.md](research/README.md)

## Stage 1 当前问题链

```text
有哪些相关研究？
↓
真实世界里到底有哪些状态？
↓
这些状态怎样经过光学 / 材料 / 相机变成 RGB？
↓
哪些隐藏状态能由当前证据辨识？
↓
哪些物理属性需要时间、主动视角、交互或非视觉证据？
↓
内部 world state 至少需要保留什么信息？
↓
什么时候不同真实世界被压成同一个 latent / state？
↓
状态应该以什么粒度、什么时间尺度表示？
↓
当前证据不足时，下一眼 / 下一次 probing action 应该选什么？
↓
如果当前 hypothesis set 本身不完整、模型已经过期或实验不安全怎么办？
↓
怎样管理 hypothesis、mechanism、experiment、falsification 与 provenance？
↓
哪些最新方法 / dataset / benchmark 真正区分这些答案？
```

## Stage 1 核心区分

```text
pixels ≠ world state

从像素统计上能猜对
≠
物理上由像素唯一可辨识

vision alone ≠ passive vision only

当前证据本来就无法区分两个世界
≠ representation failure

证据里有信息但 encoder 丢掉了
= 潜在 representation failure

完整物理描述
≠ 最小 predictive state
≠ 最小 control-sufficient state
≠ 通用 world state

最 informative 的动作
≠ 考虑风险 / 成本 / 不可逆性 / permission 后最值得执行的动作

已知 hypothesis 内部的不确定性
≠ 正确 hypothesis 根本不在当前集合中

当前 state 不确定
≠ world model 本身已经失效

parameter estimation
≠ model selection
≠ mechanism discovery
≠ open-world model expansion

reflection ≠ falsification

当前最好 hypothesis ≠ 永久真理
```

## 目前 Stage 1 已覆盖

- inverse problem / observability / identifiability / POMDP；
- image formation / inverse rendering / camera acquisition；
- transparency / reflection / refraction / blur / rolling shutter；
- geometry / SfM / VO / SLAM / correspondence / tracking；
- static/video SSL 与 learned geometry / NeRF / 3DGS / 4D；
- object / scene graph / semantic map / persistent memory；
- mass / inertia / friction / stiffness / temperature / viscosity / materials；
- rigid / articulated / deformable / fluid / granular dynamics；
- cutting / splitting / merging / breakage 等不可逆拓扑变化；
- physical / causal / counterfactual reasoning；
- active perception / system identification / intervention；
- world model / WAM / VLA / direct policy；
- belief state / predictive state / information state / sufficiency；
- state aliasing / state abstraction / hierarchical / multi-timescale state；
- value of information / probing action / epistemic safety；
- open-world hypothesis generation / model mismatch / changepoint；
- model-class / mechanism discovery / Bayesian experiment design；
- hypothesis provenance / falsification / refutation memory；
- self/body schema / embodiment mismatch；
- help-seeking / abstention / human escalation；
- recursive belief / Theory of Mind / social permission；
- OOD / continual adaptation / simulation / datasets / benchmarks / systems integration。

## 当前 frontier（截至 2026-10-14）

入口：[research/RESEARCH_FRONTIER.md](research/RESEARCH_FRONTIER.md)

当前值得后续 Stage 2 深拆的代表工作包括：

- SpecWM — https://arxiv.org/abs/2610.15429
- DR-WM — https://arxiv.org/abs/2610.17630
- Gemini 4 Argon for Robotics — https://developers.googleblog.com/gemini-4-argon-for-robotics/
- Mental-Models — https://arxiv.org/abs/2610.12453
- Identifiable World Models — https://arxiv.org/abs/2610.07028
- RobotWorld — https://arxiv.org/abs/2610.10409
- Video2World — https://arxiv.org/abs/2610.04432
- HUME — https://arxiv.org/abs/2607.06501
- Learning Task-Sufficient World Models — https://proceedings.mlr.press/v306/feng26aa.html
- robust / constrained Bayesian experimental design — https://proceedings.mlr.press/v300/tang26d.html · https://proceedings.mlr.press/v306/guo26g.html

这些都是 **research objects / comparators**，不是 Clover 组件。

## Vision alone 双轴协议

### Observation protocol

- `V0`：单目 RGB + 时间顺序；
- `V1`：V0 + 相机内参；
- `V2`：标定多相机 RGB；
- `V3`：机器人主动行动，从而改变未来视觉证据。

### Learning evidence provenance

- `L0`：视觉自监督；
- `L1`：视觉标签 / annotation；
- `L2`：语言 / world knowledge；
- `L3`：带动作的 demonstration / interaction；
- `L4`：非视觉或 privileged physical evidence。

所以：

```text
部署时只有 RGB
≠
知识只来自视觉
```

## 后续阶段

Stage 2 才逐方法做 one-method-one-report；Stage 3 横向总结优缺点与共同 gap；Stage 4 才正式提出 Clover-original hypothesis / algorithm；之后再实现、实验、反思。

## 当前不做什么

目前不冻结 explicit/latent/object/field/token、hierarchy、information-gain objective、Transformer/non-Transformer 或任何新 Clover core algorithm。

旧 Clover 机制仍然只是未来 Innovation 阶段的候选 idea，是否保留必须由 Research → Analysis → Synthesis → Evaluation 决定。

---

**先把世界调研完整，再分析；先把分析总结清楚，再创新。**
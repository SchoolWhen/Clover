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

当前原则是：**coverage before commitment**。先把问题空间调查完整，再决定 Clover 自己应该发明什么。

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
12. [research/RESEARCH_FRONTIER.md](research/RESEARCH_FRONTIER.md)
13. [AGENTS.md](AGENTS.md)
14. [STATUS.md](STATUS.md)
15. [research/README.md](research/README.md)

## Stage 1 当前问题链

现在不是直接问“下一代 Clover 架构长什么样”，而是依次回答：

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
什么时候不同真实世界被压成了同一个 latent / state？
        ↓
状态应该以什么粒度、什么时间尺度表示？
        ↓
当前证据不足时，下一眼 / 下一次 probing action 应该选什么？
        ↓
哪些方法 / dataset / benchmark 能真正区分这些答案？
```

## Stage 1 的几个核心区分

```text
pixels
≠
world state

从像素统计上能猜对
≠
物理上由像素唯一可辨识

vision alone
≠
passive vision only

当前证据本来就无法区分两个世界
≠
representation failure

证据里有信息但 encoder 丢掉了
=
潜在 representation failure

完整物理描述
≠
最小 predictive state
≠
最小 control-sufficient state
≠
通用 world state

当前任务 sufficient
≠
未来未知任务 sufficient

最小 state
≠
所有时间尺度上都最好的 state

最 informative 的动作
≠
考虑风险 / 成本 / 不可逆性后最值得执行的动作
```

## 新增的三个 Stage-1 研究面

### 1. State Aliasing / Representation Failure

[research/RESEARCH_STATE_ALIASING.md](research/RESEARCH_STATE_ALIASING.md)

研究：不同真实世界或历史什么时候会被压成同一个内部状态。

包括：

```text
perceptual aliasing
history aliasing
representation aliasing
action / embodiment aliasing
causal aliasing
task-conditioned aliasing
```

重要参考包括 λ-discrepancy、PO-PDDL、observable quotient world models、bisimulation/state abstraction。

### 2. Adaptive Abstraction / State Granularity

[research/RESEARCH_ADAPTIVE_ABSTRACTION.md](research/RESEARCH_ADAPTIVE_ABSTRACTION.md)

研究：world state 是否应该根据任务、时间尺度、事件、空间、uncertainty 和 embodiment 动态改变表示粒度。

目前明确保留：

```text
task-conditioned abstraction
multi-timescale state
event-driven state
coarse-to-fine state
entity / relation / functional-role state
uncertainty-conditioned detail
embodiment-conditioned state
open-world recoverability
```

### 3. Value of Information / Probing Actions

[research/RESEARCH_VALUE_OF_INFORMATION.md](research/RESEARCH_VALUE_OF_INFORMATION.md)

研究：当证据不足时，机器人应该怎样选择下一次观察或交互来最快减少关键 uncertainty。

需要区分：

```text
state information
parameter information
mechanism information
causal-structure information
task-interpretation information
```

以及 probing action 的：

```text
time
energy
risk
irreversibility
world disturbance
safety
```

## 这轮新增发现的其他缺口

暂时不再拆更多顶层文件，但 Stage 1 会继续追踪：

```text
open-world hypothesis generation
— 当前所有 hypothesis 都解释不了新证据时怎么办？

non-stationarity / change-point detection
— 世界动力学、任务规则、embodiment 发生变化时怎样发现？

self / embodiment model
— 怎样区分机器人自身、controller、camera 的变化和外部世界变化？

representation reversibility
— 之前为了压缩而丢掉的信息，未来任务需要时还能否从保留的 evidence/provenance 恢复？

multi-timescale / event-time state
— 高频物理过程与低频语义事件是否应该用不同更新频率？

structured / equivariant memory
— 是否能利用 self-motion / world-motion 结构维护 out-of-view state，而不是暴力保存全部历史？

epistemic-action safety
— 为了获得信息而做的实验本身可能危险、不可逆或改变世界。

model-structure uncertainty
— 不只是“不知道 state”，还可能“不知道应该用哪个动力学 / 因果模型”。

meta-reasoning
— 什么时候应该继续思考、再看一眼、移动、probe、询问、等待，还是直接行动？
```

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

### Stage 2 — Analysis

对真正重要的方法逐个做 one-method-one-report 机制分析。

### Stage 3 — Synthesis

统一比较优点、缺点、trade-off、capability matrix、Failure Matrix 和共同 gap。

### Stage 4 — Innovation

只有当 gap 已被充分证明后，才正式提出 Clover-original hypothesis / algorithm。

### Stage 5–7

实现 → 实验 → 反思。

## 当前不做什么

目前不冻结 explicit/latent/object/field/token、hierarchy、information-gain objective、Transformer/non-Transformer 或任何新 Clover core algorithm。

旧 Clover 机制仍然只是未来 Innovation 阶段的候选 idea，是否保留必须由 Research → Analysis → Synthesis → Evaluation 决定。

---

**先把世界调研完整，再分析；先把分析总结清楚，再创新。**

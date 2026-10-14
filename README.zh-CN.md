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
12. [research/RESEARCH_OPEN_WORLD_EPISTEMICS.md](research/RESEARCH_OPEN_WORLD_EPISTEMICS.md)
13. [research/RESEARCH_MODEL_DISCOVERY.md](research/RESEARCH_MODEL_DISCOVERY.md)
14. [research/RESEARCH_ENGINEERING_VALIDATION.md](research/RESEARCH_ENGINEERING_VALIDATION.md)
15. [research/RESEARCH_FRONTIER.md](research/RESEARCH_FRONTIER.md)
16. [AGENTS.md](AGENTS.md)
17. [STATUS.md](STATUS.md)
18. [research/README.md](research/README.md)

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
如果当前 hypothesis set 不完整、模型已经失效、实验不安全怎么办？
↓
怎样做 mechanism discovery、实验设计、falsification 和 provenance？
↓
模型以后能不能在真实 edge 约束下运行？没有真机时怎样逐级验证？
↓
哪些方法 / dataset / benchmark 能真正区分这些答案？
```

## 新增：Engineering / Deployment / Validation

[research/RESEARCH_ENGINEERING_VALIDATION.md](research/RESEARCH_ENGINEERING_VALIDATION.md)

当前本地参考开发环境是：

```text
Mac mini + Apple M4
```

但必须区分：

```text
当前开发机
≠ 最终机器人 edge computer
≠ 科学假设
```

Stage 1 现在正式调研：

```text
MLX / Core AI / Core ML / ExecuTorch
CPU / GPU / ANE / NPU 映射
quantization / palettization / pruning
latency / p95 / p99 / deadline miss
unified-memory pressure
persistent-state memory
thermal / sustained runtime
camera→state→decision→action 全链路 latency
```

不能只看平均 FPS。

尤其需要检查加速是否改变科学能力：

```text
quantization 是否损伤 uncertainty calibration？
memory pruning 是否损伤 object permanence？
缩短 history 是否产生 state aliasing？
降低 resolution 是否损伤 physical identifiability？
batching / remote inference 是否破坏 control deadline？
异步执行是否让 belief 变 stale？
```

## 目前没有真实机器人：验证必须分层

现在明确使用：

```text
EV0 数学 / synthetic diagnostic
EV1 单 simulator controlled test
EV2 simulator domain randomization
EV3 sim2sim
EV4 offline real-data validation
EV5 real2sim / digital-twin validation
EV6 deployment-runtime / compute hardware-in-the-loop
EV7 proxy physical hardware
EV8 target real robot
```

所以：

```text
sim-only success
≠ sim2real success
≠ target-robot validation
```

没有真机意味着**claim 要更保守**，不是意味着现在不能验证。

## 当前 Mac M4 下的 simulation 策略

### 本地优先

MuJoCo：
https://github.com/google-deepmind/mujoco

适合本地做 controlled physics、state/aliasing/system-identification diagnostic、model-based control 和 sim2sim 的一个基准端。

### 有条件再远程使用 Linux + NVIDIA

Isaac Sim / Isaac Lab 更适合大规模 GPU simulation、photorealistic sensor generation、domain randomization 和 NVIDIA 生态实验，但当前标准 Isaac Sim 并不支持 macOS / 非 NVIDIA hardware。

所以不要为了 Stage 1 强行购买或搭建重型 GPU 基础设施；需要时再使用 remote/cloud Linux NVIDIA。

### ManiSkill

Mac 可作为有限 CPU/render path，但完整 GPU parallel simulation 仍更适合 Linux + NVIDIA。

## Sim2Real / Real2Sim / Real2Sim2Real

以后必须分别研究：

```text
Sim2Real
sim training / testing
→ real deployment

Real2Sim
real observation / telemetry
→ calibrated simulation / digital twin

Real2Sim2Real
real evidence
→ simulator calibration/randomization
→ training / analysis
→ real execution
→ new real evidence
→ recalibration
```

但：

```text
simulator fit 得更好
≠ simulator 就是真实世界
```

还要结合 identifiability：多个参数组合可能产生相似 trajectory。

## 未来还需要继续调研的“工程后半程”问题

暂时不继续拆顶层文件，但要保留：

```text
runtime failure monitoring
fault injection / sensor dropout / latency
watchdog / degraded mode
model update regression
checkpoint / rollback
failure replay / telemetry
training-data / model provenance
security / adversarial physical inputs
world-state / memory integrity
long-running memory leak / cache growth
online adaptation safety
real robot wear / data-collection cost
low-cost proxy robot validation
```

这些不决定 Clover 的最终 representation，但会决定结果是否可信、能不能长期运行、能不能复现。

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

目前不冻结 explicit/latent/object/field/token、hierarchy、information-gain objective、Transformer/non-Transformer、具体 edge 芯片、具体 simulator 或任何新 Clover core algorithm。

Mac mini M4 是当前参考开发环境，不是最终答案；simulator 是实验仪器，不是真实世界。

---

**先把世界调研完整，再分析；先把分析总结清楚，再创新。**
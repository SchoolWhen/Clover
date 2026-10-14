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
14. [research/RESEARCH_FOUNDATION_MODEL_SYSTEMS.md](research/RESEARCH_FOUNDATION_MODEL_SYSTEMS.md)
15. [research/RESEARCH_ENGINEERING_VALIDATION.md](research/RESEARCH_ENGINEERING_VALIDATION.md)
16. [research/RESEARCH_FRONTIER.md](research/RESEARCH_FRONTIER.md)
17. [AGENTS.md](AGENTS.md)
18. [STATUS.md](STATUS.md)
19. [research/README.md](research/README.md)

## Stage 1 当前问题链

```text
有哪些相关研究？
↓
真实世界里有哪些状态？
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
状态应该用什么粒度、什么时间尺度表示？
↓
当前证据不足时，下一眼 / probing action 应该是什么？
↓
如果 hypothesis set 不完整、模型失效或实验不安全怎么办？
↓
怎样做 mechanism discovery、实验设计、falsification 和 provenance？
↓
Foundation Model 的 backbone / data / token / context / cache / kernel / harness 会怎样改变能力与成本？
↓
模型能不能在真实 edge 约束下运行？没有真机时怎样逐级验证？
↓
哪些方法 / dataset / benchmark 真正能区分这些答案？
```

## 新增：Foundation Model Systems

[research/RESEARCH_FOUNDATION_MODEL_SYSTEMS.md](research/RESEARCH_FOUNDATION_MODEL_SYSTEMS.md)

DeepSeek / Qwen 专门 watch：
[research/foundation_models/DEEPSEEK_QWEN.md](research/foundation_models/DEEPSEEK_QWEN.md)

这次审计发现，Stage 1 之前对现代大模型系统层覆盖不足。现在正式调研：

```text
Dense vs MoE
总参数 vs 每 token 激活参数
full / sparse / linear / hybrid attention
multimodal fusion
visual / video tokenization
long context
KV/cache hierarchy
streaming perception
data mixture / alignment / curriculum
synthetic data provenance
SFT / RL / distillation
FP16 / FP8 / FP4 / INT8 / INT4
kernel / compiler / runtime
expert / tensor / context parallelism
agent harness / tools / external memory
backbone reuse vs from-scratch
small proxy → frontier scaling validity
```

必须区分：

```text
科学 world-state 假设
≠ foundation-model backbone
≠ training recipe
≠ inference runtime
≠ agent harness

long context
≠ persistent grounded world memory

serving KV cache
≠ epistemic world memory

base model
≠ model + harness
≠ model + harness + tools / memory

hosted product
≠ open-weight checkpoint
除非确认是同一个 artifact

总参数
≠ 激活参数
≠ 实际内存
≠ 通信开销
```

### DeepSeek 当前重点

截至 2026-10-15，重点跟踪：

- DeepSeek-V4.1-Flash：552B MoE，输入 8B active、输出 16B active，原生视觉理解，1M context；
- Causal Encoder–Decoder、压缩/稀疏 attention、KV 压缩；
- FlashMLA / DeepSelect / DeepGEMM / DeepEP / TileKernels；
- speculative decoding / conditional sparse memory；
- DeepSeek Harness；
- Janus 作为“理解与生成视觉编码解耦”的历史对照。

这里真正重要的是：

```text
model architecture
+
cache
+
kernels
+
communication
+
post-training data
+
harness
```

共同决定最终系统表现。

### Qwen 当前重点

截至 2026-10-15，重点跟踪：

- Qwen3.8-Max：2.4T total / 95B active 的长时程 agent reference；
- Qwen3.8-Omni / Realtime：连续 multimodal runtime / agent reference；
- Qwen3.5：native multimodal + hybrid linear/full attention + sparse MoE；
- Qwen3-VL：dense / MoE 多尺度多模态 family；
- FlashQLA、Qwen-MM-Plugins、Qwen-Live-Harness；
- Qwen-RobotWorld、Qwen-RobotManip、Qwen-VLA、Qwen-Drive。

Qwen-RobotManip 给出的重要工程信号是：

```text
跨 embodiment 海量机器人数据
如果没有 representation / motion / behavior alignment
不一定越多越好，反而可能互相冲突。
```

所以 Stage 1 现在把 **training data 本身**也视为一级研究变量，而不是只研究网络结构。

## Mac mini M4：现在能做什么

当前本地参考：

```text
Mac mini + Apple M4
```

适合：

```text
small / medium open VLM baseline
MLX / MLX-VLM
Core AI / Core ML
visual-token / frame-rate ablation
context vs explicit memory
quantization / cache experiment
streaming state prototype
MuJoCo integration
runtime / unified-memory profiling
```

不应该把 552B DeepSeek 或 2.4T Qwen 当成本地部署目标；这类 frontier model 只在确实需要回答 scaling 问题时用 remote/cloud/API 做 comparator。

## Foundation Model 还要重点补的实验问题

```text
visual token budget vs physical-state retention
video FPS / token sampling vs fast dynamics
long raw context vs explicit grounded memory（等 byte / 等 latency）
KV precision vs uncertainty calibration
MoE expert 是否会形成 physical/spatial specialization
small proxy → frontier 是否保留同一个机制结论
frozen backbone vs LoRA/adapter vs partial/full tuning
language prior 对 physical reasoning 的污染程度
incremental visual encoding / streaming prefill
fast controller + slow reasoner 的同步
harness / tool / external memory 到底贡献多少 benchmark 分数
kernel/runtime version drift
不同硬件 backend 的数值差异是否累积成 world-state drift
API hosted model 与 open checkpoint 是否真的等价
architecture gain 与 data/post-training gain 如何拆开
```

## Engineering / Deployment / Validation

[research/RESEARCH_ENGINEERING_VALIDATION.md](research/RESEARCH_ENGINEERING_VALIDATION.md)

当前开发机、最终机器人计算平台与科学假设必须分开：

```text
当前开发机
≠ 最终机器人 edge computer
≠ 科学假设
```

后续不能只看平均 FPS，还要测：

```text
cold load / first inference
p50 / p95 / p99 / deadline miss
peak / persistent-state memory
thermal / sustained runtime
camera→state→decision→action 全链路 latency
```

并检查优化是否改变科学能力：

```text
quantization 是否损伤 uncertainty？
visual-token pruning 是否丢物理证据？
memory pruning 是否损伤 permanence？
缩短 history 是否产生 aliasing？
异步执行是否让 belief stale？
```

## 目前没有真实机器人：验证必须分层

```text
EV0 数学 / synthetic diagnostic
EV1 controlled simulator
EV2 randomized simulator
EV3 sim2sim
EV4 offline real-data / policy evaluation
EV5 real2sim / digital twin
EV6 deployment-runtime / compute HIL
EV7 proxy physical hardware
EV8 target real robot
```

所以：

```text
sim-only success
≠ sim2real success
≠ target-robot validation
```

没有真机意味着 claim 要更保守，不意味着现在不能严谨验证。

## Simulation 策略

### 本地
MuJoCo：https://github.com/google-deepmind/mujoco

### 必要时 remote Linux + NVIDIA
Isaac Sim / Isaac Lab、大规模 GPU simulation、photorealistic sensor generation、NVIDIA-specific SysID。

不要为了 Stage 1 强行让重型 NVIDIA 基础设施成为本地依赖。

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

目前不冻结：

```text
explicit / latent / object / field / token
DeepSeek / Qwen / 其他 foundation backbone
MoE / dense / linear attention / Transformer 路线
hierarchy
information-gain objective
具体 edge 芯片
具体 simulator
任何新的 Clover core algorithm
```

Mac mini M4 是参考开发环境，不是最终答案；DeepSeek/Qwen 是重要研究对象，不是默认技术选型；simulator 是实验仪器，不是真实世界。

---

**先把世界调研完整，再分析；先把分析总结清楚，再创新。**
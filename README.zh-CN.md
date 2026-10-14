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
15. [research/RESEARCH_TRAINING_POSTTRAINING.md](research/RESEARCH_TRAINING_POSTTRAINING.md)
16. [research/RESEARCH_ENGINEERING_VALIDATION.md](research/RESEARCH_ENGINEERING_VALIDATION.md)
17. [research/RESEARCH_FRONTIER.md](research/RESEARCH_FRONTIER.md)
18. [AGENTS.md](AGENTS.md)
19. [STATUS.md](STATUS.md)
20. [research/README.md](research/README.md)

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
模型经过什么 pretraining / SFT / BC / co-training / RL / distillation / deployment learning 才变成现在这样？
↓
模型能不能在真实 edge 约束下运行？没有真机时怎样逐级验证？
↓
哪些方法 / dataset / benchmark 真正能区分这些答案？
```

## Foundation Model Systems

[research/RESEARCH_FOUNDATION_MODEL_SYSTEMS.md](research/RESEARCH_FOUNDATION_MODEL_SYSTEMS.md)

DeepSeek / Qwen 专门 watch：
[research/foundation_models/DEEPSEEK_QWEN.md](research/foundation_models/DEEPSEEK_QWEN.md)

Stage 1 正式调研：

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

long context ≠ persistent grounded world memory
serving KV cache ≠ epistemic world memory
base model ≠ model + harness ≠ model + tools / memory
hosted product ≠ open-weight checkpoint
总参数 ≠ 激活参数 ≠ 实际内存 ≠ 通信开销
```

## 新增：Training / Post-Training / Embodied Learning

[research/RESEARCH_TRAINING_POSTTRAINING.md](research/RESEARCH_TRAINING_POSTTRAINING.md)

这次补充后，训练过程不再被当成“实现细节”，而是正式研究变量：

```text
TR0  base pretraining
TR1  continued/domain pretraining
TR2  SFT / behavior cloning
TR3  co-training / auxiliary objective
TR4  preference / conservative offline alignment
TR5  verifier/reward RL
TR6  online embodied RL
TR7  on-policy distillation
TR8  strong-to-weak distillation
TR9  simulator/world-model post-training
TR10 deployment-rollout / self-improvement
TR11 continual / test-time adaptation
```

最重要的规则是：

```text
architecture
× data
× objective
× update scope
× interaction regime
× runtime
→ observed capability
```

所以两个模型分数不同，不能先假设是 backbone / representation 导致的。

### DeepSeek / Qwen 的后训练启示

DeepSeek-R1 说明：纯 RL 可以激发 reasoning，但也可能带来 repetition / readability / language mixing 等问题；加入 cold-start 和多阶段训练会改变最终行为。

DeepSeek-V4.1-Flash 的公开说明则采用：

```text
SFT
→ RL
→ on-policy distillation
```

而且官方强调主要改进集中在自动合成 agent tasks / environments 和 rollout 数据管线，而不是新的 RL 算法。

Qwen3 flagship 使用：

```text
Long-CoT cold-start SFT
→ reasoning RL
→ thinking / non-thinking fusion
→ general RL
```

Qwen3-VL 又加入 multimodal SFT、strong-to-weak distillation 与 multimodal RL。

这说明：

```text
“post-training”
不是一个操作，
而是多个阶段分别安装 / 保留 / 改写不同能力。
```

### 机器人训练和 LLM 一样吗？

只在高层结构上类似：

```text
general prior
→ specialization
→ feedback
→ deployment
```

但机器人动作会改变真实世界和下一帧输入，因此训练问题根本更难：

```text
covariate shift
continuous / multimodal action
control frequency / latency
embodiment-specific semantics
real-world reset 很贵甚至不可逆
reward sparse / delayed
contact dynamics
hardware drift
safety / irreversible action
sim2real gap
teleoperation quality
```

所以：

```text
LLM 的 SFT → RL
≠ 可以直接照搬成 robot recipe
```

### 当前重点机器人训练范式

```text
Behavior Cloning / imitation
Action Chunking
Diffusion / Flow action expert
VLM + VLA co-training
future-latent / world-model auxiliary
cross-embodiment alignment
human-video latent-action pretraining
synthetic / simulation pretraining
offline sample reweighting
online RL
on-policy teacher distillation
simulated/world-model RL
failure / recovery / deployment self-training
```

重点参考：

- OpenVLA-OFT — https://arxiv.org/abs/2502.19645
- π0 / π0.5 — https://www.physicalintelligence.company/download/pi0.pdf · https://www.physicalintelligence.company/download/pi05.pdf
- Qwen-RobotManip — https://arxiv.org/abs/2606.17846
- GR00T N1.7 — https://developer.nvidia.com/blog/develop-humanoid-robot-policies-end-to-end-with-nvidia-isaac-gr00t/
- VLAFlow — https://arxiv.org/abs/2607.01586
- VLA-OPD — https://arxiv.org/abs/2603.26666
- TEMPO — https://arxiv.org/abs/2608.07314
- RehearseVLA — https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_RehearseVLA_Simulated_Post-Training_for_VLAs_with_Physically-Consistent_World_Model_CVPR_2026_paper.html
- LoopWAM — https://arxiv.org/abs/2610.18873

Qwen-RobotManip 特别强调：

```text
跨 embodiment 海量机器人数据
如果没有 representation / motion / behavior alignment
不一定越多越好，反而可能互相冲突。
```

VLAFlow 则在固定 π0-style 架构 / backbone / action space 下比较 action-only、language co-training、future-latent alignment 和组合，说明 **objective 本身会改变 transfer behavior**。

### 后训练可能提升一项、损伤另一项

必须继续跟踪：

```text
catastrophic forgetting
reward overoptimization
perception-reasoning interference
action-mode collapse
unsafe exploration
simulator exploitation
embodiment over-specialization
calibration loss
memory / state regression
deployment-data feedback bias
```

因此以后不能只看 task success。

## Mac mini M4：现在能做什么

当前本地参考：

```text
Mac mini + Apple M4
```

适合：

```text
small / medium open VLM baseline
frozen backbone + state/action head
LoRA / adapter tuning
MLX / Core AI / Core ML
visual-token / frame-rate ablation
context vs explicit memory
quantization / cache experiment
offline behavior cloning
flow / diffusion action-head experiment
small MuJoCo RL
teacher distillation
streaming state prototype
runtime / unified-memory profiling
```

不应该把 552B DeepSeek 或超大 Qwen 当成本地部署目标；frontier model 只在确实需要验证 scaling 时用 remote/cloud/API 做 comparator。

并且：

```text
4B proxy 上成立
≠ frontier MoE 上自动成立
```

重要机制必须做 scaling validation。

## Engineering / Deployment / Validation

[research/RESEARCH_ENGINEERING_VALIDATION.md](research/RESEARCH_ENGINEERING_VALIDATION.md)

当前开发机、最终机器人计算平台与科学假设必须分开：

```text
当前开发机
≠ 最终机器人 edge computer
≠ 科学假设
```

后续不能只看平均 FPS，还要测 cold load、first inference、p50/p95/p99、deadline miss、peak/persistent-state memory、thermal/sustained runtime 和 camera→state→decision→action 全链路 latency。

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
对真正重要的方法逐个做 one-method-one-report 机制分析，并把 architecture 与 training recipe 分开报告。

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
SFT / RL / distillation / robot training recipe
MoE / dense / linear attention / Transformer 路线
hierarchy
information-gain objective
具体 edge 芯片
具体 simulator
任何新的 Clover core algorithm
```

Mac mini M4 是参考开发环境，不是最终答案；DeepSeek/Qwen 是重要研究对象，不是默认技术选型；training recipe 是实验变量，不是预设答案；simulator 是实验仪器，不是真实世界。

---

**先把世界调研完整，再分析；先把分析总结清楚，再创新。**
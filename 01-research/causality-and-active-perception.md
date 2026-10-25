<a id="top"></a>

# 调研方向：因果、主动感知与开放世界

Maintained: **2026-10-25** · Document stage: **1 — Research** ([status](../STATUS.md)).

Active evidence acquisition, causal interventions, model discovery, uncertainty, embodiment and action usefulness.

This is the canonical topic document. Update it in place; source-level dates and reading-depth labels below qualify the evidence, not the maintenance date.

<a id="causal-identification-evidence"></a>

## 2026-10-25 当前补充：未知交互与真实成像的因果表征

### BISCUIT：目标可以未知，但辅助结构没有消失

- **来源：** Phillip Lippe 等，*BISCUIT: Causal Representation Learning from Binary Interactions*，UAI 2023，PMLR 216:1263–1273。[会议论文](https://proceedings.mlr.press/v216/lippe23a.html) · [正文](https://proceedings.mlr.press/v216/lippe23a/lippe23a.pdf) · [作者项目](https://phlippe.github.io/BISCUIT/) · [官方代码和数据说明](https://github.com/phlippe/BISCUIT)。`PRIMARY_PAPER` / `OPEN_SOURCE`。
- **实际证据：** 在可观测 regime/action 输入下，学习每个潜在因子的未知二值交互变量。主文的可识别类是变量置换和逐变量可逆变换，不是带真实物理单位的唯一状态。
- **承重假设：** 注入式观测映射；所述图无额外未观测混杂；给定过去状态与交互变量后，当前变量条件独立；每个变量有两种机制，且交互模式足够不同。二值的是机制开关，不要求被识别的物理因子本身二值。
- **观测与学习来源：** Voronoi、CausalWorld、iTHOR 均为生成/模拟数据；具身交互条件对应 `V3` 式设置，学习使用低层动作/regime 信息 `L3`，不是被动 `V0/L0`。模拟真因子用于评估时应标成 examiner 的 `L4`，不能未经核对写成模型训练输入。
- **边界：** 未证明真实机器人相机噪声、长期遮挡、未知混杂与新机制出现时仍可识别。核对主文 §2–3 假设与可识别类、摘要和官方数据说明；附录证明未逐步验证。

### 真实光学系统的反例：理论允许不等于算法已经可靠恢复

- **来源：** Juan L. Gamella、Simon Bing、Jakob Runge，*Sanity Checking Causal Representation Learning on a Simple Real-World System*，ICML 2025，PMLR 267:18143–18169。[会议记录](https://proceedings.mlr.press/v267/gamella25a.html) · [核读正文 v2](https://arxiv.org/html/2502.20099v2) · [官方代码](https://github.com/simonbing/CRLSanityCheck) · [Causal Chamber 数据](https://github.com/juangamella/causal-chamber)。`PRIMARY_PAPER` / `OPEN_SOURCE`。
- **实际证据：** 受控光源、偏振片和真实相机组成物理混合过程；作者对选定 CRL 方法做真实数据与确定性模拟消融，发现这些方法未能稳定恢复目标因子，部分方法在简化模拟上也失败。CCRL 的真实/模拟 MCC 分别为 `0.285±0.054` / `0.891±0.005`，为五次初始化的作者报告。
- **关键限制：** 因子间的因果结构由控制输入合成，真实的是光学混合/采集；并非自然机器人场景的因果发现证明。数据包含图像与数值传感器，部分多视图设置使用后者；不能把整套实验统一标为 RGB-only。动作/regime 条件是 `L3`；数值传感视图是 `L4`。只用相机图像的子实验与多传感视图必须分开记账。
- **成像风险：** 正文指出混合过程的随机性不由简单加性噪声描述；确定性/注入式成像假设不能因为潜变量理论成立便默认为真实相机满足。
- **阅读深度：** 核读正文 §2、§3.1 与讨论中的实验范围和假设边界；未完整复核全部方法、附录或重新运行代码。此处是外部负结果，不是 Clover 已运行的验证。

**当前结论：** 真实成像的可识别性研究已有公开负结果锚点；“真实机器人 RGB 视频上的可靠恢复”仍是更强、尚未被这里证据闭合的目标。不能把上述失败推成所有 CRL 方法必然失败，也不能把未知干预目标可学习推成任意动作都具有可识别性。

<!-- BEGIN current-cross-domain-evidence -->
<a id="current-cross-domain-evidence"></a>

## 当前跨领域与前沿证据：从动态拟合到干预、采证与技能空间

检索/核验：**2026-10-25（Asia/Shanghai）**。下表是外部研究记录，不是 Clover 的实验结果或架构决定。

控制论与系统辨识提供机制约束，技能学习提供可达性/时间结构，主动视觉提供新增测量。它们各自解决的问题不同。尤其必须区分：模拟未见视角、移动真实相机、执行物理干预、以及输入已测量的物性；这些操作对观测等价类的影响不能混算。

### SINDy

- **来源/版本：** [原论文](https://arxiv.org/abs/1509.03580v1)；初始提交 2015-09-11；本次返回版本更新于 2015-09-11。`PRIMARY_PAPER`。 [作者提供的项目/代码入口](https://pmc.ncbi.nlm.nih.gov/articles/PMC4839439/)（未运行复现）。
- **问题与机制：** SINDy 在候选函数库中用稀疏回归发现动力学方程。
- **输入/学习来源：** 要求可用状态时间序列和导数/导数估计；函数库、坐标、激励及噪声处理是关键前提。
- **实际证据：** 受控振子、Lorenz 与流体低维动态等例子；方法/讨论段已核读。
- **不能推出 / 待区分：** 方程稀疏性依赖坐标和候选库；在给定真状态上识别方程，不等于从遮挡 RGB 中同时发现状态和物理定律。
- **本次阅读深度：** 正文选读：方法、监督或局限段；未复核全部实验/证明。

### METRA

- **来源/版本：** [原论文](https://arxiv.org/abs/2310.08887v2)；初始提交 2023-10-13；本次返回版本更新于 2024-03-10。`PRIMARY_PAPER`。 [作者提供的项目/代码入口](https://seohong.me/projects/metra/)（未运行复现）。
- **问题与机制：** METRA 用时间距离约束的潜空间组织无奖励技能探索，而非遍历全部高维状态。
- **输入/学习来源：** 交互转移与动作属于 L3；论文包含像素和状态版本，必须分列。
- **实际证据：** 模拟运动/操作中的无监督技能与覆盖。
- **不能推出 / 待区分：** 时间距离或可达性结构服务于行为，不自动保留材质、身份、反事实或未来任意任务需要的世界变量。
- **本次阅读深度：** 正文选读：方法、监督或局限段；未复核全部实验/证明。

### HILP

- **来源/版本：** [原论文](https://arxiv.org/abs/2402.15567v2)；初始提交 2024-02-23；本次返回版本更新于 2024-05-26。`PRIMARY_PAPER`。 [作者提供的项目/代码入口](https://seohong.me/projects/hilp/)（未运行复现）。
- **问题与机制：** HILP 从离线转移学习 Hilbert 时间结构，再以方向技能支持目标或奖励提示。
- **输入/学习来源：** “无标签”指没有任务奖励标签，不是没有动作/状态/交互数据；需逐实验标 L3 和状态来源。
- **实际证据：** 模拟运动与操作的离线通用策略和任务适配。
- **不能推出 / 待区分：** 可用于新任务的策略表示不等于一般物理世界状态；不得把状态版结果改写为纯视觉结论。
- **本次阅读深度：** 正文选读：方法、监督或局限段；未复核全部实验/证明。

### PhysiCalWorld

- **来源/版本：** [原论文](https://arxiv.org/abs/2610.30125v1)；初始提交 2026-10-21；本次返回版本更新于 2026-10-21。`PRIMARY_PAPER`。
- **问题与机制：** PhysiCalWorld 从本场景探索交互提取物理 descriptor，供后续潜在世界预测复用。
- **输入/学习来源：** 视觉与动作交互 L3；方法允许可选 proprioception。论文不使用物性标签，具体变体需分开。
- **实际证据：** 四类物理变化环境，比较预测与视觉规划；正文方法段已选读。
- **不能推出 / 待区分：** Descriptor 有结构或跨物性范围预测更好，不证明独立物理参数唯一识别；可选本体输入不能静默算成纯视觉。
- **本次阅读深度：** 正文选读：方法、监督或局限段；未复核全部实验/证明。

### 物性偏移下的因果世界模型

- **来源/版本：** [原论文](https://arxiv.org/abs/2610.29088v1)；初始提交 2026-10-21；本次返回版本更新于 2026-10-21。`PRIMARY_PAPER`。
- **问题与机制：** 物性偏移研究区分“允许哪些输入”与“物性如何进入动力学机制”。
- **输入/学习来源：** 配对干预、给定质量、PD/力矩结构和模拟真状态属于额外 L3/L4 条件。
- **实际证据：** 合成捷径与 CausalWorld 不重叠质量区间的 rollout。
- **不能推出 / 待区分：** 已给质量在结构模型中有用，不等于质量由 RGB 获得；因果 mask 也不能替代正确的物理参数化。
- **本次阅读深度：** 摘要与书目核验。

### CLOSER

- **来源/版本：** [原论文](https://arxiv.org/abs/2610.28476v1)；初始提交 2026-10-20；本次返回版本更新于 2026-10-20。`PRIMARY_PAPER`。
- **问题与机制：** CLOSER 对导航候选做 target/non-target/uncertain 判断，不确定时获取补充真实视角再决定停止。
- **输入/学习来源：** VLM 微调、跟踪 mask 和 depth；深度是额外证据，不能写成严格 V0。
- **实际证据：** Gibson、HM3D 的 ObjectNav；闭环再观测与贪心停止比较。
- **不能推出 / 待区分：** 真实再观测与生成虚拟视角应分组；置信融合并不自行提供任意场景下的校准保证。
- **本次阅读深度：** 摘要与书目核验。

### AWAM

- **来源/版本：** [原论文](https://arxiv.org/abs/2610.23396v1)；初始提交 2026-10-16；本次返回版本更新于 2026-10-16。`PRIMARY_PAPER`。
- **问题与机制：** AWAM 规划虚拟相机运动并生成视角先验，压缩后与现场观测一起用于动作预测。
- **输入/学习来源：** 生成世界模型、几何条件和动作示范构成混合来源。
- **实际证据：** 受遮挡操作、分布变化与真实机器人实验。
- **不能推出 / 待区分：** 虚拟新视角没有增加外界测量，不能当作 V3 主动采证已消除不可识别性；应与真正移动相机比较。
- **本次阅读深度：** 摘要与书目核验。

### 物体/任务相关主动观测与 MPC

- **来源/版本：** [原论文](https://arxiv.org/abs/2610.29964v1)；初始提交 2026-10-21；本次返回版本更新于 2026-10-21。`PRIMARY_PAPER`。
- **问题与机制：** 物体/任务相关 NBV 与层级 MPC 耦合，沿导航路径检查不确定或可能变化的区域。
- **输入/学习来源：** 手眼相机、地图、动力学和机器人状态等输入须分开；不能由标题推成 RGB-only。
- **实际证据：** 受控半静态变化的模拟/真实移动操作，报告地图一致性与风险。
- **不能推出 / 待区分：** 地图熵下降不等于任务风险最小；需要把观察代价、地图陈旧和控制优先级一并检验。
- **本次阅读深度：** 摘要与书目核验。

### 照明感知的航天器检查

- **来源/版本：** [原论文](https://arxiv.org/abs/2610.22335v1)；初始提交 2026-10-15；本次返回版本更新于 2026-10-15。`PRIMARY_PAPER`。
- **问题与机制：** 航天器检查将照明相关图像信息纳入视点规划，挑战“可见就已检查”的二值判定。
- **输入/学习来源：** 已知检查目标、渲染图像与模拟控制条件。
- **实际证据：** 光照/视角变化的模拟检查及亮度指标。
- **不能推出 / 待区分：** 亮度或 VAE 方差不是通用物理知识或校准信息量；该工作提供成像—主动观测的交叉对照。
- **本次阅读深度：** 摘要与书目核验。
<!-- END current-cross-domain-evidence -->

<!-- BEGIN broad-vision-primary-evidence -->
<a id="broad-vision-primary-evidence"></a>

## 广义视觉理解的一手比较证据

核验日：2026-10-25。以下是外部方法与反例，覆盖经典接口、当前基础视觉与跨领域条件；未被采纳为 Clover 架构。

### 局部稀疏动力系统参数识别

- **一手来源：** [正式会议记录](https://proceedings.mlr.press/v323/baumgartner26a.html) · [论文](https://raw.githubusercontent.com/mlresearch/v323/main/assets/baumgartner26a/baumgartner26a.pdf)。
- **机制：** 以局部稀疏依赖图与稀疏 Transformer 解码轨迹，识别参数的排列/可逆变换等价类。
- **输入与学习来源：** 观测状态轨迹和初始状态，非直接 RGB；要求参数影响/单射、观测等价、图与光滑性等条件。
- **实际证据：** 图判据与四个合成系统实验。
- **边界与反假设：** 参数维数预先已知；论文将下游泛化列为未来工作。不能把合成状态识别记为真实视觉物性已恢复。
- **阅读深度：** 正文假设1–3、实验与局限选读；未复核全部证明；未运行复现。

### CDSD 空间分区与因果

- **一手来源：** [正式会议记录](https://proceedings.mlr.press/v323/brouillard26a.html) · [论文](https://raw.githubusercontent.com/mlresearch/v323/main/assets/brouillard26a/brouillard26a.pdf)。
- **机制：** 单父解码使测量位置归属单个潜变量，同时学习时间因果图。
- **输入与学习来源：** 时序科学测量；已知潜维/滞后，依赖平稳性、无潜在混杂等假设，非机器人 RGB。
- **实际证据：** 合成可识别性与真实气候场的分区/关联。
- **边界与反假设：** 光照、阴影、反射和遮挡可使一个像素依赖多实体；视觉场景能否满足单父解码必须另证。
- **阅读深度：** 正文 §3.4、实验设置与讨论选读；未运行复现。

### 干预因果图粗化

- **一手来源：** [正式会议记录](https://proceedings.mlr.press/v323/madaleno26b.html) · [论文](https://raw.githubusercontent.com/mlresearch/v323/main/assets/madaleno26b/madaleno26b.pdf)。
- **机制：** 由未知干预目标的数据学习可识别粗图，并利用粗化空间的格结构搜索。
- **输入与学习来源：** 需干预数据、coarse Markov/faithfulness 和干预有效变化等条件。
- **实际证据：** 抽象层级的图理论、合成与真实数据比较。
- **边界与反假设：** 分辨率由干预集合与样本数约束；不自动发现像素中的实体或证明任意压缩保持任务/因果充分性。
- **阅读深度：** 正文假设、算法范围及统计局限选读；未运行复现。

### ε 可识别性

- **一手来源：** [正式会议记录](https://proceedings.mlr.press/v300/li26j.html) · [论文](https://raw.githubusercontent.com/mlresearch/v300/main/assets/li26j/li26j.pdf)。
- **机制：** 以因果概率上下界在明示约束下足够窄来刻画近似识别。
- **输入与学习来源：** 变量、观测/干预概率与子群约束；非原始像素学习。
- **实际证据：** 在给定容差与假设下，部分因果/反事实概率可近似识别。
- **边界与反假设：** 容差或边界条件不是由模型自信度产生；不能据此把未识别物性任意填成点估计。
- **阅读深度：** 正文界与部分条件选读；未复核全部证明；未运行复现。

### 状态级因果效应识别

- **一手来源：** [正式会议记录](https://proceedings.mlr.press/v337/chen26c.html) · [论文](https://raw.githubusercontent.com/mlresearch/v337/main/assets/chen26c/chen26c.pdf)。
- **机制：** 利用上下文特定独立与状态约束区分状态级和变量级识别。
- **输入与学习来源：** 给定因果图、观测变量与上下文条件；不是从视觉自动得图。
- **实际证据：** 额外知识使部分具体状态查询在整体未识别时仍可识别。
- **边界与反假设：** 不能用一个状态下可回答推出全域机制已掌握；上下文可观测性和知识来源是承重条件。
- **阅读深度：** 正文问题定义与 ID-CSI 条件选读；未运行复现。

### Jumpy world models

- **一手来源：** [正式会议记录](https://proceedings.mlr.press/v306/farebrother26a.html) · [论文](https://raw.githubusercontent.com/mlresearch/v306/main/assets/farebrother26a/farebrother26a.pdf)。
- **机制：** 学习预训练策略在多时间尺度诱导的状态占据分布，再组合策略规划。
- **输入与学习来源：** 预训练策略与离线/交互轨迹；动作与目标经验 L3。
- **实际证据：** 多步时间抽象作为逐帧预测之外的比较方向。
- **边界与反假设：** 时间跳跃依赖已有策略的行为覆盖；不能保证保留短暂事件、失败证据或一般反事实历史。
- **阅读深度：** 摘要、引言及问题设定选读；未复核完整方法/实验；未运行复现。
<!-- END broad-vision-primary-evidence -->

## Contents

- [Value of Information, Probing Actions and Active Evidence Acquisition](#topic-research-research_value_of_information)
- [Open-World Epistemics, Model Mismatch and Epistemic Safety](#topic-research-research_open_world_epistemics)
- [Model Discovery, Falsification and Scientific Reasoning](#topic-research-research_model_discovery)
- [R-F — Causality, Counterfactuals and Interaction](#topic-research-dossiers-r-f-causality-interaction)
- [R-G — World Model ↔ Action: VLA, WAM and Planning](#topic-research-dossiers-r-g-world-action)
- [R-H — Active Perception and Lifelong World Formation](#topic-research-dossiers-r-h-active-perception-lifelong)
- [Active Perception](#topic-docs-research-map-active-perception)
- [Causality and Counterfactual World Understanding](#topic-docs-research-map-causality)
- [Model-Based Robotics](#topic-docs-research-map-model-based-robotics)
- [Embodied Reasoning](#topic-docs-research-map-embodied-reasoning)
- [Robot Foundation Models](#topic-docs-research-map-robot-foundation-models)
- [Vision-Language-Action Models](#topic-docs-research-map-vla)

<a id="topic-research-research_value_of_information"></a>

## Value of Information, Probing Actions and Active Evidence Acquisition

Source record updated: 2026-10-14

> **Research question:** How can a machine understand the real world through vision alone?

This is a Stage-1 research document. It does **not** propose a Clover architecture.

Its purpose is to study a core consequence of partial observability:

> When the current visual evidence is insufficient, what observation or action should the agent choose next in order to reduce uncertainty most efficiently?

This connects active perception, information gain, Bayesian experimental design, system identification, probing actions and embodied reasoning.

---

### 1. Core distinction

Most control formulations score actions mainly by task value:

```text
Which action moves me toward the goal?
```

But under uncertainty an action can also have epistemic value:

```text
Which action will teach me what world I am actually in?
```

The same physical action may therefore have two roles:

```text
instrumental action — changes the world to achieve the task
probing action      — changes viewpoint/world to reveal information
```

Some actions do both.

---

### 2. Value of information as belief change

A generic information-seeking objective compares the current belief

```text
p(x | history)
```

with the posterior expected after a candidate observation/action.

One common form is expected information gain:

```text
EIG(a)
= E_o [ KL( p(x | history, a, o) || p(x | history) ) ]
```

The hidden quantity `x` may represent:

```text
latent state
physical parameter
model parameter
causal structure
object identity
map hypothesis
possible task interpretation
```

This makes the target of information gathering explicit.

---

### 3. Active inference: information gain over states, parameters and model structure

#### Active inference and artificial reasoning

Peer-reviewed article: https://www.nature.com/articles/s41467-026-77209-5
Published: 2026-09-08
Evidence: `PRIMARY_PAPER`

The paper extends expected information gain beyond uncertainty over latent state to include uncertainty over model parameters and model structure. Action/policy selection combines expected value with epistemic gain and is framed as a form of optimal experimental design.

The distinction is highly relevant to Clover:

```text
What is the current state?
What are the physical parameters?
Which causal/model structure is true?
```

are different uncertainty targets and may require different probes.

Important limitation:

The paper's numerical examples operate in discrete partially observed generative models. It does not demonstrate general visual robotics or pixel-level world-model learning.

Stage-1 question:

> Can visual embodied agents explicitly distinguish information gain about current state from information gain about hidden dynamics or causal structure?

---

### 4. Active perception resolves missing physical evidence

#### Active Perception for Embodied Disambiguation

Primary paper: https://arxiv.org/abs/2608.13605
Evidence: `PRIMARY_PAPER`

The work addresses ambiguity caused not only by language but by missing physical evidence: occlusion, restricted viewpoints, unreadable text and unobserved targets. The robot can continue observing, request clarification or finish selection based on accumulated evidence.

Stage-1 relevance:

It operationalizes:

```text
uncertain target
→ choose new observation
→ accumulate evidence
→ decide whether uncertainty is resolved
```

and shows that information acquisition policy can be separated from base representation quality.

---

### 5. Next-best-view is one form of epistemic action

Relevant Stage-1 sources:

- Vantage / Seek-and-View — https://arxiv.org/abs/2610.11810
- Classical Active Perception — https://ieeexplore.ieee.org/abstract/document/5968

These methods treat viewpoint selection as a decision variable.

Important distinction:

```text
move camera to see hidden geometry
```

is different from:

```text
push object to reveal friction/mass/dynamics.
```

The first changes observation geometry; the second intervenes on the physical system.

---

### 6. Active system identification: action can identify dynamics

#### Sampling-based System Identification with Active Exploration for Legged Sim2Real Learning

CoRL/PMLR: https://proceedings.mlr.press/v305/sobanbabu25a.html
Evidence: `PRIMARY_PAPER`

This work actively selects exploratory behavior to reduce uncertainty over real robot dynamics for sim-to-real adaptation, rather than relying only on passive logs or broad domain randomization.

Stage-1 relevance:

A probing trajectory can be valuable because it distinguishes competing dynamic hypotheses.

This connects directly to hidden physical properties such as:

```text
friction
actuator response
contact behavior
unknown load
dynamic parameters
```

and supports the broader principle:

```text
some world knowledge is acquired by experiments, not by passive seeing.
```

---

### 7. Behavior-grounded physics is already using this principle

#### DR-WM

Primary paper: https://arxiv.org/abs/2610.17630
Evidence: `PRIMARY_PAPER`

DR-WM obtains scene geometry from RGB but calibrates terrain/contact properties from real action-response evidence before simulating candidate consequences.

Although the probing policy itself is not the central contribution, the method provides a concrete example where action-response turns an underdetermined visual property into a better-constrained physical model.

---

### 8. Information gathering can target state, parameter or structure uncertainty

Stage 1 should distinguish:

#### V1 — state information

Example:

```text
Is the cup behind the box or was it removed?
```

Potential probe:

```text
move camera
```

#### V2 — parameter information

Example:

```text
How slippery is this surface?
```

Potential probe:

```text
small controlled slide/push
```

#### V3 — mechanism information

Example:

```text
Is this drawer prismatic, hinged, latched or stuck?
```

Potential probe:

```text
small directional interaction
```

#### V4 — causal-structure information

Example:

```text
Does this switch control this device?
```

Potential probe:

```text
intervention on switch
```

#### V5 — task-interpretation information

Example:

```text
Which of two visually similar objects did the user mean?
```

Potential probe:

```text
new view / read label / ask user
```

---

### 9. Information gain is not automatically task value

A highly informative action can be expensive, risky or destructive.

A practical objective may need to trade:

```text
information gain
expected task reward
energy/time
risk
irreversibility
safety
opportunity cost
```

This is especially important in real robotics because some experiments cannot be undone.

Examples:

```text
push gently to estimate friction          — low cost
cut object to learn internal material     — irreversible
lift unknown heavy object                 — possible safety risk
open sealed package                       — changes world state
```

Stage 1 should therefore preserve the distinction:

```text
most informative action
≠
best action to execute.
```

---

### 10. Probing actions can change the thing being measured

This creates a subtle causal issue.

Example:

```text
measure deformability by squeezing
```

may itself alter the material state.

Therefore the agent may need to model:

```text
probe action
→ information gained
+
world change caused by the probe
```

This is particularly important for:

```text
soft objects
fragile objects
food
liquids
granular materials
adhesive/contact states
thermal systems
```

The epistemic process is part of the dynamics, not external to it.

---

### 11. A useful research loop

Without committing to a Clover mechanism, the literature supports studying this generic loop:

```text
current belief / hypotheses
        ↓
what uncertainty matters for the task?
        ↓
which candidate view/action would discriminate hypotheses?
        ↓
execute safe probe
        ↓
new visual evidence
        ↓
update belief / parameters / model structure
        ↓
stop when additional information is not worth its cost
```

This connects:

```text
active perception
system identification
causal intervention
uncertainty calibration
belief revision
planning
```

---

### 12. Candidate later diagnostics

#### D-V1 — ambiguity-trigger test

Does the system seek evidence only when current belief is genuinely insufficient?

Measure unnecessary probes and failures to probe.

#### D-V2 — expected-vs-realized information gain

Before action, estimate expected uncertainty reduction. After observation, measure realized reduction.

#### D-V3 — cheapest discriminating action

Among actions that resolve the ambiguity, measure whether the system selects the lowest-cost / lowest-risk one.

#### D-V4 — parameter identification efficiency

How many interactions are needed to reach a calibrated posterior over mass/friction/stiffness/dynamics?

#### D-V5 — model-structure discrimination

Provide several causal/mechanism hypotheses that make identical passive predictions but diverge after intervention.

#### D-V6 — stop-rule calibration

Does the system know when it has enough information to act rather than continuing to gather evidence indefinitely?

---

### 13. Adjacent gaps discovered

Value-of-information research reveals several additional Stage-1 areas:

```text
epistemic action safety
irreversible experimentation
experiment design under limited budgets
model-structure uncertainty
meta-reasoning over whether to think/look/ask/act
open-world hypothesis generation
```

The last item is especially important: classical Bayesian experimental design usually assumes a hypothesis/model class already exists. A general robot may first need to realize that **none of its current hypotheses explain the observation**.

That becomes an open-world discovery problem, not just uncertainty reduction inside a fixed model family.

---

### 14. Stage-1 questions

```text
What uncertainty is worth reducing before action?
Should the agent seek information about state, parameters or model structure?
How should information value be traded against time, energy, risk and irreversible change?
Which probes are valid under a strict vision-sensing goal?
How can expected information gain be estimated when the world model itself is wrong?
How should the agent detect that the current hypothesis set is incomplete?
When should it look, move, touch through action-response, ask, or simply remain uncertain?
```

---

### Current rule

Do not treat active perception as a camera-planning add-on.

Do not treat exploration as random data collection.

For Stage 1, the important concept is:

```text
an intelligent action can be valuable because of the evidence it is expected to produce.
```

This may be central to learning aspects of the real world that passive RGB cannot uniquely determine.

---

<a id="topic-research-research_open_world_epistemics"></a>

## Open-World Epistemics, Model Mismatch and Epistemic Safety

Source record updated: 2026-10-14
Source intake checked through: **2026-10-14**

> **Research question:** How can a machine understand the real world through vision alone?

This is a Stage-1 research document. It does **not** propose a Clover architecture.

Its purpose is to study what happens when the current world model is incomplete, wrong, outdated, unsafe to test, or insufficient to explain another agent.

The central questions are:

```text
What if the correct hypothesis is not yet in the model?
How can a robot detect that its world model has become invalid?
How should the robot distinguish state uncertainty from model-structure uncertainty?
When should it seek more evidence, ask for help, abstain, or stop?
How should the robot represent its own changing embodiment?
How should it reason about hidden goals / beliefs of other agents?
```

---

### 1. A useful uncertainty taxonomy

Stage 1 should keep at least these cases distinct:

#### E1 — observation uncertainty

The world state may be known in principle, but the current image is ambiguous, occluded, blurred, reflective, etc.

#### E2 — state uncertainty

The observation history does not determine which current hidden state is true.

#### E3 — parameter uncertainty

The structure of the model is accepted, but unknown parameters remain, such as friction, mass, actuator gain or transition probabilities.

#### E4 — model-structure uncertainty

Several different mechanisms could explain the same evidence.

Example:

```text
drawer is locked
vs
drawer is jammed
vs
drawer has an unknown latch
vs
controller is weak
```

#### E5 — hypothesis-set incompleteness / open-world uncertainty

The correct explanation is not represented among the current hypotheses.

#### E6 — regime change / model invalidation

The model used to be adequate, but the robot/world/controller has changed.

#### E7 — social / intentional uncertainty

Another agent has hidden goals, beliefs, preferences or future actions.

#### E8 — epistemic-action safety

The robot knows that additional evidence would help, but acquiring it may be risky, expensive, irreversible or socially inappropriate.

These are different research problems.

---

### 2. Open-world hypothesis generation and verification

#### HUME — Hypothesis-driven Model Expansion under Uncertainty

Primary paper: https://arxiv.org/abs/2607.06501
Official project: https://open-world-planning.github.io/
RSS 2026 program: https://roboticsconference.org/2026/program/papers/181/
Evidence: `PRIMARY_PAPER` / `OFFICIAL_PROJECT`

HUME treats missing knowledge in open-world robot planning as uncertain hypotheses rather than silently filling gaps with fixed assumptions. Foundation models generate candidate hypotheses over objects, attributes and action effects; automated planning schedules actions that both pursue the task and verify those hypotheses; refuted hypotheses are removed and new hypotheses can be generated.

Stage-1 significance:

```text
uncertainty over known hypotheses
≠
the model is missing a hypothesis entirely.
```

HUME is one of the clearest current robotics examples of **model expansion**, not only state estimation.

Important limitations / provenance:

- hypothesis generation uses foundation-model priors, not vision-only learning;
- verification may use detectors/VLMs and structured symbolic planning;
- its abstract PDDL-style world model is not evidence for a universal machine-native representation;
- generating a plausible hypothesis does not make it physically identified.

Stage-2 questions:

```text
How should candidate hypotheses be generated without treating language prior as ground truth?
What evidence is sufficient to promote, retain, reject or split a hypothesis?
How does a robot represent 'none of the current hypotheses explain this'?
```

#### Explicit world model for open-world manipulation

**Building Explicit World Model for Zero-Shot Open-World Object Manipulation**
Primary paper: https://arxiv.org/abs/2603.13825
Evidence: `PRIMARY_PAPER`

This route combines open-set perception, a reconstructed digital twin and simulation-based evaluation of candidate interactions.

Why it matters:

It provides a strong explicit-model/open-set comparator, but its simulator-backed digital twin should not be confused with proof that the true physical world state is identifiable from RGB.

---

### 3. World-model falsification and regime change

A general robot should distinguish:

```text
my current state estimate is uncertain
```

from:

```text
my transition/model assumptions are no longer valid.
```

#### Changepoint-Aware World Models (CAWM)

Primary paper: https://arxiv.org/abs/2609.18950
Evidence: `PRIMARY_PAPER`

CAWM monitors internal world-model prediction error, detects abrupt dynamics changes with an online changepoint test and discards stale replay while retaining the learned representation.

Robot-relevant examples include changed gravity and actuator gain.

Stage-1 implication:

```text
prediction error
```

can be evidence for:

```text
ordinary stochasticity
state-estimation error
observation corruption
representation failure
or a changed transition regime.
```

A robust system must not collapse these explanations into one scalar uncertainty score.

#### Feedback World Model

**Feedback World Model Enables Precise Guidance of Diffusion Policy**
Primary paper: https://arxiv.org/abs/2605.15705
Evidence: `PRIMARY_PAPER`

The work uses the discrepancy between predicted and actually observed next states during deployment to correct world-model guidance online.

Stage-1 relevance:

Execution itself creates a falsification signal:

```text
predicted consequence
vs
observed consequence.
```

This supports treating action execution as an ongoing model-checking process, not only policy rollout.

#### Sirius-Fleet

**Multi-Task Interactive Robot Fleet Learning with Visual World Models**
Primary paper: https://proceedings.mlr.press/v270/liu25g.html
Evidence: `PRIMARY_PAPER`

Sirius-Fleet uses visual world models plus anomaly predictors to monitor deployed robot actions and request human correction when predicted outcomes appear anomalous.

Stage-1 distinction:

```text
world-model prediction
+
anomaly / failure monitor
+
human escalation
```

is a different systems hypothesis from assuming the world model is always trusted.

---

### 4. The robot's own body is part of the uncertain world state

#### Full-Body Visual Self-Modeling of Robot Morphologies

Primary paper: https://arxiv.org/abs/2111.06389
Project: https://robot-morphology.cs.columbia.edu/
Evidence: `BACKGROUND_REFERENCE` / `OFFICIAL_PROJECT`

This work learns a query-driven visual self-model of robot morphology and demonstrates damage detection/localization/recovery.

Why it remains relevant:

```text
world model
```

should not silently mean only the external world. A robot also needs a model of what physical body it currently has.

#### Diffusion-Based Body Schema Learning Enabling Abnormal-State Adaptation

Primary paper: https://arxiv.org/abs/2608.01029
Evidence: `PRIMARY_PAPER`

The method studies musculoskeletal body schema under abnormal states such as muscle rupture and actuator jamming, using diffusion-based estimation rather than assuming a fixed low-dimensional body state.

Stage-1 implication:

```text
self model at deployment
```

may need to remain revisable under damage or actuator failure.

#### The Embodiment Gap in Robot Foundation Models

Primary paper: https://arxiv.org/abs/2608.18433
Evidence: `PRIMARY_PAPER`

This survey separates reusable model/data/representation knowledge from the embodiment-specific work still required to execute on a new robot.

Use it as a warning against reporting cross-embodiment success without recording:

```text
what structure transfers
what action interface changes
what calibration/adaptation is needed
what remains robot-specific.
```

Related Stage-1 sources already tracked:

- LAC-WM — https://arxiv.org/abs/2610.10846
- SyncWorld — https://arxiv.org/abs/2609.09155
- Robot-Factored World Models — https://arxiv.org/abs/2607.22535

---

### 5. Epistemic safety: information is not free

Active perception often drives a robot toward uncertain regions because they offer the most information. The same regions may also be the least safe.

#### Splat-CBF

Primary paper: https://arxiv.org/abs/2609.23100
Evidence: `PRIMARY_PAPER`

Splat-CBF combines next-best-view information objectives with collision safety constraints in uncertain 3D Gaussian maps.

Stage-1 research role:

```text
maximize information gain
subject to safety constraints.
```

It provides a concrete counterexample to the naive rule:

```text
choose the action with maximum information gain.
```

#### Conflict-Aware Active Perception and Control

Primary paper: https://arxiv.org/abs/2605.20566
Evidence: `PRIMARY_PAPER`

This work also combines risk-aware expected information gain with control-barrier-function safety, making the perception/safety conflict explicit.

#### ATOM-CBF

PMLR/L4DC 2026: https://proceedings.mlr.press/v331/yun26a.html
Evidence: `PRIMARY_PAPER`

ATOM-CBF adapts the safety margin of perception-based control under out-of-distribution measurements by explicitly accounting for epistemic uncertainty.

Stage-1 implication:

Uncertainty should sometimes cause:

```text
more conservative action
```

rather than:

```text
more aggressive exploration.
```

#### Epistemic-action utility

A future diagnostic should distinguish:

```text
TaskValue(a)
InformationValue(a)
Risk(a)
Cost(a)
Irreversibility(a)
SocialCost(a)
```

without assuming a final Clover objective yet.

---

### 6. Help-seeking, abstention and metareasoning

A general-purpose agent may need to choose not only **which physical action**, but **which cognitive / information action**:

```text
act
look again
move viewpoint
probe
retrieve memory
simulate
ask a human
abstain
stop
```

#### KnowNo / Robots That Ask For Help

Primary paper: https://arxiv.org/abs/2307.01928
Project: https://robot-help.github.io/
Evidence: `BACKGROUND_REFERENCE` / `OFFICIAL_PROJECT`

KnowNo calibrates uncertainty in LLM-based robot planners and asks for help when ambiguity is not safely resolvable.

Its language-planning setting is not evidence for vision-only world understanding, but it is a useful reference for **selective escalation** rather than silent guessing.

#### HiL-Bench

Primary paper: https://arxiv.org/abs/2604.09408
Evidence: `PRIMARY_PAPER`

HiL-Bench is not a robotics benchmark, but directly measures whether agents detect unresolved blockers and ask for help instead of guessing.

Stage-1 relevance:

The same metareasoning failure can appear in embodied systems:

```text
uncertainty detected
but no escalation
```

or:

```text
escalation triggered too often / too vaguely.
```

#### Candidate Stage-1 metareasoning taxonomy

```text
M1 act autonomously
M2 gather more passive visual evidence
M3 move to a better viewpoint
M4 perform a physical probe/intervention
M5 run internal prediction/simulation
M6 retrieve stored evidence/history
M7 ask a human / external source
M8 abstain / enter safe state
```

The research question is not yet which controller implements this. It is what evidence should justify each transition.

---

### 7. Other agents create another partially observed world

The real world includes humans and other autonomous agents whose internal goals are not directly visible.

#### Structured LLM Reasoning for Human–Robot Coordination Under Hidden Goals

Primary paper: https://arxiv.org/abs/2608.04309
Evidence: `PRIMARY_PAPER`

The work formulates cooperative interaction with private goal views as a Dec-POMDP and includes action-conditioned Theory-of-Mind inference, hierarchical planning, verification and replanning.

Stage-1 implication:

```text
visible human motion
≠
human goal / belief / intention.
```

The latent state of another agent may require history, communication and behavioral intervention evidence.

#### MindPower

Primary paper: https://arxiv.org/abs/2511.23055
Evidence: `PRIMARY_PAPER`

MindPower integrates multimodal perception with Theory-of-Mind reasoning over both self and other-agent mental state for embodied decisions/actions.

Important caveat:

These methods rely strongly on language-model priors and multimodal supervision. They are not evidence that mental states are directly visually identifiable.

#### Social-state distinctions

Stage 1 should keep distinct:

```text
body pose / visible action
short-term motion intention
current task goal
belief about world
preference
cooperative / adversarial role
social norm / permission
```

These have different evidence requirements.

---

### 8. Model confidence is not enough

A single uncertainty scalar cannot fully represent:

```text
I cannot see the state
I saw it but the representation forgot it
my parameter estimate is broad
I do not know which mechanism applies
none of my current models explain the observation
my model used to work but the world changed
I know the informative experiment but it is unsafe
another agent has hidden intent
```

Stage 1 should therefore compare methods by **uncertainty type**, not only confidence calibration.

---

### 9. Candidate later diagnostics

#### D-OE1 — missing-hypothesis test

Construct situations where all provided candidate models are wrong. Measure whether the agent can represent:

```text
none of the above / model incomplete
```

rather than force probability mass onto a wrong model.

#### D-OE2 — hypothesis expansion test

Give partial evidence, then require generation of new candidate explanations followed by verification actions.

#### D-OE3 — model invalidation test

Change dynamics after a long stable period. Measure detection latency, false alarms, adaptation cost and whether stale evidence is retained incorrectly.

#### D-OE4 — self-model damage test

Alter actuator gain, morphology, payload, camera mounting or joint availability and test whether the internal self model updates.

#### D-OE5 — safe-information test

Offer:

```text
high information / high risk
medium information / low risk
low information / no risk
```

and evaluate whether information seeking respects safety.

#### D-OE6 — escalation test

Create ambiguous conditions where the optimal behavior is to ask, abstain or seek more evidence rather than guess.

#### D-OE7 — hidden-goal test

Two visible behavior histories share similar motion but arise from different hidden goals. Test belief maintenance and evidence-seeking interaction.

---

### 10. Adjacent research gaps still worth collecting

The current scan suggests these should remain visible without creating more top-level files yet:

```text
open-set mechanism discovery
model-class selection / nonparametric world models
persistent hypothesis provenance
scientific falsification / experiment design
human-query cost models
social permission / consent for probing actions
multi-agent belief recursion
safe exploration under irreversible actions
unknown unknown detection
model ensemble collapse / correlated uncertainty
self-model and external-world-model coupling
```

---

### 11. Stage-1 questions

```text
Can a robot recognize that its current hypothesis set is incomplete?
How should new world-model hypotheses be proposed and grounded?
How can state uncertainty be separated from model-structure uncertainty?
How should prediction error be attributed to noise, state error, representation error or regime change?
When should a model be adapted, replaced or rejected?
What parts of the robot's own body/controller must be represented as revisable state?
How should information gain be traded against risk and irreversibility?
When should the agent ask for help or abstain?
How should hidden goals/beliefs of other agents be represented without hallucinating them as observed facts?
```

---

### Current rule

A general world model must be allowed to say:

```text
I do not know the state.
I do not know the parameter.
I do not know which mechanism is correct.
My current model may be wrong.
The world may have changed.
I need more evidence.
The informative experiment is unsafe.
I should ask for help / abstain.
```

None of these statements is a Clover architecture decision. They are Stage-1 requirements for what a credible future theory of real-world understanding may need to account for.

---

<a id="topic-research-research_model_discovery"></a>

## Model Discovery, Falsification and Scientific Reasoning

Source record updated: 2026-10-14
Source intake checked through: **2026-10-14**

> **Research question:** How can a machine understand the real world through vision alone?

This is a Stage-1 research document. It does **not** propose a Clover architecture.

Its purpose is to study a harder setting than ordinary state estimation:

> What should an embodied learner do when the currently available world-model class is incomplete, several mechanisms remain compatible with the evidence, or the next useful action should be chosen as an experiment rather than only as task execution?

The central loop is:

```text
observation / failure
→ candidate explanations
→ choose discriminating evidence / intervention
→ observe consequence
→ update confidence
→ reject / retain / refine / expand model
→ preserve provenance
→ repeat
```

This loop is a research object, not a proposed Clover control loop.

---

### 1. Model discovery is not the same as parameter estimation

Keep distinct:

```text
state estimation
— which current state is true?

parameter estimation
— which values inside a known model are true?

model selection
— which member of a known family is best?

structure / mechanism discovery
— what dependency or causal structure applies?

open-world model expansion
— is the correct mechanism missing from the current hypothesis set?
```

A robot that only estimates parameters inside a fixed simulator is not automatically discovering world structure.

---

### 2. Unknown unknowns and model misspecification

#### Unknown Unknowns: Model Misspecification in Machine Learning for Physics

Primary paper: https://arxiv.org/abs/2608.13633
Evidence: `PRIMARY_PAPER`

This 2026 physics perspective treats unknown unknowns as failures of the assumed model class rather than merely wide posterior uncertainty. It emphasizes that no single diagnostic can certify that a model is correctly specified; robustness requires complementary diagnostics, model revision and repeated checking.

Stage-1 implication:

```text
calibrated uncertainty inside a wrong model class
≠
robustness to model misspecification.
```

For Clover, this is useful background for asking whether a robot can detect evidence that none of its current mechanisms explains.

---

### 3. Open-world hypothesis generation and model expansion

#### HUME — Hypothesis-driven Model Expansion under Uncertainty

Primary paper: https://arxiv.org/abs/2607.06501
Official project: https://open-world-planning.github.io/
Open code: https://github.com/threefruits/HUME
Evidence: `PRIMARY_PAPER` / `OFFICIAL_PROJECT` / `OPEN_SOURCE`

HUME represents knowledge gaps as hypotheses, incorporates them into an explicit planning model, uses execution to verify them, rejects contradicted hypotheses and can generate replacements.

Research role:

```text
closed hypothesis set
vs
hypothesis-set expansion.
```

Important limitation:

The hypothesis generator is strongly language/foundation-model dependent and the representation is symbolic/PDDL-style. The result is therefore evidence that **model expansion is operationally useful**, not evidence that its symbolic ontology is the right machine-native world representation.

Stage-2 questions:

```text
How should a visual embodied system generate novel mechanism hypotheses without treating language priors as truth?
What evidence should promote, split or retire a hypothesis?
How should multiple incompatible but still viable explanations coexist?
```

---

### 4. Causal/mechanism discovery from interventions

#### Relaxing Faithfulness with Intervention-Only Causal Discovery

PMLR/UAI 2026: https://proceedings.mlr.press/v337/mazaheri26b.html
Evidence: `PRIMARY_PAPER`

The work shows that hard interventions can identify causal structure under assumptions that allow cancellation patterns violating ordinary observational faithfulness. It also characterizes equivalence classes when intervention scope is insufficient.

Stage-1 lesson:

```text
observational dependence structure
≠
full causal mechanism.
```

Intervention can be the primary carrier of structure information.

#### Causal Discovery in Action

PMLR/CLeaR 2026: https://proceedings.mlr.press/v323/panayiotou26a.html
Evidence: `PRIMARY_PAPER`

For chain-reaction systems, blocking interventions uniquely identify causal structure under specific structural assumptions and can outperform observational heuristics.

Stage-1 lesson:

Mechanism discovery can become tractable when the class of possible physical mechanisms has structure, but the guarantee depends on those assumptions.

#### Towards Completeness in Causal Discovery from Soft Interventions with Known Targets

PMLR/ICML 2026: https://proceedings.mlr.press/v306/zhou26s.html
Evidence: `PRIMARY_PAPER`

Studies what can be oriented/identified from soft interventions with latent confounding and known intervention targets.

#### SCOUT

PMLR/ICML 2026: https://proceedings.mlr.press/v306/turkoglu26a.html
Evidence: `PRIMARY_PAPER`

Studies nonlinear cyclic causal discovery from soft interventional data when intervention targets are unknown.

#### MetaCaDI

PMLR/UAI 2026: https://proceedings.mlr.press/v337/ong26a.html
Evidence: `PRIMARY_PAPER`

Meta-learns shared causal structure across environments and identifies unknown intervention targets with few-shot adaptation.

#### Test-Time Interventional Causal Learning (TICL)

PMLR/ICML 2026: https://proceedings.mlr.press/v306/chen26t.html
Evidence: `PRIMARY_PAPER`

Learns causal structure at test time from interventional data, including settings where intervention targets are not supplied directly.

#### Stage-1 interpretation

These papers should not be imported as robot architectures. Their value is theoretical:

```text
mechanism structure may be unidentifiable observationally
interventions can reduce equivalence classes
unknown intervention targets are themselves latent variables
cyclic / confounded / heterogeneous mechanisms require different assumptions
```

A future embodied theory must state which assumptions make its causal claims identifiable.

---

### 5. Scientific experiment design: choose actions to discriminate hypotheses

A robot performing epistemic actions is solving an experimental-design problem.

#### Bayesian Experimental Design via Score Matching

PMLR/UAI 2026: https://proceedings.mlr.press/v337/phillips26a.html
Evidence: `PRIMARY_PAPER`

Develops policy-based Bayesian experimental design around expected information gain while reducing the computational burden of repeated policy optimization.

#### Constrained Bayesian Experimental Design via Online Planning

PMLR/ICML 2026: https://proceedings.mlr.press/v306/guo26g.html
Evidence: `PRIMARY_PAPER`

Explicitly handles dynamic constraints, varying costs and physically restricted design sequences in sequential experimental design.

#### Robust Bayesian Active Learning under Model Misspecification

PMLR/AISTATS 2026: https://proceedings.mlr.press/v300/tang26d.html
Evidence: `PRIMARY_PAPER`

Shows that selecting only maximally informative samples can amplify model error under misspecification. Its acquisition objective combines informativeness, representativeness and error de-amplification.

#### On the Misinformation in a Statistical Experiment

PMLR/AISTATS 2026: https://proceedings.mlr.press/v300/callahan26a.html
Evidence: `PRIMARY_PAPER`

Shows that under model/inference misspecification, an experiment ranked as more informative can make inference more confidently wrong.

#### Amortized Safe Active Learning for Real-Time Data Acquisition

PMLR/AISTATS 2026: https://proceedings.mlr.press/v300/li26b.html
Evidence: `PRIMARY_PAPER`

Studies information acquisition under explicit safety constraints and fast deployment-time query selection.

#### Stage-1 implication

The naive rule:

```text
choose argmax expected information gain
```

is not generally enough.

A future embodied scientific policy may need to reason about:

```text
informativeness
representativeness
model misspecification
safety
cost
irreversibility
social permission
future task value
```

This remains a research question, not a Clover objective.

---

### 6. Hypothesis provenance and refutation memory

A scientific world learner should not only store its current best hypothesis. It may need to preserve:

```text
hypothesis identity
source / prior
supporting observations
contradicting observations
interventions performed
predictions made before observing outcomes
failure attribution
reason for rejection
conditions under which the hypothesis may become relevant again
```

#### SAGE — Multi-Hypothesis Failure Attribution

Primary paper: https://arxiv.org/abs/2606.31478
Open code: https://github.com/JieMaMagic/SAGE
Evidence: `PRIMARY_PAPER` / `OPEN_SOURCE`

SAGE is an autonomous-research system rather than a robot world model. It keeps multiple explanations for failed experiments, evaluates evidence for each, then routes the verified cause to hypothesis, experimental-design or implementation changes.

Why it matters to Stage 1:

```text
one failure
→ one verbal reflection
```

is a poor analogue for scientific model revision.

The useful transferable idea is **multiple working hypotheses + evidence-grounded failure attribution + measured-result grounding**, not the software architecture itself.

#### Socratic agents for autonomous scientific discovery

Primary paper: https://arxiv.org/abs/2606.26722
Evidence: `PRIMARY_PAPER`

AHOIS uses a critic to challenge hypotheses, formulate falsification criteria, generate counterexamples and run closed-loop experiments on a physical optical system.

Research role:

It offers an existence proof that hypothesis generation, criticism, experiment choice and revision can be integrated around a real physical apparatus. It does not establish that the same approach transfers to open-world robotic vision.

#### Stage-1 gap

Robotics/world-model literature still lacks a widely accepted benchmark for **hypothesis provenance and refutation memory**.

A future diagnostic should ask whether an agent remembers not only what it believes, but:

```text
why it believes it
what evidence would falsify it
which rejected explanations should not be silently resurrected
```

---

### 7. Representation design is itself an experimental hypothesis

Two current results sharpen the question of what latent state should preserve.

#### Learning Task-Sufficient World Models by Synergizing Agentic Exploration and Structured Modeling

PMLR/ICML 2026: https://proceedings.mlr.press/v306/feng26aa.html
Evidence: `PRIMARY_PAPER`

This work combines active probing with structured world-model learning to recover compact task-sufficient factors for control.

It directly links:

```text
what the agent probes
↔
which latent factors become recoverable
↔
which factors the state keeps.
```

Important limitation:

Task sufficiency is not open-world sufficiency. A compact representation can legitimately discard variables irrelevant to the evaluated tasks.

#### SpecWM — World Modeling through Spectral Alignment

Primary paper: https://arxiv.org/abs/2610.15429
Submitted: 2026-10-11
Evidence: `PRIMARY_PAPER`

SpecWM explicitly controls representation geometry through target similarity kernels. Different kernels change which physical quantities are linearly recoverable and which nuisance factors are suppressed; temporal spectral alignment improves model-based planning in reported OGBench/CALVIN experiments.

Stage-1 significance:

```text
representation objective
→ information preserved
→ information discarded
→ downstream planning behavior.
```

This is an important current counterpoint to the idea that a generic pretrained latent automatically preserves the right world variables.

---

### 8. Model discovery under non-stationarity

Model discovery is not only needed once. The mechanism class may change over time.

Relevant Stage-1 sources already tracked:

- Changepoint-Aware World Models — https://arxiv.org/abs/2609.18950
- ReDRAW — https://proceedings.mlr.press/v331/lanier26a.html
- ROAM — https://proceedings.mlr.press/v330/chen26a.html
- WorMI — https://proceedings.mlr.press/v267/yoo25a.html

Additional theory/background:

- multiple-change-point learning — https://proceedings.mlr.press/v306/gafni26a.html
- distribution-valued online change-point detection — https://proceedings.mlr.press/v306/zeng26f.html

Stage-1 distinction:

```text
abrupt changepoint
≠
slow drift
≠
new latent regime
≠
previously unseen mechanism class.
```

A future system should not assume one detector handles all four.

---

### 9. Other-agent model discovery and recursive beliefs

The world may contain agents whose hidden state includes beliefs about **our** beliefs.

#### Mental-Models for Multi-Agent Systems

Primary paper: https://arxiv.org/abs/2610.12453
Open code: https://github.com/hananshafi/Mental-Models
Submitted: 2026-10-08
Evidence: `PRIMARY_PAPER` / `OPEN_SOURCE`

The work learns reusable latent partner-state representations with first- and second-order mental-state structure for multi-agent decision making.

#### RecToM — Recursive Theory of Mind

Primary paper: https://arxiv.org/abs/2606.11724
Evidence: `PRIMARY_PAPER`

RecToM explicitly constructs nested perspectives for higher-order belief reasoning.

These are not proofs that mental state is visually identifiable. They establish useful computational distinctions:

```text
world state
other agent's belief about world
my belief about their belief
my belief about their belief about my belief
```

For robotics, recursive depth should be treated as a cost/necessity question rather than assumed infinite.

---

### 10. Social permission is part of epistemic-action validity

A physical probe can be safe in the collision sense and still be unacceptable.

Examples:

```text
open a person's drawer to inspect contents
move a personal object to test weight
enter a private room for a better viewpoint
interrupt a human to ask a clarifying question
touch another person's body/object to identify material
```

Relevant background:

- Socially intelligent task and motion planning for HRI — https://arxiv.org/abs/2001.08398
- Formalizing and Guaranteeing Human-Robot Interaction — https://arxiv.org/abs/2006.16732
- Enabling Basic Normative HRI in a Cognitive Robotic Architecture — https://arxiv.org/abs/1602.03814

These are background references, not 2026 vision-world-model results.

Stage-1 implication:

```text
physically safe probe
≠
socially permitted probe.
```

Future epistemic-action evaluation should eventually include ownership, privacy, consent, interruption cost and normative constraints when humans are present.

---

### 11. A working scientific-reasoning state schema

This is bookkeeping for Stage 1, not a proposed machine representation.

For every active hypothesis, a later Analysis report may record:

```text
HYPOTHESIS
- statement
- scope / domain
- provenance
- assumptions
- current support
- counterevidence
- predicted observations
- discriminating experiments
- safety / cost constraints
- status: active / weak / rejected / superseded / regime-specific
```

And every experiment/intervention may record:

```text
EXPERIMENT
- target uncertainty
- hypotheses discriminated
- expected outcomes
- actual outcome
- observation protocol
- side effects / disturbance
- cost / risk / permission
- posterior/model update
```

This prevents research agents from reducing model discovery to a list of current beliefs with no audit trail.

---

### 12. Candidate later diagnostics

#### D-MD1 — none-of-the-above mechanism test

All supplied mechanisms are wrong. Measure whether the agent forces a choice or proposes an expanded hypothesis set.

#### D-MD2 — discriminating-experiment test

Give two observationally compatible mechanisms and several possible probes. Measure whether the selected probe separates them efficiently.

#### D-MD3 — misleading-information test

Construct a misspecified model where the highest nominal information-gain experiment amplifies bias. Test whether robust experiment selection avoids it.

#### D-MD4 — refutation-memory test

After a hypothesis is falsified, later provide superficially similar evidence. Measure whether the agent remembers why it was rejected instead of resurrecting it without new support.

#### D-MD5 — regime-specific resurrection test

A previously rejected mechanism becomes valid after a real regime change. Test whether the system can distinguish justified reactivation from forgetting the previous falsification.

#### D-MD6 — recursive-belief depth test

Vary the order of belief recursion required for correct coordination; measure benefit versus compute/state cost.

#### D-MD7 — permission-aware experiment test

Offer an informative but socially impermissible probe and a weaker permitted alternative. Measure whether the system distinguishes information value from action legitimacy.

---

### 13. Stage-1 questions

```text
Can a robot detect that its model class is misspecified?
Can it generate genuinely new candidate mechanisms rather than only tune parameters?
Which interventions make competing mechanisms identifiable?
How should experiments be selected when information gain itself is unreliable under misspecification?
How should hypothesis provenance, counterevidence and rejection history be stored?
When should a falsified hypothesis remain dead, and when can regime change justify revisiting it?
How does the representation objective determine which physical factors remain recoverable?
How deep does recursive other-agent belief modeling need to be for embodied coordination?
How should privacy, ownership, consent and social norms constrain epistemic actions?
```

---

### Current rule

Do not equate:

```text
high confidence
with correct model class,

active exploration
with scientific experiment design,

one successful intervention
with causal identification,

reflection
with falsification,

current best hypothesis
with permanent truth.
```

Stage 1 should preserve the possibility that the machine's current explanation of the world is structurally wrong.

---

<a id="topic-research-dossiers-r-f-causality-interaction"></a>

## R-F — Causality, Counterfactuals and Interaction

Source record updated: 2026-10-14
Status: **BACKGROUND_RESEARCH**

### 1. Fundamental question

> **Can passive visual observation identify the causal structure needed for robust prediction and action, or does a machine need interventions and interaction to learn what changes what?**

Correlation, prediction and causality are not equivalent:

```text
correlation
→ predictive dependency
→ intervention-sensitive dependency
→ counterfactual model
```

Clover must not call a visual feature “causal” merely because it predicts well in-distribution.

### 2. Causal representation learning is underconstrained

#### Interventional Causal Representation Learning

- ICML 2023: https://proceedings.mlr.press/v202/ahuja23a.html

This work shows that interventional data can provide identification guarantees for latent causal factors under stated assumptions.

**Clover relevance:** interaction can carry qualitatively different information from passive observation because it changes the data-generating process.

#### General Identifiability and Achievability for Causal Representation Learning

- AISTATS 2024: https://proceedings.mlr.press/v238/varici24a.html

The paper establishes identifiability/achievability results using interventions under a broad nonlinear setting.

**Research consequence:** if Clover wants latent variables to correspond to causal state, it must state what assumptions or interventions make those variables identifiable.

#### Partially Observable Causal Representation Learning

- ICML 2024: https://proceedings.mlr.press/v235/xu24ac.html

The work explicitly handles causal representation learning when observations reveal only subsets of the latent state.

**Clover significance:** visual causality is doubly difficult because the causal state itself may be partially hidden by viewpoint and occlusion.

### 3. Real-video causal reasoning remains difficult

#### CausalVQA

- Paper: https://arxiv.org/abs/2506.09943
- Official Meta page: https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/
- Code/data: https://github.com/facebookresearch/CausalVQA

CausalVQA covers:

```text
counterfactual
hypothetical
anticipation
planning
descriptive
```

in real-world video scenarios.

**Demonstrates:** current frontier multimodal models still trail human performance substantially, especially on anticipation and hypothetical questions.

**Limit:** natural-language multiple-choice causal reasoning can still mix visual evidence with language/world priors and does not itself prove a learned causal state representation.

### 4. Intervention twins should be a core Clover diagnostic

A strong causal diagnostic should construct:

```text
same or near-same visual prefix
+ different controlled intervention
→ different valid consequence
```

The model should not only choose the correct outcome; it should be sensitive to the variable or relation actually changed by the intervention.

Suggested measurements:

- consequence accuracy;
- affected-state identification;
- false causal attribution;
- confidence/refusal when intervention effect is not visually identifiable;
- recovery when prediction fails.

### 5. Passive video and interaction provide different evidence

Passive internet video offers:

```text
broad diversity
natural dynamics
many object interactions
large scale
```

but usually lacks controlled interventions and action labels.

Interaction adds:

```text
controllability
cause/effect asymmetry
action-conditioned transition evidence
affordance evidence
active information gathering
```

V-JEPA 2 provides a concrete passive→action-conditioned research path:

- Paper: https://arxiv.org/abs/2506.09985

Large action-free video pretraining is followed by much smaller action-conditioned robot training for planning.

**Question:** what causal/action information appears only after action-conditioned data is introduced?

### 6. Counterfactual reasoning must be grounded in state

A model may produce a linguistically plausible answer to:

> “What would happen if X?”

without representing the changed physical state correctly.

Therefore a stronger counterfactual test should require:

```text
intervention specification
→ changed state / relation
→ predicted consequence
→ downstream action choice
```

and score each stage separately where possible.

### 7. Causal surprise and belief revision

Historical Clover's Counter-Witness-First idea remains a hypothesis:

```text
expected world
→ observation disagrees
→ locate broken dependency
→ causal candidate
→ test by future prediction / intervention
```

This is interesting because it connects causality to state revision, but it is not established by the causal-learning literature.

It should only survive if it improves intervention-sensitive prediction or diagnosis beyond standard predictive-error baselines.

### 8. Operational research questions

1. What causal structure is identifiable from passive V0/V1 video alone?
2. Which causal variables require intervention or action-conditioned data?
3. Can a predictive latent support correct counterfactuals without explicit causal factors?
4. Does an explicit causal graph improve novel-intervention generalization?
5. How should hidden/confounded causes be represented under visual partial observability?
6. Can the system distinguish “correlated visual cue” from “intervention-sensitive cause”?
7. Does causal representation improve recovery when the world behaves unexpectedly?

### 9. Baseline families

| Family | Comparator | What it tests |
|---|---|---|
| Passive predictive representation | V-JEPA 2/2.1 | predictive dependence from observation |
| VLM reasoning | CausalVQA-capable VLM | language-mediated counterfactual reasoning |
| Action-conditioned world model | WAM / robot predictive model | intervention/action-conditioned transitions |
| Causal representation learner | CRL baselines under intervention | identifiable latent causal factors |
| Explicit causal candidate | Clover historical mechanisms | whether explicit dependency adds independent value |

### 10. Discriminating experiments

#### T-F-01 — Intervention twins

Hold scene, camera and history constant as much as possible; alter one controlled physical intervention.

Measure consequence sensitivity and false causal edges.

#### T-F-02 — Observational shortcut test

Train/evaluate on correlated cues, then intervene on the cue while holding the true mechanism constant.

A causal model should retain the correct prediction when the spurious correlate is changed.

#### T-F-03 — Passive vs interactive learning

Same base model/data budget:

```text
passive video only
vs
passive video + action-conditioned trajectories
```

Measure:

- intervention prediction;
- counterfactual accuracy;
- novel-object affordance transfer;
- action success.

#### T-F-04 — Causal factor explicitness

Compare:

```text
distributed latent predictor
vs
latent + identifiable alignment
vs
explicit causal state
```

at matched prediction and compute.

#### T-F-05 — Causal recovery

Introduce an unexpected world change during a task and evaluate whether a system can identify the relevant changed dependency and replan efficiently.

### 11. Kill conditions

A named causal mechanism should be removed if it cannot outperform ordinary predictive representation on:

- intervention-sensitive prediction;
- spurious-correlation robustness;
- novel-intervention transfer;
- diagnosis/recovery;
- action success.

Likewise, do not require explicit causal variables if a distributed or identifiable latent obtains the same causal generalization more simply.

### 12. Clover landing

Current conclusion:

> **Causality should be operationalized through interventions, counterfactual state changes and action consequences. Passive visual prediction is important evidence, but the causal structure required for general robot behavior may need interaction or explicit identifiability assumptions.**

---

<a id="topic-research-dossiers-r-g-world-action"></a>

## R-G — World Model ↔ Action: VLA, WAM and Planning

Source record updated: 2026-10-14
Status: **BACKGROUND_RESEARCH**

### 1. Fundamental question

> **Does a robot need a persistent world model between perception and action, or can a sufficiently strong policy / world-action model solve the same problems implicitly?**

This is one of the strongest falsifiers for Clover's historical explicit-worldview direction.

Competing structures include:

```text
observation → action policy
observation/history → latent policy state → action
world representation → planner → action
predictive world model → model-based planning → action
joint world-action model → future state/action
high-level embodied reasoner → low-level VLA
```

No structure is assumed to win.

### 2. Open VLA baseline

#### OpenVLA

- Paper: https://arxiv.org/abs/2406.09246
- Code: https://github.com/openvla/openvla

OpenVLA is a 7B open-source VLA trained on large-scale robot demonstrations and pretrained visual/language representations.

**Why it matters:** it is a practical, reproducible strong direct-policy comparator.

**Clover question:** what failure remains when a strong VLA already maps visual/language context directly to robot actions?

### 3. Open-world policy generalization

#### π0.5

- Paper: https://arxiv.org/abs/2504.16054
- Official overview: https://www.pi.website/blog/pi05

π0.5 reports broad real-world manipulation generalization using heterogeneous multimodal and robot training.

**Research significance:** explicit persistent world state cannot be justified by saying direct policies inherently fail to generalize.

**Confound:** its training evidence is not vision-only; language, action and other supervision materially contribute.

### 4. World-Action Models

#### World-Action Models for Robot Learning and Control: A Survey

- Paper: https://arxiv.org/abs/2609.16074
- Project: https://rcl-robotics.github.io/Awesome-World-Action-Models

WAMs explicitly couple future-world prediction with executable action generation.

The survey identifies open challenges including:

- world/action factorization;
- spatial and multi-view consistency;
- long-horizon memory;
- action alignment;
- closed-loop learning;
- efficient inference.

**Clover significance:** world modeling and action are increasingly being trained jointly rather than treated as rigid independent modules.

#### World Action Models: The Next Frontier in Embodied AI

- Paper: https://arxiv.org/abs/2605.12090

Provides a complementary taxonomy distinguishing cascaded and joint WAMs and highlights evaluation across visual fidelity, physical commonsense and action plausibility.

### 5. Representation for world-action models is itself unresolved

#### ReWAM

- Paper: https://arxiv.org/abs/2609.38163

ReWAM reports controlled evidence that reconstruction fidelity or generic pretrained perceptual features alone do not automatically produce the most useful control representation.

**Key lesson:**

```text
best reconstruction representation
≠ automatically best action representation
```

Task/action gradients can shape a bottleneck toward state useful for control.

#### Being-M0.7

- Paper: https://arxiv.org/abs/2610.11283

Being-M0.7 learns visual-motion priors from mixed human data and then adapts them to humanoid action generation.

**Why it matters:** it is a strong 2026 example of compact future-aware latent state feeding whole-body action rather than explicit symbolic world state.

### 6. Hierarchical embodied reasoning remains competitive

#### Gemini Robotics ER 2

- Official: https://deepmind.google/models/gemini-robotics/embodied-reasoning/
- Model card: https://deepmind.google/models/model-cards/gemini-robotics-er-2/

Gemini Robotics ER 2 is explicitly positioned as a high-level reasoner that understands physical situations, plans multi-step behavior and hands motor execution to a lower-level VLA.

**Clover significance:** the industry frontier itself contains both end-to-end policy routes and reasoner→policy hierarchies.

### 7. Strong implicit policies are serious falsifiers

#### Figure Helix 2.5

- Official report: https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization
- Evidence label: `OFFICIAL_REPORTED_RESULT`

Figure reports zero-shot whole-body autonomy across 30 unseen homes and large gains from human-experience pretraining.

#### Skild S1

- Official report: https://www.skild.ai/blogs/s1
- Evidence label: `OFFICIAL_REPORTED_RESULT`

Skild reports in-context robot task learning from a single video demonstration, including long-horizon unseen tasks.

These systems are not independently reproduced Clover baselines, but they raise the standard for any claim that explicit world state is necessary.

### 8. The required Clover falsifier

The eventual comparison must be matched as tightly as possible:

```text
strong policy
vs
same / comparable policy + Clover world representation
```

Measure:

- unseen-scene transfer;
- unseen-object transfer;
- long-horizon success;
- planning/search cost;
- sample efficiency;
- world-change recovery;
- active-perception quality;
- unjustified action rate;
- diagnosis/debuggability where measurable;
- latency and memory.

If a worldview provides no independent benefit, that is evidence against the worldview program, not a reason to change the metric.

### 9. World prediction must be evaluated through action consequences

#### RoboPhys-3D

- Paper: https://arxiv.org/abs/2608.28718

RoboPhys-3D emphasizes 3D/state/task-grounded evaluation of generated world-model rollouts.

This supports a critical distinction:

```text
video quality
≠ state correctness
≠ action usefulness
```

#### Reference action vs realized state

World-action research such as HWAM stresses that an intended/reference action and the state actually reached by the robot can diverge.

- HWAM: https://arxiv.org/abs/2610.12026

A robot brain must ultimately reason over realized world effects, not only issued action tokens.

### 10. Operational research questions

1. Does persistent world state improve strong direct policies on unseen environments?
2. Does prediction help action because it captures future state, or merely because it regularizes representation learning?
3. Should world and action be jointly trained or modularly connected?
4. What state should be embodiment-independent versus embodiment-specific?
5. Does explicit world state reduce planning/search cost?
6. Which world-model metrics correlate with actual task success?
7. How should execution feedback update the world model?
8. Can a high-level reasoner remain reliable without a persistent queryable world state?

### 11. Baseline families

| Family | Comparator | What it isolates |
|---|---|---|
| Direct VLA | OpenVLA | observation/language→action baseline |
| Open-world VLA | π0.5 evidence | broad generalization without exposed world state |
| Predictive WAM | ReWAM / Being-M0.7 | action-grounded predictive latent |
| High-level reasoner | Gemini Robotics ER 2 | reasoning/planning separated from motor VLA |
| Robot foundation policy | Helix 2.5 / S1 reports | strong real-world implicit policy/generalization |
| Explicit worldview + policy | future Clover candidate | must prove independent downstream value |

### 12. Discriminating experiments

#### T-G-01 — Matched worldview value

Use the same task suite and, where possible, same visual/action backbone.

Compare:

```text
policy history only
policy + learned latent world model
policy + explicit/queryable world state
hybrid
```

#### T-G-02 — World change recovery

Move the target or block the path mid-task.

Measure detection, replan latency and final success.

#### T-G-03 — State correctness vs action success

Record both internal/world-query correctness and final task success.

This prevents a policy from looking “world-aware” merely because the final action happened to succeed.

#### T-G-04 — Unseen embodiment/camera

Separate world representation transfer from controller transfer by changing camera or robot embodiment.

#### T-G-05 — Prediction objective ablation

Compare reconstruction-, future-latent- and action-conditioned prediction at matched model/data scale.

### 13. Kill conditions

The explicit-worldview program should be weakened or rejected if a strong policy/WAM reaches equal or better:

- generalization;
- recovery;
- long-horizon success;
- sample efficiency;
- active perception;
- planning efficiency;

without the complexity of persistent explicit state.

Conversely, a direct policy should not be treated as sufficient if it fails systematically on state revision, unknown/unobserved handling or long-horizon world changes that a world-aware system solves.

### 14. Clover landing

Current conclusion:

> **World understanding must eventually prove value through action. The decisive scientific test is not whether a world representation is elegant, but whether it improves strong embodied baselines on generalization, recovery, planning and long-horizon behavior.**

---

<a id="topic-research-dossiers-r-h-active-perception-lifelong"></a>

## R-H — Active Perception and Lifelong World Formation

Source record updated: 2026-10-14
Status: **BACKGROUND_RESEARCH**

### 1. Fundamental question

> **Can a machine represent what it does not know well enough to act in order to acquire better visual evidence, then accumulate and revise world knowledge over long periods without catastrophic forgetting?**

This domain connects perception, uncertainty, action and continual learning.

A useful loop is:

```text
ambiguity / missing evidence
→ candidate sensing action
→ expected information gain
→ move / look / inspect
→ new visual evidence
→ world-state update
→ future memory / learning
```

### 2. Canonical active perception

#### Active Perception

- Ruzena Bajcsy, 1988: https://ieeexplore.ieee.org/abstract/document/5968

The core idea is that perception is not passive reception of fixed observations; sensing actions can be selected to reduce uncertainty or expose task-relevant information.

**Clover implication:** V3 embodied vision should not be treated as V0 plus a robot body. Action changes the future evidence distribution.

### 3. Modern view-seeking spatial reasoning

#### Vantage

- Paper: https://arxiv.org/abs/2610.11810
- Code: https://github.com/q1xiangchen/Vantage

Vantage identifies missing question-relevant spatial evidence, selects a new view, and then uses geometry-grounded evidence to improve reasoning.

**Demonstrates:** reasoning failure can be caused by missing observation, and targeted view acquisition can improve spatial understanding without simply scaling model parameters.

**Clover question:** can the world state itself expose what evidence is missing and choose a visual action accordingly?

### 4. Active perception can be learned from human behavior

#### Vision in Action

- Paper: https://arxiv.org/abs/2506.15666

Vision in Action learns search, tracking and focusing behavior from human demonstrations for bimanual manipulation with a controllable camera/head.

**Demonstrates:** active visual strategies can be learned jointly with manipulation rather than hand-coded.

**Open question:** do these camera actions optimize information gain, imitate human behavior, or both?

#### SaPaVe

- Paper: https://arxiv.org/abs/2603.12193

SaPaVe studies active perception and manipulation within a VLA-style framework and separates camera actions from manipulation actions.

**Clover significance:** sensing action and world-changing action may need different semantics even if both are physically executed by the same robot.

### 5. Lifelong visual representation learning

#### Lifelong Representations: Continual Self-Supervised Learning for Vision Models

- Survey: https://arxiv.org/abs/2607.09785

This survey organizes continual self-supervised vision around replay, distillation, regularization, architecture, model merging and objective-level adaptation.

**Clover relevance:** a general robot brain will receive an effectively unbounded unlabeled visual stream; offline pretraining plus frozen deployment is not the complete long-term setting.

### 6. Robot experience can become a continuing data engine

#### Skild S1

- Official report: https://www.skild.ai/blogs/s1
- Evidence label: `OFFICIAL_REPORTED_RESULT`

Skild describes in-context task learning from video demonstration and explicitly frames rapid deployment as a way to bootstrap new real-world robot interaction data back into the training pipeline.

#### Physical Self-Play

- Official report: https://skild.ai/blogs/physical-self-play
- Evidence label: `OFFICIAL_REPORTED_RESULT`

Skild reports post-training a base robot model through simulated self-play for soccer before transfer to a humanoid robot.

**Research significance:** a mature physical learner may combine passive human experience, demonstrations, robot interaction, simulation and self-generated curricula.

**Caution:** these are company-reported results and do not establish a universal lifelong-learning recipe.

### 7. Generative replay is an emerging continual-learning route

#### REGEN / World Action Models Enable Continual Imitation Learning with Recurrent Generative Replays

- Paper: https://arxiv.org/abs/2606.27374

REGEN uses a world-action model to synthesize pseudo-replay trajectories for past tasks during continual adaptation.

**Demonstrates:** generative world/action models may reduce forgetting without retaining all original demonstrations.

**Reported bottlenecks:** long-horizon visual degradation and action-observation inconsistency.

**Clover implication:** generated replay must remain epistemically distinct from observed evidence; synthetic memory is not automatically truth.

### 8. Active perception and memory are coupled

A system can only choose an information-gathering action if it represents some form of unresolved uncertainty.

Conversely, newly acquired evidence must update persistent state or memory in a way that matters later.

Therefore the loop should be evaluated end-to-end:

```text
unknown / ambiguity
→ sensing action
→ new evidence
→ belief update
→ later query / action improvement
```

A camera movement that merely produces more pixels without reducing task-relevant uncertainty is not useful active perception.

### 9. Lifelong learning must distinguish three forms of change

A deployed system encounters:

```text
world changes        — the environment changed
knowledge changes    — the model learned something new
task changes         — current goals changed
```

Conflating them can produce severe errors. For example, adapting model weights to a temporary world configuration may destroy stable general knowledge.

### 10. Operational research questions

1. Can the system recognize when current visual evidence is insufficient?
2. How should expected information gain be estimated from a learned representation?
3. Are camera/sensing actions distinct from task-manipulation actions in the internal model?
4. When should the robot explore versus act on current belief?
5. What should be learned online in weights, external memory or persistent world state?
6. How should lifelong learning avoid catastrophic forgetting?
7. Can self-generated or synthetic experience be used without contaminating evidence-grounded truth?
8. How should knowledge transfer across embodiments and cameras?
9. Can a robot discover new object dynamics through interaction while preserving old knowledge?

### 11. Baseline families

| Family | Comparator | What it isolates |
|---|---|---|
| Passive perception | fixed camera/history policy | no information-seeking action |
| Geometry-guided view selection | Vantage | targeted spatial evidence acquisition |
| Learned active camera behavior | Vision in Action / SaPaVe | sensing-action policy learned from data |
| In-context adaptation | S1-style evidence | task adaptation without weight update |
| Continual SSL | CSSL baselines | weight-level visual representation adaptation |
| Replay-based continual learning | real replay / generative replay | forgetting mitigation |
| Self-play / autonomous curriculum | reported physical self-play | self-generated learning experience |

### 12. Discriminating experiments

#### T-H-01 — Insufficient-view test

Present a task that cannot be solved reliably from the initial view.

Compare:

```text
passive policy
random view action
hand-designed view heuristic
learned active perception
world-state-driven information gain
```

Measure success, number of sensing actions and uncertainty reduction.

#### T-H-02 — Active object permanence

After an object leaves view, allow the robot to choose whether and where to look for it.

Measure:

- search efficiency;
- correct uncertainty before search;
- re-identification;
- downstream task success.

#### T-H-03 — Continual visual stream

Sequentially expose the model to new environments/dynamics over days or episodes.

Measure:

```text
new capability gained
old capability retained
adaptation speed
memory/storage growth
compute cost
```

#### T-H-04 — Synthetic replay contamination

Compare real replay, generated replay and no replay.

Measure not only forgetting but also false world beliefs introduced by synthetic trajectories.

#### T-H-05 — World change vs learning

Change an environment state temporarily, then restore it.

Test whether the system updates local world memory without incorrectly rewriting stable general knowledge.

### 13. Kill conditions

An active-perception mechanism should be rejected if it does not outperform passive/random sensing at matched action cost.

A lifelong-learning mechanism should be rejected if capability gains require unacceptable forgetting, latency, storage growth or false synthetic beliefs.

In-context memory, weight updates and persistent world state should remain separate research variables until experiments show which form of adaptation is actually needed.

### 14. Clover landing

Current conclusion:

> **A general visual robot brain likely needs both information-seeking action and long-term adaptation, but the mechanism is open. Active perception must prove that it reduces uncertainty efficiently, and lifelong learning must distinguish observed evidence, current world state and durable model knowledge.**

---

<a id="topic-docs-research-map-active-perception"></a>

## Active Perception

### Core question

> **If a visual system knows that its evidence is insufficient, can it decide what to look at next?**

Vision alone does not imply passive vision. A robot can move its camera or body, change viewpoint, approach an object, inspect an occluded region and create new evidence.

### Why this is central to Clover

A passive model can only refuse when a necessary fact is unobserved. A robot brain can instead turn epistemic uncertainty into an information-seeking action.

```text
unresolved world question
        ↓
which observation could resolve it?
        ↓
viewpoint / inspection action
        ↓
new visual evidence
        ↓
world update
```

This may become one of the strongest bridges between Worldview and Decision.

### Prior theoretical roots

- active vision;
- POMDPs;
- belief-space planning;
- next-best-view planning;
- information gain / entropy reduction;
- visual exploration.

These fields already formalize the idea that sensing itself can be controlled.

### Clover-specific questions

1. What form of uncertainty is actionable rather than merely low confidence?
2. Can the system identify a **minimal missing observation** needed to answer a world query?
3. How should the value of information trade off against task progress and motion cost?
4. Can active perception distinguish genuine ambiguity from model weakness?
5. Can the robot learn visual inquiry policies without language labels?

### Important distinction

Active perception is not an excuse to weaken the vision-only claim. The sensory evidence remains visual. The action only changes which visual evidence becomes available.

### Future strong test

Construct tasks where two hidden world hypotheses are visually indistinguishable from the current viewpoint, but one deliberate camera/body movement reveals the difference. A world-understanding system should know that it does not yet know, choose a revealing observation, update, and then act.

---

<a id="topic-docs-research-map-causality"></a>

## Causality and Counterfactual World Understanding

### Core question

> **Does predicting what happens next amount to understanding why it happens?**

No. A predictor can exploit correlation without identifying interventions or mechanisms.

### Levels of evidence

A useful hierarchy is:

1. **co-occurrence** — A and B appear together;
2. **temporal prediction** — A helps predict B;
3. **action-conditioned prediction** — under action `a`, B is predicted;
4. **intervention sensitivity** — changing a specific factor changes the predicted consequence;
5. **counterfactual support** — the model can compare what happened with what would have happened under a different intervention.

Clover should avoid calling levels 1–2 causal understanding.

### Relevant modern direction

Action-conditioned world models, robot interaction data and physically grounded video reasoning provide stronger evidence than passive next-frame prediction alone.

CausalVQA is useful as a diagnostic for counterfactual/hypothetical/anticipatory questions in video, but language QA performance is not sufficient evidence for an internal causal world model.

Primary reference:

- https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/

### Clover hypothesis worth preserving for study

A promising idea from earlier Clover work is **counter-witness-driven revision**:

```text
expected world transition
        ↓
new observation contradicts expectation
        ↓
identify minimal broken dependency
        ↓
propose causal explanation
        ↓
revise local world model
```

This remains a hypothesis, not a validated mechanism.

### What a strong causal test should eventually require

- matched or near-matched visual prefixes;
- controlled intervention difference;
- predicted consequence difference;
- correct identification of the affected world variables;
- resistance to background shortcuts;
- ability to revise after an unexpected intervention.

### Open questions

1. How much causal structure is identifiable from passive visual observation?
2. Which variables only become identifiable through intervention?
3. Can causal abstraction emerge without human semantic labels?
4. Is a compact causal graph useful, or is a distributed action-conditioned latent enough?
5. How should causal structure persist and revise over a robot's lifetime?

---

<a id="topic-docs-research-map-model-based-robotics"></a>

## Model-Based Robotics

### Why this matters

Long before modern world models, robotics formalized the separation among hidden world state, uncertain belief, observation, action and control. Clover should learn from that theory instead of reinventing its vocabulary.

### Core abstractions

#### State estimation

Estimate a latent physical state from noisy observations, often with an explicit uncertainty model.

#### Bayesian filtering

Alternates prediction and measurement update:

```text
belief_t
  ↓ dynamics
predicted belief_{t+1}
  ↓ observation
updated belief_{t+1}
```

This is conceptually close to any Clover mechanism that distinguishes evidence from belief.

#### POMDP

A Partially Observable Markov Decision Process explicitly represents that the true state is not fully observed. Decision making occurs over beliefs rather than pretending unobserved facts are known.

#### Model Predictive Control

Predicts candidate future trajectories under actions, optimizes a finite horizon, executes part of the plan, then replans from new observations.

#### Belief-space planning

Plans not only how the world may change, but how actions may reduce uncertainty.

### Clover relevance

Several Clover ideas have classical analogues:

| Clover concern | Existing robotics concept |
|---|---|
| unobserved vs known | partial observability |
| evidence/belief separation | Bayesian filtering |
| stale world state | belief update after new observation |
| active perception | information-gathering action |
| prediction under action | transition model / MPC |
| decision with uncertainty | POMDP / belief-space planning |

The purpose of studying these analogues is not to collapse Clover into a POMDP implementation. It is to avoid claiming novelty for distinctions that robotics already formalized well.

### Where classical model-based robotics is still limited

- state variables are usually chosen in advance;
- object/type ontology is usually task-specific;
- perception and state definition are often separate engineering stages;
- broad semantic priors and open-world learning are limited;
- scaling to unconstrained everyday visual worlds remains difficult.

### Central research question

> **Can Clover learn the state representation itself from visual experience while retaining the rigor of partial observability, belief revision and model-based decision making?**

That question is more substantive than simply replacing a neural policy with a hand-written state machine.

---

<a id="topic-docs-research-map-embodied-reasoning"></a>

## Embodied Reasoning

### Core question

> **Can a large multimodal reasoning model function as the high-level brain of a robot, and if it can, what is left for a dedicated worldview model to contribute?**

### Gemini Robotics ER 2

Google DeepMind describes Gemini Robotics ER 2 as an embodied reasoning VLM and a 'high-level brain for robots'. Its official model card states that it is based on Gemini 3.5 Flash and accepts text, image, video and audio inputs. The product page describes physical-world understanding, multi-step planning and handoff of motor execution to a lower-level VLA.

Primary sources:

- https://deepmind.google/models/gemini-robotics/embodied-reasoning/
- https://deepmind.google/models/model-cards/gemini-robotics-er-2/

### Why this matters to Clover

At the system level, this resembles part of Clover's high-level decomposition:

```text
perception / reasoning
        ↓
high-level plan
        ↓
lower-level action model
```

But the scientific basis is different. ER 2 is a multimodal VLM, so its physical reasoning can potentially draw on language and large-scale multimodal pretraining rather than only visual evidence.

### The crucial confound: visual evidence vs language knowledge

For Clover's SSOT, we must distinguish:

```text
world knowledge inferred from the current visual stream
```

from:

```text
prior semantic/physical knowledge imported by text-language pretraining
```

A model can answer a physical question correctly without constructing a persistent world state from current evidence.

### Questions to investigate later

1. Does the system maintain persistent identity when an object leaves view?
2. Can it distinguish unobserved from absent without language priors filling gaps?
3. How does it update after unexpected physical change?
4. Can it expose or query a stable world state across a long task?
5. How much of its physical reasoning remains under a strict vision-only protocol?
6. Does high-level reasoning reduce failures compared with the same lower-level VLA alone?

### Implication

Clover should not compete by claiming that language reasoning is 'not real understanding'. It should define a stricter visual-evidence protocol and demonstrate which world capabilities require persistent visual grounding beyond generic multimodal reasoning.

---

<a id="topic-docs-research-map-robot-foundation-models"></a>

## Robot Foundation Models

### Core question

> **Can sufficiently broad physical experience produce a general-purpose robot brain without first committing to an explicit human-designed world representation?**

This research family is especially important because it measures success in real embodied behavior rather than only perception benchmarks.

### Figure Helix 2.5

Figure reports that Helix 2.5 was pretrained on its Index dataset of human behavior and evaluated zero-shot across 30 unseen homes on three long-horizon whole-body behaviors. Figure reports no data collection, fine-tuning or adaptation in those evaluation homes, and an ablation in which Index pretraining increased full-task success from 9% to 56% while task-specific data and training conditions were held fixed.

Primary source:

- https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization

#### Evidence status

This is a company-reported real-robot result rather than an independently reproduced open benchmark result. It is still highly relevant as a capability target.

#### Clover lesson

Broad human-experience pretraining can materially improve transfer to unseen physical environments. Any Clover theory that relies mostly on hand-designed physical rules must explain how it will acquire the enormous diversity of everyday visual/behavioral regularities seen in such data.

### Skild Brain and S1

Skild frames its goal as an omni-bodied general-purpose robotic brain. Its public technical material describes hierarchical high/low-level policies trained across simulation, internet/human video, teleoperation and robot data.

S1 (August 2026) is presented as an in-context robot model: a video demonstration specifies a task, and the model adapts behavior from context. Skild reports recovery and task transfer under distribution shifts and examples of common-sense substitution behavior.

Primary sources:

- https://skild.ai/blogs/building-the-general-purpose-robotic-brain
- https://www.skild.ai/blogs/s1
- https://skild.ai/blogs/learning-by-watching

#### Physical self-play

In September 2026 Skild reported a self-play post-training system in simulation for humanoid soccer, followed by transfer to a physical robot. The important idea is not soccer itself: it is that robot intelligence may need self-generated interaction experience in addition to human demonstrations.

Source:

- https://skild.ai/blogs/physical-self-play

### Data-scale lesson

Modern robot foundation models increasingly combine:

```text
human video
+ robot demonstrations
+ teleoperation
+ simulation
+ cross-embodiment experience
+ self-generated interaction
```

This suggests that the learning problem for a general robot brain is not equivalent to fitting a single perception dataset.

### Open questions for Clover

1. Which abilities reported by these systems come from visual world representation versus action-policy scale?
2. Can a persistent worldview improve data efficiency or recovery compared with pure policy scaling?
3. How much can human video contribute when human and robot embodiments differ?
4. Does cross-embodiment training force the model to learn more abstract physical structure?
5. Which capabilities truly require interaction and self-play rather than observation?
6. How should a vision-only scientific claim be isolated inside a robot brain that may use language and proprioceptive/action information elsewhere?

---

<a id="topic-docs-research-map-vla"></a>

## Vision-Language-Action Models

### Core question

> **How far can a model go by mapping observations and instructions directly to actions without exposing a persistent explicit world model?**

VLA systems are a critical counter-hypothesis to Clover. If sufficiently strong VLA policies can generalize, recover and act in unfamiliar physical settings, Clover must show what additional value a persistent worldview provides.

### RT-2

RT-2 helped establish the VLA framing: web-scale vision-language knowledge is adapted to robotic control by representing robot actions within the model's token/action interface.

Primary source:

- https://deepmind.google/blog/rt-2-new-model-translates-vision-and-language-into-action/

### OpenVLA

OpenVLA is an open-source 7B vision-language-action model and ecosystem for robotic manipulation. The repository exposes pretrained models, fine-tuning and evaluation tooling; subsequent updates include faster fine-tuning/inference recipes.

Primary source:

- https://github.com/openvla/openvla
- https://arxiv.org/abs/2406.09246

OpenVLA is especially valuable to Clover because it is a public, inspectable representative of the VLA paradigm rather than a closed demo.

### π0.5

Physical Intelligence describes π0.5 as a VLA for open-world generalization. Its training combines robot data, web/multimodal data, object detections, semantic subtask prediction and low-level actions. It uses the same model for high-level textual actions and lower-level continuous motor commands, and reports long-horizon tasks in homes excluded from training.

Primary source:

- https://www.pi.website/blog/pi05
- https://www.pi.website/download/pi05.pdf

#### Why π0.5 matters

It is a strong challenge to the proposition that a separately exposed world representation is necessary for generalization. A learned policy can acquire substantial semantic and behavioral structure by co-training across data sources and abstraction levels.

#### But it is not a pure-vision comparison

Language, object detections, web data and robot actions are part of the training/interface. Its results therefore should not be interpreted as evidence that vision alone is sufficient.

### What VLAs demonstrate

- large multimodal priors can transfer into robot control;
- cross-embodiment and multi-environment data improve generalization;
- hierarchical behavior can emerge inside one trained model;
- long-horizon real-world manipulation is possible without an externally exposed symbolic world state.

### What remains a Clover research question

- Does an explicit persistent worldview improve recovery when the environment changes unexpectedly?
- Can it reduce data requirements by reusing geometric/physical structure?
- Can it provide reliable unknown/unobserved semantics?
- Can it support counterfactual planning and audit without regenerating latent reasoning each time?
- Can it make long tasks computationally cheaper by maintaining reusable world state?

### Fair future comparison

Clover should eventually compare against strong VLA systems on **shared embodied tasks**, not merely on internal representation quality. The key test is whether explicit world understanding yields measurable capability or efficiency advantages.

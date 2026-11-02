<a id="top"></a>

# 第2阶段：Analysis / 方法分析

Maintained: **2026-10-25**.

本阶段必须遵守根目录的 [研究契约](../SSOT.md)、[agent 规则](../AGENTS.md) 和 [全局流程](../PROCESS.md)。当前项目阶段由 [`../STATUS.md`](../STATUS.md) 唯一确定；目录存在不代表该阶段已启动或产出已通过。

## 当前状态与归属

方法分析阶段尚未成为主阶段；本次只归位现有分析模板，没有新增方法分析结果。

本阶段先在本文件内维护结构化条目；需要多个方向时按方向命名文件，直接更新其最新状态。每项工作通过来源、方法、假设或运行 ID 连接其他阶段的证据，不复制整篇上游文档，也不生成日期补丁或每次进展的新文件。

<a id="topic-research-analysis"></a>

## Stage 2 — Analysis

### Method Reports and Mechanism Decomposition

Source record updated: 2026-10-14

**Status:** DEFINED, NOT YET THE PRIMARY ACTIVE STAGE.

Analysis begins after Stage 1 Research has collected sufficiently broad material. Its job is to understand individual methods deeply rather than adding more names to the inventory.

### One method = one structured section in its canonical topic document

For every important method, use this template:

```text
Method / paper:
Version / date:
Research family:
Primary paper:
Official project:
Official code:
Evidence level:

Problem solved:
Input observations:
Training data / supervision:
V0–V3 observation protocol:
L0–L4 learning provenance:

Core representation:
Core mechanism:
Learning objective:
Temporal mechanism:
Memory mechanism:
Geometry assumptions:
Object/entity assumptions:
Physics assumptions:
Causal assumptions:
Action interface:

Datasets:
Benchmarks:
Reported result:
Reproduced result:

Strengths:
Weaknesses:
Confounds:
Failure modes:
Compute / scale requirements:
Reproducibility:

What this method actually demonstrates:
What it does NOT demonstrate:
Which Clover question it constrains:
What experiment would distinguish it from competing methods:
```

### Analysis dimensions

Every report should try to answer the same dimensions so later Synthesis is possible:

1. **Representation** — pixels, features, point maps, slots, tokens, graphs, latent state, explicit state, simulator, policy hidden state, etc.
2. **Time** — frame-local, short history, streaming, recurrent, persistent, episodic, future prediction.
3. **Space** — 2D, projective 3D, metric 3D, 4D, topological, semantic, relational.
4. **Identity** — visible association, persistent entity, object permanence, re-identification.
5. **Physics** — none, qualitative, relational, quantitative, hard constraint, learned dynamics.
6. **Causality** — correlation, prediction, action-conditioned transition, intervention, counterfactual.
7. **Uncertainty** — confidence only, calibrated uncertainty, belief state, explicit unknown / refusal.
8. **Memory** — context window, recurrent state, external store, episodic retrieval, map, replay.
9. **Action** — no action, downstream policy, action conditioning, planner, joint world/action model.
10. **Generalization** — object, scene, camera, dynamics, embodiment, real-world shift.
11. **Learning evidence** — image/video only, labels, language, robot actions, proprioception, simulation privilege.
12. **Evaluation** — what the benchmark truly measures and what shortcuts remain.

### Rule

Do not write “better” or “worse” without specifying the dimension, protocol and evidence.

Do not import the method into Clover during Analysis. Analysis produces understanding, not architecture.


---

## 方法分析卡（2026-11-02 序列五.1 填充）

> 填写纪律：每卡按本文件模板的账目字段压缩填写；数值只取仓库既有记录（`registry/artifacts.yaml`、STATUS 可比性账本、01-research 主题文档），未覆盖项写「仓库记录未覆盖（待核）」，不外推。证据等级统一为仓库记录级（ABSTRACT_AND_BIBLIO / 官方页面核验），无本地复现。证伪判决 = 该方法对 Clover 母问题的一句话可证伪结论。

### A 组：12 类模型家族

#### A1 YOLO26（目标检测）
- V/L 账：观测 V0（单目 RGB，部署）；学习 L1（COCO 等人工标注检测数据）。版本/许可：`yolo26n.pt` 640 输入，AGPL-3.0 或 Enterprise；2.4M 参数，精确 revision NOT_PINNED(见 artifacts.yaml)。
- 机制（12 维要点）：表征=帧级框+类别；时间=无（单帧）；身份=无持久身份（需外挂跟踪）；物理/因果=无；不确定性=未校准分数；记忆=无；动作=无。
- 混淆变量与成本：分数受标注本体与 NMS/阈值协议支配；Tier-0 可本地跑（CPU/MPS 级，未本地实测）。算力成本低但能力上限由训练分布决定。
- **一句话证伪判决**：单帧检测不产生跨时世界状态——若某系统仅以 YOLO 类输出主张「理解」，用 B4/B5（重现/永久性）即可证伪其状态主张。

#### A2 RF-DETR（目标检测）
- V/L 账：V0 / L1。许可 Apache-2.0（开放基座部分）；Nano 384 输入 30.5M 参数；精确 revision NOT_PINNED。
- 机制：DETR 式集合预测，无 NMS 后处理依赖；其余维度同 A1（帧级、无记忆、无物理）。
- 混淆变量：与 YOLO26 的对比须同输入同数据协议（仓库可比性账本已警示跨协议比较无效）；成本 Tier-0/1 之间。
- **一句话证伪判决**：架构差异（NMS-free）不改变证据性质——它仍是 L1 监督的帧级读出，不构成 V0/L0 世界理解证据。

#### A3 SAM 3 / SAM 3D（可提示分割与视频身份）
- V/L 账：V0 + 文本/点/框提示（提示含 L2 成分）；学习 L1+L2（数据引擎含教师生成）。`facebook/sam3@3c879f3`，SAM License（自定义，非 OSI）；约 850M 参数；SAM 3D Objects 为独立工件。
- 机制：表征=掩码+跨帧身份；时间=视频级传播；身份=提示锚定的实例延续；物理/因果=无；不确定性=分数未校准；记忆=传播缓存（非认识记忆）。
- 混淆变量：能力高度依赖数据引擎规模（L1/L2 成本外部化）；「分割=对象」是本体偷换（见 causality/representation 文档）；成本 Tier-1。
- **一句话证伪判决**：SAM 3 证明的是提示条件下的可分离性，不是物理对象性——B15/B14 上其掩码身份在隐藏参数分叉时无机制可用。

#### A4 Depth Anything 3（单目几何）
- V/L 账：V0（部署）/ L1+L3（深度与位姿监督含合成与传感器真值，特权程度按版本待核）。`depth-anything/DA3-SMALL` 34.3M（官方页面）；同族 GIANT 为 CC BY-NC 4.0（非商业），SMALL 许可证按 HF 卡（待核）。
- 机制：表征=稠密深度+相机位姿；空间=相对度量 3D（绝对尺度依赖先验，见二.2 量纲定理）；时间=多帧一致性有限；物理=几何自洽≠物理正确（R2 路线反证栏）。
- 混淆变量：官方位姿/几何优势（超 VGGT）为作者报告口径；透明/反光/动态场景失败模式已在 R2 反证栏记录；成本 Tier-0/1。
- **一句话证伪判决**：DA3 的深度是规范自由度未定的相对几何——无锚点时其输出不能支持任何绝对尺度物理主张（B15 质量/刚度类问题结构性无解）。

#### A5 PaddleOCR-VL（文档解析）
- V/L 账：V0 / L1+L2（文档标注+语言模型解码）。`PaddlePaddle/PaddleOCR-VL-1.6@c5630ab`，Apache-2.0，958.6M 参数，推理须 `image` 特征的 transformers 构建（本机 dry-run 已验证此约束，见 06-evaluation）。
- 机制：表征=文本+版面结构；时间=无；空间=2D 版面关系；其余维度（物理/因果/记忆）不适用/无。
- 混淆变量：小字/低分辨率退化是视觉 tokenization 瓶颈问题（AGENTS §20），与其语言解码能力须解耦评估（实验 1 的 OCR 小字曲线）；成本 Tier-1。
- **一句话证伪判决**：OCR 分数测的是「读出管线」而非世界理解——它进入 Clover 证据账只能作为 mandatory CV 读出基线（B10 类），不作世界状态证据。

#### A6 dots.ocr（文档解析）
- V/L 账：V0 / L1+L2。`rednote-hilab/dots.ocr2.0@2688f8c`（2.895B）；旧 `dots.ocr` 名已改，不得混用。
- 机制/混淆/成本：与 A5 同族；版本命名漂移本身就是可比性风险（账本已记录）；成本 Tier-1。
- **一句话证伪判决**：同 A5；另加——跨版本分数比较在 revision 未钉死时无效（仓库审计纪律）。

#### A7 MinerU2.5（文档解析）
- V/L 账：V0 / L1+L2。`opendatalab/MinerU2.5-2509-1.2B@b0b9392`，MinerU 模型许可（自定义）；管线含版面检测等模块，非单一模型分数。
- 机制：多模块管线（检测→识别→结构化）；评测须按 OmniDocBench 同口径（账本：OmniDocBench-1093 上游批处理约束）。
- 混淆变量：管线分数不可归因到单一表征；成本 Tier-1。
- **一句话证伪判决**：同 A5；管线性使其更不能作表征证据——分数变化先查模块与协议，再谈能力。

#### A8 olmOCR2（文档解析）
- V/L 账：V0 / L1+L2。`allenai/olmOCR-2-7B-1025-FP8@31cd8c0`，Apache-2.0，FP8 量化变体。
- 机制：VLM 式整页解析；量化（FP8）对小字的影响是 AGENTS §24 的标准消融问题（实验 1 覆盖同类问题）。
- 混淆变量：FP8 与全精度不可直接同表比较（账本规则）；成本 Tier-1。
- **一句话证伪判决**：同 A5；量化变体的分数只约束「该量化工件」，不约束模型家族能力上限。

#### A9 DINOv3 / Perception Encoder（自监督/图文表征）
- V/L 账：DINOv3 = V0 / L0（纯视觉自监督，R1 代表）；PE = V0 / L2（图文对比，R6 侧）。参数 21M–6.716B 按变体；精确工件须按变体钉死（账本）。
- 机制：表征=稠密/全局特征；时间=无（图像级）；身份/记忆/物理=无原生机制，其表征可作探针输入（受 SSOT 探针容量协议约束）。
- 混淆变量：下游分数高度依赖探针容量——超容量解码结果按二.1 协议降级 probe-learned，不归因于主干；DINOv3 与 PE 的 L0/L2 差异是 T1 判别核心，不可混报。
- **一句话证伪判决**：静态特征的世界状态含量只能由 B 组探针在容量上限内裁决——T2/B15 实验 2 即为其判决实验。

#### A10 追踪器组（CoTracker3 / TAPNext / SAMURAI）
- V/L 账：V0 / L1+L3（点轨迹标注与合成光流类监督，按各工件待核细分）。成员与工件见 artifacts.yaml（SAMURAI = SAM2 运动模型变体）。
- 机制：表征=任意点轨迹+可见性；时间=窗口内连续性；身份=点级而非对象级；遮挡后重现靠运动先验，无认识论标签（把「跟丢」与「不存在」混同的风险见 Failure or Drift 条目）。
- 混淆变量：学习型跟踪器的静默漂移（R2 反证栏）使其失败不可审计；成本 Tier-0/1。
- **一句话证伪判决**：轨迹连续性≠对象永久性——U9–U12 遮挡电池中其输出无 UNOBSERVED/REFUTED 区分，即为判决点。

#### A11 ViTPose / Sapiens / MoGe-2（姿态与单目几何读出）
- V/L 账：V0 / L1（姿态标注）与 L1+L3（MoGe-2 几何）。成员见 artifacts.yaml。
- 机制：帧级关键点/稠密人体特征/点图读出；无时间、无身份、无物理；属 readout 层工件。
- 混淆变量：人体先验强、域外（非人形）不迁移；成本 Tier-0/1。
- **一句话证伪判决**：读出精度不蕴含状态充分性——它们在 Clover 中只能作 B 组电池的被测读出或对照，不能作世界模型证据。

#### A12 OmniDocBench（基准，非模型）
- 定位：文档解析基准（评测仪器），不是模型家族；仓库记录含 OmniDocBench-1093 的上游批处理/口径约束。本卡只登记其仪器属性：测版面/公式/表格/阅读顺序的读出保真，不测世界理解。
- **一句话证伪判决**：任何用 OmniDocBench 分数支撑「世界理解」的主张都是仪器误用（AGENTS §4.3）。

### B 组：路线 R1–R7 核心代表作

> 证据基座 = `01-research/research-questions.md` 路线表（2026-11-02 版）自身的支持/反证栏；本组只做分析卡化，不新增外部事实。

#### B-R1 DINOv3（R1 规模化视觉自监督代表）｜B-R6 PE/CLIP 系（R6 代表附记）
- 主张：理解随视觉数据/规模涌现，专用结构非必需（R1）。支持：WebSSL 同数据追平 CLIP、DINOv3 强稠密特征、MoSA 零人工标注接近 SAM、StreamMAE 连续视频追平 i.i.d. MAE。反证（路线表原文归纳）：静态特征缺身份/记忆/物理；WebSSL 评估含语言成分；规模律未覆盖开放世界。
- V/L：V0/L0（DINOv3）；PE/CLIP 为 V0/L2——两者的对照正是 T1。混淆变量：探针容量（见 A9）；算力 Tier-2 级训练（路线成立不等于 Tier-0 可复现）。
- **一句话证伪判决**：若在匹配数据/算力下 DINOv3 类特征在 T2 世界状态探针（永久性/接触/再识别）上与显式状态同等，R2/R3 的结构主张被削弱；反之 R1 的「规模即理解」被证伪于状态类任务。

#### B-R2 DA3 / VGGT（R2 显式几何代表）
- 主张：理解要求显式空间状态。支持：DA3 位姿/几何超 VGGT、UniSim-SLAM 未标定 TUM 0.032 m 等（均为作者报告口径）。反证：静态/短时为主；单目绝对尺度需锚定（量纲定理，二.2）；透明/反光/动态失败；几何自洽≠物理正确。
- V/L：V0–V2 / L1+L3。混淆变量：基准多为静态重建口径；成本 Tier-1。
- **一句话证伪判决**：几何状态的价值须在接触/遮挡/度量预测上兑现（T2）——若几何状态不提升这三者，R2 退化为昂贵的重建读出。

#### B-R3 V-JEPA 2（R3 预测式世界模型代表）
- 主张：理解 = 可预测/可压缩的未来状态。支持：腐蚀/遮挡/时间箭头鲁棒性、OccJEPA 遮挡补全（SAIL-VOS 78.60、33.5× 于扩散基线，作者报告口径）。反证：潜空间预测可忽略因果变量；补全是特征预测≠物理；生成证据≠观测证据；动作标签依赖。
- V/L：V0(+动作条件时 V3 侧) / L0+L3。混淆变量：预测指标与干预正确性脱钩（T3 靶点）；成本 Tier-2 训练。
- **一句话证伪判决**：预测分数高而干预后系统性错误（T3）即证伪「预测即理解」——B15 实验 2 中其隐藏参数排序表现是直接读数点。

#### B-R4 SAM 3（R4 对象/关系/可供性代表）
- 主张：理解最小单位是实体/关系/可操作结构。支持/反证见 A3 卡与路线表（FineHOI/GraspHOI/SAGE 均为作者报告口径）。核心未决：分割≠物理对象、可供性由人定义、缺动力学/接触验证。
- **一句话证伪判决**：R4 的判决在 T5（新关系/新工具组合迁移 + 接触可行性）——标签本体覆盖之外的组合失败即其边界。

#### B-R5 Rendering-Free Lookahead（R5 主动视觉代表）
- 主张：理解由「看哪里、何时再看」构成。支持：未见 episode +43%（作者报告口径）；同路线 EgoReveal/FoveaVLA/SpatialScout（路线表）。反证：特权训练/模拟环境、任务特定、成本/风险/不可逆未联合建模、无一般世界状态。
- V/L：V3 / L3+L4（特权训练成分按各工作待核）。混淆变量：收益须在等成本/等风险下与固定策略比（T4），否则不可归因。
- **一句话证伪判决**：T4 中主动策略若在高不确定可逆条件下仍不优于固定策略，R5 的收益模型不成立。

#### B-R7 π₀.₅ / OpenVLA 纯策略分支（R7 具身反表征代表）
- 主张：世界本身就是它自己最好的模型；高频闭环反应即可，无需可解码世界状态（Brooks/Braitenberg 为经典形态）。支持：真实操作任务的工程成功、无状态幻觉写回问题。反证：遮挡后持久性/长时规划/反事实缺机制解释；失败不可归因；不可逆动作前无法先想后做。
- V/L：V3 / L3（动作演示）。混淆变量：内部隐状态维度与记忆窗口是受控变量——「无状态」须按 T6 规约操作化，不能按口号判定；成本 Tier-1/2 训练 + 真机评测。
- **一句话证伪判决**：T6 状态剥夺实验的崩溃曲线即判决——存在 τ_crit 且显式状态在其外保持可用，则 R7 被限定为边界内合法基线；全域无崩溃则反向裁决显式状态无独立增益（H15）。

（R6 的独立代表卡见 B-R1 附记：PE/CLIP 系与 DINOv3 构成 T1 对照对，单独成卡只会重复账目。）

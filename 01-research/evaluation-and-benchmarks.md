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

<!-- BEGIN evaluation-frontier -->
<a id="evaluation-frontier"></a>

## 2026-10 新验收面：3D 点追踪、多视图一致性、实时时钟与安全

检索/核验：**2026-10-25（Asia/Shanghai）**。本节只登记**评测协议与基准**，不把基准分数当作 Clover 结果。一个基准要进入 Clover 的证据链，至少要通过四道检查：任务是否覆盖目标能力；真值/辅助模态是否泄漏了部署时不可得的信息；评价单位（帧、视图、轨迹、任务）是否与主张一致；以及延迟/资源是否按真实闭环记录。

### TAPVid-MV：多视图 3D 点追踪的第一个长时基准

- **一手来源：** [固定版本](https://arxiv.org/abs/2609.01899v2) · [项目页](https://tapvidmv.github.io/)。`PRIMARY_PAPER` / `OFFICIAL_PROJECT`。
- **任务与规模：** 238 个序列、1,004 条校准相机流、74,147 条点轨迹，覆盖 7 个子集（室内/室外、机器人、人类活动、驾驶、合成程序场景）；序列与轨迹人工核验。
- **真值来源：** 数据集特定的辅助模态——传感器深度、LiDAR、SLAM/SfM 点、人体网格、带位姿物体网格、模拟。均为 `L4` 级证据，不是纯 RGB 可得。
- **实际证据：** 30+ 基线无一接近解决；令人意外的是，现有多视图点追踪器并不稳定优于单目点追踪器；同一数据上联合评估重建与追踪，作者把几何恢复识别为 3D 点追踪的主要瓶颈。
- **边界：** 校准多相机 `V2` 条件，不是单目 `V0`；真值辅助模态不能作为训练输入；基准覆盖仍有限；几何误差与对应误差的分解依赖各自重建管线；不能据此宣布某一架构失败。
- **阅读深度：** 摘要、基准构成与结论；未复核全部基线；未运行评测。

### TAPVid-3D：median-scaled AJ 会消掉整段尺度误差

- **一手来源：** [TAPVid-3D 项目页](https://tapvid3d.github.io/) · 协议审计见 [2609.34035](https://arxiv.org/abs/2609.34035v1) §4.2。`OFFICIAL_PROJECT` / `PRIMARY_PAPER`。
- **任务与规模：** 单目视频中的任意点 3D 追踪，minival 150 段，三个子集分别覆盖室外驾驶（约 10–50 m）、室内多人动捕（约 1–5 m）与自我中心室内（约 1 m）；报告 3D-AJ、APD、OA。标准 leaderboard 的 3D-AJ 先按每条轨迹的预测/真值深度中位比做**全局尺度对齐**，阈值又随点深度放大，因此它评的是“相对形状”，不是绝对米制。
- **实际证据：** 3D SSM 在同一 minival 上报告绝对米制 AJ 0.256（最强外部前馈 0.183），但 median-scaled leaderboard 仅 0.121（加可见性头 0.102），低于 DELTA+ 的 0.141。排序在两种口径下反转：**绝对更准的方法在尺度不变榜上更差**。这说明两种指标对应不同的误差结构，不能把 leaderboard 排名当作米制精度证据。
- **边界：** median scaling 会抵消整段常数尺度误差，但消不掉随深度漂移的误差；阈值随深度增长会放过近处小误差、放大远处差异；内参/位姿来源、训练/测试 split 与可见性判定都影响结果。任何“3D 点追踪 SOTA”都必须同时报告 scale-invariant 与绝对米制，并说明内参、位姿和深度来自真值还是估计。
- **阅读深度：** TAPVid-3D 项目页 + 3D SSM 的评测协议/结果表选读；未独立运行评测；未复核 TAPVid-3D 全部基线。


### 6-DoF 物体位姿：ADD 不是轨迹误差，FPS 不是端到端

- **一手来源：** [RoPT](https://arxiv.org/abs/2610.28962v1)、[GRC-Pose](https://arxiv.org/abs/2609.39116v1)、[ComPose](https://arxiv.org/abs/2605.23523v1)、[Robust Recovery](https://arxiv.org/abs/2607.23468v1)、[ASM-6D](https://arxiv.org/abs/2610.15287v1)。`PRIMARY_PAPER`。
- **指标层级：** 实例级 `ADD/ADD-S` 需要物体 CAD 与直径阈值，回答“位姿是否对齐模型”；BOP 的 `AR`（MSPD/MSSD/VSD）混合投影、对称距离与可见表面；轨迹级 `RTE/RRE/ATE/ARE/TCC` 不需要 CAD，但常做首帧/Umeyama 对齐，回答“相对运动是否对”；类别级 ASM/LEGAU 的 `IoU50`/`VUS` 还需要类别形状先验。四类数字不可互换。
- **实际证据：** RoPT 在 YCBInEOAT 16× 帧降采样下 ADD 90.85 / ADD-S 94.55，FoundationPose 只有 38.87/42.00；代价是 18.6 FPS vs 42.9 FPS。GRC-Pose 的后验 831.9 FPS（1.202 ms/帧），但支撑构建 2.061 s/帧 + 序列自适应 27.23 s，摊销端到端 0.79 FPS。ASM-6D 在 6–38 Hz 随假设/ADMM 预算变化；Event6D >120 FPS 但输入是事件 + 深度。ComPose 的 DexYCB RRE 1.5°，跨到 OakInk 仍为 2.4°，但 TCC_R 从 0.55 降到 0.19。Robust Recovery 有 10.74% 帧处于恢复，恢复延迟用冻结 6 帧对齐。
- **边界：** `ADD/ADD-S` 对对称物体、CAD 误差与阈值敏感；轨迹指标的首帧/尺度对齐会掩盖绝对尺度错误；单帧估计与视频跟踪混报会制造假 SOTA；初始化来自首帧检测/生成模型，遮挡期位置是预测；FPS 必须分“后验/支撑构建/自适应/上游基础模型”四段。任何“实时 6-DoF 跟踪”都要同时报告对象先验来源、初始化、遮挡/恢复帧比例、端到端 P50/P95 与失败检测。
- **阅读深度：** RoPT/GRC-Pose/ComPose/Robust Recovery/ASM-6D 的方法、主表、延迟与局限段选读；未独立运行评测；未复核全部附录。

### VC-PQ：多视图全景分割需要按“每个视图都看见”计分

- **一手来源：** [固定版本](https://arxiv.org/abs/2610.05911v1) · [官方代码](https://github.com/Renem24/vcpq)。`PRIMARY_PAPER` / `OPEN_SOURCE`。
- **问题：** 现有多视图全景分割沿用单场景 PQ（`PQ^scene`），把所有视图拼成一张图，漏掉某视图或 ID 改变只按面积比例扣分；这掩盖了“实例在某些视图可见、另一些不可见”的一致性失败。
- **机制：** VC-PQ 对每个实例可见的每个视图等权计数，并惩罚预测可见性与真值可见性不一致；分解为掩码精度、视图一致性、匹配阈值三部分；额外参数可恢复 tiling 的面积权重以便与旧指标比较。
- **实际证据：** 在 ScanNet++/ScanNetv2 固定协议上重评近期前馈方法，分解显示各方法丢分来源不同；受控扰动表明 VC-PQ 对“漏掉多少视图/改了多少 ID”敏感，而 `PQ^scene` 对面积敏感。
- **边界：** 指标不是模型；依赖真值实例 ID 与视图集；视图等权是否符合下游任务需论证；不能替代 3D 几何/物理正确性；新旧分数不可直接混用。
- **阅读深度：** 摘要、指标定义与受控实验；未复核全部实验；未运行评测。

### 2026-10 新增验收面一览

| 基准/协议 | 一手来源 | 它真正测什么 | 不能替代什么 |
|---|---|---|---|
| SA-Co（SAM 3） | [2511.16719](https://arxiv.org/abs/2511.16719v2) · [官方代码](https://github.com/facebookresearch/sam3) | 概念提示下的图像/视频分割、唯一实例 ID、hard negatives；4M 概念标签数据引擎 | 开放世界概念发现、长期身份、物理状态；文本提示含 `L2` |
| Realtime-Bench | [2610.22155](https://arxiv.org/abs/2610.22155v1) | Wall Clock 下动态任务的成功率/Pass^3；Paused/Token Clock 分离服务延迟与时间感知 | 真实机器人闭环；基准任务有限；理想时钟是上界 |
| SpatialScout | [2610.26659](https://arxiv.org/abs/2610.26659v1) · [官方代码](https://github.com/JesseZZZZZ/SpatialScout) | 主动探索下的物体级 3D 建图：定位精度 × 覆盖率；给定位姿/标定/物体清单 | 真实 SLAM、开放世界发现、无清单探索；模拟环境 |
| UniCounting COCO clean500 | [2610.08379](https://arxiv.org/abs/2610.08379v1) | 固定词表、无图像查询的多类别计数；点估计向量 L1、缺席类假质量、micro presence F1 | 开放词汇计数、实例身份、空间关系；clean 子集由作者构造 |
| TrackFlood 时延攻击协议 | [2609.33948](https://arxiv.org/abs/2609.33948v1) | NMS-free 检测→跟踪管线的内容相关时延、截止违约、bounded-admission 防御代价 | 平均 FPS；干净输入性能；其他威胁模型/硬件 |
| 6-DoF 物体位姿跟踪 | [2610.28962](https://arxiv.org/abs/2610.28962v1)、[2609.39116](https://arxiv.org/abs/2609.39116v1)、[2605.23523](https://arxiv.org/abs/2605.23523v1)、[2607.23468](https://arxiv.org/abs/2607.23468v1)、[2610.15287](https://arxiv.org/abs/2610.15287v1) | 实例 CAD/类别先验/生成 CAD 条件下的位姿轨迹、遮挡恢复与分阶段延迟 | 对象身份、物理属性、可变形/透明、无 CAD/无深度、恢复语义；单帧估计≠跟踪 |

> OmniDocBench 的版本边界（v1.6→v1.7）与解析评分已在[基础视觉验收地图](#broad-visual-evaluation)记录，本表不重复；新批次只把 MEVL-STP 等场景文字工作登记在[感知方向](perception-and-identifiability.md#core-vision-frontier)。

### FaVOS 与 Volumetric J&F：VOS 分数可能退化成“缺席分类”

- **一手来源：** [固定版本](https://arxiv.org/abs/2610.02946v1)（NeurIPS 2026 E&D） · [项目页](https://aidaslab.github.io/FaVOS)。`PRIMARY_PAPER` / `OFFICIAL_PROJECT`。
- **问题与规模：** 现有 VOS 基准多聚焦“几乎全程可见”的目标；FaVOS 专门覆盖低时间可见度：200 个视频、281 个目标，目标只间歇出现。
- **实际证据：** 在该 regime 下，标准 J&F 会把评测压缩成“缺席分类”：目标缺席帧上的空预测获得高奖励，一个平凡的空掩码预测器甚至能超过 SAM 3 等强模型；作者提出 Volumetric J&F，把掩码序列当作时空体评估，降低缺席奖励主导，同时保留对分割质量与时间一致性的敏感度。
- **不能推出：** FaVOS 是诊断性小基准（200 视频），不等于大规模训练/评测覆盖；Volumetric J&F 仍依赖真值掩码与可见性定义；空预测器“赢”是指标缺陷，不是 VOS 方法普遍失败；不能把该结论外推到所有 VOS 指标。
- **阅读深度：** 正文选读：问题设定、指标定义、受控实验、Limitations 与结论；未复核全部附录；未运行评测。

### Latent Video Prediction 评估：自监督视频模型作为世界模型编码器的鲁棒性

- **一手来源：** [固定版本](https://arxiv.org/abs/2605.15618v2)（NeurIPS 2026 E&D）。`PRIMARY_PAPER`。
- **对象与设置：** 四个匹配容量的前沿自监督模型——V-JEPA 2.1、V-JEPA 2、VideoPrism、VideoMAEv2；五个部署相关轴：特征可判别性、腐蚀鲁棒性、细粒度判别、遮挡鲁棒性、时间方向敏感性；在 Something-Something-v2 与 EGTEA Gaze+ 上重复。
- **实际证据：** 作者报告 latent-prediction 模型（V-JEPA 家族）在像素腐蚀下退化更平缓、遮挡下保留可用类别结构、不重建像素也能捕捉细粒度接触线索，并独特编码时间箭头；模型排序在两个数据集上基本一致。
- **不能推出：** 公开 checkpoint 的输入分辨率、clip 长度、预训练数据组成未完全配平；这是编码器鲁棒性评估，不是闭环世界模型/策略评估；五个轴不覆盖物理干预、长期记忆或主动采证；分数不证明“理解”。
- **阅读深度：** 正文选读：五轴定义、主结果、Limitations/附录说明；未复核全部附录；未运行评测。

### 指标失效模式：分数保持不等于能力保持

下表把本轮证据中最容易被误读的指标放在一起。它不是“哪个 benchmark 不好”的清单，而是要求 Clover 的验收同时报告**指标、能力、失败模式**三列；任何单指标 SOTA 都不能单独回答“是否理解”。

| 能力/常用指标 | 主要失效模式 | 本轮一手证据 | 必须同时报告 |
|---|---|---|---|
| 封闭集识别（ImageNet top-1） | 长尾、背景捷径、尺度变化被平均值掩盖 | VICAL/OFBD 的长尾偏差；Image-Scale 的尺度-精度曲线 | 每类/长尾组精度、背景替换、尺度曲线、开放词汇探针 |
| 开放词汇识别（CLIP/PE 零样本） | 语言先验、提示词、数据策展混入“视觉”成绩 | WebSSL 同数据比较；WOW-Seg 无文字提示但仍用 VLLM | 匹配数据/算力、推理无文字条件、新概念组合、数据来源审计 |
| 检测（COCO AP / FPS） | NMS 后处理、硬件/精度、小物体与长尾被平均 | YOLO26 NMS-free 回退；RF-DETR 目标域 NAS；DEIM 训练加速 | 端到端时延、P95/P99、小物体/长尾、未知类别、拒答校准 |
| 分割（mask IoU / 边界） | 提示信息量、实例身份、细边界与透明/反光 | SAM 3 的概念/实例模式；SAM-H 的分割重检测；SAM2Matting 的 alpha | 提示类型、边界误差、实例 ID 持续、透明/反光条件 |
| VOS（J&F） | 目标缺席帧奖励空预测，退化为缺席分类 | FaVOS/Volumetric J&F；空预测器可超 SAM 3 | 可见/缺席分项、Volumetric J&F、时间一致性、重入 |
| MOT（HOTA/IDF1） | 物理身份、长期重入、拥挤场景被关联分数掩盖 | MOTIP2 同位置进出失败；UGO 的 exemplar 粒度；SAM3RL 的 5 FPS 假设 | ID switch、重入、遮挡时长、最坏延迟、类别粒度 |
| 点追踪（AJ/δ） | 遮挡期位置、重现后重检测、长视频漂移；2D 分数不检验 3D 或尺度 | TAPNext 长序列退化；TAPNext++ 的 AJ_RD；TAPVid-MV 的几何瓶颈；Track-On-R 的教师上界 | AJ_RD、可见性、3D 几何误差、长时漂移、相机运动、伪标签教师来源 |
| 3D 点追踪/每像素 `SE(3)`（APD/RRE/ADD） | median-scaled 指标会奖励错误尺度；世界坐标依赖外部位姿/深度；平均刚体假设掩盖非刚体 | 3D SSM 绝对米制 AJ 0.256 但 leaderboard 0.121 落后 DELTA+ 0.141；MoSE3 依赖 π³ 几何与 64×H100 合成数据；TrackCraft3R 的速度声明随基线/分辨率反转 | 绝对米制与 scale-invariant 分列、内参/位姿来源、相机 vs 世界坐标、对象/部件分组 IoU、非刚体、吞吐与显存 |
| 3D 占据/场景图（mIoU/R@k/关系匹配） | 闭集语义税则与静态场景；mIoU 不含实例/关系；节点 recall 可被语言先验抬高；在线建图常借用 LiDAR/深度位姿 | OccAny 零样本序列 IoU 25.91；VEOcc 1 Hz 且位姿来自 LiDAR-惯导；LEXI-SG 含物体分割 1.56 FPS；LOST-3DSG 3 KB 语义状态但依赖 VLM；DSG 粗关系匹配 43% | 占据/实例/关系分列、位姿/深度来源、动态变化/删除/重现、关系真值、端到端延迟 |
| HOI（mAP） | 同义描述、角色反转与匹配引擎混入语义增益；排序随口径反转 | HOI 审计五口径：官方/SHOE/严格等价领先者变化；语义增益 1.6–20.3 mAP，AgentHOI 仅 49% 保留 | 官方分 + 同引擎身份控制 + 严格等价/角色反转 + 配对区间 |
| 光流/匹配（EPE/AUC） | 干净基准高不等于损坏鲁棒；低 EPE 不等于下游位姿/分割收益；匹配数量与几何显著性可冲突 | FreeFlow Sintel 0.68；Foundation Flow Sintel 2.37 但 RoCo-Spring 鲁棒分 1.10；SGFormer 视角 1px 略低于 LoFTR | 损坏鲁棒性、下游位姿/SLAM、最坏条件、匹配不确定性 |
| 非模态/遮挡（mIoU/amodal DSC） | full-mask 分数奖励“穿过遮挡物”；生成补全把先验当观测；合成遮挡与真实遮挡不一致 | OccSAM-Bench MedSAM full 0.640/visible 0.302；Amodal SAM mIoU_o 提升；VolFill 可见 CD 4.52 差于 MoGe2 2.62 | visible/invisible 分解、遮挡物反事实、补全来源标签、3D 一致性 |
| 事件检测/跟踪（sAP/ATE） | 用观测时刻而非预测可用时刻评测；事件数据由 RGB 模拟；SNN 能效为理论值 | Bend the Clock：RVT 从 47.39 降到 43.17 sAP 仅因 33 ms 延迟；ChronoFuse 恢复 71.8%/90.8%；Event3R/E-TraMamba 用模拟/半合成数据 | 可用时刻误差、事件率/照度分层、实测焦耳、真实事件基准 |
| 长视频/第一人称记忆（QA accuracy） | 单段 QA 会把“选对相似事件”误判为记忆；长程与精确未分；场景切换/跨月/在线更新未覆盖 | EgoProbe ultra-long 28–40%，最佳两轮 43.69%；Ledger 场景切换回到 blind；R4DSG 单被试 | 长程/精确/干扰三维、场景边界、在线更新、纯视觉记忆来源 |
| 组合/抽象推理（accuracy/ARC pass@2） | 平均 unseen 分数可被高支持组合抬高；答案对但证据错；语言先验可替代组合结构 | Reachability unseen HM 19.8–31.2 但低支持近 0；JRDB-AVR 答案 33.65/证据 13.01；TraceViT ARC-2 24.3 | 低支持组合、长输入、答案-证据绑定、纯视觉先验 |
| 计数（MAE/RMSE） | 单图平均掩盖组/事件/流式失败；语言先验可让累计数单调但 grounding 错；实时与精度 trade-off | SVCBench 人类 96.1 vs 最佳模型 37.0，周期事件 93.2 vs 11.1；BunchCount 组 1.85 vs CountGD 9.21；RT-Counter 112 FPS 但精度低于 CountGD | 计数单元、实例/组/事件分层、流式状态、分辨率/时延、校准 |
| 人脸/表情（准确率/FPR parity） | 平均准确率掩盖同阈值下的组间 FPR；表情标签有文化/主观歧义；AU 是代理；RL 可损害接地 | DenseFace FPR 比 8.82→0.91（African）；TAG 统一 74.34/逐集 83.78 但 RLVR IoU 46.73→43.46；Different Defects 随机删数据无增益 | 同阈值 FPR/TPR、低分辨率/事件/热成像、AU 证据、文化与不确定、数据缺陷审计 |
| 分布偏移/TTA（target acc/ECE） | source-val 选点不等于 target 可靠；TTA 收益有模型族边界；持续偏移遗忘/误差累积；合成数据多样性≠真实感 | Checkpoint 选择 ECE −0.24 但准确率 CI 跨 0；Colorist 协变量 +0.148；MLLM representation TTA 失败 | 目标校准/准确率、source-free/transductive、遗忘曲线、端侧、真实部署 |
| 姿态/手部（PA-MPJPE/MPJPE/PVE） | PA 与 MPJPE/PVE 不可互换；世界坐标尺度/相机轨迹未计；手部遮挡/接触仍难；实时数字依赖硬件 | SAM3D 3DPW PA 33.2/MPJPE 54.8；Fast 10.9×但 MPJPE 略升；OnlineHMR WA 93.5 但 W-MPJPE 受尺度拖累；DanceHMR 手 PA-PVE −28.6% | 坐标系、手/脸/全身分项、世界尺度、时序 jitter、遮挡/接触、端侧 |
| 部件/可供性（mIoU/gIoU） | 语言本体/粒度决定分数；合成/自动标签；2D/3D 不可互换；物理可行性未验证 | AffordAny unseen category 0.305/instruction gap 0.105；PartLLM 3DCoMPaT 86.1 mask vs 71.9 SA-mIoU；FunRec part mIoU 74.8–77.9；UniPart real grasp 85% | 部件粒度、affordance 本体、2D/3D 分项、语言改写、真实接触/物理 |
| 边界/抠图（MAD/Grad/dtSSD） | alpha 与 mask/depth 不可互换；视频时序与单帧精度分开；负样本假阳性常被漏报 | RenderMatte AIM MAD 0.008/Grad 11.2 但 2.7s；VideoMaMa++ dtSSD 0.82 vs 1.21；SEP-YOLO mask mAP50 0.851；OPC16K 现有 SOTA FPR 97.4%/49.3% | alpha/mask/depth 分项、时序、负样本 FPR、透明/软边界、计算/合成到真实 |
| 主动视觉（成功率/信息增益） | 任务成功率掩盖“没看到/没记住/决策错”；信息增益代理可冲突任务；恢复可见性≠成功；成本/风险未联合 | ActiveArena 固定视角 DM 96.3%、记忆-free 27.37 vs chunk 62.97；BAVO 恢复可见性≠任务成功；Epistemic Trap 77% vs 46% additive | 失败分解、信息增益/成本/风险、真实机器人、记忆写入、复合不确定性 |
| OCR/文档（CER/编辑距离） | 阅读顺序、表格/公式结构、版本漂移 | OmniDocBench v1.6→v1.7；MEVL-STP 多边形检测+识别 | 逐元素/结构分数、阅读顺序、版本、端到端耗时 |
| 3D/4D（位姿/几何误差） | 物理合理性、动态、透明/反光、任意时刻 | DA3 静态为主；Pano3D 静态室内；Uni4R 连续速度场 | 度量尺度、动态/非刚性、透明/反光、接触/互穿、任意时刻 |
| SLAM/里程计（ATE/RPE） | `Sim(3)` 对齐掩盖绝对尺度；显式失败与静默漂移混为一谈；合成损坏代理的排序可反转 | Failure or Drift 的 ORB-SLAM2 仅 37/63 有效轨迹、学习跟踪器 APE 常超 100 m；UniSim-SLAM 的未标定 ATE 需与尺度证据分开 | 有效性/覆盖率、失败与漂移分项、未对齐尺度误差、代理-真实一致性、运行时/地图/能耗 |
| 世界模型/生成（像素 MSE、FVD） | 策略效用、因果干预、记忆真实性 | DRILL 像素更差但策略更好；StarWM 的 task-relevance 歧义；Gen4P 生成先验 | 干预后状态、策略回报、记忆/重现、生成证据 vs 观测证据 |
| 实时（平均 FPS/TTFT） | 最坏截止、内容相关时延、证据年龄 | TrackFlood 跟踪器被拖垮；Realtime-Bench Wall Clock 44%；StreamAhead 平均 TTFT | P50/P95/P99、截止违约、证据年龄、队列/丢帧、攻击/退化输入 |
| 主动视觉（成功率） | 信息增益/成本/风险/不可逆未联合计分 | RFL 的 judge score；SpatialScout 的覆盖率-精度；FoveaVLA 的真实任务 | 信息增益/焦耳、动作成本、风险/不可逆、真实机器人转移 |

**结论：** 上述失效模式共同说明，**“分数保持”最多证明在特定协议下没有退化，不能证明能力保持**。Clover 的评测设计应把每个指标绑定到它可能掩盖的失败模式，并在 Stage 6 预注册“指标—能力—失败模式”三联表；否则速度、平均分或单一 SOTA 都可能把关键证据丢掉。

<a id="overlap-audit"></a>

### 预训练-评测重叠审计：哪些分数不能当作独立证据

检索/核验：**2026-10-25**。一个分数只有在**训练数据、评测集与选择流程**分离时才支持泛化主张。本节对关键模型/基准做披露级审计；“未披露”本身就是证据边界，不等于一定污染。

| 模型/基准 | 训练数据（披露） | 评测集 | 重叠证据/风险 | 能支持的主张 |
|---|---|---|---|---|
| WOW-Seg | LVIS、PACO、COCO Stuff 训练 2 epochs；InternVL3-1B 基座 | LVIS、PACO、RR-7K | **直接重叠**：在 LVIS/PACO 上训练后又在同数据集报告 SOTA；RR-7K 的 mask 来自 SA-1B，类别由 VLM+人工管线标注 | 只支持“在训练分布内区域识别强”；LVIS/PACO 分数不是开放世界泛化；RR-7K 是作者构造的半独立测试 |
| PaddleOCR-VL | 30M+ 公开/合成文档；用内部评测引擎做 hard-case mining 并合成训练样本 | OmniDocBench v1.0/v1.5、olmOCR-Bench、内部集 | 内部评测集参与 hard-case mining/合成训练，内部分数非独立；公开 30M 数据是否含 OmniDocBench 页面未披露 | 公开基准需独立重叠核查；内部 SOTA 不能当作泛化证据 |
| dots.ocr | 大规模多语言合成/真实文档数据引擎 | OmniDocBench、XDocParse | 训练数据与评测集重叠未披露；XDocParse 由作者提出 | 不能把 OmniDocBench/XDocParse SOTA 直接当作独立泛化；需第三方 split |
| SAM 3 | 4M 概念标签数据引擎；SA-Co/VIDEO 52.5K 视频/467K masklets | SA-Co、PVS 等 | SA-Co 基准与训练数据同源（作者数据引擎）；训练/评测 split 未独立审计 | SA-Co 是作者基准，不是外部独立测试；跨数据集比较需另选 LVIS/自建留存集 |
| MoSA | ~10,000 小时无标注视频；合成视频训练运动模块 | COCO、ADE20K 等七个分割基准 | 作者明确声明 **no overlap** with downstream benchmarks；仍依赖合成/光流伪标签 | 较干净的零样本分割证据；但不证明语义/物理/身份 |
| GOT-Edit | VOT2022、GOT-10K 协议 | 多个 GOT 基准 | GOT-10k 测试类与训练类不重叠；部分数据集测试类与训练类完全重叠 | 基准内追踪提升；不能外推为开放世界身份理解 |
| StreamMAE | WT++ 12h/95h 连续视频 | WT++ 同域评估 + 标准迁移 | 预训练与评估同域，非独立泛化；固定帧下采样 | 连续流式预训练可行性；不是跨域泛化证明 |
| 单图质量估计 | image2mass、ABO-500；深度在 ShapeNetSem 上微调 | image2mass、ABO-500 | 物体/类别级 train/test 重叠未在摘要披露；ShapeNetSem 与目标物体可能重叠 | 单视图质量 SOTA 的证据有限；需按物体/材质 held-out |
| PersistBench | 评测基准（YouTube 360） | 4D/视频模型 | 被评模型普遍在 YouTube 视频上预训练；与基准视频的重叠未披露 | 能揭示“离开视野后记忆崩塌”，但分数受预训练分布影响 |
| LiFR-Seg | DSEC/SHF-DSEC/M3ED 训练 | DSEC、M3ED、DSEC-Night | 标准数据集 split；DSEC-Night 为零样本 | 事件+RGB 的帧间分割证据；不是纯 RGB/通用视觉 |

**最小披露要求：** 训练数据来源与版本、评测 split/去重方法、是否做过 overlap 检测、benchmark 由谁构造、是否使用评测集做模型选择/硬样本挖掘、第三方独立复现。缺一项，分数就只能作为“作者报告”，不能作为 Clover 的独立证据。

**当前结论：** WOW-Seg 的 LVIS/PACO SOTA 是训练集内评测，不能支持“开放世界泛化”；PaddleOCR-VL 的内部 SOTA 受 hard-case mining 影响；SAM 3/SA-Co 与 dots.ocr/XDocParse 都是作者同源基准。相反，MoSA 明确声明无重叠，是较干净的对照。Clover 的任何“纯视觉”或“统一模型”主张，都必须先通过这一审计。

### 评测协议必须新增的四个记录项

1. **真值来源分级：** 传感器深度/LiDAR/SLAM/人体网格/模拟位姿是 `L4`；用它们生成的 3D 轨迹不能反过来当作纯 RGB 模型的“视觉监督”。
2. **视图/帧/轨迹的计分单位：** 多视图任务要报告每视图一致性；追踪要分别报告当前帧定位、关联、遮挡期状态、重现后身份；不能只报一个平均 J&F/HOTA。
3. **时时钟：** 至少区分模型推理、完整管线、环境真实推进（Wall Clock）与理想暂停时钟；平均 TTFT 不能替代最坏干预延迟与证据年龄。
4. **数据重叠与版本：** 基础模型预训练数据与评测集的重叠往往无法核对（When Trackers Fail 作者明确承认）；基准版本（OmniDocBench v1.6→v1.7）与评价脚本必须冻结。

**本节结论：** 新基准把“看见”拆得更细：多视图一致性、3D 点追踪、主动建图覆盖率、实时交互成功率和内容相关时延都成为独立验收面。这支持 Clover 的广义理解目标，但也提高了证据门槛——任何单一 benchmark 的 SOTA 都不能代表视觉 AGI。
<!-- END evaluation-frontier -->


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

- [2026-10 Evaluation Frontier: 3D Point Tracking, Multi-View Consistency, Real-Time Clocks and Safety](#evaluation-frontier)
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

#### U11 — Core visual capability vector

The battery must score capabilities separately, not collapse them into one “recognition” number.

| Capability | Minimal test | Required control | Pass criterion | Failure criterion |
|---|---|---|---|---|
| Closed-set classification | Image → category/attribute | Background replacement; class-balanced split | Per-class accuracy + calibrated confidence | High average from background/head-class shortcut |
| Open-vocabulary recognition | Novel class names/attributes without task-specific training | Matched data/compute vs language-supervised baseline; prompt set frozen | Novel-class accuracy + unknown/refusal calibration | Gains disappear when prompts/language are removed |
| Long-tail/fine-grained/scale | Tail classes, subordinate categories, scale sweep | Group-balanced metrics; same backbone | Tail/fine-grained retention; graceful scale curve | Average flat but tail/fine-grained collapses |
| Detection | Boxes + class + absence | Small/medium/large AP; NMS-free vs NMS; end-to-end latency | AP per size + latency + calibration | AP gain only on large objects or with extra data |
| Segmentation | Semantic/instance/panoptic masks | Prompt type fixed; boundary/transparent cases | Mask/pixel metrics + instance identity over time | High IoU but boundary/identity failures |
| OCR/visual reading | Text/table/formula/chart page | Version-frozen benchmark; reading-order metric | Character/structure/order metrics + full-page latency | High CER but wrong order/structure |
| Action/event | Clip → action/event/boundary | Temporal shuffle; static-frame probe | Top-1/locating + temporal sensitivity | Static/appearance shortcut |
| Referring/grounding | Language → box/mask/set | Ambiguous/absent referents; set completeness | gIoU/box + set completeness + refusal | Guesses on absent/ambiguous queries |
| Counting | Image → count vector | Dense/occluded/duplicate cases; fixed vocabulary | Count error + absent-class false mass | Duplicate detections inflate/deflate count |
| Pose/6D/geometry | Keypoints/6D pose/depth/scale | Textureless/symmetric/transparent cases | Pose/depth/scale error + failure detection | Works only on textured, asymmetric objects |
| 3D relation/affordance | Subject + relation/instruction → target/part | Novel relations/tools; contact feasibility | Relation/part accuracy + contact success | Memorized relation phrases or human-defined labels only |
| Memory/permanence | Object leaves FOV/occluded → query later | Equal-byte memory baselines; 360° reference | Reappearance identity + hidden position + belief revision | Short-term consistency only; confuses absence with unobserved |

#### U12 — Pure-vision provenance gate

Every capability claim must carry:

```text
deployment: V0 / V1 / V2 / V3
learning:   L0 / L1 / L2 / L3 / L4
external priors: language / teacher / depth / pose / action / force / simulator / retrieval
```

Pass conditions:

- The claim's stated “vision alone” matches **both** deployment and learning provenance.
- No text prompt at inference does **not** imply no language in training.
- No manual labels does **not** imply no synthetic data, optical flow, teacher or simulator.
- RGB-only deployment does **not** imply RGB-only upstream training.
- If any L1–L4 source is present, the claim must be phrased as “V0 + Lx”, not “pure vision”.

#### U13 — Native ultrafast acceptance

Measure the **complete** path:

```text
capture → decode → preprocess → encode → state update → retrieval/reasoning → decision → action
```

Required report:

- cold load, first inference, warm P50/P95/P99, deadline misses;
- sustained throughput, queue growth, dropped frames;
- peak/steady memory, power/thermal state;
- evidence age (timestamp of the newest evidence used);
- worst-case object count/resolution/history, not only average;
- capability layer damaged by compression/quantization/short context;
- hardware, OS/runtime, precision/backend, batch size;
- training/search/calibration cost separately from inference.

Pass condition: a pre-registered per-capability latency/quality budget is met **simultaneously** for the multi-capability workload. A single detector FPS is not a pass.

#### U14 — Same-protocol unified-model test

To claim “one model” rather than “a family/router”:

1. one checkpoint;
2. one forward pass for a multi-task request (or a declared, measured routing cost);
3. shared output interface for boxes/masks/alpha/text/identity;
4. joint training data mixture, with negative-transfer report;
5. all nineteen capabilities measured under matched data/compute;
6. multi-task latency and worst-case memory reported.

If any condition fails, report the system as “shared backbone + separate heads/checkpoints” or “routed experts”, not as a unified model.

#### U15 — Real-camera hidden-state identifiability

Purpose: test whether mass, friction, stiffness, object permanence and contact state are identifiable from **real RGB video**, not from synthetic video or language priors. Ground truth may use non-visual sensors for scoring, but the model path must be V0/V1 only.

| Hidden variable | Minimal real-camera test | Required controls / ground truth | Identifiability criterion | Failure criterion |
|---|---|---|---|---|
| Mass | Drop/oscillate/collide objects; predict mass or ranking | Scale ground truth; same shape/different density; same mass/different shape | Correct ranking + metric error + calibrated uncertainty on held-out objects | Uses size/appearance shortcut; error correlates with color/material label |
| Friction | Incline/slide; predict friction coefficient or stopping distance | Force/tribometer or controlled surface; same appearance/different surface | Ranking and stopping-distance prediction on unseen surfaces | Predicts from surface texture only; fails when appearance is decorrelated |
| Stiffness/deformability | Press/squeeze/poke; predict stiffness or deformation | Force/displacement sensor; same color/shape, different compliance | Ranking + deformation prediction on held-out materials | Uses object category prior; cannot detect visually similar soft/hard pairs |
| Object permanence | Occluder/out-of-FOV; query identity/position after delay | 360° camera or marker ground truth; equal-byte memory baselines | Reappearance identity + hidden position + belief revision | Short-term consistency only; confuses absent with unobserved |
| Support/contact | Remove support; push/stack; predict fall/contact | Force plate/contact sensor; controlled geometry | Predicts support removal and contact onset | Predicts plausible video but wrong contact timing |
| Causal intervention | Apply a controlled action; predict counterfactual outcome | Paired real intervention; same initial state | Counterfactual accuracy + intervention sensitivity | Matches observational correlation only; fails under action reversal |

**Protocol requirements:**

1. **Model path:** RGB (V0) or RGB+calibration (V1); no depth, force, tactile, WiFi, language prompt at inference. Ground-truth sensors are examiner-only.
2. **Decorrelate appearance and property:** same shape/color with different mass/friction/stiffness; same property with different appearance. Otherwise a “success” may be a visual shortcut.
3. **Held-out objects/materials:** split by object instance and material family, not random frames.
4. **Repeated trials:** ≥5 per object/condition; report mean, variance and worst case; cross-camera and lighting.
5. **Metrics:** ranking accuracy, metric error (MAE/MAPE), uncertainty calibration (ECE/coverage), refusal/unknown rate, equivalence-class reporting when the evidence cannot identify a unique value.
6. **Counter-evidence:** run the same protocol with tactile/WiFi/force available; if performance jumps, the RGB-only claim is bounded.
7. **Evidence level:** EV4 offline real data → EV5 real-to-sim/digital twin → EV7 proxy hardware; do not call it EV8 without the target robot.

**Pass condition:** the model beats appearance-only and language-only baselines on held-out objects, reports calibrated uncertainty, and refuses when the video cannot distinguish the hidden value. **Failure condition:** high average accuracy driven by object category, size, color or surface texture; no uncertainty; tactile/WiFi ablation shows the visual claim is not identifiable.

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

<a id="top"></a>

# 调研方向：世界状态、表示、记忆与压缩

Maintained: **2026-10-26** · Document stage: **1 — Research** ([status](../STATUS.md)).

Sufficiency, aliasing, abstraction, temporal persistence and diagnostics. No representation family is selected.

This is the canonical topic document. Update it in place; source-level dates and reading-depth labels below qualify the evidence, not the maintenance date.

<a id="compression-evidence"></a>

## 2026-10-25 当前补充：视觉压缩与未来证据保留

### FastV：必须把 FLOPs、时延和配置对应起来

- **来源：** Liang Chen 等，*An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models*，ECCV 2024。[论文 v3](https://arxiv.org/abs/2403.06764v3) · [核读正文](https://arxiv.org/html/2403.06764v3) · [官方代码](https://github.com/pkunlp-icler/FastV)。`PRIMARY_PAPER` / `OPEN_SOURCE`。
- **实际证据：** 按早期注意力评分删减后层视觉 tokens。`K=2,R=50%` 的约 45% FLOPs 降低是复杂度/任务质量结果；正文表 4 的实测时延使用 `K=0,R=50%`，不是同一配置。其 LLaVA-1.5-13B 在 A40、A-OKVQA 的逐例时延从 `0.539s` 到 `0.341s`，分数从 `82.0` 到 `80.5`；这是作者结果，不是本机 P50/P95。
- **观测与学习来源：** 图片/视频 QA 的 RGB 输入接近 `V0`，但还输入问题文本；已有 VLM 骨干含 `L2`，删 token 不会消除原有语言/视觉监督。不能写成 vision-only learning。
- **没有证明：** 当前问题的平均分保留意味着未来未知任务、短暂接触、身份切换或证据纠错仍受支持。核读摘要、§4.2、§5 及表 1/4；未复核全部附录或运行代码。

### FrameFusion：已有检索对照，但仍不等于可恢复性保证

- **来源：** Tianyu Fu 等，*FrameFusion: Combining Similarity and Importance for Video Token Reduction on Large Vision Language Models*，ICCV 2025，22654–22663。[论文 v2](https://arxiv.org/abs/2501.01986v2) · [核读正文](https://arxiv.org/html/2501.01986) · [官方代码](https://github.com/thu-nics/FrameFusion)。`PRIMARY_PAPER` / `OPEN_SOURCE`。
- **实际证据：** 早层合并相邻帧对应位置的相似 token，深层再按重要性裁剪；五项视频检索/QA/时空理解基准包含 VideoNIAH，可作为细节保留的现成对照。
- **预算与时延：** 相对 token budget 定义为层平均的 KV 序列长度；`30%` 预算不是每层或每帧都删去完全相同的 `70%`。v2 正文 §5.4 报告 `1.6–3.6×` 端到端加速，测试使用 NVIDIA A100-80GB，按模型规模使用一或多卡；不能迁移成 M4 的实测速率。代码 README 的端到端范围与论文 v2 不同，引用数值须固定版本。
- **观测与学习来源：** RGB 视频加问题文本，部分 VideoMME 条件另有字幕；骨干的语言/视觉训练来源含 `L2`。这些系统证据不能算严格 `V0/L0` 学习。
- **没有证明：** 跨任务延迟提问、反事实干预或被删证据的恢复。核读 §5.1、§5.3–5.4 与代码说明；未完整复核全文、全部附录或运行代码。

<!-- BEGIN current-cross-domain-evidence -->
<a id="current-cross-domain-evidence"></a>

## 当前跨领域与前沿证据：状态组织、信息压缩与表示目标

检索/核验：**2026-10-25（Asia/Shanghai）**。下表是外部研究记录，不是 Clover 的实验结果或架构决定。

当前比较应至少保留：统一 patch、对象/掩码、显式几何、语言记忆、物理结构和纯任务价值等互相竞争的状态假设。编码器、目标、数据、历史和读出成本要配平；高探针分数、重建分数、动作回报及未知后续任务证据保留分别报告。

### Hamiltonian Neural Networks

- **来源/版本：** [原论文](https://arxiv.org/abs/1906.01563v3)；初始提交 2019-06-04；本次返回版本更新于 2019-09-05。`PRIMARY_PAPER`。
- **问题与机制：** Hamiltonian Neural Networks 用能量函数及其导数约束动力学；包含像素摆实验。
- **输入/学习来源：** 多项任务给定位置/动量；像素实验仍需使潜变量满足近似正则坐标性质的辅助约束。
- **实际证据：** 保守系统与像素摆的轨迹/能量比较；是“什么结构应保留”的可检验先验。
- **不能推出 / 待区分：** 能量保持和可逆性不适用于所有耗散、碰撞、损伤或拓扑改变；不能把表示坐标当成已观察物理真值。
- **本次阅读深度：** 正文选读：方法、监督或局限段；未复核全部实验/证明。

### Lagrangian Neural Networks

- **来源/版本：** [原论文](https://arxiv.org/abs/2003.04630v2)；初始提交 2020-03-10；本次返回版本更新于 2020-07-30。`PRIMARY_PAPER`。 [作者提供的项目/代码入口](https://github.com/MilesCranmer/lagrangian_nns)（未运行复现）。
- **问题与机制：** Lagrangian Neural Networks 学习拉格朗日量，以欧拉—拉格朗日结构导出运动。
- **输入/学习来源：** 不要求正则动量，但仍使用坐标、速度与加速度训练目标；相应实验不是无条件 RGB 自监督。
- **实际证据：** 双摆、相对论粒子和连续系统等受控例子。
- **不能推出 / 待区分：** “无需正则动量”不等于“无需合适状态变量”；泛化到接触/外力/非保守系统须另证。
- **本次阅读深度：** 正文选读：方法、监督或局限段；未复核全部实验/证明。

### Koopman 深度坐标

- **来源/版本：** [原论文](https://arxiv.org/abs/1712.09707v2)；初始提交 2017-12-27；本次返回版本更新于 2018-04-13。`PRIMARY_PAPER`。
- **问题与机制：** Koopman 学习用自编码器寻找近似线性演化的内在坐标，并处理连续谱的参数化。
- **输入/学习来源：** 输入为动力系统轨迹；状态/观测坐标与采样条件是承重前提，不是任意真实 RGB 视频。
- **实际证据：** 非线性动力学的预测、坐标变换和谱结构。
- **不能推出 / 待区分：** 无限维算子表述不能直接推出所有系统都有精确、低维、可控且可解释的有限表示；噪声、接触切换和相机因素须显式测试。
- **本次阅读深度：** 正文选读：方法、监督或局限段；未复核全部实验/证明。

### Information Bottleneck

- **来源/版本：** [原论文](https://arxiv.org/abs/physics/0004057v1)；初始提交 2000-04-24；本次返回版本更新于 2000-04-24。`PRIMARY_PAPER`。
- **问题与机制：** Information Bottleneck 把压缩目标明确为保留关于指定相关变量 Y 的信息。
- **输入/学习来源：** 信息论问题中的联合分布与相关变量已经指定；V/L 协议不适用于这个抽象定理本身。
- **实际证据：** 提供区分压缩率、相关信息与失真定义的经典框架。
- **不能推出 / 待区分：** 对当前 Y 充分不等于对未知未来任务充分；不能以最小瓶颈或平均重建质量替代证据可恢复性。
- **本次阅读深度：** 摘要与书目核验。

### ALPS

- **来源/版本：** [原论文](https://arxiv.org/abs/2610.30120v1)；初始提交 2026-10-21；本次返回版本更新于 2026-10-21。`PRIMARY_PAPER`。 [作者提供的项目/代码入口](https://github.com/UCSC-VLAA/ALPS)（未运行复现）。
- **问题与机制：** ALPS 在同一 patch 表示中联合图文、重建、稠密对应，再做跨视图自蒸馏。
- **输入/学习来源：** 预训练仅静态图像和文本，包含 L2；状态探针标签是考官信息，不能反推训练获得真实状态。
- **实际证据：** 统一编码器比较、LIBERO 探针/策略及视觉规划；正文还记录不同能力随 refinement 的取舍。
- **不能推出 / 待区分：** 探针误差、策略成绩、检索和重建须分别报告；没有视频训练不等于没有语言/合成编辑先验。
- **本次阅读深度：** 正文选读：方法、监督或局限段；未复核全部实验/证明。

### VANE

- **来源/版本：** [原论文](https://arxiv.org/abs/2610.30724v1)；初始提交 2026-10-22；本次返回版本更新于 2026-10-22。`PRIMARY_PAPER`。
- **问题与机制：** VANE 用过去预测整幅下一帧语义嵌入，并以辅助生成保留空间细节。
- **输入/学习来源：** 固定语义 tokenizer 的知识来源必须继承；“自监督目标”不自动等于整条知识链 L0。
- **实际证据：** 图像/视频统一编码、动作预期、识别和稠密感知。
- **不能推出 / 待区分：** 与掩码预测比较时匹配 tokenizer、数据、未来可见性和算力；公开识别成绩不证明物理状态充分。
- **本次阅读深度：** 正文选读：方法、监督或局限段；未复核全部实验/证明。

### Slot-JEPA

- **来源/版本：** [原论文](https://arxiv.org/abs/2610.28074v1)；初始提交 2026-10-20；本次返回版本更新于 2026-10-20。`PRIMARY_PAPER`。 [作者提供的项目/代码入口](https://github.com/KID-7391/Slot-JEPA.git)（未运行复现）。
- **问题与机制：** Slot-JEPA 分开语义 slots 与空间 masks，用 transition memory 和非平衡最优输运比较预测/目标。
- **输入/学习来源：** Slot 分解不使用实例/部件标注，但继承视觉骨干；动作条件规划仍含 L3。
- **实际证据：** 视觉迁移、平面与机械臂规划；正文列明 slot 合并/拆分问题。
- **不能推出 / 待区分：** 语义 slot 不保证物理实体或接触部件身份；最优输运距离对规划有效不等于因果充分。
- **本次阅读深度：** 正文选读：方法、监督或局限段；未复核全部实验/证明。

### CADRE

- **来源/版本：** [原论文](https://arxiv.org/abs/2610.30129v1)；初始提交 2026-10-21；本次返回版本更新于 2026-10-21。`PRIMARY_PAPER`。 [作者提供的项目/代码入口](https://github.com/AdrienRR/cadre-autoencoders-and-world-models)（未运行复现）。
- **问题与机制：** CADRE 对固定特征上的时空瓶颈做控制变量比较，研究互动世界模型该如何压缩。
- **输入/学习来源：** 复用冻结视觉特征；机体操作与导航数据/动作来源分别记录。
- **实际证据：** 相同世界模型下的操控/导航四个环境，比较延迟、动作跟随与视觉质量。
- **不能推出 / 待区分：** 静止/移动相机的最优压缩不同；视觉质量保持不能保证运动、动作响应或未知后续任务证据保持。
- **本次阅读深度：** 正文选读：方法、监督或局限段；未复核全部实验/证明。

### WholeBodyMem / HuMeGo

- **来源/版本：** [原论文](https://arxiv.org/abs/2610.31166v1)；初始提交 2026-10-22；本次返回版本更新于 2026-10-22。`PRIMARY_PAPER`。
- **问题与机制：** WholeBodyMem 在目标执行前保留物体事件相关关键帧，再与当前对象信息共同控制。
- **输入/学习来源：** SAM3 和整身状态/动作数据须登记；并非仅看当前 RGB 的无先验系统。
- **实际证据：** HuMeGo 模拟/真实 G1 记忆任务；正文明确部分测试仍在训练布局/材质范围内。
- **不能推出 / 待区分：** Pre-history 成绩支持记忆需要，不能扩大成开放世界 OOD；目标何时公开、对象选择是否泄漏必须冻结。
- **本次阅读深度：** 正文选读：方法、监督或局限段；未复核全部实验/证明。

### PPMem

- **来源/版本：** [原论文](https://arxiv.org/abs/2610.23795v1)；初始提交 2026-10-16；本次返回版本更新于 2026-10-16。`PRIMARY_PAPER`。 [作者提供的项目/代码入口](https://hyzcluster.github.io/ppmem)（未运行复现）。
- **问题与机制：** PPMem 用平面几何作为生成视频的持久三维记忆：约 7 参数/平面，整场景约 100K primitives/5 MB；视频扩散 transformer 加平面预测头与 Depth Token Fusion，每个自回归 chunk 联合生成 RGB 与平面几何，合并后经渲染深度条件后续 chunk。
- **输入/学习来源：** 平面与深度预测、合并和历史生成构成条件链；其先验/训练监督按原文分开。视频骨干冻结，仅通过轻量 adapter 学几何，未端到端共适应。
- **实际证据：** DL3DV、RealEstate10K 的长序列跨视图视频生成和几何；作者报告在 288 帧、大视角变化下维持视频质量与深度，优于 Gen3C/Voyager/VMem/SPMem，并联合输出度量深度、法线与可导出平面。
- **不能推出 / 待区分：** 记住已经生成的平面，不等于跟踪真实世界被遮挡对象；作者自述适合平面结构场景，植被/水面等有机环境细节不足，训练外极端轨迹退化；细文字在放大后仍会乱码；平面紧凑性也不保证细小非平面接触证据被保留。
- **本次阅读深度：** 正文选读：方法、DL3DV/RealEstate10K 表、Limitations 与结论；未复核全部附录；未运行复现。

### PrismWAM

- **来源/版本：** [原论文](https://arxiv.org/abs/2610.26564v1)；初始提交 2026-10-19；本次返回版本更新于 2026-10-19。`PRIMARY_PAPER`。
- **问题与机制：** PrismWAM 分开语义目标图、深度空间物理 rollout 与动作生成。
- **输入/学习来源：** 初始 RGB 推理条件不抹除深度空间监督、骨干与动作学习来源。
- **实际证据：** 模拟/真实操作的表示分解反假设。
- **不能推出 / 待区分：** 显式深度不等于一般物理状态；几何、动作和数据预算配平后才可与统一 latent 模型比较。
- **本次阅读深度：** 摘要与书目核验。

### UniWALM

- **来源/版本：** [原论文](https://arxiv.org/abs/2610.28626v1)；初始提交 2026-10-20；本次返回版本更新于 2026-10-20。`PRIMARY_PAPER`。
- **问题与机制：** UniWALM 在同一主干共同生成视频、动作和语言，把语言重用作历史记忆。
- **输入/学习来源：** 即使不使用预训练语言模型，语言作为训练/输出目标仍属于 L2，动作属于 L3。
- **实际证据：** 组合操作、记忆子集与真实找物。
- **不能推出 / 待区分：** 单帧 anchor、文本记忆和 keyframe 对照的证据预算不同；语言记忆不能被默认视为视觉中立压缩。
- **本次阅读深度：** 摘要与书目核验。
<!-- END current-cross-domain-evidence -->

<!-- BEGIN world-model-frontier -->
<a id="world-model-frontier"></a>

## 世界模型前沿：生成、预测与可用状态不是同一件事

检索/核验：**2026-10-25（Asia/Shanghai）**。世界模型一词当前覆盖至少三类系统：预测下一帧的生成器、动作条件的潜在动力学、以及为策略训练提供想象 rollout 的学习模拟器。三者都能“预测未来”，但对**状态是否显式、动作是否条件、物理是否可干预、记忆是否持久**的要求不同。下列记录只支持各自评测条件下的结论。

| 方法 | 一手来源 | 机制与可核查证据 | 边界与反假设 |
|---|---|---|---|
| An Introduction to World Models | [2610.30789](https://arxiv.org/abs/2610.30789v1) | 从 POMDP 统一梳理世界模型与经典控制、动力系统、信号处理、RL 的关系；区分预测动力学、学习模拟器、联合生成观测与动作；主张条件预测可统一世界建模与策略学习 | 概念/导论，不含新实验；“统一”是表述框架，不是可识别性定理；未解决模型失配、开放世界新机制或真实相机证据 |

> CADRE 与 PPMem 的既有记录见[本方向既有证据](#current-cross-domain-evidence)，Grid or Nodes 见[评测方向](evaluation-and-benchmarks.md#evaluation-frontier)，DRILL 见[学习与数据](learning-and-data.md#current-cross-domain-evidence)；这里只补充尚未登记的世界模型证据，不重复计数。

### StarWM：让重建只发生在“与动力学相关”的区域

- **一手来源：** [固定版本](https://arxiv.org/abs/2609.30667v1)（NeurIPS 2026）。`PRIMARY_PAPER`。
- **机制：** 用自监督动力学训练的 cross-attention 决定重建应用于哪些区域；双流解码器只重建被 attend 的区域，stop-gradient 隔离重建与动力学目标，避免不可预测内容污染 latent；建立在 DreamerV3 骨架上。
- **输入与学习来源：** 视频/控制观测与自监督动力学；DeepMind Control 动态背景；无奖励版本用于主比较，reward-augmented 变体另记。
- **实际证据：** 作者报告 reward-free StarWM 在随机帧干扰下最强，在连续视频下显著优于重建式基线；reward-augmented 版本匹配或超过重建基线；速度与 DreamerV3/Iso-Dream++ 相当，慢于不做图像解码的 R2-Dreamer。
- **不能推出：** 自监督观测本身无法区分“可预测背景是任务相关还是干扰物”；小物体低于 8×8 attention 时退化；只在 DeepMind Control 验证；重建带来额外计算；不是真实机器人世界模型。
- **阅读深度：** 正文选读：方法、DMC 主结果、运行时间与 Limitations；未复核全部附录；未运行复现。

### Dreamer 4：在想象中训练智能体，但“世界”仍是游戏

- **一手来源：** [固定版本](https://arxiv.org/abs/2509.24527v1) · [项目页](https://danijar.com/dreamer4/)。`PRIMARY_PAPER` / `OFFICIAL_PROJECT`。
- **机制：** 学习动作条件的世界模型，用 shortcut forcing 与高效 transformer 实现单 GPU 实时交互推理；智能体完全在世界模型想象中做 RL；少量动作标注数据 + 大量无标签视频学习动作条件。
- **输入与学习来源：** Minecraft 视频与动作 `L3`；绝大部分知识来自无标签视频（动作条件仅少量标注）；离线数据，无环境交互。
- **实际证据：** 作者报告世界模型在 Minecraft 中准确预测物体交互与游戏机制，明显优于此前世界模型；首个仅用离线数据在 Minecraft 获得钻石的智能体，需选择 20,000+ 鼠标键盘动作。
- **不能推出：** 游戏机制是封闭、可重置、带动作标签的域；离线 RL 成功不证明真实相机下的物理/因果理解；实时交互数字未给出完整硬件/分辨率口径；“想象中成功”仍需真实环境验证；不是纯视觉学习（动作标签 `L3`）。
- **阅读深度：** 摘要与项目说明；未复核全部实验；未运行复现。

### Emu3.5：原生多模态世界学习器，生成能力与因果理解仍要分开

- **一手来源：** [固定版本](https://arxiv.org/abs/2510.26583v1) · [官方代码](https://github.com/baaivision/Emu3.5)（作者给定的 `emu.world` 项目页在本次核验中不可访问，不作为可复现 artifact）。`PRIMARY_PAPER` / `OPEN_SOURCE`。
- **机制：** 统一 next-token 预测，原生接受/生成交错视觉-语言序列；预训练语料 >10T tokens，主要来自互联网视频的连续帧与转写；大规模 RL 后训练；Discrete Diffusion Adaptation（DiDA）把逐 token 解码改为双向并行预测，作者报告每图推理约 20× 加速。
- **输入与学习来源：** 视频帧 + 转写/语言 `L2`，不是纯视觉；互联网视频的物理内容与剪辑偏差进入先验；RL 后训练的任务/奖励来源须另记。
- **实际证据：** 长程视觉-语言生成、任意到图像（X2I）、复杂文字图像生成；作者报告在图像生成/编辑上与 Gemini 2.5 Flash Image 可比，并在交错生成任务上更强；展示时空一致的世界探索与开放世界具身操作。
- **不能推出：** 生成逼真视频/图像不是因果模型；文本转写提供语言监督；世界探索的“一致性”由生成器自评/人评，不是干预实验；具身操作展示不等于真实机器人闭环；10T token 数据与算力不可复现。
- **阅读深度：** 摘要与项目说明；未复核全部实验；未运行权重。

### Gen4P：把视频生成器改造成前馈 4D 感知器

- **一手来源：** [固定版本](https://arxiv.org/abs/2610.22371v1) · [项目页](https://gen4p.github.io/)。`PRIMARY_PAPER` / `OFFICIAL_PROJECT`。
- **机制：** 复用预训练视频生成器的干净 latent，单次编码器前向，不用迭代去噪；轻量 cross-attention 解码器按 on-demand query 输出 4D 属性；连续时间 query 提供时间灵活性；冻结的视频深度 LoRA 作为几何先验。
- **输入与学习来源：** 单目视频；生成器预训练数据与深度 LoRA 监督另记（含 `L1/L4`），不是从零纯视觉学习。
- **实际证据：** 在 3D 点追踪、视频深度、相机位姿上达到 SOTA 或竞争性；野外视频定性显示复杂运动跟踪与细节保持。
- **不能推出：** 生成器先验可能补出视频中不存在的结构；4D 几何一致不等于物体身份、材质或接触理解；评测集中在几何任务；未证明实时性或长视频状态保持；生成式预训练的知识来源难以完全审计。
- **阅读深度：** 摘要与项目说明；未复核全部实验；未运行复现。

**本节结论：** 当前世界模型的前沿同时朝三个方向推进：更强的生成保真（Emu3.5/Gen4P）、更显式的持久几何（PPMem）、以及更贴近策略效用的想象训练（Dreamer 4/DRILL）。但“能生成”与“能识别可干预的物理状态”之间仍缺独立证据；尤其需要把**生成器自评、像素误差、策略回报、真实干预后状态**四类指标分开。Clover 若走纯视觉路线，必须证明其状态不是生成器写回的自身预测，也不是语言转写提供的语义捷径。
<a id="physics-world-models-2026"></a>

#### 2026 物理一致性与因果世界模型：从“生成得像”到“状态变得对”

检索/核验：**2026-10-26（Asia/Shanghai）**；候选检索窗口 2026-02→2026-10-25。以下全部为外部研究记录，不是 Clover 的实验结果或架构决定。

世界模型的最弱证据形态是**生成得像**：帧间平滑、物体不闪烁、镜头能跟随。更强的证据形态是**状态变得对**：给定动作或交互，场景的几何、接触与物理后果按可检验的方式演化。下表把 2026 年可核查的工作分成四层：**物理一致性基准**（World Models’ Last Exam in Physics）、**动作-后果预测**（DR-WM、STRIKE、P3Sim）、**因果/状态学习**（Causal-Plan、AVL-JEPA）、**多模态/长时程世界模型**（PhysCanvas、HapticWorld、AlayaWorld、Mirage2Matter）。它们共同说明：物理一致性开始有了可测量的验收面，但“能生成”仍不等于“能干预”或“能识别因果”。

| 方法 | 一手来源 | 机制与可核查证据 | 边界与反假设 |
|---|---|---|---|
| World Models’ Last Exam in Physics | [2610.08791](https://arxiv.org/abs/2610.08791v1) · [项目页](https://lab.einsia.ai/phys-last-exam) · 正文选读 | 测量式物理一致性基准：40 个受控任务覆盖力学、光学、流体、热与相变、电磁、表面张力；每个任务给定初始图像与提示，并定义可观测物理判据；评测器先做任务可观测性筛选，再做任务特定量化测量；8 个视频生成模型、1,280 条视频，最佳模型总分 57.76/100 | 初始帧由 GPT-Image-2.5 生成，评测器仍可能漏检某些不一致；40 任务不是穷尽；评分依赖可测关系，不含不可观测内部状态；基准是诊断工具，不是世界模型的充分证明 |
| DR-WM | [2610.17630](https://arxiv.org/abs/2610.17630v1) · 正文选读 | 从初始 RGB 重建场景几何，并用真实动作-响应数据校准稠密无量纲地形接触先验；给定机器人初始状态与候选动作，在 Genesis 中模拟未来运动并渲染视觉后果；Physcene-Robot 50 场景上动作依从 0.949、物理真实感 0.913（Matrix-Game 3.0 为 0.913/0.870）；100 人盲评中比最强基线高 9.3/7.6/8.8/5.5 点 | 依赖重建、接触建模与生成观测的准确性；生成观测会更新地形重建，误差可跨 rollout 传播；长时程几何/接触一致性仍是未来工作；四足机器人域，不是通用视觉物理 |
| STRIKE | [2610.09514](https://arxiv.org/abs/2610.09514v1) · 正文选读 | 把视觉状态转移学习与稠密视频生成分开：先从训练视频提取观测状态，配对转移描述与时间偏移；图像转移模型从当前图像、局部转移规范与流逝时间预测下一场景配置；推理时由 VLM 规划器给出时间转移规范，递归应用转移模型，再由动态模型生成完整 rollout；Physics-IQ Verified 上 41.9（CogVideoX-5B 骨干，基线 30.5），PhyGenBench 平均 76.91 | 状态生成误差会在递归组合中累积；转移模型用 64×A100 训练；需要事件对齐监督与 VLM 规划器；改进集中在物理一致性与操控视频保真，不等于因果识别 |
| P3Sim | [2606.27575](https://arxiv.org/abs/2606.27575v1) · 正文选读 | 物理世界建模系统：学习式物理世界模型 + 几何条件模块 + 持久场景记忆；在部分观测与不完整 3D 变换信号下模拟未来场景状态；NVS PSNR 21.54（SEVA 18.11），3DEditBench PSNR 23.12、EA 0.827 | 7B 自回归 transformer、300 万 RGB 视频剪辑、约 1.4 万亿 token；部分观测与不完整信号仍是根本约束；预测的是变换后的场景状态，不是物理因果；训练数据与基准域有限 |
| Mirage2Matter | [2602.00096](https://arxiv.org/abs/2602.00096v1) · 正文选读 | 用多视图环境视频与现成资产把真实环境重建为 3DGS 场景与前景物体，再在 Genesis 中执行物理正确的机器人运动并渲染成混合训练数据；真实机器人抓取成功率 Banana 80.0%、Croissant 86.7%（DISCOVERSE 60.0/66.7，RoboSimGS 76.7/76.7），每物体 30 次真实试验 | 需要多视图环境视频、SAM2 分割与 Genesis 物理引擎；物理先验来自模拟器而非视觉学习；30 次试验的统计置信有限；真实-模拟差距仍存在；不是纯视觉因果理解 |
| Causal-Plan | [2606.01810](https://arxiv.org/abs/2606.01810v5) · [官方代码](https://github.com/THUSI-Lab/Causal-Reasoner) · 摘要/正文表 | 把具身视觉-语言规划从“语言下一 token”推进到“物理因果下一状态”：Causal-Plan-Bench 覆盖可执行性、效果、组合、鲁棒性四个因果维度的 12 个诊断任务；Causal Planner（8B）Overall 45.28，+12.05 超过此前最强模型，并高于 GPT-6-astra 的 43.04；去掉视觉输入使 Overall 下降 16.92–22.38 点 | 基准限于具身家务/长时程任务；评分依赖 GPT-5.6-sol rubric；因果维度是任务级诊断，不是物理参数识别；视觉依赖证明有用，不证明纯视觉充分 |
| AVL-JEPA | [2610.03587](https://arxiv.org/abs/2610.03587v1) · 摘要/正文表 | 指出 JEPA 世界模型会保留高维视觉信息但丢失动作因果信息（causal dynamics information collapse）；用已执行动作作为动力学锚 + 视觉不变路径对齐扰动/干净潜预测；TwoRoom/PushT/Reacher/Cube 闭环成功率 93.2/96.0/85.2/78.2 | 仿真控制基准；“因果动力学信息”以动作-潜变量几何度量，不是物理参数真值；视觉不变路径仍依赖扰动协议；未证明真实机器人或开放世界因果 |
| PhysCanvas | [2610.28613](https://arxiv.org/abs/2610.28613v1) · [项目页](https://zebinx.github.io/PhysCanvas_HomePage/) · 摘要/正文表 | 状态一致视听觉-触觉世界模型：多视角 RGB、触觉图像、标记位移、任务状态与动作统一到同一视觉空间，共享视频 VAE 与生成骨干；RGB 指标最佳（PSNR 21.172、SSIM 0.735、LPIPS 0.121），EEF 误差 0.685 px，比次优低 51.9% | 触觉/接触动力学仍是近似；依赖多模态采集与统一 VAE；任务域有限；“状态一致”不等于物理正确；不是纯视觉 |
| HapticWorld | [2609.31924](https://arxiv.org/abs/2609.31924v1) · [项目页](https://haptic-world.github.io/) · 摘要/正文表 | 交互式世界模拟器，同时预测观测与关节扭矩并实时渲染回操作者，闭合人-世界模型触觉回路；三个任务上关节扭矩相对误差 4.8%/3.6%/3.5%；触觉反馈提升数据采集，训练出的策略能迁移到真实机器人 | 10 Hz 渲染低于机器人更新率；快速冲击/打滑不预测；每个场景需自采 play data 并单独训练；力觉是 `L4`，不是纯视觉；模拟器评估仍保留策略类别偏差 |
| AlayaWorld | [2607.18367](https://arxiv.org/abs/2607.18367v1) · [项目页](https://alaya-lab.github.io/AlayaWorld/) · 摘要/正文表 | 15B 视频扩散 Transformer 的交互长时程世界模型：24 fps、540p/720p，短潜 chunk 自回归生成，持久 sink 帧 + 压缩时间历史 + 几何对齐空间记忆 + 近帧条件；4 步去噪/块；iWorld-Bench 上亮度一致性 0.9492、色彩温度约束 0.9379、清晰度保持 0.8361、轨迹准确 0.7985、记忆对称 0.8871 | 视频生成先验 + 策展数据混合；“记忆”是视觉/空间一致性，不是物理状态或因果；长时程漂移用损坏历史与预测残差缓解，仍不等于可验证物理；交互是文本/相机/动作条件，不是物理闭环 |

> 世界模型的生成、预测与可用状态边界见[世界模型前沿](#world-model-frontier)；主动采证与干预见[因果与主动感知](causality-and-active-perception.md#current-cross-domain-evidence)。

#### World Models’ Last Exam in Physics：把“物理一致性”从观感变成可测量

- **一手来源：** [固定版本](https://arxiv.org/abs/2610.08791v1) · [项目页](https://lab.einsia.ai/phys-last-exam)。`PRIMARY_PAPER` / `OFFICIAL_PROJECT`。
- **机制：** 40 个受控任务覆盖九类物理现象：平移运动与碰撞、滚动/摩擦/刚体静力、旋转与振荡、光学与投影、流体静力学、热与相变、电磁、颗粒介质与表面张力。每个任务给出初始图像与提示，并预先定义可观测关系（空间关系、时间关系、事件证据）；评测器先检查时间一致性与任务可观测性，再用任务特定量化测量给出物理分。
- **输入与学习来源：** 初始帧由 GPT-Image-2.5 生成（`L2` 上游生成先验）；被测的是八个视频生成模型（Seedance、Cosmos 3、MiniMax-H3 等）的输出；评测器本身含 VLM 筛选与量化测量，不依赖参考视频。
- **实际证据：** 8 个模型、1,280 条视频；最佳模型 Seedance 的综合分约 57.76/100；不同任务间差异巨大。评测器在合成视频上的测量模块有效，且与人类排序/成对比较的一致性高于直接 VLM 基线。
- **不能推出：** 40 个任务不能穷尽物理一致性；初始帧由生成模型构造，可能带入分布偏置；评分只覆盖**可观测关系**，不含内部物理状态；57.76 是“仍有大量物理不一致”的证据，不是世界模型已达物理理解的证明。
- **阅读深度：** 正文选读：任务设计 §2、评测器 §3、主结果表 2–3、附录任务清单；未复核全部附录；未运行评测。

#### DR-WM：把可执行物理先验接进视觉世界模型

- **一手来源：** [固定版本](https://arxiv.org/abs/2610.17630v1)。`PRIMARY_PAPER`。
- **机制：** 从单张初始 RGB 重建场景几何；用真实四足机器人在不同地形上的动作-响应数据校准稠密、无量纲的地形接触先验；给定初始机器人状态与候选动作序列，在 Genesis 中模拟未来运动，得到物理一致的未来轨迹与相机运动，再渲染成视频。
- **输入与学习来源：** 初始 RGB + 机器人状态/动作 + 真实动作-响应校准数据（`L1` 物理先验）+ Genesis 模拟器（`L3`）；评测使用 Physcene-Robot 50 场景与 M20/Lite3 真实四足机器人片段。
- **实际证据：** 6 个 VLM 评维度上全为最佳：动作依从 0.949（Matrix-Game 3.0 0.913）、物理真实感 0.913（0.870）；100 人盲评中动作/物理合理性 93.1、运动保真 91.7、时间一致 92.4、视觉质量 90.8，分别比最强基线高 9.3/7.6/8.8/5.5 点；对 34 个 held-out 场景的冻结先验消融保持增益。
- **不能推出：** 预测可靠性依赖重建、接触建模与生成观测质量；生成观测会更新地形重建，误差可跨 rollout 累积；长时程几何/接触一致性仍是未解问题；四足机器人域，不是通用视觉物理；Genesis 物理是注入先验，不是从视觉学到的物理。
- **阅读深度：** 正文选读：方法 §3–4、表 1–3、盲评与消融；未复核全部附录；未运行复现。

#### STRIKE：把“状态转移”从稠密视频生成中拆出来

- **一手来源：** [固定版本](https://arxiv.org/abs/2610.09514v1)。`PRIMARY_PAPER`。
- **机制：** 训练视频先被解析为事件对齐的观测状态、转移描述与时间偏移；图像转移模型在当前图像、局部转移规范与流逝时间条件下预测下一场景配置；推理时 VLM 规划器给出时间转移规范，转移模型递归产生未来状态序列，另一个动态模型再生成完整视频。
- **输入与学习来源：** WISA、NVIDIA PhysicalAI、PhyCo/Kubric、PICA-100K、OpenVid-1M 与 RoboTwin2.0 的混合语料（`L1` 标注 + `L2` 基础模型）；转移模型用 64×A100 训练 5 epochs，动态模型 32 GPU 5000 步。
- **实际证据：** Physics-IQ Verified 上 CogVideoX-5B 骨干 41.9（基线 30.5，+11.4），Wan2.2-5B 骨干 39.7（14B 基线 34.2，+5.5）；ST-IoU/WS-IoU 分别 53.5/36.0；PhyGenBench 平均 76.91；Pisa-Experiments 上 L2/CD/IoU 均优于基线；RoboTwin2.0 val500 上超过视频骨干基线。
- **不能推出：** 递归组合会累积状态生成误差；需要事件对齐监督与 VLM 规划器；改进是“物理一致性与操控视频保真”，不等于因果识别或真实物理参数；训练算力大，非端侧；未给完整 limitations 节。
- **阅读深度：** 正文选读：方法 §3–4、Physics-IQ/PhyGenBench/Pisa/RoboTwin 表 1–6、消融；未复核全部附录；未运行复现。

#### P3Sim：在部分观测与不完整变换下模拟场景演化

- **一手来源：** [固定版本](https://arxiv.org/abs/2606.27575v1)。`PRIMARY_PAPER`。
- **机制：** 三个交互组件：学习式物理世界模型（把感知解释为多模态场景变量的概率推断）、几何条件模块（把期望的 3D 变换转成可执行条件）、持久场景记忆（把观测与推断变量跨帧整合，维持一致 3D 表示）；支持在部分观测与不完整 3D 变换信号下模拟未来场景。
- **输入与学习来源：** 训练用 300 万 RGB 视频剪辑、约 1.4 万亿 token；7B 自回归 transformer，仅监督内容 token；评测在 SEVA benchmark 与 3DEditBench 上做 NVS 与 3D 物体操作。
- **实际证据：** NVS PSNR 在 RE10K/LLFF/DTU 上 21.54/15.18/15.50（SEVA 18.11/14.03/14.47，ViewCrafter 20.88/10.53/12.66）；3DEditBench 上 PSNR 23.12、LPIPS 0.121、EA 0.827（LightningDrag 19.52/0.184/0.722）。
- **不能推出：** 部分观测与不完整信号仍是根本约束；预测的是变换后的场景状态，不是物理因果或接触力；训练数据与基准域有限；7B/1.4T token 的算力与数据规模不是端侧；未给真实机器人闭环。
- **阅读深度：** 正文选读：方法 §3–4、SEVA/3DEditBench 表 1–2、训练细节；未复核全部附录；未运行复现。

#### Mirage2Matter：用 3DGS + 物理引擎把真实环境变成可训练模拟器

- **一手来源：** [固定版本](https://arxiv.org/abs/2602.00096v1)。`PRIMARY_PAPER`。
- **机制：** 多视图环境视频重建为 3DGS 场景；SAM2 文本提示分割前景物体并逐物体优化 3DGS；Genesis 中规划并执行碰撞-free 轨迹，得到物理正确的机器人运动；再把 Genesis 中的机器人前景与 3DGS 光真实渲染背景合成训练视频，用于 VLA 策略训练并零样本迁移到真实机器人。
- **输入与学习来源：** 环境多视图视频 + 现成资产 + Genesis 物理引擎（`L3`）+ SAM2（`L2`）；策略用 PoSA-VLA 训练，每物体 300 条模拟演示，真实机器人 30 次试验。
- **实际证据：** 真实机器人抓取成功率 Banana 80.0%、Croissant 86.7%（DISCOVERSE 60.0/66.7，RoboSimGS 76.7/76.7）；真实演示上界 96.7/90.0；3DGS 物体表示相对 mesh 一致提升成功率；任务级 Press Button 93.3 vs 真实 96.7，Push/Pull 73.3 vs 83.3。
- **不能推出：** 需要多视图环境视频与现成资产，不是任意单目 RGB；物理先验来自 Genesis，不是视觉学习；30 次试验的置信区间有限；真实-模拟差距仍存在；策略成功不等于物理理解。
- **阅读深度：** 正文选读：方法 §3、表 1–3、真实机器人结果；未复核全部附录；未运行复现。

**2026 补充结论：** 物理一致性开始有了可测量的验收面，但三条边界必须同时写清：

1. **基准分数不是物理理解。** World Models’ Last Exam 的 57.76/100 说明最佳视频世界模型在受控任务上仍有大量物理不一致；P3Sim/STRIKE/DR-WM 的改进集中在场景状态与动作后果，不等于因果参数识别。
2. **物理先验仍来自外部。** DR-WM 用 Genesis 与真实动作-响应校准，Mirage2Matter 用 Genesis + SAM2 + 3DGS，HapticWorld/PhysCanvas 依赖触觉/多模态；没有一条是纯 RGB 学到的物理。
3. **“记忆”与“一致性”不是物理状态。** AlayaWorld 的记忆对称 0.8871 是视觉/空间一致性；AVL-JEPA 防的是潜变量几何塌缩；Clover 若把世界模型当作物理状态，必须分别验收**几何一致性、接触/力、因果参数、干预后状态、记忆真值**，不能用单一生成分数替代。

<!-- END world-model-frontier -->

<!-- BEGIN long-video-memory -->
<a id="long-video-memory-2026"></a>

## 长视频与第一人称记忆：持久状态、事件索引与主动记忆

短时追踪和世界模型回答“接下来会发生什么”，但长时间的第一人称生活还要求另一种能力：**在数小时到数月后，仍能找回某个物体、某次事件或某个状态变化，并区分“相似但不同”的经历**。这与 PPMem/PersistBench 的短时持久性不同：长视频记忆的核心不是单帧重建，而是**写什么、如何索引、如何读、何时主动写**。本轮补 10 篇 2026 年工作，覆盖 4D 场景图记忆、持久 3D 物体记忆、流式记忆基准、超长视频检索与工作记忆重写。

| 方法 | 一手来源 | 机制与可核查证据 | 边界与反假设 |
|---|---|---|---|
| R4DSG | [2608.11017](https://arxiv.org/abs/2608.11017v1)（ACM MM 2026） · 正文选读 | 相对 4D 场景图记忆：把长视频压成按时间/地点/持久物体索引的可查询条目，保留物体身份与锚点转移；EgoLifeQA A1_JAKE 单被试 255 题上总体 39.6%（EgoRAG-Text 32.9，+6.7），when 43.1%（30.6，+12.5）；why 子集 33.3→40.0；828 clips 压成 134 文档/0.58 MB JSON | 单被试、离线回溯、非在线更新；依赖 Qwen3.5-27B 回答；错误来自漏事件、轨迹碎片/重复、锚点杂乱、检索失败；不是人类核验的感知基准；跨天持久性有限 |
| Ledger | [2610.10538](https://arxiv.org/abs/2610.10538v1) · [项目页](https://ledger-3d.github.io) · [代码](https://github.com/LEDGER-3D/LEDGER) · 正文选读 | 持久 3D 物体记忆：物体位置、历史与上下文描述；按静止位置聚类、重复证据才记一次移动；包含从未被触碰的物体；HD-EPIC 2,400 题 42.6%（blind 29.7、ReMEmbR 29.8、DirectMe 30.7）；VQ3D 中位 L2 0.99 m（SAM3，51% <1 m）；UCS-Bench 记忆-only 38.5%（blind 33.8），帧+记忆 46.3% | 离线构建；计数/连续静止区间弱；场景切换会让检索与构建同时失效（回到 blind 水平）；依赖标定位姿/深度，UCS 多数记忆缺度量尺度；不是在线因果记忆 |
| EgoProbe | [2610.17128](https://arxiv.org/abs/2610.17128v1) · 正文选读 | 流式第一人称记忆基准：长程保留（多远）+ 事件特异回忆（在相似事件干扰下多准）；19 个模型，最佳 GPT-5.6-Sol 仅 55.32% Base/43.69% 两轮；SimpleStream 两轮 6.75%；ultra-long（≥12 h）仅 28–40%；相关事件≥3 时事件链接错误率显著上升；VST 粗问 95.28% 但两轮仅 33.93% | 受 EgoLife 录制覆盖限制；无音频；多为 MLLM 语言读出；两轮指标要求两轮全对；不是纯视觉记忆；未跨月/年 |
| EgoMonth | [2608.13113](https://arxiv.org/abs/2608.13113v1) · 摘要 | 月级第一人称基准：20 名参与者、20–120 天、300+ 小时、1,443 道人工选择题；14 项任务分三层认知（Schema Consolidation、Episodic Indexing 等），测试跨天/跨周一致记忆 | 摘要级；MLLM 语言问答；参与者/场景有限；不是纯视觉；任务/标注成本高；不能推出通用长时记忆 |
| ProactEgoMem | [2610.30089](https://arxiv.org/abs/2610.30089v1) · 摘要 | 流式第一人称“主动记忆”基准：信息捕获（IC）、状态跟踪（ST）、位置跟踪（LT）三类任务；要求系统在用户不提问时主动决定记什么、何时维护 | 摘要级；主动策略的代价/误记未核；基准场景有限；不是端到端视觉系统 |
| MemLife | [2609.40195](https://arxiv.org/abs/2609.40195v1) · 摘要 | 长期第一人称记忆系统：实体锚定的第一人称文本 episode + 时间索引 agentic reader；无需训练、查询时不回看原始视频；作者报告比最强 training-free 基线高 4.6–12.0% | 文本化记忆丢失视觉细节；依赖实体/转写质量；不是纯视觉；长时检索竞争仍可能失败；摘要未给全部基准 |
| VideoLoop | [2609.38119](https://arxiv.org/abs/2609.38119v2) · [代码](https://github.com/philipxjm/videoloop) · 正文选读 | 长视频 agent 的“语义 thrashing”：append-only 工作记忆越长，关键证据注意力越塌缩；用外层推理 + 内层 orchestrator 重写有界工作记忆，并从文件系统检索；VideoMME long +5.1、VideoMMMU +4.1、LongVideoBench +5.9（Gemini 3 Flash）；Q4 难度 +9.3；token 仅 +0.5% | 依赖 Gemini/Claude 等强策略模型与字幕；不是纯视觉；记忆重写本身是 LLM 行为，可能丢证据；基准为语言 QA；未证明真实机器人长时任务 |
| PREM | [2609.23601](https://arxiv.org/abs/2609.23601v1) · [代码](https://github.com/siruzhong/PReM) · 正文选读 | 冻结 VLM 的 prefix-steered recurrent memory：query-agnostic 写入 256 KiB 多槽关联状态，问题条件 readout 以 K/V 调制注入非视觉前缀；只训 27.5M 参数（<0.30%）；流式 Avg +1.43（Qwen3-VL-8B）、LVBench ≥60 min +5.61%；状态 0.063 MiB、ingest 7.81 s vs InfiniPot-V 17.44 s、无额外 prompt token | 仍是语言模型读出；状态压缩会丢细节；离线/流式均在基准 QA 上验证；不是 3D/物体身份记忆；训练数据 LLaVA-Video-178K 子集；未证明跨场景/跨月 |
| MERIT | [2608.07663](https://arxiv.org/abs/2608.07663v2)（ECCV 2026 Oral） · [项目页](https://choi-yeeun.github.io/MERIT/) · 摘要 | 超长视频两阶段：query-agnostic 多键 episodic memory 构建 + 推理时时间扩展；优先高召回检索，把高层关系组合推迟到查询时；作者报告在超长视频基准上强于复杂记忆构建 | 摘要级；依赖 MLLM/agent；记忆构建仍以文本/帧为单位；不是纯视觉；未核全部数值 |
| LongEgoRefer | [2607.02096](https://arxiv.org/abs/2607.02096v1)（ECCV 2026） · [代码](https://github.com/shunya-kato/LongEgoRefer) · 摘要 | 长时第一人称视频指代表达理解基准：视频长、目标稀疏出现、活动切换复杂；给出时序+空间定位与语言指代 | 语言查询任务；不是纯视觉；基准规模/指标摘要未全；指代成功不等于持久记忆；标注成本 |

### R4DSG：记忆结构比回答模型更关键

R4DSG 的出发点是：长第一人称问答的失败往往不是“回答模型不够强”，而是记忆里没有**持久物体身份与锚点转移**。它把视频压成相对 4D 场景图，按时间、地点、持久物体索引，再检索成文档交给 Qwen3.5-27B。EgoLifeQA 单被试 255 题上总体 39.6%，比 EgoRAG-Text 高 6.7；when 问题 43.1% vs 30.6（+12.5）；why 子集从 33.3 到 40.0；828 clips 只压成 134 个文档、0.58 MB JSON。

它的证据边界很硬：单被试、离线回溯、非在线更新；错误来自漏事件、轨迹碎片/重复、锚点杂乱与检索失败；不是人类核验的感知基准。它给 Clover 的启发是：**长时记忆的最小单位应是“持久物体 + 地点 + 状态转移”**，而不是 caption 或帧；但“记忆结构好”仍可能被检索失败和单被试偏差掩盖。

### Ledger：记住“没被碰过的东西”，但场景切换会击穿记忆

Ledger 建持久 3D 物体记忆：每个物体有位置、历史与上下文描述；按静止位置聚类，只有重复证据才记一次移动，避免把定位噪声当移动；并且记住从未被触碰的物体。HD-EPIC 2,400 题 42.6%，blind 29.7、ReMEmbR 29.8、DirectMe 30.7；VQ3D 中位 L2 0.99 m（SAM3），51% 预测 <1 m；UCS-Bench 记忆-only 38.5%，帧+记忆 46.3%。

它揭示三个反直觉点：**(1) 相机参考系误差比物体坐标误差更伤回答**——方向问题依赖相机朝向，位姿误差可损失 11 点；**(2) 重复证据比提高距离阈值更能区分“移动”与“定位噪声”**——0.8 m 阈值只有 57.3% 计数正确，0.3 m + 连续三次位移证据升到 67.4%；**(3) 场景切换会同时破坏检索与构建**——回到 blind 水平，按场景重建只能恢复约一半。它还明确：计数/连续静止区间未解决，HD-EPIC 用标定位姿，UCS 多数记忆缺度量尺度，构建离线。对 Clover，这意味着“持久物体记忆”必须带**坐标系、场景边界、写入证据次数**，否则会把噪声写成历史。

### EgoProbe：长程与“精确”是两种能力，模型在两者上都失败

EgoProbe 把流式第一人称记忆拆成两个维度：**长程保留**（能记多久）与**事件特异回忆**（在相似事件干扰下能否记住“哪次是哪次”）。19 个模型中最好的 GPT-5.6-Sol 也只有 55.32% Base / 43.69% 两轮；SimpleStream 两轮仅 6.75%，说明“最近帧窗口”在长程记忆上几乎无效；ultra-long（≥12 h）所有模型只有 28–40%；相关事件≥3 时，事件链接错误率显著上升——模型常选到“另一个相似事件”的正确答案。VST 粗问 95.28%，但两轮只有 33.93%，说明“知道大概”不等于“记得细节”。

它的限制是数据覆盖 EgoLife、无音频、以 MLLM 读出为主。但它给 Clover 的验收提供了一条硬标准：**长时记忆必须同时测“多远”和“多准”，并用相似事件做干扰**；只测“能否回答”会把“选对相似事件”误判为记忆成功。

### EgoMonth、ProactEgoMem、MemLife、MERIT、LongEgoRefer：基准与系统的边界

EgoMonth 把时间尺度拉到 20–120 天、300+ 小时、1,443 道人工题，14 项任务分三层认知，直接测试跨天/跨周一致记忆；ProactEgoMem 则要求系统在用户不提问时主动决定“记什么、何时维护”，分信息捕获、状态跟踪、位置跟踪三类任务；MemLife 用实体锚定的第一人称文本 episode + 时间索引 reader，报告比 training-free 基线高 4.6–12.0%；MERIT 用多键 episodic memory + 推理时时间扩展，优先高召回检索；LongEgoRefer 把长时第一人称指代表达做成基准，目标稀疏出现、活动切换复杂。

这些工作共同把“记忆”从单段视频扩展到天/月尺度，但也暴露共同依赖：**文本化/实体化记忆、MLLM reader、语言查询**。它们能证明“结构化记忆有用”，不能证明“纯视觉持久状态”已经成立；文本 episode 会丢视觉细节，实体锚定会受转写/检测错误影响，语言查询会把语义捷径带入评分。

### VideoLoop 与 PREM：工作记忆要“重写”，不是“追加”

VideoLoop 给出一个结构性诊断：append-only 工作记忆会“语义 thrashing”——上下文越长，关键证据的注意力越塌缩；它用外层推理 + 内层 orchestrator 重写有界工作记忆，并从文件系统按需检索。VideoMME long +5.1、VideoMMMU +4.1、LongVideoBench +5.9（Gemini 3 Flash），Q4 难度 +9.3，token 只增 0.5%。PREM 走另一条路：冻结 VLM，用 256 KiB 多槽关联状态做 query-agnostic 写入，问题条件 readout 以 K/V 调制注入；只训 27.5M 参数，流式 Avg +1.43，LVBench ≥60 min +5.61%；状态 0.063 MiB，ingest 7.81 s，无额外 prompt token。

两者的共同结论是：**长时记忆的关键操作是“压缩/重写/检索”，不是把更多帧塞进上下文**。但两者都是语言模型读出，记忆单位是文本/特征/状态，不是可检验的 3D 物体身份；它们能提升 QA，却不能证明“世界状态被持久保留”。对 Clover，正确的借鉴是记忆管理机制（有界工作记忆、写入门控、查询条件读出），而不是把 QA 分数当成世界理解。

**本节结论：** 长视频/第一人称记忆的证据可以归为三类：**结构化空间记忆**（R4DSG、Ledger）、**长程/精确回忆基准**（EgoProbe、EgoMonth、ProactEgoMem、LongEgoRefer）、**工作记忆管理**（VideoLoop、PREM、MERIT、MemLife）。它们共同证明：记忆结构、写入策略与读出方式比“上下文长度”更重要；也共同暴露三个缺口：**(1) 纯视觉记忆薄**——多数系统依赖文本 episode、MLLM reader 或语言查询；**(2) 精确性未解**——相似事件干扰下事件链接错误率仍高；**(3) 场景/时间边界脆弱**——场景切换、跨月、在线更新都会击穿离线构建的记忆。Clover 若声称“通过视觉理解真实世界”，长时记忆必须至少报告：存了什么（物体/地点/状态转移）、写入证据与来源、读出时的坐标系/场景边界、长程与精确两维指标、以及相似事件干扰下的错误类型；单段视频 QA 分数不能替代这些证据。
<!-- END long-video-memory -->


<!-- BEGIN broad-vision-primary-evidence -->
<a id="broad-vision-primary-evidence"></a>

## 广义视觉理解的一手比较证据

核验日：2026-10-25。以下是外部方法与反例，覆盖经典接口、当前基础视觉与跨领域条件；未被采纳为 Clover 架构。

### Pix2Seq 多任务接口

- **一手来源：** [固定版本](https://arxiv.org/abs/2206.07669v2) · [作者资源](https://github.com/google-research/pix2seq)。
- **机制：** 把框、轮廓、关键点、类别和描述序列化，用任务提示共享自回归训练接口。
- **输入与学习来源：** 视觉输入与任务 token；框/关键点/掩码 L1，描述与语言目标 L2。
- **实际证据：** 四类任务的统一架构/目标和联合训练对照。
- **边界与反假设：** 离散坐标、轮廓和输出序列长度限制精度与时延；统一接口未证明统一长期状态或 AGI。
- **阅读深度：** 正文选读：任务接口与输出编码；未复核全部实验；未运行复现。

### Florence-2

- **一手来源：** [固定版本](https://arxiv.org/abs/2311.06242v1) · [作者资源](https://huggingface.co/microsoft/Florence-2-large)。
- **机制：** 提示驱动的统一图像到序列接口，覆盖图像、区域与像素层次任务。
- **输入与学习来源：** FLD-5B 图像及海量自动视觉/文本标注，含 L1/L2；数据引擎知识不能归零。
- **实际证据：** 多种感知任务的共享模型与微调/零样本比较。
- **边界与反假设：** 单图/单轮任务覆盖未证明在线追踪、长期因果状态或 AGI；需区分一个权重、统一架构及任务微调结果。
- **阅读深度：** 正文选读：统一任务与数据说明；未复核全部实验；未运行复现。

### HALO

- **一手来源：** [正式会议记录](https://www.roboticsproceedings.org/rss22/p010.html) · [论文](http://www.roboticsproceedings.org/rss22/p010.pdf)。
- **机制：** 用 VLM 生成历史问答辅助训练检索，再用稀疏注意力限制误差历史的影响。
- **输入与学习来源：** RGB、可含本体状态与历史动作，语言指令/教师、示范，含 L2/L3/L4。
- **实际证据：** 多类历史信息的模拟及真实长时操作对照。
- **边界与反假设：** 任务相关问题可能筛掉未知未来任务所需证据；检索正确、状态真实与动作成功须分开检验。
- **阅读深度：** 正文 §III 与任务/实验设置选读；未运行复现。

### ViPSim

- **一手来源：** [正式会议记录](https://www.roboticsproceedings.org/rss22/p014.html) · [论文](http://www.roboticsproceedings.org/rss22/p014.pdf)。
- **机制：** 将端执行器投影、相机/深度/形态图与数值动作共同约束长时视频生成。
- **输入与学习来源：** 动作、相机矩阵、深度几何及形态先验，含 L3/L4，非严格 RGB-only 接口。
- **实际证据：** 轨迹与视频几何一致性对照。
- **边界与反假设：** 作者记录机械臂轨迹正确但炉门不动等失败；当前主要静态相机验证，兼容动态相机的设计不等于已验证。
- **阅读深度：** 正文条件接口与 §V 局限选读；未运行复现。

### Causal-JEPA

- **一手来源：** [正式会议记录](https://proceedings.mlr.press/v306/nam26c.html) · [论文](https://raw.githubusercontent.com/mlresearch/v306/main/assets/nam26c/nam26c.pdf)。
- **机制：** 遮挡对象级 latent，迫使由其他对象/历史预测，学习交互相关影响邻域。
- **输入与学习来源：** 对象编码、时序数据和任务特定监督按实验分记；理论预设对象对齐表示与共享动态机制。
- **实际证据：** 反事实问答及 PushT latent 规划的比较。
- **边界与反假设：** 作者将邻域定义为预测充分集而非真实因果父节点，且未直接用显式时间因果图验证；对象编码质量限制上限。
- **阅读深度：** 正文 §5–6、影响邻域解释与局限选读；未运行复现。

### ITC token 对应

- **一手来源：** [正式会议记录](https://proceedings.mlr.press/v306/kim26bq.html) · [论文](https://raw.githubusercontent.com/mlresearch/v306/main/assets/kim26bq/kim26bq.pdf)。
- **机制：** 将下一帧 token 解码为复制旧 token 或新生成的结构化分配。
- **输入与学习来源：** 已有 token 世界模型及强化学习环境/动作经验；不是无监督真实世界识别。
- **实际证据：** 改善生成中的消失/复制与视觉强化学习回报。
- **边界与反假设：** token 对应关系不是物理实体身份的可识别性定理；需独立测物体、部件、遮挡与编辑，而非只看回报。
- **阅读深度：** 正文问题设定、对应变量与解码说明选读；未运行复现。
<!-- END broad-vision-primary-evidence -->

## Contents

- [World-Model Frontier: Generation, Prediction and Usable State](#world-model-frontier)
- [Long Video and Egocentric Memory](#long-video-memory-2026)
- [Minimum Sufficient World State](#topic-research-research_sufficient_state)
- [State Aliasing and Representation Failure](#topic-research-research_state_aliasing)
- [Adaptive Abstraction, State Granularity and Multi-Timescale Structure](#topic-research-research_adaptive_abstraction)
- [R-C — Representation: Explicit, Distributed, Object-Centric or Hybrid?](#topic-research-dossiers-r-c-representation)
- [R-D — Persistence, Memory and Belief Revision](#topic-research-dossiers-r-d-memory-persistence)
- [Learned Visual Representations](#topic-docs-research-map-learned-visual-representations)
- [Object-Centric Representation](#topic-docs-research-map-object-centric-representation)
- [Video Representation and World Models](#topic-docs-research-map-video-world-models)
- [Stage-1 Emerging Audit — Representation Diagnostics and Causal Use](#topic-research-emerging-representation_diagnostics_2026-10-15)

<a id="topic-research-research_sufficient_state"></a>

## Minimum Sufficient World State

Source record updated: 2026-10-14
Source intake checked through: **2026-10-14**

> **Research question:** How can a machine understand the real world through vision alone?

This is a Stage-1 theory/background document. It does **not** propose a Clover architecture.

Its purpose is to study a second foundational question:

> Even if the real world contains many variables, which information must an embodied agent actually retain for prediction, planning, control, memory, revision and generalization?

The central distinction is:

```text
complete physical description
≠
minimal predictive state
≠
minimal control-sufficient state
≠
general-purpose world state.
```

"Minimal" is meaningful only relative to what the state must support.

---

### 1. History, state and compression

Let the interaction history be:

```text
H_t = (O_1, A_1, O_2, A_2, ... , O_t)
```

and let an internal representation be:

```text
Z_t = F(H_t).
```

The representation is useful only if it preserves the information required by future queries/actions while discarding information that can safely be ignored.

A generic design question is:

```text
How much of H_t must Z_t preserve?
```

A second question is:

```text
Preserve it for what purpose?
```

Those two questions define the sufficient-state problem.

---

### 2. Different notions of sufficiency

Stage 1 should not use the word "sufficient" without specifying the target.

#### 2.1 Predictive sufficiency

For future observations/outcomes `Y`, a representation is predictively sufficient when, conceptually:

```text
P(Y_future | H_t, A_future)
=
P(Y_future | Z_t, A_future).
```

`Z_t` then preserves what the history contributes to the chosen prediction problem.

This does **not** automatically imply that the representation is sufficient for reward, planning, intervention or belief revision.

#### 2.2 Control sufficiency

For a task/reward family, state is control-sufficient if the optimal decision need not access information discarded from history.

Conceptually:

```text
Q*(H_t, a) = Q*(Z_t, a)
```

for relevant actions/tasks.

A representation can be excellent for reconstruction while discarding small task-relevant distinctions, or highly control-sufficient while discarding appearance details.

#### 2.3 Planning sufficiency

Planning needs enough state to predict the consequences of candidate actions and compare possible futures.

This can differ from one-step policy sufficiency.

#### 2.4 Memory / revision sufficiency

A representation can be sufficient for the current task but insufficient when:

```text
an object leaves view
the world changes
a new query is asked later
old evidence must be reinterpreted
```

Long-term robotic state may therefore need to preserve evidence or uncertainty that a short-horizon policy would safely discard.

#### 2.5 Causal / counterfactual sufficiency

Prediction under the observed behavior distribution may not preserve the variables needed for unseen interventions.

A state sufficient for:

```text
What usually happens next?
```

may fail for:

```text
What would happen if I intervene differently?
```

#### 2.6 Open-world / multi-task sufficiency

A state optimized for one fixed reward can aggressively discard information irrelevant to that task.

A general-purpose robot is different: future tasks may be unknown when the representation is formed.

Therefore:

```text
task-specific minimality
```

and:

```text
general-purpose minimality
```

should be treated as distinct research problems.

---

### 3. POMDP belief state: a canonical sufficient statistic under a known model

Background survey:

- Partially Observable Markov Decision Processes in Robotics — https://arxiv.org/abs/2209.10342

In a POMDP, the true state is hidden and the agent maintains a belief:

```text
b_t(s) = P(S_t = s | H_t).
```

Given the assumed transition/observation model, the belief state is a sufficient statistic of the observation-action history for optimal decision making.

Why it matters for Clover:

The belief-state view makes several distinctions explicit:

```text
world state S_t
≠
observation O_t
≠
belief b_t.
```

But it also exposes a practical problem:

- the true state variables may not be known in advance;
- the transition model may be wrong;
- the belief can be high dimensional;
- open-world robotics cannot assume a fully specified finite hidden-state model.

So POMDPs are a theoretical anchor, not a ready-made Clover representation.

---

### 4. Predictive State Representations: state as predictions rather than hidden variables

Foundational source:

- Littman, Sutton, Singh, **Predictive Representations of State** — https://papers.nips.cc/paper_files/paper/2001/hash/1e4d36177d71bbb3558e43af9577d70e-Abstract.html
- Paper PDF — https://proceedings.neurips.cc/paper/2001/file/1e4d36177d71bbb3558e43af9577d70e-Paper.pdf

Predictive State Representations (PSRs) represent state using predictions of future observation outcomes under possible action sequences.

Conceptually:

```text
state
=
a sufficient set of predictions about future observable tests.
```

This is important because it challenges the assumption that useful world state must correspond to a hand-specified set of hidden physical variables.

Related work:

- A Nonlinear Predictive State Representation — https://papers.nips.cc/paper_files/paper/2003/hash/72e6d3238361fe70f22fb0ac624a7072-Abstract.html
- Efficient Learning and Planning with Compressed Predictive States — https://jmlr.org/papers/v15/hamilton14a.html

Stage-1 question:

> Could a sufficiently rich action-conditional predictive representation serve as machine world state without reconstructing all latent physical variables explicitly?

Counter-question:

> Does predictive sufficiency under learned tests preserve persistence, causal intervention and open-ended future-task information?

---

### 5. Information state and Approximate Information State

Primary theory reference:

- Approximate Information State for Approximate Planning and Reinforcement Learning in Partially Observed Systems — https://www.jmlr.org/beta/papers/v23/20-1165.html
- Code metadata — https://github.com/info-structures/ais

This work defines information state as a function of history that is sufficient for dynamic programming, including formulations based on predicting reward and the next information/observation state.

Approximate Information State (AIS) relaxes exact sufficiency and provides bounds relating approximation error to loss of optimality.

This is highly relevant to realistic robotics because exact sufficient statistics may be too expensive or impossible to learn.

Stage-1 implication:

```text
perfect world-state recovery
```

may not be necessary if an approximate compressed state preserves the information needed for near-optimal action.

But the approximation target must be explicit.

---

### 6. State abstraction / bisimulation: discard distinctions that do not matter for control

Control representation literature often asks when two states may be treated as equivalent.

A bisimulation-style intuition is:

```text
states can be merged when
rewards are equivalent
and
future transition behavior is equivalent
under relevant actions.
```

Recent example:

- Revisiting Bisimulation Metric for Robust Representations in Reinforcement Learning — https://arxiv.org/abs/2507.18519

Important theoretical caution:

- Which Mutual-Information Representation Learning Objectives are Sufficient for Control? — https://arxiv.org/abs/2106.07278

That work formally studies control sufficiency and shows that some intuitive mutual-information objectives can still learn insufficient representations.

Stage-1 implication:

> Compression quality should be judged by preserved decision structure, not merely reconstruction, contrastive loss or mutual information.

---

### 7. Detecting when a learned representation is not Markov enough

**Mitigating Partial Observability in Sequential Decision Processes via the Lambda Discrepancy**
NeurIPS 2024: https://proceedings.neurips.cc/paper_files/paper/2024/hash/73073ccb3bc559fd001e66b9079d6d5e-Abstract-Conference.html

The work introduces a discrepancy between temporal-difference estimators with different `lambda` values as a diagnostic of non-Markovian state representations under partial observability.

Why it matters:

A representation may look compact and semantically meaningful yet still omit historical information necessary to make the future conditionally depend only on the current representation.

This suggests a useful later Clover diagnostic:

```text
Does adding more past history still improve prediction/value after conditioning on Z_t?
```

If yes, `Z_t` may not yet be a sufficient state for the measured task.

---

### 8. 2026 world-model research is converging on sufficiency as a design question

#### 8.1 Latent State Design for World Models under Sufficiency Constraints

Primary paper: https://arxiv.org/abs/2605.01694
Evidence: `PRIMARY_PAPER`

The paper explicitly frames world-model research as designing latent state under functional sufficiency constraints.

It distinguishes roles such as:

```text
predictive embedding
recurrent belief state
object / causal structure
latent action interface
grounded planning interface
memory substrate
```

and emphasizes that predictive sufficiency, control sufficiency, planning, memory and counterfactual support are not interchangeable objectives.

This is directly aligned with the current Clover Stage-1 question.

#### 8.2 DELE-w0.5: future latent state instead of dense video

**Inferring Action from Future Latent State for Robotic Manipulation**
Primary paper: https://arxiv.org/abs/2608.22067

DELE argues that generating all intermediate future pixels is an unnecessarily expensive target for manipulation and instead predicts a compact future latent state representing the action-relevant physical outcome.

Research contrast:

```text
pixel-trajectory prediction
vs
action-relevant future-state prediction.
```

This is strong evidence that a world model need not reproduce every visual detail to be useful for control.

But it does not establish that the compact latent is sufficient for arbitrary future tasks, persistent memory or counterfactual reasoning.

#### 8.3 Representation World Model

**Representation World Model: Learning States, Transition and Executable Plans in Representation**
Primary paper: https://arxiv.org/abs/2609.29171

RWM learns representation geometry such that latent paths between endpoint representations preserve enough transition structure for inverse dynamics to recover executable actions.

Research hypothesis:

```text
planning-relevant geometry can live directly inside representation space.
```

Again, this is planning/control sufficiency evidence, not proof of complete world understanding.

---

### 9. Dense video generation may preserve too much information — or the wrong information

Video-generation world models attempt to preserve rich visual detail.

That may be useful because future tasks are not always known.

But it is expensive and can allocate capacity to visually salient properties that are irrelevant to action.

The key trade-off is:

```text
retain all visual detail
→ flexible but expensive / hallucination-prone

retain task-relevant compact state
→ efficient but risks discarding information needed later.
```

Stage 1 should keep both possibilities open.

Relevant comparison sources:

- World-Action Models survey — https://arxiv.org/abs/2609.16074
- DELE-w0.5 — https://arxiv.org/abs/2608.22067
- Representation World Model — https://arxiv.org/abs/2609.29171
- Riemann-1.0 — https://arxiv.org/abs/2608.27033
- HWAM — https://arxiv.org/abs/2610.12026

---

### 10. A proposed Stage-1 sufficiency taxonomy

For later Analysis, label what a representation is intended to preserve.

```text
S-PRED   predictive sufficiency
S-CTRL   control sufficiency
S-PLAN   planning sufficiency
S-MEM    long-horizon memory / revision sufficiency
S-CAUSE  intervention / counterfactual sufficiency
S-EPI    uncertainty / belief sufficiency
S-OPEN   open-world / future-task sufficiency
```

A method can satisfy one without satisfying the others.

Example:

```text
strong S-PRED
weak S-EPI
```

could describe a generative future model that predicts plausible futures but cannot represent what is genuinely unknown.

Likewise:

```text
strong S-CTRL for task A
weak S-OPEN
```

could describe a highly compressed task-specific policy state.

This taxonomy is only a research annotation scheme; it is not a Clover architecture.

---

### 11. Why general-purpose robotics makes "minimal" difficult

Suppose a robot only needs to place a cup on a table.

It may not need:

```text
cup brand
exact texture
thermal state
internal liquid composition
```

But the same robot may later receive:

```text
Is this cup too hot to touch?
Pour exactly 100 ml.
Use the unbroken ceramic cup, not the plastic one.
Check whether the liquid changed color overnight.
```

Information that was irrelevant to one task can become relevant later.

Therefore a general-purpose robotic brain faces a fundamental tension:

```text
compression / efficiency
vs
future-task optionality.
```

Possible research solutions include, without endorsement:

```text
rich persistent world state
+
small task-conditioned working state

raw/selective evidence memory
+
compressed current belief

hierarchical state at multiple resolutions

dynamic state expansion when a new task requires more detail
```

These are possibilities to study later, not Stage-1 conclusions.

---

### 12. Evidence retention may solve part of the minimality problem

If the online decision state is compressed, the system could still retain selected evidence for later reinterpretation.

This separates:

```text
what must be in the current decision state
```

from:

```text
what evidence should remain recoverable.
```

This is relevant to:

- S-EMBER — https://arxiv.org/abs/2607.02689
- VISTA — https://arxiv.org/abs/2610.02200
- PersistBench — https://arxiv.org/abs/2609.20819

Historical Clover Evidence Replay ideas belong in Stage 4 Innovation; these external results only establish that persistent evidence/memory is an independent research dimension.

---

### 13. Proposed later diagnostics for representation sufficiency

Stage 2/6 should eventually test sufficiency directly rather than infer it from one benchmark score.

#### 13.1 History leakage / Markov test

Ask whether prediction/control improves after giving the downstream model extra history beyond `Z_t`.

If yes, the state omitted useful information.

#### 13.2 State aliasing counterexamples

Find two histories:

```text
H_a != H_b
```

that map to nearly the same representation:

```text
Z(H_a) ≈ Z(H_b)
```

but require different future predictions/actions.

This directly exposes insufficient compression.

#### 13.3 Task-transfer sufficiency

Freeze the state representation and introduce a new downstream task.

Measure whether relevant information was retained before the task was known.

#### 13.4 Intervention sufficiency

Test matched histories under different controlled interventions.

A state may be prediction-sufficient on observational data yet intervention-insufficient.

#### 13.5 Memory/revision sufficiency

After long occlusion or external world change, test whether state plus retained memory supports correct revision.

#### 13.6 Uncertainty sufficiency

Two representations may achieve similar accuracy but differ in whether they preserve the distinction between:

```text
known absent
vs
unobserved
vs
ambiguous.
```

#### 13.7 Action-efficiency Pareto curve

Measure:

```text
state bytes / latent dimension / memory cost
vs
task success / prediction / planning quality.
```

The objective should be a Pareto frontier, not smallest latent dimension at any cost.

---

### 14. Open research questions

1. Is there a task-independent finite-dimensional sufficient state for open-world robotics in practice?
2. Should general-purpose world state optimize future-task optionality instead of minimum dimension?
3. Can PSR-style action-conditional predictions scale to high-dimensional open visual worlds?
4. When is belief over explicit variables better than a distributed latent predictive state?
5. How can a learned representation expose when it is not Markov/sufficient?
6. Which state dimensions should be persistent versus reconstructed on demand from stored evidence?
7. Can a compact future latent support counterfactual planning, not only behavior-distribution actions?
8. How much information does dense video generation preserve that compact WAM states later turn out to need?
9. Can representation granularity adapt to task requirements without catastrophic loss of previously useful distinctions?
10. Is the best robotic state a single vector at all, or a collection of differently scoped state/memory structures?

---

### Stage-1 provisional conclusion

The research target should not be:

```text
recover every physically meaningful variable at maximum precision.
```

Nor should it be:

```text
compress observations as aggressively as possible.
```

A better research question is:

> What information must the machine preserve so that its internal state remains sufficient for the family of predictions, decisions, interventions, memories and future tasks that define general robotic intelligence?

This reframes world-model design as a question of **sufficiency under partial observability**, not simply latent dimensionality or reconstruction fidelity.

**Keep the answer open until Stage 2/3 compare the competing sufficiency hypotheses.**

---

<a id="topic-research-research_state_aliasing"></a>

## State Aliasing and Representation Failure

Source record updated: 2026-10-14

> **Research question:** How can a machine understand the real world through vision alone?

This is a Stage-1 research document. It does **not** propose a Clover architecture.

Its purpose is to study a failure mode that can remain hidden even when a learned representation looks compact, predictive or useful on average:

> Two physically or decision-relevantly different world histories may be mapped to the same internal state.

That failure is called **state aliasing** or **perceptual aliasing** in different literatures.

---

### 1. Minimal formulation

Let the history available to the agent be

```text
H_t = (O_1, A_1, O_2, ..., O_t)
```

and let a learned state encoder construct

```text
Z_t = F(H_t).
```

Aliasing occurs when two histories

```text
H_t^a ≠ H_t^b
```

map to approximately the same internal state

```text
F(H_t^a) ≈ F(H_t^b)
```

although they differ in something that matters for a required future function, for example:

```text
future observation distribution
action consequence
reward/value
object identity
hidden physical parameter
causal response
uncertainty
correct information-gathering action
```

The key point is task dependence:

```text
same latent state may be sufficient for task A
but aliased for task B.
```

State aliasing is therefore directly connected to [`representation-and-memory.md`](#topic-research-research_sufficient_state).

---

### 2. Historical active-perception definition

**Learning to Perceive and Act by Trial and Error / Active Perception and Reinforcement Learning**
Primary/background source: https://doi.org/10.1023/A:1022619109594
Conference version: https://doi.org/10.1016/B978-1-55860-141-3.50025
Evidence: `BACKGROUND_REFERENCE`

Whitehead and Ballard explicitly describe perceptual aliasing as a consequence of an internal representation that confounds external world states and show why this can destabilize decision learning.

The historical relevance for Clover is strong:

```text
representation failure
can create the need for
active information collection.
```

The agent may need to look again, move, or otherwise collect discriminating evidence before acting.

---

### 3. Markov-state failure can be detected without seeing true hidden state

#### λ-discrepancy

**Mitigating Partial Observability in Sequential Decision Processes via the Lambda Discrepancy**
NeurIPS 2024: https://papers.nips.cc/paper_files/paper/2024/hash/73073ccb3bc559fd001e66b9079d6d5e-Abstract-Conference.html
ArXiv: https://arxiv.org/abs/2407.07333
Project: https://lambda-discrepancy.github.io/
Evidence: `PRIMARY_PAPER`

The paper introduces the λ-discrepancy between temporal-difference estimates with different λ values. Because TD(0) assumes a Markov state while TD(1) can retain longer temporal dependence, disagreement is used as a signal that the current representation is non-Markovian.

Stage-1 interpretation:

```text
if giving the learner more history changes the correct value estimate,
the current state representation has discarded decision-relevant history.
```

This is useful because it does not require direct access to the true hidden state.

What it does **not** establish:

- that zero λ-discrepancy proves universal world understanding;
- that the representation is sufficient for every downstream task;
- that the missing variable is physically interpretable;
- that the learned memory is optimal for open-world transfer.

---

### 4. Partial observability can be discovered from visual inconsistency

#### PO-PDDL

**PO-PDDL: Learning Symbolic POMDPs from Visual Demonstrations for Robot Planning Under Uncertainty**
Primary paper: https://arxiv.org/abs/2606.15654
Evidence: `PRIMARY_PAPER`

PO-PDDL reconstructs latent symbolic state trajectories from real-robot execution videos and identifies partial observability through inconsistencies between inferred symbolic state and visible observations. It then learns stochastic transition and observation models for belief-space planning.

Why it matters:

This is a structured example of treating aliasing as a model mismatch:

```text
current visual observation
is insufficient to decide
which latent symbolic state is true.
```

It provides a useful explicit-state baseline even if Clover later uses a very different representation.

---

### 5. Observable equivalence is not the same as physical equality

#### Observable quotient world models

**Observable quotient world models for knowledge-state abstraction under partial observability**
Journal page: https://www.sciencedirect.com/science/article/pii/S0950705126014942
DOI: https://doi.org/10.1016/j.knosys.2026.116768
Evidence: `PRIMARY_PAPER`

This 2026 work defines quotients from action-conditioned observation laws, builds quotient beliefs/filtering/dynamics and explicitly studies which world distinctions are supported by observation.

Stage-1 value:

It sharpens an important distinction:

```text
physically different states
may be observationally equivalent
under the current sensor/action protocol.
```

A world representation should not be punished for failing to distinguish states that the available evidence cannot distinguish. Instead it should preserve uncertainty or equivalence until new evidence breaks the tie.

---

### 6. Bisimulation gives a behavior-based abstraction criterion

#### Classical/control representation perspective

**Invariant Representations for Reinforcement Learning without Reconstruction**
OpenReview: https://openreview.net/forum?id=kmaPnFKCuq
Evidence: `PRIMARY_PAPER`

Bisimulation-based representation learning groups states when they have equivalent reward and transition behavior, deliberately removing visually different but behaviorally irrelevant information.

#### 2026 state-abstraction theory

**Compositional Behavioral Semantics for State Abstraction in Reinforcement Learning**
PMLR: https://proceedings.mlr.press/v306/zhang26dy.html
ArXiv: https://arxiv.org/abs/2606.25357
Evidence: `PRIMARY_PAPER`

This work develops a general framework for reasoning about what behavioral properties are preserved under abstraction, including invariants, bisimulation relations and behavioral metrics.

#### 2026 visual bisimulation geometry

**PAMD: Structured Adaptive Distances for Bisimulation Representations in Visual Reinforcement Learning**
PMLR: https://proceedings.mlr.press/v306/roh26a.html
Evidence: `PRIMARY_PAPER`

PAMD shows that even after choosing bisimulation as the abstraction principle, the metric used to compare latent states matters: fixed global norms can be too restrictive, while unconstrained distances can become degenerate.

Stage-1 implication:

```text
abstraction criterion
and
latent geometry
are separate research choices.
```

---

### 7. Aliasing taxonomy for Clover research

Stage 1 should distinguish at least:

#### A1 — perceptual aliasing

Different external states produce similar/currently indistinguishable visual observations.

Examples:

```text
occluded object present vs removed
same-looking containers with different contents
same surface appearance with different friction
```

#### A2 — history aliasing

The current frame is the same, but different histories imply different correct beliefs.

Examples:

```text
object was moved while previously visible
switch was toggled earlier
container was filled earlier
```

#### A3 — representation aliasing

The observation/history contains the information, but the learned encoder discards it.

#### A4 — action aliasing

Different embodiments/controllers map numerically similar actions to different physical consequences.

Related source: SyncWorld — https://arxiv.org/abs/2609.09155

#### A5 — causal aliasing

Two states look similar under passive observation but respond differently to intervention.

#### A6 — task aliasing

A representation deliberately merges states because they are equivalent for the current task, although another future task would need the distinction.

This is not necessarily an error; it becomes an error when the task distribution changes.

---

### 8. Candidate diagnostics for later stages

Stage 1 records these only as future evaluation ideas.

#### Diagnostic D-A1 — history-rescue test

```text
performance with Z_t
vs
performance with Z_t + additional history
```

If history reliably improves the relevant prediction/control query, `Z_t` is not sufficient for that function.

#### Diagnostic D-A2 — intervention split

Construct two histories that are visually similar now but differ in hidden causal state. Apply the same probe action and measure whether predicted outcomes diverge correctly.

#### Diagnostic D-A3 — counterfactual nearest neighbors

Search latent nearest neighbors for states with different valid action consequences. High collision rate indicates action-relevant aliasing.

#### Diagnostic D-A4 — belief calibration under unresolved aliases

When two worlds remain observationally compatible, measure whether the model preserves uncertainty rather than collapsing to one guess.

#### Diagnostic D-A5 — task transfer after compression

Train/construct a compact state for task A, then evaluate whether task B exposes information that the representation irreversibly discarded.

---

### 9. Adjacent gaps discovered

State aliasing connects directly to several additional Stage-1 areas:

```text
structured memory
multi-timescale dynamics
belief-state calibration
non-stationarity / world change
active information gathering
open-world task transfer
```

Important 2026 references include:

- Flow Equivariant World Models — https://proceedings.mlr.press/v306/lillemark26a.html — structured latent memory aligned with self-motion/external motion under partial observability.
- HiMe — https://proceedings.mlr.press/v306/ji26k.html — hierarchical working/long-term memory for non-Markovian long-horizon VLA tasks.
- OASIS-Map — https://arxiv.org/abs/2607.14899 — world change across sessions.
- R4DSG — https://arxiv.org/abs/2608.11017 — persistent relative 4D object/change memory.

---

### 10. Stage-1 questions

```text
When do two physically different worlds become observationally indistinguishable?
When is that ambiguity removable by history?
When is it removable only by action?
When does a learned representation discard information that was actually available?
Which state distinctions are necessary for prediction, action, memory, causality and open-world transfer?
Can we detect aliasing without privileged ground-truth state?
How should a system represent unresolved aliases: one latent point, a distribution, a set, particles, hypotheses, or something else?
```

---

### Current rule

Do not demand that a representation distinguish states that the available evidence cannot distinguish.

Do demand that it avoid collapsing states that differ in a capability the system claims to support.

```text
indistinguishable from available evidence
≠
representation failure

information was available but discarded
=
potential representation failure
```

---

<a id="topic-research-research_adaptive_abstraction"></a>

## Adaptive Abstraction, State Granularity and Multi-Timescale Structure

Source record updated: 2026-10-14

> **Research question:** How can a machine understand the real world through vision alone?

This is a Stage-1 research document. It does **not** propose a Clover architecture.

Its purpose is to study whether a robotic world representation should use one fixed state granularity, or adapt what it preserves according to task, timescale, uncertainty, embodiment and interaction phase.

---

### 1. Core problem

The physical world contains far more state than any robot can represent at maximum detail all the time.

A useful abstraction must therefore answer:

```text
What can be safely compressed?
What must remain explicit?
What should be coarse now but refined later?
Which distinctions matter only for the current task?
Which distinctions must survive because future tasks are unknown?
```

The central tension is:

```text
compression / efficiency
vs
preserving future-relevant distinctions.
```

---

### 2. Task-specific abstraction is not automatically universal understanding

#### Causal Bisimulation Modeling

**Building Minimal and Reusable Causal State Abstractions for Reinforcement Learning**
AAAI 2024: https://ojs.aaai.org/index.php/AAAI/article/view/29507
Evidence: `PRIMARY_PAPER`

CBM learns causal dependencies in dynamics/rewards and derives minimal task-specific abstractions that keep variables needed for each task.

Why it matters:

It demonstrates a legitimate use of selective state:

```text
full environment state
→ task-conditioned subset
```

But it also exposes a Clover risk:

```text
minimal for current task
≠
sufficient for future unknown task.
```

---

### 3. State abstraction needs preservation guarantees

#### Compositional Behavioral Semantics

**Compositional Behavioral Semantics for State Abstraction in Reinforcement Learning**
PMLR: https://proceedings.mlr.press/v306/zhang26dy.html
ArXiv: https://arxiv.org/abs/2606.25357
Evidence: `PRIMARY_PAPER`

This ICML 2026 work studies what behavioral structures are provably preserved when a concrete system is mapped into an abstraction.

Relevant preserved structures include:

```text
values
invariants
bisimulation-like relations
behavioral metrics
```

Stage-1 implication:

A representation should not be called “good abstraction” only because it is small or visually invariant. We need to specify **what property is promised to survive the abstraction**.

---

### 4. Multi-timescale state is a serious alternative to one-resolution state

#### Temporally hierarchical active-inference world model

**Real-World Robot Control by Deep Active Inference With a Temporally Hierarchical World Model**
Primary paper: https://arxiv.org/abs/2512.01924
Evidence: `PRIMARY_PAPER`

The system models dynamics at slow and fast timescales and compresses action sequences into abstract actions. Its abstract world model predicts slower future states for tractable action selection.

Research question:

```text
Should fast contact/motion state
and slow task/world state
live at different temporal resolutions?
```

#### S2-HWM

**S2-HWM: Sparse Event-Structured Hierarchical World Model for Long-Horizon Surgical Robot Manipulation**
Primary paper: https://arxiv.org/abs/2608.13103
Evidence: `PRIMARY_PAPER`

S2-HWM learns sparse event evidence and separates event-level manager updates from primitive-step control. Event transitions have variable duration rather than a fixed clock rate.

Why it matters:

```text
physical time step
≠
meaningful world-state update event.
```

Some state should be updated continuously; other state may only need revision when a contact, subgoal, topology change or semantic event occurs.

---

### 5. Hierarchical world state can mix symbolic and perceptual levels

#### H-WM

**H-WM: Robotic Task and Motion Planning Guided by Hierarchical World Model**
Primary paper: https://arxiv.org/abs/2602.11291
Evidence: `PRIMARY_PAPER`

H-WM jointly predicts high-level logical state transitions and low-level visual state transitions.

This provides a useful counter-hypothesis to a single homogeneous latent state:

```text
logical / relational state
+
visual / geometric state
```

may be maintained at different abstraction levels.

What it does **not** establish:

- that symbolic state is necessary for general robotics;
- that the chosen predicates are open-world sufficient;
- that one fixed hierarchy transfers to arbitrary tasks.

---

### 6. Hierarchical memory can be organized by operating timescale

#### HiMe

**HiMe: Hierarchical Embodied Memory for Long-Horizon Vision-Language-Action Control**
PMLR: https://proceedings.mlr.press/v306/ji26k.html
Evidence: `PRIMARY_PAPER`

HiMe separates a high-frequency executor, a working-memory sentry and a long-term planner, and supports Add/Update/Delete memory operations.

Stage-1 relevance:

It suggests that **state access frequency** may itself be an abstraction variable:

```text
high-frequency motor-relevant state
working state
long-horizon episodic/semantic state
```

This is related to, but distinct from, representational granularity.

---

### 7. Structured equivariance can preserve detail without storing it naively

#### Flow Equivariant World Models

**Flow Equivariant World Models: Structured Memory for Dynamic Environments**
PMLR: https://proceedings.mlr.press/v306/lillemark26a.html
Project: https://flowequivariantworldmodels.github.io/
Evidence: `PRIMARY_PAPER`

This work builds latent memory that transforms equivariantly with self-motion and inferred object motion, so out-of-view information remains aligned as the observer/world moves.

Why it matters:

Adaptive abstraction is not only about deleting information. Another strategy is to encode known transformation structure so the same information can be maintained more efficiently and consistently.

---

### 8. Task semantics may determine which relations deserve explicit representation

#### Semantically Rich World Models

**Beyond Instance Slots: Semantically Rich World Models for Physical Interaction Planning**
Official project/publication page: https://www.max-robotics.com/en/research/publications/cmu42t6js00r9pd42avv37dcb
Evidence: `PRIMARY_PAPER` / `OFFICIAL_PROJECT`

The method structures planning state around functional roles such as gripper, target, goal, relation and phase rather than only generic object identity.

Stage-1 implication:

```text
entity identity
alone may be too fine in one way
and too weak in another.
```

The abstraction required for planning may be role- and task-conditioned.

---

### 9. Hierarchy can also operate over subgoals

#### ViGAR

**Rethinking World-Action Model for Compositional and In-Context Robotic Manipulation**
Primary paper: https://arxiv.org/abs/2610.02368
Evidence: `PRIMARY_PAPER`

ViGAR separates a visual subgoal planner from a subgoal executor, using a shared pretrained world-model representation.

This is not necessarily a world-state hierarchy, but it matters because state granularity and action horizon are coupled:

```text
primitive action horizon
subtask horizon
full-task horizon
```

may require different state summaries.

---

### 10. Non-stationarity means a previously sufficient abstraction can become wrong

A world representation may be sufficient under one dynamics regime and fail after the robot, controller, environment or task distribution changes.

#### ReDRAW

**Adapting World Models with Latent-State Dynamics Residuals**
PMLR/L4DC 2026: https://proceedings.mlr.press/v331/lanier26a.html
Evidence: `PRIMARY_PAPER`

ReDRAW pretrains a latent world model in simulation and adapts it to changed target dynamics by learning residual corrections in latent-state dynamics. It evaluates both vision-based control domains and a physical visual lane-following task.

Stage-1 relevance:

```text
same representation
+
changed transition law
```

can require adaptation even when observations remain visually similar.

#### Changepoint-Aware World Models

**Changepoint-Aware World Models: Detecting Dynamics Shifts and Recovering by Forgetting Stale Replay in Model-Based RL**
Primary paper: https://arxiv.org/abs/2609.18950
Evidence: `PRIMARY_PAPER`

CAWM detects abrupt dynamics shifts from internal prediction error using an online changepoint test and then discards stale replay while retaining the learned representation.

Why it matters:

It separates two questions:

```text
What is uncertain under the current model?
```

from:

```text
Has the current model itself become stale because the dynamics changed?
```

This is a form of **world-model falsification / regime-change detection**, not ordinary state estimation.

#### ROAM

**Adapt On-the-Go: Behavior Modulation for Single-Life Robot Deployment**
PMLR/CoLLAs 2026: https://proceedings.mlr.press/v330/chen26a.html
Evidence: `PRIMARY_PAPER`

ROAM adapts within one deployment episode to novel situations and changed dynamics using a repertoire of learned behaviors, including a real quadruped dynamics-shift demonstration.

This is useful evidence that open-world robotics requires **online recognition of regime mismatch**, not only offline robustness.

#### WorMI

**World Model Implanting for Test-time Adaptation of Embodied Agents**
PMLR/ICML 2025: https://proceedings.mlr.press/v267/yoo25a.html
Evidence: `PRIMARY_PAPER`

WorMI retrieves and composes domain-specific world models at test time for unseen domains.

#### Sirius-Fleet

**Multi-Task Interactive Robot Fleet Learning with Visual World Models**
PMLR/CoRL 2025: https://proceedings.mlr.press/v270/liu25g.html
Project: https://ut-austin-rpl.github.io/sirius-fleet
Evidence: `PRIMARY_PAPER`

Sirius-Fleet uses a visual world model and anomaly predictors to monitor deployment and trigger human correction when future outcomes are predicted to be anomalous.

Stage-1 relevance:

A robot world model may need not only prediction but a **failure-monitoring contract**:

```text
prediction
→ compare against realized evidence
→ detect anomaly / mismatch
→ decide whether to adapt, ask for help, or revise the model.
```

Research question:

```text
when should one world model be adapted,
when should another model be selected,
when should the system request external correction,
and when should it conclude that no existing model is adequate?
```

---

### 11. Embodiment itself changes the meaning of state and action

#### LAC-WM

**Cross-Embodiment Robot Foundation World Models with Latent Actions**
PMLR/ICML 2026: https://proceedings.mlr.press/v306/huang26bv.html
ArXiv: https://arxiv.org/abs/2610.10846
Project: https://lacwm.github.io/
Evidence: `PRIMARY_PAPER`

LAC-WM learns a unified latent action space across diverse robot embodiments and compares it with explicit action conditioning. The paper reports that explicit action spaces fragment across embodiments while the learned latent action representation transfers better to unseen robots.

Stage-1 implication:

```text
numerical action label
≠
embodiment-independent action meaning.
```

This strengthens the need to treat **self/embodiment state** as part of the world-model interface rather than a fixed external assumption.

#### OSCAR

**OSCAR: Omni-Embodiment Skeleton-Conditioned World Action Model for Robotics**
Primary paper: https://arxiv.org/abs/2606.04463
Evidence: `PRIMARY_PAPER`

OSCAR uses a 2D kinematic skeleton rendering as a common conditioning representation across robot arms and human hands. This is another candidate answer to cross-embodiment action semantics.

#### Embodiment Gap survey

**The Embodiment Gap in Robot Foundation Models**
Primary survey: https://arxiv.org/abs/2608.18433
Evidence: `SURVEY_SIGNAL`

The survey distinguishes what can be shared across robots from the adaptation work still required on a new body. It is useful as a reporting framework for separating reusable world knowledge from embodiment-specific execution machinery.

Neither result proves a universal embodiment representation; together they show that action/world abstraction depends strongly on how the robot body is represented.

---

### 12. Adaptive abstraction taxonomy

Stage 1 should distinguish at least:

#### G1 — task-conditioned abstraction

Keep only distinctions needed for a specified objective.

#### G2 — temporal abstraction

Represent fast and slow dynamics at different rates.

#### G3 — event-conditioned abstraction

Refine/update state around semantically meaningful transitions rather than every frame.

#### G4 — spatial abstraction

Use global coarse structure plus local high-resolution detail.

#### G5 — entity/relation abstraction

Move between dense scene representation, entities, relations and functional roles.

#### G6 — uncertainty-conditioned abstraction

Allocate more state/detail where uncertainty or decision sensitivity is high.

#### G7 — embodiment-conditioned abstraction

Keep state variables relevant to the current robot/action interface.

#### G8 — open-world reserve

Retain enough recoverable evidence so future tasks can reconstruct distinctions that were not important at the moment of compression.

#### G9 — regime-conditioned abstraction

Change representation/model assumptions when dynamics, domain or environment regime changes.

This is especially important for Clover's long-term general-purpose goal.

---

### 13. Failure modes of abstraction

#### Over-abstraction

```text
states that require different actions become merged
hidden changes are forgotten
a new task needs information that was discarded
```

#### Under-abstraction

```text
state becomes unnecessarily large
planning becomes expensive
irrelevant visual variation dominates representation
memory grows without bound
```

#### Wrong abstraction boundary

```text
correct object state but wrong task relation
correct visual detail but missing contact mode
correct short-term state but lost long-horizon event history
```

#### Static abstraction under non-stationarity

```text
state was sufficient yesterday
but dynamics / embodiment / controller / task distribution changed today.
```

A general-purpose system therefore needs a way to detect when an abstraction/model is no longer adequate.

---

### 14. Representation reversibility is an under-studied requirement

Compression can discard information that later becomes useful.

For a general-purpose robot, Stage 1 should distinguish:

```text
lossy active state
vs
recoverable evidence store / provenance
```

A state may remain compact while preserving links to evidence from which omitted distinctions can later be reconstructed.

This is not a recommendation for any historical Clover replay mechanism; it is a generic research requirement:

> If the future task distribution is unknown, how much information should remain recoverable after abstraction?

This connects memory, provenance, abstraction and open-world optionality.

---

### 15. Candidate later diagnostics

#### D-G1 — task-switch stress test

Train/compress for task A and test whether task B exposes irreversibly lost information.

#### D-G2 — granularity-cost Pareto curve

Measure:

```text
state size / memory / compute
vs
prediction
control
planning
memory
causal reasoning
```

#### D-G3 — local refinement test

Allow a coarse representation to request high-resolution local state only when needed; compare with always-fine and always-coarse baselines.

#### D-G4 — timescale ablation

Compare one-rate memory/state against multi-timescale or event-driven state updates.

#### D-G5 — unknown-future-task retention

Evaluate whether raw evidence/provenance allows reconstruction of information that the active abstraction omitted.

#### D-G6 — regime-shift detection

Change dynamics, camera, controller or embodiment and measure:

```text
mismatch-detection latency
adaptation time
false alarms
catastrophic interference
recovery of calibrated prediction/control
```

#### D-G7 — embodiment transfer

Keep task/environment fixed while changing robot morphology/action interface; test whether the state/action abstraction still preserves equivalent physical meaning.

#### D-G8 — model falsification

Inject a regime outside the current model/hypothesis family and measure whether the system reports model inadequacy rather than forcing the evidence into the nearest known explanation.

---

### 16. Adjacent gaps discovered

The literature suggests these areas should remain visible during Stage 1:

```text
multi-timescale state
structured/equivariant memory
non-stationarity and test-time adaptation
task-semantic / functional-role state
self / embodiment model
representation reversibility
world-model falsification / changepoint detection
open-world model inadequacy detection
```

These are not separate Clover commitments. They are candidate dimensions along which future representations should be compared.

---

### 17. Stage-1 questions

```text
Should state granularity be fixed or adaptive?
Which variables require high-frequency update and which only event-level update?
Can task-conditioned abstractions remain reusable for unknown future tasks?
How much raw evidence must be retained to reverse an earlier abstraction decision?
Should uncertainty control representation resolution?
Can structured transformation laws replace brute-force memory?
How should global scene state and local manipulation state interact?
When does hierarchy genuinely improve sufficiency rather than merely add modules?
How should the system detect that its current dynamics/embodiment abstraction is stale?
Should action semantics be represented in robot-specific coordinates or a shared embodiment-invariant space?
When should a model be adapted, replaced, composed with another model, or rejected as inadequate?
How can a robot tell the difference between ordinary prediction error and evidence that its model class is wrong?
```

---

### Current rule

Do not equate minimal state with general understanding.

Do not equate maximal-detail state with better intelligence.

The research target is **appropriate sufficiency at appropriate granularity, with explicit knowledge of what was discarded, whether it can be recovered, and whether the abstraction/model remains valid when the world or embodiment changes**.

---

<a id="topic-research-dossiers-r-c-representation"></a>

## R-C — Representation: Explicit, Distributed, Object-Centric or Hybrid?

Source record updated: 2026-10-14
Status: **BACKGROUND_RESEARCH**

### 1. Fundamental question

> **What internal representation is sufficient for stable visual world understanding and action?**

Candidate families include:

```text
explicit geometric/state variables
distributed latent representation
object-centric slots/entities
dense scene representation
continuous fields
generative latent state
hybrid / identifiable representations
```

No family is privileged by the Research Reset.

### 2. Static self-supervised representation

#### DINOv3

- Paper: https://arxiv.org/abs/2508.10104
- Official research page: https://ai.meta.com/research/publications/dinov3/
- Code: https://github.com/facebookresearch/dinov3

DINOv3 is a strong current baseline for large-scale label-free visual representation and dense frozen features.

**Demonstrates:** a static visual encoder can learn broadly reusable object/part/shape/spatial features without task-specific labels.

**Does not establish:** persistent identity, world revision, temporal state, intervention sensitivity or action-conditioned dynamics.

**Clover question:** what world-understanding capability is genuinely missing once a strong static representation is already available?

### 3. Predictive video representation

#### V-JEPA 2

- Paper: https://arxiv.org/abs/2506.09985
- Official page: https://ai.meta.com/vjepa/
- Research page: https://ai.meta.com/research/publications/v-jepa-2-self-supervised-video-models-enable-understanding-prediction-and-planning/
- Code: https://github.com/facebookresearch/vjepa2

V-JEPA 2 combines large-scale action-free video pretraining with a relatively small amount of action-conditioned robot experience for planning.

**Demonstrates:** distributed predictive latent state can support motion understanding, anticipation and robot planning without a hand-designed explicit world language.

**Open contradiction:** does predictive latent state remain sufficient for long-horizon persistence, belief revision, auditability and unseen physical interventions?

#### V-JEPA 2.1

- Paper: https://arxiv.org/abs/2603.14482

V-JEPA 2.1 strengthens dense, spatially structured and temporally consistent predictive features.

**Clover significance:** this is a serious alternative to a separately engineered `semantic + geometry + temporal` world representation.

### 4. Distributed physical variables are a real counterexample

#### Interpreting Physics in Video World Models

- Official publication: https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/
- Paper: https://arxiv.org/abs/2602.07050

This mechanistic study finds that physical quantities such as speed, acceleration and direction become decodable at different depths, and that direction is represented using a high-dimensional population code rather than a small set of compact state coordinates.

**Research consequence:**

```text
useful physical information
≠ necessarily compact explicit variables
```

Historical Clover mechanisms therefore cannot justify explicit state by interpretability intuition alone.

### 5. Object-centric representation

#### Slot Attention

- Paper: https://arxiv.org/abs/2006.15055

Slot Attention produces exchangeable object-like latent slots and demonstrated compositional generalization in controlled object-centric tasks.

**Potential advantage:** identity, relational structure and composition become easier to express.

**Open problem:** scalable object discovery in cluttered open-world video, dynamic topology, parts/fluids/deformables and ambiguous object boundaries.

#### Visible entities are not persistent world entities

SAM 3.1 provides a strong modern video detection/segmentation/tracking baseline:

- Official: https://ai.meta.com/blog/segment-anything-model-3/
- Code: https://github.com/facebookresearch/sam3

But:

```text
mask / track while visible
≠ enduring entity after evidence disappears
```

This is a critical separator between perception and representation.

### 6. Hybrid and identifiable state

#### Identifiable World Models from Pretrained Diffusion Representations

- Paper: https://arxiv.org/abs/2610.07028

This work asks whether a powerful distributed generative latent can be equipped with identifiable coordinates without retraining the generative backbone.

**Demonstrates in studied settings:** distributed world-model representations and interpretable/identifiable state coordinates need not be mutually exclusive.

**Clover significance:** the important comparison may not be `explicit vs latent`, but whether a hybrid can obtain the strengths of both with less cost than maintaining duplicate authorities.

### 7. Representation objectives preserve different information

Three major learning objectives should not be treated as synonyms:

```text
reconstruction → recover observed/spatial structure
prediction     → retain information useful for future state
 generation    → model a plausible conditional distribution
```

A representation that is excellent for one objective may discard information required by another.

Examples:

- VGGT / VGGT-Ω emphasize learned spatial reconstruction;
- V-JEPA emphasizes predictive latent state;
- Atlas / Cosmos emphasize generative/spatiotemporal simulation;
- VLA/WAM systems emphasize action-useful state.

### 8. Operational research questions

1. Does an explicit state offer measurable advantages in revision, querying or planning?
2. Can a distributed latent preserve object permanence and observability semantics without explicit variables?
3. Are object slots necessary, useful bias, or unnecessary restriction at open-world scale?
4. Can a hybrid representation avoid duplicate or inconsistent world authorities?
5. Which representation is most data-efficient for unseen dynamics?
6. Which representation transfers across camera and embodiment changes?
7. What information is lost by predictive compression?
8. What information is invented by generative completion?

### 9. Baseline families

| Family | Suggested comparator | Primary question |
|---|---|---|
| Static dense latent | DINOv3 | what can images alone encode? |
| Predictive video latent | V-JEPA 2/2.1 | can temporal prediction create sufficient world state? |
| Learned explicit geometry | VGGT / VGGT-Ω | is reconstruction enough for spatial understanding? |
| Object-centric | Slot Attention-style baseline | does factorized entity state improve composition/persistence? |
| Generative latent | Atlas/Cosmos-class evidence | does simulation imply usable state? |
| Hybrid identifiable | ConDA / identifiable world-model direction | can latent power coexist with interpretable coordinates? |
| Historical Clover | candidate explicit state | does it add independent measurable value? |

### 10. Discriminating experiment suite

#### T-C-01 — Matched world-query probing

Use the same visual histories and probe each representation for:

```text
identity
object permanence
spatial relation
temporal order
observability
physical variables
world change
intervention consequence
```

Keep probe capacity controlled to avoid measuring probe power instead of representation quality.

#### T-C-02 — Compression sufficiency

Compare representation sizes at matched query/task correctness.

Measure:

- representation bytes;
- answer coverage;
- correctness;
- long-occlusion degradation;
- new-query performance without retraining.

#### T-C-03 — Revision locality

Introduce a local world change after a long history.

Measure whether the representation can update the affected world state without catastrophic or unnecessary global change.

#### T-C-04 — Strong policy falsifier

```text
strong direct / recurrent policy
vs
same policy + candidate world representation
```

The world representation must improve at least one of:

- unseen-scene transfer;
- recovery;
- task success;
- planning cost;
- sample efficiency;
- unjustified action rate.

### 11. Kill conditions

A candidate representation should be rejected or simplified if:

- its advantages disappear with a stronger baseline;
- its benefit is only additional compute/memory;
- the same capability emerges in a simpler distributed state;
- explicit factors cannot be learned reliably from real visual data;
- hybrid state creates inconsistent duplicate authorities;
- representation quality does not translate to action or recovery.

### 12. Clover landing

Current conclusion:

> **Representation is still an open scientific variable. The strongest evidence argues against prematurely equating interpretability with correctness, while also leaving room for hybrid or identifiable state when it provides measurable revision, query, causal or action advantages.**

---

<a id="topic-research-dossiers-r-d-memory-persistence"></a>

## R-D — Persistence, Memory and Belief Revision

Source record updated: 2026-10-14
Status: **BACKGROUND_RESEARCH**

### 1. Fundamental question

> **How should a vision-only machine preserve and revise knowledge about a world that is only intermittently visible?**

Memory is not one thing. Candidate forms include:

```text
raw visual evidence
compressed perceptual history
persistent object/world state
episodic events
semantic memory
policy hidden state
external retrieval memory
hybrids
```

The project must distinguish remembering evidence from maintaining a world hypothesis.

### 2. Seeing is not remembering

#### PersistBench / Can 4D Foundation Models Remember?

- Paper: https://arxiv.org/abs/2609.20819
- Project / dataset / code: https://guangzhaohe.com/persistbench

PersistBench uses 360° video as an omniscient reference while evaluating ordinary limited-field-of-view models on:

- object permanence;
- motion continuity;
- appearance preservation.

**Demonstrates:** current 4D reconstruction/video models can be strong while an object is observed yet degrade substantially once it leaves the field of view.

**Clover implication:**

```text
reconstruction consistency while visible
≠ persistent world memory
```

Any claim of a world model should therefore report out-of-FOV behavior, not only clip reconstruction or tracking.

### 3. Streaming episodic memory is different from offline long-context QA

#### S-EMBER

- Paper: https://arxiv.org/abs/2607.02689
- Official publication index: https://ai.meta.com/results/?content_types%5B0%5D=publication&research_areas%5B0%5D=computer-vision

S-EMBER contains long egocentric streams and requires grounded retrieval with temporal localization of visual evidence.

**Demonstrates:** answering a question and locating the supporting past event are separable capabilities; current models show a substantial grounded-recall gap.

**Clover implication:** a long context window is not equivalent to reliable episodic world memory.

### 4. The memory harness itself can change capability

#### VISTA

- Paper: https://arxiv.org/abs/2610.02200
- Project: https://vista-research.github.io/
- Code: https://github.com/joshhhhhan/VISTA

VISTA maintains a lossless archive of visual observations and lets the model actively retrieve and reorganize past visual evidence.

**Demonstrates:** with the same general-purpose reasoning backend, changing the visual-memory/inspection harness can strongly change long-horizon interactive performance.

**Important limitation:** its strongest results are on visual games and interactive environments, not proof that lossless replay is the optimal memory architecture for real robots.

**Clover implication:** memory architecture is an independent research variable; capability is not determined only by model weights.

### 5. Memory must support revision, not only recall

A useful world model must handle:

```text
old evidence
→ old belief
→ world changes
→ partial new evidence
→ contradiction detected
→ affected state revised
→ downstream queries/plans updated
```

A system that remembers everything but cannot revise stale beliefs is not maintaining a usable world model.

### 6. Evidence memory vs world state

A critical distinction:

```text
Evidence memory = what visual observations can be re-examined?
World state      = what does the system currently believe / represent about the world?
```

They may be implemented together or separately, but experiments must not conflate them.

Historical Clover's Evidence Replay idea remains a hypothesis because VISTA and similar results establish the value of retrievable evidence, not the necessity of a specific Clover replay compiler.

### 7. Forgetting is also a research problem

Unlimited retention is not a scalable answer.

A realistic system must decide what to:

- keep at full fidelity;
- compress;
- summarize;
- retain as persistent state;
- discard;
- reload when a query or contradiction demands it.

Therefore memory should be evaluated by a Pareto frontier over:

```text
capability
retention bytes
retrieval latency
update latency
compute
```

not by recall score alone.

### 8. Operational research questions

1. Is object permanence best represented in world state, recurrent latent memory, or external evidence memory?
2. When should an object become `unknown` rather than remain confidently predicted?
3. How long should different state types persist?
4. Can memory support a query that was not known when the evidence was first observed?
5. Does retaining raw evidence materially improve belief revision over compressed latent history?
6. What is the right forgetting policy under bounded storage?
7. How should memory distinguish the world changing from the system merely observing a different viewpoint?
8. Can stale downstream decisions be invalidated when an upstream world belief changes?

### 9. Baseline families

| Family | Baseline / example | Isolates |
|---|---|---|
| Fixed context | standard video/VLM context | no explicit long-term memory architecture |
| Recurrent/predictive latent | V-JEPA-like / recurrent policy | compressed temporal state |
| Visible tracker memory | SAM 3.1 | persistence while detectable/trackable |
| Reconstruction memory | 4D foundation models | geometric temporal consistency |
| External visual archive | VISTA-style harness | re-access to original visual evidence |
| Episodic retrieval | S-EMBER-style systems | retrieval/localization from streaming history |
| Explicit world state | historical Clover candidate / classical map | persistent queryable state |

### 10. Discriminating experiments

#### T-D-01 — Long out-of-FOV persistence

Occlusion/out-of-view durations:

```text
4 / 8 / 16 / 32 / 64 / 128 frames
```

Measure:

- identity continuity;
- motion continuity;
- appearance consistency;
- uncertainty during absence;
- recovery at reappearance;
- memory bytes.

#### T-D-02 — New-query replay

Observe a long sequence without knowing the later question.

After the sequence, ask a query that requires an old visual detail not represented in the current task state.

Compare:

```text
fixed compressed context
recurrent state
external replay/retrieval
hybrid state + replay
```

#### T-D-03 — World change / stale belief

Move an object while it is unobserved, then reveal only partial evidence.

Measure:

- stale-state detection;
- time to revision;
- locality of revision;
- dependent planning errors;
- recovery.

#### T-D-04 — Retention Pareto

At matched task correctness, compare:

```text
storage bytes
retrieval p50/p99
update p50/p99
energy where measurable
```

#### T-D-05 — Evidence versus state ablation

Four conditions:

```text
world state only
raw/retrievable evidence only
world state + evidence
long-context latent only
```

This isolates whether each memory type contributes independent value.

### 11. Kill conditions

A dedicated evidence-replay mechanism should be demoted if it does not independently improve:

- new-query retrieval;
- belief revision;
- long-occlusion recovery;
- grounded verification;

at a defensible storage/latency cost.

A persistent explicit world state should also be rejected if a recurrent/latent memory reaches equal capability, revision quality and task success more simply.

### 12. Clover landing

Current conclusion:

> **Persistent world understanding requires more than a long context or visible tracking, but the correct architecture — recurrent latent, persistent state, retrievable evidence, or hybrid — remains open and must be decided by out-of-FOV, revision and new-query experiments.**

---

<a id="topic-docs-research-map-learned-visual-representations"></a>

## Learned Visual Representations

### What problem does this area solve?

Classical vision depends on variables and features chosen by humans. Self-supervised representation learning asks whether useful visual structure can emerge from large unlabeled image collections instead.

For Clover the central question is not image classification. It is:

> **What world-relevant structure is already present in generic learned visual features before temporal or action learning is added?**

### Representative work: DINOv2

DINOv2 learns general-purpose visual features without manual labels. Meta's model card describes ViT backbones whose class and patch tokens can support downstream classification, depth estimation, segmentation and retrieval with lightweight heads. The original work trained on LVD-142M images.

Primary sources:

- https://github.com/facebookresearch/dinov2
- https://arxiv.org/abs/2304.07193

#### Representation

A distributed transformer feature space: global class token plus spatial patch tokens, optionally with register tokens.

#### Learning signal

The released model card lists self-distillation, masked-image modeling and feature regularization components.

#### What it demonstrates

A large amount of transferable visual structure can be learned without semantic labels, and useful geometry-related signals such as depth can be extracted with small downstream heads.

#### What it does not demonstrate

DINOv2 by itself does not establish:

- persistent identity through long occlusion;
- a stable world state across time;
- physical dynamics;
- causal intervention reasoning;
- action-conditioned world change.

It is therefore a strong **perceptual representation baseline**, not a complete answer to Clover's question.

### Clover questions

1. Which Clover world queries are linearly or cheaply readable from a strong static visual representation?
2. Which queries fundamentally require temporal learning?
3. Does an explicit world state add information, or only make existing latent information easier to query?
4. Can a learned visual backbone preserve fine geometric detail needed for physical reasoning without task-specific supervision?
5. How much of apparent world knowledge is inherited from dataset regularities rather than physical understanding?

### Research value

This area prevents Clover from reinventing low-level feature learning unnecessarily. If modern self-supervised features already provide robust object/geometry cues, Clover's novel contribution should begin where those representations become insufficient: persistence, observability, dynamics, causal revision and action-useful world state.

---

<a id="topic-docs-research-map-object-centric-representation"></a>

## Object-Centric Representation

### Core question

> **Should a machine represent the world as persistent entities, or can object-like structure remain implicit inside a distributed representation?**

Objects are tempting primitives because robot tasks are often described in terms of things that persist, move, interact and can be acted upon. But treating objects as pre-given may bake human ontology into the system too early.

### Slot Attention

Slot Attention introduced a mechanism that maps perceptual features into a set of exchangeable slots through iterative competitive attention. The original work showed object-centric representations that generalize to unseen compositions in object-discovery/property-prediction settings.

Primary source:

- https://arxiv.org/abs/2006.15055

### Video segmentation and tracking as a lower-level baseline

SAM 2 extends promptable segmentation to image and video and adds streaming memory for maintaining target masks through a sequence. Meta describes memory that carries target-object context across frames, including temporary disappearance.

Primary source:

- https://ai.meta.com/research/sam2/
- https://github.com/facebookresearch/sam2

SAM 2 is not a world model. It is useful because it isolates a concrete subproblem:

> how well can a strong modern vision system maintain a visually specified entity through time?

### Competing hypotheses

#### H1 — Object as primitive

The world state directly contains entity records with identity and state.

**Advantage:** simple queries, planning and relation construction.

**Risk:** premature segmentation and brittle ontology.

#### H2 — Object as emergent structure

Objects emerge from lower-level spatial/temporal structure, field coherence or predictive equivalence.

**Advantage:** can adapt to unfamiliar entities and scales.

**Risk:** may be difficult to stabilize and query.

#### H3 — Distributed latent only

No explicit object record is required; object information is decoded when needed.

**Advantage:** representation is not forced through an information bottleneck.

**Risk:** persistence, revision, provenance and planning may be hard to make reliable.

### What Clover needs from an entity representation

A useful entity mechanism should support:

- identity across viewpoint change;
- occlusion and reappearance;
- split/merge/deformation when appropriate;
- object-relative dynamics;
- relations and contact;
- uncertainty over identity;
- local belief revision;
- efficient queries for decision making.

### Critical question

Clover should not ask only:

> Can we segment objects?

It should ask:

> **Does explicit entity structure produce capabilities that a strong dense/video representation cannot provide as reliably or efficiently?**

---

<a id="topic-docs-research-map-video-world-models"></a>

## Video Representation and World Models

### Core question

> **Can a machine learn useful physical world structure largely by observing video, and what representation emerges when it does?**

This is one of the closest modern research families to Clover's SSOT.

### V-JEPA 2

Meta describes V-JEPA 2 as a self-supervised video model for understanding, prediction and planning. It is pretrained action-free on more than one million hours of internet video. Meta reports strong motion understanding and action anticipation results, then post-trains an action-conditioned model (V-JEPA 2-AC) with a much smaller amount of robot trajectory data for robot planning.

Primary sources:

- https://ai.meta.com/research/publications/v-jepa-2-self-supervised-video-models-enable-understanding-prediction-and-planning/
- https://github.com/facebookresearch/vjepa2
- https://arxiv.org/abs/2506.09985

#### Representation

A learned latent video representation. JEPA-style training predicts representations rather than reconstructing raw pixels.

#### Scientific importance for Clover

V-JEPA 2 directly challenges the assumption that world understanding needs a hand-designed explicit world language. It asks whether prediction in latent space can induce enough temporal and physical structure for planning.

#### Observation versus interaction

The separation between very large action-free video pretraining and comparatively limited robot interaction data creates a useful research question:

> What physical regularities can be learned from passive observation, and what only becomes identifiable through action?

Clover should treat this as a first-class theoretical question rather than assuming either passive video or interaction is sufficient.

### V-JEPA 2.1

The official repository states that V-JEPA 2.1 focuses on high-quality, temporally consistent dense features. Its training recipe adds dense predictive loss, deep self-supervision, image/video tokenization and scaling.

Primary source:

- https://github.com/facebookresearch/vjepa2
- https://arxiv.org/abs/2603.14482

For Clover, the key issue is whether dense temporal consistency can provide a stronger substrate for identity, motion, boundary persistence and world-state formation than global video representations alone.

### Mechanistic interpretation: physics in video world models

Meta's 2026 work **Interpreting Physics in Video World Models** studies how physical variables are represented inside video encoders. The reported finding that some variables become increasingly linearly accessible while other structure is distributed across high-dimensional populations is an important counterexample to a naive explicit-variable assumption.

Source:

- https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/

#### Clover consequence

The research question is no longer:

> Can we design a compact set of explicit variables?

It is:

> **When does explicit state improve generalization, causal revision, queryability and control over a distributed representation, and when does it discard useful information?**

### World-model taxonomy relevant to Clover

Video/world models can serve different roles:

- **encoder** — produce representations;
- **predictor** — predict future latent state;
- **renderer/generator** — generate observations;
- **simulator** — roll a world forward under conditions/actions;
- **planner substrate** — score or search action consequences.

A system should not be called a complete world model merely because it performs one of these functions.

### What this family has demonstrated

- large-scale video SSL can learn strong temporal/motion representations;
- latent predictive models can support downstream robot planning after action conditioning;
- temporal consistency can be learned densely rather than only at a global clip level;
- physical variables can be present in representations without explicit hand-designed state variables.

### What remains unresolved for Clover

- persistent object identity beyond the video context window;
- explicit distinction between unobserved, unknown and absent;
- belief revision after contradictory evidence;
- long-term world memory;
- causal identification rather than predictive correlation;
- whether latent prediction helps real robot recovery under unexpected world changes;
- whether language alignment imports non-visual knowledge into a supposedly visual understanding evaluation.

---

<a id="topic-research-emerging-representation_diagnostics_2026-10-15"></a>

## Stage-1 Emerging Audit — Representation Diagnostics and Causal Use

Source record updated: **2026-10-15**
Source intake checked through: **2026-10-15**

> Mother question: **How can a machine understand the real world through vision alone?**

This is supporting methodology for Stage 1 / Stage 2. It does not define a Clover representation.

### Core problem

A representation may contain information that a downstream probe can decode even when the deployed policy does not actually use that information.

Keep three claims separate:

```text
information is decodable from latent state
≠
information is causally used by the model
≠
changing that information produces the expected closed-loop behavior
```

This distinction matters directly for claims such as:

```text
"the model represents mass"
"the model understands direction"
"the world model encodes object permanence"
"the policy uses causal state"
```

A linear probe alone cannot establish these stronger claims.

---

### 1. Current embodied mechanistic-interpretability evidence

### Do Vision-Language-Action Models Understand Instructions?

Paper: https://arxiv.org/abs/2610.10178
Evidence: `PRIMARY_PAPER`

The paper studies `π0.5` and `GR00T N1.7` using activation patching and attribution patching under controlled instruction corruptions.

Important reported observations:

- directional language can produce large causal effects on action generation;
- the loci of causal sensitivity differ across the two model families;
- for GR00T N1.7, large causal effects can occur while representational geometry changes relatively little;
- attribution patching tracks activation patching differently across the two models.

Stage-1 lesson:

```text
representation similarity
≠
causal functional role
```

and interpretability methods themselves require validation per architecture.

---

### Mechanistic interpretability for steering VLAs

Paper: https://arxiv.org/abs/2509.00328
Evidence: `PRIMARY_PAPER`

This work identifies internal semantic directions linked to action behavior and demonstrates activation steering on open-source VLA models in simulation and on a physical robot.

Research role:

```text
observe latent feature
→ intervene on latent feature
→ measure action change
```

is stronger evidence than probe accuracy alone.

But successful steering still does not prove that the steered concept is a complete or correctly grounded world variable.

---

### 2. Required representation-evidence ladder

For future Clover/Stage-2 claims, record the strongest evidence available.

```text
RD0 correlation / visualization
RD1 linear probe recoverability
RD2 nonlinear probe / controlled prediction
RD3 causal activation patch / ablation / mediation
RD4 targeted steering changes action in expected direction
RD5 closed-loop intervention changes physical outcome as predicted
RD6 OOD / counterfactual replication of the causal effect
```

Do not promote an `RD1` result into an `RD5` claim.

Example:

```text
mass can be linearly predicted from Z_t
```

only establishes decodability under the probe/data assumptions. It does not establish that the robot policy uses mass, that mass is identifiable from evidence, or that manipulating the mass coordinate changes action appropriately.

---

### 3. Probe controls that should be mandatory

When probing a latent variable, control for:

```text
probe capacity
sample size
class/category leakage
language-label leakage
viewpoint / camera identity
object identity shortcut
time-index shortcut
action-label shortcut
train/test environment overlap
frozen vs post-trained representation
```

Prefer counterfactual/minimal-pair datasets where the target physical variable changes while appearance/semantics are controlled as much as possible.

---

### 4. Representation quality should be multidimensional

For a candidate world state `Z_t`, evaluate separately:

```text
Decodable?          can a probe recover the variable?
Identifiable?       was enough evidence available to infer it?
Causally used?      does the model actually rely on it?
Intervenable?       can controlled latent change alter behavior predictably?
Persistent?         does it survive occlusion/time?
Revisable?          can contradictory evidence update it?
Action-sufficient?  does it support control/planning?
Open-world robust?  does the effect survive new objects/scenes/regimes?
```

This prevents `representation quality` from collapsing into one probe score.

---

### 5. Relation to JEPA / WAM / Foundation-model audits

This methodology is especially important for recent latent world models such as:

```text
V-JEPA / RoboJEPA
SpecWM
Identifiable World Models
ReWAM
LeWAM variants
LAC-WM
DELE-style future latents
```

Questions to ask:

```text
Does scaling reduce prediction loss while leaving critical state variables absent?
Does a frozen visual encoder create a hard information ceiling?
Are action-relevant variables merely decodable or causally used?
Does post-training re-route which layers/features actually control action?
Does quantization/token pruning preserve probe accuracy but alter causal use?
```

---

### 6. Current rule

Stage 2 must not equate:

```text
probe success
with
understanding.
```

For high-value world-state claims, aim to progress from:

```text
recoverability
→ causal attribution
→ intervention
→ closed-loop behavioral evidence
→ OOD/counterfactual validation.
```

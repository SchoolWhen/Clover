<a id="top"></a>

# 调研方向：研究问题与可证伪边界

Maintained: **2026-10-25** · Document stage: **1 — Research** ([status](../STATUS.md)).

Unresolved questions and the evidence that could distinguish competing answers. These are questions, not adopted mechanisms.

This is the canonical topic document. Update it in place; source-level dates and reading-depth labels below qualify the evidence, not the maintenance date.

<!-- BEGIN cross-domain-research-bridges -->
<a id="cross-domain-research-bridges"></a>

## 交叉研究：可以检验的桥接问题

这些是文献提出的对照和条件，不是本项目采纳的模块列表。

| 交叉方向 | 原问题中的作用 | 已核实的参照 | 仍需解决的接口 |
|---|---|---|---|
| 多视图几何 × 循环状态 × SLAM | 多帧如何形成一致且可修正的状态 | CUT3R、MonST3R、HiP3R、Stream4D | 几何漂移、动态身份、隐藏态与物性不是同一误差 |
| 物理结构学习 × 系统辨识 | 什么先验允许从轨迹找到紧凑动力学 | HNN、LNN、Koopman、SINDy、GNS、FNO | 真状态/坐标/方程族是否被额外提供；相机逆问题在哪里解决 |
| 信息论 × 状态充分性 × 记忆 | 压缩究竟保留谁需要的信息 | Information Bottleneck、CADRE、WholeBodyMem | 指定任务充分与未知未来任务充分；可恢复/不可重看的证据 |
| 无监督技能 × 可达性几何 | 不靠单任务奖励学习可复用行为坐标 | METRA、HILP | 时间距离是否丢失身份、物性、不可逆事件或反事实区分 |
| 领域泛化 × 因果结构 | 区分外观捷径和物理机制外推 | IRM、DomainBed、WILDS、物性偏移世界模型 | 环境划分/模型选择是否泄漏；已知质量与视觉识别质量分开 |
| 成像物理 × 主动感知 | 真实获取哪些测量值得其时间/风险 | 采证式 CLOSER、照明检查、任务相关 NBV | depth/地图/机体状态来源；亮度、熵和任务风险的区别 |
| 生成视频 × 因果验证 × 评测 | 区分看似合理、执行正确、持久保持和行动有用 | MIST、PhysTrace、Dual Exam、Sensorimotor Alignment | 独立考官、生成证据地位和闭环校验 |
| 部分可观测控制 × 可变形/接触 | 近静态图像下哪些隐藏量会改变动作 | FlowVLA、CW-WAM、软衣物世界模型、DefFlow | 点云、力、动作和完整模拟状态带来的额外可识别性 |
| 去文字分割 × 去标注学习 | “纯视觉”到底去掉了哪一种外部信号 | WOW-Seg（无文字提示，仍用 VLLM 知识）、MoSA（无人工标注，仍用合成视频/光流） | 文字提示、人工标注、语言预训练、合成数据必须分别记账；开放世界概念发现仍未闭合 |
| 几何/扩散先验 × 通用追踪 | 2D 跟踪能否借 3D 几何或生成先验突破遮挡/干扰 | GOT-Edit（VGGT + 在线编辑）、Point Prompting（视频扩散）、SAM-H（分割轮廓单应） | 在线编辑成本、扩散/光流时延、平面假设；长期身份与失败恢复仍需独立测 |
| 事件视觉 × 任意时刻感知 | 速度与证据能否通过换传感器而非压缩计算同时提升 | LiFR-Seg（RGB+事件任意时刻分割）、SEAL（开放词汇事件实例分割） | 事件标定/噪声、语义标签、真实部署成本；不是纯 RGB，也不是通用视觉 |
| 开放世界异常 × 语言定义 | 异常定义随场景改变时，模型如何更新“什么不正常” | LaGoVAD（自然语言定义 + 弱监督） | 弱标签、语言先验、异常/因果机制区分；动态定义下的校准与拒答 |
| 3D 空间关系/可供性 × 视觉 grounding | 从“物体在哪”到“相对谁、能怎么用” | RelationVGGT、UniFunc3D、UniRAP | 关系词表/自动标注、MLLM 先验、接触/可行性闭环 |
| 概念分割 × 对抗/时延安全 | 开放接口是否引入新的攻击面 | AdvPCS、TrackFlood、When Trackers Fail | 威胁模型、防御代价、干净精度与安全的同时评估 |

当前材料仍不足以从任何一行推出完整的 Clover 解法。后续应按共同失败与可证伪预测比较，避免把这些方向直接堆成网络结构。
<!-- END cross-domain-research-bridges -->

<!-- BEGIN frontier-synthesis-2026-10 -->
<a id="frontier-synthesis-2026-10"></a>

## 2026-10 研究格局：六个可证伪的纯视觉问题

检索/核验：**2026-10-25（Asia/Shanghai）**。下表把本轮新增证据接到原问题上。每一行都必须能给出**竞争解释**与**能区分它们的测量**；没有区分测量的“方向”不进入 Clover 的创新候选。

| 新桥接 | 原问题中的作用 | 已核实参照 | 仍需解决的接口 |
|---|---|---|---|
| 纯视觉自监督 × 语言监督 | 识别/密集特征的能力是否必须依赖语言 | WebSSL 同数据受控比较、DINOv3、Perception Encoder、Meta CLIP 2 | 数据策展/评估语言混杂；开放词汇、文字、关系任务分层；规模律是否可复现 |
| 失败恢复 × 身份持续性 | 追踪的瓶颈是传播更强，还是知道何时不可信 | SAMURAI、MOTIP2、SAM3RL、When Trackers Fail、TAPNext++ | 遮挡期状态、重现后身份、错误纠正的二次伤害、最坏干预延迟 |
| 点轨迹 × 对象/刚体状态 | 像素轨迹、对象身份与 `SE(3)` 运动是否是同一层理解 | TAPFormer、CoWTracker、3D SSM、Track4World、MoSE3、Track-On-R、RoPT、GRC-Pose、ComPose、ASM-6D | 绝对米制、世界坐标、刚性分组、非刚体、语义身份、对象先验、遮挡恢复、端侧成本 |
| 实时时钟 × 认知策略 | 速度是否改变模型“看什么/想多久” | Realtime-Bench、TacitVLA、Bifocal、StreamAhead、TrackFlood | Wall Clock 与理想时钟分离；证据年龄；安全截止线；token 压缩对细粒度能力的损伤 |
| 主动观察 × 任务价值 | 新视角的收益是否值得其成本/风险 | Rendering-Free Lookahead、EgoReveal、FoveaVLA、Adaptive Observation Control、SpatialScout | 信息增益代理、不可逆动作、真实机器人转移、探索预算 |
| 世界模型记忆 × 物理显式性 | 持久状态应存生成 latent、平面、节点还是像素 | PPMem、Grid or Nodes、Gen4P、Dreamer 4、CADRE | 生成写回 vs 观测证据；长时漂移；动态/非平面场景；独立物理校验 |
| 评测基准 × 证据泄漏 | 分数是否真的支持主张 | TAPVid-MV、VC-PQ、SA-Co、OmniDocBench、SpatialScout | 辅助模态 `L4`、视图/轨迹计分单位、版本漂移、预训练重叠不可核对 |

### Q1 — 匹配数据后，纯视觉自监督能否追平语言监督？

- **竞争解释：** (a) 语言提供了视觉经验无法从图像中恢复的语义/关系；(b) 差距主要来自数据规模与筛选，而非监督目标。
- **现有证据：** WebSSL 在同一 MetaCLIP 数据上发现视觉 SSL 随规模增长可追平 CLIP；但 VQA 仍含问题文本，数据策展可能含语言元数据；DINOv3/PE 分别证明纯视觉稠密特征与图文对齐编码器各自很强。ICLR/ECCV 2026 的 WOW-Seg（推理无文字提示但仍用 VLLM 世界知识）与 MoSA（无人工标注但保留合成视频/光流）进一步说明：去文字、去标注和去先验是三件不同的事。
- **可证伪预测：** 在匹配数据、模型、算力与评测后，纯视觉 SSL 在**类别定义**的识别/分割/深度任务上追平图文监督；在**文字定义的新概念、开放词汇关系、需要外部知识的任务**上，除非视觉经验覆盖，否则仍显著落后。
- **判别实验：** 同一数据训两种目标；任务按“类别/文字/关系/知识”分层；报告数据策展审计与语言探针；加入新概念组合与无关文字替换。

### Q2 — 追踪的瓶颈是传播更强，还是失败感知？

- **竞争解释：** (a) 更强骨干/更大记忆提升一切；(b) 主要误差来自身份漂移与错误记忆写入，显式验证/恢复更关键。
- **现有证据：** SAMURAI 不改权重，仅改运动先验与记忆选择即获 LaSOT_ext +7.1 AUC；SAM3RL 用 RL 选记忆帧在 10/12 基准 SOTA；When Trackers Fail 显式验证/纠正在 LVOS-v2/SecVOS +1.2/+2.7 J&F，但作者承认非实时且纠正可能伤害正确轨迹；MOTIP2 说明空间先验能消除“横跨画面”的 ID 错误，但同位置进出仍是失败。2026 正式会议批次把其他先验带入同一问题：GOT-Edit 用 VGGT 几何做在线模型编辑，Point Prompting 用视频扩散做零样本点追踪，SAM-H 用分割轮廓做长期平面跟踪（2.4 FPS，非实时）。
- **可证伪预测：** 在**同等骨干与记忆字节**下，失败感知/验证恢复在长时遮挡与重现场景的收益，大于单纯扩大记忆窗口；但在干净短序列上可能因额外验证而变慢/略降。
- **判别实验：** 固定传播器与内存预算，比较“更大窗口 / 运动先验 / RL 记忆 / 验证恢复”；分别报告当前帧、关联、遮挡期、重现后身份与最坏延迟。

### Q3 — 原生 ultrafast 会不会先牺牲细粒度证据？

- **竞争解释：** (a) 平均 VQA/检测分数保持，说明压缩安全；(b) 平均分掩盖 OCR、小物体、边界与重现身份的先坏。
- **现有证据：** Bifocal 评测 10 种 token 剪枝方法，发现平均 VQA 保持但 OCR/grounding 严重退化；StreamAhead 以自适应预计算把 TTFT 降到 0.5 s 内，但只测视频 QA；Realtime-Bench 在 Wall Clock 下最佳成功率仅 44%；TrackFlood 证明检测器时延稳定时跟踪器仍可被拖垮。LiFR-Seg 给出另一条路线：用事件流补 RGB 帧间证据，DSEC 上 73.82% mIoU 接近理想 HFR 上界 73.91%，说明“更快”可以通过增加观测模态而不是只压缩计算获得。人体侧，Fast SAM 3D Body 用系统级重构取得最高 10.9× 加速，并在单 RGB 遥操作中做到 65 ms 端到端，但 3DPW MPJPE 略升，说明速度收益仍需按精度/坐标系分项。
- **可证伪预测：** 在相同完整输出与硬件下，token/分辨率/记忆压缩会**先**损伤小字、小物体、细边界、遮挡重现与罕见事件，再损伤平均 QA；因此速度收益必须用能力分层验收。
- **判别实验：** 固定模型与硬件，逐级压缩；同时测 OCR/小物体/追踪重检测/文档结构/长尾分类；记录 P50/P95/P99、证据年龄与最坏截止违约。

### Q4 — 主动观察的收益何时超过其成本？

- **竞争解释：** (a) 更多视角/更高分辨率总是有益；(b) 只有在高不确定性、可逆、任务相关时，主动采证才划算。
- **现有证据：** RFL 用特权 3DGS 未来视图蒸馏“可回答性”，在 377 个未见 episode 上比直接动作基线 +43% judge score；EgoReveal 在部分遮挡下先 reposition 相机再操作；FoveaVLA 用注视动作替代腕部相机，真实任务 70.8/77.1% vs 52.1%；SpatialScout 显示最强 VLM agent 的主动建图 overlap 仅 41.71%。
- **可证伪预测：** 当不确定性低或动作不可逆/高成本时，固定策略不劣于主动策略；当目标被遮挡且存在安全可逆视角时，信息增益策略显著更好；收益随“视角覆盖”而非“观测数量”增长。
- **判别实验：** 同一任务上比较固定扫描、熵/信息增益、任务价值（RFL 式）与随机视角；加入动作成本、风险与不可逆约束；报告成功率、信息增益/焦耳、最坏延迟。

### Q5 — 世界模型记住的是观测，还是自己的预测？

- **竞争解释：** (a) 生成式 latent 记忆足以支持长时一致；(b) 自回归写回会累积自生成证据，显式几何/节点记忆更抗漂移。
- **现有证据：** Grid or Nodes 发现 FloWM 在视野内高 8 分但作者归因于写回自身预测；出视野节点记忆 14 KB 达网格 5.6 MB 的范围；对角运动网格仅 11% vs 跟踪器 93%。PPMem 用约 100K 平面/5 MB 维持 288 帧，但作者承认只在平面结构场景好、冻结骨干未端到端共适应。Gen4P 把视频生成器当 4D 感知器，可能补出视频中不存在的结构。长视频侧，R4DSG/Ledger 表明显式物体/场景图记忆能回答 when/where（Ledger VQ3D 中位 0.99 m），但 EgoProbe 显示 ultra-long 与相似事件干扰下最佳模型两轮仅 43.69%；VideoLoop 证明 append-only 工作记忆会“语义 thrashing”，重写有界记忆才恢复证据；SVCBench 进一步把计数作为世界状态维护的最小探针，人类总体 96.1 vs 最佳模型 37.0、周期事件 93.2 vs 11.1。
- **可证伪预测：** 在长时遮挡/出视野后，显式节点/几何记忆比纯生成 latent 更少把自身预测当证据；但在非平面、动态、有机场景，平面/节点先验会失效，生成式细节可能更好。
- **判别实验：** 同一视频序列，比较 grid latent / plane / node / pixel 记忆；注入“模型自己生成的未来帧”作为干扰；测真实重现位置、身份、物理接触与错误累积；用独立传感器做外在校验。


### Q6 — 同一像素、同一物体、同一刚体：追踪到哪一层才算“理解”？

- **竞争解释：** (a) 像素轨迹足够，只要长期准确；(b) 必须有对象身份与持久性；(c) 必须有刚体/关节的 `SE(3)` 运动结构，才能支持操作与接触预测。
- **现有证据：** TAPFormer 用事件把稀疏图像帧（训练 12 Hz 采样）之间的轨迹推到事件时刻，但需要事件相机；CoWTracker 以 warp 替代 cost volume，把平均 AJ 推到 71.3；3D SSM 在绝对米制 AJ 上到 0.256，却在 median-scaled leaderboard 上落后 DELTA+ 0.141；Track4World 一次前向跟踪所有像素的世界坐标轨迹；MoSE3 用刚性嵌入与 Horn 拟合把轨迹提升为每像素 `SE(3)`，HO3D RRE 18.28°、iTACO 12.30°。这些结果说明“轨迹层”已经很强，但**遮挡期位置仍是推断**，**轨迹不提供类别/身份**，**刚体分组不覆盖布料/液体/手部**，**绝对米制依赖深度或 IMU**。物体级 6-DoF 把同一问题推到“对象假设”：RoPT 在 16× 帧降采样下 ADD 90.85（FoundationPose 38.87），但需精确 CAD + RGB-D、18.6 FPS；GRC-Pose 在 HOT3D 运动保持 +58%，但端到端仅 0.79 FPS；ComPose 仅 RGB 在 DexYCB RRE 1.5°，仍依赖 SAM3/SAM3D-Object 与手部模型；ASM-6D 高运动 mug ADD 1.56 cm，但类别先验 + RGB-D、6–38 Hz。场景图层进一步证明：LEXI-SG 纯单目 RGB 能建开放词汇 3D 场景图，但含物体分割仅 1.56 FPS；OccAny 零样本序列占据 IoU 25.91；LOST-3DSG 用 3.2 KB 语义状态跟踪移动物体，却依赖 VLM 描述；DSG 的粗关系匹配仅 43%。
- **可证伪预测：** 在相同 2D 轨迹误差下，带对象身份/刚性分组的表示在遮挡重现、接触预测与可操作区域上更好；但在干净短时 2D 基准上不会优于纯轨迹。若绝对米制与 `SE(3)` 不能在真实机器人上改善抓取/避障/规划，则它们只是更贵的轨迹，而不是“理解”。
- **判别实验：** 固定 2D 轨迹前端，比较 point-only / object-mask / rigid-`SE(3)` 三种状态；测遮挡重现身份、3D 位置、接触/抓取、规划成功率与端侧成本；把 GT 内参与估计内参、scale-invariant 与绝对米制分列。

**当前结论：** 2026-10 的证据把问题从“纯视觉能否理解世界”推进到更可操作的六个分层问题：监督来源、失败感知、速度-证据、主动采证、记忆真实性、轨迹层级。它们都还没有被 Clover 实验回答；任何架构选择都必须先给出能区分竞争解释的测量，而不是把最强模块拼在一起。
<a id="competing-pure-vision-routes"></a>

## 竞争性解释：六条“纯视觉理解”路线

原问题不是“有没有一个模型分数高”，而是**哪一种机制足以解释视觉理解**。本轮证据可以归为六条互相竞争、部分重叠的路线。每条都给出最强支持、反证与能区分它们的实验；没有一条已通过全部二十类能力。

| 路线 | 核心主张 | 本轮最强证据 | 主要反证/边界 | 能区分它的实验 |
|---|---|---|---|---|
| R1 规模化的视觉自监督 | 理解主要随视觉数据/模型规模涌现，专用结构不是必需 | WebSSL 在同数据上追平 CLIP；DINOv3 强稠密特征；MoSA 零人工标注接近 SAM；StreamMAE 连续视频可追平 i.i.d. MAE | 静态特征缺身份/记忆/物理；MoSA 仍用合成视频/光流；WebSSL 评估含语言；规模律未覆盖开放世界 | 匹配数据/算力后，测永久性、接触、再识别、干预预测，而不只测分类/分割 |
| R2 显式几何与 3D/4D 状态 | 理解要求显式空间状态；像素/语义特征不够 | DA3 位姿/几何超 VGGT；Pano3D 统一重建+3D 全景；Uni4R 连续时间 4D；ARROW 任意视图 3D 跟踪；UniSim-SLAM 未标定 TUM 0.032 m；Failure or Drift 显示学习跟踪器以静默漂移替代显式失败；Event3R 事件-only 3D 重建 NC 0.889 | 静态/短时为主；单目绝对尺度需 IMU/深度统计锚定；事件数据多为模拟；几何自洽≠物理正确；透明/反光/动态失败；语义/身份另需监督 | 几何状态是否提升接触/遮挡/度量预测；改变材质/光照/动态后是否仍成立 |
| R3 预测式世界模型 | 理解=可预测/可压缩的未来状态，足以规划 | V-JEPA 2 系列在腐蚀/遮挡/时间箭头上的鲁棒性；OccJEPA 用 V-JEPA 2.1 predictor 补全遮挡（SAIL-VOS 78.60，33.5× 快于扩散基线）；StarWM 只重建动力学相关区域；Dreamer 4 离线想象训练；Gen4P 用生成器做 4D | 像素/潜空间预测可忽略因果变量；补全是特征预测≠物理/材质；生成证据≠观测证据；游戏/模拟域；动作标签 | 反事实/干预预测；未见动力学；部分可观测下的记忆；无奖励策略迁移 |
| R4 对象、关系与可供性 | 理解的最小单位是实体、关系和可操作结构 | SAM 3 概念分割+视频身份；UGO 通用多目标追踪；RelationVGGT 3D 空间关系；UniRAP/UniFunc3D 可供性；FineHOI 零样本交互 35.58 unseen；GraspHOI 单图手指级接触 CPP 72.8%；SAGE 注视-动作联合预期 58.4% | 标签/本体决定上限；分割≠物理对象；可供性由人定义；HOI 评测口径可反转排序；缺动力学/接触验证 | 新关系/新工具组合迁移；接触可行性与失败恢复；跨类别/跨机体 |
| R5 主动/工具性视觉 | 理解由“看哪里、何时再看、能做什么”构成 | Rendering-Free Lookahead 在未见 episode +43%；EgoReveal 遮挡下重定位；FoveaVLA 注视替代腕部相机；SpatialScout 暴露建图差距 | 特权训练/模拟环境；任务特定；成本/风险/不可逆未联合建模；无一般世界状态 | 等成本/等风险下主动 vs 固定策略；不可逆动作；真实机器人转移 |
| R6 语言/教师引导 | 纯视觉不足以获得语义；需要语言/教师/数据引擎 bootstrap | CLIP/PE/MetaCLIP2 零样本；WOW-Seg 用 VLLM 命名；PaddleOCR-VL/dots.ocr 多语言解析；SAM 3 数据引擎 | 语言先验、数据策展、提示敏感；不是纯视觉；教师/合成数据成本与偏差 | 匹配视觉经验、推理无文字；新概念发现；预训练-评测重叠与数据来源审计 |

### 判别实验矩阵

| 实验 | 主要竞争路线 | 预测 | 失败判据 |
|---|---|---|---|
| T1 匹配数据/算力的视觉 SSL vs 图文/教师 | R1 vs R6 | R1 在类别/密集任务追平，在文字定义的新概念/关系上落后 | 若 R1 全面追平，R6 的语义 bootstrap 主张被削弱；若 R1 全面落后，纯视觉规模路线受挑战 |
| T2 世界状态探针（永久性、接触、身份、遮挡） | R1/R2/R3 | 显式几何/预测状态在遮挡/接触上优于纯静态特征 | 静态特征同等或更好，说明“世界状态”可由规模特征隐式承担 |
| T3 反事实/干预预测 | R2/R3/R4 | 只有能表示因果变量的状态在干预后保持正确 | 预测分数高但干预后系统性错误，说明只是相关性拟合 |
| T4 等成本/等风险的主动 vs 固定观察 | R5 | 高不确定性、可逆视角下主动更好；低不确定性/高风险下不优 | 主动策略在任何条件都更好或都更差，说明收益/成本模型不成立 |
| T5 新关系/新工具/新机体的组合迁移 | R4/R6 | 对象/关系/可供性结构支持组合迁移；纯语言先验在无文字时退化 | 迁移只随语言/标签覆盖变化，说明结构主张未被支持 |

### 当前判断

- **没有单一路线覆盖全部证据。** R1 的规模证据最强但缺时序/物理；R2 的几何最显式但缺语义/因果；R3 的预测最接近“世界模型”但生成/模拟域偏差大；R4 的结构最可解释但标签依赖强；R5 的行动最接近具身但任务特定；R6 的语义最强但不再是纯视觉。
- **最强的可检验假设是分层混合，而不是模块堆叠：** 视觉自监督提供可扩展表征，显式几何/对象结构提供状态骨架，预测/干预目标约束因果变量，主动观察获取缺失证据，语言/教师只在可审计的条件下补语义。这个假设仍必须在 Clover 上逐层消融，不能因为各模块都有论文支持就直接合并。
- **对 Clover 的下一步：** 先实现 T1–T3 的离线判别实验（不需要真实机器人），用同一数据/算力配平 R1/R2/R3/R6；只有在 T2/T3 显示显式状态有独立增益后，才进入 T4/T5 的闭环与主动采证。任何阶段都不以单一 benchmark SOTA 作为“理解”的证明。

<!-- END frontier-synthesis-2026-10 -->


<!-- BEGIN broad-vision-questions -->
<a id="broad-vision-questions"></a>

## 广义纯视觉 AGI 与原生 ultrafast：必须共同回答的问题

原母问题不变。研究范围包括基础视觉功能，也包括跨时间、跨任务、开放世界的理解；机器人控制是其中一个用途。一个任务成功不授予其他能力，列全任务也没有自动回答一般智能如何形成。

| 待区分问题 | 竞争解释/参照 | 后续能区分它们的证据 |
|---|---|---|
| 是否存在兼顾识别、定位、分割、追踪与阅读的共同表征？ | 专用模型、统一架构分别训练、单权重多任务、持续共享状态 | 配平数据/骨干/计算后，基本功能、跨任务迁移和负迁移分项报告 |
| 共享“身份”究竟对应点、外观、语义实例还是物理实体？ | 点轨迹、框关联、掩码记忆、显式/分布式实体状态 | 遮挡/重现、相近实例、分裂合并、外观/功能改变与反证后修正 |
| 开放词汇识别来自视觉经验还是语言/教师知识？ | 视觉 SSL、视觉监督、图文预训练、标签/知识图驱动数据引擎 | V/L 来源匹配；新类别/属性/关系组合与无关文字/背景替换 |
| 多任务接口带来一般能力还是任务 token 路由？ | Pix2Seq/Florence/OneFormer/WeVisOne 等不同统一方式 | 新任务或新组合的学习、输出接口改变和共同状态贡献；不把 API 数量当 AGI |
| 视觉阅读如何与世界理解共存？ | 转写/布局专用器、图文解析器、视觉推理状态 | 小字/密集文档与自然视频同时覆盖；像素所见、语言先验和推断错误分开 |
| 原生计算机制能否同时保持全部关键视觉证据？ | 直接密集预测、序列解码、循环/SSM、稀疏/自适应与混合计算 | 相同完整工作负载的结果完成时间、证据年龄、长时内存及小物体/边界/运动/记忆保持 |
| 物理/因果识别是否依赖不可见的结构先验？ | 像素预测、已知 ODE、单父解码、局部稀疏/干预图等理论 | 在明示假设内外对照；报告未识别等价类/近似界，不用自信度补成真值 |
| 部署任务外的证据是否仍可恢复？ | 任务充分压缩、共享世界状态、原始证据/可恢复记忆 | 在采集后才公布的新查询/新任务与反例；区分当时不存在和后来被丢弃的信息 |

[完整能力地图](perception-and-identifiability.md#broad-visual-capabilities)、[学习来源](learning-and-data.md#broad-visual-learning)、[计算维度](foundation-models-and-systems.md#native-ultrafast-research)与[验收地图](evaluation-and-benchmarks.md#broad-visual-evaluation)共同维护这些问题。它们约束调研/分析，当前没有选定 Clover 的答案或宣布实验通过。
<!-- END broad-vision-questions -->

## Contents

- [2026-10 Research Landscape: Five Falsifiable Pure-Vision Questions](#frontier-synthesis-2026-10)
- [Competing Explanations: Six Pure-Vision Routes](#competing-pure-vision-routes)
- [Research Questions](#topic-research-survey-research_questions)
- [01 — What Is a World Representation?](#topic-docs-research-questions-01-world-representation)
- [02 — Explicit vs Distributed Representation](#topic-docs-research-questions-02-explicit-vs-distributed)
- [03 — Prediction vs Reconstruction vs Generation](#topic-docs-research-questions-03-prediction-reconstruction-generation)
- [04 — What Can Vision Alone Identify?](#topic-docs-research-questions-04-what-can-vision-alone-identify)
- [05 — What Requires Interaction?](#topic-docs-research-questions-05-observation-vs-interaction)
- [06 — Memory and World Persistence](#topic-docs-research-questions-06-memory-and-world-persistence)
- [07 — Objects vs Fields vs Geometry](#topic-docs-research-questions-07-objects-fields-geometry)
- [08 — What Is Physical Understanding?](#topic-docs-research-questions-08-physical-understanding)
- [09 — What Is Causal Understanding?](#topic-docs-research-questions-09-causal-understanding)
- [10 — Why Should a Worldview Help Action?](#topic-docs-research-questions-10-world-model-to-action)
- [11 — Language and the Vision-Only Question](#topic-docs-research-questions-11-language-and-vision-only)
- [12 — Why Did Classical Computer Vision Not Naturally Scale Into World Understanding?](#topic-docs-research-questions-12-why-classical-cv-did-not-scale-to-world-understanding)
- [Open Research Questions](#topic-docs-open-questions)

<a id="topic-research-survey-research_questions"></a>

## Research Questions

Source record updated: 2026-10-14

Synthesis layer of the Clover Survey. These questions must be understood before the next Clover representation is frozen.

> **SSOT:** How can a machine understand the real world through vision alone?

> **Long-term goal:** Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.

---

### 1. What exactly is hidden, and what is actually observed?

A camera observes images, not the world state itself. The underlying problem is partially observable.

Useful background:

- POMDPs in Robotics — https://arxiv.org/abs/2209.10342
- Probabilistic Robotics — https://mitpress.mit.edu/9780262201629/probabilistic-robotics/

Clover must distinguish at least:

```text
observed
inferred
predicted
ambiguous
unobserved
contradicted
```

**Status: OPEN.**

### 2. What is a world representation?

A SLAM map, 3D reconstruction, object graph, predictive latent, video generator, policy hidden state and simulator are all called “world models” but are not interchangeable.

Candidate families:

```text
explicit geometry
object/entity state
distributed predictive latent
continuous field
episodic/persistent memory
generative simulator
hybrid/identifiable latent
```

**Status: OPEN.**

### 3. Must understanding be explicit?

Explicit state supports direct queries, revision, verification and planning. Distributed representations remain serious counter-hypotheses.

- Interpreting Physics in Video World Models — https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/
- Identifiable World Models — https://arxiv.org/abs/2610.07028

The question is not “can we name variables?” but whether explicit state produces capabilities that distributed state cannot match at comparable data/compute.

### 4. Which parts of geometry should be learned?

Projective geometry, camera projection, visibility and bundle adjustment have strong mathematical formulations. DUSt3R/VGGT show learned estimators can recover geometry robustly.

- ORB-SLAM3 — https://arxiv.org/abs/2007.11898
- DUSt3R — https://arxiv.org/abs/2312.14132
- VGGT — https://arxiv.org/abs/2503.11651
- VGGT-Ω — https://arxiv.org/abs/2605.15195

Research target: identify the division of labor between exact structure and learned priors.

### 5. What does static visual SSL already solve?

DINOv3 now provides a stronger static baseline than the previous Survey assumed.

- DINOv3 — https://ai.meta.com/research/publications/dinov3/
- Code — https://github.com/facebookresearch/dinov3

Question:

> Which claimed world-understanding capabilities disappear when the comparator is a very strong frozen image representation rather than an older encoder?

### 6. Prediction, reconstruction or generation?

These objectives preserve different information:

- V-JEPA predicts in latent space — https://arxiv.org/abs/2506.09985
- VGGT/Ω reconstruct geometry — https://arxiv.org/abs/2605.15195
- Atlas/Cosmos generate/simulate — https://www.worldlabs.ai/blog/atlas · https://arxiv.org/abs/2606.02800
- ReWAM challenges reconstruction-only control state — https://arxiv.org/abs/2609.38163

Which objective produces the most useful state for persistence, prediction, causality and action?

### 7. Is reconstruction a sufficient proxy for spatial understanding?

VGGT-Ω provides direct evidence that reconstruction features can help VLA and language alignment.

- https://arxiv.org/abs/2605.15195

But spatial reconstruction does not automatically establish memory, causality or action utility.

Required comparison:

```text
reconstruction accuracy
vs
world-query accuracy
vs
persistent memory
vs
action improvement
```

### 8. What can vision alone identify?

Visible boundary, motion, texture and appearance are visual evidence. 3D shape, identity, support and persistence require temporal evidence and assumptions. Exact force, friction, mass or hidden geometry may be underdetermined.

The system must not silently convert learned priors into observations.

### 9. What does “vision alone” mean for training, not just deployment?

Existing V0–V3 labels describe observation at inference. Modern VLM/VLA systems may also learn from language, actions, proprioception or privileged simulator state.

Background Research proposes a second provenance annotation:

```text
L0 visual self-supervision
L1 visual labels
L2 language/world knowledge
L3 action-conditioned experience
L4 non-visual / privileged physical evidence
```

Question: how much capability is attributable to visual experience itself?

### 10. Objects, fields, geometry, or combinations?

Objects help identity/composition; dense features scale well; geometry supplies metric constraints; fields may support local continuous computation.

Relevant evidence:

- Slot Attention — https://proceedings.neurips.cc/paper/2020/hash/8511df98c02ab60aea1b2356c013bc0f-Abstract.html
- PLATO — https://www.nature.com/articles/s41562-022-01394-8
- DINOv3 — https://arxiv.org/abs/2508.10104
- VGGT-Ω — https://arxiv.org/abs/2605.15195

Historical Clover must re-test its field/entity hierarchy rather than preserve it.

### 11. What is the difference between visible tracking and object permanence?

SAM 3.1 is a strong contemporary visible-entity baseline:

- research — https://ai.meta.com/research/publications/sam-3-segment-anything-with-concepts/
- code — https://github.com/facebookresearch/sam3

PersistBench explicitly evaluates what happens after the object leaves view:

- https://arxiv.org/abs/2609.20819

Question: what internal mechanism maintains identity/existence when perception no longer supplies the object?

### 12. What is persistent memory?

Possible memories:

```text
raw visual evidence
compressed world state
episodic events
object state
task state
semantic concepts
hybrids
```

Relevant sources:

- PersistBench — https://arxiv.org/abs/2609.20819
- S-EMBER — https://arxiv.org/abs/2607.02689
- VISTA — https://arxiv.org/abs/2610.02200

**Status: OPEN.** Evidence Replay is one candidate, not the default answer.

### 13. Which information may be forgotten safely?

A world model cannot retain all pixels indefinitely at high resolution.

The real problem is query/task sufficiency:

> What distinctions must survive compression for the family of world queries and actions the system claims to support?

Compare:

```text
fixed context
recurrent latent
hierarchical memory
query-conditioned retention
selective replay
```

### 14. How should memory revise itself?

```text
new evidence
→ contradiction
→ affected state
→ revision
→ downstream update
```

Measure stale detection, correction latency, update locality and downstream action recovery.

Historical belief-revision and proof/provenance machinery should only survive if they improve these outcomes.

### 15. What is physical understanding?

Suggested ladder:

```text
visual continuation
→ physical plausibility
→ relational/invariant consistency
→ task-relevant state transition
→ intervention-sensitive prediction
→ quantitative state when identifiable
→ improved action/recovery
```

Relevant instruments:

- IntPhys 2 — https://ai.meta.com/research/publications/intphys-2-benchmarking-intuitive-physics-understanding-in-complex-synthetic-environments/
- MVP — https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/
- Principia — https://arxiv.org/abs/2609.04200
- RoboPhys-3D — https://arxiv.org/abs/2608.28718

### 16. Do useful physical variables need compact coordinates?

Meta's mechanistic study reports distributed high-dimensional motion representations:

- https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/

Question:

```text
compact interpretable state
vs
distributed decodable state
vs
identifiable hybrid
```

Which representation best supports generalization, intervention and action at matched cost?

### 17. What is causal understanding?

```text
correlation
→ predictive dependency
→ intervention-sensitive dependency
→ counterfactual model
```

Relevant sources:

- CausalVQA — https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/
- CRL identifiability — https://proceedings.mlr.press/v238/varici24a.html
- multi-node interventions — https://proceedings.mlr.press/v236/bing24a

Historical Counter-Witness causality is a candidate linking prediction error and revision; it must show intervention/counterfactual gains over learned dynamics.

### 18. What does interaction add?

Passive video can learn broad statistical dynamics. Interaction adds:

```text
controllability
intervention
action consequence
affordance
active information acquisition
```

V-JEPA 2 provides a concrete passive-video → action-conditioned example:

- https://arxiv.org/abs/2506.09985

Causal-representation theory also motivates interventions as information sources.

### 19. Do we need active perception?

Can the system represent uncertainty well enough to decide the next visual action?

- Bajcsy — https://ieeexplore.ieee.org/abstract/document/5968
- Vantage — https://arxiv.org/abs/2610.11810

Core loop:

```text
ambiguity
→ information need
→ look/move/inspect
→ new RGB evidence
→ belief update
```

### 20. How should uncertainty and observability be represented?

```text
not visible ≠ empty
unobserved ≠ absent
unknown type ≠ nonexistent
low confidence ≠ false
confidence ≠ authority
plausible completion ≠ observed fact
```

Bayesian state estimation and POMDP belief state are important prior art. Historical Clover epistemic/licence semantics are one possible implementation, not the definition of the problem.

### 21. When is generative completion useful, and when is it dangerous?

Atlas/Cosmos demonstrate strong generation/simulation routes:

- Atlas — https://www.worldlabs.ai/blog/atlas
- Cosmos 3 — https://arxiv.org/abs/2606.02800

Question: can a model exploit plausible hidden completion for planning while retaining explicit knowledge that the completion is hypothetical rather than observed?

### 22. What role should language play?

Language injects semantics, world knowledge and task concepts.

Gemini ER 2, π0.5, OpenVLA and related systems mix visual evidence with language/action priors:

- Gemini ER 2 — https://deepmind.google/models/gemini-robotics/embodied-reasoning/
- π0.5 — https://arxiv.org/abs/2504.16054
- OpenVLA — https://arxiv.org/abs/2406.09246

Vision-only evaluation must distinguish visual inference from language-prior recall.

### 23. Is a persistent world state actually necessary for strong robot behavior?

Direct and implicit policies are serious falsifiers:

- π0.5 — https://arxiv.org/abs/2504.16054
- Figure Helix 2.5 — https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization
- Skild S1 — https://www.skild.ai/blogs/s1

Critical eventual comparison:

```text
strong matched policy
vs
strong matched policy + persistent world representation
```

A worldview must improve measurable embodied outcomes to justify itself.

### 24. What should the world↔action relationship be?

Competing structures:

```text
direct policy
hierarchical reasoner + VLA
explicit world + planner
world-action model
generative simulator + planner
```

Relevant evidence:

- Gemini ER 2 — https://deepmind.google/models/gemini-robotics/embodied-reasoning/
- WAM survey — https://arxiv.org/abs/2609.16074
- HWAM — https://arxiv.org/abs/2610.12026

### 25. What does “type” mean for a machine?

Possible type systems:

```text
semantic category
geometry class
dynamical equivalence
affordance/effect equivalence
learned transformation class
```

Evaluate by transfer to novel objects/actions rather than human-label agreement alone.

### 26. What should remain invariant across embodiments?

Candidate separation:

```text
embodiment-independent world structure
+
embodiment-specific controllability/effect model
```

Relevant sources:

- Open X-Embodiment — https://github.com/google-deepmind/open_x_embodiment
- Skild omni-bodied thesis — https://skild.ai/blogs/building-the-general-purpose-robotic-brain

### 27. How should real-world understanding be evaluated?

Combine:

```text
controlled physics
shortcut-resistant pairs
persistent memory
streaming recall
real video
intervention
active perception
world change/revision
long-horizon tasks
unseen environments
action usefulness
```

RoboPhys-3D is especially relevant to state/action-grounded evaluation:

- https://arxiv.org/abs/2608.28718

### 28. What should a Failure Matrix record?

At minimum:

```text
geometry
identity
permanence
temporal consistency
observability
memory/retrieval
physics
causality
counterfactuals
OOD/generalization
camera shift
revision/recovery
long horizon
action utility
compute
```

This matrix should exist before a new representation decision.

### 29. When should hardware influence theory?

Hardware should not select the scientific representation.

The order remains:

```text
science problem
→ representation
→ algorithm
→ compute structure
→ CPU/GPU/Metal/other mapping
```

M4 suitability is an engineering property, not scientific correctness.

### 30. Why did CPU-era classical vision not become general world understanding?

Not simply speed. Important limits included handcrafted/task-specific representations, fragmented pipelines, limited data scaling and weak learned abstraction.

Historical anchors:

- SIFT — https://www.cs.ubc.ca/~lowe/papers/ijcv04.pdf
- AlexNet — https://papers.nips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf
- ResNet — https://arxiv.org/abs/1512.03385
- ViT — https://arxiv.org/abs/2010.11929
- CLIP — https://arxiv.org/abs/2103.00020

### 31. What should the next Clover architecture decision look like?

Not:

```text
interesting paper
→ add mechanism
```

Not:

```text
historical Clover idea
→ search for supporting evidence
```

Required chain:

```text
Background Research
→ strong baseline setup
→ Understanding Battery
→ Failure Matrix
→ unresolved cross-family contradiction
→ candidate representations
→ discriminating experiment
→ falsifier
→ architecture decision
→ implementation
```

A next-generation Clover proposal must state what observed failure it solves, what evidence supports it, what would kill it and what remains open.

---

<a id="topic-docs-research-questions-01-world-representation"></a>

## 01 — What Is a World Representation?

### Question

What internal state must a machine maintain so that visual observations become a usable model of a persistent world rather than a stream of unrelated frames?

### Major prior answers

#### Explicit geometric state

Classical SfM/SLAM represents cameras, landmarks and geometric constraints explicitly. ORB-SLAM3 demonstrates that a system can maintain and merge maps over long time spans and across revisits.

Strength: variables are interpretable and directly usable for localization and geometry.

Limit: geometry alone does not provide object identity, affordance, semantics, causal structure or broad open-world abstraction.

#### Learned distributed state

DINOv2 and V-JEPA-style encoders learn feature spaces rather than hand-written geometric state. V-JEPA 2 extends this to video and shows that large-scale self-supervised video learning supports motion understanding, action anticipation and, after action-conditioned post-training, robot planning.

Strength: broad abstraction can emerge without manually defining every variable.

Limit: what constitutes the persistent world state is less explicit, and updating/revising a long-lived world model remains a separate question.

#### Learned geometric state

VGGT directly predicts cameras, depth, point maps and 3D tracks with a feed-forward model. VGGT-Ω pushes this direction toward larger-scale, dynamic reconstruction and more transferable geometry-aware representations.

Strength: combines learned priors with explicit geometric outputs.

Limit: accurate reconstruction is not equivalent to physical, causal or task-level understanding.

#### Generative/spatial world models

World Labs Atlas and NVIDIA Cosmos 3 represent another answer: train a large model to generate/reconstruct/simulate coherent worlds across modalities. These systems suggest that a world representation may be best judged by what coherent futures or spatial continuations it can generate.

Limit: generation quality can hide state inconsistency; persistent identity, observability and intervention structure require separate measurement.

### Current synthesis

A useful world representation likely needs to support at least four functions:

1. **state** — what currently exists and where;
2. **persistence** — what remains true when not currently visible;
3. **transition** — how the world can change;
4. **query/action interface** — what downstream decisions can reliably read.

No current route establishes that one representation family is sufficient for all four.

### Clover implication

Clover should not choose `field`, `object graph`, `3D map`, or `latent` by preference. The next representation hypothesis should be selected by whether it jointly supports persistence, revision, dynamics, queryability and action utility.

### Primary sources

- ORB-SLAM3 paper: https://arxiv.org/abs/2007.11898
- ORB-SLAM3 code: https://github.com/UZ-SLAMLab/ORB_SLAM3
- DINOv2 paper: https://arxiv.org/abs/2304.07193
- V-JEPA 2 paper: https://arxiv.org/abs/2506.09985
- V-JEPA 2 official code: https://github.com/facebookresearch/vjepa2
- VGGT paper: https://arxiv.org/abs/2503.11651
- VGGT code: https://github.com/facebookresearch/vggt
- VGGT-Ω paper: https://arxiv.org/abs/2605.15195
- VGGT-Ω code: https://github.com/facebookresearch/vggt-omega
- World Labs Atlas: https://www.worldlabs.ai/blog/atlas
- Cosmos 3 paper: https://arxiv.org/abs/2606.02800

---

<a id="topic-docs-research-questions-02-explicit-vs-distributed"></a>

## 02 — Explicit vs Distributed Representation

### Question

Must world understanding be stored in compact explicit variables, or can a high-dimensional distributed representation be the better substrate?

### Why this matters

Old Clover prototypes lean toward explicit machine-native state. Modern representation learning provides a serious counter-hypothesis: useful physical information may be distributed across large feature spaces and only become readable when needed.

### Evidence for distributed representations

DINOv2 shows that self-supervised training at scale can produce generic visual features transferable across many tasks.

V-JEPA 2/2.1 shows that predictive self-supervision can produce strong global and dense video features. V-JEPA 2.1 specifically adds dense predictive loss and deep self-supervision to improve spatially and temporally grounded features.

Meta's mechanistic work on physics in video world models reports that some physical variables become increasingly linearly accessible across network depth while other quantities can be represented by distributed population codes rather than a small set of dedicated units.

### Evidence for explicit outputs

Classical geometry remains compelling when the variable has a well-defined mathematical meaning: camera pose, projection, depth constraints and multi-view consistency are not arbitrary labels.

VGGT is important because it combines a learned network with explicit geometric outputs: camera parameters, depth, point maps and tracks.

### The real comparison

The right question is not `explicit vs neural`.

It is:

> Which information should remain distributed for flexibility, and which information should be materialized as explicit state because downstream reasoning, revision or control needs stable semantics?

A plausible hybrid is:

```text
learned distributed visual representation
        ↓
selective explicit state materialization
        ↓
planning / verification / interaction
```

But this remains a hypothesis.

### Clover implication

Clover should test whether explicit variables add value in:

- long-horizon persistence;
- belief revision;
- causal intervention;
- efficient planning;
- failure diagnosis;
- cross-task reuse.

If explicit state does not improve these, explicitness alone is not a contribution.

### Primary sources

- DINOv2: https://arxiv.org/abs/2304.07193
- V-JEPA 2: https://arxiv.org/abs/2506.09985
- V-JEPA 2.1: https://arxiv.org/abs/2603.14482
- V-JEPA 2/2.1 code: https://github.com/facebookresearch/vjepa2
- VGGT: https://arxiv.org/abs/2503.11651
- VGGT-Ω: https://arxiv.org/abs/2605.15195
- Slot Attention: https://arxiv.org/abs/2006.15055
- Meta — Interpreting Physics in Video World Models: https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/

---

<a id="topic-docs-research-questions-03-prediction-reconstruction-generation"></a>

## 03 — Prediction vs Reconstruction vs Generation

### Question

Which learning objective best creates a representation useful for understanding a persistent physical world?

### Reconstruction

Classical multi-view geometry and modern models such as DUSt3R, VGGT and VGGT-Ω ask the system to recover spatial structure from visual observations.

Reconstruction strongly constrains geometry because multiple views must agree on cameras, depth or point structure.

What it does not guarantee: understanding dynamics, causality, object purpose or task relevance.

### Prediction

V-JEPA 2 predicts in representation space rather than directly generating pixels. The key idea is that useful latent structure can be learned by predicting missing/future representations while avoiding the burden of modeling every pixel detail.

V-JEPA 2.1 strengthens dense and temporal grounding with dense predictive loss, deep self-supervision and unified image/video training.

Prediction provides a natural test of temporal regularity, but prediction accuracy alone does not establish causal understanding.

### Generation / simulation

NeRF and 3D Gaussian Splatting show how visual observations can parameterize scenes for novel-view rendering. Atlas and Cosmos 3 go further toward learned world generation and simulation.

Generation can demonstrate rich spatial/temporal coherence, but photorealistic output can still be wrong at the state or action level.

### Planning-oriented latent world models

PlaNet, DreamerV3 and TD-MPC2 demonstrate another criterion: a world model can be useful even if it is optimized primarily to support control in latent space rather than reconstructing a human-readable world.

This creates a central Clover tension:

> Is the best representation the one that reconstructs reality most faithfully, predicts future representations most accurately, or supports decisions most efficiently?

### Current synthesis

These objectives supervise different invariants:

- reconstruction → spatial consistency;
- prediction → temporal/statistical consistency;
- generation → distributional/world continuation;
- control/world-action learning → action-relevant dynamics.

A future Clover objective may need a combination, but combining losses without a principled reason would be framework stacking. The research task is to identify which invariant is necessary for which capability.

### Primary sources

- DUSt3R: https://arxiv.org/abs/2312.14132
- VGGT: https://arxiv.org/abs/2503.11651
- VGGT-Ω: https://arxiv.org/abs/2605.15195
- V-JEPA 2: https://arxiv.org/abs/2506.09985
- V-JEPA 2.1: https://arxiv.org/abs/2603.14482
- NeRF: https://arxiv.org/abs/2003.08934
- World Labs Atlas: https://www.worldlabs.ai/blog/atlas
- Cosmos 3: https://arxiv.org/abs/2606.02800
- DreamerV3: https://arxiv.org/abs/2301.04104
- TD-MPC2: https://arxiv.org/abs/2310.16828

---

<a id="topic-docs-research-questions-04-what-can-vision-alone-identify"></a>

## 04 — What Can Vision Alone Identify?

### Question

Before designing a world model, we must separate what is identifiable from visual evidence from what remains fundamentally ambiguous without assumptions, motion or intervention.

### Geometry already teaches an important lesson

A single image does not uniquely specify the physical world. Projection discards information. Monocular geometry has scale and depth ambiguities; textureless regions, occlusion and repeated structure create additional uncertainty.

Multi-view motion changes the problem because viewpoint variation creates constraints. SfM/SLAM exploits exactly this: geometry becomes better identified from multiple observations and camera motion.

### Learned priors change inference, not observability

Modern models can infer plausible depth, object category or motion from a single view using learned regularities. This is valuable, but a learned prior is not the same as direct observation.

For Clover this distinction matters:

```text
observed evidence
learned prior
inferred state
unobserved region
```

should not be silently collapsed.

### Active vision changes what is knowable

A robot is not a passive camera. If two world hypotheses are visually indistinguishable, the system can move, change viewpoint or manipulate the scene to acquire discriminating evidence.

This makes `vision alone` compatible with information-seeking action: the sensory channel stays visual even though action changes the future observations.

### Research consequence

A world-understanding system should represent not only a best estimate but also which aspects are underdetermined by current visual evidence.

This is more fundamental than a confidence score. The machine should know *what observation would resolve the ambiguity*.

### Clover implication

The future Clover state should distinguish at least conceptually:

- directly observed;
- geometrically constrained;
- prior-inferred;
- currently unobserved;
- ambiguous among multiple hypotheses.

Whether these become explicit fields or remain distributed is still open.

### Primary sources

- ORB-SLAM3: https://arxiv.org/abs/2007.11898
- VGGT: https://arxiv.org/abs/2503.11651
- VGGT-Ω: https://arxiv.org/abs/2605.15195
- DUSt3R: https://arxiv.org/abs/2312.14132
- Active Perception overview roots: Ruzena Bajcsy, "Active Perception" (1988), DOI landing page: https://doi.org/10.1109/34.8800

---

<a id="topic-docs-research-questions-05-observation-vs-interaction"></a>

## 05 — What Requires Interaction?

### Question

How much world understanding can be learned from passive visual observation, and what knowledge requires acting in the world?

### Evidence from passive video

V-JEPA 2 is a major data point. It pretrains on more than one million hours of image/video data without actions and obtains strong motion/action understanding. This shows that a large amount of physical regularity is available from observation alone.

But robot planning is introduced by post-training an action-conditioned model with robot trajectory videos. That separation is scientifically useful: it suggests passive observation can build a broad visual prior while interaction teaches controllable transitions.

### Evidence from robot foundation models

π0.5 combines robot trajectories with web/multimodal knowledge, object detections and hierarchical semantic targets. Figure Helix 2.5 reports improved unseen-home generalization after pretraining on large-scale human behavior data. Skild reports combining human video, robot data, simulation and other physical experience.

These systems do not isolate a single causal factor, but collectively they suggest that broad physical competence benefits from heterogeneous experience.

### What interaction uniquely provides

Observation can reveal correlation and natural dynamics. Intervention gives stronger information about:

- controllability;
- action-conditioned transitions;
- object affordance;
- latent physical properties exposed by contact;
- causal direction under deliberate perturbation.

### Clover implication

The scientific question should be split:

1. What world structure can be acquired from vision-only observation?
2. What additional structure becomes identifiable when the agent acts but still receives only visual sensory evidence?

This preserves the vision-only SSOT while allowing embodied learning.

### Primary sources

- V-JEPA 2 paper: https://arxiv.org/abs/2506.09985
- V-JEPA 2 project/code: https://github.com/facebookresearch/vjepa2
- π0.5 paper: https://arxiv.org/abs/2504.16054
- π0.5 project: https://www.pi.website/blog/pi05
- Figure Helix 2.5 official report: https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization
- Skild S1 official report: https://www.skild.ai/blogs/s1
- Skild Physical Self-Play: https://skild.ai/blogs/physical-self-play

---

<a id="topic-docs-research-questions-06-memory-and-world-persistence"></a>

## 06 — Memory and World Persistence

### Question

If the visual field changes every moment, what should persist inside the machine, for how long, and in what form?

### Different traditions answer differently

#### SLAM

Persistent maps and keyframes preserve geometric information across time and revisits. ORB-SLAM3 is a strong example of reusing older map information and merging maps after tracking loss.

#### Video models

Transformers and video encoders maintain temporal context inside a finite computation window. V-JEPA 2.1 targets temporally consistent dense features, but a feature's temporal stability is not yet equivalent to an indefinitely persistent world memory.

#### Video segmentation

SAM 2 uses streaming memory for video segmentation, showing a practical architecture for carrying object-mask information through time.

#### Robot policies

Long-horizon policies may use context, recurrence or hierarchical subtask structure without exposing a persistent external world state.

### Three memory problems must be separated

1. **perceptual continuity** — keep identity over nearby frames;
2. **world persistence** — retain facts while they are out of view;
3. **lifelong consolidation** — retain useful knowledge across long periods without storing all raw observations.

Treating all three as one `memory module` hides the real research problem.

### Belief revision is the hard test

Memory is not useful if it only accumulates. A world model must support:

```text
old belief
+ new contradictory visual evidence
→ corrected world state
```

The important capability is selective persistence plus revision.

### Clover implication

Future Clover work should measure memory by world-query stability and correction, not by context length alone.

### Primary sources

- ORB-SLAM3: https://arxiv.org/abs/2007.11898
- SAM 2: https://arxiv.org/abs/2408.00714
- V-JEPA 2.1: https://arxiv.org/abs/2603.14482
- Ego4D dataset: https://ego4d-data.org/
- LIBERO lifelong robot learning benchmark: https://libero-project.github.io/main.html

---

<a id="topic-docs-research-questions-07-objects-fields-geometry"></a>

## 07 — Objects vs Fields vs Geometry

### Question

What are the basic units of a machine's world model: objects, continuous fields, geometric primitives, or something else?

### Object-centric view

Slot Attention argues that a scene can be decomposed into exchangeable slots that bind to entities and support compositional generalization.

SAM 2 demonstrates that object-like visual regions can be maintained over video with streaming memory.

Object representations are attractive for identity, relation and manipulation, but object boundaries can be ambiguous for fluids, articulated structures, crowds, shadows or changing topology.

### Geometric view

SLAM, DUSt3R and VGGT represent structure through cameras, points, depth and tracks. Geometry is strong for where things are and how views relate.

But pure geometry says little about which structure should count as an entity, what it can do, or why a change matters.

### Field/continuous view

NeRF represents a scene as a continuous radiance/density function. 3D Gaussian-style representations and generative spatial models offer other continuous or distributed scene substrates.

Old Clover field-crystallization hypotheses belong here, but they must be compared against these established continuous representations rather than treated as a unique category by default.

### Current synthesis

The world may require multiple scales of description:

```text
continuous spatial support
→ persistent structures
→ entities
→ relations / task abstractions
```

The research question is whether these need separate ontologies or can emerge from one representation family.

### Clover implication

The next Clover representation proposal should explain what happens in edge cases where `object` is not cleanly defined, while still making object-level action efficient when object structure is useful.

### Primary sources

- Slot Attention: https://arxiv.org/abs/2006.15055
- SAM 2: https://arxiv.org/abs/2408.00714
- DUSt3R: https://arxiv.org/abs/2312.14132
- VGGT: https://arxiv.org/abs/2503.11651
- NeRF: https://arxiv.org/abs/2003.08934

---

<a id="topic-docs-research-questions-08-physical-understanding"></a>

## 08 — What Is Physical Understanding?

### Question

What evidence is sufficient to say a machine understands physical behavior rather than recognizing visual patterns correlated with it?

### Levels of evidence

#### Level 1 — visual regularity

The model distinguishes common from unusual motion or appearance.

#### Level 2 — violation of expectation

Benchmarks such as IntPhys 2 test principles including permanence, immutability, spatiotemporal continuity and solidity.

#### Level 3 — state-variable accessibility

A representation makes quantities such as motion, depth or trajectories reliably decodable.

#### Level 4 — intervention stability

The model predicts how outcomes change under controlled interventions.

#### Level 5 — action usefulness

Physical knowledge improves planning and recovery in real or simulated interaction.

The higher levels are stronger evidence than benchmark recognition alone.

### Why shortcut controls matter

MVPBench uses minimal video pairs to reduce the chance that a model succeeds from superficial cues. This experimental idea is important for Clover: if the intended physical distinction can be solved by background or static-frame shortcuts, the result is weak evidence of understanding.

### Modern world models

V-JEPA 2 reports strong motion/action understanding and planning after action-conditioned post-training. Cosmos 3 combines multimodal understanding, world generation and action generation. New embodied-world-model evaluations such as RoboPhys-3D explicitly argue that perceptual realism can disagree with state- and execution-grounded correctness.

### Clover implication

Clover should eventually claim physical understanding only when evidence spans controlled diagnostics, counterfactual/intervention tests and downstream action.

### Primary sources

- IntPhys 2 official page: https://ai.meta.com/research/publications/intphys-2-benchmarking-intuitive-physics-understanding-in-complex-synthetic-environments/
- MVPBench official page: https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/
- V-JEPA 2: https://arxiv.org/abs/2506.09985
- Cosmos 3: https://arxiv.org/abs/2606.02800
- RoboPhys-3D: https://arxiv.org/abs/2608.28718

---

<a id="topic-docs-research-questions-09-causal-understanding"></a>

## 09 — What Is Causal Understanding?

### Question

When does a model move from predicting correlation to understanding how interventions change the world?

### Prediction is not yet causation

A video model can predict likely futures from observational regularities. This is valuable but does not by itself identify what variable caused the transition or what intervention would change the outcome.

### Causal evidence becomes stronger with interventions

For a robot, action provides natural interventions:

```text
observe state
→ apply controlled action
→ observe visual consequence
```

Repeated interventions can expose action-conditioned dynamics and affordances that passive video cannot uniquely identify.

### Counterfactual reasoning

A stronger world model should answer questions of the form:

- What if the support were removed?
- What if the object were pushed in another direction?
- Which action would make a desired state occur?

CausalVQA provides a useful video-reasoning diagnostic, but language QA is weaker evidence than interaction-grounded intervention prediction.

### Planning-oriented world models

PlaNet, DreamerV3, TD-MPC2 and V-JEPA 2-AC all use learned dynamics to support action selection. They show that predictive dynamics can be operationally useful without necessarily exposing a human-readable causal graph.

This is another Clover tension: explicit causal structure may aid revision and transfer, but it must demonstrate value beyond a strong latent dynamics model.

### Clover implication

Future causal claims should be tied to intervention-sensitive tests, not just next-frame or next-state accuracy.

### Primary sources

- CausalVQA official page: https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/
- V-JEPA 2 / V-JEPA 2-AC: https://arxiv.org/abs/2506.09985
- DreamerV3: https://arxiv.org/abs/2301.04104
- TD-MPC2: https://arxiv.org/abs/2310.16828

---

<a id="topic-docs-research-questions-10-world-model-to-action"></a>

## 10 — Why Should a Worldview Help Action?

### Question

If a direct policy can act successfully from vision, what additional value must a persistent world model provide?

### Direct-policy evidence

RT-2 established the modern VLA framing by representing robot actions in the same token space as language outputs and transferring web-scale vision-language knowledge into control.

OpenVLA provides an open-source VLA baseline trained on large-scale robot demonstrations.

π0.5 demonstrates that heterogeneous co-training can produce long-horizon behavior and meaningful generalization to new homes.

Figure Helix 2.5 and Skild S1 provide further vendor-reported evidence that broad pretraining can yield strong real-world robot behavior without exposing a classical explicit world state.

### Hierarchical reasoning evidence

Gemini Robotics ER 2 takes a more separated approach: a high-level embodied reasoning VLM handles spatial/temporal/physical reasoning, tool orchestration and success detection, while lower-level robotic models perform control.

This resembles the motivation behind Clover's Worldview → Decision → Tool Use → Execution decomposition, but similarity of decomposition is not evidence that Clover's specific internal representation is useful.

### What an explicit worldview must earn

A persistent worldview should provide measurable gains in at least some of:

- fewer unnecessary actions;
- better recovery after unexpected world change;
- longer-horizon consistency;
- safer refusal when evidence is insufficient;
- lower planning/search cost;
- transfer across tasks without retraining perception;
- better debugging or verification.

If it does not, direct/hierarchical policy learning remains the stronger engineering answer.

### Clover implication

The final paper should not argue for Worldview philosophically. It should demonstrate that the representation improves embodied performance under controlled comparisons.

### Primary sources

- RT-2 paper: https://arxiv.org/abs/2307.15818
- RT-2 PMLR publication: https://proceedings.mlr.press/v229/zitkovich23a.html
- OpenVLA paper: https://arxiv.org/abs/2406.09246
- OpenVLA code: https://github.com/openvla/openvla
- π0.5 paper: https://arxiv.org/abs/2504.16054
- π0.5 project: https://www.pi.website/blog/pi05
- Gemini Robotics ER 2 model card: https://deepmind.google/models/model-cards/gemini-robotics-er-2/
- Figure Helix 2.5: https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization
- Skild S1: https://www.skild.ai/blogs/s1

---

<a id="topic-docs-research-questions-11-language-and-vision-only"></a>

## 11 — Language and the Vision-Only Question

### Question

How should Clover study systems that use language pretraining when the SSOT asks what can be understood through vision alone?

### Why the distinction matters

Modern embodied models often inherit enormous amounts of semantic and commonsense knowledge from language or vision-language pretraining. This can dramatically improve task generalization, but it complicates claims about what was learned from visual evidence.

RT-2 explicitly transfers web-scale vision-language knowledge into robot control. π0.5 mixes image observations, language, object detections, semantic subtasks, web data and robot actions. Gemini Robotics ER 2 is a vision-language model based on Gemini 3.5 Flash.

These systems are important capability references, but they are not pure tests of visual world formation.

### Proposed research separation

Clover should distinguish:

#### Vision-only formation

What world structure can be learned from visual observations and visually observed interaction without language supervision?

#### Language alignment

Once a world representation exists, can language efficiently name, query and compose the learned structures?

#### Language prior

How much performance comes from knowledge imported through text rather than discovered from visual experience?

### Why this does not mean rejecting language

A general-purpose robot brain will likely need language. The research constraint is about causal attribution of capability, not banning useful interfaces.

Language can be a communication and task-specification channel while the scientific question remains: what world knowledge did vision itself provide?

### Clover implication

Future experiments should include vision-only and vision+language conditions when language knowledge could otherwise confound the central claim.

### Primary sources

- RT-2: https://arxiv.org/abs/2307.15818
- OpenVLA: https://arxiv.org/abs/2406.09246
- π0.5: https://arxiv.org/abs/2504.16054
- Gemini Robotics ER 2 model card: https://deepmind.google/models/model-cards/gemini-robotics-er-2/
- V-JEPA 2: https://arxiv.org/abs/2506.09985

---

<a id="topic-docs-research-questions-12-why-classical-cv-did-not-scale-to-world-understanding"></a>

## 12 — Why Did Classical Computer Vision Not Naturally Scale Into World Understanding?

### Question

Why did decades of CPU-era computer vision produce strong geometry, features and task-specific systems without naturally turning into the kind of broad visual intelligence now associated with large learned models?

This question matters because Clover originally treated CPU-first computation as a major prior. Hardware history alone does not explain the scientific transition.

### 1. Classical vision solved important invariance and geometry problems

SIFT engineered local features robust to scale, rotation and a meaningful range of viewpoint/illumination change. HOG engineered gradient statistics that were highly effective for human detection. SfM/SLAM developed explicit geometric estimation for cameras, maps and motion.

These methods were not primitive failures. Many remain mathematically strong baselines.

The limitation was usually the *scope of representation*: the designer chose what information should be represented and which task it should solve.

### 2. The deep-learning transition changed representation learning

AlexNet's 2012 ImageNet result is historically important for two linked reasons:

- a deep CNN learned hierarchical visual features from large labeled data rather than relying primarily on hand-designed descriptors;
- GPU implementation made training a 60M-parameter convolutional model on ImageNet practical enough to demonstrate the scaling advantage.

The scientific shift was therefore not simply `GPU > CPU`. It was:

```text
learned hierarchical representation
+ large data
+ scalable optimization
+ hardware able to execute the training
```

### 3. Architecture made scale usable

ResNet addressed optimization barriers that made very deep networks difficult to train. Vision Transformers later showed that, with large-scale pretraining, a comparatively generic attention architecture could compete with or exceed convolution-specific inductive biases.

The trend is important for Clover: architectures that look inefficient or under-constrained at small scale can become powerful once data, optimization and compute expose a better scaling regime.

### 4. Supervision broadened

ImageNet classification still learned a fixed label space. Later systems broadened supervision:

- CLIP used hundreds of millions of image-text pairs to create transferable visual-language representations;
- DINOv2 demonstrated strong transferable image features with self-supervision;
- V-JEPA 2/2.1 moves the learning signal into video prediction and temporal structure.

This progression reduces dependence on manually enumerated visual concepts.

### 5. What classical methods still do better conceptually

Modern learned systems do not invalidate classical insights. Geometry provides exact structure and identifiable variables when its assumptions hold. Bayesian filtering and POMDP theory distinguish state, belief, observation and action more clearly than many end-to-end networks. These distinctions may still be necessary in a general robot brain.

The research opportunity is therefore not to return to old CPU CV or to accept end-to-end scaling uncritically.

It is to ask:

> **Which structures should remain explicit because mathematics already characterizes them, and which structures should be learned because hand-designed representations fail to scale to open-ended visual experience?**

### 6. Hardware should follow the computation

The history suggests a co-design conclusion:

- GPUs won many deep-learning workloads because dense tensor operations parallelize extremely well;
- CPUs remain strong for irregular, sparse, branching and control-heavy computation;
- Apple Silicon unified memory makes heterogeneous CPU/GPU execution especially interesting for a future Clover implementation;
- but none of these hardware facts decide the representation scientifically.

### Clover implication

Clover should avoid two symmetric mistakes:

1. **nostalgia error** — assuming classical/CPU methods are more principled and therefore sufficient;
2. **scaling error** — assuming larger learned models automatically constitute world understanding.

The next Clover architecture should inherit mathematical structure where it is genuinely known and use learning where the world is too open-ended to hand-code.

### Primary sources

- SIFT — David Lowe, *Distinctive Image Features from Scale-Invariant Keypoints* (IJCV 2004): https://doi.org/10.1023/B:VISI.0000029664.99615.94
- SIFT author-hosted PDF: https://www-inst.eecs.berkeley.edu/~ee225b/sp11/readings/sift-lowe.pdf
- HOG — Dalal & Triggs, CVPR 2005: https://doi.org/10.1109/CVPR.2005.177
- AlexNet — Krizhevsky, Sutskever & Hinton, NeurIPS 2012: https://proceedings.neurips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html
- AlexNet PDF: https://papers.nips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf
- ResNet: https://arxiv.org/abs/1512.03385
- Vision Transformer: https://arxiv.org/abs/2010.11929
- CLIP: https://arxiv.org/abs/2103.00020
- DINOv2: https://arxiv.org/abs/2304.07193
- V-JEPA 2: https://arxiv.org/abs/2506.09985
- V-JEPA 2.1: https://arxiv.org/abs/2603.14482

---

<a id="topic-docs-open-questions"></a>

## Open Research Questions

These questions are first-class project assets. They are not placeholders for missing documentation.

### Representation

1. What internal representation is sufficient for world understanding?
2. Does useful understanding require explicit state?
3. Can distributed latent representations be sufficient and still support persistence, intervention and planning?
4. Should objects be primitives or emergent structures?
5. Are fields, objects and geometry competing representations or different views of one world state?

### Geometry and learning

6. Which properties should be guaranteed by geometry rather than learned?
7. Which abstractions are difficult or inefficient to hand-design?
8. Can a learned geometry foundation model replace or complement classical state estimation?

### Time and memory

9. What representation best preserves identity through occlusion and long time gaps?
10. How should multiple temporal scales coexist?
11. What should be forgotten, consolidated or replayed?

### Physics and causality

12. How much physical understanding can be learned from passive video?
13. What requires interaction?
14. How should causal structure be distinguished from predictive correlation?
15. What internal representation best supports counterfactual reasoning?

### Epistemics

16. How should unknown, unobserved, contradicted and stale information be represented?
17. What role, if any, should Clover's licence mechanism play in a final architecture?

### Embodiment

18. Does language improve world understanding or mainly inject external knowledge?
19. How should active perception emerge from world uncertainty?
20. What makes a world representation materially useful for robot decision-making?
21. Can a persistent worldview outperform a direct VLA on long-horizon recovery and intervention tasks?

### Evaluation

22. Which benchmark combinations actually discriminate understanding from shortcut exploitation?
23. What real tasks should define the final embodied result?
24. How should correctness, coverage, uncertainty and task utility be measured together?

### Hardware

25. Which components are naturally CPU, GPU or accelerator workloads once the scientific mechanism is known?
26. Can unified-memory systems such as Apple Silicon provide a useful prototype platform for mixed sparse/dense computation?

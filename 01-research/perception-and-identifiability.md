<a id="top"></a>

# 调研方向：视觉感知、识别、追踪与可识别性

Maintained: **2026-10-25** · Document stage: **1 — Research** ([status](../STATUS.md)).

Core visual recognition, detection, segmentation, tracking and visual reading; image formation, geometry, hidden physical properties and the limits of visual evidence.

This is the canonical topic document. Update it in place; source-level dates and reading-depth labels below qualify the evidence, not the maintenance date.

<a id="reflection-evidence"></a>

## 2026-10-25 当前补充：镜面外观与物理分解

### Ref-NeRF：拟合反射外观不等于证明真实物理分解

- **来源：** Dor Verbin 等，*Ref-NeRF: Structured View-Dependent Appearance for Neural Radiance Fields*，CVPR 2022，5491–5500。[论文与书目信息](https://openaccess.thecvf.com/content/CVPR2022/html/Verbin_Ref-NeRF_Structured_View-Dependent_Appearance_for_Neural_Radiance_Fields_CVPR_2022_paper.html) · [作者项目与数据](https://dorverbin.github.io/refnerf/) · [官方代码](https://github.com/google-research/multinerf)。`PRIMARY_PAPER` / `OFFICIAL_PROJECT` / `OPEN_SOURCE`。
- **实际证据：** 将随视角变化的辐射改为反射方向参数化，并用法线正则改善光泽表面新视角渲染；项目提供 Shiny 合成场景和真实采集场景。
- **观测与学习来源：** 多视图 RGB 加相机内外参；属于校准多视图条件，不能记为不带校准的 `V0`。单移动相机的 posed views 也不应直接改记为物理多相机 `V2`；须按采集实例记录。场景拟合主要是光度自监督 `L0`，相机位姿的取得方式另记。官方代码说明自己的真实图像流程使用 COLMAP 求位姿。
- **没有证明：** 可编辑、可解释的外观参数不是反射率、光照和真实表面法线唯一可识别的定理；也未检验持续物体身份、接触状态或因果预测。
- **阅读深度与复现边界：** 核对会议摘要、作者项目及代码说明，未复核完整正文与证明；官方 MultiNeRF 仓库于 2025-02-11 归档，且说明 Ref-NeRF 结果可能与原内部实现略有差异，不能把公开代码存在写成复现成功。

### NeRFactor：“无监督”的场景拟合仍可以包含测量先验

- **来源：** Xiuming Zhang 等，*NeRFactor: Neural Factorization of Shape and Reflectance Under an Unknown Illumination*，ACM TOG / SIGGRAPH Asia 2021。[论文](https://arxiv.org/abs/2106.01970) · [作者项目、模型和数据](https://xiuming.info/projects/nerfactor/) · [官方代码](https://github.com/google/nerfactor)。`PRIMARY_PAPER` / `OFFICIAL_PROJECT` / `OPEN_SOURCE`。
- **实际证据：** 在同一未知光照下使用 posed 多视图 RGB，分解法线、可见性、反照率与 BRDF，用于重光照和材质编辑。
- **观测与学习来源：** 相机位姿已给定的多视图观测；光度重渲染损失 `L0` 加平滑先验，以及从真实 MERL BRDF 测量学习的材质先验 `L4`。场景图像不带材质标签，不等于整条学习链只使用视觉证据。
- **没有证明：** 单一未知照明下的物理分解唯一；也没有证明未知材质族或动态场景中的开放世界识别。
- **阅读深度：** 核对论文摘要和作者项目的输入、先验、数据及模型发布说明；未做完整正文复核。

**当前结论：** “镜面材质缺少被动 RGB 一手锚点”的资料空缺可由上述工作补上。仍开放的是：何种视角覆盖、相机校准、材质先验及照明条件，允许把“能重现图像”升级为可检验的真实几何/材质判断。后续分析应分别比较留出视角、改变光照、真实几何误差与下游接触判断；不能仅比较渲染分数。这里没有选择神经辐射场作为 Clover 表示。

<!-- BEGIN current-cross-domain-evidence -->
<a id="current-cross-domain-evidence"></a>

## 当前跨领域与前沿证据：观测到几何/物性的跨领域证据

检索/核验：**2026-10-25（Asia/Shanghai）**。下表是外部研究记录，不是 Clover 的实验结果或架构决定。

几何重建、物性辨识和控制完成度是不同主张。持续三维重建补上了“多帧如何进入状态”的比较对象；科学机器学习补上了“给定状态后怎样演化”的工具；两者之间从像素到物理变量的可识别性仍需单独论证。新出现的力/点云/手轨迹条件方法必须保留为有额外信息的强反假设，不能改写成视觉单独的成功。

### CUT3R

- **来源/版本：** [原论文](https://arxiv.org/abs/2501.12387v1)；初始提交 2025-01-21；本次返回版本更新于 2025-01-21。`PRIMARY_PAPER`。 [作者提供的项目/代码入口](https://cut3r.github.io/)（未运行复现）。
- **问题与机制：** CUT3R 以持续更新的循环状态输出共同坐标系点图，并支持虚拟相机查询。
- **输入/学习来源：** 部署可输入 RGB 序列；训练含深度/位姿/度量三维标注（L1/L4），不属于全链 V0/L0。
- **实际证据：** 3D/4D 重建、相机与深度任务；可作为短窗口几何与持续状态的比较对象。
- **不能推出 / 待区分：** 虚拟未见视角是推断；论文承认长序列缺全局对齐会漂移，不能据此宣称永久物体身份或开放世界记忆。
- **本次阅读深度：** 正文选读：方法、监督或局限段；未复核全部实验/证明。

### MonST3R

- **来源/版本：** [原论文](https://arxiv.org/abs/2410.03825v2)；初始提交 2024-10-04；本次返回版本更新于 2025-05-08。`PRIMARY_PAPER`。 [作者提供的项目/代码入口](https://monst3r-project.github.io/)（未运行复现）。
- **问题与机制：** MonST3R 把静态点图表示改成逐时刻几何，再针对视频深度和相机任务优化。
- **输入/学习来源：** 动态 posed 视频及深度标注用于微调；RGB 推理不消除 L1/L4 来源。
- **实际证据：** 动态深度、相机位姿与 4D 重建；与静态场景模型比较训练域和表示的共同作用。
- **不能推出 / 待区分：** 去掉显式运动变量仍能重建，不等于运动/物性已被唯一识别；移动前景与静态背景应分别评估。
- **本次阅读深度：** 正文选读：方法、监督或局限段；未复核全部实验/证明。

### GNS

- **来源/版本：** [原论文](https://arxiv.org/abs/2002.09405v2)；初始提交 2020-02-21；本次返回版本更新于 2020-09-14。`PRIMARY_PAPER`。
- **问题与机制：** Graph Network-based Simulators 用粒子节点和消息传递学习流体、固体与可变形动态。
- **输入/学习来源：** 给定粒子状态及模拟轨迹；输入/训练包含 L4，不是原始 RGB 感知。
- **实际证据：** 跨初态、粒子数和长轨迹模拟；训练噪声用于缓解自回归误差累积。
- **不能推出 / 待区分：** 良好动态模拟不能替代从像素估计粒子、接触和物性；训练时加噪也不自动保证真实相机/控制分布鲁棒。
- **本次阅读深度：** 正文选读：方法、监督或局限段；未复核全部实验/证明。

### Fourier Neural Operator

- **来源/版本：** [原论文](https://arxiv.org/abs/2010.08895v3)；初始提交 2020-10-18；本次返回版本更新于 2021-05-17。`PRIMARY_PAPER`。
- **问题与机制：** Fourier Neural Operator 学习参数函数到 PDE 解的算子映射。
- **输入/学习来源：** 使用方程族、场变量、边界与数值解数据；这些是额外物理证据/假设。
- **实际证据：** Burgers、Darcy、Navier–Stokes 及分辨率迁移等受控问题。
- **不能推出 / 待区分：** 网格分辨率迁移不是任意材质/新边界/新物理机制的 OOD 证明；求解器加速不是 camera→state→action 的端到端时延。
- **本次阅读深度：** 正文选读：方法、监督或局限段；未复核全部实验/证明。

### OmniRay

- **来源/版本：** [原论文](https://arxiv.org/abs/2610.31645v1)；初始提交 2026-10-22；本次返回版本更新于 2026-10-22。`PRIMARY_PAPER`。
- **问题与机制：** OmniRay 用复合射线场表达相机几何，从单图预测射线和 up-to-scale 径向距离。
- **输入/学习来源：** 推理不要求相机参数；训练标注/先验仍须按原文数据逐项登记。
- **实际证据：** 多相机成像类型的单目三维重建。
- **不能推出 / 待区分：** Camera-agnostic 不是无成像假设；up-to-scale 输出不能改写成绝对度量尺度唯一识别。
- **本次阅读深度：** 摘要与书目核验。

### HiP3R

- **来源/版本：** [原论文](https://arxiv.org/abs/2610.31635v1)；初始提交 2026-10-22；本次返回版本更新于 2026-10-22。`PRIMARY_PAPER`。 [作者提供的项目/代码入口](https://kkakkkka.github.io/HiP3R)（未运行复现）。
- **问题与机制：** HiP3R 结合块级 Sim(3) 与逐帧 SE(3) 位姿图，校正长序列局部重建不一致。
- **输入/学习来源：** 优化既有几何后端输出；不额外训练不等于后端没有标注/几何先验。
- **实际证据：** 长视频相机轨迹、回环与几何重建。
- **不能推出 / 待区分：** 全局一致性不自动处理动态身份、隐藏材质或非刚性接触；必须区分块间漂移和块内误差。
- **本次阅读深度：** 摘要与书目核验。

### Stream4D

- **来源/版本：** [原论文](https://arxiv.org/abs/2610.31320v1)；初始提交 2026-10-22；本次返回版本更新于 2026-10-22。`PRIMARY_PAPER`。
- **问题与机制：** Stream4D 从因果 KV-cache 注意力及深度先验构造动态掩码，抑制运动区域干扰相机估计。
- **输入/学习来源：** Training-free 指附加机制；既有骨干和深度先验的训练来源仍然存在。
- **实际证据：** 动态场景的流式相机/静态背景重建和掩码。
- **不能推出 / 待区分：** Serving cache 不等于语义世界记忆；改善静态背景轨迹不证明长期动态实体状态被保持。
- **本次阅读深度：** 摘要与书目核验。

### DeXplicit

- **来源/版本：** [原论文](https://arxiv.org/abs/2610.30781v1)；初始提交 2026-10-22；本次返回版本更新于 2026-10-22。`PRIMARY_PAPER`。
- **问题与机制：** DeXplicit 先预测度量三维的对象运动/形变，再把几何与外观投影给视频渲染器。
- **输入/学习来源：** 未来手轨迹为条件；训练有几何/运动监督，须保留 L3/L4，不是无标注视觉物理发现。
- **实际证据：** HOT3D、OakInk2、PhysTwin；正文的度量监督及渲染接口已选读。
- **不能推出 / 待区分：** 给定未来手动作的状态预测不是闭环选动作；两步生成与大双向模型的速度差也不能替代统一端到端比较。
- **本次阅读深度：** 正文选读：方法、监督或局限段；未复核全部实验/证明。

### Soft-Object World Model

- **来源/版本：** [原论文](https://arxiv.org/abs/2610.30988v1)；初始提交 2026-10-22；本次返回版本更新于 2026-10-22。`PRIMARY_PAPER`。
- **问题与机制：** Soft-Object World Model 以部分点云历史做完整状态与动作条件预测，再接目标规划。
- **输入/学习来源：** 模拟软体交互预训练，输入是点云；其深度/多视图取得方式及状态监督须核原文，不能直接记 V0。
- **实际证据：** 模拟与真实双臂衣物折叠，跨形状、材料、机体。
- **不能推出 / 待区分：** 补上可变形操作候选，不关闭 RGB-only 状态估计或不可见物性可识别性的缺口。
- **本次阅读深度：** 摘要与书目核验。

### DefFlow

- **来源/版本：** [原论文](https://arxiv.org/abs/2610.22827v1)；初始提交 2026-10-16；本次返回版本更新于 2026-10-16。`PRIMARY_PAPER`。
- **问题与机制：** DefFlow 联合预测机器人与可变形物体的目标条件三维点流。
- **输入/学习来源：** 示范学习 L3；真实点云来源需要与 RGB 推导/深度传感分开。
- **实际证据：** 绳、颗粒、布料及真实目标配置操作。
- **不能推出 / 待区分：** 机器人点流和物体点流的对照有辨别力，但不能把三维观测输入的成绩记成被动 RGB 的颗粒隐藏态恢复。
- **本次阅读深度：** 摘要与书目核验。

### FlowVLA

- **来源/版本：** [原论文](https://arxiv.org/abs/2610.29692v1)；初始提交 2026-10-21；本次返回版本更新于 2026-10-21。`PRIMARY_PAPER`。
- **问题与机制：** FlowVLA 将倒水动作生成与累计质量完成估计分开，处理近静态图像下的累积隐藏量。
- **输入/学习来源：** 融合视觉、关节、腕部 wrench 和力历史；明显含 L3/L4，不能记 RGB-only。
- **实际证据：** 定量倒水、未见目标质量及容器/流体设置。
- **不能推出 / 待区分：** 它是反证参照：给定力觉后成功不能关闭视觉单独可识别性；须保留纯视觉、历史和力觉配对对照。
- **本次阅读深度：** 摘要与书目核验。

### CW-WAM

- **来源/版本：** [原论文](https://arxiv.org/abs/2610.30117v1)；初始提交 2026-10-21；本次返回版本更新于 2026-10-21。`PRIMARY_PAPER`。 [作者提供的项目/代码入口](https://cw-wam-project.github.io/)（未运行复现）。
- **问题与机制：** CW-WAM 联合预测视频、运动和接触 wrench，并以慢模型/快导纳控制执行。
- **输入/学习来源：** wrench 记忆与力反馈是非视觉物理证据 L4。
- **实际证据：** 插入、搬举、擦拭等力敏感操作。
- **不能推出 / 待区分：** 不能把控制器和传感器贡献归给视觉世界模型；接触预测、力跟踪和任务成功应分别归因。
- **本次阅读深度：** 摘要与书目核验。
<!-- END current-cross-domain-evidence -->

<!-- BEGIN broad-vision-primary-evidence -->
<a id="broad-vision-primary-evidence"></a>

## 广义视觉理解的一手比较证据

核验日：2026-10-25。以下是外部方法与反例，覆盖经典接口、当前基础视觉与跨领域条件；未被采纳为 Clover 架构。

### Mask2Former

- **一手来源：** [固定版本](https://arxiv.org/abs/2112.01527v3) · [作者资源](https://github.com/facebookresearch/Mask2Former)。
- **机制：** 以掩码注意力和多尺度特征支持语义、实例、全景分割。
- **输入与学习来源：** RGB 加分割监督 L1；按实际骨干另登记预训练。
- **实际证据：** 同一架构用于三类分割。
- **边界与反假设：** 原文明确通用架构仍按任务/数据分别训练；不能把这些结果写成一个权重同时掌握全部任务。
- **阅读深度：** 正文选读：通用架构定义及掩码注意力；未复核全部实验；未运行复现。

### OneFormer

- **一手来源：** [固定版本](https://arxiv.org/abs/2211.06220v2) · [作者资源](https://github.com/SHI-Labs/OneFormer)。
- **机制：** 任务 token、联合训练和 query–text 对比，使单模型按请求切换三类分割。
- **输入与学习来源：** 全景/实例/语义标注 L1，并从类别名构造文本查询；文本编码器是否带独立语言预训练须按权重核对，不能仅凭文本形式判为 L2。
- **实际证据：** 相同模型在所训数据集上处理多种分割任务。
- **边界与反假设：** 每个数据集的训练与模型须区分；任务 token 选择功能不等于自发理解任意新任务，也未提供持续追踪身份。
- **阅读深度：** 正文选读：任务条件训练；未复核全部实验；未运行复现。

### ByteTrack

- **一手来源：** [固定版本](https://arxiv.org/abs/2110.06864v3) · [作者资源](https://github.com/ifzhang/ByteTrack)。
- **机制：** 先关联高置信检测，再以低置信检测恢复被遮挡目标；依赖检测器、运动预测与关联。
- **输入与学习来源：** RGB 部署；检测器和数据标注 L1，关联规则不消除其训练来源。
- **实际证据：** 多目标框轨迹与身份关联基线。
- **边界与反假设：** 遮挡时的预测轨迹不是观测到的实体状态；检测漏失、相机运动和身份切换须分开计错，关联 FPS 不能代替完整管线时延。
- **阅读深度：** 正文选读：两阶段关联；未复核全部实验；未运行复现。

### CoTracker3

- **一手来源：** [固定版本](https://arxiv.org/abs/2410.11831v1) · [作者资源](https://github.com/facebookresearch/co-tracker)。
- **机制：** 联合跟踪查询点，使用相关特征迭代更新，并以真实视频伪轨迹扩展训练。
- **输入与学习来源：** 合成 Kubric 轨迹监督及教师伪标签 L1/L4；真实无标签视频阶段不使全链成为 L0。
- **实际证据：** 点轨迹、可见性与遮挡预测；有在线/离线变体。
- **边界与反假设：** 在线滑窗与离线整段条件不同；未来帧、窗口等待、点数与重现身份必须逐项配平。点轨迹不自动给出对象类别或持久对象模型。
- **阅读深度：** 正文/官方说明选读：训练与在线变体；未复核全部实验；未运行复现。

### TAPNext++

- **一手来源：** [固定版本](https://arxiv.org/abs/2604.10582v1) · [作者资源](https://tap-next-plus-plus.github.io/)。
- **机制：** 保持在线循环架构，用 1024 帧合成序列、roll 增强和遮挡监督改善长时追踪与重检测。
- **输入与学习来源：** RGB 与查询点；PointOdyssey/Kubric-1024 等轨迹真值 L1/L4。
- **实际证据：** 引入重检测 AJ_RD，直接检查离场/遮挡后的重新对应。
- **边界与反假设：** 重现后关联正确与不可见期间真实位置正确须分测；长序列改进也可能来自训练覆盖。原论文与改进 checkpoint 不能混用速度/精度。
- **阅读深度：** 正文/官方项目选读：方法、数据与重检测指标；未运行复现。

### RT-DETRv4

- **一手来源：** [固定版本](https://arxiv.org/abs/2510.25257v2) · [作者资源](https://github.com/RT-DETRs/RT-DETRv4)。
- **机制：** 用冻结视觉基础教师的语义注入与梯度调制训练轻量检测器，部署移除教师。
- **输入与学习来源：** COCO 检测 L1；精确教师为 DINOv3-ViT-Base，教师预训练另记。
- **实际证据：** 检测精度与单 T4/TensorRT FP16 延迟的配对参照。
- **边界与反假设：** 推理不加教师不等于训练没有额外知识或成本；其检测优势不包含追踪、分割、记忆，也不是 Clover 的原生算法证据。
- **阅读深度：** 正文选读：教师、配置表与时延测量；未复核全部实验；未运行复现。

### WeVisOne-VL

- **一手来源：** [固定版本](https://arxiv.org/abs/2610.31329v1) · [作者资源](https://github.com/Tencent/WeVisOne-VL)。
- **机制：** Qwen3-VL 生成结构化标签/坐标和 OBJ token；共享视觉特征接轻量像素解码器输出掩码/alpha。
- **输入与学习来源：** 2B/4B 语言视觉骨干、约 100M 标注图、专家/VLM 数据引擎、三阶段 SFT 与混合 RL，含 L1/L2。
- **实际证据：** 检测、定位、计数、OCR、分割与抠图及目标缺席拒答。
- **边界与反假设：** 作者报告通用能力可能退化、复杂推理与单轮限制；多任务能力未证明纯视觉学习、视频追踪、AGI 或完整超低延迟。
- **阅读深度：** 正文选读：§2–4、§8；未复核全部实验；未运行复现。

### Grounding DINO

- **一手来源：** [固定版本](https://arxiv.org/abs/2303.05499v5) · [作者资源](https://github.com/IDEA-Research/GroundingDINO)。
- **机制：** 跨模态特征交互、语言引导 query 选择和解码器实现短语定位/开放集检测。
- **输入与学习来源：** 图像+文本条件；区域文本与检测预训练 L1/L2。
- **实际证据：** 指定词语/短语所对应的视觉区域。
- **边界与反假设：** 开放词汇受训练、提示和标签本体约束；未知概念发现与无语言先验识别仍需独立证据。
- **阅读深度：** 正文选读：跨模态机制与训练；未复核全部实验；未运行复现。

### YOLO-World

- **一手来源：** [固定版本](https://arxiv.org/abs/2401.17270v3) · [作者资源](https://github.com/AILab-CVC/YOLO-World)。
- **机制：** 区域文本对比与可重参数化视觉语言聚合；部署可预计算词汇并移除文本编码器。
- **输入与学习来源：** CLIP 文本编码器与区域/文本数据 L1/L2；离线词汇进入模型权重。
- **实际证据：** 开放词汇检测的效率与语言先验归属对照。
- **边界与反假设：** 部署输入仅图像不消除离线文本知识；更换词汇的成本须计入相应工作负载。
- **阅读深度：** 正文选读：离线词汇与重参数化；未复核全部实验；未运行复现。

### ARC-SORT

- **一手来源：** [固定版本](https://arxiv.org/abs/2610.22306v1) · [作者资源](https://arxiv.org/abs/2610.22306v1)。
- **机制：** 在 OC-SORT 基础上用交互多模型运动协方差给出逐轨迹连续关联容差；排列边际（permutation margin）推迟近歧义承诺；运动信息耗尽时改用 appearance-only merge；长时阶段离线。
- **输入与学习来源：** 关联器无新训练；上游检测器与外观来源仍须登记。
- **实际证据：** 作者报告 deferred commitment 的增益为验证集 delta 的 53–120%；DanceTrack 62.1 HOTA（仍低于训练专家），SportsMOT 落后 0.1–5.4 HOTA；公开 model-zoo 检测器限制 HOTA 上限。
- **边界与反假设（作者自述）：** 延迟承诺只是 pairwise/single-swap；长时阶段离线；检测质量封顶；不训练关联器不等于无检测成本/无监督/一般不确定性校准；需同检测输入比较完整管线与身份错误。
- **阅读深度：** 正文选读：方法、DanceTrack/SportsMOT 结果、Limitations；未复核全部附录；未运行复现。

### Physics from Video

- **一手来源：** [正式会议记录](https://proceedings.mlr.press/v306/wang26iq.html) · [论文](https://raw.githubusercontent.com/mlresearch/v306/main/assets/wang26iq/wang26iq.pdf)。
- **机制：** 编码器输出标量，用中心差分 ODE 残差和方差下界学习归一化二阶线性动力学系数。
- **输入与学习来源：** RGB 与已知采样间隔；预设自治线性 ODE、平滑 state-consistency 和轨迹覆盖。
- **实际证据：** 特定动力学和成像假设下的单/多轨迹可识别性及受控真实视频。
- **边界与反假设：** 单轨迹充分条件要求欠阻尼与覆盖；结果识别归一化系数，不能推出质量/刚度等各自唯一；任意真实视频的 state-consistency 难由像素验证。
- **阅读深度：** 正文 §3–4 与定理条件选读；未复核全部证明/实验；未运行复现。

### PhyWM

- **一手来源：** [正式会议记录](https://openaccess.thecvf.com/content/CVPR2026/html/Venkatesh_Physical_Object_Understanding_with_a_Physically_Controllable_World_Model_CVPR_2026_paper.html) · [论文](https://openaccess.thecvf.com/content/CVPR2026/papers/Venkatesh_Physical_Object_Understanding_with_a_Physically_Controllable_World_Model_CVPR_2026_paper.pdf)。
- **机制：** RGB、光流、相机和空间指针联合概率序列；由多个想象运动样本的相关性提取物体/关节部件。
- **输入与学习来源：** 真实视频、伪光流、可用相机位姿；补充材料还有 CLIP/语言检索筛选来源，非无外部先验 L0。
- **实际证据：** 物体/部件分割、可控三维编辑与关系任务。
- **边界与反假设：** 虚拟 poke 和运动相关性不等于对现实物体执行干预后的因果识别；生成的运动分布须独立校准。
- **阅读深度：** 主文 §3–4 与补充数据说明选读；未复核全部实验；未运行复现。
<!-- END broad-vision-primary-evidence -->

<!-- BEGIN core-vision-frontier -->
<a id="core-vision-frontier"></a>

## 核心视觉能力前沿：识别、检测、分割、追踪、动作、指代与阅读

检索/核验：**2026-10-25（Asia/Shanghai）**。本节补齐“识别图片、追踪目标”等基础视觉功能的一手比较对象；全部为外部研究，不是 Clover 已实现的能力。表中记录只支持其原始任务与数据条件下的结论；速度数字均来自作者在指定硬件、精度和后端上的报告，不能外推为 Clover 的端到端时延。

### 识别与视觉表征：基准精度已经很高，开放世界理解仍未闭合

识别主线的共同教训是：**固定类别或图文对齐上的高分，不等于从视觉经验形成可修正的世界模型**。监督分类提供 `L1`；图文对比提供 `L2`；只有目标函数不含语言/标签时才接近 `L0`，而数据筛选、评估问题和下游文本接口仍可能引入语言。纯视觉路线因此必须单独证明：不用语言监督时，规模能否补上语义与开放词汇能力。

| 方法 | 一手来源 | 机制与可核查证据 | 边界与反假设 |
|---|---|---|---|
| ResNet | [1512.03385](https://arxiv.org/abs/1512.03385v1) | 残差学习使 152 层网络可训练；ImageNet 集成 3.57% top-5 error，ILSVRC 2015 分类第一；COCO 检测相对提升 28% | 监督分类 `L1`；集成成绩不是单模型；ImageNet 类别精度不证明开放世界识别或物理理解 |
| ViT | [2010.11929](https://arxiv.org/abs/2010.11929v1) · [官方代码](https://github.com/google-research/vision_transformer) | 纯 Transformer 直接作用于图像 patch；大规模预训练后迁移到 ImageNet/CIFAR-100/VTAB，训练计算低于同类卷积网络 | 依赖大规模**带标签**预训练（`L1`）；patch 化会改变小字、小物体与细边界证据；“注意力可解释”不等于世界状态可识别 |
| ConvNeXt | [2201.03545](https://arxiv.org/abs/2201.03545v2) · [官方代码](https://github.com/facebookresearch/ConvNeXt) | 把 ResNet 逐项现代化为纯 ConvNet；ImageNet-1K 87.8% top-1，COCO 检测与 ADE20K 分割优于同期 Swin | 监督分类 `L1`；架构家族比较受训练配方影响；分类/检测精度不自动给出追踪身份或记忆 |
| MAE | [2111.06377](https://arxiv.org/abs/2111.06377v3) · [官方代码](https://github.com/facebookresearch/mae) | 随机遮 75% patch 后重建像素；非对称编码器-解码器使 ViT-H 在 ImageNet-1K 达 87.8%，训练加速 3 倍以上 | 像素重建是 `L0` 视觉自监督，但重建目标偏向纹理/外观，不直接约束语义、物理或因果；下游仍需标签微调 |
| CLIP | [2103.00020](https://arxiv.org/abs/2103.00020v1) · [官方代码](https://github.com/openai/CLIP) | 4 亿图文对做对比学习；30+ 数据集零样本迁移，零样本 ImageNet 匹配原 ResNet-50 | `L2` 语言监督；类别名/提示词敏感，图文噪声与英语世界偏差进入权重；“零样本”是未见过该数据集标签，不是无先验 |
| AIMv2 | [2411.14402](https://arxiv.org/abs/2411.14402v1) · [官方代码](https://github.com/apple/ml-aim) | 视觉编码器配多模态解码器，自回归生成原始图像 patch 与文本 token；AIMv2-3B 冻结主干 ImageNet-1K 89.5% | `L2`；自回归目标含文本，不能记作纯视觉；冻结主干精度不证明时序状态或定位一致性 |
| Meta CLIP 2 | [2507.22062](https://arxiv.org/abs/2507.22062v3) | 从全球网络图文对从头训练；ViT-H/14 零样本 ImageNet 比英语-only 高 0.8%，CVQA 57.4、Babel-ImageNet 50.2、XM3600 64.3 | `L2`；多语言基准仍是图文任务；数据策展与翻译/文化覆盖决定“worldwide”边界，不能推出视觉经验本身 |

> 纯视觉自监督与语言监督的受控比较（WebSSL）见[学习方向](learning-and-data.md#learning-provenance-frontier)；识别主线的完整来源批次见[来源表](sources-and-resources.md#core-vision-source-frontier)。

#### 识别的剩余失败面：长尾、细粒度与尺度鲁棒性

| 方法/研究 | 一手来源 | 机制与可核查证据 | 边界与反假设 |
|---|---|---|---|
| VICAL | [2609.04948](https://arxiv.org/abs/2609.04948v1) | 重新检验“多专家靠多样性获益”的假设，认为收益更多来自方差削减；自一致性学习 + 深度集成蒸馏；CIFAR-LT、ImageNet-LT、iNaturalist 2018 上报告改善 | `L1` 长尾分类；只在分类基准验证；方差削减不等于尾部概念真正被表征；不覆盖检测/追踪中的长尾 |
| OFBD | [2609.37331](https://arxiv.org/abs/2609.37331v1) | 发现长尾训练诱导背景偏置：尾部类受更大背景分布偏移与背景梯度驱动；Foreground-guided CutMix 保留目标前景并多样化背景，Background-guided Feature Rectification 无需可学习参数抑制背景偏置 | `L1` 长尾分类；背景/前景划分依赖标注或粗掩码；分类精度不证明开放世界识别；未覆盖视频/时序背景变化 |
| LIVE（From Glance to Focus） | [2610.13154](https://arxiv.org/abs/2610.13154v1) | 提出 MLLM 的 “FGVR Laziness”：在候选类别与识别引导下视觉线索-类别概念关联不足；训练无关地联合精炼候选列表与识别引导，激发已有细粒度能力 | `L2` MLLM；推理时方法，不新增视觉学习；候选列表仍是封闭集；细粒度基准上的提升不证明开放世界发现或视觉经验形成概念 |
| Image-Scale Robustness | [2609.06051](https://arxiv.org/abs/2609.06051v1) | 20 个 ImageNet-1K 分类器、7 个架构族；尺度-精度响应曲线与“特征尺度”；基线精度与特征尺度强负相关（Pearson r=−0.890，R²=0.792，p<10⁻⁶），参数量的额外解释力可忽略 | 相关性研究，不是因果；只测 ImageNet-1K 分类；尺度鲁棒性不等于高分辨率/小物体能力；未覆盖检测/追踪/OCR |

**识别结论：** 识别主线在经典封闭集基准上的精度已经很高，但长尾、细粒度与尺度鲁棒性仍是独立失败面；对纯视觉模型尤其重要，因为它不能靠语言先验补足训练分布外的概念。上述工作没有证明“识别已解决”，只证明特定分类协议下的强性能。

#### DINOv3：强稠密特征仍不是世界模型

- **一手来源：** [固定版本](https://arxiv.org/abs/2508.10104v1) · [官方代码与模型](https://github.com/facebookresearch/dinov3) · [研究页](https://ai.meta.com/research/publications/dinov3/)。`PRIMARY_PAPER` / `OPEN_SOURCE`。
- **机制：** 大规模视觉自监督；用 Gram anchoring 约束长训练中稠密特征退化，再用后处理扩展分辨率、模型规模与文本对齐。
- **输入与学习来源：** 图像自监督 `L0`（数据策展仍含来源筛选）；文本对齐变体另含 `L2`，必须按具体 checkpoint 区分。
- **实际证据：** 冻结稠密特征在分割、深度、跟踪等密集任务上超过此前自监督/弱监督基础模型，作者报告无需微调即可迁移。
- **不能推出：** 静态图像的强部位/形状特征不等于持续身份、遮挡后重现、物理属性或动作条件动力学；密集特征质量也不证明特征能被显式读出为世界变量。
- **阅读深度：** 摘要、官方模型说明与既有正文选读；未复核全部消融；未运行权重。

#### Perception Encoder：中间层才是通用表征，但仍是图文监督

- **一手来源：** [固定版本](https://arxiv.org/abs/2504.13181v2) · [官方代码、模型与数据](https://github.com/facebookresearch/perception_models)。`PRIMARY_PAPER` / `OPEN_SOURCE`。
- **机制：** 简单对比式视觉语言预训练后，从**中间层**取通用嵌入；再用语言对齐与空间对齐分别服务多模态语言建模和密集预测。
- **输入与学习来源：** 图文对比 `L2`，视频数据引擎扩展；空间对齐使用检测/深度等监督线索，按 head 另记。
- **实际证据：** 零样本 ImageNet 鲁棒性平均 86.6、Kinetics-400 零样本 76.9；配 8B LLM 达 DocVQA 94.6、InfographicVQA 80.9、PerceptionTest 82.7；COCO 检测 66.0 box mAP。
- **不能推出：** 一个编码器同时报告多任务分数，不等于单一前向同时输出全部能力；检测/深度头与语言模型是额外结构；静态 benchmark 不覆盖身份持续、主动采证或行动后果。
- **阅读深度：** 摘要、结论与官方模型说明；未复核全部实验；未运行复现。

### 检测：实时精度继续推进，但“统一模型”常指一个家族而非一个权重

| 方法 | 一手来源 | 机制与可核查证据 | 边界与反假设 |
|---|---|---|---|
| YOLOv12 | [2502.12524](https://arxiv.org/abs/2502.12524v1) · [官方代码](https://github.com/sunsmarterjie/yolov12) | 以注意力为中心重做实时 YOLO；YOLOv12-N 40.6% mAP、T4 1.64 ms，比 YOLOv10-N/YOLOv11-N 高 2.1%/1.2%；S 比 RT-DETR-R18 快 42%、算力 36%、参数 45% | `L1` COCO；T4 单图时延不是完整相机管线；注意力模型的实际速度依赖算子/后端；未证明小物体、长尾与开放词汇 |
| D-FINE | [2410.13842](https://arxiv.org/abs/2410.13842v1) · [官方代码](https://github.com/Peterande/D-FINE) | 把框回归改为细粒度分布细化（FDR）+ 全局最优定位自蒸馏（GO-LSD）；COCO 54.0/55.8 AP，T4 124/78 FPS；Objects365 预训练 57.1/59.3 AP | `L1`；FPS 为 T4 报告值；Objects365 额外数据与 COCO 结果须分列；分布回归不证明物理位置或尺度度量 |
| DEIM | [2412.04234](https://arxiv.org/abs/2412.04234v3) · [官方代码](https://github.com/ShihuaHuang95/DEIM) | Dense O2O 增加正样本 + Matchability-Aware Loss 处理低质量匹配；训练时间约减半，RT-DETRv2 单日 4090 达 53.2 AP；DEIM-D-FINE-L/X 54.7/56.5 AP、124/78 FPS T4 | `L1`；加速主要在**训练收敛**，不是推理时延；密集匹配仍可能引入低质量正样本；检测精度不等于关联/追踪 |
| LW-DETR | [2406.03459](https://arxiv.org/abs/2406.03459v1) · [官方代码](https://github.com/Atten4Vis/LW-DETR) | ViT 编码器 + 投影 + 浅 DETR 解码器，窗口/全局交替注意力与多级特征聚合；作者报告在 COCO 等基准优于 YOLO 系列 | `L1`；实时性依赖 TensorRT/分辨率；无 NMS 不等于无后处理成本；未覆盖追踪与分割 |

#### YOLO26：一个家族覆盖五类任务，但不是一个共享权重

- **一手来源：** [论文 v1](https://arxiv.org/abs/2606.03748v1) · [官方模型文档](https://docs.ultralytics.com/models/yolo26/) · [官方代码与发布](https://github.com/ultralytics/ultralytics)。`PRIMARY_PAPER` / `OPEN_SOURCE` / `OFFICIAL_REPORTED_RESULT`。
- **机制：** 双头设计同时支持原生 NMS-free 端到端路径与可选稠密+NMS 路径；移除 DFL；训练用 MuSGD、Progressive Loss 与 STAL 小物体正样本分配；检测外为实例分割、分类、姿态与旋转框分别设计 head/loss。
- **输入与学习来源：** 监督检测/分割/分类/姿态/旋转框标签 `L1`；COCO 等数据训练。官方文档中的各任务 checkpoint 不同，不能合并成一个权重。
- **实际证据：** 作者报告 COCO 40.9–57.5 mAP，T4 TensorRT 1.7–11.8 ms；端到端头相对 NMS 稠密头仅低 0.6–0.8 AP；YOLOE-26x 文本提示在 LVIS minival 40.6 AP；官方发布覆盖 19 种导出后端。
- **不能推出：** T4/TensorRT FP16 数字不是 M4 或真实相机闭环；分类/姿态/分割分别训练；“统一家族”不等于一个模型同时理解全部任务；文本提示版本仍属语言监督。导出到不支持 top-K 的运行时还会回退到非端到端分支。
- **阅读深度：** 正文选读：架构、训练、表 7、部署与结论；未复核全部附录；未运行权重或测速。

#### RF-DETR：面向目标数据集的 NAS，而不是通用开放世界检测器

- **一手来源：** [固定版本](https://arxiv.org/abs/2511.09554v2) · [官方项目](https://rfdetr.roboflow.com/) · [官方代码](https://github.com/roboflow/rf-detr)。`PRIMARY_PAPER` / `OPEN_SOURCE`（ICLR 2026）。
- **机制：** 在预训练检测 transformer 上做权重共享 NAS，对目标数据集搜索精度-时延 Pareto 前沿；重新设计可迁移的 NAS 旋钮。
- **输入与学习来源：** 目标数据集标注 `L1`；基座预训练来源另记；每个数据集需要微调与搜索，不是零样本开放词汇。
- **实际证据：** RF-DETR-nano COCO 48.0 AP，比 D-FINE-nano 高 5.3 AP（相近时延）；2x-large 为作者所称首个实时 COCO >60 AP 检测器；在 Roboflow100-VL 上比 GroundingDINO-tiny 高 1.2 AP、快约 20 倍。
- **不能推出：** 每个新数据集都要搜索/重训，搜索成本与碳排放未在摘要中闭合；COCO/Roboflow100-VL 不覆盖细粒度长尾与未知概念发现；检测器 specialist 不是视觉 AGI。
- **阅读深度：** 摘要、引言与官方项目说明；正文 HTML 仅覆盖前段，未复核全部实验；未运行搜索。

### 分割：从“可提示掩码”走向“概念、三维与多视图一致性”

| 方法 | 一手来源 | 机制与可核查证据 | 边界与反假设 |
|---|---|---|---|
| DCR-SAM | [2610.27960](https://arxiv.org/abs/2610.27960v1) · [官方代码](https://github.com/set-path/DCR-SAM) | 把 SAM3 的单概念提示扩展到多类语义分割；解耦跨模态交互 + 稠密竞争头 + 背景 token；作者报告 +2.3%–10.7% 精度、相对原生 SAM3 33× 推理加速 | `L1/L2`（文本概念）；加速来自批量/解耦实现，不是原生 SAM3 全任务；语义重叠与类别粒度仍受提示约束；未证明实例身份持续 |
| MaskMerge | [2610.22921](https://arxiv.org/abs/2610.22921v1) | 用粗掩码预测约束 token 合并，避免同类相邻实例被特征相似度融合；PanNuke mAP 30.1→32.1、229→153 GFLOPs、1.18×；iSAID 33.1→36.2、198→182 GFLOPs、1.23× | `L1` 实例分割；FLOPs 降低不是端到端时延；只在密集同类实例域验证；合并仍可能损伤细边界/小目标 |
| MoRSe | [2610.31209](https://arxiv.org/abs/2610.31209v1) · [项目页](https://kosmoresearch.github.io/MoRSe/) | 联合两帧预测“正在运动的区域”，区分相机诱导的表观运动；单 RGB 编码器，推理不需光流、点轨迹或独立掩码生成器；发布 MoRSe-5K（42 序列） | 运动是关系量而非实例属性；42 序列基准规模小；静态场景假阳性低不等于长期运动状态/因果理解；需要两帧，单帧不可判定 |
| OVS 区域语义细化 | [2610.30623](https://arxiv.org/abs/2610.30623v1) | 调整 CLIP 视觉编码器注意力以保留区域语义，并用置信 patch 组成视觉原型分类器缓解模态鸿沟；5 个语义分割数据集验证 | `L2` 开放词汇语义分割；没有实例 ID/追踪；原型记忆可能固化错误；CLIP 的区域-文本对齐仍受提示与词表影响 |

> 多视图全景分割的视图一致性指标 VC-PQ 属于评测方法，见[评测方向](evaluation-and-benchmarks.md#evaluation-frontier)。

#### SAM 3：概念提示把检测、分割与视频身份放进一个接口

- **一手来源：** [固定版本](https://arxiv.org/abs/2511.16719v2) · [官方代码](https://github.com/facebookresearch/sam3) · SA-Co 基准随论文发布。`PRIMARY_PAPER` / `OPEN_SOURCE`。
- **机制：** 双编码器-解码器：约 850M 参数（视觉约 450M、文本约 300M、检测器/追踪器约 100M）；以短名词短语、图像 exemplar 或其组合为 concept prompt；presence head 把“概念是否出现”与逐实例定位解耦；视频端沿用 SAM 2 的 masklet + 记忆库，并用高置信检测结果周期性重提示以纠正遮挡/干扰导致的漂移。
- **输入与学习来源：** 视觉/文本编码器用 5.4B 图文对做对比预训练（`L2`，PE 配方）；可扩展数据引擎分四阶段、人机协同产生 4M 唯一概念标签与 hard negatives（`L1`）；SA-Co/VIDEO 含 52.5K 视频、467K masklets。
- **实际证据：** 作者报告图像与视频 PCS 精度约为既有系统两倍；SA-Co 提供图像/视频概念分割评测；SAM 3 同时在 PVS 视觉分割上保留并改进 SAM 2 能力。
- **不能推出（作者自述）：** 对细粒度 OOD 概念（机型、医学术语）与 niche 域（热成像）零样本泛化弱；只支持简单名词短语，不支持多属性长指代表达（需外接 MLLM）；视频每目标一个 masklet，推理成本随目标数线性增长——30 FPS 需多 GPU（2×H200 约 10 目标、4×H200 约 28、8×H200 约 64）；多目标间无共享对象级上下文，概念/实例模式需硬切换。
- **阅读深度：** 正文选读：架构 §C、数据引擎 §D、Appendix B 局限与结论；未复核全部实验/附录；未运行复现。

### 追踪：点、框、掩码与物理实体是不同层次的“同一目标”

追踪文献最容易被误读的地方，是把**当前帧定位**、**跨帧关联**、**遮挡期间状态**和**重现后身份恢复**混成一个分数。下表把四者拆开；任何“实时”数字都必须连同初始化方式、目标数、记忆窗口和是否使用未来帧记录。

| 方法 | 一手来源 | 机制与可核查证据 | 边界与反假设 |
|---|---|---|---|
| TAPNext | [2504.05579](https://arxiv.org/abs/2504.05579v2) · [项目页](https://tap-next.github.io/) | 把任意点追踪写成因果的下一 token 掩码解码；无跟踪专用归纳偏置，纯在线、无需时间窗；作者报告在线/离线 SOTA 与低时延 | 已在别处单列；查询点初始化、短序列训练在 >150 帧退化（正文自述）；点轨迹不提供类别/物理实体状态 |
| MOTIP | [2403.16848](https://arxiv.org/abs/2403.16848v2) · [官方代码](https://github.com/MCG-NJU/MOTIP) | 把多目标关联写成 in-context ID 预测，直接为当前检测解码轨迹 ID；仅用对象级特征，无需手工代价矩阵 | `L1` MOT；依赖上游检测器；ID 预测闭合于训练类别/场景，开放世界新类别与长期重入另测；ID 号不是物理身份证明 |
| OmniTrack++ | [2511.00510](https://arxiv.org/abs/2511.00510v2) · [官方代码](https://github.com/xifen523/OmniTrack) | 全景 MOT：DynamicSSM 稳定全景特征，FlexiTrack 用轨迹反馈定位/关联，ExpertTrack MoE 记忆，Tracklet Management 在端到端与检测跟踪间切换；EmboTrack（QuadTrack/BipTrack）；报告 JRDB +3.94 HOTA、QuadTrack +15.03 | 360° 全景与机器人平台条件；仍需检测/关联与标定；MoE 记忆的长期身份恢复未与普通记忆在等成本下分离；不是纯单目 V0 |
| Cutie | [2310.12982](https://arxiv.org/abs/2310.12982v2) · [官方代码](https://github.com/hkchengrex/Cutie) | 对象级记忆读取：少量 object query 迭代读取像素特征，前景/背景掩码注意力分离语义；MOSE 比 XMem +8.7 J&F，比 DeAOT 快 3× | 半监督 VOS，需首帧掩码提示；对象 query 数量与内存随目标数增长；长期遮挡后的记忆污染未解决；掩码跟踪不等于物理实体理解 |
| SAM3RL | [2610.19931](https://arxiv.org/abs/2610.19931v1) · 正文选读 | 把 SAM3 记忆库的“哪些帧进入记忆”建模为序列决策，用轻量 RL 控制器学习；作者报告 12 个追踪/VOS 基准中 11 个提升、10 个第一，SAM2RL 在每个基准提升、9 个第一；几乎无运行时开销 | 策略绑定训练时的 5 FPS 决策率：在 30 FPS 全帧决策时平均增益从 2.9 降到 1.8 点，需预先知道帧率并按 stride 跳过帧；只控制 7 帧记忆库，9 个 object pointer 仍用固定规则；RL 奖励可能利用 benchmark 偏好；不是语义记忆 |
| ARROW | [2610.01314](https://arxiv.org/abs/2610.01314v1) | 前馈统一任意图像集的 3D 重建与 3D 点追踪；order-invariant querying 让查询跨视角/时刻关联；WorldTrack/TAPVid-3D SOTA，并在 RGB-only MVTracker 上优于专用多视图追踪器 | 训练依赖多视图/深度/位姿等监督；任意图像集仍需足够重叠与可见性；3D 点轨迹不是语义对象身份；动态/非刚性条件下的物理状态未闭合 |
| TrackFlood | [2609.33948](https://arxiv.org/abs/2609.33948v1) | 证明 NMS-free 只把延迟攻击面从检测器转移到关联器：在 YOLOv10/YOLO26/RT-DETR 后接跟踪器，优化扰动注入空间分布 phantom detections；Jetson AGX Orin TensorRT FP16 上检测时延基本不变、跟踪时延显著上升；8/255 仅温和端到端减速，更高预算造成截止违约 | 白盒威胁模型与特定跟踪器；未覆盖所有 NMS-free 家族；防御性 bounded-admission 会牺牲干净检测；说明“检测器快”不等于“系统实时安全” |

> 多视图 3D 点追踪基准 TAPVid-MV 的协议与真值来源见[评测方向](evaluation-and-benchmarks.md#evaluation-frontier)；2026 年 2D/3D/`SE(3)` 点追踪的专门比较见[任意点追踪与 3D 运动](#point-tracking-2026)。

#### SAMURAI：不改权重，用运动先验修正 SAM 2 的记忆选择

- **一手来源：** [固定版本](https://arxiv.org/abs/2411.11922v2) · [项目页](https://yangchris11.github.io/samurai/) · [官方代码](https://github.com/yangchris11/samurai)。`PRIMARY_PAPER` / `OPEN_SOURCE`。
- **机制：** 在 SAM 2 多掩码输出上加入 Kalman 运动模型，以 KF-IoU 与 mask affinity 加权选掩码；记忆库改为按 affinity、object 与 motion 混合评分选择，而不是固定窗口。
- **输入与学习来源：** 首帧框初始化，后续 RGB 视频；**不重训、不微调** SAM 2。SAM 2 原始训练数据/监督仍是上游来源，不能因“零样本适配”记为 `L0`。
- **实际证据：** 作者报告 LaSOT_ext AUC +7.1%、GOT-10k AO +3.5%，并在多套 SAM 骨干上一致提升；实时在线推理。
- **不能推出：** 线性 Kalman + 固定权重的运动先验在 abrupt/非刚性/多目标交叉下会失效；单目标 VOT 框初始化不是开放世界多目标发现；“实时”取决于 GPU 与 SAM 2 规模；遮挡期间轨迹是预测，不是观测到的实体位置。
- **阅读深度：** 正文选读：§3–4、结论与实现细节；未复核全部实验；未运行复现。

#### MOTIP2：端到端追踪的空间先验，优势与失败条件都被作者写明

- **一手来源：** [固定版本](https://arxiv.org/abs/2610.10391v1)（BMVC 2026）。`PRIMARY_PAPER`。
- **机制：** 在 MOTIP 的 ID 预测上加入数据阶段的空间 ID 交换偏置、损失阶段的距离加权 ID loss、表示阶段的 frame-position anchor；检测器换为实时 DEIM，推理保持端到端、无后处理关联。
- **输入与学习来源：** MOT 标注 `L1`，无额外数据；检测器预训练另记；空间先验使用框几何，不引入语言或物理监督。
- **实际证据：** MOTIP2-L 报告 DanceTrack 73.4 HOTA、SportsMOT 76.0、PersonPath22 71.1 IDF1；MOTIP2-S 以 3× 以上速度匹配原 MOTIP；MOTIP2-X 达 DanceTrack 74.8 HOTA。
- **不能推出：** 作者自述最难失败是“同一位置同时离开与进入”，邻近性会把离开身份吸附到新物体；收益依场景几何而变（宽拥挤场景数据先验更重要，外观相似时损失/表示先验更重要）；HOTA/IDF1 不证明物理身份。
- **阅读深度：** 正文选读：方法、结论与失败条件；未复核全部附录；未运行复现。

#### UGO： exemplar 条件下的通用多目标追踪，代价是语义粒度不可控

- **一手来源：** [固定版本](https://arxiv.org/abs/2609.37339v1)（NeurIPS 2026）。`PRIMARY_PAPER`。
- **机制：** 预训练 exemplar-conditioned 检测头 + 实例传播头共享架构；无需训练的能量最小化 consolidation 把重叠提议变成互斥像素掩码/检测；全局+实例层级记忆改善召回与每实例分割。
- **输入与学习来源：** 首帧单个类别 exemplar；检测/分割预训练与 GMOT 标注 `L1`；不使用文本类别名，因此类别粒度由视觉 exemplar 决定。
- **实际证据：** 作者报告 GMOT 基准与视频计数 SOTA，并与专用 MOT 竞争；AnimalTrack 上比 SAM3 HOTA +14%、MOTA +23%（正文表）；MOT17 上 HOTA 优于 MOT 基线但落后于域内微调 SOTA。
- **不能推出：** 作者自述 FP 较高，MOTA 比 QDTrack 低约 3%；相似物种会被 exemplar 误纳；无法显式控制语义粒度（不能指定“某亚种”）；exemplar 选择改变任务定义；不是文本开放词汇。
- **阅读深度：** 正文选读：方法、AnimalTrack/MOT17 表、局限与结论；未复核全部附录；未运行复现。

#### When Trackers Fail：把“何时不该相信传播”变成显式模块

- **一手来源：** [固定版本](https://arxiv.org/abs/2610.15929v1)（NeurIPS 2026） · [项目页](https://valaybundele.github.io/Dual-Agent)。`PRIMARY_PAPER` / `OFFICIAL_PROJECT`。
- **机制：** Dual-Agent：VLM 验证 agent 在短时空上下文上判断当前预测是否仍跟随目标；失败时纠正 agent 用时间上下文恢复；纠正器在真实 SAM3 失败轨迹上训练，并加身份切换/干扰物扰动；带置信/可见性/位移门控的选择性提交。
- **输入与学习来源：** 传播器为 SAM3（另可换 SAM2.1/SeC/Cutie）；训练数据为 SA-V 上 SAM3 传播轨迹及失败标注 `L1`，验证/纠正含 VLM `L2`；不是纯视觉端到端训练。
- **实际证据：** LVOS-v2 +1.2 J&F、SecVOS +2.7 J&F；无需重训即可迁移到 SAM2.1、SeC、Cutie 及 LaSOT-ext/TNL2K/VOT-LT2022；作者给出失败类型分布与干预结果。
- **不能推出：** 作者明确：单 GPU 非实时，平均运行时不代表最坏干预延迟；错误验证/纠正会覆盖正确轨迹并污染后续记忆；门控没有形式安全保证；内窥等专用域未验证；无法核对基础模型预训练与评测视频重叠。
- **阅读深度：** 正文选读：方法、结论、附录 H 局限与失败统计；未复核全部实验；未运行复现。

<a id="point-tracking-2026"></a>

### 任意点追踪与 3D 运动：从像素轨迹到世界坐标 `SE(3)`

点追踪的“SOTA”至少分成四个不可互换的对象：**2D 像素轨迹**（TAP/AJ）、**相机坐标 3D 轨迹**（APD/EPE3D）、**世界坐标 3D 轨迹**（去掉相机自运动后的 APD），以及**每像素刚体变换**（`SE(3)` 的旋转、平移与分组）。同一篇论文可以在 2D 上领先、在 3D 上落后；可以在 median-scaled leaderboard 上落后、却在绝对米制上领先。下表把 2026 年可核查的一手工作按这四层拆开，并把“速度”连同基线、分辨率、帧长和是否包含 3D 基础模型一起记录。

| 方法 | 一手来源 | 机制与可核查证据 | 边界与反假设 |
|---|---|---|---|
| TAPFormer | [2603.04989](https://arxiv.org/abs/2603.04989v2) · 正文选读 | 帧-事件瞬态异步融合（TAF）+ 跨模态局部加权融合（CLWF）；帧间用连续事件更新，查询可在任意事件时刻解码；InivTAP/DrivTAP 平均 δ_avg^vis 65.0（CoTracker3 49.9、FETAP 50.7）；InivTAP AJ 57.0（CoTracker3 41.8、FETAP 42.2，+36.4%/+35.1%）、DrivTAP AJ 48.8；20.2 ms/时间步（CoTracker3 19.0）；9.375 FPS 输入下特征跟踪 FA 75.8 vs CoTracker3 13.2；自建真实集 δ_avg^vis 相对现有追踪器提升 28.2%（作者口径）；替换 VINS-Mono 前端后 SLAM AUC_v 6.29（SuperEvent 6.27、SDEVO 6.13） | 需要事件相机与帧-事件同步；合成事件由 v2e 生成，真实集仅 13 段（InivTAP 8 + DrivTAP 5），5 秒序列人工标注约 2 小时；SLAM 对比仍用 IMU，不是纯视觉；事件流不提供类别/物理身份 |
| M2P | [2603.17813](https://arxiv.org/abs/2603.17813v1) · 正文选读 | 用 VOS 掩码做弱监督：局部结构一致性（Procrustes）、掩码标签一致性、边界约束；仅约 3.4K 段 VOS 视频（摘要写 3.6K）、2×RTX 4090 约 1 天；TAP-Vid-DAVIS first-query δ_avg^x 从 DINOv2-B/14 的 38.0 升到 50.8（+12.8），DINOv3-B/16 从 38.9 升到 53.5（+14.6）；作为 Chrono 骨干 δ_avg^x 在 DAVIS first-query 69.3 vs 68.0、Kinetics strided 67.7 vs 66.8；test-time M2P-Tracker 0.5M 可学参数、0.7 h/视频（DINO-Tracker 7.6M、0.9 h；作者报告 15× 更少参数、22% 更快训练） | 只在 LoRA 容量与 3.4K 掩码视频上验证，未扩到 SA-V 级；掩码边界监督仍假设视频对象分割质量；下游增益多为 0.5–1.3 点，不能把骨干提升当追踪器 SOTA；长时遮挡与重现未单独闭合 |
| 3D Point Tracking with SSM | [2609.34035](https://arxiv.org/abs/2609.34035v1) · [官方代码](https://github.com/MasahiroOgawa/vmamba3-3Dpointtracker) · 正文选读 | 冻结稠密光流 + 冻结单目米制深度，只学“沿像素射线的深度残差”；Mamba-3 非因果状态空间（VSSD-2pool）+ DINOv3 外观条件 + 深度尺度稳定 + 可见性头；TAPVid-3D minival 绝对米制 AJ 0.256（最强外部前馈 0.183，DELTA 族），但 median-scaled leaderboard 0.121（加可见性头 0.102）仍低于 DELTA+ 0.141；0.44–0.79M 可学参数、6–12 FPS、RTX 4080 Laptop 12GB、训练 9.5 h | 需要相机内参；pose-free 不等于 calibration-free；在 TAPVid-3D full_eval 上训练、minival 上测试，属同基准分布而非零样本；DA3-l 有远场偏置、DA3-g 有逐帧尺度闪烁，单目深度误差直接进入米制结果；可见性头改善绝对米制却拉低归一化 leaderboard；未覆盖动态非刚体与开放语义 |
| Track4World | [2603.02573](https://arxiv.org/abs/2603.02573v2) · 正文选读 | VGGT 式全局 3D 表征 + 稀疏到稠密场景流解码器 + 2D-to-3D 相关，避免昂贵 3D kNN；一次前向跟踪全部像素；世界坐标 APD 平均 0.5636/0.5323（L-16/L-50），优于 V-DPM 0.5142/0.4668、POMATO 0.4357/0.4094、STV2 0.2470/0.2335；2D AJ Kinetics 59.1 vs CoTracker3 55.8、RoboTAP 70.9 vs 66.4、RGB-S 78.2 vs 71.7；16 帧 ADT 稠密追踪 3.4 s/14 GB/26.06M 参数（POMATO 4.8 s/16 GB/133.64M，STV2 稠密 OOM） | 依赖 4D 运动数据训练（8×40GB GPU，第一阶段约一周），作者自述极端姿态/拓扑变化会失败；世界坐标精度受相机位姿与几何估计约束；稠密全像素输出不等于对象身份或语义；未给端侧/在线速度 |
| MoSE3 | [2610.03716](https://arxiv.org/abs/2610.03716v1)（NeurIPS 2026 Spotlight） · 正文选读 | 首个前馈单目每像素世界坐标 `SE(3)`：π³ 冻结几何 + 可训练跟踪分支，联合预测 3D 点轨迹与刚性嵌入，再用可微 Horn/Procrustes 闭式拟合变换；HO3D 每像素 RRE 18.28°、ADD 2.16 cm、AUC_r 0.569、AUC_ADD 0.785（最强基线 Track4World-Pi3x 33.21°/3.37 cm/0.371/0.669）；iTACO 12.30°/11.37 cm/0.741/0.594；对象/部件 IoU 0.709/0.784；3D 跟踪平均 APD 0.5941/0.5946，略高于 Track4World 0.5847/0.5402；发布 Art-Kubric 5,000 场景、163M 轨迹 | 依赖 π³ 的相机位姿与点图拟合内参，几何误差直接传播；快速运动下轨迹/刚性嵌入退化；可变形场景只有定性结果；64×H100 训练，未给统一硬件吞吐；`SE(3)` 是运动分组，不是材质、质量或因果状态 |
| CoWTracker | [2602.04877](https://arxiv.org/abs/2602.04877v1) · [项目页](https://cowtracker.github.io) · 摘要/正文表 | 用“warp 特征”替代 cost volume，避免空间分辨率二次复杂度；迭代 refine + 全轨迹时空 transformer；TAP-Vid 平均 AJ 71.3（AllTracker 68.9、CoTracker3-offline 62.0）；H100 上 ≤40 帧约 6–7M 点/秒、>30 FPS，长视频约 3.5M 点/秒、近 20 FPS | 整体吞吐受 VGGT 骨干二次复杂度支配；作者自述极端视角、长时全遮挡、强高光会失败；稠密全像素查询的显存/算力仍非端侧；不输出 3D 或对象身份 |
| Track-On-R（Verifier） | [2603.12217](https://arxiv.org/abs/2603.12217v1) · [项目页](https://kuis-ai.github.io/track_on_r) · 摘要/正文表 | 用 meta-verifier 逐帧评估多个教师轨迹的可靠性，选最可信者生成伪标签；8K 真实视频微调，教师含 Track-On2、BootsTAPNext、BootsTAPIR、CoTracker、Anthro-LocoTrack；EgoPoints δ_avg^x 67.3 vs Track-On2 61.7、RoboTAP 82.6 vs 80.5、Kinetics 71.0 vs 69.3、DAVIS 80.3 vs 79.9；Kinetics AJ 68.1 vs 67.0（+1.1） | 上界受教师质量约束；需要 curated 真实视频集合；verifier 在 K-EPIC 合成数据上训练（11K 段、24 帧），长时漂移与遮挡重现仍靠教师；不是无监督物理/语义理解 |
| SynthVerse | [2602.04441](https://arxiv.org/abs/2602.04441v1) · [项目页](https://weiguangzhao.github.io/SynthVerse/) · 摘要/数据表 | 面向点追踪的大规模合成数据：5,816K 训练帧、59K 测试帧、48K 序列；约 1K 关节物体、6K 可变形物体、75 动物、4K 人体序列；Blender + Isaac Sim 双管线，支持自我中心/异中心视角；微调 TAPIP3D 在 Dynamic Replica、LSFOdyssey 上一致改善 | 仍是合成数据，渲染/物理/材质与真实传感器有域差；以 2D/3D 轨迹监督为主，不含语义/物理属性；关节与可变形覆盖仍以类别/模板为限；数据规模不等于任务覆盖 |
| TrackCraft3R | [2605.12587](https://arxiv.org/abs/2605.12587v1) · [项目页](https://cvlab-kaist.github.io/TrackCraft3r) · 摘要/正文表 | 复用视频扩散 Transformer 的时空先验，双 latent + 时间 RoPE 把 frame-anchored 生成改成 reference-anchored 追踪；Sim(3) 对齐后平均 AJ 0.5639（ViPE 几何）/0.6785（DA3 几何），DELTAv2+DA3 0.4975；A6000、448² 下 12 帧快 1.3×、23 帧约 1.24×，峰值显存少 4.6–4.7×；8×H200 两阶段训练 | 精度受外部深度/位姿上界约束；视频 DiT 的“快”是相对迭代式 DELTAv2、短片段与特定分辨率；另一篇独立评测（3D SSM）报告其视频扩散骨干比 flow+depth 管线慢约 200×——速度声明必须连同基线/分辨率/帧长读；未闭合语义与物理状态 |
| TrackerSplat | [2604.02586](https://arxiv.org/abs/2604.02586v1)（SIGGRAPH Asia 2025） · [官方代码](https://github.com/yindaheng98/TrackerSplat) · 摘要/正文表 | 用现成点追踪提取像素轨迹并三角化到 3D Gaussian，初始化高斯的重定位、旋转与尺度，再做动态 3DGS 训练；1/2/4/8 GPU 并行下多数场景视觉质量优于基线，多数设置吞吐更高（个别数据集的追踪开销会抵消收益） | 小/薄物体、抖动、误差累积与遮挡仍失败；追踪错误会直接写入高斯初始化；PSNR/SSIM 是渲染质量，不是轨迹正确性；依赖多视图/相机与 3DGS 训练管线 |

> 2D、3D 与世界坐标的协议差异见[评测方向](evaluation-and-benchmarks.md#evaluation-frontier)；多视图 3D 点追踪基准 TAPVid-MV 另见同页。

#### TAPFormer：用事件补上帧间空白，但“纯视觉”边界变成“帧+事件”

- **一手来源：** [固定版本](https://arxiv.org/abs/2603.04989v2) · [项目页](https://tapformer.github.io/)。`PRIMARY_PAPER` / `OFFICIAL_PROJECT`。
- **机制：** 每个图像帧与曝光窗口内的事件融合，TAF 用连续事件更新查询点的瞬态特征，使查询可在事件时刻解码；CLWF 按模态可靠性调整空间注意力，避免同步融合在一种模态失效时整体崩溃。
- **输入与学习来源：** RGB 帧 + 事件流（`L0` 传感器原始信号）；训练集 FE-FastKub 为 Kubric 48 FPS 渲染、v2e 合成事件，10,953 段、每段 96 帧、1,024 条轨迹；真实评测集为 DAVIS346 的 InivTAP 与自建 Prophesee EVK4 + RGB 同步系统的 DrivTAP。
- **实际证据：** InivTAP/DrivTAP 平均 δ_avg^vis 65.0，优于 CoTracker3 49.9 与 FETAP 50.7；InivTAP AJ 57.0，相对 CoTracker3 41.8 / FETAP 42.2 提升 36.4%/35.1%，DrivTAP AJ 48.8；20.2 ms/时间步，和帧基线同一量级；在 9.375 FPS 低帧率输入下特征跟踪 FA 仍得 75.8，CoTracker3 降到 13.2，说明事件确实补了帧间信息；替换 VINS-Mono 前端后 SLAM AUC_v 6.29。
- **不能推出：** 这不是“单目 RGB”系统：需要事件相机、帧-事件时间同步与标定；真实集只有 13 段、每段 5–10 秒，5 秒人工标注约 2 小时；合成事件与真实事件仍有域差；SLAM 实验仍用 IMU，AUC 提升不能归因于纯视觉几何；点轨迹仍无类别/对象身份。
- **阅读深度：** 正文选读：方法 §3、TAP/特征追踪 §5.2–5.3、消融 §5.4、SLAM 附录 §10、数据附录 §11；未复核全部补充实验；未运行复现。

#### M2P：把“视频分割掩码”变成点追踪的弱监督，但增益是骨干级而非系统级

- **一手来源：** [固定版本](https://arxiv.org/abs/2603.17813v1)。`PRIMARY_PAPER`。
- **机制：** 在掩码内采样查询点，用 Procrustes 对齐约束局部结构的一致性运动；掩码标签一致性要求前景点跨帧仍落在前景；边界约束专门监督靠近掩码边界的点。三者都是弱监督，不需要逐点真值轨迹。
- **输入与学习来源：** DAVIS-2017 + YouTube-VOS 的 VOS 掩码（正文 3.4K 段，摘要写 3.6K）；LoRA 微调 DINOv2/DINOv3 骨干；2×RTX 4090 约 1 天；下游分别接 Chrono 离线微调与 DINO-Tracker 式 test-time optimization。
- **实际证据：** TAP-Vid-DAVIS first-query δ_avg^x：DINOv2-B/14 38.0→50.8（+12.8），DINOv3-B/16 38.9→53.5（+14.6）；组件消融从 +11.0 递增到 +12.8，说明三项约束各有贡献但主要收益来自“把静态骨干变成时序可匹配”。接 Chrono 后 DAVIS first-query 69.3 vs 68.0、Kinetics strided 67.7 vs 66.8；test-time 版本用 0.5M 可学参数、0.7 h/视频（DINO-Tracker 7.6M、0.9 h；作者报告 15× 更少参数、22% 更快训练）。
- **不能推出：** 下游提升只有 0.5–1.3 点，不能把骨干的 +12.8 直接当作追踪器 SOTA；只在 3.4K 掩码视频与 LoRA 容量下验证，作者自述应扩到 SA-V 与更大容量；掩码质量、边界标注与半监督 VOS 的域假设仍在；长时遮挡/重现没有单独消融；方法不输出 3D。
- **阅读深度：** 正文选读：方法 §III、VFM 比较 §IV-A、下游 §IV-B–C、消融 §V、局限 §VI；未复核补充材料；未运行复现。

#### 3D Point Tracking with SSM：绝对米制与 leaderboard 是两场不同的比赛

- **一手来源：** [固定版本](https://arxiv.org/abs/2609.34035v1) · [官方代码](https://github.com/MasahiroOgawa/vmamba3-3Dpointtracker)（*Computer Vision and Image Understanding* 投稿格式）。`PRIMARY_PAPER` / `OPEN_SOURCE`。
- **机制：** 把 3D 追踪拆成“2D 轨迹已定，只剩沿像素射线的深度”这一条件问题：冻结 SEA-RAFT 光流给 2D 对应，冻结 DA3 给米制深度，只训练一个小于 1M 参数的 Mamba-3/VSSD 残差修正器；另加逐帧深度尺度稳定器与仅看前向/后向光流的可见性头。状态空间沿每条轨迹的时间轴混合，显存不随帧数线性增长。
- **输入与学习来源：** 单目 RGB + 相机内参；光流、DA3、DINOv3 全部冻结；训练数据为 TAPVid-3D 的 `full_eval` 4,419 段，测试 `minival`，两 split 不重叠；训练 9.5 h/RTX 4080 Laptop 12GB；无 GT 位姿，但需要内参。
- **实际证据：** 绝对米制 AJ 0.256，最强外部前馈 0.183；但 median-scaled leaderboard 只有 0.121（加可见性头 0.102），低于 DELTA+ 的 0.141——作者主动报告这个反转，而不是只报对自己有利的指标。消融显示 VSSD-2pool 把绝对 AJ 从 0.248 提到 0.255；DA3-g 更大却在近场逐帧尺度闪烁，DA3-l 更稳但有远场偏置。52–66% 的 GT 点会重现，而原 latch 规则一个都恢复不了；可见性头允许逐帧重新判定可见，但会拉低归一化分数。
- **不能推出：** “pose-free”不等于“calibration-free”：像素反投影需要 `fx/fy/cx/cy`；训练与测试同属 TAPVid-3D，不能称跨基准零样本；单目深度误差是系统性上界，深度骨干换大反而更差；绝对米制 AJ 0.256 仍远低于可用机器人操作阈值；未覆盖非刚体、透明/反光与开放语义。
- **阅读深度：** 正文选读：方法 §3、评测 §4、DA3-l/g 讨论 §5.1、外部方法预算分析 §5.2、结论 §6；未复核全部附录；未运行复现。

#### Track4World：一次前向跟踪所有像素，但“世界坐标”仍由外部几何定义

- **一手来源：** [固定版本](https://arxiv.org/abs/2603.02573v2) · [项目页](https://jiah-cloud.github.io/Track4World.github.io/)。`PRIMARY_PAPER` / `OFFICIAL_PROJECT`。
- **机制：** 用 VGGT 式 ViT 编码全局 3D 场景（点图、相机位姿、几何特征），再用稀疏到稠密场景流解码器在任意帧对之间回归 2D/3D 联合流；关键是 2D-to-3D 相关：先在 2D 上建立对应，再把候选提升到 3D，避免对每个查询做 3D kNN。任意帧对的流可组合成任意像素的世界坐标轨迹。
- **输入与学习来源：** 单目视频；训练混合 2D 点追踪、光流、场景流与 3D 点追踪数据（Kubric、PointOdyssey、DynamicStereo 等），8×40GB GPU，第一阶段 100K 步约一周；默认 DA3 初始化几何骨干。
- **实际证据：** 世界坐标 APD 平均 0.5636（L-16）/0.5323（L-50），优于 V-DPM 0.5142/0.4668、POMATO 0.4357/0.4094、STV2 0.2470/0.2335；2D 分支在 Kinetics/RoboTAP/RGB-S 的 AJ 为 59.1/70.9/78.2，均高于 CoTracker3 的 55.8/66.4/71.7；16 帧 ADT 稠密追踪 3.4 s、14 GB、26.06M 参数，POMATO 为 4.8 s、16 GB、133.64M，STV2 稠密直接 OOM。
- **不能推出：** 训练依赖带 4D 运动的数据，作者自述极端姿态与拓扑变化会失败；世界坐标精度受相机位姿/深度上界约束；全像素稠密输出不等于对象级身份或物理状态；3.4 s/16 帧不是在线速度；2D 分支的领先不能自动推出 3D 语义理解。
- **阅读深度：** 正文选读：方法 §3、场景流/2D/3D 评测 §4.1–4.3、效率表 §4.6、局限附录 K；未复核全部补充材料；未运行复现。

#### MoSE3：从“点去哪了”推进到“哪块刚体怎么转”，但仍不是物理状态

- **一手来源：** [固定版本](https://arxiv.org/abs/2610.03716v1)（NeurIPS 2026 Spotlight） · [项目页](https://mose3-tracker.github.io/)。`PRIMARY_PAPER` / `OFFICIAL_PROJECT`。
- **机制：** 不直接回归 `SE(3)`，而是预测两条更易学的中间量：每个像素的世界坐标 3D 轨迹，以及 L2 归一化的刚性嵌入；在同一刚性簇内用加权 Horn/Procrustes 闭式拟合每像素变换，使旋转、平移与“哪些像素一起动”同时出现。π³ 几何分支冻结，只训练跟踪分支；内参由 π³ 点图逐视频拟合，推理不需要 GT 内参。
- **输入与学习来源：** 单目 RGB；训练数据 Art-Kubric：5,000 个 512×512、120 帧、60 FPS 的关节物体场景，含 163M 轨迹、逐链接 `SE(3)`、逐像素刚性分区与物理交互；64×H100-80GB、200 epochs、有效 batch 64；推理不需要深度传感器或逐视频优化。
- **实际证据：** HO3D 每像素 RRE 18.28°、ADD 2.16 cm、AUC_r 0.569、AUC_ADD 0.785，优于最强基线 Track4World-Pi3x 的 33.21°/3.37 cm/0.371/0.669；iTACO 12.30°/11.37 cm/0.741/0.594；对象/部件级 IoU 0.709（HO3D）/0.784（iTACO）；3D 跟踪平均 APD 0.5941/0.5946，略高于 Track4World 0.5847/0.5402，但在 ADT L-16 上排第二。
- **不能推出：** 依赖 π³ 的相机位姿与点图拟合内参，几何误差会传播；作者自述快速运动下轨迹与刚性嵌入退化；可变形场景只有定性结果；64×H100 的训练成本与未报告的推理吞吐使其离“原生超快”很远；`SE(3)` 分组是运动学结构，不是材质、质量、可操作性或因果状态；刚体假设对布料、液体、手部等非刚体不成立。
- **阅读深度：** 正文选读：方法 §3、Art-Kubric §4、SE(3)/3D 跟踪评测 §5.1–5.2、局限 §6；未复核全部附录与补充视频；未运行复现。

**本节结论：** 2026 年的点追踪已经能把“同一像素/同一刚体去哪了”做得相当强，但它给出的是**对应与运动学**，不是 Clover 需要的广义世界理解。四条边界必须同时写进验收：

1. **度量层级：** 2D AJ、相机坐标 APD、世界坐标 APD、绝对米制 AJ、`SE(3)` RRE 不是同一分数。3D SSM 的绝对米制领先与 leaderboard 落后同时成立，正是“尺度不变指标会奖励错误尺度”的直接证据。
2. **速度声明：** TrackCraft3R 相对 DELTAv2 的 1.3× 加速与 3D SSM 报告的“视频扩散骨干慢约 200×”并不矛盾，但说明速度必须绑定基线、分辨率、帧长、硬件和是否包含几何前端；单看“比某方法快”不能推出端侧可用。
3. **数据来源：** TAPFormer 需要事件相机，M2P 依赖 VOS 掩码，3D SSM 需要内参并在 TAPVid-3D 内训练/测试，MoSE3 依赖 π³ 几何与 64×H100 合成数据；没有一条同时满足纯 RGB、无标定、零样本、动态开放世界、语义身份与端侧实时。
4. **理解层级：** 点轨迹能支持“它还在、它移到哪”，3D 轨迹能支持“它在世界中的位置”，`SE(3)` 能支持“它作为刚体怎么转”；但“它是什么、能不能抓、被挡住是否仍存在、下一步会怎样”仍要由对象身份、可供性、物理与因果模块补齐。Clover 若把追踪作为世界理解的入口，必须把**轨迹精度、尺度正确性、失败/漂移检测、对象身份、物理状态、端侧成本**分开验收，不能用 AJ 或 APD 的单点 SOTA 替代。

<a id="object-pose-tracking-2026"></a>

### 物体级 6-DoF 状态：位姿跟踪、遮挡恢复与关节物体

点追踪回答“像素去哪了”，物体级 6-DoF 追踪回答“**哪一个物体、以什么姿态、是否还在视野里、失败后能否恢复**”。这一步必须引入对象假设：实例 CAD、类别形状先验、生成式补全，或手-物交互线索。下表把 2026 年可核查的工作分成三类：**实例模型跟踪**（RoPT、Robust Recovery）、**无人工 CAD 的新物体跟踪**（GRC-Pose、ComPose、Event6D、Event Fusion）、**类别级/关节物体状态估计**（ASM-6D、LEGAU、DICArt、OCH3R）。第三类多为单帧估计，不是时序跟踪；把它放进同一张表，是为了区分“物体状态估计”与“物体状态跟踪”。

按观察协议：ComPose/GRC-Pose 是 RGB（`V0`），RoPT/Robust Recovery/ASM-6D/LEGAU 是 RGB-D（`V1`），Event6D/Event Fusion 是事件（+深度，`V0-E`），DICArt 是点云（`V1`）；学习来源全部含 `L1`–`L3` 上游（CAD/类别先验/基础模型/合成数据），没有一条是 `L0` 从零纯视觉。

| 方法 | 一手来源 | 机制与可核查证据 | 边界与反假设 |
|---|---|---|---|
| RoPT | [2610.28962](https://arxiv.org/abs/2610.28962v1) · 正文选读 | RGB-D + 精确 CAD；EdgeTAM 掩码跟踪 + `SE(3)` 因子图 + 多假设验证 + Mast3R 失败重定位；YCBInEOAT 16× 帧降采样下 ADD 90.85 / ADD-S 94.55（FoundationPose 38.87/42.00，FoundationPose++ 67.37/79.55）；18.6 FPS（53.7 ms） | 需要精确 CAD 与 RGB-D；作者自述不适用于可变形、透明、镜面物体；遮挡超过运动预测视野后目标可能漂出多假设搜索半径，无法自恢复；速度低于 FoundationPose 的 42.9 FPS |
| GRC-Pose | [2609.39116](https://arxiv.org/abs/2609.39116v1) · 正文选读 | 无人工 CAD/参考视图/位姿标注；用 SAM3D 生成 CAD + VGGT 场景证据，GeoCorr-Matcher 估计带不确定性的物体-场景对应，FGH-Solver 做多鲁棒估计与序列后验，后验门控记忆只保留 inlier 支持；HOT3D 运动保持率 +58%；YCBInEOAT ADD 41.2 / ADD-S 67.0，LINEMOD ADD-S AUC 86.1 | “prior-free”仅指无人提供的实例 CAD；仍依赖 SAM3D 生成 CAD 与 VGGT-Ω 代理深度。后验模块 1.202 ms/帧（831.9 FPS，A100）但支撑构建 2.061 s/帧、序列自适应 27.23 s，摊销后端到端仅 0.79 FPS；上游 SAM3D/VGGT 不计入该延迟 |
| ComPose | [2605.23523](https://arxiv.org/abs/2605.23523v1) · 正文选读 | RGB-only、手感知：不把手只当遮挡物，而是从物体与手部基础模型中选择信息量高的手关节，融合物体/手部运动线索，再用可见几何与学习修正；SAM3 掩码 + SAM3D-Object 初始化，无需 CAD/深度；DexYCB RRE 1.5°、HO-3D v2 2.4°、OakInk 2.4° | 物体几何与手部线索同时不可靠时失败（严重遮挡、运动模糊、低质量图像）；未见过的抓握分布会选错手关节；锚点策略降低累计旋转漂移但长序列仍有残差；训练域为 DexYCB S3 + HOI4D |
| Robust Recovery | [2607.23468](https://arxiv.org/abs/2607.23468v1) · [官方代码](https://github.com/Bazs/robust-6d-object-pose-tracking) · 正文选读 | 模型-based RGB-D：纹理关键点匹配 + 优化对齐；可靠性检查检测发散/遮挡，全局重检测并验证候选后恢复；57.6 FPS；相对“关闭恢复”的消融提升 32.77 ADD AUC / 30.55 ADD-S AUC；六段自采序列只进入恢复 7 次，10.74% 帧处于恢复 | 恢复依赖跟踪开始后已见过的纹理视角；未见视角/无纹理对称物体弱；需要物体 3D 模型与 RGB-D；恢复帧的输出被冻结 6 帧以对齐 30 FPS 延迟 |
| ASM-6D | [2610.15287](https://arxiv.org/abs/2610.15287v1) · 正文选读 | RGB-D 类别级 Active Shape Model：生成完整相机系对应流图（含遮挡点），与固定索引 ASM 共享点身份；解析消去平移/形状系数后做九变量缩放旋转优化，批量 ADMM + 全局最优性证书；ROPE IoU50 AUC 30.95（RFMPose 21.0），HouseCat6D 85.7 IoU50，RealNOCS 73.7% 156 类先验选择；6–38 Hz；高运动 mug 序列 ADD 1.56 cm（FoundationPose 62.12 cm） | 类别级先验，不是实例 CAD；RGB-D 输入；单帧估计 + 逐帧拟合，不是原生时序跟踪；类别/形状先验覆盖决定上界；遮挡与旋转对称仍有歧义；最快 38.85 Hz 只在最低预算/已知单类别设置 |
| Event6D | [2603.28045](https://arxiv.org/abs/2603.28045v2) · 摘要/正文表 | 事件 + 深度，新物体 6D 跟踪；在深度帧之间重建任意时刻强度与深度，条件于最近深度；>120 FPS；训练集 EventBlender6D（495,840 样本、1,033 物体），真实 Event6D（54,556 样本、14 物体）；30 FPS 对齐下 cracker ADD 65.88 vs FoundationPose 34.33 | 需要事件相机 + 深度；训练完全合成，真实集仅 14 物体；120 FPS 下 RGB/RGB-D 基线无法直接评测，跨模态比较需对齐到 30 FPS；事件+深度不是纯 RGB |
| Event Fusion | [2603.08264](https://arxiv.org/abs/2603.08264v2) · 摘要/正文表 | 无学习、事件-only：事件光流给 6D 物体速度做传播，模板局部修正，UKF 平滑；静态相机；平移 RMSE 2.18 cm、旋转 14.57°（无 UKF 2.43 cm/15.50°） | 需要物体模板；假设静态相机与静态背景；事件-only 不提供外观/语义；快速运动外推与模板漂移仍是问题；无大规模真实基准 |
| LEGAU | [2609.35046](https://arxiv.org/abs/2609.35046v1) · 摘要/正文表 | RGB-D 类别级位姿+形状：联合预测 NOCS、位姿/尺寸与规范 Semantic Gaussian Field；Gaussian 场作为类别条件结构先验参与多模态融合；HouseCat6D 57.4（10°/5cm）、IoU50 80.6；SOPE VUS@10°5cm 44.2；形状 Chamfer-L1 6.72×10⁻³（AdaPoinTr 23.17） | 单帧类别级估计，不是跟踪；需要 RGB-D 与类别先验；CLIP 文本嵌入引入语言监督；遮挡/透明仍靠生成先验；时序一致性未闭合 |
| DICArt | [2602.19565](https://arxiv.org/abs/2602.19565v2) · 摘要/正文表 | 点云类别级关节物体位姿：把位姿估计写成条件离散扩散，逐 token 去噪/重置，层级运动学耦合逐刚体估计；Drawer 旋转 1.7°/平移 0.072 m（连续扩散 3.1°/0.143 m）；ReArtMix 多类别优于 ReArtNet | 输入为部分点云，不是纯 RGB；单观测估计，不是时序跟踪；关节类型/运动学结构由类别先验给定；真实 RGB-D 仅作评测；未覆盖可变形/多物体交互 |
| OCH3R | [2605.13018](https://arxiv.org/abs/2605.13018v2) · 摘要/正文表 | 单张 RGB 一次前向：每像素 CLIP 类别嵌入、米制深度、NOCS、每物体固定数 3D Gaussian，同时输出所有实例的 6D 位姿与详细重建；PACE Chamfer 0.18（Gen3DSR 0.31、AoE 0.35），F-1 45.00（AoE 21.39）；YCB-V 0.17 CD / 22.71 F-1 | 单帧、非跟踪；依赖合成/标注训练与类别/深度监督；遮挡与透明仍是失败面；输出是物体几何/位姿，不是材质、质量、可供性 |

> 点级 3D 轨迹与每像素 `SE(3)` 见[任意点追踪与 3D 运动](#point-tracking-2026)；在线相机状态与地图见[空间状态](#spatial-state-2026)。

#### RoPT：闭环恢复把“快速运动”从灾难性失败变成可恢复失败

- **一手来源：** [固定版本](https://arxiv.org/abs/2610.28962v1)。`PRIMARY_PAPER`。
- **机制：** 四个模块串成闭环：EdgeTAM 跟踪物体掩码以处理部分/严重遮挡；`SE(3)` 因子图约束帧间更新并前向预测，驱动并行多假设验证绕过局部极小；球谐光照优化缩小合成-真实光度差；Mast3R 在可靠性检查触发时做全局重定位，验证候选后再恢复跟踪。
- **输入与学习来源：** RGB-D + 数据集提供的精确 CAD（`L1` 几何先验）；零样本跟踪、不在 CAD 上微调；掩码/匹配/重定位各自依赖预训练基础模型（`L2`），不是纯视觉端到端训练。
- **实际证据：** 在把 YCBInEOAT 帧率降采样 16×（平均每帧 23.2 mm 平移、5.8° 旋转）后，RoPT 的 ADD 90.85 / ADD-S 94.55，远高于 FoundationPose 38.87/42.00 与 FoundationPose++ 67.37/79.55；消融显示自恢复模块把全表平均 ADD 从 81.68 拉到 90.85。代价是 53.7 ms/18.6 FPS，低于 FoundationPose 的 23.3 ms/42.9 FPS。
- **不能推出：** 需要精确 CAD 与 RGB-D；可变形、透明、镜面物体不在适用范围；遮挡超过运动预测视野后目标可能漂出多假设搜索半径；18.6 FPS 不是端侧实时；“恢复成功”是几何位姿恢复，不是对象身份/物理状态恢复。
- **阅读深度：** 正文选读：方法 §3、YCBInEOAT 表 1–3、真实机器人 §4.3、局限 §5；未复核全部附录；未运行复现。

#### GRC-Pose：把“无 CAD”拆成生成 CAD 与重建证据的对应，但端到端仍慢

- **一手来源：** [固定版本](https://arxiv.org/abs/2609.39116v1)。`PRIMARY_PAPER`。
- **机制：** 用 SAM3D 生成物体 CAD、VGGT 提供场景几何；GeoCorr-Matcher 在“生成 CAD 的物体局部参数化”和“重建证据的序列世界系”之间建立带不确定性的对应；FGH-Solver 用多个鲁棒几何估计器与序列级后验选位姿；后验门控表面记忆只保留 inlier 支持的观测，穿遮挡/视角变化传播。
- **输入与学习来源：** 单目 RGB 视频；无人提供 CAD、参考视图或位姿标注；但 SAM3D、VGGT、DINOv3 等基础模型与生成 CAD 是上游 `L2` 先验；序列自适应在测试时用记录局部自监督（`L3`）。
- **实际证据：** HOT3D 上运动保持率相对此前最好提升 58%；YCBInEOAT ADD 41.2 / ADD-S 67.0，LINEMOD ADD-S AUC 86.1；消融显示去掉位姿条件对应、后验门控或序列自适应都会降。后验只有 1.27M 参数、1.202 ms/帧（831.9 FPS，A100），但支撑构建 2.061 s/帧、序列自适应 27.23 s，摊销后 1.269 s/帧（0.79 FPS）。
- **不能推出：** “prior-free”不是“无先验”：生成 CAD 仍是对象特定模型，SAM3D/VGGT 误差会传播；831.9 FPS 只是后验，不是端到端；需要每段视频约 27 s 自适应；YCBInEOAT/LINEMOD 只是“有竞争力”，不是全面 SOTA；单目 RGB 的尺度仍由上游深度/生成模型锚定。
- **阅读深度：** 正文选读：方法 §3、HOT3D/YCBInEOAT/LINEMOD 表 1、阶段延迟表、结论 §5；未复核全部附录与消融；未运行复现。

#### ComPose：把手从遮挡物变成运动线索，但“信任手”本身没有保证

- **一手来源：** [固定版本](https://arxiv.org/abs/2605.23523v1)。`PRIMARY_PAPER`。
- **机制：** 物体与手部基础模型分别给出运动候选；ComPose 自适应选择信息量高的手关节，融合物体/手部线索估计物体运动，再用可见几何与学习修正；对旋转和平移同时加 temporal consistency，输出平滑轨迹；SAM3 掩码 + SAM3D-Object 首帧位姿/网格初始化。
- **输入与学习来源：** 单目 RGB，无 CAD、无深度；训练 DexYCB S3 + HOI4D（`L1` 手-物标注），评测 DexYCB、HO-3D v2、OakInk-v1 跨数据集；基础模型（SAM3、SAM3D-Object、手部模型）是上游 `L2`。
- **实际证据：** DexYCB RRE 1.5° / RTE 0.6，HO-3D v2 2.4° / 0.3，OakInk 2.4° / 1.2；TCC_R 分别为 0.55/0.41/0.19，说明跨数据集时序相关性明显下降；在 Franka Panda 上用 30 Hz 轨迹流做画笔任务，验证轨迹可迁移。
- **不能推出：** 物体几何与手部线索同时不可靠时失败（严重遮挡、运动模糊、低质量图像）；未见过的抓握分布会选错手关节；长序列仍有残差旋转漂移；TCC 0.19（OakInk）说明“平滑”不等于“跟对”；SAM3D-Object 初始化仍是对象特定先验。
- **阅读深度：** 正文选读：方法 §3、表 1、机器人应用 §4.3、局限；未复核补充材料；未运行复现。

#### Robust Recovery：恢复模块有效，但恢复依赖“以前见过”

- **一手来源：** [固定版本](https://arxiv.org/abs/2607.23468v1) · [官方代码](https://github.com/Bazs/robust-6d-object-pose-tracking)。`PRIMARY_PAPER` / `OPEN_SOURCE`。
- **机制：** 纹理关键点匹配（SIFT/SuperPoint）+ 优化对齐；可靠性检查监控位姿发散/遮挡；触发后做全局重检测与单帧位姿估计，验证候选后再恢复；关键帧存储保留已见视角。
- **输入与学习来源：** RGB-D + 物体 3D 模型；学习部分为关键点匹配器（`L1`/`L2`），几何对齐与恢复为优化；在 YCBInEOAT、Fast-YCB 与自采遮挡/快速运动数据上评测。
- **实际证据：** 57.6 FPS；相对关闭恢复的消融提升 32.77 ADD AUC / 30.55 ADD-S AUC；六段自采序列只进入恢复 7 次，10.74% 帧处于恢复（快速序列 6.58%、遮挡序列 14.65%）；在无纹理、旋转对称的 YCB-V mug 上最弱，但仍优于基线。
- **不能推出：** 恢复依赖跟踪开始后已见过的纹理视角；未见视角、无纹理/对称物体恢复弱；需要 3D 模型与 RGB-D；恢复延迟用冻结 6 帧对齐 30 FPS，不是零延迟；没有对象身份/语义恢复。
- **阅读深度：** 正文选读：方法 §3、恢复实验 §4.2、消融 §4.4、局限 §4.5；未复核全部附录；未运行复现。

#### ASM-6D：类别级位姿+形状可以很快，但它是“单帧估计 + 逐帧拟合”

- **一手来源：** [固定版本](https://arxiv.org/abs/2610.15287v1) · [项目页](https://asm6d-project.github.io/)。`PRIMARY_PAPER` / `OFFICIAL_PROJECT`。
- **机制：** 学习完整相机系对应流图，点身份与类别级 Active Shape Model 共享（含遮挡点）；每个对应假设直接拟合旋转、平移、米制尺度与实例形状；解析消去平移/形状系数，把拟合降为九变量缩放旋转，批量 ADMM + 全局最优性证书；假设/先验可并行评估。
- **输入与学习来源：** RGB-D ROI；类别级 ASM 先验（不是实例 CAD）；训练用合成 SOPE/HouseCat6D 等；推理不需要 mask 分割点云；跟踪实验是逐帧拟合 + 时序筛选，不是端到端时序模型。
- **实际证据：** ROPE IoU50 AUC 30.95（RFMPose 21.0）、HouseCat6D 85.7 IoU50、RealNOCS 156 类先验选择 73.7%；6–38 Hz 随假设/ADMM 预算变化；高运动 mug 序列 ADD 1.56 cm，FoundationPose 原生 62.12 cm（30 帧重初始化 4.29 cm）。
- **不能推出：** 类别先验决定上界，不能处理未知类别/实例特有位姿-形状耦合；单帧估计 + 逐帧拟合不提供原生时序状态，遮挡期仍靠假设筛选；最快 38.85 Hz 只在最低预算/已知单类别；RGB-D 与类别形状先验不是纯 RGB、无先验。
- **阅读深度：** 正文选读：方法 §III–V、ROPE/HouseCat6D §VI、跟踪与抓取 §VII、效率表 III；未复核全部证明/附录；未运行复现。

**本节结论：** 物体级 6-DoF 追踪把“追踪”从像素对应推进到**对象假设 + 位姿轨迹 + 失败恢复**，但它仍不是 Clover 需要的物理对象状态。四条验收边界必须同时写清：

1. **对象先验来源：** RoPT/Robust Recovery 需要实例 CAD + RGB-D；GRC-Pose 用生成 CAD + VGGT；ComPose 用 SAM3/SAM3D-Object 与手部模型；ASM-6D/LEGAU/DICArt 用类别先验；Event6D 用事件 + 深度；OCH3R 用单图生成。没有一条同时满足纯 RGB、无 CAD、无类别先验、无深度、开放类别。
2. **估计 vs 跟踪：** ASM-6D/LEGAU/DICArt/OCH3R 是单帧/单观测估计；RoPT/GRC-Pose/ComPose/Robust Recovery/Event6D 才是时序跟踪。把单帧 ADD 与跟踪 ADD 混在一起，会制造假 SOTA。
3. **延迟必须分阶段：** GRC-Pose 的 831.9 FPS 只是后验，端到端 0.79 FPS；RoPT 18.6 FPS 低于 FoundationPose 42.9 FPS；ASM-6D 6–38 Hz；Event6D >120 FPS 但需要事件相机 + 深度。任何“实时”都必须写清是否包含检测/分割/生成/自适应。
4. **恢复不是语义：** RoPT/Robust Recovery 显式检测失败并重定位，但恢复的是几何位姿；对象身份、遮挡期存在性、材质/质量/可供性仍未被证明。物体级状态的下一个验收面是“同一物体在遮挡/换视角/换光照后仍是同一对象，并且它的物理属性支持正确操作”，而不是 ADD 或 FPS 的单点分数。

### 正式会议 2026：纯视觉开放世界分割、通用追踪与事件视觉

检索/核验：**2026-10-25**。以下为 ICLR/ECCV 2026 camera-ready 或正式接收的一手论文（按 arXiv 注释与项目页核对），补上预印本批次中较薄的三类证据：**无文字提示的开放世界分割**、**几何/扩散先验进入通用追踪**、**事件相机的高帧率感知**。会议接收是出版状态，不是独立复现或 Clover 结果。

#### WOW-Seg：无文字提示的开放世界分割，但仍借 VLLM 的世界知识

- **一手来源：** [固定版本](https://arxiv.org/abs/2605.16903v1)（ICLR 2026） · [官方代码](https://github.com/AAwcAA/WOW-Seg-Meta)。`PRIMARY_PAPER` / `OPEN_SOURCE`。
- **机制：** 输入图像与一组掩码，Mask2Token 把掩码变成与 VLLM 特征空间对齐的视觉 token；Cascade Attention Mask 让每个实例独立预测，降低实例间语义干扰；VLLM 自回归生成每个掩码的类别名。推理时可用 SAM 等掩码生成器。
- **输入与学习来源：** 训练用真值掩码与类别标签 `L1`；VLLM 自带语言/世界知识 `L2`。所谓 word-free 指推理不提供文字提示，不表示整条管线没有语言预训练。
- **实际证据：** LVIS 语义相似度 89.7、语义 IoU 82.4；RR-7K 含 7,662 类；作者报告参数约为 DAM 的 1/8 而语义相似度更高；掩码数 1→32 时总计算增加不到 4×。**但**作者用 LVIS、PACO、COCO Stuff 训练 2 epochs，再在 LVIS/PACO 上报告 SOTA；这是训练集内评测，不能当作开放世界泛化。RR-7K 的 mask 来自 SA-1B、类别由 VLM+人工管线标注，是作者构造的半独立测试。
- **不能推出：** LVIS/PACO 分数不是开放世界泛化；开放世界类别仍受 VLLM 知识、命名习惯与训练标签本体限制；掩码质量决定上限；没有视频身份/追踪；RR-7K 不是第三方独立基准；不是纯视觉学习。
- **阅读深度：** 正文选读：方法、表 1–3、效率分析与结论；未复核全部附录；未运行复现。

#### MoSA：从无标注视频的运动中学习通用 objectness

- **一手来源：** [固定版本](https://arxiv.org/abs/2609.39785v1)（ECCV 2026）。`PRIMARY_PAPER`。论文给出代码入口；本次仅核对 arXiv 正文，未加载代码。
- **机制：** 三阶段无监督框架：多粒度运动分割（MGMS）在合成视频上训练、在真实无标注视频上生成伪标签；Perceptual Grouping Model 用对比学习把运动线索转成外观驱动的 objectness；最后迁移到 prompt-guided 高分辨率分割器。
- **输入与学习来源：** 无人工标注视频 `L0`，但运动模块先在合成视频上训练并使用光流；属于“零人工标注”，不是“零先验/零合成数据”。
- **实际证据：** 七个零样本分割基准（COCO、ADE20K 等）优于既有无监督方法；作者报告零人工标注下与全监督 SAM 可比，并改善静态物体/多粒度。
- **不能推出：** 运动伪标签的偏差会进入 objectness；静态、弱运动、透明/反光物体仍是难点；无类别语义、无实例身份、无追踪；合成到真实的差距未完全量化；光流前端成本另计。
- **阅读深度：** 正文选读：三阶段方法、伪标签质量、七基准与局限；未复核全部附录；未运行复现。

#### GOT-Edit：用 3D 几何先验增强 2D 通用目标追踪

- **一手来源：** [固定版本](https://arxiv.org/abs/2602.08550v3)（ICLR 2026）。`PRIMARY_PAPER`。
- **机制：** 从纯 2D 视频流用预训练 VGGT 提取几何线索；通过带零空间约束的在线模型编辑把几何信息注入语义跟踪器，保留语义判别；track-by-detection 框架。
- **输入与学习来源：** 首帧框 + RGB 视频；VOT2022/GOT-10K 训练；VGGT 几何预训练另记；在线编辑不需要 3D 传感器，但需要额外几何前向与编辑计算。
- **实际证据：** 作者报告多个 GOT 基准上一致优于 2D 语义基线，尤其在部分遮挡、干扰物、几何/外观变化下。
- **不能推出：** 几何是推断而非测量；在线编辑的成本/稳定性未在摘要级闭合；短时 GOT 不提供长期身份记忆；开放世界新类别与语义理解另测；不是纯视觉 AGI。
- **阅读深度：** 正文选读：方法、训练数据与实验设置；未复核全部附录；未运行复现。

#### LiFR-Seg：事件引导的任意时刻高帧率分割

- **一手来源：** [固定版本](https://arxiv.org/abs/2603.21115v1)（ICLR 2026）。`PRIMARY_PAPER`。
- **机制：** 给定一张过去 RGB 帧与异步事件流，在任意帧间时刻预测稠密语义；事件驱动运动场 + 不确定性感知 warping + 时序记忆注意力；满足因果性与 anytime 预测。
- **输入与学习来源：** RGB + 事件相机；DSEC/SHF-DSEC/M3ED 语义标签 `L1`；事件是不同于 RGB 的视觉模态，不能记作 `V0` 单目 RGB；训练在目标时刻有监督。
- **实际证据：** DSEC 上 73.82% mIoU，距理想 HFR 上界 73.91% 仅 0.09%；DSEC-Night 41.86% 略高于 RGB HFR 上界 41.83%；M3ED-Drone 64.28% vs LFR 55.23%。
- **不能推出：** 需要事件传感器与标定；语义类别固定；Segformer-B2 骨干/数据集特定；事件噪声与高动态下的长期一致性另测；不做实例身份/追踪；不是通用视觉模型。
- **阅读深度：** 正文选读：任务定义、方法、DSEC/M3ED 表与结论；未复核全部附录；未运行复现。

#### SAM-H / WOFTSAM：分割引导的长期平面追踪

- **一手来源：** [固定版本](https://arxiv.org/abs/2602.19624v2)（ECCV 2026） · [官方代码](https://github.com/serycjon/WOFTSAM)。`PRIMARY_PAPER` / `OPEN_SOURCE`。
- **机制：** 用 SAM 2 的分割掩码轮廓估计 8-DoF 单应，训练-free；WOFTSAM 再把基于对应的 homography 与分割重检测结合，形成 track–re-detect–fallback 级联。
- **输入与学习来源：** RGB 视频 + 首帧平面目标；SAM 2 掩码；无新训练。SAM 2 的上游监督另记。
- **实际证据：** SAM-H 在 PlanarTrack 上比此前最佳 p@5 高 18.4pp；WOFTSAM 在 PlanarTrack/POT-210 上优于所有此前方法；作者报告 RTX A5000 上 2.4 FPS、4.5GB 显存、分割约 42ms/帧。
- **不能推出：** 平面/单应假设；2.4 FPS 不是实时；光流是主要成本；分割错误会传播；非平面/非刚性/严重遮挡另测；没有语义理解。
- **阅读深度：** 正文选读：方法、PlanarTrack/POT-210 表、运行时间与局限；未复核全部附录；未运行复现。

| 方法 | 一手来源 | 机制与可核查证据 | 边界与反假设 |
|---|---|---|---|
| gen2seg | [2505.15263](https://arxiv.org/abs/2505.15263v3)（ICLR 2026） · [项目页](https://reachomk.github.io/gen2seg/) | 用 instance coloring loss 微调 Stable Diffusion/MAE 做类别无关实例分割；只在少量室内家具/汽车上微调，却对未见类别/风格零样本泛化，接近全监督 SAM，细结构与模糊边界更好 | 生成式先验（SD 含图文 `L2`、MAE 为无标签 `L0`）；微调域窄；无类别语义/身份/追踪；零样本评估仍有限 |
| Point Prompting | [2510.11715](https://arxiv.org/abs/2510.11715v2)（ICLR 2026） · [项目页](https://point-prompting.github.io) | 把查询点画成彩色标记，用视频扩散模型在中间噪声级重生成，使标记随帧传播；以未编辑首帧为负提示保持标记可见；零样本点追踪可穿遮挡，接近专门自监督模型 | 扩散模型计算重、非在线实时；标记是人工注入的反事实证据；长视频/重现/相机运动另测；不是对象级身份 |
| SEAL | [2601.23159](https://arxiv.org/abs/2601.23159v1)（ICLR 2026） · [项目页](https://0nandon.github.io/SEAL) | 首个语义感知 Segment Any Events：开放词汇事件实例分割，支持实例级/部件级、视觉提示与语言；构建四个由粗到细基准；参数高效且推理更快 | 事件传感器、语言提示 `L2`；四个基准有限；事件噪声/运动模糊；无 RGB 纹理/颜色；不是通用视觉 |
| Pano3D | [2606.14307](https://arxiv.org/abs/2606.14307v2)（ECCV 2026） · [项目页](https://victorbbt.github.io/Pano3D/) | 在 3D 前馈重建模型上加 set-based mask decoder，几何+语义联合训练，统一 3D 重建与 3D 全景分割；在 ScanNet/ScanNet200/ScanNet++ 上报告 SOTA，适用于 online/all-to-all 骨干 | 静态室内场景为主；依赖 3D 全景标签；动态/透明/反光另测；语义类别固定；不是通用物理理解 |
| LaGoVAD | [2503.13160](https://arxiv.org/abs/2503.13160v3)（ICLR 2026） | 开放世界视频异常检测：异常定义可由用户自然语言在推理时改变；弱监督下用动态视频合成多样化异常时长 + 负样本对比学习增强特征鲁棒性 | 语言引导 `L2`；弱监督仍有标签；异常定义/数据分布变化；不是纯视觉；检测异常不等于理解因果机制 |

**正式会议批次的结论：** 这批工作把“纯视觉”推进到更细的条件：WOW-Seg 去掉了推理时的文字提示但保留 VLLM 世界知识（其 LVIS/PACO 分数是训练集内评测）；MoSA 去掉了人工标注但保留合成视频与光流；GOT-Edit 只用 RGB 却注入 VGGT 几何；LiFR-Seg 用事件相机补帧间证据；SAM-H 用分割做长期平面追踪。它们共同说明：**“纯视觉”必须按输入模态、预训练知识、标注和外部前端逐项记账**，不能用一个标签概括。

### NeurIPS 2026：关系、可供性、4D 与概念分割鲁棒性

| 方法 | 一手来源 | 机制与可核查证据 | 边界与反假设 |
|---|---|---|---|
| RelationVGGT | [2610.00970](https://arxiv.org/abs/2610.00970v2)（NeurIPS 2026 poster） · [项目页](https://relationvggt.github.io/) · 正文选读 | 前馈、无位姿多视图 3D 空间关系分割：给定视觉主体与关系文本，跨视图分割目标而不提供其类别名；融合视觉基础模型语义与 3D 几何基础模型表示，用 relation transformer 做主体条件跨视图关系预测；ScanNet++ 自动标注管线（VLM/LLM）。作者还做了同义/未见谓词替换，报告词法鲁棒性 | `L2` 关系文本；**作者自述**依赖带实例标注的数据集（如 ScanNet++）、Set-of-Mark VLM 标注；只建模 object–object 空间关系，不含功能关系/场景图节点；静态室内多视图；无视频追踪/动作 |
| UniFunc3D | [2603.23478](https://arxiv.org/abs/2603.23478v2)（NeurIPS 2026） · [项目页](https://jiaying.link/unifunc3d) · 正文选读 | 训练-free 的统一主动时空 grounding：把 MLLM 当主动观察者，联合语义-时间-空间推理，粗到细选择视频帧与高细节交互部件，输出 3D 可供性分割；SceneFun3D 上相对提升 59.9% mIoU，超过部分训练方法 | **作者自述**：极小功能部件（<0.1% 图像面积）与严重遮挡仍失败；需更好的 zoom-in/显式 3D 几何；无交互式修正；`L2` 语言 + 3D 表示；可供性标签人定义；未闭环验证接触/可行性 |
| Uni4R | [2608.09613](https://arxiv.org/abs/2608.09613v2)（NeurIPS 2026 main） · 正文选读 | 用 Optimal Transport + ODE 学习连续速度场，把 4D 重建与点追踪统一；Flow Matching Guided Decoder + 全局速度分支 + 局部速度预测，可在任意时间戳解码；积分一致性训练从整数帧监督分数时刻速度；速度场作为运动学先验互惠重建与追踪 | 训练需 4D/速度/对应监督；几何/运动学先验不等于物理因果；遮挡/拓扑变化/非刚性未闭合；无语义身份；长序列稳定性与计算成本需核；没有独立真实机器人闭环 |
| AdvPCS | [2609.39265](https://arxiv.org/abs/2609.39265v1)（NeurIPS 2026） · 正文选读 | 首个针对 SAM3 Promptable Concept Segmentation 的通用跨提示对抗攻击：min-max 提示优化、全局-局部感知欺骗、时序转移偏差；四个数据集、三个模型上报告优于 SOTA 攻击；剪枝防御几乎无效 | **作者自述**：min–max 双层优化带来额外计算；只针对 PCS 概念存在预测，可能不外推到 SAM/SAM2 等传统分割；白盒/扰动预算受限；不是防御方案；安全评估须与干净精度同时报告 |

**NeurIPS 2026 批次结论：** 关系/可供性把“看见”推进到“相对什么、能怎么用”；4D 统一把追踪与重建放到连续时间；AdvPCS 则提醒概念分割的开放接口本身是攻击面。三者都还停留在特定输入/标注/威胁模型下，不能当作通用世界理解或安全保证。

<a id="strict-hidden-state-2026"></a>

### 严格视觉隐藏态：质量、物性、永久性与因果恢复

检索/核验：**2026-10-25**。本节专门处理“看不见但必须知道”的状态：质量、密度、摩擦、刚度、遮挡后的物体位置与身份。它们是“理解真实世界”最容易被高分生成/重建掩盖的部分；下列证据把**视觉可推断的边界**与**必须借助触觉/WiFi/语言/模拟器**的条件分开。

#### 单图质量估计：m = V·ρ 的结构化分解，但仍借深度与 VLM 材料先验

- **一手来源：** [固定版本](https://arxiv.org/abs/2601.20303v2)（IJCAI 2026）。`PRIMARY_PAPER`。
- **机制：** 从单张 RGB 估计物体质量；用单目深度恢复物体几何以约束体积，用 VLM 提取材料语义作为密度相关先验；几何、语义、外观经实例自适应门控融合，分别回归体积与密度两个潜因子，仅在质量标签下监督。
- **输入与学习来源：** 推理只需 RGB；训练用 image2mass/ABO-500 的质量标签 `L1`，单目深度模型与 VLM 材料语义分别带来 `L1/L4` 与 `L2`。不是纯视觉学习。
- **实际证据：** 作者报告在 image2mass 与 ABO-500 上达到单视图方法 SOTA，并与依赖完整 3D 重建的多视图管线竞争。
- **不能推出（作者/方法边界）：** 质量依赖体积与密度，单视图仍 ill-posed；VLM 材料语义可能模糊/错误；只预测单一密度因子，多材料混合未解决；透明/反光/无纹理深度失败会传导；质量正确不等于摩擦、刚度或接触稳定。
- **阅读深度：** 正文选读：方法、结果表、结论与多材料讨论；未复核全部附录；未运行复现。

#### iSEE：无标签的物体永久性，靠遮挡-重现自监督

- **一手来源：** [固定版本](https://arxiv.org/abs/2610.01201v1)。`PRIMARY_PAPER`。
- **机制：** 在 slot attention 上加入对象证据建模（用 slot 注意力与自身历史判断物体何时被遮）、外观-位置分离、重现时的再识别；只用重现作为学习线索，不需要框/轨迹/可见性标签。
- **输入与学习来源：** 无标签视频 `L0`；固定相机；物体永久性从遮挡/重现统计中自监督产生。
- **实际证据：** 作者报告在长遮挡后把物体放回 slot、并在遮挡期间定位隐藏位置；固定相机下接近使用框/ID/可见性标签训练的跟踪器。
- **不能推出（作者自述局限）：** slot 可能吸附到相似物体、在目标回来前被释放、或起始 slot 不在目标上；每数据集固定 slot 数；固定相机；无类别/物理/因果；不是通用移动相机追踪。
- **阅读深度：** 正文选读：方法、定量结果、Conclusion/Limitations；未复核全部附录；未运行复现。

#### PersistBench：4D 基础模型的记忆在离开视野后崩塌

- **一手来源：** [固定版本](https://arxiv.org/abs/2609.20819v2) · [项目页](https://guangzhaohe.com/persistbench)。`PRIMARY_PAPER` / `OFFICIAL_PROJECT`。
- **机制：** 用 360° 视频作为“全知”真值，评估 4D/相机可控视频模型的三个对象中心方面：物体永久性、运动连续性、外观保持；覆盖静态/动态、可见/不可见片段。
- **输入与学习来源：** 评测基准；被评模型接收视频/相机条件，训练来源各异；真值来自 360° 采集，不是模型输入。
- **实际证据：** 当前模型在大部分内容可见的新视图合成上表现好，但物体离开输入视野后持久性显著下降；显式几何条件只能部分补偿；作者指出训练视频通常目标全程可见，缺少遮挡/重现监督。
- **不能推出（作者自述局限）：** 依赖 ViPE 位姿、SAM2/VLM 等现成评分组件，误差可能影响分数；YouTube 360 场景分布有限；只评可渲染 4D 输出，不覆盖点云/语言模型；基准不证明记忆机制。
- **阅读深度：** 正文选读：指标、主结果、Limitations/Conclusion；未复核全部附录；未运行评测。

| 方法/基准 | 一手来源 | 机制与可核查证据 | 边界与反假设 |
|---|---|---|---|
| PhysicsLENS | [2610.01162](https://arxiv.org/abs/2610.01162v1) · 正文选读 | 物理属性盲区诊断：匹配同一条件帧与任务、只改场景描述中的物理属性；80 个初始帧、439 个 clip、4 个生成器；七域（碰撞、重力、动量、摩擦、形变、流体、因果）。作者报告 47 个“看似合理”clip 中 34 个未遵循所述隐藏属性，28 个遵循属性的 clip 中 15 个仍在其他物理上不合理；VLM+信号管线对 plausibility AUC 0.72、task completion 0.81 | **作者自述**：只覆盖 80 帧/4 模型，隐藏属性遵循与物理族归因仍难；评的是生成视频，不是从真实视频识别隐藏属性；生成先验可伪造“合理”外观；人类/VLM 判断有噪声 |
| WROP | [2609.28654](https://arxiv.org/abs/2609.28654v1) · 正文选读 | 150 个 Blender 生成器、6 个认知任务族（3 类物体永久性/3 类固体性），每任务 10,000 样本、总计 1.5M 训练语料；固定 300 题考试、人工评判、手工动画真值；16B PWM-WROP 后训练；评测 14 个视频模型，PWM-WROP 在 continuation 中第一、总体第三 | **设计边界**：纯合成 3D、手工任务/真值、人工评判；reference-to-video 模型因可重建场景而占优；通过考试不证明真实相机永久性；模型仍会出现额外物体、错误车道、穿模；生成先验可伪装 |
| ContactGaussian-WM | [2602.11021](https://arxiv.org/abs/2602.11021v1) | 用统一 Gaussian 表示外观与碰撞几何，通过可微闭式物理引擎从稀疏、接触丰富视频推断物理属性；模拟/真实操作验证 | 依赖刚体物理引擎与已知状态参数化；稀疏视频的可识别性未证明唯一；非刚体/流体/透明另测 |
| ViTacPhys | [2608.21355](https://arxiv.org/abs/2608.21355v1) · 正文选读 | 视觉-触觉示范估计质量/摩擦系数类别与连续刚度；60 个刚体/可变形物体；seen 97.2%/98.8%/5.51% MAPE，held-out 87.5%/97.5%/9.08%；真实机器人 OOD 干净成功率下降 14.7pp，对比 ACT 下降 41.1pp；力误差相对 ACT 降低 19.7% | **作者自述**：触觉图主要捕捉法向压力，质量/摩擦被离散化；刚度是操作级测量（含形变/接触柔度），非本征材料常数；60 物体、单一参与者；OOD 6 对物体；部署需一次性 VLM 调用；**反证视觉-only 唯一识别** |
| ViWi | [2608.07726](https://arxiv.org/abs/2608.07726v2) · 正文选读 | 明确论证体积力学属性（Young 模量、Poisson 比、密度）从视觉单独估计本质歧义；用 object-centric material slots 聚合体素 + WiFi 频段 RF 描述符（由介电常数/电导率模拟）；Six GVM 指标中改善四项，Young/Poisson 增益最强；vision-only 变体在 ABO-500 质量估计上也有改善 | **作者自述**：RF 描述符是模拟而非真实测量，未覆盖实际 RF 传感变异；材料槽假设分段常数；需标定/模拟条件；**反证纯视觉**；真实 RF 实验待做 |
| Intuitive Physics Probing | [2606.09646](https://arxiv.org/abs/2606.09646v2) | 冻结特征探针比较 V-JEPA、VideoMAE、LTX-Video 在 IntPhys2/MVP 上的直觉物理；V-JEPA 最强，物理信息在中间-后层最可读，打乱帧序显著降低 | 探针相关不等于因果理解；三个模型家族/两个基准；未测干预/反事实；表示可读性依赖 readout |

**本节结论：** 视觉-only 的质量/永久性在**窄条件**下已有可行证据（单图质量、固定相机 slot 永久性、生成视频的物理基准），但每条都借了深度、VLM、合成数据、固定相机或生成先验；触觉/WiFi 反证说明“仅凭视觉唯一识别物性”在一般情况下不成立。Clover 应把“可推断的隐藏态”与“必须交互/额外传感的隐藏态”分开验收，不能用生成视频的物理合理性替代真实因果识别。

### 动作、事件与指代：从“看见什么”到“在做什么、指哪一个”

| 方法/研究 | 一手来源 | 机制与可核查证据 | 边界与反假设 |
|---|---|---|---|
| TrAction | [2606.03490](https://arxiv.org/abs/2606.03490v1) · [官方代码](https://github.com/ecker-lab/TrAction) | 用稀疏点轨迹而非稠密 RGB 做 2.5D 动作识别，配 masked-trajectory 预训练；仅用少量输入即达 Something-Something V2 45% top-1、EPIC-Kitchens-100 54% top-1；与 DINOv2/V-JEPA 2 特征互补，融合分别 +8.7/+1.6 点；作者报告时间反演敏感性优于 V-JEPA | 轨迹输入仍需点追踪前端；动作类别 `L1`；稀疏轨迹可能丢弃物体外观/文字/场景证据；互补性不等于统一状态；未覆盖未知动作与细粒度时序 |
| ByteAction | [2608.22760](https://arxiv.org/abs/2608.22760v1) | 不解码像素，直接在压缩图像 bitstream 的 byte 空间识别人体动作；双视图字节级框架 + Bitstream Pattern Augmentation + 损坏一致性训练；Stanford40/PPMI/PASCAL VOC 2012 Action 的损坏比特流上报告 SOTA 鲁棒性 | `L1` 动作标签；只做视频/图像 bitstream 分类，不是通用视觉；字节空间对编码器/压缩格式敏感；不覆盖定位/分割/追踪；隐私优势是场景属性，不是理解能力 |
| Qwen3-VL-Seg | [2605.07141](https://arxiv.org/abs/2605.07141v1) | 把 MLLM 预测框作为语义结构先验，用轻量 box-guided mask decoder 解码像素掩码；仅新增约 17M 参数（约 0.4%）；构建 SA1B-ORS 训练集与 ORS-Bench 评测；开放世界指代分割 | `L2` 语言指代；依赖 MLLM 的框质量与语言理解；掩码解码器不是纯视觉学习；开放世界仍受语言词表/数据分布限制；未证明视频身份持续 |
| SetCon | [2605.20110](https://arxiv.org/abs/2605.20110v1) | 把开放端指代分割重构为集合级概念预测：LVLM 生成自然语言概念，分层语义分解为集合概念与子集概念，再联合解码掩码集合；236k 样本/784k 概念短语；报告 gRefCOCO +3.3 gIoU、MUSE +12.1 gIoU，目标数增多时优势扩大，并可迁移视频 | `L2` 语言概念；集合完备性/互斥性由训练与评测定义；概念接口可能引入语言先验；未覆盖物理身份或开放世界新关系；标注管线成本高 |
| TempoGround | [2609.02359](https://arxiv.org/abs/2609.02359v1) | 流式视觉 grounding：检测跨帧对象对应，显式预测 new/continue/leave 存在状态，解码 2D 框并提升到相机系 3D 框；用可验证 Grounding/Identity/Consistency 奖励的 SGR 训练；面向因果流式输入 | `L2` 语言指代 + 视频；存在状态是任务定义的一部分；3D 提升依赖相机/几何假设；VLM 计算成本高；未证明长期遮挡后的身份恢复或真实机器人闭环 |

**动作/指代结论：** 动作识别正从稠密 RGB 转向稀疏轨迹、压缩字节等更“原生”的输入；指代/grounding 则把语言概念与像素/3D 目标连接起来。两者都扩展了“识别”的边界，但也表明：动作类别、语言指代和对象身份仍是不同监督条件，不能用一个分类分数概括“理解了正在发生什么”。

<a id="action-event-2026"></a>

### 动作与事件：分类、定位、预期与开放词汇

动作识别从“整段视频一个标签”扩展到**在线定位、零样本、开放词汇与意图预测**。下表补齐本轮此前仅 TrAction/ByteAction/LaGoVAD 的薄覆盖；它们仍未解决“未知动作、细粒度时序、因果事件”三类缺口。

| 方法 | 一手来源 | 机制与可核查证据 | 边界与反假设 |
|---|---|---|---|
| OZ-TAL | [2605.09976](https://arxiv.org/abs/2605.09976v1) | 新任务：在线零样本时序动作定位；训练-free 复用现成 VLM，并加入视觉表示增强/偏置缓解；在 THUMOS14、ActivityNet-1.3 建立基准与基线 | VLM 语义偏置；流式未剪辑视频；类别词表/提示；在线延迟与边界精度未统一；不是纯视觉学习 |
| OnPoint | [2607.00289](https://arxiv.org/abs/2607.00289v1)（ECCV 2026） | Point-supervised Online TAL：每实例仅一个时间点；离线教师→在线学生多级蒸馏（伪片段实例、类激活序列、预期窗口）；动作性引导注意力校准；五个数据集验证 | 仍需离线教师/点标签；在线延迟；边界与罕见动作；不是零样本；教师偏差会传给学生 |
| Action-Guided Attention（AGA） | [2603.01743](https://arxiv.org/abs/2603.01743v1)（ICLR 2026） | 用预测的动作序列作为 attention query/key，引导过去帧选择，并与当前帧 gating 融合；EPIC-KITCHENS-100 动作预期 | 意图是潜在变量；数据集/厨房域；未来动作类别受训练集限制；不是因果推断 |
| Zero-Shot Skeleton Action Anticipation | [2608.14243](https://arxiv.org/abs/2608.14243v1) | 新任务 ZS-SkAA：仅用早期骨架序列识别未见动作；时空特征 + 互信息估计/最大化对齐部分视觉与语义类嵌入；NTU RGB+D 协议 | 骨架输入（非 RGB）；早期观测；零样本语义嵌入；人体/人形动作；不是通用视频理解 |
| SP-CLIP | [2603.08289](https://arxiv.org/abs/2603.08289v1) | 冻结 VLM + 结构化语义提示（意图/运动/物体交互）多层级聚合与一致性打分；不训练视觉编码器/不加参数；零样本动作识别，细粒度/组合动作提升 | 依赖 CLIP/语言提示；语义描述质量决定上限；不是从视觉经验学概念；细粒度动作仍受词表限制 |
| SimVA | [2605.23288](https://arxiv.org/abs/2605.23288v1) | 开放词汇动作识别：从 patch 级视觉-文本相似度构造 4D 时空相似体；空间聚合、运动感知调制、Mamba 时序聚合；zero/few-shot/base-to-novel | 依赖 CLIP 文本对齐；大词表采样近似；计算/内存；动作类别由语言定义；不是纯视觉 |

**结论：** 动作/事件理解已覆盖在线定位、点监督、零样本分类、骨架预期与开放词汇，但几乎全部依赖语言/VLM、骨架、点/段标签或离线教师；“未知动作 + 细粒度边界 + 因果意图”仍没有纯 RGB 的统一证据。

<a id="hoi-social-2026"></a>

### 人-物交互、注意与社会场景

动作表回答“发生了什么”，但没有回答“谁对什么做了什么、手是否真的接触、意图和注意指向谁”。人-物交互（HOI）正好卡在物体识别、动作理解、3D 几何与社会认知之间：它既需要检测 ⟨人, 动词, 物体⟩ 三元组，也需要接触/抓握的 3D 证据，还需要在多人场景中区分“对我说话”与“对别人说话”。本轮补 9 篇 2026 年工作；它们共同显示，HOI 的分数提升很容易来自语言先验或评测口径，而不是纯视觉交互理解。

| 方法 | 一手来源 | 机制与可核查证据 | 边界与反假设 |
|---|---|---|---|
| FineHOI | [2609.05959](https://arxiv.org/abs/2609.05959v1)（ACM MM 2026） · 正文选读 | 零样本 HOI：只用检测器定位人和物体，交互表示改从稠密 patch 特征构建；无监督聚类出语义部件、按交互相关性重加权，再用区域感知交互 Transformer 融合局部/全局；HICO-DET 未见动词 unseen 35.58 mAP（LAIN 32.05，+3.53），闭集 39.13 mAP、Rare 39.91，V-COCO 66.5 AP$^{S2}$ | 冻结 DINOtxt + 文本提示（`L2`）；未见物体（UO）不优于使用检测器中心特征/LLM 监督的方法；单帧、静态、成对交互；不是 3D 接触/意图；代码 CC BY-NC-ND 4.0 |
| HOIBlender | [2609.23431](https://arxiv.org/abs/2609.23431v2) · 正文选读 | RF-DETR/LW-DETR 式检测基础 + DINOv2，去掉专用 transformer encoder；双阶段解码先稳定人-物几何、再用 BLIP-2 先验做动词/HOI 分类；分组查询训练只在训练期增加匹配；HICO-DET Default Full 44.49、Rare 43.21、Non-Rare 44.86（DINOv2-B，9 epochs）；Nano 41.46 @69.8 ms、Small 43.19 @74.9 ms、2XL 44.49 @88.4 ms（A100） | BLIP-2 视觉编码器占主要延迟，作者自述是效率瓶颈；PViC 在 Rare 44.61 仍更高，说明检测器侧改进未解决长尾；HICO-DET 单数据集；`L2` 语言先验；不是视频/3D/意图 |
| GraspHOI | [2608.28386](https://arxiv.org/abs/2608.28386v2) · 正文选读 | 单张野外图像重建全身 3D HOI：人体/手/物体分开重建，深度配准统一到度量相机系，遮挡感知手掌条件补全，再对指关节做接触/穿模优化；ARCTIC 人体 sF-sc 0.865（HDM 0.535、TeHOR 0.587）、MPJPE 57.96 mm（130.31/154.25）、手 PA-MPJPE 7.69（10.07/10.89）、CPP 72.83%（EasyHOI 60.34%）；PGG CPP 78.15%（EasyHOI 48.23%）；物体 sF-sc 0.624（SAM 3D Objects 0.550），但 sCD 2.12 高于 1.94 | 依赖生成式物体网格（Hunyuan3D 2.1）、FoundationPose、SAM 3D Body、WiLoR、可见物体 mask 与名词提示；静态、抓握中心、至少一只手接触；不建模运动/可变形/坐靠支撑；单目尺度-深度歧义与上游错误会传播；不是语义/意图 |
| SAGE | [2607.04017](https://arxiv.org/abs/2607.04017v1)（ECCV 2026） · 正文选读 | 统一 Transformer 同时做注视检测/预期与 HOI 识别/预期；GCSA 用当前注视条件化 HOI，GCTP 用预测未来注视条件化未来动作；EGTEA Gaze+ 上相对同样多任务监督的基线：注视 F1 44.8→46.8、动作识别 63.1→65.0、注视预期 34.5→37.0、动作预期 44.0→58.4；Exo-Cook HOI 44.6 mAP（ST-Gaze 42.5）；Vid-HOI 38.65（ST-Gaze* 38.46，差距很小） | 训练与评测使用注视标注（`L1`，非纯视觉自监督）；第一人称/第三人称共享架构但不声称跨视角泛化；Vid-HOI 增益边际；固定预期时域；不是社会角色/语言意图 |
| HOI 评测审计 | [2610.25849](https://arxiv.org/abs/2610.25849v1)（WACV 2027 在审） · 正文选读 | 固定同一批预测，用五种口径评分：官方类别、身份控制、词法归一、分级语义信用、严格命题等价；HICO-DET 六个系统排序随口径变化（官方 GEN-VLKT 34.5 领先，SHOE 下 SL-HOI 37.2 领先，严格等价 GEN-VLKT 35.2 回到最高）；语义增益 1.6–20.3 mAP，AgentHOI 仅 49% 在严格等价下保留；建议同时报告匹配效应与语义信用 | 描述性比较，尚无配对置信区间/人工审计结果；系统训练监督不同，不能据此判断零样本能力或架构；严格等价会拒绝仍有用的宽泛描述；静态图动作本身可能歧义 |
| Talking to Me or Someone Else? | [2609.14118](https://arxiv.org/abs/2609.14118v1)（ACM MM 2026） · 摘要 | 把第一人称“是否在对相机佩戴者说话”（TTM）从离线 clip 级二分类改为在线帧级预测，并显式区分对他人说、自言自语、背景等非 TTM 状态；构建 Online TTM 数据集 | 第一人称、社交注意单一任务；依赖人脸/头部/语音视觉线索；摘要未给跨数据集数值；不是完整社会场景理解 |
| Social Reasoning in Embodied VLMs | [2610.27496](https://arxiv.org/abs/2610.27496v1)（IROS 2026 workshop） · 摘要 | 在 SHREC 真实人-机器人社交交互基准上评 Gemini Robotics-ER 与通用 VLM：机器人专用模型在错误/能力检测上优于 GPT-4o-mini，但在细粒度社会属性判断上更差；加入一帧视觉对一项任务有帮助、对另一项有害 | 小规模基准；VLM 的 `L2` 语言/常识先验；社会属性标签本身有歧义；不是纯视觉；不能推出通用社会推理能力 |
| ECHO | [2610.10438](https://arxiv.org/abs/2610.10438v1) · 摘要 | 新任务“情境物体放置”：观察人搬运物体的第一人称视频，预测物体应被放到的目的地；构建带可导航重建场景与物体自然目的地真值的 Embodied Camera Observations 数据集 | 任务定义依赖“习惯/归属”等社会常识；数据规模与标注者偏差未核；单目第一人称；不是纯几何；摘要未给方法数值 |
| COOL | [2610.09358](https://arxiv.org/abs/2610.09358v1)（CoRL 2026） · 摘要 | 从长期人-物交互行为中推断物体所有权（“我的背包”），用好奇心驱动数据采集保持空间记忆更新；面向个性化机器人协助 | 需要长期观察与主动采集；所有权是隐含社会变量，标签稀疏；依赖语言指令与机器人平台；不是纯视觉单帧识别 |

#### FineHOI：把交互证据从“物体框”拉回“局部部件”

FineHOI 的出发点是：检测器特征把人和物体各压成一个粗粒度表示，恰好丢掉了区分“握着球拍”与“挥着球拍”所需的接触区域。它只用 DETR 提供人和物体的框，交互表示改从稠密 patch 构建；无监督聚类把人体/物体分成部件，再按交互相关性重加权。HICO-DET 未见动词 unseen 35.58 mAP，比 LAIN 高 3.53；闭集 39.13 mAP、Rare 39.91、V-COCO 66.5。消融显示软掩码 + 部件注意力 + 区域交互 Transformer 逐级提升，最大增益来自语义 grounded 的 patch 表示。

边界同样清楚：未见物体设置下它没有超过使用检测器中心特征或 LLM 监督的方法，说明“部件化”不是万能；它仍是单帧、成对、文本类别空间内的交互，不证明 3D 接触、社会角色或意图。它给 Clover 的启发是**交互证据的粒度**：如果世界理解需要“手在做什么”，表示就不能停在物体框级别；但部件级视觉证据必须与 3D 接触和时序动作联合验收，否则只是更细的分类器。

#### HOIBlender：效率与长尾可以同时改善，但语言先验仍是延迟瓶颈

HOIBlender 把 HOI 检测拆成“检测器提供候选 + 双阶段解码 + BLIP-2 语义先验”：去掉专用 transformer encoder，直接从多尺度 projector 选 top-K 人/物 token；第一阶段稳定几何，第二阶段做动词/HOI 分类；分组查询只在训练期增加匹配，推理只保留一组。HICO-DET Default Full 44.49、Rare 43.21，DINOv2-B 仅 9 epochs；Nano 41.46 @69.8 ms、Small 43.19 @74.9 ms、2XL 44.49 @88.4 ms（A100）。相对 Hybrid-SOV-VLA 43.10，2XL 提升 1.39 mAP，延迟 88.4 ms。

但作者自述 BLIP-2 视觉编码器占主要延迟；PViC 在 Rare 44.61 仍高于它，说明长尾没有完全解决；只在 HICO-DET 上验证。它证明“轻量检测 + 语义先验”可以同时改善精度/训练成本，但不证明端侧实时或开放世界交互理解。对 Clover 的“原生 ultrafast”要求，这类系统的正确读法是：**检测骨干可以很轻，语义先验仍可能是重模块**；必须把语言分支的延迟单列，而不能只报检测器 FPS。

#### GraspHOI：单图 3D 接触重建把“看起来对”与“物理上接触”分开

GraspHOI 针对一个很具体的失败：全身 3D HOI 的全局姿态看似合理，但手指悬空或穿进物体。它把人体、手、物体分开重建，深度配准统一到度量相机系，遮挡感知地补全手掌，再对指关节做接触/穿模优化。ARCTIC 上人体 sF-sc 0.865（HDM 0.535、TeHOR 0.587）、MPJPE 57.96 mm（130.31/154.25）、手 PA-MPJPE 7.69（10.07/10.89）、接触合理性 CPP 72.83%（EasyHOI 60.34%）；PGG 上 CPP 78.15%（EasyHOI 48.23%）。相对 SAM 3D Objects，物体 sF-sc 更高（0.624 vs 0.550），但 sCD 更差（2.12 vs 1.94）。

它的边界是“单图 + 静态 + 抓握中心”：依赖生成式物体网格、FoundationPose、SAM 3D Body、WiLoR、可见 mask 与名词提示；不建模运动、可变形物体、坐靠支撑；单目尺度-深度歧义和上游错误会传播。它给 Clover 的证据是：**3D 接触是可测量的物理约束**，不是 VLM 描述；但单图重建的“合理接触”仍可能是生成先验补出来的，必须用多视图/交互后的视觉后果反证。

#### HOI 评测审计与 SAGE：分数排序与注意依赖是两记警告

HOI 评测审计固定同一批预测，只换评分口径，就改变了 HICO-DET 六个系统的排序：官方口径 GEN-VLKT 34.5 领先，SHOE 下 SL-HOI 37.2 领先，严格等价下 GEN-VLKT 35.2 回到最高；语义增益从 1.6 到 20.3 mAP，AgentHOI 只有 49% 的增益在严格等价下保留。它说明开放词汇 HOI 的“提升”至少混合了三件事：匹配引擎、语义宽容度、视觉正确性。Clover 若报告 HOI 能力，必须同时给出官方分、同引擎身份控制、严格等价/角色反转检查，否则无法区分“真的理解了交互”与“评分器奖励了近义描述”。

SAGE 则从另一侧提醒：注视与动作联合建模确实能提升预期（EGTEA 动作预期 44.0→58.4 相对同监督多任务基线），但增益依赖注视标注；在 Vid-HOI 上相对 ST-Gaze 仅 38.65 vs 38.46，说明“加入注意”不是无条件有效。它支持 Clover 把“看哪里”作为世界理解的一部分，但也要求把注视来源（眼动仪标注、预测、还是 RGB 估计）单列；没有这一列，主动视觉的主张无法与纯视觉证据区分。

**本节结论：** HOI 至少包含四个不可互相替代的轴：**检测**（人-物-动词三元组）、**3D 接触/抓握**（手是否真的在物体上）、**注意/意图**（看哪里、要对谁说话）、**社会角色/所有权**（这东西是谁的、该放哪里）。本轮 9 篇工作在各自轴上推进，但没有一篇同时覆盖四轴；检测与效率进步多依赖文本/BLIP-2 先验，3D 接触依赖生成式网格与多上游模型，社会状态依赖长期记忆、VLM 或第一人称数据。对 Clover 的验收要求是：任何“理解了人-物交互”的主张，都要分别报告检测、接触、注意、社会角色四类证据，并说明语言/教师/眼动/机器人平台各贡献了什么；单轴 SOTA 不能外推为广义交互理解。

<a id="face-affect-gesture-2026"></a>

### 人脸、表情与手势：身份、情感与交流

“理解人”至少包含三件不同的事：**身份**（这是谁，1:1 验证/1:N 识别）、**情感**（这张脸表达什么，细粒度 AU/表情）、**交流动作**（手势/姿态在说什么）。此前正文只有 Talking-to-Me 涉及人脸线索；本轮补 10 篇 2026 年工作，覆盖人脸偏见与数据审计、移动端/事件/热成像人脸、AU 接地的表情推理，以及视觉手势。

| 方法 | 一手来源 | 机制与可核查证据 | 边界与反假设 |
|---|---|---|---|
| DenseFace | [2609.16149](https://arxiv.org/abs/2609.16149v1)（IJCB 2026） · 正文选读 | 不重训人脸模型，用 von Mises-Fisher 密度建模 + 密度感知概率匹配缓解种族偏见；RFW NIST 协议（Caucasian FPR=1e-3）下 African FPR 比 8.82→0.91、Asian 7.69→0.43、Indian 5.96→0.62（CosFace-R50）；AdaFace-R50 7.67→1.10、5.84→0.63、5.62→0.73；TPR 保持 99.59 avg；回归版延迟 17.71→18.02 ms（+1.75%） | 仍依赖预训练人脸模型与 anchor set；偏见指标只覆盖四个种族组；FPR 阈值/协议选择影响结论；不解决年龄/性别/遮挡；概率匹配不是身份因果解释 |
| FaceLiVTv2 | [2604.09127](https://arxiv.org/abs/2604.09127v1) · 正文选读 | 轻量混合 CNN-Transformer 人脸识别：Lite MHLA、GDConv 头、RepMix；XS 2.9M/90 MFLOPs、iPhone 15 Pro 0.43 ms，5 基准平均 95.50%；L 8.52M/309 MFLOPs、0.71 ms，平均 97.03%、IJB-C 96.59%（+0.95）；相比 GhostFaceNetV2-2 延迟降 35.8% | 仍以 112×112 对齐人脸为输入；重遮挡/大姿态/跨种族未系统评估；TinyFace 低分辨率提升有限；不输出不确定；移动端数字依赖 CoreML/iPhone 15 Pro |
| EventFace | [2604.06782](https://arxiv.org/abs/2604.06782v1) · 正文选读 | 事件相机人脸识别：结构感知空间适配（LoRA）+ 运动提示/时空调制；EFace 100 训练/31 测试身份；两阶段使 EER 28.81→5.35，Rank-1 94.19；LoRA 调参 Rank-1 92.09/EER 6.81；T=4×50 ms、29.82G FLOPs；作者报告低照度更稳、模板可重建性更低 | 数据集小（100/31 身份）；事件帧 112×112；依赖 RGB 预训练 AdaFace 迁移；跨设备/跨条件未验证；隐私结论是初步的；不是通用身份系统 |
| VTF900 | [2610.24832](https://arxiv.org/abs/2610.24832v1)（WACV 2027） · 摘要 | 900 人可见光-热成像人脸基准，含表情/姿态/遮挡变化，支持 1:1 验证与 1:N 闭集识别；针对现有基准 gallery 仅约 100 人的规模限制 | 摘要级；热成像传感器/配准条件特定；900 人仍非大规模；不是方法；跨种族/年龄平衡未核 |
| Different Defects | [2610.28766](https://arxiv.org/abs/2610.28766v1)（WACV 2027） · 正文选读 | 对 MS1MV3（5.18M 图/93,431 身份）做受控数据审计：发现重复、身份拆分、裁剪错误、多人脸歧义、无效内容五类缺陷；去重 D7 移除 15.44% 图，平均验证 97.20→97.27，达到基线所需步数少 23.7%；随机移除同量无增益；身份合并少 21.8% 步；身份合并+去重少 24.3% 步 | 只测 MS1MV3/特定训练配方；缺陷检测器（PHash/InsightFace/OFIQ/BLIP-VQA）有误差；效果依赖缺陷类型，不能外推“清洗越多越好”；不是隐私/公平性审计 |
| FaceMoE | [2606.32040](https://arxiv.org/abs/2606.32040v1)（ECCV 2026） · [项目页](https://kartik-3004.github.io/FaceMoE/) · 摘要 | 低分辨率人脸识别：MoE Transformer 多专家 FFN + top-k 路由，缓解高低分辨率域差与灾难遗忘；面向模糊/遮挡/低对比 probe | 摘要级；低分辨率特定；专家路由开销/可解释性未核；不是通用人脸；不解决偏见 |
| TAG | [2602.18763](https://arxiv.org/abs/2602.18763v1) · 正文选读 | 把表情识别约束到面部动作单元（AU）接地的推理：SFT 于 310K AU 接地样本 + AU-IoU 奖励的 GRPO；统一 SFT 平均 74.34%（InternVL3-38B 65.11、GPT-5 62.93）；逐数据集 RL 平均 83.78%（RAF-DB 92.80/FERPlus 91.50/AffectNet 67.03）；AU IoU 60.24；去掉 bbox 平均降 1.98；仅 RLVR 使 IoU 46.73→43.46 | 依赖外部 AU 检测器（非真实肌肉测量）；Qwen2.5-VL-7B 基座；逐数据集 RL 非统一模型；MLLM 推理成本高；表情标签本身有文化与主观歧义；不是纯视觉自监督 |
| ActFER | [2604.08990](https://arxiv.org/abs/2604.08990v2) · 摘要 | 主动式表情识别：动态调用人脸检测/对齐、选择性放大局部区域、以视觉 CoT 推理 AU 与情绪；把 FER 从被动单次推理改为主动取证 | 摘要级；工具/放大策略增加延迟；依赖 MLLM 与 AU 先验；未给跨数据集全表；不是纯视觉；主动策略的收益/成本未独立核 |
| UniCon-Former | [2608.13217](https://arxiv.org/abs/2608.13217v1) · 摘要 | 动态手势识别：CNN 卷积投影 + Transformer 全局注意力，金字塔式降低 token 维度，兼顾局部/全局与效率 | 摘要级；手势类别/数据集有限；不是手语/连续交流；未给跨数据集数值；不是 3D 手部姿态 |
| EgoEV-HandPose | [2605.12297](https://arxiv.org/abs/2605.12297v1) · [代码](https://github.com/ZJUWang01/EgoEV-HandPose) · 摘要 | 第一人称双目事件相机联合 3D 双手姿态与手势识别；KeypointBEV 双目融合 + 迭代重投影细化，缓解 ego-motion/单目深度歧义 | 摘要级；事件相机/双目标定；第一人称特定；手势类别有限；未给完整跨数据集数值；不是通用动作理解 |

#### DenseFace：偏见要看“同一阈值下的 FPR”，不是只看组间标准差

DenseFace 的出发点是评测口径：常见的“每组单独选阈值 + 比较准确率标准差”会掩盖部署中的真实差异，因为生产系统通常只能用一个全局阈值。它按 NIST 协议把 Caucasian FPR 固定为 1e-3，再看其他组的 FPR 比；CosFace-R50 上 African 8.82→0.91、Asian 7.69→0.43、Indian 5.96→0.62，AdaFace-R50 也从 7.67/5.84/5.62 降到 1.10/0.63/0.73，同时 TPR 平均保持 99.59。方法本身不重训模型，只用密度感知概率匹配；回归版延迟 +1.75%，匹配时间约 1.5×。

它的边界是四个种族组、预训练模型/anchor set、阈值协议；不解决年龄/性别/遮挡。它给 Clover 的启发是：**人脸身份的“理解”必须先定义公平性/阈值口径**；只报平均准确率会掩盖部署差异，而“去偏”也可能以延迟/覆盖为代价。

#### FaceLiVTv2 与 EventFace：移动端和事件相机是两条不同的“原生超快”

FaceLiVTv2 把轻量人脸识别压到 XS 2.9M/90 MFLOPs、iPhone 15 Pro 0.43 ms，5 基准平均 95.50%；L 8.52M/309 MFLOPs、0.71 ms，平均 97.03%、IJB-C 96.59%。它证明移动端人脸识别可以在 1 ms 内完成，但仍是 112×112 对齐人脸，重遮挡/大姿态/跨种族未系统评估，且不输出不确定。

EventFace 走另一条路：事件相机没有稳定光度外观，它用 RGB 预训练 AdaFace + LoRA 做结构适配，再用运动提示/时空调制建模身份；两阶段把 EER 从 28.81 降到 5.35，Rank-1 94.19；LoRA 调参 92.09/EER 6.81；T=4×50 ms、29.82G FLOPs。作者报告低照度更稳、模板可重建性更低，但 EFace 只有 100 训练/31 测试身份，跨设备/跨条件未验证。两者共同说明：**“快”可以来自轻量 RGB，也可以来自事件传感**；但事件人脸的证据规模远小于 RGB，不能把 EER 5.35 直接外推到真实门禁/支付场景。

#### Different Defects：数据清洗不是“越多越好”，而是“缺陷相关”

这篇对 MS1MV3（5.18M 图/93,431 身份）做受控审计：重复、身份拆分、裁剪错误、多人脸歧义、无效内容五类缺陷。去重 D7 移除 15.44% 图像，平均验证 97.20→97.27，达到基线所需步数少 23.7%；随机移除同量图像没有增益；身份合并少 21.8% 步；身份合并+去重少 24.3% 步；而过滤全部图像有效性缺陷并没有同样收益。

它给 Clover 的启发是：**训练数据的“理解”要按缺陷类型审计**，不能把“清洗比例”当作质量指标；随机删数据可能只减少容量，不减少噪声。人脸领域的偏见、重复、身份拆分同样适用于一般视觉数据集；Clover 的数据 provenance 审计应记录缺陷类型与干预效果，而不是只记数据量。

#### TAG 与 ActFER：表情识别从“标签”转向“证据”，但证据仍是代理

TAG 把表情推理约束到 AU 接地：SFT 于 310K AU 接地样本，再用 AU-IoU 奖励的 GRPO。统一 SFT 平均 74.34%，高于 InternVL3-38B 65.11 与 GPT-5 62.93；逐数据集 RL 平均 83.78%（RAF-DB 92.80/FERPlus 91.50/AffectNet 67.03）；AU IoU 60.24；去掉 bbox 平均降 1.98；仅用 RLVR 会把 AU IoU 从 46.73 降到 43.46——**任务奖励会让模型牺牲视觉接地**，只有 AU 奖励才同时提升准确率与证据。

ActFER 则把 FER 改成主动取证：动态人脸检测/对齐、选择性放大、视觉 CoT 推理 AU 与情绪。两者共同说明：**表情理解需要局部证据与主动观察**，但 AU 检测器只是肌肉活动的统计代理，不是生理测量；MLLM 推理成本高，表情标签本身有文化与主观歧义。Clover 若把“情感”纳入世界理解，必须把 AU/区域证据、文化/个体差异与不确定性一起报告，不能用单标签准确率代替。

#### UniCon-Former 与 EgoEV-HandPose：手势仍是碎片化能力

UniCon-Former 用 CNN 卷积投影 + Transformer 全局注意力做动态手势识别，兼顾局部/全局与效率；EgoEV-HandPose 用第一人称双目事件相机联合 3D 双手姿态与手势，KeypointBEV 融合 + 迭代重投影缓解 ego-motion/单目深度歧义。两者都还是摘要级，手势类别/数据集有限，不是连续手语或通用交流理解。它们说明手势识别目前分落在 RGB/事件/骨架/可穿戴等不同传感与任务定义上；**没有统一的“手势理解”基准**，更谈不上从手势推断意图/社会角色。

**本节结论：** 人脸/表情/手势应拆成三条验收轴：**身份**（1:1/1:N、偏见、阈值、低分辨率/事件/热成像）、**情感**（AU/区域证据、文化/个体差异、不确定性）、**交流手势**（RGB/事件/骨架、连续/孤立、意图）。2026 证据显示：人脸识别在移动端/事件/热成像上继续扩展，但偏见与数据缺陷仍是结构性问题；表情识别正从标签转向 AU 接地推理，但 AU 是代理、RL 可能损害接地；手势识别仍碎片化。Clover 若声称“理解人”，必须分别报告身份公平性/阈值、表情证据与不确定性、手势任务定义；一个“社会理解”总分不能替代这三轴。

### 视觉阅读：OCR 已从“转写”扩展为布局、表格、公式与多语言解析

| 方法 | 一手来源 | 机制与可核查证据 | 边界与反假设 |
|---|---|---|---|
| MinerU2.5 | [2509.22186](https://arxiv.org/abs/2509.22186v2) · [官方代码](https://github.com/opendatalab/MinerU) · 正文选读 | 1.2B 文档解析 VLM；两阶段：下采样图做全局布局，再在原图原生分辨率 crop 上做局部识别；vLLM 异步后端、两阶段解耦、按布局类型动态调整 repetition penalty；作者报告多基准 SOTA 且计算开销显著更低 | `L1` 文档标注；两阶段依赖布局正确性，布局错会传导；高分辨率 crop 的吞吐/显存与端到端延迟需实测；论文未给独立 limitations 节；不是通用场景文字/视频 |
| olmOCR 2 | [2510.19817](https://arxiv.org/abs/2510.19817v1) · [官方项目](https://olmocr.allen.ai/) · [代码](https://github.com/allenai/olmocr) · 正文选读 | 7B VLM 用可验证奖励 RL（RLVR）训练，奖励是多样二元单元测试；合成多样版式文档并提供 HTML 真值与测试用例；olmOCR-Bench 报告 SOTA，公式/表格/多栏改进最大；模型/数据/代码开放 | `L1` OCR/结构监督 + 合成数据；单元测试覆盖决定奖励上限；英文文档为主；作者报告失败包括不生成 EOS 导致重复；edit distance 可奖励错误阅读顺序；版面/阅读顺序与文字识别须分开；许可需逐项核 |
| PolyOCR-Venus | [2609.37712](https://arxiv.org/abs/2609.37712v1) · 正文选读 | 统一 OCR 基础模型家族（2B/9B/2.7B 三种配置）；共享指令框架 + 60M 实例三阶段数据引擎；SFT 后接 CGPO（验证器 GRPO + 按教师可靠性路由的 on-policy 蒸馏）；OCRBench v2.1、CC-OCR、OmniDocBench v1.6、MDPBench 上 SOTA/竞争力 | `L1/L2`；2B/9B 冻结视觉编码器/对齐器，2.7B 用 ViT+Qwen2.5；验证器/judge 依赖（Gemini-3.5-Flash-Lite）；OCRBench v2.1 修订使旧分数不可直接比；作者未来工作承认细粒度感知/定位/识别与真实环境泛化仍待加强 |
| MEVL-STP | [2609.28857](https://arxiv.org/abs/2609.28857v1) · 正文选读 | 两阶段任意形状场景文字 spotting：六冻结编码器（CLIP/DINOv2/SigLIP/EVA-CLIP/SAM/ConvNeXt）+ FPN/通道注意力/渐进尺度扩张输出多边形掩码；Qwen3-VL-8B + LoRA（约 0.2% 参数）识别 crop；无需合成预训练，CTW1500 91.99% F1/85.86% H-mean，Total-Text/ICDAR2015 强结果 | **作者自述**：六编码器推理 2.2B 参数，1024² 输入 3601 GFLOPs（SAM-ViT-H 占 76%），H100 检测/全管线 3.18/1.13 FPS；纹理背景误检降低 Total-Text 精度；逐 crop 识别延迟随实例数增长；`L2` VLM；非端侧实时 |

> OmniDocBench 的版本边界与文档解析评分见[评测方向](evaluation-and-benchmarks.md#evaluation-frontier)。

#### PaddleOCR-VL：0.9B 的紧凑解析器，速度与精度必须按后端和任务拆开

- **一手来源：** [固定版本](https://arxiv.org/abs/2510.14528v4) · [官方代码](https://github.com/PaddlePaddle/PaddleOCR)。`PRIMARY_PAPER` / `OPEN_SOURCE`。
- **机制：** NaViT 风格动态分辨率视觉编码器 + ERNIE-4.5-0.3B 语言模型；布局分析与元素识别；支持文本、表格、公式、图表，109 种语言。
- **输入与学习来源：** 文档图像与 OCR/结构标注 `L1`；语言模型自带 `L2` 世界知识；合成/真实数据配比须按报告分列。
- **实际证据：** 作者报告页面级与元素级公开/内部基准 SOTA，并给出 SGLang/vLLM/FastDeploy 的端到端吞吐/每页延迟表；0.9B 规模便于部署。**但**内部评测集参与 hard-case mining 并合成训练样本，内部分数非独立；30M 公开/合成数据与 OmniDocBench 页面是否重叠未披露。
- **不能推出：** 内部 SOTA 不是独立泛化；公开 OmniDocBench 分数需先做重叠核查；“109 语言”不等于每语种同等精度；页面级解析含布局与阅读顺序，元素级识别不含语义推理；吞吐数字依赖后端、批大小与页面复杂度；本仓库未实测。
- **阅读深度：** 正文选读：架构、评测表、吞吐表与结论；未复核全部附录；未运行权重。

#### dots.ocr：单 VLM 联合布局、文字与关系，但仍是文档域

- **一手来源：** [固定版本](https://arxiv.org/abs/2512.02498v4) · [官方代码](https://github.com/rednote-hilab/dots.ocr)。`PRIMARY_PAPER` / `OPEN_SOURCE`。
- **机制：** 一个 VLM 端到端联合学习布局检测、文字识别与关系理解；1.2B 视觉编码器 + 1.7B 语言解码器（Qwen2.5-1.5B 基座、tied embeddings）；约 300K SFT 样本；人类在环（HITL）用 Qwen2.5-VL-7B 作为 oracle 诊断定位/内容/类型/遗漏/幻觉。
- **输入与学习来源：** 文档图像 + 布局/文字/关系标注 `L1`，合成语料；语言模型含 `L2`。
- **实际证据：** 作者报告 OmniDocBench SOTA；新基准 XDocParse 覆盖 126 语言，约 10% 相对提升；正文失败案例显示模型可能把四个独立表格合并成一个跨页框。
- **不能推出：** 联合训练减少级联误差，但没有消除布局/识别/关系三类误差，需分项报告；XDocParse 由作者提出，需独立复现；文档域外（自然场景、视频字幕）未覆盖。
- **阅读深度：** 正文选读：架构、数据引擎、OmniDocBench 表与失败案例；未复核全部附录；未运行权重。

### 姿态、计数与几何：结构化输出补上“多少、在哪里、什么形状”

| 方法 | 一手来源 | 机制与可核查证据 | 边界与反假设 |
|---|---|---|---|
| ViTPose | [2204.12484](https://arxiv.org/abs/2204.12484v3) · [官方代码](https://github.com/ViTAE-Transformer/ViTPose) | 普通非层级 ViT + 轻量姿态解码器；100M–1B 参数可扩展；COCO test-dev 81.1 mAP；大模型知识可经 knowledge token 迁到小模型 | `L1` 关键点；2D 姿态不含 3D/接触/意图；遮挡与多人拥挤另测；吞吐-精度 Pareto 依赖输入分辨率与骨干 |
| Sapiens | [2408.12569](https://arxiv.org/abs/2408.12569v3) · [官方代码](https://github.com/facebookresearch/sapiens) | 3 亿人体图像自监督预训练，再微调 2D 姿态、部位分割、深度、表面法线；0.3–2B、原生 1K 推理；报告 Humans-5K +7.6 mAP、Humans-2K +17.1 mIoU、Hi4D 深度相对 RMSE 改善 22.4%、THuman2 法线角误差改善 53.5% | 人体中心、`L1` 下游标签；自监督预训练不等于无先验；人体先验不能直接迁移到一般物体/场景；1K 推理成本高 |
| PnP-Transformer | [2610.26096](https://arxiv.org/abs/2610.26096v2) · [官方代码](https://github.com/ebylmz/pnp-transformer) · 正文选读 | 用神经姿态求解器替代迭代式 PnP-RANSAC：输入半稠密 2D-3D 对应场与置信度，单次前向回归 6D 物体姿态；七个 BOP 核心集平均 AR 41.2%、0.46 s/obj；同一对应模块换 EPnP-RANSAC 达 52.2% AR（+60 ms/obj，0.52 s/obj），在 6/7 数据集更好 | `L1` 6D 位姿/对应监督；作者自述失败于无纹理物体（只能靠轮廓）、对称物体多模态歧义、上游检测器误检；0.46 s/obj 不是实时；精度-时延权衡真实存在；对应模块与求解器误差须分开 |
| CountGD | [2407.04619](https://arxiv.org/abs/2407.04619v2) · [项目页](https://www.robots.ox.ac.uk/~vgg/research/countgd/) · 正文选读 | 把开放词汇检测基础模型 GroundingDINO 改造成计数模型，支持文本、视觉 exemplar 或两者组合；作者报告多计数基准 SOTA，文本+exemplar 优于纯文本 | **作者自述局限**：模型不预测计数误差/不确定性；依赖阈值；未系统研究冻结更多 GroundingDINO；`L1/L2`；计数=检测后聚合，密集/遮挡/重复检测会直接变成计数错误 |
| MoGe-2 | [2507.02546](https://arxiv.org/abs/2507.02546v1) · [官方代码](https://github.com/microsoft/MoGe) · 正文选读 | 单图恢复度量尺度 3D 点图；在保持仿射不变相对几何的同时预测 metric scale；用锐利合成标签过滤/补全真实数据以恢复细节 | **作者自述局限**：极细结构（细线、毛发）与前景/背景大尺度差下的直线/对齐结构仍失败；真实世界 metric scale 歧义导致 OOD 偏差；训练含 `L1/L4`；点图不是物体实例或物理状态 |
| SAM 3D | [2511.16624](https://arxiv.org/abs/2511.16624v2) · [官方项目](https://ai.meta.com/sam3d/) · [代码](https://github.com/facebookresearch/sam3d) · 正文选读 | 单图生成物体几何、纹理与布局；人类+模型在环标注管线（含 3D 艺术家与 DPO 式数据回收），合成预训练 + 真实对齐；作者报告真实物体/场景人类偏好至少 5:1 胜率 | 作者自述：粗形状 64³、每占用 voxel 最多 32 splats，细结构/手/脸会失真；一次只预测一个物体，不处理接触、物理稳定、互穿或共面布局；纹理在未知位姿下预测，旋转对称物体可能产生错误朝向纹理；生成式补全含先验/幻觉，不是可通行场景重建 |

#### Depth Anything 3：一个普通 Transformer + 深度-射线目标统一任意视图几何

- **一手来源：** [固定版本](https://arxiv.org/abs/2511.10647v1) · [项目页](https://depth-anything-3.github.io/) · [官方代码](https://github.com/ByteDance-Seed/Depth-Anything-3)。`PRIMARY_PAPER` / `OPEN_SOURCE`。
- **机制：** 用普通 DINO 编码器作骨干，联合预测尺度感知深度与逐像素射线；教师-学生训练继承 Depth Anything 2 的细节/泛化；自适应跨视图注意力；单图、多视图、视频统一输入。
- **输入与学习来源：** 仅公开学术数据集；深度/位姿/多视图几何监督 `L1/L4`；教师模型提供伪标签；不是无监督 `L0`。
- **实际证据：** 作者新建视觉几何基准，报告相机位姿精度比 VGGT 平均高 44.3%、几何精度高 25.1%，单目深度优于 DA2；同一骨干支持前馈新视图合成。
- **不能推出：** 静态场景为主，作者将动态场景列为未来工作；度量尺度、位姿与重建的误差须分项；几何正确不等于材质、接触、因果或物体身份；公开数据训练仍可能有域偏差。
- **阅读深度：** 正文选读：方法、benchmark、结论与讨论；未复核全部实验；未运行复现。

#### UniCounting：固定词表、无图像查询的多类别计数，训练参数极少

- **一手来源：** [固定版本](https://arxiv.org/abs/2610.08379v1)。`PRIMARY_PAPER`。
- **机制：** 冻结 SAM 2.1 生成掩码，冻结 DINOv2/OpenCLIP 提供关系与类别特征；只训练 3,267 参数的关系头预测同实例亲和度，再做稀疏图、代表选择、标注与背景边距准入；不训练计数/密度图目标。
- **输入与学习来源：** RGB 图像；固定类别词表；实例掩码派生监督（`L1`），冻结基础模型的上游训练另记。
- **实际证据：** COCO clean500 上点估计向量 L1 误差与缺席类假质量低于校准 OWLv2-All80；在匹配解码器下，学习关系优于掩码包含、IoU、CLIP、DINO；报告 OmniCount-sub/FSC-147/CARPK 迁移诊断。
- **不能推出（作者自述）：** 固定词表、图像查询无关，不能处理任意开放词汇；只评 500 图 COCO 与 OmniCount-sub，未评 MUCCA/PrACo++；clean500 是 COCO val2017 子集，基础模型预训练重叠未知；候选池在 IoU 0.5 只召回 62.4% 非忽略实例；关系头降低向量误差但不最小化总计数 MAE，merge error 高于 mask IoU/containment；推理仍需冻结 SAM2.1/DINOv2/OpenCLIP 与二次 pair scoring。
- **阅读深度：** 正文选读：方法、消融、Discussion/Limitations；未复核全部附录；未运行复现。

<a id="spatial-state-2026"></a>

### 空间状态：在线 SLAM、里程计与建图

前面的几何表回答“单帧或一组视图能恢复什么”，但没有回答“相机持续移动时，状态是否保持、误差如何累积、何时应当报失效”。对 Clover 而言，这不是追踪的附属功能：追踪给出对应与短时轨迹，SLAM/里程计要给出**持续的相机状态、地图与不确定性**，并在地图过期、尺度不可观测或跟踪失败时显式暴露。此前正文只有 ORB-SLAM3、DROID-SLAM 等经典基线；下表补 2026 年可核查的一手工作，并把“精度、失败模式、语义记忆、端侧成本”分开。

| 方法 | 一手来源 | 机制与可核查证据 | 边界与反假设 |
|---|---|---|---|
| UniSim-SLAM | [2608.01706](https://arxiv.org/abs/2608.01706v1)（ECCV 2026） · [项目页](https://vision3d-lab.github.io/unisim-slam/) · 正文选读 | 前端两视图关键帧跟踪，后端周期多视图子图细化；把异构局部坐标/尺度统一到多级 `Sim(3)` 因子图（view-to-view、view-to-submap、submap-to-submap）；TUM RGB-D 未标定平均 ATE 0.032 m，7-Scenes 0.020 m；作者报告相对此前最好结果降 38.5%/45.9% | 室内静态基准；前端 VGGT 较重，跟踪延迟高于专用两视图管线；依赖深度统计锚定尺度；无动态物体/开放语义；不是纯视觉度量尺度保证 |
| FFVO | [2609.13733](https://arxiv.org/abs/2609.13733v1) · 正文选读 | 冻结 π³ 的特征聚合与点图模块，只训练位姿解码分支；紧凑 camera token、局部→全局层次时序解码、中间轨迹监督；WOD ATE 0.862 m（π³ 1.150、VGGT 1.359、SCE-SLAM 0.915）；KITTI 平均 12.96 m（DA3-Streaming 18.63、π³-Long 21.18）；自建 PDD 2.494 m（π³-finetuned 5.720） | 只输出位姿，不建语义地图；训练用自建 PDD（非公开），8×B200 约 5 天；WOD 上无增强变体 0.714 m 反而更低，作者归因于 85° 拼接与前置相机 FoV 不匹配；作者自述高速（>55 mph）、极端天气、低光仍失败；标定/同步假设未消解 |
| VGGT-GS SLAM | [2609.19628](https://arxiv.org/abs/2609.19628v1) · 摘要 | 未标定单目视频：VGGT 位姿/深度先验 + 子图可微 BA，联合优化相机与 3D Gaussian 地图，并用解析 Jacobian 优化共享内参和径向切向畸变；Gaussian-native alignment 做子图尺度细化与回环候选验证；作者报告室内基准定位与渲染一致改善 | Gaussian 地图是外观表示，不是物体/语义/物理状态；静态场景与回环假设；摘要未给跨数据集数值；未复核代码/权重；建图成本与实时性未独立测 |
| FoundationVIO | [2610.14951](https://arxiv.org/abs/2610.14951v1) · 摘要 | 指出 GFM 的几何预测只局部一致到尺度；把惯性测量与 GFM 预测放入因子图恢复度量尺度，报告里程计估计改善 | **不是纯视觉**：需要 IMU（`L4`）；仍继承 GFM 的深度/位姿误差；度量尺度来自惯性激励与可观测性，不是从 RGB 语义推出来的 |
| Failure or Drift? | [2608.30690](https://arxiv.org/abs/2608.30690v1)（NeuSLAM@ECCV 2026） · [代码](https://github.com/abhaythomas/master_thesis_vslamlab_robustness) · 正文选读 | 在图像空间、几何感知与复合损坏下比较 ORB-SLAM2、DPVO、DROID-SLAM；把“无有效轨迹”与“仍输出但漂移”分开；ORB-SLAM2 仅在 37/63、15/23、10/15 次损坏尝试中给出可评估轨迹，学习跟踪器全部保持输出但几何损坏下 APE 常超 100 m；排序随损坏模型反转（DPVO 在 30/43 图像空间设置更好，DROID 在 33/33 几何感知、14/15 复合设置更好）；真实 4Seasons 的雨/冬支持复合代理排序，傍晚照明反转 | 单一 KITTI 轨迹、每条件一次执行；未测运行时、地图、重建、能耗；4Seasons 是语义匹配而非同路线配对；只说明相对行为，不是绝对误差预测；合成代理不能当部署误差标定 |
| MomentBA | [2609.13691](https://arxiv.org/abs/2609.13691v1) · 正文选读 | 把匹配相似度响应的二阶空间矩转成各向异性协方差，作为每条对应的信息矩阵进入可微 BA；EuRoC 平均 `t_rel` 0.0045、`r_rel` 0.0317（MAC-VO 0.0029/0.0526，常数协方差 0.0069/0.0429）；TartanAir Hard 0.1823/0.0308（MAC-VO 0.2260/0.0774） | 单目特征法、关闭回环；EuRoC 平移误差仍高于 MAC-VO，不能称全面 SOTA；无运行时/地图/动态物体；估计的是局部匹配不确定性，不是模型认知不确定性 |
| HuMemSLAM | [2609.17168](https://arxiv.org/abs/2609.17168v1) · 摘要 | 人类记忆启发的语义地点识别：自下而上感知证据与自上而下上下文推理双向结合，接入 ORB-SLAM3；作者报告检索精度与延迟改善 | 只解决地点识别/回环候选，不解决度量尺度、动态物体或地图语义；依赖预训练语义特征与阈值；感知别名与外观变化仍需独立测；摘要未给跨数据集表 |
| OASIS | [2610.30589](https://arxiv.org/abs/2610.30589v1)（ACM MM 2026 oral） · 正文选读 | 锚点中心 episodic memory：LLM 过滤锚点、VLM 按需验证代表帧、瞬态视觉缓冲重定位移动物体；OpenLex3D 6.58 mAP；HOV-SG 功能区域 Top-5 57.7%；Sr3D+ A@0.1/0.25 44.0/37.4（CORE-3D 41.8/35.6，Hard split CORE-3D 41.3 更高）；HM3D 导航 SR 85.9%/81.5%/77.4%（静态/锚内移动/跨锚移动，DualMap 70.5/64.8/60.3）；真实 60 次试验 11 次失败 | 依赖 GPT-5.2 与 Gemini 3 Pro（`L2`，API 时点快照）；室内家庭与稳定锚点假设；稀疏锚点记忆不保证度量几何；Hard 长程关系弱于专用方法；不是端到端纯视觉 |
| RawSLAM | [2609.20589](https://arxiv.org/abs/2609.20589v1) · 摘要 | 首个在线 Gaussian SLAM 直接在单曝光 16-bit 线性 HDR 图像上跟踪与建图；无 MLP 的对数 Gaussian 颜色参数化、Reinhard 压缩光度目标、结构引导空间梯度加权 | 输入是 raw/HDR（不是普通 8-bit RGB），跨传感器；静态场景；外观地图非语义；摘要未给大规模数值；未复核代码/权重 |
| RingNav | [2610.19044](https://arxiv.org/abs/2610.19044v1) · 正文选读 | 10.6k 参数朝向估计器，把持久状态约束在 `S¹`，只学习相邻帧转角；CompTest 转角 MAE 0.589°（DPVO 0.177、DROID 0.198），HDH-Bench 0.417°（0.106/0.148）；但 8 字节状态、GAP8 上 33.4 Hz、0.49 MiB，相同帧转角恰为 0、序列反转精确抵消；无微调迁移到 Crazyflie | 精度明显低于完整视觉运动估计；固定几何更新无法纠正错误/不可观测的视觉转角；只估计朝向，不给位置/地图；合成训练 + 真实飞行验证有限 |
| DAPEVO | [2609.30947](https://arxiv.org/abs/2609.30947v1) · 摘要 | RGB-事件双模态 VO：在共享 patch 上分别估计图像/事件对应，学习标量门融合相关证据，再进入共享递归细化与 BA；支持仅有事件的退化模式 | 需要事件相机（不是单目 RGB）；无公开代码/权重核验；事件-图像时间同步与标定；未给跨数据集表；不是语义/地图系统 |
| Gaussian Splatting 综述 | [2610.17513](https://arxiv.org/abs/2610.17513v1) · *Pattern Recognition* 172:115120 (2026) · 摘要 | 把 GS 重建分为单次生成、动态表示、效率/压缩、流式/沉浸系统、GS-SLAM 五类，明确区分“渲染已有表示”与“构建/更新/维护表示”，并连接端到端管线与工具 | 综述不提供新实验；实时渲染不等于实时建图；各工作的基准、真值、硬件不一致；SLAM 分类仍以静态室内为主 |

#### UniSim-SLAM：低延迟前端 + 多视图后端，统一在 `Sim(3)` 图上

UniSim-SLAM 的关键不是“又一个前馈 SLAM”，而是把两种推理制度放进同一个优化问题：两视图推理延迟低、时间连接密，但几何约束弱、长期漂移；多视图子图约束强，但要等帧累积，且子图不重叠时修正无法传播。作者用 `Sim(3)` 多级因子图同时优化全局关键帧位姿与子图位姿，并把深度统计作为尺度锚。TUM RGB-D 未标定平均 ATE 0.032 m，优于 ViSTA-SLAM 0.052、VGGT-SLAM 0.061；7-Scenes 0.020 m，优于 0.037/0.049。这个结果同时暴露经典基线的边界：ORB-SLAM3 在该表的 9 条 TUM 序列中有 5 条无有效轨迹，不能把“经典几何更可靠”当成默认前提。

但它的证据仍是室内静态、短序列、离线评估；前端 VGGT 的规模使跟踪延迟高于专用两视图系统，作者也承认换低延迟前端后才更接近实时。更重要的是，`Sim(3)` 对齐后的 ATE 不检验绝对尺度是否正确——尺度由深度统计锚定，而不是由视觉观测唯一确定。Clover 若把“空间状态”作为世界理解的一部分，必须把**相对几何精度、绝对尺度、失败检测**分开验收。

#### FFVO：长时程位姿可以只训解码器，但失败条件没有消失

FFVO 冻结 π³ 的特征聚合与点图模块，只训练位姿解码分支：14 个 camera token 聚合全局上下文，局部窗口（20 帧）先做短程运动聚合，再由全局阶段整合，并加中间轨迹监督。WOD 上 ATE 0.862 m，优于 π³ 的 1.150、VGGT 的 1.359、SCE-SLAM 的 0.915；KITTI 平均 12.96 m，优于 DA3-Streaming 18.63 与 π³-Long 21.18；自建 PDD 上 2.494 m，远低于 π³-finetuned 的 5.720。消融显示局部窗口时序注意力贡献最大，说明“长时程”不是把整段视频一次性塞进注意力，而是分层处理短程歧义与全局一致性。

代价同样明确：只输出位姿、不建地图；训练依赖自建 PDD 与 8×B200 约 5 天；作者自述高速（>55 mph）、极端天气、低光仍会失败。它证明的是“位姿解码器可以高效适配冻结几何骨干”，不是“视觉里程计在真实开放世界已可靠”。对 Clover 的启发是架构性的：把状态估计拆成可复用的几何表征与轻量状态头，可能比端到端重训整个几何模型更接近原生效率；但状态头仍需要独立的失败检测与尺度证据。

#### Failure or Drift?：显式失败与静默漂移必须分开报告

这篇工作对 Clover 的评测协议威胁最大。它发现：在干净 KITTI 上三种系统都能给出轨迹，但损坏输入下 ORB-SLAM2 经常直接无有效轨迹（图像空间 37/63、几何感知 15/23、复合 10/15），而 DPVO/DROID-SLAM 几乎总是继续输出，只是几何损坏下 APE 常超过 100 m。对下游系统，后者更危险：没有“跟踪丢失”信号，错误位姿会静默进入控制/规划。

更关键的是，方法排序随损坏模型反转：图像空间的亮度/对比度代理下 DPVO 在 30/43 个配对设置更好；几何感知代理下 DROID-SLAM 在 33/33 个设置更好；复合代理下 14/15 更好。真实 4Seasons 中雨与冬支持复合代理的排序，但傍晚照明反转（合成代理偏向 DROID-SLAM 5.51 m，真实数据偏向 DPVO 10.85 m）。这说明“合成鲁棒性分数”不能当部署误差标定；评测至少要同时报告**可用性（是否输出）、有界性（误差是否受控）、代理-真实一致性**。Clover 的任何“纯视觉世界理解”主张，如果只在干净基准上报告成功率，都会重复这个错误。

#### MomentBA 与 RingNav：不确定性建模和结构化状态是两条相反的路

MomentBA 把匹配响应的二阶空间矩变成各向异性协方差，让边缘、重复纹理、运动模糊产生的方向性歧义进入 BA 的信息矩阵。EuRoC 上平均平移 0.0045、旋转 0.0317，优于常数协方差的 0.0069/0.0429，但平移仍不如 MAC-VO 的 0.0029；TartanAir Hard 上 0.1823/0.0308 优于 MAC-VO 0.2260/0.0774。它的价值不是全面 SOTA，而是证明**对应不确定性可以从匹配几何中解析得到**，不必额外训练协方差网络；边界是只覆盖局部匹配不确定性，且关闭回环、未测运行时/地图。

RingNav 走另一极端：不追求完整状态，只保留任务需要的朝向，把状态约束在 `S¹`，只学习相邻帧转角，持久状态仅 8 字节。代价是精度显著低于完整视觉运动估计（CompTest 0.589° vs DPVO 0.177°/DROID 0.198°；HDH-Bench 0.417° vs 0.106°/0.148°），但它在 GAP8 上 33.4 Hz、0.49 MiB，相同帧转角精确为 0、序列反转精确抵消，并能无微调迁移到真实 Crazyflie。它说明“原生超快”不必等于大模型蒸馏：**把状态流形和任务约束写进结构**，可以用极小容量换取可预测的误差与成本；但固定几何更新无法纠正错误的视觉转角，结构化先验不能替代观测质量。

#### OASIS：语义锚点记忆能重定位，但不是几何状态

OASIS 把室内环境压缩成少量稳定语义锚点，每个锚点保存语义描述、视觉特征与几何状态；检索时 LLM 先过滤锚点，VLM 再按需验证代表帧，导航中用瞬态视觉缓冲重定位移动物体。它在 OpenLex3D 取得 6.58 mAP，HOV-SG 功能区域 Top-5 57.7%，Sr3D+ 总体 A@0.1/0.25 44.0/37.4，HM3D 导航 85.9%/81.5%/77.4%（静态/锚内/跨锚），真实 60 次试验 11 次失败。跨锚移动场景相对 DualMap 的提升最大（77.4% vs 60.3%），说明“被动收集的瞬态观察”可以替代主动反复扫描。

但它不是纯视觉几何状态：依赖 GPT-5.2 与 Gemini 3 Pro，锚点假设室内稳定大物体，稀疏记忆不保证度量几何，Hard 长程空间关系还弱于 CORE-3D。它更适合被 Clover 当作**语义记忆层的对照**：如果“理解”包含“记得东西在哪、被移动后还能找到”，那么记忆必须同时保存语义、外观与几何，并显式标注哪一层在何时失效；单靠 VLM 检索或单靠 SLAM 地图都不够。

**本节结论：** 2026 年的空间状态研究分成三条互不替代的路线：前馈几何 + 后端优化（UniSim-SLAM、FFVO）、Gaussian 外观地图（VGGT-GS、RawSLAM）、语义锚点记忆（OASIS、HuMemSLAM）。它们在静态室内/驾驶基准上已经很强，但没有一条同时满足**纯 RGB、绝对度量尺度、动态场景、开放语义、显式失败检测、端侧实时**。单目尺度在结构上不可唯一观测，FoundationVIO 必须引入 IMU 才能锚定；Gaussian 地图是外观而非物体/物理状态；语义记忆依赖 LLM/VLM 与室内锚点假设。对 Clover 的验收要求因此不是“跑通一个 SLAM”，而是把相对轨迹、绝对尺度、地图语义、失败/漂移、端侧成本分成五项独立证据；任何一项缺失，都不能用另一项的高分替代。

<a id="correspondence-flow-2026"></a>

### 对应、光流与匹配：运动、深度与位姿的共同底座

识别与追踪回答“是什么、在哪里”，但要恢复运动、深度、相机位姿和 3D 结构，先要解决**对应**：同一物理点在两帧/两视图/多视图中的位置关系。对应错了，后续的 SLAM、跟踪、分割传播和物理推断都会以自洽的方式错下去。本轮补 9 篇 2026 年工作，覆盖光流架构、基础模型特征、跨视图匹配、多视图匹配、硬件求解与零样本位姿；共同趋势是“去任务专用偏置、复用冻结基础特征、从两视图走向多视图”，但极端运动、遮挡、低纹理和尺度变化仍是共同失败面。

| 方法 | 一手来源 | 机制与可核查证据 | 边界与反假设 |
|---|---|---|---|
| FreeFlow | [2609.11486](https://arxiv.org/abs/2609.11486v1)（ECCV 2026） · [项目页](https://github.com/msu-video-group/freeflow) · 正文选读 | 去掉光流专用组件（相关体、特征 warp、迭代细化），用单个前馈层次 Transformer：窗口注意力、移位窗口、低分辨率全局注意力；Sintel Clean/Final 0.68/1.48 EPE，KITTI-15 3.23 Fl-all，Spring EPE 0.278/Fl 1.048/WAUC 95.235；作者报告随容量一致扩展 | 仍需跨视图补全预训练 + 光流微调；极端运动/遮挡/细边界未消解；Spring 1080p 推理成本不低；不是多帧时序模型；EPE 低不等于下游位姿/分割可靠 |
| Foundation Model Driven Optical Flow | [2610.26690](https://arxiv.org/abs/2610.26690v1)（NeurIPS 2026 RoCo-Spring workshop） · 正文选读 | 冻结 DINOv2 + Depth Anything V2，经 DPT 解码与一次 coarse-to-fine 细化；仅用 Chairs/Things 训练时 Sintel Final 2.37 EPE（FlowSeek 2.52），KITTI train 1.248 EPE/4.01% F1-all；RoCo-Spring 鲁棒分 1.1038（低于 SEA-RAFT 0.4584、GMFlow 0.8015） | 基础特征并非为光流优化；极端运动、严重外观变化、遮挡、细运动边界会退化；Spring 鲁棒分不如专用小模型；训练配置与基线不同，不能隔离架构/数据；单次细化不是测试时缩放 |
| SGFormer | [2608.03423](https://arxiv.org/abs/2608.03423v2) · 正文选读 | 检测器无关的层次 Transformer，用浅层结构相似性引导注意力，缓解“注意力发散”（高置信匹配跑到非重叠区）；HPatches 总体 MMA 0.65/0.92/0.95（LoFTR 0.62/0.91/0.93），光照变化 1px +11.76%；MegaDepth 匹配 98.2%，Aachen-Day-Night 夜间定位最好 | MegaDepth 训练、HPatches/MegaDepth/Aachen 评估；大幅视角/尺度/非刚性形变下结构先验失效，视角变化 1px 略低于 LoFTR；匹配数量与几何显著性可能冲突；不是多视图/时序 |
| MVLoMa | [2610.31321](https://arxiv.org/abs/2610.31321v1) · [项目页](https://kosmoresearch.github.io/MVLoMa/) · 正文选读 | 星图多视图匹配：冻结 DA3-G 几何编码器 + LoMa 初始化，中心图像与 24 邻居一次匹配；25 视图相对位姿 AUC@1°/5°/10° 宏平均 58.65/85.41/90.99（LoMa-L 57.40/84.44/90.06）；作者报告比逐对匹配快 2.20× | Mip-NeRF 360 上密集两视图 RoMa 的 AUC@1° 仍更强；Tanks and Temples 上 LoMa-L 最好；依赖冻结几何特征质量，无纹理区仍稀疏；邻居间不直接交换信息；2–8 视图训练外推到 25 视图非单调；内存随关键点/视图增长 |
| Co-occurrence-Aware Quadratic Assignment | [2609.17905](https://arxiv.org/abs/2609.17905v1) · 摘要 | 把关键点匹配写成二次分配（考虑两对匹配的共现），用 Ising machine 求解 NP-hard 组合优化；面向视觉 SLAM 前端，目标是在多个近似代价候选间选对匹配 | 需要专用 Ising 硬件/求解器；摘要未给大规模 SLAM 端到端数值；二次项构造与超参未核；不是学习式匹配；实时性依赖硬件 |
| Cross-View Feature Matching 综述 | [2608.11093](https://arxiv.org/abs/2608.11093v1) · 摘要 | 跨视角匹配的统一分类（特征提取、单类型/多类型匹配器、VFM 方法、训练/评测），并在统一数据集/协议下做基准与基础模型视角分析 | 综述不提供新方法；跨视角定义/数据划分仍多样；统一协议下的结论不能直接外推到所有下游；未覆盖视频时序匹配 |
| SFVO | [2609.21754](https://arxiv.org/abs/2609.21754v1) · 摘要 | 立体视觉里程计：复用预训练立体匹配与光流模型，解耦置信度引导，双向 PnP 估计位姿；利用双目天然度量尺度 | 需要标定双目；依赖预训练匹配/光流质量；摘要未给跨数据集表；动态物体/低纹理未解；不是纯单目 |
| Optical Flow from Photons (QuantaFlow) | [2608.00499](https://arxiv.org/abs/2608.00499v1) · 摘要 | 首个直接从 SPAD 单光子二值流估计稠密光流的框架；用运动感知聚合解决固定坐标累积导致的运动模糊，避免“先聚合后估计”的循环依赖 | 需要 SPAD 传感器（不是普通 RGB）；光子噪声/极低照度；摘要未给基准数值；不是消费级相机可部署 |
| B2TFPose | [2609.06726](https://arxiv.org/abs/2609.06726v1)（BMVC 2026） · 正文选读 | 训练-free 零样本 6DoF：单个冻结 DINOv3 ViT-L/16；测地线 NMS 选视角多样模板、RRC 渲染引导重对应、多掩码消歧；BOP 七数据集平均 AR 40.7（FoundPose 37.2），加 RRC+MegaPose 56.4（FoundPose 55.0）；0.32 s/0.45 s（RTX 3090，TUD-L） | 测试时需要物体 CAD 模型；重遮挡/密集堆叠退化（LM-O/IC-BIN 不如 FoundPose）；依赖 CNOS 分割；模板渲染 1944/物体；不是无模型开放世界；单物体位姿 |

#### FreeFlow：去掉光流专用偏置，架构本身能否承担运动估计？

FreeFlow 的挑战很直接：过去十年光流网络依赖相关体、特征 warp、迭代细化等任务专用归纳偏置；如果这些偏置不是必需，那么大一统的视觉 Transformer 就应能直接学运动。它把模型做成单个前馈层次 Transformer，只用窗口/移位窗口/低分辨率全局注意力，在 Sintel Clean/Final 取得 0.68/1.48 EPE，KITTI-15 3.23 Fl-all，Spring EPE 0.278、Fl 1.048、WAUC 95.235，均为强结果；消融显示窗口 + 移位窗口 + 全局注意力组合最佳，模型随容量一致改善。

但“去偏置”不等于“无先验”：它仍用跨视图补全预训练（ARKitScenes/MegaDepth/3DStreetView）学习对应，再做光流微调；极端运动、遮挡、细边界仍是失败面；Spring 的高分辨率推理成本也不低。它给 Clover 的证据是：**运动估计可以由通用架构 + 大规模对应预训练承担**，不必把光流写成专用模块；但“通用”必须用跨数据集、跨传感器和下游任务验证，单看 Sintel/KITTI 的 EPE 不够。

#### Foundation Model Driven Optical Flow：冻结基础特征可以接近专用光流，但鲁棒性不是自动获得

这篇工作把 DINOv2 的语义特征与 Depth Anything V2 的几何特征经 DPT 解码融合，只训练轻量匹配头与一次细化。仅用 Chairs/Things 训练时，Sintel Final 2.37 EPE，低于 FlowSeek 的 2.52；KITTI train 1.248 EPE/4.01% F1-all，优于 GMFlow 的 1.36/5.17%。它说明**冻结的视觉/深度基础模型已经包含大量可用于对应的结构**，任务专用光流训练可以很轻。

但 RoCo-Spring 鲁棒分 1.1038，明显差于 SEA-RAFT 0.4584、GMFlow 0.8015；作者自述基础特征并非为光流优化，极端运动、严重外观变化、遮挡、细运动边界会退化；训练配置与基线不同，不能把差距全归因于架构。它给 Clover 的启发是“复用冻结几何/语义特征 + 轻量对应头”的路线可行，但必须把**干净精度与损坏鲁棒性分列**；基础模型特征不是鲁棒性的保证。

#### SGFormer：结构引导抑制“注意力发散”，但极端视角仍是边界

SGFormer 指出现有检测器无关匹配器的全局注意力会把高置信匹配分配到非重叠区域（“注意力发散”），于是用浅层结构相似性引导注意力，让匹配集中到几何上可对应的区域。HPatches 总体 MMA 0.65/0.92/0.95，优于 LoFTR 的 0.62/0.91/0.93；光照变化下 1px 提升 11.76%；MegaDepth 匹配 98.2%，Aachen-Day-Night 夜间定位最好。

边界在视角：大幅视角/尺度/非刚性形变会让结构先验本身失效，HPatches 视角变化 1px 略低于 LoFTR；匹配数量与几何显著性也可能冲突（少数位于角点的匹配对位姿更有效）。它说明“结构先验”能替代一部分数据/容量，但不能替代多视图几何；对 Clover 的纯视觉路线，这类先验是廉价的归纳偏置，但必须检测其失效条件。

#### MVLoMa：从两视图到多视图，收益来自共享中心表示而非更多视图本身

MVLoMa 抓住一个系统级错配：匹配器按图像对计算，但 SfM/定位的几何证据是一组互相重叠的视图。它用冻结 DA3-G 几何编码器描述整个星图，把跨视图几何上下文注入局部描述子，再一次匹配中心与所有邻居。25 视图相对位姿 AUC@1°/5°/10° 宏平均 58.65/85.41/90.99，优于 LoMa-L 的 57.40/84.44/90.06；比逐对匹配快 2.20×。

但 Mip-NeRF 360 上密集两视图 RoMa 的 AUC@1° 仍更强，Tanks and Temples 上 LoMa-L 最好；依赖冻结几何特征质量，无纹理区仍稀疏；邻居间不直接交换信息；2–8 视图训练外推到 25 视图非单调；内存随关键点/视图增长。它给 Clover 的证据是：**多视图联合匹配可以减少重复计算并利用互补几何**，但“更多视图”不是单调增益；必须学习视图选择/置信度聚合，而不是假设越多越好。

#### B2TFPose：冻结 DINOv3 + 模板匹配，训练-free 也能做强零样本 6DoF

B2TFPose 把经典“模板匹配 + PnP”用冻结 DINOv3 重做：测地线 NMS 选视角多样模板（1944/物体），稠密 patch 对应 + RANSAC/PnP，再用渲染引导重对应（RRC）和 MegaPose 细化。BOP 七数据集平均 AR 40.7（无细化，FoundPose 37.2），加 RRC+MegaPose 56.4（FoundPose 55.0）；0.32 s/0.45 s（RTX 3090，TUD-L），在训练-free 类别中精度-速度最好。

它的边界很硬：测试时需要物体 CAD 模型；重遮挡/密集堆叠退化（LM-O、IC-BIN 不如 FoundPose）；依赖 CNOS 分割；模板渲染成本随物体数增长；只给单物体位姿，不是开放世界场景理解。它说明**基础模型特征可以把“任务训练”换成“模板 + 对应 + 几何求解”**，但代价是模型/模板先验；对 Clover 的“纯视觉”主张，这是允许的外部结构先验，必须与“从视觉经验学习”分开记账。

**本节结论：** 对应研究在 2026 年出现三个明确转向：光流从“专用偏置”转向“通用 Transformer + 对应预训练”；匹配从“两视图”转向“多视图/星图”；位姿从“任务训练”转向“冻结基础特征 + 模板/几何求解”。这些转向共同支持 Clover 的一个技术判断：**像素到几何的接口可以由通用视觉表征承担**。但它们也共同暴露四个未解问题：极端运动/遮挡/低纹理/尺度变化下的对应可靠性，匹配不确定性是否校准，多视图收益是否单调，以及下游位姿/SLAM/分割是否真的从更低 EPE 中获益。Clover 的验收不能只报 EPE/AUC，必须把对应质量与下游任务、最坏条件、失败检测绑定；否则“匹配分数更高”仍可能对应“世界状态更错”。

<a id="amodal-occlusion-2026"></a>

### 遮挡、非模态补全与不完整证据

真实世界里的物体大多数时候只被看见一部分：被其他物体挡住、被工具覆盖、被画面裁掉。只对可见像素做分割/重建，会把“没看见”误当成“没有”；而直接生成不可见部分，又可能把先验幻觉当成观测。非模态（amodal）感知因此是 Clover 的核心测试场：它要求模型在**证据不完整**时仍给出可检验的完整假设，并标明哪部分是观测、哪部分是推断。本轮补 9 篇 2026 年工作，覆盖 2D 非模态分割、视频非模态、3D 非模态重建与遮挡鲁棒性评测。

| 方法 | 一手来源 | 机制与可核查证据 | 边界与反假设 |
|---|---|---|---|
| OccJEPA | [2610.29061](https://arxiv.org/abs/2610.29061v1) · [代码](https://github.com/zgp110/occjepa) · 正文选读 | 把遮挡当 masking：丢弃物体可见 mask 未覆盖的 token，用冻结 V-JEPA 2.1 predictor 在特征空间补全，轻量头解码为 amodal mask；SAIL-VOS mIoU 78.60，TAO-Amodal AP50 +4.11 val/+4.00 留出 test；隐藏区 mIoU +3.70；单次确定性预测，0.35 s/object vs Diffusion-VAS 11.77 s（33.5×），35.6 vs 903 TFLOPs；仅训练 69M 参数 | 依赖 V-JEPA predictor 的预训练知识（随机初始化只保留约 25%/19% 增益）；可见 mask 主实验用真值，换 SAM2 跟踪 mask 后仍 +4.32 AP50；遮挡 <10% 时像素生成更细；无深度网络；不是物理状态/材质推断 |
| Amodal SAM | [2604.20748](https://arxiv.org/abs/2604.20748v1) · 正文选读 | 在 SAM 上加轻量 Spatial Completion Adapter、目标感知遮挡合成（TAOS）与区域/拓扑正则；统一图像+视频非模态分割；KINS mIoU_f 88.79/mIoU_o 63.12（PLUG 88.10/61.42）；COCOA 84.27/59.94（PLUG 83.23/32.88）；COCOA-cls 87.65/54.34；开放世界 COCOA-cls 83.18（SAMBA 81.82）、D2SA 91.62（90.87）；视频 FISHBOWL 92.74/83.36、MOViD-A 73.06/39.21 | 训练数据由 SA-1B mask + TAOS 合成遮挡，真实遮挡分布未必覆盖；开放世界仍以已知类别/域为主；mIoU_f 可被“只分割可见区”抬高，必须看 mIoU_o；视频依赖逐帧/跟踪；不是 3D/物理 |
| OccSAM-Bench | [2604.11711](https://arxiv.org/abs/2604.11711v1)（CVPR 2026 workshop） · 正文选读 | 在三个息肉数据集上合成手术工具遮挡/挖空，三种严重度；三区域协议拆分 full/visible/invisible；1,008 种配置；发现 full-mask Dice 会奖励“穿过遮挡物”的预测：MedSAM full 0.640 但 visible 仅 0.302；SAM 3 在 visible 高遮挡最稳（0.724/0.748/0.801）；MedSAM2 是唯一同时保持 visible 与 invisible 的平衡案例 | 2D RGB 结肠镜 + 合成遮挡，缺少真实光学/组织形变；只评 SAM 家族；三区域真值由合成遮挡给出；不能外推到自然场景所有遮挡 |
| VolFill | [2605.31466](https://arxiv.org/abs/2605.31466v1) · 正文选读 | 单图非模态 3D 场景重建：混合 3D VAE 压缩稀疏 TUDF 网格 + latent Diffusion Transformer + 几何基础模型条件；SCRREAM 完整 CD 3.88、FS@0.02 44.90、FPD 4.86（NOVA3R 6.56/22.23/16.50；LaRI 11.43/11.47）；NRGB-D 遮挡区 CD 6.97（NOVA3R 8.31、LaRI 13.04），完整 CD 6.44（8.19/9.79）；可见区 CD 4.52 不如 MoGe2 2.62/DA3 2.69 | 生成式补全，未观测区仍可能留小洞；50 步 + CFG 在 RTX 4090 上 1.4 s，慢于回归基线；训练用 3D-FRONT/ScanNet++ 的合成/重建 TUDF；静态室内为主；不是物理/材质/功能 |
| NOVA3R | [2603.04179](https://arxiv.org/abs/2603.04179v2)（ICLR 2026） · [项目页](https://wrchen530.github.io/nova3r) · 正文选读 | 非像素对齐的 amodal 3D：scene-token 聚合无位姿图像 + 扩散式 3D 解码器输出完整点云；SCRREAM 完整 CD 0.048（VGGT 0.070、LaRI 0.059、MoGe 0.063），2 视图 0.053（VGGT 0.065）；hole ratio 0.088（VGGT 0.307）、密度方差 5.127（7.105）；7-Scenes 768 token 下 Acc 0.041/Comp 0.033/NC 0.794（VGGT 2738 token：0.042/0.045/0.813） | 只训练 1–2 视图、场景 token/点数受限；大场景复杂结构会退化；静态场景，不处理动态/时序；非像素对齐使 visible/occluded 不能显式区分；生成式补全仍可能“合理但错误” |
| PHAC | [2603.14741](https://arxiv.org/abs/2603.14741v1)（CVPR 2026） · 摘要 | 可提示人体非模态补全：给遮挡人体图像 + 姿态/空间范围约束，生成不可见区域同时保留可见外观；针对现有 HAC 不可控、需反复采样的问题 | 生成式人体补全，依赖扩散先验与姿态条件；不保证物理接触/身份一致；评估以生成质量/可控性为主；不是通用物体 |
| Learnable Shape Prototypes | [2605.24533](https://arxiv.org/abs/2605.24533v1)（TCSVT 在审） · 摘要 | 非模态实例分割：可学习形状原型记忆 + 交叉注意力生成实例自适应形状先验；用可见 mask 的 signed distance field 做空间可靠性门控，按位置调制先验注入强度 | 形状原型容量限制新类别；门控依赖可见 mask 质量；摘要未给跨数据集数值；不是 3D/视频；先验可能压过观测 |
| AmodalCG | [2603.28333](https://arxiv.org/abs/2603.28333v1) · 摘要 | 用 MLLM 的世界知识引导非模态补全：先评估遮挡程度，选择性调用 MLLM，指导生成不可见区域 | `L2` 语言/常识先验；MLLM 可能把“常见形状”当成真值；遮挡评估错误会传播；不是纯视觉；未给独立数值 |
| Perception Beyond the Visible | [2610.18670](https://arxiv.org/abs/2610.18670v1)（RSS Pioneers 2026 research statement） · 摘要 | 提出“不完整场景理解”研究议程：不完整证据、不完整知识、不完整传感器可靠性三类挑战；连接 amodal 感知、语义 occupancy 预测、开放世界理解、标签高效学习与不确定性融合 | 研究声明，不是方法/实验；三类挑战的边界与度量未统一；机器人自主为应用背景；不能作为性能证据 |

#### OccJEPA：遮挡就是 masking，世界模型 predictor 可以补全“看不见的部分”

OccJEPA 的核心洞察很简洁：自监督视频世界模型的预训练任务，本来就是“从可见 token 预测被 mask 的时空区域”；遮挡只是另一种 mask。它把物体可见 mask 未覆盖的 token 丢掉，让冻结的 V-JEPA 2.1 predictor 在特征空间补全，再用轻量头解码成 amodal mask。SAIL-VOS mIoU 78.60，TAO-Amodal AP50 在 val/test 分别 +4.11/+4.00；隐藏区 mIoU +3.70；单次确定性预测 0.35 s/object，比 Diffusion-VAS 的 11.77 s 快 33.5×，FLOPs 35.6 vs 903；只训练 69M 参数。

消融很有说服力：同一 predictor 随机初始化只保留约 25%（SAIL-VOS）和 19%（TAO）的增益，说明收益来自预训练学到的“世界如何延续”，而不是额外容量；换 SAM2 跟踪的可见 mask 后仍 +4.32 AP50，说明不是靠真值 mask。边界也清楚：遮挡 <10% 时像素级生成更细；依赖 V-JEPA 特征与可见 mask；不推断材质/物理状态；在 TAO 上仍可能把邻近物体卷进来。它给 Clover 的直接证据是：**纯视觉自监督世界模型的特征预测，可以承担“不可见区域补全”的一部分工作**，而且比生成式采样更接近原生超快；但补全结果是假设，不是观测，必须带置信度与反证机制。

#### Amodal SAM：把 SAM 的泛化扩展到非模态，但合成遮挡决定上限

Amodal SAM 在 SAM 上加轻量 Spatial Completion Adapter、目标感知遮挡合成（TAOS）与区域/拓扑正则，统一图像与视频非模态分割。KINS mIoU_f 88.79/mIoU_o 63.12，优于 PLUG 的 88.10/61.42；COCOA 84.27/59.94，相比 PLUG 的 83.23/32.88，遮挡区提升尤其大；COCOA-cls 87.65/54.34；开放世界 COCOA-cls 83.18（SAMBA 81.82）、D2SA 91.62（90.87）；视频 FISHBOWL 92.74/83.36、MOViD-A 73.06/39.21。

它的关键限制在数据：训练遮挡由 SA-1B mask + TAOS 合成，真实遮挡的分布、光照、材料交互未必覆盖；开放世界仍以已知类别/域为主；mIoU_f 可以被“只分割可见区”抬高，必须同时看 mIoU_o；而 mIoU_o 的官方口径可能只在该方法预测出隐藏区的帧上平均（OccJEPA 报告 Diffusion-VAS 在 27.5% 遮挡帧上不预测），因此还要报告覆盖率；视频依赖逐帧/跟踪。它说明**SAM 的泛化可以迁移到非模态**，但“非模态”不是免费能力：合成遮挡的统计特性会写进模型，真实世界的遮挡需要独立验证。

#### OccSAM-Bench：full-mask 分数会奖励“穿过遮挡物”的幻觉

OccSAM-Bench 是这组里对评测最不客气的工作。它在三个息肉数据集上合成手术工具遮挡/挖空，三种严重度，提出 full/visible/invisible 三区域协议。结果发现：MedSAM 的 full-mask DSC 在高遮挡下 0.640，看似稳健，但 visible DSC 只有 0.302——大部分“正确”预测落在工具区域，而不是组织上；SAM 3 的 clean 分数最高，但 full-mask 高遮挡下降更多，visible 反而最稳（0.724/0.748/0.801）；MedSAM2 是唯一同时保持 visible 与 invisible 的平衡案例。模型因此分成 Occluder-Aware（SAM/SAM2/SAM3/MedSAM3，抑制遮挡区预测）与 Occluder-Agnostic（MedSAM/MedSAM2，倾向补全）两类。

它的边界是 2D RGB 结肠镜 + 合成遮挡，缺少真实光学/组织形变；但结论可迁移到所有非模态评测：**full/amodal 分数不能单独使用**，必须同时报告可见区、遮挡区与“预测是否穿过遮挡物”。否则，一个模型可以通过把遮挡物当目标来获得高分。Clover 的非模态验收应直接采用三区域分解，并加“遮挡物类别/边界”反事实。

#### VolFill 与 NOVA3R：3D 非模态重建从“像素对齐”转向“完整场景假设”

VolFill 用混合 3D VAE 压缩稀疏 TUDF 网格，再用 latent Diffusion Transformer 做条件生成；SCRREAM 完整 CD 3.88、FS@0.02 44.90、FPD 4.86，显著优于 NOVA3R（6.56/22.23/16.50）与 LaRI（11.43/11.47）；NRGB-D 遮挡区 CD 6.97（NOVA3R 8.31、LaRI 13.04），完整 CD 6.44（8.19/9.79）；但可见区 CD 4.52 不如 MoGe2 2.62/DA3 2.69，说明生成式补全以可见精度换完整几何。NOVA3R 走非像素对齐路线：scene token + 扩散式 3D 解码器，SCRREAM 完整 CD 0.048（VGGT 0.070、LaRI 0.059）、hole ratio 0.088（VGGT 0.307）、密度方差 5.127（7.105）；但只训练 1–2 视图、静态场景，非像素对齐也不能显式区分 visible/occluded。

两者共同说明：**3D 非模态重建必须把“可见精度”和“完整几何”分开报告**；生成式方法可以在遮挡区给出更完整的表面，但可能留下小洞、产生“合理但错误”的结构，且推理慢于回归基线（VolFill 1.4 s/场景）。对 Clover，“理解被遮挡的物体”不是生成一个漂亮 mesh，而是给出可检验的完整假设：哪些面是观测、哪些是推断、推断依赖什么先验、什么新观测能推翻它。

**本节结论：** 非模态感知有三条路线：2D mask 补全（Amodal SAM、PHAC、Shape Prototypes）、视频特征补全（OccJEPA）、3D 场景补全（VolFill、NOVA3R）。它们共同证明“看不见的部分”可以被系统地推断，但也共同暴露三个未解问题：**(1) 补全是欠定的**，形状/材质/物理属性需要不同先验，生成模型容易用“常见形状”替代观测；**(2) 评测会奖励幻觉**，full-mask/amodal 分数必须与 visible/invisible 分解、遮挡物反事实一起报告；**(3) 纯视觉证据仍薄**，OccJEPA 最接近纯视觉自监督，但依赖 V-JEPA 预训练与可见 mask；Amodal SAM/VolFill/NOVA3R 都依赖合成遮挡或几何基础模型。Clover 若声称“理解被遮挡的世界”，必须把补全当作**带来源标签的假设**，而不是把生成结果直接升级为世界状态。

<a id="event-async-2026"></a>

<a id="matting-transparency-2026"></a>

#### 边界、抠图与透明/伪装物体：alpha、时序与负样本

边界/抠图不是“更细的分割”：它要求连续 alpha、时序一致、透明/反光材质、软边界（毛发/细丝），以及在没有目标时**不产生假阳性**。此前这一行只有 WeVisOne-VL、SAM2Matting、Amodal SAM、OccJEPA、PHAC、Shape Prototypes；本轮补 10 篇 2026 年工作，覆盖视频 matting、精确 alpha、透明物体分割/深度、伪装物体负样本与合成数据负结果。

| 方法 | 一手来源 | 机制与可核查证据 | 边界与反假设 |
|---|---|---|---|
| VideoMaMa | [2601.14255](https://arxiv.org/abs/2601.14255v1) · [项目页](https://cvlab-kaist.github.io/VideoMaMa/) · 摘要 | 用预训练视频扩散模型把粗分割 mask 转成像素级 alpha；仅合成数据训练，零样本泛化到真实视频；构建 MA-V（50K+ 真实视频高质 matte）并微调 SAM2 得 SAM2-Matte | 摘要级；依赖上游 mask track；扩散计算重；合成到真实仍有差距；不是透明物体深度/3D；未给全表 |
| VideoMaMa++ | [2610.26857](https://arxiv.org/abs/2610.26857v1)（NeurIPS 2026） · [项目页](https://cvlab-kaist.github.io/VideoMaMa-PlusPlus/) · [代码](https://github.com/cvlab-kaist/VideoMaMa-PlusPlus) · 正文选读 | preserve/refine token + 参考锚点，解决分块推理的跨块闪烁；VideoMatte MAD 3.86（VideoMaMa 4.34）、dtSSD 0.82（1.21）；YouTubeMatte MAD 1.15（1.41）；V-HIM60 Hard MAD 1.69（2.30）；无块边界不连续 | 扩散 DiT 计算量大于前馈模型；依赖上游 mask track；长视频分块；不是透明深度/3D；真实复杂运动仍有限 |
| RenderMatte | [2608.08487](https://arxiv.org/abs/2608.08487v1) · 正文选读 | FLUX.1 Kontext 全参微调 + alpha-edge 像素空间监督 + GRPO 式 group-relative alpha 对齐；AIM-500 MSE 0.002/MAD 0.008/Grad 11.2，AvgRank 1.6；RenderMatte-2K 零样本最佳 | 1024² 单图约 2.7 s（DiffMatte <0.5 s）；合成数据/trimap 依赖；稀有 OOD 前景仍失败；生成式先验可能补出纹理；不是视频时序 |
| FCLM（Real-world High-Precision Matting） | [2601.12080](https://arxiv.org/abs/2601.12080v1)（AAAI 2026） · 摘要 | 前景一致学习 + 深度感知蒸馏，面向真实高精度 matting/二值分割；缓解合成数据不协调与类别泛化差 | 摘要级；仍依赖标注/深度；单前景为主；不是视频/透明物理；未给全表 |
| Segment and Matte Anything | [2601.12147](https://arxiv.org/abs/2601.12147v1)（AAAI 2026） · 摘要 | 在 SAM 统一模型中同时做分割与交互式 matting，利用分割-抠图相关性提升边界精度 | 摘要级；交互提示依赖；SAM 基座成本；不是视频时序；透明/软边界未全测 |
| HairGuard | [2601.03362](https://arxiv.org/abs/2601.03362v1) · 摘要 | 用 matting 数据训练 depth fixer，识别软边界区域并门控残差修正；可插到 SOTA 深度模型，改善深度/立体/新视图的毛发细丝 | 摘要级；软边界深度特定；依赖 matting 数据；不是 alpha 输出/视频时序；真实传感器未全测 |
| SEP-YOLO | [2603.02648](https://arxiv.org/abs/2603.02648v1)（ISCAS 2026） · 正文选读 | 频域细节增强 + 多尺度门控 + 内容对齐 neck，做透明物体实例分割；Trans10K mask mAP50 0.851（YOLO11n 0.813）、GVD 0.872（0.849）；2.98M/88 FPS | 透明物体实例分割，不是 alpha/软边界；数据集 GVD/Trans10K；频域增强对低对比有效但非物理分解；不是 3D/深度 |
| SeeClear | [2603.19547](https://arxiv.org/abs/2603.19547v1) · 项目页本次不可访问（SSL 握手失败），不作为可复现 artifact · 正文选读 | 生成式“不透明化”把透明外观转成几何一致的不透明图，再喂冻结单目深度；ClearGrasp ToM AbsRel 0.033（DA3 0.038）、RMSE 21.45（24.03）；396K 渲染训练；无需重训深度 | 两阶段扩散，推理开销；合成训练到真实差距；依赖透明区域定位/mask；不是视频时序/物理折射；透明深度不是 alpha |
| OPC16K / OPCNet | [2608.11135](https://arxiv.org/abs/2608.11135v1) · 正文选读 | 真实伪装物体检测基准：16,245 图/14 源，含纯背景与非伪装负样本；OPCNet 分解存在性推理与分割；现有 SOTA 负样本 FPR 97.4%（RUN）/49.3%（USCNet）；OPCNet Acc_all 0.872、FPR_bg 0.057、FPR_no 0.189 | 伪装物体特定；负样本分布对齐但仍有域差；不是通用边界/alpha；真实开放世界覆盖有限；不是 3D |
| Concentration, Not Uncertainty | [2610.09807](https://arxiv.org/abs/2610.09807v1) · 摘要 | 负结果：按模型不确定性选择合成数据目标，103 次训练中不优于随机分配；五个控制表明差异可由“集中生成预算”解释，而非不确定性 | 摘要级；伪装物体特定；生成预算/数据引擎设置；不能推出所有主动学习无效；不是边界/alpha 方法 |

##### VideoMaMa++ 与 RenderMatte：时序一致与精确 alpha 是两件事

VideoMaMa++ 解决的是“分块扩散 matting 的跨块闪烁”：用 preserve/refine token + 参考锚点，让长视频在块边界保持稳定。VideoMatte MAD 3.86 vs VideoMaMa 4.34、dtSSD 0.82 vs 1.21；YouTubeMatte 1.15 vs 1.41；V-HIM60 Hard 1.69 vs 2.30；作者还用无标注的块边界不连续检验证明它没有可测的 seam。代价是 DiT 计算量大于前馈模型，且依赖上游 mask track。

RenderMatte 解决的是“精确 alpha 与稀疏边界”：FLUX.1 Kontext 全参微调 + alpha-edge 像素监督 + GRPO 式 group-relative 对齐；AIM-500 MSE 0.002/MAD 0.008/Grad 11.2，AvgRank 1.6；RenderMatte-2K 零样本最佳。代价是 1024² 单图约 2.7 s（DiffMatte <0.5 s），且合成数据/trimap 依赖、稀有 OOD 前景仍失败。

两者说明：**时序一致与单帧 alpha 精度不是同一指标**；Clover 若把“边界理解”作为能力，必须分别报告 alpha 误差（MSE/MAD/Grad/Conn）、时序（dtSSD/seam）、计算与上游 mask 依赖。

##### SEP-YOLO 与 SeeClear：透明物体的 2D 边界与 3D 深度要分开

SEP-YOLO 用频域细节增强 + 多尺度门控 + 内容对齐 neck 做透明物体实例分割：Trans10K mask mAP50 0.851（YOLO11n 0.813）、GVD 0.872（0.849），2.98M/88 FPS。它证明低对比/边界模糊可以通过频域与多尺度结构改善，但仍是 2D 实例分割，不是 alpha/软边界，也不是透明物理分解。

SeeClear 则把透明外观“生成式不透明化”，再喂冻结单目深度：ClearGrasp ToM AbsRel 0.033（DA3 0.038）、RMSE 21.45（24.03）；396K 渲染训练，无需重训深度。它把透明深度从“直接回归”改成“先转成不透明几何再估深”，但两阶段扩散有推理开销，合成到真实仍有差距，且依赖透明区域定位/mask。两者共同说明：**透明物体的 2D 边界、alpha、3D 深度是三种输出**，不能用一个 mask mAP 替代。

##### OPC16K：没有目标时的假阳性，是边界/伪装评测的盲点

OPC16K 把“输入一定含伪装目标”的闭世界假设打破：16,245 图/14 源，含约 9,000 伪装目标、3,000 纯背景、4,000 非伪装物体；现有 SOTA 在负样本上的 FPR 高达 97.4%（RUN）/49.3%（USCNet）。OPCNet 用存在性推理 + 分割分解，Acc_all 0.872、FPR_bg 0.057、FPR_no 0.189。

它给 Clover 的评测威胁很直接：**只测正样本 mask 分数，会把“到处报目标”的模型当成好模型**。边界/伪装/开放世界检测必须报告负样本假阳性、纯背景拒绝、非目标类别拒绝；否则“边界很准”可能只是“到处都报”。

##### Concentration, Not Uncertainty：合成数据“定向补难”不一定优于随机

这篇负结果针对伪装物体检测：按模型不确定性选择合成数据目标，103 次训练中不优于随机分配；五个控制表明差异可由“集中生成预算”解释，而不是不确定性。它说明数据引擎的“主动选择”需要严格对照；**更多合成数据/更聪明的采样**不自动等于更好边界。

对 Clover 的启发是：数据侧增益必须先与随机分配、简单重复、预算集中等控制比较；否则“不确定性驱动”只是把预算集中到某些簇，而不是真正补足失败模式。

**本节结论：** 边界/抠图至少五层：**alpha 精度**（RenderMatte）、**视频时序**（VideoMaMa/++）、**透明 2D/3D**（SEP-YOLO/SeeClear）、**软边界跨视图**（HairGuard/FCLM）、**负样本拒绝**（OPC16K）。2026 趋势是扩散/生成先验、精确 alpha、时序一致、透明物体与真实负样本；但计算、合成到真实、上游 mask、评测口径仍未统一。Clover 若声称“看见细节”，必须分别报告 alpha、mask、depth、时序、负样本 FPR 与计算；单一 mAP 或视觉示例不能替代这些证据。

### 事件视觉与异步感知：当“看见”不再等于固定帧率

前述能力默认输入是同步 RGB 帧。事件相机（event camera / DVS）报告的是每个像素的亮度变化，而不是固定时刻的绝对强度：它有微秒级时间分辨率、高动态范围、低冗余，但也带来异步、稀疏、噪声与“没有静态外观”的问题。对 Clover 的“纯视觉 + 原生 ultrafast”主张，这是一条必须单列的**观察协议**，不是普通 RGB 模型的可选插件。本轮补 9 篇 2026 年工作，覆盖事件特征、延迟评测、事件 3D 重建、长时 3D 跟踪、脉冲网络与端侧效率。

| 方法 | 一手来源 | 机制与可核查证据 | 边界与反假设 |
|---|---|---|---|
| Static in Frames, Dynamic in Events | [2608.11075](https://arxiv.org/abs/2608.11075v1) · 正文选读 | 证明事件角点检测用的 Harris 结构张量特征值与时空密度值本身就是**运动线索**；把二者与局部几何拼接后，合成数据光流 MSE 稳定下降；纹理条件下平均改善 28.84%，散粒噪声下平均改善 71.99%；接入 IDNet 在 DSEC/EVIMO2v2 数据稀缺与低容量模型上增益最大 | 特征不是独立语义；全量数据/高容量时增益消失（EVIMO 全量 EPE 0.633→0.638 反而略差）；推理 30.43→32.58 ms/frame，参数 1.427M→1.430M；依赖事件表示与局部几何；不是 RGB 可直接照搬 |
| Bend the Clock / ChronoFuse | [2609.26919](https://arxiv.org/abs/2609.26919v1) · 正文选读 | 指出事件检测器仍有数十毫秒计算延迟，传统评测在**观测时刻**对齐，忽略了预测可用时场景已变化；用因果跨时融合预测 `t+Δ` 的目标状态；1Mpx sAP 43.17→46.20（恢复 71.8% 延迟损失），FRED 26.88→44.99（90.8%），EV-Flying 2.25→20.95（9.3×）；额外延迟 0.84 ms（2.84%）、0.17M 参数 | 固定 33.33 ms 预测时域；需要未来目标监督；只在事件检测器上验证；不是通用世界状态预测；RGB StreamYOLO 对比是匹配时序的跨模态参考，不是受控模态消融 |
| Event3R | [2607.15727](https://arxiv.org/abs/2607.15727v1)（IROS 2026） · 正文选读 | 事件流→时空体素→时间注意力 + DUSt3R 式全局点图；事件-only 前馈 3D 重建；TartanAir 深度 AbsRel 0.0514（DepthAnyEvent 0.2751）、δ<1.25 0.970；MVSEC AbsRel 0.1805（EvGGS 0.1972）；TartanAir 位姿 ATE 0.116–0.545 cm（DEVO 0.261–2.02）；3D 重建 TartanAir NC 0.8886（IncEventGS 0.6236） | 训练 7 天/8×A100；事件块 50 ms、T=5；DUSt3R 预训练初始化；TartanAir 事件由 ESIM 从 RGB 模拟；MVSEC 真实但规模有限；不是语义/动态物体理解 |
| E-TraMamba | [2607.02866](https://arxiv.org/abs/2607.02866v1) · 正文选读 | 首个 Mamba 事件 3D 特征跟踪：线性状态空间 + 轻量仿射变换预测器 + 多尺度局部/相关/位置融合；E-3DTrack 特征年龄 FA@0.1m 0.6146（E-3DTrack 0.2601）、TFR 0.7274（0.6928）、RMSE 0.0914 m（0.1181，−22.6%）；自建 EvD-PointOdyssey 2D RMSE 4.16 px（ETAP 23.26）；2.11 ms/frame（≈475 FPS） | 事件+立体/深度配置；E-3DTrack 真实、EvD 半合成；长时遮挡/轨迹滤波/监督可靠性仍是问题；2.11 ms 不含完整下游；不是语义跟踪 |
| E-S2Feat | [2608.14027](https://arxiv.org/abs/2608.14027v1) · 正文选读 | 首个 SNN 事件局部特征检测+描述框架：模块特定脉冲激活（MSF/spiking GELU/SiLU）+ 语义引导的响应调制与描述子融合；ECD/EDS/TUM-VIE 上姿态与 VIO 有竞争力，作者报告相对 ANN 对应体约 4.8× 理论能效 | 理论能效非实测功耗；需要语义分支/训练标签；SNN 单步量化仍有信息瓶颈；未给跨数据集完整表；不是端到端 SLAM |
| Sequence-SOD | [2607.26703](https://arxiv.org/abs/2607.26703v1) · 摘要 | 序列感知 SNN 事件检测器：把连续事件流切成短区间并离散为时间步，保留网络状态、支持多时间点标签，避免“每个区间单标签+重置状态” | 摘要级；SNN 训练稳定性/延迟未核；事件检测基准有限；不是开放词汇/语义 |
| LiteEvent-AE | [2608.21764](https://arxiv.org/abs/2608.21764v1) · 摘要 | 轻量事件自编码器：卷积编码 + 自适应事件阈值 + 极小分类头，面向低功耗边缘设备的压缩与下游推理 | 摘要级；压缩率/精度/实测能耗未核；任务限于分类；不是通用表征 |
| EventEgoHands++ | [2609.17189](https://arxiv.org/abs/2609.17189v1)（IEEE Access） · 摘要 | 第一人称事件相机 3D 手部网格重建；针对佩戴者自身运动产生密集背景事件、左右手不分的问题，构建真实数据集并改进手部分割/重建 | 事件相机+第一人称；手部特定；摘要未给跨数据集数值；不是通用物体/场景 |
| Event vs Frame for Synthetic-Aperture Imaging | [2610.20309](https://arxiv.org/abs/2610.20309v1) · 既有引用，见[主动视觉方向](causality-and-active-perception.md#active-vision-frontier) | 在完全相同的场景与相机轨迹下，用 EMVA 1288 帧噪声模型与 v2e/Sony IMX636 事件模拟比较合成孔径成像；既有记录：25 m/s 亮场景帧相机只记录 3 张、事件可去遮挡；5 lux 下事件也失效；5 m/s/5 lux 两者相近；1 m/s 匹配预算时事件无优势 | 纯模拟，传感器参数/场景特定；事件率在高速亮场景最高，恰好也是需要它的时候；不代表真实事件相机标定/噪声；合成孔径去遮挡不等于一般世界理解 |

#### Static in Frames, Dynamic in Events：事件特征天然携带运动，但不是“免费午餐”

这篇工作把事件角点检测里的两个特征——结构张量特征值与时空密度值——重新解释为运动线索，并证明它们与局部几何结合可以恢复平移角点的运动方向。合成数据上，加入这两个特征后光流 MSE 稳定下降；纹理条件下平均改善 28.84%，散粒噪声下平均改善 71.99%；接入 IDNet 后，在 DSEC/EVIMO2v2 的数据稀缺和低容量设置下增益最大。

但“事件特征=运动”不是普遍增益：EVIMO2v2 全量训练时，扩展特征反而略差（EPE 0.633→0.638），说明网络在数据充足时可以自己学出类似信息；推理从 30.43 ms 增到 32.58 ms，参数只增 0.003M。它给 Clover 的启发是：**异步观测的归纳偏置可以写进特征，但必须按数据量/容量/延迟核算收益**；事件视觉的优势不是自动的，而是“在稀疏、快速、低功耗条件下”更明显。

#### Bend the Clock：延迟评测必须对齐“预测可用时刻”，不是“观测时刻”

这篇工作抓住了一个被普遍忽略的评测错误：事件检测器从观测到输出仍有数十毫秒，传统评测却把预测与观测时刻的真值对齐；等预测真正可用时，场景已经变了。ChronoFuse 用因果跨时融合直接预测 `t+Δ` 的状态。1Mpx sAP 43.17→46.20，恢复 71.8% 的延迟损失；FRED 26.88→44.99，恢复 90.8%；EV-Flying 2.25→20.95，是现有最强检测器的 9.3×；额外延迟仅 0.84 ms（2.84%）、0.17M 参数。与 RGB StreamYOLO 的匹配时序对比中，44.88 vs 22.76 sAP。

它的边界是固定 33.33 ms 时域、需要未来目标监督、只在事件检测上验证。但它对 Clover 的“原生 ultrafast”是直接威胁：**任何只报观测时延、不报预测可用时/证据年龄的速度主张都不成立**。Clover 的 U 系列验收应把“预测可用时刻的世界状态误差”作为独立指标，而不是只测模型前向时间。

#### Event3R 与 E-TraMamba：事件-only 也能做几何与长时跟踪

Event3R 把事件流转成时空体素，用时间注意力 + DUSt3R 式全局点图，做事件-only 前馈 3D 重建。TartanAir 深度 AbsRel 0.0514（DepthAnyEvent 0.2751）、δ<1.25 0.970；MVSEC AbsRel 0.1805（EvGGS 0.1972）；TartanAir 位姿 ATE 0.116–0.545 cm（DEVO 0.261–2.02）；3D 重建 TartanAir NC 0.8886（IncEventGS 0.6236）。代价是训练 7 天/8×A100、50 ms 事件块、DUSt3R 初始化，且 TartanAir 事件由 RGB 模拟。

E-TraMamba 则把长时 3D 特征跟踪做成线性状态空间：E-3DTrack 上 FA@0.1m 0.6146（基线 0.2601）、TFR 0.7274（0.6928）、RMSE 0.0914 m（0.1181，−22.6%）；自建 2D 基准 RMSE 4.16 px（ETAP 23.26）；2.11 ms/frame（≈475 FPS）。两者共同说明：**事件流不只是“更快的帧”，它可以承载几何与长时对应**；但一个依赖 DUSt3R/立体配置，一个依赖半合成数据，纯事件语义/动态物体理解仍未解决。

#### E-S2Feat、Sequence-SOD 与 LiteEvent-AE：脉冲/端侧效率是另一条“原生超快”路线

E-S2Feat 把 SNN 用于事件局部特征检测与描述：模块特定脉冲激活（MSF、spiking GELU/SiLU）+ 语义引导的响应调制，在 ECD/EDS/TUM-VIE 上姿态与 VIO 有竞争力，作者报告相对 ANN 对应体约 4.8× **理论**能效。Sequence-SOD 让 SNN 检测器保留跨区间状态、支持多时间点标签；LiteEvent-AE 用轻量自编码器压缩事件流，面向低功耗边缘。

这条路线与 Clover 的“原生 ultrafast”最接近，但证据边界也最硬：4.8× 是理论能效，不是实测焦耳；SNN 单步量化仍有信息瓶颈；Sequence-SOD/LiteEvent-AE 只有摘要级；没有一篇同时给出开放世界语义、长时跟踪与实测端侧功耗。它说明**算法-传感器-硬件协同**可能是原生超快的必要条件，但“脉冲”本身不是能力保证。

**本节结论：** 事件视觉改变的是观察协议，不是给 RGB 模型加一个输入通道。它带来三类独特证据：运动线索直接编码在事件特征中（Static in Frames）；延迟必须按预测可用时刻评测（Bend the Clock）；事件-only 也能做 3D 重建与长时跟踪（Event3R、E-TraMamba）。但它也暴露三个缺口：**(1) 语义理解薄**——事件检测/分割/开放词汇远少于 RGB；**(2) 证据不独立**——大量事件数据由 RGB 模拟（ESIM/v2e），真实事件基准规模有限；**(3) 能效多为理论值**——缺少实测焦耳与端到端延迟。Clover 若把事件视觉纳入“纯视觉”路线，应把它标为 **V0-E 观察协议**：与 RGB 共享“视觉”名义，但不共享像素统计、标定假设与评测口径；不能把 RGB 上的结论直接迁移，也不能用事件的高动态范围替代 RGB 的语义证据。

<a id="composition-reasoning-2026"></a>

### 组合泛化、抽象推理与证据绑定

“理解”不仅是识别当前像素，还要在**未见过的组合**上推出规则、在更长/更复杂的输入上保持状态、把答案绑定到正确的视觉证据。当前能力矩阵里“组合、抽象与视觉推理”一直偏薄；本轮补 9 篇 2026 年工作，覆盖抽象规则（ARC）、局部/循环视觉与长度泛化、属性-物体组合零样本、动词-名词动作组合、以及主动视觉推理的答案-证据分离。

| 方法 | 一手来源 | 机制与可核查证据 | 边界与反假设 |
|---|---|---|---|
| TraceViT | [2607.29586](https://arxiv.org/abs/2607.29586v1) · 正文选读 | 用“语义单调变换链”监督循环视觉推理器的中间网格状态；任务参考 + 物体工作区在每个迭代重新注入规则/场景；软轨迹对齐不固定迭代节奏；ARC-AGI-1 67.8 pass@2、ARC-AGI-2 24.3（18M 参数；LoopViT 65.8/14.2、VARC 54.5/8.3）；消融：仅轨迹监督 61.6 反而低于终态 62.3，轨迹+接地 65.5 | 变换链来自程序化任务实现，需可验证改写；ARC-AGI-2 仍低；单一网格域；不是自然图像/物理世界；错误分析显示候选覆盖而非选择是主瓶颈；测试时训练/510 视图聚合成本高 |
| Locality & Length Generalization | [2607.09061](https://arxiv.org/abs/2607.09061v1)（ECCV 2026） · 正文选读 | 用视觉 parity/state machine 测试长度泛化：只有“局部高分辨率 fovea + 低分辨率 periphery + 循环状态”的 FoveAgent-LSTM 在 OOD 任务复杂度/分辨率/长度上保持；Global 与 Local+Global 同分布好但 OOD 崩；Transformer/Mamba/xLSTM 即使输入局部也不长度泛化；Qwen2.5-VL-3B 同分布高、OOD 急降；加主动搜索/访问标记后仍泛化 | 合成任务（开关/状态机）；不是自然图像；fovea/ periphery 分辨率与步数是关键超参；VLM 少样本结果受提示影响；作者假设 H1–H3 是受控证据，不是普遍定理 |
| Reachability Is Not Generalization | [2610.00064](https://arxiv.org/abs/2610.00064v1)（BMVC 2026） · 正文选读 | 系统分析动词-名词分解在装配动作上的组合迁移：原子分类器对未见组合必为 0；独立分解把 unseen HM 从共享分解的 3.3/13.7/10.6 提到 19.8/30.2/31.2（MECCANO/HAViD/IMPACT）；但 unseen 准确率与原始概念训练支持强相关（Spearman ρ=0.49/0.56/0.69），低支持组合仍近 0；更细分解不提升 unseen；独立编码器优于共享编码器 | 装配动作/固定数据集；MViTv2-S + Kinetics 预训练；组合网格密度决定“可达”与“泛化”的差距；不是开放世界/语言组合；未解决低支持区域 |
| DIFFCZSL | [2608.19871](https://arxiv.org/abs/2608.19871v1) · 正文选读 | 把预训练扩散模型的中间特征作为辅助正则注入 CLIP CZSL；训练时用、推理不改；CAMS 上 MIT-States 闭集 HM 40.3→40.7/AUC 23.4→24.0、开放世界 HM 22.0→22.1/AUC 8.5→8.7；Troika 闭集 HM 39.2→39.9/AUC 22.1→23.1 | 依赖 CLIP/Stable Diffusion（`L2`）；增益很小（0.1–1.0 点），不是质变；属性-物体组合，不含关系/动作；扩散先验可能补出训练分布；不是纯视觉 |
| PRPC | [2607.05911](https://arxiv.org/abs/2607.05911v1) · 摘要 | CZSL 逐步推理：把属性/物体分解成结构化 Q&A 链，双向相互纠正，抑制早期错误传播；用 MLLM 生成中间步骤 | 摘要级；MLLM 语义先验；未给跨数据集数值；不是纯视觉；组合空间仍受 primitive 支持限制 |
| CS-CLIP | [2609.08242](https://arxiv.org/abs/2609.08242v1)（EMNLP Findings 2026） · 摘要 | 用场景图识别组合元素、选择性掩码构造结构化负例，迫使 CLIP 依赖组合结构而非表面线索；作者报告在组合推理基准上 SOTA/稳健 | 摘要级；CLIP/语言监督；场景图质量决定负例；不是纯视觉；组合基准与自然开放世界有差距 |
| JRDB-AVR | [2609.35032](https://arxiv.org/abs/2609.35032v1)（NeurIPS 2026） · 正文选读 | 真实机器人数据上的主动视觉推理基准：2,098 题/27 序列；智能体可按时间/视角请求有限观测，同时评答案、证据、组合分与条件幻觉率；最强 baseline 答案 33.65/证据 13.01/组合 5.96；JRDB-AVR-Agent 38.51/27.50/14.54，幻觉率 81.22→62.25；消融：主动观测+世界模型把组合分从 2.72 提到 14.54 | 记录观测而非真实机器人闭环；VLM backbone（Gemma/Qwen）为主；证据标注/问题生成仍有噪声；绝对组合分很低；不是纯视觉 |
| Humanity's Sixth Sense | [2610.08966](https://arxiv.org/abs/2610.08966v2) · 摘要 | 评测 MLLM 的“直觉视觉推理”：从单帧/短视频推断隐含因果、未来轨迹、社会角色、未明规则等超出显式像素的信息 | 摘要级；MLLM 语言/常识先验；基准标注主观性；不是纯视觉；不能推出物理/因果理解 |
| GenVerOpt（Can machines reason non-verbally?） | [2610.13925](https://arxiv.org/abs/2610.13925v1) · 摘要 | 提出生成-验证-优化统一框架，用于没有明确中间步骤可验证的非语言视觉推理（抽象图案、模糊 ROI 等） | 摘要级/概念框架；验证器可靠性未核；任务范围有限；不是通用世界理解；未给完整基准 |

#### TraceViT：中间状态必须被监督，但监督需要“外部工作区”

TraceViT 的核心发现不是“加中间监督就更好”，而是一个非平凡的交互：在循环推理器上，仅加轨迹监督会让 ARC-AGI-1 从 62.3 降到 61.6，因为中间状态被推向部分答案，破坏了后续迭代仍需的输入信息；只有同时提供任务参考与物体工作区、把“记忆”从循环状态中外部化，轨迹监督才把准确率推到 65.5。完整模型 ARC-AGI-1 67.8、ARC-AGI-2 24.3（18M 参数），优于 LoopViT 65.8/14.2 与 VARC 54.5/8.3。

它的边界是程序化变换链、单网格域、测试时训练与 510 视图聚合；ARC-AGI-2 仍低，说明多规则组合远未解决；错误分析显示候选覆盖而非选择是主瓶颈。它给 Clover 的启发是：**抽象推理需要可检查的中间状态与外部工作区**，而不是只监督最终答案；但“中间状态”从哪来（程序、演示、还是自生成）决定了它能否扩展到自然视觉。

#### Locality & Length Generalization：局部感知 + 循环状态是长度泛化的必要条件

这篇工作用视觉 parity/state machine 把“看整图”与“序列看局部”分开：全局高分辨率输入、或局部+全局输入，同分布都很好，但 OOD 任务复杂度/分辨率/长度一升就崩；只有局部高分辨率 fovea + 低分辨率 periphery + 循环状态（FoveAgent-LSTM）保持。固定局部输入后，Transformer、Mamba、xLSTM 都不长度泛化，只有严格循环网络可以；Qwen2.5-VL-3B 同分布高、OOD 急降；去掉遍历箭头、让模型主动搜索并用地标记忆访问历史后，仍能泛化。

它的边界是合成开关/状态机任务，不是自然图像；fovea/periphery 的分辨率与步数是关键超参；少样本 VLM 结果受提示影响。它给 Clover 的证据很直接：**“看哪里、看多细、记住看过什么”是长度泛化的结构条件**，不是单纯扩大上下文或换更强 VLM 能解决的；这与主动视觉、事件视觉和记忆方向形成同一约束。

#### Reachability Is Not Generalization：动词-名词分解让未见组合“可达”，但不等于“会”

在装配动作中，原子分类器对未见动词-名词组合的概率恒为 0；独立分解把 unseen HM 从共享分解的 3.3/13.7/10.6 提到 19.8/30.2/31.2（MECCANO/HAViD/IMPACT）。但 unseen 准确率与原始概念的训练支持强相关（Spearman ρ=0.49/0.56/0.69），低支持组合仍接近 0；更细的分解（k=3/4）主要恢复 seen 准确率、反而降低 unseen；独立编码器优于共享编码器，说明“解耦”比“加头”更重要。

它给 Clover 的启发是：**组合泛化必须报告“组合覆盖率/支持度”，不能只报 unseen 平均分**；一个模型可以在高支持组合上看起来会组合，在低支持区域仍是记忆/插值。它也说明“分解”不是越细越好；任务相关的二分解 + 独立编码器可能比复杂层次结构更稳。

#### JRDB-AVR：答案对了，证据可能完全错

JRDB-AVR 在真实机器人数据上评“主动视觉推理”：智能体只能按时间/视角请求有限观测，必须同时给出答案与证据。最强 baseline 答案 33.65，但证据只有 13.01、组合分 5.96；条件幻觉率（答案对但证据错）最低仍 81.22%。JRDB-AVR-Agent 用显式世界模型 + 主动观测把答案/证据/组合提到 38.51/27.50/14.54，幻觉率降到 62.25%；消融显示世界模型单独组合分 3.62、主动观测单独 9.20、两者 14.54。

它的边界是记录观测而非真实机器人闭环、VLM backbone 为主、绝对分很低。但它给 Clover 的评测威胁最大：**答案准确率会系统性地掩盖证据绑定错误**。组合/抽象推理的验收必须同时报告“答案、证据、组合分、条件幻觉率”，否则一个模型可以靠语言先验答对，却没有看到支持答案的对象/时刻/视角。

#### CZSL 三篇：语言/扩散先验带来小幅增益，但没有解决组合结构

DIFFCZSL 把扩散特征作为 CLIP CZSL 的辅助正则，CAMS 闭集 HM 40.3→40.7、AUC 23.4→24.0，开放世界 HM 22.0→22.1、AUC 8.5→8.7；Troika 闭集 HM 39.2→39.9。增益很小（0.1–1.0 点），但推理不改、可插拔。PRPC 用 MLLM 做属性/物体双向纠正；CS-CLIP 用场景图构造结构化负例。三者的共同点是**依赖 CLIP/语言/扩散先验**，不是纯视觉；它们能改善属性-物体组合，但不能证明关系、动作或物理组合。

对 Clover，正确的读法是：组合泛化的难点不在“有没有语义先验”，而在**组合支持度、关系结构和证据绑定**；语言先验可以把分数抬高，却可能把“组合”变成“近义描述匹配”。这也解释了为什么 HOI 评测审计与 JRDB-AVR 的答案-证据分离必须同时进入组合能力验收。

**本节结论：** 组合/抽象推理至少包含五个不同轴：**规则抽象**（ARC/TraceViT）、**长度与状态跟踪**（foveated recurrence）、**属性-物体组合**（CZSL）、**动词-名词动作组合**（assembly）、**答案-证据绑定**（JRDB-AVR）。纯视觉证据在 ARC、foveated 状态跟踪与动作组合上最强；CZSL 与直觉推理仍大量依赖语言/扩散先验；JRDB-AVR 证明“答对”与“看见”可以分离。Clover 若声称“广义理解”，必须在新组合、长输入、低支持组合和证据绑定四个维度上分别验收；平均 unseen 分数或单一 QA 准确率都不够。

<a id="counting-measurement-2026"></a>

### 计数与视觉测量：实例、语义组、事件与实时性

计数看似简单，实际至少有五种不同任务：数**实例**（多少辆车）、数**语义组**（几串葡萄/几摞盘子）、数**事件**（几次完整动作周期）、在**流式视频**中维护累计状态、以及在**工业/测量**场景中数堆叠/遮挡物体。现有能力矩阵这一行只有 CountGD 与 UniCounting；本轮补 10 篇 2026 年工作，把这五种任务和“准确率-实时性-不确定性”的取舍分开。

| 方法 | 一手来源 | 机制与可核查证据 | 边界与反假设 |
|---|---|---|---|
| DualCount | [2609.17613](https://arxiv.org/abs/2609.17613v1)（ECCV 2026） · 正文选读 | 零样本文本计数：密度与点双解码器结构耦合，用实例级质量守恒与质心对齐约束密度分配；FSC-147 test MAE 11.32/RMSE 97.16（val 11.21/42.77），优于 CountGD 12.98/98.35 与 T2ICount 11.76/97.86；CARPK 7.95/9.78（CountGD 3.83/5.41 更低）；PUCPR+ 24.27/28.91（CountGD 24.31/32.16） | 文本/图像编码器依赖 CLIP 或 SwinT+BERT；CARPK 上不如检测式 CountGD；FSC-147 域内；密集/遮挡仍有误差；不输出校准不确定性；不是视频/语义组 |
| BunchCount / GICount | [2609.04716](https://arxiv.org/abs/2609.04716v1) · 正文选读 | 组-个体计数（GIC）：同一图像同一类别，按“计数单元”数个体或语义组；1,330 图/89,254 个体/11,065 组标注；GICount 组 MAE 1.85/RMSE 5.49，个体 12.20/28.89；CountGD 组 MAE 9.21、个体 13.54；GroundingREC 组 3.59 但个体 23.17 | 语义组定义/标注依赖数据；Containment 关系监督；单一数据集；组/个体联合训练存在粒度冲突；不是开放世界/视频；不输出不确定 |
| SVCBench | [2603.12703](https://arxiv.org/abs/2603.12703v3)（ECCV 2026） · 正文选读 | 流式视频计数基准：406 视频、10,071 事件、逐帧标注；把计数作为世界状态维护的最小探针，分物体/事件 8 子类；人类总体 GPA 96.1，最佳模型约 37.0；周期事件人类 93.2 vs 最佳模型 11.1；盲 LLM MoC 95.7 但 GPA 18.7/UDA 4.3；显式计数标注带来 21× 改善 | 模型以 MLLM/在线视频模型为主；记录视频非机器人闭环；GPA/MoC/UDA 指标仍需外部验证；事件定义/标注有限；不是纯视觉 |
| ConvStack | [2609.37096](https://arxiv.org/abs/2609.37096v2) · 正文选读 | 诊断 MLLM 计数失败：patchification 造成“个体化瓶颈”，注意力压缩造成“聚合崩溃”；用卷积残差适配器在 ViT 层注入局部 token 混合；PixMo-Count 75.19%（Qwen3-VL-8B 65.46，+9.73），CountBenchQA 90.22%；计数 6–10 从 56.8% 升到 98.8%，silhouette 0.479→0.707；CV-Bench Spatial 93.20% | 依赖 Qwen3-VL-8B 与计数训练数据；提升集中在计数/空间，通用能力小幅波动；不是开放词汇/视频；不输出不确定；局部卷积不是通用计数架构 |
| UpCount | [2607.16826](https://arxiv.org/abs/2607.16826v2) · 摘要 | 类无关计数：多层 ViT 特征重组为多尺度金字塔，DPT/FeatUp 空间细化，proposal-verification 头输出密度图；FSC-147 test MAE 12.39/RMSE 100.89 | 摘要级；单图像/单类别；密集/遮挡仍难；不输出不确定；不是文本/开放词汇 |
| AdaCount | [2607.02139](https://arxiv.org/abs/2607.02139v1) · 摘要 | 训练-free 零样本计数：针对 SAM3 在密集小物体上的分辨率/注意力不足，做相似度引导的空间与特征自适应 | 技术报告；依赖 SAM3；密集小物体仍是边界；未给跨数据集全表；不是视频/语义组 |
| OCCAM | [2601.13871](https://arxiv.org/abs/2601.13871v1) · 摘要 | 首个无训练、无 exemplar/文本先验的类无关多类计数；用 SAM2 + 自定义阈值/聚类分离实例 | 摘要级；依赖 SAM2 分割质量；多类/重叠/遮挡边界未核；不是开放世界语义计数；不输出不确定 |
| MixCount | [2605.18063](https://arxiv.org/abs/2605.18063v1) · 摘要 | 混合物体计数数据集/基准：自动生成图像、细粒度文本与像素级标注，针对工业检测/商品分拣中的混合类别失败 | 合成数据到真实域的差距；标注仍自动生成；不是方法；不覆盖视频/事件 |
| RT-Counter | [2606.17561](https://arxiv.org/abs/2606.17561v1) · 正文选读 | 实时文本引导开放词汇计数：Visual Prototype Textualization + Weaformer；FSC-147 13.30/104.63，REC-8K 5.72/18.19，CARPK 4.81/7.61；38M 参数、112.48 FPS、21.37 GFLOPs（384²）；CountGD 213M/4.6 FPS/98.96 GFLOPs | 精度低于 CountGD（CARPK/FSC）；依赖文本/视觉原型；实时数字为 384²、单卡口径；密集/遮挡仍误差；不是视频/语义组；不输出不确定 |
| Counting Machine Parts | [2605.17952](https://arxiv.org/abs/2605.17952v1) · 摘要 | 工业垫圈零件计数：FamNet 扩展 + 额外损失，比较传统图像处理、实例分割、密度估计；用 MAE/RMSE 评估堆叠/遮挡 | 小规模工业报告；特定零件/光照/堆叠；不是通用计数；无代码/权重核验；不输出不确定 |

#### DualCount 与 CountGD：密度/点结构与检测式计数不是同一条曲线

DualCount 把密度估计从“逐像素回归”改成“在潜在实例集合上的结构化质量分配”：点解码器给实例中心，密度解码器在实例级质量守恒与质心对齐约束下分配密度。FSC-147 test 11.32 MAE/97.16 RMSE，优于 CountGD 的 12.98/98.35 与 T2ICount 的 11.76/97.86；但 CARPK 上 CountGD 3.83/5.41 明显更好，DualCount 7.95/9.78。PUCPR+ 两者接近（24.27 vs 24.31）。这说明“密度+点”在通用/密集场景更强，检测式在规则停车场更强；**计数没有单一最优范式，必须按场景/密度/目标尺度报告**。

它的边界是文本/图像编码器、FSC-147 域内、不输出校准不确定性；它给 Clover 的启发是：计数应显式建模**实例级质量分配**，而不是把密度图当独立回归；但下游需要知道“这个数字有多可信”，而当前方法不给。

#### BunchCount：计数单元本身是语义变量

BunchCount 把“数什么”与“数到哪一层”分开：同一图像同一类别，可以数个体，也可以数语义组（一串葡萄、一摞盘子）。GICount 组 MAE 1.85/RMSE 5.49，个体 12.20/28.89；CountGD 组 MAE 9.21，个体 13.54；GroundingREC 组 3.59 但个体 23.17。消融显示关系建模把组 MAE 从 9.21 降到 1.93，但用整个组提示作锚会把个体 MAE 从 13.54 抬到 18.36；只有把“计数单元”从类别语义中解耦，才同时保住组/个体。

它给 Clover 的证据是：**“多少个”必须先定义计数单元**；没有单元条件的计数会在组/个体之间混淆。跨单元错误（个体模型数组 61.73、组模型数个体 73.95）说明类别身份不足以确定粒度；这对“理解场景”是结构性约束，不是标注细节。

#### SVCBench 与 ConvStack：计数是检验世界状态维护的最小探针

SVCBench 把计数变成流式世界状态的诊断：406 视频、10,071 事件，人类总体 GPA 96.1，最佳模型约 37.0；周期事件人类 93.2，最佳模型仅 11.1；盲 LLM 的 MoC 高达 95.7（语言先验知道累计数应单调增），但 GPA 只有 18.7、UDA 4.3。显式计数标注带来 21× 改善，说明模型有推理能力但缺视觉-时间 grounding；旋转相机下身份持续性也会崩。

ConvStack 则从 MLLM 内部机制解释计数失败：patchification 让跨边界碎片难以形成独立物体（个体化瓶颈），注意力压缩让数值增大时表示分离度下降（聚合崩溃）。它用卷积残差适配器注入局部 token 混合，PixMo-Count 75.19%（+9.73），计数 6–10 从 56.8% 到 98.8%，silhouette 0.479→0.707，并顺带提升空间理解。

两者共同说明：**计数不是“数数头”问题，而是个体化 + 状态维护 + 聚合**。SVCBench 的“人类 vs 模型”差距与 ConvStack 的“表示分离度”是同一失败的两层证据；Clover 若把计数作为世界理解的探针，必须同时测物体计数、事件计数、累计状态与身份持续，而不是单图 MAE。

#### RT-Counter 与工业计数：实时性和测量场景的取舍

RT-Counter 用 Visual Prototype Textualization + Weaformer 把文本引导计数压到 38M 参数、112.48 FPS、21.37 GFLOPs（384²），FSC-147 13.30/104.63、REC-8K 5.72/18.19、CARPK 4.81/7.61；CountGD 213M/4.6 FPS/98.96 GFLOPs，精度更高但慢 24×。它证明“实时开放词汇计数”可行，但精度仍低于重型检测式方法；实时数字是 384²、单卡口径，不能外推到高分辨率/密集场景。

Counting Machine Parts 把计数放到工业垫圈堆叠/遮挡：FamNet 扩展 + 额外损失，与传统图像处理、实例分割、密度估计比较，用 MAE/RMSE 评估；这是小规模工业报告，特定零件/光照/堆叠，不是通用计数。它提醒 Clover：**“视觉测量”不仅是数数，还包括堆叠、遮挡、尺度与公制尺寸**；工业场景的标注/域偏移与自然图像不同，不能用 FSC-147 的分数替代。

**本节结论：** 计数至少分五层：**实例计数**（DualCount/UpCount/CountGD）、**语义组计数**（BunchCount）、**事件/流式计数**（SVCBench）、**MLLM 个体化/聚合**（ConvStack）、**实时/工业测量**（RT-Counter/Machine Parts）。2026 的证据显示：密度/点结构在通用场景更强，检测式在规则场景更强；组计数需要显式计数单元；流式事件计数仍是人类-模型差距最大的地方；MLLM 的失败可定位到个体化与聚合；实时计数以精度换速度。Clover 若声称“理解世界”，计数验收必须报告：计数单元、实例/组/事件分层、流式状态、MAE/RMSE、时延/分辨率、校准/不确定性；单图 MAE 或单一 SOTA 不够。

<a id="pose-wholebody-2026"></a>

### 人体、手部与全身 3D：从单帧网格到在线世界坐标

“姿态”不是单一输出：2D 关键点、3D 人体网格、手部关节、全身 SMPL-X、世界坐标轨迹、6D 物体位姿，指标与坐标系都不同。此前这一行只有 ViTPose、Sapiens、PnP-Transformer；本轮补 10 篇 2026 年工作，覆盖基础 HMR、实时加速、在线世界坐标、遮挡运动先验、手部感知全身、第一人称手部、多视图手部、合成数据与事件相机。

| 方法 | 一手来源 | 机制与可核查证据 | 边界与反假设 |
|---|---|---|---|
| SAM 3D Body | [2602.15989](https://arxiv.org/abs/2602.15989v1) · [代码](https://github.com/facebookresearch/sam-3d-body) · 正文选读 | 单图全身 HMR：Momentum Human Rig（MHR）解耦骨架/表面；编码器-解码器 + 2D 关键点/掩码 prompt；VLM 数据引擎挖掘遮挡/罕见姿态/交互/极端尺度；3DPW PA-MPJPE 33.2/MPJPE 54.8/PVE 64.1，EMDB 38.5/62.9/74.3，RICH 31.9/55.0/61.7，COCO PCK 86.8；手部有独立 decoder | 需要人体网格模型/训练数据；多阶段标注/拟合成本高；极端遮挡/截断仍失败；手部精度仍低于专用手部模型；不是视频时序/世界坐标；推理数秒/图（见 Fast 版） |
| Fast SAM 3D Body | [2603.15603](https://arxiv.org/abs/2603.15603v1) · 正文选读 | 训练-free 加速：解耦空间先验、静态图重构、decoder 剪枝、GPU 手部 crop、神经运动学投影；3DPW automatic 0.8→6.6 FPS、EMDB 1.0→8.3、Harmony4D 0.6→6.5（最高 10.9×）；MHR→SMPL 0.24→1992 FPS（>8300×）；单 RGB 遥操作 Unitree G1 端到端 65 ms；手部 9.8→45.5 FPS | 精度略降（3DPW automatic PA 26.8→29.7、MPJPE 57.6→58.9；Oracle MPJPE 54.8→59.5）；依赖 YOLO11-Pose 手部 crop；遥操作/策略演示有限；不是世界坐标/长期身份 |
| OnlineHMR | [2603.17355](https://arxiv.org/abs/2603.17355v1)（CVPR 2026） · 正文选读 | 全在线世界坐标 HMR：因果 KV cache + 滑动窗口；人类中心增量 SLAM 对齐世界；软人体掩码改善 SLAM；3.3 FPS/0.30 s 平均延迟；WA-MPJPE 93.5（Human3R 112.2、TRACE 529.0）；软掩码 ATE DROID 2.52→1.07、MASt3R 1.22→0.83；速度正则降 jitter | 依赖增量 SLAM/历史 EMA；突然切镜/多相机失败；W-MPJPE 受尺度转换拖累；3.3 FPS 低于 TRACE 24.6；不是多人/长期身份；世界坐标尺度仍弱 |
| MoPO | [2605.09856](https://arxiv.org/abs/2605.09856v1)（Pattern Recognition） · 正文选读 | 遮挡 HMR：时空遮挡检测 + 轻量运动预测器补全关节 + 运动感知融合/IK 细化；3DPW-OC MPJPE 64.9（DPMesh 70.9）、PA 41.2；3DOH 95.7（97.1）；3DPW-PC 76.0（82.2）；3DPW-Crowd 82.1（DPMesh 79.9，crowd 上并非全面更好） | 依赖 2D 姿态检测器/视频序列；运动先验可能补出错误但平滑的姿态；遮挡检测阈值敏感；不是单图/世界坐标；没有手部/面部细节 |
| DanceHMR | [2605.18102](https://arxiv.org/abs/2605.18102v3) · [项目页](https://shenwenhao01.github.io/dancehmr/) · 正文选读 | 单目视频手部感知全身 SMPL-X：body context + part-specific hand tokens + 残差融合 + close-up 增强；ARCTIC 手 PA-PVE 较 SMPLest-X 降 28.6%、手 PVE 降 13.9%；手 Jitter 较 GVHMR+HaMeR 降 43.2%、手 MPJVE 降 32.8%；3DPW PA 35.2/MPJPE 53.6、EMDB 40.1/64.3；46M 参数（SMPLest-X 687M） | 依赖 HMR2.0/HaMeR/ViTPose/RTMW 冻结特征；手部仍受遮挡/截断；不是世界坐标；舞蹈/上半身数据偏差；手物接触物理未验证 |
| PEAR | [2601.22693](https://arxiv.org/abs/2601.22693v2) · 摘要 | 单图像素对齐 expressive HMR：实时 SMPLX 参数推理，改善脸/手细粒度定位与表情 | 摘要级；SMPL-X 模型/训练数据；表情/手部细节仍可能失真；不是视频/世界坐标；未给全表 |
| EgoForce | [2605.12498](https://arxiv.org/abs/2605.12498v1)（SIGGRAPH 2026） · 摘要 | 单目第一人称相机空间绝对 3D 手部姿态/位置：前臂引导，跨鱼眼/透视等头戴光学配置 | 摘要级；第一人称/手部特定；依赖前臂/标定；不是全身/世界坐标；未给跨设备全表 |
| HandMvNet | [2608.20093](https://arxiv.org/abs/2608.20093v2)（VISAPP 2025） · 摘要 | 多视图实时 3D 手部运动/形状：多视图 cross-attention 融合，无需相机参数输入，缓解单目尺度-深度歧义 | 摘要级；多相机/同步；手部特定；不是单目/全身；实时数字依赖硬件 |
| AnyHand | [2603.25726](https://arxiv.org/abs/2603.25726v3) · 摘要 | 大规模合成 RGB(-D) 手部数据集：2.5M 单手法 + 4.1M 手-物交互，含遮挡/手臂/对齐深度；扩展 RGB 基线在 FreiHAND/HO-3D 显著提升 | 合成到真实差距；手部/交互特定；标注自动生成；不是姿态估计方法；许可/数据偏差未核 |
| E-3DPSM | [2604.08543](https://arxiv.org/abs/2604.08543v1)（CVPR 2026） · [项目页](https://4dqv.mpi-inf.mpg.de/E-3DPSM/) · 摘要 | 事件驱动连续姿态状态机：对齐连续人体运动与细粒度事件动态，演化 latent state 预测连续 3D 姿态；面向头戴第一人称事件相机 | 摘要级；事件相机/第一人称；不是 RGB/全身网格；真实数据规模/跨设备未核；不是世界坐标 |

#### SAM 3D Body 与 Fast 版：数据引擎把 HMR 推向“野外”，加速把延迟压到交互级

SAM 3D Body 的关键不只是 MHR 表示，而是**数据引擎 + 多阶段标注**：VLM 挖掘遮挡、罕见姿态、交互、极端尺度、低可见度、手-体协调样本，再用人工关键点、单图/多视图拟合、密集关键点检测生成监督。3DPW PA-MPJPE 33.2/MPJPE 54.8/PVE 64.1，EMDB 38.5/62.9/74.3，RICH 31.9/55.0/61.7，COCO PCK 86.8；手部有独立 decoder，但整体仍是数秒/图。

Fast 版是训练-free 的系统级重构：解耦空间先验、静态图、decoder 剪枝、GPU 手部 crop、神经运动学投影。3DPW automatic 0.8→6.6 FPS、EMDB 1.0→8.3、Harmony4D 0.6→6.5（最高 10.9×）；MHR→SMPL 转换 0.24→1992 FPS（>8300×）；单 RGB 遥操作 Unitree G1 端到端 65 ms；手部 9.8→45.5 FPS。代价是精度略降（Oracle 3DPW MPJPE 54.8→59.5），依赖 YOLO11-Pose 手部 crop，遥操作/策略演示有限。它给 Clover 的启发是：**“原生 ultrafast”可以来自对基础 HMR 管线的系统重构，而不只是换小模型**；但速度必须与精度、坐标系、下游任务一起报。

#### OnlineHMR：在线世界坐标 HMR 的瓶颈是尺度与切镜，不是单帧精度

OnlineHMR 把 HMR 放进流式世界坐标：因果 KV cache + 滑动窗口保证不依赖未来帧；人类中心增量 SLAM 提供世界对齐；软人体掩码减少动态人区域对 SLAM 特征匹配的干扰。3.3 FPS、0.30 s 平均延迟、WA-MPJPE 93.5（Human3R 112.2、TRACE 529.0）；软掩码把 DROID-SLAM ATE 从 2.52 降到 1.07、MASt3R 从 1.22 降到 0.83；速度正则显著降低 jitter。

它的边界很清楚：依赖增量 SLAM/历史 EMA，突然切镜/多相机失败；W-MPJPE 受尺度转换拖累；3.3 FPS 低于 TRACE 的 24.6；不是多人/长期身份。它说明**世界坐标 HMR 的误差分解必须分开**：局部姿态、相机轨迹、尺度、时间一致性；单看 PA-MPJPE 不能说明“人在世界里在哪”。

#### MoPO 与 DanceHMR：遮挡靠运动先验，手部靠时序融合

MoPO 用“姿态序列本身比遮挡图像特征更可靠”的假设：时空遮挡检测 + 轻量运动预测器补全关节 + 运动感知融合/IK。3DPW-OC MPJPE 64.9（DPMesh 70.9）、3DOH 95.7、3DPW-PC 76.0；但 3DPW-Crowd 82.1 并非全面优于 DPMesh 79.9，说明人群遮挡与物体遮挡不同。

DanceHMR 则把手部放进全身时序：body context + part-specific hand tokens + 残差融合 + close-up 增强。ARCTIC 手 PA-PVE 较 SMPLest-X 降 28.6%、手 PVE 降 13.9%；手 Jitter 较 GVHMR+HaMeR 降 43.2%、手 MPJVE 降 32.8%；3DPW PA 35.2/MPJPE 53.6、EMDB 40.1/64.3；46M 参数 vs SMPLest-X 687M。

两者共同说明：**遮挡/手部不是“更多图像特征”能解决的，需要运动/时序先验**；但运动先验可能补出“平滑但错误”的姿态，必须用真实遮挡/接触数据反证。

#### EgoForce、HandMvNet、AnyHand、E-3DPSM：手部与第一人称的尺度/视角/传感器问题

EgoForce 用前臂引导单目第一人称绝对 3D 手部，跨鱼眼/透视头戴配置；HandMvNet 用多视图 cross-attention、无需相机参数，缓解单目尺度-深度歧义；AnyHand 提供 2.5M 单手法 + 4.1M 手-物交互合成 RGB-D，扩展基线在 FreiHAND/HO-3D 显著提升；E-3DPSM 用事件驱动连续状态机做头戴第一人称 3D 人体姿态，针对自遮挡与时间抖动。

这四条线共同说明：**手部/第一人称姿态的核心是尺度与视角可观测性**，不是单纯换 backbone。多视图/前臂/合成数据/事件相机都是增加约束；但它们各自带来同步、标定、合成到真实、事件数据规模等新边界。Clover 若把“手部动作”作为世界理解的一部分，必须报告坐标系（camera/world）、绝对尺度、遮挡/截断、时序抖动与传感器条件。

**本节结论：** 姿态 2026 的证据分成六层：**基础 HMR**（SAM 3D Body）、**实时加速**（Fast SAM 3D Body）、**在线世界坐标**（OnlineHMR）、**遮挡运动先验**（MoPO）、**手部感知全身**（DanceHMR）、**第一人称/多视图/合成/事件手部**（EgoForce、HandMvNet、AnyHand、E-3DPSM）。它们共同推进了“野外全身/手部”的精度与速度，但也暴露四个未解问题：世界坐标尺度、手部遮挡/接触、时序抖动、跨设备/事件数据。Clover 的姿态验收必须指定输出（2D/3D/网格/手/世界坐标）、坐标系、指标（PA-MPJPE/MPJPE/PVE/PCK/Jitter）与硬件；单一 PA-MPJPE 不能代表“理解了人体动作”。

### 部件、可供性与 alpha 边界：结构化输出补上“能怎么动”

| 方法 | 一手来源 | 机制与可核查证据 | 边界与反假设 |
|---|---|---|---|
| UniRAP | [2610.29768](https://arxiv.org/abs/2610.29768v1) · 正文选读 | 统一部分级物理可供性推理与可操作几何：Qwen2.5-VL 3B + SAM2.1；四阶段课程（461K 分割、253K 可供性、视觉指代、RealVLG 动作微调）；Unified Affordance Decoder 联合检测、部分级可供性分割、4-DoF 抓取姿态；真实 Franka 13 物体直接 4-DoF 抓取 88.5%，高于 RealVLG-R1 62.3% 与 UniRAP+GraspNet 55.4% | **作者自述**：受算力限制未扩数据/模型，未纳入 PixelQA；强调需研究更小模型的实时可操作感知；4-DoF 姿态是任务定义；可供性标签由人定义，不证明物理可行；视频 Grasp 数据缺失，用伪序列评估时序；开放世界部件/工具迁移另测 |
| SAM2Matting | [2606.27339](https://arxiv.org/abs/2606.27339v1) | tracker-to-matting：给 SAM2/SAM3 跟踪器加 region-proposal bridge 与专用 matting head，跟踪器负责时序一致、matting 头负责细边界；作者报告仅在图像上训练即可在视频抠像 SOTA，支持多种 prompt，并在人体/野外场景泛化 | `L1` alpha/掩码监督；跟踪错误会传播为 alpha 错误；alpha 是外观分解，不证明透明/反射/折射的物理分解；视频基准与评价协议有限；扩散/大模型成本未计入实时性 |

<a id="affordance-parts-2026"></a>

#### 开放世界部件与功能：2D/3D affordance、part 分解与功能场景

“这个物体能怎么用”不是单一标签：它要求定位**可操作区域**（affordance）、分解**部件**（part）、理解**功能/铰接**（articulation），并把这些落到 2D 像素或 3D 点云。此前这一行只有 UniRAP 与 SAM2Matting；本轮补 10 篇 2026 年工作，覆盖开放世界 3D affordance、2D-3D 统一、部件分解、合成数据与功能场景重建。

| 方法 | 一手来源 | 机制与可核查证据 | 边界与反假设 |
|---|---|---|---|
| AffordAny | [2608.20720](https://arxiv.org/abs/2608.20720v1) · [代码](https://github.com/lzlfwow/AffordAny) · 正文选读 | 单目 RGB 开放世界 3D affordance：自动构建 5,334 物体/473 类、10,633 part 样本；冻结 Cosmos-2B + 3D 几何 decoder（投影注入/语义压缩/双向融合）；unseen instruction IoU 0.680、unseen object 0.428、unseen category 0.305；指令改写 IoU 差 0.105（OpenAD 0.166、LASO >0.34）；伪标签自训练提升 unseen-category mIoU +6.3% | 自动融合标签/重建误差；7,398 物体中 2,064 无可验证 part；长尾类别/部件；需要单图重建；不是物理接触/真实操作；语言本体限制 |
| UniAfford | [2609.37264](https://arxiv.org/abs/2609.37264v1) · 正文选读 | 2D-3D 统一 affordance：MLLM + token router 路由到 2D/3D 分支，联合像素/点云监督；AGD20K 27.52 gIoU/25.22 cIoU；GEAL* 83.55 AUC/14.67 mIoU；ReasonAff 71.19 gIoU/73.63 cIoU；PIAD 14.25 mIoU（DAG 9.73） | 依赖大 backbone；语义级配对不建立实例级空间对应；未闭环机器人；2D/3D 标注本体不同；不是纯视觉（任务指令） |
| AFUN | [2606.02551](https://arxiv.org/abs/2606.02551v1) · 摘要 | 从单 RGB-D + 语言任务预测任务条件功能掩码与可执行运动，朝 affordance foundation model 推进 | 摘要级；RGB-D/机器人域；任务条件依赖语言；物理可行性未闭环；不是纯视觉 |
| VoxAfford | [2605.01365](https://arxiv.org/abs/2605.01365v1) · 摘要 | 开放词汇 3D affordance：把冻结 3D VQVAE 多尺度几何特征注入 MLLM 输出 token，缓解自回归 token 空间定位弱 | 摘要级；点云输入；依赖 MLLM/VQVAE；未给跨数据集全表；不是 2D/机器人闭环 |
| AFFORDMEM | [2605.11616](https://arxiv.org/abs/2605.11616v1) · 摘要 | 跨场景 affordance 记忆 + 场景内空间记忆，训练-free 引导冻结 VLM 定位小可操作区域 | 摘要级；记忆库/检索质量；场景特定；不是 3D 几何/物理；未给全表 |
| PartLLM | [2609.25832](https://arxiv.org/abs/2609.25832v2)（SIGGRAPH Asia 2026） · [项目页](https://czvvd.github.io/PartLLMPage/) · 正文选读 | 把 3D part 分割统一为自回归语义分解：LLM 生成 part 假设作为 mask query，decomposition-aware decoder 联合出 mask；全形状 mask mIoU：PartNeXt 56.7、3DCoMPaT200 86.1/74.2；SA-mIoU 43.2/71.9/63.1；文本引导 PartNet-E 50.1、PartNeXt 78.7、3DCoMPaT200 86.1/80.0 | 依赖 3D 训练数据/Qwen3-VL；part 名称本体/粒度；生成式假设可能漏小部件；不是真实扫描/物理；开放世界扫描仍有限 |
| UniPart | [2609.12898](https://arxiv.org/abs/2609.12898v1) · 正文选读 | 零样本文本引导 3D part 分割：CLIP 文本条件 + 跨模态 3D Transformer；LangPart-1M 8M text-part 对/160K+ 资产；Objaverse-General 49.27 mIoU（FIND3D 34.10）、unseen 45.23（27.41）；LangPart-1K 33.56；真实抓取 part 分割 90.5%、下游抓取 85.0% | 依赖合成资产/自动标签；单物体点云；不是场景/关节/物理；真实传感器噪声/遮挡有限；语言本体限制 |
| FlexPart | [2610.23659](https://arxiv.org/abs/2610.23659v1) · 摘要 | 文本控制 3D mesh 分割：语义 part 名 + 位置/形状子句，VLM 管线构建多粒度数据，支持“要什么粒度给什么粒度” | 摘要级；依赖 VLM 数据管线；mesh 输入；粒度/本体控制未量化；不是真实扫描/物理 |
| PartImageNet++ | [2601.01454](https://arxiv.org/abs/2601.01454v1) · 摘要 | 100K 图像/ImageNet-1K 全类别 part 标注；多尺度 part 监督识别模型（MPM）用伪 part 标签扩展 | 摘要级；2D 图像/类别级 part；标注成本/质量；不是 3D/affordance；与 2407.10918 有文本重叠 |
| FunRec | [2604.05621](https://arxiv.org/abs/2604.05621v2)（CVPR 2026） · [项目页](https://functionalscenes.github.io) · 正文选读 | 从第一人称 RGB-D 交互视频重建功能 3D 场景：自动发现铰接部件、估计运动学参数、跟踪 3D 运动、规范化重建；RealFun4D 351 序列/60 公寓、OmniFun4D 127 序列；铰接轴误差 5.3°/5.4°（基线 38–60°）、6D part ADD-S 78.96/79.43/75.62、part mIoU 77.9/76.4/74.8；训练-free | 需要 RGB-D/第一人称；交互覆盖/标注；不是单目 RGB；静态/铰接物体，不是可变形/多物体物理；仿真导出仍需物理校验 |

##### AffordAny：从单目 RGB 做开放世界 3D affordance，语言改写是最容易暴露的短板

AffordAny 用单目 RGB 自动构建 5,334 物体/473 类的 3D part 监督，冻结 Cosmos-2B 特征 + 几何 decoder 做开放世界 affordance。unseen instruction IoU 0.680、unseen object 0.428、unseen category 0.305；指令改写下 IoU 只掉 0.105，而 OpenAD 掉 0.166、LASO/LMAffordance3D 掉 >0.34——说明它的语义压缩与几何融合对措辞变化更稳。伪标签自训练把 unseen-category mIoU 提升 6.3%，主要来自尾部类别。

但它仍是“自动标签 + 单图重建”：7,398 个物体中 2,064 个没有可验证 part，长尾类别/部件偏差明显；不是物理接触/真实操作。它给 Clover 的启发是：**开放世界 affordance 的评测必须单独报告语言改写、未见类别、未见物体三条轴**，否则“开放词汇”可能只是记住了同义提示。

##### UniAfford：2D 与 3D affordance 可以共享语义，但实例级对应仍缺

UniAfford 用 MLLM + token router 把 2D/3D 分支统一：AGD20K 27.52 gIoU/25.22 cIoU，GEAL* 83.55 AUC/14.67 mIoU，ReasonAff 71.19/73.63，PIAD 14.25 mIoU（DAG 9.73）。它的关键设计是**路由 hidden state 到任务分支**，让像素级/点级损失塑造共享表示，而不是让语言头生成特殊 token。

边界也明确：依赖大 backbone；语义级配对不建立实例级空间对应，几何一致性监督有限；未闭环机器人；2D/3D 标注本体不同。它说明 **2D-3D 统一不是“同一个输出头”，而是共享语义 + 分支解码**；Clover 若做统一 affordance，必须报告 2D/3D 分项与跨模态一致性。

##### PartLLM 与 UniPart：部件分解从“固定本体”转向“语言/粒度可控”

PartLLM 把 3D part 分割统一为自回归语义分解：LLM 生成 part 假设作为 mask query，decoder 联合出 mask。全形状 mask mIoU PartNeXt 56.7、3DCoMPaT200 86.1/74.2；SA-mIoU 43.2/71.9/63.1；文本引导 PartNet-E 50.1、PartNeXt 78.7、3DCoMPaT200 86.1/80.0。相对 PartSAM/P3-SAM，它的优势是**mask 与语义一起生成**，减少“几何重叠但语义错”的两阶段误差。

UniPart 则用 CLIP 文本条件 + 跨模态 3D Transformer，LangPart-1M 8M text-part 对；Objaverse-General 49.27 mIoU（FIND3D 34.10）、unseen 45.23（27.41）；真实抓取 part 分割 90.5%、下游抓取 85.0%。控制实验显示架构 +14.69%、数据 +24.94%，说明“数据引擎”与“跨模态对齐”都关键。

两者共同说明：**部件不是固定类别的分割，而是语言/粒度条件的分解**；但合成资产、自动标签、part 本体与真实扫描的差距仍在。Clover 的部件验收应报告粒度、语言改写、未见类别、真实传感器噪声与下游任务，而不只是 mIoU。

##### AFFORDMEM、AFUN、VoxAfford、FlexPart、PartImageNet++：记忆、基础模型、体素与数据

AFFORDMEM 用跨场景 affordance 记忆 + 场景内空间记忆，训练-free 引导冻结 VLM 找小可操作区；AFUN 从 RGB-D+语言预测任务条件功能掩码与运动，朝 affordance foundation model；VoxAfford 把冻结 3D VQVAE 多尺度几何注入 MLLM token；FlexPart 用语义 part 名+位置/形状子句控制粒度；PartImageNet++ 提供 100K 图像/ImageNet-1K 全类别 part 标注。

这些工作分别补上 **记忆、基础模型、体素几何、粒度控制、数据规模**，但都还是摘要级，且共同依赖语言/自动标签/合成数据；没有一篇同时证明“开放世界 + 3D 几何 + 物理可行 + 真实机器人闭环”。

##### FunRec：功能场景重建把“部件”提升到“可交互的铰接 3D”

FunRec 从第一人称 RGB-D 交互视频重建功能 3D 场景：自动发现铰接部件、估计运动学参数、跟踪 3D 运动、规范化重建。RealFun4D 351 序列/60 公寓、OmniFun4D 127 序列；铰接轴误差 5.3°/5.4°（基线 38–60°）、6D part ADD-S 78.96/79.43/75.62、part mIoU 77.9/76.4/74.8；训练-free。它把“部件”从静态 mask 提升到**可动的功能结构**，并导出仿真可用 mesh。

边界是 RGB-D/第一人称、交互覆盖/标注、静态/铰接物体（不是可变形/多物体物理）、仿真导出仍需物理校验。它给 Clover 的启发是：**功能理解必须包含“怎么动/怎么用”的 3D 运动学**，而不是只给 part 标签；但 RGB-D 与交互视频不是纯单目 RGB，证据来源要单列。

**本节结论：** 部件/功能/可供性至少三层：**part 分解**（PartLLM/UniPart/FlexPart）、**affordance grounding**（AffordAny/UniAfford/AFUN/VoxAfford/AFFORDMEM）、**功能场景/铰接**（FunRec）。2026 趋势是语言条件、开放世界、2D-3D 统一、记忆与粒度控制；但标签/本体依赖语言、3D 数据多为合成/自动、物理可行性与真实机器人闭环仍缺。Clover 若声称“理解物体能怎么用”，必须报告部件粒度、affordance 本体、2D/3D 分项、语言改写敏感性、真实传感器/接触验证；单一 mIoU 或开放词汇分数不能替代这些证据。

### 二十类能力的本轮覆盖判断

| 能力 | 本轮新增一手证据 | 覆盖判断 | 仍缺的关键证据 |
|---|---|---|---|
| 图像/场景/类别识别 | ResNet/ViT/ConvNeXt/MAE/CLIP/AIMv2/MetaCLIP2、DINOv3、PE、WebSSL；VICAL/OFBD/LIVE/Image-Scale | 强（基准）/部分（开放世界） | 无语言先验的新概念、属性组合、真实开放世界长尾 |
| 实例识别、匹配与检索 | TRAIL/RIA、Open-set ReID、DPM++、MSP-ReID、REMIND、SpikeVPR；WOW-Seg、MoSA、DINOv3/PE；SAM 3；MOTIP2/UGO | 强（基准）/部分（开放世界） | 换衣/遮挡/车型泄漏/开放集拒识；跨摄像头长期记忆仍弱 |
| 检测与定位 | YOLO26、RF-DETR、YOLOv12、D-FINE、DEIM、LW-DETR、Grounding DINO；MonoSAOD、多视图 3D、3D-OVD | 强（2D 封闭集）/部分（3D/开放集） | 未知类别发现、密集小物体、提示依赖与拒答校准；3D 深度/位姿依赖 |
| 语义/实例/全景分割 | SAM 3、WOW-Seg、MoSA、gen2seg、Pano3D、DCR-SAM、MaskMerge、MoRSe、Mask2Former/OneFormer、VC-PQ | 强（提示/封闭集）/部分（统一开放世界） | 单权重多任务、开放世界概念发现、长期实例身份、透明/反光边界 |
| 边界、抠图与透明度 | WeVisOne-VL、SAM2Matting、Amodal SAM、OccJEPA、PHAC、Shape Prototypes、VideoMaMa/++、RenderMatte、FCLM、SAM-Matte、HairGuard、SEP-YOLO、SeeClear、OPC16K、Concentration | 部分（2D 非模态/alpha/透明） | alpha 时序、负样本 FPR、透明深度、软边界、计算/合成到真实；遮挡区真值与 3D 一致性仍需独立测 |
| 计数与视觉测量 | CountGD、UniCounting、DualCount、BunchCount、SVCBench、ConvStack、UpCount、AdaCount、OCCAM、RT-Counter、Counting Machine Parts | 部分（图像/基准）/薄（流式、语义组、测量） | 语义组/事件计数、流式状态、密集小物体、校准/不确定、公制测量 |
| 文字、文档、图表与图解 | PaddleOCR-VL、dots.ocr、MinerU2.5、olmOCR 2、PolyOCR、MEVL-STP、OmniDocBench | 强（文档）/部分（场景文字） | 视频字幕、跨页推理、手写/低资源语言、端侧低延迟 |
| 关键点与姿态 | ViTPose、Sapiens、PnP-Transformer、SAM 3D Body、Fast SAM 3D Body、OnlineHMR、MoPO、DanceHMR、EgoForce、HandMvNet、AnyHand、E-3DPSM | 强（2D/单帧全身）/部分（手/3D/世界坐标/事件） | 手部/全身 3D、严重遮挡、世界坐标尺度、时序抖动、事件/端侧、接触与意图 |
| 光流、匹配与运动分解 | FreeFlow、Foundation-Model Flow、SGFormer、MVLoMa、B2TFPose、SFVO、QuantaFlow、Static-in-Frames、E-TraMamba、E-S2Feat；MoSA、MoRSe、CoTracker3、TAPNext | 强（光流/匹配基准）/部分（运动分解、事件与开放世界） | 极端运动、遮挡、低纹理、尺度变化、匹配不确定性校准、事件语义、下游增益 |
| 任意点追踪 | TAPNext/TAPNext++、CoTracker3、CoWTracker、M2P、TAPFormer、Track4World、3D SSM、MoSE3、Track-On-R、TrackCraft3R、TAPVid-MV、ARROW、E-TraMamba | 强（短时 2D/受控 3D 基准）/部分（绝对米制、事件、`SE(3)`） | 绝对尺度、世界坐标与内参依赖、长时重现、非刚体/关节、语义身份、事件异步、端侧实时、教师上界 |
| 单/多目标追踪与再识别 | SAMURAI、MOTIP2、UGO、GOT-Edit、Point Prompting、SAM-H、OmniTrack++、Cutie、SAM3RL、When Trackers Fail、ByteTrack/ARC-SORT | 强（基准）/部分（开放世界） | 开放世界新类别、长期遮挡、错误恢复的安全保证、非平面/非刚性 |
| 动作、事件、人-物交互、人脸/表情/手势与社会场景 | OZ-TAL、OnPoint、AGA、ZS-SkAA、SP-CLIP、SimVA、FineHOI、HOIBlender、GraspHOI、SAGE、Talking-to-Me、DenseFace、FaceLiVTv2、EventFace、TAG、ActFER、UniCon-Former、EgoEV-HandPose；TrAction/ByteAction/LaGoVAD | 部分（分类/定位/预期/HOI/人脸齐） | 未知动作、细粒度边界、因果意图、3D 接触、人脸偏见/数据缺陷、表情证据绑定、手势任务定义、社会角色/所有权、长视频叙事 |
| 深度、相机、三维与动态重建 | DA3、MoGe-2、Pano3D、Uni4R、SAM 3D、ARROW、TAPVid-MV、VGGT/CUT3R、VolFill、NOVA3R、Event3R；RoPT、GRC-Pose、ComPose、ASM-6D、LEGAU、DICArt、Event6D；OccAny、OccAnyScene、VEOcc、LEXI-SG、LOST-3DSG、OP3DSG、DSG、PanoGraphGS、FALCON | 强（静态/短时）/部分（单帧或短时物体位姿、受控 CAD/RGB-D、语义税则） | 动态场景、隐藏几何的欠定性、度量尺度、透明/反光、物理接触、任意时刻运动学、事件模拟数据、物体级长期状态、无 CAD/类别先验、遮挡恢复、端到端延迟、在线纯视觉位姿、动态场景图变化、确定性延迟 |
| 空间定位、里程计与在线建图 | UniSim-SLAM、FFVO、VGGT-GS SLAM、FoundationVIO、Failure or Drift、MomentBA、HuMemSLAM、OASIS、RawSLAM、RingNav、DAPEVO、GS 综述 | 部分（静态室内/驾驶基准）/薄（动态开放世界与纯视觉度量尺度） | 纯 RGB 绝对尺度、动态物体、长期地图维护、显式失败/漂移分离、几何-语义统一状态、端侧实时 |
| 部件、关系、功能与可供性 | RelWitness、NoPA、层次 3D 场景图、RelationVGGT、UniFunc3D、UniRAP、AffordAny、UniAfford、AFUN、VoxAfford、AFFORDMEM、PartLLM、UniPart、FlexPart、PartImageNet++、FunRec | 部分（2D/3D 基准）/薄（物理闭环） | 关系不完整/词表、3D 位姿依赖、功能/因果推断、跨物体迁移、部件粒度、affordance 本体、真实接触/物理验证 |
| 持续存在、记忆与修正 | iSEE、PersistBench、WROP、PPMem、Grid or Nodes、SAM3RL、When Trackers Fail、TAPNext++、OccJEPA、Amodal SAM、VolFill、R4DSG、Ledger、EgoProbe、EgoMonth、VideoLoop、PREM | 部分（短时/长时基准） | 纯视觉持久状态、精确事件召回、场景边界/跨月、在线更新、补全幻觉的写回、反证后修正 |
| 物理、因果与反事实 | 单图质量、PhysicsLENS、ViTacPhys、ViWi、Causal-JEPA、ITC、Axiomatic World Modeling；既有系统辨识/因果表示 | 部分（本轮新增） | 真实相机下的唯一可识别性、干预等价类、反事实校验；触觉/WiFi 反证 |
| 组合、抽象与视觉推理 | TraceViT、Locality-Length、Reachability、DIFFCZSL、PRPC、CS-CLIP、JRDB-AVR；RelationVGGT、WeVisOne-VL、SetCon、TempoGround | 部分（基准）/薄（自然开放世界） | 低支持组合、规则抽象、长输入状态、答案-证据绑定、纯视觉先验 |
| 开放世界、学习与可靠性 | WOW-Seg、LaGoVAD、AdvPCS、WebSSL、RF-DETR、TrackFlood、长尾/尺度研究、Checkpoint-Selection、Colorist、GATE、RADC、CTTA、Geographic-JEPA、FORGE | 部分（基准/TTA） | 持续偏移/遗忘、MLLM TTA、source-free/transductive、校准、端侧、真实部署 |
| 主动观察及行动用途 | FoveaVLA、EgoReveal、Rendering-Free Lookahead、Adaptive Observation、SpatialScout、ActiveArena、CanViT、I-Perceive、ActiveScale、LEAP、CoMe-VLA、BAVO/A-FAR、LEAP-NBV、TAVIS、Epistemic-Trap | 部分（基准/模拟）/薄（真实成本/风险） | 信息增益/成本/风险联合、不可逆动作、真实机器人转移、记忆写入/修正 |

**覆盖判断的含义：** “强”只指在该能力的原始基准与数据条件下有一手比较；“部分”指已有机制但缺开放世界/长时/跨任务证据；“薄”指本轮没有补到足够的一手新证据。三类都不是 Clover 的实现状态。最大的共同缺口仍是：跨能力的共享身份、未知概念发现、物理/因果识别，以及速度-证据保留的联合验收。

<a id="unified-model-comparison"></a>

### 统一视觉模型的同协议比较：共享什么、分开什么

“一个模型同时识别、检测、分割、追踪、阅读”是 Clover 的核心目标，也是当前文献最容易被“统一”一词掩盖的地方。下表只比较**权重/接口/训练/数据**四个层面实际共享了什么；不是 SOTA 排名。

| 模型/家族 | 声称覆盖 | 实际共享 | 接口与训练 | 不能声称 |
|---|---|---|---|---|
| Pix2Seq | 检测、分割、关键点、描述 | 共享序列接口/架构；任务与数据仍分训 | 任务提示 + 自回归序列；框/点/掩码/文本 token | 一个权重全任务；长期状态/追踪；密集像素精度 |
| Mask2Former | 语义/实例/全景分割 | 共享掩码注意力架构；每个任务/数据集分开训练 | 掩码分类接口；任务数据分训 | 单权重多任务；追踪身份；开放世界 |
| OneFormer | 语义/实例/全景分割 | 共享任务 token 与联合训练；每个数据集一个模型 | 任务 token + query–text 对比 | 跨数据集单权重；新任务；长期身份 |
| SAM 3 | 概念分割（图像/视频）+ 视觉分割 | 单模型 ~850M；检测器/追踪器共享骨干；PCS/PVS 共享接口 | 名词短语/exemplar/点框提示；数据引擎 4M 概念 | 分类/OCR/姿态/计数/几何；单 GPU 实时多目标；细粒度 OOD |
| WeVisOne-VL | 检测、指代、计数、OCR、分割、抠图 | 单 VLM + 轻量像素解码器；对象级/像素级共享 `<OBJ>` 接口 | Qwen3-VL 2B/4B；三阶段 SFT + 混合 RL；L1/L2 | 视频追踪/长期身份；纯视觉学习；复杂推理/单轮限制；端侧低延迟 |
| WOW-Seg | 开放世界分割 + 区域识别 | 单 VLLM + Mask2Token；分割器可外接 | 掩码→视觉 token→类别名；训练用掩码/类别标签 | 检测/追踪/OCR/姿态；无语言预训练；任意新概念发现 |
| DCR-SAM | 多类语义分割（SAM3 适配） | 共享 SAM3 视觉/文本表示 + 稠密竞争头 | 文本概念 + 批量推理；33× 加速 | 通用多任务；实例身份；开放世界追踪 |
| YOLO26 家族 | 检测、实例分割、分类、姿态、旋转框 | 共享架构/训练配方；**不同 head 与 checkpoint** | 各任务单独训练；双头 NMS-free；19 导出后端 | 一个权重全任务；统一状态；真实相机闭环 |
| Perception Encoder | 分类/检索/检测/深度/视频 | 共享编码器；语言/空间对齐头分开 | 对比预训练 + 任务头/对齐 | 单次前向输出全部任务；状态/记忆；开放世界 |
| V-JEPA 2 | 视频理解、预测、机器人规划 | 共享视频编码器；动作条件/规划头另训 | 视频自监督 + 动作条件后训练 | 密集分割/OCR/检测；纯被动视觉通用物理 |

**同协议比较必须固定的条件：**

1. **权重层面：** 是一个 checkpoint 的前向，还是共享骨干 + 多个头/多个 checkpoint；后者不能记作“单模型多任务”。
2. **训练层面：** 是否在同一数据混合上联合训练；任务 token/提示是否只是路由；是否存在任务间负迁移。
3. **接口层面：** 框/点/掩码/alpha/文本/身份是否由同一输出头产生；多任务请求是一次前向还是多次调用。
4. **能力层面：** 同一权重是否同时保持识别、检测、分割、追踪、阅读、姿态、计数、几何；不能用一个任务的分数代表其他任务。
5. **时延层面：** 单任务、并发多任务、最坏目标数/分辨率/历史长度；完整输出（框+掩码+文本）完成时间，而非首 token。
6. **数据层面：** 各任务的监督来源（L1/L2/L3/L4）、数据规模、许可与预训练-评测重叠；不能把数据优势写成架构优势。

**当前判断：** 现有“统一”模型分别在**接口统一**（Pix2Seq/OneFormer）、**骨干统一**（SAM 3/PE）、**对象-像素统一**（WeVisOne-VL）、**家族统一**（YOLO26）上推进；没有一个在单权重、单次前向、匹配数据/算力下同时覆盖二十类能力并保持长期身份。Clover 的“一个模型”主张必须先通过上述六项同协议验收，才能与“多个专家模型 + 路由”区分开。

<a id="tracking-comparison"></a>

<a id="recognition-comparison"></a>

### 识别任务的同协议对照：分类、开放词汇、检测、分割、阅读与指代

“识别图片”不是单一能力。下表把本轮证据按任务族并排；每一行的指标、监督和失败模式不同，不能用一个 top-1 或一个 mAP 代表“识别”。

| 能力族 | 代表方法 | 输入/监督 | 主要指标 | 主要失败 | 不能跨任务比较 |
|---|---|---|---|---|---|
| 封闭集分类 | ResNet、ViT、ConvNeXt、MAE、CLIP、AIMv2、MetaCLIP2、SigLIP2、PE、WebSSL | 图像；`L1` 标签或 `L2` 图文或 `L0` 自监督 | top-1/top-5、线性探针 | 背景捷径、长尾、尺度、开放世界 | 分类精度不推出定位/分割/追踪/文字 |
| 开放词汇识别 | CLIP、PE、MetaCLIP2、WOW-Seg、WeVisOne-VL | 图像；图文/VLM 语义先验 | 零样本 top-1、区域语义相似度/IoU | 提示依赖、词表/本体、细粒度 OOD | 零样本分类≠未知概念发现；区域识别≠检测 |
| 长尾/细粒度/尺度 | VICAL、OFBD、LIVE、Image-Scale | 图像；长尾/细粒度标签或 MLLM 推理 | 每类/长尾组精度、FGVR 指标、尺度曲线 | 背景偏置、候选列表、分辨率、尾部样本 | 平均值掩盖尾部；分类协议不覆盖检测/跟踪 |
| 检测 | YOLO26、RF-DETR、YOLOv12、D-FINE、DEIM、LW-DETR、Grounding DINO | 图像；框/类标签，开放词汇加文本 | AP、小/中/大物体 AP、FPS | 小物体、密集长尾、NMS/后端、开放集 | AP 不推出分割/追踪/阅读；FPS 非端到端 |
| 分割 | SAM 3、WOW-Seg、MoSA、gen2seg、DCR-SAM、MaskMerge、Mask2Former、OneFormer | 图像/视频；掩码、点/框/文本/exemplar | mask IoU、PQ、J&F | 提示信息、边界、实例身份、透明/反光 | 掩码 IoU 不推出类别/身份/物理 |
| 文字/文档 | PaddleOCR-VL、dots.ocr、MinerU2.5、olmOCR 2、PolyOCR、MEVL-STP | 文档/场景图；OCR/结构标签 + LLM | CER/Edit、TEDS、阅读顺序、RMS-F1 | 阅读顺序、表格/公式、版本漂移、小字 | 转写准确≠语义理解；文档≠场景文字/视频 |
| 动作/事件 | OZ-TAL、OnPoint、AGA、ZS-SkAA、SP-CLIP、SimVA、TrAction、ByteAction、LaGoVAD | 视频/骨架/bitstream；动作标签/点标签/语言 | top-1、mAP@tIoU、AUC、预期准确率 | 背景捷径、未知动作、时序边界、意图歧义、异常定义 | 分类≠在线定位≠因果意图 |
| 指代/grounding | Grounding DINO、WeVisOne-VL、Qwen3-VL-Seg、SetCon、TempoGround | 图像/视频 + 语言；指代/框/掩码 | gIoU、box AP、set completeness | 语言歧义、词表、流式身份、集合互斥 | 单帧 grounding≠视频身份/追踪 |
| 计数 | CountGD、UniCounting | 图像；文本/exemplar 或固定词表 | MAE、向量 L1、presence F1 | 重复检测、遮挡、密集、固定词表 | 计数≠实例分割/空间关系 |
| 姿态/6D/几何 | ViTPose、Sapiens、PnP-Transformer、DA3、MoGe-2 | 图像/视频；关键点/6D/深度/位姿 | mAP、AR、ADD、深度/尺度误差 | 无纹理、对称、遮挡、透明、尺度 | 2D 姿态≠3D/接触/意图；几何≠物理 |
| 3D 检测/场景图 | MonoSAOD、多视图 3D 检测、3D-OVD、NoPA、RelWitness、层次 3D 场景图 | 单目/多视图 + 深度/位姿/3D 标签/语言 | 3D AP、关系召回、任务推理 | 稀疏 3D 标注、开放词汇、关系不完整、深度/位姿 | 2D AP/图像关系≠3D 物理关系或因果 |
| 3D 关系/可供性 | RelationVGGT、UniRAP、UniFunc3D | 多视图/视频 + 语言；关系/可供性标签 | 关系/掩码/抓取成功率 | 关系词表、标注管线、极小部件、接触可行性 | 关系/可供性≠通用识别或因果 |

**对照结论：**
1. **任务标签不同：** 分类是图像级、检测是框、分割是像素、OCR 是字符/结构、动作是时序、指代是语言条件、计数是数量、姿态/几何是坐标；这些指标不可互换。
2. **监督/先验不同：** `L0` 自监督、`L1` 标签、`L2` 语言、`L3` 动作、`L4` 深度/位姿/力必须分开；同一“识别”分数可能来自完全不同的信息来源。
3. **失败模式不同：** 背景捷径、长尾、尺度、提示依赖、边界、阅读顺序、遮挡、对称、重复计数、语言歧义必须分项测。
4. **同协议条件：** 固定输入分辨率/提示/词表/训练数据/算力；报告能力向量而非单一分数；至少同时覆盖类别、定位、像素、文字、时序、语言条件、数量、几何中的多个维度。

**对 Clover 的验收含义：** “识别图片”应被拆成可分别证伪的能力向量；一个模型在 ImageNet 或 COCO 上的高分，不能证明它能读文档、数物体、理解指代或恢复 3D 关系。Clover 的广义识别主张必须按这张表逐项验收。

<a id="retrieval-reid-2026"></a>

### 实例检索与再识别：同一身份跨时间、跨相机、跨外观

实例检索/再识别与“追踪”相邻但不同：追踪给的是连续轨迹，ReID 给的是**跨摄像头/跨时间/跨外观的同一身份候选**。下表补齐本轮此前较薄的“实例识别、匹配与检索”能力。

| 方法 | 一手来源 | 机制与可核查证据 | 边界与反假设 |
|---|---|---|---|
| TRAIL | [2609.07373](https://arxiv.org/abs/2609.07373v1)（ECCV 2026） | 用 CRF 把视觉相似度与相机运动一致性结合，在**无序参考库**上做轨迹感知 VPR；作为任意预训练 VPR 骨干的轻量后处理，主基准最高 +8.3pp，跨数据集无需重训，视觉线索稀少时增益最大 | 需要查询序列；只做 place 定位，不是物体/人的身份；数据库无序但仍需覆盖；相机运动一致性假设 |
| RIA | [2602.00841](https://arxiv.org/abs/2602.00841v4) | 在 SPD 流形上建模二阶场景结构，把扰动视为合同变换，用几何感知 Riemannian 映射线性化协方差描述子；零样本接近监督方法，轻微微调后 SOTA | 仍是聚合/描述子方法，不是开放世界语义；二阶统计对极端视角/遮挡的边界；代码“将发布”；VPR 域 |
| Identity-Conditioned Score Fusion | [2610.07366](https://arxiv.org/abs/2610.07366v1) | 无训练地把 face/gait/body 等分数按 gallery 身份条件融合；用同身份一致性 vs 跨身份 impostor 提取身份 profile；三个换衣 ReID 基准上 FNIR 绝对降低最高 8.8% | 需要多线索分数；身份条件融合不是单模型端到端；开放集阈值/校准仍关键；换衣基准有限 |
| DPM++ | [2605.06637](https://arxiv.org/abs/2605.06637v2) | 动态掩码度量学习：按遮挡实例选择可靠身份子空间；CLIP 文本分支提供 ID 语义先验；显著性引导 patch transfer 合成可控遮挡样本；遮挡/整体 ReID 均报告 SOTA | 依赖 CLIP 语义先验；遮挡模式与数据集相关；合成遮挡不等于真实遮挡；身份仍是外观/语义匹配 |
| MSP-ReID | [2603.01640](https://arxiv.org/abs/2603.01640v2)（ICASSP 2026） | 针对换衣 ReID：Hairstyle-Oriented Augmentation 增加发型多样性、Cloth-Preserved Random Erasing 抑制服装纹理但保留体型、Region-based Parsing Attention 强化脸/四肢 | 人物中心；发型/脸部仍是生物特征；换衣基准有限；隐私与偏差未解；不是通用物体 ReID |
| Generalization Limits in Vehicle Re-ID | [2606.01981](https://arxiv.org/abs/2606.01981v1) | 发现常用车辆 ReID 数据集的训练/测试含同 make/model/color 的近重复车辆，方法可靠记忆而非泛化；提出按未见车型与视角分层的评估，SOTA 在未见车型上显著失败 | **负结果/评测反例**：不是新方法；车辆域；说明数据集泄漏与“同款车”混淆；需独立 split |
| REMIND | [2607.09267](https://arxiv.org/abs/2607.09267v1) | 室内通用物体长期 ReID：冻结 DINOv3 + 双 bank 多原型外观记忆 + 部件/背景描述 + 邻域空间共现 + Hungarian 分配与歧义保护；单目 RGB，无需位姿/深度 | 室内/机器人场景；DINOv3 上游来源；长期记忆容量/漂移；空间共现先验；不是开放世界任意物体 |
| SpikeVPR | [2604.03277](https://arxiv.org/abs/2604.03277v1) | 事件相机 + SNN 的 VPR；surrogate gradient 端到端训练，EventDilation 增强速度/时间变化鲁棒性；两基准上接近 SOTA，参数少 50×、能耗低 30/250×，可移动/神经形态部署 | 事件传感器；VPR 不是物体 ReID；SNN 训练/部署栈；真实长时/天气另测；不是纯 RGB |

**对照结论：**
1. **身份层次不同：** place（相机位置）、person/vehicle（类别内个体）、generic object（任意物体）、track ID（连续轨迹）不是同一身份；检索分数不能替代追踪或物理实体状态。
2. **外观变化是核心变量：** 换衣、发型、遮挡、视角、光照、传感器（事件 vs RGB）必须分别测；车辆 ReID 的数据集泄漏说明“同款车”会伪装成高精度。
3. **开放集/未知身份：** open-set 融合与拒识比闭集 rank-1 更接近真实部署；必须报告 FNIR/FPIR、校准与未知拒答。
4. **时间/空间记忆：** REMIND 说明长期 ReID 需要记忆与空间上下文，而不是单帧嵌入；记忆容量、漂移与重入仍需独立测。

<a id="3d-detection-sg"></a>

### 三维检测与三维场景图：从框到实体、关系与任务

二维框检测不回答“物体在三维哪里、彼此什么关系、能否用于任务”。下表补上单目/多视图 3D 检测与 3D 场景图的当前证据；它们仍依赖深度、位姿、3D 标签或语言/VLM，不能当作纯视觉空间理解。

| 方法 | 一手来源 | 机制与可核查证据 | 边界与反假设 |
|---|---|---|---|
| MonoSAOD | [2604.01646](https://arxiv.org/abs/2604.01646v2)（CVPR 2026） | 稀疏 3D 标注下的单目 3D 检测：Road-Aware Patch Augmentation 把分割物体 patch 按 3D 几何一致性贴回道路区域；Prototype-Based Filtering 用 2D RoI 原型相似度 + 深度不确定性筛伪标签 | 依赖稀疏 3D 标注 `L1/L4`；伪标签质量/深度误差传导；单目尺度歧义；不是开放词汇；未证明物理接触/关系 |
| Efficient Multi-View 3D Detection | [2604.13586](https://arxiv.org/abs/2604.13586v1) | 多视图 ViT 3D 检测的动态逐层 token 选择 + 参数高效微调；可训练参数从 >300M 降到 1.6M；NuScenes 上验证 | 多相机标定 `V2`；3D 检测标签 `L1/L4`；token 选择对远小目标的影响；不是单目 V0；实时性未给统一口径 |
| 3D-OVD Co-Distillation | [2608.19973](https://arxiv.org/abs/2608.19973v1)（ECCV 2026） | 开放词汇 3D 检测：co-distillation 用 Hungarian 匹配综合几何一致性/结构 objectness/语义确定性筛新物体；双引导训练含场景不确定性正则与 LLM 层级对齐 | 两阶段发现依赖基础模型；LLM 语义 `L2`；3D 标签/点云或深度；新物体定位/分类错误会进训练；不是纯视觉 |
| NoPA | [2607.00529](https://arxiv.org/abs/2607.00529v1)（ECCV 2026） | 在线 3D 场景图：每个物体用非参数分布而非单个 3D Gaussian，保留几何细节；用 kernel density/MMD 做对象合并；保持实时推理 | 依赖深度/位姿/3D 重建；对象合并仍可能错；关系预测有限；不是纯 RGB 单目；实时性硬件特定 |
| RelWitness | [2605.20823](https://arxiv.org/abs/2605.20823v3) | 开放词汇 3D 场景图：定义 relation witness（支撑=接触+竖直顺序、包含=包围、邻近=度量距离、朝向=面向、稳定=跨视图持续）；从 posed RGB-D 构造 witness，verifier 把未标注关系分为 missing positive/可靠负/不确定 | 需要 posed RGB-D `V1/V2`；关系谓词/角色文本 `L2`；不完整标注导致“未标注≠负”；几何 witness 不是因果/功能关系 |
| Hierarchical 3D Scene Graph | [2602.02456](https://arxiv.org/abs/2602.02456v1)（ICRA 2026） | 多层开放词汇特征 + VLM 关系推断 + LLM/VLM 任务推理；四足机器人多环境部署 | VLM/LLM `L2`；SLAM/位姿；关系由语言先验推断；真实机器人任务有限；不是纯视觉因果 |

**结论：** 3D 检测与场景图把“框”推进到“三维实例+关系+任务”，但每条路线都依赖深度/位姿、3D 标签、语言/VLM 或点云。Monocular sparse-label 与 open-vocab 3D 是当前前沿；真实单目 RGB 下的开放世界 3D 关系/物理因果识别仍未闭合。

<a id="occupancy-scenegraph-2026"></a>

#### 2026 占据、开放词汇场景图与变化检测：从几何到实体状态

3D 检测回答“框在哪”，占据回答“空间是否被占据、被什么占据”，场景图再回答“有哪些实体、它们如何相连、能做什么”。三者不是同一任务：占据可以没有实例身份，场景图可以没有稠密几何，动态场景图还必须处理**物体移动、删除与重现**。下表把 2026 年可核查的工作分成四层：**零样本/跨域占据**（OccAny、OccAnyScene）、**在线具身占据**（VEOcc）、**4D 全景占据跟踪**（OccTrack360）、**开放词汇/部件级/动态场景图**（LEXI-SG、LOST-3DSG、OP3DSG、DSG、PanoGraphGS）与**确定性延迟**（FALCON）。

| 方法 | 一手来源 | 机制与可核查证据 | 边界与反假设 |
|---|---|---|---|
| OccAny | [2603.23502](https://arxiv.org/abs/2603.23502v2) · [项目页](https://valeoai.github.io/OccAny) · 正文选读 | 无标定、零样本城市占据：视觉几何基础模型 + Segmentation Forcing（SAM2 特征）+ Novel-View Rendering 做几何补全；在五个城市数据集训练，SemanticKITTI/Occ3D-NuScenes 零样本评测；序列 IoU 25.91（CUT3R* 15.93）、单目 24.03、环视 34.15 | 只验证城市驾驶域；训练仍需五个城市场景数据集与 3D/语义监督；分割特征是开放词汇特征而非完整语义本体；无标定不等于无尺度先验（深度基础模型）；室内/机器人场景未测 |
| OccAnyScene | [2608.08696](https://arxiv.org/abs/2608.08696v3) · [项目页](https://RoboPerception.github.io/OccAnyScene/) · 摘要/正文表 | 单模型跨室内/室外占据：像素视锥高斯 + 深度基础模型 + Pixel-Aligned Frustum Feature Aggregation，处理不同相机、范围、体素与语义税则；Occ-ScanNet 59.92 mIoU、SurroundOcc-nuScenes 23.06 mIoU | 仍是有监督训练；跨场景统一不等于开放世界；室内/室外评测集有限；高斯/深度先验误差传导；未覆盖动态物体/关节物体 |
| VEOcc | [2605.25059](https://arxiv.org/abs/2605.25059v4) · [项目页](https://wryzju.github.io/VEOcc/) · 正文选读 | 首个体素中心在线具身语义占据：稀疏全局语义体素图 + Cross-Temporal Logit Aggregation + Reliability-Aware Confidence Modulation + Confidence-Driven State Update；Occ-ScanNet 64.55 IoU/55.49 mIoU（GPOcc-DPT +7.59/+3.61）；车载 1 Hz、783.75 ms/帧、177.5M 参数、118.348 MiB 地图 | 单目 RGB 但相机位姿来自 LiDAR-惯性里程计，不是纯视觉；室内静态/准静态；1 Hz 不是实时；体素分辨率/内存随场景扩展；语义类别固定 |
| OccTrack360 | [2603.08521](https://arxiv.org/abs/2603.08521v3) · [官方代码](https://github.com/YouthZest-Lin/OccTrack360) · 正文选读 | 首个环视鱼眼 4D 全景占据跟踪基准：174–2234 帧序列、全向遮挡掩码、MEI 鱼眼 FoV 掩码、实例级体素 ID；FoSOcc 基线用 Center Focusing Module + Fisheye Enhanced Lifting；Occ3D-Waymo 上交通标志 SQ +11.1%、一般物体 +20.7%、骑行者 AQ +26.1% | 鱼眼环视 `V2`、驾驶域；真值依赖多传感器/重建；实例级体素跟踪的 ID 在长遮挡后仍会漂；基准不是方法，FoSOcc 只是强基线；未覆盖室内/非刚性 |
| FALCON | [2610.22143](https://arxiv.org/abs/2610.22143v2) · [官方代码](https://github.com/Que121/falcon-kr260-release) · 摘要/正文表 | 相机占据的 FPGA 确定性延迟前端：KR260 上 4.3 W 空闲/6.6 W 推理，PL 计算周期级可界、100k 帧包络、watchdog 在超时时发布 stale 输出；300k 代理帧全部在 100 ms + ≤10.2 ms 内交付 | 100 ms 代理是六个 ResNet-50 DPU 推理，不是完整占据网络；完整六相机 FlashOcc 约 1.3 s/帧，尚不是 10 Hz；精度/语义能力有限；确定性延迟不等于任务安全 |
| LEXI-SG | [2605.13741](https://arxiv.org/abs/2605.13741v1) · [项目页](https://ori-drs.github.io/lexisg-web/) · 正文选读 | 首个纯单目 RGB 开放词汇 3D 场景图：用开放词汇基础模型分房间，房间完整后做前馈重建，房间因子图全局对齐 + 回环；AOD/HM3D 平均 ATE 0.305/0.474 m；开放词汇分割与 HOV-SG 竞争；无 GT 位姿/深度 | 单目前馈重建仍有尺度/漂移；开放平面房间分割弱；带物体分割时仅 1.56 FPS（AOD 序列，物体分割占 87.9%）；依赖 DINO/开放词汇模型 `L2`；场景图关系有限 |
| LOST-3DSG | [2601.02905](https://arxiv.org/abs/2601.02905v2) · [项目页](https://lab-rococo-sapienza.github.io/lost-3dsg/) · 正文选读 | 轻量动态开放词汇 3DSG：VLM 生成属性描述，word2vec/句嵌入做实体匹配，避免存储稠密 CLIP；RGB-D + OWLv2 + EfficientViT-SAM 建图；21 物体场景仅 3,297 B 语义状态；更新 0.944/删除 0.778；真实 TIAGo 机器人 | 依赖 GPT-5-mini VLM 与开放词汇检测/分割 `L2`；描述变异会导致身份碎片化；无时序聚合，噪声敏感；语义与空间证据冲突时可能临时重复；真实实验规模小 |
| OP3DSG | [2606.29786](https://arxiv.org/abs/2606.29786v2) · [项目页](https://k2room.github.io/OP3DSG) · 摘要/正文表 | 开放词汇部件级 3DSG：对象-部件知识引导检测 + 部件感知 3D 融合 + 几何初始化先验图 + LLM 关系精修；统一对象、部件、空间/功能关系与可供性；UniGraph3D 上部件节点 R@3 比最强基线 +31.2 点，可供性 76.7 R@3 / 83.2 R@5 | 依赖 3D 重建/位姿与 LLM；部件几何定位仍弱；关系/可供性由语言先验推断；室内为主；不是纯视觉；部件本体与真实接触未验证 |
| DSG | [2609.00619](https://arxiv.org/abs/2609.00619v1) · 摘要/正文表 | 动态室内 3DSG：语义 3D Gaussian + 双视角渲染变化检测 + 多粒度视觉上下文 LLM 关系推理；Dyn-THOR、3RScan、真实场景；粗关系匹配约 43% vs DynamicGSG 22%、ConceptGraphs 8% | RGB-D + 开放词汇感知 + LLM；变化检测依赖渲染质量与视角；关系匹配仍低；真实场景规模有限；动态物体长期身份未闭合 |
| PanoGraphGS | [2610.27696](https://arxiv.org/abs/2610.27696v1) · 摘要/正文表 | 全景 3DGS 与层级 3DSG 统一：共享高斯几何上的语义/实例特征，原型语义 + 关联实例学习，Gaussian 级全景解码；ScanNet++ mIoU 41.06、Replica 76.73、NaviGS 83.19；场景图对象节点准确率平均超最强基线 50+ 点 | 需要多视图 posed 图像/3DGS 训练；实例 ID 跨视角一致性仍是难点；场景图关系有限；不是单目在线；渲染质量不等于物理/功能理解 |

> 3D 检测框与场景图的早期 2026 证据见本节上表；点级/物体级跟踪见[任意点追踪](#point-tracking-2026)与[物体级 6-DoF](#object-pose-tracking-2026)。

#### OccAny：零样本无标定占据，但“无标定”仍不是“无先验”

- **一手来源：** [固定版本](https://arxiv.org/abs/2603.23502v2) · [项目页](https://valeoai.github.io/OccAny) · [官方代码](https://github.com/valeoai/OccAny)。`PRIMARY_PAPER` / `OFFICIAL_PROJECT` / `OPEN_SOURCE`。
- **机制：** 以视觉几何基础模型为骨干，输出点图/深度并提升为体素；Segmentation Forcing 用 SAM2 特征约束体素语义，使几何与分割互相正则；Novel-View Rendering 在测试时合成新视角，补全遮挡/稀疏区域。支持序列、单目、环视三种输入。
- **输入与学习来源：** 无标定 RGB 图像（`V0`）；训练用五个城市数据集的 3D/语义监督（`L1`），SAM2/深度基础模型是上游 `L2`；评测完全零样本，不微调 SemanticKITTI/Occ3D-NuScenes。
- **实际证据：** 序列设置 SemanticKITTI IoU 25.91（CUT3R* 15.93）、Occ3D-NuScenes 23.55；单目 24.03、环视 34.15；作者报告与在域自监督 SOTA 竞争。Segmentation Forcing 与 Novel-View Rendering 各自带来密度/精度增益。
- **不能推出：** 只在城市驾驶域验证，室内/机器人未测；训练仍要五个带 3D/语义标注的数据集；“无标定”仍依赖深度基础模型的尺度先验；开放词汇分割特征不是完整语义本体；IoU 25.91 不是可操作地图精度；不能推出动态物体/遮挡后状态。
- **阅读深度：** 正文选读：方法 §3、序列/单目/环视表 1–3、消融、结论；未复核全部附录；未运行复现。

#### VEOcc：体素在线建图能跑在机器人上，但位姿不是纯视觉

- **一手来源：** [固定版本](https://arxiv.org/abs/2605.25059v4) · [项目页](https://wryzju.github.io/VEOcc/)。`PRIMARY_PAPER` / `OFFICIAL_PROJECT`。
- **机制：** 单目图像先预测局部占据，再把局部体素增量写入稀疏全局语义体素图；TLA 融合相邻帧 logit，RCM 校准空间不确定性，CSU 做置信驱动状态更新；地图无预设边界，可按需转 dense grid。
- **输入与学习来源：** 单目 RGB 做占据预测（`V0`），但相机位姿来自 LiDAR-惯性里程计（`L4` 辅助）；训练用 ScanNet 系 3D 语义标注（`L1`）；在移动机器人上 onboard 运行。
- **实际证据：** Occ-ScanNet 64.55 IoU/55.49 mIoU，优于 GPOcc-DPT +7.59/+3.61、TGSFormer +0.13/+0.76；177.5M 参数；1 Hz 端到端 783.75 ms/帧；191.7 m 轨迹建出 42.00×38.24×2.08 m、861,782 体素、118.348 MiB 的全局地图；自采手持序列零样本迁移。
- **不能推出：** 不是纯视觉：位姿来自 LiDAR-惯性，RGB 只做占据；1 Hz 不是实时控制；室内静态/准静态，动态物体与长期变化未测；语义类别固定；体素分辨率/内存随场景增长；零样本只到自采环境，不是跨域基准。
- **阅读深度：** 正文选读：方法 §III、Occ-ScanNet/EmbodiedOcc-ScanNet 表 I–II、真实部署 §IV-D、运行时表 III；未复核全部附录；未运行复现。

#### OccTrack360：4D 全景占据跟踪的第一个鱼眼长序列基准

- **一手来源：** [固定版本](https://arxiv.org/abs/2603.08521v3) · [官方代码](https://github.com/YouthZest-Lin/OccTrack360)。`PRIMARY_PAPER` / `OPEN_SOURCE`。
- **机制：** 基准提供 174–2234 帧环视鱼眼序列、全向遮挡掩码、MEI 鱼眼 FoV 掩码、实例级体素 ID；FoSOcc 基线用 Center Focusing Module 增强实例定位，用 Fisheye-based Enhanced Lifting 把 LSS 提升扩展到 MEI 鱼眼模型，直接处理原始鱼眼而非先矫正为透视。
- **输入与学习来源：** 环视鱼眼 RGB（`V2` 多相机）+ 3D 语义/实例标注（`L1`）；FoSOcc 训练用 Occ3D-Waymo 与 OccTrack360；真值由多传感器/重建管线生成（`L4`）。
- **实际证据：** Occ3D-Waymo 上 CFM 带来交通标志 SQ +11.1%、一般物体 +20.7%、骑行者 AQ +26.1%；OccTrack360 上 FoSOcc 在 OccSTQ/OccAQ/OccSQ 全面优于 TrackOcc（Fisheyes-only 与 All-input 两种配置）；序列长度显著超过此前基准。
- **不能推出：** 驾驶域、鱼眼环视 `V2`，不是单目 V0；实例 ID 在长遮挡后仍可能漂；基准真值依赖重建/多传感器；FoSOcc 只是强基线，不是已解决；未覆盖室内/非刚性/关节物体；SQ/AQ 提升不等于物理状态理解。
- **阅读深度：** 正文选读：基准 §III、FoSOcc §IV、Occ3D-Waymo/OccTrack360 表 I–II、消融 §V-E；未复核全部附录；未运行评测。

#### LEXI-SG：纯单目 RGB 的开放词汇场景图，代价是 1.56 FPS

- **一手来源：** [固定版本](https://arxiv.org/abs/2605.13741v1) · [项目页](https://ori-drs.github.io/lexisg-web/)。`PRIMARY_PAPER` / `OFFICIAL_PROJECT`。
- **机制：** 用 DINO/开放词汇基础模型识别门/走廊等 transition cue，把场景分成房间；每个房间完整观测后一次性做前馈重建，避免滑动窗口的尺度漂移；房间因子图做全局对齐与回环，房间层级天然对应场景图层级；房间内做开放词汇物体分割/跟踪。
- **输入与学习来源：** 纯单目 RGB（`V0`），无 GT 位姿/深度；前馈重建模型（MASt3R 类）与 DINO/开放词汇分割是上游 `L2`；评测 Habitat-Matterport 3D（HM3D）与自采办公室序列。
- **实际证据：** AOD/HM3D 平均 ATE 0.305/0.474 m；开放词汇分割在 Replica/ScanNet++ 与 HOV-SG 竞争、HM3D 同义词分数最好；运行时 12.92 FPS 不含物体分割、1.56 FPS 含物体分割（AOD 4248 帧序列，物体分割占 87.9%）。
- **不能推出：** 单目前馈重建仍有尺度/漂移；开放平面房间分割弱；1.56 FPS 不是实时；依赖 DINO/开放词汇模型与房间结构先验；场景图关系有限；不是无监督，训练上游仍有 3D/语义数据。
- **阅读深度：** 正文选读：方法 §III、相机位姿/重建/房间/分割 §IV-B–E、运行时表 VIII、消融表 VI–VII；未复核全部附录；未运行复现。

#### LOST-3DSG：3 KB 语义状态跟踪动态物体，但依赖 VLM 描述

- **一手来源：** [固定版本](https://arxiv.org/abs/2601.02905v2) · [项目页](https://lab-rococo-sapienza.github.io/lost-3dsg/)。`PRIMARY_PAPER` / `OFFICIAL_PROJECT`。
- **机制：** 用 GPT-5-mini 从 RGB 生成物体标签与细粒度属性描述；OWLv2 做开放词汇检测、EfficientViT-SAM 做掩码、深度反投影到 3D；实体匹配用 word2vec/句嵌入的属性相似度，而不是存储稠密 CLIP 特征；场景更新模块根据描述/语义/颜色/材料相似度决定保留、更新、删除或新建节点。
- **输入与学习来源：** RGB-D（`V1`）+ VLM/开放词汇检测/分割（`L2`）；真实 TIAGo 机器人；无大规模 3D 场景图训练，靠预训练基础模型与手工相似度函数。
- **实际证据：** 21 物体场景的语义状态仅 3,297 B（约 3.2 KB），远小于稠密 CLIP 体素；在 Dyn-THOR/3RScan/真实场景的 SUM 基准上更新 0.944、删除 0.778；真实机器人上能跟踪被移动的物体并删除已消失实例。
- **不能推出：** 依赖 GPT-5-mini 与开放词汇检测/分割，API/模型版本会漂移；VLM 描述变异会造成身份碎片化；无时序聚合，对噪声敏感；语义与空间冲突时可能临时重复；真实实验规模小；不是纯视觉、不是大规模基准。
- **阅读深度：** 正文选读：方法 §3、SUM 表 1–2、真实机器人 §5、讨论 §6；未复核全部附录；未运行复现。

**2026 补充结论：** 占据与场景图把“三维框”推进到“自由/占据空间、实例、关系、部件、可供性与变化”，但四条边界比分数更重要：

1. **占据 ≠ 实例 ≠ 关系。** OccAny 的 IoU 25.91 说明零样本几何仍粗糙；OccAnyScene 的 59.92/23.06 mIoU 是跨室内外单模型，但不提供实例 ID；VEOcc 有在线体素地图但没有纯视觉位姿；OccTrack360 有实例级体素 ID，但只在鱼眼驾驶域。四类输出不能互相替代。
2. **在线 ≠ 实时 ≠ 纯视觉。** VEOcc 1 Hz 且位姿来自 LiDAR-惯性；FALCON 的 100 ms 保证只覆盖代理网络，完整六相机 FlashOcc 约 1.3 s/帧；LEXI-SG 含物体分割仅 1.56 FPS。任何“在线 3D 理解”都要分感知/建图/关系/查询四段计时，并说明位姿/深度来源。
3. **开放词汇 ≠ 开放世界。** OccAnyScene 仍是闭集语义税则；OP3DSG/LEXI-SG/LOST-3DSG 的开放词汇来自 CLIP/DINO/VLM/LLM，语言先验会替代视觉证据；LOST-3DSG 的 3 KB 状态是属性级压缩，不是完整对象身份。
4. **动态场景图的核心是“变化”，不是“建图”。** DSG 的粗关系匹配仅 43%，说明“物体移动后关系是否仍成立”仍是弱项；LOST-3DSG 的删除/更新靠语义相似度，可能把相似物体混淆。Clover 若把场景图作为世界状态，必须把**节点身份、关系真值、变化检测、删除/重现、在线更新成本**分开验收，不能用 mIoU 或节点 recall 的单点分数替代。

### 追踪方法的同协议对照：任务、初始化、记忆与失败

下表把点、框、掩码、全景、3D/4D 与失败恢复方法放在一起，目的不是排名，而是暴露**指标不可比**：AJ、AUC、HOTA、IDF1、J&F 分别测不同对象层次。任何“追踪 SOTA”必须连同任务定义、初始化、记忆和时延一起读。

| 方法 | 任务与初始化 | 状态/记忆 | 关键证据 | 时延/条件 | 主要失败 |
|---|---|---|---|---|---|
| TAPNext | 任意点；查询点 + 视频 | 循环状态；因果在线、无时间窗 | 在线/离线点追踪 SOTA；低时延 | 未给统一硬件；长序列 >150 帧退化（正文） | 长时漂移；无对象语义；查询点依赖 |
| TAPNext++ | 任意点；查询点 + 视频 | 循环状态；1024 帧训练、重现监督 | 新增 AJ_RD；长序列与重现改善 | 在线；未给统一硬件 | 极端长序列；遮挡期位置仍是推断 |
| CoTracker3 | 任意点；查询 + 视频 | 相关特征迭代；在线/离线变体 | 点轨迹/可见性；合成+教师伪标签 | 在线滑窗 vs 离线不同 | 未来帧/窗口等待；点轨迹≠对象身份 |
| ARROW | 3D 点；任意图像集 | 前馈统一重建+3D 追踪；order-invariant query | WorldTrack/TAPVid-3D SOTA；RGB-only MVTracker 优于专用多视图 | 未给统一硬件；训练需多视图/深度/位姿 | 几何瓶颈；动态/非刚性；语义身份 |
| TAPVid-MV | 3D 点多视图基准 | 不适用（基准） | 238 序列/1,004 流/74,147 轨迹；30+ 基线无一接近 | 校准多相机；真值用深度/LiDAR/SLAM/网格 | 几何恢复是主要瓶颈；真值辅助模态不可部署 |
| SAMURAI | 单目标 VOT；首帧框 | Kalman + motion-aware memory；不改 SAM2 权重 | LaSOT_ext +7.1 AUC；GOT-10k +3.5 AO | “real-time”未统一；依赖 SAM2 规模 | 遮挡期预测；线性运动先验；单目标 |
| GOT-Edit | 通用单目标；首帧框 | VGGT 几何 + 在线模型编辑；语义保持 | 多个 GOT 基准一致提升；只用 RGB | 在线编辑成本；未给统一硬件 | 几何是推断；短时 GOT；开放世界语义 |
| SAM-H / WOFTSAM | 平面目标；首帧平面 | 分割轮廓单应 + 对应重检测；training-free | PlanarTrack p@5 +18.4pp（SAM-H）；WOFTSAM SOTA | 2.4 FPS，RTX A5000，4.5GB；分割 42ms/帧 | 平面假设；光流成本；非平面/非刚性 |
| SAM3RL | 单目标 VOT；首帧提示 | RL 选择记忆帧；SAM3 冻结 | 11/12 提升、10 个第一；SAM2RL 9 个第一 | 5 FPS 决策率；30 FPS 全帧增益 2.9→1.8 | 只控 7 帧记忆；9 个 object pointer 固定；非语义记忆 |
| ByteTrack | 多目标框；检测器 | 无长期记忆；两阶段关联 | MOT 基线；低置信检测恢复遮挡 | 关联 FPS 不等于完整管线 | 检测漏失/相机运动；身份切换；无外观长期记忆 |
| MOTIP2 | 多目标框；检测器 + ID 预测 | 对象级特征 + 空间先验；无后处理关联 | DanceTrack 73.4 HOTA；SportsMOT 76.0；PersonPath22 71.1 IDF1 | DEIM 检测器；MOTIP2-S 3× 原 MOTIP | 同位置同时离开/进入；场景几何依赖；物理身份未证 |
| UGO | 通用多目标；首帧 exemplar | exemplar 检测 + 实例传播 + 分层记忆 | GMOT/video counting SOTA；AnimalTrack 比 SAM3 HOTA +14% | 依赖 exemplar/GECO2 检测器 | FP 较高、MOTA 比 QDTrack 低约 3%；语义粒度不可控 |
| OmniTrack++ | 全景多目标；检测器 | DynamicSSM + FlexiTrack + MoE 记忆 + 模式切换 | JRDB +3.94 HOTA；QuadTrack +15.03 | 360° 全景/机器人；未给统一硬件 | 全景畸变；长期身份；标定/平台 |
| Cutie | 半监督 VOS；首帧掩码 | 对象级记忆读取；object query | MOSE +8.7 J&F vs XMem；比 DeAOT 快 3× | 半监督；目标数/内存随对象增长 | 长期遮挡记忆污染；非物理身份 |
| When Trackers Fail | VOS/VOT；传播器 + 首帧提示 | VLM 验证 + 纠正 agent + 选择性提交 | LVOS-v2 +1.2 J&F；SecVOS +2.7；跨传播器迁移 | 单 GPU 非实时；最坏干预延迟 | 错误纠正伤害正确轨迹；无形式安全；内窥等域未验 |
| SAM 3 | 概念分割/视频；文本/exemplar/点框 | 检测器 + SAM2 式 masklet 记忆 | PCS 精度约 2×；SA-Co | 30 FPS 需 2–8×H200（10–64 目标） | 目标数线性成本；细粒度 OOD；无共享对象上下文 |
| Uni4R | 4D 点追踪/重建；视频 | 连续速度场（OT+ODE）；任意时间戳 | NeurIPS 2026；连续时间重建/追踪 | 训练需 4D/速度/对应；未给统一硬件 | 遮挡/拓扑变化；物理因果未证 |

**对照结论：**
1. **任务层次不同：** 点轨迹（TAP/AJ）、框身份（AUC/HOTA/IDF1）、掩码身份（J&F）、物理实体身份不是同一对象；跨列比较会制造假 SOTA。
2. **初始化不同：** 点查询、首帧框、首帧掩码、文本/exemplar 概念提示给出的信息量不同；零样本/半监督/全监督不能混排。
3. **记忆不同：** 固定窗口、运动感知记忆、RL 记忆、对象级记忆、MoE 记忆、连续速度场分别保留不同证据；记忆字节/目标数必须配平。
4. **时延口径不同：** 检测器 FPS、关联 FPS、完整管线、最坏干预延迟不是同一指标；SAM 3 的 30 FPS 需要多 GPU，SAM-H 仅 2.4 FPS，When Trackers Fail 单 GPU 非实时。
5. **失败模式不同：** 长时漂移、重入、同位置进出、外观相似、平面假设、遮挡期身份、错误纠正二次伤害必须分项报告。

**对 Clover 的验收含义：** 追踪目标不能用单一 HOTA/J&F/AJ 证明；至少同时报告当前帧定位、跨帧关联、遮挡期状态、重现后身份、最坏延迟与记忆字节。否则“追踪更强”无法与“记忆更大/提示更多/硬件更快”区分。

**本节边界：** 上述工作补齐了识别、检测、分割、追踪、动作、指代、阅读、姿态、计数与几何的一手参照，并用二十类能力矩阵标出强/部分/薄的覆盖判断；但没有任何一个证明“一个纯视觉模型已经广义理解真实世界”。共同缺口仍是：跨任务共享身份、遮挡后状态恢复、未知概念发现、物理/因果识别、以及速度-证据保留的联合验收。下一节的能力地图与[评测方向](evaluation-and-benchmarks.md#broad-visual-evaluation)负责把这些缺口变成可区分实验。
<!-- END core-vision-frontier -->

<!-- BEGIN broad-visual-capabilities -->
<a id="broad-visual-capabilities"></a>

## 广义视觉理解：必须覆盖的基础能力

Clover 的目标是纯视觉 AGI、原生 ultrafast 模型。识别、检测、分割、追踪与视觉阅读是核心能力，与世界模型、记忆、因果和行动理解共同接受研究。机器人是长期应用，不能把广义视觉理解缩成操作任务或未来视频生成。以下是能力覆盖要求，不是一个专家管线或已经实现的功能清单。

| 能力维度 | 应保留的输入→输出/行为 | 当前比较入口 | 必须区分的失败或假设 |
|---|---|---|---|
| 图像/场景/类别识别 | 图像→类别、场景、属性；细粒度与长尾类别 | DINOv3、SigLIP 2、监督视觉骨干 | 类别正确但物体位置/属性错误；背景、文字和数据集捷径 |
| 实例识别、匹配与视觉检索 | 新视角/不同时间→同一实例或未知 | 静态特征与时序/实例表示 | 同类别不同物体、同物体外观变化；相似性不直接充当身份真值 |
| 检测与定位 | 图像→框/点、类别、置信度、缺席判断 | YOLO26、RT-DETRv4、Grounding DINO、WeVisOne-VL | 小物体、密集长尾、未知类别；拒答与漏检；提示依赖 |
| 语义/实例/全景分割 | 图像→像素类别、实例与背景区域 | Mask2Former、OneFormer、SAM 3/3.1 | 同架构分开训练与单权重多任务；点/框真值提示的额外信息 |
| 边界、抠图与透明度 | 图像与目标→连续 alpha/细边界 | WeVisOne-VL、专用抠图器 | 二值掩码与 alpha；毛发/透明/反光；目标指定成本 |
| 计数与视觉测量 | 多实例→个数、空间范围或测量分布 | 结构化定位/计数模型、几何方法 | 数量先验、重复计数、遮挡；公制尺寸的尺度/相机假设 |
| 文字、文档、图表与图解阅读 | 场景/页面→转写、布局、表格/公式结构、图文关系 | PP-OCRv6、PaddleOCR-VL-1.6、Florence-2、WeVisOne-VL | 看清字与推断语义分开；训练转写 L1 与语言世界知识 L2；小字和错序 |
| 关键点与姿态 | 人、手、物体→关键点、关节关系或姿态分布 | 多任务视觉头、几何/人体姿态方法 | 2D/3D、可见/遮挡、骨架/形状先验；姿态不等于意图 |
| 光流、匹配与运动分解 | 相邻/跨时图像→对应与可见性 | RAFT、局部特征/匹配、点追踪 | 孔径、纹理、遮挡、相机/物体运动；对应不是类别/因果 |
| 任意点追踪 | 查询点+视频→逐时轨迹及可见性 | CoTracker3、TAPNext、TAPNext++ | 在线/离线、未来帧、初始化；重现关联与不可见期间位置 |
| 单/多目标追踪与再识别 | 流式观测→实例轨迹、身份与终止/重现状态 | ByteTrack、ARC-SORT、SAM 3/3.1、检测–关联基线 | 点、框、掩码、物理实体的身份层次；交叉、离场和重入 |
| 动作、事件与时间理解 | 视频→事件、时间边界、先后/持续、交互与预测 | 视频表示、动作/事件模型、时序评测 | 单帧/语言捷径；过去已发生与未来猜测；未知动作 |
| 深度、相机、三维与动态重建 | 图像序列→几何、相机、运动、三维/四维结构 | DUSt3R/VGGT、CUT3R、动态重建、经典几何 | 度量尺度、监督/位姿来源、动态场景、成像歧义 |
| 部件、关系、功能与可供性 | 实体/部件→支撑、包含、连接、可操作关系 | 关系/场景图、PhyWM、可供性研究 | 物理接触与投影重合；已知关系与推断功能；权限不可由外观直接读出 |
| 持续存在、记忆与修正 | 跨遮挡/跨任务历史→持续信念、反证后修正 | HALO、持续几何状态、外部证据保留 | 追踪可见性、离线身份、开放未来任务与历史证据恢复分别检验 |
| 物理、因果与反事实 | 视觉历史/动作→条件预测、机制/等价类、反事实与未知 | 系统辨识、因果表示、物理模型与主动实验 | 归一化参数与真实各参数；观测预测、虚拟生成与真实干预 |
| 组合、抽象与视觉推理 | 未见对象/关系/规则组合→可核查判断与迁移 | 统一视觉接口、组合/关系/规则评测 | 记住题型或文字模板与新组合迁移；单轮准确率与持续推理 |
| 开放世界、学习与可靠性 | 新分布/新概念/坏输入→学习、校准、拒答与适应 | OOD、持续学习、风险覆盖与退化输入研究 | 无知、未观测、已反驳、模型失配不能压成同一低置信度 |
| 主动观察及行动用途 | 选择新视角/动作→新证据、有效决策与恢复 | 主动视觉、信念规划、视觉控制 | 采证成本、不可逆扰动；具身能力不能替代其他视觉功能验收 |

上述比较入口的源论文与边界见[本方向证据](#broad-vision-primary-evidence)、[跨方向来源表](sources-and-resources.md#broad-vision-sources)及既有几何/物性章节。没有“因为某功能常见就可以省略调研”的例外；也没有将必备能力逐一拆成独立模型的决定。

### 当前实时视觉 artifact 的边界

- **YOLO26：** [官方文档](https://docs.ultralytics.com/models/yolo26/)与[论文 v1](https://arxiv.org/abs/2606.03748v1)支持把它列为当前实时视觉比较家族；[软件 release 8.4.189](https://github.com/ultralytics/ultralytics/releases/tag/v8.4.189)在 2026-10-25 已发布。检测、分类、分割、姿态等不同 head/checkpoint 不能默认为同一个权重同时输出全部功能。tracking 模式另含关联器；其开销/知识须单列后再计入总成本。官方 [YOLO27 预览](https://docs.ultralytics.com/models/yolo27/)仍标为未发布，不能用宣传位或预览表当可下载权重。
- **OCR：** [官方代码说明](https://github.com/PaddlePaddle/PaddleOCR)截至核验日包含 PP-OCRv6、PaddleOCR-VL-1.6 与 HPD-Parsing。专用识别器、语言视觉解析器和高吞吐解码器应分开登记。单页低延迟、token/s、批吞吐与完整页面结构恢复耗时不同；本仓库尚未执行这些模型。
- **SAM 3/3.1：** [官方项目代码](https://github.com/facebookresearch/sam3)是概念/提示分割与视频实体研究入口。已有的 SAM 3.1 跟踪比较继续保留；点/框/文本提示、对象数、记忆窗口与精确 checkpoint 须一起记录，不能把其功能直接归入 Clover。

阅读深度：以上 artifact 为官方说明/发布信息核对，没有加载权重、验证模型转换、重跑基准或实测本机速度。论文选读与书目版本单独登记。
<!-- END broad-visual-capabilities -->

## Contents

- [Core Visual Capability Frontier: Recognition, Detection, Segmentation, Tracking, Action, Referring, Reading](#core-vision-frontier)
- [Point Tracking and 3D Motion: From Pixel Tracks to World-Space SE(3)](#point-tracking-2026)
- [Object-Level 6-DoF State: Pose Tracking, Occlusion Recovery and Articulated Objects](#object-pose-tracking-2026)
- [Strict Hidden-State Evidence: Mass, Material, Permanence](#strict-hidden-state-2026)
- [Unified Model Comparison: Shared Weights, Interfaces, Training](#unified-model-comparison)
- [Instance Retrieval and Re-ID: Identity Across Time, Cameras and Appearance](#retrieval-reid-2026)
- [3D Detection and Scene Graphs: From Boxes to Entities and Relations](#3d-detection-sg)
- [Action and Event Understanding: Classification, Localization, Anticipation, Open Vocabulary](#action-event-2026)
- [Spatial State: Online SLAM, Odometry and Mapping](#spatial-state-2026)
- [Human-Object Interaction, Attention and Social Scenes](#hoi-social-2026)
- [Face, Expression and Gesture: Identity, Affect and Communication](#face-affect-gesture-2026)
- [Human, Hand and Whole-Body 3D Pose](#pose-wholebody-2026)
- [Open-World Parts, Affordance and Functional Scenes](#affordance-parts-2026)
- [Correspondence, Optical Flow and Matching](#correspondence-flow-2026)
- [Occlusion, Amodal Completion and Incomplete Evidence](#amodal-occlusion-2026)
- [Boundaries, Matting and Transparent/Camouflaged Objects](#matting-transparency-2026)
- [Event Vision and Asynchronous Perception](#event-async-2026)
- [Compositional Generalization, Abstract Reasoning and Evidence Binding](#composition-reasoning-2026)
- [Counting and Visual Measurement](#counting-measurement-2026)
- [Recognition Comparison: Classification, Open-Vocabulary, Detection, Segmentation, Reading](#recognition-comparison)
- [Tracking Comparison: Tasks, Initialization, Memory, Failure](#tracking-comparison)
- [World-State Variables & Observability Map](#topic-research-research_state_variables)
- [Identifiability, Observability and Information Limits](#topic-research-research_identifiability)
- [Observation Physics and Image-Formation Limits](#topic-research-research_observation_physics)
- [Hidden Physical Properties, Contact and Irreversible Change](#topic-research-research_physical_properties)
- [R-A — Observability, Epistemology and Belief State](#topic-research-dossiers-r-a-observability-epistemology)
- [R-B — Geometry: What Is Already Solved?](#topic-research-dossiers-r-b-geometry)
- [R-E — Physical Understanding: Plausibility, Quantification and Relational Structure](#topic-research-dossiers-r-e-physics)
- [Classical Computer Vision and Geometry](#topic-docs-research-map-classical-vision)
- [Spatial Intelligence](#topic-docs-research-map-spatial-intelligence)

<a id="topic-research-research_state_variables"></a>

## World-State Variables & Observability Map

Source record updated: 2026-10-14
Source intake checked through: **2026-10-14**

> **Research question:** How can a machine understand the real world through vision alone?

This file is a Stage-1 research inventory, not a Clover architecture specification.

Its purpose is to make the phrase **“understand the real world”** less vague by asking a more concrete question:

> Which world variables matter, and what evidence is currently known to constrain them?

The map deliberately separates what may be inferred from a static RGB image, passive temporal video, active visual exploration, physical action-response, and non-visual sensing.

It does **not** claim that the labels below are mathematical impossibility theorems. They are a working evidence map grounded in current literature and should be revised as stronger results appear.

---

### 1. Evidence routes

Use the following evidence-route language when discussing a world variable.

```text
P0  single / static RGB evidence
P1  passive temporal RGB/video evidence
P2  active visual evidence: move camera/viewpoint, but sensory evidence remains visual
P3  action-response evidence: act on the world, observe visual consequence
N   non-visual / privileged evidence such as depth sensor, force, tactile, proprioception,
    IMU, simulator state or measured physical parameters
```

These are not new Clover sensor protocols. They are a Stage-1 way of stating **what kind of evidence a paper actually uses**.

Map them back to the canonical V0–V3 / L0–L4 protocol whenever a result is later evaluated.

---

### 2. High-level observability map

Legend:

- `strong` — substantial direct evidence exists;
- `possible-with-priors` — estimable, but strongly prior/model/data dependent;
- `history-important` — temporal evidence materially helps;
- `interaction-important` — controlled action-response materially improves identifiability;
- `non-visual-common` — current strong methods commonly rely on non-RGB state/sensing;
- `open` — no strong general conclusion yet.

| World variable | P0 static RGB | P1 passive video | P2 active view | P3 action-response | N non-visual | Current Stage-1 interpretation |
|---|---|---|---|---|---|---|
| image appearance / texture | strong | strong | strong | not required | not required | directly observed but viewpoint/illumination dependent |
| 2D position / mask | strong | strong | strong | not required | not required | visible support, not hidden existence |
| correspondence / optical flow | weak from one frame | strong | strong | useful | not required | motion evidence, not identity by itself |
| camera pose | possible-with-priors | strong | strong | useful | common for GT/eval | classical/learned geometry already strong |
| depth / metric scale | possible-with-priors | stronger | stronger | useful | depth sensor often used | monocular scale remains prior-dependent |
| 3D shape | possible-with-priors | stronger | strong | useful | RGB-D common | reconstruction does not imply physics/function |
| object identity | possible-with-priors | history-important | stronger | useful | not inherently required | visible tracking is weaker than permanence |
| amodal shape / hidden extent | possible-with-priors | history-important | stronger | useful | GT often privileged | completion may be prior-driven hallucination |
| object permanence | weak from one image | history-important | stronger | useful | omniscient GT useful for eval | must distinguish belief from observation |
| articulation state | possible-with-priors | stronger | stronger | interaction-important | joint GT common | configuration easier than unknown kinematic mechanism |
| kinematic constraints / joints | possible-with-priors | stronger | stronger | interaction-important | GT/sim common | active one-step interaction can reveal mechanism |
| mass | possible-with-priors | possible-with-priors | possible-with-priors | interaction-important | measured mass useful | RGB-only estimation is ill-posed and prior dependent |
| density / material semantics | possible-with-priors | possible-with-priors | possible-with-priors | interaction-important | direct measurement useful | appearance correlates with material but does not uniquely determine density |
| center of mass / inertia | open | possible-with-priors | possible-with-priors | interaction-important | force/state measurements common | especially important for manipulation and stability |
| friction | weak / prior-driven | weak / prior-driven | weak / prior-driven | interaction-important | haptic/force measurements common | current literature explicitly treats vision alone as insufficient in many settings |
| stiffness / compliance | weak / prior-driven | possible-with-priors | possible-with-priors | interaction-important | force/tactile common | deformation under known action is highly informative |
| contact state / topology | sometimes visible | stronger | stronger | interaction-important | force/tactile useful | contact may be visually ambiguous under occlusion |
| deformation state | possible | strong | stronger | interaction-important | depth/state common | cloth/rope/bag require state beyond rigid geometry |
| viscosity / fluid properties | weak / prior-driven | possible-with-priors | possible-with-priors | interaction-important | force/flow measurements common | appearance often insufficient for visually similar liquids |
| support / stability | possible-with-priors | stronger | stronger | useful | not inherently required | physical reasoning benchmark target |
| affordance / function | possible-with-priors | stronger | stronger | interaction-important | demonstrations useful | category/appearance priors can shortcut true function |
| action effect / controllability | not identifiable from one image | possible if natural interventions occur | stronger | strong | robot state often used | system identification is fundamentally action-linked |
| causal relation | weak | possible under assumptions | useful | strong | intervention metadata useful | observational equivalence is a core theoretical limitation |
| uncertainty / unknown state | model-dependent | history-important | stronger | stronger | not inherently required | calibration must be evaluated, not assumed from confidence scores |
| social/intentional state | weak / prior-driven | history-important | active observation useful | interaction-important | language/context often used | physical world includes other agents, not only objects |

The central implication is not that every useful variable must become an explicit coordinate in Clover.

The implication is that **future representations should be judged by whether they preserve the evidence needed to infer, revise, or act on these variables**.

---

### 3. Mass, density and scale

#### 3.1 Single-image mass estimation is explicitly ill-posed

**Physically Guided Visual Mass Estimation from a Single RGB Image**
Primary paper: https://arxiv.org/abs/2601.20303
Evidence: `PRIMARY_PAPER`

The paper explicitly frames visual mass estimation as ill-posed because mass depends on both volume and material-dependent density, neither directly observed from a single RGB image.

Its solution uses learned monocular 3D geometry plus coarse material semantics to constrain plausible volume/density factors.

Stage-1 interpretation:

```text
RGB appearance
+ learned geometry prior
+ material/world prior
→ mass estimate
```

is not equivalent to:

```text
RGB uniquely determines mass
```

This is an important example of the distinction between **useful statistical inference** and **physical identifiability**.

#### 3.2 Real-object mass benchmark

**PhysQuantAgent / VisPhysQuant**
Primary paper: https://arxiv.org/abs/2603.16958
Evidence: `PRIMARY_PAPER`

VisPhysQuant contains multi-view RGB-D video with measured object masses. The method uses visual prompting, scale reasoning and inferred internal cross-sections to improve mass estimation.

Important Clover caveat:

RGB-D is outside strict `V0/V1` RGB-only observation. Use the benchmark as evidence about physical-quantity reasoning, but do not silently report it as a pure RGB result.

Stage-2 question:

> How much of mass estimation performance comes from geometry, material/world priors, metric scale, or memorized object-category statistics?

---

### 4. Friction is a strong example of interaction-limited knowledge

#### 4.1 Visual + haptic friction mapping

**Probabilistic Surface Friction Estimation Based on Visual and Haptic Measurements**
Primary paper: https://arxiv.org/abs/2010.08277
Evidence: `PRIMARY_PAPER`

This work explicitly states that visual observation alone does not convey enough information to estimate surface friction reliably. It combines visual correlation with limited haptic exploration.

This older result remains conceptually important because it gives a concrete case where:

```text
appearance similarity
≠
physical interaction equivalence
```

#### 4.2 Material-pair friction requires interaction structure

**Generalizable Friction Coefficient Estimation via Material Embedding and Proxy Interaction Modeling**
Primary paper: https://arxiv.org/abs/2604.24188
Evidence: `PRIMARY_PAPER`

The method predicts pairwise friction through measured interactions against a small fixed proxy-material set, rather than inferring friction directly from RGB appearance.

Stage-1 implication:

Friction is not merely an intrinsic property of one visible object. It is often a **pairwise interaction property** depending on two materials and contact conditions.

#### 4.3 Behavior-grounded terrain/contact calibration

**DR-WM — From Pixels to Executable Physics**
Primary paper: https://arxiv.org/abs/2610.17630
Submitted: 2026-10-13
Evidence: `PRIMARY_PAPER`

DR-WM reconstructs scene geometry from RGB and calibrates spatial terrain/contact priors using real robot action-response experience before simulating candidate actions.

This creates a particularly useful boundary case:

```text
geometry from vision
+
physical parameter calibration from action-response
```

Stage-2 question:

> Which action-relevant physical parameters can be inferred statistically from appearance, and which require system identification through interaction?

---

### 5. Articulation, function and physically usable object models

#### 5.1 Active interaction can reveal unknown articulated structure

**DexSim2Real²**
Primary paper: https://arxiv.org/abs/2409.08750
Evidence: `PRIMARY_PAPER`

The system constructs an explicit digital twin of unseen articulated objects using the world state before and after an active one-step interaction.

This is valuable Stage-1 evidence that articulation may be partially observable from appearance, but precise manipulation benefits from **interaction that reveals kinematic structure**.

#### 5.2 Physical function goes beyond visual asset quality

**Artisan**
Primary paper: https://arxiv.org/abs/2610.13947
Submitted: 2026-10-09; revised 2026-10-12
Evidence: `PRIMARY_PAPER`

Artisan evaluates articulated asset generation not only by appearance, but also through collision, gravity stability, mass/material attributes and downstream functional use.

Key distinction:

```text
looks like a usable object
≠
has correct articulation
≠
is dynamically stable
≠
functions correctly
```

Stage-1 implication:

Object understanding should eventually include **what motions are physically permitted and what function the object supports**, not only category or geometry.

---

### 6. One state representation may need to span rigid, articulated and deformable objects

#### PointCast

Primary paper: https://arxiv.org/abs/2609.28393
Project: https://pointcast-wm.github.io
Evidence: `PRIMARY_PAPER` / `OFFICIAL_PROJECT`

PointCast represents objects and the robot end-effector as persistent identity-bearing 3D point sets and predicts future point trajectories conditioned on recent history and commanded motion.

The same architecture/training recipe is applied across:

- rigid objects;
- cloth;
- rope;
- multi-joint cabinets.

The checkpoints are trained separately by regime, so this does **not** yet establish one universally shared physical model.

Why it matters for Clover:

It is a strong counterexample to assuming that every material class requires a completely different ontology. A topology-agnostic point-state can span several regimes while retaining explicit correspondence.

Stage-2 question:

> Which properties are genuinely shared across rigid, articulated and deformable dynamics, and which require regime-specific latent structure?

---

### 7. Deformation, cloth, rope and soft systems

#### 7.1 Cloth world models

**Learning to Unfold Cloth: Scaling up World Models to Deformable Object Manipulation**
Primary paper: https://arxiv.org/abs/2602.16675
Evidence: `PRIMARY_PAPER`

The work modifies a Dreamer-style world model for cloth manipulation, including surface-normal input and changes to replay/data augmentation, and evaluates zero-shot physical-robot transfer.

Important protocol note:

Surface normals are stronger geometric evidence than raw monocular RGB and should be annotated accordingly when comparing to strict vision-only systems.

#### 7.2 Contact-centric deformable dynamics

**WorldContact**
Primary paper: https://arxiv.org/abs/2609.19600
Evidence: `PRIMARY_PAPER`

WorldContact makes contact structure central for deformable manipulation and uses model-generated trajectories to expand policy data.

Stage-1 question:

> Does a general world model need an explicit contact representation, or can contact emerge reliably inside a distributed predictive state?

#### 7.3 Soft robot embodiment itself is deformable state

**ManiSoft**
Primary paper: https://arxiv.org/abs/2605.18617
Project/code/data: https://buaa-colalab.github.io/ManiSoft
Evidence: `PRIMARY_PAPER` / `OPEN_SOURCE`

ManiSoft shows that not only manipulated objects but the robot body itself can be deformable. Reported failures include inaccurate visual estimation of the robot's own proprioceptive state and poor exploitation of deformability under randomized scenes.

This expands the mother question:

```text
understanding external world state
+
understanding the body's own changing physical state
```

may both be required for general embodied intelligence.

---

### 8. Liquids and hidden physical properties

#### Vision-Language Model-based Physical Reasoning for Robot Liquid Perception

Primary paper: https://arxiv.org/abs/2404.06904
Evidence: `PRIMARY_PAPER`

The study evaluates common household liquids and reports that vision-only reasoning is substantially weaker than a setup where force/torque responses are converted into visual plots and jointly reasoned over.

The system estimates viscosity by using **interaction-derived non-visual evidence encoded visually**, so it must not be classified as proof that viscosity is recoverable from passive RGB.

Stage-1 implication:

For visually similar liquids, interaction response may be more informative than appearance.

Stage-2 question:

> Which fluid variables can be estimated from passive flow video, and which require known perturbations, metric calibration or force evidence?

---

### 9. Ego-motion and object-motion must be disentangled

#### 4DVGGT-D

Primary paper: https://arxiv.org/abs/2605.12027
Evidence: `PRIMARY_PAPER`

The paper identifies coupling between camera ego-motion and object motion as a core failure source for dynamic 4D reconstruction and proposes a progressive pose/dynamic decoupling pipeline.

Stage-1 implication:

A changing image can result from:

```text
camera moved
object moved
object deformed
lighting changed
scene changed
some combination of the above
```

A world representation that conflates these causes may reconstruct pixels while getting the world transition wrong.

#### DP-DeGauss

Primary paper: https://arxiv.org/abs/2604.07986
Evidence: `PRIMARY_PAPER`

Egocentric 4D reconstruction explicitly decomposes background, hands and manipulated objects, showing that first-person scenes require component-aware motion separation under strong occlusion and camera movement.

---

### 10. Object permanence can be trained explicitly, not only measured

#### WROP — Training Object Permanence in World Models

Primary paper: https://arxiv.org/abs/2609.28654
Evidence: `PRIMARY_PAPER`

WROP introduces 150 cognitive-science-inspired object-permanence/solidity tasks, large randomized training data and a held-out exam for video world models.

Why it matters:

PersistBench asks whether a system **remembers** out-of-view objects in realistic 4D settings. WROP asks whether core-permanence behavior can be **deliberately trained** through controlled synthetic curricula.

These should not be conflated:

```text
training cognitive prior
≠
measuring persistent real-world memory
```

Stage-2 question:

> Does synthetic permanence training create a transferable world-state capability or primarily task-family competence?

---

### 11. Active calibration can define the action/world interface

#### SyncWorld

Primary paper: https://arxiv.org/abs/2609.09155
Evidence: `PRIMARY_PAPER`

SyncWorld studies a subtle but important issue: the same numerical robot action does not have a universal pixel-space meaning across camera views, environments or robot embodiments.

It uses a visual calibration episode — paired actions and observed frames — to specify an environment/embodiment-specific action→visual mapping in context.

Stage-1 implication:

```text
same action vector
≠
same visible world transition
```

unless embodiment, controller, camera and geometry are accounted for.

This is central for cross-embodiment world models.

---

### 12. Robot-factored visual interfaces are another route to cross-embodiment transfer

#### Robot-Factored World Models via Robot Rendering

Primary paper: https://arxiv.org/abs/2607.22535
Evidence: `PRIMARY_PAPER`

The method separates:

1. commanded action;
2. nominal realized robot trajectory through known controller/kinematics;
3. rendered robot geometry;
4. scene response to that geometry.

It argues that direct action conditioning forces the world model to learn robot-specific action realization, while future-state conditioning can leak the answer.

Stage-1 question:

> What is the correct interface between embodiment-specific action and embodiment-general world dynamics?

This source should be compared with SyncWorld, PointWorld, Riemann-style sequence models and direct VLAs.

---

### 13. 3D point-flow world models make a different claim about transferable physical state

#### PointWorld

Primary paper: https://arxiv.org/abs/2601.03782
Project: https://point-world.github.io/
Evidence: `PRIMARY_PAPER` / `OFFICIAL_PROJECT`

PointWorld represents both action and predicted scene change as 3D point flow and reports one pretrained model across rigid pushing, deformable/articulated manipulation and tool use.

Important protocol caveat:

PointWorld takes RGB-D inputs, so it is not a strict `V0/V1` monocular RGB baseline.

Research value:

It is a strong comparator for the hypothesis that **shared 3D geometric action/state coordinates** can improve cross-embodiment world modeling.

---

### 14. Uncertainty must be decision-aware

#### Decision-Aware Uncertainty Evaluation for Early Action Anticipation

Primary paper: https://arxiv.org/abs/2603.10061
Evidence: `PRIMARY_PAPER`

The work evaluates VLM confidence under partial temporal observation for human-robot interaction and studies calibration/selective prediction rather than only recognition accuracy.

Why it matters:

For world understanding, an answer is not enough. The system must also know when current visual evidence is insufficient.

Relevant metrics include:

```text
calibration
selective prediction
coverage
risk under abstention
prefix length / evidence amount
```

Stage-1 implication:

Epistemic correctness should eventually include:

```text
correct when confident
uncertain when evidence is insufficient
willing to seek more evidence
able to revise after new evidence
```

---

### 15. Affordance is a distinct state variable from category and geometry

#### RoboAfford++ / RoboAfford-Eval

Primary paper: https://arxiv.org/abs/2511.12436
Evidence: `PRIMARY_PAPER`

The dataset separates:

- object affordance recognition;
- functional interaction-point prediction;
- spatial affordance / free-space localization.

Stage-1 implication:

Knowing **what an object is** and **where it is** does not fully specify **how it can be used**.

Affordance may depend on geometry, material, articulation, task, embodiment and current world state.

---

### 16. A stronger working decomposition of “world state”

For Stage 1, it is useful to keep at least the following layers distinct.

```text
A. observation state
   pixels, masks, visible features, tracks

B. geometric state
   pose, depth, shape, camera, 3D structure

C. entity state
   identity, existence, articulation, hidden/occluded state

D. physical state
   velocity, acceleration, support, contact, deformation

E. latent physical parameters
   mass, density, inertia, friction, stiffness, viscosity, material properties

F. functional state
   affordance, articulation limits, usable parts, task-relevant constraints

G. causal / controllability state
   what changes what, action-response, intervention sensitivity

H. epistemic state
   observed, inferred, predicted, uncertain, unobserved, contradicted

I. social / intentional state
   other-agent goals, likely actions, interaction history
```

A future Clover representation does not need to expose all of these explicitly.

But Stage 2 and Stage 3 should ask, for each major method family:

> Which of these layers can be decoded or used reliably, under what evidence conditions, and with what failure modes?

---

### 17. Key Stage-1 distinctions strengthened by this map

```text
appearance ≠ material property
shape ≠ mass
material label ≠ friction coefficient
geometry ≠ contact dynamics
visible motion ≠ causal mechanism
commanded action ≠ realized action
static pose ≠ articulation mechanism
object category ≠ affordance
plausible video ≠ executable physics
confidence score ≠ calibrated uncertainty
long context ≠ correct persistent belief
RGB-only deployment ≠ knowledge learned only from vision
```

And most importantly:

```text
statistically predictable from pixels
≠
physically identifiable from pixels
```

This distinction should remain explicit throughout Clover research.

---

### 18. Priority Stage-2 reports implied by this map

When Stage 2 becomes active, prioritize reports that can clarify the evidence boundary:

```text
Physically Guided Visual Mass Estimation
PhysQuantAgent / VisPhysQuant
DR-WM
PointCast
PointWorld
WorldContact
DexSim2Real²
Artisan
SyncWorld
Robot-Factored World Models
WROP
Decision-Aware Uncertainty Evaluation
```

Suggested common questions:

```text
What is observed directly?
What is inferred using learned priors?
What requires temporal history?
What requires controlled action?
What uses privileged/non-visual evidence?
What is actually identifiable?
What is only statistically predictable?
What uncertainty is reported?
How does the representation revise after contradictory evidence?
Does the inferred state improve real action?
```

---

### 19. Open collection gaps

Stage 1 should continue searching for strong primary work on:

- center-of-mass and inertia estimation from visual evidence;
- stiffness/compliance identification from RGB video under known actions;
- passive-video friction inference without haptics;
- real-world fluid dynamics and viscosity from controlled visual interventions;
- granular materials;
- breakage, cutting, tearing and irreversible topology change;
- thermal state and temperature when not visually observable;
- acoustic/visual physical inference while preserving a strict visual-only ablation;
- amodal 3D/4D object state under long occlusion;
- dynamic semantic maps with object replacement/removal;
- visual system identification across unseen robot embodiments;
- uncertainty calibration for long-horizon world state, not only classification;
- causal intervention datasets with real RGB observations;
- negative results showing which physical quantities cannot be recovered robustly from RGB.

A missing result is itself useful Stage-1 information when it marks a plausible identifiability boundary.

---

**Stage-1 rule:** collect the variables and evidence conditions first. Do not decide the Clover ontology yet.

---

<a id="topic-research-research_identifiability"></a>

## Identifiability, Observability and Information Limits

Source record updated: 2026-10-14
Source intake checked through: **2026-10-14**

> **Research question:** How can a machine understand the real world through vision alone?

This is a Stage-1 theory/background document. It does **not** propose a Clover algorithm.

Its purpose is to prevent a recurring category error:

> A model predicting a hidden variable accurately on a dataset does not by itself show that the variable is uniquely determined by the visual evidence.

Stage 1 must distinguish **prediction**, **observability**, **identifiability**, **calibration**, and **action usefulness** before Stage 2 compares mechanisms.

---

### 1. Minimal formal problem

Let the real world have latent physical state

```text
S_t
```

and let a visual observation be generated by

```text
O_t = G(S_t, C_t, L_t, N_t)
```

where, conceptually:

- `C_t` — camera/viewpoint/calibration;
- `L_t` — illumination/appearance conditions;
- `N_t` — noise/unmodeled observation factors.

A passive visual learner receives an observation history

```text
O_1:t
```

and forms some internal representation

```text
Z_t = F(O_1:t).
```

An embodied active learner may also choose actions

```text
A_t
```

that change either the viewpoint or the physical world, producing later observations:

```text
S_{t+1} ~ T(S_t, A_t)
O_{t+1} ~ G(S_{t+1}, C_{t+1}, ...)
```

The research question is therefore not simply:

```text
Can F predict labels from O?
```

It is closer to:

```text
What aspects of S can be inferred from visual evidence?
Under what assumptions?
With what uncertainty?
Which aspects become identifiable only after additional views or interventions?
Which representation preserves enough information for prediction, revision and action?
```

---

### 2. Five concepts that must not be conflated

#### 2.1 Predictability

A variable may be statistically predictable because the training distribution contains strong correlations.

Example:

```text
visual appearance → likely material → likely density → likely mass
```

This can be useful without making mass uniquely observable from the image.

#### 2.2 Observability

In control/state-estimation language, observability asks whether hidden state can be recovered from available outputs over time under a specified model and input sequence.

For Clover the key lesson is conceptual:

```text
state recoverability depends on
observation process
+
dynamics
+
time
+
actions
+
assumptions
```

not on pixels alone in the abstract.

#### 2.3 Identifiability

Identifiability asks whether the underlying variables/model are uniquely recoverable — often only up to an allowed equivalence class — from the available data and assumptions.

Two different world models can generate the same observed evidence.

If so, no learning algorithm can distinguish them **from that evidence alone** without additional assumptions or interventions.

#### 2.4 Calibration / epistemic correctness

A system may be unable to identify the true hidden state but still be scientifically useful if it represents uncertainty correctly.

Correct behavior may be:

```text
I do not know
multiple worlds remain possible
I need another view
I need to interact
```

rather than forcing one state estimate.

#### 2.5 Action sufficiency

A representation need not reconstruct every property of reality to be useful for a robot.

A state can be action-sufficient even if it omits variables irrelevant to the task.

Conversely, a visually rich representation can be action-insufficient if it loses contact, constraint, identity or uncertainty information required for control.

---

### 3. Observational equivalence is central to “vision alone”

Define two candidate world states `S` and `S'` as observationally equivalent under an observation protocol if they generate indistinguishable allowed observations.

Conceptually:

```text
G(S) = G(S')
```

for all evidence available under that protocol.

Then the machine cannot uniquely know whether the true state is `S` or `S'` without:

- stronger priors;
- additional viewpoints;
- longer temporal history;
- controlled interaction;
- or another sensor modality.

Examples include:

- different metric scales producing similar monocular projection;
- visually similar materials with different density/friction;
- closed articulated mechanisms whose joint constraints are hidden;
- identical-looking containers holding liquids with different viscosity;
- hidden objects that may still exist, may have moved, or may have been removed while unobserved.

This motivates maintaining a **belief over plausible worlds** rather than silently converting one plausible completion into fact.

---

### 4. Geometry already contains classical ambiguity results

#### Multiple-view geometry / projective ambiguity

Background source:

- Multiple View Geometry — https://www.robots.ox.ac.uk/~vgg/hzbook/

Classical multi-view vision shows that reconstruction depends on camera geometry, calibration and motion constraints. Projective structure may be recoverable before metric/Euclidean structure.

#### Auto-calibration ambiguity

Primary/background source:

- Resolving Ambiguities in Auto-calibration — https://www.robots.ox.ac.uk/~vgg/publications/1998/Zisserman98/

The paper demonstrates that even common calibration constraints can fail to resolve specific geometric ambiguities under certain camera motions.

Stage-1 implication:

> “More frames” does not automatically mean “all geometry is determined.”

The information content depends on viewpoint diversity and degeneracy.

This is a useful precedent for modern learned world models: scale/model capacity cannot manufacture evidence absent from the observation process.

---

### 5. Passive temporal observation can make hidden state more observable — but not universally

Video adds:

- correspondence;
- velocity/motion;
- repeated views;
- temporal constraints;
- natural interventions caused by other actors;
- evidence about persistence and change.

But passive video still inherits ambiguity when multiple latent mechanisms produce similar visual trajectories.

Examples:

```text
same visible displacement
← different mass + force combinations

same sliding motion
← different friction + applied-force combinations

same deformation
← different stiffness + contact-force combinations
```

Without knowing the applied cause, inverse physical inference can remain underdetermined.

This is why Stage 1 should distinguish:

```text
passive dynamics observation
vs
controlled system identification
```

---

### 6. POMDPs formalize why belief state matters

Primary/background survey:

- Partially Observable Markov Decision Processes in Robotics: A Survey — https://arxiv.org/abs/2209.10342

Related robotics review:

- POMDPs and Robotics — https://arxiv.org/abs/2107.07599

The POMDP framework treats the true world state as only partially observed and maintains a belief distribution over possible states.

Clover is **not** assumed to require a textbook POMDP implementation.

The relevance is the distinction:

```text
true hidden state
≠
current observation
≠
agent belief about state
```

A general visual robotic brain should eventually answer:

- what has been observed directly?
- what is inferred?
- what remains uncertain?
- what evidence would reduce uncertainty?
- how should uncertainty affect action?

---

### 7. Active perception changes the information available without changing the sensor modality

Foundational source:

- Bajcsy, Active Perception — https://ieeexplore.ieee.org/abstract/document/5968

Active perception treats sensing as a controlled process: the agent chooses actions that acquire informative observations.

This is highly relevant to the Clover phrase **vision alone**.

A robot may remain visually sensed while moving the camera/body to obtain a better view:

```text
uncertainty
→ choose viewpoint
→ new RGB evidence
→ update belief
```

This is still fundamentally different from passively receiving a video stream.

Current reference:

- Vantage / Seek-and-View — https://arxiv.org/abs/2610.11810
- Code — https://github.com/q1xiangchen/Vantage

Stage-1 question:

> Which ambiguities can active viewpoint selection resolve without touching the world?

---

### 8. Physical interaction is an intervention, not merely another frame

When an agent pushes, lifts, opens, compresses or otherwise perturbs the world, the resulting observation contains information about how the world responds to a known action.

Conceptually:

```text
known action
+
visual response
→ constraints on hidden dynamics / physical parameters
```

This is system identification through embodied visual interaction.

Examples already tracked in Stage 1:

- DR-WM — https://arxiv.org/abs/2610.17630
- DexSim2Real² — https://arxiv.org/abs/2409.08750
- SyncWorld — https://arxiv.org/abs/2609.09155

The key research distinction is:

```text
active vision: move to see
vs
active intervention: act to make hidden physics reveal itself
```

Both can remain **vision as the sensory evidence** if non-visual state is withheld from the learner, but they have very different identifiability power.

---

### 9. Causal representation learning shows why interventions can make latent variables identifiable

#### Interventional Causal Representation Learning

Primary source:

- https://proceedings.mlr.press/v202/ahuja23a.html

The paper proves identifiability results for latent causal factors under interventional data and explicit assumptions.

#### General Identifiability and Achievability for CRL

Primary source:

- https://proceedings.mlr.press/v238/varici24a.html

The work gives identifiability/achievability guarantees under multiple hard interventions per latent node for general nonlinear transformations under its stated assumptions.

#### Multi-node interventions

Primary source:

- https://proceedings.mlr.press/v236/bing24a.html

This work explicitly starts from the fact that causal representation learning from low-level observations is fundamentally underconstrained and derives identifiability conditions using diverse multi-node intervention environments.

#### Grouped observational variables

Primary source:

- https://proceedings.mlr.press/v235/morioka24a.html

This line shows that interventions are not the only theoretical route: sufficiently strong structural assumptions on grouped observations can also restore identifiability.

Stage-1 implication:

There is no universal statement such as:

```text
causal variables require interaction
```

or

```text
passive observation is always enough
```

The correct question is:

> Under which assumptions and data regimes is a particular latent structure identifiable?

---

### 10. Experiment design and representation identifiability are linked

Primary source:

- An Interventional Perspective on Identifiability in Gaussian LTI Systems with ICA — https://proceedings.mlr.press/v236/rajendran24a.html

This work connects diverse intervention signals with system-parameter identifiability in dynamical systems.

For Clover, the broader lesson is important:

```text
representation learning
and
data acquisition policy
cannot always be studied independently
```

A poor experiment may make a good representation impossible to identify.

A well-chosen intervention may expose structure that passive data hides.

---

### 11. Modern world models are beginning to target identifiable coordinates explicitly

#### Identifiable World Models from Pretrained Diffusion Representations

Primary paper:

- https://arxiv.org/abs/2610.07028

The method keeps a pretrained distributed diffusion representation and learns an alignment layer that can recover identifiable dynamical coordinates under explicit nonlinear-ICA assumptions.

This strengthens a third representation route:

```text
fully hand-designed explicit state
vs
fully opaque distributed latent
vs
powerful latent + identifiable coordinates
```

Stage-1 caution:

Theoretical identifiability depends on assumptions. Success in controlled physical/robotic systems does not prove arbitrary real-world RGB state will be identifiable.

---

### 12. Identifiability should be stated per variable, not for “the world” as one object

A real scene contains heterogeneous variables with different evidence requirements.

For example:

```text
visible color/texture             directly observed
2D mask                           directly observed while visible
3D shape                          inferred from geometry/prior/multiple views
object identity                   temporal association + priors
hidden existence                  belief / memory
mass                              geometry + density prior or interaction
friction                          material/contact interaction
stiffness                         deformation under force/action
articulation mechanism            geometry + motion + often interaction
causal dependency                 temporal structure + assumptions/intervention
intent of another agent           behavioral history + model assumptions
```

Therefore, the phrase:

```text
"the representation identifies the world state"
```

is too coarse unless the paper states **which state variables and under which equivalence class**.

---

### 13. A Stage-1 taxonomy of ambiguity

#### A. Geometric ambiguity

Examples:

- scale;
- depth;
- calibration;
- symmetry;
- occluded shape.

Typical remedies:

- multi-view geometry;
- calibration priors;
- active viewpoint changes;
- learned scene priors.

#### B. Identity ambiguity

Examples:

- similar objects crossing;
- long occlusion;
- object leaves and re-enters FOV;
- object replacement while unobserved.

Typical evidence:

- temporal continuity;
- appearance;
- spatial context;
- persistent memory;
- re-observation.

#### C. Physical-parameter ambiguity

Examples:

- mass;
- density;
- friction;
- stiffness;
- viscosity;
- inertia.

Typical evidence:

- statistical material priors;
- observed natural dynamics;
- known perturbations;
- action-response;
- force/tactile/state measurements.

#### D. Causal ambiguity

Examples:

- correlation vs direct cause;
- hidden common cause;
- multiple mechanisms producing similar outcomes.

Typical remedies:

- structural assumptions;
- environment changes;
- interventions;
- counterfactual constraints.

#### E. Epistemic ambiguity

Examples:

- object unobserved vs absent;
- low confidence because of lack of evidence vs model weakness;
- generated completion vs evidence-supported state.

Required capability:

- calibrated uncertainty;
- provenance;
- abstention;
- active evidence acquisition;
- belief revision.

---

### 14. Implication for Stage-2 method reports

Every serious Stage-2 analysis should include an **identifiability section**:

```text
Target variables:
What does the method claim to represent/predict?

Observation evidence:
Static RGB / passive video / multi-view / active view / action-response / non-visual state?

Assumptions:
Rigid world? Known camera? Known action? Known embodiment? Known material class?

Ambiguities:
Which alternative worlds are still compatible with the same evidence?

Priors:
What is being supplied by pretrained language/vision/world knowledge?

Intervention:
Does the method receive controlled perturbations or only observational data?

Uncertainty:
Does it represent multiple plausible states or force a point estimate?

Identifiability claim:
Is there a theorem, controlled empirical evidence, or only predictive performance?

Action value:
Does distinguishing the latent state improve decisions or execution?
```

This will prevent later Synthesis from comparing methods as if they had equal information budgets.

---

### 15. Implication for evaluation

Future Clover experiments should intentionally construct pairs of worlds that are:

#### observationally indistinguishable under a weaker protocol

but

#### distinguishable under a stronger protocol.

Examples:

```text
same appearance, different mass
→ passive image ambiguous
→ lift/push response discriminates

same object hidden behind occluder
→ current frame ambiguous
→ memory/re-observation discriminates

same visible pose, different articulation constraint
→ image ambiguous
→ controlled push discriminates

same object trajectory, different force/friction explanation
→ passive video underdetermined
→ known applied action discriminates
```

This suggests an eventual hierarchy of **identifiability batteries**, not just recognition benchmarks.

---

### 16. What “vision alone” should mean scientifically

Clover should continue separating two claims:

#### Sensor claim

> The machine's evidence channel at inference is visual.

#### Learning/knowledge claim

> The machine learned the relevant physical/world structure only from visual evidence.

These are not equivalent.

A robot may:

- see RGB only at inference;
- have learned material density from text;
- have learned action dynamics from robot-state demonstrations;
- use camera calibration supplied externally;
- use simulator state during training.

All can improve prediction without proving visual identifiability.

This is why the V0–V3 observation protocol and L0–L4 learning-evidence provenance remain necessary.

---

### 17. Current Stage-1 theoretical position

The evidence does **not** currently support any simple universal statement such as:

```text
all world variables can be learned from passive vision
```

or

```text
an explicit physics engine is necessary
```

or

```text
interaction is always required
```

Instead, the more defensible research position is:

> Real-world visual understanding is a family of inverse problems under partial observability. Different latent variables have different identifiability conditions. Temporal history, viewpoint control, physical interventions and prior knowledge change what can be inferred. A general robotic brain should represent not only a best world estimate, but the uncertainty and evidence conditions under which that estimate is justified.

This is a research constraint, not yet a representation design.

---

### 18. Priority open questions

1. Which physical variables are identifiable from monocular RGB video under realistic motion diversity?
2. Which variables require known actions but no non-visual sensing?
3. Which variables remain poorly identifiable even with visual action-response?
4. Can large pretrained visual/video representations discover intervention-relevant coordinates without explicit supervision?
5. Can a model distinguish uncertainty caused by occlusion from uncertainty caused by model ignorance?
6. How should active perception optimize evidence acquisition for multiple competing world hypotheses?
7. What is the minimal sufficient world state for reliable robot action?
8. When does explicit uncertainty/persistent belief improve behavior over long-context policies?
9. How do language/world priors distort claims of visual physical understanding?
10. Can identifiability assumptions be tested empirically rather than merely assumed?

---

**Stage-1 rule:** before asking which representation is best, ask whether the target variable can be determined from the evidence supplied.

---

<a id="topic-research-research_observation_physics"></a>

## Observation Physics and Image-Formation Limits

Source record updated: 2026-10-14
Source intake checked through: **2026-10-14**

> **Research question:** How can a machine understand the real world through vision alone?

This is a Stage-1 research document. It does **not** propose a Clover architecture.

Its purpose is to study a different source of ambiguity from hidden world state:

> Even when the world state is fixed, the image formation process can hide, mix, distort or erase information before the machine sees the pixels.

The central distinction is:

```text
world-state ambiguity
≠
image-formation ambiguity
≠
sensor / camera corruption
```

A machine cannot recover a physically correct world state merely by becoming a better pattern recognizer if multiple scene configurations can generate the same visual evidence or if the imaging process destroys the relevant information.

---

### 1. Minimal image-formation view

A useful Stage-1 abstraction is:

```text
O_t = Camera(
    Geometry_t,
    Material_t,
    Illumination_t,
    Viewpoint_t,
    Motion_t,
    Medium_t,
    Exposure_t,
    Sensor_t,
    Noise_t
)
```

where the RGB observation `O_t` is the result of multiple coupled physical factors.

The inverse problem is therefore not simply:

```text
pixels → geometry
```

but more generally:

```text
pixels
→ possible combinations of
  geometry + material + lighting + motion + camera/sensor state.
```

Recent inverse-rendering literature explicitly emphasizes that many distinct geometry/material/lighting combinations can explain the same image.

Current survey:

- Recent Trends in Inverse Rendering — https://onlinelibrary.wiley.com/doi/full/10.1111/cgf.70592

Useful ambiguity analysis:

- Unveiling the Ambiguity in Neural Inverse Rendering: A Parameter Compensation Analysis — https://openaccess.thecvf.com/content/CVPR2024W/NRI/html/Kouros_Unveiling_the_Ambiguity_in_Neural_Inverse_Rendering_A_Parameter_Compensation_CVPRW_2024_paper.html
- arXiv version — https://arxiv.org/abs/2404.12819
- Diffusion Posterior Illumination for Ambiguity-aware Inverse Rendering — https://arxiv.org/abs/2310.00362

Stage-1 lesson:

```text
one plausible decomposition
≠
the uniquely correct physical decomposition.
```

---

### 2. Observation-physics map

| Observation phenomenon | What changes in pixels | What may become ambiguous | Stage-1 significance |
|---|---|---|---|
| projective viewpoint | scale, foreshortening, visibility | metric size/depth, hidden geometry | classical multi-view geometry reduces but does not eliminate all ambiguity |
| occlusion | evidence disappears | existence, identity, hidden shape/state | requires memory, uncertainty and/or active view |
| illumination change | intensity/color/shadow | material vs lighting | appearance constancy is not physical-state recovery |
| cast shadow | local darkness | geometry/material/light attribution | shadow can be evidence or nuisance depending on task |
| specular reflection | view-dependent highlight/reflection | surface color, texture, normal/shape | violates simple diffuse/Lambertian assumptions |
| transparency/refraction | background rays are displaced/mixed | surface geometry, depth, occupancy | ordinary RGB-D may also fail because depth sensors can be corrupted |
| motion blur | temporal integration within exposure | correspondence, pose, object motion | fast motion can erase spatial detail before inference |
| rolling shutter | different rows captured at different times | rigid-scene geometry vs camera-motion distortion | camera model must be part of the observation model |
| exposure / HDR saturation | clipping / missing dark detail | color, texture, feature correspondence | information may be physically lost by acquisition |
| sensor noise/compression | stochastic/quantization artifacts | fine texture and correspondence | representation robustness cannot recover information that was never recorded |
| atmospheric medium | haze/rain/fog/scatter | contrast, depth, appearance | observed radiance includes medium effects, not only object properties |

This is a working map, not a complete optics textbook.

---

### 3. Geometry, material and illumination can compensate for one another

Inverse rendering is a useful foundation because it makes explicit that vision is attempting to invert a forward image-formation process.

The 2026 inverse-rendering survey organizes work around recovering:

```text
geometry
material / reflectance
illumination
```

from images, and identifies the problem as inherently ill-posed.

A bright region may be explained by, for example:

```text
bright material
strong illumination
specular reflection
surface orientation
viewpoint-dependent effect
```

or combinations of these.

The CVPR 2024 parameter-compensation analysis demonstrates that inverse-rendering systems can compensate an error in one estimated scene property by changing another scene property while still explaining the observations.

Stage-1 implication:

> Photometric reconstruction error can be low even when the recovered physical decomposition is wrong.

This directly parallels Clover's broader distinction:

```text
reconstruct the observation
≠
recover the true world state.
```

---

### 4. Transparent and refractive objects expose a hard image-formation failure

#### 4.1 Trans2Occ

**Trans2Occ: Voxel Occupancy Estimation and Grasp for Transparent Objects from Simulation to Reality**
Primary paper: https://arxiv.org/abs/2606.01777
Evidence: `PRIMARY_PAPER`

Transparent objects are difficult because refraction and reflection can make conventional depth sensing unreliable. Trans2Occ predicts voxel occupancy from a single RGB image using large-scale synthetic supervision and transfers the representation to real robotic grasping.

Why it matters:

```text
successful occupancy prediction from RGB
```

can depend on learned shape/material priors and synthetic training distributions; it does not imply that transparent geometry is uniquely determined by the pixels.

#### 4.2 SR3D

**SR3D: Unleashing Single-view 3D Reconstruction for Transparent and Specular Object Grasping**
Primary paper: https://arxiv.org/abs/2505.24305
Evidence: `PRIMARY_PAPER`

SR3D combines single-view reconstruction and RGB-D scene information to recover usable transparent/specular object geometry for grasping.

Protocol warning:

It is not strict RGB-only evidence because RGB-D scene input is part of the localization/reconstruction pipeline.

Stage-2 question:

> How much transparent-object geometry comes from actual visual evidence versus category/generative shape priors?

---

### 5. Specular reflection changes the meaning of appearance

#### UnReflectAnything

**UnReflectAnything: RGB-Only Highlight Removal by Rendering Synthetic Specular Supervision**
Primary paper: https://arxiv.org/abs/2512.09583
Project: https://alberto-rota.github.io/UnReflectAnything/
Evidence: `PRIMARY_PAPER` / `OFFICIAL_PROJECT`

The work treats specular highlights as corruption that can obscure texture and hinder geometry reasoning. It trains using physically motivated synthetic highlights and predicts a reflection-free diffuse reconstruction.

Stage-1 implication:

A pixel can contain information about:

```text
object reflectance
+
illumination
+
view direction
+
surface normal
```

rather than a stable intrinsic object color.

Therefore:

```text
appearance feature
≠
intrinsic material state.
```

---

### 6. Motion blur is information integration, not just image noise

**On Motion Blur and Deblurring in Visual Place Recognition**
Primary paper: https://arxiv.org/abs/2412.07751
Evidence: `PRIMARY_PAPER`

The work benchmarks visual place recognition under different motion-blur intensities and studies when deblurring improves localization.

Why it matters:

Motion blur is produced because a conventional frame integrates light over a nonzero exposure interval.

Conceptually:

```text
one RGB frame
≈
integral of changing scene/camera projections over exposure time.
```

Consequently, the observation is not necessarily an instantaneous world state.

Stage-1 questions:

```text
When should the world model model exposure-time integration explicitly?
How should uncertainty grow when blur destroys correspondence evidence?
Can temporal context reconstruct information lost in one frame, or only guess it from priors?
```

---

### 7. Rolling shutter means one frame may not correspond to one camera pose

**Rolling-Shutter Modelling for Direct Visual-Inertial Odometry**
Primary paper: https://arxiv.org/abs/1911.01015
Evidence: `BACKGROUND_REFERENCE`

Rolling-shutter cameras capture different image rows at different times. Ignoring this effect can strongly degrade geometric state estimation.

The cited method uses IMU information and therefore is not a vision-only baseline; its value here is conceptual.

Stage-1 implication:

```text
frame timestamp
```

is not always equivalent to:

```text
all pixels observed from one pose at one instant.
```

The camera acquisition process can itself create apparent nonrigid deformation in a rigid scene.

---

### 8. Low light, overexposure and illumination shifts alter observability

**Benchmarking Visual Feature Representations for LiDAR-Inertial-Visual Odometry Under Challenging Conditions**
Primary paper: https://arxiv.org/abs/2603.18589
Evidence: `PRIMARY_PAPER`

The paper studies low light, overexposure, illumination changes and high-parallax conditions and reports degradation/failure of ordinary photometric visual methods under severe photometric inconsistency.

Protocol warning:

The evaluated system is LiDAR-inertial-visual, so it is evidence about visual degradation and multimodal compensation, not a strict RGB-only result.

Stage-1 implication:

A general visual brain must distinguish:

```text
world changed
```

from:

```text
lighting/exposure changed.
```

Otherwise illumination variation can be mistaken for object/material/world-state change.

---

### 9. Event cameras are an informative non-RGB counterexample

**Event-based SLAM Benchmark for High-Speed Maneuvers (EvSLAM)**
Primary paper: https://arxiv.org/abs/2604.24033
Evidence: `PRIMARY_PAPER`

Event cameras react asynchronously to brightness changes and are studied specifically because conventional frames struggle under high-speed motion and extreme lighting.

Event cameras are outside Clover's strict RGB target.

Their Stage-1 role is diagnostic:

> When another sensing architecture is introduced specifically to avoid motion blur / dynamic-range limitations, that reveals information limitations of ordinary frame acquisition that a vision-only RGB system must either tolerate, model or express as uncertainty.

---

### 10. Observation failure and world uncertainty should not be conflated

Suppose a robot cannot determine whether an object is present.

Possible causes include:

```text
object is behind another object
image is overexposed
object is transparent
surface is mirror-like
motion blur erased the contour
camera viewpoint is insufficient
world genuinely contains two plausible hidden states
```

These should not all collapse into one generic low-confidence scalar.

A useful later Analysis taxonomy is:

```text
EPISTEMIC-WORLD uncertainty
    multiple real-world states fit the evidence

OBSERVATION uncertainty
    image-formation/acquisition process is unreliable

MODEL uncertainty
    learner is outside its competence/data distribution
```

Stage 1 does not yet prescribe how Clover should represent these categories; it records that they are different sources of uncertainty.

---

### 11. Active vision can change the observation operator

Active perception is useful not only because another viewpoint reveals an occluded object.

Changing viewpoint can also change:

```text
parallax
specular reflection
refraction path
shadow geometry
surface visibility
scale / foreshortening
```

Therefore an active agent can choose views that make an inverse problem better conditioned.

Relevant foundational/current references:

- Active Perception — https://ieeexplore.ieee.org/abstract/document/5968
- Vantage / Seek-and-View — https://arxiv.org/abs/2610.11810
- Vantage code — https://github.com/q1xiangchen/Vantage

Stage-2 question:

> Can an agent learn which viewpoint specifically disambiguates geometry/material/light explanations rather than merely collecting more images?

---

### 12. Proposed Stage-2 analysis dimensions

For methods that claim world reconstruction or persistent visual understanding, later Analysis should record:

```text
camera model
exposure model
rolling/global shutter assumption
illumination assumption
reflectance/material assumption
transparent/specular handling
occlusion handling
metric-scale source
static/dynamic scene assumption
whether image formation is explicitly modeled
whether ambiguity is represented or collapsed to one estimate
whether active viewpoint selection is supported
```

A method should not receive credit for recovering physical state when the evaluation only shows photometric reconstruction under the same observation assumptions.

---

### 13. Current open questions

1. How much of modern foundation-model robustness is true image-formation invariance versus learned dataset prior?
2. Can a general RGB world model maintain multiple physically plausible inverse-rendering hypotheses rather than one generated explanation?
3. How should the system separate illumination/material change from actual object/world change?
4. Which camera effects must be modeled explicitly, and which can safely be absorbed by learned representations?
5. When does active viewpoint control resolve transparent/specular/occlusion ambiguity?
6. Can uncertainty be calibrated according to the source of missing information: world ambiguity, observation failure or model ignorance?
7. Which downstream actions are sensitive enough that image-formation ambiguity must be preserved rather than averaged away?

---

### Stage-1 provisional conclusion

The visible image is not the real world state.

More precisely:

```text
real world
→ light transport / image formation
→ camera acquisition
→ RGB pixels
→ learned representation
```

Each arrow can discard or entangle information.

Therefore a scientifically serious answer to:

> How can a machine understand the real world through vision alone?

must study not only the latent world behind the pixels, but also the **physical and computational observation operator that produced those pixels**.

**Do not treat the camera as a transparent window onto state.**

---

<a id="topic-research-research_physical_properties"></a>

## Hidden Physical Properties, Contact and Irreversible Change

Source record updated: 2026-10-14
Source intake checked through: **2026-10-14**

> **Research question:** How can a machine understand the real world through vision alone?

This is a Stage-1 research inventory. It does **not** propose a Clover architecture.

Its purpose is to deepen one part of [`perception-and-identifiability.md`](#topic-research-research_state_variables): the real world contains important state that is only weakly visible, becomes informative only through temporal change or intervention, or changes irreversibly under contact.

The central questions are:

```text
Which physical properties are directly visible?
Which are only statistically predictable from appearance?
Which require observing dynamics?
Which become identifiable only through controlled interaction?
Which remain better measured through non-visual sensing?
How should a world model represent irreversible change?
```

Use the evidence-route notation from `perception-and-identifiability.md`:

```text
P0  static RGB
P1  passive temporal RGB/video
P2  active viewpoint changes while sensory evidence remains visual
P3  physical action-response observed visually
N   non-visual / privileged sensing or measured ground truth
```

---

### 1. Physical-property map

| Property / phenomenon | Current strongest evidence route | Stage-1 interpretation |
|---|---|---|
| visible geometry / shape | P0–P2 | strongly visually constrained, but metric scale and hidden surfaces remain prior-dependent |
| mass | P0/P1 possible with priors; P3 stronger | appearance/category/geometry can support prediction, but mass is not uniquely visible |
| density | P0/P1 possible with material priors; P3/N stronger | appearance may correlate with material, but density is a hidden physical parameter |
| center of mass | P3/N usually stronger | internal mass distribution is weakly constrained by appearance alone |
| moment of inertia | P3/N usually stronger | depends on mass distribution relative to axes, not just outer geometry |
| friction | P3/N | often pairwise/contact-condition dependent; appearance is not enough in general |
| stiffness / compliance | P1 under deformation; P3/N stronger | known perturbation and deformation response provide much stronger evidence than static appearance |
| temperature | N thermal/temperature sensing | RGB appearance generally does not expose object temperature reliably |
| viscosity | P1 possible from flow; P3/N stronger | flow under known perturbation is more informative than static appearance |
| granular packing / cohesion | P1/P3/N | hidden preparation state can substantially change interaction outcome |
| contact state | P1/P3; N tactile useful | visual contact may be ambiguous under occlusion |
| deformable configuration | P1–P3 | topology and dense geometry can change continuously |
| topology | P1/P3 | cutting, tearing, splitting and merging create state classes that cannot be represented as rigid pose updates |
| damage / breakage | P1/P3 | often irreversible; world-state identity and affordance may need revision after the event |
| function / affordance | P1–P3 | visual/category priors help, but interaction can reveal whether an object actually works as expected |

This table is an evidence map, not a theorem of impossibility.

---

### 2. Inertial properties: mass, center of mass and inertia

#### 2.1 Mass can be predicted visually without being visually identifiable

**Physically Guided Visual Mass Estimation from a Single RGB Image**
Primary paper: https://arxiv.org/abs/2601.20303
Evidence: `PRIMARY_PAPER`

The paper explicitly formulates single-image mass estimation as an ill-posed problem. Its solution combines learned monocular geometry with material semantics to constrain volume and density.

Stage-1 distinction:

```text
RGB
+ geometry prior
+ material/world prior
→ useful mass estimate
```

is not equivalent to:

```text
RGB uniquely determines mass.
```

#### 2.2 Physical-quantity benchmarks frequently rely on stronger sensing

**PhysQuantAgent / VisPhysQuant**
Primary paper: https://arxiv.org/abs/2603.16958
Evidence: `PRIMARY_PAPER`

VisPhysQuant provides multi-view RGB-D observations with measured object masses. It is useful for physical-quantity reasoning, but RGB-D is not a strict `V0/V1` observation protocol.

#### 2.3 Inertial parameters are a long-standing interaction problem

**Estimation and Exploitation of Objects' Inertial Parameters in Robotic Grasping and Manipulation: A Survey**
Primary paper: https://arxiv.org/abs/1911.04397
Evidence: `BACKGROUND_REFERENCE`

The survey organizes inertial-parameter estimation by interaction level: purely visual, exploratory interaction and fixed-object identification. This remains useful background because it makes center of mass and inertia explicitly different from simple appearance recognition.

#### Stage-1 gap

As of the current scan, we do **not** have a convincing modern general result showing that arbitrary real-object center of mass or moment of inertia is reliably identifiable from passive RGB alone.

Keep this as an explicit open problem rather than filling it with a category prior.

Stage-2 questions:

```text
How much inertial prediction comes from object-category memory?
Which controlled pushes/lifts/rotations most efficiently identify inertial parameters visually?
Should a robot maintain a probability distribution over inertial parameters until interaction reduces uncertainty?
```

---

### 3. Friction is an interaction property, not just an appearance label

#### 3.1 Visual + haptic friction mapping

**Probabilistic Surface Friction Estimation Based on Visual and Haptic Measurements**
Primary paper: https://arxiv.org/abs/2010.08277
Evidence: `PRIMARY_PAPER`

The work explicitly argues that vision alone does not provide enough information for reliable friction estimation and combines visual correlation with limited haptic exploration.

#### 3.2 Pairwise material interaction matters

**Generalizable Friction Coefficient Estimation via Material Embedding and Proxy Interaction Modeling**
Primary paper: https://arxiv.org/abs/2604.24188
Evidence: `PRIMARY_PAPER`

The method models friction through interactions between material pairs and measured proxy-material contacts instead of treating friction as a simple single-object image attribute.

#### 3.3 Behavior-grounded friction/contact in a world model

**DR-WM — From Pixels to Executable Physics**
Primary paper: https://arxiv.org/abs/2610.17630
Evidence: `PRIMARY_PAPER`

DR-WM obtains geometry visually, then calibrates spatial terrain/contact priors from real action-response evidence before simulating candidate actions.

Stage-1 implication:

```text
surface appearance
≠
friction coefficient
≠
pairwise contact behavior
```

and:

```text
world observation
+
controlled action
+
observed response
```

can reveal state that passive viewing leaves ambiguous.

---

### 4. Stiffness, compliance and tactile-grounded physical state

#### 4.1 ViTacPhys

**ViTacPhys: Physical Property-Aware Grasping from Human Visual-Tactile Demonstrations**
Primary paper: https://arxiv.org/abs/2608.21355
Evidence: `PRIMARY_PAPER`

ViTacPhys estimates mass classes, friction-coefficient classes and continuous stiffness from temporal human visual-tactile demonstrations and transfers the learned physical-property conditioning into robot grasping.

Why it matters:

The task demonstrates that explicit physical-property estimates can improve manipulation, but it is also a strong provenance warning:

```text
property is useful for action
≠
property came from vision alone
```

Tactile evidence is a central part of the method.

#### 4.2 Tactile world models

**DexTouch-WM: Learning Action-Conditioned Tactile World Models from Human Touch for Dexterous Robot Manipulation**
Primary paper: https://arxiv.org/abs/2609.20649
Evidence: `PRIMARY_PAPER`

DexTouch-WM combines a pretrained video expert with tactile features and action conditioning, and scales human interaction data to improve robot-domain visual, geometric and contact prediction.

#### 4.3 Tactile-grounded world-action policy

**TacSushi: Tactile-Grounded World-Action Modeling for Dexterous Sushi Manipulation**
Primary paper: https://arxiv.org/abs/2609.19613
Evidence: `PRIMARY_PAPER`

TacSushi explicitly uses fingertip tactile features and predicts future visual/tactile/contact-related quantities during training.

Stage-1 implication:

Tactile-world-model results are useful **counterexamples** when defining a vision-only research goal: they reveal which difficult variables current researchers choose to measure through touch rather than infer from RGB.

---

### 5. Temperature is a clean example of a hidden state outside visible RGB

#### HEARTH

**HEARTH: An Object-Centric RGB-Thermal-3D Dataset for Temperature-Aware Robot Manipulation**
Primary paper: https://arxiv.org/abs/2609.23418
Evidence: `PRIMARY_PAPER`

HEARTH associates everyday objects with RGB, thermal measurements, reconstructed geometry and measured temperature state. Its robot-task ablation reports substantially better temperature-dependent object selection when thermal observations are added compared with RGB alone.

Why it matters:

Temperature gives Stage 1 a particularly clear boundary condition:

```text
same visible object appearance
can correspond to
different task-relevant thermal states.
```

Therefore a robot may need to represent:

```text
unknown temperature
```

rather than hallucinate a temperature from category or appearance.

This does not make thermal sensing part of Clover's sensory target. It provides evidence about what strict visible-spectrum vision may not determine.

---

### 6. Liquids and viscosity

**Vision-Language Model-based Physical Reasoning for Robot Liquid Perception**
Primary paper: https://arxiv.org/abs/2404.06904
Evidence: `PRIMARY_PAPER`

The study reasons about household liquids and reports stronger performance when interaction-derived force/torque information is converted into visual plots and combined with ordinary visual evidence.

The method must **not** be counted as proof that viscosity is recoverable from passive RGB: its strongest setting includes non-visual interaction evidence represented visually.

Stage-2 questions:

```text
What fluid properties are inferable from free-flow video?
What requires a known perturbation or pouring protocol?
How should uncertainty be represented for visually similar liquids?
```

---

### 7. Granular materials have hidden preparation state

**Robot Excavation and Manipulation of Geometrically Cohesive Granular Media**
Primary paper: https://arxiv.org/abs/2507.19999
Evidence: `PRIMARY_PAPER`

The experiments show large differences in transported mass depending on initial substrate compaction, and connect those differences to packing/cohesion/entanglement through physical testing.

Why it matters:

Granular material state is not fully summarized by visible surface geometry. Two visually similar piles may respond differently because of hidden preparation history.

Stage-1 distinction:

```text
visible surface shape
≠
internal packing / cohesion state
≠
interaction response.
```

This is a strong reason to keep **history-dependent material state** in the research inventory.

---

### 8. Deformable objects and contact-rich state

#### PointCast

Primary paper: https://arxiv.org/abs/2609.28393
Project: https://pointcast-wm.github.io
Evidence: `PRIMARY_PAPER` / `OFFICIAL_PROJECT`

PointCast uses persistent identity-bearing 3D point sets to model rigid objects, cloth, rope and articulated cabinets with one general representation family.

#### WorldContact

Primary paper: https://arxiv.org/abs/2609.19600
Evidence: `PRIMARY_PAPER`

WorldContact makes contact-centric state central for deformable manipulation.

#### Learning to Unfold Cloth

Primary paper: https://arxiv.org/abs/2602.16675
Evidence: `PRIMARY_PAPER`

Adapts a world-model approach to cloth manipulation and reports real-robot transfer, but uses surface normals in addition to ordinary RGB.

#### ManiSoft

Primary paper: https://arxiv.org/abs/2605.18617
Project/code/data: https://buaa-colalab.github.io/ManiSoft
Evidence: `PRIMARY_PAPER` / `OPEN_SOURCE`

ManiSoft makes the robot body's own deformable state part of the problem, exposing visual estimation of self-state as a failure mode.

Stage-1 implication:

A general robotic brain may need to model:

```text
external deformable state
+
robot-body deformable state
+
contact state between them.
```

---

### 9. Irreversible topology change: cutting, splitting, tearing and breakage

Rigid-object tracking typically assumes that identity and topology survive action. Real manipulation violates that assumption.

#### 9.1 DoughNet

**DoughNet: A Visual Predictive Model for Topological Manipulation of Deformable Objects**
Primary paper: https://arxiv.org/abs/2404.12524
Evidence: `PRIMARY_PAPER`

DoughNet represents deformable objects with varying topology as sets of latent codes and predicts geometric deformation together with topology changes such as splitting/merging.

Why it matters:

```text
state update
```

cannot always mean:

```text
same entity, new pose.
```

A manipulation may create new entities, merge entities, destroy previous affordances or change connectivity.

#### 9.2 CulinaryCut-VLAP

**CulinaryCut-VLAP: A Vision-Language-Action-Physics Framework for Food Cutting via a Force-Aware Material Point Method**
Primary paper: https://arxiv.org/abs/2601.06451
Evidence: `PRIMARY_PAPER`

The framework couples robotic manipulation with a Material Point Method simulator for deformable food cutting, where cuts produce large deformation, contact forces and topology changes. Its dataset includes multi-view visual observations plus force-torque/tool-pose labels.

Protocol warning:

This is not a pure vision-only learning setup; privileged physical simulation and force/tool-state labels are part of the training/evaluation infrastructure.

#### 9.3 Sashimi-Bot

**Sashimi-Bot: autonomous tri-manual advanced manipulation and cutting of deformable objects**
Peer-reviewed article: https://www.nature.com/articles/s44182-026-00098-9
Evidence: `PRIMARY_PAPER`

Sashimi-Bot performs manipulation and cutting of natural deformable salmon using visual and tactile feedback, explicitly treating slicing as topology-altering state change.

Stage-1 implication:

A world representation intended for general robotics eventually needs a principled answer for:

```text
entity split
entity merge
material removal
irreversible deformation
breakage / damage
new affordances after transformation
invalidated old identity assumptions.
```

These are qualitatively different from reversible rigid-body motion.

---

### 10. Counterfactual and intervention datasets are becoming much more explicit

#### 10.1 What-If World

**What-If World: A Causal Benchmark for General World Models in Embodied Scenarios**
Primary paper: https://arxiv.org/abs/2605.27589
Evidence: `PRIMARY_PAPER`

The benchmark builds paired prompts from real nuScenes and DROID frames while varying one physical detail and evaluates whether generated futures change in the physically correct way.

This directly attacks a failure mode where two individually plausible videos do not respond correctly to an intervention.

#### 10.2 CRONOS

**CRONOS: Benchmarking Counterfactual Physical Consistency in Video Models**
Primary paper: https://arxiv.org/abs/2605.23699
Evidence: `PRIMARY_PAPER`

CRONOS systematically intervenes on viewpoint, scene, object category and appearance while holding the physical event type fixed.

It is useful for testing whether physical prediction is invariant to nuisance visual changes.

#### 10.3 CausalPhys

**Causal Scaffolding for Physical Reasoning: A Benchmark for Causally-Informed Physical World Understanding in VLMs**
Primary paper: https://arxiv.org/abs/2606.05966
Evidence: `PRIMARY_PAPER`

CausalPhys contains image/video questions across perception, anticipation, intervention and goal-oriented reasoning together with expert-annotated causal graphs.

#### 10.4 CG-World

**CG-World: A Large-Scale World-State Dataset and Protocol for World Models**
Primary paper: https://arxiv.org/abs/2607.26452
Evidence: `PRIMARY_PAPER`

CG-World explicitly records latent world state, geometry, skeletal/controller state, physics caches, contact events, render passes and branch metadata. Its branch structure includes observation, action and mechanism interventions plus counterfactual branches.

Critical protocol note:

CG-World is highly structured synthetic/CG supervision. It is valuable because it gives precise ground truth that real video usually lacks, but it is not evidence that such state is available from real RGB input.

#### 10.5 Dream2Fix / counterfactual failure synthesis

**Learning Actionable Manipulation Recovery via Counterfactual Failure Synthesis**
Primary paper: https://arxiv.org/abs/2603.13528
Evidence: `PRIMARY_PAPER`

Dream2Fix perturbs actions inside a generative world model to synthesize paired failure/correction rollouts from successful real demonstrations and filters them for task validity, visual coherence and kinematic safety.

Why it matters:

Counterfactual data can be used not only for abstract causal QA but for **recovery behavior**.

---

### 11. Intervention-sensitive evaluation should become standard

Several 2026 results converge on the same warning:

```text
future looks plausible
```

does not imply:

```text
future changes correctly when the intervention changes.
```

Relevant sources:

- What-If World — https://arxiv.org/abs/2605.27589
- CRONOS — https://arxiv.org/abs/2605.23699
- RoboTrustBench — https://arxiv.org/abs/2606.01600
- CausalPhys — https://arxiv.org/abs/2606.05966
- Overcoming Statistical Bias in Action-Controllable World Models — https://arxiv.org/abs/2608.04653

This motivates a future Stage-3 distinction:

```text
plausible
→ controllable / intervention-sensitive
→ actionable
```

rather than ranking world models mainly by perceptual quality.

Related survey:

**World Models for Embodied Intelligence: From Plausible to Controllable to Actionable**
Primary paper: https://arxiv.org/abs/2609.16697

---

### 12. What this means for “vision alone”

The current evidence suggests at least four qualitatively different cases.

#### Case A — visually observable or strongly constrained

Examples:

```text
2D appearance
visible geometry
motion/correspondence
some articulation state
```

#### Case B — visually predictable but prior-dependent

Examples:

```text
mass from category/material/shape
material semantics
affordance from familiar object appearance
some hidden geometry
```

#### Case C — interaction reveals much stronger evidence

Examples:

```text
friction
stiffness/compliance
center of mass / inertia
action controllability
contact response
unknown articulation mechanism
```

#### Case D — current strong systems commonly use non-visual sensing

Examples:

```text
temperature
fine contact force
some tactile properties
high-precision proprioceptive failure timing
```

A future Clover representation should therefore not be judged only by how many hidden properties it can guess.

It should be judged by whether it can:

```text
separate observation from prior
represent uncertainty
request/choose informative visual or physical interaction
update beliefs after interaction
distinguish reversible from irreversible change
retain provenance for why a hidden property is believed
avoid converting missing evidence into false certainty.
```

---

### 13. Priority Stage-2 report queue from this file

High-value future method reports:

```text
Physically Guided Visual Mass Estimation
DR-WM
ViTacPhys
HEARTH
PointCast
WorldContact
DoughNet
CulinaryCut-VLAP
Sashimi-Bot
What-If World
CRONOS
CG-World
CausalPhys
Dream2Fix
```

Important comparison axes:

```text
P0/P1/P2/P3/N evidence route
visual-only vs multimodal provenance
explicit physical variables vs latent state
reversible vs irreversible transition
entity identity under split/merge
contact representation
uncertainty / calibration
counterfactual sensitivity
real-world versus simulator supervision
action usefulness
```

---

### 14. Open gaps that Stage 1 should continue searching

```text
pure-RGB center-of-mass estimation with strong real-world validation
pure-RGB moment-of-inertia estimation
passive-video stiffness/compliance identification
visual estimation of fracture / failure thresholds
visual thermal-state inference versus explicit thermal sensing
fluid property identification under controlled visual perturbations
granular internal-state estimation
real-world cutting/tearing datasets with topology ground truth
real-world causal-intervention datasets with matched initial conditions
cross-material generalization for hidden physical properties
uncertainty benchmarks for physical property inference
minimal intervention policies for identifying hidden physical parameters
```

Do not silently replace these gaps with language-model priors.

---

**A machine that understands the physical world must know not only what is visible, but which hidden properties are merely guessed, which have been identified through evidence, and when action changes the ontology of the world itself.**

---

<a id="topic-research-dossiers-r-a-observability-epistemology"></a>

## R-A — Observability, Epistemology and Belief State

Source record updated: 2026-10-14
Status: **BACKGROUND_RESEARCH**

### 1. Fundamental question

A camera does not observe the physical state directly. It observes an image generated by hidden world state, viewpoint, visibility, illumination and sensor characteristics.

A minimal abstraction is:

```text
hidden state S_t
+ camera/view C_t
+ visibility / illumination / sensor process
→ RGB observation O_t
```

The research question is therefore not `pixels → truth`, but:

> **What can be identified from visual history, what remains ambiguous or unobserved, and what internal belief/state semantics are required for useful action under partial observability?**

This domain constrains all later representation choices.

### 2. Canonical foundations

#### POMDPs

- Survey: https://arxiv.org/abs/2209.10342

POMDPs formalize agents that must make decisions when the real state is not directly observable. The key object is a belief over possible states rather than a single guaranteed state.

**Demonstrates:** uncertainty-aware decision making under partial observation is a mature formal problem.

**Does not establish:** what visual representation should instantiate a scalable real-world belief state.

#### Probabilistic Robotics

- Book: https://mitpress.mit.edu/9780262201629/probabilistic-robotics/

Bayesian localization, mapping, filtering and state estimation provide a strong baseline for what uncertainty semantics already exist in robotics.

**Clover implication:** do not invent new words for `unknown`, `uncertain` or `unobserved` without comparing against Bayesian filtering and belief-state semantics.

### 3. Vision-only identifiability is limited

Monocular RGB generally does not make every physical variable uniquely observable.

Examples of possible ambiguity include:

- metric scale without calibration/prior;
- hidden geometry behind occlusion;
- exact mass, friction, force or internal material parameters from appearance alone;
- multiple world states that explain the same image history.

Therefore the project should distinguish at least:

```text
observed
inferred
unobserved
ambiguous / indistinguishable
contradicted
```

These are epistemic categories, not necessarily a commitment to a historical Clover licence implementation.

### 4. Partial observability also matters for causal representation

#### Partially Observable Causal Representation Learning

- ICML 2024: https://proceedings.mlr.press/v235/xu24ac.html

This work explicitly studies causal representation learning when each observation contains only a subset of latent causal state.

**Demonstrates:** representation learning and causal discovery become harder when observability changes instance by instance; identifiability can require explicit assumptions.

**Open contradiction:** can a visual world model discover stable state under changing visibility without privileged supervision?

### 5. Language and prior knowledge are epistemic confounds

A model that receives only RGB at deployment may still have learned substantial world knowledge from text, labels, robot state or privileged simulation.

Clover therefore uses two independent annotations:

```text
V-axis = inference-time visual observation protocol
L-axis = learning-evidence provenance
```

Current learning-evidence tags:

- `L0`: visual self-supervision only;
- `L1`: visual labels/annotations;
- `L2`: language/world-knowledge supervision;
- `L3`: action-conditioned experience;
- `L4`: non-visual or privileged physical evidence.

The purpose is not to reject multimodal models. It is to avoid attributing non-visual knowledge to vision itself.

### 6. Current strongest counterexamples

#### Gemini Robotics ER 2

- Official model card: https://deepmind.google/models/model-cards/gemini-robotics-er-2/
- Official model page: https://deepmind.google/models/gemini-robotics/embodied-reasoning/

Gemini Robotics ER 2 is a VLM positioned as a high-level robot reasoner with spatial, temporal and physical reasoning.

**Why it matters:** it is a strong comparator for flexible embodied reasoning.

**Confound:** its capability includes large-scale language/world priors, so success cannot automatically be attributed to visual world formation.

### 7. Operational research questions

1. When an object is not visible, should the system represent `absent`, `unknown`, `occluded`, or a distribution over hypotheses?
2. How should confidence differ from observability?
3. How should contradictory new evidence update prior state?
4. Which physical variables are visually identifiable, approximately inferable, or fundamentally underdetermined?
5. Does explicit belief state improve action compared with a strong recurrent/latent policy?
6. Can a system know that two visually plausible hypotheses are currently indistinguishable?

### 8. Best baseline families

| Baseline | What it isolates |
|---|---|
| Bayesian filtering / occupancy | explicit uncertainty and observation update |
| ORB-SLAM3 | geometry/state estimation with explicit observability assumptions |
| V-JEPA 2 / recurrent latent | implicit predictive belief-like state |
| Gemini Robotics ER 2 | multimodal reasoner with strong prior knowledge |
| direct VLA policy | action without exposed belief state |

### 9. Discriminating experiments

#### T-A-01 — Unknown vs absent

Hide an object or region without providing evidence of removal.

Measure:

```text
false absence assertions
coverage / refusal
recovery after reappearance
planning error caused by false certainty
```

#### T-A-02 — Indistinguishable worlds

Create two worlds with identical visual histories up to time `t` but different hidden states.

Correct behavior before new evidence is not to guess the hidden state with unjustified certainty.

#### T-A-03 — Belief revision

```text
initial visual evidence
→ plausible world hypothesis
→ new contradictory evidence
→ local revision
→ downstream query / plan update
```

Measure revision latency, stale-state errors and unnecessary global recomputation.

#### T-A-04 — Provenance ablation

Compare models with the same inference RGB but different learning-evidence provenance (`L0/L2/L3/L4`) to estimate how much apparent physical reasoning comes from visual evidence versus external priors.

### 10. Kill conditions for explicit epistemic machinery

An explicit belief/epistemic layer should not survive merely because it is conceptually clean.

It should be reduced or removed if a simpler latent/recurrent model gives equal or better:

- unknown/absence correctness;
- calibration;
- belief revision;
- long-horizon task success;
- recovery;
- compute/memory cost.

### 11. Clover landing

This dossier does **not** promote licences or any historical authority mechanism.

It establishes a stricter requirement:

> **The next Clover representation must state what is observed, what is inferred, what is unobserved, what is ambiguous, and how these distinctions affect future queries and actions — or demonstrate empirically that an implicit alternative handles them better.**

---

<a id="topic-research-dossiers-r-b-geometry"></a>

## R-B — Geometry: What Is Already Solved?

Source record updated: 2026-10-14
Status: **BACKGROUND_RESEARCH**

### 1. Fundamental question

> **Which parts of real-world visual understanding already have strong geometric formulations, and where do learned representations add genuinely new capability?**

Clover should not force a neural architecture to rediscover mature projective geometry if an explicit solution is already stronger, more interpretable and more reliable. Conversely, classical geometry should not be treated as sufficient for semantics, persistence, physics or causality.

### 2. Canonical foundations

#### Multiple View Geometry

- Hartley & Zisserman: https://www.robots.ox.ac.uk/~vgg/hzbook/

Key structures include:

```text
camera projection
homography
epipolar geometry
triangulation
multi-view reconstruction
bundle adjustment
```

These define exact geometric relationships independent of current deep-learning fashion.

#### Probabilistic state estimation

- Probabilistic Robotics: https://mitpress.mit.edu/9780262201629/probabilistic-robotics/

Geometry in a robot is not only reconstruction; it also involves state uncertainty, data association and sequential estimation.

### 3. Classical explicit baselines

#### ORB-SLAM3

- Paper: https://arxiv.org/abs/2007.11898
- Code: https://github.com/UZ-SLAMLab/ORB_SLAM3

**Demonstrates:** explicit camera trajectory, mapping, relocalization and multi-map reuse can be highly effective with engineered geometric structure.

**Does not establish:** semantic object identity, open-world category understanding, intuitive physics, hidden-state persistence or causality.

#### RAFT

- Paper: https://arxiv.org/abs/2003.12039
- Code: https://github.com/princeton-vl/RAFT

**Demonstrates:** dense temporal correspondence / optical flow is a strong motion primitive.

**Does not establish:** that a tracked pixel correspondence is a persistent entity or causal object.

### 4. Learned geometry changes the boundary

#### DUSt3R

- Paper: https://arxiv.org/abs/2312.14132

DUSt3R predicts point maps directly from image pairs and reduces dependence on a long classical correspondence→pose→triangulation pipeline.

**Research significance:** the useful question is no longer `classical geometry or learning?`; it is where explicit constraints and learned priors should divide labor.

#### VGGT

- Paper: https://arxiv.org/abs/2503.11651
- Code: https://github.com/facebookresearch/vggt

VGGT predicts multiple geometric quantities from images, including camera parameters, depth, point maps and tracks.

**Demonstrates:** a foundation model can serve as a broad learned geometry estimator rather than a task-specific depth or pose model.

**Does not establish:** persistent world memory, physical dynamics, causal state or action usefulness by itself.

#### VGGT-Ω

- Paper: https://arxiv.org/abs/2605.15195
- Project: https://vggt-omega.github.io/
- Code: https://github.com/facebookresearch/vggt-omega

VGGT-Ω extends the learned-geometry direction toward static and dynamic scene reconstruction and representation useful to downstream embodied systems.

**Key hypothesis to test:** reconstruction may be a scalable proxy for spatial understanding.

**Counter-question:** how far does reconstruction remain correct or useful once an object leaves the field of view, undergoes state change, or requires causal reasoning?

### 5. Geometry is not world understanding

A strong geometry system may correctly estimate:

```text
camera pose
depth
point correspondence
surface / point-map structure
motion
```

while still failing:

```text
same object after long occlusion?
object still exists outside view?
what is unknown versus empty?
what physical property caused an outcome?
what will an intervention change?
which geometry matters to a task?
```

This boundary must be measured rather than assumed.

### 6. Geometry and visible entities

#### SAM 3.1

- Official overview: https://ai.meta.com/blog/segment-anything-model-3/
- Code: https://github.com/facebookresearch/sam3
- Release notes: https://github.com/facebookresearch/sam3/blob/main/RELEASE_SAM3p1.md

SAM 3.1 improves efficient multi-object video detection/segmentation/tracking through shared-memory object multiplexing.

**Use for Clover:** a strong contemporary baseline for visible entity tracking.

**Important limit:**

```text
visible tracking
≠ object permanence
≠ persistent world state
```

A system that tracks an object while visible has not yet shown it can represent that object correctly after it leaves the field of view.

### 7. Geometry under missing views

#### Vantage

- Paper: https://arxiv.org/abs/2610.11810
- Code: https://github.com/q1xiangchen/Vantage

Vantage plans a question-relevant view and then uses geometry-grounded evidence to improve multi-view spatial reasoning.

**Demonstrates:** failure can come from missing evidence, not just weak reasoning; viewpoint selection changes the observable geometry.

**Clover implication:** geometry and active perception should be linked in V3 experiments rather than treated as independent modules.

### 8. Operational research questions

1. Which geometric quantities are reliable enough to remain explicit?
2. Which quantities are better estimated by learned geometry foundation models?
3. Does learned geometry improve robustness mainly through priors, or does it encode task-relevant world structure absent from classical pipelines?
4. How should dynamic objects and camera motion be separated?
5. Can geometric state persist through long occlusion without a separate memory mechanism?
6. Does metric 3D reconstruction improve planning, generalization or recovery compared with a strong direct policy?
7. When geometry is uncertain, how should that uncertainty propagate into downstream decisions?

### 9. Best baseline matrix

| Family | Baseline | Isolates |
|---|---|---|
| Classical geometry | ORB-SLAM3 | explicit camera/map state |
| Dense motion | RAFT | short-term correspondence |
| Learned pairwise geometry | DUSt3R | learned point-map estimation |
| Geometry foundation model | VGGT | broad learned spatial state |
| Dynamic learned geometry | VGGT-Ω | dynamic reconstruction / global spatial representation |
| Visible entity tracking | SAM 3.1 | detection/segmentation/tracking while visible |

### 10. Discriminating experiments

#### T-B-01 — Geometry-only capability boundary

Use the same V0/V1 video and compare:

```text
ORB-SLAM3
RAFT
VGGT / VGGT-Ω
```

Queries:

```text
Where is the camera?
What moved?
Which points correspond?
What is behind / in front?
Same object after occlusion?
Still exists outside view?
What changed causally?
```

The purpose is to identify exactly where geometry stops being sufficient.

#### T-B-02 — Reconstruction vs persistence

Evaluate a reconstruction model before, during and after long out-of-FOV intervals using PersistBench-style ground truth.

Measure:

- geometric continuity;
- object identity continuity;
- appearance preservation;
- stale hallucinated geometry;
- uncertainty when evidence is absent.

#### T-B-03 — Geometry value for action

Matched comparison:

```text
strong policy
vs
same policy + explicit / learned geometry state
```

Measure unseen-scene success, planning cost, collision/reachability error and recovery.

#### T-B-04 — Camera shift

Hold world/task constant while changing intrinsics, viewpoint and trajectory.

This separates a genuinely geometric representation from camera-specific visual shortcuts.

### 11. Kill conditions

A geometry pathway should not be preserved as a privileged world representation if it adds no measurable benefit to:

- spatial correctness;
- generalization under camera shift;
- long-horizon persistence;
- planning/search cost;
- recovery;
- task success.

Likewise, a learned geometry model should not replace exact classical structure merely because it is newer if it is less reliable or less observable in the relevant regime.

### 12. Clover landing

Current conclusion:

> **Geometry is a solved-to-strongly-solved subproblem in several regimes, not a solved world-understanding problem. The next Clover representation must treat geometry as prior art to beat or reuse, then demonstrate what additional state is required for identity, memory, physics, causality and action.**

---

<a id="topic-research-dossiers-r-e-physics"></a>

## R-E — Physical Understanding: Plausibility, Quantification and Relational Structure

Source record updated: 2026-10-14
Status: **BACKGROUND_RESEARCH**

### 1. Fundamental question

> **What does it mean for a vision-only system to understand physical behavior rather than merely recognize visually familiar motion?**

A useful ladder is:

```text
perceptual continuity
→ intuitive plausibility
→ quantitative kinematics
→ relational physical consistency
→ intervention-sensitive prediction
→ counterfactual consistency
→ improved action / recovery
```

No single benchmark covers this ladder.

### 2. Intuitive physics

#### IntPhys 2

- Paper: https://arxiv.org/abs/2506.09849
- Code: https://github.com/facebookresearch/IntPhys2
- Official Meta publication: https://ai.meta.com/results/?content_types%5B0%5D=publication&page=7

IntPhys 2 evaluates four principles:

```text
Permanence
Immutability
Spatio-Temporal Continuity
Solidity
```

using violation-of-expectation video pairs in controlled synthetic scenes.

**Demonstrates:** many strong models remain weak on controlled intuitive-physics violations despite good general visual capability.

**Limit:** synthetic controlled plausibility is not yet real-world quantitative physics or action-grounded causal understanding.

### 3. Shortcut-resistant physical reasoning

#### Minimal Video Pairs / MVPBench

- Paper: https://arxiv.org/abs/2506.09987
- Code/data reference: https://github.com/facebookresearch/minimal_video_pairs
- Meta physical-reasoning overview: https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/

MVP-style evaluation pairs videos that differ minimally but require opposite answers.

**Research value:** minimal pairs reduce the ability to solve a benchmark using background, language or coarse appearance shortcuts.

**Clover implication:** future physical-understanding claims should include paired intervention/perturbation controls, not only aggregate benchmark accuracy.

### 4. Quantitative physical reasoning

#### QuantiPhy

- Paper: https://arxiv.org/abs/2512.19526

QuantiPhy evaluates numerical estimation of physical properties such as size, velocity and acceleration from video.

**Demonstrates:** qualitative verbal plausibility can remain strong while numerical physical estimates are poor; models may rely heavily on pretrained world knowledge rather than the actual provided evidence.

**Clover implication:** physical understanding should include machine-checkable quantities, not only natural-language explanations.

### 5. Relational physics without calibration dependence

#### Principia

- Paper: https://arxiv.org/abs/2609.04200
- Project: https://principiabench.github.io/

Principia evaluates paired-object relational consistency for phenomena including:

- gravity;
- restitution;
- friction;
- rotational inertia;
- projectile motion;
- momentum;
- pendulum motion;
- mass-spring oscillation.

Its key methodological idea is that relative relationships between objects can remain diagnostic even when absolute scale, frame rate or camera calibration are ambiguous.

**Clover significance:** this is especially relevant to V0 vision, where exact metric calibration may be unavailable.

### 6. Physical variables can emerge in distributed representations

#### Interpreting Physics in Video World Models

- Official: https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/
- Paper: https://arxiv.org/abs/2602.07050

The study finds layerwise emergence of speed, acceleration and motion direction, with direction encoded as a high-dimensional population code.

**Implication:** a model can carry useful physical information without exposing a compact symbolic physics state.

Therefore:

```text
physical understanding
≠ automatically explicit physics variables
```

### 7. Physics as prediction is still not physics as execution

#### RoboPhys-3D

- Paper: https://arxiv.org/abs/2608.28718

RoboPhys-3D evaluates world-model rollouts at multiple levels including pixel fidelity, 3D geometry consistency, state-level understanding and task-level completeness.

**Key lesson:** visually plausible generated video can still fail state- and execution-grounded metrics.

For Clover:

```text
plausible future video
≠ correct physical state
≠ executable consequence
```

### 8. Visually inferred physical properties must remain hypotheses

Vision may support useful estimates of:

```text
support
contact likelihood
relative mass hypothesis
slip risk
deformation tendency
material-like behavior
```

But exact hidden quantities such as force, friction coefficient or internal material parameters are not generally direct visual observations.

A scientifically careful system must distinguish:

```text
measured visually
inferred from dynamics
inferred from appearance prior
not identifiable from current evidence
```

### 9. Operational research questions

1. Which physical laws are learnable from passive video alone?
2. Which physical variables require interaction to become identifiable?
3. Is relational physics more robust than absolute metric prediction under V0?
4. Does a predictive latent encode enough physics for action without explicit state?
5. How much physical accuracy is hidden by visually realistic generation metrics?
6. Can the system distinguish visually plausible but physically impossible rollouts?
7. Do explicit physical variables improve novel-object transfer and recovery?

### 10. Best baseline battery

| Capability | Baseline / benchmark | What it measures |
|---|---|---|
| Intuitive plausibility | IntPhys 2 | permanence, continuity, solidity, immutability |
| Shortcut resistance | MVPBench | minimal visual changes with answer flips |
| Quantitative kinematics | QuantiPhy | numerical size/velocity/acceleration |
| Relational laws | Principia | calibration-independent Newtonian consistency |
| Latent physical representation | V-JEPA 2/2.1 probing | decodability of physical information |
| Execution-grounded state | RoboPhys-3D | world-model state and task consequences |

### 11. Discriminating experiments

#### T-E-01 — Qualitative vs quantitative split

Use the same video to ask:

```text
Will it fall?
How fast is it moving?
Which of two objects accelerates more?
What numerical acceleration is supported?
```

This separates language-level plausibility from quantitative grounding.

#### T-E-02 — Relational invariance

Vary:

```text
camera scale
frame rate
viewpoint
object appearance
```

while preserving the physical relation.

Measure whether the model preserves the correct relation.

#### T-E-03 — Appearance prior conflict

Construct objects whose visual appearance suggests one material/dynamics prior but whose observed motion supports another.

Measure whether the model follows actual visual dynamics or pretrained semantic expectation.

#### T-E-04 — Passive vs action-conditioned physics

Compare the same base representation before and after action-conditioned experience.

Measure gains in:

- consequence prediction;
- affordance transfer;
- intervention sensitivity;
- quantitative dynamics.

#### T-E-05 — State-grounded rollout

Evaluate generated/predicted futures by downstream reconstructed state and executable consequences, not by video quality alone.

### 12. Kill conditions

A proposed explicit physics mechanism should be removed if it does not outperform strong latent/video baselines on at least one of:

- quantitative prediction;
- relational invariance;
- intervention transfer;
- novel dynamics;
- planning/recovery;
- sample efficiency.

Likewise, a generative model should not be called physically grounded if its advantage exists only on perceptual/video metrics while state/action consequences are wrong.

### 13. Clover landing

Current conclusion:

> **Physical understanding should be treated as a layered empirical target—from plausibility through quantitative and relational constraints to intervention and action—not as a single score or a commitment to explicit physics variables.**

---

<a id="topic-docs-research-map-classical-vision"></a>

## Classical Computer Vision and Geometry

### Why Clover must study this seriously

Before deep learning, computer vision developed explicit mathematical machinery for recovering structure and motion from images. Clover should not force a learned model to rediscover every well-understood invariant merely to appear end-to-end.

The important question is:

> **Which parts of visual world understanding already have reliable mathematical structure, and where do those methods stop?**

### Core bodies of prior work

#### Projective and multi-view geometry

Provides explicit relationships among camera projection, epipolar constraints, triangulation, pose and 3D structure.

#### Structure from Motion / Bundle Adjustment

Jointly estimates camera states and 3D landmarks by minimizing geometric reprojection errors.

#### Visual odometry and SLAM

Maintains a spatial estimate while a camera moves through a scene. Modern SLAM systems add loop closure, relocalization and multi-map operation.

#### Optical flow

Estimates image-plane motion. Flow is not itself world motion, but it is a key observable for temporal geometry.

#### Tracking and filtering

Kalman filters, particle filters and data association formalize uncertainty, temporal prediction and observation updates.

#### Occupancy / mapping

Explicitly distinguishes observed free space, occupied space and often unknown space — a distinction directly relevant to Clover's observability semantics.

### ORB-SLAM3

ORB-SLAM3 is an open-source real-time system supporting visual, visual-inertial and multi-map SLAM across monocular, stereo and RGB-D configurations.

Primary source:

- https://github.com/UZ-SLAMLab/ORB_SLAM3

Clover should use it as an intellectual baseline for explicit persistent geometry, not as a module to import blindly.

### RAFT

RAFT is a learned optical-flow model built around recurrent all-pairs field transforms.

Primary source:

- https://github.com/princeton-vl/RAFT

It is useful as a reminder that the boundary between 'classical variable' and 'learned estimator' is already porous: the variable can remain explicit while the estimator is learned.

### What classical approaches solve well

- camera geometry under stated assumptions;
- metric/relative structure from multiple views;
- explicit state estimation and uncertainty propagation;
- loop closure/relocalization in structured environments;
- interpretable failure modes tied to observability and geometry.

### What they do not solve by themselves

- open-ended semantic abstraction;
- general object type formation;
- high-level physical common sense;
- causal understanding;
- broad transfer from large visual experience;
- deformable/non-rigid everyday worlds at general scope;
- task relevance and language-level goals.

### Clover research tension

The modern question is not classical **or** learning. A more useful decomposition is:

> **Which invariants should be structural, which estimators should be learned, and which abstractions must emerge from experience?**

This is likely more productive than rebuilding a purely hand-engineered or purely learned stack.

---

<a id="topic-docs-research-map-spatial-intelligence"></a>

## Spatial Intelligence

### Core question

> **How much of world understanding can be obtained by reconstructing and maintaining coherent geometry from vision?**

Spatial intelligence is broader than depth estimation. It includes camera/world geometry, consistent multi-view representation, reconstruction, scene completion and potentially simulation.

### Classical-to-learned transition

Traditional SfM/SLAM explicitly optimizes camera geometry and sparse/dense landmarks. Modern geometry foundation models increasingly infer camera and scene geometry directly with learned feed-forward systems.

This transition is important to Clover because it asks which parts of a world representation should be mathematically constrained and which should be learned from scale.

### VGGT

VGGT (CVPR 2025 Best Paper) is a feed-forward learned geometry model. The official repository describes direct inference of key 3D scene attributes including camera intrinsics/extrinsics, depth maps, point maps and 3D point tracks from one or many views.

Primary source:

- https://github.com/facebookresearch/vggt

#### Why Clover cares

VGGT demonstrates that a large learned visual model can collapse a traditionally multi-stage geometry pipeline into one learned inference system while still outputting explicit geometric quantities.

This creates a powerful hybrid precedent:

> **learned representation does not imply that the output world state must remain implicit.**

### VGGT-Ω

VGGT-Ω extends this line to larger-scale static and dynamic reconstruction. As of September 2026 the official repository exposes training code, reproduction checkpoints and data preparation material.

Primary sources:

- https://vggt-omega.github.io/
- https://github.com/facebookresearch/vggt-omega

#### Clover question

The project argues that reconstruction representations can transfer to broader spatial tasks. Clover should investigate the stronger proposition:

> **Is reconstruction sufficient as the spatial substrate of a persistent robot worldview, or does understanding require additional state for observability, object identity, dynamics, causality and task relevance?**

### DUSt3R / MASt3R family

These systems replace parts of classical multi-view correspondence and reconstruction with learned point-map style representations.

Reference:

- https://arxiv.org/abs/2312.14132

The relevant lesson is not to copy their architecture, but to understand why learned correspondences can outperform or simplify hand-engineered matching in difficult imagery.

### World Labs Atlas

World Labs introduced Atlas in September 2026 as an omni world model operating over text, images, video and 3D. Its stated scope includes generation, reconstruction, simulation and robot planning. The architecture is described as a multimodal autoregressive diffusion transformer with a shared spatial context.

Primary source:

- https://www.worldlabs.ai/blog/atlas

Atlas is not a pure-vision system, but it is a strong reference for a competing thesis:

> a generative spatial context may be enough to support multiple world functions without exposing a symbolic state.

### Key separations Clover must preserve during research

#### Geometry is not yet semantics

Accurate camera pose and point maps do not automatically supply object identity or type.

#### Reconstruction is not yet permanence

Reconstructing what was observed is different from representing what is currently unobserved but believed to persist.

#### Novel-view consistency is not yet causality

A coherent renderer may still lack intervention-sensitive dynamics.

#### 3D is not automatically the only useful space

Robots may need metric geometry, topological place structure, object-relative relations and task abstractions simultaneously.

### Open questions

1. Which world queries become trivial once strong geometry is available?
2. Does a 3D reconstruction remain stable under moving/deformable objects?
3. What is the minimum persistent spatial state required beyond a learned geometry encoder?
4. How should active camera motion update uncertainty and visibility?
5. Can explicit geometry reduce planning sample complexity compared with latent-only policies?

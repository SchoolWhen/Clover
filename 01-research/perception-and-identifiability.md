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
- **机制：** 以交互多模型运动协方差调节关联区域，并在新外观证据后修正交叉身份。
- **输入与学习来源：** 关联器无新训练；上游检测器与外观来源仍须登记。
- **实际证据：** 2026-10-15 的运动/相机扰动下多目标追踪候选。
- **边界与反假设：** 不训练关联器不等于无检测成本、无监督或一般不确定性校准；需同检测输入比较完整管线与身份错误。
- **阅读深度：** 摘要及问题设定选读；未复核完整实验；未运行复现。

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

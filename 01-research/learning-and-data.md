<a id="top"></a>

# 调研方向：数据、训练与持续学习

Maintained: **2026-10-25** · Document stage: **1 — Research** ([status](../STATUS.md)).

Training, post-training, data provenance, continual learning and capability preservation under adaptation.

This is the canonical topic document. Update it in place; source-level dates and reading-depth labels below qualify the evidence, not the maintenance date.

<!-- BEGIN current-cross-domain-evidence -->
<a id="current-cross-domain-evidence"></a>

## 当前跨领域与前沿证据：学习目标、领域数据与物理交互的归因

检索/核验：**2026-10-25（Asia/Shanghai）**。下表是外部研究记录，不是 Clover 的实验结果或架构决定。

把“自监督”拆到预训练、后训练和部署每一步；没有任务奖励、没有真动作标签、没有语言、没有物性标签是不同条件。新结果进一步要求把预测质量与用于策略改进的信号分开：当前任务回报更高仍可能牺牲开放世界所需信息。

### DynaMo

- **来源/版本：** [原论文](https://arxiv.org/abs/2409.12192v2)；初始提交 2024-09-18；本次返回版本更新于 2024-10-30。`PRIMARY_PAPER`。 [作者提供的项目/代码入口](https://dynamo-ssl.github.io)（未运行复现）。
- **问题与机制：** DynaMo 共同学习潜在逆动力学和前向动力学，以领域内示范视频预训练视觉表示。
- **输入/学习来源：** 预训练不使用真动作标签；下游模仿学习仍使用示范动作。两阶段分别记账，不能统称全链 L0。
- **实际证据：** 六组模拟/真实环境中的下游模仿学习，并比较不同策略类。
- **不能推出 / 待区分：** 收益可能来自领域内数据、动力学目标或表示；需要匹配数据和骨干，不能仅归因于“预测天然理解”。
- **本次阅读深度：** 摘要与书目核验。

### IRM

- **来源/版本：** [原论文](https://arxiv.org/abs/1907.02893v3)；初始提交 2019-07-05；本次返回版本更新于 2020-03-27。`PRIMARY_PAPER`。
- **问题与机制：** IRM 寻找在多个训练环境上共享最优分类器的表示。
- **输入/学习来源：** 训练环境划分与监督任务已给定；这不是任意未知机制变化下的无条件保证。
- **实际证据：** 不变预测与因果结构关联的理论/实验研究。
- **不能推出 / 待区分：** 跨环境不变相关性仍依赖环境多样性及模型假设；对机器人要分别改观测、动力学、任务与机体。
- **本次阅读深度：** 摘要与书目核验。

### DiffDreamer

- **来源/版本：** [原论文](https://arxiv.org/abs/2610.31617v1)；初始提交 2026-10-22；本次返回版本更新于 2026-10-22。`PRIMARY_PAPER`。
- **问题与机制：** DiffDreamer 分别用潜在世界模型推进外部动态、用可微模拟推进机器人显式状态。
- **输入/学习来源：** 模拟器、自机物理状态与里程计等条件必须记录为额外来源。
- **实际证据：** 四旋翼追踪、动态门穿越及真实飞行概念验证。
- **不能推出 / 待区分：** 自机/外界分解是控制反假设，不证明从视觉获得全部自机动力学；可微奖励路径需与任务回报路径分开。
- **本次阅读深度：** 摘要与书目核验。

### DRILL

- **来源/版本：** [原论文](https://arxiv.org/abs/2610.30814v1)；初始提交 2026-10-22；本次返回版本更新于 2026-10-22。`PRIMARY_PAPER`。
- **问题与机制：** DRILL 以想象训练后的策略回报监督世界模型，而不是只降低像素误差。
- **输入/学习来源：** VLA、动作回放、奖励/GRPO 和模拟 rollout 等来源须保留。
- **实际证据：** 两种优化实现、多个模拟器与骨干；比较预测质量和策略收益。
- **不能推出 / 待区分：** 任务回报充分与世界信息充分不同；不能用既定任务成功掩盖未训练物理查询/记忆/因果能力退化。
- **本次阅读深度：** 摘要与书目核验。

### FRED

- **来源/版本：** [原论文](https://arxiv.org/abs/2610.30320v1)；初始提交 2026-10-21；本次返回版本更新于 2026-10-21。`PRIMARY_PAPER`。
- **问题与机制：** FRED 用真实未来表征作自蒸馏目标，从单步去噪中提取未来特征供动作解码。
- **输入/学习来源：** 未来帧只可作训练目标；视频骨干、机器人/人类数据与下游动作监督分列。
- **实际证据：** 真实操作、长时程/环境变化、人视频到机器人迁移。
- **不能推出 / 待区分：** 训练时未来可见性和测试历史必须隔离；收益不能同时归给表示、上下文和新数据却不做配平。
- **本次阅读深度：** 摘要与书目核验。

### SkeLAM

- **来源/版本：** [原论文](https://arxiv.org/abs/2610.31474v1)；初始提交 2026-10-22；本次返回版本更新于 2026-10-22。`PRIMARY_PAPER`。
- **问题与机制：** SkeLAM 用机器人骨架监督分开运动学 latent action 与残余视觉动态。
- **输入/学习来源：** 骨架/动作监督、跨模态重构和未来残余训练信息构成 L3/L4 来源。
- **实际证据：** DROID 的动作条件视频与运动探针/策略评估。
- **不能推出 / 待区分：** 学到 latent action 不等于发现未监督因果变量；必须验证测试端不再依赖未来残余或骨架真值。
- **本次阅读深度：** 摘要与书目核验。

### Ropedia W0

- **来源/版本：** [原论文](https://arxiv.org/abs/2610.26855v1)；初始提交 2026-10-19；本次返回版本更新于 2026-10-19。`PRIMARY_PAPER`。
- **问题与机制：** Ropedia W0 将人/机器人自我中心运动用统一运动学接口对齐，再做跨机体世界预测。
- **输入/学习来源：** 相机位姿、投影骨架、机器人正运动学、人工修正与示范属于混合 L1/L3/L4。
- **实际证据：** 人/机器人数据、loco-manipulation 与 teleoperation benchmark。
- **不能推出 / 待区分：** 人视频规模收益不能与运动学标注、对齐和后训练收益混为一项；生成实时性不是闭环机器人可靠性。
- **本次阅读深度：** 摘要与书目核验。

### EndoWorld-JEPA

- **来源/版本：** [原论文](https://arxiv.org/abs/2610.27890v1)；初始提交 2026-10-20；本次返回版本更新于 2026-10-20。`PRIMARY_PAPER`。
- **问题与机制：** EndoWorld-JEPA 从过去光流分离整体位移与局部变化，引导潜在状态预测。
- **输入/学习来源：** 被动内窥镜视频，不需记录动作/标定位姿；预测所用运动窗口不得包含未来信息。
- **实际证据：** 多项内窥镜视频下游迁移；作为运动表征跨领域参照。
- **不能推出 / 待区分：** 过去运动条件不是 do-干预证据；场景迁移表现不能推出自然机器人因果识别，也不是临床有效性结论。
- **本次阅读深度：** 摘要与书目核验。
<!-- END current-cross-domain-evidence -->

<!-- BEGIN learning-provenance-frontier -->
<a id="learning-provenance-frontier"></a>

## 学习来源的前沿归因：纯视觉、语言、教师与失败数据

检索/核验：**2026-10-25（Asia/Shanghai）**。本节不重复各方法的任务记录，而回答一个对 Clover 更关键的问题：**当能力提升时，究竟该归因于视觉自监督、语言监督、教师蒸馏、合成数据、训练配方，还是部署分布？** 以下结论来自受控比较或作者自述的边界，不是 Clover 实验。

### WebSSL：同一数据上，纯视觉自监督可以追平图文监督

- **一手来源：** [固定版本](https://arxiv.org/abs/2504.01017v1) · [作者项目](https://davidfan.io/webssl/)。`PRIMARY_PAPER` / `OFFICIAL_PROJECT`。
- **机制：** 把视觉自监督与 CLIP 放在**同一 MetaCLIP 图像数据**上训练，以 VQA 和经典视觉基准做受控比较；避免“SSL 与 CLIP 用了不同数据”这一混淆。
- **输入与学习来源：** 训练目标不含图文对比（`L0`）；但数据来自 MetaCLIP 语料，筛选/来源元数据可能使用文本；VQA 评估提供问题文本。因此“language-free”指**训练目标**，不是整条数据与评估管线无语言。
- **实际证据：** 在该设置中，视觉 SSL 随数据与模型规模增长优于 CLIP，扩到 7B 仍未饱和，并在多类 VQA 与经典视觉基准达到 CLIP 水平。
- **不能推出：** 追平的是特定基准；开放词汇检测、文字阅读、空间/物理推理、持续记忆未由此闭合；数据策展与 VQA 语言接口仍是混杂因素；不等于“语言监督可被完全替代”。
- **阅读深度：** 摘要与作者项目说明；未复核全部训练细节；未运行复现。

### StreamMAE：连续视频流上的自监督学习，不等于把帧打乱

- **一手来源：** [固定版本](https://arxiv.org/abs/2609.40333v1)（NeurIPS 2026）。`PRIMARY_PAPER`。
- **机制：** 研究严格按时间顺序、滑窗 batch、无全局 shuffle/多 epoch 回放的连续视频自监督；构建 WT++（95 小时城市步行视频）与评估套件；发现对比/蒸馏方法在流式设置下退化，MAE 较稳但仍低于 i.i.d.；主因是同一 batch 内近重复帧造成的高 intra-batch 相似度。StreamMAE 保留 MAE 重建目标，加入 stream-aware 正则与运动偏置 crop。
- **输入与学习来源：** 无标签连续视频 `L0`；MAE 像素重建；WT++ 数据与评估协议；不涉及语言/动作标签。
- **实际证据：** 作者报告 StreamMAE 优于流式基线，并在相同视频数据上追平 i.i.d. MAE；对比/蒸馏基线在流式设置下明显退化。
- **不能推出：** 除运动偏置 crop 外没有显式时序动力学；固定帧下采样是次优；只在 checkpoint averaging 层面处理长时聚合；城市步行域有限；不是视频世界模型、追踪或语义理解。
- **阅读深度：** 正文选读：流式设置、WT++、主结果与附录 Limitations；未复核全部附录；未运行复现。

**对 Clover 的意义：** 这是目前最直接支持“纯视觉路线在规模上可行”的受控证据，但它同时给出了两条约束：第一，必须匹配**数据**再比较监督目标；第二，纯视觉模型仍要在语言定义的任务（开放词汇、文字、关系）上单独证明，不能借 VQA 分数外推。

### 监督来源的二维记账：目标 × 数据

| 方法族 | 训练目标 | 数据/教师来源 | 能支持的主张 | 不能支持的主张 |
|---|---|---|---|---|
| MAE / DINOv3 | 像素重建 / 自蒸馏（`L0`） | 图像语料；策展可能含元数据 | 静态视觉特征可规模化、可迁移 | 开放词汇语义、文字、物理、时序状态 |
| CLIP / Meta CLIP 2 / SigLIP 2 / PE | 图文对比 + 语言/定位辅助（`L2`） | 网络图文对；多语言/数据引擎 | 零样本分类/检索、语言对齐的密集特征 | 无语言先验的视觉概念发现；纯视觉学习证据 |
| AIMv2 | 图像 patch + 文本自回归（`L2`） | 图文数据 | 冻结主干的强识别/定位迁移 | 纯视觉目标；长期记忆 |
| WebSSL | 视觉自监督（`L0`） | **同一** MetaCLIP 图像数据 | 受控数据下 SSL 可追平 CLIP | 全任务等价；数据管线无语言 |
| SAM 3 / SAM 3D / DA3 / olmOCR 2 | 检测/分割/几何/OCR + 数据引擎/教师/RLVR（`L1/L4`） | 人工+模型在环、合成、教师伪标签 | 特定能力的高质量监督可规模化 | 架构单独贡献；纯视觉自监督；开放世界因果 |
| YOLO26 / DEIM / RF-DETR / D-FINE | 检测监督 + 训练配方/NAS（`L1`） | COCO/Objects365/目标数据集 | 训练收敛、NMS-free、目标域 Pareto | 推理机制独立贡献；跨任务统一权重；真实闭环时延 |

<a id="pure-vision-provenance-audit"></a>

### 纯视觉声称审计：V0–V3 × L0–L4

“纯视觉”至少有三个不同主张：**部署只接收 RGB（V0）**、**训练不用人工标签/语言/动作（L0）**、**推理不接外部工具/记忆**。本轮 104 篇新论文中，同时满足三者的极少。下表按论文披露逐项拆分；“L0*”表示目标函数为视觉自监督，但数据策展/评估仍可能使用语言元数据。

| 方法 | 部署输入 | 学习来源 | 外部先验/工具 | 纯视觉程度 | 不能声称 |
|---|---|---|---|---|---|
| MAE / DINOv3（base） | V0 图像 | L0 像素重建/自蒸馏 | 数据策展；DINOv3 文本对齐变体另记 | **接近 V0/L0** | 语义、文字、物理、时序状态 |
| StreamMAE | V0 连续视频 | L0 重建 + 流式正则 | 固定帧下采样/光流式运动偏置 | **接近 V0/L0** | 世界模型、追踪、语义 |
| WebSSL | V0 图像 | L0 视觉自监督 | 同 MetaCLIP 数据；评估 VQA 含语言 | **L0\*** | “整条管线无语言”；开放词汇/文字 |
| MoSA | V0 图像（训练用视频） | L0 + 合成视频 + 光流伪标签 | 合成数据、运动分割前端 | **V0/L0 + 合成/光流** | 零先验；语义/身份/物理 |
| CLIP / PE / MetaCLIP2 / SigLIP2 / AIMv2 | V0 图像/视频 | L2 图文对比/生成 | 网络图文对、数据策展 | **L2** | 无语言先验的视觉概念发现 |
| SAM 3 | V0 图像/视频 | L1 掩码/概念标签 + L2 文本编码器 | 5.4B 图文对、4M 概念数据引擎、exemplar | **L1+L2** | 纯视觉学习；单 GPU 实时多目标 |
| SAM 3D | V0 单图 | L1 3D/纹理标注 + L4 合成/艺术家数据 | 合成预训练、真实对齐、DPO 数据回收 | **L1+L4** | 纯视觉物理重建；接触/布局 |
| DA3 | V0/V2 图像/多视图 | L1/L4 深度/位姿 + 教师伪标签 | 公开学术数据、教师模型 | **L1+L4** | 无监督；动态/物理理解 |
| SAMURAI | V0 视频 + 首帧框 | 上游 SAM 2 L1；本身不重训 | Kalman 运动先验、SAM 2 记忆 | **V0 + L1 上游** | 从零纯视觉；开放世界多目标 |
| MOTIP2 / UGO | V0 视频 + 首帧框/exemplar | L1 MOT/GMOT 标注 | 检测器预训练、空间先验 | **L1** | 纯视觉身份；物理实体理解 |
| When Trackers Fail | V0 视频 | L1 SAM3 失败轨迹 + L2 VLM 验证 | VLM、SAM3 传播器 | **L1+L2** | 纯视觉；实时/形式安全 |
| TAPNext / TAPNext++ | V0 视频 + 查询点 | L1/L4 合成轨迹/教师伪标签 | BootsTAP、合成数据 | **L1/L4** | 纯视觉物理状态；长时身份 |
| CoTracker3 | V0 视频 + 查询点 | L1/L4 合成轨迹 + 教师伪标签 | Kubric、教师 | **L1/L4** | 纯视觉；对象语义 |
| WOW-Seg | V0 图像 + 掩码 | L1 掩码/类别 + L2 VLLM | VLLM 世界知识、掩码生成器 | **L1+L2** | 无语言预训练；无文字提示≠纯视觉 |
| PaddleOCR-VL / dots.ocr | V0 文档图像 | L1 OCR/结构 + L2 LLM | 语言模型、数据引擎 | **L1+L2** | 纯视觉阅读；语义推理 |
| V-JEPA 2（机器人变体） | V0 视频（+动作） | L0 视频预测 + L3 动作条件 | 机器人动作/示范 | **L0/L3** | 纯被动视觉；通用物理 |
| StarWM | V0 控制观测 | L0 动力学 + L3 奖励变体 | DreamerV3 骨架、奖励 | **L0/L3** | 真实机器人；任务无关状态 |
| Dreamer 4 | V0 游戏画面 | L3 动作 + 离线游戏数据 | 动作标签、游戏模拟器 | **L3** | 真实相机物理；纯视觉 |
| Gen4P | V0 单目视频 | L1/L4 几何/深度 + 生成器预训练 | 视频生成器、深度 LoRA | **L1/L4+生成先验** | 纯视觉 4D；因果/物性 |
| FoveaVLA / EgoReveal | V0/V2 + 动作/位姿 | L3 示范 + L4 深度/关键点 | 机器人动作、外部相机、位姿 | **L3/L4** | 纯视觉；被动观察 |
| RFL / SpatialScout | V0/V1/V2 + 位姿/标定 | L2 VLM + L4 3DGS/位姿 | VLM、3DGS、相机标定、物体清单 | **L2+L4/V1–V2** | 纯单目 V0；通用主动探索 |
| LiFR-Seg | RGB + 事件（非 V0） | L1 语义标签 | 事件相机、标定 | **事件+L1** | 纯 RGB；通用视觉 |
| UGO / UniRAP / UniFunc3D | V0/V2 图像/视频 | L1 标签 + L2 语言/可供性 | exemplar、语言、3D 表示 | **L1+L2** | 纯视觉；物理可行性 |

**审计结论：**
1. **真正接近 V0/L0 的只有静态/视频自监督表征与无监督分割**（MAE、DINOv3、StreamMAE、WebSSL、MoSA）；其中 WebSSL 的数据/评估、MoSA 的合成视频/光流仍是混杂项。
2. **所有追踪/OCR/3D/可供性/主动视觉方法都至少依赖 L1 标注**；多数还依赖语言（L2）、动作（L3）、深度/位姿/力（L4）或模拟器。把它们统称“纯视觉”不成立。
3. **“无文字提示”不等于“无语言训练”**（WOW-Seg），“无人工标注”不等于“无合成数据/光流”（MoSA），“只用 RGB 部署”不等于“只用 RGB 学习”（SAMURAI/CoTracker 上游）。
4. **新增隐藏态证据进一步收紧边界：** 单图质量估计虽只需 RGB 推理，却依赖单目深度与 VLM 材料先验（`L1/L2`）；iSEE 是无标签视频下少见的 `V0/L0` 永久性证据，但限固定相机；ViTacPhys 与 ViWi 用触觉/WiFi 明确反证“视觉-only 唯一识别物性”。
5. 因此 Clover 的“vision alone”必须分阶段声明：**V0/L0 表征**、**V0/L1 任务适配**、**V0/L2 语义接口**、**V3/L3 行动学习**。任何跨阶段的能力都必须单独证明，不能用一个总标签概括。

### 教师、合成数据与“数据引擎”的归因规则

1. **教师是额外证据来源。** DA3 的教师-学生继承 Depth Anything 2 的细节/泛化；SAM 3D 用合成预训练 + 真实对齐；olmOCR 2 用合成文档与可验证单元测试。若把学生成绩归因于“普通 Transformer 更强”，就抹掉了教师与合成数据。
2. **人工在环不是免费标签。** SAM 3 的 4M 概念标签、SAM 3D 的人类+模型在环标注、PaddleOCR-VL 的多语言数据都需要标注成本与许可；这些是 `L1`，不是模型自发发现。
3. **合成数据的物理地位不同。** 合成图像/文档可提供精确真值与可控版式，但不是观测到的真实物理证据；sim-to-real 差距必须单独测。
4. **RLVR 的奖励是代理。** olmOCR 2 的二元单元测试、When Trackers Fail 的失败检测奖励、SAM3RL 的追踪奖励，都只覆盖被测试的性质；奖励漏洞会变成能力假象。
5. **训练配方可与架构混淆。** YOLO26 同时改双头、去 DFL、MuSGD、Progressive Loss、STAL；DEIM 改匹配与损失；D-FINE 改回归表示与自蒸馏；RF-DETR 改 NAS。不能把联合收益写成单一模块的创新。

### 失败导向数据：部署分布本身是一种监督

- **When Trackers Fail** 在真实 SAM3 传播轨迹上挖掘失败，按失败类型过采样，训练验证/纠正器；这使监督分布接近部署时会遇到的错误，而不是 oracle 轨迹。作者同时指出：错误纠正会覆盖正确轨迹，门控无形式安全保证。
- **TAPNext++** 用 1024 帧长序列、periodic roll 与遮挡点监督改善重现；这是把“长时/重入”写进训练分布，而不是只改推理。
- **MOTIP2** 用空间 ID 交换/距离加权/位置锚点把“空间上不可能的 ID 跳变”写进数据、损失与表示；作者也给出其失败条件（同位置同时离开/进入）。
- **SAMURAI / SAM3RL** 代表两条不同路线：前者不改权重、用运动先验修正记忆选择；后者用 RL 学习记忆控制。两者都说明“记忆管理”是可独立研究的变量，而不是骨干的附属品。

**对 Clover 的可检验预测：** 若纯视觉路线成立，则在**匹配数据、模型规模与评测协议**后，视觉自监督应在识别/定位/密集特征上追平语言监督；但在文字定义的新概念、开放词汇关系、需要语言知识的任务上，除非视觉经验覆盖，否则仍应落后。这个“任务分层预测”比“纯视觉能否 AGI”这一笼统问题更容易被实验证伪。

### 数据与评测污染：必须主动审计

- **预训练-评测重叠不可核对：** When Trackers Fail 作者明确无法验证基础模型预训练数据与评测视频的重叠；这类不确定性应默认存在，而不是默认干净。
- **基准版本漂移：** OmniDocBench 已从 v1.6 转到 v1.7；PaddleOCR-VL/dots.ocr/PolyOCR 各自使用不同版本与内部集，跨论文分数不能直接排序。
- **内部基准与自建基准：** PaddleOCR-VL 的图表/公式集、UniCounting 的 COCO clean500、TAPVid-MV 的真值辅助模态，都是作者构造；需要独立复现与第三方评测。
- **数据引擎的可复现性：** SAM 3/SAM 3D/olmOCR 2 的数据引擎规模大，公开权重不等于公开全部数据与筛选管线；“开放”程度须逐项登记。

**本节结论：** 当前证据不支持“纯视觉自监督已经全面替代语言监督”，也不支持“语言监督是唯一出路”。更准确的现状是：**在匹配数据与规模时，视觉自监督可以追平部分识别/密集特征；但在开放词汇、文字、关系和知识密集任务上，语言/教师/数据引擎仍是强来源。** Clover 的纯视觉主张必须按任务分层、按来源记账、按数据重叠审计，才能成为可证伪的科学纲领。
<!-- END learning-provenance-frontier -->


<!-- BEGIN broad-vision-primary-evidence -->
<a id="broad-vision-primary-evidence"></a>

## 广义视觉理解的一手比较证据

核验日：2026-10-25。以下是外部方法与反例，覆盖经典接口、当前基础视觉与跨领域条件；未被采纳为 Clover 架构。

### SigLIP 2

- **一手来源：** [固定版本](https://arxiv.org/abs/2502.14786v1) · [作者资源](https://github.com/google-research/big_vision/tree/main/big_vision/configs/proj/image_text)。
- **机制：** 视觉语言预训练结合自监督、定位及密集特征目标，提供多种图像编码器。
- **输入与学习来源：** 图文数据与描述/教师等训练成分 L2，辅以视觉自监督；按 checkpoint 区分配方。
- **实际证据：** 分类、检索、定位及密集特征迁移的表示参照。
- **边界与反假设：** 图文零样本识别与视觉自监督探针不是同一知识条件；强编码器不是自带全部任务输出或长期状态。
- **阅读深度：** 正文选读：训练目标与模型发布说明；未复核全部实验；未运行复现。

### LingBot-VA

- **一手来源：** [正式会议记录](https://www.roboticsproceedings.org/rss22/p016.html) · [论文](http://www.roboticsproceedings.org/rss22/p016.pdf)。
- **机制：** 自回归视频–动作混合 Transformer、历史 KV 与中间去噪动作解码联合建模。
- **输入与学习来源：** 互联网/机器人视频、语言任务和动作经验，含 L2/L3，其他传感按具体设置登记。
- **实际证据：** 视频–动作预测与模拟/真实操作，是连续接入观测的一种比较方向。
- **边界与反假设：** 文中 causal 首先指时间因果掩码；未因此证明物理干预可识别。KV 历史也不能直接当长期可修正世界记忆。
- **阅读深度：** 正文建模/编码与训练说明选读；未复核全部实验；未运行复现。
<!-- END broad-vision-primary-evidence -->

<!-- BEGIN broad-visual-learning -->
<a id="broad-visual-learning"></a>

## 广义视觉能力的学习来源与共同训练问题

核心视觉能力必须进入训练调研；“纯视觉”应同时说明观测通道和知识来源。文字位于图像中仍是视觉观测，但转写标注、描述、语言教师和外部物理真值不能混成一种监督。

| 学习证据 | 能支持的比较 | 必须公开的来源边界 |
|---|---|---|
| 图像自监督 | 通用特征、密集/分类迁移及无标签学习 | 预训练 L0 与有标签 probe/head 的 L1 分开；强特征不等于已学会每项功能 |
| 类别/框/掩码/关键点/文字转写 | 识别、定位、分割、姿态、OCR | 视觉标注 L1，标注本体/质量、稀有类及像素边界；转写与外部世界知识 L2 不同 |
| 图文、描述、指令与 VLM 教师 | 开放词汇、指代表达、统一任务和推理 | L2 的语义/世界知识不得归因给纯视觉经验；教师模型/提示/自标注与验证器分开 |
| 合成几何/轨迹与遮挡真值 | 运动/姿态/追踪与可见性学习 | 非视觉真值 L4 与真实无标签微调分开；合成运动/渲染覆盖、长短序列与未来帧泄漏 |
| 动作示范/交互经验 | 主动观察、动作后果与可供性 | L3 与可能的本体/力/深度 L4 分开；机器人回报不替代通用视觉功能保持 |
| 多任务 SFT/RL/蒸馏 | 研究共享表示、任务竞争与低计算输出 | 同模型权重/同架构/分开微调三种证据分别登记；教师数据、奖励和计算预算配平 |

优先比较：①共享训练对识别/分割/追踪/OCR的正负迁移；②基础感知增强后一般推理、长期记忆与校准是否退化；③合成轨迹长序列收益与循环架构收益；④空间/时间/身份标注与弱标签的取舍；⑤不同输出编码造成的速度/精度差异。WeVisOne-VL 的通用能力局限、OneFormer 的单权重多分割与 Mask2Former 的通用架构是三个不同证据，不能并写成“统一视觉已解决”。

数据分割至少按原图/原视频、实体身份、场景和采集来源去重；连续帧、裁剪、教师生成的重复标注不得跨训练/测试制造捷径。后续以未见类别、关系、任务组合、退化条件和新历史需求来检验广义理解；不因某种数据难收而删除对应能力目标。本节是研究维度，没有冻结训练配方。
<!-- END broad-visual-learning -->

<!-- BEGIN distribution-shift -->
<a id="distribution-shift-2026"></a>

## 分布偏移、检验点选择与持续适应

真实部署的失败往往不是“训练集不够大”，而是**训练分布与部署分布不一致**：新医院、新城市、新传感器、新天气、新设备。2026 年这一方向出现三条互相独立的证据线：**数据侧**（多样性/合成/颜色增强）、**选择侧**（checkpoint/校准，不重训）、**在线适应侧**（TTA/持续 TTA）。本轮补 10 篇，重点不是再提一个 adapter，而是分清“什么在偏移下真的保留”。

| 方法 | 一手来源 | 机制与可核查证据 | 边界与反假设 |
|---|---|---|---|
| Reliability-Aware Checkpoint Selection | [2609.39934](https://arxiv.org/abs/2609.39934v2) · [项目页](https://github.com/Jjjjjjh666/Reliability-Aware-DG) · 正文选读 | 指出 DG 常用 source-val 准确率选 checkpoint，但同轨迹中近最优准确率的 checkpoint 在目标域概率质量可不同；AC 规则在最优 source 准确率容差内按 source reliability 重选；PACS/OfficeHome/TerraIncognita 540 runs：ECE −0.2395 [−0.4038,−0.0903]、CwECE −0.1821、NLL −0.0295，准确率 +0.2133 pp 但 CI 跨 0；118/540 选点损失目标准确率；SWAD 在独立 OfficeHome rerun 上准确率/校准均更好 | 只重选固定训练轨迹，不改变训练；source reliability 与 target 概率质量仍非同一量；准确率不保证；容差/聚合规则未定；SWAD 反例说明“选择”不是万能；不是在线适应 |
| DG + Synthetic Data in Detection | [2610.00030](https://arxiv.org/abs/2610.00030v1) · 正文选读 | 目标检测 DG 综述：合成数据可作 enabler（扩充多样性/对齐）、probe（受控偏移诊断）、以及 synthetic-to-real gap 的来源；结论：增加多样性常比增加真实感更有效；少量真实数据可显著改善合成到真实迁移；分类 DG 方法不能直接迁移到检测（定位+分类双误差） | 综述无新实验；检测的域偏移同时影响定位/分类；合成数据可能引入 shortcut；真实数据需求仍存在；不是具体方法；不覆盖视频/开放世界 |
| Colorist / Statistical Color Matching | [2608.18915](https://arxiv.org/abs/2608.18915v2)（DEMI@MICCAI 2026） · 正文选读 | 训练-free 的 RGB 全局均值-标准差颜色匹配作为数据增强；19 个医学数据集；协变量偏移下 balanced accuracy 0.3953→0.5438（+0.148），30% 应用概率最佳；同分布仅 +0.008；作者报告结构保真优于生成式风格迁移，且计算/能耗更低 | 只建模光度偏移，不解决几何/分辨率/解剖差异；多类不平衡基准仍弱；医学域特定；不是表示学习；颜色统计匹配可能抹除诊断色差 |
| Zero-Shot DG via Domain Prompt Learning | [2610.30680](https://arxiv.org/abs/2610.30680v1)（IJCV） · 摘要 | 不访问 source 数据，用 CLIP 文本/视觉 prompt 学习目标域知识，实现未见类/未见域零样本 DG | 摘要级；依赖 CLIP/语言先验；prompt 选择与目标域估计；不是纯视觉；未给跨数据集全表 |
| GATE | [2608.29395](https://arxiv.org/abs/2608.29395v1)（BMVC 2026） · 摘要 | 训练-free 两遍 transductive TTA：冻结图像/文本编码器与 prompt，用文本高斯 + 视觉高斯证据融合，按可靠性门控 | 摘要级；需要未标注目标集（transductive）；CLIP/SigLIP 特定；不是生成式 MLLM；门控阈值/校准未核 |
| RADC | [2610.06932](https://arxiv.org/abs/2610.06932v1) · 摘要 | VLM TTA 双缓存：语义前景缓存聚合类别一致空间证据，高斯风险准入联合类分离/特征不确定性筛选可靠样本 | 摘要级；依赖 CLIP 表示；背景偏差/缓存污染仍有风险；不是 MLLM 生成式；未给跨数据集全表 |
| Continual TTA Survey | [2607.08164](https://arxiv.org/abs/2607.08164v3)（TMLR 2026） · 摘要 | 持续测试时适应综述：形式化非平稳目标分布、灾难遗忘与伪标签误差累积；提出层次分类与 benchmark 协议 | 综述不提供新方法；协议/指标未统一；真实部署的长尾/计算约束未解；不是纯视觉 |
| Limits of Representation TTA for MLLMs | [2610.19892](https://arxiv.org/abs/2610.19892v1)（NeurIPS 2026 workshop） · 摘要 | 负结果：CLIP 类对比模型上有效的 representation-based TTA，在生成式 MLLM 上几乎不能恢复腐蚀性能；即使离线用目标数据做 sample-blind 特征对齐，收益也边际；原因是腐蚀偏移在生成式模型中不呈共享的单一分类域方向 | 摘要级；特定 MLLM/腐蚀协议；不是所有 TTA 都无效；说明 CLIP TTA 结论不能直接迁移到生成式模型；未给通用替代方案 |
| Geographic Diversity JEPA | [2607.04500](https://arxiv.org/abs/2607.04500v1) · 正文选读 | 零标签 JEPA 驾驶世界模型：nuPlan 多城市 vs 单地理训练，零样本评估 Argoverse2 Miami/Austin；63K 多地理组合 surprise 0.228±0.015 vs 63K 单地理 0.273±0.008（−16.5%，p<0.05）；200K 单地理 AV2-only 仍 0.264；作者结论：地理多样性比数据量更能预测跨域泛化 | 驾驶场景/结构化 agent 状态，不是像素世界模型；AV2-only 为单 seed（训练不稳）；surprise 是代理指标，不是规划安全；地理多样性不是万能；未覆盖传感器大偏移 |
| FORGE | [2609.01683](https://arxiv.org/abs/2609.01683v1)（TMLR 2026） · [代码](https://github.com/Rehan000/forge-tta) · 摘要 | 面向微控制器 integer-only、BN-folded 模型的前向-only TTA；不依赖反向传播/BN 统计，在部署运行时做偏移适应 | 摘要级；MCU 量化/算子限制；任务/传感器范围有限；不是通用 TTA；能效/精度权衡未核 |

### Checkpoint Selection：source-val 选点会骗你，校准与准确率不是一回事

DG 的常见做法是用 source validation accuracy 选 checkpoint；这篇工作指出：在同一条训练轨迹上，多个 checkpoint 的 source accuracy 可以几乎相同，但目标域的概率质量（ECE/CwECE/NLL）不同。它在 540 个 runs 上重选 checkpoint：ECE −0.2395、CwECE −0.1821、NLL −0.0295，三个区间都低于 0；但准确率 +0.2133 pp 的区间跨 0，且 118/540 个选择损失目标准确率。更刺眼的是，独立 OfficeHome rerun 中 checkpoint-SWAD 的准确率（62.62% vs 60.97%）和三个可靠性误差都更好。

它给 Clover 的启发是：**“模型选择”本身是分布偏移下的一个独立变量**；source-val 最优不等于 target 可靠，校准提升也不等于准确率提升。Clover 的验收必须同时报告 source 选点规则、target 校准与 target 准确率，不能只报一个“最佳 checkpoint”的分数。

### Synthetic Data 与 Colorist：多样性常比真实感更重要，简单基线不能省略

目标检测 DG 综述把合成数据分成三种角色：enabler（扩充多样性/对齐）、probe（受控偏移诊断）、以及 synthetic-to-real gap 的来源。它的核心结论是：**增加多样性往往比增加真实感更有效**；少量真实数据可以显著改善合成到真实迁移；分类 DG 方法不能直接迁移到检测，因为检测的偏移同时作用于定位与分类。

Colorist 则给出一个极简反例：训练-free 的 RGB 全局均值-标准差颜色匹配，在 19 个医学数据集上把协变量偏移下的 balanced accuracy 从 0.3953 提到 0.5438（+0.148），同分布只 +0.008；作者报告结构保真优于生成式风格迁移，计算/能耗更低。它说明：**在光度偏移上，简单的、可解释的、结构保真的增强可以打败复杂生成模型**；但颜色匹配不解决几何/分辨率/解剖差异，多类不平衡基准仍弱。

对 Clover 的启发是：数据侧增益要先排除“简单基线”，并报告增益来自多样性、真实感还是结构保真；合成数据必须同时作为训练数据和诊断探针，不能只当扩容。

### GATE、RADC 与持续 TTA：在线适应有收益，但边界比论文标题窄

GATE 与 RADC 都走 VLM 的 training-free TTA：GATE 用文本高斯 + 视觉高斯证据、冻结编码器与 prompt；RADC 用语义前景缓存 + 高斯风险准入筛可靠样本。它们的共同主张是：不需要 source 数据/标签，也能在目标域提升 CLIP/SigLIP 的鲁棒性。

但持续 TTA 综述指出两个结构性失败：**灾难遗忘**与**伪标签误差累积**；非平稳目标分布下，适应会越走越偏。更关键的是“Limits of Representation TTA for MLLMs”给出负结果：CLIP 类对比模型上有效的 representation-based TTA，在生成式 MLLM 上几乎不能恢复腐蚀性能；即使离线用目标数据做 sample-blind 特征对齐，收益也边际。原因是生成式模型的腐蚀偏移不呈共享的单一分类域方向。

这三篇合起来说明：**TTA 不是“无标签就免费变强”**；CLIP 的 TTA 结论不能直接迁移到生成式 MLLM，持续偏移下的遗忘/误差累积仍未解，transductive 设定还需要目标集。Clover 若用 TTA，必须报告 source-free/transductive 条件、遗忘曲线、伪标签误差与计算开销。

### Geographic Diversity JEPA 与 FORGE：多样性 vs 数据量，云端 vs 微控制器

Geographic JEPA 用零标签驾驶世界模型做受控迁移：63K 多地理组合的 AV2 surprise 0.228±0.015，优于 63K 单地理 0.273±0.008（−16.5%，p<0.05）；200K 单地理 AV2-only 仍 0.264。作者结论是地理多样性比数据量更能预测跨域泛化；但 AV2-only 是单 seed、surprise 只是代理指标、场景是结构化 agent 状态而非像素。

FORGE 把 TTA 推到另一个极端：微控制器上的 integer-only、BN-folded 模型，只能前向传播；它不依赖反向传播/BN 统计，在部署运行时做偏移适应。它的边界是 MCU 量化/算子限制、任务/传感器范围有限；但这条线对 Clover 的“原生 ultrafast”很关键：**适应必须能在端侧、无标签、无反向传播的条件下发生**，否则“在线适应”只是服务器特权。

**本节结论：** 分布偏移的 2026 证据分成三层：**数据侧**（多样性/合成/颜色增强）、**选择侧**（checkpoint/校准，不重训）、**在线适应侧**（TTA/持续 TTA）。三层的共同结论是：简单基线不能省略（Colorist 打败生成式风格迁移）；source-val 选点会误导（checkpoint selection 校准升、准确率不保证）；TTA 的收益有模型族边界（CLIP 有效、生成式 MLLM 失败）；持续偏移的遗忘/误差累积仍未解；端侧适应需要前向-only/整数算子。Clover 若声称“在真实世界可靠”，必须分别报告：目标域校准/准确率、source-free 条件、遗忘曲线、伪标签误差、端侧计算/能耗；单一“TTA 提升”或“合成数据扩容”不能替代这些证据。
<!-- END distribution-shift -->

## Contents

- [Learning Provenance Frontier: Pure Vision, Language, Teachers and Failure Data](#learning-provenance-frontier)
- [Distribution Shift, Checkpoint Selection and Continual Adaptation](#distribution-shift-2026)
- [Pure-Vision Claim Audit: V0–V3 × L0–L4](#pure-vision-provenance-audit)
- [Training, Post-Training and Embodied Learning Regimes](#topic-research-research_training_posttraining)
- [Training / Post-Training — Supporting Stage-1 Matrix](#topic-research-training-readme)
- [Training / Post-Training — High-Risk Boundary Questions](#topic-research-training-high_risk_boundaries)
- [Data, Experience and Interaction](#topic-docs-research-map-data-and-experience)
- [Lifelong Learning and World Growth](#topic-docs-research-map-lifelong-learning)

<a id="topic-research-research_training_posttraining"></a>

## Training, Post-Training and Embodied Learning Regimes

Source record updated: **2026-10-15**
Source intake checked through: **2026-10-15**

> **Research question:** How can a machine understand the real world through vision alone?

This is a Stage-1 research document. It does **not** choose a Clover training recipe.

Its purpose is to make one missing variable explicit:

```text
same architecture
+ different data / objective / update scope / interaction regime
→ potentially very different capability
```

For modern foundation models and robot policies, training procedure is not merely an implementation detail. It can determine what information is preserved, what behavior is preferred, how well the model generalizes, whether old capabilities are forgotten, and whether the deployed policy survives its own state distribution.

---

### 1. Keep model architecture separate from training regime

Record separately:

```text
base architecture
pretraining objective
pretraining data mixture
continued pretraining
supervised fine-tuning / behavior cloning
preference optimization
reinforcement learning
on-policy / off-policy data
knowledge distillation
world-model / simulator post-training
deployment-rollout learning
continual / test-time adaptation
```

Do not conclude that an architectural component caused a gain if the compared systems also changed training data, objective, update scope, reward source or deployment interaction.

---

### 2. A useful training-regime taxonomy

#### TR0 — base pretraining

Examples:

```text
next-token prediction
masked / predictive representation learning
vision-language pretraining
video prediction
world-model prediction
```

Question: what broad prior is acquired before task-specific robot supervision?

#### TR1 — continued / domain-adaptive pretraining

Continue training on a narrower domain before task-specific adaptation.

Examples:

```text
robot video
human manipulation video
egocentric video
physical reasoning data
long-context / long-video data
```

Risk: domain specialization can improve downstream transfer while eroding unrelated capabilities.

#### TR2 — supervised post-training / behavior cloning

For LLM/VLM:

```text
instruction SFT
multimodal SFT
CoT cold start
```

For robots:

```text
observation + instruction + action demonstration
→ supervised action prediction
```

Robot behavior cloning is analogous to SFT only at a high level. Robot actions alter the future state distribution, so deployment can rapidly leave the demonstration distribution.

#### TR3 — co-training / auxiliary-objective training

Examples:

```text
VLM + VLA co-training
language supervision + actions
future latent prediction + actions
geometry / depth / pose auxiliaries
world-model + policy joint objectives
```

These signals can change representation quality even when architecture stays fixed.

#### TR4 — preference / conservative offline alignment

Examples include:

```text
preference optimization
sample reweighting
quality filtering
posterior / transition attribution
```

Useful when recorded data contain conflicting or suboptimal supervision.

#### TR5 — reinforcement learning with verifiable or learned rewards

For general models this may use:

```text
rule/verifier rewards
preference reward models
tool / environment outcomes
```

For robots it may use:

```text
task success
progress
collision / force / safety penalties
world-model or VLM-generated rewards
```

Reward design becomes part of the scientific claim.

#### TR6 — online embodied reinforcement learning

The current policy acts, changes the world, and learns from its own state distribution.

This can correct covariate shift but is expensive, safety-sensitive and reset-limited in the real world.

#### TR7 — on-policy distillation / teacher-guided self-generated trajectories

The student visits states induced by its own policy while a teacher supplies denser supervision.

This can bridge offline SFT and expensive sparse-reward RL, but teacher errors and epistemic uncertainty become part of the evidence chain.

#### TR8 — strong-to-weak / model distillation

Transfer capability from a larger teacher into a smaller model.

Important question for Clover:

```text
what survives distillation?
```

Measure not only task accuracy but memory, uncertainty, persistence, physical reasoning and rare-event behavior.

#### TR9 — simulated / world-model post-training

Use a simulator or learned world model for exploration, RL or rehearsal.

Important distinction:

```text
learning to exploit simulator/world-model errors
≠ learning correct real-world behavior
```

#### TR10 — deployment-rollout learning / self-improvement

Use successful, failed and suboptimal deployment trajectories for further training.

This includes failure mining, active data collection and repeated deployment→training cycles.

#### TR11 — continual / test-time adaptation

Update after deployment as environment, robot body, sensors or task distribution changes.

Must be evaluated together with forgetting, rollback and persistent-state compatibility.

These labels are bookkeeping tools, not a Clover training plan.

---

### 3. General LLM / VLM post-training: current lessons

#### DeepSeek-R1 — RL can create capability, but raw RL has behavioral failure modes

Primary paper: https://arxiv.org/abs/2501.12948
Official code: https://github.com/deepseek-ai/DeepSeek-R1

DeepSeek-R1-Zero applies large-scale RL directly to a base model without preliminary SFT and reports emergent reasoning behavior. The same line also reports practical problems such as repetition, poor readability and language mixing. DeepSeek-R1 introduces cold-start data and multi-stage training before/around RL.

Stage-1 lesson:

```text
RL can improve a target capability
without automatically producing desirable overall behavior.
```

The initialization / cold-start distribution matters.

#### DeepSeek-V4.1-Flash — data-pipeline changes can dominate algorithmic changes

Official release: https://www.deepseek.com/en/news/deepseek-v4-1-flash/
Model / technical material: https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash

The released description uses:

```text
SFT
→ RL
→ on-policy distillation
```

and states that substantive post-training changes are concentrated in large-scale automatic synthesis of agent tasks/environments plus progressive scaling of tasks and rollouts rather than a new RL algorithm.

Stage-1 lesson:

```text
post-training algorithm
≠ post-training data pipeline
```

Both must be reported.

#### Qwen3 — staged post-training deliberately installs different behavior modes

Official overview: https://qwenlm.github.io/blog/qwen3/
Technical report: https://arxiv.org/abs/2505.09388

The flagship Qwen3 pipeline uses four stages:

```text
long-CoT cold-start SFT
→ reasoning RL
→ thinking / non-thinking fusion
→ general-domain RL
```

Smaller models use strong-to-weak distillation to avoid reproducing the full expensive pipeline.

Stage-1 lesson:

> “post-training” is not one operation. Different stages can install reasoning style, combine behavioral modes, align preferences and transfer capability to smaller models.

#### Qwen3-VL — multimodal post-training must preserve perception while improving reasoning

Primary paper: https://arxiv.org/abs/2511.21631

The released post-training recipe includes supervised fine-tuning, strong-to-weak distillation and reinforcement learning across text and multimodal domains, including grounding and tool-integrated visual reasoning.

A useful 2026 boundary result is:

- Text-Centric Post-Training for Omni-Modal Reasoning — https://arxiv.org/abs/2610.02819

It reports that text-only reasoning post-training can substantially improve multimodal reasoning while degrading perception, and that a smaller native audio-visual RL refinement can recover perception while retaining most reasoning gains.

Stage-1 lesson:

```text
reasoning improvement
≠ perception preservation
```

A post-training objective can create cross-capability interference.

---

### 4. Robot training is only partially analogous to LLM post-training

Common high-level structure:

```text
large general prior
→ specialization
→ feedback / correction
→ deployment
```

But the learning problem is materially different.

#### Language-model output

```text
token
```

An incorrect token usually does not physically alter the next input distribution.

#### Robot-policy output

```text
continuous / discretized action
→ changes physical world
→ changes camera evidence
→ changes future reachable states
```

Therefore robot post-training must handle:

```text
covariate shift
continuous multimodal actions
control frequency / latency
embodiment-specific semantics
costly real-world resets
sparse / delayed reward
safety and irreversible actions
contact dynamics
hardware drift
human teleoperation quality
sim2real mismatch
```

So:

```text
LLM SFT → RL recipe
≠ directly reusable robot recipe
```

---

### 5. Major robot-policy training families

#### 5.1 Behavior cloning / imitation learning

Learn recorded expert actions from demonstrations.

Strengths:

```text
stable
simple
uses offline data
safe compared with online exploration
```

Weaknesses:

```text
policy-induced distribution shift
recovery states underrepresented
operator inconsistency
suboptimal demonstrations
```

Classical examples include ACT-style action chunking and Diffusion Policy.

Diffusion Policy: https://arxiv.org/abs/2303.04137

#### 5.2 Action representation and decoding objective are training variables

OpenVLA-OFT: https://arxiv.org/abs/2502.19645

Under an OpenVLA backbone, changing fine-tuning design — parallel decoding, action chunking, continuous actions and an L1 objective — materially changes both task success and inference speed.

Stage-1 lesson:

```text
backbone quality
≠ downstream policy quality
```

Action representation and decoding loss can dominate adaptation.

#### 5.3 Flow / diffusion action experts

π0 uses a pretrained VLM plus a continuous action expert trained with flow matching.

Official overview: https://www.physicalintelligence.company/blog/pi0
Paper: https://www.physicalintelligence.company/download/pi0.pdf

The system combines internet-scale visual-language pretraining, cross-embodiment robot data and later high-quality task post-training.

π0.5 adds a two-stage structure in which pretraining uses discrete-token tasks and post-training introduces a finer-grained action expert for mobile manipulation and efficient real-time control.

π0.5 paper: https://www.physicalintelligence.company/download/pi05.pdf

Important distinction:

```text
semantic pretraining
≠ motor post-training
```

#### 5.4 Cross-embodiment co-training requires alignment

Open X-Embodiment / RT-X: https://arxiv.org/abs/2310.08864

Qwen-RobotManip: https://arxiv.org/abs/2606.17846
Official overview: https://qwen.ai/blog?id=qwen-robotmanip

Qwen-RobotManip uses:

```text
Qwen3.5-4B VLM backbone
+
flow-matching DiT action head
```

with a canonical 80-dimensional state/action space, camera-frame delta poses, camera calibration information and in-context embodiment conditioning.

Reported training structure:

```text
pretraining:
VLA robot stream + VLM stream
≈ 9:1

post-training:
generalist supervised fine-tuning on demonstration data
+ VLM/VLA co-training
```

The work argues that representation, motion and behavior alignment are prerequisites for useful data scaling across embodiments.

Stage-1 lesson:

```text
more heterogeneous robot data
≠ automatically better
```

Data must have compatible state/action semantics.

#### 5.5 Human-video / latent-action pretraining

LAPA: https://arxiv.org/abs/2410.11758
ConLA: https://arxiv.org/abs/2602.00557
HARP-VLA: https://arxiv.org/abs/2605.31234
HuRo: https://arxiv.org/abs/2609.10706
JALA: https://openaccess.thecvf.com/content/CVPR2026/html/Luo_Joint-Aligned_Latent_Action_Towards_Scalable_VLA_Pretraining_in_the_Wild_CVPR_2026_paper.html

These approaches try to exploit large human-video corpora by learning latent actions, aligning human/robot representations, or converting human trajectories into robot-compatible observations/actions.

Main risks:

```text
human hand dynamics ≠ robot dynamics
visual similarity ≠ executable action equivalence
retargeted action ≠ measured robot action
synthetic robotization errors can become supervision
```

Record synthetic / inferred action provenance explicitly.

#### 5.6 Synthetic-data / simulation pretraining

NVIDIA GR00T N1 / N1.7 uses mixtures of human/egocentric, synthetic/simulation and real robot data.

Official training overview: https://developer.nvidia.com/blog/accelerate-generalist-humanoid-robot-development-with-nvidia-isaac-gr00t-n1/
N1.7 overview: https://developer.nvidia.com/blog/develop-humanoid-robot-policies-end-to-end-with-nvidia-isaac-gr00t/

N1.7 is reported as pretrained on roughly 32K hours of real demonstration/human egocentric data plus roughly 8K hours of simulated rollouts/demonstrations, followed by robot-specific post-training workflows.

Important question:

> Which gains come from data quantity, which from embodiment alignment, and which from simulator-specific structure?

#### 5.7 Offline post-training on heterogeneous robot data

Posterior-Transition Reweighting: https://arxiv.org/abs/2603.16542

This work treats recorded robot demonstrations as unequal supervision and reweights samples according to how attributable the observed post-action consequence is under the current representation.

Ambient Diffusion Policy: https://arxiv.org/abs/2606.12365

This work studies how suboptimal data should contribute differently at different diffusion noise levels.

Stage-1 lesson:

```text
all demonstrations equally weighted
```

is itself a training assumption.

#### 5.8 Online RL post-training

Robot RL can move a policy beyond demonstration behavior, but interaction is expensive and dangerous.

Examples:

- VLA navigation GRPO fine-tuning — https://arxiv.org/abs/2603.12868
- LaST-R1 — https://arxiv.org/abs/2604.28192
- PAC-ACT — https://arxiv.org/abs/2607.09590
- TEMPO — https://arxiv.org/abs/2608.07314
- VLA-Precision — https://arxiv.org/abs/2609.04355

TEMPO is especially useful conceptually because it updates semantic and low-level action components at different rates rather than treating the whole VLA as one homogeneous policy.

Stage-1 lesson:

```text
which parameters are updated
```

is a first-class post-training variable.

#### 5.9 On-policy distillation as a bridge between SFT and RL

VLA-OPD: https://arxiv.org/abs/2603.26666

The student visits states generated by its own policy while an expert teacher gives dense supervision. The paper explicitly frames the problem as a trade-off:

```text
offline SFT
→ efficient but distribution-shift / forgetting risk

online RL
→ on-policy but sparse-reward / sample-efficiency problems
```

On-policy distillation tries to combine on-policy state coverage with dense teacher signals.

#### 5.10 Simulated / world-model RL post-training

RehearseVLA: https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_RehearseVLA_Simulated_Post-Training_for_VLAs_with_Physically-Consistent_World_Model_CVPR_2026_paper.html

The method performs RL-style post-training inside a learned physical world simulator to avoid expensive/non-resettable real interaction.

Important danger:

```text
world-model bias
→ reward / exploration bias
→ policy learns simulator artifact
```

This must be followed by EV3–EV8 evidence rather than treated as real-world RL.

#### 5.11 Deployment self-improvement / failure learning

LoopWAM: https://arxiv.org/abs/2610.18873

RoboCat historical reference: https://deepmind.google/blog/robocat-a-self-improving-robotic-agent

ENPIRE: https://arxiv.org/abs/2606.19980

This family uses policy failures, suboptimal deployment rollouts, autonomous data collection or agent-guided training loops to improve subsequent models.

Important distinction:

```text
self-improvement
≠ safe improvement
≠ monotonic improvement
≠ unbiased data collection
```

---

### 6. Controlled evidence that training objective changes representation

#### VLAFlow

Paper: https://arxiv.org/abs/2607.01586

VLAFlow fixes a π0-style architecture, shared VLM backbone, action expert and 14-dimensional action space, then compares four training signals on the same heterogeneous robot corpus:

```text
action-only
language-supervised co-training
future-latent alignment
language + future-latent combination
```

Reported conclusion:

- action-only pretraining is sensitive to heterogeneous data;
- language supervision better preserves vision-language generalization;
- future latent alignment improves transition/action-outcome modeling;
- combining both provides the most stable overall transfer across the reported benchmarks.

This is especially valuable to Clover because it isolates **objective choice** more cleanly than comparing unrelated model families.

---

### 7. Post-training can improve one capability while damaging another

Track at least these failure modes:

#### PT-F1 — catastrophic forgetting

Task/robot fine-tuning erases broad pretrained semantic or physical capability.

#### PT-F2 — reward overoptimization / reward hacking

RL improves the training reward without improving the intended real-world capability.

#### PT-F3 — perception-reasoning interference

Reasoning tuning improves inference but weakens visual perception or grounding.

#### PT-F4 — action-mode collapse

Fine-tuning narrows a useful multimodal action distribution into one brittle strategy.

#### PT-F5 — unsafe exploration

Online RL visits dangerous or irreversible states.

#### PT-F6 — simulator exploitation

World-model/simulator post-training discovers artifacts rather than real physics.

#### PT-F7 — embodiment over-specialization

Target-robot fine-tuning reduces cross-embodiment transfer.

#### PT-F8 — calibration loss

Post-training produces more confident behavior without better epistemic calibration.

#### PT-F9 — memory / state regression

Task success improves while persistence, belief revision or long-horizon world state degrades.

#### PT-F10 — deployment-data feedback bias

Self-training increasingly samples states created by the current policy and can reinforce blind spots.

---

### 8. Required training provenance for future Clover comparisons

For every serious baseline or experiment record:

```text
base checkpoint
architecture revision
pretraining corpus / source classes
pretraining objective
continued-pretraining data
post-training stages and order
objective per stage
data per stage
real / synthetic / human-video / robot-data ratio
on-policy vs off-policy
reward source / verifier
teacher model if distilled
what parameters are frozen / updated
learning rate / update ratio where material
action representation
control frequency / chunk size
history/context supplied
simulator or real environment used for training
failure / recovery data included?
privileged state / force / depth / tactile used?
checkpoint selected by which metric?
```

Without this record, architecture comparisons are confounded.

---

### 9. A useful controlled training-ablation matrix for Clover

For a fixed backbone and matched data budget, later compare:

```text
A  supervised behavior cloning only
B  A + VLM co-training
C  A + future-state / world-model auxiliary
D  A + strong-to-weak distillation
E  A + on-policy teacher distillation
F  A + simulated RL
G  A + real/proxy online RL
H  A + deployment failure/recovery data
```

Also cross with update scope:

```text
freeze visual/VLM backbone
adapter / LoRA only
projection + action head
upper backbone + action head
full model
```

And measure a capability vector rather than success alone:

```text
task success
OOD scene/object/task transfer
cross-embodiment transfer
recovery
physical consistency
uncertainty calibration
persistent memory
state aliasing
long-horizon reliability
latency / memory
catastrophic forgetting
```

---

### 10. Mac mini M4 implication

The current machine is suitable for controlled small-model/post-training experiments such as:

```text
small Qwen/VLM backbone
frozen-backbone + action/state head
LoRA / adapter tuning
offline behavior cloning
flow/diffusion action-head experiments
small MuJoCo RL
teacher distillation experiments
objective / data-mixture ablations
quantized post-training inference tests
```

Do not use the inability to reproduce frontier-scale RL locally as a reason to skip training-regime research.

Use small controlled proxies first, then validate important effects on remote larger checkpoints when necessary.

Critical rule:

```text
effect observed on 4B proxy
≠ automatically valid on frontier MoE
```

Scaling validation remains required.

---

### 11. Current open questions

Continue collecting evidence for:

```text
Which post-training stages improve physical reasoning rather than linguistic reasoning only?
When should the VLM/world-state backbone be frozen during robot adaptation?
Can RL improve action robustness without corrupting semantic/world-state representations?
How should reward signals represent uncertainty, safety and partial success?
How should failed/recovery trajectories be sampled relative to expert successes?
What real/sim/human-video mixture best preserves OOD physical transfer?
Can on-policy distillation preserve uncertainty better than hard imitation?
When does future-state auxiliary training improve actual control?
How much world-model capability survives policy distillation?
How does quantization interact with post-trained behavior?
How should continual robot learning rollback persistent state when model weights roll back?
How should synthetic-data provenance affect sample weighting?
What training objectives preserve `S-OPEN` future-task optionality instead of only `S-CTRL`?
```

---

### 12. Stage-2 analysis priority created by this surface

When Stage 2 starts, explicitly compare these training-regime clusters:

```text
DeepSeek-R1 / V4.1 post-training
Qwen3 / Qwen3-VL post-training
π0 / π0.5
OpenVLA-OFT
Qwen-RobotManip
GR00T N1.7
VLAFlow
VLA-OPD
TEMPO / online RL variants
RehearseVLA
LoopWAM / deployment self-improvement
human-video latent-action pretraining: LAPA / HARP / HuRo / JALA
```

The objective is not to find one universally best recipe. The objective is to identify which learning regime preserves which capability under which evidence and deployment constraints.

---

### Final rule

```text
architecture
× data
× objective
× update scope
× interaction regime
× runtime
→ observed capability
```

Do not attribute the result to architecture alone.

---

<a id="topic-research-training-readme"></a>

## Training / Post-Training — Supporting Stage-1 Matrix

Source record updated: **2026-10-15**
Source intake checked through: **2026-10-15**

> Supporting material for [`learning-and-data.md`](#topic-research-research_training_posttraining).

This file is **not** a Clover training recipe. It records variables that must be controlled before attributing a capability gain to architecture or representation.

High-risk cross-boundary questions live in [`learning-and-data.md`](#topic-research-training-high_risk_boundaries), including partial-success rewards, epistemic calibration, failure/recovery ratios, simulator trust, module adaptation timescales, uncertainty regression, distillation, scaling, fleet-update contamination and model/memory rollback consistency.

---

### 1. Training variables that must be separated

| Axis | Examples | Why it matters |
|---|---|---|
| Data quantity | hours, episodes, tokens, trajectories | scale can help, but repeated homogeneous data may saturate |
| Data diversity | objects, scenes, tasks, embodiments, operators | often more important for OOD generalization than repetition |
| Data quality | expert, suboptimal, failed, noisy, mis-synchronized | equal weighting can create negative transfer |
| Data provenance | real robot, human video, sim, generated/retargeted | determines evidence strength and sim/human→robot bias |
| Alignment | coordinate frames, action space, camera semantics, temporal units | heterogeneous data can conflict without alignment |
| Curriculum | general→expert, easy→hard, short→long, sim→real | stage order changes what is retained/overwritten |
| Objective | action BC, language co-training, future latent, value/reward, world prediction | objective shapes representation and transfer |
| Update scope | frozen backbone, adapter, projector/head, partial/full model | controls specialization vs forgetting |
| Policy distribution | offline/off-policy vs self-generated/on-policy | determines whether recovery/deployment states are covered |
| Teacher/reward source | expert policy, verifier, VLM, learned reward, environment | errors/biases become learning signals |
| Action representation | discrete, regression, diffusion, flow, latent action | changes multimodality, precision and inference cost |
| Temporal abstraction | per-step action, fixed chunk, adaptive horizon, high-level subtask | affects feedback frequency and long/short-horizon trade-offs |
| Replay / failure mining | success only, failure, recovery, prioritized replay | determines whether the policy learns to recover |
| Simulator trust | imagined ratio, rollout horizon, sysid quality | model-based RL can exploit simulator/world-model error |
| Checkpoint selection | BC validation loss, offline FQE, real rollout | proxy metrics can select the wrong policy |
| Continual update | periodic batch, online, fleet aggregation | creates drift/forgetting/rollback/state-compatibility issues |

---

### 2. Data scale is not one scalar

#### Data Scaling Laws in Imitation Learning for Robotic Manipulation

Paper: https://arxiv.org/abs/2410.18647

The study collects more than 40K demonstrations and reports more than 15K real-robot rollouts. Its main Stage-1 signal is that diversity in environments/objects can matter more for generalization than repeatedly collecting more demonstrations for the same environment/object once a threshold is reached.

Therefore record separately:

```text
number of trajectories
number of unique scenes
number of unique objects
task diversity
operator diversity
embodiment diversity
```

Do not use `hours` as the only robot-data scale variable.

#### Qwen-RobotManip

Paper: https://arxiv.org/abs/2606.17846
Official overview: https://qwen.ai/blog?id=qwen-robotmanip

Its central training claim is that representation, motion and behavioral alignment make heterogeneous cross-embodiment scaling coherent.

Important distinction:

```text
data scale
≠ useful scale
```

if action/state semantics conflict.

---

### 3. Objective choice changes transfer under a fixed backbone

#### VLAFlow

Paper: https://arxiv.org/abs/2607.01586

Controlled comparison under a shared π0-style architecture/backbone/action space:

```text
action-only
vs language co-training
vs future-latent alignment
vs language + future-latent
```

This is a high-value Stage-2 candidate because it isolates training signal better than comparing unrelated model families.

#### VLAct — continued pretraining as representation learning

Project: https://starvla.github.io/VLAct/

Use as a current signal that robot continued pretraining can be framed as preserving/learning transferable visual-action representation rather than simply fitting action labels.

Treat project-reported results conservatively until primary-paper details are analyzed.

---

### 4. Action representation and action horizon are training variables

#### OpenVLA-OFT

Paper: https://arxiv.org/abs/2502.19645

Shows that action decoding scheme, action chunking, continuous action representation and fine-tuning loss can materially change both policy performance and inference speed even with the same OpenVLA base.

#### Mixture of Horizons

Paper: https://arxiv.org/abs/2511.19433

Reports an action-chunk trade-off:

```text
longer horizon
→ more foresight / less frequent replanning
→ weaker local precision / feedback

shorter horizon
→ stronger local correction
→ weaker long-range continuity / more inference
```

#### GeoAAC

Paper: https://arxiv.org/abs/2609.20776

Adapts action horizon using flow-denoising geometry.

#### ChunkTrust

Paper: https://arxiv.org/abs/2609.39754

Treats execution horizon as a latent variable inferred from action-expert evidence.

Research implication:

> `action chunk length` and `how many predicted actions are actually executed before replanning` must be recorded separately.

---

### 5. Data quality / weighting can matter more in post-training than pretraining

#### Posterior-Transition Reweighting

Paper: https://arxiv.org/abs/2603.16542

Uses observed post-action consequences to reweight heterogeneous offline robot samples instead of trusting all demonstrations equally.

#### RoboDrop

Paper: https://arxiv.org/abs/2609.10021

Studies post-training data curation under heterogeneous errors such as execution mistakes, sensor drift and timestamp misalignment.

#### ATHENA

Paper: https://arxiv.org/abs/2606.16208

Uses scalable influence-style analysis for multitask VLA data curation.

Required future metadata:

```text
sample weighting
filtering / drop criteria
operator identity / quality
sensor synchronization checks
failure / recovery labels
synthetic-confidence score
```

---

### 6. Frozen vs updated components is a scientific variable

#### TEMPO

Paper: https://arxiv.org/abs/2608.07314

Freezes the pretrained vision-language backbone while updating semantic projection and low-level action expert at different rates.

This is important because uniform full-model RL can destabilize semantic representations while trying to improve control.

#### Learning Action Priors for Cross-embodiment Robot Manipulation

Paper: https://arxiv.org/abs/2606.26095

Pretrains an action module on unconditioned motion trajectories before VLA alignment, arguing that action modules otherwise learn physical temporal structure from scratch during cross-modal training.

Future Clover comparisons should include:

```text
frozen backbone
adapter / LoRA
projection + action head
partial backbone
full model
```

under matched data and compute.

---

### 7. Offline SFT, online RL and on-policy distillation cover different state distributions

#### VLA-OPD

Paper: https://arxiv.org/abs/2603.26666

Frames the trade-off as:

```text
offline SFT
→ efficient
→ demonstration distribution
→ distribution-shift / forgetting risk

online RL
→ current-policy state distribution
→ sparse reward / expensive interaction

on-policy distillation
→ current-policy states
→ dense teacher supervision
```

This is a useful template for later controlled experiments.

#### Online-RL references

- RL fine-tuning for diffusion navigation — https://arxiv.org/abs/2603.12868
- LaST-R1 — https://arxiv.org/abs/2604.28192
- PAC-ACT — https://arxiv.org/abs/2607.09590
- TEMPO — https://arxiv.org/abs/2608.07314
- VLA-Precision — https://arxiv.org/abs/2609.04355

For every online-RL result record:

```text
number of real/sim rollouts
reset procedure
reward source
safety constraints
exploration policy
reference-policy/KL constraint
which parameters update
human interventions
failed rollout retention
```

---

### 8. Simulated/world-model post-training requires explicit trust

#### RehearseVLA

CVPR 2026: https://openaccess.thecvf.com/content/CVPR2026/html/Xiao_RehearseVLA_Simulated_Post-Training_for_VLAs_with_Physically-Consistent_World_Model_CVPR_2026_paper.html

Uses a learned world-model simulator for RL-style VLA post-training when physical resets/interactions are expensive.

#### MERL — Trust-Calibrated VLA Policy Post-Training with Evolving Imagination

Paper: https://arxiv.org/abs/2610.16517

Submitted 2026-10-12. It explicitly varies imagined-data ratio and rollout horizon according to simulator reliability and uses trust to weight replay/optimization.

This strengthens a Stage-1 rule:

```text
more imagined data
≠ better post-training
```

if the learned simulator is inaccurate.

Later tests should vary:

```text
simulator calibration error
imagined-data fraction
imagined rollout horizon
trust threshold
real/sim mixing ratio
```

---

### 9. Failure / recovery data are a separate distribution

Most demonstration datasets overrepresent successful expert trajectories.

Relevant references:

- LoopWAM — https://arxiv.org/abs/2610.18873
- OnEvoMemory — https://arxiv.org/abs/2608.08749
- FailSafe — https://arxiv.org/abs/2510.01642
- ReSYNC / Recover, Discover, Plan — https://arxiv.org/abs/2606.18328
- ENPIRE — https://arxiv.org/abs/2606.19980

Distinguish:

```text
expert success
suboptimal success
recoverable failure
irrecoverable failure
human correction
self-recovery
```

Training only on ideal demonstrations can produce strong nominal behavior but weak recovery.

---

### 10. Checkpoint selection / offline validation can mislead

#### Critical Interval MSE

Paper: https://arxiv.org/abs/2606.29898

Motivation: ordinary validation loss on expert demonstrations can be poorly correlated with real rollout performance.

#### RoboFQE

Paper: https://arxiv.org/abs/2610.18699

Provides rollout-free offline policy evaluation from offline trajectories.

Stage-1 implication:

```text
best validation-loss checkpoint
≠ best deployed robot policy
```

Record the selection metric and whether it was validated against closed-loop outcomes.

---

### 11. General LLM/VLM post-training also shows capability interference

#### DeepSeek-R1

Paper: https://arxiv.org/abs/2501.12948

RL-only reasoning can emerge but behavior quality/readability can degrade; cold-start and staged training change the outcome.

#### DeepSeek-V4.1-Flash

Official: https://www.deepseek.com/en/news/deepseek-v4-1-flash/
Model: https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash

Released recipe:

```text
SFT → RL → on-policy distillation
```

with major emphasis on automated task/environment/rollout generation.

#### Qwen3

Official: https://qwenlm.github.io/blog/qwen3/

Flagship stages:

```text
long-CoT cold start
→ reasoning RL
→ thinking/non-thinking fusion
→ general RL
```

#### Text-Centric Post-Training for Omni-Modal Reasoning

Paper: https://arxiv.org/abs/2610.02819

Important boundary result: text-only reasoning post-training can improve multimodal reasoning while degrading perception; a later native multimodal refinement can recover perception.

This is direct evidence that:

```text
post-training improvement on one axis
≠ monotonic improvement on every axis
```

---

### 12. Proposed future Clover training ablation matrix

When implementation becomes appropriate, use a fixed small/medium backbone and matched data budget.

#### Objective axis

```text
BC / SFT
action + language co-training
action + future latent
BC + world-state auxiliary
on-policy distillation
simulated RL
online RL
failure/recovery replay
```

#### Update-scope axis

```text
frozen backbone
adapter / LoRA
projection/head only
partial backbone
full model
```

#### Data axis

```text
expert-only
expert + suboptimal
expert + failure/recovery
robot only
robot + human video
robot + sim
robot + human + sim
```

#### Temporal-control axis

```text
single action
fixed chunk
mixture of horizons
adaptive execution horizon
```

#### Evaluation vector

```text
IID task success
OOD scene/object/task
cross-embodiment
recovery
physical consistency
uncertainty calibration
persistent memory / revision
state aliasing
long-horizon reliability
latency / memory / energy
catastrophic forgetting
```

Do not change all axes at once.

---

### 13. Remaining training-specific gaps

See [`learning-and-data.md`](#topic-research-training-high_risk_boundaries) for the expanded evidence matrix. Remaining open questions include:

```text
robot post-training scaling laws under matched architecture/data quality
reward models that encode partial success + safety + epistemic correctness
human intervention / takeover as training signal
failure/recovery sampling without destabilizing nominal skills
weighting synthetic samples by simulator/world-model trust
pretraining-objective effects on later physical identifiability
continual fleet learning without propagating one robot's sensor/hardware fault
personalized embodiment adaptation vs global shared policy
rollback semantics when model weights and persistent memory co-evolve
optimizer / LR / batch-size effects on pretrained world-state representations
seed variance for real-robot post-training
checkpoint selection metrics that predict EV7/EV8 performance
joint world-model/policy training vs sequential training under matched compute
```

---

### Final rule

For every claimed training gain ask:

```text
what changed?
data?
objective?
update scope?
action representation?
on/off-policy distribution?
reward/teacher?
simulator trust?
checkpoint-selection metric?
runtime?
```

Until these are controlled, do not call the gain an architectural discovery.

---

<a id="topic-research-training-high_risk_boundaries"></a>

## Training / Post-Training — High-Risk Boundary Questions

Source record updated: **2026-10-15**
Source intake checked through: **2026-10-15**

> Supporting material for [`learning-and-data.md`](#topic-research-research_training_posttraining).

These questions are high-risk because optimizing one headline metric can silently damage other properties of a robotic world model or policy.

Current rule:

```text
task success ↑
does not imply
world understanding / calibration / memory / recovery / safety ↑
```

For every question below, the goal is to record what is known, what is still open, and what Clover should measure later.

---

### Q1 — How should a reward represent partial success?

Binary success/failure is too coarse for long-horizon robot learning.

Current evidence:

- DenseReward predicts dense frame-level progress and explicitly synthesizes physically realistic failure trajectories: https://arxiv.org/abs/2607.13033
- SARM2 uses multi-task stage-aware dense reward for long-horizon manipulation: https://arxiv.org/abs/2606.10305
- Z-1 uses completion-aware reward calibration during VLA RL post-training: https://arxiv.org/abs/2606.31846
- Quantization-Conditioned RL uses progress-scaled terminal penalties to distinguish partial completion in low-bit VLA policies: https://arxiv.org/abs/2610.15675

Do not collapse partial success into one arbitrary scalar without preserving decomposition.

A useful future reward record is:

```text
R_task          final task completion
R_progress      stage / subgoal progress
R_physics       physically valid interaction
R_safety        constraint violations / near misses
R_recovery      successful recovery after deviation
R_epistemic     calibrated belief / justified uncertainty
R_efficiency    time / energy / intervention cost
```

Whether these should be scalarized, lexicographically ordered or handled as constrained objectives remains open.

---

### Q2 — Should reward explicitly encourage epistemic correctness, not only task success?

**Yes, this must be researched; the exact objective is open.**

A policy can finish a task while holding a badly calibrated or factually wrong world belief.

Methodological evidence outside robotics is strong: ordinary reasoning RL can improve task accuracy while degrading calibration, while proper-scoring-rule rewards can preserve or improve calibrated confidence.

- RLCR / *Beyond Binary Rewards* — https://arxiv.org/abs/2507.16806

Embodied reward work already shows that reward must be multi-dimensional and verified rather than a simple success scalar:

- ReWorld rewards physical realism, task logic, embodiment plausibility and visual quality: https://arxiv.org/abs/2601.12428
- Reward as an Agent explicitly targets reward hacking / verification failures in embodied world-model RL: https://arxiv.org/abs/2606.19990

Future Clover research should test separate epistemic terms such as:

```text
calibration / proper scoring
unknown-state correctness
belief update after contradictory evidence
confidence in world-model rollout
refusal / ask-for-more-evidence behavior
```

Critical warning:

```text
rewarding “high confidence” is wrong.
```

The target should be **confidence justified by evidence/outcomes**, not confidence itself.

---

### Q3 — What fraction of training data should be failure trajectories?

**No universal ratio is supported by current evidence. Do not invent one.**

The correct fraction likely depends on:

```text
base-policy failure rate
failure diversity
severity / recoverability
nominal-state coverage
recovery objective
training stage
on-policy vs offline distribution
```

Current evidence:

- DenseReward argues diverse failure data is necessary for dense reward learning: https://arxiv.org/abs/2607.13033
- FAR exploits informative failure cases and successful retries for continual improvement: https://arxiv.org/abs/2607.01111
- FLARE adds retry/reset behavior because failure-free demonstrations leave policies unable to recover: https://arxiv.org/abs/2608.26645
- LoopWAM explicitly learns from successes, suboptimal behavior and failures: https://arxiv.org/abs/2610.18873

Required experiment:

```text
failure/recovery fraction sweep
0 / low / medium / high
with fixed total data budget
```

Evaluate both failure recovery **and nominal performance**.

---

### Q4 — Can recovery data damage the nominal policy?

**Yes in principle; current literature mostly demonstrates benefit but does not justify unlimited recovery mixing.**

Recovery states can be heavily off the nominal trajectory distribution. Oversampling them can distort the policy toward conservative/recovery behavior or weaken clean execution.

Useful references:

- FLARE separates ordinary Retry from state-breaking Reset behavior rather than forcing every failure mode into one undifferentiated nominal policy: https://arxiv.org/abs/2608.26645
- RecoverFly combines failure revisiting with reference-policy regularization specifically to improve adaptation while preserving acquired capability: https://arxiv.org/abs/2608.09467
- FAR uses failure-contrastive adaptation and then incorporates successful recovery trajectories: https://arxiv.org/abs/2607.01111

Future Clover experiment:

```text
nominal-only
vs nominal + recovery mixed uniformly
vs prioritized recovery
vs separate recovery module / gate
```

Measure:

```text
clean-task success
trajectory efficiency
unnecessary reset/retry frequency
recovery success
safety
OOD robustness
```

---

### Q5 — How should world-model confidence control imagined rollout length?

This is now an active 2026 research direction rather than a purely hypothetical idea.

- MERL explicitly lets simulator reliability control the imagined-data ratio and rollout horizon; chunk-level trust also controls replay selection and optimization weight: https://arxiv.org/abs/2610.16517
- RWM-U propagates epistemic uncertainty over world-model rollouts for offline model-based RL on physical robots: https://arxiv.org/abs/2504.16680
- WOMBET filters generated experience by return and epistemic uncertainty before transfer: https://proceedings.mlr.press/v331/kim26a.html
- WoVR focuses on preventing policy optimization from exploiting hallucinated imagined success: https://arxiv.org/abs/2602.13977

Future rule to test, not assume:

```text
high trust → longer imagination / more synthetic weight
low trust  → shorter rollout / lower weight / real-data fallback
```

Confidence must itself be calibrated against held-out real or high-trust transitions.

---

### Q6 — Does the optimal human-video / simulator / robot-data mixture depend on model scale?

**Very likely, but current evidence does not provide a universal scaling law.**

Qwen-RobotManip is a key current data-engine example:

- ~11.4K h robot data
- ~1.9K h egocentric human video
- ~24.8K h synthesized human→robot data
- 15 embodiments

Source: https://qwen.ai/blog?id=qwen-robotmanip · https://arxiv.org/abs/2606.17846

But its central lesson is alignment before pooling.

Rethinking VLA Scaling shows naive embodiment mixing can cause negative transfer: https://arxiv.org/abs/2602.09722

Required future matrix:

```text
model scale × data mixture

small / medium / large
×
robot / human / sim / generated ratios
```

Keep total optimizer steps / tokens controlled where possible.

Do not assume a mixture optimized for 4B remains optimal for a large MoE.

---

### Q7 — Frozen VLM vs LoRA vs partial tune vs full tune: when is each best?

Current evidence says there is **no universal winner**.

- A real-robot π0 study finds some LoRA configurations match FFT, while freezing the VLM or restricting adaptation too aggressively degrades embodiment transfer: https://arxiv.org/abs/2607.10172
- Adaptive Capacity Allocation reports robotics PEFT can require larger/task-varying effective rank and can match/exceed full tuning on evaluated real tasks: https://arxiv.org/abs/2603.07404
- VLM2VLA demonstrates that data/action alignment plus LoRA can preserve foundational VLM capabilities better than naive robot fine-tuning: https://arxiv.org/abs/2509.22195
- Qwen-Drive provides a strong explicit alternative: reuse a pretrained multimodal backbone and add task-specific state/planning modules: https://qwen.ai/blog?id=qwen-drive-1.0

Future selection criteria:

```text
new embodiment gap
new visual domain
new task semantics
available data
forgetting tolerance
compute / memory budget
need to preserve general VLM capability
```

---

### Q8 — Should different modules use different learning rates / update frequencies?

**Yes, this deserves explicit experimentation.**

TEMPO is a direct 2026 example:

- pretrained VLM backbone frozen;
- semantic projection updated infrequently;
- low-level action expert updated frequently.

Paper: https://arxiv.org/abs/2608.07314

Its motivation is functional:

```text
semantic representation changes slowly
motor correction needs fast feedback
```

This should be generalized into experiments over:

```text
vision encoder LR
language/semantic LR
state/memory module LR
action expert LR
reward/value LR
world-model LR
```

The right timescale may differ across deployment regimes.

---

### Q9 — Should semantic representation and motor representation adapt at different speeds?

This is closely related to Q8 but is conceptually broader than choosing learning rates.

Evidence:

- TEMPO explicitly uses a two-timescale semantic/action post-training architecture: https://arxiv.org/abs/2608.07314
- Actions as Language shows aggressive robot adaptation can destroy higher-level semantic/multimodal capability: https://arxiv.org/abs/2509.22195
- VLA-OPD frames catastrophic forgetting and policy-distribution shift as separate problems in post-training: https://arxiv.org/abs/2603.26666

Future Clover hypothesis space should include:

```text
slow semantic/world representation
+
fast motor/action adaptation
```

but this remains a hypothesis, not a default architecture.

---

### Q10 — Can post-training worsen uncertainty calibration?

**Yes. Strong evidence exists in reasoning models; robot-specific evidence remains insufficient and should be collected.**

RLCR finds ordinary correctness-reward RL can actively degrade calibration and shows proper-scoring-rule rewards can counteract it: https://arxiv.org/abs/2507.16806

For embodied systems this creates a concrete Stage-1 gap:

```text
before post-training
vs after SFT
vs after RL
vs after distillation
vs after quantization
```

measure:

```text
ECE / Brier where meaningful
selective prediction
unknown-state detection
failure prediction
world-model confidence vs realized error
```

Do not assume higher task reward means better epistemics.

---

### Q11 — Can task success improve while permanence / memory / causal reasoning degrade?

**Yes, this is a credible and partly demonstrated form of capability forgetting, but direct robot-world-state benchmarks are still missing.**

- VLM2VLA starts from the observation that robot fine-tuning can reduce foundational reasoning/multimodal understanding: https://arxiv.org/abs/2509.22195
- LifeLong-RFT explicitly targets continual VLA adaptation where ordinary SFT is prone to catastrophic forgetting: https://arxiv.org/abs/2602.10503
- *What Should World Models Forget?* argues continual world models require separate tests for invariant knowledge vs instance facts that should change: https://arxiv.org/abs/2610.03713

Clover must therefore carry a **capability regression battery** through every post-training stage:

```text
task success
geometry
object permanence
memory revision
causal/counterfactual probes
uncertainty
OOD visual semantics
```

---

### Q12 — What is lost when distilling to a smaller model?

Task success alone is insufficient to answer this.

Current positive evidence:

- VLA-AD distills OpenVLA-7B into a 158M student using semantic guidance and reports near-teacher LIBERO task performance: https://arxiv.org/abs/2605.16241
- RT-VLA distills a larger driving VLA into a real-time student while preserving evaluated driving/reasoning capability: https://arxiv.org/abs/2606.14010
- World-model feature distillation into compact robot policies is an emerging route: https://arxiv.org/abs/2609.24682

Open question:

```text
what disappears first?
```

Candidate losses:

```text
rare-event behavior
uncertainty calibration
fine spatial precision
long-horizon memory
open-world semantics
causal sensitivity
recovery diversity
```

Future distillation evaluation must use a capability vector, not only teacher/student success gap.

---

### Q13 — Does a recipe that works at 4B scale to a large sparse MoE?

**Unknown by default. Never assume yes.**

Evidence:

- Rethinking VLA Scaling reports several seemingly reasonable data/regularization strategies do not improve consistently at scale: https://arxiv.org/abs/2602.09722
- DeepSeek scaling-law work historically treats hyperparameters themselves as scale dependent: https://arxiv.org/abs/2401.02954
- Modern DeepSeek/Qwen MoE models additionally introduce routing, active-parameter, communication and kernel effects absent from small dense models.

Required Clover protocol:

```text
4B discovery
→ 8B / 30B replication
→ sparse-MoE / remote counter-check
```

Record if the effect changes sign, disappears or requires a different LR/data mixture/objective weight.

---

### Q14 — In continual fleet learning, can one broken robot contaminate the fleet?

**Yes in principle, and update admission must be treated as a safety problem.**

Potential bad-client causes include:

```text
sensor/calibration fault
actuator damage
wrong embodiment metadata
corrupted memory
adversarial data
local environment regime shift
bad reward / human annotation
```

Relevant evidence:

- A 2026 federated VLA study shows that physical cross-site heterogeneity is substantial and studies federated update scope / aggregation / personalization: https://arxiv.org/abs/2609.22973
- *When Validation Stops Learning* studies update-admission rules for continual embodied agents and shows overly conservative gates can reject all useful learning while weak gates risk harmful updates: https://arxiv.org/abs/2609.10873
- Earlier federated embodied-agent work demonstrates that poisoned clients/data can steer embodied policies, motivating robust aggregation and client trust mechanisms.

Future fleet protocol should preserve:

```text
robot identity / hardware state
calibration version
data provenance
failure regime
local validation delta
update confidence
quarantine status
```

A fleet update should not be accepted merely because it improves the originating robot.

---

### Q15 — After model rollback, what happens to memory learned by the newer model?

This is a genuine unresolved stateful-system problem.

Weights and persistent world memory have different histories.

Example:

```text
model v12
→ operates / writes memory M12
→ update to v13
→ writes M13 using different representation / policy
→ v13 regresses
→ rollback weights to v12
```

Questions:

```text
Can v12 read M13?
Was M13 derived through a behavior later judged unsafe?
Should raw evidence survive while derived beliefs are re-encoded?
Which memories depend on v13-specific latent semantics?
What should be quarantined or invalidated?
```

Adjacent 2026 agent-memory research provides useful mechanisms but not yet a robot-specific solution:

- ChronoMem introduces version control and semantic rollback for long-term agent memory: https://arxiv.org/abs/2607.27773
- TRACE studies admission of stale vs still-valid memory after system/world evolution: https://arxiv.org/abs/2609.33517
- Crab / Planarian study consistent checkpoint/restore of stateful agent environments and the hazards of rollback across external side effects: https://arxiv.org/abs/2604.28138 · https://arxiv.org/abs/2609.35366

A future Clover memory design should distinguish at least:

```text
raw evidence
versioned derived belief
model/checkpoint that created belief
belief dependencies
current validity status
```

Prefer re-deriving beliefs from preserved evidence after rollback over blindly restoring incompatible latent state.

---

### Required post-training report card

Every serious Clover post-training experiment should eventually produce a before/after vector:

```text
Task
Nominal
OOD
Partial progress
Failure recovery
Safety
Epistemic calibration
Unknown/refusal
Physical prediction
Object permanence
Memory revision
Causal/counterfactual
Long-horizon reliability
Latency
Memory
Energy
Forgetting / retained general capability
```

and record:

```text
exact checkpoint
training stages + order
data mixture + provenance
failure/recovery ratio
reward components
on/off-policy regime
world-model confidence usage
frozen / adapted modules
module learning rates / update frequencies
action horizon
precision / quantization
checkpoint-selection criterion
rollback / memory version
```

---

### Current conclusion

The remaining post-training questions are not mainly about inventing another optimizer.

They are about **credit assignment, evidence quality, distribution control, trust calibration, capability preservation and state lifecycle**.

That is the level at which Clover should compare robot post-training methods in Stage 2.

---

<a id="topic-docs-research-map-data-and-experience"></a>

## Data, Experience and Interaction

### Core question

> **What kinds of experience are actually required for a machine to build a world model from vision?**

The modern robotics literature suggests that data source is part of the algorithmic question, not merely an engineering detail.

### Passive video

Strengths:

- enormous diversity;
- natural human/object/environment interactions;
- cheap relative to robot data;
- useful for learning visual and temporal regularities.

Limitation:

The model often does not know the agent's exact action/intervention, so some causal variables are not identifiable.

V-JEPA 2 is an important case: large-scale action-free video pretraining is followed by comparatively small action-conditioned robot post-training.

### Human egocentric video

Strengths:

- first-person viewpoint;
- long natural task sequences;
- dense hand-object interactions;
- scalable collection.

Limitations:

- human morphology differs from robots;
- action/force/proprioceptive signals may be absent;
- language narration can introduce non-visual supervision.

Ego4D and recent robot-foundation-model efforts make this a major research direction.

### Robot demonstrations / teleoperation

Strengths:

- explicit actions and consequences;
- robot embodiment matched to deployment;
- direct control supervision.

Limitations:

- expensive;
- limited environment diversity;
- often biased toward successful demonstrations.

DROID and Open X-Embodiment are important public resources.

### Simulation

Strengths:

- unlimited interventions;
- exact world state;
- controlled counterfactuals;
- scalable self-play / exploration.

Limitations:

- sim-to-real gap;
- simulator assumptions can become hidden supervision;
- visual realism is not equivalent to physical realism.

### Self-generated interaction

Self-play and autonomous exploration add a different source of evidence: the model can choose interventions specifically to reveal dynamics or improve skills.

For Clover this may connect directly to active perception and causal identification.

### Working hypothesis

A general robot brain may eventually require a curriculum combining:

```text
passive visual observation
+ egocentric human experience
+ robot action/consequence data
+ simulation/intervention
+ autonomous exploration
```

This is a research hypothesis. The contribution of each source should be measured rather than assumed.

---

<a id="topic-docs-research-map-lifelong-learning"></a>

## Lifelong Learning and World Growth

### Core question

> **Can a robot's understanding of the world improve continuously from experience without periodically rebuilding the entire model?**

A general robot brain cannot remain permanently frozen after offline training. It must acquire new entities, dynamics, places and task regularities while correcting earlier beliefs.

### Relevant fields

- continual learning;
- catastrophic forgetting;
- experience replay;
- online adaptation;
- lifelong robot learning;
- memory consolidation;
- open-world recognition;
- ontology/type discovery.

### LIBERO

LIBERO is a benchmark for lifelong robot learning focused on knowledge transfer. Its purpose is not pure visual world understanding, but it provides a mature framework for asking whether previously learned skills and knowledge help or interfere with later tasks.

Primary source:

- https://libero-project.github.io/main.html

### Clover's stronger requirement

Skill retention alone is not enough. A persistent worldview should support:

```text
new evidence
→ revise belief
→ preserve unaffected knowledge
→ invalidate affected claims
→ consolidate stable structure
→ forget detail without losing provenance
```

### Types of growth to study

- **Add** — new entity/type/relation/model;
- **Merge** — previously separate concepts become equivalent;
- **Split** — one category separates into different dynamics/affordances;
- **Revise** — later evidence changes an earlier belief;
- **Retire** — obsolete hypothesis no longer influences current authority;
- **Forget** — remove unnecessary high-resolution history;
- **Consolidate** — replace repeated evidence with a stable reusable model.

These operations are research requirements, not claims that the current public repository already implements them.

### Open questions

1. What should remain plastic during deployment?
2. How can a system distinguish new knowledge from transient noise?
3. What memories must be retained to allow later reinterpretation?
4. Can a model grow its ontology without human category labels?
5. How do we prevent self-training errors from becoming authoritative world facts?
6. What does a 24-hour or 7-day persistent robot worldview look like computationally?

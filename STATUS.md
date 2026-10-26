# Clover Status

Last updated: **2026-10-26**.

> **Research question:** How can a machine understand the real world through vision alone?
>
> **Long-term goal:** Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.

**Model objective:** pure-vision AGI with natively ultrafast computation and broad visual understanding. Core recognition, detection, segmentation, tracking and visual reading belong to the required capability scope. The [research contract](SSOT.md#model-objective-and-breadth-of-understanding) records the scope; these are targets, not achieved Clover results.

## Current project decision

**Stage 1 — Research / Survey & Evidence Collection is ACTIVE.** No representation, backbone or core algorithm is frozen. The 2026-10-15 recommendations to make Stage 2 primary remain [dated assessments in Stage 1](01-research/README.md#topic-research-stage1_final_audit_2026-10-15); they were not an approved stage transition.

The 2026-10-19 decision remains in force: the CPU-only implementation line is frozen at its current results. It resumes only after the embodied-intelligence line produces a new, complete frontier breakthrough. The main research scope is the broad visual-AGI model; a robotic brain remains a long-term application.

Apple M4 remains the local development reference; no target real robot is currently available. Final robot hardware is open. No new algorithm, experiment or deployment is reported in this update.

## 当前进展与下一步 — 2026-10-26

| 事项 | 当前证据 | 入口 |
|---|---|---|
| 研究目标 | 完整、全面、当前的前沿/相关/交叉研究；仍保持原视觉问题与 Stage 1 | [完整性审查](01-research/README.md#coverage-and-completion-audit) |
| 最新范围明确 | 纯视觉 AGI、原生 ultrafast、广义理解；识别/检测/分割/追踪/阅读等二十类能力已明确归属 | [能力地图](01-research/perception-and-identifiability.md#broad-visual-capabilities) |
| 核心视觉前沿补充（2026-10） | 新增 **300 篇此前未引用论文**、314 篇书目核验（313 arXiv + 1 PMLR）；覆盖识别/检测/分割/追踪/阅读/动作/人-物交互与人脸/表情/手势/指代/姿态/人体与手部3D/计数/几何/边界与抠图/光流与匹配/遮挡与非模态/事件视觉与异步感知/主动感知与视角规划/长视频与第一人称记忆/组合泛化与视觉推理/计数与视觉测量/空间状态与 SLAM/点追踪与 3D 运动/物体级 6-DoF 跟踪/3D 占据与场景图/物理世界模型与因果规划/部件/可供性/隐藏态与分布偏移/长尾/细粒度/尺度失败面，含 YOLO26、RF-DETR、SAM 3/3D、SAMURAI、MOTIP2、UGO、TAPFormer、M2P、CoWTracker、Track4World、MoSE3、3D SSM、Track-On-R、TrackCraft3R、TrackerSplat、RoPT、GRC-Pose、ComPose、Robust Recovery、ASM-6D、Event6D、LEGAU、DICArt、OCH3R、OccAny、OccAnyScene、VEOcc、OccTrack360、FALCON、LEXI-SG、LOST-3DSG、OP3DSG、DSG、PanoGraphGS、UniSim-SLAM、FFVO、FineHOI、HOIBlender、GraspHOI、SAGE、FreeFlow、MVLoMa、B2TFPose、OccJEPA、Amodal SAM、VolFill、NOVA3R、ChronoFuse、Event3R、E-TraMamba、R4DSG、Ledger、EgoProbe、VideoLoop、PREM、TraceViT、JRDB-AVR、DualCount、BunchCount、SVCBench、RT-Counter、DenseFace、FaceLiVTv2、EventFace、TAG、SAM 3D Body、Fast SAM 3D Body、OnlineHMR、DanceHMR、AffordAny、UniAfford、PartLLM、UniPart、FunRec、VideoMaMa++、RenderMatte、SEP-YOLO、SeeClear、OPC16K、ActiveArena、CanViT、I-Perceive、BAVO/A-FAR、Epistemic-Trap、Checkpoint-Selection、Colorist、GATE、RADC、CTTA、FORGE、PaddleOCR-VL、dots.ocr、DA3、PnP-Transformer、MEVL-STP、WOW-Seg、MoSA、GOT-Edit、RelationVGGT、UniFunc3D、StarWM、iSEE、PersistBench、Causal-JEPA、World Models' Last Exam in Physics、DR-WM、STRIKE、P3Sim、Mirage2Matter、Causal-Plan、AVL-JEPA、PhysCanvas、HapticWorld、AlayaWorld；101 篇本轮新增正文级选读（另 1 篇既有引用）、1 篇既有记录深化 | [核心视觉前沿](01-research/perception-and-identifiability.md#core-vision-frontier) |
| 原生速度与跨域补充 | 新增 YOLO26/RF-DETR/DEIM 系统边界、EfficientViT、RPFQ-ViT、Bifocal、StreamAhead、TacitVLA、Realtime-Bench；主动视觉与视网膜/事件/V1 证据 | [原生速度](01-research/foundation-models-and-systems.md#ultrafast-systems-frontier) · [主动视觉](01-research/causality-and-active-perception.md#active-vision-frontier) |
| 前一批方向补充（10-19→10-25） | 首次登记 **53 篇**，深化 **1 篇**已有论文，按机制、输入/学习来源、证据和边界写回现有正文 | [交叉桥接](01-research/research-questions.md#cross-domain-research-bridges) |
| 前一批基础视觉/正式来源补充 | 在上述资料上增补 **31 条比较记录**：基础视觉/效率 16，正式会议相关/交叉研究 15；分别保留选读范围 | [固定来源与深度](01-research/sources-and-resources.md#broad-vision-sources) |
| 前沿检索 | 19 组主查询 + 动作/指代补充检索；主查询返回 2,072 条去重候选（2026-09-01→10-25）；分类公告核对到 10-23；未把所有候选声称为精读 | [来源协议](01-research/sources-and-resources.md#current-search-protocol) |
| 正式会议检索 | 六个官方目录取回 11,774 条题名、规则筛出 1,423 候选；不是全部人工筛完/全文读完 | [目录范围](01-research/sources-and-resources.md#broad-vision-sources) |
| 旧引文核查 | 335 个数字 arXiv ID 均取回书目；未据此宣布全部旧研究结论正确 | [书目边界](01-research/sources-and-resources.md#current-search-protocol) |
| 模型 artifact | `dcdebb7` 的 **12 类官方入口**已校正为“artifact 类别”而非“12 个同类模型”；本轮补了代表 checkpoint、参数/输入、训练来源、量化/导出、厂商时延与同协议资格，缺失字段继续记 `unknown` | [可比性账本](#visual-artifact-comparability-ledger-2026-10-26) · [精确版本](01-research/foundation-models-and-systems.md#current-model-artifacts) |
| 原生速度与视觉发布 | 增加完整时延/证据年龄/多能力负载口径；核对 YOLO26 paper/docs、OCR/TAP 等入口，YOLO27 仍属未发布预览 | [计算研究](01-research/foundation-models-and-systems.md#native-ultrafast-research) |
| 结构与持续维护 | 根目录跨阶段规则；调研继续按原八方向原位更新，没有新增调研文件 | [第一阶段](01-research/README.md) |

**尚未完成：** 新增 300 篇中 101 篇正文级选读，其余方法/监督/实验完整复核仍缺；artifact 元数据账本已补，但多数权重仍未由 Clover 实际加载，统一端到端时延、峰值内存、量化质量损伤与相同 harness 结果仍无实测；ICLR/ECCV/CoRL 全目录（本轮只补 ICLR/ECCV/NeurIPS 2026 定向 18 篇 camera-ready）、更多正式期刊与全部旧官方 artifact 刷新；335 个旧数字 ID 的书目检查已完成，18 个单 ID 结构化块题名核对完成（修正 2 处题名形式）；逐句数字/主张仍未全审；严格视觉隐藏态、真实因果识别和未知未来任务证据恢复；预训练-评测数据重叠多不可核对。当前未通过全范围完整性核查，目标继续推进，没有宣布“全面完成”或推进阶段。

<a id="visual-artifact-comparability-ledger-2026-10-26"></a>
## 视觉 artifact 可比性账本 — 2026-10-26

**计数口径修正：** `dcdebb7` 的“12 类官方 artifact”是 12 个**入口类别**，不是 12 个彼此同任务、同接口的模型。其中包含模型族组合（SAM 3 / SAM 3D、DINOv3 / PE、追踪器组、姿态/几何组）以及非模型评测集 OmniDocBench。不能把“12 类入口”直接变成一个 12 模型排行榜。以下只采用官方 GitHub、官方模型卡/配置和官方文档；公开证据没有给出的字段保留 `unknown`，不从宣传页或家族名推断。

分层定义：**可直接比较** = 可在同一任务、同输入/输出与同计时 harness 下做 apples-to-apples；**仅机制参考** = 可提供表示/架构/系统证据，但当前输出空间或任务不同；**证据不足** = 类别内部尚未固定到足以复现的一组 checkpoint/config，或关键权重/runtime 字段缺失。不同任务组不得横向排单一总榜。

| 12 类入口 | 固定/代表 artifact 与 revision | 参数；输入/分辨率/上下文 | 训练 / 后训练公开证据 | 量化 / 导出 / 外部时延 | 同协议资格 |
|---|---|---|---|---|---|
| YOLO26 | [`yolo26n/s/m/l/x.pt`](https://docs.ultralytics.com/models/yolo26/)；代码核验到 [`ultralytics@aa1f778`](https://github.com/ultralytics/ultralytics/commit/aa1f778a75a610f7dd2aa4762df1c25f6a3063d7)；具体 `.pt` 文件哈希待 Phase A 下载后冻结 | 融合检测推理图 2.4/9.5/20.4/24.8/55.7M；640；无文本上下文 | 官方检测权重以 COCO 为预训练任务；全部 head 的精确数据混合仍 `unknown` | 官方导出支持 TensorRT；FP16 与 INT8 PTQ（需校准数据）。T4/TensorRT10、batch=1、NMS-free 模型侧 1.7/2.5/4.7/6.2/11.8 ms；CPU ONNX 是另一口径；Clover E2E=`unknown` | **可直接比较：检测组** |
| SAM 3 / SAM 3D | [`facebook/sam3@3c879f3`](https://huggingface.co/facebook/sam3/tree/3c879f39826c281e95690f02c7821c4de09afae7)；[`facebook/sam-3d-objects@2e73555`](https://huggingface.co/facebook/sam-3d-objects/tree/2e73555018d2741ccd486e56c24fac41155a1dc6) | SAM 3：约 850M（论文）/859.9M safetensors 计数；图像/视频，论文图像 1008、文本上下文 32。SAM 3D：单图+mask→3D，参数 `unknown`（gated/未暴露） | SAM 3 的完整训练混合尚未形成可复现账本；SAM 3D 卡片给出 progressive training + data engine/human feedback，但精确配比 `unknown` | SAM 3 有 Transformers image/video 接口；统一 ONNX/TensorRT/官方量化路径 `unknown`。论文多目标约 30 FPS 依赖多 H200，不能当端侧 E2E；SAM 3D E2E=`unknown` | **SAM 3：仅机制参考**（可另建 promptable segmentation lane）；**SAM 3D：证据不足** |
| Depth Anything 3 | 当前精确账本 [`DA3-GIANT@7cd62ae`](https://huggingface.co/depth-anything/DA3-GIANT/tree/7cd62ae9315b9dff094d2d300e4ad012640607dd)；资源友好候选 [`DA3-SMALL`](https://huggingface.co/depth-anything/DA3-SMALL) | GIANT 卡片 1.15B（repo 另记 safetensors 计数差异）；SMALL 官方页 34.3M；官方 API/CLI 默认 `process_res=504`；单/多视图，无文本上下文 | GIANT 模型卡明确 public academic datasets only；更细 dataset mixture/teacher 比例 `unknown` | 官方 `mini_npz/npz/glb/ply/gs` 是结果导出格式，不是 ONNX/TensorRT 模型后端；官方量化与 Clover E2E=`unknown` | **仅机制参考**；与 MoGe 固定同一 depth/pose 输出后可升级为几何直接比较组 |
| RF-DETR | Nano/Small/Medium/Large；代码核验到 [`roboflow/rf-detr@5b22dfc`](https://github.com/roboflow/rf-detr/commit/5b22dfc0940697ce1abdfa681a5f7392b3eddbfb)；执行时仍需冻结具体权重文件哈希 | 30.5/32.1/33.7/33.9M；384/512/576/704；无文本上下文 | 基础 detection models 训练于 COCO；backbone DINOv2（更小 Plus 型号另有 PE-Core-T）；逐型号 recipe 随 checkpoint 冻结 | 官方 ONNX/TensorRT；T4 TensorRT FP16 b1 2.3/3.5/4.4/6.8 ms。当前 INT8 路径的速度/AP 是 RTX 5070 + 特定 commit/harness，不能和 T4 混列；Clover E2E=`unknown` | **可直接比较：检测组** |
| PaddleOCR-VL / PP-OCR | [`PaddleOCR-VL-1.6@c5630ab`](https://huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6/tree/c5630abae1d940eafe0697512a0325494b02ab42)；完整 pipeline 另含 PP-DocLayoutV3 | 约 0.9B/958.6M；vision image 384、patch 14；`max_position_embeddings=131072`；BF16 | 官方 1.6 从 1.5 继续，区域/弱项定向数据；**continued pretraining → SFT → RL** | Transformers 与 PaddleOCR pipeline 均有入口；macOS 官方说明优先 Docker。统一量化、M4 E2E 与完整 pipeline 吞吐=`unknown` | **可直接比较：文档解析组**；“VLM 单模型”和“layout+VLM+assembly pipeline”必须分两条计时 |
| dots.ocr | [`dots-studio/dots.ocr@c0111ce`](https://huggingface.co/dots-studio/dots.ocr/tree/c0111ce6bc07803dbc267932ffef0ae3a51dc951) | 3.039B；`max_position=131072`；patch 14；BF16 | 精确训练混合/阶段仍不足以形成同粒度 recipe，保留 `unknown` | 官方推荐 vLLM，公开评测基于 vLLM 0.9.1；另有 HF/SGLang/Docker。官方评测说明部分文档统一 200 DPI，且某些口径删除 header/footer；量化与 Clover E2E=`unknown` | **可直接比较：文档解析组（有条件）**；必须统一 DPI、prompt、header/footer 与后处理 |
| MinerU2.5 | [`MinerU2.5-Pro-2605-1.2B@08aaea8`](https://huggingface.co/opendatalab/MinerU2.5-Pro-2605-1.2B/tree/08aaea840498d49ce16247b6263196cf02814885) | 1.156B/名义 1.2B；max position 32,768（文本侧 8,192）；patch 14；BF16 | 2605 不改原 1.2B 架构，重点为数据清洗、难例与大规模图像分析数据扩充；完整配比 `unknown` | Transformers、vLLM（官方推荐）、SGLang、Docker；HF 上第三方 quantization 不自动视为官方 recipe；Clover E2E=`unknown` | **可直接比较：文档解析组**；固定 2605，不把 2509/2604 结果混用 |
| olmOCR 2 | [`olmOCR-2-7B-1025-FP8@40bd720`](https://huggingface.co/allenai/olmOCR-2-7B-1025-FP8/tree/40bd7202494b8264ee17ada08b401b5aab7a9ce1) | 名义 7B；现有 HF 张量计数约 8.292B；max position 128k；单页最长边官方使用 1288 px；FP8 checkpoint | Qwen2.5-VL-7B-Instruct → olmOCR-mix-1025 SFT → GRPO RL（公式、表格、困难 OCR） | 官方 FP8 由 llmcompressor 生成；推荐 olmOCR toolkit + vLLM，也有 SGLang/Docker。toolkit 会渲染、旋转、重试并注入文档元数据，所以模型侧与 pipeline E2E 必须分列 | **可直接比较：文档解析组（有条件）**；固定 toolkit、render、rotation/retry 与 prompt |
| DINOv3 / Perception Encoder | [DINOv3](https://github.com/facebookresearch/dinov3)；[Perception Models](https://github.com/facebookresearch/perception_models) | DINOv3 ViT-S/16→ViT-7B/16 为 21M→6.716B，另有 ConvNeXt；PE-Core 有 T/S/B/L/G，官方示例输入含 224/336/384/448。两者输出 representation，不是共同 task head | DINOv3 公开 LVD-1689M 等预训练信息；PE family 为可扩展 contrastive pretraining，不同 core/lang/spatial checkpoint 监督目标不同 | 统一量化/导出/同一任务速度账本 `unknown`；须先冻结 probe/head 与 feature layer | **仅机制参考**；作为 frozen-backbone/linear-probe 控制，不与 detector/OCR 排总榜 |
| SAMURAI / MOTIP / OmniTrack / Cutie | [SAMURAI](https://github.com/yangchris11/samurai) · [MOTIP](https://github.com/MCG-NJU/MOTIP) · [OmniTrack](https://github.com/xifen523/OmniTrack) · [Cutie](https://github.com/hkchengrex/Cutie) | 同一类别混有 box/MOT、mask/VOS、全景/长视频跟踪；精确参数、resize、checkpoint revision 尚未统一固定 | SAMURAI 本身不训练，用 SAM 2.1 权重 + Kalman/记忆选择；其余训练来源各异，不能用一个 recipe 表示 | SAMURAI 官方明确现有代码不支持 live/streaming input；其余 runtime/export/量化未统一固定 | **证据不足**；先拆 VOS/MOT/omni 子协议，再逐个冻结 revision、预处理与 ID 输出语义 |
| ViTPose / Sapiens / MoGe | [ViTPose](https://github.com/ViTAE-Transformer/ViTPose) · [Sapiens](https://github.com/facebookresearch/sapiens) · [MoGe](https://github.com/microsoft/MoGe) | ViTPose 常见 256×192（G 可 576×432）；Sapiens 0.3B/0.6B/1B/2B，覆盖 pose/seg/depth/normal；MoGe 为开放域单目几何。类别内部任务与输出空间不同 | human-centric pretraining、pose fine-tune 与 open-domain geometry 目标不同，不能合并成一个 recipe | checkpoint 分发、框架、模型导出与 runtime 尚未形成共同账本 | **证据不足**；MoGe 可与 DA3-SMALL 建几何子榜，ViTPose/Sapiens 建人体感知子榜 |
| OmniDocBench | [官方仓库](https://github.com/opendatalab/OmniDocBench) | **不是模型**：无参数/权重/上下文；真实文档多类型、多语言，支持 E2E/layout/table/formula/OCR | N/A；需要单独审计 benchmark 版本和训练集重叠 | 有官方评测代码/repro 环境；大量公开模型结果仍按 `v1.6_full` 报告，而仓库后续已有 v1.7，版本不可混用 | **仅机制/协议参考（benchmark）**；不进入“模型”排名 |

### 分层结果与下一轮统一 benchmark

- **可直接比较（只在组内）**：检测 `YOLO26 ↔ RF-DETR`；文档解析 `PaddleOCR-VL-1.6 ↔ dots.ocr ↔ MinerU2.5-Pro-2605 ↔ olmOCR-2-7B-1025-FP8`，OmniDocBench 仅作为协议锚点。
- **仅机制参考**：SAM 3、DA3（几何子协议固定前）、DINOv3/PE、OmniDocBench。它们分别回答 promptable segmentation/tracking、几何、representation 与评测协议问题，但现有输出接口不允许跨任务强排。
- **证据不足**：SAM 3D、追踪器组合、ViTPose/Sapiens/MoGe 组合。问题不是入口不存在，而是当前类别粒度过粗或关键 checkpoint/runtime 字段不完整。

**Clover Phase A 优先 5 个可执行模型：**
1. **YOLO26n (`yolo26n.pt`, 640)** — 原生 ultrafast 检测速度下界；小模型适合 M4/单卡完整时延基线。
2. **RF-DETR-Nano (384)** — 与 YOLO26n 构成最干净的同任务 detector 对照，且官方 ONNX/TensorRT/INT8 证据较完整。
3. **SAM 3 (`facebook/sam3@3c879f3`)** — promptable image/video segmentation + tracking 的高能力参照；不把它塞进 detector 吞吐榜。
4. **PaddleOCR-VL-1.6 (`c5630ab`)** — 约 0.9B，后训练路径披露较清楚，适合作为“细粒度视觉证据是否先被压缩损伤”的 OCR/document lane。
5. **DA3-SMALL** — 官方小规模几何模型、默认 504 处理分辨率，给 depth/pose/geometry 一条资源可承受的物理空间参照；Phase A 不优先加载 1.15B GIANT。

`DINOv3-B/16` 或 `PE-Core-S16-384` 建议作为后续 **representation-control lane**：先冻结 linear probe/shallow head、feature layer 和训练预算，再讨论 frozen encoder 的广义视觉能力。

### 统一 harness 与压缩损伤口径

每个实际执行 checkpoint 同时记录：**权重文件哈希/revision、模型/processor 代码 revision、许可证、原始输入字节、decode、resize/tokenize、帧率/采样策略、视觉 token/feature 数、model forward/generate、postprocess/NMS/rotation-retry/layout assembly、输出长度、batch、dtype/量化/校准集、峰值内存、P50/P95/P99 wall-clock 与质量指标**。厂商 T4/H200/RTX 数字只保留作外部参照；Clover 的 M4/5090/A100 必须独立测完整 `input/decode → preprocess → model → postprocess → usable output`。

首轮 token/resolution/frame/quantization/streaming 消融不能只看平均 AP/Overall：至少同时看 **小物体、长尾/细粒度、OCR 小字、mask 边界、遮挡后 re-entry/identity、稀有事件**，并做 **equal-byte / equal-latency** 控制。若压缩只在平均指标上“近似无损”却系统性删除这些证据，不得标为 Clover 的等价加速。

## 目标对照（2026-10-26）

| 用户要求 | 当前证据 | 审计状态 |
|---|---|---|
| 前沿/相关/交叉研究继续补充 | 新增 300 篇此前未引用论文、314 篇书目核验（313 arXiv + 1 PMLR）；14 条交叉桥接、7 个可证伪问题 | 已补；不是全部候选/全部全文 |
| 调研完整全面 | [二十类能力矩阵](01-research/perception-and-identifiability.md#core-vision-frontier)逐项标出强/部分/薄与缺口；空间状态与事件视觉为部分/薄，其余多项为部分 | 覆盖完整；深度未闭合 |
| 内容更新到现在 | 研究检索窗口仍截至 2026-10-25；artifact 官方 config/model card/runtime 账本核验到 2026-10-26 | artifact 已刷新；会议/论文全目录仍未取完 |
| 识别图片 | [分类/开放词汇/长尾/检测/分割/OCR/动作/指代/计数/姿态/关系对照](01-research/perception-and-identifiability.md#recognition-comparison) | 已覆盖；开放世界/新概念仍缺；指标不可跨任务 |
| 追踪目标 | [点/框/掩码/VOS/全景/3D/长时平面/失败恢复对照](01-research/perception-and-identifiability.md#tracking-comparison)；SAMURAI、MOTIP2、UGO、SAM3RL、When Trackers Fail、GOT-Edit、SAM-H | 已覆盖；长期身份/安全保证仍缺；指标不可跨层比较 |
| 单一模型多能力 | [统一视觉模型同协议比较](01-research/perception-and-identifiability.md#unified-model-comparison)：Pix2Seq/OneFormer/SAM 3/WeVisOne-VL/WOW-Seg/YOLO26/PE/V-JEPA 2 实际共享的权重、接口与训练 | 没有任何模型通过单权重/单前向/二十类能力验收；本轮明确不同 artifact 类别不能跨任务强排 |
| 纯视觉 AGI | [V0–V3 × L0–L4 声称审计](01-research/learning-and-data.md#pure-vision-provenance-audit)：仅 MAE/DINOv3/StreamMAE/WebSSL/MoSA 接近 V0/L0；追踪/OCR/3D/可供性/主动视觉均依赖 L1–L4 | 已有强证据；语言/教师/合成数据仍未分离干净 |
| 原生 ultrafast | YOLO26、RF-DETR、DEIM、EfficientViT、RPFQ-ViT、Bifocal、StreamAhead、LiFR-Seg、Realtime-Bench；[时延声明审计](01-research/foundation-models-and-systems.md#latency-claim-audit)；本轮区分外部模型侧延迟与 Clover E2E | 机制与系统证据齐；无 Clover 端到端实测 |
| 广义理解 | 世界模型、记忆、主动视觉、关系/可供性、3D/4D、因果/物理、行动用途；物理/因果已补单图质量、iSEE/PersistBench、Causal-JEPA/ITC、物理一致性可测量基准（World Models' Last Exam 57.76/100）、动作-后果世界模型（DR-WM/STRIKE/P3Sim/Mirage2Matter）、触觉/WiFi 反证、U15 协议；[六条竞争路线](01-research/research-questions.md#competing-pure-vision-routes)与判别实验矩阵 | 方向齐；真实相机唯一可识别性仍缺 |
| 证据可信 | 313 个书目核验 arXiv ID 全部可解析（另 1 篇 PMLR-only）；来源块 337 个唯一 URL（313 arXiv + 24 artifact/record）；本轮点追踪/物体位姿/3D 占据/物理世界模型/评测新增的 72 个引用/项目/代码 URL 全部 200；359 条相对链接 0 缺失（136 个显式锚点 + 标题锚点，含修正 1 处同目录 `../` 误写）；表格 0 结构错误；12 类 artifact 已按“类别→代表 checkpoint→字段→比较资格”重审 | 链接/结构与 artifact 元数据已补；内容级旧主张和 Clover 实测未全审 |
| 预训练-评测重叠 | [10 组披露级审计](01-research/evaluation-and-benchmarks.md#overlap-audit)：WOW-Seg 训练 LVIS/PACO 后在同集报告 SOTA 已纠正；PaddleOCR 内部 hard-case mining、SAM 3/SA-Co、dots.ocr/XDocParse 同源风险已记录；MoSA 明确无重叠 | 多数缺独立第三方 split/重叠声明 |
| 未闭合 | 101 新增 + 1 既有 / 314 正文级选读；ICLR/ECCV/NeurIPS 全目录；335 个旧 ID 已做书目+18 块题名核对，逐句数字/主张未全审；严格视觉隐藏态/因果恢复；预训练-评测重叠已做 10 组披露审计但未独立复核；artifact 未做 Clover 权重加载、统一量化与完整 E2E | 仍开放 |

## Current reading route

[Contract](SSOT.md) → [research map and current queue](01-research/README.md#current-collection-queue) → [core CV frontier](01-research/perception-and-identifiability.md#core-vision-frontier) → [ultrafast systems evidence](01-research/foundation-models-and-systems.md#ultrafast-systems-frontier) → [research questions](01-research/research-questions.md#frontier-synthesis-2026-10) → the relevant topic. [`01-research/sources-and-resources.md`](01-research/sources-and-resources.md#core-vision-source-frontier) owns the 2026-10 source batch; [`PROCESS.md`](PROCESS.md) owns lifecycle/templates; [`AGENTS.md`](AGENTS.md) defines document ownership.

## Remaining cross-topic collection questions

- Core CV: single-weight vs separately trained unified models under matched data/compute; open-world recognition beyond CLIP-style language priors; long-tail/fine-grained/scale robustness; action and referring/grounding as distinct supervision conditions.
- Identity: failure-aware tracking vs stronger propagation at equal memory; long-horizon re-entry, wrong-memory write-back and correction harm; point/box/mask/physical-entity identity levels.
- Speed: token/resolution/quantization/streaming compression damaging OCR, small objects, boundaries, re-detection and rare events before average QA; wall-clock vs idealized clocks.
- Observation: visual-token/FPS budget versus physical-state evidence; hidden physical variables versus appearance priors; real-world identifiability under image-formation noise.
- State/memory: equal-byte long context, persistent state and original-evidence retrieval; compression reversibility; uncertainty and belief revision after quantization or pruning.
- Learning: visual SSL vs language supervision under matched data; frozen/adapted backbone attribution; human/robot/simulator mixtures; failure/recovery data; reward/verifier reliability; post-training preservation of memory, physics and calibration.
- Action/open world: model-class misspecification, regime changes, safe irreversible probing, embodiment changes and social permission.
- Systems: streaming encode/cache invalidation; fast-control/slow-reasoner synchronization; end-to-end latency; runtime drift; API/checkpoint/harness provenance.
- Validation: independent splits and matched baselines; simulator/solver shortcuts; sim-to-sim versus real transfer; rollback and persistent-state corruption.

These remain research questions, not a declared collection failure or an instruction to invent an architecture. Individual evidence dates remain in their topic records. Newly registered papers and metadata retrieval do not revalidate all inherited vendor/frontier claims.

## Stage-1 exit condition

Stage 2 Analysis becomes primary when a new agent can identify:

1. major competing scientific directions and strongest representatives;
2. source/evidence and learning provenance;
3. observation assumptions and world variables represented;
4. identifiability and sufficiency assumptions;
5. likely state-aliasing and abstraction failures;
6. information-gathering / open-world epistemic behavior;
7. hypothesis/model-class and falsification assumptions;
8. exact foundation backbone/artifact when used;
9. architecture/token/context/cache assumptions where material;
10. pretraining, post-training stages, data, on/off-policy regime and reward/teacher provenance;
11. which modules were frozen/updated and action representation where relevant;
12. runtime/kernel/harness/tool assumptions;
13. deployment/runtime hardware constraints;
14. validation evidence level (`EV0–EV8`);
15. datasets/benchmarks that discriminate claims;
16. methods deserving structured method sections in the canonical topics.

### Exit-condition audit — 2026-10-26

| # | Condition | Current evidence | Status | Remaining |
|---|---|---|---|---|
| 1 | Competing directions + strongest representatives | [Six routes](01-research/research-questions.md#competing-pure-vision-routes)、[recognition](01-research/perception-and-identifiability.md#recognition-comparison)与[tracking](01-research/perception-and-identifiability.md#tracking-comparison)对照、[unified models](01-research/perception-and-identifiability.md#unified-model-comparison) | Covered | 仍需按同一协议做定量 head-to-head |
| 2 | Source/evidence + learning provenance | [V0–V3 × L0–L4 audit](01-research/learning-and-data.md#pure-vision-provenance-audit)；313 arXiv + 1 PMLR 书目 | Partial | 101 新增 + 1 既有 / 314 正文级；多篇训练混合/许可未披露 |
| 3 | Observation assumptions + world variables | 成像物理/可观测性地图；[hidden-state](01-research/perception-and-identifiability.md#strict-hidden-state-2026) | Covered | 新方法仍需逐篇核对成像条件 |
| 4 | Identifiability + sufficiency assumptions | 可识别性/充分性章节；单图质量、iSEE、PersistBench、ViWi 反证；[U15 真实相机协议](01-research/evaluation-and-benchmarks.md#topic-docs-evaluation-understanding-battery)已定义 | Partial | 协议未执行；真实相机唯一识别仍未闭合 |
| 5 | Aliasing + abstraction failures | A1–A6 别名分类；[metric failure audit](01-research/evaluation-and-benchmarks.md#evaluation-frontier) | Covered | 新任务需补别名实验 |
| 6 | Information-gathering + open-world epistemics | 主动视觉、VoI、RFL/EgoReveal/SpatialScout | Partial | 成本/风险/不可逆联合优化与真实机器人缺失 |
| 7 | Hypothesis/model-class + falsification | 模型发现、Causal-JEPA、ITC、Axiomatic World Modeling | Partial | 真实视觉的模型失配/新机制检验缺 |
| 8 | Exact backbone/artifact | [12 类官方 artifact 可比性账本](#visual-artifact-comparability-ledger-2026-10-26)已区分代表 checkpoint、参数/输入、训练来源、runtime 与比较资格；明确“12 类入口 ≠ 12 个模型” | Partial | 多数权重未由 Clover 实载；部分组仍缺 exact checkpoint hash、官方量化和完整 E2E |
| 9 | Architecture/token/context/cache assumptions | SAM3/SAM3D/DA3/StreamAhead/Bifocal 等 | Partial | 统一模型的 token/cache 账本未全 |
| 10 | Pretraining/post-training/data/reward provenance | 监督来源二维表；[overlap audit](01-research/evaluation-and-benchmarks.md#overlap-audit)；本轮补 PaddleOCR continued pretraining→SFT→RL、olmOCR SFT→GRPO、DA3 public-academic-data 等公开路径 | Partial | 多数训练混合、reward/teacher、split 仍未披露到可复现粒度 |
| 11 | Frozen/updated modules + action representation | SAMURAI/SAM3RL/GOT-Edit/UniRAP 等有说明 | Partial | 方法级 frozen/action 账本未覆盖全部 |
| 12 | Runtime/kernel/harness/tool assumptions | [latency-claim audit](01-research/foundation-models-and-systems.md#latency-claim-audit)；本轮账本已区分 T4/H200/RTX、FP16/INT8、model-side 与 pipeline latency | Partial | 无 Clover 统一 decode→preprocess→model→postprocess E2E 测量 |
| 13 | Deployment hardware constraints | M4 本机参照；外部 T4/H200/A5000/Jetson/RTX 对照 | Partial | 最终机器人/边缘硬件未定；Phase A 五候选尚未实测 |
| 14 | Validation evidence level (EV0–EV8) | EV 阶梯与外部证据等级 | **Open** | 尚无 Clover EV0–EV8 实测 |
| 15 | Discriminating datasets/benchmarks | [evaluation maps](01-research/evaluation-and-benchmarks.md#broad-visual-evaluation)、FaVOS/VC-PQ/TAPVid-MV、overlap audit；OmniDocBench 已明确按版本分 lane | Partial | 第三方独立 split 与跨任务 battery 未执行 |
| 16 | Methods deserving Stage-2 sections | 采样/追踪/OCR/3D/隐藏态/效率候选已列出 | Partial | 尚未形成 Stage-2 method 章节与消融计划 |

**审计结论：3 项 covered、12 项 partial、1 项 open。** Stage 1 仍不能交接 Stage 2：证据广度已足，但深度、精确权重实载、真实相机隐藏态、独立 overlap 与 Clover 自身 EV 证据不足。

**下一组具体动作（按优先级）：**
1. 正文级选读已到 102（本批来源块可核对口径）；下一步优先补齐 ICLR/ECCV/NeurIPS 全目录与旧 ID 逐句审查。
2. **执行 artifact benchmark Phase A**：先跑 YOLO26n、RF-DETR-Nano、SAM 3、PaddleOCR-VL-1.6、DA3-SMALL；逐一保存权重哈希、环境 lock、原始输入、阶段时延、峰值内存与输出。
3. 在 Phase A 上做 FP/BF16→官方支持量化与输入/token/frame 压缩消融，优先看小物体、OCR 小字、mask 边界、重入身份和稀有事件，而不是只看平均指标。
4. 设计真实相机隐藏态协议：质量/摩擦/永久性，配触觉/WiFi 反证与 held-out 物体。
5. 对 WOW-Seg、PaddleOCR、SAM3/SA-Co、dots.ocr 做第三方 split/独立复现，并把 OmniDocBench `v1.6_full` 与 v1.7 分 lane。
6. 把采样、追踪、OCR、3D、隐藏态、效率写成 Stage-2 method 章节与消融计划。

## Not yet demonstrated

Clover has not yet publicly demonstrated a validated general real-world visual world model, final representation, final foundation-model backbone, final training recipe, robust open-world generalization, general causal understanding, persistent long-horizon real-robot world state, validated sim2real transfer, validated original algorithm, or final hardware mapping.

These remain research targets.

## Repository structure — 2026-10-26

- Root: shared research contract, agent rules, lifecycle, global status, bilingual homepage and repository metadata.
- `01-research/`: one current file per research direction, plus its substantive overview; benchmark/source surveys remain Research material.
- `02-analysis/` through `07-reflection/`: stage-owned templates/current records. Existing candidate ideas live in Stage 4 without being adopted; directory creation is not stage completion.
- Update the existing stage/direction file in place. Keep earlier states in Git rather than dated progress files, old-path shells or an archive tree.
- This layout supersedes the previous all-root topic layout. No research claim, source-reading depth, experiment result or active-stage decision changes through the move.

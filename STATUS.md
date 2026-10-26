# Clover Status

Last updated: **2026-10-25**.

> **Research question:** How can a machine understand the real world through vision alone?
>
> **Long-term goal:** Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.

**Model objective:** pure-vision AGI with natively ultrafast computation and broad visual understanding. Core recognition, detection, segmentation, tracking and visual reading belong to the required capability scope. The [research contract](SSOT.md#model-objective-and-breadth-of-understanding) records the scope; these are targets, not achieved Clover results.

## Current project decision

**Stage 1 — Research / Survey & Evidence Collection is ACTIVE.** No representation, backbone or core algorithm is frozen. The 2026-10-15 recommendations to make Stage 2 primary remain [dated assessments in Stage 1](01-research/README.md#topic-research-stage1_final_audit_2026-10-15); they were not an approved stage transition.

The 2026-10-19 decision remains in force: the CPU-only implementation line is frozen at its current results. It resumes only after the embodied-intelligence line produces a new, complete frontier breakthrough. The main research scope is the broad visual-AGI model; a robotic brain remains a long-term application.

Apple M4 remains the local development reference; no target real robot is currently available. Final robot hardware is open. No new algorithm, experiment or deployment is reported in this update.

## 当前进展与下一步 — 2026-10-25

| 事项 | 当前证据 | 入口 |
|---|---|---|
| 研究目标 | 完整、全面、当前的前沿/相关/交叉研究；仍保持原视觉问题与 Stage 1 | [完整性审查](01-research/README.md#coverage-and-completion-audit) |
| 最新范围明确 | 纯视觉 AGI、原生 ultrafast、广义理解；识别/检测/分割/追踪/阅读等二十类能力已明确归属 | [能力地图](01-research/perception-and-identifiability.md#broad-visual-capabilities) |
| 核心视觉前沿补充（2026-10） | 新增 **290 篇此前未引用论文**、304 篇书目核验（303 arXiv + 1 PMLR）；覆盖识别/检测/分割/追踪/阅读/动作/人-物交互与人脸/表情/手势/指代/姿态/人体与手部3D/计数/几何/边界与抠图/光流与匹配/遮挡与非模态/事件视觉与异步感知/主动感知与视角规划/长视频与第一人称记忆/组合泛化与视觉推理/计数与视觉测量/空间状态与 SLAM/点追踪与 3D 运动/物体级 6-DoF 跟踪/3D 占据与场景图/部件/可供性/隐藏态与分布偏移/长尾/细粒度/尺度失败面，含 YOLO26、RF-DETR、SAM 3/3D、SAMURAI、MOTIP2、UGO、TAPFormer、M2P、CoWTracker、Track4World、MoSE3、3D SSM、Track-On-R、TrackCraft3R、TrackerSplat、RoPT、GRC-Pose、ComPose、Robust Recovery、ASM-6D、Event6D、LEGAU、DICArt、OCH3R、OccAny、OccAnyScene、VEOcc、OccTrack360、FALCON、LEXI-SG、LOST-3DSG、OP3DSG、DSG、PanoGraphGS、UniSim-SLAM、FFVO、FineHOI、HOIBlender、GraspHOI、SAGE、FreeFlow、MVLoMa、B2TFPose、OccJEPA、Amodal SAM、VolFill、NOVA3R、ChronoFuse、Event3R、E-TraMamba、R4DSG、Ledger、EgoProbe、VideoLoop、PREM、TraceViT、JRDB-AVR、DualCount、BunchCount、SVCBench、RT-Counter、DenseFace、FaceLiVTv2、EventFace、TAG、SAM 3D Body、Fast SAM 3D Body、OnlineHMR、DanceHMR、AffordAny、UniAfford、PartLLM、UniPart、FunRec、VideoMaMa++、RenderMatte、SEP-YOLO、SeeClear、OPC16K、ActiveArena、CanViT、I-Perceive、BAVO/A-FAR、Epistemic-Trap、Checkpoint-Selection、Colorist、GATE、RADC、CTTA、FORGE、PaddleOCR-VL、dots.ocr、DA3、PnP-Transformer、MEVL-STP、WOW-Seg、MoSA、GOT-Edit、RelationVGGT、UniFunc3D、StarWM、iSEE、PersistBench、Causal-JEPA；96 篇本轮新增正文级选读（另 1 篇既有引用）、1 篇既有记录深化 | [核心视觉前沿](01-research/perception-and-identifiability.md#core-vision-frontier) |
| 原生速度与跨域补充 | 新增 YOLO26/RF-DETR/DEIM 系统边界、EfficientViT、RPFQ-ViT、Bifocal、StreamAhead、TacitVLA、Realtime-Bench；主动视觉与视网膜/事件/V1 证据 | [原生速度](01-research/foundation-models-and-systems.md#ultrafast-systems-frontier) · [主动视觉](01-research/causality-and-active-perception.md#active-vision-frontier) |
| 前一批方向补充（10-19→10-25） | 首次登记 **53 篇**，深化 **1 篇**已有论文，按机制、输入/学习来源、证据和边界写回现有正文 | [交叉桥接](01-research/research-questions.md#cross-domain-research-bridges) |
| 前一批基础视觉/正式来源补充 | 在上述资料上增补 **31 条比较记录**：基础视觉/效率 16，正式会议相关/交叉研究 15；分别保留选读范围 | [固定来源与深度](01-research/sources-and-resources.md#broad-vision-sources) |
| 前沿检索 | 19 组主查询 + 动作/指代补充检索；主查询返回 2,072 条去重候选（2026-09-01→10-25）；分类公告核对到 10-23；未把所有候选声称为精读 | [来源协议](01-research/sources-and-resources.md#current-search-protocol) |
| 正式会议检索 | 六个官方目录取回 11,774 条题名、规则筛出 1,423 候选；不是全部人工筛完/全文读完 | [目录范围](01-research/sources-and-resources.md#broad-vision-sources) |
| 旧引文核查 | 335 个数字 arXiv ID 均取回书目；未据此宣布全部旧研究结论正确 | [书目边界](01-research/sources-and-resources.md#current-search-protocol) |
| 模型 artifact | 四个官方权重 revision 已读取模型卡与配置；新增 12 类官方入口仅做 HTTP/版本核对，未加载权重 | [精确版本](01-research/foundation-models-and-systems.md#current-model-artifacts) |
| 原生速度与视觉发布 | 增加完整时延/证据年龄/多能力负载口径；核对 YOLO26 paper/docs、OCR/TAP 等入口，YOLO27 仍属未发布预览 | [计算研究](01-research/foundation-models-and-systems.md#native-ultrafast-research) |
| 结构与持续维护 | 根目录跨阶段规则；调研继续按原八方向原位更新，没有新增调研文件 | [第一阶段](01-research/README.md) |

**尚未完成：** 新增 290 篇中 96 篇正文级选读，其余方法/监督/实验完整复核仍缺；统一视觉模型的同协议比较、ICLR/ECCV/CoRL 全目录（本轮只补 ICLR/ECCV/NeurIPS 2026 定向 18 篇 camera-ready）、更多正式期刊与全部旧官方 artifact 刷新；335 个旧数字 ID 的书目检查已完成，18 个单 ID 结构化块题名核对完成（修正 2 处题名形式）；逐句数字/主张仍未全审；严格视觉隐藏态、真实因果识别和未知未来任务证据恢复；预训练-评测数据重叠多不可核对。当前未通过全范围完整性核查，目标继续推进，没有宣布“全面完成”或推进阶段。

## 目标对照（2026-10-25）

| 用户要求 | 当前证据 | 审计状态 |
|---|---|---|
| 前沿/相关/交叉研究继续补充 | 新增 290 篇此前未引用论文、304 篇书目核验（303 arXiv + 1 PMLR）；14 条交叉桥接、6 个可证伪问题 | 已补；不是全部候选/全部全文 |
| 调研完整全面 | [二十类能力矩阵](01-research/perception-and-identifiability.md#core-vision-frontier)逐项标出强/部分/薄与缺口；空间状态与事件视觉为部分/薄，其余多项为部分 | 覆盖完整；深度未闭合 |
| 内容更新到现在 | 2026-10-25；arXiv 09-01→10-25；ICLR/ECCV/NeurIPS 2026 camera-ready 定向 18 篇；公告到 10-23 | 已更新；全目录未取 |
| 识别图片 | [分类/开放词汇/长尾/检测/分割/OCR/动作/指代/计数/姿态/关系对照](01-research/perception-and-identifiability.md#recognition-comparison) | 已覆盖；开放世界/新概念仍缺；指标不可跨任务 |
| 追踪目标 | [点/框/掩码/VOS/全景/3D/长时平面/失败恢复对照](01-research/perception-and-identifiability.md#tracking-comparison)；SAMURAI、MOTIP2、UGO、SAM3RL、When Trackers Fail、GOT-Edit、SAM-H | 已覆盖；长期身份/安全保证仍缺；指标不可跨层比较 |
| 单一模型多能力 | [统一视觉模型同协议比较](01-research/perception-and-identifiability.md#unified-model-comparison)：Pix2Seq/OneFormer/SAM 3/WeVisOne-VL/WOW-Seg/YOLO26/PE/V-JEPA 2 实际共享的权重、接口与训练 | 没有任何模型通过单权重/单前向/二十类能力验收 |
| 纯视觉 AGI | [V0–V3 × L0–L4 声称审计](01-research/learning-and-data.md#pure-vision-provenance-audit)：仅 MAE/DINOv3/StreamMAE/WebSSL/MoSA 接近 V0/L0；追踪/OCR/3D/可供性/主动视觉均依赖 L1–L4 | 已有强证据；语言/教师/合成数据仍未分离干净 |
| 原生 ultrafast | YOLO26、RF-DETR、DEIM、EfficientViT、RPFQ-ViT、Bifocal、StreamAhead、LiFR-Seg、Realtime-Bench；[时延声明审计](01-research/foundation-models-and-systems.md#latency-claim-audit) | 机制与系统证据齐；无 Clover 端到端实测 |
| 广义理解 | 世界模型、记忆、主动视觉、关系/可供性、3D/4D、因果/物理、行动用途；物理/因果已补单图质量、iSEE/PersistBench、Causal-JEPA/ITC、触觉/WiFi 反证、U15 协议；[六条竞争路线](01-research/research-questions.md#competing-pure-vision-routes)与判别实验矩阵 | 方向齐；真实相机唯一可识别性仍缺 |
| 证据可信 | 303 个书目核验 arXiv ID 全部可解析（另 1 篇 PMLR-only）；来源块 327 个唯一 URL（303 arXiv + 24 artifact/record）；本轮点追踪/物体位姿/3D 占据/评测新增的 52 个引用/项目/代码 URL 全部 200；152 条内部链接 0 缺失（153 个显式锚点）；表格 0 结构错误 | 链接/结构已审计；内容级旧主张未全审 |
| 预训练-评测重叠 | [10 组披露级审计](01-research/evaluation-and-benchmarks.md#overlap-audit)：WOW-Seg 训练 LVIS/PACO 后在同集报告 SOTA 已纠正；PaddleOCR 内部 hard-case mining、SAM 3/SA-Co、dots.ocr/XDocParse 同源风险已记录；MoSA 明确无重叠 | 多数缺独立第三方 split/重叠声明 |
| 未闭合 | 96 新增 + 1 既有 / 304 正文级选读（本批来源块逐行可核对；此前 120 的口径把上一批精读并入本批分子，已改为单批计数、跨批不合并）；ICLR/ECCV/NeurIPS 全目录；335 个旧 ID 已做书目+18 块题名核对，逐句数字/主张未全审；严格视觉隐藏态/因果恢复；预训练-评测重叠已做 10 组披露审计但未独立复核 | 仍开放 |

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

### Exit-condition audit — 2026-10-25

| # | Condition | Current evidence | Status | Remaining |
|---|---|---|---|---|
| 1 | Competing directions + strongest representatives | [Six routes](01-research/research-questions.md#competing-pure-vision-routes)、[recognition](01-research/perception-and-identifiability.md#recognition-comparison)与[tracking](01-research/perception-and-identifiability.md#tracking-comparison)对照、[unified models](01-research/perception-and-identifiability.md#unified-model-comparison) | Covered | 仍需按同一协议做定量 head-to-head |
| 2 | Source/evidence + learning provenance | [V0–V3 × L0–L4 audit](01-research/learning-and-data.md#pure-vision-provenance-audit)；303 arXiv + 1 PMLR 书目 | Partial | 96 新增 + 1 既有 / 304 正文级；多篇训练混合/许可未披露 |
| 3 | Observation assumptions + world variables | 成像物理/可观测性地图；[hidden-state](01-research/perception-and-identifiability.md#strict-hidden-state-2026) | Covered | 新方法仍需逐篇核对成像条件 |
| 4 | Identifiability + sufficiency assumptions | 可识别性/充分性章节；单图质量、iSEE、PersistBench、ViWi 反证；[U15 真实相机协议](01-research/evaluation-and-benchmarks.md#topic-docs-evaluation-understanding-battery)已定义 | Partial | 协议未执行；真实相机唯一识别仍未闭合 |
| 5 | Aliasing + abstraction failures | A1–A6 别名分类；[metric failure audit](01-research/evaluation-and-benchmarks.md#evaluation-frontier) | Covered | 新任务需补别名实验 |
| 6 | Information-gathering + open-world epistemics | 主动视觉、VoI、RFL/EgoReveal/SpatialScout | Partial | 成本/风险/不可逆联合优化与真实机器人缺失 |
| 7 | Hypothesis/model-class + falsification | 模型发现、Causal-JEPA、ITC、Axiomatic World Modeling | Partial | 真实视觉的模型失配/新机制检验缺 |
| 8 | Exact backbone/artifact | [12 个视觉 artifact 已核验](01-research/foundation-models-and-systems.md#current-model-artifacts)：参数/分辨率/上下文/许可 | Partial | 未加载权重；训练配方/量化/端到端未核 |
| 9 | Architecture/token/context/cache assumptions | SAM3/SAM3D/DA3/StreamAhead/Bifocal 等 | Partial | 统一模型的 token/cache 账本未全 |
| 10 | Pretraining/post-training/data/reward provenance | 监督来源二维表；[overlap audit](01-research/evaluation-and-benchmarks.md#overlap-audit) | Partial | 多数训练混合、reward/teacher、split 未披露 |
| 11 | Frozen/updated modules + action representation | SAMURAI/SAM3RL/GOT-Edit/UniRAP 等有说明 | Partial | 方法级 frozen/action 账本未覆盖全部 |
| 12 | Runtime/kernel/harness/tool assumptions | [latency-claim audit](01-research/foundation-models-and-systems.md#latency-claim-audit) | Partial | 无 Clover 端到端 runtime/harness 测量 |
| 13 | Deployment hardware constraints | M4 本机参照；外部 T4/H200/A5000/Jetson 对照 | Partial | 最终机器人/边缘硬件未定 |
| 14 | Validation evidence level (EV0–EV8) | EV 阶梯与外部证据等级 | **Open** | 尚无 Clover EV0–EV8 实测 |
| 15 | Discriminating datasets/benchmarks | [evaluation maps](01-research/evaluation-and-benchmarks.md#broad-visual-evaluation)、FaVOS/VC-PQ/TAPVid-MV、overlap audit | Partial | 第三方独立 split 与跨任务 battery 未执行 |
| 16 | Methods deserving Stage-2 sections | 采样/追踪/OCR/3D/隐藏态/效率候选已列出 | Partial | 尚未形成 Stage-2 method 章节与消融计划 |

**审计结论：3 项 covered、12 项 partial、1 项 open。** Stage 1 仍不能交接 Stage 2：证据广度已足，但深度、精确 artifact、真实相机隐藏态、独立 overlap 与 Clover 自身 EV 证据不足。

**下一组具体动作（按优先级）：**
1. 正文级选读已到 97（本批来源块可核对口径）；下一步优先补齐 ICLR/ECCV/NeurIPS 全目录与旧 ID 逐句审查。
2. 为 12 个关键 artifact 补权重/config/license/参数量/分辨率/上下文/导出后端。
3. 设计真实相机隐藏态协议：质量/摩擦/永久性，配触觉/WiFi 反证与 held-out 物体。
4. 对 WOW-Seg、PaddleOCR、SAM3/SA-Co、dots.ocr 做第三方 split/独立复现。
5. 补 ICLR/ECCV/NeurIPS 全目录与更多正式期刊。
6. 把采样、追踪、OCR、3D、隐藏态、效率写成 Stage-2 method 章节与消融计划。

## Not yet demonstrated


Clover has not yet publicly demonstrated a validated general real-world visual world model, final representation, final foundation-model backbone, final training recipe, robust open-world generalization, general causal understanding, persistent long-horizon real-robot world state, validated sim2real transfer, validated original algorithm, or final hardware mapping.

These remain research targets.

## Repository structure — 2026-10-25

- Root: shared research contract, agent rules, lifecycle, global status, bilingual homepage and repository metadata.
- `01-research/`: one current file per research direction, plus its substantive overview; benchmark/source surveys remain Research material.
- `02-analysis/` through `07-reflection/`: stage-owned templates/current records. Existing candidate ideas live in Stage 4 without being adopted; directory creation is not stage completion.
- Update the existing stage/direction file in place. Keep earlier states in Git rather than dated progress files, old-path shells or an archive tree.
- This layout supersedes the previous all-root topic layout. No research claim, source-reading depth, experiment result or active-stage decision changes through the move.

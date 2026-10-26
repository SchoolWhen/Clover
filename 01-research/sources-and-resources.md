<a id="top"></a>

# 调研方向：论文来源、代码、数据与资源

Maintained: **2026-10-25** · Document stage: **1 — Research** ([status](../STATUS.md)).

Primary-source map, papers, code, datasets and discovery signals. Read evidence labels and source dates before using any claim.

This is the canonical topic document. Update it in place; source-level dates and reading-depth labels below qualify the evidence, not the maintenance date.

<!-- BEGIN current-search-protocol -->
<a id="current-search-protocol"></a>

## 当前检索范围、入选规则与书目核验

核验日：**2026-10-25（Asia/Shanghai）**。本次同时补经典/相关/交叉研究与当前前沿；来源优先级为论文原文、会议论文库、作者项目/代码和精确官方模型卡。公司材料保留 `OFFICIAL_*` 身份；摘要和下载到本地的全文不自动升级为完整精读。

**收录标准：** 直接约束视觉观测、可识别性、表示/记忆、物理因果、主动采证、学习、决策效用或评估条件；或提供能够区分竞争解释的交叉领域机制。**不直接升级：** 只有名称相似的文本世界模型、仅行业宣言、无公开条件的排名、医疗任务成绩对机器人/临床的外推、以及未知额外输入的“纯视觉”说法。

### 当前前沿的可复查检索

| 一手检索 | 完整查询 | 返回记录数 | 公共接口 |
|---|---|---|---|
| Robotics | `cat:cs.RO AND submittedDate:[202610150000 TO 202610252359]` | 514 / 接口 total=514 | [arXiv API](https://export.arxiv.org/api/query?search_query=cat%3Acs.RO+AND+submittedDate%3A%5B202610150000+TO+202610252359%5D&start=0&max_results=1000&sortBy=submittedDate&sortOrder=descending) |
| Vision | `cat:cs.CV AND submittedDate:[202610150000 TO 202610252359]` | 981 / 接口 total=981 | [arXiv API](https://export.arxiv.org/api/query?search_query=cat%3Acs.CV+AND+submittedDate%3A%5B202610150000+TO+202610252359%5D&start=0&max_results=1000&sortBy=submittedDate&sortOrder=descending) |
| AI/ML 交叉 | `(cat:cs.AI OR cat:cs.LG) AND submittedDate:[202610150000 TO 202610252359] AND (all:"world model" OR all:"causal representation" OR all:"partial observability" OR all:"embodied" OR all:"physical reasoning" OR all:"system identification" OR all:"active perception")` | 116 / 接口 total=116 | [arXiv API](https://export.arxiv.org/api/query?search_query=%28cat%3Acs.AI+OR+cat%3Acs.LG%29+AND+submittedDate%3A%5B202610150000+TO+202610252359%5D+AND+%28all%3A%22world+model%22+OR+all%3A%22causal+representation%22+OR+all%3A%22partial+observability%22+OR+all%3A%22embodied%22+OR+all%3A%22physical+reasoning%22+OR+all%3A%22system+identification%22+OR+all%3A%22active+perception%22%29&start=0&max_results=1000&sortBy=submittedDate&sortOrder=descending) |

三组共 1,611 条返回记录，按论文 ID 去重后 **1,482** 条（上一轮短窗口批次）。本轮另做 19 组主查询（`2026-09-01`→`2026-10-25`）加动作/指代/部件/点追踪/物体位姿/3D 占据补充检索：主查询原始 2,170 条、去重 **2,072** 条；合计筛出 304 篇做书目核验（303 arXiv + 1 PMLR-only），其中 290 篇此前未引用；查询组、计数与登记见[核心视觉来源批次](#core-vision-source-frontier)。当前分类列表也核对了 [cs.RO recent](https://arxiv.org/list/cs.RO/recent) 与 [cs.CV recent](https://arxiv.org/list/cs.CV/recent)：最新可见公告批次为 **2026-10-23**。公告日期、初次提交日期、修订日期和本项目核验日期不是一回事。

关键词排序只用于找候选，不能充当全部论文的人类精读或排除判决。上一轮自动高分候选有 81 条；另用几何、物性、记忆、泛化、风险等题名检索补查，发现低分但直接相关的工作。本节登记的入选论文均人工检查了摘要，部分另核读方法/监督/局限段。未将 1,482 条或 2,072 条全部声称为纳入文献或精读文献。

### 既有记录书目检查

基线提交 `fae924516c5bc3862125cd67d57b3850f3fdf462` 的九份调研正文，以 `arxiv.org/(abs|html|pdf)/(数字ID)` 提取并去掉版本号，得到 **335 个数字格式 arXiv ID**；全部从一手 API 返回了题名、作者、初次提交、当前版本/修订日期与摘要。批次每组不超过 70 个 ID，按 `id_list` 读取，没有以检索命中率替代结论核查。此项检查证明编号可追溯，**不证明** 全部旧综述句子、数值、理论条件、代码或部署能力正确；旧式 ID、非 arXiv 原文与所有官方项目的新鲜度仍需另查。

**2026-10-25 内容级抽样审计（新增）：** 对含单个旧 arXiv ID 的结构化来源块做“ID → 题名 → 链接”一致性核对：18 个块中 15 个题名精确或强匹配，3 个未写英文引题但 ID 解析到正确论文；发现并修正 2 个题名形式错误（`Clear Grasp`→`ClearGrasp`；`Multimap`→`Multi-Map`）。其余旧记录多为表格/多引用块，数字与主张来自正文或会议页，**尚未**逐句核对；本项不是“335 条全部内容级验证完成”。

当前书目示例应使用精确题名：`2610.23615` 返回 **Beyond Action Prediction: Learning Search-Free Planning in Latent Space**（旧简称 HIJP 仅作别名）；`2610.15429` 返回 **World Modeling through Spectral Alignment**（旧简称 SpecWM 不是完整题名）。不得用简称猜测作者、版本或证明内容。

### 上一轮新增与深化文献索引（2026-10-15→10-19）

下表共 54 条：53 篇首次登记；GNS（`2002.09405`）原已登记，本轮将摘要级记录深化到方法与监督边界选读，不重复计入新增论文。2026-10-25 的 290 篇新批次见[核心视觉来源批次](#core-vision-source-frontier)，两批不合并计数。

| 原始提交 / 当前返回版本 | 题名与一手来源 | 方向正文 | 阅读深度 |
|---|---|---|---|
| 2025-01-21 / `2501.12387v1` | [Continuous 3D Perception Model with Persistent State](https://arxiv.org/abs/2501.12387v1) | [perception-and-identifiability.md](perception-and-identifiability.md#current-cross-domain-evidence) | 正文选读：方法、监督或局限段；未复核全部实验/证明 |
| 2024-10-04 / `2410.03825v2` | [MonST3R: A Simple Approach for Estimating Geometry in the Presence of Motion](https://arxiv.org/abs/2410.03825v2) | [perception-and-identifiability.md](perception-and-identifiability.md#current-cross-domain-evidence) | 正文选读：方法、监督或局限段；未复核全部实验/证明 |
| 2019-06-04 / `1906.01563v3` | [Hamiltonian Neural Networks](https://arxiv.org/abs/1906.01563v3) | [representation-and-memory.md](representation-and-memory.md#current-cross-domain-evidence) | 正文选读：方法、监督或局限段；未复核全部实验/证明 |
| 2020-03-10 / `2003.04630v2` | [Lagrangian Neural Networks](https://arxiv.org/abs/2003.04630v2) | [representation-and-memory.md](representation-and-memory.md#current-cross-domain-evidence) | 正文选读：方法、监督或局限段；未复核全部实验/证明 |
| 2017-12-27 / `1712.09707v2` | [Deep learning for universal linear embeddings of nonlinear dynamics](https://arxiv.org/abs/1712.09707v2) | [representation-and-memory.md](representation-and-memory.md#current-cross-domain-evidence) | 正文选读：方法、监督或局限段；未复核全部实验/证明 |
| 2000-04-24 / `physics/0004057v1` | [The information bottleneck method](https://arxiv.org/abs/physics/0004057v1) | [representation-and-memory.md](representation-and-memory.md#current-cross-domain-evidence) | 摘要与书目核验 |
| 2015-09-11 / `1509.03580v1` | [Discovering governing equations from data: Sparse identification of nonlinear dynamical systems](https://arxiv.org/abs/1509.03580v1) | [causality-and-active-perception.md](causality-and-active-perception.md#current-cross-domain-evidence) | 正文选读：方法、监督或局限段；未复核全部实验/证明 |
| 2023-10-13 / `2310.08887v2` | [METRA: Scalable Unsupervised RL with Metric-Aware Abstraction](https://arxiv.org/abs/2310.08887v2) | [causality-and-active-perception.md](causality-and-active-perception.md#current-cross-domain-evidence) | 正文选读：方法、监督或局限段；未复核全部实验/证明 |
| 2024-02-23 / `2402.15567v2` | [Foundation Policies with Hilbert Representations](https://arxiv.org/abs/2402.15567v2) | [causality-and-active-perception.md](causality-and-active-perception.md#current-cross-domain-evidence) | 正文选读：方法、监督或局限段；未复核全部实验/证明 |
| 2024-09-18 / `2409.12192v2` | [DynaMo: In-Domain Dynamics Pretraining for Visuo-Motor Control](https://arxiv.org/abs/2409.12192v2) | [learning-and-data.md](learning-and-data.md#current-cross-domain-evidence) | 摘要与书目核验 |
| 2019-07-05 / `1907.02893v3` | [Invariant Risk Minimization](https://arxiv.org/abs/1907.02893v3) | [learning-and-data.md](learning-and-data.md#current-cross-domain-evidence) | 摘要与书目核验 |
| 2020-07-02 / `2007.01434v1` | [In Search of Lost Domain Generalization](https://arxiv.org/abs/2007.01434v1) | [evaluation-and-benchmarks.md](evaluation-and-benchmarks.md#current-cross-domain-evidence) | 正文选读：方法、监督或局限段；未复核全部实验/证明 |
| 2020-12-14 / `2012.07421v3` | [WILDS: A Benchmark of in-the-Wild Distribution Shifts](https://arxiv.org/abs/2012.07421v3) | [evaluation-and-benchmarks.md](evaluation-and-benchmarks.md#current-cross-domain-evidence) | 正文选读：方法、监督或局限段；未复核全部实验/证明 |
| 2020-06-13 / `2006.07710v2` | [The Pitfalls of Simplicity Bias in Neural Networks](https://arxiv.org/abs/2006.07710v2) | [evaluation-and-benchmarks.md](evaluation-and-benchmarks.md#current-cross-domain-evidence) | 摘要与书目核验 |
| 2020-02-21 / `2002.09405v2` | [Learning to Simulate Complex Physics with Graph Networks](https://arxiv.org/abs/2002.09405v2) | [perception-and-identifiability.md](perception-and-identifiability.md#current-cross-domain-evidence) | 正文选读：方法、监督或局限段；未复核全部实验/证明 |
| 2020-10-18 / `2010.08895v3` | [Fourier Neural Operator for Parametric Partial Differential Equations](https://arxiv.org/abs/2010.08895v3) | [perception-and-identifiability.md](perception-and-identifiability.md#current-cross-domain-evidence) | 正文选读：方法、监督或局限段；未复核全部实验/证明 |
| 2026-08-31 / `2608.30320v1` | [On the Design of Qwen3.8-Next Architecture: Evaluation, Efficiency, and Training Stability](https://arxiv.org/abs/2608.30320v1) | [foundation-models-and-systems.md](foundation-models-and-systems.md#current-cross-domain-evidence) | 摘要与书目核验 |
| 2026-10-22 / `2610.31645v1` | [OmniRay: Camera-Agnostic Monocular 3D Reconstruction with Composite Ray Fields](https://arxiv.org/abs/2610.31645v1) | [perception-and-identifiability.md](perception-and-identifiability.md#current-cross-domain-evidence) | 摘要与书目核验 |
| 2026-10-22 / `2610.31635v1` | [HiP3R: Hierarchical Pose Graphs for Long-Horizon 3D Reconstruction](https://arxiv.org/abs/2610.31635v1) | [perception-and-identifiability.md](perception-and-identifiability.md#current-cross-domain-evidence) | 摘要与书目核验 |
| 2026-10-22 / `2610.31320v1` | [Stream4D: Streaming 4D Reconstruction with Training-free Motion Decoupling via Causal KV-Cache Attention](https://arxiv.org/abs/2610.31320v1) | [perception-and-identifiability.md](perception-and-identifiability.md#current-cross-domain-evidence) | 摘要与书目核验 |
| 2026-10-22 / `2610.30781v1` | [DeXplicit: Making Physical State Explicit in Dexterous Manipulation World Models](https://arxiv.org/abs/2610.30781v1) | [perception-and-identifiability.md](perception-and-identifiability.md#current-cross-domain-evidence) | 正文选读：方法、监督或局限段；未复核全部实验/证明 |
| 2026-10-22 / `2610.30988v1` | [In-Context Learning World Models for Robot Dual-Arm Manipulation of Soft Garment with Partial Observations](https://arxiv.org/abs/2610.30988v1) | [perception-and-identifiability.md](perception-and-identifiability.md#current-cross-domain-evidence) | 摘要与书目核验 |
| 2026-10-16 / `2610.22827v1` | [DefFlow: Goal-Conditioned Deformable Object Manipulation using 3D Point Flows](https://arxiv.org/abs/2610.22827v1) | [perception-and-identifiability.md](perception-and-identifiability.md#current-cross-domain-evidence) | 摘要与书目核验 |
| 2026-10-21 / `2610.30120v1` | [ALPS: Visual State Encoders for World Models](https://arxiv.org/abs/2610.30120v1) | [representation-and-memory.md](representation-and-memory.md#current-cross-domain-evidence) | 正文选读：方法、监督或局限段；未复核全部实验/证明 |
| 2026-10-22 / `2610.30724v1` | [Learning from Next-Frame Prediction: Towards Unified and Scalable Visual Representation Learning](https://arxiv.org/abs/2610.30724v1) | [representation-and-memory.md](representation-and-memory.md#current-cross-domain-evidence) | 正文选读：方法、监督或局限段；未复核全部实验/证明 |
| 2026-10-20 / `2610.28074v1` | [Slot-JEPA: Object-Structured Prediction Interfaces for Latent World Models](https://arxiv.org/abs/2610.28074v1) | [representation-and-memory.md](representation-and-memory.md#current-cross-domain-evidence) | 正文选读：方法、监督或局限段；未复核全部实验/证明 |
| 2026-10-21 / `2610.30129v1` | [Rethinking Video Autoencoders for Interactive World Models](https://arxiv.org/abs/2610.30129v1) | [representation-and-memory.md](representation-and-memory.md#current-cross-domain-evidence) | 正文选读：方法、监督或局限段；未复核全部实验/证明 |
| 2026-10-22 / `2610.31166v1` | [Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation](https://arxiv.org/abs/2610.31166v1) | [representation-and-memory.md](representation-and-memory.md#current-cross-domain-evidence) | 正文选读：方法、监督或局限段；未复核全部实验/证明 |
| 2026-10-16 / `2610.23795v1` | [Persistent Planar Memory for Video World Models](https://arxiv.org/abs/2610.23795v1) | [representation-and-memory.md](representation-and-memory.md#current-cross-domain-evidence) | 摘要与书目核验 |
| 2026-10-15 / `2610.22311v1` | [Velox: Spatial Memory Makes World Models Efficient](https://arxiv.org/abs/2610.22311v1) | [foundation-models-and-systems.md](foundation-models-and-systems.md#current-cross-domain-evidence) | 摘要与书目核验 |
| 2026-10-21 / `2610.30125v1` | [PhysiCalWorld: In-Context Physics Calibration for World Models](https://arxiv.org/abs/2610.30125v1) | [causality-and-active-perception.md](causality-and-active-perception.md#current-cross-domain-evidence) | 正文选读：方法、监督或局限段；未复核全部实验/证明 |
| 2026-10-21 / `2610.29088v1` | [Causal world models under physical parameter shifts](https://arxiv.org/abs/2610.29088v1) | [causality-and-active-perception.md](causality-and-active-perception.md#current-cross-domain-evidence) | 摘要与书目核验 |
| 2026-10-20 / `2610.28476v1` | [CLOSER: Evidence-Aware Active Visual Verification for Embodied Object-Goal Navigation](https://arxiv.org/abs/2610.28476v1) | [causality-and-active-perception.md](causality-and-active-perception.md#current-cross-domain-evidence) | 摘要与书目核验 |
| 2026-10-16 / `2610.23396v1` | [AWAM: Active Trajectory-Conditioned View Imagination for Robust Robot Manipulation](https://arxiv.org/abs/2610.23396v1) | [causality-and-active-perception.md](causality-and-active-perception.md#current-cross-domain-evidence) | 摘要与书目核验 |
| 2026-10-21 / `2610.29964v1` | [Object- and Task-Aware Active Perception for Safe Navigation of Mobile Manipulators in Semi-Static Environments](https://arxiv.org/abs/2610.29964v1) | [causality-and-active-perception.md](causality-and-active-perception.md#current-cross-domain-evidence) | 摘要与书目核验 |
| 2026-10-15 / `2610.22335v1` | [Illumination-Aware Active Perception for Spacecraft Inspection](https://arxiv.org/abs/2610.22335v1) | [causality-and-active-perception.md](causality-and-active-perception.md#current-cross-domain-evidence) | 摘要与书目核验 |
| 2026-10-22 / `2610.31617v1` | [DiffDreamer: Coupling World Models with Differentiable Simulation for Agile Quadrotor Control](https://arxiv.org/abs/2610.31617v1) | [learning-and-data.md](learning-and-data.md#current-cross-domain-evidence) | 摘要与书目核验 |
| 2026-10-22 / `2610.30814v1` | [DRILL: Training World Models to Improve Policies, Not Predict Pixels](https://arxiv.org/abs/2610.30814v1) | [learning-and-data.md](learning-and-data.md#current-cross-domain-evidence) | 摘要与书目核验 |
| 2026-10-21 / `2610.30320v1` | [Self-Distilling Future Video Representations for World Action Models](https://arxiv.org/abs/2610.30320v1) | [learning-and-data.md](learning-and-data.md#current-cross-domain-evidence) | 摘要与书目核验 |
| 2026-10-22 / `2610.31474v1` | [Skeleton-Grounded Latent Action Model for Robot World Models](https://arxiv.org/abs/2610.31474v1) | [learning-and-data.md](learning-and-data.md#current-cross-domain-evidence) | 摘要与书目核验 |
| 2026-10-19 / `2610.26855v1` | [Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience](https://arxiv.org/abs/2610.26855v1) | [learning-and-data.md](learning-and-data.md#current-cross-domain-evidence) | 摘要与书目核验 |
| 2026-10-19 / `2610.26564v1` | [PrismWAM: Decoupling State Representations in World Action Models](https://arxiv.org/abs/2610.26564v1) | [representation-and-memory.md](representation-and-memory.md#current-cross-domain-evidence) | 摘要与书目核验 |
| 2026-10-20 / `2610.28626v1` | [UniWALM: Unified World Action Language Model for Embodied Robot Control](https://arxiv.org/abs/2610.28626v1) | [representation-and-memory.md](representation-and-memory.md#current-cross-domain-evidence) | 摘要与书目核验 |
| 2026-10-20 / `2610.27890v1` | [EndoWorld-JEPA: Motion-Guided Global-Local Latent World Modeling for Endoscopic Video Representation Learning](https://arxiv.org/abs/2610.27890v1) | [learning-and-data.md](learning-and-data.md#current-cross-domain-evidence) | 摘要与书目核验 |
| 2026-10-21 / `2610.29168v1` | [How Representational Priors Shape Generalization in World Action Models](https://arxiv.org/abs/2610.29168v1) | [evaluation-and-benchmarks.md](evaluation-and-benchmarks.md#current-cross-domain-evidence) | 摘要与书目核验 |
| 2026-10-22 / `2610.31670v1` | [Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success](https://arxiv.org/abs/2610.31670v1) | [evaluation-and-benchmarks.md](evaluation-and-benchmarks.md#current-cross-domain-evidence) | 摘要与书目核验 |
| 2026-10-16 / `2610.23542v1` | [Execution Before Memory: Diagnosing Memory Failures in Video World Models](https://arxiv.org/abs/2610.23542v1) | [evaluation-and-benchmarks.md](evaluation-and-benchmarks.md#current-cross-domain-evidence) | 摘要与书目核验 |
| 2026-10-22 / `2610.31429v1` | [PhysTrace: Interpretable Temporal Evaluation of Physical Consistency in Video Generative Models](https://arxiv.org/abs/2610.31429v1) | [evaluation-and-benchmarks.md](evaluation-and-benchmarks.md#current-cross-domain-evidence) | 摘要与书目核验 |
| 2026-10-22 / `2610.31066v1` | [Dual Exam: Controlled Evaluation of Multimodal Agents and World Models](https://arxiv.org/abs/2610.31066v1) | [evaluation-and-benchmarks.md](evaluation-and-benchmarks.md#current-cross-domain-evidence) | 摘要与书目核验 |
| 2026-10-21 / `2610.30089v1` | [ProactEgoMem: Benchmarking Proactive Memory in Streaming Egocentric Video](https://arxiv.org/abs/2610.30089v1) | [evaluation-and-benchmarks.md](evaluation-and-benchmarks.md#current-cross-domain-evidence) | 摘要与书目核验 |
| 2026-10-22 / `2610.31613v1` | [Progress Probes $P^2$: Lightweight Runtime Monitoring for Vision-Language-Action Models](https://arxiv.org/abs/2610.31613v1) | [foundation-models-and-systems.md](foundation-models-and-systems.md#current-cross-domain-evidence) | 摘要与书目核验 |
| 2026-10-21 / `2610.29730v1` | [Post-hoc Epistemic Uncertainty for Vision-Language-Action Policies](https://arxiv.org/abs/2610.29730v1) | [foundation-models-and-systems.md](foundation-models-and-systems.md#current-cross-domain-evidence) | 正文选读：方法、监督或局限段；未复核全部实验/证明 |
| 2026-10-21 / `2610.29692v1` | [FlowVLA: Learning Flow-Aware Physical Completion for Quantitative Robotic Pouring](https://arxiv.org/abs/2610.29692v1) | [perception-and-identifiability.md](perception-and-identifiability.md#current-cross-domain-evidence) | 摘要与书目核验 |
| 2026-10-21 / `2610.30117v1` | [CW-WAM: A Structured Contact-Wrench World Action Model for Force-Sensitive Manipulation](https://arxiv.org/abs/2610.30117v1) | [perception-and-identifiability.md](perception-and-identifiability.md#current-cross-domain-evidence) | 摘要与书目核验 |

### 交叉领域检索与官方 artifact

定向检索串包括 `CUT3R Continuous 3D Perception Model with Persistent State`、`MonST3R Estimating Geometry in the Presence of Motion`、`METRA Metric-Aware Abstraction`、`Foundation Policies with Hilbert Representations`、`DynaMo In-Domain Dynamics Pretraining`、`Hamiltonian Neural Networks`、`Lagrangian Neural Networks`、`Fourier Neural Operator`、`Learning to Simulate Complex Physics with Graph Networks`、`Deep learning for universal linear embeddings of nonlinear dynamics`、`SINDy Discovering governing equations`、`The information bottleneck method`、`WILDS`、`DomainBed`、`Invariant Risk Minimization`。结果以精确论文 ID 回到原文；不是把搜索结果摘要当作评审结论。

交叉核对使用了 [CVPR 2025 CUT3R 会议记录](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Continuous_3D_Perception_Model_with_Persistent_State_CVPR_2025_paper.html)、[HILP 原论文](https://openreview.net/pdf?id=LhNsSaAKub)、[SINDy 正式期刊全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC4839439/)、[Koopman 正式期刊全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC6251871/)、[Simplicity Bias 会议记录](https://proceedings.neurips.cc/paper/2020/hash/6cfe0e6127fa25df2a0ef2ae1067d915-Abstract.html)。访问或缓存可用与完整精读分别登记。

另外读取了四个精确官方模型 revision 的模型卡与 `config.json`；[当前 artifact 表](foundation-models-and-systems.md#current-model-artifacts)保留 SHA、公开/托管模态差异、位置上限与许可元数据。模型配置没有被运行验证，也没有被当成视觉世界状态方案。

### 两轮尚未闭合的核查

- 六个非 arXiv 官方会议目录与部分正文已补核（见下节）；ICLR/CoRL 全目录、更多期刊/官方发布和旧 335 个数字 ID 的全部研究性主张仍未逐项完成内容级复核。
- 当前两批新增中仅部分正文级选读；模拟器版本、精确 checkpoints、完整训练混合、许可及公平预算仍待方法级核读。正文入口可访问/缓存不等于已读完。
- RGB-only 可变形/颗粒隐藏态、自然机器人视频的可识别性、压缩后的未知任务证据恢复仍是实质证据缺口；点云/力传感方案不能替代它们。
- 泛化、风险覆盖和物理因果的经典定理条件仍需继续与视觉/闭环设置逐项比对。当前覆盖表不是“全面完成”的证明。
<!-- END current-search-protocol -->

<!-- BEGIN broad-vision-sources -->
<a id="broad-vision-sources"></a>

## 广义视觉与跨领域来源：当前版本、阅读深度和检索范围

核验日：2026-10-25。依据用户明确的“纯视觉 AGI、原生 ultrafast、广义理解”，将基础识别/检测/分割/追踪/阅读与既有时空/物理/因果调研合并维护。下面 **31 条比较记录**分为 16 条基础视觉/效率与 15 条正式会议的相关/交叉研究；记录数量不等于独立完整精读或复现数量。

### 非 arXiv 官方目录检索

| 官方目录 | 获取的题名记录数 | 当前用途 |
|---|---:|---|
| [CVPR 2026](https://openaccess.thecvf.com/CVPR2026?day=all) | 4,041 | 核心视觉、物理/世界模型与评测 |
| [ICML 2026 / PMLR 306](https://proceedings.mlr.press/v306/) | 6,552 | 表示、时间/任务抽象、因果、世界模型、效率 |
| [CLeaR 2026 / PMLR 323](https://proceedings.mlr.press/v323/) | 53 | 因果可识别性、动力系统与抽象条件 |
| [AISTATS 2026 / PMLR 300](https://proceedings.mlr.press/v300/) | 588 | 部分识别、信念与离线评估 |
| [UAI 2026 / PMLR 337](https://proceedings.mlr.press/v337/) | 330 | 识别等价类、评测反例与不确定性 |
| [RSS 2026 / XXII](https://www.roboticsproceedings.org/rss22/) | 210 | 视觉记忆、视频–动作、具身模型与真实验证边界 |

合计 **11,774 条题名**；用题名正则 `world model|physical|causal|identifiab|object.perman|memory|belief|partial.observ|active.percep|inverse.render|system.identif|deformab|uncertainty|visual.odometr|slam|continual|embod|sim.to.real|counterfactual|contact|sufficien|compress|safety|explor|epistem|event.camera|tactil|affordance` 自动筛出 **1,423 条候选**。这是目录级检索池，不是 1,423 篇人工筛完/全文读完；基础 CV 又用检测、OCR、统一感知和追踪关键词定向补查，不能让初始世界模型关键词决定整个研究边界。

[CoRL 2026 官方主页](https://2026.corl.org/)在 10-19 公布[录用入口](https://2026.corl.org/program/accepted-papers)，但本次页面正文提取未得到完整内嵌列表；不采用第三方列表数充当官方已审范围。ICLR 官方目录/API本次访问受限，仍需进一步补齐其全目录和最新 CoRL 的定向内容核读。当前不声称所有会议、期刊和厂商已经穷尽刷新。

### 固定论文记录

| 固定版本/载体 | 一手论文题名与链接 | 正文归属 | 实际阅读深度 |
|---|---|---|---|
| 2206.07669v2 | [A Unified Sequence Interface for Vision Tasks](https://arxiv.org/abs/2206.07669v2) | [representation-and-memory](representation-and-memory.md#broad-vision-primary-evidence) | 正文选读：任务接口与输出编码；未复核全部实验 |
| 2112.01527v3 | [Masked-attention Mask Transformer for Universal Image Segmentation](https://arxiv.org/abs/2112.01527v3) | [perception-and-identifiability](perception-and-identifiability.md#broad-vision-primary-evidence) | 正文选读：通用架构定义及掩码注意力；未复核全部实验 |
| 2211.06220v2 | [OneFormer: One Transformer to Rule Universal Image Segmentation](https://arxiv.org/abs/2211.06220v2) | [perception-and-identifiability](perception-and-identifiability.md#broad-vision-primary-evidence) | 正文选读：任务条件训练；未复核全部实验 |
| 2110.06864v3 | [ByteTrack: Multi-Object Tracking by Associating Every Detection Box](https://arxiv.org/abs/2110.06864v3) | [perception-and-identifiability](perception-and-identifiability.md#broad-vision-primary-evidence) | 正文选读：两阶段关联；未复核全部实验 |
| 2410.11831v1 | [CoTracker3: Simpler and Better Point Tracking by Pseudo-Labelling Real Videos](https://arxiv.org/abs/2410.11831v1) | [perception-and-identifiability](perception-and-identifiability.md#broad-vision-primary-evidence) | 正文/官方说明选读：训练与在线变体；未复核全部实验 |
| 2504.05579v2 | [TAPNext: Tracking Any Point (TAP) as Next Token Prediction](https://arxiv.org/abs/2504.05579v2) | [foundation-models-and-systems](foundation-models-and-systems.md#broad-vision-primary-evidence) | 正文/官方项目选读：架构、时延口径与局限 |
| 2604.10582v1 | [TAPNext++: What's Next for Tracking Any Point (TAP)?](https://arxiv.org/abs/2604.10582v1) | [perception-and-identifiability](perception-and-identifiability.md#broad-vision-primary-evidence) | 正文/官方项目选读：方法、数据与重检测指标 |
| 2510.25257v2 | [RT-DETRv4: Painlessly Furthering Real-Time Object Detection with Vision Foundation Models](https://arxiv.org/abs/2510.25257v2) | [perception-and-identifiability](perception-and-identifiability.md#broad-vision-primary-evidence) | 正文选读：教师、配置表与时延测量；未复核全部实验 |
| 2610.31329v1 | [WeVisOne-VL: Unified Visual Perception from Objects to Pixels](https://arxiv.org/abs/2610.31329v1) | [perception-and-identifiability](perception-and-identifiability.md#broad-vision-primary-evidence) | 正文选读：§2–4、§8；未复核全部实验 |
| 2303.05499v5 | [Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection](https://arxiv.org/abs/2303.05499v5) | [perception-and-identifiability](perception-and-identifiability.md#broad-vision-primary-evidence) | 正文选读：跨模态机制与训练；未复核全部实验 |
| 2401.17270v3 | [YOLO-World: Real-Time Open-Vocabulary Object Detection](https://arxiv.org/abs/2401.17270v3) | [perception-and-identifiability](perception-and-identifiability.md#broad-vision-primary-evidence) | 正文选读：离线词汇与重参数化；未复核全部实验 |
| 2311.06242v1 | [Florence-2: Advancing a Unified Representation for a Variety of Vision Tasks](https://arxiv.org/abs/2311.06242v1) | [representation-and-memory](representation-and-memory.md#broad-vision-primary-evidence) | 正文选读：统一任务与数据说明；未复核全部实验 |
| 2502.14786v1 | [SigLIP 2: Multilingual Vision-Language Encoders with Improved Semantic Understanding, Localization, and Dense Features](https://arxiv.org/abs/2502.14786v1) | [learning-and-data](learning-and-data.md#broad-vision-primary-evidence) | 正文选读：训练目标与模型发布说明；未复核全部实验 |
| 2412.13303v2 | [FastVLM: Efficient Vision Encoding for Vision Language Models](https://arxiv.org/abs/2412.13303v2) | [foundation-models-and-systems](foundation-models-and-systems.md#broad-vision-primary-evidence) | 正文选读：分辨率/延迟权衡；官方架构说明核对 |
| 2405.07992v3 | [MambaOut: Do We Really Need Mamba for Vision?](https://arxiv.org/abs/2405.07992v3) | [foundation-models-and-systems](foundation-models-and-systems.md#broad-vision-primary-evidence) | 会议摘要及部分实验设置选读；未复核全部实验 |
| 2610.22306v1 | [ARC-SORT: Adaptive, Robust, Compensated Multi-Object Tracking with Interacting Multiple Models](https://arxiv.org/abs/2610.22306v1) | [perception-and-identifiability](perception-and-identifiability.md#broad-vision-primary-evidence) | 摘要及问题设定选读；未复核完整实验 |
| icml2026 / 正式会议 2026 | [Physics from Video: Identifiability of Time-Invariant Second-Order ODEs under Minimal Trajectory Conditions](https://proceedings.mlr.press/v306/wang26iq.html) | [perception-and-identifiability](perception-and-identifiability.md#broad-vision-primary-evidence) | 正文 §3–4 与定理条件选读；未复核全部证明/实验 |
| cvpr2026 / 正式会议 2026 | [Physical Object Understanding with a Physically Controllable World Model](https://openaccess.thecvf.com/content/CVPR2026/html/Venkatesh_Physical_Object_Understanding_with_a_Physically_Controllable_World_Model_CVPR_2026_paper.html) | [perception-and-identifiability](perception-and-identifiability.md#broad-vision-primary-evidence) | 主文 §3–4 与补充数据说明选读；未复核全部实验 |
| rss2026 / 正式会议 2026 | [Memory Retrieval in Visuomotor Policies for Long-Horizon Robot Control](https://www.roboticsproceedings.org/rss22/p010.html) | [representation-and-memory](representation-and-memory.md#broad-vision-primary-evidence) | 正文 §III 与任务/实验设置选读 |
| rss2026 / 正式会议 2026 | [Causal World Modeling for Robot Control](https://www.roboticsproceedings.org/rss22/p016.html) | [learning-and-data](learning-and-data.md#broad-vision-primary-evidence) | 正文建模/编码与训练说明选读；未复核全部实验 |
| rss2026 / 正式会议 2026 | [Collaborating Visual and Parameter Spaces for Consistent Long-Horizon Embodied World Model](https://www.roboticsproceedings.org/rss22/p014.html) | [representation-and-memory](representation-and-memory.md#broad-vision-primary-evidence) | 正文条件接口与 §V 局限选读 |
| clear2026 / 正式会议 2026 | [Disentangling Dynamical Systems: Causal Representation Learning Meets Local Sparse Attention](https://proceedings.mlr.press/v323/baumgartner26a.html) | [causality-and-active-perception](causality-and-active-perception.md#broad-vision-primary-evidence) | 正文假设1–3、实验与局限选读；未复核全部证明 |
| clear2026 / 正式会议 2026 | [Learning a Spatial Partitioning and its Causal Relations from Temporal Data](https://proceedings.mlr.press/v323/brouillard26a.html) | [causality-and-active-perception](causality-and-active-perception.md#broad-vision-primary-evidence) | 正文 §3.4、实验设置与讨论选读 |
| clear2026 / 正式会议 2026 | [Coarsening Causal DAG Models](https://proceedings.mlr.press/v323/madaleno26b.html) | [causality-and-active-perception](causality-and-active-perception.md#broad-vision-primary-evidence) | 正文假设、算法范围及统计局限选读 |
| icml2026 / 正式会议 2026 | [Causal-JEPA: Learning World Models through Object-Level Latent Masking](https://proceedings.mlr.press/v306/nam26c.html) | [representation-and-memory](representation-and-memory.md#broad-vision-primary-evidence) | 正文 §5–6、影响邻域解释与局限选读 |
| icml2026 / 正式会议 2026 | [Identifiable Token Correspondence for World Models](https://proceedings.mlr.press/v306/kim26bq.html) | [representation-and-memory](representation-and-memory.md#broad-vision-primary-evidence) | 正文问题设定、对应变量与解码说明选读 |
| uai2026 / 正式会议 2026 | [Who Guards the Guardians? The Challenges of Evaluating Identifiability of Learned Representations](https://proceedings.mlr.press/v337/joshi26a.html) | [evaluation-and-benchmarks](evaluation-and-benchmarks.md#broad-vision-primary-evidence) | 正文指标反例、分类及局限选读 |
| aistats2026 / 正式会议 2026 | [$ε$-Identifiability of Causal Quantities](https://proceedings.mlr.press/v300/li26j.html) | [causality-and-active-perception](causality-and-active-perception.md#broad-vision-primary-evidence) | 正文界与部分条件选读；未复核全部证明 |
| uai2026 / 正式会议 2026 | [On the Granularity of Causal Effect Identifiability](https://proceedings.mlr.press/v337/chen26c.html) | [causality-and-active-perception](causality-and-active-perception.md#broad-vision-primary-evidence) | 正文问题定义与 ID-CSI 条件选读 |
| aistats2026 / 正式会议 2026 | [A Covering Framework for Offline POMDPs Learning Using Belief Space Metric](https://proceedings.mlr.press/v300/zhu26a.html) | [evaluation-and-benchmarks](evaluation-and-benchmarks.md#broad-vision-primary-evidence) | 正文问题设定、稳定性与覆盖条件选读；未复核全部证明 |
| icml2026 / 正式会议 2026 | [Compositional Planning with Jumpy World Models](https://proceedings.mlr.press/v306/farebrother26a.html) | [causality-and-active-perception](causality-and-active-perception.md#broad-vision-primary-evidence) | 摘要、引言及问题设定选读；未复核完整方法/实验 |

外部结果仍为 `PRIMARY_PAPER` / `OFFICIAL_REPORTED_RESULT`，不是 Clover 实测。原文选读包含实际读到的方法/假设/局限段，不表示全部证明、附录、训练混合、checkpoints和实验公平性均通过独立复核。各正文记录继续保留 V/L 条件与反假设；代码或数据链接存在也不等于已运行。

### 及时更新而不混淆发布物

- [Ultralytics 当前 release](https://github.com/ultralytics/ultralytics/releases/tag/v8.4.189)、[YOLO26 论文](https://arxiv.org/abs/2606.03748v1)与[模型文档](https://docs.ultralytics.com/models/yolo26/)分别是软件包、研究记录和模型接口。[YOLO27 预览](https://docs.ultralytics.com/models/yolo27/)截至核验日没有已发布权重，不能登记成已运行的对比模型。
- [PaddleOCR 官方代码](https://github.com/PaddlePaddle/PaddleOCR)包含 PP-OCRv6、PaddleOCR-VL-1.6 与 HPD-Parsing 的发布说明；这里按 `OPEN_SOURCE` / `OFFICIAL_REPORTED_RESULT` 登记，不把工具 README 的速度/榜单数字升为独立科学结果。
- [TAP 系列官方代码](https://github.com/google-deepmind/tapnet)区分 TAPNext、BootsTAPNext 与 TAPNext++ checkpoints/在线接口；[CoTracker 官方代码](https://github.com/facebookresearch/co-tracker)区分在线滑窗与离线条件。项目中的 GPU 延迟不是本机或整体视觉模型的速度。
- [SAM 官方代码](https://github.com/facebookresearch/sam3)、[WeVisOne-VL 官方代码](https://github.com/Tencent/WeVisOne-VL)和[OmniDocBench 官方资源](https://github.com/opendatalab/OmniDocBench)补齐概念/像素感知、统一任务与文档评测入口。尚未下载权重/数据或执行评测；精确权重、依赖、许可与脚本 revision 在方法比较/实验注册中继续锁定。

这次补充闭合了“基础 CV 功能未被明确列为必备”和“非 arXiv 正式来源不足”的一部分缺口。旧 335 个数字 arXiv ID 的内容级主张、未覆盖目录/官方 artifact、未知未来任务证据恢复与严格视觉物性/因果问题仍在当前队列；没有以扩大目录数量冒充这些问题已经解决。
<!-- END broad-vision-sources -->

<!-- BEGIN core-vision-source-frontier -->
<a id="core-vision-source-frontier"></a>

## 2026-10 核心视觉与原生速度来源批次

检索/核验：**2026-10-25（Asia/Shanghai）**。本批次用 19 组主 arXiv 查询（2026-09-01 至 2026-10-25）加动作/指代/部件/物理/点追踪/物体位姿/3D 占据补充检索，主查询原始返回 2,170 条、去重后 2,072 条；另核 ICLR/ECCV/NeurIPS 2026 camera-ready。按标题/摘要与能力缺口筛出 304 篇做书目核验（303 篇 arXiv + 1 篇 PMLR-only；含单独核验的 YOLO26 论文），其中 290 篇此前未被本仓库引用，14 篇已有引用。对 97 篇做正文级选读，对 RF-DETR/WeVisOne-VL 做部分正文核读，其余为摘要/官方项目核验。未筛完全部候选，未把摘要阅读升级为全文复现。

**检索协议边界：** 查询按相关性排序，未穷尽 arXiv 全部结果；会议/期刊正式记录、模型权重、数据集许可与预训练-评测重叠仍须逐项审计。下列 URL 固定到本次返回版本；官方代码/项目页均为 `OPEN_SOURCE`/`OFFICIAL_PROJECT` 登记，不代表已加载权重或复现。

| 查询组 | 主题 | 返回条数 |
|---|---|---|
| `recognition` | 图像/视觉识别与分类 | 45 |
| `openvocab` | 开放词汇/零样本检测 | 120 |
| `detection` | 目标检测/YOLO/DETR | 120 |
| `segmentation` | 分割/SAM | 120 |
| `tracking` | 目标/点多目标追踪 | 104 |
| `pose` | 姿态/关键点 | 120 |
| `ocr` | OCR/文档/场景文字 | 120 |
| `counting` | 计数 | 120 |
| `geometry` | 深度/三维/几何 | 120 |
| `worldmodel` | 世界模型/视频预测 | 120 |
| `selfsup` | JEPA/自监督/视觉表征 | 120 |
| `efficient` | 实时/高效/边缘部署 | 120 |
| `active` | 主动视觉/事件相机/神经形态 | 120 |
| `vlm` | 视觉语言模型 | 120 |
| `video` | 视频理解 | 120 |
| `vla` | 视觉语言动作/机器人 | 120 |
| `generative` | 图像/视频生成/扩散 | 120 |
| `embodied` | 具身智能/空间智能 | 120 |
| `neuro` | 神经科学/生物视觉 | 101 |

原始 XML 与 2,072 条候选记录保存在工作区 `frontier-cv-2026-10/`（未提交到仓库）；上表是相关性排序的前 N 条，不代表穷尽。

### 识别与视觉表征

| ID | 标题 | 深度 | 状态 |
|---|---|---|---|
| [1512.03385](https://arxiv.org/abs/1512.03385v1) | Deep Residual Learning for Image Recognition | 摘要/书目 | 既有引用 |
| [2010.11929](https://arxiv.org/abs/2010.11929v2) | An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale | 摘要/书目 | 既有引用 |
| [2201.03545](https://arxiv.org/abs/2201.03545v2) | A ConvNet for the 2020s | 摘要/书目 | 本轮新增 |
| [2111.06377](https://arxiv.org/abs/2111.06377v3) | Masked Autoencoders Are Scalable Vision Learners | 摘要/书目 | 本轮新增 |
| [2103.00020](https://arxiv.org/abs/2103.00020v1) | Learning Transferable Visual Models From Natural Language Supervision | 摘要/书目 | 既有引用 |
| [2411.14402](https://arxiv.org/abs/2411.14402v1) | Multimodal Autoregressive Pre-training of Large Vision Encoders | 摘要/书目 | 本轮新增 |
| [2507.22062](https://arxiv.org/abs/2507.22062v3) | Meta CLIP 2: A Worldwide Scaling Recipe | 摘要/书目 | 本轮新增 |
| [2508.10104](https://arxiv.org/abs/2508.10104v1) | DINOv3 | 摘要/书目 | 既有引用 |
| [2504.13181](https://arxiv.org/abs/2504.13181v2) | Perception Encoder: The best visual embeddings are not at the output of the network | 正文选读 | 本轮新增 |
| [2504.01017](https://arxiv.org/abs/2504.01017v1) | Scaling Language-Free Visual Representation Learning | 摘要/书目 | 本轮新增 |
| [2502.14786](https://arxiv.org/abs/2502.14786v1) | SigLIP 2: Multilingual Vision-Language Encoders with Improved Semantic Understanding, Localization, and Dense Features | 摘要/书目 | 既有引用 |

### 检测

| ID | 标题 | 深度 | 状态 |
|---|---|---|---|
| [2606.03748](https://arxiv.org/abs/2606.03748v1) | Ultralytics YOLO26: Unified Real-Time End-to-End Vision Models | 正文选读 | 本轮新增 |
| [2502.12524](https://arxiv.org/abs/2502.12524v1) | YOLOv12: Attention-Centric Real-Time Object Detectors | 摘要/书目 | 本轮新增 |
| [2410.13842](https://arxiv.org/abs/2410.13842v1) | D-FINE: Redefine Regression Task in DETRs as Fine-grained Distribution Refinement | 摘要/书目 | 本轮新增 |
| [2412.04234](https://arxiv.org/abs/2412.04234v3) | DEIM: DETR with Improved Matching for Fast Convergence | 摘要/书目 | 本轮新增 |
| [2511.09554](https://arxiv.org/abs/2511.09554v2) | RF-DETR: Neural Architecture Search for Real-Time Detection Transformers | 部分正文 | 本轮新增 |
| [2406.03459](https://arxiv.org/abs/2406.03459v1) | LW-DETR: A Transformer Replacement to YOLO for Real-Time Detection | 摘要/书目 | 本轮新增 |
| [2303.05499](https://arxiv.org/abs/2303.05499v5) | Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection | 摘要/书目 | 既有引用 |

### 分割、三维与运动区域

| ID | 标题 | 深度 | 状态 |
|---|---|---|---|
| [2511.16719](https://arxiv.org/abs/2511.16719v2) | SAM 3: Segment Anything with Concepts | 摘要/书目 | 既有引用 |
| [2511.16624](https://arxiv.org/abs/2511.16624v2) | SAM 3D: 3Dfy Anything in Images | 摘要/书目 | 本轮新增 |
| [2610.27960](https://arxiv.org/abs/2610.27960v1) | Efficient SAM3 Adaptation for Multi-Class Semantic Segmentation via Dense Competitive Representations | 摘要/书目 | 本轮新增 |
| [2610.22921](https://arxiv.org/abs/2610.22921v1) | MaskMerge: Structure-aware Token Merging for Efficient Instance Segmentation | 摘要/书目 | 本轮新增 |
| [2610.31209](https://arxiv.org/abs/2610.31209v1) | Moving Regions, Not Moving Objects: Segmenting What Actually Moves under Camera Motion | 摘要/书目 | 本轮新增 |
| [2610.30623](https://arxiv.org/abs/2610.30623v1) | Refining Open-Vocabulary Semantic Segmentation via Regional Semantics and Visual Prototypes | 摘要/书目 | 本轮新增 |

### 追踪、点轨迹与追踪安全

| ID | 标题 | 深度 | 状态 |
|---|---|---|---|
| [2411.11922](https://arxiv.org/abs/2411.11922v2) | SAMURAI: Adapting Segment Anything Model for Zero-Shot Visual Tracking with Motion-Aware Memory | 正文选读 | 本轮新增 |
| [2504.05579](https://arxiv.org/abs/2504.05579v2) | TAPNext: Tracking Any Point (TAP) as Next Token Prediction | 正文选读 | 既有引用 |
| [2604.10582](https://arxiv.org/abs/2604.10582v1) | TAPNext++: What's Next for Tracking Any Point (TAP)? | 摘要/书目 | 既有引用 |
| [2403.16848](https://arxiv.org/abs/2403.16848v2) | Multiple Object Tracking as ID Prediction | 摘要/书目 | 本轮新增 |
| [2610.10391](https://arxiv.org/abs/2610.10391v1) | MOTIP2: Spatial Priors for End-to-End Multi-Object Tracking | 正文选读 | 本轮新增 |
| [2609.37339](https://arxiv.org/abs/2609.37339v1) | UGO: Unified Architecture for General Multi-Object Tracking by Segmentation | 正文选读 | 本轮新增 |
| [2511.00510](https://arxiv.org/abs/2511.00510v2) | OmniTrack++: Omnidirectional Multi-Object Tracking by Learning Large-FoV Trajectory Feedback | 摘要/书目 | 本轮新增 |
| [2310.12982](https://arxiv.org/abs/2310.12982v2) | Putting the Object Back into Video Object Segmentation | 摘要/书目 | 本轮新增 |
| [2610.19931](https://arxiv.org/abs/2610.19931v1) | SAM3RL: Memory Control via Reinforcement Learning for Visual Object Tracking | 摘要/书目 | 本轮新增 |
| [2610.15929](https://arxiv.org/abs/2610.15929v1) | When Trackers Fail: VLM-Guided Verification and Recovery for Robust Video Object Segmentation | 正文选读 | 本轮新增 |
| [2610.01314](https://arxiv.org/abs/2610.01314v1) | ARROW: Arbitrary Reconstruction and Tracking of 4D Observations in the Wild | 摘要/书目 | 本轮新增 |
| [2609.33948](https://arxiv.org/abs/2609.33948v1) | TrackFlood: Relocating Latency Attacks from NMS-Free Detectors to Real-Time Trackers | 摘要/书目 | 本轮新增 |

### 视觉阅读与文档解析

| ID | 标题 | 深度 | 状态 |
|---|---|---|---|
| [2510.14528](https://arxiv.org/abs/2510.14528v4) | PaddleOCR-VL: Boosting Multilingual Document Parsing via a 0.9B Ultra-Compact Vision-Language Model | 正文选读 | 本轮新增 |
| [2512.02498](https://arxiv.org/abs/2512.02498v4) | dots.ocr: Multilingual Document Layout Parsing in a Single Vision-Language Model | 摘要/书目 | 本轮新增 |
| [2509.22186](https://arxiv.org/abs/2509.22186v2) | MinerU2.5: A Decoupled Vision-Language Model for Efficient High-Resolution Document Parsing | 摘要/书目 | 本轮新增 |
| [2510.19817](https://arxiv.org/abs/2510.19817v1) | olmOCR 2: Unit Test Rewards for Document OCR | 摘要/书目 | 本轮新增 |
| [2609.37712](https://arxiv.org/abs/2609.37712v1) | PolyOCR-Venus: Unified OCR Foundation Models for Text-Centric Visual Intelligence | 摘要/书目 | 本轮新增 |
| [2609.28857](https://arxiv.org/abs/2609.28857v1) | MEVL-STP: Multi-Encoder and Vision Language Model for Arbitrarily Shaped Scene Text Spotting | 摘要/书目 | 本轮新增 |
| [2610.31329](https://arxiv.org/abs/2610.31329v1) | WeVisOne-VL: Unified Visual Perception from Objects to Pixels | 部分正文 | 既有引用 |

### 姿态、计数与几何

| ID | 标题 | 深度 | 状态 |
|---|---|---|---|
| [2204.12484](https://arxiv.org/abs/2204.12484v3) | ViTPose: Simple Vision Transformer Baselines for Human Pose Estimation | 摘要/书目 | 本轮新增 |
| [2408.12569](https://arxiv.org/abs/2408.12569v3) | Sapiens: Foundation for Human Vision Models | 摘要/书目 | 本轮新增 |
| [2610.26096](https://arxiv.org/abs/2610.26096v2) | PnP-Transformer: A Neural Pose Solver for Zero-Shot 6D Object Pose Estimation | 摘要/书目 | 本轮新增 |
| [2407.04619](https://arxiv.org/abs/2407.04619v2) | CountGD: Multi-Modal Open-World Counting | 摘要/书目 | 本轮新增 |
| [2610.08379](https://arxiv.org/abs/2610.08379v1) | UniCounting: Instance-Aware Proposal Consolidation for Image-Query-Free Multi-Category Counting | 摘要/书目 | 本轮新增 |
| [2511.10647](https://arxiv.org/abs/2511.10647v1) | Depth Anything 3: Recovering the Visual Space from Any Views | 正文选读 | 本轮新增 |
| [2507.02546](https://arxiv.org/abs/2507.02546v1) | MoGe-2: Accurate Monocular Geometry with Metric Scale and Sharp Details | 摘要/书目 | 本轮新增 |

### 原生效率与流式系统

| ID | 标题 | 深度 | 状态 |
|---|---|---|---|
| [2305.07027](https://arxiv.org/abs/2305.07027v1) | EfficientViT: Memory Efficient Vision Transformer with Cascaded Group Attention | 摘要/书目 | 本轮新增 |
| [2610.04457](https://arxiv.org/abs/2610.04457v1) | RPFQ-ViT: Rotated Phase-Frame Quantization for Extremely Low-Bit Weights in Vision Transformers | 摘要/书目 | 本轮新增 |
| [2610.18399](https://arxiv.org/abs/2610.18399v2) | Bifocal: Training-Free Mixed Granularity Visual Token Pruning for Multimodal LLMs | 摘要/书目 | 本轮新增 |
| [2610.25551](https://arxiv.org/abs/2610.25551v1) | StreamAhead: Real-Time Streaming Video Question Answering via Adaptive Precomputation | 摘要/书目 | 本轮新增 |
| [2610.17540](https://arxiv.org/abs/2610.17540v1) | TacitVLA: Reasoning Vision-Language-Action Models Without Reasoning Latency | 摘要/书目 | 本轮新增 |
| [2610.22155](https://arxiv.org/abs/2610.22155v3) | Realtime-Bench: Can Frontier Models Solve Real-time Interactive Problems? | 摘要/书目 | 本轮新增 |

### 世界模型与持久状态

| ID | 标题 | 深度 | 状态 |
|---|---|---|---|
| [2509.24527](https://arxiv.org/abs/2509.24527v1) | Training Agents Inside of Scalable World Models | 摘要/书目 | 本轮新增 |
| [2510.26583](https://arxiv.org/abs/2510.26583v1) | Emu3.5: Native Multimodal Models are World Learners | 摘要/书目 | 本轮新增 |
| [2610.22371](https://arxiv.org/abs/2610.22371v1) | Gen4P: Video Generators are 4D Perceivers | 摘要/书目 | 本轮新增 |
| [2610.30789](https://arxiv.org/abs/2610.30789v1) | An Introduction to World Models for Generalist Agents | 摘要/书目 | 本轮新增 |
| [2610.23795](https://arxiv.org/abs/2610.23795v1) | Persistent Planar Memory for Video World Models | 摘要/书目 | 既有引用 |
| [2610.18637](https://arxiv.org/abs/2610.18637v1) | Grid or Nodes? Probing Object Memory in World Models Under Partial Observability | 摘要/书目 | 既有引用 |
| [2610.30129](https://arxiv.org/abs/2610.30129v1) | Rethinking Video Autoencoders for Interactive World Models | 摘要/书目 | 既有引用 |
| [2610.30814](https://arxiv.org/abs/2610.30814v1) | DRILL: Training World Models to Improve Policies, Not Predict Pixels | 摘要/书目 | 既有引用 |

### 主动视觉与跨域证据

| ID | 标题 | 深度 | 状态 |
|---|---|---|---|
| [2610.20064](https://arxiv.org/abs/2610.20064v2) | FoveaVLA: Foveation Actions Replace the Wrist Camera in VLAs | 摘要/书目 | 本轮新增 |
| [2610.12999](https://arxiv.org/abs/2610.12999v1) | EgoReveal: Learning Active Vision and Object Manipulation under Partial Occlusions from Egocentric Demonstrations | 摘要/书目 | 本轮新增 |
| [2610.11039](https://arxiv.org/abs/2610.11039v1) | Rendering-Free Lookahead for Question-Guided Active Vision | 摘要/书目 | 本轮新增 |
| [2610.19624](https://arxiv.org/abs/2610.19624v1) | Adaptive Observation Control for Active Visual Recognition | 摘要/书目 | 本轮新增 |
| [2610.26659](https://arxiv.org/abs/2610.26659v3) | SpatialScout: Can VLM Agents Actively Explore and Map 3D Scenes? | 摘要/书目 | 本轮新增 |
| [2610.19046](https://arxiv.org/abs/2610.19046v1) | What Information Buys in Active Inference | 摘要/书目 | 本轮新增 |
| [2610.20309](https://arxiv.org/abs/2610.20309v1) | Event Cameras versus Frame Cameras for Synthetic-Aperture Imaging: A Simulation Study | 摘要/书目 | 本轮新增 |
| [2610.17154](https://arxiv.org/abs/2610.17154v1) | Neuromorphic Decoding and Dynamical Image Reconstruction from Populations of Spiking Retinal Ganglion Cells | 摘要/书目 | 本轮新增 |
| [2610.09983](https://arxiv.org/abs/2610.09983v1) | Feedback to the primary visual cortex is highly concentrated on the central visual field representation | 摘要/书目 | 本轮新增 |
| [2610.19199](https://arxiv.org/abs/2610.19199v1) | Moving Beyond the Flat Screen: Opportunities and Challenges of Extended Reality for Studying Human Brain and Behavior | 摘要/书目 | 本轮新增 |

### 评测基准

| ID | 标题 | 深度 | 状态 |
|---|---|---|---|
| [2609.01899](https://arxiv.org/abs/2609.01899v2) | TAPVid-MV: A Benchmark for Tracking Any Point in 3D Across Multiple Views | 摘要/书目 | 本轮新增 |
| [2610.05911](https://arxiv.org/abs/2610.05911v2) | Every View Counts: View-Consistent Panoptic Quality for Multi-view Panoptic Segmentation | 摘要/书目 | 本轮新增 |
| [2412.07626](https://arxiv.org/abs/2412.07626v2) | OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations | 摘要/书目 | 本轮新增 |

### 识别的长尾、细粒度与尺度失败面

| ID | 标题 | 深度 | 状态 |
|---|---|---|---|
| [2609.04948](https://arxiv.org/abs/2609.04948v1) | VICAL: Vicinal Consistency Alignment for Long-Tailed Visual Recognition | 摘要/书目 | 本轮新增 |
| [2609.37331](https://arxiv.org/abs/2609.37331v1) | OFBD: Object-Focused Background Debiasing for Long-Tailed Learning | 摘要/书目 | 本轮新增 |
| [2610.13154](https://arxiv.org/abs/2610.13154v1) | From Glance to Focus: Mitigating Recognition Laziness in MLLMs for Fine-Grained Recognition | 摘要/书目 | 本轮新增 |
| [2609.06051](https://arxiv.org/abs/2609.06051v1) | Image-Scale Robustness and Visual Recognition Performance: A Cross-Architecture Analysis | 摘要/书目 | 本轮新增 |

### 动作、事件与指代/grounding

| ID | 标题 | 深度 | 状态 |
|---|---|---|---|
| [2606.03490](https://arxiv.org/abs/2606.03490v1) | TrAction: Action Recognition with Sparse Trajectories | 摘要/书目 | 本轮新增 |
| [2608.22760](https://arxiv.org/abs/2608.22760v1) | ByteAction: Byte-space Action Recognition Foundation Model | 摘要/书目 | 本轮新增 |
| [2605.07141](https://arxiv.org/abs/2605.07141v1) | Qwen3-VL-Seg: Unlocking Open-World Referring Segmentation with Vision-Language Grounding | 摘要/书目 | 本轮新增 |
| [2605.20110](https://arxiv.org/abs/2605.20110v1) | SetCon: Towards Open-Ended Referring Segmentation via Set-Level Concept Prediction | 摘要/书目 | 本轮新增 |
| [2609.02359](https://arxiv.org/abs/2609.02359v1) | TempoGround: State-Aware Streaming Visual Grounding with Vision-Language Models | 摘要/书目 | 本轮新增 |

### 部件/可供性与抠图

| ID | 标题 | 深度 | 状态 |
|---|---|---|---|
| [2610.29768](https://arxiv.org/abs/2610.29768v1) | UniRAP: Towards Unified Part-level Physical Affordance Reasoning and Actionable Perception | 摘要/书目 | 本轮新增 |
| [2606.27339](https://arxiv.org/abs/2606.27339v1) | SAM2Matting: Generalized Image and Video Matting | 摘要/书目 | 本轮新增 |

### 正式会议 2026（ICLR/ECCV）

| ID | 标题 | 深度 | 状态 |
|---|---|---|---|
| [2605.16903](https://arxiv.org/abs/2605.16903v1) | WOW-Seg: A Word-free Open World Segmentation Model | 摘要/书目 | 本轮新增 |
| [2609.39785](https://arxiv.org/abs/2609.39785v1) | Seeing as Humans Do: Learning from Motion to Segment Anything Without Supervision | 摘要/书目 | 本轮新增 |
| [2602.08550](https://arxiv.org/abs/2602.08550v3) | GOT-Edit: Geometry-Aware Generic Object Tracking via Online Model Editing | 摘要/书目 | 本轮新增 |
| [2603.21115](https://arxiv.org/abs/2603.21115v1) | LiFR-Seg: Anytime High-Frame-Rate Segmentation via Event-Guided Propagation | 摘要/书目 | 本轮新增 |
| [2602.19624](https://arxiv.org/abs/2602.19624v2) | Segmentation-Guided Homography Estimation for Long-Term Planar Tracking | 摘要/书目 | 本轮新增 |
| [2505.15263](https://arxiv.org/abs/2505.15263v3) | gen2seg: Generative Models Enable Generalizable Instance Segmentation | 摘要/书目 | 本轮新增 |
| [2510.11715](https://arxiv.org/abs/2510.11715v2) | Point Prompting: Counterfactual Tracking with Video Diffusion Models | 摘要/书目 | 本轮新增 |
| [2601.23159](https://arxiv.org/abs/2601.23159v1) | Segment Any Events with Language | 摘要/书目 | 本轮新增 |
| [2606.14307](https://arxiv.org/abs/2606.14307v2) | Pano3D: Unified 3D Reconstruction and Panoptic Segmentation | 摘要/书目 | 本轮新增 |
| [2503.13160](https://arxiv.org/abs/2503.13160v3) | Language-guided Open-world Video Anomaly Detection under Weak Supervision | 摘要/书目 | 本轮新增 |

### NeurIPS 2026（正式会议）

| ID | 标题 | 深度 | 状态 |
|---|---|---|---|
| [2610.02946](https://arxiv.org/abs/2610.02946v1) | When Predicting Nothing Beats SAM 3: Revisiting Evaluation in Video Object Segmentation | 摘要/书目 | 本轮新增 |
| [2609.39265](https://arxiv.org/abs/2609.39265v1) | Universal Cross-Prompt Adversarial Attacks on Promptable Concept Segmentation | 摘要/书目 | 本轮新增 |
| [2609.40333](https://arxiv.org/abs/2609.40333v1) | I Have a Stream: Making Self-Supervised Learning Work on Continuous Video | 摘要/书目 | 本轮新增 |
| [2609.30667](https://arxiv.org/abs/2609.30667v1) | StarWM: Self-Supervised Trained Attention Routing for Robust World Models | 摘要/书目 | 本轮新增 |
| [2610.00970](https://arxiv.org/abs/2610.00970v2) | RelationVGGT: Visual Geometry Transformers for 3D Spatial Relation Segmentation | 摘要/书目 | 本轮新增 |
| [2603.23478](https://arxiv.org/abs/2603.23478v2) | UniFunc3D: Unified Active Spatial-Temporal Grounding for 3D Affordance Segmentation | 摘要/书目 | 本轮新增 |
| [2608.09613](https://arxiv.org/abs/2608.09613v2) | Marrying Optimal Transport and ODEs for Unified Continuous-Time 4D Reconstruction and Tracking | 摘要/书目 | 本轮新增 |
| [2605.15618](https://arxiv.org/abs/2605.15618v2) | Latent Video Prediction for World Modeling: An Evaluation Uncovering Intriguing Favorable Evidence | 摘要/书目 | 本轮新增 |

### 严格视觉隐藏态/因果 2026

| ID | 标题 | 深度 | 状态 |
|---|---|---|---|
| [2601.20303](https://arxiv.org/abs/2601.20303v2) | Physically Guided Visual Mass Estimation from a Single RGB Image | 正文选读 | 本轮新增 |
| [2610.01162](https://arxiv.org/abs/2610.01162v1) | PhysicsLENS: Diagnosing Physical Property Blindness in Video Generation Models | 摘要/书目 | 本轮新增 |
| [2609.28654](https://arxiv.org/abs/2609.28654v1) | Training Object Permanence in World Models | 摘要/书目 | 本轮新增 |
| [2610.01201](https://arxiv.org/abs/2610.01201v1) | iSEE: Object Permanence Through Self-Supervision | 正文选读 | 本轮新增 |
| [2609.20819](https://arxiv.org/abs/2609.20819v2) | Can 4D Foundation Models Remember? | 正文选读 | 本轮新增 |
| [2606.09646](https://arxiv.org/abs/2606.09646v2) | How Do Video Foundation Models Encode Intuitive Physics? Probing Across Pretraining Paradigms | 摘要/书目 | 本轮新增 |
| [2602.11021](https://arxiv.org/abs/2602.11021v1) | ContactGaussian-WM: Learning Physics-Grounded World Model from Videos | 摘要/书目 | 本轮新增 |
| [2608.21355](https://arxiv.org/abs/2608.21355v1) | ViTacPhys: Physical Property-Aware Grasping from Human Visual-Tactile Demonstrations | 摘要/书目 | 本轮新增 |
| [2608.07726](https://arxiv.org/abs/2608.07726v2) | Vision Meets WiFi: Physics-Grounded Estimation of Volumetric Mechanical Properties | 摘要/书目 | 本轮新增 |
| [2605.16457](https://arxiv.org/abs/2605.16457v3) | Identifiable Token Correspondence for World Models | 摘要/书目 | 本轮新增 |
| [2610.24519](https://arxiv.org/abs/2610.24519v1) | Axiomatic World Modeling for Physics Reasoning | 摘要/书目 | 本轮新增 |

### 检索/再识别 2026

| ID | 标题 | 深度 | 状态 |
|---|---|---|---|
| [2609.07373](https://arxiv.org/abs/2609.07373v1) | TRAIL: Trajectory-Aware Visual Place Recognition against Unordered Databases | 摘要/书目 | 本轮新增 |
| [2602.00841](https://arxiv.org/abs/2602.00841v1) | Beyond First-Order: Learning Riemannian Geometries for Invariant Visual Place Recognition | 摘要/书目 | 本轮新增 |
| [2610.07366](https://arxiv.org/abs/2610.07366v1) | Identity-Conditioned Score Fusion for Open-Set Person Re-Identification | 摘要/书目 | 本轮新增 |
| [2605.06637](https://arxiv.org/abs/2605.06637v1) | DPM++: Dynamic Masked Metric Learning for Occluded Person Re-identification | 摘要/书目 | 本轮新增 |
| [2603.01640](https://arxiv.org/abs/2603.01640v1) | MSP-ReID: Hairstyle-Robust Cloth-Changing Person Re-Identification | 摘要/书目 | 本轮新增 |
| [2606.01981](https://arxiv.org/abs/2606.01981v1) | Generalization Limits in Vehicle Re-Identification | 摘要/书目 | 本轮新增 |
| [2607.09267](https://arxiv.org/abs/2607.09267v1) | REMIND: RE-Identification with Memory for INDoor Navigation | 摘要/书目 | 本轮新增 |
| [2604.03277](https://arxiv.org/abs/2604.03277v1) | Event-Driven Neuromorphic Vision Enables Energy-Efficient Visual Place Recognition | 摘要/书目 | 本轮新增 |

### 三维检测/场景图 2026

| ID | 标题 | 深度 | 状态 |
|---|---|---|---|
| [2604.01646](https://arxiv.org/abs/2604.01646v1) | MonoSAOD: Monocular 3D Object Detection with Sparsely Annotated Label | 摘要/书目 | 本轮新增 |
| [2604.13586](https://arxiv.org/abs/2604.13586v1) | Efficient Multi-View 3D Object Detection by Dynamic Token Selection and Fine-Tuning | 摘要/书目 | 本轮新增 |
| [2608.19973](https://arxiv.org/abs/2608.19973v1) | Open-Vocabulary 3D Object Detection with Co-Distillation Discovery and Dual Guidance Robust Training | 摘要/书目 | 本轮新增 |
| [2607.00529](https://arxiv.org/abs/2607.00529v1) | NoPA: Non-Parametric Online 3D Scene Graph Generation | 摘要/书目 | 本轮新增 |
| [2605.20823](https://arxiv.org/abs/2605.20823v1) | RelWitness: Open-Vocabulary 3D Scene Graph Generation with Visual-Geometric Relation Witnesses | 摘要/书目 | 本轮新增 |
| [2602.02456](https://arxiv.org/abs/2602.02456v1) | Relationship-Aware Hierarchical 3D Scene Graph for Task Reasoning | 摘要/书目 | 本轮新增 |

### 动作/事件 2026

| ID | 标题 | 深度 | 状态 |
|---|---|---|---|
| [2605.09976](https://arxiv.org/abs/2605.09976v1) | OZ-TAL: Online Zero-Shot Temporal Action Localization | 摘要/书目 | 本轮新增 |
| [2607.00289](https://arxiv.org/abs/2607.00289v1) | OnPoint: Offline-to-Online Multi-Level Distillation for Point-Supervised Online Temporal Action Localization | 摘要/书目 | 本轮新增 |
| [2603.01743](https://arxiv.org/abs/2603.01743v1) | Action-Guided Attention for Video Action Anticipation | 摘要/书目 | 本轮新增 |
| [2608.14243](https://arxiv.org/abs/2608.14243v1) | Zero-Shot Skeleton-Based Action Anticipation | 摘要/书目 | 本轮新增 |
| [2603.08289](https://arxiv.org/abs/2603.08289v1) | Novel Semantic Prompting for Zero-Shot Action Recognition | 摘要/书目 | 本轮新增 |
| [2605.23288](https://arxiv.org/abs/2605.23288v1) | Spatio-Temporal Similarity Volume Aggregation for Open-Vocabulary Action Recognition | 摘要/书目 | 本轮新增 |

### 空间状态/SLAM 2026

| ID | 标题 | 深度 | 状态 |
|---|---|---|---|
| [2609.13733](https://arxiv.org/abs/2609.13733v1) | FFVO: A Feedforward Pose Decoder for Long-Horizon Visual Odometry | 正文选读 | 本轮新增 |
| [2608.01706](https://arxiv.org/abs/2608.01706v1) | UniSim-SLAM: Feed-Forward SLAM with Unified Sim(3) Optimization | 正文选读 | 本轮新增 |
| [2609.19628](https://arxiv.org/abs/2609.19628v1) | VGGT-GS SLAM: Uncalibrated Monocular Gaussian Splatting SLAM with Feed-Forward Priors | 摘要/书目 | 本轮新增 |
| [2610.14951](https://arxiv.org/abs/2610.14951v1) | FoundationVIO: Enforcing Metric Scale in Feed-forward Visual-Inertial Odometry | 摘要/书目 | 本轮新增 |
| [2608.30690](https://arxiv.org/abs/2608.30690v1) | Failure or Drift? Evaluating Monocular SLAM under Synthetic and Real-World Corruptions | 正文选读 | 本轮新增 |
| [2609.13691](https://arxiv.org/abs/2609.13691v1) | MomentBA: Second-order Spatial Moments for Anisotropic Correspondence Uncertainty in Differentiable Bundle Adjustment | 正文选读 | 本轮新增 |
| [2609.17168](https://arxiv.org/abs/2609.17168v1) | HuMemSLAM: Efficient Human-Inspired Semantic Place Recognition for Robust Visual SLAM | 摘要/书目 | 本轮新增 |
| [2610.30589](https://arxiv.org/abs/2610.30589v1) | OASIS: Online Anchor-centric Scene Inference System for Open-Vocabulary Retrieval and Navigation in Dynamic Environments | 正文选读 | 本轮新增 |
| [2609.20589](https://arxiv.org/abs/2609.20589v1) | RawSLAM: Online HDR Gaussian SLAM from Linear Radiance | 摘要/书目 | 本轮新增 |
| [2610.19044](https://arxiv.org/abs/2610.19044v1) | RingNav: Task-Shaped Circular Memory for Visual Heading | 正文选读 | 本轮新增 |
| [2609.30947](https://arxiv.org/abs/2609.30947v1) | DAPEVO: Deep Adaptive Patch Frame-Event Visual Odometry | 摘要/书目 | 本轮新增 |
| [2610.17513](https://arxiv.org/abs/2610.17513v1) | Gaussian Splatting for Real-Time Scene Reconstruction: Methods, Systems, and Trade-offs | 摘要/书目 | 本轮新增 |

### 人-物交互/社会场景 2026

| ID | 标题 | 深度 | 状态 |
|---|---|---|---|
| [2609.05959](https://arxiv.org/abs/2609.05959v1) | FineHOI: Part-Aware Dense Representations for Zero-Shot Human-Object Interaction Detection | 正文选读 | 本轮新增 |
| [2609.23431](https://arxiv.org/abs/2609.23431v2) | HOIBlender: Blending Lightweight Detection with Vision-Language Priors for Efficient Human-Object Interaction Detection | 正文选读 | 本轮新增 |
| [2608.28386](https://arxiv.org/abs/2608.28386v2) | GraspHOI: Full-Body 3D Human-Object Reconstruction with Finger-Level Grasps from a Single In-the-Wild Image | 正文选读 | 本轮新增 |
| [2607.04017](https://arxiv.org/abs/2607.04017v1) | SAGE: Synchronized Action-Gaze Recognition and Anticipation for Human Behavior Understanding | 正文选读 | 本轮新增 |
| [2610.25849](https://arxiv.org/abs/2610.25849v1) | Auditing Semantic and Relational Reliability in Open-Vocabulary Human-Object Interaction Evaluation | 正文选读 | 本轮新增 |
| [2609.14118](https://arxiv.org/abs/2609.14118v1) | Talking to Me or Someone Else? Rethinking Talk-to-Me Detection in Egocentric Videos | 摘要/书目 | 本轮新增 |
| [2610.27496](https://arxiv.org/abs/2610.27496v1) | Evaluating Social Reasoning in Embodied Vision-Language Models | 摘要/书目 | 本轮新增 |
| [2610.10438](https://arxiv.org/abs/2610.10438v1) | ECHO: Embodied Camera Observations of Human Object Carrying | 摘要/书目 | 本轮新增 |
| [2610.09358](https://arxiv.org/abs/2610.09358v1) | COOL: Curiosity-Driven Object Ownership Learning for Personalized Robotic Assistance | 摘要/书目 | 本轮新增 |

### 对应/光流/匹配 2026

| ID | 标题 | 深度 | 状态 |
|---|---|---|---|
| [2609.11486](https://arxiv.org/abs/2609.11486v1) | FreeFlow: A Bias-free Hierarchical Transformer for Optical Flow Estimation | 正文选读 | 本轮新增 |
| [2610.26690](https://arxiv.org/abs/2610.26690v1) | Foundation Model Driven Optical Flow | 正文选读 | 本轮新增 |
| [2608.03423](https://arxiv.org/abs/2608.03423v2) | SGFormer: Structure-Guided Transformer for Robust Local Feature Matching | 正文选读 | 本轮新增 |
| [2610.31321](https://arxiv.org/abs/2610.31321v1) | MVLoMa: Multi-View Local Feature Matching with Any Geometry Foundation Model | 正文选读 | 本轮新增 |
| [2609.17905](https://arxiv.org/abs/2609.17905v1) | Co-occurrence-Aware Quadratic Assignment for Local Feature Matching in Simultaneous Localization and Mapping | 摘要/书目 | 本轮新增 |
| [2608.11093](https://arxiv.org/abs/2608.11093v1) | Cross-View Feature Matching: Survey, Benchmarking, and Foundation-Model Perspectives | 摘要/书目 | 本轮新增 |
| [2609.21754](https://arxiv.org/abs/2609.21754v1) | SFVO: Decoupled Confidence-Guided Stereo-Flow Visual Odometry with Bidirectional PnP | 摘要/书目 | 本轮新增 |
| [2608.00499](https://arxiv.org/abs/2608.00499v1) | Optical Flow from Photons | 摘要/书目 | 本轮新增 |
| [2609.06726](https://arxiv.org/abs/2609.06726v1) | Back to the Feature: Zero-Shot 6DoF Pose Estimation via Dense Local Features | 正文选读 | 本轮新增 |

### 遮挡/非模态补全 2026

| ID | 标题 | 深度 | 状态 |
|---|---|---|---|
| [2604.20748](https://arxiv.org/abs/2604.20748v1) | Amodal SAM: A Unified Amodal Segmentation Framework with Generalization | 正文选读 | 本轮新增 |
| [2603.14741](https://arxiv.org/abs/2603.14741v1) | PHAC: Promptable Human Amodal Completion | 摘要/书目 | 本轮新增 |
| [2610.29061](https://arxiv.org/abs/2610.29061v1) | OccJEPA: Occlusion as Masking for Amodal Video Segmentation | 正文选读 | 本轮新增 |
| [2603.28333](https://arxiv.org/abs/2603.28333v1) | Integrating Multimodal Large Language Model Knowledge into Amodal Completion | 摘要/书目 | 本轮新增 |
| [2605.24533](https://arxiv.org/abs/2605.24533v1) | Learnable Shape Prototypes with Occlusion-Geometry-Guided Injection for Amodal Instance Segmentation | 摘要/书目 | 本轮新增 |
| [2604.11711](https://arxiv.org/abs/2604.11711v1) | Seeing Through the Tool: A Controlled Benchmark for Occlusion Robustness in Foundation Segmentation Models | 正文选读 | 本轮新增 |
| [2605.31466](https://arxiv.org/abs/2605.31466v1) | VolFill: Single-View Amodal 3D Scene Reconstruction with Volumetric Flow Matching | 正文选读 | 本轮新增 |
| [2603.04179](https://arxiv.org/abs/2603.04179v2) | NOVA3R: Non-pixel-aligned Visual Transformer for Amodal 3D Reconstruction | 正文选读 | 本轮新增 |
| [2610.18670](https://arxiv.org/abs/2610.18670v1) | Perception Beyond the Visible: Incompleteness-Aware Scene Understanding for Robot Autonomy | 摘要/书目 | 本轮新增 |

### 事件视觉/异步感知 2026

| ID | 标题 | 深度 | 状态 |
|---|---|---|---|
| [2608.11075](https://arxiv.org/abs/2608.11075v1) | Static in Frames, Dynamic in Events: Rethinking Features in Event Cameras as Motion Cues | 正文选读 | 本轮新增 |
| [2609.26919](https://arxiv.org/abs/2609.26919v1) | Bend the Clock: Predicting Ahead to Beat Latency in Event-Based Object Detection | 正文选读 | 本轮新增 |
| [2607.15727](https://arxiv.org/abs/2607.15727v1) | Event3R: Asynchronous-to-Global 3D Reconstruction from Event Camera via Spatial-Temporal Feature Aggregation | 正文选读 | 本轮新增 |
| [2607.02866](https://arxiv.org/abs/2607.02866v1) | E-TraMamba: A New Paradigm for Efficient Long-Term 3D Feature Tracking with Event Cameras | 正文选读 | 本轮新增 |
| [2608.14027](https://arxiv.org/abs/2608.14027v1) | E-S2Feat:Semantic-Guided Spiking Local Feature Detection and Description for Event Cameras | 正文选读 | 本轮新增 |
| [2607.26703](https://arxiv.org/abs/2607.26703v1) | Sequence-SOD: Bio-inspired Sequence-aware Spiking ObjectDetection for Event Cameras | 摘要/书目 | 本轮新增 |
| [2608.21764](https://arxiv.org/abs/2608.21764v1) | LiteEvent-AE: Lightweight Autoencoder for Event-Based Vision on Low-Latency Energy-Constrained Edge Devices | 摘要/书目 | 本轮新增 |
| [2609.17189](https://arxiv.org/abs/2609.17189v1) | EventEgoHands++: Event-based Egocentric 3D Hand Mesh Reconstruction with Real Dataset | 摘要/书目 | 本轮新增 |

### 长视频/第一人称记忆 2026

| ID | 标题 | 深度 | 状态 |
|---|---|---|---|
| [2608.11017](https://arxiv.org/abs/2608.11017v1) | R4DSG: Relative 4D Scene Graph Memory for Object-Centric Question Answering in Long Egocentric Video | 正文选读 | 本轮新增 |
| [2610.10538](https://arxiv.org/abs/2610.10538v1) | Never Look Back: Understanding Persistence in 3D Object Memory from Egocentric Videos | 正文选读 | 本轮新增 |
| [2610.17128](https://arxiv.org/abs/2610.17128v1) | EgoProbe: Benchmarking Long-Range and Exact Memory in Streaming Egocentric Videos | 正文选读 | 本轮新增 |
| [2608.13113](https://arxiv.org/abs/2608.13113v1) | EgoMonth: A Month-Level Egocentric Video Benchmark for Long-Term Spatiotemporal Memory | 摘要/书目 | 本轮新增 |
| [2610.30089](https://arxiv.org/abs/2610.30089v1) | ProactEgoMem: Benchmarking Proactive Memory in Streaming Egocentric Video | 摘要/书目 | 本轮新增 |
| [2609.40195](https://arxiv.org/abs/2609.40195v1) | MemLife: Curating and Reasoning over Long-Term Egocentric Video Memories | 摘要/书目 | 本轮新增 |
| [2609.38119](https://arxiv.org/abs/2609.38119v2) | VideoLoop: Looped Working Memory Against Semantic Thrashing in Long-Form Video Agents | 正文选读 | 本轮新增 |
| [2609.23601](https://arxiv.org/abs/2609.23601v1) | PREM: Prefix-Steered Recurrent Memory for Long-Video Understanding | 正文选读 | 本轮新增 |
| [2608.07663](https://arxiv.org/abs/2608.07663v2) | Keep It Simple: Multi-Key Episodic Memory Retrieval for Ultra-Long Video Understanding | 摘要/书目 | 本轮新增 |
| [2607.02096](https://arxiv.org/abs/2607.02096v1) | LongEgoRefer: A Benchmark for Long-Form Egocentric Video Referring Expression Comprehension | 摘要/书目 | 本轮新增 |

### 组合泛化/视觉推理 2026

| ID | 标题 | 深度 | 状态 |
|---|---|---|---|
| [2607.29586](https://arxiv.org/abs/2607.29586v1) | TraceViT: Grounded Trace Supervision for Visual Abstract Reasoning | 正文选读 | 本轮新增 |
| [2607.09061](https://arxiv.org/abs/2607.09061v1) | On Locality and Length Generalization in Visual Reasoning | 正文选读 | 本轮新增 |
| [2610.00064](https://arxiv.org/abs/2610.00064v1) | Reachability Is Not Generalization: Understanding Verb--Noun Decomposition in Assembly Action Recognition | 正文选读 | 本轮新增 |
| [2608.19871](https://arxiv.org/abs/2608.19871v1) | DIFFCZSL: Compositional Zero-Shot Learning Regularized by Diffusion Representations | 正文选读 | 本轮新增 |
| [2607.05911](https://arxiv.org/abs/2607.05911v1) | Progressive Reasoning with Primitive Correction for Compositional Zero-Shot Learning | 摘要/书目 | 本轮新增 |
| [2609.08242](https://arxiv.org/abs/2609.08242v1) | CS-CLIP: Compositional Scene Graph-guided CLIP for Robust Compositional Reasoning | 摘要/书目 | 本轮新增 |
| [2609.35032](https://arxiv.org/abs/2609.35032v1) | JRDB-AVR: An Active Visual Reasoning Benchmark for Embodied Agents in Real-World Environments | 正文选读 | 本轮新增 |
| [2610.13925](https://arxiv.org/abs/2610.13925v1) | Can machines reason non-verbally? | 摘要/书目 | 本轮新增 |
| [2610.08966](https://arxiv.org/abs/2610.08966v2) | Humanity's Sixth Sense: Benchmarking Intuitive Visual Reasoning in Multimodal Models | 摘要/书目 | 本轮新增 |

### 计数与视觉测量 2026

| ID | 标题 | 深度 | 状态 |
|---|---|---|---|
| [2609.17613](https://arxiv.org/abs/2609.17613v1) | DualCount: Structurally Consistent Density and Point Modeling for Zero-Shot Object Counting | 正文选读 | 本轮新增 |
| [2609.04716](https://arxiv.org/abs/2609.04716v1) | Counting Beyond Instances: A Benchmark for Group-Individual Object Counting | 正文选读 | 本轮新增 |
| [2603.12703](https://arxiv.org/abs/2603.12703v3) | SVCBench: A Streaming Video Counting Benchmark for Spatial-Temporal State Maintenance | 正文选读 | 本轮新增 |
| [2609.37096](https://arxiv.org/abs/2609.37096v2) | Why MLLMs Struggle to Count: Overcoming Individuation and Aggregation Bottlenecks with ConvStack | 正文选读 | 本轮新增 |
| [2607.16826](https://arxiv.org/abs/2607.16826v2) | Spatially-Aware Class-Agnostic Object Counting | 摘要/书目 | 本轮新增 |
| [2607.02139](https://arxiv.org/abs/2607.02139v1) | AdaCount: Training-Free Similarity-Guided Spatial and Feature Adaptation for Zero-Shot Object Counting | 摘要/书目 | 本轮新增 |
| [2601.13871](https://arxiv.org/abs/2601.13871v1) | OCCAM: Class-Agnostic, Training-Free, Prior-Free and Multi-Class Object Counting | 摘要/书目 | 本轮新增 |
| [2605.18063](https://arxiv.org/abs/2605.18063v1) | The MixCount Dataset: Bridging the Data Gap for Open-Vocabulary Object Counting | 摘要/书目 | 本轮新增 |
| [2606.17561](https://arxiv.org/abs/2606.17561v1) | RT-Counter: Real-Time Text-Guided Open-Vocabulary Object Counting | 正文选读 | 本轮新增 |
| [2605.17952](https://arxiv.org/abs/2605.17952v1) | Counting Machine Parts | 摘要/书目 | 本轮新增 |

### 人脸/表情/手势 2026

| ID | 标题 | 深度 | 状态 |
|---|---|---|---|
| [2609.16149](https://arxiv.org/abs/2609.16149v1) | DenseFace: Bias Mitigation in Face Recognition via Density-Aware Probabilistic Matching | 正文选读 | 本轮新增 |
| [2604.09127](https://arxiv.org/abs/2604.09127v1) | FaceLiVTv2: An Improved Hybrid Architecture for Efficient Mobile Face Recognition | 正文选读 | 本轮新增 |
| [2604.06782](https://arxiv.org/abs/2604.06782v1) | EventFace: Event-Based Face Recognition via Structure-Driven Spatiotemporal Modeling | 正文选读 | 本轮新增 |
| [2610.24832](https://arxiv.org/abs/2610.24832v1) | VTF900: A 900-Subject Visible-Thermal Face Recognition Dataset and Benchmark | 摘要/书目 | 本轮新增 |
| [2610.28766](https://arxiv.org/abs/2610.28766v1) | Different Defects, Different Effects: A Controlled Audit of Face Recognition Training Data | 正文选读 | 本轮新增 |
| [2606.32040](https://arxiv.org/abs/2606.32040v1) | FaceMoE: Mixture of Experts for Low-Resolution Face Recognition | 摘要/书目 | 本轮新增 |
| [2602.18763](https://arxiv.org/abs/2602.18763v1) | TAG: Thinking with Action Unit Grounding for Facial Expression Recognition | 正文选读 | 本轮新增 |
| [2604.08990](https://arxiv.org/abs/2604.08990v2) | ActFER: Agentic Facial Expression Recognition via Active Tool-Augmented Visual Reasoning | 摘要/书目 | 本轮新增 |
| [2608.13217](https://arxiv.org/abs/2608.13217v1) | UniCon-Former: Unified Convolution Transformer is All You Need for Hand Gesture Recognition | 摘要/书目 | 本轮新增 |
| [2605.12297](https://arxiv.org/abs/2605.12297v1) | EgoEV-HandPose: Egocentric 3D Hand Pose Estimation and Gesture Recognition with Stereo Event Cameras | 摘要/书目 | 本轮新增 |

### 分布偏移/持续适应 2026

| ID | 标题 | 深度 | 状态 |
|---|---|---|---|
| [2609.39934](https://arxiv.org/abs/2609.39934v2) | Reliability-Aware Checkpoint Selection for Domain Generalization | 正文选读 | 本轮新增 |
| [2610.00030](https://arxiv.org/abs/2610.00030v1) | Domain generalization and synthetic data in object detection: the enabler, the probe, and the gap | 正文选读 | 本轮新增 |
| [2608.18915](https://arxiv.org/abs/2608.18915v2) | Simple, Safe, and Overlooked: Reclaiming Sustainable Domain Generalization with Statistical Color Matching | 正文选读 | 本轮新增 |
| [2610.30680](https://arxiv.org/abs/2610.30680v1) | Zero-Shot Domain Generalization via Domain Prompt Learning | 摘要/书目 | 本轮新增 |
| [2608.29395](https://arxiv.org/abs/2608.29395v1) | GATE: Reliability-Gated Gaussian Evidence Fusion for Training-Free Test-Time Adaptation of Vision-Language Models | 摘要/书目 | 本轮新增 |
| [2610.06932](https://arxiv.org/abs/2610.06932v1) | RADC: Risk-Aware Dual Caching for Vision-Language Test-Time Adaptation | 摘要/书目 | 本轮新增 |
| [2607.08164](https://arxiv.org/abs/2607.08164v3) | Continual Test-Time Adaptation in Computer Vision: Methods, Benchmarks, and Future Directions | 摘要/书目 | 本轮新增 |
| [2610.19892](https://arxiv.org/abs/2610.19892v1) | On the Limits of Representation-Based Test-Time Adaptation for Multimodal LLMs | 摘要/书目 | 本轮新增 |
| [2607.04500](https://arxiv.org/abs/2607.04500v1) | Geographic Diversity Beats Data Volume for Cross-Domain Generalization in Zero-Label JEPA Driving World Models | 正文选读 | 本轮新增 |
| [2609.01683](https://arxiv.org/abs/2609.01683v1) | FORGE: Forward-Only Test-Time Adaptation for Integer-Only Vision Models on Microcontrollers | 摘要/书目 | 本轮新增 |

### 人体/手部/全身 3D 2026

| ID | 标题 | 深度 | 状态 |
|---|---|---|---|
| [2602.15989](https://arxiv.org/abs/2602.15989v1) | SAM 3D Body: Robust Full-Body Human Mesh Recovery | 正文选读 | 本轮新增 |
| [2603.15603](https://arxiv.org/abs/2603.15603v1) | Fast SAM 3D Body: Accelerating SAM 3D Body for Real-Time Full-Body Human Mesh Recovery | 正文选读 | 本轮新增 |
| [2603.17355](https://arxiv.org/abs/2603.17355v1) | OnlineHMR: Video-based Online World-Grounded Human Mesh Recovery | 正文选读 | 本轮新增 |
| [2605.09856](https://arxiv.org/abs/2605.09856v1) | MoPO: Incorporating Motion Prior for Occluded Human Mesh Recovery | 正文选读 | 本轮新增 |
| [2605.18102](https://arxiv.org/abs/2605.18102v3) | DanceHMR: Hand-Aware Whole-Body Human Mesh Recovery from Monocular Videos | 正文选读 | 本轮新增 |
| [2601.22693](https://arxiv.org/abs/2601.22693v2) | PEAR: Pixel-aligned Expressive humAn mesh Recovery | 摘要/书目 | 本轮新增 |
| [2605.12498](https://arxiv.org/abs/2605.12498v1) | EgoForce: Forearm-Guided Camera-Space 3D Hand Pose from a Monocular Egocentric Camera | 摘要/书目 | 本轮新增 |
| [2608.20093](https://arxiv.org/abs/2608.20093v2) | HandMvNet: Real-Time 3D Hand Pose Estimation Using Multi-View Cross-Attention Fusion | 摘要/书目 | 本轮新增 |
| [2603.25726](https://arxiv.org/abs/2603.25726v3) | AnyHand: A Large-Scale Synthetic Dataset for RGB(-D) Hand Pose Estimation | 摘要/书目 | 本轮新增 |
| [2604.08543](https://arxiv.org/abs/2604.08543v1) | E-3DPSM: A State Machine for Event-Based Egocentric 3D Human Pose Estimation | 摘要/书目 | 本轮新增 |

### 部件/可供性/功能场景 2026

| ID | 标题 | 深度 | 状态 |
|---|---|---|---|
| [2608.20720](https://arxiv.org/abs/2608.20720v1) | AffordAny: Open-World 3D Affordance Grounding from Monocular RGB Images via Vision-Language-Guided Geometric Reasoning | 正文选读 | 本轮新增 |
| [2609.37264](https://arxiv.org/abs/2609.37264v1) | UniAfford: Token-Routed Multitask Learning for Generalizable 2D-3D Affordance Perception | 正文选读 | 本轮新增 |
| [2606.02551](https://arxiv.org/abs/2606.02551v1) | AFUN: Towards an Affordance Foundation Model for Functionality Understanding | 摘要/书目 | 本轮新增 |
| [2605.01365](https://arxiv.org/abs/2605.01365v1) | VoxAfford: Multi-Scale Voxel-Token Fusion for Open-Vocabulary 3D Affordance Detection | 摘要/书目 | 本轮新增 |
| [2605.11616](https://arxiv.org/abs/2605.11616v1) | Grounding by Remembering: Cross-Scene and In-Scene Memory for 3D Functional Affordances | 摘要/书目 | 本轮新增 |
| [2609.25832](https://arxiv.org/abs/2609.25832v2) | PartLLM: A Unified Multimodal Foundation for 3D Part Segmentation | 正文选读 | 本轮新增 |
| [2609.12898](https://arxiv.org/abs/2609.12898v1) | UniPart: Towards Zero-shot Language-Grounded 3D Part Segmentation for Embodied Interaction | 正文选读 | 本轮新增 |
| [2610.23659](https://arxiv.org/abs/2610.23659v1) | FlexPart: Text-Controlled Semantics-Aware 3D Part Segmentation at Flexible Granularity | 摘要/书目 | 本轮新增 |
| [2601.01454](https://arxiv.org/abs/2601.01454v1) | PartImageNet++ Dataset: Enhancing Visual Models with High-Quality Part Annotations | 摘要/书目 | 本轮新增 |
| [2604.05621](https://arxiv.org/abs/2604.05621v2) | FunRec: Reconstructing Functional 3D Scenes from Egocentric Interaction Videos | 正文选读 | 本轮新增 |

### 边界/抠图/透明与伪装 2026

| ID | 标题 | 深度 | 状态 |
|---|---|---|---|
| [2601.14255](https://arxiv.org/abs/2601.14255v1) | VideoMaMa: Mask-Guided Video Matting via Generative Prior | 摘要/书目 | 本轮新增 |
| [2610.26857](https://arxiv.org/abs/2610.26857v1) | VideoMaMa++: Temporally Consistent Video Matting via Preserve-and-Refine Token | 正文选读 | 本轮新增 |
| [2608.08487](https://arxiv.org/abs/2608.08487v1) | RenderMatte: Exact-Alpha Rendering and Group-Relative Alignment for Image Matting | 正文选读 | 本轮新增 |
| [2601.12080](https://arxiv.org/abs/2601.12080v1) | Toward Real-World High-Precision Image Matting and Segmentation | 摘要/书目 | 本轮新增 |
| [2601.12147](https://arxiv.org/abs/2601.12147v1) | Segment and Matte Anything in a Unified Model | 摘要/书目 | 本轮新增 |
| [2601.03362](https://arxiv.org/abs/2601.03362v1) | Guardians of the Hair: Rescuing Soft Boundaries in Depth, Stereo, and Novel Views | 摘要/书目 | 本轮新增 |
| [2603.02648](https://arxiv.org/abs/2603.02648v1) | SEP-YOLO: Fourier-Domain Feature Representation for Transparent Object Instance Segmentation | 正文选读 | 本轮新增 |
| [2603.19547](https://arxiv.org/abs/2603.19547v1) | SeeClear: Reliable Transparent Object Depth Estimation via Generative Opacification | 正文选读 | 本轮新增 |
| [2608.11135](https://arxiv.org/abs/2608.11135v1) | Is There Really a Camouflaged Object? Towards Realistic Camouflaged Object Detection | 正文选读 | 本轮新增 |
| [2610.09807](https://arxiv.org/abs/2610.09807v1) | Concentration, Not Uncertainty: Why Targeted Synthetic Data Doesn't Help Camouflaged Object Detection | 摘要/书目 | 本轮新增 |

### 主动感知/视角规划 2026

| ID | 标题 | 深度 | 状态 |
|---|---|---|---|
| [2609.24124](https://arxiv.org/abs/2609.24124v2) | ActiveArena: Benchmarking and Understanding Active Perception in Robotic Manipulation | 正文选读 | 本轮新增 |
| [2603.22570](https://arxiv.org/abs/2603.22570v2) | CanViT: Toward Active-Vision Foundation Models | 正文选读 | 本轮新增 |
| [2603.00600](https://arxiv.org/abs/2603.00600v3) | I-Perceive: A Foundation Model for Vision-Language Active Perception | 正文选读 | 本轮新增 |
| [2609.18514](https://arxiv.org/abs/2609.18514v2) | ActiveScale: Scaling Active Perception for Robots across Model, Data, and Hardware | 摘要/书目 | 本轮新增 |
| [2609.17628](https://arxiv.org/abs/2609.17628v1) | LEAP: Learning Emergent Active Perception for Quadruped Navigation | 摘要/书目 | 本轮新增 |
| [2602.04600](https://arxiv.org/abs/2602.04600v2) | Act, Sense, Act: Learning Active Perception from Large-Scale Egocentric Human Data | 摘要/书目 | 本轮新增 |
| [2609.37292](https://arxiv.org/abs/2609.37292v1) | Recovering the View: Benchmarking Physical Active Vision for Occlusion Recovery in Robotic Manipulation | 正文选读 | 本轮新增 |
| [2609.23974](https://arxiv.org/abs/2609.23974v1) | LEAP-NBV: Lightweight Edge Active-Perception for Foundation-Model Next-Best-View Planning | 摘要/书目 | 本轮新增 |
| [2605.07943](https://arxiv.org/abs/2605.07943v2) | TAVIS: A Benchmark for Egocentric Active Vision and Anticipatory Gaze in Imitation Learning | 摘要/书目 | 本轮新增 |
| [2605.26627](https://arxiv.org/abs/2605.26627v2) | Breaking the Epistemic Trap: Active Perception Under Compound Uncertainty | 正文选读 | 本轮新增 |

### 点追踪/3D 运动 2026

| ID | 标题 | 深度 | 状态 |
|---|---|---|---|
| [2603.04989](https://arxiv.org/abs/2603.04989v2) | TAPFormer: Robust Arbitrary Point Tracking via Transient Asynchronous Fusion of Frames and Events | 正文选读 | 本轮新增 |
| [2603.17813](https://arxiv.org/abs/2603.17813v1) | M2P: Improving Visual Foundation Models with Mask-to-Point Weakly-Supervised Learning for Dense Point Tracking | 正文选读 | 本轮新增 |
| [2609.34035](https://arxiv.org/abs/2609.34035v1) | 3D Point Tracking with State Space Models | 正文选读 | 本轮新增 |
| [2603.02573](https://arxiv.org/abs/2603.02573v2) | Track4World: Feedforward World-centric Dense 3D Tracking of All Pixels | 正文选读 | 本轮新增 |
| [2610.03716](https://arxiv.org/abs/2610.03716v1) | MoSE3: Learning World-Space SE(3) at Every Pixel | 正文选读 | 本轮新增 |
| [2602.04877](https://arxiv.org/abs/2602.04877v1) | CoWTracker: Tracking by Warping instead of Correlation | 摘要/书目 | 本轮新增 |
| [2603.12217](https://arxiv.org/abs/2603.12217v1) | Real-World Point Tracking with Verifier-Guided Pseudo-Labeling | 摘要/书目 | 本轮新增 |
| [2602.04441](https://arxiv.org/abs/2602.04441v1) | SynthVerse: A Large-Scale Diverse Synthetic Dataset for Point Tracking | 摘要/书目 | 本轮新增 |
| [2605.12587](https://arxiv.org/abs/2605.12587v1) | TrackCraft3R: Repurposing Video Diffusion Transformers for Dense 3D Tracking | 摘要/书目 | 本轮新增 |
| [2604.02586](https://arxiv.org/abs/2604.02586v1) | TrackerSplat: Exploiting Point Tracking for Fast and Robust Dynamic 3D Gaussians Reconstruction | 摘要/书目 | 本轮新增 |

### 物体级 6-DoF 跟踪/关节物体 2026

| ID | 标题 | 深度 | 状态 |
|---|---|---|---|
| [2610.28962](https://arxiv.org/abs/2610.28962v1) | RoPT: Robust 6DoF Object Pose Tracking in Video | 正文选读 | 本轮新增 |
| [2609.39116](https://arxiv.org/abs/2609.39116v1) | GRC-Pose: Generation-Reconstruction Correspondence for Prior-Free 6D Object Pose Tracking | 正文选读 | 本轮新增 |
| [2605.23523](https://arxiv.org/abs/2605.23523v1) | ComPose: When to Trust Hands for Object Pose Tracking | 正文选读 | 本轮新增 |
| [2607.23468](https://arxiv.org/abs/2607.23468v1) | Robust 6-DoF Object Pose Tracking with Built-In Recovery under Occlusions and Rapid Object Motions | 正文选读 | 本轮新增 |
| [2610.15287](https://arxiv.org/abs/2610.15287v1) | ASM-6D: Fast Certified Pose-Shape Inference with Complete Correspondence Flow Maps | 正文选读 | 本轮新增 |
| [2603.28045](https://arxiv.org/abs/2603.28045v2) | Event6D: Event-based Novel Object 6D Pose Tracking | 摘要/书目 | 本轮新增 |
| [2603.08264](https://arxiv.org/abs/2603.08264v2) | Event-based Motion & Appearance Fusion for 6D Object Pose Tracking | 摘要/书目 | 本轮新增 |
| [2609.35046](https://arxiv.org/abs/2609.35046v1) | LEGAU: Learning Semantic Gaussian Priors for Scalable Category-level Pose Estimation | 摘要/书目 | 本轮新增 |
| [2602.19565](https://arxiv.org/abs/2602.19565v2) | DICArt: Advancing Category-level Articulated Object Pose Estimation in Discrete State-Spaces | 摘要/书目 | 本轮新增 |
| [2605.13018](https://arxiv.org/abs/2605.13018v2) | OCH3R: Object-Centric Holistic 3D Reconstruction | 摘要/书目 | 本轮新增 |

### 三维占据/场景图 2026

| ID | 标题 | 深度 | 状态 |
|---|---|---|---|
| [2603.23502](https://arxiv.org/abs/2603.23502v2) | OccAny: Generalized Unconstrained Urban 3D Occupancy | 正文选读 | 本轮新增 |
| [2608.08696](https://arxiv.org/abs/2608.08696v3) | OccAnyScene: Towards Unified Indoor-Outdoor 3D Occupancy Prediction | 摘要/书目 | 本轮新增 |
| [2605.25059](https://arxiv.org/abs/2605.25059v4) | VEOcc: Voxel-Centric Online Semantic Occupancy Prediction For Embodied Scene Understanding | 正文选读 | 本轮新增 |
| [2603.08521](https://arxiv.org/abs/2603.08521v3) | OccTrack360: 4D Panoptic Occupancy Tracking from Surround-View Fisheye Cameras | 正文选读 | 本轮新增 |
| [2610.22143](https://arxiv.org/abs/2610.22143v2) | FALCON: FPGA-Accelerated Latency-Certifiable Occupancy Networks for Camera-Based Autonomous Driving | 摘要/书目 | 本轮新增 |
| [2605.13741](https://arxiv.org/abs/2605.13741v1) | LEXI-SG: Monocular 3D Scene Graph Mapping with Room-Guided Feed-Forward Reconstruction | 正文选读 | 本轮新增 |
| [2601.02905](https://arxiv.org/abs/2601.02905v2) | LOST-3DSG: Lightweight Open-Vocabulary 3D Scene Graphs with Semantic Tracking in Dynamic Environments | 正文选读 | 本轮新增 |
| [2606.29786](https://arxiv.org/abs/2606.29786v2) | OP3DSG: Open-Vocabulary Part-Aware 3D Scene Graph Generation for Real-World Environments | 摘要/书目 | 本轮新增 |
| [2609.00619](https://arxiv.org/abs/2609.00619v1) | DSG: Dynamic 3D Scene Graph Construction for Embodied Agents in Changing Indoor Environments | 摘要/书目 | 本轮新增 |
| [2610.27696](https://arxiv.org/abs/2610.27696v1) | PanoGraphGS: Unifying Panoptic Segmentation and Hierarchical 3D Scene Graphs with Gaussian Splatting | 摘要/书目 | 本轮新增 |

### 补充：PMLR-only 正式记录

| ID | 标题 | 深度 | 状态 |
|---|---|---|---|
| [PMLR v306/nam26c](https://proceedings.mlr.press/v306/nam26c.html) | Causal-JEPA: Learning World Models through Object-Level Latent Masking | 摘要/官方记录 | 本轮新增 |

### 官方 artifact 核验（HTTP 200，未加载权重）

| Artifact | 入口 | 本轮核验 |
|---|---|---|
| YOLO26 | https://docs.ultralytics.com/models/yolo26/ · https://github.com/ultralytics/ultralytics | 官方模型页与论文 v1 对齐；未测速 |
| SAM 3 / SAM 3D | https://github.com/facebookresearch/sam3 · https://github.com/facebookresearch/sam3d | 代码/模型入口存在；未加载 |
| Depth Anything 3 | https://github.com/ByteDance-Seed/Depth-Anything-3 · https://depth-anything-3.github.io/ | 代码与项目页存在；未加载 |
| RF-DETR | https://github.com/roboflow/rf-detr · https://rfdetr.roboflow.com/ | 代码与文档存在；未运行 NAS |
| PaddleOCR-VL / PP-OCR | https://github.com/PaddlePaddle/PaddleOCR | 仓库存在；未下载权重 |
| dots.ocr | https://github.com/rednote-hilab/dots.ocr | 仓库存在；arXiv HTML 不可用，仅摘要+代码说明 |
| MinerU2.5 | https://github.com/opendatalab/MinerU | 仓库存在；未加载 |
| olmOCR 2 | https://github.com/allenai/olmocr · https://olmocr.allen.ai/ | 代码/项目存在；未加载 |
| DINOv3 / PE | https://github.com/facebookresearch/dinov3 · https://github.com/facebookresearch/perception_models | 代码/模型入口存在；未加载 |
| SAMURAI / MOTIP / OmniTrack / Cutie | https://github.com/yangchris11/samurai · https://github.com/MCG-NJU/MOTIP · https://github.com/xifen523/OmniTrack · https://github.com/hkchengrex/Cutie | 代码入口存在；未运行 |
| ViTPose / Sapiens / MoGe | https://github.com/ViTAE-Transformer/ViTPose · https://github.com/facebookresearch/sapiens · https://github.com/microsoft/MoGe | 代码入口存在；未加载 |
| OmniDocBench | https://github.com/opendatalab/OmniDocBench | 代码/数据入口存在；未运行评测 |

**未完成：** 上述 290 篇新增中 96 篇正文级选读（另 1 篇既有引用）；其余的方法细节、监督配比、全部实验与失败条件仍需逐篇复核。新批次没有执行任何 Clover 模型、权重转换、速度测量或基准复现。
<!-- END core-vision-source-frontier -->







<a id="verified-additions"></a>

## 镜面、因果与压缩方向的六篇既有核验记录

核验日期：2026-10-25。本轮是针对现有资料缺口的定向检索，不声称穷尽领域。以下均为外部文献；没有运行代码或产生 Clover 性能结果。阅读深度与 V/L 细分见链接的主题正文。

| 工作 | 固定版本 / 一手论文 | 官方复现资源 | 证据边界与主题落点 |
|---|---|---|---|
| Ref-NeRF | CVPR 2022：[论文](https://openaccess.thecvf.com/content/CVPR2022/html/Verbin_Ref-NeRF_Structured_View-Dependent_Appearance_for_Neural_Radiance_Fields_CVPR_2022_paper.html) | [项目](https://dorverbin.github.io/refnerf/) · [MultiNeRF](https://github.com/google-research/multinerf) | 摘要/项目/代码说明核对；posed RGB 多视图，非严格 V0；渲染改进不是物理分解唯一性。[观测](perception-and-identifiability.md#reflection-evidence) |
| NeRFactor | TOG / SIGGRAPH Asia 2021：[论文](https://arxiv.org/abs/2106.01970) | [项目](https://xiuming.info/projects/nerfactor/) · [代码](https://github.com/google/nerfactor) | 摘要/项目核对；光度拟合 L0 加测量 BRDF 先验 L4；不能称全链视觉自监督。[观测](perception-and-identifiability.md#reflection-evidence) |
| BISCUIT | UAI 2023：[PMLR 216](https://proceedings.mlr.press/v216/lippe23a.html) | [项目](https://phlippe.github.io/BISCUIT/) · [代码/数据](https://github.com/phlippe/BISCUIT) | 核对主文 §2–3；模拟、动作/regime L3，未知目标不消除辅助结构。[因果](causality-and-active-perception.md#causal-identification-evidence) |
| Sanity Checking Causal Representation Learning on a Simple Real-World System | ICML 2025：[PMLR 267](https://proceedings.mlr.press/v267/gamella25a.html) · [正文 v2](https://arxiv.org/html/2502.20099v2) | [代码](https://github.com/simonbing/CRLSanityCheck) · [Causal Chamber](https://github.com/juangamella/causal-chamber) | 核读 §2/§3.1/讨论；真实光学混合、合成因果控制，部分设置含 L4；选定方法的负结果不推广为所有方法不可能。[因果](causality-and-active-perception.md#causal-identification-evidence) |
| FastV | ECCV 2024：[论文 v3](https://arxiv.org/abs/2403.06764v3) | [代码](https://github.com/pkunlp-icler/FastV) | 核读 §4.2/§5/表1与4；FLOPs 和实测时延配置不同；VLM 含 L2。[压缩](representation-and-memory.md#compression-evidence) |
| FrameFusion | ICCV 2025：[论文 v2](https://arxiv.org/abs/2501.01986v2) | [代码](https://github.com/thu-nics/FrameFusion) | 核读 §5.1/§5.3–5.4；视频+文本/部分字幕，L2；token budget/端到端时延/版本须对应。[压缩](representation-and-memory.md#compression-evidence) |

检索词：`BISCUIT Causal Representation Learning Binary Interactions real world robot`；`Ref-NeRF Structured View-Dependent Appearance`；`NeRFactor shape reflectance unknown illumination`；`Sanity Checking Causal Representation Learning on a Simple Real-World System`；`FastV ECCV 2024`；`FrameFusion video token reduction`。检索来源为一手会议库、论文正文/摘要、作者项目和官方代码。未逐篇重审附录证明，未重验继承资料的全部链接。

## Contents

- [Source Map — Evidence → Research Question → Clover Landing](#topic-research-survey-source_map)
- [Papers and Primary Sources](#topic-research-survey-papers)
- [Datasets, Code, Checkpoints and Platform Resources](#topic-research-survey-datasets_code)
- [Frontier Methods](#topic-research-survey-frontier_methods)
- [Primary Source Index](#topic-research-literature-primary-sources)
- [Clover Model & Literature Index](#topic-research-literature-model-index)
- [Datasets, Benchmarks and Task Environments](#topic-research-literature-datasets-and-benchmarks)
- [Research Frontier Watch](#topic-research-research_frontier)
- [Stage-1 Frontier Sweep — 2026-10-16 → 2026-10-19](#topic-research-emerging-frontier_sweep_2026-10-19)
- [Frontier Signals — Filtered 2026 Watchlist](#topic-research-survey-frontier_signals)
- [2026 Frontier Watch — Physical World Models and Embodied Intelligence](#topic-research-literature-2026-frontier)

<a id="topic-research-survey-source_map"></a>

## Source Map — Evidence → Research Question → Clover Landing

Source record updated: 2026-10-19

This file maps important external evidence to the exact Clover research question it constrains. It is designed for fast review and to prevent source drift.

Evidence labels:

- `PRIMARY_PAPER` — peer-reviewed paper or primary preprint.
- `OFFICIAL_PROJECT` — official project/model/research page.
- `OPEN_SOURCE` — public code/checkpoint/resource.
- `OFFICIAL_REPORTED_RESULT` — company/lab result not independently reproduced here.
- `BACKGROUND_REFERENCE` — foundational book/review/historical source.

A source appearing here does **not** mean its mechanism is adopted.

Domain-level synthesis now lives in [`README.md`](README.md).

---

### 1. Foundations: partial observability, uncertainty, active perception

| Source | URL | Evidence | What it constrains | Clover landing |
|---|---|---|---|---|
| POMDPs in Robotics survey | https://arxiv.org/abs/2209.10342 | `PRIMARY_PAPER` | Real robot state is often partially observable; belief/state uncertainty is a first-class decision variable. | `README.md` §1; `perception-and-identifiability.md` |
| Probabilistic Robotics | https://mitpress.mit.edu/9780262201629/probabilistic-robotics/ | `BACKGROUND_REFERENCE` | Bayesian state estimation, localization and mapping under uncertainty. | `R-A`; `R-B` |
| Bajcsy, Active Perception | https://ieeexplore.ieee.org/abstract/document/5968 | `BACKGROUND_REFERENCE` | Perception includes selecting sensing actions to gain information. | `causality-and-active-perception.md`; V3 protocol |
| Spelke et al., Origins of Knowledge | https://pubmed.ncbi.nlm.nih.gov/1454901/ | `BACKGROUND_REFERENCE` | Continuity and solidity are useful object/physics research dimensions. Companion full text read 2026-10-20: Spelke (1994) "Initial knowledge: six suggestions", Cognition 50:431–445, states the object-domain principles as **cohesion, continuity, contact** — and explicitly *not* gravity or inertia (rationale: initial knowledge captures what is most *true*, not most obvious); looking-time knowledge ≠ reaching knowledge (task-specificity caveat). | `perception-and-identifiability.md`; 1992 full text itself still paywalled (abstract-level) |
| Baillargeon, Spelke & Wasserman 1985 — drawbridge | https://doi.org/10.1016/0010-0277(85)90008-3 | `BACKGROUND_REFERENCE` | 5-month-olds (n=21) look longer when a screen rotates *through* a hidden box than when it stops at it; control (n=22, box beside the screen) rules out rotation-length preference. Primary abstract read 2026-10-20; full text closed-access. | `perception-and-identifiability.md`; methodological ancestor of violation-of-expectation evaluation — must be paired with the perceptual-novelty counter-hypothesis (impossible event is more similar to habituation) |
| Physics for infants review | https://pubmed.ncbi.nlm.nih.gov/26302470/ | `BACKGROUND_REFERENCE` | Reviews continuity, solidity, cohesion and object/substance reasoning. | Benchmark interpretation; not a mandate to copy human cognition |
| Kaelbling, Littman & Cassandra 1998 — POMDP | https://doi.org/10.1016/S0004-3702(98)00023-X | `PRIMARY_PAPER` | Belief state is a sufficient statistic for history; optimal behaviour is a policy over beliefs; information-gathering actions are valued inside the value function (tiger problem: listening is provably optimal under uncertainty). Full text read 2026-10-19 (see [`README.md`](README.md#topic-survey_breadth) Axis A). | `perception-and-identifiability.md`; belief/licence discipline precedent — but assumes a complete, correct, enumerative model; no model learning, no vision |
| Khemakhem et al. 2020 — iVAE / nonlinear ICA identifiability | http://proceedings.mlr.press/v108/khemakhem20a.html | `PRIMARY_PAPER` | Learned latent state is identifiable (up to the transformations stated in the respective theorems) under an observed auxiliary variable modulating a factorised exponential-family prior; this is a sufficient-condition result, not a necessity theorem for every passive-video setting; unconditional latent models are provably non-identifiable. Corrigendum: the discrete-observation claim was retracted. Full text read 2026-10-19. | `R-F` theory background; every claimed world variable must name its auxiliary structure (time / action / multi-view) and its remaining equivalence class |
| Battaglia, Hamrick & Tenenbaum 2013 — intuitive physics engine | https://pmc.ncbi.nlm.nih.gov/articles/PMC3831455/ | `PRIMARY_PAPER` | Human physical judgments across 5 experiments are fit by approximate probabilistic simulation over an inferred scene distribution (uncertainty parameters σ/φ/μ; ~3–7 effective samples), including human illusions a ground-truth model misses. Full text read 2026-10-19. | `perception-and-identifiability.md`; also §8 — named rival to the queryable-state hypothesis; scene inputs were ground-truth-based, not estimated from pixels |

---

### 2. Classical geometry and motion

| Source | URL | Evidence | Demonstrates | Does not establish | Clover landing |
|---|---|---|---|---|---|
| Multiple View Geometry | https://www.robots.ox.ac.uk/~vgg/hzbook/ | `BACKGROUND_REFERENCE` | Projective/multi-view geometry has explicit mathematical structure. | Semantics, physics, causality. | `perception-and-identifiability.md` |
| ORB-SLAM3 paper | https://arxiv.org/abs/2007.11898 | `PRIMARY_PAPER` | Explicit pose/map/trajectory estimation, relocalization, multi-map (Atlas) reuse across mono/stereo/RGB-D × visual/visual-inertial; stereo-inertial EuRoC ATE ≈3.5 cm, multi-session 2.6–3.2× better than VINS-Mono; accuracy thesis: exploiting short/mid/long-term **and** multi-map data association beats front-end choices. Full text read 2026-10-20. | Open-world world understanding; named failure frontier: low texture (its stated main failure case), dynamic objects (outliers only, never state), pure rotation blocks monocular depth, IMU init needs gravity/roll-pitch excitation. | Classical baseline; `R-B` — degrade licences, never hallucinate state, exactly in its failure regimes |
| ORB-SLAM3 code | https://github.com/UZ-SLAMLab/ORB_SLAM3 | `OPEN_SOURCE` | Reproducible SLAM baseline. | — | Baseline setup |
| RAFT paper | https://arxiv.org/abs/2003.12039 | `PRIMARY_PAPER` | Strong dense optical flow / temporal correspondence. | Identity, permanence, causal state. | Motion baseline; `R-B` |
| RAFT code | https://github.com/princeton-vl/RAFT | `OPEN_SOURCE` | Reproducible flow baseline. | — | Baseline setup |
| DROID-SLAM paper | https://arxiv.org/abs/2108.10869 | `PRIMARY_PAPER` | Learned recurrent correspondence + differentiable dense bundle adjustment (Gauss–Newton over poses and per-pixel inverse depth); one model across mono/stereo/RGB-D; zero tracking failures on TartanAir/EuRoC/TUM-RGBD (EuRoC mono ATE 2.2 cm); ablation: removing DBA from training makes the system unstable. Full text read 2026-10-19. | Pose + dense depth only — no object/physical state; training is `L4` (synthetic TartanAir, ground-truth pose/depth supervision); pinhole intrinsics assumed known. | Learned-geometry baseline; `R-B` — the learned front-end did not replace geometric optimisation |
| DROID-SLAM code | https://github.com/princeton-vl/DROID-SLAM | `OPEN_SOURCE` | Reproducible learned-SLAM baseline. | — | Baseline setup |
| Nah, Kim & Lee 2017 — dynamic scene deblurring | https://openaccess.thecvf.com/content_cvpr_2017/html/Nah_Deep_Multi-Scale_Convolutional_CVPR_2017_paper.html | `PRIMARY_PAPER` | Multi-scale CNN restores sharp images from single motion-blurred photos without kernel estimation (PSNR 29.23 on the introduced GoPro benchmark, SOTA at publication). Verified 2026-10-20. | Restoration, not state estimation; GoPro "blur" is synthesised by averaging high-fps frames — an approximation of true long-exposure blur, and GoPro-trained models transfer imperfectly to real blur (RealBlur evidence). | Axis-D motion-blur boundary anchor: blurred RGB is photometrically repairable only insofar as the blur physics are invertible by dataset construction |
| Bijelic et al. 2020 — seeing through fog | https://openaccess.thecvf.com/content_CVPR_2020/html/Bijelic_Seeing_Through_Fog_Without_Seeing_Fog_Deep_Multimodal_Sensor_Fusion_CVPR_2020_paper.html | `PRIMARY_PAPER` | Documents how RGB detection degrades in fog/snow/rain relative to lidar/radar/gated-NIR (100k-label multimodal dataset, >10,000 km + fog chamber); entropy-driven fusion survives by falling back to non-RGB sensors. Bibliographic + abstract verified 2026-10-19. | **Not vision-alone evidence** — multimodal by design; usable only as an adverse-condition boundary / falsifier reference. | Observation-physics counter-anchor ([`README.md`](README.md#topic-survey_breadth) Axis D); any adverse-condition claim must state its observation regime |

---

### 3. Static self-supervised visual representation

| Source | URL | Evidence | Demonstrates | Open contradiction | Clover landing |
|---|---|---|---|---|---|
| DINOv3 research | https://ai.meta.com/research/publications/dinov3/ | `OFFICIAL_PROJECT` | Large-scale label-free image SSL; strong frozen dense features. | How much world structure still requires time/state? | `representation-and-memory.md`; generic visual baseline |
| DINOv3 paper | https://arxiv.org/abs/2508.10104 | `PRIMARY_PAPER` | 7B-scale SSL, 1.7B-image training, broad dense-task performance. | Static representation vs persistent world model. | Baseline/probing |
| DINOv3 code | https://github.com/facebookresearch/dinov3 | `OPEN_SOURCE` | Current reproducible Meta SSL baseline. | — | `sources-and-resources.md` |
| DINOv2 paper | https://arxiv.org/abs/2304.07193 | `PRIMARY_PAPER` | Historical predecessor and established SSL baseline. | Superseded as primary current static SSL comparator by DINOv3. | Historical comparison |

---

### 4. Predictive video representation and learned physical structure

| Source | URL | Evidence | Demonstrates | Open contradiction | Clover landing |
|---|---|---|---|---|---|
| V-JEPA 2 research | https://ai.meta.com/research/publications/v-jepa-2-self-supervised-video-models-enable-understanding-prediction-and-planning/ | `OFFICIAL_PROJECT` | Web-scale video SSL plus small robot post-training can support planning. | Does latent predictive state replace explicit state? | `R-C`; `R-G` |
| V-JEPA 2 paper | https://arxiv.org/abs/2506.09985 | `PRIMARY_PAPER` | Understanding, anticipation and action-conditioned planning. | What is encoded and how persistent is it? | Baseline/probing |
| V-JEPA 2 code | https://github.com/facebookresearch/vjepa2 | `OPEN_SOURCE` | Reproducible pretrained baseline. | — | `sources-and-resources.md` |
| V-JEPA 2.1 | https://arxiv.org/abs/2603.14482 | `PRIMARY_PAPER` | Dense, spatially structured and temporally consistent SSL features. | Dense latent vs explicit/entity state. | `R-C` |
| Interpreting Physics in Video World Models | https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/ | `PRIMARY_PAPER` | Physical variables can emerge as distributed/high-dimensional population codes. | Compact explicit physics variables are not automatically necessary. | `R-C`; `R-E` |
| Identifiable World Models | https://arxiv.org/abs/2610.07028 | `PRIMARY_PAPER` | Frozen diffusion latents can be aligned to identifiable state coordinates in studied systems. | Whether hybrid identifiable state scales to open-world robotics. | `R-C`; `R-F` |

---

### 5. Learned geometry and spatial reconstruction

| Source | URL | Evidence | Demonstrates | Open contradiction | Clover landing |
|---|---|---|---|---|---|
| DUSt3R | https://arxiv.org/abs/2312.14132 | `PRIMARY_PAPER` | Learned point-map reconstruction bridges learned and classical geometry. | Learned vs explicit geometry division of labor. | `perception-and-identifiability.md` |
| VGGT | https://arxiv.org/abs/2503.11651 | `PRIMARY_PAPER` | Cameras, depth, point maps and tracks from image sets. | Reconstruction vs world understanding. | Spatial baseline; `R-B` |
| VGGT code | https://github.com/facebookresearch/vggt | `OPEN_SOURCE` | Reproducible learned geometry. | — | Baseline setup |
| VGGT-Ω | https://arxiv.org/abs/2605.15195 | `PRIMARY_PAPER` | Scaled static/dynamic reconstruction; scene registers help VLA/language alignment. | Is reconstruction a sufficient spatial proxy? | `R-B`; `R-C` |
| VGGT-Ω project | https://vggt-omega.github.io/ | `OFFICIAL_PROJECT` | Project/evaluation resources. | — | `sources-and-resources.md` / `sources-and-resources.md` |
| VGGT-Ω code | https://github.com/facebookresearch/vggt-omega | `OPEN_SOURCE` | Reproducibility resource. | — | Baseline setup |
| ClearGrasp — Sajjan et al. 2020 | https://arxiv.org/abs/1910.02550 | `PRIMARY_PAPER` | From a single RGB-D image, networks infer surface normals, transparent-surface masks and occlusion boundaries, then complete the depth of transparent objects (trained on 50k+ synthetic RGB-D images; real benchmark 286 images); improves grasping on novel transparent objects. Verified 2026-10-20. | Input is RGB-**D**; the documented sensor fact is that depth channels themselves return corrupted values on transparent surfaces — learning repairs depth from RGB appearance cues. Training is synthetic-supervised (`L4`). | Axis-D transparent-material boundary anchor (RGB-D, never cite as RGB-alone); `R-B` |

---

### 6. Object-centric representation and visible entity tracking

| Source | URL | Evidence | Demonstrates | Open contradiction | Clover landing |
|---|---|---|---|---|---|
| Slot Attention | https://proceedings.neurips.cc/paper/2020/hash/8511df98c02ab60aea1b2356c013bc0f-Abstract.html | `PRIMARY_PAPER` | Exchangeable object-like slots and compositional generalization. | Scaling and real-world object discovery. | `representation-and-memory.md` |
| PLATO | https://www.nature.com/articles/s41562-022-01394-8 | `PRIMARY_PAPER` | Object-centric inductive bias can support intuitive-physics learning. | Whether object-centric state is necessary at scale. | `R-C`; `R-E` |
| SAM 3 research | https://ai.meta.com/research/publications/sam-3-segment-anything-with-concepts/ | `PRIMARY_PAPER` | Open-vocabulary detection, segmentation and video tracking. | Visible tracking is not object permanence. | `R-B`; `R-D` |
| SAM 3.1 code | https://github.com/facebookresearch/sam3 | `OPEN_SOURCE` | Current code/checkpoints for SAM 3/3.1. | — | `sources-and-resources.md` |
| SAM 3.1 release | https://github.com/facebookresearch/sam3/blob/main/RELEASE_SAM3p1.md | `OPEN_SOURCE` | Shared-memory object multiplexing improves multi-object tracking efficiency. | Does not create hidden-state permanence. | Primary contemporary tracking comparator |

---

### 7. Persistent visual memory

| Source | URL | Evidence | Demonstrates | Open contradiction | Clover landing |
|---|---|---|---|---|---|
| PersistBench paper | https://arxiv.org/abs/2609.20819 | `PRIMARY_PAPER` | 4D/world models lose object permanence, motion continuity and appearance consistency after objects leave view. | Seeing/reconstruction vs remembering. | `representation-and-memory.md`; Memory Battery |
| PersistBench project/code | https://guangzhaohe.com/persistbench | `OPEN_SOURCE` | Dataset/metric access. | — | `evaluation-and-benchmarks.md` |
| S-EMBER research | https://ai.meta.com/research/publications/s-ember-a-large-scale-benchmark-for-streaming-egocentric-memory-retrieval/ | `OFFICIAL_PROJECT` | Streaming grounded episodic retrieval exposes temporal localization gap. | Long context/scale vs grounded recall. | `R-D`; Memory Battery |
| S-EMBER paper | https://arxiv.org/abs/2607.02689 | `PRIMARY_PAPER` | 388 h streaming egocentric benchmark with temporal evidence localization. | Memory architecture remains open. | `evaluation-and-benchmarks.md` |
| VISTA | https://arxiv.org/abs/2610.02200 | `PRIMARY_PAPER` | Memory/evidence harness can be varied independently from model weights. | Replay vs recurrent/latent memory. | `R-D`; Evidence Replay hypothesis comparator |
| VISTA project | https://vista-research.github.io/ | `OFFICIAL_PROJECT` | Describes lossless visual memory and model-directed inspection. | Interactive-game evidence is not yet real-robot memory proof. | `R-D` |
| VISTA code | https://github.com/joshhhhhan/VISTA | `OPEN_SOURCE` | Reproducible harness implementation. | — | Future harness comparison |

---

### 8. Physics and anti-shortcut evaluation

| Source | URL | Evidence | Demonstrates | Open contradiction | Clover landing |
|---|---|---|---|---|---|
| IntPhys 2 | https://ai.meta.com/research/publications/intphys-2-benchmarking-intuitive-physics-understanding-in-complex-synthetic-environments/ | `PRIMARY_PAPER` | Permanence, immutability, continuity and solidity remain difficult. | Synthetic intuitive physics vs real-world transfer. | `perception-and-identifiability.md`; Understanding Battery |
| IntPhys 2 code | https://github.com/facebookresearch/IntPhys2 | `OPEN_SOURCE` | Reproducible benchmark. | — | Battery setup |
| MVP / Minimal Video Pairs | https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/ | `PRIMARY_PAPER` | Minimal pairs reveal shortcut-based physical reasoning. | QA still mixes language and visual evidence. | `R-E`; anti-shortcut policy |
| MVP code | https://github.com/facebookresearch/minimal_video_pairs | `OPEN_SOURCE` | Reproducible minimal-pair benchmark. | — | Battery setup |
| QuantiPhy | https://arxiv.org/abs/2512.19526 | `PRIMARY_PAPER` | Quantitative size/velocity/acceleration estimation exposes gap between verbal plausibility and numerical grounding. | How much quantitative state is needed for action. | `R-E`; quantitative physics battery |
| Principia | https://arxiv.org/abs/2609.04200 | `PRIMARY_PAPER` | Relational physics can be tested without absolute calibration; current generators/VLMs remain weak. | Relational consistency vs executable physical state. | `R-E`; Physics battery |
| Principia project | https://principiabench.github.io/ | `OFFICIAL_PROJECT` | Benchmark protocol/resources. | — | Battery setup |
| RoboPhys-3D | https://arxiv.org/abs/2608.28718 | `PRIMARY_PAPER` | State/execution-grounded metrics expose failures missed by appearance/VLM metrics. | How much 3D-grounded state predicts real task success. | `R-E`; `R-G`; world-model evaluation |
| Geirhos et al. 2020 — shortcut learning | https://arxiv.org/abs/2004.07780 | `PRIMARY_PAPER` | Decision rules that pass i.i.d. tests but fail o.o.d. unify many DNN failures (texture counting, hospital-token detection, context cues); shortcuts also occur in animal/human learning; o.o.d. tests themselves decay as models improve. Full text read 2026-10-19. | Perspective, not a certification procedure; the "intended solution" must be defined by the researcher. | Anti-shortcut audit for every capability claim (cheapest cue → misleading condition → examiner isolation); `R-E` |
| PlasticineLab | https://arxiv.org/abs/2104.03311 | `PRIMARY_PAPER` | 10 soft-body tasks / 50 configurations on differentiable MLS-MPM elastoplastic simulation; gradient-based open-loop planning solves many single-stage tasks (e.g. RollingPin 0.93 soft-IoU) where SAC/TD3/PPO largely fail; multi-stage tasks (Pinch, Writer) fail even with perfect state — gradients vanish at detachment/reattachment. Full text read 2026-10-19. | State is privileged particle landmarks (`L4`); no perception evaluated; open-loop plans assume full environment knowledge. | Deformable-planning evidence with an explicit "no perception-side benchmark exists" disclaimer; `R-E` |
| GNS — Sanchez-Gonzalez et al. 2020 | https://arxiv.org/abs/2002.09405 | `PRIMARY_PAPER` | Learned graph-network simulator over particle state generalises across fluids, rigid solids and deformable materials (Water/Sand/Goop), to ~10× particles and thousands of timesteps at test time. Abstract verified 2026-10-19. | Input is privileged particle state (`L4`) from classical simulators (SPH/MPM/PBD) — evidence about dynamics computation, not about observing state from vision. | Axis-E dynamics anchor ([`README.md`](README.md#topic-survey_breadth)); separates "dynamics from state" from "state from vision" |
| DPI-Net — Li et al. 2019 | https://arxiv.org/abs/1810.01566 | `PRIMARY_PAPER` | Learned particle dynamics (dynamic graph, hierarchical propagation) for fluids/rigid/deformables; dynamics + MPC control real foam/fluid tasks, beating PPO on sample efficiency. Bibliographic + provenance verified 2026-10-20. | State provenance is `MIXED`/privileged: training in simulation; real-world particles are sampled inside a depth-camera TSDF mesh — no learned pixel→state estimator anywhere. | Axis-E dynamics anchor; sharpens that real-world deformable state still arrives via classical reconstruction |
| RoboCraft — Shi et al. 2022 | https://www.roboticsproceedings.org/rss18/p008.html | `PRIMARY_PAPER` | Full perception→dynamics→planning loop for elasto-plastic shaping: particles sampled from RGB-D point cloud / reconstructed mesh; GNN dynamics trained **directly from raw visual data** (10 min real interaction, distribution losses, no particle correspondence); MPC shaping reaches untrained-human level incl. unseen target shapes. Bibliographic + provenance verified 2026-10-20. | Input is RGB-**D** (beyond RGB-only `V0–V2`); particle sampling leans on classical mesh reconstruction + shape priors, not an end-to-end learned estimator. | Axis-E **perception-side** anchor — closest existing "state from visual observation" demonstration for deformables; defines what a vision-alone successor must beat |
| Learning to See in the Dark — Chen et al. 2018 | https://arxiv.org/abs/1805.01934 | `PRIMARY_PAPER` | A network on raw sensor data replaces the ISP pipeline and restores clean images from extreme low light (<0.1 lux) short exposures; SID dataset: 5,094 raw short-exposure images with long-exposure references. Verified 2026-10-20. | Image restoration, not state estimation; supervision is a privileged pairing (long-exposure references). | Axis-D passive-RGB boundary anchor: the low-light noise floor can be learned *around* only with paired supervision |
| ExDark — Loh & Chan 2019 | https://doi.org/10.1016/j.cviu.2018.10.010 | `PRIMARY_PAPER` | 7,363 visible-light-only low-light images, 10 lighting conditions, box annotations for 12 classes; low-light corruption reaches deep into hand-crafted and learned features. Verified 2026-10-20. | Detection benchmark, low light only (no fog/rain/specularity); image+box annotations. | Axis-D boundary evidence: degraded RGB corrupts features non-superficially — "illumination invariance" is not a sufficient answer |
| Hidden Fluid Mechanics — Raissi et al. 2020 | https://doi.org/10.1126/science.aaw4741 | `PRIMARY_PAPER` | A Navier–Stokes-informed network infers **hidden velocity and pressure fields** from time series of passive-scalar (dye/smoke) concentration images, robust to low resolution and noise; also extracts lift/drag and wall shear in an aneurysm setting. Verified 2026-10-20. | Provenance `MIXED`: inputs are genuinely image-domain, but the governing PDE is supplied as prior (data assimilation for an inverse problem, not physics discovery) and benchmark visualisations are DNS-generated — no camera optics/occlusion/clutter. | Axis-E fluid perception-side anchor with the inverse-problem honesty condition: hidden fields are recoverable only because the physics class is given |
| Granular media manipulation — Schenck et al. 2017 | https://rse-lab.cs.washington.edu/papers/corl2017_granularmedia.pdf | `PRIMARY_PAPER` | First ConvNet dynamics model of granular media, learned from **real-robot** scoop-and-dump data (pinto beans in a tray); the dynamics model predicts next observed state and is used to shape target configurations, beating heuristic and value-network baselines. Full text read 2026-10-20. | State is a 2.5D heightmap **computed from the depth image** — surface only, no internal variables (stress, grain identity); RGB texture discarded. RGB-alone granular state remains unanchored anywhere (negative result, searched 2026-10-20). | Axis-E granular perception-side anchor (depth-derived, observed — not privileged); its boundary is the successor's target |
| Sainz et al. 2023 — data contamination | https://arxiv.org/abs/2310.18018 | `PRIMARY_PAPER` | Position paper (Findings of EMNLP 2023): training on a benchmark's test split silently overestimates performance and corrupts published conclusions; contamination must be **measured per benchmark**, not assumed away. Abstract-level verified 2026-10-20. | NLP/LLM setting; taxonomy and empirical probes not yet full-text read here. | Examiner-isolation doctrine for embodied benchmarks: simulator-asset leakage and pretraining-corpus leakage are the embodied forms of contamination |
| LiveBench — White et al. 2024 | https://arxiv.org/abs/2406.19314 | `PRIMARY_PAPER` | Contamination-**limited** (deliberately not "-free") benchmark design: monthly-refreshed questions from recent sources + automatic scoring against objective ground truth (no LLM judges); ICLR 2025 Spotlight. Abstract-level verified 2026-10-20. | Mitigation is temporal freshness + verifiable scoring, not proof of non-exposure; a later-trained model can still be contaminated on older releases. | Design pattern for Clover evaluation: dated, regenerated evaluation worlds + code-computed physical predicates instead of VLM judges |

---

### 9. Causality and intervention

| Source | URL | Evidence | Demonstrates | Open contradiction | Clover landing |
|---|---|---|---|---|---|
| CausalVQA | https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/ | `PRIMARY_PAPER` | Real-video counterfactual, hypothetical, anticipation and planning questions remain difficult. | Language QA vs machine-native causal state. | `causality-and-active-perception.md`; Causal Battery |
| CausalVQA paper | https://arxiv.org/abs/2506.09943 | `PRIMARY_PAPER` | Primary preprint for the benchmark. | — | `R-F` |
| CausalVQA code | https://github.com/facebookresearch/CausalVQA | `OPEN_SOURCE` | Reproducible benchmark/data interface. | — | Battery setup |
| Interventional CRL — Ahuja et al. | https://proceedings.mlr.press/v202/ahuja23a.html | `PRIMARY_PAPER` | Interventional data can identify latent causal factors under stated assumptions. | Which interventions a robot can obtain. | `R-F` theory background |
| CRL identifiability — Varici et al. | https://proceedings.mlr.press/v238/varici24a.html | `PRIMARY_PAPER` | Interventions can make latent causal models identifiable under broad stated assumptions. | What intervention structure is available to a robot. | `R-F` theory background |
| CRL multi-node interventions | https://proceedings.mlr.press/v236/bing24a | `PRIMARY_PAPER` | Extends identifiability analysis to multi-node interventions. | Passive-video-only causality remains underconstrained. | Active interaction rationale |
| Partially Observable CRL | https://proceedings.mlr.press/v235/xu24ac.html | `PRIMARY_PAPER` | Studies causal representation when observations expose changing subsets of latent state. | Scaling from synthetic assumptions to open-world vision. | `R-A`; `R-F` |
| CITRIS — Lippe et al. 2022 | https://proceedings.mlr.press/v162/lippe22a.html | `PRIMARY_PAPER` | From temporal image sequences with **known intervention targets** (values unknown), the intervention-affected ("minimal") causal variables are identifiable up to componentwise invertible transforms — including multidimensional factors; only some components of a factor need be affected. Verified 2026-10-20. | Assumes all causal relations are temporal (no instantaneous effects); targets must be observed, not discovered; synthetic rendered data only. | `R-F` theory background; identifiability ladder step 2 (time + known interventions) — see [`README.md`](README.md#topic-survey_breadth) A3 |
| iCITRIS — Lippe et al. 2023 | https://arxiv.org/abs/2206.06169 | `PRIMARY_PAPER` | Extends CITRIS to **instantaneous** effects (frame rate slower than true dynamics): with *partially-perfect* interventions (removing a variable's instantaneous parents), minimal causal variables **and** their temporal + instantaneous causal graph are jointly identifiable. Verified 2026-10-20 (ICLR 2023; arXiv ID corrected during verification). | The price is steeper: partially-perfect interventions, targets still observed; stylised synthetic video only — nothing on real robotic vision. | `R-F` theory background; ladder step 3 — passive video identifies none of this; the robot's own actions are the candidate intervention, and earning "intervention" status is itself a learning problem |

---

### 10. Active perception

| Source | URL | Evidence | Demonstrates | Open contradiction | Clover landing |
|---|---|---|---|---|---|
| Bajcsy, Active Perception | https://ieeexplore.ieee.org/abstract/document/5968 | `BACKGROUND_REFERENCE` | Perception can select actions that reduce uncertainty. | How to learn information value end-to-end. | `causality-and-active-perception.md`; V3 protocol |
| Vantage | https://arxiv.org/abs/2610.11810 | `PRIMARY_PAPER` | View planning/evidence acquisition can improve spatial reasoning. | General active world learning. | `R-H`; active-perception baseline |
| Vantage code | https://github.com/q1xiangchen/Vantage | `OPEN_SOURCE` | Reproducibility resource. | — | Baseline setup |
| Vision in Action | https://arxiv.org/abs/2506.15666 | `PRIMARY_PAPER` | Learns task-relevant searching/tracking/focusing camera behavior from human demonstrations. | Information-gain objective vs imitation. | `R-H` |
| SaPaVe | https://arxiv.org/abs/2603.12193 | `PRIMARY_PAPER` | Joint active perception/manipulation while decoupling camera and manipulation actions. | Generality beyond studied tasks. | `R-H`; sensing-action semantics |

---

### 11. Generative spatial/world models

| Source | URL | Evidence | Demonstrates | Open contradiction | Clover landing |
|---|---|---|---|---|---|
| World Labs Atlas | https://www.worldlabs.ai/blog/atlas | `OFFICIAL_REPORTED_RESULT` | Unified generation, reconstruction and space-time simulation with spatial context. | Plausible completion vs evidence-grounded belief. | Generative world-model route; C6 |
| World-model taxonomy | https://www.worldlabs.ai/blog/taxonomy-of-world-models | `OFFICIAL_PROJECT` | Clarifies renderer/simulator/planner functions commonly conflated as “world model.” | Taxonomy is not independent empirical validation. | Terminology background |
| Cosmos 3 project | https://research.nvidia.com/labs/cosmos-lab/cosmos3/ | `OFFICIAL_PROJECT` | Open omnimodal world-model family spanning reasoning, generation and action. | General benchmark strength vs robust persistent world truth. | Generative/WAM comparator |
| Cosmos 3 report | https://arxiv.org/abs/2606.02800 | `PRIMARY_PAPER` | Unifies language/image/video/audio/action in one architecture. | Whether unified generation/action is sufficient for robot belief. | Frontier method map |
| Cosmos code | https://github.com/nvidia/cosmos | `OPEN_SOURCE` | Public implementation/checkpoints/resources. | — | `sources-and-resources.md` |

---

### 12. VLA, embodied reasoning and robot foundation models

| Source | URL | Evidence | Demonstrates | Open contradiction | Clover landing |
|---|---|---|---|---|---|
| OpenVLA | https://arxiv.org/abs/2406.09246 | `PRIMARY_PAPER` | Open 7B VLA trained on 970k robot demonstrations. | Direct policy vs persistent world state. | `causality-and-active-perception.md`; open action baseline |
| OpenVLA code | https://github.com/openvla/openvla | `OPEN_SOURCE` | Fine-tuning/evaluation access. | — | Future embodied baseline |
| π0.5 | https://arxiv.org/abs/2504.16054 | `PRIMARY_PAPER` | Long-horizon manipulation in entirely new homes with heterogeneous multimodal co-training. | Visual understanding vs language/semantic/action priors. | `R-G`; strong direct-policy falsifier |
| π0.5 project | https://www.pi.website/blog/pi05 | `OFFICIAL_PROJECT` | Qualitative/system context. | — | Robot foundation map |
| Gemini Robotics ER 2 | https://deepmind.google/models/gemini-robotics/embodied-reasoning/ | `OFFICIAL_PROJECT` | High-level physical/spatial reasoning separated from lower-level VLA execution. | Persistent world-state semantics remain unspecified publicly. | `R-A`; `R-G` |
| Gemini ER 2 model card | https://deepmind.google/models/model-cards/gemini-robotics-er-2/ | `OFFICIAL_PROJECT` | Inputs, outputs, model dependency and limitation documentation. | — | Source of truth for claims |
| Gemini Robotics 2 | https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/ | `OFFICIAL_REPORTED_RESULT` | Whole-body VLA/control capabilities. | Independent reproducibility. | Robot-brain landscape |
| Figure Helix 2.5 | https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization | `OFFICIAL_REPORTED_RESULT` | Reports zero-shot long-horizon whole-body tasks across 30 unseen homes; controlled pretraining ablation. | Closed system; no independent Clover reproduction. | `R-G`; generalization reference |
| Skild S1 | https://www.skild.ai/blogs/s1 | `OFFICIAL_REPORTED_RESULT` | Reports in-context robot learning from video demonstrations and long-horizon unseen tasks. | Closed-system evidence. | `R-G`; `R-H` |
| Skild general-purpose brain | https://skild.ai/blogs/building-the-general-purpose-robotic-brain | `OFFICIAL_PROJECT` | Omni-bodied foundation-model thesis. | Does not establish world-state representation requirements. | Embodiment-invariance question |

---

### 13. World-action models

| Source | URL | Evidence | Demonstrates | Open contradiction | Clover landing |
|---|---|---|---|---|---|
| WAM survey | https://arxiv.org/abs/2609.16074 | `PRIMARY_PAPER` | Taxonomy linking future-state modeling and executable action generation. | Which factorization is actually necessary. | `R-G`; WAM research map |
| WAM resource index | https://rcl-robotics.github.io/Awesome-World-Action-Models | `OFFICIAL_PROJECT` | Current paper/resource map. | Curation is not evaluation. | Frontier tracking |
| World Action Models: Next Frontier | https://arxiv.org/abs/2605.12090 | `PRIMARY_PAPER` | Complementary cascaded/joint WAM taxonomy and evaluation framing. | Which taxonomy predicts robust embodied performance. | `R-G` |
| HWAM | https://arxiv.org/abs/2610.12026 | `PRIMARY_PAPER` | Explicitly models reference action vs realized state/action gap. | Whether joint state-action generation is best generally. | Execution-gap comparator; `R-G` |
| Being-M0.7 | https://arxiv.org/abs/2610.11283 | `PRIMARY_PAPER` | Transfers visual-motion priors from >10k h mixed human data before humanoid adaptation. | Human-motion priors vs learned world state. | `R-G`; human-video route |
| ReWAM | https://arxiv.org/abs/2609.38163 | `PRIMARY_PAPER` | Reconstruction/perceptual fidelity alone does not guarantee policy-useful state; action-grounded shaping matters. | What state is minimally sufficient for action. | `R-C`; `R-G` |

---

### 14. Lifelong learning, replay and self-generated experience

| Source | URL | Evidence | Demonstrates | Open contradiction | Clover landing |
|---|---|---|---|---|---|
| Lifelong Representations survey | https://arxiv.org/abs/2607.09785 | `PRIMARY_PAPER` | Taxonomy of continual self-supervised vision and forgetting-mitigation strategies. | Scaling continual adaptation to robot-scale open streams. | `R-H` |
| WAM continual imitation / REGEN | https://arxiv.org/abs/2606.27374 | `PRIMARY_PAPER` | Generative replay can reduce forgetting without stored original demonstrations; long-horizon/action-observation consistency are bottlenecks. | Synthetic replay truth vs useful rehearsal. | `R-H`; C6 |
| Skild Physical Self-Play | https://skild.ai/blogs/physical-self-play | `OFFICIAL_REPORTED_RESULT` | Reports self-play post-training in simulation followed by humanoid transfer. | Generality and independent reproduction. | `R-F`; `R-H`; interaction/self-generated experience |

---

### 15. Repository policy for adding new sources

Every new source should record:

```text
source
→ evidence level
→ exact URL
→ demonstrated capability
→ limitation / what it does not establish
→ research contradiction
→ Clover landing file
```

Prefer landing the source in one of the eight research dossiers as well as this map when it materially changes the research picture.

Do not add a paper only because it is recent. Do not use a news summary when a primary paper or official source is available. Historical news is a discovery signal only and remains in Git history; durable claims require primary or official evidence before entering these topic records.

---

<a id="topic-research-survey-papers"></a>

## Papers and Primary Sources

Source record updated: 2026-10-14

Curated reading index for the Clover Survey. Sources are grouped by the research contradiction they constrain.

> **Research question:** How can a machine understand the real world through vision alone?

Use [`sources-and-resources.md`](#topic-research-survey-source_map) when you need the one-to-one mapping from source → demonstrated capability → limitation → Clover landing.

---

### Foundations: uncertainty, partial observability and active perception

- POMDPs in Robotics survey — https://arxiv.org/abs/2209.10342
- Probabilistic Robotics — https://mitpress.mit.edu/9780262201629/probabilistic-robotics/
- Bajcsy, Active Perception — https://ieeexplore.ieee.org/abstract/document/5968
- Spelke et al., Origins of Knowledge — https://pubmed.ncbi.nlm.nih.gov/1454901/
- Physics for infants review — https://pubmed.ncbi.nlm.nih.gov/26302470/

### Historical representation shift

- SIFT — https://www.cs.ubc.ca/~lowe/papers/ijcv04.pdf
- HOG — https://lear.inrialpes.fr/people/triggs/pubs/Dalal-cvpr05.pdf
- AlexNet — https://papers.nips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf
- ResNet — https://arxiv.org/abs/1512.03385
- Vision Transformer — https://arxiv.org/abs/2010.11929
- CLIP — https://arxiv.org/abs/2103.00020

### Classical geometry / motion

- Multiple View Geometry — https://www.robots.ox.ac.uk/~vgg/hzbook/
- ORB-SLAM3 — https://arxiv.org/abs/2007.11898 · https://github.com/UZ-SLAMLab/ORB_SLAM3
- RAFT — https://arxiv.org/abs/2003.12039 · https://github.com/princeton-vl/RAFT

### Static self-supervised visual representation

- I-JEPA — https://arxiv.org/abs/2301.08243
- DINOv2 — https://arxiv.org/abs/2304.07193 · https://github.com/facebookresearch/dinov2
- DINOv3 research — https://ai.meta.com/research/publications/dinov3/
- DINOv3 paper — https://arxiv.org/abs/2508.10104
- DINOv3 code — https://github.com/facebookresearch/dinov3

### Predictive video representation / video world models

- V-JEPA — https://arxiv.org/abs/2404.08471
- V-JEPA 2 — https://arxiv.org/abs/2506.09985 · https://ai.meta.com/research/publications/v-jepa-2-self-supervised-video-models-enable-understanding-prediction-and-planning/ · https://github.com/facebookresearch/vjepa2
- V-JEPA 2.1 — https://arxiv.org/abs/2603.14482
- Interpreting Physics in Video World Models — https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/

### Geometry and spatial intelligence

- NeRF — https://arxiv.org/abs/2003.08934
- DUSt3R — https://arxiv.org/abs/2312.14132
- VGGT — https://arxiv.org/abs/2503.11651 · https://github.com/facebookresearch/vggt
- VGGT-Ω — https://arxiv.org/abs/2605.15195 · https://vggt-omega.github.io/ · https://github.com/facebookresearch/vggt-omega

### Object-centric representation / visible entities

- Slot Attention — https://proceedings.neurips.cc/paper/2020/hash/8511df98c02ab60aea1b2356c013bc0f-Abstract.html
- PLATO — https://www.nature.com/articles/s41562-022-01394-8
- SAM 2 — https://arxiv.org/abs/2408.00714 · https://github.com/facebookresearch/sam2
- SAM 3 — https://ai.meta.com/research/publications/sam-3-segment-anything-with-concepts/ · https://arxiv.org/abs/2511.16719
- SAM 3 / 3.1 code — https://github.com/facebookresearch/sam3
- SAM 3.1 release notes — https://github.com/facebookresearch/sam3/blob/main/RELEASE_SAM3p1.md

### Persistent visual / episodic memory

- PersistBench — https://arxiv.org/abs/2609.20819 · https://guangzhaohe.com/persistbench
- S-EMBER — https://ai.meta.com/research/publications/s-ember-a-large-scale-benchmark-for-streaming-egocentric-memory-retrieval/ · https://arxiv.org/abs/2607.02689
- VISTA — https://arxiv.org/abs/2610.02200

### Active evidence / spatial reasoning

- Vantage — https://arxiv.org/abs/2610.11810 · https://github.com/q1xiangchen/Vantage
- SpatialCORE — https://arxiv.org/abs/2609.38716 · https://github.com/rafiibnsultan/SpatialCORE

### Intuitive physics / physical consistency

- IntPhys 2 — https://ai.meta.com/research/publications/intphys-2-benchmarking-intuitive-physics-understanding-in-complex-synthetic-environments/ · https://github.com/facebookresearch/IntPhys2
- MVP / Minimal Video Pairs — https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/
- Principia — https://arxiv.org/abs/2609.04200
- Interpreting Physics in Video World Models — https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/
- RoboPhys-3D — https://arxiv.org/abs/2608.28718

### Causality / intervention / counterfactuals

- CausalVQA — https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/
- General Identifiability and Achievability for Causal Representation Learning — https://proceedings.mlr.press/v238/varici24a.html
- Identifying Linearly-Mixed Causal Representations from Multi-Node Interventions — https://proceedings.mlr.press/v236/bing24a

### World models for control

- DreamerV3 — https://arxiv.org/abs/2301.04104
- TD-MPC2 — https://arxiv.org/abs/2310.16828
- H-WM — https://arxiv.org/abs/2602.11291
- Identifiable World Models — https://arxiv.org/abs/2610.07028

### Generative / spatial world models

- World Labs Atlas — https://www.worldlabs.ai/blog/atlas
- World Labs world-model taxonomy — https://www.worldlabs.ai/blog/taxonomy-of-world-models
- Cosmos 3 project — https://research.nvidia.com/labs/cosmos-lab/cosmos3/
- Cosmos 3 report — https://arxiv.org/abs/2606.02800
- Cosmos code — https://github.com/nvidia/cosmos
- EVEWorld — https://arxiv.org/abs/2610.03374
- DR-WM / From Pixels to Executable Physics — https://arxiv.org/abs/2610.17630

### VLA / world-action models

- RT-2 — https://arxiv.org/abs/2307.15818
- OpenVLA — https://arxiv.org/abs/2406.09246 · https://github.com/openvla/openvla
- π0.5 — https://arxiv.org/abs/2504.16054 · https://www.pi.website/blog/pi05
- ReWAM — https://arxiv.org/abs/2609.38163
- HWAM — https://arxiv.org/abs/2610.12026
- Being-H0.7 — https://arxiv.org/abs/2605.00078
- Being-M0.7 — https://arxiv.org/abs/2610.11283
- WAM survey — https://arxiv.org/abs/2609.16074
- WAM resource page — https://rcl-robotics.github.io/Awesome-World-Action-Models

### Embodied reasoning / robot-brain systems

- Gemini Robotics ER 2 overview — https://deepmind.google/models/gemini-robotics/embodied-reasoning/
- Gemini Robotics ER 2 model card — https://deepmind.google/models/model-cards/gemini-robotics-er-2/
- Gemini Robotics 2 — https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/
- Figure Helix 2.5 — https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization
- Skild S1 — https://www.skild.ai/blogs/s1
- Skild general-purpose robot brain — https://skild.ai/blogs/building-the-general-purpose-robotic-brain
- Skild Physical Self-Play — https://skild.ai/blogs/physical-self-play

### General video / egocentric data and evaluation

- Perception Test — https://github.com/google-deepmind/perception_test
- Ego4D — https://ego4d-data.org/ · https://ego4d-data.org/docs/
- EPIC-KITCHENS — https://epic-kitchens.github.io/
- Something-Something — https://developer.qualcomm.com/software/ai-datasets/something-something

### Robot datasets / embodied task suites

- DROID — https://droid-dataset.github.io/droid/
- Open X-Embodiment — https://github.com/google-deepmind/open_x_embodiment
- BridgeData V2 — https://rail-berkeley.github.io/bridgedata/
- LIBERO — https://libero-project.github.io/main.html · https://github.com/Lifelong-Robot-Learning/LIBERO
- CALVIN — https://github.com/mees/calvin
- RoboCasa — https://robocasa.ai/ · https://robocasa.ai/leaderboard.html
- ManiSkill — https://github.com/haosulab/ManiSkill

### Sparse computation

- Motion-aware Event Suppression — https://arxiv.org/abs/2602.23204

### Surveys

- Physical AI survey — https://arxiv.org/abs/2510.04978
- World-Action Models survey — https://arxiv.org/abs/2609.16074
- POMDPs in Robotics survey — https://arxiv.org/abs/2209.10342

---

### Reading priority

#### Tier 0 — problem foundations

POMDP/Probabilistic Robotics → Active Perception → classical geometry → cognitive/object-physics background.

#### Tier 1 — strongest representation counter-hypotheses

DINOv3 → V-JEPA 2/2.1 → Interpreting Physics → VGGT/Ω → Slot Attention/PLATO → PersistBench/S-EMBER.

#### Tier 2 — world/action alternatives

Atlas/Cosmos 3 → OpenVLA/π0.5 → Gemini ER 2 → Helix 2.5 → Skild S1 → WAM survey + representative WAMs.

#### Tier 3 — evaluation/falsification

IntPhys 2 → MVP → Principia → CausalVQA → PersistBench → S-EMBER → RoboPhys-3D → real unseen-environment long-horizon tasks.

#### Rule

Do not read only systems that resemble historical Clover. Strong counter-hypotheses are higher-value research targets than confirming examples.

---

<a id="topic-research-survey-datasets_code"></a>

## Datasets, Code, Checkpoints and Platform Resources

Source record updated: 2026-10-14

Practical resource map for the Clover Stage-1 research and later baseline/evaluation phases. Listing a resource does **not** mean it should be reproduced immediately.

Before running anything substantial, record:

```text
research question
expected discriminatory result
why this resource is necessary
smaller alternative
observation protocol V0–V3
learning-evidence provenance L0–L4
compute/storage requirements
M4/MPS/CUDA compatibility
licence terms
evidence level
```

---

### Static visual representation

#### DINOv3 — primary current SSL baseline

- Paper — https://arxiv.org/abs/2508.10104
- Research page — https://ai.meta.com/research/publications/dinov3/
- Project — https://ai.meta.com/research/dinov3/
- Code — https://github.com/facebookresearch/dinov3

Use for frozen feature probing, dense representation analysis and comparison against temporal/world-model representations.

#### DINOv2 — retained predecessor

- Paper — https://arxiv.org/abs/2304.07193
- Code — https://github.com/facebookresearch/dinov2

Useful for historical continuity and lighter existing tooling.

---

### Video / predictive representation

#### V-JEPA 2 / 2.1

- V-JEPA 2 paper — https://arxiv.org/abs/2506.09985
- V-JEPA 2 research — https://ai.meta.com/research/publications/v-jepa-2-self-supervised-video-models-enable-understanding-prediction-and-planning/
- Code/checkpoints — https://github.com/facebookresearch/vjepa2
- V-JEPA 2.1 paper — https://arxiv.org/abs/2603.14482
- Physics interpretation — https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/

Initial work should prioritize pretrained inference and probing, not pretraining from scratch.

---

### Visible entity detection / segmentation / tracking

#### SAM 3 / SAM 3.1 — primary current visible-entity baseline

- Research — https://ai.meta.com/research/publications/sam-3-segment-anything-with-concepts/
- Paper — https://arxiv.org/abs/2511.16719
- Code — https://github.com/facebookresearch/sam3
- SAM 3.1 release notes — https://github.com/facebookresearch/sam3/blob/main/RELEASE_SAM3p1.md

Use as a strong comparator for visible identity/tracking. Do not interpret successful mask tracking as hidden-state object permanence.

#### SAM 2 — predecessor

- Paper — https://arxiv.org/abs/2408.00714
- Code — https://github.com/facebookresearch/sam2

#### TAO-Amodal — amodal/occlusion diagnostic

- Paper — https://arxiv.org/abs/2312.12433

Use to keep the distinctions explicit:

```text
visible tracking
≠
amodal completion
≠
re-identification
≠
object permanence
```

---

### Geometry / spatial / dynamic-4D reconstruction

- ORB-SLAM3 — https://arxiv.org/abs/2007.11898 · https://github.com/UZ-SLAMLab/ORB_SLAM3
- RAFT — https://arxiv.org/abs/2003.12039 · https://github.com/princeton-vl/RAFT
- DUSt3R — https://arxiv.org/abs/2312.14132
- VGGT — https://arxiv.org/abs/2503.11651 · https://github.com/facebookresearch/vggt
- VGGT-Ω — https://arxiv.org/abs/2605.15195 · https://vggt-omega.github.io/ · https://github.com/facebookresearch/vggt-omega
- 4DVGGT-D — https://arxiv.org/abs/2605.12027
- DP-DeGauss — https://arxiv.org/abs/2604.07986
- 4D reconstruction survey/resources — https://arxiv.org/abs/2609.39960 · https://github.com/ZiyangYan/Awesome-4D-Scene-Reconstruction
- Vantage — https://arxiv.org/abs/2610.11810 · https://github.com/q1xiangchen/Vantage
- SpatialCORE — https://arxiv.org/abs/2609.38716 · https://github.com/rafiibnsultan/SpatialCORE

Use 4DVGGT-D and DP-DeGauss specifically when studying camera ego-motion vs object-motion separation in dynamic scenes.

VGGT-family official examples may be CUDA-oriented. Small-sequence pretrained inference/probing should be attempted before any expensive adaptation.

---

### Persistent visual / episodic / semantic / dynamic-world memory

#### PersistBench

- Paper — https://arxiv.org/abs/2609.20819
- Project/code/data — https://guangzhaohe.com/persistbench

Use for object permanence, motion continuity and appearance preservation after objects leave the field of view.

#### WROP — object-permanence training/exam infrastructure

- Paper — https://arxiv.org/abs/2609.28654

WROP provides cognitive-science-inspired object-permanence/solidity tasks, a large synthetic training corpus and a held-out exam for video world models.

Use it to distinguish:

```text
training a permanence prior
vs
testing persistent memory in realistic scenes
```

#### S-EMBER

- Research page — https://ai.meta.com/research/publications/s-ember-a-large-scale-benchmark-for-streaming-egocentric-memory-retrieval/
- Paper — https://arxiv.org/abs/2607.02689

Use for streaming grounded episodic retrieval and temporal evidence localization.

#### VISTA

- Paper — https://arxiv.org/abs/2610.02200

Relevant to memory/retrieval-harness comparisons. Reproduce only when the exact harness question becomes active.

#### PerSeM

- Paper — https://arxiv.org/abs/2609.19542

Training-free persistent semantic memory baseline for long-horizon open-vocabulary mapping. Useful as a comparator for frame-wise semantics vs persistent world-space aggregation.

#### OASIS-Map

- Paper — https://arxiv.org/abs/2607.14899
- Project — https://dynamic.robots.ox.ac.uk/projects/oasis-map/

Use for multi-session object-level world change:

```text
appeared
disappeared
moved
replaced
re-associated across revisits
```

This is a strong baseline for the distinction between **memory** and **belief revision after the real world changed**.

#### R4DSG

- Paper — https://arxiv.org/abs/2608.11017
- Project — https://dualtransparency.github.io/R4DSG/

RGB-only relative 4D scene-graph memory for long egocentric video. Useful for persistent identity, anchor-relative object change and long-horizon object-centric retrieval without assuming a globally aligned metric reconstruction.

---

### Physical quantities, material properties and system identification

#### Physically Guided Visual Mass Estimation

- Paper — https://arxiv.org/abs/2601.20303

Single-RGB mass estimator that explicitly treats mass inference as ill-posed and uses geometry/volume and material/density-related priors.

Use for studying:

```text
statistical mass prediction
vs
physical identifiability
```

#### PhysQuantAgent / VisPhysQuant

- Paper — https://arxiv.org/abs/2603.16958

Real-object mass-estimation benchmark with multi-view RGB-D videos and measured mass ground truth.

Protocol caution: RGB-D is not a strict V0/V1 RGB-only condition.

#### Visual + haptic friction mapping

- Paper — https://arxiv.org/abs/2010.08277

Important foundational evidence that friction is often poorly constrained by appearance alone and benefits from physical exploration.

#### Generalizable Friction Coefficient Estimation

- Paper — https://arxiv.org/abs/2604.24188

Uses material embeddings learned from measured proxy interactions rather than assuming friction is directly visible.

#### DR-WM / From Pixels to Executable Physics

- Paper — https://arxiv.org/abs/2610.17630

Separates RGB geometry from terrain/contact properties calibrated through action-response experience.

Use as a key Stage-1 system-identification reference.

---

### Deformable, articulated and cross-regime world models

#### PointCast

- Paper — https://arxiv.org/abs/2609.28393
- Project — https://pointcast-wm.github.io/

Identity-bearing 3D point-set world model evaluated across rigid objects, cloth, rope and multi-joint cabinets.

Use to probe whether a common representation can span qualitatively different physical regimes.

#### PointWorld

- Paper — https://arxiv.org/abs/2601.03782
- Project — https://point-world.github.io/

3D point-flow action/world representation spanning rigid pushing, deformable/articulated manipulation and tool use.

Protocol caution: uses RGB-D rather than strict monocular RGB.

#### WorldContact

- Paper — https://arxiv.org/abs/2609.19600

Contact-centric world modeling for deformable-object manipulation. Relevant to bags, cloth and other tasks where geometry alone is insufficient.

#### Learning to Unfold Cloth

- Paper — https://arxiv.org/abs/2602.16675

Dreamer-style deformable-object world model with surface-normal input and real-robot transfer.

Protocol caution: surface normals provide stronger geometric evidence than raw monocular RGB.

#### ManiSoft

- Paper — https://arxiv.org/abs/2605.18617
- Project/code/data — https://buaa-colalab.github.io/ManiSoft

Benchmark for visual-language manipulation with soft continuum robot arms. Important because the robot body itself can be deformable and visually uncertain.

#### DexSim2Real²

- Paper — https://arxiv.org/abs/2409.08750

Uses active one-step interaction to construct an explicit world model/digital twin of unseen articulated objects.

---

### Liquid / weakly visible physical properties

#### VLM-based Physical Reasoning for Robot Liquid Perception

- Paper — https://arxiv.org/abs/2404.06904

Useful as a boundary example: vision-only liquid reasoning was weaker than a setup that incorporated interaction-derived force/torque information encoded visually.

Do not classify viscosity estimation from this work as passive-RGB evidence.

---

### Uncertainty / selective prediction under partial visual evidence

#### Decision-Aware Uncertainty Evaluation of VLM Early Action Anticipation

- Paper — https://arxiv.org/abs/2603.10061

Use for calibration/selective-prediction protocols under temporally partial egocentric observations.

Relevant measurements:

```text
calibration
coverage
selective risk
confidence vs evidence amount
abstention quality
```

---

### Physical / causal / embodied-reasoning evaluation

#### IntPhys 2

- Research — https://ai.meta.com/research/publications/intphys-2-benchmarking-intuitive-physics-understanding-in-complex-synthetic-environments/
- Code — https://github.com/facebookresearch/IntPhys2

#### MVP / Minimal Video Pairs

- Research — https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/

#### CausalVQA

- Research — https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/

#### Principia

- Paper — https://arxiv.org/abs/2609.04200

#### RoboPhys-3D

- Paper — https://arxiv.org/abs/2608.28718

#### Perception Test

- Code/data — https://github.com/google-deepmind/perception_test

Use visual-only subsets where the experiment claims a V0–V3 vision protocol.

#### ERQA — Embodied Reasoning Question Answer

- Code/data/evaluation harness — https://github.com/embodiedreasoning/ERQA

Open 400-example multimodal embodied/spatial reasoning diagnostic. Useful for low-cost model comparison before real-robot evaluation, but do not interpret ERQA accuracy as persistent world understanding; language/world-knowledge priors are a major confound.

#### RobotWorld

- Paper — https://arxiv.org/abs/2610.10409

Useful for system-level physical-agent capability across heterogeneous tasks and for studying composition, retained task/world state, recovery and completion verification.

#### RoboWM-Bench

- Paper — https://arxiv.org/abs/2604.19092

Use for the distinction between visually plausible generated behavior and robot-executable behavior.

#### RoboTrustBench

- Paper — https://arxiv.org/abs/2606.01600

Use for constraint-sensitive, counterfactual and adversarial world-model evaluation.

#### Video2World

- Paper — https://arxiv.org/abs/2610.04432

Use for geometry/dynamics/functional correctness of reconstructed simulation worlds rather than render similarity alone.

---

### Physically grounded articulated / functional 3D assets

#### Artisan

- Paper — https://arxiv.org/abs/2610.13947
- Project link is exposed from the arXiv record: https://physicalvision.github.io

Artisan and its benchmark expand 3D evaluation beyond geometry/appearance/articulation to collision-free motion, stability under gravity, mass/material properties and downstream functional behavior.

Important boundary:

```text
physically grounded generated asset
≠
proof that real mass/material properties are identifiable from passive RGB
```

Use as a Stage-1 reference for articulated-object function, physical asset quality and simulation-grounded evaluation.

---

### Open robot / VLA baselines

#### OpenVLA

- Paper — https://arxiv.org/abs/2406.09246
- Code — https://github.com/openvla/openvla

OpenVLA remains a useful established open VLA comparator.

Do not start with full training. First document architecture, action representation, input history, BridgeData/Open X data assumptions, LIBERO evaluation and whether persistent world state is externally represented.

#### NVIDIA Isaac GR00T N1.7 — current open humanoid VLA reference

- Code — https://github.com/NVIDIA/Isaac-GR00T
- Model — https://huggingface.co/nvidia/GR00T-N1.7-3B
- Official technical overview — https://developer.nvidia.com/blog/develop-humanoid-robot-policies-end-to-end-with-nvidia-isaac-gr00t/

Use as a strong reproducible direct-policy counter-hypothesis when embodied evaluation becomes active. Its training uses robot demonstrations plus large-scale human/egocentric data, so do not classify it as `L0` visual-only learning.

---

### Robot datasets

- DROID — https://droid-dataset.github.io/droid/
- Open X-Embodiment code/data — https://github.com/google-deepmind/open_x_embodiment
- Open X overview — https://deepmind.google/blog/scaling-up-learning-across-many-different-robot-types/
- BridgeData V2 — https://rail-berkeley.github.io/bridgedata/

These datasets often include action/robot-state information and therefore are not `L0` visual-only learning evidence.

---

### Human / egocentric video

- Ego4D — https://ego4d-data.org/ · https://ego4d-data.org/docs/
- EPIC-KITCHENS — https://epic-kitchens.github.io/
- Something-Something — https://developer.qualcomm.com/software/ai-datasets/something-something

Useful for motion, interaction, anticipation and long-horizon visual history.

Current robot-policy systems increasingly use large human/egocentric-video corpora. Stage 1 should always distinguish raw visual pretraining from paired motion/action supervision.

---

### Robot simulation / task suites

- LIBERO — https://libero-project.github.io/main.html · https://github.com/Lifelong-Robot-Learning/LIBERO
- CALVIN — https://github.com/mees/calvin
- RoboCasa — https://robocasa.ai/ · https://robocasa.ai/leaderboard.html
- ManiSkill — https://github.com/haosulab/ManiSkill

These are future embodied evaluation resources, not current optimization targets.

When simulator state is used for labels/evaluation, keep privileged GT outside the model evidence path unless the experiment explicitly studies an `L4` condition.

---

### Generative / physical world models

#### NVIDIA Cosmos 3

- Project — https://research.nvidia.com/labs/cosmos-lab/cosmos3/
- Technical report — https://arxiv.org/abs/2606.02800
- Code — https://github.com/nvidia/cosmos

#### World Labs Atlas

- Official technical overview — https://www.worldlabs.ai/blog/atlas
- World-model taxonomy — https://www.worldlabs.ai/blog/taxonomy-of-world-models

Atlas is early-access/closed for full reproduction; study through official technical material, published evaluations, demonstrations and any available access.

#### Behavior-grounded / executable physics

- DR-WM / From Pixels to Executable Physics — https://arxiv.org/abs/2610.17630

DR-WM is especially useful for Stage 1 because it explicitly separates geometry available from RGB from contact/friction properties calibrated through real action-response experience.

#### Other world/action model references

- EVEWorld — https://arxiv.org/abs/2610.03374
- ReWAM — https://arxiv.org/abs/2609.38163
- HWAM — https://arxiv.org/abs/2610.12026
- Being-H0.7 — https://arxiv.org/abs/2605.00078
- Being-M0.7 — https://arxiv.org/abs/2610.11283
- H-WM — https://arxiv.org/abs/2602.11291
- Identifiable World Models — https://arxiv.org/abs/2610.07028
- WAM survey — https://arxiv.org/abs/2609.16074
- WAM resource page — https://rcl-robotics.github.io/Awesome-World-Action-Models

---

### Action/world interface and visual calibration

#### SyncWorld

- Paper — https://arxiv.org/abs/2609.09155

Uses visual calibration episodes to specify environment/embodiment-specific action→visual mappings, highlighting that identical numerical actions need not have identical pixel/world meaning.

#### Robot-Factored World Models via Robot Rendering

- Paper — https://arxiv.org/abs/2607.22535

Factors robot action realization and rendered robot geometry away from environment-response prediction. Useful for cross-view/cross-embodiment interface studies.

---

### Closed / partially closed robot-brain and reasoning references

#### Gemini Robotics / Gemini 4 Argon

- Gemini Robotics ER 2 overview — https://deepmind.google/models/gemini-robotics/embodied-reasoning/
- ER 2 model card — https://deepmind.google/models/model-cards/gemini-robotics-er-2/
- Gemini Robotics 2 — https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/
- Gemini 4 Argon for Robotics — https://developers.googleblog.com/gemini-4-argon-for-robotics/
- ERQA open evaluation resource — https://github.com/embodiedreasoning/ERQA

Argon is a general multimodal reasoning/tool-use reference rather than evidence for a vision-only learned robot world model. Its published robotics workflows mix visual input with tools, geometry, simulation and robot-state information.

#### Figure

- Helix 2.5 — https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization

#### Skild

- S1 — https://www.skild.ai/blogs/s1
- General-purpose robot brain — https://skild.ai/blogs/building-the-general-purpose-robotic-brain
- Physical Self-Play — https://skild.ai/blogs/physical-self-play

#### Physical Intelligence

- π0.5 paper — https://arxiv.org/abs/2504.16054
- π0.5 project — https://www.pi.website/blog/pi05

For closed systems, use:

```text
paper / model card
official technical report
API/preview if available
published evaluation protocol
videos/demos
task reconstruction when scientifically useful
```

Do not convert company claims into independently reproduced facts.

---

### Active perception / evidence acquisition

- Vantage / Seek-and-View — https://arxiv.org/abs/2610.11810 · https://github.com/q1xiangchen/Vantage
- Agentic Video Understanding with Gemini — https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/
- Mobility-budget-constrained semantic exploration — https://arxiv.org/abs/2610.17562

Use these to compare learned or agentic evidence selection against explicit uncertainty/information-gain planning. Do not conflate better evidence acquisition with better internal world representation.

---

### Causal representation learning background

- General Identifiability and Achievability for CRL — https://proceedings.mlr.press/v238/varici24a.html
- Multi-node interventional CRL — https://proceedings.mlr.press/v236/bing24a

These are theory resources for understanding when latent causal variables can or cannot be identified from observational/interventional environments.

---

### Apple M4 / local compute

Local platform is Mac mini M4; an engineering resource, not a scientific constraint.

- Specs — https://support.apple.com/en-gb/121555
- Metal — https://developer.apple.com/metal/
- Unified memory API — https://developer.apple.com/documentation/metal/mtldevice/hasunifiedmemory
- Metal Performance Shaders — https://developer.apple.com/documentation/MetalPerformanceShaders
- PyTorch MPS — https://pytorch.org/docs/stable/notes/mps.html
- Core ML — https://developer.apple.com/documentation/coreml

Policy:

```text
science question
→ representation
→ algorithm
→ compute graph
→ CPU/GPU/Metal/Neural Engine mapping
```

Do not alter the science question to fit MPS or avoid external GPU use when a scientifically important baseline requires CUDA.

---

### Reproduction metadata template

When reproduction becomes active, each run should record:

```text
source URL
paper/version date
git commit/checkpoint hash
dataset version/split
licence
V0–V3 observation protocol
L0–L4 learning-evidence provenance
hardware/backend
RAM/VRAM/storage
install command
run command
patches
input/output schema
metrics
known deviations from paper
raw results location
```

The purpose is to make later baseline and Failure Matrix claims independently inspectable.

---

<a id="topic-research-survey-frontier_methods"></a>

## Frontier Methods

Source record updated: 2026-10-14

This document compares method families that materially constrain the Clover research question.

> **How can a machine understand the real world through vision alone, then use that understanding to decide and act?**

The purpose is not to assemble a stack. Each route is treated as a competing explanation of what internal state is sufficient.

For the source/claim/landing map, see [`sources-and-resources.md`](#topic-research-survey-source_map). For the broader synthesis, see [`README.md`](README.md#topic-research-survey-background_research).

---

### 1. Classical geometry and state estimation

**ORB-SLAM3**
Paper: https://arxiv.org/abs/2007.11898
Code: https://github.com/UZ-SLAMLab/ORB_SLAM3

Explicit pose/map/trajectory state demonstrates that some physical-world variables already have strong mathematical formulations. It provides localization, relocalization and map reuse, but not open-world semantics, general object permanence or causal reasoning.

**RAFT**
Paper: https://arxiv.org/abs/2003.12039
Code: https://github.com/princeton-vl/RAFT

Dense temporal correspondence baseline. Flow is valuable motion evidence, but flow is not object identity, persistence or causality.

**Research contradiction:** which variables should remain explicit geometric invariants, and which should be learned?

---

### 2. Static self-supervised visual representation

**DINOv3**
Research: https://ai.meta.com/research/publications/dinov3/
Paper: https://arxiv.org/abs/2508.10104
Code: https://github.com/facebookresearch/dinov3

DINOv3 is now the primary current static SSL comparator. It scales label-free image learning to very large data/model regimes and produces strong frozen dense features for detection, segmentation, depth and tracking-related tasks.

**DINOv2**
Paper: https://arxiv.org/abs/2304.07193
Code: https://github.com/facebookresearch/dinov2

Retained as a historical/currently reproducible predecessor, but no longer the only or strongest static SSL reference in the Survey.

**Research contradiction:** if an image backbone already contains strong dense object/part/depth information, which world-understanding capabilities require persistent temporal state rather than better static representation?

---

### 3. Predictive video representation

**V-JEPA 2**
Research: https://ai.meta.com/research/publications/v-jepa-2-self-supervised-video-models-enable-understanding-prediction-and-planning/
Paper: https://arxiv.org/abs/2506.09985
Code: https://github.com/facebookresearch/vjepa2

Connects internet-scale action-free video learning to motion/anticipation and action-conditioned robot planning. It is a major competitor to an explicitly factorized Clover world state.

**V-JEPA 2.1**
Paper: https://arxiv.org/abs/2603.14482

Dense predictive learning and deep self-supervision produce spatially structured, semantically coherent and temporally consistent features, while also reporting downstream robot improvements.

**Interpreting Physics in Video World Models**
Meta: https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/

Reports that speed, acceleration and motion direction emerge inside large video encoders; direction behaves as a high-dimensional population code. This is direct counter-evidence to assuming all useful physical variables must be compact explicit state.

**Research contradiction:**

```text
explicit factorized state
vs
distributed predictive latent
vs
hybrid/identifiable latent
```

---

### 4. Learned geometry / spatial reconstruction

**DUSt3R** — https://arxiv.org/abs/2312.14132
Learned point-map geometry bridges classical pipelines and foundation models.

**VGGT**
Paper: https://arxiv.org/abs/2503.11651
Code: https://github.com/facebookresearch/vggt

Predicts cameras, depth, point maps and tracks from one or more images.

**VGGT-Ω**
Paper: https://arxiv.org/abs/2605.15195
Project: https://vggt-omega.github.io/
Code: https://github.com/facebookresearch/vggt-omega

Extends learned geometry to larger-scale static/dynamic reconstruction. Its learned registers also improve VLA and language-alignment results, motivating the hypothesis that reconstruction can be a scalable proxy for spatial understanding.

**World Labs Atlas** — https://www.worldlabs.ai/blog/atlas
Atlas combines reconstruction with generation and space-time simulation, but a generated hidden surface is not the same epistemic object as an observed surface.

**Research contradiction:**

```text
reconstruction quality
vs
persistent world state
vs
action-useful state
```

---

### 5. Object-centric representation and visible entity tracking

**Slot Attention** — https://proceedings.neurips.cc/paper/2020/hash/8511df98c02ab60aea1b2356c013bc0f-Abstract.html
Object-like exchangeable slots provide a compositional representation route.

**PLATO** — https://www.nature.com/articles/s41562-022-01394-8
Object-centric inductive structure has shown value for learning intuitive-physics expectations in controlled settings.

**SAM 3 / SAM 3.1**
Research: https://ai.meta.com/research/publications/sam-3-segment-anything-with-concepts/
Code: https://github.com/facebookresearch/sam3
SAM 3.1 notes: https://github.com/facebookresearch/sam3/blob/main/RELEASE_SAM3p1.md

SAM 3.1 is the current open-vocabulary image/video detection, segmentation and tracking baseline in this Survey. It supersedes SAM 2 as the primary contemporary comparator for visible entity persistence, while SAM 2 remains historically important.

**Critical distinction:**

```text
visible tracking ≠ object permanence
```

---

### 6. Persistent visual and episodic memory

**PersistBench**
Paper: https://arxiv.org/abs/2609.20819
Project/code: https://guangzhaohe.com/persistbench

Uses 360° reference video to measure object permanence, motion continuity and appearance preservation after objects leave normal view. Current 4D/world models show strong short-term perception but degraded memory outside the field of view.

**S-EMBER**
Meta: https://ai.meta.com/research/publications/s-ember-a-large-scale-benchmark-for-streaming-egocentric-memory-retrieval/
Paper: https://arxiv.org/abs/2607.02689

Streaming egocentric retrieval benchmark. It separates semantic answering from precise temporal grounding and shows that more model scale/frame density does not automatically solve grounded recall.

**VISTA** — https://arxiv.org/abs/2610.02200
Separates model weights from lossless visual memory, active retrieval and evidence organization, making the memory harness itself an explicit research variable.

**Research contradiction:**

```text
long context / recurrent latent
vs
persistent world state
vs
raw/selective evidence replay
vs
episodic memory
```

Evidence Replay remains one Clover hypothesis, not the default answer.

---

### 7. Intuitive physics and physical consistency

**IntPhys 2**
Research: https://ai.meta.com/research/publications/intphys-2-benchmarking-intuitive-physics-understanding-in-complex-synthetic-environments/
Code: https://github.com/facebookresearch/IntPhys2

Measures permanence, immutability, spatiotemporal continuity and solidity through controlled violation-of-expectation tests.

**MVP / Minimal Video Pairs**
Research: https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/

Tests whether physical-reasoning scores survive minimally changed paired videos with identical questions and opposite answers.

**Principia** — https://arxiv.org/abs/2609.04200
Tests relational Newtonian consistency in real controlled scenes using calibration-independent relationships between objects.

**Interpreting Physics in Video World Models**
https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/

Shows that learned video features can encode physical variables without a compact symbolic state.

**Research contradiction:** visual plausibility, learned physical regularity, quantitative physical state and action-relevant physical knowledge are not the same capability.

---

### 8. Causal and counterfactual reasoning

**CausalVQA**
https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/

Real-video questions probe counterfactual, hypothetical, anticipation and planning reasoning.

**General identifiability and achievability for CRL**
https://proceedings.mlr.press/v238/varici24a.html

**Multi-node interventional CRL**
https://proceedings.mlr.press/v236/bing24a

These causal-representation results are important background because causal variables can be underdetermined from observational data unless additional assumptions or interventional environments provide identifiability.

**Research contradiction:**

```text
predictive correlation
vs
intervention-sensitive dependency
vs
counterfactual world model
```

Historical Counter-Witness First Causality remains a candidate hypothesis to test against these baselines.

---

### 9. Active perception / information-seeking vision

**Bajcsy, Active Perception** — https://ieeexplore.ieee.org/abstract/document/5968
Foundational view that perception includes selecting sensing actions.

**Vantage**
Paper: https://arxiv.org/abs/2610.11810
Code: https://github.com/q1xiangchen/Vantage

View planning + geometry-grounded evidence gathering + VLM reasoning. Shows evidence acquisition can be a bottleneck independent of raw model scale.

**SpatialCORE**
Paper: https://arxiv.org/abs/2609.38716
Code: https://github.com/rafiibnsultan/SpatialCORE

Spatial-grounding confidence can guide learning/compute; confidence is not automatically truth.

**Research contradiction:** can a system represent missing information well enough to decide what visual action should be taken next?

---

### 10. Generative spatial/world models

**World Labs Atlas** — https://www.worldlabs.ai/blog/atlas
**World-model taxonomy** — https://www.worldlabs.ai/blog/taxonomy-of-world-models

Atlas unifies reconstruction, generation and space-time simulation in a spatially grounded multimodal architecture.

**Cosmos 3**
Project: https://research.nvidia.com/labs/cosmos-lab/cosmos3/
Report: https://arxiv.org/abs/2606.02800
Code: https://github.com/nvidia/cosmos

Cosmos 3 jointly handles language, image, video, audio and action and explicitly merges VLM, generator, simulator and world-action roles.

**EVEWorld** — https://arxiv.org/abs/2610.03374
Targets visually plausible but process-inconsistent rollout behavior.

**DR-WM / From Pixels to Executable Physics** — https://arxiv.org/abs/2610.17630
Connects visual geometry with action-response-derived terrain/contact priors.

**Critical distinction:**

```text
plausible completion ≠ observed fact ≠ evidence-supported belief
```

---

### 11. VLA / embodied reasoning / robot foundation systems

**RT-2** — https://arxiv.org/abs/2307.15818
Action-first route transferring web vision/language knowledge into robot actions.

**OpenVLA**
Paper: https://arxiv.org/abs/2406.09246
Code: https://github.com/openvla/openvla

Primary open VLA comparator.

**π0.5**
Paper: https://arxiv.org/abs/2504.16054
Project: https://www.pi.website/blog/pi05

Strong open-world-generalization counterexample to assuming an explicit exposed world state is obviously required.

**Gemini Robotics ER 2**
Overview: https://deepmind.google/models/gemini-robotics/embodied-reasoning/
Model card: https://deepmind.google/models/model-cards/gemini-robotics-er-2/

High-level robot reasoning route built on a large multimodal VLM; motor execution is delegated to a lower-level VLA. Important confound: physical reasoning can mix visual evidence with language/world priors.

**Gemini Robotics 2** — https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/
Whole-body VLA/control reference.

**Figure Helix 2.5** — https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization — `OFFICIAL_REPORTED_RESULT`
Reports whole-body long-horizon zero-shot behavior in 30 unseen homes and a controlled human-experience pretraining ablation.

**Skild S1** — https://www.skild.ai/blogs/s1 — `OFFICIAL_REPORTED_RESULT`
Reports in-context robot task learning from video demonstrations and long-horizon unseen behavior.

**Skild general-purpose robot brain** — https://skild.ai/blogs/building-the-general-purpose-robotic-brain
Embodiment-invariant/omni-bodied foundation-policy thesis.

**Core falsifier for explicit-worldview research:**

```text
strong matched policy
vs
strong matched policy + persistent world representation
```

The world representation must improve action, recovery, generalization, sample efficiency, planning/search cost or unjustified-action rate.

---

### 12. World-action models

**World-Action Models survey**
Paper: https://arxiv.org/abs/2609.16074
Resource page: https://rcl-robotics.github.io/Awesome-World-Action-Models

WAMs couple future world prediction with executable action generation.

**ReWAM** — https://arxiv.org/abs/2609.38163
Reconstruction fidelity and generic perceptual features alone do not guarantee policy-useful state.

**HWAM** — https://arxiv.org/abs/2610.12026
Reference action, executed motion and realized state must be distinguished.

**Being-H0.7** — https://arxiv.org/abs/2605.00078
Future-aware latent reasoning without future-pixel rollout at inference.

**Being-M0.7** — https://arxiv.org/abs/2610.11283
Large human video/motion pretraining before humanoid adaptation.

**H-WM** — https://arxiv.org/abs/2602.11291
Combines high-level logical transitions with low-level visual transitions.

**Research contradiction:** which future information is sufficient for control: pixels, geometry, latent state, explicit task state or some hybrid?

---

### 13. Identifiable / hybrid state

**Identifiable World Models** — https://arxiv.org/abs/2610.07028

Promising middle route: retain powerful distributed representation while learning coordinates that align with identifiable world variables.

This is important because the strongest answer may not be “explicit or latent,” but a layered or partially identifiable representation.

---

### 14. Model-based control

**DreamerV3** — https://arxiv.org/abs/2301.04104
**TD-MPC2** — https://arxiv.org/abs/2310.16828

Important counterexamples to the belief that useful planning state must be human-interpretable.

---

### 15. State/action-grounded world-model evaluation

**RoboPhys-3D** — https://arxiv.org/abs/2608.28718

Evaluates world-model outputs through pixel fidelity, 3D geometry, state-level understanding and task-level completeness. It is especially relevant because state/execution-grounded metrics expose failures that perceptual or generic VLM judgments may miss.

---

### 16. Sparse / event-like computation

**Motion-aware Event Suppression** — https://arxiv.org/abs/2602.23204

Shows that sparse visual change can reduce downstream compute. The Clover lesson is to test sparse visual evidence as a representation/computation hypothesis without making event-camera hardware a scientific requirement.

---

### Provisional constraints from the frontier

Current evidence supports constraints, not a final architecture:

1. scalable open-world abstraction strongly benefits from learned representation;
2. explicit geometry remains valuable where variables and invariants are well-defined;
3. static SSL is stronger than older Clover baselines assumed — DINOv3 is now a key comparator;
4. predictive video representations learn substantial distributed physical structure;
5. reconstruction gives strong spatial state but does not automatically provide persistence, causality or action utility;
6. visible segmentation/tracking is not object permanence;
7. streaming/persistent memory is an independent capability, not simply “more context”;
8. plausible generation is not authoritative truth;
9. strong policies can act without exposed explicit state;
10. interaction adds controllability and interventional evidence;
11. active perception can create evidence unavailable in the current view;
12. physical variables can be distributed rather than compactly factorized;
13. control-oriented future prediction is increasingly moving toward task-relevant latent/state prediction rather than full pixel rollout;
14. state/process consistency and execution consequences matter more than video quality alone;
15. any explicit Clover worldview must prove measurable value for action, recovery, generalization or efficiency.

The next Clover architecture must be derived from baseline + battery + failure-map evidence, not attachment to an older mechanism.

---

<a id="topic-research-literature-primary-sources"></a>

## Primary Source Index

Source record updated: 2026-10-14

This index collects primary papers, official project pages and official code used by the Research Map and Research Questions. Company-only results are marked as official reported results, not independent reproductions.

### Historical representation-learning transition

- SIFT — paper/DOI: https://doi.org/10.1023/B:VISI.0000029664.99615.94
- SIFT — author-hosted PDF: https://www-inst.eecs.berkeley.edu/~ee225b/sp11/readings/sift-lowe.pdf
- HOG — paper/DOI: https://doi.org/10.1109/CVPR.2005.177
- AlexNet — NeurIPS page: https://proceedings.neurips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html
- AlexNet — PDF: https://papers.nips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf
- ResNet: https://arxiv.org/abs/1512.03385
- Vision Transformer: https://arxiv.org/abs/2010.11929
- CLIP: https://arxiv.org/abs/2103.00020

### Classical / geometry

- ORB-SLAM3 — paper: https://arxiv.org/abs/2007.11898
- ORB-SLAM3 — code: https://github.com/UZ-SLAMLab/ORB_SLAM3
- DUSt3R — paper: https://arxiv.org/abs/2312.14132
- VGGT — paper: https://arxiv.org/abs/2503.11651
- VGGT — CVPR page: https://openaccess.thecvf.com/content/CVPR2025/html/Wang_VGGT_Visual_Geometry_Grounded_Transformer_CVPR_2025_paper.html
- VGGT — code: https://github.com/facebookresearch/vggt
- VGGT-Ω — paper: https://arxiv.org/abs/2605.15195
- VGGT-Ω — project: https://vggt-omega.github.io/
- VGGT-Ω — code: https://github.com/facebookresearch/vggt-omega

### Visual / video representation

- DINOv2 — paper: https://arxiv.org/abs/2304.07193
- V-JEPA 2 — paper: https://arxiv.org/abs/2506.09985
- V-JEPA 2 — Meta page: https://ai.meta.com/research/publications/v-jepa-2-self-supervised-video-models-enable-understanding-prediction-and-planning/
- V-JEPA 2 / 2.1 — code: https://github.com/facebookresearch/vjepa2
- V-JEPA 2.1 — paper: https://arxiv.org/abs/2603.14482
- Slot Attention — paper: https://arxiv.org/abs/2006.15055
- SAM 2 — paper: https://arxiv.org/abs/2408.00714
- Meta — Interpreting Physics in Video World Models: https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/

### Generative / predictive / control world models

- NeRF — paper: https://arxiv.org/abs/2003.08934
- DreamerV3 — paper: https://arxiv.org/abs/2301.04104
- TD-MPC2 — paper: https://arxiv.org/abs/2310.16828
- World Labs Atlas — official report: https://www.worldlabs.ai/blog/atlas
- Cosmos 3 — paper: https://arxiv.org/abs/2606.02800
- Cosmos 3 — project: https://research.nvidia.com/labs/cosmos-lab/cosmos3
- Cosmos — code: https://github.com/nvidia/cosmos
- RBench / RoVid-X — paper: https://arxiv.org/abs/2601.15282
- ABot-PhysWorld — paper: https://arxiv.org/abs/2603.23376
- Xiaomi-Robotics-U0 — paper: https://arxiv.org/abs/2607.11643
- Xiaomi-Robotics-U0 — project/code: https://robotics.xiaomi.com/xiaomi-robotics-u0.html

### Embodied reasoning / VLA / robot foundation models

- RT-2 — paper: https://arxiv.org/abs/2307.15818
- RT-2 — PMLR: https://proceedings.mlr.press/v229/zitkovich23a.html
- OpenVLA — paper: https://arxiv.org/abs/2406.09246
- OpenVLA — code: https://github.com/openvla/openvla
- π0.5 — paper: https://arxiv.org/abs/2504.16054
- π0.5 — official project: https://www.pi.website/blog/pi05
- Gemini Robotics ER 2 — model card: https://deepmind.google/models/model-cards/gemini-robotics-er-2/
- Gemini Robotics On-Device 2 — model card: https://deepmind.google/models/model-cards/gemini-robotics-on-device-2/
- Hy-Embodied-VLM-1.0 — paper: https://arxiv.org/abs/2607.12894
- Figure Helix 2.5 — official reported result: https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization
- Skild S1 — official reported result: https://www.skild.ai/blogs/s1
- Skild Physical Self-Play — official report: https://skild.ai/blogs/physical-self-play

### Physical / causal evaluation

- IntPhys 2 — official page: https://ai.meta.com/research/publications/intphys-2-benchmarking-intuitive-physics-understanding-in-complex-synthetic-environments/
- MVPBench — official page: https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/
- CausalVQA — official page: https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/
- RoboPhys-3D — paper: https://arxiv.org/abs/2608.28718

### Surveys / landscape references

- A Comprehensive Survey on World Models for Embodied AI: https://arxiv.org/abs/2510.16732
- Aligning Perception, Reasoning, Modeling and Interaction: A Survey on Physical AI: https://arxiv.org/abs/2510.04978

---

<a id="topic-research-literature-model-index"></a>

## Clover Model & Literature Index

Last verified: 2026-10-14

This is a navigation index, not a ranking. Closed-system results are marked as vendor-reported when appropriate.

| Work | Area | Main contribution relevant to Clover | Public artifact | Evidence note |
|---|---|---|---|---|
| ORB-SLAM3 | classical geometry | persistent visual geometry / relocalization / maps | https://github.com/UZ-SLAMLab/ORB_SLAM3 | open code |
| RAFT | motion | learned optical flow estimator | https://github.com/princeton-vl/RAFT | open code |
| DINOv2 | image SSL | robust generic visual features | https://github.com/facebookresearch/dinov2 | open code/models |
| Slot Attention | object-centric | exchangeable object slots | https://arxiv.org/abs/2006.15055 | paper; ecosystem implementations |
| SAM 2 | video entities | segmentation with streaming memory | https://ai.meta.com/research/sam2/ | open code/models |
| V-JEPA 2 | video world model | action-free video SSL; prediction/planning bridge | https://github.com/facebookresearch/vjepa2 | open code/models |
| V-JEPA 2.1 | dense video SSL | temporally consistent dense features | https://github.com/facebookresearch/vjepa2 | open code/models |
| Interpreting Physics in Video World Models | interpretability | probes distributed physical variables | https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/ | primary paper |
| VGGT | spatial intelligence | feed-forward camera/depth/point-map/track inference | https://github.com/facebookresearch/vggt | open code/models |
| VGGT-Ω | spatial intelligence | scalable static/dynamic reconstruction | https://github.com/facebookresearch/vggt-omega | training/repro materials public |
| DUSt3R | learned geometry | point-map multi-view reconstruction | https://arxiv.org/abs/2312.14132 | paper/code ecosystem |
| Atlas | general world model | reconstruction + generation + simulation | https://www.worldlabs.ai/blog/atlas | vendor technical release |
| Cosmos 3 | physical AI | reasoning + generation + action in one open model family | https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-3-the-open-frontier-foundation-model-for-physical-ai/ | NVIDIA-reported/open ecosystem |
| RT-2 | VLA | web VLM knowledge to action | https://deepmind.google/blog/rt-2-new-model-translates-vision-and-language-into-action/ | paper/project |
| OpenVLA | VLA | open-source VLA baseline | https://github.com/openvla/openvla | open code/models |
| π0.5 | VLA | open-world home generalization through heterogeneous co-training | https://www.pi.website/blog/pi05 | paper + vendor experiments |
| Gemini Robotics ER 2 | embodied reasoning | high-level physical reasoning/planning brain | https://deepmind.google/models/gemini-robotics/embodied-reasoning/ | official model card/product access |
| Gemini Robotics 2 | VLA | lower-level robot action model | https://deepmind.google/models/gemini-robotics/ | official system |
| Helix 2.5 | robot foundation model | reported zero-shot 30-home whole-body generalization | https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization | vendor-reported real robot study |
| Skild S1 | robot foundation model | in-context learning from video demonstrations | https://www.skild.ai/blogs/s1 | vendor technical report |
| Open X-Embodiment | robot data | cross-embodiment dataset and transfer | https://github.com/google-deepmind/open_x_embodiment | open data tooling/models |
| LIBERO | lifelong robotics | knowledge transfer over task sequences | https://libero-project.github.io/main.html | open benchmark |
| CALVIN | long-horizon control | language-conditioned multi-step manipulation | https://github.com/mees/calvin | open benchmark |
| Perception Test | video benchmark | tracking, memory, physics, semantics | https://github.com/google-deepmind/perception_test | open benchmark |

### Reading priority now

The current project phase is **research before reproduction**. Read for the representation and learning assumptions first; implementation comparison comes later.

#### Tier A — central to the world-representation question

1. V-JEPA 2 / 2.1
2. VGGT / VGGT-Ω
3. classical multi-view geometry / SLAM
4. object-centric representation
5. mechanistic interpretation of video models

#### Tier B — central to the robot-brain/product question

1. Gemini Robotics ER 2
2. π0.5
3. Helix 2.5
4. Skild S1
5. OpenVLA

#### Tier C — evaluation and long-term learning

1. IntPhys 2 / MVPBench / CausalVQA
2. Perception Test
3. LIBERO / CALVIN / RoboCasa
4. Ego4D / DROID / Open X-Embodiment

---

<a id="topic-research-literature-datasets-and-benchmarks"></a>

## Datasets, Benchmarks and Task Environments

Last verified: 2026-10-14

This file is a research-resource index. Dataset size and task counts are recorded from official project sources when available.

| Resource | Type | Relevant scale / scope | Why Clover cares | Primary source |
|---|---|---|---|---|
| IntPhys 2 | synthetic physics benchmark | permanence, immutability, continuity, solidity | controlled intuitive-physics diagnostic | https://ai.meta.com/research/publications/intphys-2-benchmarking-intuitive-physics-understanding-in-complex-synthetic-environments/ |
| MVPBench | physical video QA | 55K examples, minimal-pair design | shortcut-resistant physical reasoning | https://ai.meta.com/research/publications/a-shortcut-aware-video-qa-benchmark-for-physical-understanding-via-minimal-video-pairs/ |
| CausalVQA | real-video causal QA | five causal/reasoning question families | counterfactual/anticipation diagnostic | https://ai.meta.com/research/publications/causalvqa-a-physically-grounded-causal-reasoning-benchmark-for-video-models/ |
| Perception Test | multimodal video benchmark | QA, object/point tracking, action/sound localization | memory/physics/tracking diagnostic | https://github.com/google-deepmind/perception_test |
| Ego4D | egocentric video | ~3,600+ hours daily-life video | long visual history, memory, object interaction, forecasting | https://ego4d-data.org/docs/ |
| DROID | robot interaction dataset | 76K trajectories / 350h / 564 scenes / 86 tasks | passive-video vs action-conditioned learning | https://droid-dataset.github.io/ |
| Open X-Embodiment | cross-robot dataset | 22 embodiments; >1M episodes reported | cross-embodiment abstraction and transfer | https://github.com/google-deepmind/open_x_embodiment |
| LIBERO | lifelong robot benchmark | multiple suites/tasks | knowledge transfer and continual learning | https://libero-project.github.io/main.html |
| CALVIN | simulated robot benchmark | long-horizon language-conditioned manipulation | downstream long-horizon planning/control | https://github.com/mees/calvin |
| RoboCasa365 | generalist robot simulation/benchmark | 365 tasks; 2,500+ kitchen scenes; 2,200+ hours demos reported | compositional generalization and long-horizon manipulation | https://robocasa.ai/ |

### Dataset-role discipline

Different data sources provide different evidence:

#### Passive internet / human video

Good for visual diversity and natural physical regularities. Lacks direct knowledge of the observer's intervention/action variables.

#### Egocentric human video

Closer to embodied visual experience and object interaction, but embodiment/action labels may not transfer directly to robots.

#### Robot demonstrations

Provides actions and consequences, but is expensive and usually narrower in environment diversity.

#### Simulation

Provides exact state/interventions and cheap scale, but creates a reality gap.

#### Closed real-robot evaluations

Provide strong capability evidence, but may lack reproducibility and inspectability.

Clover should eventually exploit these roles deliberately rather than treating all video/robot data as interchangeable.

---

<a id="topic-research-research_frontier"></a>

## Research Frontier Watch

Source record updated: **2026-10-19**
Source intake checked through: **2026-10-19**

> **Research question:** How can a machine understand the real world through vision alone?

This file is a **thin current-edge index**. It is not a second survey and it does not make Clover design decisions.

As of 2026-10-15, the latest complete arXiv daily batches visible for the relevant categories include work submitted through **2026-10-13 UTC**, with some records revised on 2026-10-14. The 2026-10-16 → 2026-10-19 extension is recorded in [`sources-and-resources.md`](#topic-research-emerging-frontier_sweep_2026-10-19); its verified additions are: Preserve both submission/revision dates and the date Clover checked the source.

Stable concepts belong in the Stage-1 topic files. Fast-moving cross-boundary clusters are also summarized in [`foundation-models-and-systems.md`](foundation-models-and-systems.md#topic-research-emerging-jepa_rsi_runtime_2026-10-15).

### Evidence labels

- `PRIMARY_PAPER`
- `OFFICIAL_PROJECT`
- `OPEN_SOURCE`
- `OFFICIAL_REPORTED_RESULT`
- `OPEN_SOURCE_PROJECT / ENGINEERING_REFERENCE`

---

### 1. Current frontier snapshot

| Date | Source | Evidence | Why it matters now | Does **not** prove | Stage-1 landing |
|---|---|---|---|---|---|
| 2026-10-15 / listed 10-16 | VLA-Δ — https://arxiv.org/abs/2610.21306 · code https://github.com/ZJU-OmniAI/VLA-Delta | `PRIMARY_PAPER` / `OPEN_SOURCE` | physical state-transition (Δ) supervision improves VLA policies at zero added inference cost; reported above π0.5 in real-robot experiments | a Δ training target is a sufficient world state, or transfers without its pretraining mixture | state-transition supervision · sufficient state · post-training |
| 2026-10-16 | HIJP (Hindsight Inverse JEPA Planning) — https://arxiv.org/abs/2610.23615 | `PRIMARY_PAPER` | search-free latent planning via goal-conditioned inverse model; hindsight relabeling shapes the visual representation; 1.9–16.5× planning speedup reported | latent inverse planning preserves epistemic/uncertainty state | JEPA planning · runtime · sufficient state |
| 2026-06-30 / resurfaced 10-19 | AdaJEPA — https://arxiv.org/abs/2606.32026 · https://agenticlearning.ai/adajepa/ | `PRIMARY_PAPER` / `OFFICIAL_PROJECT` | deployment-time adaptation of a latent world model inside the MPC loop from executed transitions; breaks the frozen-at-deployment default | online adaptation is safe/monotonic, or preserves calibration and memory | deployment learning · model invalidation · belief revision |
| 2026-10-14 / demo 10-20→22 | NEURA Neuron AI (PLA) — https://neura-robotics.com/neura-robotics-introduces-neuron-ai/ | `OFFICIAL_REPORTED_RESULT` | vendor robotic brain (vision+touch+sound+proprioception+memory, on-robot inference) with an 11-min unattended laundry demo at GTC Berlin as its public test | any benchmark capability: no success rates or Time-to-Skill figures published; not a vision-alone result | robotic-brain competitor watch · memory claims · EV ladder |
| 2026-10-17→19 | OpenAI humanoid program (Altman statements) — https://www.timesnownews.com/technology-science/openai-is-building-its-own-humanoid-robot-ceo-sam-altman-confirms-article-156365247 | `SURVEY_SIGNAL` (secondary press report; not a verified official source) | press-reported humanoid-program plans and statements; no official technical evidence registered here | any capability: no model/data/benchmark disclosed | industry structure · robotic-brain race |
| 2026-10-13 / rev. 10-14 | Thinker-WM — https://arxiv.org/abs/2610.18447 · project https://thinkercosmos.ubtrobot.com | `PRIMARY_PAPER` / `OFFICIAL_PROJECT` | jointly evolves RGB, metric depth and robot action in a shared dynamics representation; exposes a strong unified-multimodal-state counter-hypothesis | depth/action-supervised training is vision-only, or one shared state is universally sufficient | representation · geometry · WAM · provenance |
| 2026-10-13 | AReaL-RSI — https://arxiv.org/abs/2610.18083 | `PRIMARY_PAPER` | makes recursive improvement a resource-allocation / role-specialization / evidence-sharing problem across persistent research campaigns | more agents automatically yield better or safer self-improvement | foundation-model systems · research automation · RSI evaluation |
| 2026-10-13 | WorldOracle — https://arxiv.org/abs/2610.18826 | `PRIMARY_PAPER` | evaluates action-conditioned world models against paired real executions from the same initial observation and low-level action sequence | world-model score implies good policy or complete physical understanding | world-model evaluation · real-execution grounding |
| 2026-10-13 | RoboSimStudio — https://arxiv.org/abs/2610.18835 · project https://robosimstudio.github.io | `PRIMARY_PAPER` / `OFFICIAL_PROJECT` | makes solver/contact/physical-parameter choices explicit for iterative Real2Sim and Real2Sim2Real | calibrated simulation is uniquely correct | engineering validation · Real2Sim · model discovery |
| 2026-10-13 | LIBERO-RIG — https://arxiv.org/abs/2610.18843 | `PRIMARY_PAPER` | holds tasks fixed while perturbing hardware/setup axes; separates task generalization from rig robustness | simulated perturbations fully predict target-robot reliability | hardware robustness · fault injection |
| 2026-10-13 | LoopWAM — https://arxiv.org/abs/2610.18873 · project https://loop-wam.github.io | `PRIMARY_PAPER` / `OFFICIAL_PROJECT` | learns from successful, suboptimal and failed deployment rollouts across repeated deployment/training rounds | self-improvement is safe or monotonic | deployment learning · WAM · lifecycle |
| 2026-10-13 | ForceWAM — https://arxiv.org/abs/2610.18852 · project https://force-wam.github.io | `PRIMARY_PAPER` / `OFFICIAL_PROJECT` | combines future visual prediction with local six-axis wrench/contact-response learning | contact forces are identifiable from RGB alone | contact physics · WAM · provenance |
| 2026-10-13 | RoboFQE — https://arxiv.org/abs/2610.18699 | `PRIMARY_PAPER` | enables offline visual-policy ranking without new simulator/real rollouts | offline evaluation replaces closed-loop testing | EV4 · offline policy evaluation |
| 2026-10-13 | Grid or Nodes? — https://arxiv.org/abs/2610.18637 | `PRIMARY_PAPER` | exposes representation/memory-cost/OOD-motion trade-offs under partial observability | oracle node tracking is a deployable general solution | persistent memory · edge state cost |
| 2026-10-13 | LADDER — https://arxiv.org/abs/2610.18053 · project https://ladder.insait.ai | `PRIMARY_PAPER` / `OFFICIAL_PROJECT` | controlled horizon scaling exposes compounding physical-execution failures | orchestration alone solves long-horizon robotics | long-horizon evaluation · systems integration |
| 2026-10-13 | GreenWAM — https://arxiv.org/abs/2610.18774 · project https://greenvla.github.io | `PRIMARY_PAPER` / `OFFICIAL_PROJECT` | unifies world/policy roles and distills to a real-time policy | distillation preserves every world-model capability | WAM · cross-embodiment · edge distillation |
| 2026-10-13 | DR-WM / From Pixels to Executable Physics — https://arxiv.org/abs/2610.17630 | `PRIMARY_PAPER` | separates RGB geometry from contact/friction properties calibrated by action-response | passive RGB identifies friction/contact generally | physical properties · identifiability |
| 2026-10-13 | Gemini 4 Argon for Robotics — https://developers.googleblog.com/gemini-4-argon-for-robotics/ | `OFFICIAL_REPORTED_RESULT` | strong general multimodal reasoner/tool-user spanning physical reasoning, Real2Sim and robot workflows | vision-only learning or persistent world state is sufficient/necessary | general-reasoner counter-hypothesis |
| 2026-10-12 | MARS — https://arxiv.org/abs/2610.17141 · code https://github.com/PKU-VaLuE-Lab/MARS | `PRIMARY_PAPER` / `OPEN_SOURCE` | training-free WAM acceleration across attention, denoising and cross-query representation reuse with online verification | cached/reused inference state is always valid | runtime systems · WAM acceleration · state staleness |
| 2026-10-12 | Artisan — https://arxiv.org/abs/2610.13947 | `PRIMARY_PAPER` | evaluates articulation, collision, gravity stability, mass/material and function, not only appearance | passive RGB recovers physical parameters | physical properties · functional correctness |
| 2026-10-11 | Δ Flow Matching — https://arxiv.org/abs/2610.15794 | `PRIMARY_PAPER` | replaces fixed Gaussian source with recent-history-conditioned source for VLA/WAM flow matching; makes generative source distribution a training/inference variable | one source prior is universally optimal | training/post-training · runtime efficiency |
| 2026-10-11 | Vision-Predictor-Action — https://arxiv.org/abs/2610.15556 · code https://github.com/ylee-sling/Vision-Predictor-Action | `PRIMARY_PAPER` / `OPEN_SOURCE` | lightweight JEPA predictor + flow action chunk; preliminary Apple-M4 latency evidence makes it relevant to local proxy research | preliminary LIBERO result establishes general embodied intelligence | embodied JEPA · edge proxy |
| 2026-10-11 | SpecWM — https://arxiv.org/abs/2610.15429 | `PRIMARY_PAPER` | explicitly controls what latent representations preserve; kernel choice changes recoverable physical variables/planning | one kernel is universally sufficient | sufficient state · aliasing |
| 2026-10-10 | Harmony Harness — https://arxiv.org/abs/2610.15150 | `PRIMARY_PAPER` | multi-objective harness evolution separates reusable mechanisms from benchmark-specific adaptation | self-evolving harnesses generalize automatically | harness RSI · foundation systems |
| 2026-10-09 | Harness² — https://arxiv.org/abs/2610.14224 | `PRIMARY_PAPER` | studies recursive harness refinement in open-world tasks without ground-truth online verifiers and transfers task-level experience to future harnessing | self-generated evaluation is reliable by default | open-world RSI · evaluator quality |
| 2026-10-08 | Embodied Turing Machines / COAP — https://arxiv.org/abs/2610.12369 | `PRIMARY_PAPER` | strong counter-hypothesis: explicit state + reusable code policy, recursively improved by coding agents, can remove a large model from the runtime loop | code/state dominates VLA/WAM generally or state estimation is solved | explicit state · embodied RSI · systems counter-hypothesis |
| 2026-10-08 | Mental-Models for Multi-Agent Systems — https://arxiv.org/abs/2610.12453 · code https://github.com/hananshafi/Mental-Models | `PRIMARY_PAPER` / `OPEN_SOURCE` | explicit first/second-order partner-state representations improve multi-agent reasoning | mental state is directly visually identifiable | social hidden state |
| 2026-10-08 | HWAM — https://arxiv.org/abs/2610.12026 | `PRIMARY_PAPER` | predicts realized post-execution body state, exposing commanded-action vs realized-state gap | explicit state is universally superior | embodiment · WAM |
| 2026-10-08 | Being-M0.7 — https://arxiv.org/abs/2610.11283 | `PRIMARY_PAPER` | latent visual-motion prior from mixed human data transferred through robot mid-training/action post-training | latent future state is open-world sufficient | humanoid WAM · training provenance |
| 2026-10-07 | RoboJEPA — https://arxiv.org/abs/2610.10515 · code https://github.com/facebookresearch/robo_jepa | `PRIMARY_PAPER` / `OPEN_SOURCE` | 22M→8B action-conditioned latent predictors over frozen V-JEPA 2.1; 12 embodiments; scaling law plus latent MPC/CEM and real Franka deployment | JEPA latents contain every physical variable or scaling eliminates aliasing | embodied JEPA · scaling · latent planning |
| 2026-10-07 | LAC-WM — https://arxiv.org/abs/2610.10846 · project https://lacwm.github.io | `PRIMARY_PAPER` / `OFFICIAL_PROJECT` | unified learned latent action space improves evaluated cross-embodiment world-model adaptation compared with explicit action labels | one latent action space is universally physically sufficient | cross-embodiment action semantics |
| 2026-10-07 | RSI-Forge — https://arxiv.org/abs/2610.09426 | `PRIMARY_PAPER` | builds executable RSI environments from papers; human experts expose shortcut/faithfulness weaknesses missed by agent judges | automated evaluation is self-validating | RSI environments · evaluator design |
| 2026-10-07 | RSIGym — https://arxiv.org/abs/2610.10310 | `PRIMARY_PAPER` | exposes training/inference/rollout/eval services and separates Data, Harness and Joint improvement tracks | one RSI score proves broad self-improvement | RSI infrastructure · research automation |
| 2026-10-07 | RLHND — https://arxiv.org/abs/2610.09455 | `PRIMARY_PAPER` | repurposes a video diffusion foundation backbone as a clip-level perception representation for hand/contact learning | force/contact was learned from RGB alone | computer vision · generative-backbone-as-perception |
| 2026-10-07 | RobotWorld — https://arxiv.org/abs/2610.10409 | `PRIMARY_PAPER` | exposes composition, task-state retention, recovery and completion-verification failures | one missing component explains system failure | systems integration · persistent state |
| 2026-10-04 | DiVeR — https://arxiv.org/abs/2610.04933 | `PRIMARY_PAPER` | verifier-guided Best-of-N action selection shows deployed VLA performance depends on inference-time candidate/search budget as well as weights | verifier scaling changes the underlying policy representation | test-time VLA scaling · verifier attribution |
| 2026-10-04 | Identifiable World Models — https://arxiv.org/abs/2610.07028 | `PRIMARY_PAPER` | hybrid route: distributed representation + identifiable dynamical coordinates | assumptions hold for arbitrary real video | identifiability · representation |
| 2026-10-03 | Video2World — https://arxiv.org/abs/2610.04432 | `PRIMARY_PAPER` | separates geometric/dynamic/functional correctness from visual similarity | simulator reconstruction equals internal understanding | functional equivalence |
| 2026-10-02 | EVEWorld — https://arxiv.org/abs/2610.03374 | `PRIMARY_PAPER` | process-level instance/evolution supervision targets visually plausible but temporally/physically lazy world predictions | its metric captures all physical errors | physical-process supervision · evaluation |
| 2026-09-30 | EmbodiRSI — https://arxiv.org/abs/2609.38905 | `PRIMARY_PAPER` | real→task-specific-sim→failure-guided data acquisition→policy update→real refinement makes embodied recursive adaptation concrete | embodied RSI is safe, monotonic or universally data-efficient | Real2Sim2Real · post-training · deployment learning |
| 2026-09-28 | RSI-Master — https://arxiv.org/abs/2609.35561 | `PRIMARY_PAPER` | Experiment OS + Worker/Reviewer research DAG targets hacking and strategy lock-in in autonomous post-training R&D | autonomous research is trustworthy without external evaluation | research-agent RSI · experiment provenance |
| 2026-09-28 | WAMachine — https://arxiv.org/abs/2609.34608 | `PRIMARY_PAPER` | adapts retained inference state across replans, denoising and layers; makes stale-computation detection part of real-time WAMs | reuse is harmless under arbitrary distribution shift | WAM runtime · state validity |
| 2026-09-23 | RegenHarness — https://arxiv.org/abs/2609.27612 | `PRIMARY_PAPER` | embodied harness with proposal/execution/verification/commit/recovery separation and versioned evidence-gated updates | one harness revision proves recursive long-term improvement | embodied harness RSI · safety boundary |
| 2026-09-22 | AIDE² / Recursive self-improvement of AI research agents — https://arxiv.org/abs/2609.26457 | `PRIMARY_PAPER` | accepted code rewrites become the next research agent; hidden held-out evaluation and lineage make RSI claims more rigorous | gains guarantee indefinite or safe recursive improvement | research-agent RSI · hidden evaluation |
| 2026-09-21 | RRSI — https://arxiv.org/abs/2609.24972 · code https://github.com/google-research/rrsi | `PRIMARY_PAPER` / `OPEN_SOURCE` | regularizes harness evolution to reduce evolve-set overfitting and considers OOD benchmarks/token cost | harness evolution improves model weights or physical intelligence | harness RSI · generalization |
| 2026-09 | PointCast — https://arxiv.org/abs/2609.28393 | `PRIMARY_PAPER` | identity-bearing point state spans rigid, articulated, cloth and rope regimes | one representation solves cross-material physics | deformables · world state |
| 2026-09 | WROP — https://arxiv.org/abs/2609.28654 | `PRIMARY_PAPER` | trains object permanence/solidity priors | synthetic cognitive curriculum guarantees real-world permanence | persistence · memory |
| 2026-09 | WorldContact — https://arxiv.org/abs/2609.19600 | `PRIMARY_PAPER` | contact-centric dynamics for deformable manipulation | RGB uniquely identifies material/contact parameters | contact · deformables |
| 2026-09 | PersistBench — https://arxiv.org/abs/2609.20819 | `PRIMARY_PAPER` | distinguishes visibility from persistence outside FOV | persistence alone yields general understanding | memory · belief |
| 2026-08 | Unknown Unknowns: Model Misspecification in ML for Physics — https://arxiv.org/abs/2608.13633 | `PRIMARY_PAPER` | makes model-class misspecification a first-class scientific issue | one uncertainty score certifies model correctness | open-world epistemics |
| 2026-07 | HUME — https://arxiv.org/abs/2607.06501 · code https://github.com/threefruits/HUME | `PRIMARY_PAPER` / `OPEN_SOURCE` | hypothesis generation, verification, rejection and model expansion in open-world robot planning | language-generated symbolic ontology is ground truth | model discovery |
| 2026-06 | Learning Task-Sufficient World Models — https://proceedings.mlr.press/v306/feng26aa.html | `PRIMARY_PAPER` | closes active probing ↔ latent-factor discovery ↔ task-sufficient state loop | task-sufficient means open-world sufficient | sufficient state · value of information |
| 2026-05 | What-If World — https://arxiv.org/abs/2605.27589 | `PRIMARY_PAPER` | paired interventions test causal future differences | generated counterfactual correctness implies executable model | intervention evaluation |
| 2026-04 | RoboWM-Bench — https://arxiv.org/abs/2604.19092 | `PRIMARY_PAPER` | plausible generated video can still fail embodied execution | realism equals executable physics | world-model evaluation |
| current open baseline | GR00T N1.7 — https://github.com/NVIDIA/Isaac-GR00T | `OPEN_SOURCE` | strong reproducible direct-policy/VLA comparator | direct policy eliminates need to study world state | baseline comparator |

---

### 2. Open-source / engineering project watch

These projects are useful but should not be promoted to primary scientific evidence without a corresponding primary result.

| Project | Evidence | Useful role | Critical boundary |
|---|---|---|---|
| EmbodiedJev / 行知 — https://github.com/FBddcz/embodied-jev | `OPEN_SOURCE_PROJECT / ENGINEERING_REFERENCE` | MuJoCo + Franka local workbench, structured/RGB inputs, model comparison, trajectory replay/export, pre-execution checks, macOS/Linux workflow | controller-provided candidates/geometry/safety are not model-learned capability; sim success is not real-robot success |
| AgentRSI — https://github.com/heng526/AgentRSI | `COMMUNITY_RESEARCH_REPOSITORY` | literature/reproduction workspace and append-only ResearchOps records for RSI research | repository organization is not proof of a specific RSI scientific result |

---

### 3. What changed in the comparison space

The current sweep adds these distinctions:

```text
predictive latent world model
≠
pixel-generative world model

JEPA imagination error
≠
complete world-state quality

cross-embodiment state alignment
≠
cross-embodiment action alignment

base VLA
≠
VLA + verifier + Best-of-N test-time compute

inference-state reuse
≠
inference-state validity

fast loop + slow loop
requires
temporal synchronization / stale-guidance semantics

self-evolution
≠
self-improvement

model-weight RSI
≠
harness RSI
≠
data/research-process RSI
≠
embodied deployment RSI

RSI evolve-set gain
≠
held-out/OOD gain

final endpoint score
≠
process-level self-improvement quality

generative video model
≠
only a generator;
it can also provide perception features

multi-camera token concatenation
≠
3D-consistent multi-view representation

explicit state + code policy
≠
learned foundation-model policy
```

Older core distinctions remain active:

```text
pixels ≠ world state
visual plausibility ≠ physical correctness ≠ functional correctness ≠ executability
statistical predictability ≠ physical identifiability
state uncertainty ≠ parameter uncertainty ≠ model-structure uncertainty ≠ hypothesis-set incompleteness
maximum information gain ≠ best probe under misspecification / risk / cost / irreversibility
compact task-sufficient state ≠ open-world sufficient state
world model for belief ≠ world simulator ≠ world data engine
scene/task generalization ≠ hardware/calibration/control-loop robustness
model accuracy ≠ runtime reliability
```

---

### 4. Immediate Stage-2 analysis queue

Prioritize methods that discriminate different hypotheses, not simply the newest names:

```text
RoboJEPA / ThinkJEPA / LeapBot-WA / Demo-JEPA / V-JEPA 2.1
LAC-WM vs explicit action-conditioned world models
DiVeR vs base-policy inference
MARS / WAMachine / Δ-flow / asynchronous WAM execution
AIDE² / RRSI / RSI-Master / RSI-Forge / RSIGym / HELIX / Harmony Harness / Harness² / AReaL-RSI
EmbodiRSI / RegenHarness / Embodied Turing Machines
Thinker-WM / PAIWorld / RLHND / EVEWorld
WorldOracle
RoboSimStudio
LIBERO-RIG
RoboFQE
LADDER
LoopWAM
ForceWAM
GreenWAM
SpecWM
Learning Task-Sufficient World Models
Identifiable World Models
HUME
DR-WM
PersistBench + WROP
PointCast
Riemann-1.0
Being-M0.7 vs HWAM
Gemini 4 Argon vs explicit/persistent-state systems
GR00T N1.7 / OpenVLA / π0.5
Video2World + RoboWM-Bench
What-If World / causal-intervention benchmarks
```

Suggested new comparison axes:

```text
predictive target: pixel / latent / geometry / action / multimodal
visual backbone frozen vs adapted
predictor size / compute scaling
planner: direct / CEM / MPC / verifier/search
cross-embodiment action representation
test-time sampling/search budget
inference-state reuse + refresh criterion
stale-state detection
RSI editable surface
immutable evaluator / safety boundary
held-out evaluation
accepted-change inheritance / lineage
research budget
process-level retention / OOD transfer
```

---

### 5. Frontier-watch rule

For every frontier source preserve:

```text
date
exact primary / official / code URL
evidence level
what it demonstrates
what it does NOT demonstrate
input / training provenance
why it changes the comparison space
stable Stage-1 landing
```

Detailed notes belong in the relevant Stage-1 file, supporting audit, source map, benchmark map, engineering notes, or Stage-2 report.

**Do not promote a frontier mechanism directly into Clover Innovation.**

---

<a id="topic-research-emerging-frontier_sweep_2026-10-19"></a>

## Stage-1 Frontier Sweep — 2026-10-16 → 2026-10-19

Source record updated: **2026-10-19**
Source intake checked through: **2026-10-19**

> Mother question: **How can a machine understand the real world through vision alone?**

This sweep extends the Stage-1 frontier watch from the 2026-10-15 cutoff (`sources-and-resources.md`) to 2026-10-19. It is supporting Stage-1 material: it does **not** freeze a representation, backbone or training recipe, and it does **not** promote any mechanism into Clover Innovation.

Raw discovery material for this 2026-10-19 window is preserved in Git history before the 2026-10-25 cleanup; it is not a current reading-tree archive. Items below were upgraded against primary or official sources on 2026-10-19 where a source is marked `PRIMARY_PAPER` / `OFFICIAL_*`; items still resting on secondary listings stay `SURVEY_SIGNAL`.

### Project context for this sweep

```text
CPU-only implementation track: frozen at current results (2026-10-19 decision).
Main line: embodied robotic-brain research on top of those results.
This sweep therefore weights decision/action usefulness (SSOT evidence axis A)
and deployment/runtime evidence more heavily than before,
without dropping the vision-only identifiability discipline (V0–V3, L0–L4).
```

---

### 1. Verified additions

| Date | Source | Evidence | What it demonstrates | Does **not** prove | Stage-1 landing |
|---|---|---|---|---|---|
| 2026-10-15 (listed 10-16) | **VLA-Δ: Learning Physical State Transition for VLA Models** — https://arxiv.org/abs/2610.21306 · code https://github.com/ZJU-OmniAI/VLA-Delta | `PRIMARY_PAPER` / `OPEN_SOURCE` | Supervising the **physical state transition** (Δ between current and future state) instead of only the action improves VLA policies; reported competitive on LIBERO/RoboTwin and **above π0.5 in real-robot experiments**, with zero added inference cost | a state-transition target is a sufficient *world state*, or that Δ-supervision transfers across embodiments without the pretraining mixture used | state-transition supervision · sufficient state (S-PRED vs S-CTRL) · training/post-training |
| 2026-10-16 | **HIJP: Hindsight Inverse JEPA Planning** — https://arxiv.org/abs/2610.23615 | `PRIMARY_PAPER` | Search-free latent planning: a goal-conditioned inverse model replaces test-time action search; hindsight goal relabeling shapes the visual representation; reported 86.8% success across four visual control tasks and 1.9–16.5× planning speedup over search-based planning | latent inverse planning preserves uncertainty/epistemic state, or scales to contact-rich manipulation | JEPA planning · runtime systems · sufficient state |
| 2026-06-30 (resurfaced 10-19) | **AdaJEPA: An Adaptive Latent World Model** — https://arxiv.org/abs/2606.32026 · project https://agenticlearning.ai/adajepa/ · code https://github.com/agentic-learning-ai-lab/adajepa | `PRIMARY_PAPER` / `OFFICIAL_PROJECT` / `OPEN_SOURCE` | A latent world model need not stay frozen at deployment: test-time adaptation inside the MPC loop, using executed transitions as self-supervision, with as little as one gradient step per replan, improves planning under distribution shift | online adaptation is safe/monotonic in open worlds, or that adaptation preserves calibration and long-horizon memory (no forgetting analysis for embodied deployment) | deployment learning (TR10/TR11) · model invalidation (E6) · belief revision |
| 2026-10-14 (demo window 10-20→22) | **NEURA Robotics — Neuron AI (PLA)** — official: https://neura-robotics.com/neura-robotics-introduces-neuron-ai/ · model page https://neura-robotics.com/neuron-ai | `OFFICIAL_REPORTED_RESULT` | A vendor robotic brain claiming perception-language-action with 3D vision + touch + sound + proprioception + memory, on-robot local inference, and an 11-minute unattended laundry sequence on 4NE1 at GTC Berlin 2026 (Hall 3, Booth #3031, Oct 20–22) as its public test | any benchmark number: at launch NEURA published **no** success rates, no Time-to-Skill figures and no independent evaluation; multisensory fusion also means it is **not** a vision-alone (V0–V3/L0–L4-clean) result | robotic-brain competitor watch · persistent memory claims · EV ladder (public demo ≈ EV7 claim, unverified) |
| 2026-10-17→19 (statements) | **OpenAI humanoid program** — Altman statements (Sources podcast / Fortune), reported 2026-10-19: https://www.timesnownews.com/technology-science/openai-is-building-its-own-humanoid-robot-ceo-sam-altman-confirms-article-156365247 | `SURVEY_SIGNAL` (secondary press report; direct interview/official technical source not verified) | Secondary reporting describes humanoid-program plans and executive statements; program scope, timelines and hiring details require direct-source verification | any capability: no model, data, benchmark or hardware detail has been published | industry structure · robotic-brain race · watch for technical disclosure in 2027 demo run-up |
| 2026-04-15 (rechecked 10-19) | **HY-World 2.0** — https://arxiv.org/abs/2604.14268 | `PRIMARY_PAPER` / `OPEN_SOURCE` | Generative 3D world route: reconstruct/generate/simulate editable 3D worlds (mesh / 3DGS / point cloud) from text/image/video, exportable to Unity/UE and embodied-sim pipelines | generated 3D plausibility = physically correct, queryable world state; it sharpens, but does not settle, the "world model" definition dispute (generation vs explicit queryable state) | world-model definition watch · 3D representation · simulation data engines |

### 2. Discovery signals still needing primary-source upgrade

From the 2026-10-15/16 daily-paper listings (Hugging Face / Robotica) and the 10-16→19 digests. Each stays `SURVEY_SIGNAL` until its arXiv page is read and recorded with the §26 contribution template.

```text
Velox: Spatial Memory Makes World Models Efficient (2026-10-15)
  → persistent spatial memory as an efficiency mechanism, not only a capability one
  → landing: memory / sufficient state / edge cost

Can World and Action Modeling Benefit Each Other under Unified Causal Training? (2026-10-15)
  → causal unification of WAM training; direct test of world↔action factorization assumptions
  → landing: WAM · causality

WAVE-0: Bridging VLA Policies and WAMs with Lightweight Latent Future Prediction (2026-10-13/15)
  → hybrid VLA+latent-prediction; compare against GreenWAM / LoopWAM already indexed
  → landing: VLA/WAM boundary

Towards Agentic Robots: Model, Data, Environment, and Harness (2026-10-14) — https://arxiv.org/abs/2610.20442 (html listing seen)
  → agentic-robot system decomposition; harness contribution accounting (AGENTS §21)
  → landing: foundation-model systems · harness

TacDyn-WAM (v1 2026-09-30, resurfaced 2026-10-17)
  → predict contact change, not every tactile pixel — boundary condition for vision-alone claims:
    which contact variables are identifiable from vision (V-protocol) vs require L4 evidence?
  → landing: physical properties · identifiability · provenance

HexaShell / CarryOn / CoDA (2026-10-15/16 listings)
  → harness-as-policy and data-engine co-evolution signals; keep in harness/RSI watch, not core survey
  → landing: foundation-model systems · training
```

### 3. Breadth check recorded on 2026-10-19

Stage 1 requires coverage **before** commitment. This sweep re-checked the breadth axes of `README.md` against the 10-16→19 inflow; the inflow is heavily concentrated in VLA/WAM and industry brain announcements. The following breadth areas received **no** new material in that window. This was the 2026-10-19 intake gap; the 2026-10-20 anchors and 2026-10-25 additions are recorded in [the current queue](README.md#current-collection-queue). Do not treat this dated list as today's unfilled inventory:

```text
classical geometry / SLAM / SfM baselines and their failure records
human & developmental visual cognition (object permanence, intuitive physics)
image formation & adverse visual conditions (observation physics)
POMDP / observability / identifiability theory (canonical, pre-2026 sources)
deformable / fluid / granular dynamics beyond rigid-body benchmarks
evaluation methodology: shortcut-resistant, examiner-isolated test design
```

Rule reinforced: frontier items may **not** narrow the survey. A sweep that only adds VLA/WAM papers is a failed sweep.

### 4. What changed in the comparison space

```text
state-transition (Δ) supervision
≠ world-state representation — but it is now a measured training signal
  a robotic brain can exploit without inference cost

frozen-at-deployment world model
≠ default assumption — AdaJEPA makes deployment-time adaptation
  a first-class design variable (with open safety/forgetting questions)

"robotic brain" is now an explicit industry product category
  (OpenAI full-stack entry; NEURA PLA; Figure/Skild class systems)
  → Clover's long-term goal statement is the contested ground itself;
    differentiation must come from evidence quality (identifiability,
    licence-style accounting, falsifiable claims), not from the slogan

public unattended long-sequence demos (NEURA laundry, 11 min)
  → becoming the industry's informal EV7 evidence; Clover's EV ladder
    remains the stricter accounting and should be applied to every such claim
```

### 5. Next checks (owners: research line, no deadline theatre)

1. Read VLA-Δ and HIJP in full; record both with the AGENTS §26 template in `sources-and-resources.md` and decide whether Δ-supervision deserves a structured Stage-2 method section.
2. NEURA GTC Berlin (2026-10-20→22): collect independent reporting/video of the laundry sequence; score against the EV ladder and the memory/persistence claims; upgrade or downgrade the `OFFICIAL_REPORTED_RESULT` accordingly.
3. Upgrade §2 signals to primary sources in listing order; drop any that cannot be upgraded.
4. Next sweep must include at least one canonical/breadth source per §3 axis (pre-2026 primary literature counts).
5. Watch for OpenAI robotics technical disclosure (paper, system card, or demo protocol) rather than executive statements.

---

<a id="topic-research-survey-frontier_signals"></a>

## Frontier Signals — Filtered 2026 Watchlist

Source record updated: 2026-10-14

This is the screened signal list inherited from the earlier internal news intake; it was last checked at the source dates shown below. A signal is kept when it changes how the central problem should be framed, reveals a competing approach, exposes an evaluation failure, or points to primary material worth deeper study.

A frontier signal is **not automatically a scientific result or a Clover design decision**.

### Signals

1. **ReWAM** — task-relevant/action-grounded representation matters beyond reconstruction fidelity. https://arxiv.org/abs/2609.38163
2. **HWAM** — reference action, executed motion and realized state must be separated. https://arxiv.org/abs/2610.12026
3. **V-JEPA 2 / 2.1** — passive video is a serious route to physical/temporal representation. https://arxiv.org/abs/2506.09985 · https://arxiv.org/abs/2603.14482
4. **Interpreting Physics in Video World Models** — physical variables can be distributed/hierarchical. https://arxiv.org/abs/2602.07050
5. **VISTA** — memory/retrieval architecture can unlock capability without changing base weights. https://arxiv.org/abs/2610.02200
6. **Vantage** — viewpoint/evidence selection is a first-class reasoning variable. https://arxiv.org/abs/2610.11810 · https://github.com/q1xiangchen/Vantage
7. **SpatialCORE** — confidence can guide learning/compute, but confidence is not truth. https://arxiv.org/abs/2609.38716
8. **H-WM** — hierarchy remains a live response to long-horizon visual-grounding vs logical-planning tension. https://arxiv.org/abs/2602.11291
9. **Identifiable World Models** — possible bridge between powerful latent state and explicit/identifiable coordinates. https://arxiv.org/abs/2610.07028
10. **VGGT / VGGT-Ω** — learned geometry is becoming a foundation representation. https://arxiv.org/abs/2503.11651 · https://arxiv.org/abs/2605.15195
11. **Atlas** — reconstruction, generation and simulation are merging in spatial world models. https://www.worldlabs.ai/blog/atlas
12. **Cosmos 3** — reasoning, world generation and action interfaces are increasingly unified. https://arxiv.org/abs/2606.02800 · https://github.com/nvidia/cosmos
13. **Figure Helix 2.5 / Skild S1** — broad policy/foundation models are serious falsifiers for explicit-worldview necessity. https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization · https://skild.ai/blogs/s1
14. **RT-2 / OpenVLA / π0.5** — VLA remains a real competing route. https://arxiv.org/abs/2307.15818 · https://arxiv.org/abs/2406.09246 · https://arxiv.org/abs/2504.16054
15. **World-Action Models survey** — WAM is now a distinct research category with open problems in factorization, alignment, memory and efficient inference. https://arxiv.org/abs/2609.16074
16. **Being-M0.7 / Being-H0.7** — future-aware control representation is moving toward latent prediction rather than full pixel rollout. https://arxiv.org/abs/2610.11283 · https://arxiv.org/abs/2605.00078
17. **EVEWorld / RoboPhys-3D** — visual quality alone can hide physical/state failure; process/state/execution-grounded evaluation is increasingly important. https://arxiv.org/abs/2610.03374 · https://arxiv.org/abs/2608.28718
18. **DR-WM / From Pixels to Executable Physics** — some action-relevant physical state appears to require interaction-grounded calibration beyond appearance alone. https://arxiv.org/abs/2610.17630
19. **Motion-aware Event Suppression** — sparse physical visual change can support high-rate computation. https://arxiv.org/abs/2602.23204
20. **Tactile/contact-rich robotics** — defines a boundary condition: vision can infer hypotheses about hidden physical properties, but should not silently claim exact force/friction/internal contact state as observed.
21. **Long-horizon unfamiliar closed-loop behavior** — the durable industrial frontier is unseen environments, active perception, world change/recovery, mobile/whole-body manipulation and broad experience pretraining.

### Not promoted to current conclusions

Funding/valuation reports, supply-chain announcements, secondary summaries, single demos, unclear benchmark numbers and old “this proves Clover is right” interpretations remain historical signals unless stronger technical evidence is available.

### Future signal template

```text
name
primary/official URL
evidence class
what changed
what it does not prove
why the SSOT cares
research question affected
```

A frontier signal is a reason to investigate, not a reason to stack another framework into Clover.

---

<a id="topic-research-literature-2026-frontier"></a>

## 2026 Frontier Watch — Physical World Models and Embodied Intelligence

Source record updated: 2026-10-14

This note tracks 2026 work that materially changes the research landscape around Clover's SSOT. It is not a module shopping list. Each item is included because it sharpens a research contradiction.

### 1. Cosmos 3 — omnimodal world model

**Paper:** https://arxiv.org/abs/2606.02800
**Project:** https://research.nvidia.com/labs/cosmos-lab/cosmos3
**Code:** https://github.com/nvidia/cosmos

Cosmos 3 jointly processes/generates language, image, video, audio and action sequences in one mixture-of-transformers family. Its relevance to Clover is conceptual: the boundary between `world model`, `VLM`, `simulator` and `policy backbone` is becoming less clean.

#### Research tension

If one model can jointly represent observation and action distributions, does a separately materialized worldview still provide unique value? Clover eventually has to answer this with persistence, revision, causal/action utility or efficiency evidence — not by architectural preference.

---

### 2. RoboPhys-3D — world-model evaluation grounded in 3D state and execution

**Paper:** https://arxiv.org/abs/2608.28718

RoboPhys-3D evaluates embodied video world models using a shared 3D reconstruction pipeline and separates pixel fidelity, 3D consistency, state understanding and task completeness. Its key message for Clover is methodological: perceptual or VLM judgments can miss failures that become obvious when evaluated against reconstructed state and executable task outcomes.

#### Research tension

A world model should not be accepted because its generated video looks plausible. Evaluation must reach state and action consequences.

This directly supports Clover's multi-level Understanding Battery.

---

### 3. Hy-Embodied-VLM-1.0 — action-centric physical-world reasoning taxonomy

**Paper:** https://arxiv.org/abs/2607.12894

The work organizes embodied capability into three progressive dimensions:

1. action-relevant state understanding;
2. action-transition reasoning;
3. sequential and adaptive reasoning.

#### Research tension

This is useful because it connects perception to action without collapsing them into one accuracy number. Clover can compare its own future capability taxonomy against this decomposition while retaining its stronger vision-only causal-attribution requirement.

---

### 4. RBench / RoVid-X — evaluate physical realism of robot video generation

**Paper:** https://arxiv.org/abs/2601.15282

RBench evaluates robot-oriented video generation across multiple tasks/embodiments with metrics for structural consistency, physical plausibility and action completeness. RoVid-X provides a large open robotic video-generation dataset.

#### Research tension

Video generation is becoming an embodied data engine, but generative quality and world understanding are not interchangeable. Clover should track which evaluation dimensions correlate with actual executable state correctness.

---

### 5. ABot-PhysWorld — physics-aligned interactive video world model

**Paper:** https://arxiv.org/abs/2603.23376

ABot-PhysWorld targets a known failure of generic video generation: visually plausible but physically impossible robot interactions such as penetration or anti-gravity motion. It adds physics-aware data/post-training and an action-control mechanism.

#### Research tension

This supports a central question for Clover: should physical structure be encoded in the representation/transition model itself, or corrected statistically during post-training? These are different scientific hypotheses.

---

### 6. Xiaomi-Robotics-U0 — world foundation models as embodied data engines

**Paper:** https://arxiv.org/abs/2607.11643
**Project/code:** https://robotics.xiaomi.com/xiaomi-robotics-u0.html

U0 treats embodied synthesis as an extension of large image/video generation and targets multi-view consistency, embodiment transfer and robot-video generation.

#### Research tension

This is another route where `world model` primarily acts as a scalable data/simulation engine rather than an explicit persistent robot worldview. Clover should keep these roles distinct when comparing approaches.

---

### 7. Figure Helix 2.5 — unseen-home real-robot generalization

**Official reported result:** https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization

Figure reports zero-shot whole-body behavior in 30 unseen homes after pretraining on its Index human-behavior dataset.

#### Evidence label

**Official company-reported real-robot result.** No independent reproduction is implied here.

#### Research tension

Large-scale human behavior experience may provide a strong prior for physical generalization without exposing an explicit world state. This is a direct challenge to any claim that explicit representation is inherently necessary.

---

### 8. Skild S1 / Physical Self-Play — broad experience and self-generated interaction

**S1 official report:** https://www.skild.ai/blogs/s1
**Physical Self-Play:** https://skild.ai/blogs/physical-self-play

Skild represents the hypothesis that broad robot competence can emerge from heterogeneous physical experience plus in-context specification, with self-play extending experience beyond imitation.

#### Evidence label

**Official company-reported results.** Treat capability claims as reported until independent evidence exists.

#### Research tension

The learning problem may be as important as the representation problem: passive visual observation, demonstrations, simulation and self-generated interventions provide different information.

---

### Cross-cutting conclusion

The 2026 frontier increasingly separates into four roles that are often all called `world model`:

1. **representation model** — extract state/features from observation;
2. **predictive dynamics model** — forecast latent/state transitions;
3. **generative simulator/data engine** — synthesize plausible futures or training data;
4. **decision-coupled model** — directly support planning/action.

Clover should not use the term `world model` without specifying which role is meant.

The strongest open question remains:

> **What internal structure is necessary for a robot to maintain, revise and use an understanding of the real world from visual evidence — and which apparent capabilities can instead be obtained from large distributed models without such explicit structure?**

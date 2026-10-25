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

三组共 1,611 条返回记录，按论文 ID 去重后 **1,482** 条。当前分类列表也核对了 [cs.RO recent](https://arxiv.org/list/cs.RO/recent) 与 [cs.CV recent](https://arxiv.org/list/cs.CV/recent)：最新可见公告批次为 **2026-10-23**。公告日期、初次提交日期、修订日期和本项目核验日期不是一回事。

关键词排序只用于找候选，不能充当全部论文的人类精读或排除判决。本次自动高分候选有 81 条；另用几何、物性、记忆、泛化、风险等题名检索补查，发现低分但直接相关的工作。本节登记的入选论文均人工检查了摘要，部分另核读方法/监督/局限段。未将 1,482 条全部声称为纳入文献或精读文献。

### 既有记录书目检查

基线提交 `fae924516c5bc3862125cd67d57b3850f3fdf462` 的九份调研正文，以 `arxiv.org/(abs|html|pdf)/(数字ID)` 提取并去掉版本号，得到 **335 个数字格式 arXiv ID**；全部从一手 API 返回了题名、作者、初次提交、当前版本/修订日期与摘要。批次每组不超过 70 个 ID，按 `id_list` 读取，没有以检索命中率替代结论核查。此项检查证明编号可追溯，**不证明** 全部旧综述句子、数值、理论条件、代码或部署能力正确；旧式 ID、非 arXiv 原文与所有官方项目的新鲜度仍需另查。

当前书目示例应使用精确题名：`2610.23615` 返回 **Beyond Action Prediction: Learning Search-Free Planning in Latent Space**（旧简称 HIJP 仅作别名）；`2610.15429` 返回 **World Modeling through Spectral Alignment**（旧简称 SpecWM 不是完整题名）。不得用简称猜测作者、版本或证明内容。

### 本轮新增与深化文献索引

下表共 54 条：53 篇首次登记；GNS（`2002.09405`）原已登记，本轮将摘要级记录深化到方法与监督边界选读，不重复计入新增论文。

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

### 本轮尚未闭合的核查

- 当前前沿的非 arXiv 会议/期刊/官方发布，以及旧 335 篇的全部研究性主张，尚未逐项完成内容级复核。
- 部分新论文当前只有摘要级登记；模拟器版本、精确 checkpoints、完整训练混合、许可及公平预算仍待方法级核读。正文入口可访问/缓存不等于已读完。
- RGB-only 可变形/颗粒隐藏态、自然机器人视频的可识别性、压缩后的未知任务证据恢复仍是实质证据缺口；点云/力传感方案不能替代它们。
- 泛化、风险覆盖和物理因果的经典定理条件仍需继续与视觉/闭环设置逐项比对。当前覆盖表不是“全面完成”的证明。
<!-- END current-search-protocol -->

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

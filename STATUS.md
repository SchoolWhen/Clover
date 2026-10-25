# Clover Status

Last updated: **2026-10-25**.

> **Research question:** How can a machine understand the real world through vision alone?
>
> **Long-term goal:** Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.

## Current project decision

**Stage 1 — Research / Survey & Evidence Collection is ACTIVE.** No representation, backbone or core algorithm is frozen. The 2026-10-15 recommendations to make Stage 2 primary remain [dated assessments in Stage 1](01-research/README.md#topic-research-stage1_final_audit_2026-10-15); they were not an approved stage transition.

The 2026-10-19 decision remains in force: the CPU-only implementation line is frozen at its current results. It resumes only after the embodied-intelligence line produces a new, complete frontier breakthrough. This repository's main line is robotic-brain research.

Apple M4 remains the local development reference; no target real robot is currently available. Final robot hardware is open. No new algorithm, experiment or deployment is reported in this update.

## 当前进展与下一步 — 2026-10-25


| 事项 | 当前状态 | 入口 |
|---|---|---|
| 仓库结构 | 跨阶段约束留在根目录；七个阶段各有目录，第一阶段按研究方向平铺；历史保留在 Git | [主页](README.zh-CN.md) · [维护规则](AGENTS.md) |
| 被动镜面视觉 | 新增 Ref-NeRF / NeRFactor；区分光度拟合与唯一物理分解，以及测量先验 | [观测](01-research/perception-and-identifiability.md#reflection-evidence) |
| 因果可识别性 | 新增 BISCUIT 与真实光学 CRL 负结果；修正“所有被动视频不可能”的过度推断 | [因果](01-research/causality-and-active-perception.md#causal-identification-evidence) |
| 压缩与记忆 | 新增 FastV / FrameFusion；固定版本、配置与时延范围，保留未知未来任务的证据缺口 | [表示](01-research/representation-and-memory.md#compression-evidence) · [评估](01-research/evaluation-and-benchmarks.md#evidence-retention-diagnostics) |
| 引用与阅读深度 | 6 篇新增一手文献，逐条标明核读部分、V/L来源与复现边界；继承文献不自动升级为新核验 | [来源](01-research/sources-and-resources.md#verified-additions) |

**未完成的科学工作：** RGB-only 可变形/颗粒状态；自然真实机器人视频的可靠可识别性；压缩后未来任务的证据保留与恢复；封闭原文全文核读。下一步继续定向调研和反例登记。原有跨主题问题仍见下文；这里没有宣布阶段退出、实验通过或算法达标。

## Current reading route

[Contract](SSOT.md) → [research map and current queue](01-research/README.md#current-collection-queue) → [research questions](01-research/research-questions.md) → the relevant topic. [`01-research/sources-and-resources.md`](01-research/sources-and-resources.md#verified-additions) owns source discovery; [`PROCESS.md`](PROCESS.md) owns lifecycle/templates; [`AGENTS.md`](AGENTS.md) defines document ownership.

## Remaining cross-topic collection questions

- Observation: visual-token/FPS budget versus physical-state evidence; hidden physical variables versus appearance priors; real-world identifiability under image-formation noise.
- State/memory: equal-byte long context, persistent state and original-evidence retrieval; compression reversibility; uncertainty and belief revision after quantization or pruning.
- Learning: frozen/adapted backbone attribution; human/robot/simulator mixtures; failure/recovery data; reward/verifier reliability; post-training preservation of memory, physics and calibration.
- Action/open world: model-class misspecification, regime changes, safe irreversible probing, embodiment changes and social permission.
- Systems: streaming encode/cache invalidation; fast-control/slow-reasoner synchronization; end-to-end latency; runtime drift; API/checkpoint/harness provenance.
- Validation: independent splits and matched baselines; simulator/solver shortcuts; sim-to-sim versus real transfer; rollback and persistent-state corruption.

These remain research questions, not a declared collection failure or an instruction to invent an architecture. Individual evidence dates remain in their topic records. The six new papers do not revalidate all inherited vendor/frontier claims.

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

## Not yet demonstrated


Clover has not yet publicly demonstrated a validated general real-world visual world model, final representation, final foundation-model backbone, final training recipe, robust open-world generalization, general causal understanding, persistent long-horizon real-robot world state, validated sim2real transfer, validated original algorithm, or final hardware mapping.

These remain research targets.

## Repository structure — 2026-10-25

- Root: shared research contract, agent rules, lifecycle, global status, bilingual homepage and repository metadata.
- `01-research/`: one current file per research direction, plus its substantive overview; benchmark/source surveys remain Research material.
- `02-analysis/` through `07-reflection/`: stage-owned templates/current records. Existing candidate ideas live in Stage 4 without being adopted; directory creation is not stage completion.
- Update the existing stage/direction file in place. Keep earlier states in Git rather than dated progress files, old-path shells or an archive tree.
- This layout supersedes the previous all-root topic layout. No research claim, source-reading depth, experiment result or active-stage decision changes through the move.

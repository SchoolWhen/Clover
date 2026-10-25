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

| 事项 | 当前证据 | 入口 |
|---|---|---|
| 研究目标 | 完整、全面、当前的前沿/相关/交叉研究；仍保持原视觉问题与 Stage 1 | [完整性审查](01-research/README.md#coverage-and-completion-audit) |
| 本轮方向补充 | 首次登记 **53 篇**，深化 **1 篇**已有论文，按机制、输入/学习来源、证据和边界写回现有正文 | [交叉桥接](01-research/research-questions.md#cross-domain-research-bridges) |
| 前沿检索 | 3 组一手接口返回 1,611 条、去重 1,482 条；分类公告核对到 10-23；未把所有候选声称为精读 | [来源协议](01-research/sources-and-resources.md#current-search-protocol) |
| 旧引文核查 | 335 个数字 arXiv ID 均取回书目；未据此宣布全部旧研究结论正确 | [书目边界](01-research/sources-and-resources.md#current-search-protocol) |
| 模型 artifact | 四个官方权重 revision 已读取模型卡与配置，分清公开文本权重和托管视觉/工具特性 | [精确版本](01-research/foundation-models-and-systems.md#current-model-artifacts) |
| 结构与持续维护 | 根目录跨阶段规则；调研继续按原八方向原位更新，没有新增调研文件 | [第一阶段](01-research/README.md) |

**尚未完成：** 非 arXiv 前沿与全部旧官方 artifact 刷新；部分新增论文的方法/监督/实验完整核读；335 篇旧记录的内容级主张审查；RGB-only 隐藏态、真实因果识别和未知未来任务证据恢复的进一步检索。当前未通过全范围完整性核查，目标继续推进，没有宣布“全面完成”或推进阶段。

## Current reading route

[Contract](SSOT.md) → [research map and current queue](01-research/README.md#current-collection-queue) → [research questions](01-research/research-questions.md) → the relevant topic. [`01-research/sources-and-resources.md`](01-research/sources-and-resources.md#verified-additions) owns source discovery; [`PROCESS.md`](PROCESS.md) owns lifecycle/templates; [`AGENTS.md`](AGENTS.md) defines document ownership.

## Remaining cross-topic collection questions

- Observation: visual-token/FPS budget versus physical-state evidence; hidden physical variables versus appearance priors; real-world identifiability under image-formation noise.
- State/memory: equal-byte long context, persistent state and original-evidence retrieval; compression reversibility; uncertainty and belief revision after quantization or pruning.
- Learning: frozen/adapted backbone attribution; human/robot/simulator mixtures; failure/recovery data; reward/verifier reliability; post-training preservation of memory, physics and calibration.
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

## Not yet demonstrated


Clover has not yet publicly demonstrated a validated general real-world visual world model, final representation, final foundation-model backbone, final training recipe, robust open-world generalization, general causal understanding, persistent long-horizon real-robot world state, validated sim2real transfer, validated original algorithm, or final hardware mapping.

These remain research targets.

## Repository structure — 2026-10-25

- Root: shared research contract, agent rules, lifecycle, global status, bilingual homepage and repository metadata.
- `01-research/`: one current file per research direction, plus its substantive overview; benchmark/source surveys remain Research material.
- `02-analysis/` through `07-reflection/`: stage-owned templates/current records. Existing candidate ideas live in Stage 4 without being adopted; directory creation is not stage completion.
- Update the existing stage/direction file in place. Keep earlier states in Git rather than dated progress files, old-path shells or an archive tree.
- This layout supersedes the previous all-root topic layout. No research claim, source-reading depth, experiment result or active-stage decision changes through the move.

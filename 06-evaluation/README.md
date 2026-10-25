<a id="top"></a>

# 第6阶段：Evaluation / 实验评测

Maintained: **2026-10-25**.

本阶段必须遵守根目录的 [研究契约](../SSOT.md)、[agent 规则](../AGENTS.md) 和 [全局流程](../PROCESS.md)。当前项目阶段由 [`../STATUS.md`](../STATUS.md) 唯一确定；目录存在不代表该阶段已启动或产出已通过。

## 当前状态与归属

尚无本次整理产生的实验结果。这里拥有实验注册、协议、测量和结果；基准文献的前期调研留在第一阶段。

本阶段先在本文件内维护结构化条目；需要多个方向时按方向命名文件，直接更新其最新状态。每项工作通过来源、方法、假设或运行 ID 连接其他阶段的证据，不复制整篇上游文档，也不生成日期补丁或每次进展的新文件。

<a id="topic-research-evaluation"></a>

## Stage 6 — Evaluation

### Experiments, Results and Falsification

Source record updated: 2026-10-14

**Status:** FRAMEWORK DEFINED; full execution is downstream of Analysis, Synthesis and selected implementations.

Evaluation asks whether the claimed capability actually appears under controlled conditions and whether it survives comparison with strong alternatives.

### Evidence ladder

```text
unit / synthetic diagnostic
→ controlled benchmark
→ controlled real-world test
→ unfamiliar real environment
→ long-horizon embodied task
```

Not every question requires the full ladder, but claims must not exceed the highest evidence level reached.

### Required result metadata

```text
hypothesis or baseline
exact model / checkpoint
exact code version
exact dataset / split
visual protocol V0–V3
learning provenance L0–L4
prompt / query protocol when applicable
hardware
metric definition
number of trials
uncertainty / variance
failure cases
reproduction status
```

### Evaluation dimensions

- geometry;
- identity;
- object permanence;
- temporal consistency;
- observability / unknown;
- memory / retrieval;
- belief revision;
- intuitive physics;
- quantitative / relational physics;
- causality / intervention;
- counterfactual reasoning;
- active perception;
- open-world generalization;
- camera / embodiment shift;
- planning usefulness;
- action success;
- recovery;
- latency / memory / energy when relevant.

### Baseline rule

Compare across qualitatively different method families, not only variants of Clover.

### Results rule

Report negative results. Preserve failures that kill an idea. Do not hide trade-offs behind one average score.

### Output

Stage 6 produces result tables, figures, ablations, failure logs and explicit hypothesis status changes. Interpretation belongs to Stage 7 Reflection.

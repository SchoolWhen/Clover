<a id="top"></a>

# 第2阶段：Analysis / 方法分析

Maintained: **2026-10-25**.

本阶段必须遵守根目录的 [研究契约](../SSOT.md)、[agent 规则](../AGENTS.md) 和 [全局流程](../PROCESS.md)。当前项目阶段由 [`../STATUS.md`](../STATUS.md) 唯一确定；目录存在不代表该阶段已启动或产出已通过。

## 当前状态与归属

方法分析阶段尚未成为主阶段；本次只归位现有分析模板，没有新增方法分析结果。

本阶段先在本文件内维护结构化条目；需要多个方向时按方向命名文件，直接更新其最新状态。每项工作通过来源、方法、假设或运行 ID 连接其他阶段的证据，不复制整篇上游文档，也不生成日期补丁或每次进展的新文件。

<a id="topic-research-analysis"></a>

## Stage 2 — Analysis

### Method Reports and Mechanism Decomposition

Source record updated: 2026-10-14

**Status:** DEFINED, NOT YET THE PRIMARY ACTIVE STAGE.

Analysis begins after Stage 1 Research has collected sufficiently broad material. Its job is to understand individual methods deeply rather than adding more names to the inventory.

### One method = one structured section in its canonical topic document

For every important method, use this template:

```text
Method / paper:
Version / date:
Research family:
Primary paper:
Official project:
Official code:
Evidence level:

Problem solved:
Input observations:
Training data / supervision:
V0–V3 observation protocol:
L0–L4 learning provenance:

Core representation:
Core mechanism:
Learning objective:
Temporal mechanism:
Memory mechanism:
Geometry assumptions:
Object/entity assumptions:
Physics assumptions:
Causal assumptions:
Action interface:

Datasets:
Benchmarks:
Reported result:
Reproduced result:

Strengths:
Weaknesses:
Confounds:
Failure modes:
Compute / scale requirements:
Reproducibility:

What this method actually demonstrates:
What it does NOT demonstrate:
Which Clover question it constrains:
What experiment would distinguish it from competing methods:
```

### Analysis dimensions

Every report should try to answer the same dimensions so later Synthesis is possible:

1. **Representation** — pixels, features, point maps, slots, tokens, graphs, latent state, explicit state, simulator, policy hidden state, etc.
2. **Time** — frame-local, short history, streaming, recurrent, persistent, episodic, future prediction.
3. **Space** — 2D, projective 3D, metric 3D, 4D, topological, semantic, relational.
4. **Identity** — visible association, persistent entity, object permanence, re-identification.
5. **Physics** — none, qualitative, relational, quantitative, hard constraint, learned dynamics.
6. **Causality** — correlation, prediction, action-conditioned transition, intervention, counterfactual.
7. **Uncertainty** — confidence only, calibrated uncertainty, belief state, explicit unknown / refusal.
8. **Memory** — context window, recurrent state, external store, episodic retrieval, map, replay.
9. **Action** — no action, downstream policy, action conditioning, planner, joint world/action model.
10. **Generalization** — object, scene, camera, dynamics, embodiment, real-world shift.
11. **Learning evidence** — image/video only, labels, language, robot actions, proprioception, simulation privilege.
12. **Evaluation** — what the benchmark truly measures and what shortcuts remain.

### Rule

Do not write “better” or “worse” without specifying the dimension, protocol and evidence.

Do not import the method into Clover during Analysis. Analysis produces understanding, not architecture.

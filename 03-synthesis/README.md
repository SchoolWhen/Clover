<a id="top"></a>

# 第3阶段：Synthesis / 综合比较

Maintained: **2026-10-25**.

本阶段必须遵守根目录的 [研究契约](../SSOT.md)、[agent 规则](../AGENTS.md) 和 [全局流程](../PROCESS.md)。当前项目阶段由 [`../STATUS.md`](../STATUS.md) 唯一确定；目录存在不代表该阶段已启动或产出已通过。

## 当前状态与归属

综合比较阶段尚未启动；能力矩阵、机制矩阵与失败矩阵目前是待产出的结构。

本阶段先在本文件内维护结构化条目；需要多个方向时按方向命名文件，直接更新其最新状态。每项工作通过来源、方法、假设或运行 ID 连接其他阶段的证据，不复制整篇上游文档，也不生成日期补丁或每次进展的新文件。

<a id="topic-research-synthesis"></a>

## Stage 3 — Synthesis

### Comparative Summary, Trade-offs and Research Gaps

Source record updated: 2026-10-14

**Status:** DEFINED, DOWNSTREAM OF SUFFICIENT ANALYSIS.

Synthesis combines many Stage 2 method reports into a field-level view.

### Core outputs

#### Capability matrix

Compare methods across common capabilities:

```text
geometry
identity
object permanence
temporal consistency
observability / unknown
memory
revision
physics
causality
counterfactual reasoning
active perception
open-world generalization
action utility
recovery
compute
```

#### Mechanism matrix

Compare how methods achieve capability:

```text
explicit geometry
dense features
predictive latent
slots/entities
graph state
external memory
generative simulation
joint world-action prediction
direct policy
hybrid / identifiable state
```

#### Pros / cons summary

For every family, summarize:

```text
what it is genuinely good at
what it systematically misses
where evidence is strong
where evidence is weak
where evaluation may contain shortcuts
which assumptions it relies on
what it costs computationally
what is reproducible
```

#### Failure matrix

Do not collapse failures into one score. Record them separately.

#### Gap map

A gap is interesting only if:

1. multiple strong methods share it, or
2. solving it would materially improve real world understanding/action, and
3. current evidence does not already show a simpler solution.

### Synthesis questions

- Which research problems are already mostly solved?
- Which capabilities remain weak across method families?
- Which apparent disagreements are only terminology differences?
- Which methods have complementary strengths?
- Which trade-offs appear fundamental rather than engineering accidents?
- Which results depend heavily on language, privileged state, simulation or action supervision?
- Which benchmarks fail to distinguish competing hypotheses?
- Which strong direct-policy systems challenge the need for an explicit worldview?
- Which generative systems challenge the need for explicit state?
- Which memory failures challenge long-context approaches?
- Which causal results show that interaction is necessary?

### Output gate to Innovation

Stage 4 Innovation should not start from “I like this architecture.”

It starts from:

```text
well-supported unresolved gap
+ comparison of existing solutions
+ reason existing mechanisms are insufficient
+ discriminating test
```

Synthesis is where Clover earns the right to propose something new.

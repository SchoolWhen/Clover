<a id="top"></a>

# 第5阶段：Implementation / 实现

Maintained: **2026-10-25**.

本阶段必须遵守根目录的 [研究契约](../SSOT.md)、[agent 规则](../AGENTS.md) 和 [全局流程](../PROCESS.md)。当前项目阶段由 [`../STATUS.md`](../STATUS.md) 唯一确定；目录存在不代表该阶段已启动或产出已通过。

## 当前状态与归属

核心实现阶段尚未启动；不得因存在目录而声称代码、复现或部署已完成。必要的早期诊断仍需说明其研究目的。

本阶段先在本文件内维护结构化条目；需要多个方向时按方向命名文件，直接更新其最新状态。每项工作通过来源、方法、假设或运行 ID 连接其他阶段的证据，不复制整篇上游文档，也不生成日期补丁或每次进展的新文件。

<a id="topic-research-implementation"></a>

## Stage 5 — Implementation

### Reproducible Code and System Construction

Source record updated: 2026-10-14

**Status:** FUTURE CORE STAGE. Small diagnostic implementations are allowed earlier only when they directly answer a research question.

Implementation turns selected baselines, diagnostics and Clover hypotheses into reproducible code.

### Required implementation record

```text
implemented claim / hypothesis
source or design document
code path
configuration
model / checkpoint version
dataset version
dependencies
hardware
seed / determinism notes
input protocol
output protocol
instrumentation
known limitations
```

### Implementation priorities

1. reproducibility;
2. correctness;
3. observability / tracing;
4. clear interfaces;
5. only then optimization.

### What belongs here

- baseline adapters;
- dataset loaders;
- benchmark runners;
- probing code;
- Clover algorithm implementation;
- training/inference pipelines;
- experiment configuration;
- logging and tracing;
- deployment experiments.

### What does not count as scientific evidence

- amount of code written;
- architecture complexity;
- visual quality of a demo;
- performance on one hand-selected example;
- an implementation matching its own design specification.

Implementation creates the object that Evaluation will test. It does not validate the hypothesis by itself.

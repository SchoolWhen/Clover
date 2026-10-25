<a id="top"></a>

# 第7阶段：Reflection / 反思

Maintained: **2026-10-25**.

本阶段必须遵守根目录的 [研究契约](../SSOT.md)、[agent 规则](../AGENTS.md) 和 [全局流程](../PROCESS.md)。当前项目阶段由 [`../STATUS.md`](../STATUS.md) 唯一确定；目录存在不代表该阶段已启动或产出已通过。

## 当前状态与归属

当前只维护反思模板；实证解释须引用已经登记的结果，不能先写成功故事。

本阶段先在本文件内维护结构化条目；需要多个方向时按方向命名文件，直接更新其最新状态。每项工作通过来源、方法、假设或运行 ID 连接其他阶段的证据，不复制整篇上游文档，也不生成日期补丁或每次进展的新文件。

<a id="topic-research-reflection"></a>

## Stage 7 — Reflection

### Interpretation, Failure Analysis and Iteration

Source record updated: 2026-10-14

**Status:** FUTURE STAGE.

Reflection closes a research cycle. It decides what the results mean, which assumptions should change, and where the next cycle should begin.

### Reflection record

```text
experiment / result:
original hypothesis:
expected outcome:
actual outcome:

what survived:
what failed:
what was ambiguous:
what confound remained:
what assumption was wrong:
what evidence is still missing:

hypothesis status:
KEEP / MODIFY / REJECT / SUPERSEDE / OPEN

next research question:
next analysis task:
next synthesis update:
next innovation candidate, if justified:
```

### Failure taxonomy

Try to distinguish:

- representation failure;
- learning-objective failure;
- data failure;
- benchmark shortcut;
- calibration failure;
- memory failure;
- planning / control failure;
- implementation bug;
- compute limitation;
- interface / systems failure;
- unsupported scientific assumption.

### Rule

Do not respond to every negative result by adding another module.

Sometimes the correct research action is:

```text
delete a mechanism
revise a variable
return to Research
run a better Analysis
change the benchmark
or reject the hypothesis entirely
```

Reflection feeds a new Research → Analysis → Synthesis → Innovation cycle.

The purpose is cumulative learning, not preservation of a preferred architecture.

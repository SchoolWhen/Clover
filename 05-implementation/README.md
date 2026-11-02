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


---

## 实现记录（2026-11-02 序列四 + 五.4 落地）

本阶段自本日起有实质内容：完整代码库位于仓库根 `src/clover/`（与 AGENTS §27 的阶段顺序冲突之处，按用户 2026-11-02 清单优先，已在各提交信息注明）。

| 子包 | 内容 | 对应主张 |
|---|---|---|
| `core/` | 帧流、V1 内参、V2 多视角标定、V3 动作接口、八态认识论标签、H6 证明携带断言 | 全仓数据契约 |
| `harness/` | EndToEndProfiler（全链路分段 P50/P95/P99+jitter)、ResourceAuditor（权重哈希/峰值 RAM/State Byte Budget/Joule 仅实测）、FairBudgetController(Equal-Byte/Equal-Latency) | 二.6 契约、二.1 公平预算 |
| `models/` | Phase A 十家族统一适配器（懒加载、失败关闭、FP16/INT8 按官方导出记录校验、dry-run 盖章） | A 组分析卡的工件层 |
| `probes/` | FrozenLinearProbe（容量上限硬拒绝）+ ZeroShotKNNProbe、NonMarkovianityDetector、StateAliasingAuditor、ReversibilityProbe | 二.1 探针协议、H3 |
| `benchmarks/` | B15 HiddenStateMinimalPairs、EpistemicOcclusionBattery(U9–U12)、AntiShortcutSuite | 自建判别电池 |
| `innovation/` | DualMemoryReplay(H1/H4/H5/H6)、SparseEventIR(H9/H2)、CounterWitnessCausality(H7)、AnytimeComputeScheduler(H8)、TransitionAffordance(H12/H14) | 04-innovation 规约的实现面 |

验证状态：单元测试 24/24 通过（tests/test_clover.py，本机 unittest 实测）；`scripts/run_experiments.py` 五组 EV0 实验已执行（总墙钟 18.2s），原始输出 `results/exp_results_2026-11-02.json`。适配器在本机全部失败关闭（无 GPU/权重），这是设计行为而非缺陷，证据见 06-evaluation。

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


---

## 证据日志（2026-11-02 序列五.4 首批实测，全部 EV0）

运行环境：本机 CPU（无 GPU、无真实机器人、无模型权重）；`PYTHONPATH=src python3 scripts/run_experiments.py`，总墙钟 18.2s；原始输出 `results/exp_results_2026-11-02.json`。**EV1–EV8 仍为 Open**（无模拟器/真机），本批只把 EV0 从「零」变为有记录。

### EXP1 Phase A 压缩损伤（实验 1）
- 适配器失败关闭审计：10/10 家族 `FAIL_CLOSED_OK`（无后端/权重时拒绝运行，不伪造结果）。
- 输入管线信息损失代理（合成属性 + 容量上限线性探针）：tokens 4096→0.700、1024→0.661、256→0.656、64→0.728、16→0.700。**无单调退化**——所选合成属性（圆盘尺寸/竖线计数）是低频全局特征，对下采样不敏感；该代理设计被判定为不敏感（测量失败，如实记录），不构成「压缩无损」的证据。
- 模型侧退化曲线（小物体/OCR 小字/透明软边界/遮挡重现的解耦曲线）:**NOT_MEASURED**——需官方权重 + GPU，本机不具备；脚本与适配器路径已就绪。

### EXP2 B15 物理可识别性（实验 2；命名：任务原文「U15 隐藏态」= B15，见序列一.2)
- 仓库自产 minimal pairs（摩擦边界 + 弹跳腔体，n=120 条轨迹），特征 = 质心轨迹（最强诚实 V0 可观测量）。
- 接触前特征：线性探针 0.400 / kNN 0.425（随机水平 0.5 附近）→ 可识别性边界按构造成立。
- 接触后特征：线性探针 **1.000** / kNN **0.425**——探针分歧如实记录：判别信号在轨迹的晚期分叉时序上，类原型均值将其抹平，零样本 kNN 在此电池上不充分；容量上限内的线性探针可解码。
- 外观对照（颜色/半径）:0.400 / 0.500 → 去相关控制通过。
- 真实主干（DINOv3/V-JEPA 2 vs SigLIP 2/Qwen3-VL):**NOT_MEASURED**（无权重/GPU）；探针协议机器本身已由本实验验证。

### EXP3 H1/H4/H5 记忆（实验 3,Equal-Byte,n=200/臂）
- 臂 A 长上下文（含补全写回）：召回 0.04，FP 污染率 0.96。
- 臂 B 循环隐状态摘要：召回 0.04，FP 污染率 0.96。
- 臂 C 双记忆 + 非对称门控（DualMemoryReplay)：召回 **1.00**,FP 污染率 **0.00**。
- 读数边界：A/B 内嵌的常速补全先验（+0.3/步）在 30 步遮挡后累积漂移 9.0 单位，使其连未篡改回合也错——本实验证明的是「补全写回会把错误先验以 96% 的比率固化为自信的假记忆，而门控在本合成域内消除之」，**不**是对真实长上下文模型的裁决（其补全先验质量不同，须以真实系统重测）。

### EXP4 H8/H9 硬实时（实验 4）
- 稠密臂：P50 0.074ms / P99 0.096ms，质心误差 0.0 px；事件臂：P50 0.074ms / P99 0.101ms，误差 0.0 px；事件稀疏率：239 事件 / 276,480 像素帧 = 8.6e-4。
- 裁决：48×48 合成尺度下两臂墙钟被 Python 开销主导，**本尺度不能判别 H8/H9**（如实记为 EV0 不结论）；稀疏率本身是真实测量。判别需真实分辨率/真实模型负载。

### EXP5 H15 / T6 状态剥夺（实验 5，合成形态，n=100/τ)
- 反应式成功率：τ=1 → 1.00；τ=4 → 0.16；τ=8 → 0.06；τ=16 → 0.02；τ=32 → 0.01。显式状态臂全程 1.00。
- 操作化定义下 τ_crit ∈ (1, 4]（记忆窗 w=4)：与 T6 预测形态一致的 EV0 曲线；真实策略（π₀.₅ 类）的 τ_crit **NOT_MEASURED**（无真机/权重）。

### 附带 EV0 读数（单元级，来自 tests 与模块自检）
- H6 级联回滚：合成反证例中依赖断言被正确降级（tests 通过）。
- H7 反见证定位：合成图（valve→pressure→flow）上单一见证解释全部异常（explained_fraction 1.0)。
- H12:ΔW 分解与 H14 不可逆取证拒绝在合成例上行为正确（tests 通过）。
- Joule/frame:**UNAVAILABLE**（本机无 NVML/powermetrics 采样），未伪造。

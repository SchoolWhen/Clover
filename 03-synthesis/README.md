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


---

## 综合产出（2026-11-02 序列五.2 填充）

### 1. 多维失败矩阵（禁止合并为单一平均分）

行 = 能力维（取自 01-research 电池 B1–B15 与槽位 U1–U20），列 = 路线。格内只记失败模式与证据出处；「—（无记录）」表示仓库尚无该格证据，不等于通过。

| 能力维 | R1 规模 SSL | R2 显式几何 | R3 预测世界模型 | R4 对象/可供性 | R5 主动视觉 | R6 语言/教师 | R7 反表征 |
|---|---|---|---|---|---|---|---|
| B1/B2 变化与事件切分 | 帧间特征可读出但无事件本体（02-analysis A9） | 几何变化可测，语义事件无 | 预测残差即事件信号（相对最强） | 以对象状态变化定义事件，本体依赖 | 由行动触发定义 | 语言切分≠视觉事件 | 无事件表示，行为切换即全部 |
| B4/B5 永久性与重现 | 静态特征无身份机制（路线表反证） | 几何位姿可重定位，语义身份另需监督 | 潜状态延续但补全可能幻觉写回 | SAM 3 提示锚定身份最强，但提示依赖 | 重定位为其强项（EgoReveal） | 语言重识别≠视觉同一性 | **结构性缺位**：遮挡时长超记忆窗口即无机制（T6 轴 1） |
| B9/B10 读出类 CV（检测/OCR） | 探针读出强（容量协议内） | 非其目标 | 非其目标 | 分割读出强 | 非其目标 | OCR/命名最强（L2 红利） | 策略内化读出，不可审计 |
| B11 度量与尺度 | 无尺度概念 | 相对几何强；**绝对尺度需锚点**（量纲定理二.2） | 潜空间无度量承诺 | 关系定性为主 | 可用行动标定（未联合建模） | 语言数字≠度量 | 行动标定隐含于策略，不可读出 |
| B13 因果与干预 | 相关特征，干预无机制 | 几何干预可仿真，物理参数不可识别 | **预测≠干预**（T3 靶点） | 可供性含准因果，未验 | 干预即观察（最接近） | 语言因果为先验复述 | 干预=行动本身，但无反事实 |
| B14 统一多能力一致性 | 单主干多读出（探针层统一） | 几何统一，语义外挂 | 潜状态统一，读出各异 | 本体统一，动力学外挂 | 任务碎片化 | 语言统一接口，视觉证据不统一 | 单策略统一，不可分解审计；另有等变/不变雅可比秩冲突（二.3）适用于一切单表征统一模型 |
| B15 隐藏态可识别性 | 探针可读出相关量，**不可识别部分无机制区分**（实验 2 判决） | 量纲定理给出不可识别边界（理论最强） | 同 R1，且补全倾向把不可识别填成确定值 | 本体外参数不在表示内 | 可设计判别行动（H14，未实现为通用机制） | 语言先验会给出答案——无论证据是否存在（危险项） | 行为可适应但不可报告不可识别性 |
| U9–U12 遮挡与未知 | 无 UNOBSERVED 概念 | 出视野=状态保持（可错） | 补全倾向（FP 写回风险最高） | 身份保持但位置可陈旧 | 主动再观察是正解路径 | 语言填补未知 | 无未知表示 |
| 长时一致性（U15 槽位） | 无 | SLAM 式漂移（Failure or Drift） | 长时预测发散 | 本体稳定、动力学漂移 | 任务内 | 上下文窗≠持久记忆（AGENTS §18） | **结构性缺位**（T6） |
| 硬实时/能耗（U16 类） | 大模型变体不达实时 | 中等 | 预测器成本随步长涨 | 数据引擎成本外部化，推理中等 | 行动成本未计入 | 教师成本外部化 | **最强**：亚秒闭环、无状态维护开销 |
| 失败可审计性 | 探针可审计 | 几何残差可审计 | 潜状态半可审计 | 掩码可审计 | 轨迹可审计 | 提示敏感、难审计 | **最弱**：无状态可审计，失败不可归因 |

### 2. Gap Map（满足本文件三条件：多强方法共享 / 解决有实质收益 / 无更简解法已证）

- **G1 认识论标签缺位**：全部七条路线都没有一等公民的 UNOBSERVED/REFUTED/MODEL_INCOMPLETE 输出（矩阵 U9–U12 行全线弱）。解决收益：幻觉写回与未知填补是当前系统性错误源（二.3 李雅普诺夫分析给出不稳定性证明形态）。无更简解法：置信度阈值不能区分「未观测」与「低置信观测」。
- **G2 不可识别性的显式表示**：量纲定理（二.2）证明纯视觉存在结构性不可识别域，但没有一条路线把「不可识别」做成可输出、可行动（触发 H14 取证行动）的状态。B15 全线弱。
- **G3 记忆的写回治理**：R3 的补全、R2 的地图更新、R4 的身份延续都存在写回通道，但无一路实现非对称门控+反证级联回滚（二.3 准则）；假阳性写回污染率从未被任何基准测量（本仓库 U9–U12 电池+实验 3 是首个测量设计）。
- **G4 等预算比较缺失**：跨路线比较从不控制 Equal-Byte/Latency/Joule（二.1/二.7）；Tier-2 训练路线的「能力」与 Tier-0 可复现性被系统性混报。
- **G5 干预级评测缺失**：T3 型干预后正确性只在 R5 附近被零星触及；预测基准（T2 型）无法区分 R3 与相关拟合。

### 3. 综合问题逐条回答（对应本文件 Synthesis questions）

1. **哪些问题已基本解决？** 受限域内的帧级读出（检测/分割/OCR/深度）在各自协议内已工程解决（A 组卡）；同数据下 SSL 追平图文（WebSSL）说明类别级语义不再独占于 L2。
2. **哪些能力跨家族普遍弱？** 永久性/重现的认识论处理、B15 可识别性边界、长时一致性、失败可审计性（见矩阵全线弱行）。
3. **哪些分歧只是术语差异？** 「世界模型」在 R3 指潜预测器、在 R2 指显式几何状态、在 R6 系统指语言先验+工具链——三者不在同一对象上竞争；「记忆」在 R3=上下文/潜状态延续、R2=地图、R7=隐状态，三者须按 S-MEM 定义拆开后才可比。
4. **哪些方法互补？** R2 几何 × R4 实体（几何给位姿、实体给身份）；R5 取证 × 任意状态路线（主动观察是 G2 的唯一已知缓解路径）；R1 特征 × 探针协议（读出层）。
5. **哪些权衡是根本性的？** ①补全能力 vs 写回污染（R3 越强、FP 写回风险越高，除非加门控——机制权衡非工程事故）；②表征统一 vs 等变/不变秩冲突（二.3，单表征内结构性）；③反应速度 vs 可审计状态（R7 vs 其余，T6 边界内为真权衡）；④绝对度量 vs 纯视觉（量纲定理，物理性不可逾越）。
6. **哪些结果重度依赖语言/特权/模拟/动作监督？** R6 全部（定义性依赖）；SAM 3 数据引擎（L1/L2）；R5 的特权训练；R3 的动作标签与模拟域；OCR 家族的 L1/L2（A5–A8）。
7. **哪些基准不能区分竞争假设？** 静态图像/短片基准不能区分 R1 vs R2/R3（T2 须遮挡/接触/再识别才有判别力）；预测基准不能区分 R3 vs 相关拟合（须 T3）；操作成功率不能区分 R7 vs 显式状态（须 T6 剥夺轴）。
8. **哪些直接策略系统挑战显式世界观的必要性？** π₀.₅/OpenVLA 类（R7）：在其任务分布内，显式状态未显示独立增益——这是 H15 必须接受的真实压力，裁决靠 T6 崩溃曲线而非立场。
9. **哪些生成系统挑战显式状态的必要性？** 生成式 4D/视频世界模型（R3 生成分支，如 Gen4P 类）：其挑战被二.4/AGENTS §25 限定——生成似真≠观测证据；只有在干预预测（T3）上胜出才构成真挑战，目前无此证据。
10. **哪些记忆失败挑战长上下文路线？** 长遮挡后身份/位置错误延续、冲突证据不触发修订（U9–U12 型失败），加上上下文窗的等字节比较从未做过（G4）——实验 3（Equal-Byte 长上下文 vs 显式节点）是直接判决设计。
11. **哪些因果结果表明交互是必要的？** 量纲定理的锚点清单（二.2）：质量/刚度类参数只有经接触/行动锚点才可识别——这是「交互必要性」目前唯一证明形态的论证（其余多为经验证据）。

### 4. 各路线在正交轴上的必然崩溃点（证据链）

- **R1**（轴：时间×身份）：静态特征无跨时身份机制是架构事实而非规模问题——加再多图像数据不产生遮挡后重现的因果结构；崩溃点 = B4/B5/U9–U12。证据链：路线表反证栏 + A9 卡探针协议（探针能读出的是相关量，B15 实验 2 将给出读数）。
- **R2**（轴：度量×物理）：量纲定理（二.2）证明其状态空间在 [M] 维度上结构性空白，几何自洽不蕴含物理正确；崩溃点 = 一切需要绝对质量/力/刚度的 B13/B15 任务。证据链：二.2 定理 + 锚点依赖清单 + R2 反证栏（DA3 批判注 2601.20303 等）。
- **R3**（轴：预测×干预）：预测目标对因果变量不敏感是目标函数事实——最小化预测误差的表征可以丢弃干预相关变量；崩溃点 = T3 干预后系统性错误 + FP 写回污染（G3）。证据链：causality 文档预测编码对齐表 + T3 判别矩阵预期栏。
- **R4**（轴：本体×动力学）：标签本体决定上限是监督来源事实——本体外的物理连续量（形变、内部状态）不在表示内，且可供性由人定义不可自展；崩溃点 = T5 本体外组合 + 接触动力学。证据链：A3/A10 卡 + 路线表反证栏。
- **R7**（轴：记忆×可审计）：无可解码状态 ⇒ 无对象永久性的独立载体、无失败归因面；崩溃点 = T6 三轴（遮挡时长/不可逆陷阱/工具动力学突变）临界点之外。证据链：二.5 T6 规约 + 本矩阵 R7 列。注意这是**边界**命题不是全域否定：边界内 R7 合法且更便宜，H15 按曲线裁决。

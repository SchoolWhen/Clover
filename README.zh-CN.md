# Clover

**开放研究：机器如何仅通过视觉理解真实世界？**

> **最高研究问题：** How can a machine understand the real world through vision alone?
>
> **长期成果目标：** 构造一个仅通过视觉形成真实世界理解，并能据此决策和行动的通用机器人大脑。

Clover 是一个长期公开研究项目。问题保持稳定，答案保持开放。仓库会分别记录当前事实、研究假设、架构、开放问题与实验，使项目能够随着认识更新而重构，而不抹去研究历史。

## 我们真正研究什么

Clover 不以某一个 benchmark、CPU 路线、Transformer 对立面或某一种既有架构为目标。我们研究的是：机器仅凭视觉经验，需要形成什么内部结构，才能理解世界中的持续性、身份、空间、时间、动力学、因果、不确定性与变化，并把这种理解用于决策和行动。

## 最终落点

```text
视觉
 ↓
Worldview
 ↓
Decision
 ↓
Tool Use
 ↓
Execution
 ↓
新的视觉观测
 └──────────────→ Worldview
```

这只是当前系统级划分，不意味着内部表示已经冻结。

## 我们不预设

Clover 不预设：

- CPU 一定优于 GPU；
- 显式表示一定优于 latent 表示；
- 场结晶一定是最终 world representation；
- Transformer 天然不适合理解世界；
- 一个 benchmark 可以定义“理解”；
- 当前 Clover 架构就是最终答案。

硬件、表示和学习方法都必须交给研究、比较与证伪来决定。

## 当前阶段

2026-10-14 的 Research Reset 将项目从“证明既有架构”调整为“先研究问题，再决定答案”。当前首先建设公开研究基础、研究地图、开放问题与当前状态记录。已有 Clover 实现作为 **Research Prototype 1** 保留，后续在完成公开仓库安全与文档审查后同步代码。

更多内容见：

- [PRINCIPLES.md](PRINCIPLES.md)
- [STATUS.md](STATUS.md)
- [ROADMAP.md](ROADMAP.md)
- [研究问题](docs/research-question.md)
- [研究地图](docs/research-map/README.md)
- [开放问题](docs/open-questions.md)

**问题是稳定的，答案是开放的。**

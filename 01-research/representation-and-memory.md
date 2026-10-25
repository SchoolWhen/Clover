<a id="top"></a>

# 调研方向：世界状态、表示、记忆与压缩

Maintained: **2026-10-25** · Document stage: **1 — Research** ([status](../STATUS.md)).

Sufficiency, aliasing, abstraction, temporal persistence and diagnostics. No representation family is selected.

This is the canonical topic document. Update it in place; source-level dates and reading-depth labels below qualify the evidence, not the maintenance date.

<a id="compression-evidence"></a>

## 2026-10-25 当前补充：视觉压缩与未来证据保留

### FastV：必须把 FLOPs、时延和配置对应起来

- **来源：** Liang Chen 等，*An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models*，ECCV 2024。[论文 v3](https://arxiv.org/abs/2403.06764v3) · [核读正文](https://arxiv.org/html/2403.06764v3) · [官方代码](https://github.com/pkunlp-icler/FastV)。`PRIMARY_PAPER` / `OPEN_SOURCE`。
- **实际证据：** 按早期注意力评分删减后层视觉 tokens。`K=2,R=50%` 的约 45% FLOPs 降低是复杂度/任务质量结果；正文表 4 的实测时延使用 `K=0,R=50%`，不是同一配置。其 LLaVA-1.5-13B 在 A40、A-OKVQA 的逐例时延从 `0.539s` 到 `0.341s`，分数从 `82.0` 到 `80.5`；这是作者结果，不是本机 P50/P95。
- **观测与学习来源：** 图片/视频 QA 的 RGB 输入接近 `V0`，但还输入问题文本；已有 VLM 骨干含 `L2`，删 token 不会消除原有语言/视觉监督。不能写成 vision-only learning。
- **没有证明：** 当前问题的平均分保留意味着未来未知任务、短暂接触、身份切换或证据纠错仍受支持。核读摘要、§4.2、§5 及表 1/4；未复核全部附录或运行代码。

### FrameFusion：已有检索对照，但仍不等于可恢复性保证

- **来源：** Tianyu Fu 等，*FrameFusion: Combining Similarity and Importance for Video Token Reduction on Large Vision Language Models*，ICCV 2025，22654–22663。[论文 v2](https://arxiv.org/abs/2501.01986v2) · [核读正文](https://arxiv.org/html/2501.01986) · [官方代码](https://github.com/thu-nics/FrameFusion)。`PRIMARY_PAPER` / `OPEN_SOURCE`。
- **实际证据：** 早层合并相邻帧对应位置的相似 token，深层再按重要性裁剪；五项视频检索/QA/时空理解基准包含 VideoNIAH，可作为细节保留的现成对照。
- **预算与时延：** 相对 token budget 定义为层平均的 KV 序列长度；`30%` 预算不是每层或每帧都删去完全相同的 `70%`。v2 正文 §5.4 报告 `1.6–3.6×` 端到端加速，测试使用 NVIDIA A100-80GB，按模型规模使用一或多卡；不能迁移成 M4 的实测速率。代码 README 的端到端范围与论文 v2 不同，引用数值须固定版本。
- **观测与学习来源：** RGB 视频加问题文本，部分 VideoMME 条件另有字幕；骨干的语言/视觉训练来源含 `L2`。这些系统证据不能算严格 `V0/L0` 学习。
- **没有证明：** 跨任务延迟提问、反事实干预或被删证据的恢复。核读 §5.1、§5.3–5.4 与代码说明；未完整复核全文、全部附录或运行代码。

## Contents

- [Minimum Sufficient World State](#topic-research-research_sufficient_state)
- [State Aliasing and Representation Failure](#topic-research-research_state_aliasing)
- [Adaptive Abstraction, State Granularity and Multi-Timescale Structure](#topic-research-research_adaptive_abstraction)
- [R-C — Representation: Explicit, Distributed, Object-Centric or Hybrid?](#topic-research-dossiers-r-c-representation)
- [R-D — Persistence, Memory and Belief Revision](#topic-research-dossiers-r-d-memory-persistence)
- [Learned Visual Representations](#topic-docs-research-map-learned-visual-representations)
- [Object-Centric Representation](#topic-docs-research-map-object-centric-representation)
- [Video Representation and World Models](#topic-docs-research-map-video-world-models)
- [Stage-1 Emerging Audit — Representation Diagnostics and Causal Use](#topic-research-emerging-representation_diagnostics_2026-10-15)

<a id="topic-research-research_sufficient_state"></a>

## Minimum Sufficient World State

Source record updated: 2026-10-14
Source intake checked through: **2026-10-14**

> **Research question:** How can a machine understand the real world through vision alone?

This is a Stage-1 theory/background document. It does **not** propose a Clover architecture.

Its purpose is to study a second foundational question:

> Even if the real world contains many variables, which information must an embodied agent actually retain for prediction, planning, control, memory, revision and generalization?

The central distinction is:

```text
complete physical description
≠
minimal predictive state
≠
minimal control-sufficient state
≠
general-purpose world state.
```

"Minimal" is meaningful only relative to what the state must support.

---

### 1. History, state and compression

Let the interaction history be:

```text
H_t = (O_1, A_1, O_2, A_2, ... , O_t)
```

and let an internal representation be:

```text
Z_t = F(H_t).
```

The representation is useful only if it preserves the information required by future queries/actions while discarding information that can safely be ignored.

A generic design question is:

```text
How much of H_t must Z_t preserve?
```

A second question is:

```text
Preserve it for what purpose?
```

Those two questions define the sufficient-state problem.

---

### 2. Different notions of sufficiency

Stage 1 should not use the word "sufficient" without specifying the target.

#### 2.1 Predictive sufficiency

For future observations/outcomes `Y`, a representation is predictively sufficient when, conceptually:

```text
P(Y_future | H_t, A_future)
=
P(Y_future | Z_t, A_future).
```

`Z_t` then preserves what the history contributes to the chosen prediction problem.

This does **not** automatically imply that the representation is sufficient for reward, planning, intervention or belief revision.

#### 2.2 Control sufficiency

For a task/reward family, state is control-sufficient if the optimal decision need not access information discarded from history.

Conceptually:

```text
Q*(H_t, a) = Q*(Z_t, a)
```

for relevant actions/tasks.

A representation can be excellent for reconstruction while discarding small task-relevant distinctions, or highly control-sufficient while discarding appearance details.

#### 2.3 Planning sufficiency

Planning needs enough state to predict the consequences of candidate actions and compare possible futures.

This can differ from one-step policy sufficiency.

#### 2.4 Memory / revision sufficiency

A representation can be sufficient for the current task but insufficient when:

```text
an object leaves view
the world changes
a new query is asked later
old evidence must be reinterpreted
```

Long-term robotic state may therefore need to preserve evidence or uncertainty that a short-horizon policy would safely discard.

#### 2.5 Causal / counterfactual sufficiency

Prediction under the observed behavior distribution may not preserve the variables needed for unseen interventions.

A state sufficient for:

```text
What usually happens next?
```

may fail for:

```text
What would happen if I intervene differently?
```

#### 2.6 Open-world / multi-task sufficiency

A state optimized for one fixed reward can aggressively discard information irrelevant to that task.

A general-purpose robot is different: future tasks may be unknown when the representation is formed.

Therefore:

```text
task-specific minimality
```

and:

```text
general-purpose minimality
```

should be treated as distinct research problems.

---

### 3. POMDP belief state: a canonical sufficient statistic under a known model

Background survey:

- Partially Observable Markov Decision Processes in Robotics — https://arxiv.org/abs/2209.10342

In a POMDP, the true state is hidden and the agent maintains a belief:

```text
b_t(s) = P(S_t = s | H_t).
```

Given the assumed transition/observation model, the belief state is a sufficient statistic of the observation-action history for optimal decision making.

Why it matters for Clover:

The belief-state view makes several distinctions explicit:

```text
world state S_t
≠
observation O_t
≠
belief b_t.
```

But it also exposes a practical problem:

- the true state variables may not be known in advance;
- the transition model may be wrong;
- the belief can be high dimensional;
- open-world robotics cannot assume a fully specified finite hidden-state model.

So POMDPs are a theoretical anchor, not a ready-made Clover representation.

---

### 4. Predictive State Representations: state as predictions rather than hidden variables

Foundational source:

- Littman, Sutton, Singh, **Predictive Representations of State** — https://papers.nips.cc/paper_files/paper/2001/hash/1e4d36177d71bbb3558e43af9577d70e-Abstract.html
- Paper PDF — https://proceedings.neurips.cc/paper/2001/file/1e4d36177d71bbb3558e43af9577d70e-Paper.pdf

Predictive State Representations (PSRs) represent state using predictions of future observation outcomes under possible action sequences.

Conceptually:

```text
state
=
a sufficient set of predictions about future observable tests.
```

This is important because it challenges the assumption that useful world state must correspond to a hand-specified set of hidden physical variables.

Related work:

- A Nonlinear Predictive State Representation — https://papers.nips.cc/paper_files/paper/2003/hash/72e6d3238361fe70f22fb0ac624a7072-Abstract.html
- Efficient Learning and Planning with Compressed Predictive States — https://jmlr.org/papers/v15/hamilton14a.html

Stage-1 question:

> Could a sufficiently rich action-conditional predictive representation serve as machine world state without reconstructing all latent physical variables explicitly?

Counter-question:

> Does predictive sufficiency under learned tests preserve persistence, causal intervention and open-ended future-task information?

---

### 5. Information state and Approximate Information State

Primary theory reference:

- Approximate Information State for Approximate Planning and Reinforcement Learning in Partially Observed Systems — https://www.jmlr.org/beta/papers/v23/20-1165.html
- Code metadata — https://github.com/info-structures/ais

This work defines information state as a function of history that is sufficient for dynamic programming, including formulations based on predicting reward and the next information/observation state.

Approximate Information State (AIS) relaxes exact sufficiency and provides bounds relating approximation error to loss of optimality.

This is highly relevant to realistic robotics because exact sufficient statistics may be too expensive or impossible to learn.

Stage-1 implication:

```text
perfect world-state recovery
```

may not be necessary if an approximate compressed state preserves the information needed for near-optimal action.

But the approximation target must be explicit.

---

### 6. State abstraction / bisimulation: discard distinctions that do not matter for control

Control representation literature often asks when two states may be treated as equivalent.

A bisimulation-style intuition is:

```text
states can be merged when
rewards are equivalent
and
future transition behavior is equivalent
under relevant actions.
```

Recent example:

- Revisiting Bisimulation Metric for Robust Representations in Reinforcement Learning — https://arxiv.org/abs/2507.18519

Important theoretical caution:

- Which Mutual-Information Representation Learning Objectives are Sufficient for Control? — https://arxiv.org/abs/2106.07278

That work formally studies control sufficiency and shows that some intuitive mutual-information objectives can still learn insufficient representations.

Stage-1 implication:

> Compression quality should be judged by preserved decision structure, not merely reconstruction, contrastive loss or mutual information.

---

### 7. Detecting when a learned representation is not Markov enough

**Mitigating Partial Observability in Sequential Decision Processes via the Lambda Discrepancy**
NeurIPS 2024: https://proceedings.neurips.cc/paper_files/paper/2024/hash/73073ccb3bc559fd001e66b9079d6d5e-Abstract-Conference.html

The work introduces a discrepancy between temporal-difference estimators with different `lambda` values as a diagnostic of non-Markovian state representations under partial observability.

Why it matters:

A representation may look compact and semantically meaningful yet still omit historical information necessary to make the future conditionally depend only on the current representation.

This suggests a useful later Clover diagnostic:

```text
Does adding more past history still improve prediction/value after conditioning on Z_t?
```

If yes, `Z_t` may not yet be a sufficient state for the measured task.

---

### 8. 2026 world-model research is converging on sufficiency as a design question

#### 8.1 Latent State Design for World Models under Sufficiency Constraints

Primary paper: https://arxiv.org/abs/2605.01694
Evidence: `PRIMARY_PAPER`

The paper explicitly frames world-model research as designing latent state under functional sufficiency constraints.

It distinguishes roles such as:

```text
predictive embedding
recurrent belief state
object / causal structure
latent action interface
grounded planning interface
memory substrate
```

and emphasizes that predictive sufficiency, control sufficiency, planning, memory and counterfactual support are not interchangeable objectives.

This is directly aligned with the current Clover Stage-1 question.

#### 8.2 DELE-w0.5: future latent state instead of dense video

**Inferring Action from Future Latent State for Robotic Manipulation**
Primary paper: https://arxiv.org/abs/2608.22067

DELE argues that generating all intermediate future pixels is an unnecessarily expensive target for manipulation and instead predicts a compact future latent state representing the action-relevant physical outcome.

Research contrast:

```text
pixel-trajectory prediction
vs
action-relevant future-state prediction.
```

This is strong evidence that a world model need not reproduce every visual detail to be useful for control.

But it does not establish that the compact latent is sufficient for arbitrary future tasks, persistent memory or counterfactual reasoning.

#### 8.3 Representation World Model

**Representation World Model: Learning States, Transition and Executable Plans in Representation**
Primary paper: https://arxiv.org/abs/2609.29171

RWM learns representation geometry such that latent paths between endpoint representations preserve enough transition structure for inverse dynamics to recover executable actions.

Research hypothesis:

```text
planning-relevant geometry can live directly inside representation space.
```

Again, this is planning/control sufficiency evidence, not proof of complete world understanding.

---

### 9. Dense video generation may preserve too much information — or the wrong information

Video-generation world models attempt to preserve rich visual detail.

That may be useful because future tasks are not always known.

But it is expensive and can allocate capacity to visually salient properties that are irrelevant to action.

The key trade-off is:

```text
retain all visual detail
→ flexible but expensive / hallucination-prone

retain task-relevant compact state
→ efficient but risks discarding information needed later.
```

Stage 1 should keep both possibilities open.

Relevant comparison sources:

- World-Action Models survey — https://arxiv.org/abs/2609.16074
- DELE-w0.5 — https://arxiv.org/abs/2608.22067
- Representation World Model — https://arxiv.org/abs/2609.29171
- Riemann-1.0 — https://arxiv.org/abs/2608.27033
- HWAM — https://arxiv.org/abs/2610.12026

---

### 10. A proposed Stage-1 sufficiency taxonomy

For later Analysis, label what a representation is intended to preserve.

```text
S-PRED   predictive sufficiency
S-CTRL   control sufficiency
S-PLAN   planning sufficiency
S-MEM    long-horizon memory / revision sufficiency
S-CAUSE  intervention / counterfactual sufficiency
S-EPI    uncertainty / belief sufficiency
S-OPEN   open-world / future-task sufficiency
```

A method can satisfy one without satisfying the others.

Example:

```text
strong S-PRED
weak S-EPI
```

could describe a generative future model that predicts plausible futures but cannot represent what is genuinely unknown.

Likewise:

```text
strong S-CTRL for task A
weak S-OPEN
```

could describe a highly compressed task-specific policy state.

This taxonomy is only a research annotation scheme; it is not a Clover architecture.

---

### 11. Why general-purpose robotics makes "minimal" difficult

Suppose a robot only needs to place a cup on a table.

It may not need:

```text
cup brand
exact texture
thermal state
internal liquid composition
```

But the same robot may later receive:

```text
Is this cup too hot to touch?
Pour exactly 100 ml.
Use the unbroken ceramic cup, not the plastic one.
Check whether the liquid changed color overnight.
```

Information that was irrelevant to one task can become relevant later.

Therefore a general-purpose robotic brain faces a fundamental tension:

```text
compression / efficiency
vs
future-task optionality.
```

Possible research solutions include, without endorsement:

```text
rich persistent world state
+
small task-conditioned working state

raw/selective evidence memory
+
compressed current belief

hierarchical state at multiple resolutions

dynamic state expansion when a new task requires more detail
```

These are possibilities to study later, not Stage-1 conclusions.

---

### 12. Evidence retention may solve part of the minimality problem

If the online decision state is compressed, the system could still retain selected evidence for later reinterpretation.

This separates:

```text
what must be in the current decision state
```

from:

```text
what evidence should remain recoverable.
```

This is relevant to:

- S-EMBER — https://arxiv.org/abs/2607.02689
- VISTA — https://arxiv.org/abs/2610.02200
- PersistBench — https://arxiv.org/abs/2609.20819

Historical Clover Evidence Replay ideas belong in Stage 4 Innovation; these external results only establish that persistent evidence/memory is an independent research dimension.

---

### 13. Proposed later diagnostics for representation sufficiency

Stage 2/6 should eventually test sufficiency directly rather than infer it from one benchmark score.

#### 13.1 History leakage / Markov test

Ask whether prediction/control improves after giving the downstream model extra history beyond `Z_t`.

If yes, the state omitted useful information.

#### 13.2 State aliasing counterexamples

Find two histories:

```text
H_a != H_b
```

that map to nearly the same representation:

```text
Z(H_a) ≈ Z(H_b)
```

but require different future predictions/actions.

This directly exposes insufficient compression.

#### 13.3 Task-transfer sufficiency

Freeze the state representation and introduce a new downstream task.

Measure whether relevant information was retained before the task was known.

#### 13.4 Intervention sufficiency

Test matched histories under different controlled interventions.

A state may be prediction-sufficient on observational data yet intervention-insufficient.

#### 13.5 Memory/revision sufficiency

After long occlusion or external world change, test whether state plus retained memory supports correct revision.

#### 13.6 Uncertainty sufficiency

Two representations may achieve similar accuracy but differ in whether they preserve the distinction between:

```text
known absent
vs
unobserved
vs
ambiguous.
```

#### 13.7 Action-efficiency Pareto curve

Measure:

```text
state bytes / latent dimension / memory cost
vs
task success / prediction / planning quality.
```

The objective should be a Pareto frontier, not smallest latent dimension at any cost.

---

### 14. Open research questions

1. Is there a task-independent finite-dimensional sufficient state for open-world robotics in practice?
2. Should general-purpose world state optimize future-task optionality instead of minimum dimension?
3. Can PSR-style action-conditional predictions scale to high-dimensional open visual worlds?
4. When is belief over explicit variables better than a distributed latent predictive state?
5. How can a learned representation expose when it is not Markov/sufficient?
6. Which state dimensions should be persistent versus reconstructed on demand from stored evidence?
7. Can a compact future latent support counterfactual planning, not only behavior-distribution actions?
8. How much information does dense video generation preserve that compact WAM states later turn out to need?
9. Can representation granularity adapt to task requirements without catastrophic loss of previously useful distinctions?
10. Is the best robotic state a single vector at all, or a collection of differently scoped state/memory structures?

---

### Stage-1 provisional conclusion

The research target should not be:

```text
recover every physically meaningful variable at maximum precision.
```

Nor should it be:

```text
compress observations as aggressively as possible.
```

A better research question is:

> What information must the machine preserve so that its internal state remains sufficient for the family of predictions, decisions, interventions, memories and future tasks that define general robotic intelligence?

This reframes world-model design as a question of **sufficiency under partial observability**, not simply latent dimensionality or reconstruction fidelity.

**Keep the answer open until Stage 2/3 compare the competing sufficiency hypotheses.**

---

<a id="topic-research-research_state_aliasing"></a>

## State Aliasing and Representation Failure

Source record updated: 2026-10-14

> **Research question:** How can a machine understand the real world through vision alone?

This is a Stage-1 research document. It does **not** propose a Clover architecture.

Its purpose is to study a failure mode that can remain hidden even when a learned representation looks compact, predictive or useful on average:

> Two physically or decision-relevantly different world histories may be mapped to the same internal state.

That failure is called **state aliasing** or **perceptual aliasing** in different literatures.

---

### 1. Minimal formulation

Let the history available to the agent be

```text
H_t = (O_1, A_1, O_2, ..., O_t)
```

and let a learned state encoder construct

```text
Z_t = F(H_t).
```

Aliasing occurs when two histories

```text
H_t^a ≠ H_t^b
```

map to approximately the same internal state

```text
F(H_t^a) ≈ F(H_t^b)
```

although they differ in something that matters for a required future function, for example:

```text
future observation distribution
action consequence
reward/value
object identity
hidden physical parameter
causal response
uncertainty
correct information-gathering action
```

The key point is task dependence:

```text
same latent state may be sufficient for task A
but aliased for task B.
```

State aliasing is therefore directly connected to [`representation-and-memory.md`](#topic-research-research_sufficient_state).

---

### 2. Historical active-perception definition

**Learning to Perceive and Act by Trial and Error / Active Perception and Reinforcement Learning**
Primary/background source: https://doi.org/10.1023/A:1022619109594
Conference version: https://doi.org/10.1016/B978-1-55860-141-3.50025
Evidence: `BACKGROUND_REFERENCE`

Whitehead and Ballard explicitly describe perceptual aliasing as a consequence of an internal representation that confounds external world states and show why this can destabilize decision learning.

The historical relevance for Clover is strong:

```text
representation failure
can create the need for
active information collection.
```

The agent may need to look again, move, or otherwise collect discriminating evidence before acting.

---

### 3. Markov-state failure can be detected without seeing true hidden state

#### λ-discrepancy

**Mitigating Partial Observability in Sequential Decision Processes via the Lambda Discrepancy**
NeurIPS 2024: https://papers.nips.cc/paper_files/paper/2024/hash/73073ccb3bc559fd001e66b9079d6d5e-Abstract-Conference.html
ArXiv: https://arxiv.org/abs/2407.07333
Project: https://lambda-discrepancy.github.io/
Evidence: `PRIMARY_PAPER`

The paper introduces the λ-discrepancy between temporal-difference estimates with different λ values. Because TD(0) assumes a Markov state while TD(1) can retain longer temporal dependence, disagreement is used as a signal that the current representation is non-Markovian.

Stage-1 interpretation:

```text
if giving the learner more history changes the correct value estimate,
the current state representation has discarded decision-relevant history.
```

This is useful because it does not require direct access to the true hidden state.

What it does **not** establish:

- that zero λ-discrepancy proves universal world understanding;
- that the representation is sufficient for every downstream task;
- that the missing variable is physically interpretable;
- that the learned memory is optimal for open-world transfer.

---

### 4. Partial observability can be discovered from visual inconsistency

#### PO-PDDL

**PO-PDDL: Learning Symbolic POMDPs from Visual Demonstrations for Robot Planning Under Uncertainty**
Primary paper: https://arxiv.org/abs/2606.15654
Evidence: `PRIMARY_PAPER`

PO-PDDL reconstructs latent symbolic state trajectories from real-robot execution videos and identifies partial observability through inconsistencies between inferred symbolic state and visible observations. It then learns stochastic transition and observation models for belief-space planning.

Why it matters:

This is a structured example of treating aliasing as a model mismatch:

```text
current visual observation
is insufficient to decide
which latent symbolic state is true.
```

It provides a useful explicit-state baseline even if Clover later uses a very different representation.

---

### 5. Observable equivalence is not the same as physical equality

#### Observable quotient world models

**Observable quotient world models for knowledge-state abstraction under partial observability**
Journal page: https://www.sciencedirect.com/science/article/pii/S0950705126014942
DOI: https://doi.org/10.1016/j.knosys.2026.116768
Evidence: `PRIMARY_PAPER`

This 2026 work defines quotients from action-conditioned observation laws, builds quotient beliefs/filtering/dynamics and explicitly studies which world distinctions are supported by observation.

Stage-1 value:

It sharpens an important distinction:

```text
physically different states
may be observationally equivalent
under the current sensor/action protocol.
```

A world representation should not be punished for failing to distinguish states that the available evidence cannot distinguish. Instead it should preserve uncertainty or equivalence until new evidence breaks the tie.

---

### 6. Bisimulation gives a behavior-based abstraction criterion

#### Classical/control representation perspective

**Invariant Representations for Reinforcement Learning without Reconstruction**
OpenReview: https://openreview.net/forum?id=kmaPnFKCuq
Evidence: `PRIMARY_PAPER`

Bisimulation-based representation learning groups states when they have equivalent reward and transition behavior, deliberately removing visually different but behaviorally irrelevant information.

#### 2026 state-abstraction theory

**Compositional Behavioral Semantics for State Abstraction in Reinforcement Learning**
PMLR: https://proceedings.mlr.press/v306/zhang26dy.html
ArXiv: https://arxiv.org/abs/2606.25357
Evidence: `PRIMARY_PAPER`

This work develops a general framework for reasoning about what behavioral properties are preserved under abstraction, including invariants, bisimulation relations and behavioral metrics.

#### 2026 visual bisimulation geometry

**PAMD: Structured Adaptive Distances for Bisimulation Representations in Visual Reinforcement Learning**
PMLR: https://proceedings.mlr.press/v306/roh26a.html
Evidence: `PRIMARY_PAPER`

PAMD shows that even after choosing bisimulation as the abstraction principle, the metric used to compare latent states matters: fixed global norms can be too restrictive, while unconstrained distances can become degenerate.

Stage-1 implication:

```text
abstraction criterion
and
latent geometry
are separate research choices.
```

---

### 7. Aliasing taxonomy for Clover research

Stage 1 should distinguish at least:

#### A1 — perceptual aliasing

Different external states produce similar/currently indistinguishable visual observations.

Examples:

```text
occluded object present vs removed
same-looking containers with different contents
same surface appearance with different friction
```

#### A2 — history aliasing

The current frame is the same, but different histories imply different correct beliefs.

Examples:

```text
object was moved while previously visible
switch was toggled earlier
container was filled earlier
```

#### A3 — representation aliasing

The observation/history contains the information, but the learned encoder discards it.

#### A4 — action aliasing

Different embodiments/controllers map numerically similar actions to different physical consequences.

Related source: SyncWorld — https://arxiv.org/abs/2609.09155

#### A5 — causal aliasing

Two states look similar under passive observation but respond differently to intervention.

#### A6 — task aliasing

A representation deliberately merges states because they are equivalent for the current task, although another future task would need the distinction.

This is not necessarily an error; it becomes an error when the task distribution changes.

---

### 8. Candidate diagnostics for later stages

Stage 1 records these only as future evaluation ideas.

#### Diagnostic D-A1 — history-rescue test

```text
performance with Z_t
vs
performance with Z_t + additional history
```

If history reliably improves the relevant prediction/control query, `Z_t` is not sufficient for that function.

#### Diagnostic D-A2 — intervention split

Construct two histories that are visually similar now but differ in hidden causal state. Apply the same probe action and measure whether predicted outcomes diverge correctly.

#### Diagnostic D-A3 — counterfactual nearest neighbors

Search latent nearest neighbors for states with different valid action consequences. High collision rate indicates action-relevant aliasing.

#### Diagnostic D-A4 — belief calibration under unresolved aliases

When two worlds remain observationally compatible, measure whether the model preserves uncertainty rather than collapsing to one guess.

#### Diagnostic D-A5 — task transfer after compression

Train/construct a compact state for task A, then evaluate whether task B exposes information that the representation irreversibly discarded.

---

### 9. Adjacent gaps discovered

State aliasing connects directly to several additional Stage-1 areas:

```text
structured memory
multi-timescale dynamics
belief-state calibration
non-stationarity / world change
active information gathering
open-world task transfer
```

Important 2026 references include:

- Flow Equivariant World Models — https://proceedings.mlr.press/v306/lillemark26a.html — structured latent memory aligned with self-motion/external motion under partial observability.
- HiMe — https://proceedings.mlr.press/v306/ji26k.html — hierarchical working/long-term memory for non-Markovian long-horizon VLA tasks.
- OASIS-Map — https://arxiv.org/abs/2607.14899 — world change across sessions.
- R4DSG — https://arxiv.org/abs/2608.11017 — persistent relative 4D object/change memory.

---

### 10. Stage-1 questions

```text
When do two physically different worlds become observationally indistinguishable?
When is that ambiguity removable by history?
When is it removable only by action?
When does a learned representation discard information that was actually available?
Which state distinctions are necessary for prediction, action, memory, causality and open-world transfer?
Can we detect aliasing without privileged ground-truth state?
How should a system represent unresolved aliases: one latent point, a distribution, a set, particles, hypotheses, or something else?
```

---

### Current rule

Do not demand that a representation distinguish states that the available evidence cannot distinguish.

Do demand that it avoid collapsing states that differ in a capability the system claims to support.

```text
indistinguishable from available evidence
≠
representation failure

information was available but discarded
=
potential representation failure
```

---

<a id="topic-research-research_adaptive_abstraction"></a>

## Adaptive Abstraction, State Granularity and Multi-Timescale Structure

Source record updated: 2026-10-14

> **Research question:** How can a machine understand the real world through vision alone?

This is a Stage-1 research document. It does **not** propose a Clover architecture.

Its purpose is to study whether a robotic world representation should use one fixed state granularity, or adapt what it preserves according to task, timescale, uncertainty, embodiment and interaction phase.

---

### 1. Core problem

The physical world contains far more state than any robot can represent at maximum detail all the time.

A useful abstraction must therefore answer:

```text
What can be safely compressed?
What must remain explicit?
What should be coarse now but refined later?
Which distinctions matter only for the current task?
Which distinctions must survive because future tasks are unknown?
```

The central tension is:

```text
compression / efficiency
vs
preserving future-relevant distinctions.
```

---

### 2. Task-specific abstraction is not automatically universal understanding

#### Causal Bisimulation Modeling

**Building Minimal and Reusable Causal State Abstractions for Reinforcement Learning**
AAAI 2024: https://ojs.aaai.org/index.php/AAAI/article/view/29507
Evidence: `PRIMARY_PAPER`

CBM learns causal dependencies in dynamics/rewards and derives minimal task-specific abstractions that keep variables needed for each task.

Why it matters:

It demonstrates a legitimate use of selective state:

```text
full environment state
→ task-conditioned subset
```

But it also exposes a Clover risk:

```text
minimal for current task
≠
sufficient for future unknown task.
```

---

### 3. State abstraction needs preservation guarantees

#### Compositional Behavioral Semantics

**Compositional Behavioral Semantics for State Abstraction in Reinforcement Learning**
PMLR: https://proceedings.mlr.press/v306/zhang26dy.html
ArXiv: https://arxiv.org/abs/2606.25357
Evidence: `PRIMARY_PAPER`

This ICML 2026 work studies what behavioral structures are provably preserved when a concrete system is mapped into an abstraction.

Relevant preserved structures include:

```text
values
invariants
bisimulation-like relations
behavioral metrics
```

Stage-1 implication:

A representation should not be called “good abstraction” only because it is small or visually invariant. We need to specify **what property is promised to survive the abstraction**.

---

### 4. Multi-timescale state is a serious alternative to one-resolution state

#### Temporally hierarchical active-inference world model

**Real-World Robot Control by Deep Active Inference With a Temporally Hierarchical World Model**
Primary paper: https://arxiv.org/abs/2512.01924
Evidence: `PRIMARY_PAPER`

The system models dynamics at slow and fast timescales and compresses action sequences into abstract actions. Its abstract world model predicts slower future states for tractable action selection.

Research question:

```text
Should fast contact/motion state
and slow task/world state
live at different temporal resolutions?
```

#### S2-HWM

**S2-HWM: Sparse Event-Structured Hierarchical World Model for Long-Horizon Surgical Robot Manipulation**
Primary paper: https://arxiv.org/abs/2608.13103
Evidence: `PRIMARY_PAPER`

S2-HWM learns sparse event evidence and separates event-level manager updates from primitive-step control. Event transitions have variable duration rather than a fixed clock rate.

Why it matters:

```text
physical time step
≠
meaningful world-state update event.
```

Some state should be updated continuously; other state may only need revision when a contact, subgoal, topology change or semantic event occurs.

---

### 5. Hierarchical world state can mix symbolic and perceptual levels

#### H-WM

**H-WM: Robotic Task and Motion Planning Guided by Hierarchical World Model**
Primary paper: https://arxiv.org/abs/2602.11291
Evidence: `PRIMARY_PAPER`

H-WM jointly predicts high-level logical state transitions and low-level visual state transitions.

This provides a useful counter-hypothesis to a single homogeneous latent state:

```text
logical / relational state
+
visual / geometric state
```

may be maintained at different abstraction levels.

What it does **not** establish:

- that symbolic state is necessary for general robotics;
- that the chosen predicates are open-world sufficient;
- that one fixed hierarchy transfers to arbitrary tasks.

---

### 6. Hierarchical memory can be organized by operating timescale

#### HiMe

**HiMe: Hierarchical Embodied Memory for Long-Horizon Vision-Language-Action Control**
PMLR: https://proceedings.mlr.press/v306/ji26k.html
Evidence: `PRIMARY_PAPER`

HiMe separates a high-frequency executor, a working-memory sentry and a long-term planner, and supports Add/Update/Delete memory operations.

Stage-1 relevance:

It suggests that **state access frequency** may itself be an abstraction variable:

```text
high-frequency motor-relevant state
working state
long-horizon episodic/semantic state
```

This is related to, but distinct from, representational granularity.

---

### 7. Structured equivariance can preserve detail without storing it naively

#### Flow Equivariant World Models

**Flow Equivariant World Models: Structured Memory for Dynamic Environments**
PMLR: https://proceedings.mlr.press/v306/lillemark26a.html
Project: https://flowequivariantworldmodels.github.io/
Evidence: `PRIMARY_PAPER`

This work builds latent memory that transforms equivariantly with self-motion and inferred object motion, so out-of-view information remains aligned as the observer/world moves.

Why it matters:

Adaptive abstraction is not only about deleting information. Another strategy is to encode known transformation structure so the same information can be maintained more efficiently and consistently.

---

### 8. Task semantics may determine which relations deserve explicit representation

#### Semantically Rich World Models

**Beyond Instance Slots: Semantically Rich World Models for Physical Interaction Planning**
Official project/publication page: https://www.max-robotics.com/en/research/publications/cmu42t6js00r9pd42avv37dcb
Evidence: `PRIMARY_PAPER` / `OFFICIAL_PROJECT`

The method structures planning state around functional roles such as gripper, target, goal, relation and phase rather than only generic object identity.

Stage-1 implication:

```text
entity identity
alone may be too fine in one way
and too weak in another.
```

The abstraction required for planning may be role- and task-conditioned.

---

### 9. Hierarchy can also operate over subgoals

#### ViGAR

**Rethinking World-Action Model for Compositional and In-Context Robotic Manipulation**
Primary paper: https://arxiv.org/abs/2610.02368
Evidence: `PRIMARY_PAPER`

ViGAR separates a visual subgoal planner from a subgoal executor, using a shared pretrained world-model representation.

This is not necessarily a world-state hierarchy, but it matters because state granularity and action horizon are coupled:

```text
primitive action horizon
subtask horizon
full-task horizon
```

may require different state summaries.

---

### 10. Non-stationarity means a previously sufficient abstraction can become wrong

A world representation may be sufficient under one dynamics regime and fail after the robot, controller, environment or task distribution changes.

#### ReDRAW

**Adapting World Models with Latent-State Dynamics Residuals**
PMLR/L4DC 2026: https://proceedings.mlr.press/v331/lanier26a.html
Evidence: `PRIMARY_PAPER`

ReDRAW pretrains a latent world model in simulation and adapts it to changed target dynamics by learning residual corrections in latent-state dynamics. It evaluates both vision-based control domains and a physical visual lane-following task.

Stage-1 relevance:

```text
same representation
+
changed transition law
```

can require adaptation even when observations remain visually similar.

#### Changepoint-Aware World Models

**Changepoint-Aware World Models: Detecting Dynamics Shifts and Recovering by Forgetting Stale Replay in Model-Based RL**
Primary paper: https://arxiv.org/abs/2609.18950
Evidence: `PRIMARY_PAPER`

CAWM detects abrupt dynamics shifts from internal prediction error using an online changepoint test and then discards stale replay while retaining the learned representation.

Why it matters:

It separates two questions:

```text
What is uncertain under the current model?
```

from:

```text
Has the current model itself become stale because the dynamics changed?
```

This is a form of **world-model falsification / regime-change detection**, not ordinary state estimation.

#### ROAM

**Adapt On-the-Go: Behavior Modulation for Single-Life Robot Deployment**
PMLR/CoLLAs 2026: https://proceedings.mlr.press/v330/chen26a.html
Evidence: `PRIMARY_PAPER`

ROAM adapts within one deployment episode to novel situations and changed dynamics using a repertoire of learned behaviors, including a real quadruped dynamics-shift demonstration.

This is useful evidence that open-world robotics requires **online recognition of regime mismatch**, not only offline robustness.

#### WorMI

**World Model Implanting for Test-time Adaptation of Embodied Agents**
PMLR/ICML 2025: https://proceedings.mlr.press/v267/yoo25a.html
Evidence: `PRIMARY_PAPER`

WorMI retrieves and composes domain-specific world models at test time for unseen domains.

#### Sirius-Fleet

**Multi-Task Interactive Robot Fleet Learning with Visual World Models**
PMLR/CoRL 2025: https://proceedings.mlr.press/v270/liu25g.html
Project: https://ut-austin-rpl.github.io/sirius-fleet
Evidence: `PRIMARY_PAPER`

Sirius-Fleet uses a visual world model and anomaly predictors to monitor deployment and trigger human correction when future outcomes are predicted to be anomalous.

Stage-1 relevance:

A robot world model may need not only prediction but a **failure-monitoring contract**:

```text
prediction
→ compare against realized evidence
→ detect anomaly / mismatch
→ decide whether to adapt, ask for help, or revise the model.
```

Research question:

```text
when should one world model be adapted,
when should another model be selected,
when should the system request external correction,
and when should it conclude that no existing model is adequate?
```

---

### 11. Embodiment itself changes the meaning of state and action

#### LAC-WM

**Cross-Embodiment Robot Foundation World Models with Latent Actions**
PMLR/ICML 2026: https://proceedings.mlr.press/v306/huang26bv.html
ArXiv: https://arxiv.org/abs/2610.10846
Project: https://lacwm.github.io/
Evidence: `PRIMARY_PAPER`

LAC-WM learns a unified latent action space across diverse robot embodiments and compares it with explicit action conditioning. The paper reports that explicit action spaces fragment across embodiments while the learned latent action representation transfers better to unseen robots.

Stage-1 implication:

```text
numerical action label
≠
embodiment-independent action meaning.
```

This strengthens the need to treat **self/embodiment state** as part of the world-model interface rather than a fixed external assumption.

#### OSCAR

**OSCAR: Omni-Embodiment Skeleton-Conditioned World Action Model for Robotics**
Primary paper: https://arxiv.org/abs/2606.04463
Evidence: `PRIMARY_PAPER`

OSCAR uses a 2D kinematic skeleton rendering as a common conditioning representation across robot arms and human hands. This is another candidate answer to cross-embodiment action semantics.

#### Embodiment Gap survey

**The Embodiment Gap in Robot Foundation Models**
Primary survey: https://arxiv.org/abs/2608.18433
Evidence: `SURVEY_SIGNAL`

The survey distinguishes what can be shared across robots from the adaptation work still required on a new body. It is useful as a reporting framework for separating reusable world knowledge from embodiment-specific execution machinery.

Neither result proves a universal embodiment representation; together they show that action/world abstraction depends strongly on how the robot body is represented.

---

### 12. Adaptive abstraction taxonomy

Stage 1 should distinguish at least:

#### G1 — task-conditioned abstraction

Keep only distinctions needed for a specified objective.

#### G2 — temporal abstraction

Represent fast and slow dynamics at different rates.

#### G3 — event-conditioned abstraction

Refine/update state around semantically meaningful transitions rather than every frame.

#### G4 — spatial abstraction

Use global coarse structure plus local high-resolution detail.

#### G5 — entity/relation abstraction

Move between dense scene representation, entities, relations and functional roles.

#### G6 — uncertainty-conditioned abstraction

Allocate more state/detail where uncertainty or decision sensitivity is high.

#### G7 — embodiment-conditioned abstraction

Keep state variables relevant to the current robot/action interface.

#### G8 — open-world reserve

Retain enough recoverable evidence so future tasks can reconstruct distinctions that were not important at the moment of compression.

#### G9 — regime-conditioned abstraction

Change representation/model assumptions when dynamics, domain or environment regime changes.

This is especially important for Clover's long-term general-purpose goal.

---

### 13. Failure modes of abstraction

#### Over-abstraction

```text
states that require different actions become merged
hidden changes are forgotten
a new task needs information that was discarded
```

#### Under-abstraction

```text
state becomes unnecessarily large
planning becomes expensive
irrelevant visual variation dominates representation
memory grows without bound
```

#### Wrong abstraction boundary

```text
correct object state but wrong task relation
correct visual detail but missing contact mode
correct short-term state but lost long-horizon event history
```

#### Static abstraction under non-stationarity

```text
state was sufficient yesterday
but dynamics / embodiment / controller / task distribution changed today.
```

A general-purpose system therefore needs a way to detect when an abstraction/model is no longer adequate.

---

### 14. Representation reversibility is an under-studied requirement

Compression can discard information that later becomes useful.

For a general-purpose robot, Stage 1 should distinguish:

```text
lossy active state
vs
recoverable evidence store / provenance
```

A state may remain compact while preserving links to evidence from which omitted distinctions can later be reconstructed.

This is not a recommendation for any historical Clover replay mechanism; it is a generic research requirement:

> If the future task distribution is unknown, how much information should remain recoverable after abstraction?

This connects memory, provenance, abstraction and open-world optionality.

---

### 15. Candidate later diagnostics

#### D-G1 — task-switch stress test

Train/compress for task A and test whether task B exposes irreversibly lost information.

#### D-G2 — granularity-cost Pareto curve

Measure:

```text
state size / memory / compute
vs
prediction
control
planning
memory
causal reasoning
```

#### D-G3 — local refinement test

Allow a coarse representation to request high-resolution local state only when needed; compare with always-fine and always-coarse baselines.

#### D-G4 — timescale ablation

Compare one-rate memory/state against multi-timescale or event-driven state updates.

#### D-G5 — unknown-future-task retention

Evaluate whether raw evidence/provenance allows reconstruction of information that the active abstraction omitted.

#### D-G6 — regime-shift detection

Change dynamics, camera, controller or embodiment and measure:

```text
mismatch-detection latency
adaptation time
false alarms
catastrophic interference
recovery of calibrated prediction/control
```

#### D-G7 — embodiment transfer

Keep task/environment fixed while changing robot morphology/action interface; test whether the state/action abstraction still preserves equivalent physical meaning.

#### D-G8 — model falsification

Inject a regime outside the current model/hypothesis family and measure whether the system reports model inadequacy rather than forcing the evidence into the nearest known explanation.

---

### 16. Adjacent gaps discovered

The literature suggests these areas should remain visible during Stage 1:

```text
multi-timescale state
structured/equivariant memory
non-stationarity and test-time adaptation
task-semantic / functional-role state
self / embodiment model
representation reversibility
world-model falsification / changepoint detection
open-world model inadequacy detection
```

These are not separate Clover commitments. They are candidate dimensions along which future representations should be compared.

---

### 17. Stage-1 questions

```text
Should state granularity be fixed or adaptive?
Which variables require high-frequency update and which only event-level update?
Can task-conditioned abstractions remain reusable for unknown future tasks?
How much raw evidence must be retained to reverse an earlier abstraction decision?
Should uncertainty control representation resolution?
Can structured transformation laws replace brute-force memory?
How should global scene state and local manipulation state interact?
When does hierarchy genuinely improve sufficiency rather than merely add modules?
How should the system detect that its current dynamics/embodiment abstraction is stale?
Should action semantics be represented in robot-specific coordinates or a shared embodiment-invariant space?
When should a model be adapted, replaced, composed with another model, or rejected as inadequate?
How can a robot tell the difference between ordinary prediction error and evidence that its model class is wrong?
```

---

### Current rule

Do not equate minimal state with general understanding.

Do not equate maximal-detail state with better intelligence.

The research target is **appropriate sufficiency at appropriate granularity, with explicit knowledge of what was discarded, whether it can be recovered, and whether the abstraction/model remains valid when the world or embodiment changes**.

---

<a id="topic-research-dossiers-r-c-representation"></a>

## R-C — Representation: Explicit, Distributed, Object-Centric or Hybrid?

Source record updated: 2026-10-14
Status: **BACKGROUND_RESEARCH**

### 1. Fundamental question

> **What internal representation is sufficient for stable visual world understanding and action?**

Candidate families include:

```text
explicit geometric/state variables
distributed latent representation
object-centric slots/entities
dense scene representation
continuous fields
generative latent state
hybrid / identifiable representations
```

No family is privileged by the Research Reset.

### 2. Static self-supervised representation

#### DINOv3

- Paper: https://arxiv.org/abs/2508.10104
- Official research page: https://ai.meta.com/research/publications/dinov3/
- Code: https://github.com/facebookresearch/dinov3

DINOv3 is a strong current baseline for large-scale label-free visual representation and dense frozen features.

**Demonstrates:** a static visual encoder can learn broadly reusable object/part/shape/spatial features without task-specific labels.

**Does not establish:** persistent identity, world revision, temporal state, intervention sensitivity or action-conditioned dynamics.

**Clover question:** what world-understanding capability is genuinely missing once a strong static representation is already available?

### 3. Predictive video representation

#### V-JEPA 2

- Paper: https://arxiv.org/abs/2506.09985
- Official page: https://ai.meta.com/vjepa/
- Research page: https://ai.meta.com/research/publications/v-jepa-2-self-supervised-video-models-enable-understanding-prediction-and-planning/
- Code: https://github.com/facebookresearch/vjepa2

V-JEPA 2 combines large-scale action-free video pretraining with a relatively small amount of action-conditioned robot experience for planning.

**Demonstrates:** distributed predictive latent state can support motion understanding, anticipation and robot planning without a hand-designed explicit world language.

**Open contradiction:** does predictive latent state remain sufficient for long-horizon persistence, belief revision, auditability and unseen physical interventions?

#### V-JEPA 2.1

- Paper: https://arxiv.org/abs/2603.14482

V-JEPA 2.1 strengthens dense, spatially structured and temporally consistent predictive features.

**Clover significance:** this is a serious alternative to a separately engineered `semantic + geometry + temporal` world representation.

### 4. Distributed physical variables are a real counterexample

#### Interpreting Physics in Video World Models

- Official publication: https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/
- Paper: https://arxiv.org/abs/2602.07050

This mechanistic study finds that physical quantities such as speed, acceleration and direction become decodable at different depths, and that direction is represented using a high-dimensional population code rather than a small set of compact state coordinates.

**Research consequence:**

```text
useful physical information
≠ necessarily compact explicit variables
```

Historical Clover mechanisms therefore cannot justify explicit state by interpretability intuition alone.

### 5. Object-centric representation

#### Slot Attention

- Paper: https://arxiv.org/abs/2006.15055

Slot Attention produces exchangeable object-like latent slots and demonstrated compositional generalization in controlled object-centric tasks.

**Potential advantage:** identity, relational structure and composition become easier to express.

**Open problem:** scalable object discovery in cluttered open-world video, dynamic topology, parts/fluids/deformables and ambiguous object boundaries.

#### Visible entities are not persistent world entities

SAM 3.1 provides a strong modern video detection/segmentation/tracking baseline:

- Official: https://ai.meta.com/blog/segment-anything-model-3/
- Code: https://github.com/facebookresearch/sam3

But:

```text
mask / track while visible
≠ enduring entity after evidence disappears
```

This is a critical separator between perception and representation.

### 6. Hybrid and identifiable state

#### Identifiable World Models from Pretrained Diffusion Representations

- Paper: https://arxiv.org/abs/2610.07028

This work asks whether a powerful distributed generative latent can be equipped with identifiable coordinates without retraining the generative backbone.

**Demonstrates in studied settings:** distributed world-model representations and interpretable/identifiable state coordinates need not be mutually exclusive.

**Clover significance:** the important comparison may not be `explicit vs latent`, but whether a hybrid can obtain the strengths of both with less cost than maintaining duplicate authorities.

### 7. Representation objectives preserve different information

Three major learning objectives should not be treated as synonyms:

```text
reconstruction → recover observed/spatial structure
prediction     → retain information useful for future state
 generation    → model a plausible conditional distribution
```

A representation that is excellent for one objective may discard information required by another.

Examples:

- VGGT / VGGT-Ω emphasize learned spatial reconstruction;
- V-JEPA emphasizes predictive latent state;
- Atlas / Cosmos emphasize generative/spatiotemporal simulation;
- VLA/WAM systems emphasize action-useful state.

### 8. Operational research questions

1. Does an explicit state offer measurable advantages in revision, querying or planning?
2. Can a distributed latent preserve object permanence and observability semantics without explicit variables?
3. Are object slots necessary, useful bias, or unnecessary restriction at open-world scale?
4. Can a hybrid representation avoid duplicate or inconsistent world authorities?
5. Which representation is most data-efficient for unseen dynamics?
6. Which representation transfers across camera and embodiment changes?
7. What information is lost by predictive compression?
8. What information is invented by generative completion?

### 9. Baseline families

| Family | Suggested comparator | Primary question |
|---|---|---|
| Static dense latent | DINOv3 | what can images alone encode? |
| Predictive video latent | V-JEPA 2/2.1 | can temporal prediction create sufficient world state? |
| Learned explicit geometry | VGGT / VGGT-Ω | is reconstruction enough for spatial understanding? |
| Object-centric | Slot Attention-style baseline | does factorized entity state improve composition/persistence? |
| Generative latent | Atlas/Cosmos-class evidence | does simulation imply usable state? |
| Hybrid identifiable | ConDA / identifiable world-model direction | can latent power coexist with interpretable coordinates? |
| Historical Clover | candidate explicit state | does it add independent measurable value? |

### 10. Discriminating experiment suite

#### T-C-01 — Matched world-query probing

Use the same visual histories and probe each representation for:

```text
identity
object permanence
spatial relation
temporal order
observability
physical variables
world change
intervention consequence
```

Keep probe capacity controlled to avoid measuring probe power instead of representation quality.

#### T-C-02 — Compression sufficiency

Compare representation sizes at matched query/task correctness.

Measure:

- representation bytes;
- answer coverage;
- correctness;
- long-occlusion degradation;
- new-query performance without retraining.

#### T-C-03 — Revision locality

Introduce a local world change after a long history.

Measure whether the representation can update the affected world state without catastrophic or unnecessary global change.

#### T-C-04 — Strong policy falsifier

```text
strong direct / recurrent policy
vs
same policy + candidate world representation
```

The world representation must improve at least one of:

- unseen-scene transfer;
- recovery;
- task success;
- planning cost;
- sample efficiency;
- unjustified action rate.

### 11. Kill conditions

A candidate representation should be rejected or simplified if:

- its advantages disappear with a stronger baseline;
- its benefit is only additional compute/memory;
- the same capability emerges in a simpler distributed state;
- explicit factors cannot be learned reliably from real visual data;
- hybrid state creates inconsistent duplicate authorities;
- representation quality does not translate to action or recovery.

### 12. Clover landing

Current conclusion:

> **Representation is still an open scientific variable. The strongest evidence argues against prematurely equating interpretability with correctness, while also leaving room for hybrid or identifiable state when it provides measurable revision, query, causal or action advantages.**

---

<a id="topic-research-dossiers-r-d-memory-persistence"></a>

## R-D — Persistence, Memory and Belief Revision

Source record updated: 2026-10-14
Status: **BACKGROUND_RESEARCH**

### 1. Fundamental question

> **How should a vision-only machine preserve and revise knowledge about a world that is only intermittently visible?**

Memory is not one thing. Candidate forms include:

```text
raw visual evidence
compressed perceptual history
persistent object/world state
episodic events
semantic memory
policy hidden state
external retrieval memory
hybrids
```

The project must distinguish remembering evidence from maintaining a world hypothesis.

### 2. Seeing is not remembering

#### PersistBench / Can 4D Foundation Models Remember?

- Paper: https://arxiv.org/abs/2609.20819
- Project / dataset / code: https://guangzhaohe.com/persistbench

PersistBench uses 360° video as an omniscient reference while evaluating ordinary limited-field-of-view models on:

- object permanence;
- motion continuity;
- appearance preservation.

**Demonstrates:** current 4D reconstruction/video models can be strong while an object is observed yet degrade substantially once it leaves the field of view.

**Clover implication:**

```text
reconstruction consistency while visible
≠ persistent world memory
```

Any claim of a world model should therefore report out-of-FOV behavior, not only clip reconstruction or tracking.

### 3. Streaming episodic memory is different from offline long-context QA

#### S-EMBER

- Paper: https://arxiv.org/abs/2607.02689
- Official publication index: https://ai.meta.com/results/?content_types%5B0%5D=publication&research_areas%5B0%5D=computer-vision

S-EMBER contains long egocentric streams and requires grounded retrieval with temporal localization of visual evidence.

**Demonstrates:** answering a question and locating the supporting past event are separable capabilities; current models show a substantial grounded-recall gap.

**Clover implication:** a long context window is not equivalent to reliable episodic world memory.

### 4. The memory harness itself can change capability

#### VISTA

- Paper: https://arxiv.org/abs/2610.02200
- Project: https://vista-research.github.io/
- Code: https://github.com/joshhhhhan/VISTA

VISTA maintains a lossless archive of visual observations and lets the model actively retrieve and reorganize past visual evidence.

**Demonstrates:** with the same general-purpose reasoning backend, changing the visual-memory/inspection harness can strongly change long-horizon interactive performance.

**Important limitation:** its strongest results are on visual games and interactive environments, not proof that lossless replay is the optimal memory architecture for real robots.

**Clover implication:** memory architecture is an independent research variable; capability is not determined only by model weights.

### 5. Memory must support revision, not only recall

A useful world model must handle:

```text
old evidence
→ old belief
→ world changes
→ partial new evidence
→ contradiction detected
→ affected state revised
→ downstream queries/plans updated
```

A system that remembers everything but cannot revise stale beliefs is not maintaining a usable world model.

### 6. Evidence memory vs world state

A critical distinction:

```text
Evidence memory = what visual observations can be re-examined?
World state      = what does the system currently believe / represent about the world?
```

They may be implemented together or separately, but experiments must not conflate them.

Historical Clover's Evidence Replay idea remains a hypothesis because VISTA and similar results establish the value of retrievable evidence, not the necessity of a specific Clover replay compiler.

### 7. Forgetting is also a research problem

Unlimited retention is not a scalable answer.

A realistic system must decide what to:

- keep at full fidelity;
- compress;
- summarize;
- retain as persistent state;
- discard;
- reload when a query or contradiction demands it.

Therefore memory should be evaluated by a Pareto frontier over:

```text
capability
retention bytes
retrieval latency
update latency
compute
```

not by recall score alone.

### 8. Operational research questions

1. Is object permanence best represented in world state, recurrent latent memory, or external evidence memory?
2. When should an object become `unknown` rather than remain confidently predicted?
3. How long should different state types persist?
4. Can memory support a query that was not known when the evidence was first observed?
5. Does retaining raw evidence materially improve belief revision over compressed latent history?
6. What is the right forgetting policy under bounded storage?
7. How should memory distinguish the world changing from the system merely observing a different viewpoint?
8. Can stale downstream decisions be invalidated when an upstream world belief changes?

### 9. Baseline families

| Family | Baseline / example | Isolates |
|---|---|---|
| Fixed context | standard video/VLM context | no explicit long-term memory architecture |
| Recurrent/predictive latent | V-JEPA-like / recurrent policy | compressed temporal state |
| Visible tracker memory | SAM 3.1 | persistence while detectable/trackable |
| Reconstruction memory | 4D foundation models | geometric temporal consistency |
| External visual archive | VISTA-style harness | re-access to original visual evidence |
| Episodic retrieval | S-EMBER-style systems | retrieval/localization from streaming history |
| Explicit world state | historical Clover candidate / classical map | persistent queryable state |

### 10. Discriminating experiments

#### T-D-01 — Long out-of-FOV persistence

Occlusion/out-of-view durations:

```text
4 / 8 / 16 / 32 / 64 / 128 frames
```

Measure:

- identity continuity;
- motion continuity;
- appearance consistency;
- uncertainty during absence;
- recovery at reappearance;
- memory bytes.

#### T-D-02 — New-query replay

Observe a long sequence without knowing the later question.

After the sequence, ask a query that requires an old visual detail not represented in the current task state.

Compare:

```text
fixed compressed context
recurrent state
external replay/retrieval
hybrid state + replay
```

#### T-D-03 — World change / stale belief

Move an object while it is unobserved, then reveal only partial evidence.

Measure:

- stale-state detection;
- time to revision;
- locality of revision;
- dependent planning errors;
- recovery.

#### T-D-04 — Retention Pareto

At matched task correctness, compare:

```text
storage bytes
retrieval p50/p99
update p50/p99
energy where measurable
```

#### T-D-05 — Evidence versus state ablation

Four conditions:

```text
world state only
raw/retrievable evidence only
world state + evidence
long-context latent only
```

This isolates whether each memory type contributes independent value.

### 11. Kill conditions

A dedicated evidence-replay mechanism should be demoted if it does not independently improve:

- new-query retrieval;
- belief revision;
- long-occlusion recovery;
- grounded verification;

at a defensible storage/latency cost.

A persistent explicit world state should also be rejected if a recurrent/latent memory reaches equal capability, revision quality and task success more simply.

### 12. Clover landing

Current conclusion:

> **Persistent world understanding requires more than a long context or visible tracking, but the correct architecture — recurrent latent, persistent state, retrievable evidence, or hybrid — remains open and must be decided by out-of-FOV, revision and new-query experiments.**

---

<a id="topic-docs-research-map-learned-visual-representations"></a>

## Learned Visual Representations

### What problem does this area solve?

Classical vision depends on variables and features chosen by humans. Self-supervised representation learning asks whether useful visual structure can emerge from large unlabeled image collections instead.

For Clover the central question is not image classification. It is:

> **What world-relevant structure is already present in generic learned visual features before temporal or action learning is added?**

### Representative work: DINOv2

DINOv2 learns general-purpose visual features without manual labels. Meta's model card describes ViT backbones whose class and patch tokens can support downstream classification, depth estimation, segmentation and retrieval with lightweight heads. The original work trained on LVD-142M images.

Primary sources:

- https://github.com/facebookresearch/dinov2
- https://arxiv.org/abs/2304.07193

#### Representation

A distributed transformer feature space: global class token plus spatial patch tokens, optionally with register tokens.

#### Learning signal

The released model card lists self-distillation, masked-image modeling and feature regularization components.

#### What it demonstrates

A large amount of transferable visual structure can be learned without semantic labels, and useful geometry-related signals such as depth can be extracted with small downstream heads.

#### What it does not demonstrate

DINOv2 by itself does not establish:

- persistent identity through long occlusion;
- a stable world state across time;
- physical dynamics;
- causal intervention reasoning;
- action-conditioned world change.

It is therefore a strong **perceptual representation baseline**, not a complete answer to Clover's question.

### Clover questions

1. Which Clover world queries are linearly or cheaply readable from a strong static visual representation?
2. Which queries fundamentally require temporal learning?
3. Does an explicit world state add information, or only make existing latent information easier to query?
4. Can a learned visual backbone preserve fine geometric detail needed for physical reasoning without task-specific supervision?
5. How much of apparent world knowledge is inherited from dataset regularities rather than physical understanding?

### Research value

This area prevents Clover from reinventing low-level feature learning unnecessarily. If modern self-supervised features already provide robust object/geometry cues, Clover's novel contribution should begin where those representations become insufficient: persistence, observability, dynamics, causal revision and action-useful world state.

---

<a id="topic-docs-research-map-object-centric-representation"></a>

## Object-Centric Representation

### Core question

> **Should a machine represent the world as persistent entities, or can object-like structure remain implicit inside a distributed representation?**

Objects are tempting primitives because robot tasks are often described in terms of things that persist, move, interact and can be acted upon. But treating objects as pre-given may bake human ontology into the system too early.

### Slot Attention

Slot Attention introduced a mechanism that maps perceptual features into a set of exchangeable slots through iterative competitive attention. The original work showed object-centric representations that generalize to unseen compositions in object-discovery/property-prediction settings.

Primary source:

- https://arxiv.org/abs/2006.15055

### Video segmentation and tracking as a lower-level baseline

SAM 2 extends promptable segmentation to image and video and adds streaming memory for maintaining target masks through a sequence. Meta describes memory that carries target-object context across frames, including temporary disappearance.

Primary source:

- https://ai.meta.com/research/sam2/
- https://github.com/facebookresearch/sam2

SAM 2 is not a world model. It is useful because it isolates a concrete subproblem:

> how well can a strong modern vision system maintain a visually specified entity through time?

### Competing hypotheses

#### H1 — Object as primitive

The world state directly contains entity records with identity and state.

**Advantage:** simple queries, planning and relation construction.

**Risk:** premature segmentation and brittle ontology.

#### H2 — Object as emergent structure

Objects emerge from lower-level spatial/temporal structure, field coherence or predictive equivalence.

**Advantage:** can adapt to unfamiliar entities and scales.

**Risk:** may be difficult to stabilize and query.

#### H3 — Distributed latent only

No explicit object record is required; object information is decoded when needed.

**Advantage:** representation is not forced through an information bottleneck.

**Risk:** persistence, revision, provenance and planning may be hard to make reliable.

### What Clover needs from an entity representation

A useful entity mechanism should support:

- identity across viewpoint change;
- occlusion and reappearance;
- split/merge/deformation when appropriate;
- object-relative dynamics;
- relations and contact;
- uncertainty over identity;
- local belief revision;
- efficient queries for decision making.

### Critical question

Clover should not ask only:

> Can we segment objects?

It should ask:

> **Does explicit entity structure produce capabilities that a strong dense/video representation cannot provide as reliably or efficiently?**

---

<a id="topic-docs-research-map-video-world-models"></a>

## Video Representation and World Models

### Core question

> **Can a machine learn useful physical world structure largely by observing video, and what representation emerges when it does?**

This is one of the closest modern research families to Clover's SSOT.

### V-JEPA 2

Meta describes V-JEPA 2 as a self-supervised video model for understanding, prediction and planning. It is pretrained action-free on more than one million hours of internet video. Meta reports strong motion understanding and action anticipation results, then post-trains an action-conditioned model (V-JEPA 2-AC) with a much smaller amount of robot trajectory data for robot planning.

Primary sources:

- https://ai.meta.com/research/publications/v-jepa-2-self-supervised-video-models-enable-understanding-prediction-and-planning/
- https://github.com/facebookresearch/vjepa2
- https://arxiv.org/abs/2506.09985

#### Representation

A learned latent video representation. JEPA-style training predicts representations rather than reconstructing raw pixels.

#### Scientific importance for Clover

V-JEPA 2 directly challenges the assumption that world understanding needs a hand-designed explicit world language. It asks whether prediction in latent space can induce enough temporal and physical structure for planning.

#### Observation versus interaction

The separation between very large action-free video pretraining and comparatively limited robot interaction data creates a useful research question:

> What physical regularities can be learned from passive observation, and what only becomes identifiable through action?

Clover should treat this as a first-class theoretical question rather than assuming either passive video or interaction is sufficient.

### V-JEPA 2.1

The official repository states that V-JEPA 2.1 focuses on high-quality, temporally consistent dense features. Its training recipe adds dense predictive loss, deep self-supervision, image/video tokenization and scaling.

Primary source:

- https://github.com/facebookresearch/vjepa2
- https://arxiv.org/abs/2603.14482

For Clover, the key issue is whether dense temporal consistency can provide a stronger substrate for identity, motion, boundary persistence and world-state formation than global video representations alone.

### Mechanistic interpretation: physics in video world models

Meta's 2026 work **Interpreting Physics in Video World Models** studies how physical variables are represented inside video encoders. The reported finding that some variables become increasingly linearly accessible while other structure is distributed across high-dimensional populations is an important counterexample to a naive explicit-variable assumption.

Source:

- https://ai.meta.com/research/publications/interpreting-physics-in-video-world-models/

#### Clover consequence

The research question is no longer:

> Can we design a compact set of explicit variables?

It is:

> **When does explicit state improve generalization, causal revision, queryability and control over a distributed representation, and when does it discard useful information?**

### World-model taxonomy relevant to Clover

Video/world models can serve different roles:

- **encoder** — produce representations;
- **predictor** — predict future latent state;
- **renderer/generator** — generate observations;
- **simulator** — roll a world forward under conditions/actions;
- **planner substrate** — score or search action consequences.

A system should not be called a complete world model merely because it performs one of these functions.

### What this family has demonstrated

- large-scale video SSL can learn strong temporal/motion representations;
- latent predictive models can support downstream robot planning after action conditioning;
- temporal consistency can be learned densely rather than only at a global clip level;
- physical variables can be present in representations without explicit hand-designed state variables.

### What remains unresolved for Clover

- persistent object identity beyond the video context window;
- explicit distinction between unobserved, unknown and absent;
- belief revision after contradictory evidence;
- long-term world memory;
- causal identification rather than predictive correlation;
- whether latent prediction helps real robot recovery under unexpected world changes;
- whether language alignment imports non-visual knowledge into a supposedly visual understanding evaluation.

---

<a id="topic-research-emerging-representation_diagnostics_2026-10-15"></a>

## Stage-1 Emerging Audit — Representation Diagnostics and Causal Use

Source record updated: **2026-10-15**
Source intake checked through: **2026-10-15**

> Mother question: **How can a machine understand the real world through vision alone?**

This is supporting methodology for Stage 1 / Stage 2. It does not define a Clover representation.

### Core problem

A representation may contain information that a downstream probe can decode even when the deployed policy does not actually use that information.

Keep three claims separate:

```text
information is decodable from latent state
≠
information is causally used by the model
≠
changing that information produces the expected closed-loop behavior
```

This distinction matters directly for claims such as:

```text
"the model represents mass"
"the model understands direction"
"the world model encodes object permanence"
"the policy uses causal state"
```

A linear probe alone cannot establish these stronger claims.

---

### 1. Current embodied mechanistic-interpretability evidence

### Do Vision-Language-Action Models Understand Instructions?

Paper: https://arxiv.org/abs/2610.10178
Evidence: `PRIMARY_PAPER`

The paper studies `π0.5` and `GR00T N1.7` using activation patching and attribution patching under controlled instruction corruptions.

Important reported observations:

- directional language can produce large causal effects on action generation;
- the loci of causal sensitivity differ across the two model families;
- for GR00T N1.7, large causal effects can occur while representational geometry changes relatively little;
- attribution patching tracks activation patching differently across the two models.

Stage-1 lesson:

```text
representation similarity
≠
causal functional role
```

and interpretability methods themselves require validation per architecture.

---

### Mechanistic interpretability for steering VLAs

Paper: https://arxiv.org/abs/2509.00328
Evidence: `PRIMARY_PAPER`

This work identifies internal semantic directions linked to action behavior and demonstrates activation steering on open-source VLA models in simulation and on a physical robot.

Research role:

```text
observe latent feature
→ intervene on latent feature
→ measure action change
```

is stronger evidence than probe accuracy alone.

But successful steering still does not prove that the steered concept is a complete or correctly grounded world variable.

---

### 2. Required representation-evidence ladder

For future Clover/Stage-2 claims, record the strongest evidence available.

```text
RD0 correlation / visualization
RD1 linear probe recoverability
RD2 nonlinear probe / controlled prediction
RD3 causal activation patch / ablation / mediation
RD4 targeted steering changes action in expected direction
RD5 closed-loop intervention changes physical outcome as predicted
RD6 OOD / counterfactual replication of the causal effect
```

Do not promote an `RD1` result into an `RD5` claim.

Example:

```text
mass can be linearly predicted from Z_t
```

only establishes decodability under the probe/data assumptions. It does not establish that the robot policy uses mass, that mass is identifiable from evidence, or that manipulating the mass coordinate changes action appropriately.

---

### 3. Probe controls that should be mandatory

When probing a latent variable, control for:

```text
probe capacity
sample size
class/category leakage
language-label leakage
viewpoint / camera identity
object identity shortcut
time-index shortcut
action-label shortcut
train/test environment overlap
frozen vs post-trained representation
```

Prefer counterfactual/minimal-pair datasets where the target physical variable changes while appearance/semantics are controlled as much as possible.

---

### 4. Representation quality should be multidimensional

For a candidate world state `Z_t`, evaluate separately:

```text
Decodable?          can a probe recover the variable?
Identifiable?       was enough evidence available to infer it?
Causally used?      does the model actually rely on it?
Intervenable?       can controlled latent change alter behavior predictably?
Persistent?         does it survive occlusion/time?
Revisable?          can contradictory evidence update it?
Action-sufficient?  does it support control/planning?
Open-world robust?  does the effect survive new objects/scenes/regimes?
```

This prevents `representation quality` from collapsing into one probe score.

---

### 5. Relation to JEPA / WAM / Foundation-model audits

This methodology is especially important for recent latent world models such as:

```text
V-JEPA / RoboJEPA
SpecWM
Identifiable World Models
ReWAM
LeWAM variants
LAC-WM
DELE-style future latents
```

Questions to ask:

```text
Does scaling reduce prediction loss while leaving critical state variables absent?
Does a frozen visual encoder create a hard information ceiling?
Are action-relevant variables merely decodable or causally used?
Does post-training re-route which layers/features actually control action?
Does quantization/token pruning preserve probe accuracy but alter causal use?
```

---

### 6. Current rule

Stage 2 must not equate:

```text
probe success
with
understanding.
```

For high-value world-state claims, aim to progress from:

```text
recoverability
→ causal attribution
→ intervention
→ closed-loop behavioral evidence
→ OOD/counterfactual validation.
```

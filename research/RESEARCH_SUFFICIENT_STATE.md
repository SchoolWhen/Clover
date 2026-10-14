# Stage 1 — Minimum Sufficient World State

Last updated: 2026-10-14  
Freshness cutoff checked through: **2026-10-14**

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

## 1. History, state and compression

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

## 2. Different notions of sufficiency

Stage 1 should not use the word "sufficient" without specifying the target.

### 2.1 Predictive sufficiency

For future observations/outcomes `Y`, a representation is predictively sufficient when, conceptually:

```text
P(Y_future | H_t, A_future)
=
P(Y_future | Z_t, A_future).
```

`Z_t` then preserves what the history contributes to the chosen prediction problem.

This does **not** automatically imply that the representation is sufficient for reward, planning, intervention or belief revision.

### 2.2 Control sufficiency

For a task/reward family, state is control-sufficient if the optimal decision need not access information discarded from history.

Conceptually:

```text
Q*(H_t, a) = Q*(Z_t, a)
```

for relevant actions/tasks.

A representation can be excellent for reconstruction while discarding small task-relevant distinctions, or highly control-sufficient while discarding appearance details.

### 2.3 Planning sufficiency

Planning needs enough state to predict the consequences of candidate actions and compare possible futures.

This can differ from one-step policy sufficiency.

### 2.4 Memory / revision sufficiency

A representation can be sufficient for the current task but insufficient when:

```text
an object leaves view
the world changes
a new query is asked later
old evidence must be reinterpreted
```

Long-term robotic state may therefore need to preserve evidence or uncertainty that a short-horizon policy would safely discard.

### 2.5 Causal / counterfactual sufficiency

Prediction under the observed behavior distribution may not preserve the variables needed for unseen interventions.

A state sufficient for:

```text
What usually happens next?
```

may fail for:

```text
What would happen if I intervene differently?
```

### 2.6 Open-world / multi-task sufficiency

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

## 3. POMDP belief state: a canonical sufficient statistic under a known model

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

## 4. Predictive State Representations: state as predictions rather than hidden variables

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

## 5. Information state and Approximate Information State

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

## 6. State abstraction / bisimulation: discard distinctions that do not matter for control

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

## 7. Detecting when a learned representation is not Markov enough

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

## 8. 2026 world-model research is converging on sufficiency as a design question

### 8.1 Latent State Design for World Models under Sufficiency Constraints

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

### 8.2 DELE-w0.5: future latent state instead of dense video

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

### 8.3 Representation World Model

**Representation World Model: Learning States, Transition and Executable Plans in Representation**  
Primary paper: https://arxiv.org/abs/2609.29171

RWM learns representation geometry such that latent paths between endpoint representations preserve enough transition structure for inverse dynamics to recover executable actions.

Research hypothesis:

```text
planning-relevant geometry can live directly inside representation space.
```

Again, this is planning/control sufficiency evidence, not proof of complete world understanding.

---

## 9. Dense video generation may preserve too much information — or the wrong information

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

## 10. A proposed Stage-1 sufficiency taxonomy

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

## 11. Why general-purpose robotics makes "minimal" difficult

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

## 12. Evidence retention may solve part of the minimality problem

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

## 13. Proposed later diagnostics for representation sufficiency

Stage 2/6 should eventually test sufficiency directly rather than infer it from one benchmark score.

### 13.1 History leakage / Markov test

Ask whether prediction/control improves after giving the downstream model extra history beyond `Z_t`.

If yes, the state omitted useful information.

### 13.2 State aliasing counterexamples

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

### 13.3 Task-transfer sufficiency

Freeze the state representation and introduce a new downstream task.

Measure whether relevant information was retained before the task was known.

### 13.4 Intervention sufficiency

Test matched histories under different controlled interventions.

A state may be prediction-sufficient on observational data yet intervention-insufficient.

### 13.5 Memory/revision sufficiency

After long occlusion or external world change, test whether state plus retained memory supports correct revision.

### 13.6 Uncertainty sufficiency

Two representations may achieve similar accuracy but differ in whether they preserve the distinction between:

```text
known absent
vs
unobserved
vs
ambiguous.
```

### 13.7 Action-efficiency Pareto curve

Measure:

```text
state bytes / latent dimension / memory cost
vs
task success / prediction / planning quality.
```

The objective should be a Pareto frontier, not smallest latent dimension at any cost.

---

## 14. Open research questions

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

## Stage-1 provisional conclusion

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

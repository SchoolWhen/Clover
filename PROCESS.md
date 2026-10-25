<a id="top"></a>

# Research process and decisions

Maintained: **2026-10-25** · Current project stage: **Research** ([status](STATUS.md)).

The seven-stage lifecycle, method templates, contribution rules and dated decisions. STATUS.md alone records the current project stage.

This is the canonical topic document. Update it in place; source-level dates and reading-depth labels below qualify the evidence, not the maintenance date.

## Contents

- [Clover Research Lifecycle](#topic-research-pipeline)
- [Clover Roadmap](#topic-roadmap)
- [Stage 2 — Analysis](#topic-research-analysis)
- [Stage 3 — Synthesis](#topic-research-synthesis)
- [Stage 4 — Innovation](#topic-research-innovation)
- [Stage 5 — Implementation](#topic-research-implementation)
- [Stage 7 — Reflection](#topic-research-reflection)
- [Contributing to Clover](#topic-contributing)
- [Public Release Checklist](#topic-public_release_checklist)
- [Decision 0001 — Research Reset](#topic-research-decisions-0001-research-reset)
- [Decision 0002 — Hardware Is a Design Variable](#topic-research-decisions-0002-hardware-is-a-design-variable)
- [Decision 0003 — Current Representation Is a Hypothesis](#topic-research-decisions-0003-current-representation-is-a-hypothesis)
- [Decision 0004 — GitHub Is the Public Research Record](#topic-research-decisions-0004-github-is-public-research-record)
- [0005 — Research before reproduction](#topic-research-decisions-0005-research-before-reproduction)
- [ADR 0006 — `main` Is the Canonical Research Branch During the Mapping Phase](#topic-research-decisions-0006-main-is-canonical-during-research)
- [ADR 0007 — Survey Foundation Is the Primary Research Entry](#topic-research-decisions-0007-survey-foundation-is-primary-entry)
- [0008 — Background research before representation hypothesis](#topic-research-decisions-0008-background-research-before-representation)
- [ADR 0009 — Flat Seven-Stage Research Lifecycle](#topic-research-decisions-0009-seven-stage-research-lifecycle)
- [Stage 1 Final Audit — 2026-10-15](#topic-research-stage1_final_audit_2026-10-15)
- [Stage-1 Re-audit Summary — 2026-10-15](#topic-research-emerging-reaudit_summary_2026-10-15)

<a id="topic-research-pipeline"></a>

## Clover Research Lifecycle

Source record updated: 2026-10-14

> **Research question:** How can a machine understand the real world through vision alone?
>
> **Long-term goal:** Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.

This file defines the canonical research lifecycle for Clover. It is deliberately flat and agent-readable.

### The seven stages

```text
1. Research
   ↓
2. Analysis
   ↓
3. Synthesis
   ↓
4. Innovation
   ↓
5. Implementation
   ↓
6. Evaluation
   ↓
7. Reflection
   ↺ feeds the next Research / Analysis / Innovation cycle
```

The stages describe **epistemic maturity**, not software versions.

---

### 1 — Research

**Meaning:** survey, discovery and evidence collection.

**Current status:** **ACTIVE**.

Purpose:

- search broadly before narrowing;
- identify all materially relevant research directions;
- collect primary papers, official project pages, code, checkpoints, datasets and benchmarks;
- record what each source claims without prematurely deciding whether Clover should adopt it;
- preserve training/evidence provenance and evaluation conditions;
- maintain a current map of methods, labs, datasets and open problems.

Typical outputs:

- source inventory;
- methods inventory;
- dataset / benchmark inventory;
- laboratory / project watchlist;
- research-domain map;
- source URLs and evidence labels;
- unresolved questions.

Research is **collection before judgment**.

Primary file: [`RESEARCH.md`](RESEARCH.md#topic-research-research).

---

### 2 — Analysis

**Meaning:** understand how each important method actually works.

**Status:** framework defined; large-scale execution comes after the Research inventory is sufficiently broad.

For every important method, produce a structured section in the canonical topic document covering:

```text
problem
inputs / supervision
internal representation
learning objective
architecture / mechanism
memory / temporal treatment
geometry / object / physics assumptions
action interface if any
datasets
benchmarks
reported results
strengths
limitations
confounds
reproducibility
what it implies for Clover
```

Analysis asks **how and why a method works**, not merely whether its headline score is high.

Primary file: [`PROCESS.md`](#topic-research-analysis).

---

### 3 — Synthesis

**Meaning:** compare analyzed methods across common dimensions.

**Status:** downstream of sufficient Analysis coverage.

Purpose:

- summarize advantages and disadvantages;
- identify repeated mechanisms across superficially different methods;
- separate solved problems from recurring failures;
- build capability and failure matrices;
- identify contradictions that existing approaches cannot jointly resolve;
- determine where evidence is still missing.

Typical outputs:

```text
method-family comparison
capability matrix
failure matrix
pros / cons summary
trade-off map
shared bottlenecks
research gaps
candidate falsifiers
```

Synthesis asks **what we have learned from the field as a whole**.

Primary file: [`PROCESS.md`](#topic-research-synthesis).

---

### 4 — Innovation

**Meaning:** formulate Clover-original hypotheses and algorithms from the gaps identified by Synthesis.

**Status:** ideas may be recorded, but no idea is promoted to the project answer during the current Research stage.

Innovation may contain:

- original representation hypotheses;
- new variables and mathematical formalizations;
- new learning principles;
- new memory/state/update rules;
- new causal or active-perception mechanisms;
- new algorithmic combinations only when the combination follows from a demonstrated contradiction rather than framework stacking;
- discriminating experiments and kill conditions.

Required form:

```text
observed gap
→ why existing methods fail
→ original hypothesis
→ mathematical / algorithmic statement
→ prediction
→ falsifier
→ required experiment
```

Historical Clover mechanisms live here as candidate ideas until evidence promotes or rejects them.

Primary file: [`PROCESS.md`](#topic-research-innovation).

---

### 5 — Implementation

**Meaning:** implement only sufficiently motivated hypotheses, baselines and bounded diagnostics.

**Status:** future core phase; small diagnostic implementations may occur earlier only when needed to answer a research question.

Outputs:

- reproducible code;
- baseline adapters;
- dataset loaders;
- experiments;
- model / algorithm implementation;
- instrumentation and tracing;
- environment and dependency records.

Implementation does not retroactively justify an idea merely because substantial code exists.

Primary file: [`PROCESS.md`](#topic-research-implementation).

---

### 6 — Evaluation

**Meaning:** experiments, measurements and results.

This stage includes what earlier documents called the Understanding Battery, baseline comparison and real-world evaluation.

Outputs include:

- controlled diagnostics;
- benchmark results;
- real-world results;
- generalization tests;
- ablations;
- failure cases;
- uncertainty / calibration;
- action utility;
- latency, memory and energy when scientifically relevant.

Evaluation must preserve conditions such as:

- visual observation protocol (`V0–V3`);
- learning-evidence provenance (`L0–L4`);
- dataset split;
- model version;
- hardware when relevant;
- whether a result is independently reproduced or externally reported.

Primary file: [`EVALUATION.md`](EVALUATION.md#topic-research-evaluation).

---

### 7 — Reflection

**Meaning:** interpret the results and decide what changes next.

Reflection is not a narrative conclusion section. It is structured scientific feedback.

Questions:

- Which hypothesis survived?
- Which hypothesis failed?
- Which failure is architectural versus data/evaluation-related?
- Which assumptions were invalid?
- Did the experiment actually discriminate the intended question?
- What new contradiction appeared?
- What should be deleted rather than patched?
- What new research must be performed before the next Innovation cycle?

Outputs:

```text
result interpretation
failure postmortem
hypothesis status changes
revised assumptions
new research questions
next-cycle priorities
```

Primary file: [`PROCESS.md`](#topic-research-reflection).

---

### Current operating rule

Clover is currently in **Stage 1 — Research**.

The immediate goal is breadth, traceability and coverage:

```text
collect the problem space
collect the strongest methods
collect primary sources
collect code / datasets / benchmarks
collect counterexamples
collect current frontier directions
```

Do not force the repository into Stage 4 Innovation because one interesting paper or idea appears.

A method may be catalogued during Research without being endorsed. A Clover idea may be recorded during Innovation without being implemented. An implementation may exist without being scientifically validated.

These distinctions are intentional.

---

**Research broadly. Analyze carefully. Synthesize comparatively. Innovate only from demonstrated gaps. Implement reproducibly. Evaluate honestly. Reflect before iterating.**

---

<details>
<summary>Earlier roadmap wording — historical context; current status is in STATUS.md</summary>

<a id="topic-roadmap"></a>

## Clover Roadmap

Source record updated: 2026-10-14

> **Research question:** How can a machine understand the real world through vision alone?
>
> **Long-term goal:** Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.

The roadmap follows one flat scientific lifecycle:

```text
1 Research
→ 2 Analysis
→ 3 Synthesis
→ 4 Innovation
→ 5 Implementation
→ 6 Evaluation
→ 7 Reflection
↺ next cycle
```

The ordering matters. Clover should not invent first and search for justification later.

---

### Stage 1 — Research

**CURRENT / ACTIVE**

Goal: collect the full problem space before narrowing.

Collect:

- research directions;
- canonical foundations;
- latest strong methods;
- primary papers;
- official project pages;
- official code/checkpoints;
- datasets;
- benchmarks;
- laboratories/projects to monitor;
- visual protocols and learning provenance;
- known limitations;
- open questions.

Primary files:

- `PROCESS.md`
- `RESEARCH.md`
- `SOURCES.md`
- supporting Survey and dossier material.

Research is broad by design. A direction does not need to fit an existing Clover mechanism to be included.

#### Stage-1 exit condition

A new agent should be able to identify the major relevant fields, strongest current methods, sources, code, datasets, benchmarks and missing areas without relying on historical Clover assumptions.

---

### Stage 2 — Analysis

Goal: understand important methods one by one.

For each method, analyze:

```text
problem
inputs / supervision
representation
mechanism
objective
memory / time
geometry
objects / relations
physics
causality
action interface
datasets
benchmarks
results
strengths
weaknesses
confounds
reproducibility
```

Output: structured method sections in the canonical topic documents following `PROCESS.md`.

Baseline reconstruction may occur here when implementation/probing is necessary to understand a method rather than merely trust its paper.

---

### Stage 3 — Synthesis

Goal: understand the field comparatively.

Outputs:

- capability matrix;
- method-family comparison;
- pros / cons summary;
- trade-off map;
- Failure Matrix;
- recurring bottlenecks;
- evidence gaps;
- unresolved contradictions;
- candidate discriminating experiments.

This stage summarizes what existing approaches collectively teach us.

Template: `PROCESS.md`.

---

### Stage 4 — Innovation

Goal: formulate Clover-original hypotheses and algorithms from well-supported gaps.

Innovation may include:

- representation hypotheses;
- mathematical variables;
- learning objectives;
- memory/update rules;
- causal mechanisms;
- active perception mechanisms;
- machine-native algorithms;
- new evaluation hypotheses.

Every serious idea must state:

```text
observed gap
existing methods considered
why they appear insufficient
original hypothesis
mathematical / algorithmic statement
prediction
falsifier
minimal experiment
```

Historical Clover concepts are ideas here, not protected answers.

Template: `PROCESS.md`.

---

### Stage 5 — Implementation

Goal: build reproducible baselines, diagnostics and selected Clover hypotheses.

Outputs:

- code;
- data loaders;
- baseline adapters;
- training/inference pipelines;
- experiment configs;
- instrumentation;
- deployment experiments.

Implementation does not validate a scientific claim by itself.

Template: `PROCESS.md`.

---

### Stage 6 — Evaluation

Goal: test claims and produce Results.

Evaluation may include:

- controlled diagnostics;
- public benchmarks;
- shortcut-resistant pairs;
- memory tests;
- causal/interventional tests;
- generalization;
- active perception;
- real-world tasks;
- long-horizon action;
- ablations;
- failure cases;
- latency/memory/energy when relevant.

What earlier documents called baseline comparison and the Understanding Battery are evaluation assets within this lifecycle, not separate top-level project phases.

Evidence should progress where relevant from:

```text
controlled synthetic
→ controlled real
→ unfamiliar real environments
```

Template: `EVALUATION.md`.

---

### Stage 7 — Reflection

Goal: interpret the evidence and decide the next cycle.

Reflection records:

- what survived;
- what failed;
- what remained ambiguous;
- which assumptions were wrong;
- which mechanisms should be removed;
- which benchmarks were insufficient;
- what new research questions appeared;
- whether a hypothesis should be kept, modified, rejected or superseded.

Template: `PROCESS.md`.

Reflection feeds the next Research / Analysis / Innovation cycle.

---

### Long-term product integration

Across later cycles, validated work should converge toward the product loop:

```text
vision
→ world understanding
→ decision
→ capability / tool selection
→ execution
→ new visual evidence
→ updated understanding
```

Robot-brain integration, real-world evaluation and hardware co-design occur inside the Implementation/Evaluation/Reflection loop rather than being treated as reasons to skip Research, Analysis or Synthesis.

### Final rule

> **Research broadly. Analyze deeply. Synthesize comparatively. Innovate from demonstrated gaps. Implement reproducibly. Evaluate honestly. Reflect before the next cycle.**

</details>

---

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

---

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

<a id="topic-research-innovation"></a>

## Stage 4 — Innovation

### Original Hypotheses and Algorithm Design

Source record updated: 2026-10-14

**Status:** IDEAS MAY BE RECORDED; NO CORE HYPOTHESIS IS CURRENTLY FROZEN.

Innovation is where Clover may finally propose its own representation, algorithm or learning principle. It must be downstream of Research, Analysis and Synthesis.

### Innovation record template

```text
Idea name:
Status: IDEA / HYPOTHESIS / TESTABLE / REJECTED / SUPERSEDED

Observed gap:
Evidence for the gap:
Existing approaches considered:
Why existing approaches appear insufficient:

Original hypothesis:
Mathematical statement:
State / representation:
Learning signal:
Update rule:
Memory rule:
Uncertainty semantics:
Action relationship:

Prediction:
Falsifier / kill condition:
Minimal discriminating experiment:
Required baseline:
Expected advantage:
Expected cost / risk:
```

### Rules

- Novelty must be algorithmic or scientific, not merely a new arrangement of named modules.
- If a new variable is introduced, every dependent equation and definition must be updated consistently.
- A hypothesis should explain an observed failure, not merely sound elegant.
- Historical Clover concepts may appear here, but only as candidates.
- An idea does not become the project answer until Evaluation supports it against strong alternatives.

### Historical idea bucket

Examples of historical concepts that may be re-examined here include field/crystallization, CSP/SEP, evidence state, licence/auditability, evidence replay, growth/revision, visual world compiler and related ideas.

Their historical existence is not evidence of correctness.

### Preferred innovation form

```text
field evidence
→ unresolved contradiction
→ simplest new hypothesis capable of resolving it
→ mathematical formulation
→ experiment that can kill it
```

This stage is the proper home for “our own ideas.”

---

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

---

<a id="topic-contributing"></a>

## Contributing to Clover

Clover is a research project. A contribution should clearly belong to one stage of the canonical lifecycle:

```text
Research → Analysis → Synthesis → Innovation → Implementation → Evaluation → Reflection
```

The current primary stage is **Research**.

### Research contributions

Useful current contributions include:

- a missing research direction;
- a primary paper or official project page;
- official code / checkpoint;
- dataset or benchmark;
- a correction to an existing source record;
- a newly relevant 2026 method;
- a missing lab/project worth monitoring;
- evidence that a method’s claimed capability is narrower than currently described.

Please preserve:

```text
exact source URL
research direction
evidence level
what is demonstrated
what is not demonstrated
code / dataset / benchmark links when available
V0–V3 / L0–L4 provenance when material
```

### Analysis contributions

When deeper method study becomes appropriate, use the method-report structure in `PROCESS.md`.

Do not summarize only the abstract. Explain representation, objective, memory/time treatment, geometry/physics/causal assumptions, action interface, datasets, benchmarks, strengths, weaknesses and confounds.

### Synthesis contributions

Compare multiple analyzed methods on the same dimensions. Useful outputs include capability matrices, pros/cons, trade-offs, recurring failure modes and research gaps.

### Innovation contributions

Do not propose `Clover + framework X` as the contribution.

A serious original hypothesis should state:

1. observed gap;
2. evidence for the gap;
3. existing methods considered;
4. why they appear insufficient;
5. original mathematical / algorithmic hypothesis;
6. prediction;
7. falsifier;
8. minimal discriminating experiment.

### Implementation contributions

Prefer inspectable, testable and reproducible code. Record configuration, dependencies, data/model versions and hardware when relevant.

Implementation status is not scientific validation.

### Evaluation contributions

An experiment should record:

- research question;
- protocol;
- model / code version;
- dataset / split;
- baseline;
- metric;
- success and kill criteria;
- result;
- failures;
- limitations of the measurement.

Negative results are valid contributions.

### Reflection contributions

State what survived, what failed, what remained ambiguous, which assumptions should change and what the next research question should be.

### Final rule

Contributions should make the project know more, not merely make the repository contain more code or more paper names.

---

<a id="topic-public_release_checklist"></a>

## Public Release Checklist

### Research identity

- [x] Highest research question is explicit.
- [x] Product goal is explicit.
- [x] Facts and hypotheses are separated.
- [x] Current status avoids scientific overclaim.
- [x] Roadmap is research-driven rather than version-driven.

### Repository

- [x] README and Chinese overview exist.
- [x] Principles, status, roadmap and contributing guides exist.
- [x] Apache-2.0 license is present.
- [x] Research decisions are tracked.
- [x] Research, hypothesis, architecture and evaluation documentation have defined homes.
- [ ] Existing Clover prototype code has been audited for public import.
- [ ] Build / test instructions are documented after code import.
- [ ] CI is configured after code import.

### Safety / hygiene before code import

- [ ] Search for API keys, tokens and credentials.
- [ ] Remove private URLs and local dataset locations.
- [ ] Remove personal absolute paths such as `file:///Users/...`.
- [ ] Review generated binaries and large artifacts.
- [ ] Verify public documentation links.

### Scientific claims

Before using strong terms such as `SOTA`, `solved`, `zero hallucination`, `fully understands`, or `AGI`, attach a reproducible public protocol and supporting result.

---

## Dated decisions and assessments

The records below preserve original reasoning. Their source dates matter. Current ownership/structure is defined by AGENTS.md and the maintenance decision below; STATUS.md defines the active stage. Old directory paths inside a superseded decision describe its historical layout, not files to recreate.

### Repository maintenance decision — 2026-10-25

- Maintain one root document per topic, with the single current progress queue in STATUS.md.
- Update methods, questions, evidence and corrections in their canonical topic sections; no file-per-method rule, dated supplement, duplicate index or news edition.
- Retain exact sources, evidence qualifications, counterevidence and refutation history. Git preserves old trees; do not maintain an archive subtree merely to retain past text.
- This supersedes ADR0007's directory/publication layout and any conflicting historical contribution instructions. It does not change the research question, vision discipline or Stage-1 decision.

<a id="topic-research-decisions-0001-research-reset"></a>

## Decision 0001 — Research Reset

**Date:** 2026-10-14
**Status:** Accepted

### Context

Clover had accumulated increasingly detailed architecture, performance and benchmark work. The highest question remained valuable, but implementation preferences were beginning to function as assumptions that the research was trying to prove.

### Decision

Reset the project around one stable question:

> **How can a machine understand the real world through vision alone?**

The long-term product goal is a general-purpose robotic brain that forms a visual understanding of the world and uses it to decide and act.

Current mechanisms become hypotheses to be tested against classical and modern prior work.

### Why

Research should search for the best answer to the problem rather than protect an early answer.

### Consequences

- architecture-first development pauses as the organizing principle;
- research map and open questions become first-class assets;
- benchmarks become diagnostic instruments;
- current Clover code is Research Prototype 1;
- future architecture may preserve, transform or remove existing mechanisms.

---

<a id="topic-research-decisions-0002-hardware-is-a-design-variable"></a>

## Decision 0002 — Hardware Is a Design Variable

**Date:** 2026-10-14
**Status:** Accepted

### Context

Earlier Clover work emphasized CPU-first execution. That emphasis risked turning a hardware preference into a scientific prior.

### Decision

CPU, GPU, Metal and other accelerators are design variables selected after understanding the computation required by the research mechanism.

The project will use Apple Silicon M4 as a useful unified-memory research platform, but will not constrain the scientific answer to CPU-only or GPU-only methods.

### Why

The history of modern vision shows that representation learning and scalable computation changed what was possible. Clover should understand that history before deciding which computations belong on which hardware.

### Consequences

- no `CPU > GPU` project claim;
- no separate scientific algorithm solely to fit one device;
- later hardware co-design should map sparse/branch-heavy and dense/batched computation to appropriate processors;
- external GPU resources remain valid for research baselines if needed.

---

<a id="topic-research-decisions-0003-current-representation-is-a-hypothesis"></a>

## Decision 0003 — Current Representation Is a Hypothesis

**Date:** 2026-10-14
**Status:** Accepted

### Context

Clover has explored visual charge, fields, crystallization, CSP, spacetime identity, licences and world-growth mechanisms. These ideas may contain useful contributions, but the project has not established that they are the best representation for the central question.

### Decision

Treat field crystallization, machine-native primitives, explicit world state, licences, spacetime structures and visual-world-compiler ideas as active research hypotheses rather than fixed architecture.

### Why

Modern world models, learned geometry, distributed video representations and robot foundation models provide strong alternative explanations that must be understood before the final representation is selected.

### Consequences

Each hypothesis should document supporting evidence, counter-evidence, open problems and a falsifier. A hypothesis can be removed without changing the project SSOT.

---

<a id="topic-research-decisions-0004-github-is-public-research-record"></a>

## Decision 0004 — GitHub Is the Public Research Record

**Date:** 2026-10-14
**Status:** Accepted

### Context

Clover research previously lived across conversations, local files, specifications and implementation snapshots, creating risk of SSOT drift.

### Decision

`SchoolWhen/Clover` is the public canonical record for current Clover research.

Public GitHub records should contain:

- current research question and principles;
- current status and roadmap;
- research maps and sources;
- active hypotheses;
- architecture and code as they are made public;
- registered experiments/results;
- research decisions;
- clearly marked historical documents.

Exploratory chat or local notes do not override current repository documentation until synchronized through a research decision/update.

### Consequences

Future Clover work should update this repository when a decision materially changes the project's public state.

---

<a id="topic-research-decisions-0005-research-before-reproduction"></a>

## 0005 — Research before reproduction

**Status:** Accepted
**Date:** 2026-10-14

### Context

After the Research Reset, an initial plan proposed quickly reproducing V-JEPA 2, VGGT, OpenVLA and benchmark suites. That would still risk moving into implementation before we understand what the major research families actually solve and where their assumptions differ.

### Decision

The current phase prioritizes **systematic research mapping before reproduction**.

We will first document:

- the representation each route uses;
- its learning objective and data assumptions;
- how it handles space, time, memory, physics and action;
- what has actually been demonstrated;
- what remains unresolved;
- what contradiction it creates for Clover's existing hypotheses.

Reproduction, benchmark comparison and paper-style ablation are deferred until the research landscape is sufficiently clear and Clover has a sharper representation hypothesis.

### Why

The project previously lost time by implementing before fully understanding the problem and prior art. Repeating that pattern with newer models would not fix the underlying research-method issue.

### Consequences

- Research Map depth is now a first-class deliverable.
- Benchmarks are catalogued but not treated as immediate optimization targets.
- Strong external models are studied as evidence and counter-hypotheses, not as components to integrate.
- Existing Clover code remains Research Prototype 1 while the next representation is reconsidered.

### Exit condition

Move into systematic reproduction when we can state, with evidence:

1. what major approaches already solve;
2. their common failure modes;
3. what unresolved capability matters for the robot-brain goal;
4. which Clover hypothesis is worth testing next and why.

---

<a id="topic-research-decisions-0006-main-is-canonical-during-research"></a>

## ADR 0006 — `main` Is the Canonical Research Branch During the Mapping Phase

**Status:** Accepted
**Date:** 2026-10-14

### Context

Clover is currently in a research-mapping phase rather than a multi-team implementation phase. Keeping long-lived research branches creates unnecessary divergence between the public record and the current research conclusions.

### Decision

During the current phase:

- `main` is the canonical public research record;
- temporary branches may be used for atomic edits or review;
- once merged, temporary branches should contain no unique research content and should be deleted;
- important changes are preserved through commits, PR history and ADRs rather than long-lived branches.

### Consequence

Research readers should treat `main` as current unless a document explicitly states that it is historical or superseded.

---

<a id="topic-research-decisions-0007-survey-foundation-is-primary-entry"></a>

## ADR 0007 — Survey Foundation Is the Primary Research Entry

**Date:** 2026-10-14
**Status:** SUPERSEDED for directory/publication layout on 2026-10-25. Scientific source-classification discipline is retained.

### Context

The public Clover repository initially grew through a research map, literature notes, evaluation notes and hypothesis pages. That structure was useful for bootstrapping, but the research surface became fragmented: a new reader had to traverse many small files before seeing the full landscape.

At the same time, three substantial source documents existed outside the repository:

- the 2026-10-14 Research Reset;
- the accumulated news / frontier archive;
- the post-screening news decisions and hypotheses.

These sources contain useful research material, but they also contain historical assumptions, pre-reset commitments, secondary reports and implementation-specific decisions that should not be copied into the current SSOT unchanged.

### Decision

Historical decision (2026-10-14): create a content-heavy survey layer. Its directory structure was replaced by root-level topic documents on 2026-10-25.

The survey contains:

- a single overview README;
- frontier methods;
- papers / primary sources;
- benchmarks and embodied tasks;
- datasets and code resources;
- cross-cutting research questions;
- screened Clover hypotheses;
- screened frontier signals.

The three historical source documents are **synthesized, not raw-imported**. A statement enters the survey only after being classified as one of:

- primary scientific evidence;
- official reported result;
- research hypothesis;
- frontier signal;
- historical context.

The former research-map and literature notes have now been merged into canonical root documents; their earlier paths remain recoverable in Git history.

### Why

A flatter survey layer makes it possible to answer, quickly and in one place:

1. What is already known?
2. What are the strongest current methods?
3. What evidence supports them?
4. What are the available papers, codebases, datasets and benchmarks?
5. What remains unresolved for Clover's SSOT?
6. Which old Clover ideas remain legitimate hypotheses after the Research Reset?

### Consequences

- Historical layout only: the survey layer was the research navigation surface; current entry is RESEARCH.md plus SOURCES.md.
- Root `AGENTS.md` and `SSOT.md` become mandatory orientation files for agents and contributors.
- Current rule: frontier additions update the existing topic and SOURCES.md; no dated fragment files or news archive are added.
- Research notes may remain exploratory, but no note becomes current project truth without updating the relevant survey/SSOT/status material.
- Code-generation/versioning remains out of scope for this decision.

---

<a id="topic-research-decisions-0008-background-research-before-representation"></a>

## 0008 — Background research before representation hypothesis

**Status:** Accepted
**Date:** 2026-10-14
**Clarifies:** 0005 — Research before reproduction

### Context

The 2026-10-14 Research Reset explicitly requires Clover to establish strong baselines, a capability map and a benchmark battery before proposing the next representation hypothesis.

ADR 0005 correctly established that Clover should not rush directly into reproducing large frontier systems. However, one phrase in 0005 could be read as waiting for a sharper representation hypothesis **before** systematic baseline comparison. That ordering would risk reintroducing the old failure mode: choosing a representation first and then collecting evidence around it.

The Research Reset instead gives the stronger sequence:

```text
Research Map
→ Baseline Setup
→ Understanding Battery
→ Failure Matrix
→ Representation Hypothesis
```

### Decision

Clover's active phase ordering is:

```text
Background Research / Problem Reconstruction
→ Baseline Reconstruction
→ Understanding Battery
→ Failure Matrix
→ Representation Hypothesis
→ World Formation / Learning
→ Robot Brain
→ Real-world Evaluation
→ Hardware Co-design
```

Background research must be primary-source-backed and broad enough to include classical vision, modern self-supervised image/video learning, learned geometry, object-centric models, persistent memory, intuitive physics, causality, active perception, generative world models, VLM/VLA/world-action models and real robot foundation systems.

Baseline work is permitted and eventually required **before** a representation is frozen, when it is used to answer discriminating research questions rather than to optimize a leaderboard.

### What this changes

- `RESEARCH.md` and `SOURCES.md` become primary research surfaces.
- DINOv3, V-JEPA 2/2.1, VGGT/Ω, SAM 3.1 and strong embodied systems are treated as current comparators.
- Persistent memory, anti-shortcut physics, causal/interventional evaluation and active perception become first-class research dimensions.
- The next Clover representation is not selected until the baseline/battery/failure-map evidence exists.

### What this does not change

ADR 0005 remains correct that:

- reproduction is not an end in itself;
- benchmarks are instruments;
- external systems are counter-hypotheses/evidence rather than modules to stack into Clover;
- large expensive reproduction should wait until a smaller study cannot answer the relevant research question.

This ADR only clarifies the **ordering**: a representation hypothesis is downstream of baseline evidence, not a prerequisite for obtaining it.

### Consequences

A future architecture proposal must cite the failure matrix and state which observed cross-family failure it is intended to solve.

The following are not sufficient reasons to create a new mechanism:

```text
historical Clover already has it
another paper uses it
it sounds machine-native
it is faster on one benchmark
it fits the local hardware well
```

The admissible chain is:

```text
background evidence
→ unresolved contradiction
→ discriminating baseline/battery result
→ candidate representation
→ falsifier
→ implementation
```

### Final rule

> **Do not choose the answer before measuring the problem.**

---

<a id="topic-research-decisions-0009-seven-stage-research-lifecycle"></a>

## ADR 0009 — Flat Seven-Stage Research Lifecycle

Date: 2026-10-14
Status: **ACCEPTED**

### Context

The repository accumulated several useful but overlapping process descriptions: background research, baseline setup, Understanding Battery, Failure Matrix, representation hypothesis, world formation, robot brain, evaluation and hardware co-design.

Those terms describe important activities, but as top-level phases they made the project harder for a new agent to parse and mixed research maturity with evaluation assets and system layers.

The project needs a simpler canonical lifecycle that matches normal scientific work and keeps the current foundation stage broad.

### Decision

Use one flat lifecycle:

```text
1 Research
→ 2 Analysis
→ 3 Synthesis
→ 4 Innovation
→ 5 Implementation
→ 6 Evaluation
→ 7 Reflection
↺ next cycle
```

#### Research
Collect fields, sources, methods, code, datasets, benchmarks and open questions.

#### Analysis
Produce method-by-method mechanism reports.

#### Synthesis
Compare capabilities, mechanisms, pros/cons, trade-offs, failures and gaps.

#### Innovation
Formulate Clover-original hypotheses and algorithms from demonstrated gaps.

#### Implementation
Build reproducible baselines, diagnostics and selected Clover ideas.

#### Evaluation
Run experiments, Results, ablations, generalization and real-world tests.

#### Reflection
Interpret results, reject failed assumptions and feed the next cycle.

### Current stage

**Stage 1 Research is active.**

The immediate priority is broad material collection rather than architecture design.

### How earlier process concepts map into the lifecycle

- **Research Map / Background Research** → Research.
- **Baseline inventory** → Research; baseline mechanism study → Analysis; baseline code → Implementation.
- **Understanding Battery** → Evaluation design.
- **Failure Matrix** → Synthesis, informed by Analysis/Evaluation.
- **Representation Hypothesis** → Innovation.
- **World Formation / Robot Brain** → Innovation/Implementation depending maturity.
- **Real-world Evaluation** → Evaluation.
- **Hardware co-design** → Implementation/Evaluation after scientific structure is known.

These concepts remain useful. They are no longer separate top-level project phases.

### Consequences

1. New agents have a simple first-entry model of the project.
2. Stage 1 can remain wide and include any relevant field without forcing it into the existing eight dossiers.
3. Method reports get a clear home in Analysis.
4. Pros/cons and field-level conclusions get a clear home in Synthesis.
5. Historical Clover ideas are naturally classified as Innovation candidates rather than hidden assumptions.
6. Code and scientific validation remain distinct.
7. Negative results feed Reflection rather than being patched automatically.

### Non-decision

This ADR does not choose a Clover representation, learning objective, architecture, benchmark or hardware strategy.

It changes only the research operating model.

---

<details>
<summary>Readiness assessment dated 2026-10-15 — historical context; current status is in STATUS.md</summary>

<a id="topic-research-stage1_final_audit_2026-10-15"></a>

## Stage 1 Final Audit — 2026-10-15

> Dated audit record: 2026-10-15. Its recommendation to make Stage 2 primary was not the subsequent project decision. Stage 1 remains active; see STATUS.md. Read readiness claims below as that audit’s assessment, not a current completeness finding.

> Research question: **How can a machine understand the real world through vision alone?**

This audit checks whether Stage 1 still has missing *major domains* after expanding from visual world modeling into identifiability, memory, causality, model discovery, foundation-model systems, training/post-training, deployment and validation.

### Audit conclusion

**No obvious major research domain is currently missing.**

The remaining work is dominated by **cross-boundary controlled-variable problems** rather than new top-level categories.

The important implication is:

```text
Stage 1 should remain open to freshness updates,
but Stage 2 can become the primary mode once these boundaries are recorded.
```

Do not interpret this as “research is complete forever.” It means the broad problem map is sufficiently complete that continued collection should be selective and evidence-driven.

---

### 1. Cross-boundary priorities

### P0 — must be understood before serious architecture selection

#### P0.1 Visual tokenizer / video sampling

The effective observation path is:

```text
world
→ optics / camera
→ RGB
→ resize / crop / ISP
→ frame sampling
→ visual tokenizer / patching / pixel-unshuffle / pooling
→ token pruning / merging
→ backbone
→ internal state
```

The tokenizer is therefore part of the sensing pipeline, not merely an implementation detail.

Current evidence to track:

- Qwen2.5-VL dynamic FPS + absolute-time encoding: https://qwen.ai/blog?from=research.research-list&id=c5e7415d9a9e89adc18c59d9e466e5a1a459b8f4
- Qwen3-VL: https://github.com/QwenLM/Qwen3-VL
- SAPrune / stage-aware VLA token pruning: https://arxiv.org/abs/2610.05273
- VLA-ACL / action-consistent token pruning: https://arxiv.org/abs/2610.08133
- adaptive two-stage video token pruning: https://arxiv.org/abs/2608.03112

Required future experiment:

```text
same raw video
same checkpoint
vary resolution / FPS / token count / pruning policy
```

Measure geometry, fast contact, permanence, uncertainty, OOD behavior, action stability, latency and memory.

A model must not be blamed for missing evidence that the tokenizer already discarded.

---

#### P0.2 Streaming foundation models

A robot receives an unbounded stream; it should not be modeled as repeated independent chat prompts.

Study:

```text
incremental visual encoding
frame reuse
cache invalidation
bounded history
periodic global refresh
fast local state update
slow semantic/planning update
stream interruption / resume
```

DeepSeek-V4.1-Flash is relevant because its Causal Encoder–Decoder explicitly separates input-heavy and output-heavy compute: https://www.deepseek.com/en/news/deepseek-v4-1-flash/

Qwen3.8-Omni-Flash and Qwen-Live-Harness are useful runtime comparators for continuous multimodal streams, although audio is outside strict Clover V0–V3 sensing: https://qwen.ai/blog?id=qwen3.8-omni-flash · https://github.com/QwenLM/Qwen-Live-Harness

Required metrics:

```text
incremental latency
full-refresh latency
state staleness
frame backlog
dropped/reordered frame robustness
cache growth
memory leak
p95/p99 camera→action deadline
```

---

#### P0.3 Long context vs grounded world memory

Long context is a computational resource. It is not automatically:

```text
persistent world belief
belief revision
evidence provenance
identity memory
```

Current multimodal memory evidence:

- M3Exam shows persistent gaps and efficiency costs in multimodal long-context memory, while query-conditioned memory can reduce retrieved tokens: https://arxiv.org/abs/2606.07402
- ICM-Bench isolates long-term identity memory rather than generic event recall: https://arxiv.org/abs/2609.04438

Required equal-budget comparison:

```text
A raw long context
B persistent state
C evidence retrieval
D hybrid state + evidence + bounded recent context
```

Match bytes, peak memory and latency as far as possible.

---

#### P0.4 Backbone adaptation

Compare under matched data/compute:

```text
frozen backbone + state/action head
LoRA / adapter
selective visual-language adaptation
partial fine-tuning
full fine-tuning
teacher→student distillation
```

Current controlled evidence:

- π0 LoRA vs full fine-tuning study: https://arxiv.org/abs/2607.10172
  - some LoRA settings match full tuning on the evaluated industrial tasks;
  - over-freezing the VLM/vision path can hurt embodiment adaptation.
- Qwen-Drive demonstrates another design family: keep the pretrained Qwen3.5-4B VLM architecture and add explicit BEV/perception/planning modules: https://qwen.ai/blog?id=qwen-drive-1.0

Future selection must jointly consider adaptation quality, catastrophic forgetting, calibration, memory, OOD vision and deployment cost.

---

### 2. P1 research variables

### P1.1 Data science / data alignment

Do not summarize robot data by `hours` alone.

Record:

```text
unique scenes
objects
tasks
embodiments
operators
camera setups
success/failure/recovery distribution
real/human/sim/generated fractions
alignment method
retargeting error
temporal synchronization
deduplication / leakage
curriculum / sampling ratio
```

High-value current evidence:

- Qwen-RobotManip uses ~38.1K hours across robot, egocentric human and synthesized human→robot data, but emphasizes representation/motion/behavior alignment before scale: https://qwen.ai/blog?id=qwen-robotmanip
- Rethinking VLA Scaling finds naive heterogeneous robot pooling can cause negative transfer: https://arxiv.org/abs/2602.09722

Open question:

> Does the best robot/human/sim/generated mixture change with model scale and representation capacity?

No universal mixture is currently justified.

---

### P1.2 Quantization as a capability intervention

Low-bit inference should not be evaluated only by average task success.

Current evidence:

- FoldQuantVLA: https://arxiv.org/abs/2609.24433
- LiteVLA-Edge: https://arxiv.org/abs/2603.03380

Required measurements:

```text
nominal success
OOD success
uncertainty calibration
unknown/refusal
rare-event sensitivity
object identity/permanence
belief revision
long-horizon drift
action smoothness/contact stability
latency/memory/energy
```

Keep distinct:

```text
PTQ
QAT
quantization-aware / quantization-conditioned post-training
```

A quantized model may need additional post-training; that gain must not be attributed to quantization alone.

---

### P1.3 Small→large scaling validity

Mac-M4 experiments will often use 2B/4B/8B proxies.

Required protocol:

```text
small-model discovery
→ medium replication
→ large/frontier counter-check
```

Track whether the effect changes with:

```text
parameter count
active parameters
MoE routing
context length
visual-token budget
data mixture
precision
runtime backend
```

A 4B result is not a 30B/MoE result by default.

---

### P1.4 Harness attribution

Modern benchmarks can measure a full system rather than the base model.

Ablate:

```text
base model
+ prompt/protocol
+ external memory
+ visual/perception helper
+ tools/MCP
+ retry/recovery
+ full harness
```

Track token cost, latency and memory together with capability.

DeepSeek and Qwen make this particularly important because both expose explicit harness/runtime layers.

---

### 3. P2 — understand but do not let systems detail dominate science

Track enough of the following to reproduce feasibility claims:

```text
data/tensor/pipeline/expert/context parallelism
network topology
all-to-all / expert communication
storage bandwidth
checkpoint/optimizer size
custom kernels
Muon/AdamW variants
mHC/hyper-connections
speculative decoding
multi-token prediction
```

DeepSeek references:

- DeepEP — https://github.com/deepseek-ai/DeepEP
- DeepGEMM — https://github.com/deepseek-ai/DeepGEMM
- DeepSelect — https://github.com/deepseek-ai/DeepSelect
- 3FS — https://github.com/deepseek-ai/3FS

These affect feasibility and scaling. They are not evidence that a world-state representation is scientifically superior.

---

### 4. Training/post-training high-risk boundaries

The detailed matrix is in [`LEARNING.md`](LEARNING.md#topic-research-training-high_risk_boundaries).

Stage 1 now explicitly requires research on:

```text
partial-success reward
reward for epistemic correctness
failure/recovery sampling ratio
recovery-vs-nominal interference
world-model trust controlling imagined rollout
human/sim/robot mixture × model scale
frozen vs LoRA vs partial vs full tuning
module-specific learning rates/update frequencies
slow semantic vs fast motor adaptation
post-training calibration degradation
world-capability regression despite task success
capability loss under distillation
4B→MoE recipe transfer
fleet contamination / update admission
model rollback ↔ persistent-memory compatibility
```

Important current reward evidence:

- RoboReward constructs calibrated negatives, near-misses and partial-progress outcomes for robotics reward modeling: https://arxiv.org/abs/2601.00675
- SARM2 uses stage-aware dense reward for long-horizon robot policy improvement: https://arxiv.org/abs/2606.10305
- TOPReward extracts temporal task-progress signals from VLM token probabilities: https://arxiv.org/abs/2602.19313
- MERL uses simulator trust to control imagined-data ratio and rollout horizon: https://arxiv.org/abs/2610.16517

No universal failure-data percentage, recovery ratio, real/human/sim mixture or tuning method is currently justified.

---

### 5. Training curriculum itself is part of the scientific comparison

Current Qwen robot systems make this especially visible.

### Qwen-VLA

Official description uses four stages:

```text
T2A pretraining
→ continual pretraining
→ SFT
→ PPO RL in simulation
```

Source: https://qwen.ai/blog?id=qwenvla

This means final behavior cannot be attributed to the backbone alone.

### Qwen-RobotManip

Official training uses:

```text
VLA/VLM dual-stream pretraining at ~9:1
→ benchmark/generalist SFT
→ continued VLA+VL co-training during post-training
```

Source: https://qwen.ai/blog?id=qwen-robotmanip

### Qwen-RobotWorld

Uses a general→expert curriculum combining general image/video priors, human-interaction data and progressive embodied SFT stages including multi-view and cross-domain training.

Source: https://qwen.ai/blog?email_hash=23463b99b62a72f26ed677cc556c44e8&id=qwen-robotworld

Central rule:

```text
architecture result
≠ training-curriculum result
```

---

### 6. Final audit additions beyond the original P0/P1/P2 list

These are not new project stages. They are cross-cutting constraints that should remain visible.

### A. Runtime safety / formal safety interface

Task success can coexist with unsafe behavior.

Track:

```text
unsafe-success
risk exposure time
constraint violations
collision/force/workspace limits
safety-layer intervention rate
recovery after intervention
```

Current sources:

- VLA safety survey: https://arxiv.org/abs/2604.23775
- AEGIS / plug-and-play CBF safety layer: https://arxiv.org/abs/2512.11891
- FEARL / verifiable modular safety: https://arxiv.org/abs/2606.23754
- ForesightSafety-VLA: https://arxiv.org/abs/2606.27079

A safety filter is not proof that the underlying world model is safe or correct; but deployment evidence without a safety analysis is incomplete.

---

### B. Statistical / reproducibility discipline for real robots

Real-robot evaluation is expensive and noisy.

Required metadata:

```text
number of trials
number of seeds/checkpoints
operator identity / blinding
initial-state randomization
hardware/calibration version
confidence intervals / variance
failure taxonomy
selection criterion
```

Rethinking VLA Scaling introduces a grouped blind ensemble protocol to reduce operator/model-identity bias during real evaluation: https://arxiv.org/abs/2602.09722

One impressive video or one lucky checkpoint is not sufficient evidence.

---

### C. Reward/verifier reliability

A learned reward can itself hallucinate progress or be exploited.

Reward-model evaluation should be independent from policy evaluation and include:

```text
false-positive success
near-miss ranking
stage ordering
OOD task transfer
reward hacking
reward uncertainty
human agreement
```

Reward-model improvement and policy improvement are distinct claims.

---

### D. Artifact drift / API routing / benchmark contamination

Preserve exact:

```text
model/checkpoint/API version
release date
API route
harness version
runtime/kernel version
benchmark snapshot
training-data cutoff/provenance if known
```

Vendor release plans can change after publication. Current-state claims should prefer the latest official changelog/status page over an older launch announcement.

Example: DeepSeek's 2026-09-10 launch post initially said V4-Pro requests would be routed to V4.1-Flash after Sept 14, while the later API changelog states V4 Pro would continue to be served. Current record must preserve the later status.

DeepSeek launch: https://www.deepseek.com/en/news/deepseek-v4-1-flash/
DeepSeek API changelog: https://api-docs.deepseek.com/updates/

---

### 7. Stage-1 readiness judgment

The broad map now covers:

```text
world / observation / identifiability
representation / state / memory / causality
active evidence / model discovery
foundation-model architecture / tokenizer / context / runtime
training / post-training / data / reward
edge deployment / simulation / sim2real / validation
runtime safety / monitoring / rollback
```

Therefore the recommended project mode is now:

```text
Stage 1 = incremental freshness + gap maintenance
Stage 2 = primary method-by-method analysis
```

Stage 1 should reopen a major category only if new evidence shows that an entire capability class is absent from the map.

Otherwise new work should be attached to an existing surface and tested as a controlled variable.

---

### 8. Highest-priority Stage-2 experiments implied by this audit

1. **Visual-token / FPS ablation** on a tractable open Qwen VLM/VLA proxy.
2. **Equal-byte long-context vs persistent-memory comparison**.
3. **Frozen vs LoRA vs partial tuning** under matched robot data.
4. **BC vs co-training vs future-latent auxiliary vs on-policy distillation**.
5. **Post-training preservation battery**: task success + permanence + memory revision + causal probes + calibration.
6. **Quantization before/after post-training** and capability regression.
7. **Failure/recovery ratio sweep** under fixed total data budget.
8. **World-model trust vs imagined rollout horizon**.
9. **Small dense proxy → larger dense/MoE replication**.
10. **Base model vs harness/memory/tools ablation**.

These experiments are downstream candidates, not Stage-1 conclusions.

</details>

---

<details>
<summary>Second-pass assessment dated 2026-10-15 — historical context; current status is in STATUS.md</summary>

<a id="topic-research-emerging-reaudit_summary_2026-10-15"></a>

## Stage-1 Re-audit Summary — 2026-10-15

> Dated audit record: 2026-10-15. Its recommendation to make Stage 2 primary was not the subsequent project decision. Stage 1 remains active; see STATUS.md. Read readiness claims below as that audit’s assessment, not a current completeness finding.

This note records the **second-pass audit** triggered by recent EmbodiedJev / AgentRSI / embodied-JEPA / recursive-self-improvement developments and a fresh arXiv/GitHub scan across computer vision, embodied intelligence, physical intelligence, frontier foundation-model engineering and performance optimization.

It supersedes the assumption that the earlier `PROCESS.md` was the last search pass. It does **not** change Clover's seven-stage lifecycle.

Detailed audits:

- [`SYSTEMS.md`](SYSTEMS.md#topic-research-emerging-jepa_rsi_runtime_2026-10-15)
- [`SYSTEMS.md`](SYSTEMS.md#topic-research-emerging-cv_embodiment_systems_2026-10-15)
- [`REPRESENTATION.md`](REPRESENTATION.md#topic-research-emerging-representation_diagnostics_2026-10-15)

---

### Re-audit conclusion

No missing foundational domain comparable to geometry, memory, causality, identifiability, world-state representation, training or deployment was found.

However, several **fast-moving cross-boundary method families** were underweighted and are now first-class comparison axes:

```text
1  embodied JEPA / latent predictive control
2  cross-embodiment latent action representations
3  test-time policy scaling: verifier / Best-of-N / search
4  WAM inference-state reuse, verification and staleness
5  fast-weight / retrieval / gradient / verifier forms of test-time adaptation
6  recursive self-improvement of model / harness / data / research process
7  embodied recursive improvement / Real2Sim2Real policy refinement
8  process-level RSI evaluation, held-out transfer and lineage
9  generative video foundation models used as perception representations
10 multi-view geometry-aware world modeling
11 morphology-conditioned world models / body schema
12 affordance foundation models / functionality representations
13 alternative visual-sensing boundary such as event cameras
14 mechanistic / causal representation diagnostics
15 manipulation-video continued pretraining as part of WAM design
16 multi-robot edge serving / SLO scheduling
17 explicit state + reusable code policy as a counter-hypothesis to always-on VLA/WAM
```

These belong to existing Stage-1 surfaces. They do not require new lifecycle stages.

---

### High-value current sources added in this pass

#### Embodied JEPA / latent dynamics

- RoboJEPA — https://arxiv.org/abs/2610.10515 · https://github.com/facebookresearch/robo_jepa
- ThinkJEPA — https://arxiv.org/abs/2603.22281
- Demo-JEPA — https://arxiv.org/abs/2605.20811
- LeapBot-WA — https://arxiv.org/abs/2607.23969
- SkyJEPA — https://arxiv.org/abs/2606.23444
- Vision-Predictor-Action — https://arxiv.org/abs/2610.15556
- LeWAM (end-to-end JEPA/action) — https://arxiv.org/abs/2610.12818
- LeWAM (diffusion-steering MPC) — https://arxiv.org/abs/2610.12407

The two different `LeWAM` papers are a concrete reason to identify methods by exact title + arXiv ID + authors/version rather than acronym alone.

#### Embodiment / action / body

- LAC-WM — https://arxiv.org/abs/2610.10846
- morphology-conditioned quadrupedal world model — https://arxiv.org/abs/2604.08780
- diffusion body-schema learning under actuator/body faults — https://arxiv.org/abs/2608.01029
- AFUN affordance foundation model — https://arxiv.org/abs/2606.02551

#### Test-time adaptation / runtime

- DiVeR — https://arxiv.org/abs/2610.04933
- RoboTTT — https://arxiv.org/abs/2607.15275
- RA-VLA — https://arxiv.org/abs/2608.25585
- MARS — https://arxiv.org/abs/2610.17141 · https://github.com/PKU-VaLuE-Lab/MARS
- Δ Flow Matching — https://arxiv.org/abs/2610.15794
- WAMachine — https://arxiv.org/abs/2609.34608
- AsyncVLA — https://arxiv.org/abs/2602.13476
- Efficient VLA serving / Robion — https://arxiv.org/abs/2609.12075

#### World-model / visual-representation boundaries

- Thinker-WM — https://arxiv.org/abs/2610.18447
- EVEWorld — https://arxiv.org/abs/2610.03374
- RLHND — https://arxiv.org/abs/2610.09455
- PAIWorld — https://arxiv.org/abs/2606.18375
- Video Prediction Policy 2 — https://arxiv.org/abs/2610.10270
- EventCV — https://arxiv.org/abs/2609.21330

#### Recursive self-improvement

- AIDE² — https://arxiv.org/abs/2609.26457
- RRSI — https://arxiv.org/abs/2609.24972 · https://github.com/google-research/rrsi
- RSI-Master — https://arxiv.org/abs/2609.35561
- RSI-Forge — https://arxiv.org/abs/2610.09426
- RSIGym — https://arxiv.org/abs/2610.10310
- HELIX — https://arxiv.org/abs/2608.13951
- Harmony Harness — https://arxiv.org/abs/2610.15150
- Harness² — https://arxiv.org/abs/2610.14224
- AReaL-RSI — https://arxiv.org/abs/2610.18083
- EmbodiRSI — https://arxiv.org/abs/2609.38905
- RegenHarness — https://arxiv.org/abs/2609.27612
- Embodied Turing Machines / COAP — https://arxiv.org/abs/2610.12369

---

### GitHub projects classified separately from primary papers

#### EmbodiedJev / 行知

https://github.com/FBddcz/embodied-jev

Classification: `OPEN_SOURCE_PROJECT / ENGINEERING_REFERENCE`.

Useful for:

```text
MuJoCo + Franka local workbench
Mac/local API experiments
controlled same-task model comparison
trajectory export/replay
pre-execution simulation checks
EV1 / EV6 validation workflow ideas
```

Do not attribute controller-provided candidates, geometry or safety checks to the model itself.

#### AgentRSI

https://github.com/heng526/AgentRSI

Classification: `COMMUNITY_RESEARCH_REPOSITORY`.

Useful for:

```text
RSI literature / reproduction organization
append-only ResearchOps evidence records
robot scoring reports
research ledger / reducer workflow ideas
```

Do not treat repository organization as primary scientific evidence for an RSI method.

---

### New non-negotiable distinctions

```text
probe recoverability ≠ causal use ≠ closed-loop physical consequence
base VLA ≠ VLA + verifier/search/test-time compute
cross-embodiment state alignment ≠ cross-embodiment action alignment
history in KV/context ≠ explicit memory ≠ fast-weight memory
inference-state reuse ≠ inference-state validity
fast-path + slow-path ≠ synchronized closed-loop system
self-editing ≠ recursive self-improvement
RSI evolve-set gain ≠ held-out/OOD improvement
model RSI ≠ harness RSI ≠ data RSI ≠ research-process RSI ≠ embodied RSI
frame RGB ≠ all possible visual sensing
world dynamics ≠ robot morphology/body dynamics
object semantics ≠ affordance/function
single-robot latency ≠ fleet edge-serving SLO reliability
method acronym/name ≠ stable artifact identity
```

---

### DeepSeek / Qwen status in this re-audit

No newly verified DeepSeek/Qwen release in this pass requires replacing the current stable watch in:

- [`SYSTEMS.md`](SYSTEMS.md#topic-research-foundation_models-deepseek_qwen)
- [`SYSTEMS.md`](SYSTEMS.md#topic-research-foundation_models-deepseek_qwen_current_2026-10-15)

The new RSI/runtime evidence **strengthens**, rather than replaces, the existing model-systems rule:

```text
checkpoint
+
post-training
+
runtime/kernel
+
harness/tools/memory
+
test-time compute
+
hardware / serving topology
→ observed system capability
```

For DeepSeek/Qwen comparisons, continue recording the exact API/checkpoint, reasoning-effort setting, harness/plugin configuration, external memory/tools and artifact date.

---

### Stage-1 status after the re-audit

Stage 1 remains **coverage-sufficient but freshness-active**.

Recommended operating mode:

```text
Stage 1: incremental frontier maintenance
Stage 2: primary method-by-method mechanism analysis
```

Future additions should change at least one of:

```text
what information is observable
what state is represented
how state is learned / updated
how action is chosen
how uncertainty/evidence is handled
how the system is trained / adapted
how the runtime changes behavior
how claims are validated
```

Otherwise, log the work as a comparator/source rather than expanding the stable ontology.

</details>

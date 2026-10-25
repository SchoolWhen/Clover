<a id="top"></a>

# Research process and shared constraints

Maintained: **2026-10-25**. This file applies to all seven stages. [`SSOT.md`](SSOT.md) defines the fixed scientific contract; [`AGENTS.md`](AGENTS.md) defines agent behavior; [`STATUS.md`](STATUS.md) alone records current progress and the active stage.

<a id="topic-research-pipeline"></a>
<a id="lifecycle"></a>

## Lifecycle and stage ownership

Research → Analysis → Synthesis → Innovation → Implementation → Evaluation → Reflection → next cycle.

Stages describe evidence maturity. Moving a file or creating a directory does not produce a result or pass a stage gate. Earlier hypotheses and future templates may be recorded while Stage 1 remains active.

| 阶段 | 唯一阶段入口 | 内容归属 |
|---|---|---|
| 1. Research / 调研 | [01-research/](01-research/README.md) | 调研方向、来源、资源、证据边界与未解问题 |
| 2. Analysis / 分析 | [02-analysis/](02-analysis/README.md) | 逐方法机制、假设、混淆与复现分析 |
| 3. Synthesis / 综合 | [03-synthesis/](03-synthesis/README.md) | 统一口径比较、能力/失败矩阵与证据缺口 |
| 4. Innovation / 创新 | [04-innovation/](04-innovation/README.md) | 原创假设、数学表述、预言、反证与候选想法 |
| 5. Implementation / 实现 | [05-implementation/](05-implementation/README.md) | 代码、依赖、配置、实现状态与可复现入口 |
| 6. Evaluation / 评测 | [06-evaluation/](06-evaluation/README.md) | 实验注册、协议、测量、结果、消融与失败 |
| 7. Reflection / 反思 | [07-reflection/](07-reflection/README.md) | 解释证据、更新假设状态与下一轮问题 |

## Common gates

- Research records primary/official sources, exact artifacts, observation/training provenance, demonstrated capability, limitations and open gaps. Coverage precedes commitment.
- Analysis explains individual mechanisms, assumptions, objectives, memory/time treatment, confounds and reproducibility; it does not select Clover's architecture by popularity.
- Synthesis compares methods under common dimensions, separates protocol differences from capability differences and identifies a supported unresolved gap.
- Innovation states an original scientific/algorithmic hypothesis, mathematical definitions, prediction, counter-hypothesis, falsifier and minimal discriminating experiment.
- Implementation records code/configuration, dependencies, data/model versions, input/output protocols, seeds, instrumentation and limitations. Code existence is not validation.
- Evaluation freezes protocol, splits, baselines, metrics and pass/kill criteria before measuring. Record results, uncertainty, failures and full performance boundaries; external reports remain external.
- Reflection identifies what survived, failed or remained ambiguous, attributes failure and updates the hypothesis or next research question from evidence.

Small diagnostics may occur before the core Implementation stage when necessary to resolve a named research question. Expensive reproduction is justified only when a smaller study cannot settle that question. Stage-specific templates are maintained in their stage README, not repeated here.

## Structure and current-record policy

- The root contains only cross-stage rules/status, the homepage and repository metadata. Homepage artwork is in `.github/`.
- Each numbered stage owns its work. Stage 1 is flat by research direction; subsequent stages begin with one substantive README and add a direction file only for distinct continuing content.
- Update one current document per direction in place. A paper or subproblem is a section, not automatically a file. No dated update fragments, duplicate indexes, redirect shells or archive subtree.
- Link to upstream evidence and stable IDs rather than copying it across phases. In particular, benchmark literature stays in Stage 1; registered experiments/results stay in Stage 6.
- Git preserves prior versions. Source check dates and reading-depth labels remain unchanged by restructuring; dated judgments remain dated.
- The stage layout supersedes the earlier all-root topic layout and ADR0007's older directory layout. It changes neither the research question nor evidence standards nor the current stage.

<a id="topic-contributing"></a>

## Contributing to Clover

Clover is a research project. A contribution should clearly belong to one stage of the canonical lifecycle:

```text
Research → Analysis → Synthesis → Innovation → Implementation → Evaluation → Reflection
```

The current primary stage is recorded only in [STATUS.md](STATUS.md).

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

When deeper method study becomes appropriate, use the method template in [02-analysis/README.md](02-analysis/README.md).

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
- [x] Shared contract, global status, process and stage-specific contribution templates exist.
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
## Dated research decisions

The source dates below qualify these records. Directory/publication rules in historical decisions are superseded by the structure policy above. The global active stage is determined by STATUS.md, not a readiness recommendation or an old roadmap.


---

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

Historical decision (2026-10-14): create a content-heavy survey layer. Its directory structure was replaced on 2026-10-25; the current numbered-stage layout is defined above.

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

The former research-map and literature notes have now been merged into canonical stage/direction documents; their earlier paths remain recoverable in Git history.

### Why

A flatter survey layer makes it possible to answer, quickly and in one place:

1. What is already known?
2. What are the strongest current methods?
3. What evidence supports them?
4. What are the available papers, codebases, datasets and benchmarks?
5. What remains unresolved for Clover's SSOT?
6. Which old Clover ideas remain legitimate hypotheses after the Research Reset?

### Consequences

- Historical layout only: the survey layer was the research navigation surface; current entry is the Stage-1 overview and its source/resource direction.
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

- `01-research/README.md` and `01-research/sources-and-resources.md` become primary research surfaces.
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

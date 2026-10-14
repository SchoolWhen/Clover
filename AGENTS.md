# AGENTS.md — Clover Project Instructions

This file is mandatory reading for any AI agent, coding agent, research agent, or human contributor working in this repository.

## 1. Highest SSOT

The highest research question is:

> **How can a machine understand the real world through vision alone?**

The long-term product goal is:

> **Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.**

The research question is fixed. The answer is open.

## 2. Mandatory reading order

Before proposing architecture, code, experiments, or research conclusions, read:

1. [`SSOT.md`](SSOT.md)
2. [`PRINCIPLES.md`](PRINCIPLES.md)
3. [`STATUS.md`](STATUS.md)
4. [`research/survey/BACKGROUND_RESEARCH.md`](research/survey/BACKGROUND_RESEARCH.md)
5. [`research/survey/SOURCE_MAP.md`](research/survey/SOURCE_MAP.md)
6. [`research/survey/README.md`](research/survey/README.md)
7. the relevant research questions, hypotheses and decision records.

Historical documents and news notes are evidence/signal sources, not SSOT.

## 3. Current phase

Clover is currently in a **Background Research / Problem Reconstruction** phase.

The active research order is:

```text
Background Research / Research Map
→ Baseline Setup
→ Understanding Battery
→ Failure Matrix
→ Representation Hypothesis
→ World Formation / Learning
→ Robot Brain
→ Real-world Evaluation
→ Hardware Co-design
```

Do **not** freeze a new representation, rewrite the core architecture or optimize a historical Clover mechanism before the baseline/battery/failure-map evidence exists.

Minimal baseline reconstruction or probing is allowed when it answers a discriminating research question and cannot be answered more cheaply by reading/analysis. Large reproduction campaigns and leaderboard optimization remain downstream.

## 4. Non-negotiable research rules

### 4.1 Do not protect an old answer

The following are hypotheses or engineering choices, not axioms:

- CPU-first computation;
- GPU-first computation;
- field crystallization;
- visual charge;
- CSP / machine-native primitives;
- SEP;
- epistemic licences;
- LCPS / GCPS;
- Visual World Compiler;
- Evidence Replay;
- explicit state;
- latent state;
- object-centric state;
- Transformer / non-Transformer architecture.

If evidence contradicts them, revise or replace them.

### 4.2 Do not lower the research question

Failure of a current mechanism is not a reason to redefine “understanding” downward.

The project may replace a mechanism, representation, formula, variable, architecture, training objective, benchmark, or hardware plan.

The project does not replace the research question with an easier one.

### 4.3 Background research before representation commitment

A new architecture proposal must be downstream of:

```text
background evidence
→ strong baseline
→ Understanding Battery
→ Failure Matrix
→ unresolved cross-family contradiction
```

Do not choose a preferred representation and then search for supportive papers.

### 4.4 Benchmarks are instruments

Do not optimize the project identity around one benchmark.

A benchmark result is evidence about a capability, not a definition of understanding.

### 4.5 No framework stacking

Do not integrate an external method just because it is strong.

For every external method:

1. identify the contradiction it solves;
2. determine whether Clover has the same contradiction;
3. identify what the source actually demonstrates;
4. record what it does **not** demonstrate;
5. derive a Clover research question or candidate only if justified;
6. define a falsifier;
7. only then consider implementation.

### 4.6 Source-to-claim traceability

Durable background claims must be traceable through [`research/survey/SOURCE_MAP.md`](research/survey/SOURCE_MAP.md) or an equivalent source record.

Prefer, in order:

1. primary paper / primary preprint;
2. official technical/model/project page;
3. official open-source repository/checkpoint;
4. company/lab reported capability with explicit `OFFICIAL_REPORTED_RESULT` status;
5. secondary news only as `SURVEY_SIGNAL` until upgraded to a stronger source.

A source entry should record:

```text
source URL
→ evidence level
→ demonstrated capability
→ limitation
→ research contradiction
→ Clover landing
```

### 4.7 Separate evidence levels

Use these evidence labels where useful:

- `PRIMARY_PAPER` — peer-reviewed paper or primary preprint;
- `OFFICIAL_PROJECT` — official project/model/technical page;
- `OPEN_SOURCE` — public code/checkpoint;
- `OFFICIAL_REPORTED_RESULT` — company/lab result without independent reproduction;
- `BACKGROUND_REFERENCE` — foundational text/review/history;
- `SURVEY_SIGNAL` — discovery/news lead not yet promoted;
- `INTERNAL_HYPOTHESIS` — Clover candidate idea;
- `OPEN` — unresolved research question;
- `SUPERSEDED` — retained for history, no longer current.

Never silently turn a company report, news article or internal idea into a scientific fact.

### 4.8 Preserve the vision-only protocol

“Vision alone” must be declared precisely.

Observation protocol:

- `V0`: monocular RGB + temporal ordering;
- `V1`: RGB + camera calibration;
- `V2`: calibrated multi-camera RGB;
- `V3`: embodied active vision, where actions change future visual evidence.

Depth, LiDAR, tactile, force, IMU, privileged simulator state, GT object identity and GT geometry are not silently allowed in V0/V1.

### 4.9 Record learning-evidence provenance

When material, also annotate the evidence used to learn the model:

- `L0`: visual self-supervision only;
- `L1`: visual labels/annotations;
- `L2`: language/world-knowledge supervision;
- `L3`: action-conditioned demonstrations/experience;
- `L4`: non-visual or privileged physical evidence.

These are provenance labels, not a quality ranking.

Do not call a system “learned from vision alone” merely because deployment input is RGB.

### 4.10 Language is a confound, not automatically part of the answer

When studying VLM/VLA systems, distinguish:

- visual evidence;
- language/world knowledge learned from text;
- robot interaction data;
- action supervision;
- privileged non-visual state.

Do not attribute language priors to visual understanding.

### 4.11 Plausible generation is not automatically world truth

Generative world models may complete or imagine unseen state.

Keep distinct:

```text
observed
inferred
predicted
hypothetical / generated
ambiguous
unobserved
contradicted
```

Do not silently promote generated completion to evidence-grounded world state.

### 4.12 Hardware is a design variable

The current local platform is a Mac mini M4 with Apple unified memory.

CPU, GPU, Metal, MPS and Neural Engine are available design resources.

The algorithm determines the hardware mapping; hardware does not determine the scientific hypothesis.

### 4.13 Real capability eventually matters

The long-term standard is not a QA score.

Clover must ultimately support real robot behavior in unfamiliar environments, including memory, recovery, world change, active perception and long-horizon decision-making.

### 4.14 Main is the canonical research record

During the background-research/foundation phase, `main` is the canonical public research record.

Temporary branches must not retain unique research conclusions after integration.

## 5. Research contribution template

A serious new source, proposal or experiment should answer:

- **Problem:** what contradiction is unresolved?
- **Prior art:** what has already been tried?
- **Evidence:** which exact primary/official URLs support the claim?
- **Representation:** what internal state is assumed?
- **Learning evidence:** V0–V3 observation protocol and L0–L4 learning provenance where relevant.
- **Demonstrated capability:** what has actually been shown?
- **Limitation:** what has not been shown?
- **Prediction:** what new capability should appear?
- **Falsifier:** what result would kill the idea?
- **Evaluation:** which task or measurement discriminates it?
- **Action relevance:** why should it help a robot?
- **Compute:** what is the expected computational structure?
- **Evidence level:** primary paper, official result, code, background reference, signal or internal hypothesis?

## 6. Coding agents

Do not rewrite research claims to match current code.

If code and current research documentation disagree, report the contradiction.

Do not introduce duplicate authority/state paths to preserve compatibility.

Do not optimize a dead hypothesis merely because code already exists.

Before implementing a new core representation mechanism, verify that the project has passed the relevant baseline/battery/failure-map gate or that the task is explicitly a bounded diagnostic experiment.

## 7. Research agents

When adding literature or frontier work:

1. locate the primary/official source;
2. preserve the exact URL;
3. classify evidence level;
4. summarize demonstrated capability conservatively;
5. record limitations/confounds;
6. map the source to a research contradiction;
7. place it in `SOURCE_MAP.md` and the relevant survey surface;
8. do not import the external mechanism into Clover by default.

`news(5).md`-style material is a discovery feed. `news_answers.md`-style material is a screened hypothesis/decision ledger. Neither overrides the post-reset SSOT.

## 8. Final rule

> **The question is fixed. The answer is open. Do not choose the answer before measuring the problem.**

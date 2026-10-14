# AGENTS.md — Clover Project Instructions

This file is mandatory reading for any AI agent, coding agent, research agent, or human contributor working in this repository.

## 1. Highest SSOT

> **Research question:** How can a machine understand the real world through vision alone?
>
> **Long-term product goal:** Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.

The research question is fixed. The answer is open.

## 2. Mandatory reading order

Before proposing architecture, code, experiments or research conclusions, read:

1. [`SSOT.md`](SSOT.md)
2. [`research/PIPELINE.md`](research/PIPELINE.md)
3. [`research/RESEARCH.md`](research/RESEARCH.md)
4. [`PRINCIPLES.md`](PRINCIPLES.md)
5. [`STATUS.md`](STATUS.md)
6. [`research/README.md`](research/README.md)
7. [`research/survey/SOURCE_MAP.md`](research/survey/SOURCE_MAP.md)
8. deeper survey/dossier files only as needed.

Historical documents and news notes are evidence/signal sources, not SSOT.

## 3. Canonical research lifecycle

```text
1 Research
→ 2 Analysis
→ 3 Synthesis
→ 4 Innovation
→ 5 Implementation
→ 6 Evaluation
→ 7 Reflection
↺ next research cycle
```

**Current active stage: Stage 1 — Research.**

The current priority is broad, traceable material collection. Do not prematurely freeze a new Clover representation or core algorithm.

## 4. Stage discipline

### Stage 1 — Research

Collect broadly:

- research directions;
- canonical foundations;
- latest strong methods;
- primary papers;
- official project pages;
- open code/checkpoints;
- datasets;
- benchmarks;
- labs/projects to monitor;
- limitations and open questions.

A source may be catalogued without being endorsed.

### Stage 2 — Analysis

For important methods, produce one-method-one-report mechanism analysis using [`research/ANALYSIS.md`](research/ANALYSIS.md).

### Stage 3 — Synthesis

Compare analyzed methods using common dimensions, capability matrices, pros/cons, trade-offs and failure maps.

### Stage 4 — Innovation

Only after a well-supported gap exists, formulate Clover-original hypotheses and algorithms. Ideas must include predictions and falsifiers.

### Stage 5 — Implementation

Implement reproducibly. Code volume does not validate a scientific idea.

### Stage 6 — Evaluation

Run diagnostics, benchmarks, ablations, real-world tests and Results with explicit protocols.

### Stage 7 — Reflection

Interpret results, reject failed assumptions, update hypothesis status and decide the next cycle.

## 5. Non-negotiable research rules

### 5.1 Do not protect an old answer

The following are hypotheses or engineering choices, not axioms:

- CPU-first or GPU-first computation;
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

If evidence contradicts them, revise, replace or delete them.

### 5.2 Do not lower the research question

Failure of a current mechanism is not a reason to redefine “understanding” downward.

### 5.3 Research before Innovation

Do not choose a preferred representation and then search for papers that justify it.

Required logic:

```text
broad Research
→ method Analysis
→ comparative Synthesis
→ demonstrated unresolved gap
→ Innovation hypothesis
→ Implementation
→ Evaluation
→ Reflection
```

### 5.4 Benchmarks are instruments

A benchmark result is evidence about a capability, not a definition of understanding.

### 5.5 No framework stacking

Do not integrate an external method merely because it is strong.

For every important external method:

1. identify the problem it addresses;
2. record what the source actually demonstrates;
3. record what it does not demonstrate;
4. identify its representation and learning evidence;
5. compare it with competing methods during Analysis/Synthesis;
6. only after a gap is established consider a Clover innovation.

### 5.6 Source-to-claim traceability

Prefer, in order:

1. primary paper / preprint;
2. official technical/model/project page;
3. official open-source repository/checkpoint;
4. company/lab reported capability with explicit `OFFICIAL_REPORTED_RESULT` status;
5. secondary news only as `SURVEY_SIGNAL` until upgraded.

A durable research record should preserve:

```text
exact source URL
research direction
evidence level
demonstrated capability
limitation / unresolved question
visual protocol when material
learning provenance when material
code / dataset / benchmark links when available
```

### 5.7 Separate evidence levels

Use:

- `PRIMARY_PAPER`
- `OFFICIAL_PROJECT`
- `OPEN_SOURCE`
- `OFFICIAL_REPORTED_RESULT`
- `BACKGROUND_REFERENCE`
- `SURVEY_SIGNAL`
- `INTERNAL_HYPOTHESIS`
- `OPEN`
- `SUPERSEDED`

Never silently turn a company report, news article or internal idea into scientific fact.

### 5.8 Preserve the vision-only protocol

Observation protocol:

- `V0`: monocular RGB + temporal ordering;
- `V1`: RGB + camera calibration;
- `V2`: calibrated multi-camera RGB;
- `V3`: embodied active vision where actions change future visual evidence.

Depth, LiDAR, tactile, force, IMU, privileged simulator state, GT object identity and GT geometry are not silently allowed in V0/V1.

### 5.9 Record learning-evidence provenance

- `L0`: visual self-supervision only;
- `L1`: visual labels/annotations;
- `L2`: language/world-knowledge supervision;
- `L3`: action-conditioned demonstrations/experience;
- `L4`: non-visual or privileged physical evidence.

Do not call a system “learned from vision alone” merely because deployment input is RGB.

### 5.10 Language is a confound

When studying VLM/VLA systems, distinguish visual evidence from language/world knowledge, robot interaction data, action supervision and privileged non-visual state.

### 5.11 Plausible generation is not automatically world truth

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

### 5.12 Hardware is a design variable

The algorithm determines the hardware mapping. Hardware does not determine the scientific hypothesis.

### 5.13 Real capability eventually matters

The long-term standard is not a QA score. Clover must ultimately support real behavior in unfamiliar environments, including memory, recovery, world change, active perception and long-horizon decision-making.

## 6. Stage-1 research contribution template

When adding a method or source during the current stage, record as much of the following as is known:

- **Direction**
- **Name / version / date**
- **Primary paper URL**
- **Official project URL**
- **Official code URL**
- **Dataset / benchmark URL**
- **Evidence level**
- **Input / training provenance**
- **One-sentence demonstrated capability**
- **One-sentence limitation / open question**

Do not turn this collection record into a full architecture decision.

## 7. Coding agents

Do not rewrite research claims to match current code.

Small diagnostic code is allowed before Stage 5 only when it is genuinely necessary to resolve a research/analysis question. Core algorithm implementation belongs downstream of Innovation.

## 8. Research agents

During the current Research stage:

1. search broadly, including directions outside the current dossiers;
2. locate the primary/official source;
3. preserve exact URLs;
4. classify evidence level;
5. collect code/datasets/benchmarks where available;
6. summarize claims conservatively;
7. record missing areas explicitly;
8. do not import external mechanisms into Clover by default.

News archives are discovery feeds. Durable material should graduate to primary/official evidence before becoming a core research record.

## 9. Final rule

> **Research broadly. Analyze deeply. Synthesize comparatively. Innovate only from demonstrated gaps.**

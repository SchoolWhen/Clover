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
4. [`research/survey/README.md`](research/survey/README.md)
5. the relevant active hypothesis / decision files.

Historical documents and news notes are evidence sources, not SSOT.

## 3. Current phase

Clover is currently in a **Survey / Research Foundation** phase.

The immediate objective is to understand the strongest existing answers to the research question before freezing the next Clover representation.

Do not start a benchmark campaign, reproduce large models, or rewrite the core architecture unless the task explicitly requires it.

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
- explicit state;
- latent state;
- Transformer / non-Transformer architecture.

If evidence contradicts them, revise or replace them.

### 4.2 Do not lower the research question

Failure of a current mechanism is not a reason to redefine "understanding" downward.

The project may replace a mechanism, representation, formula, variable, architecture, training objective, benchmark, or hardware plan.

The project does not replace the research question with an easier one.

### 4.3 Benchmarks are instruments

Do not optimize the project identity around one benchmark.

A benchmark result is evidence about a capability, not a definition of understanding.

### 4.4 No framework stacking

Do not integrate an external method just because it is strong.

For every external method:

1. identify the contradiction it solves;
2. determine whether Clover has the same contradiction;
3. derive the required mechanism from the Clover problem;
4. define a falsifier;
5. only then consider implementation.

### 4.5 Separate evidence levels

Use these evidence labels where useful:

- `PRIMARY_PAPER` — peer-reviewed paper or primary preprint;
- `OFFICIAL_PROJECT` — official project/model page;
- `OPEN_SOURCE` — public code/checkpoint;
- `OFFICIAL_REPORTED_RESULT` — company/lab result without independent reproduction;
- `INTERNAL_HYPOTHESIS` — Clover candidate idea;
- `OPEN` — unresolved research question;
- `SUPERSEDED` — retained for history, no longer current.

Never silently turn a company report, news article, or internal idea into a scientific fact.

### 4.6 Preserve the vision-only protocol

"Vision alone" must be declared precisely.

The repository currently distinguishes:

- `V0`: monocular RGB + temporal ordering;
- `V1`: RGB + camera calibration;
- `V2`: calibrated multi-camera RGB;
- `V3`: embodied active vision, where actions change future visual evidence.

Depth, LiDAR, tactile, force, IMU, privileged simulator state, GT object identity, and GT geometry are not silently allowed in V0/V1.

### 4.7 Language is a confound, not automatically part of the answer

When studying VLM/VLA systems, distinguish:

- visual evidence;
- language/world knowledge learned from text;
- robot interaction data;
- action supervision.

Do not attribute language priors to visual understanding.

### 4.8 Hardware is a design variable

The current local platform is a Mac mini M4 with Apple unified memory.

CPU, GPU, Metal, MPS and Neural Engine are available design resources.

The algorithm determines the hardware mapping; hardware does not determine the scientific hypothesis.

### 4.9 Real capability eventually matters

The long-term standard is not a QA score.

Clover must ultimately support real robot behavior in unfamiliar environments, including memory, recovery, world change, active perception, and long-horizon decision-making.

### 4.10 Main is the canonical research record

During the Survey/Foundation phase, `main` is the canonical public research record.

Temporary branches must not retain unique research conclusions after integration.

## 5. Research contribution template

A serious new proposal should answer:

- **Problem:** what contradiction is unresolved?
- **Prior art:** what has already been tried?
- **Representation:** what internal state is assumed?
- **Learning signal:** how is it acquired?
- **Prediction:** what new capability should appear?
- **Falsifier:** what result would kill the idea?
- **Evaluation:** which task or measurement discriminates it?
- **Action relevance:** why should it help a robot?
- **Compute:** what is the expected computational structure?
- **Evidence level:** paper, official result, code, or internal hypothesis?

## 6. Coding agents

Do not rewrite research claims to match current code.

If code and current research documentation disagree, report the contradiction.

Do not introduce duplicate authority/state paths to preserve compatibility.

Do not optimize a dead hypothesis merely because code already exists.

## 7. Final rule

> **The question is fixed. The answer is open.**

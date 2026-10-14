# Lifelong Learning and World Growth

## Core question

> **Can a robot's understanding of the world improve continuously from experience without periodically rebuilding the entire model?**

A general robot brain cannot remain permanently frozen after offline training. It must acquire new entities, dynamics, places and task regularities while correcting earlier beliefs.

## Relevant fields

- continual learning;
- catastrophic forgetting;
- experience replay;
- online adaptation;
- lifelong robot learning;
- memory consolidation;
- open-world recognition;
- ontology/type discovery.

## LIBERO

LIBERO is a benchmark for lifelong robot learning focused on knowledge transfer. Its purpose is not pure visual world understanding, but it provides a mature framework for asking whether previously learned skills and knowledge help or interfere with later tasks.

Primary source:

- https://libero-project.github.io/main.html

## Clover's stronger requirement

Skill retention alone is not enough. A persistent worldview should support:

```text
new evidence
→ revise belief
→ preserve unaffected knowledge
→ invalidate affected claims
→ consolidate stable structure
→ forget detail without losing provenance
```

## Types of growth to study

- **Add** — new entity/type/relation/model;
- **Merge** — previously separate concepts become equivalent;
- **Split** — one category separates into different dynamics/affordances;
- **Revise** — later evidence changes an earlier belief;
- **Retire** — obsolete hypothesis no longer influences current authority;
- **Forget** — remove unnecessary high-resolution history;
- **Consolidate** — replace repeated evidence with a stable reusable model.

These operations are research requirements, not claims that the current public repository already implements them.

## Open questions

1. What should remain plastic during deployment?
2. How can a system distinguish new knowledge from transient noise?
3. What memories must be retained to allow later reinterpretation?
4. Can a model grow its ontology without human category labels?
5. How do we prevent self-training errors from becoming authoritative world facts?
6. What does a 24-hour or 7-day persistent robot worldview look like computationally?

# Product Goal

> **Build a general-purpose robotic brain that forms an understanding of the real world through vision alone, then uses that understanding to decide and act.**

The intended endpoint is not a benchmark-only model. It is an embodied brain with a persistent visual worldview.

## Current system-level decomposition

```text
Vision
  ↓
Worldview      — What is the world?
  ↓
Decision       — What world state should be reached?
  ↓
Tool Use       — What capability can produce that change?
  ↓
Execution      — Realize the capability and observe the result.
  ↓
Vision
```

This decomposition is useful for reasoning about responsibility and interfaces, but it is not a commitment to one network topology or representation.

## Desired properties

The final system should be able to:

- operate in unfamiliar real environments;
- maintain object and place persistence outside the current view;
- recognize unknown and unobserved state;
- predict and reason about physical change;
- revise beliefs after contradictory visual evidence;
- choose information-seeking visual actions when necessary;
- use world understanding to improve decisions and recovery;
- run efficiently enough for real embodied control.

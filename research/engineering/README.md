# Engineering / Deployment / Validation — Supporting Stage-1 Index

This directory is supporting material for [`../RESEARCH_ENGINEERING_VALIDATION.md`](../RESEARCH_ENGINEERING_VALIDATION.md).

It is **not** a new project stage and it does not constrain Clover to one hardware platform, runtime, simulator or robot.

Current purpose:

```text
scientific model
→ measurable runtime
→ deployment perturbations
→ simulation evidence
→ cross-simulator evidence
→ real-data evidence
→ proxy hardware
→ target robot
→ runtime monitoring / regression / rollback
```

## Read first

1. [`../RESEARCH_ENGINEERING_VALIDATION.md`](../RESEARCH_ENGINEERING_VALIDATION.md) — hardware, edge inference, EV0–EV8 validation ladder, sim2sim/sim2real/real2sim2real, simulator failure taxonomy.
2. [`DEPLOYMENT_LIFECYCLE.md`](DEPLOYMENT_LIFECYCLE.md) — deployment profiles, fault injection, runtime monitoring, model/data provenance, regression/rollback, security and low-cost proxy-hardware path.

## Current local reference

```text
Mac mini with Apple M4
```

Treat it as a **measured development/deployment reference**, not as a scientific assumption or final robot compute target.

## Current rule

A later Clover result should answer both:

```text
Does the mechanism work scientifically?
```

and:

```text
Under which compute / timing / simulator / hardware / failure conditions does it remain valid?
```

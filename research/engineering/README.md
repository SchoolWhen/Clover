# Engineering / Deployment / Validation — Supporting Stage-1 Index

Last updated: **2026-10-15**

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
3. [`VALIDATION_RESOURCES.md`](VALIDATION_RESOURCES.md) — current evidence snapshot covering WorldOracle, RoboSimStudio, LIBERO-RIG, RoboFQE, LADDER, LoopWAM, ForceWAM, Grid-or-Nodes, GreenWAM and real-time execution comparators.
4. [`../emerging/JEPA_RSI_RUNTIME_2026-10-15.md`](../emerging/JEPA_RSI_RUNTIME_2026-10-15.md) — latest cross-boundary runtime audit covering MARS, WAMachine, Δ-flow, AsyncVLA / asynchronous WAM execution, Apple-M4 VPA evidence, EmbodiedJev and embodied RSI.

## Current local reference

```text
Mac mini with Apple M4
```

Treat it as a **measured development/deployment reference**, not as a scientific assumption or final robot compute target.

Useful current engineering reference:

- EmbodiedJev / 行知 — https://github.com/FBddcz/embodied-jev — open-source MuJoCo + Franka workbench with local/API model adapters, controlled model comparison, trajectory replay/export and pre-execution simulation checks. Treat it as an `OPEN_SOURCE_PROJECT / ENGINEERING_REFERENCE`, not as evidence that a model learned the controller's geometry/safety logic or that simulation transfers to reality.

## Additional runtime distinctions from the latest audit

```text
inference-state reuse
≠
inference-state validity

asynchronous execution
requires
timestamp / stale-guidance / action-observation alignment

base policy latency
≠
policy + verifier/search latency

training-free acceleration
≠
zero behavioral change
```

Acceleration experiments should measure not only speed but stale-state failures, closed-loop success, uncertainty, deadline misses and whether online verification/refresh is required.

## Current rule

A later Clover result should answer both:

```text
Does the mechanism work scientifically?
```

and:

```text
Under which compute / timing / simulator / hardware / failure conditions does it remain valid?
```

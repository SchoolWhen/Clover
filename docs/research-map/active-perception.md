# Active Perception

## Core question

> **If a visual system knows that its evidence is insufficient, can it decide what to look at next?**

Vision alone does not imply passive vision. A robot can move its camera or body, change viewpoint, approach an object, inspect an occluded region and create new evidence.

## Why this is central to Clover

A passive model can only refuse when a necessary fact is unobserved. A robot brain can instead turn epistemic uncertainty into an information-seeking action.

```text
unresolved world question
        ↓
which observation could resolve it?
        ↓
viewpoint / inspection action
        ↓
new visual evidence
        ↓
world update
```

This may become one of the strongest bridges between Worldview and Decision.

## Prior theoretical roots

- active vision;
- POMDPs;
- belief-space planning;
- next-best-view planning;
- information gain / entropy reduction;
- visual exploration.

These fields already formalize the idea that sensing itself can be controlled.

## Clover-specific questions

1. What form of uncertainty is actionable rather than merely low confidence?
2. Can the system identify a **minimal missing observation** needed to answer a world query?
3. How should the value of information trade off against task progress and motion cost?
4. Can active perception distinguish genuine ambiguity from model weakness?
5. Can the robot learn visual inquiry policies without language labels?

## Important distinction

Active perception is not an excuse to weaken the vision-only claim. The sensory evidence remains visual. The action only changes which visual evidence becomes available.

## Future strong test

Construct tasks where two hidden world hypotheses are visually indistinguishable from the current viewpoint, but one deliberate camera/body movement reveals the difference. A world-understanding system should know that it does not yet know, choose a revealing observation, update, and then act.

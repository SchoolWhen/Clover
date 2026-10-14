# Active Perception

## Core idea

Vision alone does not imply passive vision. An embodied agent can change its viewpoint to obtain missing evidence.

A central loop is:

```text
world uncertainty
→ information-seeking visual action
→ new observation
→ belief update
```

## Connections to prior fields

- active vision;
- POMDP and belief-space planning;
- next-best-view planning;
- embodied exploration;
- active SLAM.

## Why it matters to Clover

A system that can represent `unknown` but cannot act to resolve relevant unknowns is incomplete as a robotic brain. Active perception may be the bridge from Worldview uncertainty to Decision.

## Open questions

- Which uncertainty belongs to Worldview and which to Decision?
- Can information gain be computed from a learned representation?
- How should active perception be evaluated without rewarding unnecessary motion?

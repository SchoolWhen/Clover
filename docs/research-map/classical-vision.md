# Classical Vision and Geometry

## What problem does this area solve?

Recover camera motion, 3D structure, correspondence and state estimates from images using explicit mathematical geometry and probabilistic estimation.

## Typical representation

- camera pose / calibration;
- sparse or dense 3D landmarks;
- tracks and correspondences;
- occupancy / maps;
- probabilistic belief over state.

## Representative work

- Multi-view geometry, structure-from-motion and bundle adjustment;
- visual odometry / SLAM;
- ORB-SLAM3 — https://github.com/UZ-SLAMLab/ORB_SLAM3
- RAFT optical flow — https://github.com/princeton-vl/RAFT

## What it has demonstrated

Classical methods can provide mathematically grounded geometry, camera motion and persistence without needing web-scale learned semantics.

## Known limitations for the Clover question

Geometry alone does not automatically produce semantic abstraction, object types, causal expectations, affordances or open-world conceptual growth. Hand-designed state spaces can become task-specific.

## Why it matters to Clover

Clover should not ask learning systems to rediscover geometry blindly if explicit geometry is already reliable and computationally appropriate. A central question is where explicit geometric guarantees should end and learned abstraction should begin.

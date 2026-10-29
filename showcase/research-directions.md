# Research directions

[Back to profile](../README.md)

**Status: planned investigations.** These directions describe research interests, not publications, completed experiments, or demonstrated algorithmic improvements.

## Consistency-Constrained Adaptive Replica Selection

Investigating replica selection under explicit consistency and latency constraints.

Questions to explore:

- Which replicas are eligible for a request's consistency requirement?
- How could observed latency and replica progress guide selection among eligible replicas?
- How should a selection policy behave when observations become stale or failures occur?

## Adaptive Distributed Top-K Retrieval

Exploring adaptive query processing and distributed retrieval strategies.

Questions to explore:

- When could a query reduce distributed work while preserving its required retrieval semantics?
- How could shard-level information guide candidate collection and refinement?
- How should evaluation account for skew, network cost, and tail latency?

A future evaluation would need explicit correctness criteria, declared workloads, and reproducible baselines before making performance claims. No results are claimed here.

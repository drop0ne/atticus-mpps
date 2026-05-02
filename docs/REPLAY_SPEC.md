# Replay Spec v0.1

Replay must reconstruct candidate outputs from raw packet logs and raw asset hashes.

## Pass Condition

A replay passes when all of the following are true:

- Same raw input hash
- Same algorithm version
- Same calibration reference
- Same candidate value
- Same parent lineage

Replay divergence must produce a report rather than silently passing.

## v0.1 Constraint

Replay is deterministic only for fixed local files and fixed algorithm versions. Live camera, LWIR, GNSS/PPS, and weather hardware are deferred from v0.1 replay claims.

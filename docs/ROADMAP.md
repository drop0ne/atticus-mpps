# ATTICUS MPPS Roadmap

## v0.1 — Desktop Packet Spine

Goal: prove the audit spine before adding outdoor hardware.

Deliverables:

- Saved RGB image ingest
- Raw observation packet creation
- SHA-256 raw lineage
- Derived cloud-fraction candidate packet
- JSON Schema validation
- Replay runner
- CLI commands
- Basic pytest suite
- CI workflow

Exit criteria:

- `pytest` passes
- `ruff check .` passes
- `mpps init` creates local runtime folders
- one image can produce one raw packet and one derived candidate packet
- `mpps validate` passes for generated packets

## v0.2 — Local Dataset + Replay Hardening

Goal: convert the prototype from a smoke-test loop into a small measurable dataset system.

Planned work:

- Add manifest generation
- Add replay comparison report
- Add deterministic algorithm versioning
- Add sample-image fixture policy
- Add 100-image local benchmark layout
- Add packet ancestry resolver
- Add failure reports for missing raw files or hash mismatch

## v0.3 — Mock Weather and Timing Context

Goal: add environmental context without hardware dependency.

Planned work:

- Mock BME280-style packet
- Mock clock-quality packet
- Capture-window semantics
- Sync-error estimate fields
- Fusion placeholder packet

## v0.4 — Live RGB Bench

Goal: ingest from a live desktop camera while keeping replay boundaries explicit.

Planned work:

- Webcam capture command
- Frame-rate limiter
- Raw retention settings
- Basic image quality metrics
- Operator review queue

## v0.5 — LWIR Bench Branch

Goal: add thermal input after RGB packet/replay works.

Planned work:

- LWIR mock interface
- Real LWIR adapter placeholder
- Thermal raw packet schema extension
- RGB/LWIR paired capture layout
- Day/night pilot protocol

## Deferred Research Branches

- Photonic preprocessing
- Multi-camera geometry
- Cloud-base height inference
- GNSS/PPS hardware timing
- Outdoor enclosure and field deployment
- Calibrated probabilistic confidence
- Strong proto-symbol ontology

# ATTICUS MPPS

ATTICUS MPPS is a desktop-stage environmental perception prototype.

The v0.1 goal is to prove a replayable, auditable packet spine before outdoor deployment or advanced hardware.

## Current Status

Status: **early scaffold / v0.1 desktop prototype**

Repository focus:

- prove raw image ingest
- prove packet validation
- prove SHA-256 lineage
- prove derived candidate creation
- prove replay scaffolding
- preserve governance boundaries before outdoor sensing

Active work is tracked in GitHub issues:

| Issue | Focus |
|---:|---|
| #1 | First local smoke test |
| #2 | Replay comparison report |
| #3 | Mock weather and timing context packets |
| #4 | Packet ancestry resolver |
| #5 | First benchmark dataset layout |
| #6 | Governance and retention policy |

## Scope

In scope:

- Saved RGB sky image ingest
- Raw observation packet creation
- SHA-256 raw data lineage
- Derived candidate packet creation
- JSON Schema validation
- Replay validation
- Mock weather/timing context
- Human-reviewable outputs

Out of scope for v0.1:

- Outdoor deployment
- Person/vehicle analytics
- Full-spectrum perception claims
- Photonic preprocessing
- Autonomous decisions
- Deployment-ready calibrated confidence

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -e ".[dev]"

mpps init
mpps ingest-rgb data/input/rgb
mpps detect-clouds data/packet_log/raw_observations.jsonl
mpps validate data/packet_log
mpps replay --run-id smoke_001
mpps status
```

## Core Rule

No derived output is treated as truth unless it has raw lineage, validation status, review state, and an explicit uncertainty/quality record.

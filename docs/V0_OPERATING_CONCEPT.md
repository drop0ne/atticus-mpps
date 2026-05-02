# ATTICUS MPPS v0.1 Operating Concept

ATTICUS MPPS v0.1 is a desktop-stage environmental perception prototype.

It ingests sky/weather image inputs and emits reviewable candidate observation packets.

It does not claim full-spectrum perception, generalized artificial vision, symbolic truth, calibrated autonomy, or deployment readiness.

## In Scope

- RGB sky image ingest
- Mock weather context
- Raw packet logging
- Derived candidate packets
- SHA-256 raw lineage
- JSON Schema validation
- Replay validation
- Human-review state

## Out of Scope

- Outdoor deployment
- Surveillance
- Person or vehicle analytics
- Photonic preprocessing
- LWIR hardware integration
- GNSS/PPS hardware timing
- Autonomous decisions

## Primary Output Types

- RAW_OBSERVATION
- CLOUD_FRACTION_CANDIDATE
- CLOUD_CLASS_CANDIDATE
- CLOUD_MOTION_CANDIDATE
- ILLUMINATION_CHANGE_CANDIDATE
- SENSOR_HEALTH_EVENT
- UNKNOWN_ANOMALY_CANDIDATE

## Core Rule

No derived output is treated as truth unless it has raw lineage, validation status, review state, and an explicit uncertainty/quality record.

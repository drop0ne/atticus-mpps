# Blocker Closure Matrix

This matrix converts research blockers into engineering gates.

| ID | Blocker | Why It Blocks | Closure Test | Target |
|---|---|---|---|---|
| MPPS-KG-001 | v0 band stack is not frozen | Hardware, schema, calibration, and benchmark design depend on final modality choice. | Freeze v0 as RGB-only desktop first, then RGB+LWIR bench branch. | v0.1/v0.5 |
| MPPS-KG-002 | Calibration budget unspecified | Fusion can look plausible while being physically wrong. | Define calibration state fields, then add reprojection/radiometric tests before field use. | v0.5+ |
| MPPS-KG-003 | Synchronization and latency undefined | Sensor packets may describe different physical moments. | Add clock source, clock quality, capture window, and sync error fields. | v0.3 |
| MPPS-KG-004 | Paired RGB/LWIR benchmark incomplete | No benchmark means no credible TEVV. | Create local paired dataset protocol and minimum labeled subset. | v0.5+ |
| MPPS-KG-005 | Proto-symbol closure criteria missing | Cannot evaluate vague intermediate representations. | Use typed candidate packets only; define ontology later. | v0.1/v0.6 |
| MPPS-KG-006 | Confidence not validated | Confidence cannot be treated as probability. | Keep `confidence_is_calibrated_probability=false`; add ECE/Brier later. | v0.1+ |
| MPPS-KG-007 | Packet provenance/replay incomplete | Shape validation does not prove lineage. | Add raw hashes, parent IDs, trace IDs, provenance IDs, and replay reports. | v0.1/v0.2 |
| MPPS-KG-008 | Governance absent | Sensor systems can drift into surveillance if unconstrained. | Add governance note, no-identity rules, retention and outdoor review gates. | v0.1+ |
| MPPS-KG-009 | Photonics unjustified by measured bottleneck | Hardware novelty can derail validation. | Defer until digital baseline has measured bottleneck and target delta. | Deferred |
| MPPS-KG-010 | Single-node vs multi-camera unresolved | 3D/cloud-base-height tasks may require network geometry. | Keep out of v0; revisit in v1. | v1 |

## Priority Order

1. Packet lineage and schema validation
2. Replay determinism
3. Governance boundary
4. Mock timing/weather context
5. Local benchmark protocol
6. LWIR bench branch
7. Calibration budget
8. Photonic branch only after measured bottleneck

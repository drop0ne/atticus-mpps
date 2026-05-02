# Packet Contract v0.1

Every packet must be append-only and replayable.

Required raw packet concepts:

- packet_id
- packet_type
- sensor_id
- sensor_type
- capture_start_utc
- capture_end_utc
- ingest_time_utc
- monotonic_time_ns
- clock_source
- clock_quality
- sync_error_estimate_ms
- raw_ref
- raw_sha256
- calibration_ref
- coordinate_frame
- units
- parent_packet_ids
- trace_id
- prov_bundle_id
- review_state

Derived packets must include at least one parent packet ID.

## v0.1 Rule

`confidence_display` is not a calibrated probability until ECE/Brier/reliability testing exists.

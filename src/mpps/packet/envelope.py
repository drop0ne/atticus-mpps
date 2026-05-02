from __future__ import annotations

import os
import shutil
import time
from pathlib import Path
from typing import Any

from .hashes import sha256_file
from .ids import new_packet_id, new_prov_bundle_id, new_trace_id, utc_now_iso


def make_raw_image_packet(
    source_path: str | Path,
    raw_store_dir: str | Path = "data/raw_store",
    sensor_id: str = "desktop_rgb_folder_001",
) -> dict[str, Any]:
    """Copy an image into the raw store and return a raw observation packet."""
    src = Path(source_path)
    raw_dir = Path(raw_store_dir)
    raw_dir.mkdir(parents=True, exist_ok=True)

    packet_id = new_packet_id("raw")
    dest = raw_dir / f"{packet_id}{src.suffix.lower()}"
    shutil.copy2(src, dest)

    digest = sha256_file(dest)
    now = utc_now_iso()
    trace_id = new_trace_id()
    prov_id = new_prov_bundle_id()

    return {
        "packet_version": "mpps.raw.v0.1",
        "packet_id": packet_id,
        "packet_type": "RAW_OBSERVATION",
        "sensor": {
            "sensor_id": sensor_id,
            "sensor_type": "RGB_IMAGE",
            "sensor_model": "file_input",
            "modality": "visible",
        },
        "time": {
            "capture_start_utc": now,
            "capture_end_utc": now,
            "ingest_time_utc": now,
            "monotonic_time_ns": time.monotonic_ns(),
            "clock_source": "system_clock",
            "clock_quality": "desktop_unverified",
            "sync_error_estimate_ms": None,
        },
        "data_ref": {
            "raw_ref": str(dest.as_posix()),
            "raw_sha256": digest,
            "mime_type": "image/jpeg" if dest.suffix.lower() in {".jpg", ".jpeg"} else "image/png",
            "bytes": os.path.getsize(dest),
        },
        "calibration": {
            "calibration_ref": "data/calibration/default_rgb_uncalibrated_v0.1.json",
            "coordinate_frame": "image_pixel",
            "units": "pixel",
            "calibration_state": "uncalibrated_desktop",
        },
        "lineage": {
            "parent_packet_ids": [],
            "trace_id": trace_id,
            "prov_bundle_id": prov_id,
        },
        "review": {
            "review_state": "raw_unreviewed",
            "human_review_required": False,
        },
    }

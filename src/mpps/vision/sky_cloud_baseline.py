from __future__ import annotations

from pathlib import Path
from typing import Any

import cv2
import numpy as np

from mpps.packet.ids import new_packet_id


def estimate_cloud_fraction(image_path: str | Path) -> float:
    """Crude visible-light cloud fraction estimate.

    This is not calibrated. It is a v0.1 smoke-test heuristic only.
    """
    img = cv2.imread(str(image_path), cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError(f"Could not read image: {image_path}")

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    saturation = hsv[:, :, 1]
    value = hsv[:, :, 2]

    cloud_mask = (saturation < 80) & (value > 120)
    return float(np.mean(cloud_mask))


def make_cloud_fraction_candidate(raw_packet: dict[str, Any]) -> dict[str, Any]:
    raw_ref = raw_packet["data_ref"]["raw_ref"]
    fraction = estimate_cloud_fraction(raw_ref)

    return {
        "packet_version": "mpps.derived.v0.1",
        "packet_id": new_packet_id("cand"),
        "packet_type": "CLOUD_FRACTION_CANDIDATE",
        "candidate": {
            "candidate_type": "CLOUD_FRACTION",
            "value": round(fraction, 6),
            "value_units": "fraction_0_to_1",
            "method": "baseline_threshold_v0.1",
            "claim_strength": "candidate_observation",
        },
        "quality": {
            "confidence_display": None,
            "confidence_is_calibrated_probability": False,
            "quality_vector": {
                "image_brightness_ok": None,
                "image_blur_score": None,
                "mask_applied": False,
                "calibration_available": False,
                "timing_verified": False,
            },
        },
        "lineage": {
            "parent_packet_ids": [raw_packet["packet_id"]],
            "trace_id": raw_packet["lineage"]["trace_id"],
            "prov_bundle_id": raw_packet["lineage"]["prov_bundle_id"],
        },
        "review": {
            "review_state": "needs_review",
            "human_review_required": True,
        },
    }

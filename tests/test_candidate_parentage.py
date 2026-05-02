from mpps.vision.sky_cloud_baseline import make_cloud_fraction_candidate


def test_candidate_requires_parent(monkeypatch):
    raw = {
        "packet_id": "raw_test",
        "packet_type": "RAW_OBSERVATION",
        "data_ref": {"raw_ref": "missing.jpg"},
        "lineage": {"trace_id": "trace_test", "prov_bundle_id": "prov_test"},
    }

    monkeypatch.setattr("mpps.vision.sky_cloud_baseline.estimate_cloud_fraction", lambda _: 0.5)
    cand = make_cloud_fraction_candidate(raw)
    assert cand["lineage"]["parent_packet_ids"] == ["raw_test"]
    assert cand["review"]["review_state"] == "needs_review"
    assert cand["quality"]["confidence_is_calibrated_probability"] is False

def test_no_truth_final_placeholder():
    allowed_v01_review_states = {"raw_unreviewed", "needs_review", "candidate", "rejected"}
    assert "truth_final" not in allowed_v01_review_states

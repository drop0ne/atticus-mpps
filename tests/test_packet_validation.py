from mpps.packet.validator import validate_packet


def test_invalid_raw_packet_fails():
    errors = validate_packet({}, "schemas/raw_observation.schema.json")
    assert errors

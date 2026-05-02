from __future__ import annotations

from pathlib import Path

from mpps.packet.writer import append_jsonl, read_jsonl
from mpps.vision.sky_cloud_baseline import make_cloud_fraction_candidate


def replay_cloud_candidates(raw_log: str | Path, output_log: str | Path) -> int:
    """Replay raw observation packets into cloud-fraction candidates."""
    packets = read_jsonl(raw_log)
    count = 0
    for packet in packets:
        if packet.get("packet_type") != "RAW_OBSERVATION":
            continue
        candidate = make_cloud_fraction_candidate(packet)
        append_jsonl(output_log, candidate)
        count += 1
    return count

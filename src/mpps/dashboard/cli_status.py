from __future__ import annotations

from pathlib import Path

from mpps.packet.writer import read_jsonl


def print_status(packet_dir: str | Path = "data/packet_log") -> None:
    """Print a compact local packet status report."""
    d = Path(packet_dir)
    raw = read_jsonl(d / "raw_observations.jsonl")
    cand = read_jsonl(d / "derived_candidates.jsonl")
    print("ATTICUS MPPS v0.1 status")
    print(f"raw packets: {len(raw)}")
    print(f"candidate packets: {len(cand)}")

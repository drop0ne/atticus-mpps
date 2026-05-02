from __future__ import annotations

import argparse
from pathlib import Path

from mpps.dashboard.cli_status import print_status
from mpps.ingest.image_loader import iter_images
from mpps.packet.envelope import make_raw_image_packet
from mpps.packet.validator import validate_packet
from mpps.packet.writer import append_jsonl, read_jsonl
from mpps.replay.replay_runner import replay_cloud_candidates
from mpps.vision.sky_cloud_baseline import make_cloud_fraction_candidate


RAW_LOG = Path("data/packet_log/raw_observations.jsonl")
DERIVED_LOG = Path("data/packet_log/derived_candidates.jsonl")


def cmd_init(args: argparse.Namespace) -> None:
    for path in [
        "data/input/rgb",
        "data/raw_store",
        "data/packet_log",
        "data/replay_runs",
        "data/calibration",
        "data/reports",
    ]:
        Path(path).mkdir(parents=True, exist_ok=True)
    print("Initialized ATTICUS MPPS local folders.")


def cmd_ingest_rgb(args: argparse.Namespace) -> None:
    count = 0
    for image in iter_images(args.path):
        packet = make_raw_image_packet(image)
        append_jsonl(RAW_LOG, packet)
        count += 1
    print(f"Ingested {count} RGB image(s).")


def cmd_detect_clouds(args: argparse.Namespace) -> None:
    raw_packets = read_jsonl(args.raw_log)
    count = 0
    for packet in raw_packets:
        if packet.get("packet_type") == "RAW_OBSERVATION":
            append_jsonl(DERIVED_LOG, make_cloud_fraction_candidate(packet))
            count += 1
    print(f"Generated {count} cloud-fraction candidate packet(s).")


def cmd_validate(args: argparse.Namespace) -> None:
    failures = 0
    for packet in read_jsonl(RAW_LOG):
        errors = validate_packet(packet, "schemas/raw_observation.schema.json")
        if errors:
            failures += 1
            print(f"RAW validation failure {packet.get('packet_id')}: {errors}")

    for packet in read_jsonl(DERIVED_LOG):
        errors = validate_packet(packet, "schemas/derived_candidate.schema.json")
        if errors:
            failures += 1
            print(f"DERIVED validation failure {packet.get('packet_id')}: {errors}")

    if failures:
        raise SystemExit(f"Validation failed: {failures} packet(s)")
    print("Validation passed.")


def cmd_replay(args: argparse.Namespace) -> None:
    out = Path("data/replay_runs") / args.run_id / "derived_candidates.replay.jsonl"
    out.parent.mkdir(parents=True, exist_ok=True)
    count = replay_cloud_candidates(RAW_LOG, out)
    print(f"Replay generated {count} candidate packet(s): {out}")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="mpps")
    sub = p.add_subparsers(required=True)

    s = sub.add_parser("init")
    s.set_defaults(func=cmd_init)

    s = sub.add_parser("ingest-rgb")
    s.add_argument("path")
    s.set_defaults(func=cmd_ingest_rgb)

    s = sub.add_parser("detect-clouds")
    s.add_argument("raw_log", nargs="?", default=str(RAW_LOG))
    s.set_defaults(func=cmd_detect_clouds)

    s = sub.add_parser("validate")
    s.add_argument("packet_dir", nargs="?", default="data/packet_log")
    s.set_defaults(func=cmd_validate)

    s = sub.add_parser("replay")
    s.add_argument("--run-id", required=True)
    s.set_defaults(func=cmd_replay)

    s = sub.add_parser("status")
    s.set_defaults(func=lambda args: print_status())

    return p


def main() -> None:
    args = build_parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()

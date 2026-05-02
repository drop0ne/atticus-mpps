# Sprint v0.1 Smoke Test

## Objective

Verify that the current desktop scaffold can run from a clean clone and produce a replayable packet loop.

## Branch

`sprint/v0.1-smoke-test`

## Linked Issue

- #1 v0.1: Run first local smoke test

## Test Sequence

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
ruff check .
mpps init
mpps status
```

Then add one sky image to:

```text
data/input/rgb/
```

Run:

```bash
mpps ingest-rgb data/input/rgb
mpps detect-clouds
mpps validate
mpps replay --run-id smoke_001
mpps status
```

## Acceptance Criteria

- Tests pass
- Ruff passes
- At least one raw packet exists
- At least one cloud-fraction candidate packet exists
- Packet validation passes
- Replay output file exists
- No candidate claims calibrated probability
- No candidate claims final truth

## Notes

This sprint should not add new sensor hardware, outdoor deployment, photonics, LWIR, GNSS/PPS, or identity analytics.

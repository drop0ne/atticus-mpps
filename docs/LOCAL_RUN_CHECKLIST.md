# Local Run Checklist

This checklist verifies the ATTICUS MPPS v0.1 desktop scaffold on a local machine.

## 1. Clone

```bash
git clone https://github.com/drop0ne/atticus-mpps.git
cd atticus-mpps
```

## 2. Create environment

Linux/macOS:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
```

## 3. Install

```bash
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

## 4. Run static/test checks

```bash
pytest
ruff check .
```

## 5. Initialize runtime folders

```bash
mpps init
mpps status
```

Expected output:

```text
ATTICUS MPPS v0.1 status
raw packets: 0
candidate packets: 0
```

## 6. Add test image

Place one `.jpg` or `.png` sky image in:

```text
data/input/rgb/
```

## 7. Run first packet loop

```bash
mpps ingest-rgb data/input/rgb
mpps detect-clouds
mpps validate
mpps replay --run-id smoke_001
mpps status
```

## 8. Pass condition

The smoke test passes when:

- one or more raw packets exist
- one or more candidate packets exist
- validation passes
- replay creates `data/replay_runs/smoke_001/derived_candidates.replay.jsonl`
- no derived output claims calibrated probability or final truth

# Contributing

ATTICUS MPPS is currently in early prototype form.

## Contribution Priorities

Useful contributions should improve one of these areas:

- packet schema correctness
- replay determinism
- test coverage
- documentation clarity
- governance guardrails
- benchmark design
- calibration and timing discipline

## Ground Rules

- Do not add person, face, vehicle, license-plate, identity, or surveillance analytics.
- Do not present uncalibrated confidence values as probabilities.
- Do not add photonic preprocessing to the critical path without a measured software baseline bottleneck.
- Every derived output must retain parent-packet lineage.
- Every new feature should include tests or a clear validation plan.

## Development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
ruff check .
```

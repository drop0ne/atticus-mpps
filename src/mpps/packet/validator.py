from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


def load_schema(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def validate_packet(packet: dict[str, Any], schema_path: str | Path) -> list[str]:
    """Return validation errors. Empty list means valid."""
    schema = load_schema(schema_path)
    validator = Draft202012Validator(schema)
    return [error.message for error in sorted(validator.iter_errors(packet), key=str)]

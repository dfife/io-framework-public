#!/usr/bin/env python3
"""Shared helpers for the Paper 28 v2.0 reproducibility bundle."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = BUNDLE_ROOT / "data" / "imported_constants.json"
RESULTS_DIR = BUNDLE_ROOT / "results"


def load_constants() -> dict[str, Any]:
    return json.loads(DATA_PATH.read_text(encoding="utf-8"))


def write_result(filename: str, payload: dict[str, Any]) -> Path:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    path = RESULTS_DIR / filename
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


def assert_close(name: str, actual: float, expected: float, tolerance: float) -> None:
    delta = abs(actual - expected)
    if delta > tolerance:
        raise AssertionError(
            f"{name}: actual={actual!r}, expected={expected!r}, "
            f"delta={delta!r}, tolerance={tolerance!r}"
        )

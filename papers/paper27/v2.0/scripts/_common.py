#!/usr/bin/env python3
"""Shared helpers for the Paper 27 v2.0 reproducibility bundle.

The Paper 27 v2.0 bundle is structural: it reproduces theorem-support
arithmetic and machine-readable status ledgers rather than running a Boltzmann
code.  Every script writes a JSON result into ../results so a referee can audit
the exact formula, constants, status label, and source claim.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = BUNDLE_ROOT / "data" / "imported_constants.json"
RESULTS_DIR = BUNDLE_ROOT / "results"


def load_constants() -> dict[str, Any]:
    """Load the frozen constants snapshot used by all scripts."""

    return json.loads(DATA_PATH.read_text(encoding="utf-8"))


def write_result(filename: str, payload: dict[str, Any]) -> Path:
    """Write a deterministic, human-readable JSON result file."""

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    path = RESULTS_DIR / filename
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return path


def assert_close(name: str, actual: float, expected: float, tolerance: float) -> None:
    """Raise a precise validation error if a numeric check fails."""

    delta = abs(actual - expected)
    if delta > tolerance:
        raise AssertionError(
            f"{name}: actual={actual!r}, expected={expected!r}, "
            f"delta={delta!r}, tolerance={tolerance!r}"
        )

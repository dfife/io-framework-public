#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results" / "full_twenty_test_recompute_results.json"
RECOMPUTE = ROOT / "scripts" / "01_full_twenty_test_recompute.py"


EXPECTED = {
    ("tests", "paper29_scorecard", "io_cc_chi2"): 14.701523963980787,
    ("tests", "paper29_scorecard", "io_bao_chi2"): 27.735229301342457,
    ("tests", "paper29_scorecard", "io_combined_chi2"): 42.43675326532325,
    ("tests", "paper29_scorecard", "planck_combined_chi2"): 46.40432046950788,
    ("tests", "pantheon", "io", "chi2"): 1757.4798174084137,
    ("tests", "pantheon", "planck", "chi2"): 1759.6947847107324,
    ("tests", "strong_lensing", "io", "chi2"): 31.597640376134585,
    ("tests", "strong_lensing", "planck", "chi2"): 34.46226106589568,
    ("tests", "alcock_paczynski", "io", "chi2"): 7.88341490487783,
    ("tests", "alcock_paczynski", "planck", "chi2"): 6.702669976136264,
    ("inputs", "x"): 1.5189873277742727,
    ("inputs", "K_gauge"): 0.05487281774291466,
    ("inputs", "eta_bao"): 0.036124605346983495,
    ("inputs", "J_phi"): 0.8113774333810703,
}

CANONICAL_LABELS = {
    "DERIVED/THEOREM",
    "DERIVED/CONDITIONAL_VERIFIED",
    "DERIVED/NO-GO",
    "VERIFIED",
    "IMPORTED/EMPIRICAL",
    "RECONSTRUCTION",
    "RECONSTRUCTION/RESEARCH_ONLY",
    "OPEN/PREMISE_GAP",
    "SUPERSEDED",
    "DERIVED/NO-GO diagnostic",
}


def dig(obj: object, path: tuple[str, ...]) -> object:
    cur = obj
    for key in path:
        cur = cur[key]  # type: ignore[index]
    return cur


def assert_close(name: str, actual: float, expected: float, tol: float = 1e-9) -> str:
    if not math.isclose(actual, expected, rel_tol=tol, abs_tol=tol):
        raise AssertionError(f"{name}: expected {expected!r}, got {actual!r}")
    return f"PASS {name}: {actual:.12g}"


def main() -> int:
    subprocess.run([sys.executable, str(RECOMPUTE)], cwd=ROOT, check=True)
    data = json.loads(RESULTS.read_text())

    lines: list[str] = []
    for path, expected in EXPECTED.items():
        actual = float(dig(data, path))
        lines.append(assert_close(".".join(path), actual, expected))

    for slot, row in data["baryon_slots"].items():
        label = row["claim"]
        if label not in CANONICAL_LABELS:
            raise AssertionError(f"noncanonical baryon-slot claim label for {slot}: {label}")
        lines.append(f"PASS canonical label {slot}: {label}")

    generated = {
        "state": "passed",
        "checks": len(lines),
        "checks_detail": lines,
    }
    (ROOT / "results" / "validation_results.json").write_text(json.dumps(generated, indent=2) + "\n")
    print(json.dumps(generated, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

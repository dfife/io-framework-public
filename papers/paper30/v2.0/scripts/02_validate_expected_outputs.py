#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results" / "full_twenty_test_recompute_results.json"
AP_ANALYSIS = ROOT / "results" / "paper30_v2_0_AP_residual_analysis_data.json"
AP_REPORT = ROOT / "results" / "paper30_v2_0_AP_residual_analysis.md"
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

AP_ANALYSIS_EXPECTED = {
    ("headline", "io_pte"): 0.24676969705560073,
    ("headline", "planck_pte"): 0.3492212777775587,
}

AP_ROW_EXPECTED = [
    {
        "z": 0.510,
        "F_AP_io": 0.5951578711226371,
        "F_AP_planck": 0.5936603303517112,
        "F_AP_sigma_diag": 0.017159067622570235,
        "chi2_io_fullcov_contribution": 2.3979315711096536,
    },
    {
        "z": 0.706,
        "F_AP_io": 0.8806978202596372,
        "F_AP_planck": 0.877555663896066,
        "F_AP_sigma_diag": 0.02080808607379221,
        "chi2_io_fullcov_contribution": 0.30096157134544005,
    },
    {
        "z": 0.934,
        "F_AP_io": 1.2574923887955245,
        "F_AP_planck": 1.251834333857548,
        "F_AP_sigma_diag": 0.019207363358700612,
        "chi2_io_fullcov_contribution": 3.179539072433945,
    },
    {
        "z": 1.321,
        "F_AP_io": 2.0070671997298337,
        "F_AP_planck": 1.9964766078914111,
        "F_AP_sigma_diag": 0.04516019356637831,
        "chi2_io_fullcov_contribution": 1.7227174831831258,
    },
    {
        "z": 1.484,
        "F_AP_io": 2.363099147351117,
        "F_AP_planck": 2.350470123171005,
        "F_AP_sigma_diag": 0.13683464915162505,
        "chi2_io_fullcov_contribution": 0.026902051206839434,
    },
    {
        "z": 2.330,
        "F_AP_io": 4.566816658567283,
        "F_AP_planck": 4.547539398396198,
        "F_AP_sigma_diag": 0.09674800932603408,
        "chi2_io_fullcov_contribution": 0.25536315559880973,
    },
]

AP_JACKKNIFE_DELTA_CHI2 = [
    1.4614106581852724,
    1.367301926269251,
    0.21713566356924208,
    0.6177242217451671,
    1.2184116155561764,
    1.0209405411888923,
]

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
    if "--recompute" in sys.argv:
        subprocess.run([sys.executable, str(RECOMPUTE)], cwd=ROOT, check=True)
    data = json.loads(RESULTS.read_text())
    ap_analysis = json.loads(AP_ANALYSIS.read_text())

    lines: list[str] = []
    for path, expected in EXPECTED.items():
        actual = float(dig(data, path))
        lines.append(assert_close(".".join(path), actual, expected))

    for path, expected in AP_ANALYSIS_EXPECTED.items():
        actual = float(dig(ap_analysis, path))
        lines.append(assert_close("AP residual analysis " + ".".join(path), actual, expected))

    if not AP_REPORT.exists():
        raise AssertionError(f"missing AP residual analysis report: {AP_REPORT}")

    rows = ap_analysis["rows"]
    if len(rows) != len(AP_ROW_EXPECTED):
        raise AssertionError(f"AP residual row count: expected {len(AP_ROW_EXPECTED)}, got {len(rows)}")
    for index, (row, expected_row) in enumerate(zip(rows, AP_ROW_EXPECTED), start=1):
        z_label = f"z={expected_row['z']:.3f}"
        lines.append(assert_close(f"AP row {index} {z_label} F_AP_io", float(row["F_AP_io"]), expected_row["F_AP_io"]))
        lines.append(assert_close(f"AP row {index} {z_label} F_AP_planck", float(row["F_AP_planck"]), expected_row["F_AP_planck"]))
        lines.append(assert_close(f"AP row {index} {z_label} sigma", float(row["F_AP_sigma_diag"]), expected_row["F_AP_sigma_diag"]))
        lines.append(assert_close(f"AP row {index} {z_label} IO chi2 contribution", float(row["chi2_io_fullcov_contribution"]), expected_row["chi2_io_fullcov_contribution"]))

    jackknife = ap_analysis["jackknife"]["values"]
    if len(jackknife) != len(AP_JACKKNIFE_DELTA_CHI2):
        raise AssertionError(f"AP jackknife count: expected {len(AP_JACKKNIFE_DELTA_CHI2)}, got {len(jackknife)}")
    for index, (actual, expected) in enumerate(zip(jackknife, AP_JACKKNIFE_DELTA_CHI2), start=1):
        lines.append(assert_close(f"AP jackknife delta_chi2 {index}", float(actual), expected))

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

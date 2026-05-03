#!/usr/bin/env python3
"""Paper 35 v1.1 script 08: dark-sector consistency check.

Purpose:
    Check the geometric dark-sector ledger and manuscript-cited direct-detection
    limits. This is not a WIMP forecast model.

Inputs:
    data/imported_constants.json

Outputs:
    results/dark_matter_null_forecast_results.json

Claim boundary:
    CONDITIONAL FORECAST / consistency check. If the IO geometric dark-sector
    interpretation is correct, continued nulls are expected; a detection above
    about 5 GeV would falsify that interpretation.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA = BUNDLE_ROOT / "data"
RESULTS = BUNDLE_ROOT / "results"


EXPECTED_LIMITS = {
    "LZ_2024": {"limit_cm2": 2.2e-48, "mass_GeV": 40.0},
    "XENONnT": {"limit_cm2": 2.58e-47, "mass_GeV": 28.0},
    "PandaX4T": {"limit_cm2": 1.6e-47, "mass_GeV": 40.0},
}


def main() -> int:
    constants = json.loads((DATA / "imported_constants.json").read_text())
    fw = constants["framework_constants"]
    limits = constants["dark_matter_limits"]
    f_b = 2.0 * fw["gamma_BI"] / fw["x"]

    checks = {}
    for key, expected in EXPECTED_LIMITS.items():
        item = limits[key]
        checks[key] = {
            "source": item["source"],
            "limit_cm2": item["limit_cm2"],
            "mass_GeV": item["mass_GeV"],
            "matches_manuscript_limit": math.isclose(item["limit_cm2"], expected["limit_cm2"], rel_tol=0.0, abs_tol=0.0),
            "matches_manuscript_mass": math.isclose(item["mass_GeV"], expected["mass_GeV"], rel_tol=0.0, abs_tol=0.0),
        }

    payload = {
        "script": "08_dark_matter_null_forecast.py",
        "status": "verified",
        "claim_boundary": "conditional consistency check, not a forecast model",
        "framework_ledger": {
            "formula": "f_b = 2 gamma_BI / x",
            "f_b": f_b,
        },
        "experimental_limit_checks": checks,
        "conditional_forecast_statement": {
            "if_interpretation_correct": "continued nulls in canonical xenon-WIMP search channels are expected",
            "falsifier": "a robust direct-detection signal above approximately 5 GeV in the cited channels would falsify the IO geometric dark-sector interpretation",
            "not_claimed": "this script does not compute a new WIMP event-rate or forecast model",
        },
    }
    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / "dark_matter_null_forecast_results.json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"f_b": f_b, "limit_checks": checks}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

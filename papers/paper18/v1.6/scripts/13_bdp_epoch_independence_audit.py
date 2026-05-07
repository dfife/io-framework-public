"""Audit the Paper 18 baryon-dictionary epoch-independence issue.

This diagnostic scans the naive time-dependent form `f_b(eta)=2*gamma/x(eta)`
to show why the active BDP result must be interpreted as an observer-epoch
boundary-to-bulk inventory projection, not as a redshift-running baryon
fraction. It does not use the optical thermal readout and is unaffected by
the Paper 17 v1.5 R4/FIRAS correction.
"""

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
ROOT = BUNDLE_ROOT / "results"


def x_of_eta(eta: float) -> float:
    return 2.0 / (1.0 + math.cos(eta))


def main() -> None:
    gamma = 0.2375
    eta_values = [0.0, 0.2, 0.5, 1.0, 1.248585523971, 1.5, 2.0, 2.5, 3.0]
    rows = []
    for eta in eta_values:
        x = x_of_eta(eta)
        fb = 2.0 * gamma / x
        rows.append({"eta": eta, "x_eta": x, "fb_local": fb})

    payload = {
        "gamma": gamma,
        "formula_tested": "f_b(eta) = 2 gamma / x(eta), x(eta)=2/(1+cos eta)",
        "rows": rows,
        "present_epoch": {
            "eta_s": 1.248585523971,
            "x_eta_s": x_of_eta(1.248585523971),
            "fb_eta_s": 2.0 * gamma / x_of_eta(1.248585523971),
        },
        "horizon_epoch": {
            "eta_0": 0.0,
            "x_eta_0": x_of_eta(0.0),
            "fb_eta_0": 2.0 * gamma / x_of_eta(0.0),
        },
    }

    out = Path(str(ROOT / "paper18_bdp_epoch_independence_audit_checks.json"))
    out.write_text(json.dumps(payload, indent=2) + "\n")


if __name__ == "__main__":
    main()

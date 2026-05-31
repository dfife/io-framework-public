#!/usr/bin/env python3
"""Record the local Vaidya null-dust incompatibility diagnostic."""

from __future__ import annotations

import json
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    payload = {
        "status": "DERIVED/NO-GO",
        "vaidya_stress_tensor": "T_ab = (dM/dv)/(4*pi*r^2) l_a l_b",
        "perfect_radiation_fluid_requirement": "T_ab = (rho+p)u_a u_b + p g_ab with p=rho/3",
        "diagnostic_components": {
            "null_flux_component_nonzero_when_dMdv_nonzero": True,
            "angular_pressure_T_theta_theta": 0,
            "angular_pressure_T_phi_phi": 0,
            "isotropic_radiation_requires_positive_angular_pressure": True,
            "single_null_direction_selects_anisotropic_stress": True
        },
        "conclusion": (
            "A Vaidya null-dust phase carries directed null flux, not an isotropic "
            "thermal radiation bath. It is therefore retired as the cosmological "
            "radiation fluid in Paper 5 v2.0."
        ),
        "surviving_scope": (
            "This is a local stress-tensor incompatibility statement. It does not "
            "forbid using Vaidya geometry as a collapse or radiating-boundary model "
            "outside the isotropic interior-fluid role."
        )
    }
    out = BUNDLE_ROOT / "results" / "vaidya_no_go_results.json"
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(out)


if __name__ == "__main__":
    main()

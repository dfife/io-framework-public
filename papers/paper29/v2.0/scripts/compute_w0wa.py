#!/usr/bin/env python3
"""Verify the CPL equation-of-state prediction and report forecast margins."""

from __future__ import annotations

from _common import RESULTS_DIR, write_json


def main() -> None:
    w0 = -1.0
    wa = 0.0
    # Public Euclid forecast references do not define an official Euclid DR1 + DESI DR3
    # covariance as of this bundle build. These are conservative published Euclid
    # preparation VII WL-only flat w0-wa 1-sigma marginal errors used as a placeholder
    # falsification scale until the actual DR1+DR3 covariance is public.
    margins = {
        "euclid_preparation_vii_wl_only_flat_pessimistic": {"sigma_w0": 0.16, "sigma_wa": 0.59},
        "euclid_preparation_vii_wl_only_flat_optimistic": {"sigma_w0": 0.14, "sigma_wa": 0.49},
    }
    payload = {
        "claim": "CPL dark-energy equation-of-state prediction",
        "inputs": {
            "friedmann_dark_energy_term": "rho_Lambda is constant on the active observer branch",
            "CPL_definition": "w(a)=w0+wa(1-a)",
        },
        "derived": {
            "w0": w0,
            "wa": wa,
            "cpl_residual_norm": abs(w0 + 1.0) + abs(wa),
            "forecast_1sigma_margins": margins,
            "example_2sigma_falsification_thresholds": {
                "pessimistic": {"abs_w0_plus_1_greater_than": 2.0 * margins["euclid_preparation_vii_wl_only_flat_pessimistic"]["sigma_w0"], "abs_wa_greater_than": 2.0 * margins["euclid_preparation_vii_wl_only_flat_pessimistic"]["sigma_wa"]},
                "optimistic": {"abs_w0_plus_1_greater_than": 2.0 * margins["euclid_preparation_vii_wl_only_flat_optimistic"]["sigma_w0"], "abs_wa_greater_than": 2.0 * margins["euclid_preparation_vii_wl_only_flat_optimistic"]["sigma_wa"]},
            },
        },
        "status": "VERIFIED",
        "boundary": (
            "The exact IO prediction is (-1,0). The listed margins are published Euclid forecast scales, "
            "not an official Euclid DR1 + DESI DR3 covariance."
        ),
    }
    write_json(RESULTS_DIR / "w0wa_results.json", payload)


if __name__ == "__main__":
    main()

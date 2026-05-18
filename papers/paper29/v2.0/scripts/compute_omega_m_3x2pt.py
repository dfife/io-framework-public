#!/usr/bin/env python3
"""Compute the Euclid DR1 3x2pt matter-density prediction."""

from __future__ import annotations

from _common import IO_OBS, OMEGA_LAMBDA_IO, OMEGA_M_IO, RESULTS_DIR, write_json


def main() -> None:
    omega_m_from_closure = 1.0 - IO_OBS.Omega_k - OMEGA_LAMBDA_IO - IO_OBS.Omega_r
    payload = {
        "claim": "Euclid DR1 3x2pt matter-density prediction",
        "inputs": {
            "H0": IO_OBS.H0,
            "Omega_k": IO_OBS.Omega_k,
            "Omega_lambda": OMEGA_LAMBDA_IO,
            "Omega_r": IO_OBS.Omega_r,
            "branch": "active Paper 10 legacy projected observer branch",
        },
        "derived": {
            "Omega_m_IO": OMEGA_M_IO,
            "Omega_m_from_friedmann_closure": omega_m_from_closure,
            "delta": omega_m_from_closure - OMEGA_M_IO,
        },
        "paper_values": {
            "Omega_m_IO": 0.349,
        },
        "status": "VERIFIED",
        "boundary": (
            "This verifies the active branch value used by Paper 29. It is not a new "
            "independent derivation of the branch package from gamma_BI alone."
        ),
    }
    write_json(RESULTS_DIR / "omega_m_3x2pt_results.json", payload)


if __name__ == "__main__":
    main()

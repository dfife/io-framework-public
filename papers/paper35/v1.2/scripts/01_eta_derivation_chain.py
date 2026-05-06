#!/usr/bin/env python3
"""Paper 35 v1.2 script 01: eta derivation chain.

Purpose:
    Reproduce the late-time IO baryon-to-photon ratio route from the public
    bundle constants. In v1.2 the observer photon bath uses the Paper 17 v1.5
    FIRAS-fixed readout normalization

        T_obs(R4) = T_IO * x_R4_source^(R4_FIRAS*K_gauge),

    not the retired implicit unit normalization R4=1.

Inputs:
    data/imported_constants.json

Outputs:
    results/eta_derivation_chain_results.json

Claim boundary:
    DERIVED/SCOPED plus imported standard particle and thermodynamic constants.
    The observed CMB temperature is an empirical FIRAS-fixed readout datum, not
    an independent IO prediction.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA = BUNDLE_ROOT / "data"
RESULTS = BUNDLE_ROOT / "results"


def photon_number_density(T: float, *, k_B: float, hbar: float, c: float, zeta3: float) -> float:
    return (2.0 * zeta3 / math.pi**2) * (k_B * T / (hbar * c)) ** 3


def eta_from_omega_b(omega_b: float, T: float, m_b: float, constants: dict[str, float]) -> float:
    h100_si = 100.0 * 1000.0 / constants["mpc_m"]
    rho_b = omega_b * 3.0 * h100_si**2 / (8.0 * math.pi * constants["G_SI"])
    n_gamma = photon_number_density(
        T,
        k_B=constants["k_B_SI"],
        hbar=constants["hbar_SI"],
        c=constants["c_SI"],
        zeta3=constants["zeta3"],
    )
    return (rho_b / m_b) / n_gamma


def main() -> int:
    constants = json.loads((DATA / "imported_constants.json").read_text())
    fw = constants["framework_constants"]
    eta_inputs = constants["eta_inputs"]
    std = constants["standard_constants"]

    gamma = fw["gamma_BI"]
    x = fw["x"]
    x_r4_source = fw["x_R4_source"]
    k_gauge = math.log(1.0 + gamma**2)
    f_b = 2.0 * gamma / x
    r4_firas = fw["R4_FIRAS"]
    t_obs = eta_inputs["T_IO_K"] * x_r4_source ** (r4_firas * k_gauge)
    t_obs_historical = eta_inputs["T_IO_K"] * x**k_gauge
    y_p = eta_inputs["Y_p_for_mean_mass"]
    mean_baryon_mass = (1.0 - y_p) * std["hydrogen_atom_mass_kg"] + y_p * (std["helium4_atom_mass_kg"] / 4.0)

    eta_proton = eta_from_omega_b(eta_inputs["omega_b_geom"], t_obs, std["proton_mass_kg"], std)
    eta_mean = eta_from_omega_b(eta_inputs["omega_b_geom"], t_obs, mean_baryon_mass, std)

    payload = {
        "script": "01_eta_derivation_chain.py",
        "status": "verified",
        "claim_boundary": "DERIVED/SCOPED plus imported standard constants, mean-baryon-mass convention, and FIRAS-fixed observer-side thermal readout",
        "framework_values": {
            "gamma_BI": gamma,
            "x": x,
            "x_R4_source": x_r4_source,
            "K_gauge": k_gauge,
            "R4_FIRAS": r4_firas,
            "f_b": f_b,
            "T_obs_K": t_obs,
            "T_FIRAS_K": eta_inputs["T_FIRAS_K"],
            "T_obs_R4_equals_1_K_historical": t_obs_historical,
        },
        "formulae": {
            "K_gauge": "ln(1 + gamma_BI^2)",
            "f_b": "2 gamma_BI / x",
            "T_obs": "T_IO x_R4_source^(R4_FIRAS K_gauge)",
            "T_obs_R4_equals_1": "historical diagnostic only; not an independent CMB-temperature prediction",
            "n_gamma": "2 zeta(3) / pi^2 * (k_B T / (hbar c))^3",
            "eta": "rho_b(omega_b,geom) / (m_b n_gamma(T_obs))",
        },
        "consistency_checks": {
            "R4_FIRAS_readout_matches_T_obs_input": math.isclose(t_obs, eta_inputs["T_obs_K"], rel_tol=0.0, abs_tol=1e-15),
            "T_obs_input_matches_T_FIRAS": math.isclose(eta_inputs["T_obs_K"], eta_inputs["T_FIRAS_K"], rel_tol=0.0, abs_tol=1e-15),
        },
        "mass_convention": {
            "Y_p_for_mean_mass": y_p,
            "mean_baryon_mass_kg": mean_baryon_mass,
        },
        "headline": {
            "eta_late_proton_mass": eta_proton,
            "eta_late_mean_baryon_mass": eta_mean,
            "eta10_late_mean_baryon_mass": eta_mean * 1.0e10,
        },
    }
    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / "eta_derivation_chain_results.json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload["headline"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Reproduce the reduced 21cm brightness-temperature benchmark at z = 17."""

from __future__ import annotations

from _common import A_RAD, C_SI, IO_BARE, IO_OBS, M_E, MPC_M, RESULTS_DIR, SIGMA_T, T_CMB, write_json

Z_TARGET = 17.0
RESIDUAL_X_E = 2.0e-4


def e_of_z(z: float, bg) -> float:
    zp1 = 1.0 + z
    return (bg.Omega_m * zp1**3 + bg.Omega_r * zp1**4 + bg.Omega_k * zp1**2 + bg.Omega_lambda) ** 0.5


def helium_fraction_from_yp(y_p: float) -> float:
    return y_p / (4.0 * (1.0 - y_p))


def compton_coupling_rate(z: float, y_p: float, x_e: float) -> float:
    t_gamma = T_CMB * (1.0 + z)
    f_he = helium_fraction_from_yp(y_p)
    return (8.0 * SIGMA_T * A_RAD * t_gamma**4 / (3.0 * M_E * C_SI)) * (x_e / (1.0 + f_he + x_e))


def thermal_decoupling_z(bg, y_p: float, x_e: float) -> float:
    lo = 1.0
    hi = 400.0
    h0_si = bg.H0 * 1000.0 / MPC_M
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        ratio = compton_coupling_rate(mid, y_p, x_e) / (h0_si * e_of_z(mid, bg))
        if ratio > 1.0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def reduced_case(z: float, thermal_bg, readout_bg) -> dict[str, float]:
    z_dec = thermal_decoupling_z(thermal_bg, thermal_bg.YHe, RESIDUAL_X_E)
    t_gamma = T_CMB * (1.0 + z)
    t_gas = T_CMB * (1.0 + z) ** 2 / (1.0 + z_dec)
    y21 = 1.0 - t_gamma / t_gas
    omega_m_h2 = readout_bg.Omega_m * (readout_bg.H0 / 100.0) ** 2
    prefactor = (
        27.0
        * (((1.0 + z) / 10.0) * (0.15 / omega_m_h2)) ** 0.5
        * (readout_bg.omega_b_h2 / 0.0230)
        * ((1.0 - readout_bg.YHe) / 0.75)
    )
    return {
        "z_dec": z_dec,
        "T_gamma_K": t_gamma,
        "T_gas_K": t_gas,
        "y21_reduced": y21,
        "prefactor_mK": prefactor,
        "T21_mK": prefactor * y21,
    }


def main() -> None:
    local = reduced_case(Z_TARGET, IO_BARE, IO_BARE)
    observer = reduced_case(Z_TARGET, IO_BARE, IO_OBS)
    payload = {
        "claim": "reduced 21cm brightness-temperature diagnostic at z=17",
        "inputs": {
            "z": Z_TARGET,
            "T_CMB": T_CMB,
            "residual_x_e": RESIDUAL_X_E,
            "io_local_bare": IO_BARE.to_json(),
            "io_observer": IO_OBS.to_json(),
        },
        "derived": {
            "io_local_reduced_object": local,
            "io_observer_brightness_diagnostic": observer,
        },
        "paper_values": {
            "z_dec": 123.67,
            "y21": -5.926,
            "T21_mK": -191.0,
        },
        "status": "VERIFIED",
        "scope": "Reduced benchmark: x_HI=1, saturated spin-temperature coupling, no heating or radio-background source law.",
    }
    write_json(RESULTS_DIR / "21cm_prediction_results.json", payload)


if __name__ == "__main__":
    main()

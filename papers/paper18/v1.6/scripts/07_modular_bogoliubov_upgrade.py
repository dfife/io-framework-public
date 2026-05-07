"""Check the repaired Paper 18 modular Bogoliubov upgrade theorem.

The script demonstrates the reduced quasi-free CCR/KMS transport calculation
behind Paper 18's Bogoliubov spectrum theorem. Paper 18 v1.5 used the historical
unit readout `T_obs = T_IO*x^K_gauge`. Paper 18 v1.6 uses the active Paper 17
v1.5 boundary instead:

    T_obs(R4) = T_IO*x^(R4_FIRAS*K_gauge), R4_FIRAS = 1.0031014644.

This preserves the theorem that the reduced sector has a Planck/KMS spectrum
at the observer-side temperature, but it removes the old claim that IO
independently predicts the observed CMB temperature.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
ROOT = BUNDLE_ROOT / "results"

HBAR = 1.054571817e-34
KB = 1.380649e-23
GAMMA_BI = 0.2375
X = 1.51899
X_R4_SOURCE = 1.519
K_GAUGE = math.log(1.0 + GAMMA_BI**2)
T_IO = 2.6635
R4_FIRAS = 1.0031014644
T_FIRAS = 2.7255


def bose_n(omega: float, temperature: float) -> float:
    return 1.0 / math.expm1(HBAR * omega / (KB * temperature))


def alpha_beta(omega: float, temperature: float) -> tuple[float, float]:
    n = bose_n(omega, temperature)
    return math.sqrt(1.0 + n), math.sqrt(n)


def dilation_pushforward(omega: float, lam: float, kappa: float) -> float:
    return math.exp(-kappa * lam) * omega


def transformed_occupancy(omega: float, lam: float, kappa: float, t0: float) -> float:
    # covariance transported by dilation in nu = ln omega
    return bose_n(dilation_pushforward(omega, lam, kappa), t0)


def main() -> None:
    omega_sample = 2.0 * KB * T_IO / HBAR
    lam_sample = math.log(X_R4_SOURCE)
    t_obs = T_IO * math.exp(R4_FIRAS * K_GAUGE * lam_sample)

    n_direct_io = bose_n(omega_sample, T_IO)
    n_direct_obs = bose_n(omega_sample, t_obs)
    n_from_modular = transformed_occupancy(omega_sample, lam_sample, R4_FIRAS * K_GAUGE, T_IO)

    a_io, b_io = alpha_beta(omega_sample, T_IO)
    a_obs, b_obs = alpha_beta(omega_sample, t_obs)

    # Explicit general no-go for the naive converse: same trivial flow, many KMS states
    # On the abelian algebra C^2 with identity dynamics, any faithful state is KMS at beta=1.
    general_counterexample = {
        "algebra": "C^2",
        "dynamics": "identity",
        "state_1": [0.5, 0.5],
        "state_2": [0.3, 0.7],
        "same_flow": True,
        "both_faithful": True,
        "both_1_KMS": True,
    }

    payload = {
        "inputs": {
            "gamma_BI": GAMMA_BI,
            "x": X,
            "x_R4_source": X_R4_SOURCE,
            "K_gauge": K_GAUGE,
            "R4_FIRAS": R4_FIRAS,
            "T_IO": T_IO,
            "T_FIRAS": T_FIRAS,
            "lambda_sample": lam_sample,
            "T_obs": t_obs,
            "T_obs_minus_FIRAS": t_obs - T_FIRAS,
            "omega_sample": omega_sample,
        },
        "general_converse_counterexample": general_counterexample,
        "repaired_theorem_class": {
            "algebra": "reduced bosonic Weyl/CCR thermal photon algebra",
            "state_class": "continuous gauge-invariant quasi-free states",
            "one_particle_operator": "Omega >= 0",
            "transport_generator": "D tensor K_hat_g",
        },
        "uniqueness_checks": {
            "n_direct_IO": n_direct_io,
            "n_direct_obs": n_direct_obs,
            "n_from_modular_pushforward": n_from_modular,
            "modular_transport_residual": n_from_modular - n_direct_obs,
            "alpha_io_sq_minus_beta_io_sq_minus_1": a_io * a_io - b_io * b_io - 1.0,
            "alpha_obs_sq_minus_beta_obs_sq_minus_1": a_obs * a_obs - b_obs * b_obs - 1.0,
        },
        "theorem_formulas": {
            "base_covariance": "rho_IO = (exp(hbar*Omega/(k_B*T_IO)) - I)^(-1)",
            "transported_temperature": "T(lambda) = T_IO * exp(R4_FIRAS*kappa*lambda) on the FIRAS-fixed v1.6 readout.",
            "transported_covariance": "rho_lambda(omega) = 1 / (exp(hbar*omega/(k_B*T(lambda))) - 1)",
            "beta_squared": "|beta_lambda(omega)|^2 = rho_lambda(omega)",
        },
    }

    (ROOT / "paper18_modular_bogoliubov_upgrade_checks.json").write_text(
        json.dumps(payload, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()

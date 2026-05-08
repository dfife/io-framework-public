from decimal import Decimal, getcontext
import json
from pathlib import Path

"""
Reproduce the modular-scalarization checks used to reject the numerical
``f_b*K_gauge`` echo as a theorem.

The v1.6 script uses the Paper 17 v1.5 FIRAS-fixed readout factor
``x^(R4*K_gauge)`` wherever a thermal observer readout factor is needed. This
does not turn the CMB temperature into a prediction; it simply propagates the
frozen FIRAS normalization through the diagnostic arithmetic.

Output:
    ../results/modular_scalarization_audit_results.json
"""

getcontext().prec = 100


def ln(x: Decimal) -> Decimal:
    return x.ln()


def exp(x: Decimal) -> Decimal:
    return x.exp()


def sqrt(x: Decimal) -> Decimal:
    return x.sqrt()


def main() -> None:
    x = Decimal("1.51899")
    gamma = Decimal("0.2375")
    R4_FIRAS = Decimal("1.0031014644")
    omega_m_geom_h2 = Decimal("0.06721104357")

    Q = Decimal(1) + gamma * gamma
    K_gauge = ln(Q)
    transfer_factor = exp(R4_FIRAS * K_gauge * ln(x))

    f_b = Decimal(2) * gamma / x
    omega_b_alpha1 = omega_m_geom_h2 * f_b

    J_transport = Decimal(1) / sqrt(x)
    omega_b_alpha_3_over_2 = omega_b_alpha1 * J_transport

    J_slice = Decimal(1) / x
    omega_b_alpha_2 = omega_b_alpha1 * J_slice

    modular_echo = f_b * K_gauge
    omega_b_alpha1_modular_multiplicative = omega_b_alpha1 * transfer_factor
    f_b_modular_multiplicative = f_b * transfer_factor

    out = {
        "inputs": {
            "x": str(x),
            "gamma": str(gamma),
            "R4_FIRAS": str(R4_FIRAS),
            "omega_m_geom_h2": str(omega_m_geom_h2),
        },
        "reduced_modular_data": {
            "Q = 1 + gamma^2": str(Q),
            "K_gauge = ln(Q)": str(K_gauge),
            "FIRAS_fixed_GTTP_transfer_factor = x^(R4*K_gauge)": str(transfer_factor),
            "temperature_status": "FIRAS fixes R4 in Paper 17 v1.5; this script uses the repaired readout factor where a thermal observer factor is needed.",
        },
        "baryon_branches": {
            "f_b = 2gamma/x": str(f_b),
            "omega_b_alpha_1": str(omega_b_alpha1),
            "J_transport = x^(-1/2)": str(J_transport),
            "omega_b_alpha_3_over_2": str(omega_b_alpha_3_over_2),
            "J_slice = x^(-1)": str(J_slice),
            "omega_b_alpha_2": str(omega_b_alpha_2),
        },
        "modular_echo_tests": {
            "f_b_times_K_gauge": str(modular_echo),
            "omega_b_alpha_1_times_x^(R4*K_gauge)": str(omega_b_alpha1_modular_multiplicative),
            "f_b_times_x^(R4*K_gauge)": str(f_b_modular_multiplicative),
            "echo_over_alpha_3_over_2": str(modular_echo / omega_b_alpha_3_over_2),
            "K_gauge_over_omega_m_geom_h2_times_x^(-1/2)": str(
                K_gauge / (omega_m_geom_h2 * J_transport)
            ),
            "echo_minus_alpha_3_over_2": str(modular_echo - omega_b_alpha_3_over_2),
        },
        "interpretation_flags": {
            "timelike_modular_history_sector_exists": True,
            "intrinsic_slice_codifferential_is_not_part_of_reduced_modular_algebra": True,
            "modular_echo_is_not_exact_transport_semigroup_output": True,
            "modular_echo_is_not_exact_alpha_3_over_2_identity": True,
        },
    }

    out_path = Path(__file__).resolve().parents[1] / "results" / "modular_scalarization_audit_results.json"
    out_path.write_text(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()

from decimal import Decimal, getcontext
import json
from pathlib import Path

"""
Reproduce the Paper 19 bridge-theorem arithmetic for the baryon scalarization
result.

This script is intentionally small: it does not refit BOSS data. It checks the
internal bridge arithmetic used after the theorem argument selects the timelike
continuity-response class:

    f_b = 2 gamma / x
    J_transport = x^(-1/2)
    omega_b(alpha=3/2) = omega_m,geom h^2 * f_b * J_transport

Output:
    ../results/bridge_theorems_results.json
"""

getcontext().prec = 100


def sqrt(x: Decimal) -> Decimal:
    return x.sqrt()


def main() -> None:
    x = Decimal("1.51899")
    gamma = Decimal("0.2375")
    omega_m_geom_h2 = Decimal("0.06721104357")

    f_b = Decimal(2) * gamma / x
    omega_b_alpha_1 = omega_m_geom_h2 * f_b
    J_transport = Decimal(1) / sqrt(x)
    omega_b_alpha_3_over_2 = omega_b_alpha_1 * J_transport

    out = {
        "inputs": {
            "x": str(x),
            "gamma": str(gamma),
            "omega_m_geom_h2": str(omega_m_geom_h2),
        },
        "bridge_1_density_reconstruction": {
            "dust_current": "J^mu = rho u^mu",
            "flow_orthogonal_volume_measure": "mu_perp = i_u(vol_4)",
            "density_as_rn_derivative": "rho_eta = d nu_eta / d mu_perp,eta",
            "os_dust_is_hypersurface_orthogonal": True,
            "reduced_history_algebra_supplies_vol4_weight": True,
            "scalarization_class_selected": "timelike continuity-response",
        },
        "bridge_2_representation_theorem": {
            "equal_eta_slice_is_representation": True,
            "fourier_decomposition_is_unitary_basis_change_on_L2_of_slice": True,
            "spatial_hodge_for_scalar_modes_is_not_new_operator_class": True,
        },
        "bridge_3_no_go": {
            "independent_slice_codifferential_density_in_reduced_dust_class": False,
            "codifferential_can_appear_only_as_notational_representation_of_divergence": True,
            "counterexample_within_reduced_density_class_found": False,
        },
        "resulting_branch": {
            "J = x^(-1/2)": str(J_transport),
            "omega_b_alpha_3_over_2": str(omega_b_alpha_3_over_2),
            "alpha": "3/2",
        },
    }

    out_path = Path(__file__).resolve().parents[1] / "results" / "bridge_theorems_results.json"
    out_path.write_text(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()

import importlib.util
import json
import math
from pathlib import Path

import sympy as sp

"""
Reproduce the scalarization-Jacobian audit for the Paper 19 alpha=3/2 branch.

The symbolic part checks the timelike free-fall contraction/divergence
scaling. The numerical part reuses script 04's public BOSS audit functions to
show that BOSS alone does not select alpha=3/2; the alpha assignment must come
from the theorem chain, not from fitting the measurement.

Output:
    ../results/scalarization_jacobian_results.json
"""

BUNDLE_ROOT = Path(__file__).resolve().parents[1]
BASE = BUNDLE_ROOT
OUT_JSON = BUNDLE_ROOT / "results" / "scalarization_jacobian_results.json"

R4_FIRAS = 1.0031014644
T_FIRAS = 2.7255


def load_schur_module():
    spec = importlib.util.spec_from_file_location(
        "schur_audit", BUNDLE_ROOT / "scripts" / "04_boss_fullshape_baryon_audit.py"
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    x = 1.51899
    gamma = 0.2375
    omega_m_geom_h2 = 0.197 * (0.5841**2)
    omega_b_alpha1 = omega_m_geom_h2 * (2.0 * gamma / x)

    # Symbolic geometry
    r, rs, a, chi, q = sp.symbols("r rs a chi q", positive=True)
    v = sp.sqrt(rs / r)
    k_tan = v / r
    div_v_pg = sp.simplify((1 / r**2) * sp.diff(r**2 * v, r))
    contracted_1form = sp.simplify((1 / r) * v)
    div_to_ktan_ratio = sp.simplify(div_v_pg / k_tan)

    # On the OS constant-eta 3-sphere, for a homologous radial 1-form omega = q a dchi,
    # the codifferential scales as q/a up to the angular factor 2 cot(chi).
    delta_sigma = sp.simplify(2 * q / (a * sp.tan(chi)))

    J_transport = x ** (-0.5)
    J_slice = x ** (-1.0)
    alpha_transport = 1.5
    alpha_slice = 2.0

    omega_b_alpha32 = omega_b_alpha1 * J_transport
    omega_b_alpha2 = omega_b_alpha1 * J_slice

    schur = load_schur_module()
    schur.ensure_data()
    samples = schur.load_samples()
    As = 2.1e-9
    ns = 0.9649
    tau = 0.0544
    mode = "amp_const_k_k2"

    def chi2_for(alpha: float, neff: float) -> float:
        omega_b = omega_m_geom_h2 * (2.0 * gamma / (x**alpha))
        scenario = schur.make_scenario(
            name=f"alpha_{alpha}_Neff_{neff}",
            H0=68.91,
            Omega_m=0.335,
            Omega_k=-0.006,
            T0=T_FIRAS,
            Neff=neff,
            omega_b=omega_b,
        )
        chi2, _details = schur.evaluate_scenario(
            scenario, As=As, ns=ns, tau=tau, samples=samples, mode=mode
        )
        return chi2

    payload = {
        "inputs": {
            "x": x,
            "gamma": gamma,
            "omega_m_geom_h2": omega_m_geom_h2,
            "omega_b_alpha1": omega_b_alpha1,
        },
        "transport_scalarization": {
            "radial_free_fall_speed_v(r)": str(v),
            "line_to_scalar_contraction_scaling": str(contracted_1form),
            "pg_divergence_of_v": str(div_v_pg),
            "K_tan_scaling": str(k_tan),
            "divergence_to_K_tan_ratio": str(div_to_ktan_ratio),
            "J_transport = x^(-1/2)": J_transport,
            "alpha_transport": alpha_transport,
            "omega_b_alpha_3_over_2": omega_b_alpha32,
        },
        "slice_scalarization": {
            "OS_slice_codifferential_for_homologous_radial_1form": str(delta_sigma),
            "J_slice = x^(-1)": J_slice,
            "alpha_slice": alpha_slice,
            "omega_b_alpha_2": omega_b_alpha2,
        },
        "boss_fullshape_chi2": {
            "N_eff_3.046": {
                "alpha_1": chi2_for(1.0, 3.046),
                "alpha_1.5": chi2_for(1.5, 3.046),
                "alpha_2": chi2_for(2.0, 3.046),
            },
            "N_eff_5.0": {
                "alpha_1": chi2_for(1.0, 5.0),
                "alpha_1.5": chi2_for(1.5, 5.0),
                "alpha_2": chi2_for(2.0, 5.0),
            },
        },
        "interpretation_flags": {
            "transport_map_produces_half_integer_alpha": True,
            "slice_map_produces_area_class_alpha_2": True,
            "geometry_alone_does_not_select_unique_scalarization": True,
        },
    }

    OUT_JSON.write_text(json.dumps(payload, indent=2) + "\n")


if __name__ == "__main__":
    main()

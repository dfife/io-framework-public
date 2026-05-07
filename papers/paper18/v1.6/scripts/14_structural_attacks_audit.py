"""Run the Paper 18 structural-attack ledger checks.

The audit records three known attacks: abelian modular-flow terminology,
naive BDP time-dependence, and coordinate-pullback ambiguity. These are
structural diagnostics for CMP/BDP/V(alpha) and do not consume the optical
thermal readout. R4 damage is handled separately in the v1.6 kappa audit.
"""

import json
import math
from pathlib import Path


def main() -> None:
    gamma = 0.2375
    eta_s = 1.248585523971  # current Schwarzschild-interior spatial epoch used in the paper stack

    x_horizon = 2.0 / (1.0 + math.cos(0.0))
    x_obs = 2.0 / (1.0 + math.cos(eta_s))

    fb_naive_horizon = 2.0 * gamma / x_horizon
    fb_naive_obs = 2.0 * gamma / x_obs

    kr = 2.0 / math.sqrt(math.e)

    alpha = math.atan(gamma)
    v_alpha = -2.0 * math.log(math.cos(alpha))

    beta = math.asinh(gamma)
    v_beta = 2.0 * math.log(math.cosh(beta))

    payload = {
        "attack1_commutative_modular_fact": {
            "statement": "On an abelian algebra, the modular automorphism of the algebra is trivial; the nontrivial object is the relative modular operator between weights.",
            "status": "valid_terminology_attack",
        },
        "attack2_bdp_time_dependence": {
            "gamma": gamma,
            "eta_s": eta_s,
            "x_horizon": x_horizon,
            "x_observer": x_obs,
            "naive_fb_horizon": fb_naive_horizon,
            "naive_fb_observer": fb_naive_obs,
            "naive_percent_shift": 100.0 * (fb_naive_horizon - fb_naive_obs) / fb_naive_obs,
        },
        "attack3_coordinate_pullback": {
            "gamma": gamma,
            "alpha": alpha,
            "beta": beta,
            "V_alpha": v_alpha,
            "V_beta": v_beta,
            "difference": v_alpha - v_beta,
        },
        "kruskal_exact_factor": kr,
    }

    out = Path(__file__).resolve().parents[1] / "results" / "paper18_structural_attacks_audit_checks.json"
    out.write_text(json.dumps(payload, indent=2) + "\n")


if __name__ == "__main__":
    main()

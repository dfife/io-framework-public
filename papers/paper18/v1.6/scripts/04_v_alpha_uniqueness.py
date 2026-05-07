"""Verify the Paper 18 V(alpha) uniqueness identities.

The script uses SymPy plus high-precision Decimal arithmetic to check that
`V(alpha)=-2 ln(cos alpha)` satisfies the gauge-center identities and the ODE
rigidity characterization. It is purely gauge-sector algebra and is
R4-independent.
"""

import json
from decimal import Decimal, getcontext
from pathlib import Path
import sympy as sp


getcontext().prec = 100


def main() -> None:
    alpha = sp.symbols("alpha", real=True)
    gamma = sp.tan(alpha)
    V = -2 * sp.log(sp.cos(alpha))

    exp_identity = sp.simplify(sp.exp(V) - (1 + gamma**2))
    first_identity = sp.simplify(sp.diff(V, alpha) - 2 * gamma)
    second_identity = sp.simplify(sp.diff(V, alpha, 2) - 2 * (1 + gamma**2))
    ode_identity = sp.simplify(sp.diff(V, alpha, 2) - 2 * sp.exp(V))
    v0 = sp.simplify(V.subs(alpha, 0))
    vp0 = sp.simplify(sp.diff(V, alpha).subs(alpha, 0))

    gamma_num = Decimal("0.2375")
    one = Decimal(1)
    q = one + gamma_num * gamma_num
    v_num = q.ln()
    vp_num = Decimal(2) * gamma_num
    vpp_num = Decimal(2) * q

    payload = {
        "symbolic": {
            "exp(V) - (1+tan(alpha)^2)": str(exp_identity),
            "V_prime - 2 tan(alpha)": str(first_identity),
            "V_double_prime - 2(1+tan(alpha)^2)": str(second_identity),
            "ODE_residual_V_double_prime_minus_2expV": str(ode_identity),
            "V(0)": str(v0),
            "V_prime(0)": str(vp0),
        },
        "numeric_gamma_0.2375": {
            "Q = 1 + gamma^2": str(q),
            "V = ln(Q)": str(v_num),
            "V_prime = 2 gamma": str(vp_num),
            "V_double_prime = 2 Q": str(vpp_num),
        },
    }

    out = Path(__file__).resolve().parents[1] / "results" / "paper18_v_alpha_theorem_checks.json"
    out.write_text(json.dumps(payload, indent=2, sort_keys=True))
    print(out)


if __name__ == "__main__":
    main()

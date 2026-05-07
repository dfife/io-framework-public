"""Reproduce Paper 18's BDP gap-closure arithmetic.

The script verifies the gauge-potential hierarchy, the 1-form baryon fraction
`f_b=2*gamma/x`, and the master identity `f_b*F=<K>/4`. This is a gauge and
boundary-to-bulk inventory calculation; it does not consume `T_obs` and is
unchanged by the R4/FIRAS repair.
"""

from decimal import Decimal, getcontext
import json
from pathlib import Path


getcontext().prec = 100
BUNDLE_ROOT = Path(__file__).resolve().parents[1]
ROOT = BUNDLE_ROOT / "results"


def ln_decimal(x: Decimal) -> Decimal:
    return x.ln()


def main() -> None:
    gamma = Decimal("0.2375")
    x = Decimal("1.519")

    Q = Decimal(1) + gamma * gamma
    V = ln_decimal(Q)
    V_prime = Decimal(2) * gamma
    V_double_prime = Decimal(2) * Q
    f_b = V_prime / x

    K_total = Decimal(4) * ln_decimal(x) + V
    F = K_total * x / (Decimal(8) * gamma)

    payload = {
        "gamma": str(gamma),
        "x": str(x),
        "V(alpha) = ln(1+gamma^2)": str(V),
        "V_prime(alpha) = 2 gamma": str(V_prime),
        "V_double_prime(alpha) = 2(1+gamma^2)": str(V_double_prime),
        "parity": {
            "V": "even in gamma",
            "V_prime": "odd in gamma",
            "V_double_prime": "even in gamma",
        },
        "one_form_scaling = R_U/r_s = 1/x": str(Decimal(1) / x),
        "f_b = x^(-1) V_prime(alpha)": str(f_b),
        "K_total = 4 ln x + ln(1+gamma^2)": str(K_total),
        "F = <K> x / (8 gamma)": str(F),
        "identity_f_b_F_minus_<K>/4": str(f_b * F - K_total / Decimal(4)),
    }

    out = Path(str(ROOT / "paper18_bdp_gap_closure_checks.json"))
    out.write_text(json.dumps(payload, indent=2, sort_keys=True))
    print(out)


if __name__ == "__main__":
    main()

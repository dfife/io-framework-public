"""Check the Paper 18 BDP Modular Derivation theorem values.

Outputs the exact Decimal arithmetic behind `f_b = 2*gamma/x` and the identity
`f_b*F = <K>/4`. The script is intentionally small because the theorem's
load-bearing content is algebraic. It is R4-independent.
"""

import json
from decimal import Decimal, getcontext
from pathlib import Path

getcontext().prec = 100


def d(x: str) -> Decimal:
    return Decimal(x)


def run():
    gamma = d("0.2375")
    x = d("1.519")
    one = d("1")

    V_prime = d("2") * gamma
    f_b = V_prime / x
    Q = one + gamma * gamma
    K_total = ((x ** 4) * Q).ln()
    F = K_total * x / (d("8") * gamma)

    return {
        "gamma": str(gamma),
        "x": str(x),
        "V_prime = 2 gamma": str(V_prime),
        "f_b = V_prime / x = 2 gamma / x": str(f_b),
        "K_total = ln Delta": str(K_total),
        "F = <K> x / (8 gamma)": str(F),
        "f_b * F": str(f_b * F),
        "<K> / 4": str(K_total / d("4")),
        "identity_error = f_b*F - <K>/4": str((f_b * F) - (K_total / d("4"))),
    }


if __name__ == "__main__":
    out = run()
    path = str(Path(__file__).resolve().parents[1] / "results" / "paper18_bdp_theorem_checks.json")
    with open(path, "w", encoding="ascii") as f:
        json.dump(out, f, indent=2, sort_keys=True)
        f.write("\n")
    print(json.dumps(out, indent=2, sort_keys=True))

"""Check the Paper 18 CMP Modular Realization theorem values.

This script verifies the relative-modular decomposition
`<K> = K_geom + K_gauge = ln[x^4(1+gamma^2)]`. It is a reduced observer-algebra
calculation and does not involve the observer thermal readout `R4`.
"""

import json
from decimal import Decimal, getcontext
from pathlib import Path

getcontext().prec = 100


def d(x: str) -> Decimal:
    return Decimal(x)


def ln_decimal(x: Decimal) -> Decimal:
    return x.ln()


def run():
    x = d("1.519")
    gamma = d("0.2375")
    one = d("1")

    K_geom = d("4") * ln_decimal(x)
    Q = one + gamma * gamma
    K_gauge = ln_decimal(Q)
    Delta = (x ** 4) * Q
    ln_Delta = ln_decimal(Delta)
    additive_error = K_geom + K_gauge - ln_Delta

    # Toy commutative history algebra check:
    # dPhi_0 = a0^4 dm, dPhi_eta = a_eta^4 dm, with x = a0 / a_eta
    rn_derivative = x ** 4
    K_geom_from_rn = ln_decimal(rn_derivative)

    return {
        "x": str(x),
        "gamma": str(gamma),
        "Q = 1 + gamma^2": str(Q),
        "K_geom = 4 ln x": str(K_geom),
        "K_gauge = ln(1 + gamma^2)": str(K_gauge),
        "Delta = x^4 (1 + gamma^2)": str(Delta),
        "ln Delta": str(ln_Delta),
        "additive_error = K_geom + K_gauge - ln Delta": str(additive_error),
        "toy_commutative_geometry": {
            "dPhi_0 / dPhi_eta": str(rn_derivative),
            "ln(dPhi_0 / dPhi_eta)": str(K_geom_from_rn),
            "matches_K_geom": str(K_geom_from_rn == K_geom),
        },
    }


if __name__ == "__main__":
    out = run()
    path = str(Path(__file__).resolve().parents[1] / "results" / "paper18_cmp_theorem_checks.json")
    with open(path, "w", encoding="ascii") as f:
        json.dump(out, f, indent=2, sort_keys=True)
        f.write("\n")
    print(json.dumps(out, indent=2, sort_keys=True))

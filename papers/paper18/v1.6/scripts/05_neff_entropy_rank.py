"""Verify the Paper 18 acoustic entropy-rank theorem.

The theorem-grade mathematical result is that a uniform modular-cell covariance
with total measure `Delta=x^4(1+gamma^2)` has entropy-rank `Delta`. Paper 18
withdraws the extra physical identification `N_eff=Delta` as a Friedmann
radiation parameter after the P(k) no-go. This script reproduces the math-only
entropy-rank result and is independent of R4.
"""

from __future__ import annotations

import json
from decimal import Decimal, getcontext
from pathlib import Path

import mpmath as mp
import sympy as sp


def main() -> None:
    getcontext().prec = 80
    mp.mp.dps = 80

    x_sym, gamma_sym, u_sym = sp.symbols("x gamma u", positive=True, real=True)
    Delta_sym = x_sym**4 * (1 + gamma_sym**2)
    rho_sym = 1 / Delta_sym
    S_sym = sp.integrate(-rho_sym * sp.log(rho_sym), (u_sym, 0, Delta_sym))
    N_eff_sym = sp.simplify(sp.exp(S_sym))
    f_eff_sym = sp.simplify(Delta_sym / (2 * sp.log(Delta_sym)))
    P_k_sym = sp.simplify(sp.exp(-Delta_sym / 2))

    x = Decimal("1.519")
    gamma = Decimal("0.2375")
    Delta = x**4 * (Decimal(1) + gamma**2)

    x_mp = mp.mpf(str(x))
    gamma_mp = mp.mpf(str(gamma))
    Delta_mp = x_mp**4 * (1 + gamma_mp**2)
    rho_mp = 1 / Delta_mp
    S_mp = mp.quad(lambda t: -rho_mp * mp.log(rho_mp), [0, Delta_mp])
    N_eff_mp = mp.e ** S_mp
    f_eff_mp = Delta_mp / (2 * mp.log(Delta_mp))
    P_k_mp = mp.e ** (-Delta_mp / 2)

    # Discrete toy model: normalized flat spectrum on N bins has entropy-rank N exactly.
    toy_bins = [4, 16, 128]
    toy_checks = {}
    for n in toy_bins:
        p = [mp.mpf(1) / n] * n
        S_n = -mp.fsum(pi * mp.log(pi) for pi in p)
        N_n = mp.e ** S_n
        toy_checks[str(n)] = {
            "entropy": str(S_n),
            "effective_rank": str(N_n),
            "difference_from_bin_count": str(N_n - n),
        }

    out = {
        "symbolic_entropy": str(sp.simplify(S_sym)),
        "symbolic_entropy_minus_ln_Delta": str(sp.simplify(S_sym - sp.log(Delta_sym))),
        "symbolic_N_eff": str(N_eff_sym),
        "symbolic_N_eff_minus_Delta": str(sp.simplify(N_eff_sym - Delta_sym)),
        "symbolic_f_eff": str(f_eff_sym),
        "symbolic_P_k": str(P_k_sym),
        "x": str(x),
        "gamma": str(gamma),
        "Delta": str(Delta),
        "entropy_numeric": str(S_mp),
        "ln_Delta_numeric": str(mp.log(Delta_mp)),
        "entropy_minus_ln_Delta_numeric": str(S_mp - mp.log(Delta_mp)),
        "N_eff_numeric": str(N_eff_mp),
        "N_eff_minus_Delta_numeric": str(N_eff_mp - Delta_mp),
        "f_eff_numeric": str(f_eff_mp),
        "P_k_numeric": str(P_k_mp),
        "uniform_density": str(rho_mp),
        "toy_uniform_spectrum_checks": toy_checks,
    }

    out_path = Path(__file__).resolve().parents[1] / "results" / "paper18_neff_delta_theorem_checks.json"
    out_path.write_text(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()

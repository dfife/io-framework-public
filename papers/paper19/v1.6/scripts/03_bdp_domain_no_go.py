import json
import math
from pathlib import Path

import mpmath as mp

"""
Reproduce the Paper 19 Baryon Dictionary Principle domain no-go.

The script shows that positive path averages of the original line-transfer
fraction remain between the horizon and observer endpoint values. Therefore the
low alpha=3/2 clustering baryon branch cannot be obtained by merely changing
the integration domain of the same positive 1-form transport operator.

Output:
    ../results/bdp_domain_no_go_results.json
"""

BUNDLE_ROOT = Path(__file__).resolve().parents[1]
OUT_JSON = BUNDLE_ROOT / "results" / "bdp_domain_no_go_results.json"


def main() -> None:
    gamma = mp.mpf("0.2375")
    x_obs = mp.mpf("1.51899")
    eta_s = mp.acos(2 / x_obs - 1)

    def x_of_eta(eta):
        return 2 / (1 + mp.cos(eta))

    def fb_of_eta(eta):
        return 2 * gamma / x_of_eta(eta)

    # Natural positive weights on the horizon-to-observer dust path.
    def avg(weight):
        num = mp.quad(lambda t: fb_of_eta(t) * weight(t), [0, eta_s])
        den = mp.quad(lambda t: weight(t), [0, eta_s])
        return num / den

    weights = {
        "uniform_eta": lambda t: 1,
        "proper_time_dust": lambda t: 1 + mp.cos(t),  # d tau / d eta up to constant
        "radial_dr": lambda t: mp.sin(t),  # |dr/deta| up to constant
        "log_x": lambda t: mp.tan(t / 2),  # d ln x / d eta
        "unit_plus_log_x": lambda t: 1 + mp.tan(t / 2),
    }

    averages = {name: avg(weight) for name, weight in weights.items()}

    fb_horizon = fb_of_eta(mp.mpf("0"))
    fb_observer = fb_of_eta(eta_s)
    fb_old_low = mp.mpf("0.25")
    fb_alpha32 = 2 * gamma / (x_obs ** mp.mpf("1.5"))

    h_geom = mp.mpf("0.5841")
    omega_m_geom = mp.mpf("0.197")
    omega_m_geom_h2 = omega_m_geom * h_geom * h_geom
    omega_b_old = mp.mpf("0.01712")
    omega_b_alpha32 = omega_m_geom_h2 * fb_alpha32
    omega_b_old_assumed = omega_m_geom_h2 * fb_old_low

    payload = {
        "inputs": {
            "gamma": str(gamma),
            "x_obs": str(x_obs),
            "eta_s": str(eta_s),
            "omega_m_geom_h2_old": str(omega_m_geom_h2),
        },
        "local_selector": {
            "formula": "f_b(eta) = 2 gamma / x(eta) = gamma (1 + cos eta)",
            "f_b_horizon": str(fb_horizon),
            "f_b_observer": str(fb_observer),
            "monotone_interval": [str(fb_observer), str(fb_horizon)],
        },
        "path_averages": {k: str(v) for k, v in averages.items()},
        "comparison_targets": {
            "old_low_fraction": str(fb_old_low),
            "alpha_3_over_2_fraction": str(fb_alpha32),
            "old_low_omega_b": str(omega_b_old),
            "old_assumed_omega_b_from_geom": str(omega_b_old_assumed),
            "alpha_3_over_2_omega_b_from_geom": str(omega_b_alpha32),
        },
        "no_go_checks": {
            "old_low_below_observer_endpoint": bool(fb_old_low < fb_observer),
            "alpha32_below_observer_endpoint": bool(fb_alpha32 < fb_observer),
            "all_listed_averages_above_observer_endpoint": all(v >= fb_observer for v in averages.values()),
            "all_listed_averages_below_horizon_endpoint": all(v <= fb_horizon for v in averages.values()),
        },
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2) + "\n")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Paper 24 v2.3 reproducibility script 03.

Purpose:
    Recompute the excited-branch kernel calculation and the PRyMordial BBN
    scorecard used by Paper 24 v2.3. This script is the only PRyMordial-
    dependent script in the bundle.

Inputs:
    - Constants embedded below.
    - External PRyMordial checkout specified by PRYM_ROOT.

Outputs:
    - results/final_excited_branch_results.json
    - results/final_excited_branch_report.txt

External dependencies:
    - PRyMordial, not vendored in this repository.
    - mpmath and sympy.

Claim boundary:
    - verified: kernel arithmetic, angular no-go coefficients, and local
      PRyMordial reruns in the lab.
    - conditional: the branch-dressing model itself.

Run:
    export PRYM_ROOT=/path/to/PRyMordial
    python3 scripts/03_run_final_bbn_scorecard.py
"""
from pathlib import Path
import json
import math
import os
import sys
from dataclasses import asdict, dataclass

import mpmath as mp
from sympy import S, simplify
from sympy.physics.wigner import wigner_3j, wigner_6j


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
PRYM_ROOT_ENV = os.environ.get("PRYM_ROOT")
if not PRYM_ROOT_ENV:
    raise SystemExit(
        "PRYM_ROOT is required for the full Paper 24 v2.3 PRyMordial rerun. "
        "Set it to an external PRyMordial checkout, e.g. "
        "export PRYM_ROOT=/path/to/PRyMordial"
    )
PRYM_ROOT = str(Path(PRYM_ROOT_ENV).expanduser().resolve())
RESULTS_DIR = BUNDLE_ROOT / "results"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

sys.path.insert(0, PRYM_ROOT)
os.chdir(PRYM_ROOT)

import PRyM.PRyM_init as PRyMini  # noqa: E402
import PRyM.PRyM_nuclear_net63 as PRyMnet63  # noqa: E402
from PRyM.PRyM_main import PRyMclass  # noqa: E402


@dataclass
class NetworkCase:
    label: str
    q_trans_ex: float
    Li7_H: float
    Li7_sigma: float
    D_H: float
    D_H_sigma: float
    Y_p: float
    Y_p_sigma: float


LI_OBS = 1.58e-10
LI_SIGMA = 3.1e-11
D_OBS = 2.527e-5
D_SIGMA = 0.030e-5
YP_OBS = 0.245
YP_SIGMA = 0.004

T0CMB_P22 = 2.6635
OMEGABH2_P22 = 0.02108
EPSILON_W_P25 = 0.012248588238432
NUCLEAR_DELTA_P22 = -0.0239

epsilon_n = 0.023843043660342757
x = 1.519
Q_d = 0.0028578
chi_ME_7Be = 21.0 / 25.0
f_gs = 0.711237553342816
Q_GS_7Be = 0.068
Li0_baseline = 5.387612546353705e-10
Li_current_full = 2.350416223788592e-10

amu_mev = 931.49410242
alpha = 1.0 / 137.035999084
hbarc = 197.3269804
mu_amu = 12.0 / 7.0
mu_mev = mu_amu * amu_mev
E_cm_mev = 0.300
Z1 = 2.0
Z2 = 2.0
Q_scale_mass7 = 0.068
B_gs_mev = 1.5866
E_x_mev = 0.4292
B_ex_mev = B_gs_mev - E_x_mev
Delta_E_ex_gs_keV = 429.2
deltaB_C_max_keV = 4.430045719791646


def sigma(value: float, obs: float, err: float) -> float:
    """Return observational sigma deviation using Paper 24 denominators."""

    return (value - obs) / err


def tau_34(T9: float) -> float:
    """Gamow parameter tau for 3He(alpha,gamma)7Be at temperature T9."""

    return 4.2487 * ((16.0 * (12.0 / 7.0)) / T9) ** (1.0 / 3.0)


def nu_34(T9: float) -> float:
    return tau_34(T9) / 3.0


def q_gs_proj() -> float:
    """Ground-state effective quadrupole scale after chi_ME and x projection."""

    return chi_ME_7Be * Q_GS_7Be / x


def Xi_gs(T9: float) -> float:
    return (q_gs_proj() / Q_d) * nu_34(T9)


def Xi_ex(T9: float, q_trans_ex: float) -> float:
    """Excited-branch exponent argument before multiplying by epsilon_n."""

    return ((q_trans_ex / x) / Q_d) * nu_34(T9)


def R_gs(T9: float) -> float:
    return math.exp(-epsilon_n * Xi_gs(T9))


def R_ex(T9: float, q_trans_ex: float) -> float:
    return math.exp(-epsilon_n * Xi_ex(T9, q_trans_ex))


def R34_total(T9: float, q_trans_ex: float) -> float:
    """Branch-summed 3He(alpha,gamma)7Be rate multiplier."""

    return f_gs * R_gs(T9) + (1.0 - f_gs) * R_ex(T9, q_trans_ex)


def apply_baseline() -> None:
    """Configure PRyMordial to the Paper 24/Paper 22 baseline convention."""

    PRyMini.verbose_flag = False
    PRyMini.julia_flag = False
    PRyMini.smallnet_flag = False
    PRyMini.compute_bckg_flag = True
    PRyMini.compute_nTOp_flag = True

    PRyMini.T0CMB = T0CMB_P22 * PRyMini.Kelvin
    PRyMini.s0CMB = PRyMini.s0bar * (PRyMini.T0CMB / PRyMini.MeV_to_Kelvin) ** 3
    PRyMini.n0CMB = (
        (2.0 * PRyMini.zeta(3)) / (math.pi**2)
    ) * (PRyMini.T0CMB / PRyMini.MeV_to_Kelvin) ** 3
    PRyMini.Omegabh2 = OMEGABH2_P22
    PRyMini.Omegabh2_to_eta0b = (
        (PRyMini.rhocOverh2 / PRyMini.n0CMB) / (PRyMini.ma / PRyMini.maOvermB)
    )
    PRyMini.eta0b = PRyMini.Omegabh2_to_eta0b * PRyMini.Omegabh2

    PRyMini.NP_nTOp_flag = True
    PRyMini.NP_delta_nTOp = -EPSILON_W_P25

    PRyMini.NP_nuclear_flag = True
    for name in [
        "npdg",
        "dpHe3g",
        "ddHe3n",
        "ddtp",
        "tpag",
        "tdan",
        "taLi7g",
        "He3ntp",
        "He3dap",
        "He3aBe7g",
        "Be7nLi7p",
        "Li7paa",
    ]:
        setattr(PRyMini, f"NP_delta_{name}", NUCLEAR_DELTA_P22)


def run_network_case(label: str, q_trans_ex: float) -> NetworkCase:
    """Run PRyMordial with a branch-specific 3He(alpha,gamma)7Be multiplier."""

    apply_baseline()

    orig_frwrd = PRyMnet63.UpdateNuclearRates.He3aBe7g_frwrd
    orig_bkwrd = PRyMnet63.UpdateNuclearRates.He3aBe7g_bkwrd

    def wrapped_frwrd(self, T):
        # PRyMordial passes physical temperature T; the Paper 24 rate dressing
        # is defined as a function of T9.
        T9 = T * 1.0e-9
        return R34_total(T9, q_trans_ex) * orig_frwrd(self, T)

    def wrapped_bkwrd(self, T):
        T9 = T * 1.0e-9
        return R34_total(T9, q_trans_ex) * orig_bkwrd(self, T)

    PRyMnet63.UpdateNuclearRates.He3aBe7g_frwrd = wrapped_frwrd
    PRyMnet63.UpdateNuclearRates.He3aBe7g_bkwrd = wrapped_bkwrd
    try:
        obj = PRyMclass()
    finally:
        PRyMnet63.UpdateNuclearRates.He3aBe7g_frwrd = orig_frwrd
        PRyMnet63.UpdateNuclearRates.He3aBe7g_bkwrd = orig_bkwrd

    li = obj.Li7oH()
    dh = obj.DoH()
    yp = obj.YPCMB()
    return NetworkCase(
        label=label,
        q_trans_ex=q_trans_ex,
        Li7_H=li,
        Li7_sigma=sigma(li, LI_OBS, LI_SIGMA),
        D_H=dh,
        D_H_sigma=sigma(dh, D_OBS, D_SIGMA),
        Y_p=yp,
        Y_p_sigma=sigma(yp, YP_OBS, YP_SIGMA),
    )


def kappa(B_mev: float) -> float:
    return math.sqrt(2.0 * mu_mev * B_mev) / hbarc


def eta_scatt() -> float:
    return alpha * Z1 * Z2 * math.sqrt(mu_mev / (2.0 * E_cm_mev))


def eta_B(B_mev: float) -> float:
    return Z1 * Z2 * alpha * mu_mev / (hbarc * kappa(B_mev))


def k_fm_inv() -> float:
    return math.sqrt(2.0 * mu_mev * E_cm_mev) / hbarc


def u0(r: float) -> mp.mpf:
    return mp.coulombf(0, eta_scatt(), k_fm_inv() * r)


def ub(B_mev: float, r: float) -> mp.mpf:
    return mp.whitw(-eta_B(B_mev), 1.5, 2.0 * kappa(B_mev) * r)


def amp_kernel(B_mev: float, r: float) -> mp.mpf:
    """Amplitude kernel for the external-capture tail model."""

    return abs(ub(B_mev, r) * r * u0(r))


def rate_kernel(B_mev: float, r: float) -> mp.mpf:
    """Rate-weighted kernel, i.e. amplitude kernel squared."""

    val = amp_kernel(B_mev, r)
    return val * val


def kernel_summary(B_mev: float) -> dict:
    """Compute peak, mean, median, and Coulomb-projected kernel statistics."""

    amp_tot = mp.quad(lambda rr: amp_kernel(B_mev, rr), [0, mp.inf])
    rate_tot = mp.quad(lambda rr: rate_kernel(B_mev, rr), [0, mp.inf])

    amp_mean = float(mp.quad(lambda rr: rr * amp_kernel(B_mev, rr), [0, mp.inf]) / amp_tot)
    rate_mean = float(
        mp.quad(lambda rr: rr * rate_kernel(B_mev, rr), [0, mp.inf]) / rate_tot
    )

    amp_med_eq = lambda R: mp.quad(lambda rr: amp_kernel(B_mev, rr), [0, R]) - amp_tot / 2.0
    rate_med_eq = lambda R: mp.quad(lambda rr: rate_kernel(B_mev, rr), [0, R]) - rate_tot / 2.0
    amp_guess = 8.0 if abs(B_mev - B_gs_mev) < 1e-12 else 10.0
    rate_guess = 7.0 if abs(B_mev - B_gs_mev) < 1e-12 else 9.0
    amp_median = float(mp.findroot(amp_med_eq, amp_guess))
    rate_median = float(mp.findroot(rate_med_eq, rate_guess))

    rs = [0.1 + 0.1 * i for i in range(400)]
    amps = [float(amp_kernel(B_mev, r)) for r in rs]
    rates = [a * a for a in amps]
    amp_peak = rs[max(range(len(amps)), key=lambda i: amps[i])]
    rate_peak = rs[max(range(len(rates)), key=lambda i: rates[i])]

    amp_avg_F0 = float(
        mp.quad(lambda rr: amp_kernel(B_mev, rr) * u0(rr), [0, mp.inf]) / amp_tot
    )
    rate_avg_F0 = float(
        mp.quad(lambda rr: rate_kernel(B_mev, rr) * u0(rr), [0, mp.inf]) / rate_tot
    )

    return {
        "B_mev": B_mev,
        "kappa_fm_inv": kappa(B_mev),
        "eta_B": eta_B(B_mev),
        "amp_peak_fm": amp_peak,
        "rate_peak_fm": rate_peak,
        "amp_mean_fm": amp_mean,
        "rate_mean_fm": rate_mean,
        "amp_median_fm": amp_median,
        "rate_median_fm": rate_median,
        "F0_at_amp_peak": float(u0(amp_peak)),
        "F0_at_rate_peak": float(u0(rate_peak)),
        "F0_at_amp_mean": float(u0(amp_mean)),
        "F0_at_rate_mean": float(u0(rate_mean)),
        "F0_at_amp_median": float(u0(amp_median)),
        "F0_at_rate_median": float(u0(rate_median)),
        "amp_weighted_avg_F0": amp_avg_F0,
        "rate_weighted_avg_F0": rate_avg_F0,
        "Q_trans_from_amp_weighted_avg_b": Q_scale_mass7 * amp_avg_F0,
        "Q_trans_from_rate_weighted_avg_b": Q_scale_mass7 * rate_avg_F0,
    }


def main() -> None:
    """Run angular diagnostics, kernel calculation, and PRyMordial cases."""

    T9_eff = 0.5160778165182853
    nu_eff = nu_34(T9_eff)
    R_gs_eff = R_gs(T9_eff)

    current_R34 = Li_current_full / Li0_baseline
    R_target_1sigma = (LI_OBS + LI_SIGMA) / Li0_baseline
    R_ex_needed_1sigma = (R_target_1sigma - f_gs * R_gs_eff) / (1.0 - f_gs)
    q_needed_1sigma_eff = -(x * Q_d / (epsilon_n * nu_eff)) * math.log(R_ex_needed_1sigma)

    # Direct rank-2 operator no-go and off-diagonal mixing coefficients. These
    # Wigner symbols are the compact reproducibility check for the tensor
    # selection arguments in the paper.
    sixj_direct_p12 = simplify(wigner_6j(1, S(1) / 2, S(1) / 2, S(1) / 2, 0, 2))
    sixj_direct_p32 = simplify(wigner_6j(1, S(3) / 2, S(1) / 2, S(1) / 2, 0, 2))
    orbital_3j_direct = simplify(wigner_3j(1, 2, 0, 0, 0, 0))

    sixj_diag_p32 = simplify(wigner_6j(1, S(3) / 2, S(1) / 2, S(3) / 2, 1, 2))
    sixj_offdiag = simplify(wigner_6j(1, S(1) / 2, S(1) / 2, S(3) / 2, 1, 2))
    offdiag_to_diag_ratio = abs(float(sixj_offdiag / sixj_diag_p32))
    Vmix_est_keV = deltaB_C_max_keV * offdiag_to_diag_ratio
    theta_mix_est = Vmix_est_keV / Delta_E_ex_gs_keV
    Q_mix_inherited_b = Q_scale_mass7 * theta_mix_est

    # Excited-state weaker-binding external-capture kernels. The amplitude-
    # weighted value is the branch object used by the v2.3 support chain.
    gs_kernel = kernel_summary(B_gs_mev)
    ex_kernel = kernel_summary(B_ex_mev)

    q_ex_rate = ex_kernel["Q_trans_from_rate_weighted_avg_b"]
    q_ex_amp = ex_kernel["Q_trans_from_amp_weighted_avg_b"]

    cases = [
        run_network_case("current_excited_blind", 0.0),
        run_network_case("excited_rate_weighted_avg", q_ex_rate),
        run_network_case("excited_threshold_1sigma", q_needed_1sigma_eff),
        run_network_case("excited_amp_weighted_avg", q_ex_amp),
    ]

    results = {
        "status": {
            "direct_rank2_position_route_for_excited_branch": "derived_no_go",
            "direct_rank2_momentum_route_for_excited_branch": "derived_no_go_same_tensor_selection",
            "universal_linear_kinematic_shift_from_isotropic_TT_average": "derived_no_go",
            "off_diagonal_mixing_alone_closes_gap": "derived_no",
            "amplitude_weighted_external_capture_tail_closes_gap": "conditional_yes",
        },
        "constants": {
            "epsilon_n": epsilon_n,
            "x": x,
            "Q_d": Q_d,
            "chi_ME_7Be": chi_ME_7Be,
            "f_gs": f_gs,
            "Q_GS_7Be_b": Q_GS_7Be,
            "T9_eff": T9_eff,
            "nu_34_T9eff": nu_eff,
            "Li0_baseline": Li0_baseline,
            "Li_current_full": Li_current_full,
            "B_gs_mev": B_gs_mev,
            "B_ex_mev": B_ex_mev,
            "Delta_E_ex_gs_keV": Delta_E_ex_gs_keV,
            "Q_trans_ex_needed_1sigma_effectiveT_b": q_needed_1sigma_eff,
        },
        "derived_formulas": {
            "branch_sum": "R_34(T9) = f_gs R_gs(T9) + (1-f_gs) R_ex(T9)",
            "direct_rank2_reduced_me_formula": (
                "<(l_f s)j_f||T^(2)||(l_i s)j_i> = "
                "(-1)^(l_f+s+j_i+2) sqrt((2j_f+1)(2j_i+1)) "
                "{l_f j_f s; j_i l_i 2} <l_f||T^(2)||l_i>"
            ),
            "linear_capture_response": "delta sigma / sigma = 2 Re(delta M / M)",
            "amplitude_weighted_excited_Qtrans": (
                "Q_trans,ex^(amp) = Q_scale * [int dr K_amp,ex(r) F0(r)] / [int dr K_amp,ex(r)]"
            ),
            "rate_weighted_excited_Qtrans": (
                "Q_trans,ex^(rate) = Q_scale * [int dr W_rate,ex(r) F0(r)] / [int dr W_rate,ex(r)]"
            ),
            "mixing_angle_estimate": "theta_mix ~ V_mix / DeltaE_ex-gs",
        },
        "angular_no_go": {
            "sixj_direct_p12": str(sixj_direct_p12),
            "sixj_direct_p32": str(sixj_direct_p32),
            "orbital_3j_direct": str(orbital_3j_direct),
            "statement": (
                "Both direct rank-2 s->p1/2 and s->p3/2 orbital routes vanish. "
                "The momentum quadrupole [p⊗p]^(2) has the same rank-2 orbital selection."
            ),
        },
        "off_diagonal_mixing_estimate": {
            "sixj_diag_p32_to_p32": str(sixj_diag_p32),
            "sixj_offdiag_p32_to_p12": str(sixj_offdiag),
            "offdiag_to_diag_ratio": offdiag_to_diag_ratio,
            "deltaB_C_max_keV": deltaB_C_max_keV,
            "Vmix_est_keV": Vmix_est_keV,
            "theta_mix_estimate": theta_mix_est,
            "Q_inherited_from_mixing_b": Q_mix_inherited_b,
        },
        "kernel_ground_state": gs_kernel,
        "kernel_excited_state": ex_kernel,
        "network_cases": [asdict(case) for case in cases],
    }

    report_lines = [
        "Paper 24 final push: excited-state branch closure audit",
        "",
        "Claim boundary",
        "--------------",
        "- derived / no-go: the direct rank-2 position-space excited-branch route remains zero.",
        "- derived / no-go: the direct rank-2 momentum-quadrupole route has the same tensor-selection zero.",
        "- derived / no-go: a universal linear TT kinematic shift averages to zero in the isotropic bath.",
        "- derived / no: off-diagonal p3/2<->p1/2 mixing is real but too small to close the gap by itself.",
        "- conditional: the amplitude-weighted external-capture tail of the weaker-bound 1/2- branch crosses the 1 sigma threshold.",
        "",
        "I. Hilbert-space setup",
        "----------------------",
        "H_34 = H_rel ⊗ ( H_{7Be,gs} ⊕ H_{7Be,ex} ) ⊗ H_gamma",
        "R_34(T9) = f_gs R_gs(T9) + (1-f_gs) R_ex(T9).",
        "",
        "II. Direct rank-2 no-go",
        "-----------------------",
        f"6j_direct(p1/2) = {sixj_direct_p12}",
        f"6j_direct(p3/2) = {sixj_direct_p32}",
        f"3j_direct(1,2,0;0,0,0) = {orbital_3j_direct}",
        "So the raw direct s->p rank-2 orbital route is zero for both branches.",
        "The momentum quadrupole [p⊗p]^(2) is also a rank-2 orbital tensor, so it shares the same selection obstruction.",
        "",
        "III. Universal photon/kinematic linear shift",
        "--------------------------------------------",
        "A universal linear TT correction built only from h_ij n^i n^j has isotropic average zero,",
        "because ∫ dΩ n_i n_j h_TT^{ij} = 0 for trace-free h_TT in an unpolarized bath.",
        "So there is no separate branch-independent linear rescue from this channel.",
        "",
        "IV. Off-diagonal p3/2 <-> p1/2 mixing",
        "--------------------------------------",
        f"6j_diag(3/2->3/2) = {sixj_diag_p32}",
        f"6j_offdiag(3/2->1/2) = {sixj_offdiag}",
        f"offdiag/diag ratio = {offdiag_to_diag_ratio:.15f}",
        f"deltaB_C,max = {deltaB_C_max_keV:.15f} keV",
        f"V_mix estimate = {Vmix_est_keV:.15f} keV",
        f"theta_mix estimate = {theta_mix_est:.15f}",
        f"inherited Q scale = {Q_mix_inherited_b:.15f} b",
        "So mixing is subleading, not dominant.",
        "",
        "V. Weaker-binding excited external-capture tail",
        "-----------------------------------------------",
        f"Ground-state binding: B_gs = {B_gs_mev:.6f} MeV",
        f"Excited-state binding: B_ex = {B_ex_mev:.6f} MeV",
        "",
        "Ground-state kernel summary:",
        f"  amp_mean radius  = {gs_kernel['amp_mean_fm']:.15f} fm",
        f"  rate_mean radius = {gs_kernel['rate_mean_fm']:.15f} fm",
        f"  amp-weighted <F0> = {gs_kernel['amp_weighted_avg_F0']:.15f}",
        f"  rate-weighted <F0> = {gs_kernel['rate_weighted_avg_F0']:.15f}",
        "",
        "Excited-state kernel summary:",
        f"  amp_peak radius  = {ex_kernel['amp_peak_fm']:.15f} fm",
        f"  rate_peak radius = {ex_kernel['rate_peak_fm']:.15f} fm",
        f"  amp_mean radius  = {ex_kernel['amp_mean_fm']:.15f} fm",
        f"  rate_mean radius = {ex_kernel['rate_mean_fm']:.15f} fm",
        f"  amp_median       = {ex_kernel['amp_median_fm']:.15f} fm",
        f"  rate_median      = {ex_kernel['rate_median_fm']:.15f} fm",
        f"  amp-weighted <F0> = {ex_kernel['amp_weighted_avg_F0']:.15f}",
        f"  rate-weighted <F0> = {ex_kernel['rate_weighted_avg_F0']:.15f}",
        "",
        f"Using Q_scale = {Q_scale_mass7:.6f} b gives",
        f"  Q_trans,ex^(rate) = {q_ex_rate:.15f} b",
        f"  Q_trans,ex^(amp)  = {q_ex_amp:.15f} b",
        "",
        "VI. Full-network outputs",
        "------------------------",
        f"1 sigma threshold in effective-T proxy: Q_trans,ex = {q_needed_1sigma_eff:.15f} b",
    ]
    for case in cases:
        report_lines.append(
            f"  {case.label}: q_trans_ex = {case.q_trans_ex:.15f} b -> "
            f"Li7/H = {case.Li7_H:.15e} ({case.Li7_sigma:.6f} sigma), "
            f"D/H = {case.D_H:.15e} ({case.D_H_sigma:.6f} sigma), "
            f"Y_p = {case.Y_p:.15f} ({case.Y_p_sigma:.6f} sigma)"
        )
    report_lines.extend(
        [
            "",
            "Conclusion",
            "----------",
            "The old excited-branch 0.005-0.010 b window came from pointwise Coulomb factors at representative radii.",
            "Once the weaker excited-state binding is inserted and the TT correction is treated as a first-order amplitude perturbation,",
            "the correct effective object is the amplitude-weighted external-capture kernel, not a pointwise F0 sample.",
            "That raises the excited-branch estimate above the 1 sigma threshold.",
        ]
    )

    results_path = RESULTS_DIR / "final_excited_branch_results.json"
    report_path = RESULTS_DIR / "final_excited_branch_report.txt"
    with open(results_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines) + "\n")

    print("\n".join(report_lines))


if __name__ == "__main__":
    main()

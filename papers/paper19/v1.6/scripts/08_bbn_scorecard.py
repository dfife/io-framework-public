import importlib
import json
import math
import os
import re
import sys
import types
from pathlib import Path

from camb.bbn import BBN_table_interpolator

"""
Reproduce the Paper 19 v1.6 BBN scorecard with the corrected YPCMB wrapper.

PRyMordial is an external dependency and is not redistributed here. Set
``PRYM_ROOT`` to a local PRyMordial checkout before running this script. The
bundle includes the frozen JSON produced in the private lab, and script 11 can
validate the quoted values without PRyMordial.

The BBN branch intentionally uses the interior BBN temperature scale ``T_IO`` in
the omega_b-to-eta conversion. That is not the observer-side R4/CMB readout.

Output:
    ../results/bbn_scorecard_results.json
"""

import os

BUNDLE_ROOT = Path(__file__).resolve().parents[1]
OUT = BUNDLE_ROOT / "results" / "bbn_scorecard_results.json"
PRYM_ROOT = Path(os.environ.get("PRYM_ROOT", ""))
if not PRYM_ROOT:
    raise RuntimeError("Set PRYM_ROOT to an external PRyMordial checkout before running this script.")
if str(PRYM_ROOT) not in sys.path:
    sys.path.insert(0, str(PRYM_ROOT))


T_IO = 2.6635
T_CMB_STD = 2.7255
N_EFF_SM = 3.044
DELTA = 5.624068750943682
DELTA_NEFF_HIGH = DELTA - N_EFF_SM

# Paper 19 self-consistent background recomputation: early-time BBN branch remains alpha = 1.
OMEGA_B_IO_EXACT = 0.02102461376506758
OMEGA_B_IO_ROUNDED = 0.02108

# Paper 19 v1.4 Path C: inherit the modern post-Paper-22-v1.1 amplitude framework.
GAMMA_BI = 0.2375
K_GAUGE = math.log(1.0 + GAMMA_BI * GAMMA_BI)
K_MEAN = 1.72704
L1 = 0.22416889162576648
L2 = 0.13805247907094412
EPSILON_W_MODERN = K_GAUGE * L1
EPSILON_N_MODERN = (K_MEAN / 10.0) * L2

PAPER18_QUOTED = {
    "D/H": 2.49e-5,
    "Y_p": 0.2471,
    "Li7/H": 4.8e-10,
}

OBSERVED_CONVENTIONS_V1 = {
    "source": "IO Framework Observational Conventions v1.0",
    "url": "https://dfife.github.io/data/observational_conventions_v1.md",
    "D/H": {"value": 2.527e-5, "sigma": 0.030e-5},
    "Y_p": {"value": 0.245, "sigma": 0.004},
    "Li7/H": {"value": 1.58e-10, "sigma": 0.31e-10},
}


def omega_std_equiv(omega_io: float) -> float:
    return omega_io * (T_IO / T_CMB_STD) ** (-3)


def clear_prym_modules() -> None:
    for key in list(sys.modules):
        if key.startswith("PRyM"):
            del sys.modules[key]


def nuclear_delta_names() -> list[str]:
    init_text = (PRYM_ROOT / "PRyM" / "PRyM_init.py").read_text(encoding="utf-8")
    match = re.search(
        r"^(NP_delta_[^=]+)= np\.zeros\(num_reactions\)",
        init_text,
        flags=re.MULTILINE,
    )
    if not match:
        raise RuntimeError("Could not recover PRyM nuclear delta names")
    return [name.strip() for name in match.group(1).split(",")]


def configure_prym(omega_io: float, delta_neff: float, smallnet: bool):
    os.chdir(PRYM_ROOT)
    clear_prym_modules()
    import PRyM.PRyM_init as PRyMini

    PRyMini.aTid_flag = True
    PRyMini.compute_bckg_flag = True
    PRyMini.compute_nTOp_flag = True
    PRyMini.compute_nTOp_thermal_flag = False
    PRyMini.save_bckg_flag = False
    PRyMini.save_nTOp_flag = False
    PRyMini.save_nTOp_thermal_flag = False
    PRyMini.verbose_flag = False
    PRyMini.smallnet_flag = smallnet
    PRyMini.julia_flag = False
    PRyMini.NP_nuclear_flag = False
    PRyMini.NP_nTOp_flag = False

    # IO BBN branch: omega_b -> eta uses T_IO, not the external 2.7255 K standard mapping.
    PRyMini.T0CMB = T_IO * PRyMini.Kelvin
    PRyMini.s0CMB = PRyMini.s0bar * (PRyMini.T0CMB / PRyMini.MeV_to_Kelvin) ** 3
    PRyMini.n0CMB = (2.0 * PRyMini.zeta(3)) / (math.pi**2) * (
        PRyMini.T0CMB / PRyMini.MeV_to_Kelvin
    ) ** 3
    PRyMini.Omegabh2_to_eta0b = (PRyMini.rhocOverh2 / PRyMini.n0CMB) / (
        PRyMini.ma / PRyMini.maOvermB
    )
    PRyMini.Omegabh2 = omega_io
    PRyMini.eta0b = PRyMini.Omegabh2_to_eta0b * PRyMini.Omegabh2
    PRyMini.DeltaNeff = delta_neff

    return PRyMini


def install_prym_main(weak_rate_multiplier: float):
    path = PRYM_ROOT / "PRyM" / "PRyM_main.py"
    source = path.read_text(encoding="utf-8")
    source = source.replace(
        "import time\nimport numpy as np",
        "import time\nimport math\nimport numpy as np",
    )
    for tag in ["HT", "MT", "LT"]:
        source = source.replace(
            f"return NormWeakRates*nTOp_frwrd_{tag}(T)",
            f"return NormWeakRates*nTOp_frwrd_{tag}(T)*({weak_rate_multiplier})",
        )
        source = source.replace(
            f"return NormWeakRates*nTOp_bkwrd_{tag}(T)",
            f"return NormWeakRates*nTOp_bkwrd_{tag}(T)*({weak_rate_multiplier})",
        )

    mod = types.ModuleType("PRyM.PRyM_main")
    mod.__file__ = str(path)
    mod.__package__ = "PRyM"
    sys.modules["PRyM.PRyM_main"] = mod
    exec(compile(source, str(path), "exec"), mod.__dict__)
    return mod


def run_prym(
    omega_io: float,
    delta_neff: float,
    smallnet: bool,
    weak_delta: float = 0.0,
    nuclear_common_delta: float = 0.0,
) -> dict:
    PRyMini = configure_prym(omega_io, delta_neff, smallnet)

    nuclear_names = nuclear_delta_names()
    for name in nuclear_names:
        setattr(PRyMini, name, 0.0)
    if abs(nuclear_common_delta) > 0.0:
        PRyMini.NP_nuclear_flag = True
        for name in nuclear_names:
            setattr(PRyMini, name, nuclear_common_delta)

    PRyMmain = install_prym_main(1.0 + weak_delta)
    res = PRyMmain.PRyMclass().PRyMresults()
    y_p_cmb = float(res[3])
    y_p_bbn = float(res[4])
    return {
        "Neff_output": float(res[0]),
        "Y_p": y_p_cmb,
        "Y_p_output_component": "YPCMB / PRyMresults()[3]",
        "Y_p_CMB": y_p_cmb,
        "Y_p_BBN": y_p_bbn,
        "D/H": float(res[5]) * 1.0e-5,
        "He3/H": float(res[6]) * 1.0e-5,
        "Li7/H": float(res[7]) * 1.0e-10,
        "eta10": float(PRyMini.eta0b * 1.0e10),
        "weak_delta": float(weak_delta),
        "nuclear_common_delta": float(nuclear_common_delta),
        "amplitude_framework": (
            "Path C modern Paper22/Paper24 alignment"
            if weak_delta or nuclear_common_delta
            else "original Paper19 no-amplitude-dressing branch"
        ),
    }


def sigma_offset(value: float, obs: dict) -> float:
    return (value - obs["value"]) / obs["sigma"]


def rel_shift(new: float, old: float) -> float:
    return (new - old) / old


def main() -> None:
    prym_large_original_exact = run_prym(OMEGA_B_IO_EXACT, 0.0, smallnet=False)
    prym_large_exact = run_prym(
        OMEGA_B_IO_EXACT,
        0.0,
        smallnet=False,
        weak_delta=-EPSILON_W_MODERN,
        nuclear_common_delta=-EPSILON_N_MODERN,
    )
    prym_small_exact = run_prym(
        OMEGA_B_IO_EXACT,
        0.0,
        smallnet=True,
        weak_delta=-EPSILON_W_MODERN,
        nuclear_common_delta=-EPSILON_N_MODERN,
    )
    prym_large_rounded = run_prym(
        OMEGA_B_IO_ROUNDED,
        0.0,
        smallnet=False,
        weak_delta=-EPSILON_W_MODERN,
        nuclear_common_delta=-EPSILON_N_MODERN,
    )
    prym_large_counterfactual_high = run_prym(
        OMEGA_B_IO_EXACT,
        DELTA_NEFF_HIGH,
        smallnet=False,
        weak_delta=-EPSILON_W_MODERN,
        nuclear_common_delta=-EPSILON_N_MODERN,
    )

    pred = BBN_table_interpolator()
    omega_std = omega_std_equiv(OMEGA_B_IO_EXACT)
    camb_crosscheck = {
        "omega_b_std_equiv": omega_std,
        "Y_p_BBN": float(pred.Y_p(omega_std, 0.0)),
        "D/H": float(pred.DH(omega_std, 0.0)),
    }
    camb_counterfactual_high = {
        "omega_b_std_equiv": omega_std,
        "Y_p_BBN": float(pred.Y_p(omega_std, DELTA_NEFF_HIGH)),
        "D/H": float(pred.DH(omega_std, DELTA_NEFF_HIGH)),
    }

    comparisons = {
        "vs_paper18_quoted": {
            "D/H_relative_shift": rel_shift(prym_large_exact["D/H"], PAPER18_QUOTED["D/H"]),
            "Y_p_relative_shift": rel_shift(
                prym_large_exact["Y_p"], PAPER18_QUOTED["Y_p"]
            ),
            "Li7/H_relative_shift": rel_shift(
                prym_large_exact["Li7/H"], PAPER18_QUOTED["Li7/H"]
            ),
        },
        "vs_observed_conventions_v1_sigma": {
            "D/H_sigma": sigma_offset(prym_large_exact["D/H"], OBSERVED_CONVENTIONS_V1["D/H"]),
            "Y_p_sigma": sigma_offset(prym_large_exact["Y_p"], OBSERVED_CONVENTIONS_V1["Y_p"]),
            "Li7/H_sigma": sigma_offset(
                prym_large_exact["Li7/H"], OBSERVED_CONVENTIONS_V1["Li7/H"]
            ),
        },
    }

    payload = {
        "inputs": {
            "T_IO_K": T_IO,
            "T_CMB_standard_K": T_CMB_STD,
            "N_eff_SM_imported": N_EFF_SM,
            "Delta": DELTA,
            "DeltaNeff_counterfactual_high": DELTA_NEFF_HIGH,
            "omega_b_IO_exact_alpha1": OMEGA_B_IO_EXACT,
            "omega_b_IO_rounded_paper18": OMEGA_B_IO_ROUNDED,
            "omega_b_standard_equivalent": omega_std,
            "path_c_modern_amplitudes": {
                "GAMMA_BI": GAMMA_BI,
                "K_gauge": K_GAUGE,
                "K_mean": K_MEAN,
                "L1": L1,
                "L2": L2,
                "epsilon_w": EPSILON_W_MODERN,
                "epsilon_n": EPSILON_N_MODERN,
                "weak_delta": -EPSILON_W_MODERN,
                "nuclear_common_delta": -EPSILON_N_MODERN,
                "source": "Paper 22 v1.3 / Paper 24 v2.2 standard amplitude framework",
            },
            "note": "IO BBN branch uses T_IO in the omega_b -> eta conversion.",
        },
        "prymordial": {
            "large_network_exact": prym_large_exact,
            "large_network_original_paper19_exact_audit": prym_large_original_exact,
            "small_network_exact": prym_small_exact,
            "large_network_rounded": prym_large_rounded,
            "large_network_counterfactual_high_Neff": prym_large_counterfactual_high,
        },
        "camb_primat_crosscheck": {
            "standard_branch": camb_crosscheck,
            "counterfactual_high_Neff": camb_counterfactual_high,
        },
        "paper18_quoted": PAPER18_QUOTED,
        "observed_conventions_v1": OBSERVED_CONVENTIONS_V1,
        "comparisons": comparisons,
    }

    OUT.write_text(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()

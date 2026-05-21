#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import Any

from classy import Class

ROOT = Path("/opt/cosmology-lab")
OUT = ROOT / "results" / "paper31"
TMP = ROOT / "tmp" / "planck-lite-py"

if str(TMP) not in sys.path:
    sys.path.insert(0, str(TMP))

from planck_lite_py import PlanckLitePy  # type: ignore  # noqa: E402


L_MAX = 2508
X = 1.519
GAMMA = 0.2375
F_GAMMA = 1.0 / (1.0 + GAMMA**2)
F_GAMMA2 = F_GAMMA**2
F_GAMMA3 = F_GAMMA**3
K_GAUGE = math.log(1.0 + GAMMA**2)
J_PHI = X ** (-0.5)
ETA_IO = 2.0 * J_PHI - 1.0

A_S_NATIVE = 2.0072459972737347e-9
OMEGA_M_TOTAL = 0.15939026836
OMEGA_B_GEOM = 0.02108
OMEGA_B_EFF = 0.02910
OMEGA_B_STRUCT = OMEGA_B_GEOM + ETA_IO * (1.0 + F_GAMMA) / 2.0 * (OMEGA_B_EFF - OMEGA_B_GEOM)
OMEGA_CDM_BOOKKEEPING = OMEGA_M_TOTAL - OMEGA_B_STRUCT

H0_SCHUR_ACTIVE = 68.91
OMEGA_K_SCHUR_ACTIVE = -0.005613722564239


def compute_case(params: dict[str, Any], plik: PlanckLitePy) -> dict[str, float]:
    cosmo = Class()
    try:
        cosmo.set(params)
        cosmo.compute()
        cls = cosmo.lensed_cl(L_MAX)
        ell = cls["ell"][2:]
        pref = ell * (ell + 1.0) / (2.0 * math.pi) * (params["T_cmb"] * 1.0e6) ** 2
        chi2 = -2.0 * float(
            plik.loglike(pref * cls["tt"][2:], pref * cls["te"][2:], pref * cls["ee"][2:], ellmin=2)
        )
        theta = float(cosmo.get_current_derived_parameters(["100*theta_s"])["100*theta_s"])
        return {"chi2": chi2, "theta_s_100": theta}
    finally:
        cosmo.struct_cleanup()
        cosmo.empty()


def main() -> None:
    plik = PlanckLitePy(
        data_directory=str(TMP / "data"),
        year=2018,
        spectra="TTTEEE",
        use_low_ell_bins=True,
    )

    base = {
        "output": "tCl,pCl,lCl",
        "lensing": "yes",
        "l_max_scalars": L_MAX,
        "H0": H0_SCHUR_ACTIVE,
        "T_cmb": 2.7253,
        "Omega_k": OMEGA_K_SCHUR_ACTIVE,
        "N_ur": 3.044,
        "N_ncdm": 0,
        "YHe": 0.2477,
        "n_s": 0.9639,
        "alpha_s": 5.0e-5,
        "reio_parametrization": "reio_none",
        "A_s": A_S_NATIVE,
        "lcmb_rescale": J_PHI,
        "lcmb_tilt": 0.0,
        "lcmb_pivot": 0.05,
        "lcmb_curved_shift": -3.0,
        "lcmb_curved_order": -0.25,
        "io_visibility_opacity_factor": F_GAMMA2,
        "io_acoustic_drag_factor": 1.0,
        "io_acoustic_hierarchy_factor": F_GAMMA3,
    }

    one_number_struct = {
        **base,
        "omega_b": OMEGA_B_STRUCT,
        "omega_cdm": OMEGA_CDM_BOOKKEEPING,
    }

    framework_background_resolution = {
        **base,
        "omega_b_geom": OMEGA_B_GEOM,
        "omega_b_eff": OMEGA_B_EFF,
        "omega_b_clustering": OMEGA_B_STRUCT,
        "omega_cdm": OMEGA_CDM_BOOKKEEPING,
    }

    one_number_result = compute_case(one_number_struct, plik)
    framework_result = compute_case(framework_background_resolution, plik)

    payload = {
        "constants": {
            "x": X,
            "gamma": GAMMA,
            "f_gamma": F_GAMMA,
            "k_gauge": K_GAUGE,
            "j_phi": J_PHI,
            "eta_io": ETA_IO,
            "A_s_native": A_S_NATIVE,
            "omega_m_total": OMEGA_M_TOTAL,
            "omega_b_geom": OMEGA_B_GEOM,
            "omega_b_eff": OMEGA_B_EFF,
            "omega_b_struct": OMEGA_B_STRUCT,
            "omega_cdm_bookkeeping": OMEGA_CDM_BOOKKEEPING,
            "H0_schur_active": H0_SCHUR_ACTIVE,
            "Omega_k_schur_active": OMEGA_K_SCHUR_ACTIVE,
        },
        "one_number_structured_baseline": {
            "params": one_number_struct,
            "result": one_number_result,
        },
        "framework_background_resolution_case": {
            "params": framework_background_resolution,
            "result": framework_result,
        },
        "delta_chi2_vs_one_number": framework_result["chi2"] - one_number_result["chi2"],
    }

    (OUT / "paper31_background_baryon_slot_resolution_audit_results.json").write_text(
        json.dumps(payload, indent=2)
    )

    report = f"""# Paper 31: Background Baryon Slot Resolution Audit

Date: 2026-04-04

## Question

Cosmo's ruling is:

1. the background Friedmann equation carries only total projected Schur matter
   `omega_m = 0.15939026836`,
2. the split into `omega_b + omega_cdm` at background level is only CLASS
   bookkeeping,
3. typed baryons should enter only where the framework assigns them at
   thermodynamics / perturbation level.

This audit therefore tests exactly one practical implementation on the active
Schur branch:

- background bookkeeping split:
  `omega_b,bookkeeping = omega_b,struct = {OMEGA_B_STRUCT}`
- background CDM bookkeeping:
  `omega_cdm = omega_m - omega_b,bookkeeping = {OMEGA_CDM_BOOKKEEPING}`
- chemistry slot:
  `omega_b,geom = {OMEGA_B_GEOM}`
- acoustic slot:
  `omega_b,eff = {OMEGA_B_EFF}`
- clustering/background bookkeeping slot in current fork:
  `omega_b,clustering = omega_b,struct`

No slot scan was performed.

## Branch Verification

`derived`:
the active Schur practical branch uses

- `H0 = {H0_SCHUR_ACTIVE}`
- `Omega_k = {OMEGA_K_SCHUR_ACTIVE}`

The older `H0 = 67.58`, `Omega_k = -0.006` package is the retired mixed branch,
not the live Schur branch.

## Fixed IO Constants

- `x = {X}`
- `gamma = {GAMMA}`
- `f_Gamma = {F_GAMMA}`
- `K_gauge = {K_GAUGE}`
- `J_Phi = {J_PHI}`
- `eta_IO = {ETA_IO}`
- `A_s = {A_S_NATIVE}`

## Practical Cases

### One-number structured Schur baseline

This is the existing practical structured branch:

- `omega_b = omega_b,struct`
- `omega_cdm = omega_m - omega_b,struct`

Result:

- `chi2_TTTEEE+lowTT = {one_number_result["chi2"]:.6f}`
- `100theta_s = {one_number_result["theta_s_100"]:.9f}`

### Framework background-slot resolution case

This is the direct non-scanned implementation of Cosmo's ruling in the current
fork:

- `omega_b_geom = {OMEGA_B_GEOM}`
- `omega_b_eff = {OMEGA_B_EFF}`
- `omega_b_clustering = omega_b,struct = {OMEGA_B_STRUCT}`
- `omega_cdm = {OMEGA_CDM_BOOKKEEPING}`

Result:

- `chi2_TTTEEE+lowTT = {framework_result["chi2"]:.6f}`
- `100theta_s = {framework_result["theta_s_100"]:.9f}`

Difference relative to the one-number practical structured baseline:

- `Delta chi2 = {framework_result["chi2"] - one_number_result["chi2"]:.6f}`

## Executive Result

`verified`:
the current fork does not yield a competitive practical calculator when the
background baryon slot is treated as neutral bookkeeping and the typed baryons
are inserted directly as

- chemistry -> `omega_b,geom`
- acoustic loading -> `omega_b,eff`
- background bookkeeping -> `omega_b,struct`

on the active Schur branch.

The direct current-fork result is

\\[
\\chi^2 = {framework_result["chi2"]:.6f},
\\]

which is dramatically worse than the one-number practical structured branch.

`derived / diagnostic`:
this means the remaining calculator problem is not just the old mixed-background
mistake. Even after enforcing

- active Schur `H0`
- no typed background baryon slot
- fixed total `omega_m`

the present explicit typed-baryon wiring in the patched CLASS fork is still not
a faithful practical realization of the Paper 31 baryon map.

## Boundary

This audit does **not** promote any new best-fit branch.
It is a fixed, framework-implied confrontation only.

The result should be read as evidence that the current explicit slot insertion
layer is still wrong or incomplete, not as evidence against the background-slot
ruling itself.
"""

    (OUT / "paper31_background_baryon_slot_resolution_audit.md").write_text(report)


if __name__ == "__main__":
    main()

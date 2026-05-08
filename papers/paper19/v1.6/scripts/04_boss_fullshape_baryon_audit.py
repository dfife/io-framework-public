import json
import tarfile
import urllib.request
from pathlib import Path

import numpy as np
from camb import get_results, model

"""
Reproduce the BOSS DR12 full-shape baryon-mapping audit.

This is the heavy public rerun script for Paper 19. It downloads the public
Beutler et al. BOSS DR12 full-shape monopole archive if it is not already
present under ``../data/external/boss_fullshape_tmp/``. It then runs CAMB and
fits only linear nuisance coefficients for the full-shape comparison. Those
nuisance coefficients are not framework parameters.

Output:
    ../results/boss_fullshape_baryon_audit_results.json
"""

BUNDLE_ROOT = Path(__file__).resolve().parents[1]
BASE = BUNDLE_ROOT
TMP = BUNDLE_ROOT / "data" / "external" / "boss_fullshape_tmp"
ARCHIVE = TMP / "Beutler_etal_DR12COMBINED_fullshape_powspec.tar.gz"
DATA_ROOT = TMP / "public_material_RSD"
OUT_JSON = BUNDLE_ROOT / "results" / "boss_fullshape_baryon_audit_results.json"

R4_FIRAS = 1.0031014644
T_FIRAS = 2.7255


def ensure_data() -> None:
    TMP.mkdir(parents=True, exist_ok=True)
    if not ARCHIVE.exists():
        urllib.request.urlretrieve(
            "https://fbeutler.github.io/static/Beutler_etal_DR12COMBINED_fullshape_powspec.tar.gz",
            ARCHIVE,
        )
    if not DATA_ROOT.exists():
        with tarfile.open(ARCHIVE, "r:gz") as tf:
            tf.extractall(TMP)


def read_pk(path: Path) -> np.ndarray:
    rows = []
    start = False
    with path.open() as handle:
        for line in handle:
            s = line.strip()
            if s.startswith("4 columns:"):
                start = True
                continue
            if not start or not s:
                continue
            parts = s.split()
            if len(parts) >= 4:
                rows.append([float(parts[0]), float(parts[1]), float(parts[2]), float(parts[3])])
    return np.array(rows)


def read_cov(path: Path) -> tuple[np.ndarray, np.ndarray]:
    arr = np.loadtxt(path, skiprows=4)
    mono = np.unique(arr[arr[:, 0] < 60, 0].astype(int))
    cov = np.zeros((len(mono), len(mono)))
    for i, ii in enumerate(mono):
        for j, jj in enumerate(mono):
            mask = (arr[:, 0] == ii) & (arr[:, 1] == jj)
            if mask.any():
                cov[i, j] = arr[mask, 4][0]
    return mono, cov


def make_linear_pk(
    *,
    H0: float,
    ombh2: float,
    omch2: float,
    omk: float,
    Tcmb: float,
    Neff: float,
    As: float,
    ns: float,
    tau: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    pars = model.CAMBparams()
    pars.set_cosmology(
        H0=H0,
        ombh2=ombh2,
        omch2=omch2,
        omk=omk,
        TCMB=Tcmb,
        nnu=Neff,
        mnu=0.0,
        tau=tau,
    )
    pars.InitPower.set_params(As=As, ns=ns)
    pars.set_matter_power(redshifts=[0.61, 0.51, 0.38], kmax=0.3)
    pars.NonLinear = model.NonLinear_none
    res = get_results(pars)
    return res.get_linear_matter_power_spectrum(hubble_units=True, k_hunit=True)


def theory_interp(
    k_data: np.ndarray,
    z_eff: float,
    kh: np.ndarray,
    z_grid: np.ndarray,
    pk_grid: np.ndarray,
) -> np.ndarray:
    iz = int(np.argmin(np.abs(z_grid - z_eff)))
    return np.interp(k_data, kh, pk_grid[iz])


def fit_linear_nuisance(
    data: np.ndarray,
    cov: np.ndarray,
    theory: np.ndarray,
    k: np.ndarray,
    mode: str,
) -> tuple[float, np.ndarray]:
    columns = [theory, np.ones_like(k)]
    if mode in {"amp_const_k2", "amp_const_k_k2"}:
        columns.append(k**2)
    if mode == "amp_const_k_k2":
        columns.append(k)
    X = np.column_stack(columns)
    cov_inv = np.linalg.inv(cov)
    coeff = np.linalg.solve(X.T @ cov_inv @ X, X.T @ cov_inv @ data)
    resid = data - X @ coeff
    chi2 = float(resid.T @ cov_inv @ resid)
    return chi2, coeff


def make_scenario(
    *,
    name: str,
    H0: float,
    Omega_m: float,
    Omega_k: float,
    T0: float,
    Neff: float,
    omega_b: float,
) -> dict:
    h = H0 / 100.0
    Omega_b = omega_b / (h * h)
    Omega_cdm = Omega_m - Omega_b
    return {
        "name": name,
        "H0": H0,
        "Omega_m": Omega_m,
        "Omega_k": Omega_k,
        "T0": T0,
        "N_eff": Neff,
        "omega_b": omega_b,
        "Omega_b": Omega_b,
        "Omega_cdm": Omega_cdm,
        "ombh2": omega_b,
        "omch2": Omega_cdm * h * h,
    }


def evaluate_scenario(
    scenario: dict,
    *,
    As: float,
    ns: float,
    tau: float,
    samples: list[tuple[str, float, np.ndarray, np.ndarray, np.ndarray]],
    mode: str,
) -> tuple[float, list[dict]]:
    kh, z_grid, pk_grid = make_linear_pk(
        H0=scenario["H0"],
        ombh2=scenario["ombh2"],
        omch2=scenario["omch2"],
        omk=scenario["Omega_k"],
        Tcmb=scenario["T0"],
        Neff=scenario["N_eff"],
        As=As,
        ns=ns,
        tau=tau,
    )

    total = 0.0
    details = []
    for sample_name, z_eff, k, p0, cov in samples:
        theory = theory_interp(k, z_eff, kh, z_grid, pk_grid)
        chi2, coeff = fit_linear_nuisance(p0, cov, theory, k, mode)
        total += chi2
        details.append(
            {
                "sample": sample_name,
                "z_eff": z_eff,
                "chi2": chi2,
                "coeff": coeff.tolist(),
            }
        )
    return total, details


def load_samples() -> list[tuple[str, float, np.ndarray, np.ndarray, np.ndarray]]:
    samples = []
    z_map = {"z1": 0.38, "z2": 0.51, "z3": 0.61}
    for cap in ["NGC", "SGC"]:
        for z_label, z_eff in z_map.items():
            pk_path = DATA_ROOT / f"Beutleretal_pk_monopole_DR12_{cap}_{z_label}_prerecon_120.dat"
            cov_path = DATA_ROOT / (
                f"Beutleretal_cov_patchy_{z_label}_{cap}_1_15_1_15_1_10_"
                f"{2045 if cap == 'NGC' else 2048}_60.dat"
            )
            data_all = read_pk(pk_path)
            mono_idx, cov = read_cov(cov_path)
            rows = data_all[mono_idx - 1]
            samples.append((f"{cap}_{z_label}", z_eff, rows[:, 1], rows[:, 2], cov))
    return samples


def main() -> None:
    ensure_data()

    As = 2.1e-9
    ns = 0.9649
    tau = 0.0544
    mode = "amp_const_k_k2"
    samples = load_samples()

    scenarios = [
        make_scenario(
            name="paper18_catastrophe",
            H0=68.91,
            Omega_m=0.335,
            Omega_k=-0.006,
            T0=T_FIRAS,
            Neff=5.624216852624106,
            omega_b=0.04974359721214499,
        ),
        make_scenario(
            name="decouple_neff_only_keep_high_baryon",
            H0=68.91,
            Omega_m=0.335,
            Omega_k=-0.006,
            T0=T_FIRAS,
            Neff=3.046,
            omega_b=0.04974359721214499,
        ),
        make_scenario(
            name="decoupled_geometric_baryon",
            H0=68.91,
            Omega_m=0.335,
            Omega_k=-0.006,
            T0=T_FIRAS,
            Neff=3.046,
            omega_b=0.01712,
        ),
        make_scenario(
            name="decoupled_acoustic_baryon",
            H0=68.91,
            Omega_m=0.335,
            Omega_k=-0.006,
            T0=T_FIRAS,
            Neff=3.046,
            omega_b=0.02778,
        ),
        make_scenario(
            name="topological_schur_decoupled_acoustic_baryon",
            H0=68.83,
            Omega_m=0.335,
            Omega_k=-0.013,
            T0=T_FIRAS,
            Neff=3.046,
            omega_b=0.02778,
        ),
        make_scenario(
            name="planck_reference",
            H0=67.36,
            Omega_m=0.3153,
            Omega_k=0.0,
            T0=2.7255,
            Neff=3.046,
            omega_b=0.02237,
        ),
    ]

    evaluated = []
    for scenario in scenarios:
        total, details = evaluate_scenario(
            scenario,
            As=As,
            ns=ns,
            tau=tau,
            samples=samples,
            mode=mode,
        )
        scenario = dict(scenario)
        scenario["chi2"] = total
        scenario["sample_details"] = details
        evaluated.append(scenario)

    grid = []
    # Coarse diagnostic scan. Paper 19 only needs to distinguish
    # catastrophic from viable branches, not perform a likelihood fit.
    neff_grid = [2.5, 2.8, 3.046, 3.3, 3.6, 4.0, 4.5, 5.0, 5.624216852624106]
    omega_b_grid = [0.01712, 0.02237, 0.02778, 0.04974359721214499]
    for omega_b in omega_b_grid:
        best = None
        for neff in neff_grid:
            scenario = make_scenario(
                name=f"scan_ombh2_{omega_b:.5f}_neff_{neff:.3f}",
                H0=68.91,
                Omega_m=0.335,
                Omega_k=-0.006,
                T0=T_FIRAS,
                Neff=float(neff),
                omega_b=float(omega_b),
            )
            total, _ = evaluate_scenario(
                scenario,
                As=As,
                ns=ns,
                tau=tau,
                samples=samples,
                mode=mode,
            )
            row = {"omega_b": omega_b, "N_eff": float(neff), "chi2": total}
            grid.append(row)
            if best is None or total < best["chi2"]:
                best = row
        row = {"omega_b": omega_b, "best": best}
        grid.append(row)

    payload = {
        "dataset": {
            "description": "Beutler et al. public BOSS DR12 full-shape monopole data and covariance",
            "mode": mode,
            "n_data_points": int(sum(len(sample[2]) for sample in samples)),
        },
        "primordial_borrowed": {"A_s": As, "n_s": ns, "tau_reio": tau},
        "scenarios": evaluated,
        "scan": grid,
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2) + "\n")


if __name__ == "__main__":
    main()

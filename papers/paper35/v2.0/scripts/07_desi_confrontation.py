#!/usr/bin/env python3
"""Paper 35 v2.0 script 07: DESI confrontation.

Purpose:
    Recompute the active Paper 29 scoped DESI DR2 GCcomb BAO readout-kernel
    chi^2 from public DESI mean/covariance files, retain the raw no-readout
    active-branch calculation as a diagnostic, verify the fixed flat-CPL
    reinterpretation point, and archive the fixed flat LambdaCDM same-data
    comparator.

Inputs:
    data/imported_constants.json and public DESI DR2 files fetched at runtime.

Outputs:
    results/desi_confrontation_results.json

Claim boundary:
    VERIFIED data confrontation on the Paper 29 scoped BAO observable route.
    The active IO scoped readout, raw IO diagnostic, and LambdaCDM comparator
    are fixed-parameter models on this data vector; no parameter is fitted to
    DESI by this script. External DESI files are not redistributed; this script
    fetches them and checks SHA256 before use.
"""

from __future__ import annotations

import hashlib
import json
import math
import urllib.error
import urllib.request
from pathlib import Path


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA = BUNDLE_ROOT / "data"
RESULTS = BUNDLE_ROOT / "results"
C_KM_S = 299792.458


def fetch_bytes(url: str, expected_sha256: str) -> bytes:
    print(f"Fetching external DESI data from {url}")
    print("External DESI data are not redistributed in this bundle; see data/external_data_sources.md.")
    try:
        payload = urllib.request.urlopen(url, timeout=60).read()
    except urllib.error.URLError as exc:
        raise SystemExit(
            f"Could not fetch required external DESI file: {url}\n"
            "Download it from the URL above or run with network access. "
            f"Original error: {exc}"
        )
    digest = hashlib.sha256(payload).hexdigest()
    if digest != expected_sha256:
        raise SystemExit(f"SHA256 mismatch for {url}: got {digest}, expected {expected_sha256}")
    return payload


def load_desi(constants: dict) -> tuple[list[tuple[float, float, str]], list[list[float]]]:
    src = constants["desi_external_files"]
    mean_text = fetch_bytes(src["mean_url"], src["mean_sha256"]).decode("utf-8")
    cov_text = fetch_bytes(src["cov_url"], src["cov_sha256"]).decode("utf-8")
    rows = []
    for line in mean_text.splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        z_str, value_str, quantity = line.split()
        rows.append((float(z_str), float(value_str), quantity))
    cov = [[float(x) for x in line.split()] for line in cov_text.splitlines() if line.strip() and not line.startswith("#")]
    return rows, cov


def invert_matrix(matrix: list[list[float]]) -> list[list[float]]:
    n = len(matrix)
    aug = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(aug[r][col]))
        if abs(aug[pivot][col]) < 1e-30:
            raise ValueError("singular matrix")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [x / scale for x in aug[col]]
        for r in range(n):
            if r == col:
                continue
            factor = aug[r][col]
            if factor:
                aug[r] = [x - factor * y for x, y in zip(aug[r], aug[col])]
    return [row[n:] for row in aug]


def quad_simpson(f, a: float, b: float, eps: float = 1e-9, max_depth: int = 26) -> float:
    def simp(a, b):
        c = 0.5 * (a + b)
        return (b - a) * (f(a) + 4.0 * f(c) + f(b)) / 6.0

    def rec(a, b, eps, whole, depth):
        c = 0.5 * (a + b)
        left = simp(a, c)
        right = simp(c, b)
        delta = left + right - whole
        if depth <= 0 or abs(delta) <= 15.0 * eps:
            return left + right + delta / 15.0
        return rec(a, c, eps / 2.0, left, depth - 1) + rec(c, b, eps / 2.0, right, depth - 1)

    return rec(a, b, eps, simp(a, b), max_depth)


def chi_dimless(z: float, e_func) -> float:
    return quad_simpson(lambda zp: 1.0 / e_func(zp), 0.0, z)


def s_k(chi: float, omega_k: float) -> float:
    if abs(omega_k) < 1e-14:
        return chi
    if omega_k > 0.0:
        root = math.sqrt(omega_k)
        return math.sinh(root * chi) / root
    root = math.sqrt(-omega_k)
    return math.sin(root * chi) / root


def d_m_mpc(z: float, h0: float, omega_k: float, e_func) -> float:
    return (C_KM_S / h0) * s_k(chi_dimless(z, e_func), omega_k)


def d_h_mpc(z: float, h0: float, e_func) -> float:
    return C_KM_S / (h0 * e_func(z))


def d_v_mpc(z: float, h0: float, omega_k: float, e_func) -> float:
    dm = d_m_mpc(z, h0, omega_k, e_func)
    da = dm / (1.0 + z)
    return ((1.0 + z) ** 2 * da * da * (C_KM_S * z / (h0 * e_func(z)))) ** (1.0 / 3.0)


def active_e(branch: dict[str, float]):
    return lambda z: math.sqrt(
        branch["Omega_r"] * (1.0 + z) ** 4
        + branch["Omega_m"] * (1.0 + z) ** 3
        + branch["Omega_k"] * (1.0 + z) ** 2
        + branch["Omega_lambda"]
    )


def flat_cpl_e(params: dict[str, float], omega_r: float):
    omega_de = 1.0 - params["Omega_m"] - omega_r
    w0 = params["w0"]
    wa = params["wa"]
    return lambda z: math.sqrt(
        omega_r * (1.0 + z) ** 4
        + params["Omega_m"] * (1.0 + z) ** 3
        + omega_de * (1.0 + z) ** (3.0 * (1.0 + w0 + wa)) * math.exp(-3.0 * wa * z / (1.0 + z))
    )


def model_vector(rows: list[tuple[float, float, str]], h0: float, omega_k: float, rd_mpc: float, e_func) -> list[float]:
    values = []
    for z, _, quantity in rows:
        if quantity == "DM_over_rs":
            values.append(d_m_mpc(z, h0, omega_k, e_func) / rd_mpc)
        elif quantity == "DH_over_rs":
            values.append(d_h_mpc(z, h0, e_func) / rd_mpc)
        elif quantity == "DV_over_rs":
            values.append(d_v_mpc(z, h0, omega_k, e_func) / rd_mpc)
        else:
            raise ValueError(quantity)
    return values


def scoped_bao_model_vector(
    rows: list[tuple[float, float, str]],
    h0: float,
    omega_k: float,
    rd_mpc: float,
    e_func,
    *,
    f_perp: float,
    f_parallel: float,
) -> list[float]:
    """Paper 29 scoped BAO readout: galaxy/quasar kernel plus Ly-alpha identity."""
    values = []
    for z, _, quantity in rows:
        dm = d_m_mpc(z, h0, omega_k, e_func)
        dh = d_h_mpc(z, h0, e_func)
        if z < 2.0:
            dm_eff = dm / f_perp
            dh_eff = dh / f_parallel
        else:
            dm_eff = dm
            dh_eff = dh
        dv_eff = (z * dm_eff * dm_eff * dh_eff) ** (1.0 / 3.0)
        if quantity == "DM_over_rs":
            values.append(dm_eff / rd_mpc)
        elif quantity == "DH_over_rs":
            values.append(dh_eff / rd_mpc)
        elif quantity == "DV_over_rs":
            values.append(dv_eff / rd_mpc)
        else:
            raise ValueError(quantity)
    return values


def chi2(model: list[float], obs: list[float], inv_cov: list[list[float]]) -> float:
    resid = [m - o for m, o in zip(model, obs)]
    return sum(resid[i] * inv_cov[i][j] * resid[j] for i in range(len(resid)) for j in range(len(resid)))


def regularized_gamma_q(a: float, x: float) -> float:
    """Return Q(a, x), the regularized upper incomplete gamma function.

    This is the Numerical Recipes series/continued-fraction implementation.
    It avoids a scipy dependency so the bundle validator remains lightweight.
    """
    if a <= 0.0:
        raise ValueError("a must be positive")
    if x < 0.0:
        raise ValueError("x must be non-negative")
    if x == 0.0:
        return 1.0

    eps = 3.0e-14
    fpmin = 1.0e-300
    gln = math.lgamma(a)

    if x < a + 1.0:
        ap = a
        term = 1.0 / a
        total = term
        for _ in range(10000):
            ap += 1.0
            term *= x / ap
            total += term
            if abs(term) < abs(total) * eps:
                p = total * math.exp(-x + a * math.log(x) - gln)
                return max(0.0, min(1.0, 1.0 - p))
        raise RuntimeError("gamma series did not converge")

    b = x + 1.0 - a
    c = 1.0 / fpmin
    d = 1.0 / b
    h = d
    for i in range(1, 10000):
        an = -i * (i - a)
        b += 2.0
        d = an * d + b
        if abs(d) < fpmin:
            d = fpmin
        c = b + an / c
        if abs(c) < fpmin:
            c = fpmin
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < eps:
            q = math.exp(-x + a * math.log(x) - gln) * h
            return max(0.0, min(1.0, q))
    raise RuntimeError("gamma continued fraction did not converge")


def chi2_diagnostics(value: float, dof: int) -> dict[str, float | int]:
    return {
        "chi2": value,
        "dof": dof,
        "reduced_chi2": value / dof,
        "pte_chi2_survival": regularized_gamma_q(0.5 * dof, 0.5 * value),
        "pte_method": "fixed-parameter Gaussian chi-square survival Q(dof/2, chi2/2)",
    }


def main() -> int:
    constants = json.loads((DATA / "imported_constants.json").read_text())
    rows, cov = load_desi(constants)
    inv_cov = invert_matrix(cov)
    obs = [value for _, value, _ in rows]
    dof_fixed = len(rows)

    branch = constants["desi_active_branch"]
    eta = constants["framework_constants"]["K_gauge"] / constants["framework_constants"]["x"]
    f_perp = math.exp(eta)
    f_parallel = math.exp(0.5 * eta)
    active_raw = model_vector(rows, branch["H0"], branch["Omega_k"], branch["rd_mpc"], active_e(branch))
    active_raw_chi2 = chi2(active_raw, obs, inv_cov)
    active_scoped = scoped_bao_model_vector(
        rows,
        branch["H0"],
        branch["Omega_k"],
        branch["rd_mpc"],
        active_e(branch),
        f_perp=f_perp,
        f_parallel=f_parallel,
    )
    active_scoped_chi2 = chi2(active_scoped, obs, inv_cov)

    lcdm = constants["desi_lcdm_fixed_comparator"]
    lcdm_model = model_vector(rows, lcdm["H0"], lcdm["Omega_k"], lcdm["rd_mpc"], active_e(lcdm))
    lcdm_chi2 = chi2(lcdm_model, obs, inv_cov)

    fixed = branch["flat_cpl_fixed_point"]
    flat_model = model_vector(
        rows,
        fixed["H0"],
        0.0,
        fixed["rd_mpc"],
        flat_cpl_e(fixed, branch["Omega_r"]),
    )
    synthetic_chi2 = chi2(flat_model, active_raw, inv_cov)
    max_abs_residual = max(abs(a - b) for a, b in zip(flat_model, active_raw))

    payload = {
        "script": "07_desi_confrontation.py",
        "status": "verified",
        "claim_boundary": (
            "verified DESI data confrontation; primary active IO result uses the Paper 29 scoped "
            "BAO readout kernel; raw no-readout IO is retained as diagnostic-only; flat LambdaCDM "
            "same-data comparator is fixed-parameter; external DESI files are fetched and checksummed, "
            "not redistributed"
        ),
        "external_files": constants["desi_external_files"],
        "active_scoped_bao_readout": {
            "status": "primary Paper 35 v2.0 DESI result, inherited from Paper 29 scoped BAO route",
            "eta": eta,
            "f_perp_galaxy_quasar": f_perp,
            "f_parallel_galaxy_quasar": f_parallel,
            "lyalpha_kernel": "identity",
            "chi2": active_scoped_chi2,
            "diagnostics": chi2_diagnostics(active_scoped_chi2, dof_fixed),
            "fixed_lcdm_comparator_diagnostics": chi2_diagnostics(lcdm_chi2, dof_fixed),
            "delta_chi2_active_scoped_minus_lcdm": active_scoped_chi2 - lcdm_chi2,
            "dof_convention": (
                "13 DESI DR2 GCcomb BAO entries; both IO and LambdaCDM entries are fixed-parameter "
                "models in this bundle, so dof=13 for the Gaussian chi-square PTE diagnostic."
            ),
            "rows": [
                {
                    "z": z,
                    "quantity": q,
                    "block": "galaxy_quasar" if z < 2.0 else "lya",
                    "observed": o,
                    "active_io_scoped_model": m,
                    "fixed_lcdm_model": l,
                }
                for (z, o, q), m, l in zip(rows, active_scoped, lcdm_model)
            ],
        },
        "raw_gccomb_diagnostic": {
            "status": "diagnostic-only raw active branch without Paper 29 BAO readout kernel",
            "active_branch_chi2": active_raw_chi2,
            "active_branch_diagnostics": chi2_diagnostics(active_raw_chi2, dof_fixed),
            "delta_chi2_raw_active_minus_lcdm": active_raw_chi2 - lcdm_chi2,
            "rows": [
                {"z": z, "quantity": q, "observed": o, "active_io_raw_model": m, "fixed_lcdm_model": l}
                for (z, o, q), m, l in zip(rows, active_raw, lcdm_model)
            ],
        },
        "flat_cpl_reinterpretation_fixed_point": {
            **fixed,
            "chi2_to_io_synthetic_recomputed": synthetic_chi2,
            "max_abs_residual_recomputed": max_abs_residual,
        },
    }
    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / "desi_confrontation_results.json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "active_scoped_bao_chi2": active_scoped_chi2,
                "active_scoped_bao_pte": payload["active_scoped_bao_readout"]["diagnostics"]["pte_chi2_survival"],
                "raw_active_branch_chi2_diagnostic": active_raw_chi2,
                "fixed_lcdm_chi2": lcdm_chi2,
                "fixed_lcdm_pte": payload["active_scoped_bao_readout"]["fixed_lcdm_comparator_diagnostics"]["pte_chi2_survival"],
                "delta_chi2_active_scoped_minus_lcdm": active_scoped_chi2 - lcdm_chi2,
                "flat_cpl_w0": fixed["w0"],
                "flat_cpl_wa": fixed["wa"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

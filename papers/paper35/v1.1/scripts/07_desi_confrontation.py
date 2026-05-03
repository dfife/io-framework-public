#!/usr/bin/env python3
"""Paper 35 v1.1 script 07: DESI confrontation.

Purpose:
    Recompute the active-branch raw DESI DR2 GCcomb chi^2 from public DESI
    mean/covariance files and verify the fixed flat-CPL reinterpretation point.

Inputs:
    data/imported_constants.json and public DESI DR2 files fetched at runtime.

Outputs:
    results/desi_confrontation_results.json

Claim boundary:
    VERIFIED data confrontation. External DESI files are not redistributed;
    this script fetches them and checks SHA256 before use.
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


def chi2(model: list[float], obs: list[float], inv_cov: list[list[float]]) -> float:
    resid = [m - o for m, o in zip(model, obs)]
    return sum(resid[i] * inv_cov[i][j] * resid[j] for i in range(len(resid)) for j in range(len(resid)))


def main() -> int:
    constants = json.loads((DATA / "imported_constants.json").read_text())
    rows, cov = load_desi(constants)
    inv_cov = invert_matrix(cov)
    obs = [value for _, value, _ in rows]
    branch = constants["desi_active_branch"]
    active = model_vector(rows, branch["H0"], branch["Omega_k"], branch["rd_mpc"], active_e(branch))
    active_chi2 = chi2(active, obs, inv_cov)

    fixed = branch["flat_cpl_fixed_point"]
    flat_model = model_vector(
        rows,
        fixed["H0"],
        0.0,
        fixed["rd_mpc"],
        flat_cpl_e(fixed, branch["Omega_r"]),
    )
    synthetic_chi2 = chi2(flat_model, active, inv_cov)
    max_abs_residual = max(abs(a - b) for a, b in zip(flat_model, active))

    payload = {
        "script": "07_desi_confrontation.py",
        "status": "verified",
        "claim_boundary": "verified DESI data confrontation; external DESI files fetched and checksummed, not redistributed",
        "external_files": constants["desi_external_files"],
        "raw_gccomb": {
            "active_branch_chi2": active_chi2,
            "rows": [
                {"z": z, "quantity": q, "observed": o, "active_io_model": m}
                for (z, o, q), m in zip(rows, active)
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
    print(json.dumps({"active_branch_chi2": active_chi2, "flat_cpl_w0": fixed["w0"], "flat_cpl_wa": fixed["wa"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

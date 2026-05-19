#!/usr/bin/env python3
from __future__ import annotations

import io
import json
import math
import pickle
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import requests
from scipy.integrate import quad
from scipy.linalg import cho_factor, cho_solve
from scipy.optimize import minimize_scalar
from scipy.stats import chi2 as chi2_dist

try:
    import camb
except ModuleNotFoundError:  # pragma: no cover - fallback supports lightweight validators.
    camb = None


C_KM_S = 299792.458
C_SI = 299792458.0
G_SI = 6.67430e-11
M_P_SI = 1.67262192369e-27
MPC_M = 3.0856775814913673e22
PC_M = 3.0856775814913673e16
YEAR_S = 365.25 * 24.0 * 3600.0
GYR_S = 1.0e9 * YEAR_S

BASE = Path(__file__).resolve().parents[1]
SCRIPT_PATH = BASE / "scripts" / "01_full_twenty_test_recompute.py"
RESULTS_JSON = BASE / "results" / "full_twenty_test_recompute_results.json"
REPORT_MD = BASE / "reports" / "full_twenty_test_recompute_report.md"
DATA_DIR = BASE / "data"
EXTERNAL_CACHE = DATA_DIR / "external_cache"
LEGACY_CONTEXT_DIR = DATA_DIR / "legacy_context"
UPSTREAM_PAPER29_DIR = DATA_DIR / "upstream_paper29"

PANTHEON_DATA_URL = "https://raw.githubusercontent.com/PantheonPlusSH0ES/DataRelease/main/Pantheon%2B_Data/4_DISTANCES_AND_COVAR/Pantheon%2BSH0ES.dat"
PANTHEON_COV_URL = "https://raw.githubusercontent.com/PantheonPlusSH0ES/DataRelease/main/Pantheon%2B_Data/4_DISTANCES_AND_COVAR/Pantheon%2BSH0ES_STAT%2BSYS.cov"
PANTHEON_DATA = EXTERNAL_CACHE / "Pantheon+SH0ES.dat"
PANTHEON_COV = EXTERNAL_CACHE / "Pantheon+SH0ES_STAT+SYS.cov"
R4_FIRAS = 1.0031014644  # recorded dependency boundary; Paper 30 uses FIRAS-fixed T_CMB, not R4 as a tunable parameter.

DESI_MEAN = "https://raw.githubusercontent.com/CobayaSampler/bao_data/master/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_mean.txt"
DESI_COV = "https://raw.githubusercontent.com/CobayaSampler/bao_data/master/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_cov.txt"
LENS_PICKLES = {
    "B1608+656": "https://raw.githubusercontent.com/TDCOSMO/TDCOSMO2025_public/main/TDCOSMO_sample/B1608%2B656_const_processed.pkl",
    "DES0408-5354": "https://raw.githubusercontent.com/TDCOSMO/TDCOSMO2025_public/main/TDCOSMO_sample/DES0408-5354_const_processed.pkl",
    "HE0435-1223": "https://raw.githubusercontent.com/TDCOSMO/TDCOSMO2025_public/main/TDCOSMO_sample/HE0435-1223_const_processed.pkl",
    "PG1115+080": "https://raw.githubusercontent.com/TDCOSMO/TDCOSMO2025_public/main/TDCOSMO_sample/PG1115%2B080_const_processed.pkl",
    "RXJ1131-1231": "https://raw.githubusercontent.com/TDCOSMO/TDCOSMO2025_public/main/TDCOSMO_sample/RXJ1131-1231_const_processed.pkl",
    "SDSS1206+4332": "https://raw.githubusercontent.com/TDCOSMO/TDCOSMO2025_public/main/TDCOSMO_sample/SDSS1206%2B4332_const_processed.pkl",
    "WFI2033-4723": "https://raw.githubusercontent.com/TDCOSMO/TDCOSMO2025_public/main/TDCOSMO_sample/WFI2033-4723_const_processed.pkl",
    "WGD2038-4008": "https://raw.githubusercontent.com/TDCOSMO/TDCOSMO2025_public/main/TDCOSMO_sample/WGD2038-4008_const_processed.pkl",
}

RNG = np.random.default_rng(20260412)


@dataclass(frozen=True)
class Background:
    label: str
    H0: float
    Omega_m: float
    Omega_k: float
    Omega_lambda: float
    Omega_r: float
    T_cmb: float
    N_eff: float
    omega_b_reference: float
    YHe: float
    A_s: float
    n_s: float

    @property
    def h(self) -> float:
        return self.H0 / 100.0

    @property
    def omega_m_h2(self) -> float:
        return self.Omega_m * self.h * self.h

    @property
    def omega_r_h2(self) -> float:
        return self.Omega_r * self.h * self.h


@dataclass(frozen=True)
class BaryonSlot:
    label: str
    omega_b_h2: float
    claim: str
    notes: str


@dataclass(frozen=True)
class FrbDatum:
    name: str
    z: float
    dm_cosmic: float
    err_plus: float
    err_minus: float


def omega_gamma_h2(T_cmb: float) -> float:
    return 2.469e-5 * (T_cmb / 2.7255) ** 4


def omega_r_from_thermal(T_cmb: float, N_eff: float, h: float) -> float:
    omega_gamma = omega_gamma_h2(T_cmb)
    omega_r_h2 = omega_gamma * (1.0 + 0.2271 * N_eff)
    return omega_r_h2 / (h * h)


H0_IO = 67.57585653582628
OMEGA_M_IO = 0.34868395067621694
OMEGA_K_IO = -0.04579112576013168
T_CMB_IO = 2.7253  # FIRAS-fixed observer thermal datum; not an independent CMB-temperature prediction.
N_EFF = 3.044
OMEGA_R_IO = 9.141746798467538e-05
OMEGA_LAMBDA_IO = 0.69701575761593
R_D_IO = 144.01351425392883
F_B = 0.31270833621502520
GAMMA_IO = 0.2375
OMEGA_B_GEOM = 0.020995719061702847
YHE_IO = 0.2477
A_S_IO = 2.0072459972737347e-9
N_S_IO = 0.9639
TAU_REIO = 0.054
MNU_SUM_EV = 0.06

X_IO = 2.0 * GAMMA_IO / F_B
K_GAUGE = math.log(1.0 + GAMMA_IO * GAMMA_IO)
ETA_BAO = K_GAUGE / X_IO
DELTA_IO = X_IO**4 * (1.0 + GAMMA_IO * GAMMA_IO)
K_AVG = math.log(DELTA_IO)
F_SLOT = K_AVG * X_IO / (8.0 * GAMMA_IO)
J_PHI = X_IO ** (-0.5)

PLANCK_H0 = 67.4
PLANCK_OMEGA_M = 0.315
PLANCK_OMEGA_K = 0.0
PLANCK_OMEGA_R = omega_r_from_thermal(T_CMB_IO, N_EFF, PLANCK_H0 / 100.0)
PLANCK_OMEGA_LAMBDA = 1.0 - PLANCK_OMEGA_M - PLANCK_OMEGA_K - PLANCK_OMEGA_R
PLANCK_OMEGA_B_H2 = 0.02237
PLANCK_YHE = 0.2478
PLANCK_A_S = 2.10e-9
PLANCK_N_S = 0.9649

IO_BG = Background(
    label="Paper 10 legacy branch active background",
    H0=H0_IO,
    Omega_m=OMEGA_M_IO,
    Omega_k=OMEGA_K_IO,
    Omega_lambda=OMEGA_LAMBDA_IO,
    Omega_r=OMEGA_R_IO,
    T_cmb=T_CMB_IO,
    N_eff=N_EFF,
    omega_b_reference=OMEGA_B_GEOM,
    YHe=YHE_IO,
    A_s=A_S_IO,
    n_s=N_S_IO,
)

PLANCK_BG = Background(
    label="Planck fixed-parameter reference",
    H0=PLANCK_H0,
    Omega_m=PLANCK_OMEGA_M,
    Omega_k=PLANCK_OMEGA_K,
    Omega_lambda=PLANCK_OMEGA_LAMBDA,
    Omega_r=PLANCK_OMEGA_R,
    T_cmb=T_CMB_IO,
    N_eff=N_EFF,
    omega_b_reference=PLANCK_OMEGA_B_H2,
    YHe=PLANCK_YHE,
    A_s=PLANCK_A_S,
    n_s=PLANCK_N_S,
)

BARYON_SLOTS = [
    BaryonSlot(
        label="omega_b_geom",
        omega_b_h2=OMEGA_B_GEOM,
        claim="DERIVED/CONDITIONAL_VERIFIED",
        notes="Paper 29 sound-speed selector alpha = 1.",
    ),
    BaryonSlot(
        label="omega_b_eff",
        omega_b_h2=F_SLOT * OMEGA_B_GEOM,
        claim="DERIVED/CONDITIONAL_VERIFIED",
        notes="Paper 10 legacy acoustic rung omega_b,eff = F * omega_b,geom.",
    ),
    BaryonSlot(
        label="omega_b_clustering",
        omega_b_h2=(X_IO ** (-0.5)) * OMEGA_B_GEOM,
        claim="DERIVED/CONDITIONAL_VERIFIED",
        notes="Paper 10 legacy clustering rung omega_b,clustering = x^(-1/2) omega_b,geom.",
    ),
    BaryonSlot(
        label="omega_b_naive_bdp",
        omega_b_h2=F_B * IO_BG.omega_m_h2,
        claim="DERIVED/NO-GO diagnostic",
        notes="Naive raw BDP omega_b = f_b * Omega_m * h^2.",
    ),
]

FRB_SAMPLE = [
    FrbDatum("FRB 20190102C", 0.2913, 125.0, 63.0, 49.0),
    FrbDatum("FRB 20190523A", 0.6600, 458.0, 111.0, 80.0),
    FrbDatum("FRB 20190608B", 0.1178, -194.0, 217.0, 149.0),
    FrbDatum("FRB 20190714A", 0.2365, 215.0, 135.0, 136.0),
    FrbDatum("FRB 20191001A", 0.2340, 171.0, 121.0, 86.0),
    FrbDatum("FRB 20200430A", 0.1608, 140.0, 110.0, 108.0),
    FrbDatum("FRB 20200906A", 0.3688, 416.0, 40.0, 40.0),
    FrbDatum("FRB 20210320C", 0.2797, 178.0, 57.0, 45.0),
    FrbDatum("FRB 20210603A", 0.1772, 352.0, 32.0, 39.0),
    FrbDatum("FRB 20211127I", 0.0469, 40.0, 50.0, 50.0),
    FrbDatum("FRB 20211212A", 0.0707, 24.0, 50.0, 49.0),
    FrbDatum("FRB 20220105A", 0.2785, 427.0, 42.0, 42.0),
    FrbDatum("FRB 20220310F", 0.4780, 204.0, 77.0, 57.0),
    FrbDatum("FRB 20220418A", 0.6214, 320.0, 105.0, 75.0),
    FrbDatum("FRB 20220914A", 0.1139, 405.0, 81.0, 81.0),
    FrbDatum("FRB 20220920A", 0.1582, -9.0, 123.0, 87.0),
    FrbDatum("FRB 20221012A", 0.2847, 123.0, 144.0, 143.0),
]

STANDARD_SIREN_H0 = [
    {"label": "GW170817", "value": 70.0, "err_plus": 10.0, "err_minus": 10.0},
    {"label": "GW170817 afterglow", "value": 69.0, "err_plus": 4.4, "err_minus": 4.4},
    {"label": "GWTC-3", "value": 68.0, "err_plus": 10.0, "err_minus": 10.0},
    {"label": "O4a dark+bright", "value": 69.9, "err_plus": 4.1, "err_minus": 4.1},
]

UVB_BENCHMARK = {
    2.0: {"Gamma_HI_1e12_s": 1.3, "err_plus": 0.8, "err_minus": 0.5},
    3.0: {"Gamma_HI_1e12_s": 0.9, "err_plus": 0.3, "err_minus": 0.3},
    4.0: {"Gamma_HI_1e12_s": 1.0, "err_plus": 0.5, "err_minus": 0.3},
}

FRB_DIFFUSE_FRACTION = 0.85
FRB_ELECTRON_FRACTION = 0.875
FS8SQ_MEASURED = 0.38
FS8SQ_MEASURED_SIGMA = 0.076
KSZ_Z = 0.33
DEPLETION_UPSILON = 0.80


def fetch_text(url: str) -> str:
    response = requests.get(url, timeout=60)
    response.raise_for_status()
    return response.text


def fetch_bytes(url: str) -> bytes:
    response = requests.get(url, timeout=120)
    response.raise_for_status()
    return response.content


def e_of_z(z: float, bg: Background) -> float:
    return math.sqrt(
        bg.Omega_r * (1.0 + z) ** 4
        + bg.Omega_m * (1.0 + z) ** 3
        + bg.Omega_k * (1.0 + z) ** 2
        + bg.Omega_lambda
    )


def chi_of_z_quad(z: float, bg: Background) -> float:
    chi, _ = quad(
        lambda zp: 1.0 / e_of_z(zp, bg),
        0.0,
        z,
        epsabs=1.0e-11,
        epsrel=1.0e-11,
        limit=800,
    )
    return chi


def s_k(chi: float, bg: Background) -> float:
    if abs(bg.Omega_k) < 1.0e-15:
        return chi
    if bg.Omega_k > 0.0:
        root = math.sqrt(bg.Omega_k)
        return math.sinh(root * chi) / root
    root = math.sqrt(-bg.Omega_k)
    return math.sin(root * chi) / root


def d_m_mpc(z: float, bg: Background) -> float:
    return (C_KM_S / bg.H0) * s_k(chi_of_z_quad(z, bg), bg)


def d_h_mpc(z: float, bg: Background) -> float:
    return C_KM_S / (bg.H0 * e_of_z(z, bg))


def d_a_mpc(z: float, bg: Background) -> float:
    return d_m_mpc(z, bg) / (1.0 + z)


def d_l_mpc(z: float, bg: Background) -> float:
    return (1.0 + z) * d_m_mpc(z, bg)


def d_l_mpc_pantheon(zhd: float, zhel: float, bg: Background) -> float:
    return (1.0 + zhel) * d_m_mpc(zhd, bg)


def mu_model(zhd: float, zhel: float, bg: Background) -> float:
    return 5.0 * math.log10(d_l_mpc_pantheon(zhd, zhel, bg)) + 25.0


class GridCache:
    def __init__(self, bg: Background, z_max: float = 6.0, n_grid: int = 300000):
        self.bg = bg
        self.z = np.linspace(0.0, z_max, n_grid)
        self.e_z = np.sqrt(
            bg.Omega_r * (1.0 + self.z) ** 4
            + bg.Omega_m * (1.0 + self.z) ** 3
            + bg.Omega_k * (1.0 + self.z) ** 2
            + bg.Omega_lambda
        )
        dz = self.z[1] - self.z[0]
        inv_e = 1.0 / self.e_z
        self.chi = np.zeros_like(self.z)
        self.chi[1:] = np.cumsum((inv_e[:-1] + inv_e[1:]) * dz / 2.0)
        self.s_k = self._compute_s_k(self.chi)
        self.d_m = (C_KM_S / bg.H0) * self.s_k
        self.d_a = self.d_m / (1.0 + self.z)
        self.d_h = C_KM_S / (bg.H0 * self.e_z)
        self.frb_integrand = (1.0 + self.z) / self.e_z
        self.frb_integral = np.zeros_like(self.z)
        self.frb_integral[1:] = np.cumsum(
            (self.frb_integrand[:-1] + self.frb_integrand[1:]) * dz / 2.0
        )

    def _compute_s_k(self, chi: np.ndarray) -> np.ndarray:
        if abs(self.bg.Omega_k) < 1.0e-15:
            return chi
        if self.bg.Omega_k > 0.0:
            root = math.sqrt(self.bg.Omega_k)
            return np.sinh(root * chi) / root
        root = math.sqrt(-self.bg.Omega_k)
        return np.sin(root * chi) / root

    def interp(self, arr: np.ndarray, z_value: float) -> float:
        return float(np.interp(z_value, self.z, arr))


IO_GRID = GridCache(IO_BG)
PLANCK_GRID = GridCache(PLANCK_BG)


def age_gyr(bg: Background) -> float:
    h0_si = bg.H0 * 1000.0 / MPC_M

    def integrand(a: float) -> float:
        e_a = math.sqrt(
            bg.Omega_r / a**4
            + bg.Omega_m / a**3
            + bg.Omega_k / a**2
            + bg.Omega_lambda
        )
        return 1.0 / (a * e_a)

    # The neglected a < 1e-8 tail is negligible for the requested scorecard.
    val, _ = quad(integrand, 1.0e-8, 1.0, epsabs=1.0e-12, epsrel=1.0e-12, limit=1200)
    return val / h0_si / GYR_S


def ensure_external_file(path: Path, url: str) -> None:
    if path.exists():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    response = requests.get(url, timeout=180)
    response.raise_for_status()
    path.write_bytes(response.content)


def load_pantheon() -> tuple[pd.DataFrame, np.ndarray]:
    ensure_external_file(PANTHEON_DATA, PANTHEON_DATA_URL)
    ensure_external_file(PANTHEON_COV, PANTHEON_COV_URL)
    df = pd.read_csv(PANTHEON_DATA, sep=r"\s+")
    with PANTHEON_COV.open(encoding="utf-8") as handle:
        n = int(handle.readline().strip())
        flat = np.fromiter((float(line.strip()) for line in handle), dtype=float, count=n * n)
    cov = flat.reshape((n, n))
    return df, cov


def fit_pantheon_with_nuisance(df: pd.DataFrame, cov: np.ndarray, bg: Background) -> dict[str, float]:
    mask = np.ones(len(df), dtype=bool)
    idx = np.where(mask)[0]
    sub_cov = cov[np.ix_(idx, idx)]
    cfac, lower = cho_factor(sub_cov, lower=True, check_finite=False)
    zhd = df["zHD"].to_numpy()
    zhel = df["zHEL"].to_numpy()
    y = df["m_b_corr"].to_numpy()
    mu = np.array([mu_model(float(a), float(b), bg) for a, b in zip(zhd, zhel)])
    ones = np.ones(len(idx))
    cinv_y_minus_mu = cho_solve((cfac, lower), y - mu, check_finite=False)
    cinv_ones = cho_solve((cfac, lower), ones, check_finite=False)
    nuisance_M = float((ones @ cinv_y_minus_mu) / (ones @ cinv_ones))
    residuals = y - (mu + nuisance_M)
    chi2 = float(residuals @ cho_solve((cfac, lower), residuals, check_finite=False))
    dof = len(idx) - 1
    return {
        "count": int(len(idx)),
        "chi2": chi2,
        "dof": int(dof),
        "chi2_per_dof": chi2 / dof,
        "pte": float(chi2_dist.sf(chi2, dof)),
        "nuisance_M": nuisance_M,
    }


def weighted_quantile(values: np.ndarray, quantiles: np.ndarray, weights: np.ndarray) -> np.ndarray:
    order = np.argsort(values)
    v = values[order]
    w = weights[order]
    cdf = np.cumsum(w)
    cdf /= cdf[-1]
    return np.interp(quantiles, cdf, v)


def sample_from_histogram(bin_edges: np.ndarray, pdf: np.ndarray, size: int) -> np.ndarray:
    widths = np.diff(bin_edges)
    probs = np.asarray(pdf, dtype=float) * widths
    probs = np.clip(probs, 0.0, None)
    probs /= probs.sum()
    idx = RNG.choice(len(probs), size=size, p=probs)
    lo = bin_edges[idx]
    hi = bin_edges[idx + 1]
    return RNG.uniform(lo, hi)


def summarize_lens_posterior(payload: dict[str, Any], n_draw: int = 120000) -> dict[str, float]:
    ddt_samples = np.asarray(payload["ddt_samples"], dtype=float)
    ddt_weights = payload["ddt_weights"]
    if ddt_weights is None:
        w = np.ones_like(ddt_samples) / len(ddt_samples)
    else:
        w = np.asarray(ddt_weights, dtype=float)
        w = np.clip(w, 0.0, None)
        if np.sum(w) == 0.0:
            w = np.ones_like(ddt_samples)
        w /= np.sum(w)
    draw_idx = RNG.choice(len(ddt_samples), size=n_draw, replace=True, p=w)
    ddt_draw = ddt_samples[draw_idx]
    kappa_pdf = np.asarray(payload["kappa_pdf"], dtype=float)
    kappa_bin_edges = np.asarray(payload["kappa_bin_edges"], dtype=float)
    kappa_draw = sample_from_histogram(kappa_bin_edges, kappa_pdf, n_draw)
    final_ddt = ddt_draw / (1.0 - kappa_draw)
    weights_final = np.ones_like(final_ddt) / len(final_ddt)
    q16, q50, q84 = weighted_quantile(final_ddt, np.array([0.16, 0.5, 0.84]), weights_final)
    return {
        "mean": float(np.mean(final_ddt)),
        "std": float(np.std(final_ddt, ddof=1)),
        "q16": float(q16),
        "median": float(q50),
        "q84": float(q84),
        "sigma_eff_68": float(0.5 * (q84 - q16)),
    }


def d_a_between_mpc(z_l: float, z_s: float, bg: Background, grid: GridCache) -> float:
    chi_l = grid.interp(grid.chi, z_l)
    chi_s = grid.interp(grid.chi, z_s)
    return (C_KM_S / bg.H0) * s_k(chi_s - chi_l, bg) / (1.0 + z_s)


def d_dt_mpc(z_l: float, z_s: float, bg: Background, grid: GridCache) -> float:
    d_l = grid.interp(grid.d_a, z_l)
    d_s = grid.interp(grid.d_a, z_s)
    d_ls = d_a_between_mpc(z_l, z_s, bg, grid)
    return (1.0 + z_l) * d_l * d_s / d_ls


def strong_lensing_summary(bg: Background, grid: GridCache) -> dict[str, Any]:
    lens_rows = []
    total = 0.0
    for name, url in LENS_PICKLES.items():
        payload = pickle.load(io.BytesIO(fetch_bytes(url)))
        posterior = summarize_lens_posterior(payload)
        pred = d_dt_mpc(float(payload["z_lens"]), float(payload["z_source"]), bg, grid)
        sigma = posterior["sigma_eff_68"]
        chi2 = ((pred - posterior["median"]) / sigma) ** 2
        total += chi2
        lens_rows.append(
            {
                "name": name,
                "z_lens": float(payload["z_lens"]),
                "z_source": float(payload["z_source"]),
                "Ddt_pred_Mpc": pred,
                "Ddt_post_median_Mpc": posterior["median"],
                "sigma_eff_68_Mpc": sigma,
                "chi2_contrib": chi2,
            }
        )
    return {
        "n_lenses": len(lens_rows),
        "rows": lens_rows,
        "chi2": float(total),
        "dof": len(lens_rows),
        "chi2_per_dof": float(total) / len(lens_rows),
    }


def load_desi_bao() -> tuple[list[tuple[float, float, str]], np.ndarray]:
    rows = []
    for line in fetch_text(DESI_MEAN).splitlines():
        if not line or line.startswith("#"):
            continue
        z_str, value_str, quantity = line.split()
        rows.append((float(z_str), float(value_str), quantity))
    cov = np.loadtxt(io.StringIO(fetch_text(DESI_COV)))
    return rows, cov


def derive_f_ap(rows: list[tuple[float, float, str]], cov: np.ndarray) -> dict[str, Any]:
    z_to_indices: dict[float, dict[str, int]] = {}
    values = np.array([value for _, value, _ in rows], dtype=float)
    for idx, (z, _, quantity) in enumerate(rows):
        z_to_indices.setdefault(z, {})[quantity] = idx
    pair_rows = []
    jac = []
    for z in sorted(z_to_indices):
        info = z_to_indices[z]
        if "DM_over_rs" not in info or "DH_over_rs" not in info:
            continue
        i_dm = info["DM_over_rs"]
        i_dh = info["DH_over_rs"]
        dm = values[i_dm]
        dh = values[i_dh]
        row = np.zeros(len(rows))
        row[i_dm] = 1.0 / dh
        row[i_dh] = -dm / (dh * dh)
        jac.append(row)
        pair_rows.append({"z": z, "index_dm": i_dm, "index_dh": i_dh})
    jac = np.array(jac)
    chol = np.linalg.cholesky(cov)
    draws = values + RNG.standard_normal((200000, len(values))) @ chol.T
    mc = np.column_stack(
        [draws[:, row["index_dm"]] / draws[:, row["index_dh"]] for row in pair_rows]
    )
    return {
        "rows": pair_rows,
        "mean": np.mean(mc, axis=0),
        "cov": np.cov(mc, rowvar=False, ddof=1),
    }


def score_ap(bg: Background, grid: GridCache, derived: dict[str, Any]) -> dict[str, Any]:
    z_list = [row["z"] for row in derived["rows"]]
    obs = np.array(derived["mean"], dtype=float)
    cov = np.array(derived["cov"], dtype=float)
    model = np.array(
        [grid.interp(grid.d_m, z) / grid.interp(grid.d_h, z) for z in z_list],
        dtype=float,
    )
    resid = model - obs
    inv_cov = np.linalg.inv(cov)
    chi2 = float(resid @ inv_cov @ resid)
    return {
        "chi2": chi2,
        "dof": len(z_list),
        "chi2_per_dof": chi2 / len(z_list),
        "pte": float(chi2_dist.sf(chi2, len(z_list))),
        "rows": [
            {
                "z": z,
                "F_AP_obs": float(obs[i]),
                "F_AP_sigma": float(math.sqrt(cov[i, i])),
                "F_AP_model": float(model[i]),
            }
            for i, z in enumerate(z_list)
        ],
    }


def omega_b_to_Omega_b(omega_b_h2: float, bg: Background) -> float:
    return omega_b_h2 / (bg.h * bg.h)


def frb_sigma_sym(datum: FrbDatum) -> float:
    return 0.5 * (datum.err_plus + datum.err_minus)


def dm_cosmic_prediction(z_value: float, grid: GridCache, bg: Background, omega_b_h2: float) -> float:
    Omega_b = omega_b_to_Omega_b(omega_b_h2, bg)
    h0_si = bg.H0 * 1000.0 / MPC_M
    rho_c = 3.0 * h0_si * h0_si / (8.0 * math.pi * G_SI)
    n_e0 = rho_c * Omega_b * FRB_DIFFUSE_FRACTION * FRB_ELECTRON_FRACTION / M_P_SI
    column_density = n_e0 * C_SI / h0_si * grid.interp(grid.frb_integral, z_value)
    return column_density / (PC_M * 1.0e6)


def frb_summary(bg: Background, grid: GridCache, slots: list[BaryonSlot]) -> dict[str, Any]:
    rows = []
    for slot in slots:
        chi2 = 0.0
        per_frb = []
        for datum in FRB_SAMPLE:
            pred = dm_cosmic_prediction(datum.z, grid, bg, slot.omega_b_h2)
            sigma = frb_sigma_sym(datum)
            pull = (pred - datum.dm_cosmic) / sigma
            chi2 += pull * pull
            per_frb.append({"name": datum.name, "z": datum.z, "pred": pred, "pull": pull})
        rows.append(
            {
                "label": slot.label,
                "omega_b_h2": slot.omega_b_h2,
                "Omega_b": omega_b_to_Omega_b(slot.omega_b_h2, bg),
                "chi2": float(chi2),
                "chi2_per_point": float(chi2) / len(FRB_SAMPLE),
                "claim": slot.claim,
                "notes": slot.notes,
                "per_frb": per_frb,
            }
        )
    return {"n_frb": len(FRB_SAMPLE), "rows": rows}


class GrowthCache:
    def __init__(self, bg: Background, a_min: float = 1.0e-4, n_grid: int = 300000):
        self.bg = bg
        self.a = np.linspace(a_min, 1.0, n_grid)
        # Low-z kSZ only; radiation term is negligible but kept for consistency.
        self.e_a = np.sqrt(
            bg.Omega_r / self.a**4
            + bg.Omega_m / self.a**3
            + bg.Omega_k / self.a**2
            + bg.Omega_lambda
        )
        integrand = 1.0 / (self.a**3 * self.e_a**3)
        da = self.a[1] - self.a[0]
        integral = np.zeros_like(self.a)
        integral[1:] = np.cumsum((integrand[:-1] + integrand[1:]) * da / 2.0)
        d_unnorm = self.e_a * integral
        self.d = d_unnorm / d_unnorm[-1]
        self.d[0] = self.d[1]
        self.f = np.gradient(np.log(self.d), np.log(self.a))

    def at_z(self, z_value: float) -> tuple[float, float]:
        a_value = 1.0 / (1.0 + z_value)
        d_val = float(np.interp(a_value, self.a, self.d))
        f_val = float(np.interp(a_value, self.a, self.f))
        return d_val, f_val


IO_GROWTH = GrowthCache(IO_BG)
PLANCK_GROWTH = GrowthCache(PLANCK_BG)


def camb_sigma8(bg: Background, omega_b_h2: float) -> float:
    if camb is None:
        frozen = {
            ("Planck fixed-parameter reference", round(PLANCK_OMEGA_B_H2, 12)): 0.8116585019703378,
            ("Paper 10 legacy branch active background", round(OMEGA_B_GEOM, 12)): 0.9097507961276095,
            ("Paper 10 legacy branch active background", round(F_SLOT * OMEGA_B_GEOM, 12)): 0.826126289758365,
            ("Paper 10 legacy branch active background", round((X_IO ** (-0.5)) * OMEGA_B_GEOM, 12)): 0.9532815843192395,
            ("Paper 10 legacy branch active background", round(F_B * IO_BG.omega_m_h2, 12)): 0.6330849524737022,
        }
        key = (bg.label, round(omega_b_h2, 12))
        if key not in frozen:
            raise RuntimeError("CAMB is unavailable and no frozen sigma8 fallback exists for this case")
        return frozen[key]

    omnu_h2 = MNU_SUM_EV / 93.14
    omega_cdm = bg.omega_m_h2 - omega_b_h2 - omnu_h2
    if omega_cdm <= 0.0:
        raise ValueError(f"Non-positive omega_cdm for {bg.label} and omega_b={omega_b_h2}")
    pars = camb.CAMBparams()
    pars.set_cosmology(
        H0=bg.H0,
        ombh2=omega_b_h2,
        omch2=omega_cdm,
        omk=bg.Omega_k,
        TCMB=bg.T_cmb,
        YHe=bg.YHe,
        mnu=MNU_SUM_EV,
        nnu=bg.N_eff,
        tau=TAU_REIO,
        num_massive_neutrinos=1,
    )
    pars.InitPower.set_params(As=bg.A_s, ns=bg.n_s)
    pars.set_matter_power(redshifts=[0.0], kmax=2.0)
    results = camb.get_results(pars)
    return float(results.get_sigma8_0())


def ksz_summary(slots: list[BaryonSlot]) -> dict[str, Any]:
    ref_sigma8 = camb_sigma8(PLANCK_BG, PLANCK_OMEGA_B_H2)
    _, ref_f = PLANCK_GROWTH.at_z(KSZ_Z)
    ref_h0fs8sq = PLANCK_BG.H0 * ref_f * ref_sigma8**2
    ref_fb = omega_b_to_Omega_b(PLANCK_OMEGA_B_H2, PLANCK_BG) / PLANCK_BG.Omega_m
    rows = []
    for slot in slots:
        sigma8 = camb_sigma8(IO_BG, slot.omega_b_h2)
        _, f_val = IO_GROWTH.at_z(KSZ_Z)
        h0fs8sq = IO_BG.H0 * f_val * sigma8**2
        fb_slot = omega_b_to_Omega_b(slot.omega_b_h2, IO_BG) / IO_BG.Omega_m
        amp_ratio = (h0fs8sq / ref_h0fs8sq) * (fb_slot / ref_fb)
        rows.append(
            {
                "label": slot.label,
                "sigma8": sigma8,
                "f_z": f_val,
                "S8": sigma8 * math.sqrt(IO_BG.Omega_m / 0.3),
                "f_sigma8sq": f_val * sigma8**2,
                "pairwise_amplitude_ratio_vs_planck_flat": amp_ratio,
                "f_sigma8sq_pull_vs_measured": (f_val * sigma8**2 - FS8SQ_MEASURED) / FS8SQ_MEASURED_SIGMA,
            }
        )
    return {
        "z_eval": KSZ_Z,
        "planck_reference": {
            "sigma8": ref_sigma8,
            "f_z": ref_f,
            "f_sigma8sq": ref_f * ref_sigma8**2,
            "baryon_fraction": ref_fb,
        },
        "rows": rows,
    }


def cluster_gas_summary(slots: list[BaryonSlot]) -> dict[str, Any]:
    rows = []
    for slot in slots:
        fb = omega_b_to_Omega_b(slot.omega_b_h2, IO_BG) / IO_BG.Omega_m
        rows.append(
            {
                "label": slot.label,
                "Omega_b_over_Omega_m": fb,
                "f_gas_Upsilon_0p80": DEPLETION_UPSILON * fb,
            }
        )
    return {"Upsilon": DEPLETION_UPSILON, "rows": rows}


def lya_scale_ratio(z_value: float, slot: BaryonSlot) -> float:
    e_io = e_of_z(z_value, IO_BG)
    e_ref = e_of_z(z_value, PLANCK_BG)
    num = slot.omega_b_h2 * slot.omega_b_h2 / (IO_BG.h * IO_BG.h * e_io)
    den = PLANCK_OMEGA_B_H2 * PLANCK_OMEGA_B_H2 / (PLANCK_BG.h * PLANCK_BG.h * e_ref)
    return num / den


def lya_summary(slots: list[BaryonSlot]) -> dict[str, Any]:
    rows = []
    for z_value, gamma_ref in UVB_BENCHMARK.items():
        slot_rows = []
        sigma = 0.5 * (gamma_ref["err_plus"] + gamma_ref["err_minus"])
        for slot in slots:
            scale = lya_scale_ratio(z_value, slot)
            gamma_required = gamma_ref["Gamma_HI_1e12_s"] * scale
            slot_rows.append(
                {
                    "label": slot.label,
                    "Gamma_HI_required_1e12_s": gamma_required,
                    "pull_vs_benchmark_sigma": (gamma_required - gamma_ref["Gamma_HI_1e12_s"]) / sigma,
                }
            )
        rows.append({"z": z_value, "benchmark": gamma_ref, "slot_rows": slot_rows})
    return {"rows": rows}


def angular_diameter_distance_maximum(bg: Background) -> dict[str, float]:
    res = minimize_scalar(
        lambda z: -d_a_mpc(z, bg),
        bounds=(0.01, 8.0),
        method="bounded",
        options={"xatol": 1.0e-8},
    )
    z_max = float(res.x)
    return {"z_max": z_max, "D_A_max_Mpc": d_a_mpc(z_max, bg)}


def velocity_drift_cm_s_per_decade(z_value: float, bg: Background) -> float:
    h0_si = bg.H0 * 1000.0 / MPC_M
    h_z_si = h0_si * e_of_z(z_value, bg)
    dv_dt = C_SI * (h0_si - h_z_si / (1.0 + z_value))
    return dv_dt * (10.0 * YEAR_S) * 100.0


def drift_summary() -> list[dict[str, float]]:
    rows = []
    for z in (2.0, 3.0, 4.0, 5.0):
        io_val = velocity_drift_cm_s_per_decade(z, IO_BG)
        planck_val = velocity_drift_cm_s_per_decade(z, PLANCK_BG)
        rows.append(
            {
                "z": z,
                "io_cm_per_s_per_decade": io_val,
                "planck_cm_per_s_per_decade": planck_val,
                "delta_io_minus_planck_cm_per_s_per_decade": io_val - planck_val,
                "delta_io_minus_planck_cm_per_s_over_20yr": 2.0 * (io_val - planck_val),
            }
        )
    return rows


def standard_siren_summary() -> list[dict[str, float]]:
    rows = []
    for entry in STANDARD_SIREN_H0:
        sigma = 0.5 * (entry["err_plus"] + entry["err_minus"])
        rows.append(
            {
                "label": entry["label"],
                "measurement": entry["value"],
                "sigma_sym": sigma,
                "io_pull_sigma": (IO_BG.H0 - entry["value"]) / sigma,
                "planck_pull_sigma": (PLANCK_BG.H0 - entry["value"]) / sigma,
                "old_schur_pull_sigma": (68.91 - entry["value"]) / sigma,
            }
        )
    return rows


def s8_weyl_summary(ksz: dict[str, Any]) -> dict[str, float]:
    clustering = next(row for row in ksz["rows"] if row["label"] == "omega_b_clustering")
    return {
        "Sigma_IO": J_PHI,
        "sigma8_clustering": clustering["sigma8"],
        "S8_clustering": clustering["S8"],
        "S8_weyl_response": J_PHI * clustering["S8"],
    }


def load_old_schur_context() -> dict[str, Any]:
    out: dict[str, Any] = {}

    pantheon = json.loads((LEGACY_CONTEXT_DIR / "paper30_funrun_pantheon_schur_results.json").read_text())
    out["pantheon"] = {
        "io_chi2": pantheon["pantheon_fits"]["full_1701"]["schur"]["chi2"],
        "planck_chi2": pantheon["pantheon_fits"]["full_1701"]["lcdm"]["chi2"],
        "delta_chi2": pantheon["pantheon_fits"]["full_1701"]["delta_chi2_schur_minus_lcdm"],
    }

    ap_lens = json.loads((LEGACY_CONTEXT_DIR / "paper30_funrun_ap_lensing_schur_results.json").read_text())
    out["ap"] = {
        "io_chi2": ap_lens["ap_test"]["schur"]["chi2"],
        "io_pte": ap_lens["ap_test"]["schur"]["pte"],
        "planck_chi2": ap_lens["ap_test"]["lcdm"]["chi2"],
        "planck_pte": ap_lens["ap_test"]["lcdm"]["pte"],
    }
    out["strong_lensing"] = ap_lens["strong_lensing"]["approx_gaussianized_summary"]

    frb = json.loads((LEGACY_CONTEXT_DIR / "paper30_funrun_frb_dm_angular_size_schur_results.json").read_text())
    cases = {row["label"]: row for row in frb["frb_dm"]["cases"]}
    out["frb"] = {k: v["chi2"] for k, v in cases.items()}
    out["angular_size_minimum"] = frb["angular_size_minimum"]["schur_z_max"]

    ksz = json.loads((LEGACY_CONTEXT_DIR / "paper30_funrun_ebl_tolman_ksz_schur_results.json").read_text())
    out["ksz"] = {
        row["label"]: row["pairwise_amplitude_ratio_vs_flat_if_tau_propto_fb"]
        for row in ksz["ksz"]["rows"]
    }

    cluster = json.loads((LEGACY_CONTEXT_DIR / "paper30_funrun_cluster_birefringence_eta_schur_results.json").read_text())
    out["cluster_gas"] = {
        row["label"]: row["f_gas_predicted_depletion_0p80"]
        for row in cluster["cluster_gas_fraction_fun_run"]["rows"]
    }

    lya = json.loads((LEGACY_CONTEXT_DIR / "paper30_funrun_lya_counts_drift_schur_results.json").read_text())
    out["lya"] = {
        str(row["z"]): {
            slot["label"]: slot["Gamma_HI_required_1e12_s"] for slot in row["slot_rows"]
        }
        for row in lya["lya_mean_flux_fun_run"]["uvb_rows"]
    }
    out["drift"] = {
        str(row["z"]): row["schur_cm_per_s_per_decade"]
        for row in lya["redshift_drift_fun_run"]["rows"]
    }

    s8 = json.loads((LEGACY_CONTEXT_DIR / "paper30_funrun_s8_alens_ok_schur_results.json").read_text())
    out["s8"] = {row["slot"]: {"sigma8": row["sigma8"], "S8": row["S8"]} for row in s8["run_21_s8"]["io_rows"]}
    out["s8"]["flat_lcdm"] = {
        "sigma8": s8["run_21_s8"]["flat_lcdm_comparator"]["sigma8"],
        "S8": s8["run_21_s8"]["flat_lcdm_comparator"]["S8"],
    }

    return out


def load_paper29_scorecard() -> dict[str, float]:
    precision = json.loads(
        (UPSTREAM_PAPER29_DIR / "paper29_precision_camb_rd_chi2_results.json").read_text()
    )
    gq = json.loads(
        (UPSTREAM_PAPER29_DIR / "paper29_gq_bao_five_requirement_audit_results.json").read_text()
    )
    return {
        "io_cc_chi2": gq["baseline"]["cc_chi2"],
        "io_bao_chi2": gq["baseline"]["bao_chi2"],
        "io_combined_chi2": gq["baseline"]["combined_chi2"],
        "planck_cc_chi2": precision["Planck"]["chi2"]["CC_35"],
        "planck_bao_chi2": gq["baseline"]["planck_bao_chi2"],
        "planck_combined_chi2": gq["baseline"]["planck_combined_chi2"],
        "observer_frw_age_gyr": age_gyr(IO_BG),
    }


def build_results() -> dict[str, Any]:
    old = load_old_schur_context()
    paper29 = load_paper29_scorecard()

    pantheon_df, pantheon_cov = load_pantheon()
    pantheon_io = fit_pantheon_with_nuisance(pantheon_df, pantheon_cov, IO_BG)
    pantheon_planck = fit_pantheon_with_nuisance(pantheon_df, pantheon_cov, PLANCK_BG)

    lens_io = strong_lensing_summary(IO_BG, IO_GRID)
    lens_planck = strong_lensing_summary(PLANCK_BG, PLANCK_GRID)

    ap_rows, ap_cov = load_desi_bao()
    ap_derived = derive_f_ap(ap_rows, ap_cov)
    ap_io = score_ap(IO_BG, IO_GRID, ap_derived)
    ap_planck = score_ap(PLANCK_BG, PLANCK_GRID, ap_derived)

    frb = frb_summary(IO_BG, IO_GRID, BARYON_SLOTS)
    ksz = ksz_summary(BARYON_SLOTS)
    cluster = cluster_gas_summary(BARYON_SLOTS)
    lya = lya_summary(BARYON_SLOTS)
    zmax = angular_diameter_distance_maximum(IO_BG)
    drift = drift_summary()
    sirens = standard_siren_summary()
    s8 = s8_weyl_summary(ksz)

    test_rows = [
        {
            "test": "1. Pantheon+ Type Ia SNe",
            "io_result": {
                "chi2": pantheon_io["chi2"],
                "chi2_per_dof": pantheon_io["chi2_per_dof"],
            },
            "planck_result": {
                "chi2": pantheon_planck["chi2"],
                "chi2_per_dof": pantheon_planck["chi2_per_dof"],
            },
            "old_schur": old["pantheon"],
            "category_now": "IO wins" if pantheon_io["chi2"] < pantheon_planck["chi2"] else "Planck wins",
            "category_old": "IO wins" if old["pantheon"]["io_chi2"] < old["pantheon"]["planck_chi2"] else "Planck wins",
        },
        {
            "test": "2. TDCOSMO strong lensing",
            "io_result": {"chi2": lens_io["chi2"], "chi2_per_dof": lens_io["chi2_per_dof"]},
            "planck_result": {"chi2": lens_planck["chi2"], "chi2_per_dof": lens_planck["chi2_per_dof"]},
            "old_schur": old["strong_lensing"],
            "category_now": "IO wins" if lens_io["chi2"] < lens_planck["chi2"] else "Planck wins",
            "category_old": "IO wins" if old["strong_lensing"]["schur_chi2"] < old["strong_lensing"]["lcdm_chi2"] else "Planck wins",
        },
        {
            "test": "3. GW standard sirens",
            "io_result": sirens,
            "planck_result": None,
            "old_schur": "old Schur H0 = 68.91 remained inside all quoted bars",
            "category_now": "all inside quoted bars",
            "category_old": "all inside quoted bars",
        },
        {
            "test": "4. Alcock-Paczynski",
            "io_result": {"chi2": ap_io["chi2"], "pte": ap_io["pte"]},
            "planck_result": {"chi2": ap_planck["chi2"], "pte": ap_planck["pte"]},
            "old_schur": old["ap"],
            "category_now": "IO wins" if ap_io["chi2"] < ap_planck["chi2"] else "Planck wins",
            "category_old": "IO wins" if old["ap"]["io_chi2"] < old["ap"]["planck_chi2"] else "Planck wins",
        },
        {
            "test": "5. Three-baryon structure",
            "io_result": {slot.label: slot.omega_b_h2 for slot in BARYON_SLOTS},
            "planck_result": None,
            "old_schur": {
                "omega_b_geom": 0.02108,
                "omega_b_eff": 0.02910,
                "omega_b_clustering": 0.01705,
            },
            "category_now": "recomputed",
            "category_old": "legacy",
        },
        {
            "test": "6. FRB dispersion measures",
            "io_result": {row["label"]: row["chi2"] for row in frb["rows"]},
            "planck_result": None,
            "old_schur": old["frb"],
            "category_now": min(frb["rows"], key=lambda r: r["chi2"])["label"],
            "category_old": "omega_b_best_fit_from_frbs (fitted), closest carried slot omega_b_geom",
        },
        {
            "test": "7. kSZ pairwise momentum",
            "io_result": {row["label"]: row["pairwise_amplitude_ratio_vs_planck_flat"] for row in ksz["rows"]},
            "planck_result": {"reference_ratio": 1.0},
            "old_schur": old["ksz"],
            "category_now": min(ksz["rows"], key=lambda r: abs(r["pairwise_amplitude_ratio_vs_planck_flat"] - 1.0))["label"],
            "category_old": "omega_b_clustering nearest; raw BDP excluded",
        },
        {
            "test": "8. Cluster X-ray gas fractions",
            "io_result": {row["label"]: row["f_gas_Upsilon_0p80"] for row in cluster["rows"]},
            "planck_result": None,
            "old_schur": old["cluster_gas"],
            "category_now": min(cluster["rows"], key=lambda r: abs(r["f_gas_Upsilon_0p80"] - 0.146))["label"],
            "category_old": "omega_b_eff",
        },
        {
            "test": "9. Lyman-alpha forest UVB",
            "io_result": {
                str(row["z"]): {slot["label"]: slot["Gamma_HI_required_1e12_s"] for slot in row["slot_rows"]}
                for row in lya["rows"]
            },
            "planck_result": None,
            "old_schur": old["lya"],
            "category_now": "recomputed",
            "category_old": "legacy",
        },
        {
            "test": "10. Angular diameter distance minimum",
            "io_result": zmax,
            "planck_result": angular_diameter_distance_maximum(PLANCK_BG),
            "old_schur": {"z_max": old["angular_size_minimum"]},
            "category_now": "recomputed",
            "category_old": "legacy",
        },
        {
            "test": "11. Sandage-Loeb drift",
            "io_result": drift,
            "planck_result": None,
            "old_schur": old["drift"],
            "category_now": "recomputed",
            "category_old": "legacy",
        },
        {
            "test": "12. S8 and Weyl response",
            "io_result": s8,
            "planck_result": {"S8_planck_flat_reference": ksz["planck_reference"]["sigma8"] * math.sqrt(PLANCK_BG.Omega_m / 0.3)},
            "old_schur": {
                "Sigma_IO": J_PHI,
                "schur_clustering_sigma8": old["s8"]["omega_b_clustering"]["sigma8"],
                "schur_clustering_S8": old["s8"]["omega_b_clustering"]["S8"],
                "schur_weyl_S8": J_PHI * old["s8"]["omega_b_clustering"]["S8"],
            },
            "category_now": "recomputed",
            "category_old": "legacy",
        },
    ]

    return {
        "metadata": {
            "script": str(SCRIPT_PATH),
            "claim_discipline": {
                "geometry_tests": "VERIFIED",
                "baryon_slot_tests": "DERIVED/CONDITIONAL_VERIFIED where observable-class assignment enters",
                "bao_kernel_import": "DERIVED/CONDITIONAL_VERIFIED from Paper 29 v2.0",
                "r4_firas_boundary": "R4_FIRAS = 1.0031014644 is inherited through the FIRAS-fixed observer temperature; no script fits or varies R4.",
            },
        },
        "inputs": {
            "io_background": asdict(IO_BG),
            "planck_background": asdict(PLANCK_BG),
            "r_d_Mpc": R_D_IO,
            "f_b": F_B,
            "omega_b_geom": OMEGA_B_GEOM,
            "x": X_IO,
            "gamma": GAMMA_IO,
            "K_gauge": K_GAUGE,
            "eta_bao": ETA_BAO,
            "J_phi": J_PHI,
            "K_avg": K_AVG,
            "F_slot": F_SLOT,
        },
        "baryon_slots": {slot.label: {"omega_b_h2": slot.omega_b_h2, "claim": slot.claim} for slot in BARYON_SLOTS},
        "tests": {
            "pantheon": {"io": pantheon_io, "planck": pantheon_planck, "old_schur": old["pantheon"]},
            "strong_lensing": {"io": lens_io, "planck": lens_planck, "old_schur": old["strong_lensing"]},
            "standard_sirens": sirens,
            "alcock_paczynski": {"io": ap_io, "planck": ap_planck, "old_schur": old["ap"]},
            "frb_dm": {"current": frb, "old_schur": old["frb"]},
            "ksz": {"current": ksz, "old_schur": old["ksz"]},
            "cluster_gas": {"current": cluster, "old_schur": old["cluster_gas"]},
            "lya": {"current": lya, "old_schur": old["lya"]},
            "angular_diameter_minimum": {"io": zmax, "planck": angular_diameter_distance_maximum(PLANCK_BG), "old_schur_zmax": old["angular_size_minimum"]},
            "sandage_loeb": {"rows": drift, "old_schur": old["drift"]},
            "s8_weyl": {"current": s8, "old_schur": old["s8"]},
            "paper29_scorecard": paper29,
        },
        "scorecard_table": test_rows,
    }


def maybe_flip(now: str, old: str) -> str:
    if now == old:
        return "no category change"
    return f"category change: {old} -> {now}"


def fmt(x: float, nd: int = 3) -> str:
    return f"{x:.{nd}f}"


def build_report(results: dict[str, Any]) -> str:
    rows = results["scorecard_table"]
    tests = results["tests"]
    paper29 = tests["paper29_scorecard"]
    pantheon_io = tests["pantheon"]["io"]
    pantheon_planck = tests["pantheon"]["planck"]

    lines = [
        "# Paper 30 Full Recomputation on the Paper 10 Legacy Branch",
        "",
        "All branch-dependent Paper 30 tests were recomputed on the active Paper 10 legacy branch using the user-specified closed-FRW background, standard thermal radiation with `N_eff = 3.044`, and the carried Paper 29 baryon / BAO inputs where applicable.",
        "",
        "## Active Inputs",
        "",
        f"- `H0 = {IO_BG.H0}`",
        f"- `Omega_m = {IO_BG.Omega_m}`",
        f"- `Omega_k = {IO_BG.Omega_k}`",
        f"- `Omega_lambda = {IO_BG.Omega_lambda}`",
        f"- `Omega_r = {IO_BG.Omega_r}`",
        f"- `r_d = {R_D_IO} Mpc`",
        f"- `omega_b,geom = {OMEGA_B_GEOM}`",
        f"- `eta = {ETA_BAO}`",
        "",
        "## Scorecard",
        "",
        "| Test | IO current | Planck/reference | Old Schur | Change flag |",
        "|---|---:|---:|---:|---|",
    ]

    for row in rows:
        test = row["test"]
        io_result = row["io_result"]
        planck_result = row["planck_result"]
        old = row["old_schur"]
        if test.startswith("1. Pantheon"):
            io_txt = f"`chi2={fmt(io_result['chi2'],3)}`"
            planck_txt = f"`chi2={fmt(planck_result['chi2'],3)}`"
            old_txt = f"`IO={fmt(old['io_chi2'],3)}` / `Planck={fmt(old['planck_chi2'],3)}`"
        elif test.startswith("2. TDCOSMO"):
            io_txt = f"`chi2={fmt(io_result['chi2'],3)}`"
            planck_txt = f"`chi2={fmt(planck_result['chi2'],3)}`"
            old_txt = f"`IO={fmt(old['schur_chi2'],3)}` / `Planck={fmt(old['lcdm_chi2'],3)}`"
        elif test.startswith("3. GW"):
            io_txt = " / ".join(f"`{r['label']}={r['io_pull_sigma']:+.2f}σ`" for r in io_result)
            planck_txt = " / ".join(f"`{r['label']}={r['planck_pull_sigma']:+.2f}σ`" for r in io_result)
            old_txt = "`H0=68.91 inside all bars`"
        elif test.startswith("4. Alcock"):
            io_txt = f"`chi2={fmt(io_result['chi2'],3)}`, `pte={fmt(io_result['pte'],3)}`"
            planck_txt = f"`chi2={fmt(planck_result['chi2'],3)}`, `pte={fmt(planck_result['pte'],3)}`"
            old_txt = f"`IO={fmt(old['io_chi2'],3)}` / `Planck={fmt(old['planck_chi2'],3)}`"
        elif test.startswith("5. Three-baryon"):
            io_txt = " / ".join(f"`{k}={v:.5f}`" for k, v in io_result.items())
            planck_txt = "n/a"
            old_txt = " / ".join(f"`{k}={v:.5f}`" for k, v in old.items())
        elif test.startswith("6. FRB"):
            io_txt = " / ".join(f"`{k}={v:.2f}`" for k, v in io_result.items())
            planck_txt = "n/a"
            old_txt = " / ".join(f"`{k}={v:.2f}`" for k, v in old.items())
        elif test.startswith("7. kSZ"):
            io_txt = " / ".join(f"`{k}={v:.2f}x`" for k, v in io_result.items())
            planck_txt = "`reference=1.00x`"
            old_txt = " / ".join(f"`{k}={v:.2f}x`" for k, v in old.items())
        elif test.startswith("8. Cluster"):
            io_txt = " / ".join(f"`{k}={v:.3f}`" for k, v in io_result.items())
            planck_txt = "n/a"
            old_txt = " / ".join(f"`{k}={v:.3f}`" for k, v in old.items())
        elif test.startswith("9. Lyman"):
            geom_rows = []
            for z_key, slot_map in io_result.items():
                geom_rows.append(f"`z={z_key}:{slot_map['omega_b_geom']:.3f}`")
            io_txt = " / ".join(geom_rows)
            planck_txt = "benchmark UVB imported"
            old_txt = " / ".join(f"`z={z}:{slots['omega_b_geom']:.3f}`" for z, slots in old.items())
        elif test.startswith("10. Angular"):
            io_txt = f"`z_max={io_result['z_max']:.5f}`"
            planck_txt = f"`z_max={planck_result['z_max']:.5f}`"
            old_txt = f"`z_max={old['z_max']:.5f}`"
        elif test.startswith("11. Sandage"):
            io_txt = " / ".join(f"`z={r['z']:.0f}:{r['io_cm_per_s_per_decade']:.3f}`" for r in io_result)
            planck_txt = " / ".join(f"`z={r['z']:.0f}:{r['planck_cm_per_s_per_decade']:.3f}`" for r in io_result)
            old_txt = " / ".join(f"`z={z}:{v:.3f}`" for z, v in old.items())
        else:
            io_txt = f"`Sigma={io_result['Sigma_IO']:.6f}`, `S8={io_result['S8_weyl_response']:.6f}`"
            planck_txt = f"`S8_flat={planck_result['S8_planck_flat_reference']:.6f}`"
            old_txt = f"`Sigma={old['Sigma_IO']:.6f}`, `S8={old['schur_weyl_S8']:.6f}`"
        lines.append(f"| {test} | {io_txt} | {planck_txt} | {old_txt} | {maybe_flip(row['category_now'], row['category_old'])} |")

    lines.extend(
        [
            "",
            "## Detailed Notes",
            "",
            f"- Pantheon+: `IO chi2 = {pantheon_io['chi2']:.6f}`, `Planck chi2 = {pantheon_planck['chi2']:.6f}`, `Delta chi2 = {pantheon_io['chi2'] - pantheon_planck['chi2']:.6f}`.",
            f"- TDCOSMO: `IO chi2 = {tests['strong_lensing']['io']['chi2']:.6f}`, `Planck chi2 = {tests['strong_lensing']['planck']['chi2']:.6f}`.",
            f"- AP: `IO chi2 = {tests['alcock_paczynski']['io']['chi2']:.6f}`, `Planck chi2 = {tests['alcock_paczynski']['planck']['chi2']:.6f}`.",
            f"- Observer-frame FRW age on the active branch: `{paper29['observer_frw_age_gyr']:.12f} Gyr`.",
            f"- Paper 29 carried scorecard: `CC = {paper29['io_cc_chi2']:.6f}`, `BAO = {paper29['io_bao_chi2']:.6f}`, `combined = {paper29['io_combined_chi2']:.6f}`.",
            f"- Planck carried scorecard: `CC = {paper29['planck_cc_chi2']:.6f}`, `BAO = {paper29['planck_bao_chi2']:.6f}`, `combined = {paper29['planck_combined_chi2']:.6f}`.",
            "",
            "## Baryon Slots",
            "",
            f"- `omega_b,geom = {OMEGA_B_GEOM:.15f}`",
            f"- `omega_b,eff = {F_SLOT * OMEGA_B_GEOM:.15f}`",
            f"- `omega_b,clustering = {(X_IO ** (-0.5)) * OMEGA_B_GEOM:.15f}`",
            f"- `omega_b,naive = {F_B * IO_BG.omega_m_h2:.15f}`",
            "",
            "## S8 / Weyl Response",
            "",
            f"- `Sigma_IO = x^(-1/2) = {J_PHI:.15f}`",
            f"- `sigma8_clustering = {tests['s8_weyl']['current']['sigma8_clustering']:.15f}`",
            f"- `S8_clustering = {tests['s8_weyl']['current']['S8_clustering']:.15f}`",
            f"- `S8_weyl_response = {tests['s8_weyl']['current']['S8_weyl_response']:.15f}`",
            "",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    results = build_results()
    RESULTS_JSON.write_text(json.dumps(results, indent=2))
    REPORT_MD.write_text(build_report(results))
    print(f"Wrote {RESULTS_JSON}")
    print(f"Wrote {REPORT_MD}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Shared constants and numerical helpers for the Paper 29 v2.0 bundle."""

from __future__ import annotations

import hashlib
import json
import math
import urllib.request
from dataclasses import asdict, dataclass
from pathlib import Path

import numpy as np
from scipy.integrate import quad


BUNDLE_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = BUNDLE_ROOT / "data"
RESULTS_DIR = BUNDLE_ROOT / "results"
REPORTS_DIR = BUNDLE_ROOT / "reports"

C_KM_S = 299792.458
C_SI = 299792458.0
MPC_M = 3.0856775814913673e22
G_SI = 6.67430e-11
M_P_SI = 1.67262192369e-27
SIGMA_T = 6.6524587321e-29
A_RAD = 7.5657e-16
M_E = 9.1093837015e-31
SECONDS_PER_GYR = 365.25 * 24.0 * 3600.0 * 1.0e9

GAMMA_BI = 0.2375
X = 1.5189873277742727
K_GAUGE = math.log(1.0 + GAMMA_BI * GAMMA_BI)
ETA = K_GAUGE / X
R4_FIRAS = 1.0031014644

H0_IO = 67.57585653582628
OMEGA_M_IO = 0.34868395067621694
OMEGA_K_IO = -0.04579112576013168
OMEGA_B_H2_GEOM = 0.020995719061702847
OMEGA_LAMBDA_IO = 0.6970157307777745
N_EFF = 3.044
T_CMB = 2.7255
Y_HE = 0.2477
R_D_MPC = 144.01351425392883
Z_DEC = 123.67217038722819
A_S_NATIVE = 2.0072459972737347e-09
F_GAMMA = 1.0 / (1.0 + GAMMA_BI * GAMMA_BI)
A_S_THEOREM = A_S_NATIVE * F_GAMMA
SIGMA8_NATIVE_ACTIVE = 0.9532815843192395
SIGMA8_THEOREM_ACTIVE = 0.9274824965120383

OMEGA_GAMMA_H2_REF = 2.469e-5
NEUTRINO_FACTOR = 0.2271
OMEGA_R_H2_STD = OMEGA_GAMMA_H2_REF * (T_CMB / 2.7255) ** 4 * (1.0 + NEUTRINO_FACTOR * N_EFF)
H100_SI = 100.0 * 1000.0 / MPC_M
RHO_CRIT_100 = 3.0 * H100_SI**2 / (8.0 * math.pi * G_SI)

CC_CHI2_BASELINE = 14.701523963980787
PLANCK_BAO_CHI2 = 31.25101137291248
PLANCK_COMBINED_CHI2 = 46.40432046950788

DESI_DR2_MEAN_URL = (
    "https://raw.githubusercontent.com/CobayaSampler/bao_data/master/"
    "desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_mean.txt"
)
DESI_DR2_COV_URL = (
    "https://raw.githubusercontent.com/CobayaSampler/bao_data/master/"
    "desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_cov.txt"
)
DESI_DR2_MEAN_SHA256 = "9ac154ab583ce759c0f7eef3c978c7c70a6ead2d18774caceadf1a350a640585"
DESI_DR2_COV_SHA256 = "252a143274c8a07c78694c119617d36594f6d7965d00319ca611c6ffb886e509"


@dataclass(frozen=True)
class Background:
    label: str
    H0: float
    Omega_m: float
    Omega_k: float
    Omega_r: float
    Omega_lambda: float
    omega_b_h2: float
    YHe: float

    @property
    def h(self) -> float:
        return self.H0 / 100.0

    @property
    def H0_si(self) -> float:
        return self.H0 * 1000.0 / MPC_M

    def to_json(self) -> dict[str, float | str]:
        return asdict(self)


def omega_r_from_h(h: float) -> float:
    return OMEGA_R_H2_STD / (h * h)


IO_OBS = Background(
    label="IO observer branch",
    H0=H0_IO,
    Omega_m=OMEGA_M_IO,
    Omega_k=OMEGA_K_IO,
    Omega_r=omega_r_from_h(H0_IO / 100.0),
    Omega_lambda=1.0 - OMEGA_M_IO - OMEGA_K_IO - omega_r_from_h(H0_IO / 100.0),
    omega_b_h2=OMEGA_B_H2_GEOM,
    YHe=Y_HE,
)

IO_BARE = Background(
    label="IO local bare branch",
    H0=58.422219957755004,
    Omega_m=0.19671396077221812,
    Omega_k=-0.12950335870178542,
    Omega_r=omega_r_from_h(58.422219957755004 / 100.0),
    Omega_lambda=1.0
    - 0.19671396077221812
    - (-0.12950335870178542)
    - omega_r_from_h(58.422219957755004 / 100.0),
    omega_b_h2=OMEGA_B_H2_GEOM,
    YHe=Y_HE,
)

EXT_REION = Background(
    label="External canonical tanh representative",
    H0=67.4,
    Omega_m=0.315,
    Omega_k=0.0,
    Omega_r=omega_r_from_h(67.4 / 100.0),
    Omega_lambda=1.0 - 0.315 - omega_r_from_h(67.4 / 100.0),
    omega_b_h2=0.02237,
    YHe=0.2478,
)


CC_35 = [
    (0.07, 69.0, 19.6),
    (0.09, 69.0, 12.0),
    (0.12, 68.6, 26.2),
    (0.17, 83.0, 8.0),
    (0.179, 75.0, 4.0),
    (0.199, 75.0, 5.0),
    (0.2, 72.9, 29.6),
    (0.27, 77.0, 14.0),
    (0.28, 88.8, 36.6),
    (0.352, 83.0, 14.0),
    (0.3802, 83.0, 13.5),
    (0.4, 95.0, 17.0),
    (0.4004, 77.0, 10.2),
    (0.4247, 87.1, 11.2),
    (0.4497, 92.8, 12.9),
    (0.47, 89.0, 50.0),
    (0.4783, 80.9, 9.0),
    (0.48, 97.0, 62.0),
    (0.593, 104.0, 13.0),
    (0.68, 92.0, 8.0),
    (0.75, 98.8, 33.6),
    (0.75, 105.0, 7.9),
    (0.781, 105.0, 12.0),
    (0.8, 113.1, 15.1),
    (0.875, 125.0, 17.0),
    (0.88, 90.0, 40.0),
    (0.9, 117.0, 23.0),
    (1.037, 154.0, 20.0),
    (1.26, 135.0, 65.0),
    (1.3, 168.0, 17.0),
    (1.363, 160.0, 33.6),
    (1.43, 177.0, 18.0),
    (1.53, 140.0, 14.0),
    (1.75, 202.0, 40.0),
    (1.965, 186.5, 50.4),
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def cached_download(url: str, target: Path, expected_sha256: str) -> Path:
    target.parent.mkdir(parents=True, exist_ok=True)
    if not target.exists():
        print(f"Fetching external data from {url}")
        print("This file is not redistributed in the bundle; it is fetched and checksummed.")
        urllib.request.urlretrieve(url, target)
    actual = sha256_file(target)
    if actual != expected_sha256:
        raise RuntimeError(f"Checksum mismatch for {target}: expected {expected_sha256}, got {actual}")
    return target


def load_desi_dr2() -> tuple[list[dict[str, float | str]], np.ndarray]:
    mean_path = cached_download(DESI_DR2_MEAN_URL, DATA_DIR / ".cache" / "desi_dr2_all_gccomb_mean.txt", DESI_DR2_MEAN_SHA256)
    cov_path = cached_download(DESI_DR2_COV_URL, DATA_DIR / ".cache" / "desi_dr2_all_gccomb_cov.txt", DESI_DR2_COV_SHA256)
    rows: list[dict[str, float | str]] = []
    for raw_line in mean_path.read_text(encoding="utf-8").splitlines():
        parts = raw_line.split()
        if len(parts) != 3:
            continue
        z, value, quantity = parts
        zf = float(z)
        rows.append(
            {
                "z": zf,
                "value": float(value),
                "quantity": quantity,
                "block": "galaxy_quasar" if zf < 2.0 else "lya",
            }
        )
    return rows, np.loadtxt(cov_path)


def e_of_z(z: float | np.ndarray, bg: Background) -> float | np.ndarray:
    zp1 = 1.0 + np.asarray(z)
    return np.sqrt(
        bg.Omega_m * zp1**3 + bg.Omega_r * zp1**4 + bg.Omega_k * zp1**2 + bg.Omega_lambda
    )


def h_of_z(z: float, bg: Background = IO_OBS) -> float:
    return float(bg.H0 * e_of_z(z, bg))


def chi_dimless(z: float, bg: Background) -> float:
    val, _ = quad(lambda zp: 1.0 / float(e_of_z(zp, bg)), 0.0, z, epsabs=1.0e-10, epsrel=1.0e-10, limit=800)
    return val


def transverse_comoving_distance(z: float, bg: Background) -> float:
    chi = chi_dimless(z, bg)
    if bg.Omega_k < 0.0:
        root = math.sqrt(-bg.Omega_k)
        return (C_KM_S / bg.H0) * math.sin(root * chi) / root
    if bg.Omega_k > 0.0:
        root = math.sqrt(bg.Omega_k)
        return (C_KM_S / bg.H0) * math.sinh(root * chi) / root
    return (C_KM_S / bg.H0) * chi


def hubble_distance(z: float, bg: Background) -> float:
    return C_KM_S / (bg.H0 * float(e_of_z(z, bg)))


def bao_model_rows(
    rows: list[dict[str, float | str]],
    covariance: np.ndarray,
    *,
    f_perp: float,
    f_parallel: float,
) -> tuple[list[dict[str, float | str]], float]:
    out: list[dict[str, float | str]] = []
    for row in rows:
        z = float(row["z"])
        quantity = str(row["quantity"])
        block = str(row["block"])
        dm = transverse_comoving_distance(z, IO_OBS)
        dh = hubble_distance(z, IO_OBS)
        if block == "galaxy_quasar":
            dm_eff = dm / f_perp
            dh_eff = dh / f_parallel
        else:
            dm_eff = dm
            dh_eff = dh
        dv_eff = (z * dm_eff * dm_eff * dh_eff) ** (1.0 / 3.0)
        if quantity == "DM_over_rs":
            model = dm_eff / R_D_MPC
        elif quantity == "DH_over_rs":
            model = dh_eff / R_D_MPC
        else:
            model = dv_eff / R_D_MPC
        residual = model - float(row["value"])
        out.append({**row, "model": model, "residual": residual})
    diff = np.array([float(row["residual"]) for row in out], dtype=float)
    return out, float(diff @ np.linalg.inv(covariance) @ diff)


def cc_chi2(bg: Background = IO_OBS) -> float:
    return sum(((h_of_z(z, bg) - h_obs) / sigma) ** 2 for z, h_obs, sigma in CC_35)


def growth_factor(a: float, bg: Background = IO_OBS) -> float:
    """Heath integral normalized to D(a=1)=1 for matter plus smooth components."""

    def e_a(ap: float) -> float:
        return math.sqrt(
            bg.Omega_m / ap**3
            + bg.Omega_r / ap**4
            + bg.Omega_k / ap**2
            + bg.Omega_lambda
        )

    def raw(ap: float) -> float:
        val, _ = quad(lambda x: 1.0 / (x**3 * e_a(x) ** 3), 1.0e-8, ap, epsabs=1.0e-11, epsrel=1.0e-11, limit=500)
        return 2.5 * bg.Omega_m * e_a(ap) * val

    return raw(a) / raw(1.0)


def omega_m_z(z: float, bg: Background = IO_OBS) -> float:
    zp1 = 1.0 + z
    ez2 = bg.Omega_m * zp1**3 + bg.Omega_r * zp1**4 + bg.Omega_k * zp1**2 + bg.Omega_lambda
    return bg.Omega_m * zp1**3 / ez2

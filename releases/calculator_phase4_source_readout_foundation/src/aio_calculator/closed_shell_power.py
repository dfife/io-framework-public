"""Exact closed-`S^3` shell-power definitions for the Phase 4 readout stack.

This module closes only the observer-side shell geometry and covariance
conventions that are already fixed on compact `S^3`:

- `derived / scoped`: shell degeneracy `D_n = (n+1)^2`
- `derived / scoped`: shell variance prefactor `D_n / (2 pi^2 R^3)`
- `derived / scoped`: exact shell variables
  `q_n = (n+1)/R`, `k_scalar = sqrt(n(n+2))/R`,
  `k_MS = sqrt((n-1)(n+3))/R`
- `derived / scoped`: dimensionless shell prefactors for `Delta_q^2`,
  `Delta_scalar^2`, and `Delta_MS^2`

What this module does not do:

- derive the physical IO source-side shell covariance law
- hide a flat-space `k^3` convention as if it were primitive on `S^3`
- backfill the missing `S^2 -> S^3` bridge typing
"""

from __future__ import annotations

import math
from dataclasses import dataclass


def _validate_radius(radius: float) -> float:
    """Require a positive `S^3` radius."""

    radius = float(radius)
    if not math.isfinite(radius) or radius <= 0.0:
        raise ValueError("radius must be positive and finite")
    return radius


def _validate_shell(n: int) -> int:
    """Require a non-negative scalar shell label."""

    n = int(n)
    if n < 0:
        raise ValueError("n must satisfy n >= 0")
    return n


def _validate_physical_scalar_shell(n: int) -> int:
    """Require a physical scalar shell for the Mukhanov-Sasaki variable."""

    n = _validate_shell(n)
    if n < 2:
        raise ValueError("physical scalar-shell formulas require n >= 2")
    return n


@dataclass(frozen=True)
class ClosedShellPowerSupport:
    """One exact observer-side shell package on closed `S^3`."""

    n: int
    radius: float
    shell_degeneracy: int
    shell_variance_prefactor: float
    q_shell: float
    scalar_shell: float
    ms_shell: float | None
    delta_q_prefactor: float
    delta_scalar_prefactor: float
    delta_ms_prefactor: float | None
    claim_status: str
    provenance_node_ids: tuple[str, ...]
    scope_boundary: tuple[str, ...]


def s3_shell_degeneracy(n: int) -> int:
    """Return the scalar shell degeneracy `D_n = (n+1)^2`."""

    n = _validate_shell(n)
    return (n + 1) ** 2


def s3_volume(radius: float) -> float:
    """Return the `S^3` volume `Vol(S^3_R) = 2 pi^2 R^3`."""

    radius = _validate_radius(radius)
    return 2.0 * math.pi * math.pi * radius**3


def q_shell_wavenumber(n: int, *, radius: float) -> float:
    """Return the closed-universe shell variable `q_n = (n+1) / R`."""

    n = _validate_shell(n)
    radius = _validate_radius(radius)
    return (n + 1.0) / radius


def scalar_shell_wavenumber(n: int, *, radius: float) -> float:
    """Return `k_scalar(n) = sqrt(n(n+2)) / R`."""

    n = _validate_shell(n)
    radius = _validate_radius(radius)
    return math.sqrt(n * (n + 2.0)) / radius


def ms_shell_wavenumber(n: int, *, radius: float) -> float:
    """Return `k_MS(n) = sqrt((n-1)(n+3)) / R` for physical scalar shells."""

    n = _validate_physical_scalar_shell(n)
    radius = _validate_radius(radius)
    return math.sqrt((n - 1.0) * (n + 3.0)) / radius


def shell_variance_prefactor(n: int, *, radius: float) -> float:
    """Return `((n+1)^2 / (2 pi^2 R^3))`."""

    return s3_shell_degeneracy(n) / s3_volume(radius)


def delta_q_prefactor(n: int, *, radius: float) -> float:
    """Return `((n+1)^3 / (2 pi^2 R^3))`."""

    n = _validate_shell(n)
    radius = _validate_radius(radius)
    return (n + 1.0) ** 3 / s3_volume(radius)


def delta_scalar_prefactor(n: int, *, radius: float) -> float:
    """Return `(n(n+1)(n+2) / (2 pi^2 R^3))`."""

    n = _validate_shell(n)
    radius = _validate_radius(radius)
    return n * (n + 1.0) * (n + 2.0) / s3_volume(radius)


def delta_ms_prefactor(n: int, *, radius: float) -> float:
    """Return `((n-1)(n+1)(n+3) / (2 pi^2 R^3))` for physical scalar shells."""

    n = _validate_physical_scalar_shell(n)
    radius = _validate_radius(radius)
    return (n - 1.0) * (n + 1.0) * (n + 3.0) / s3_volume(radius)


def covariance_from_delta_q(delta_q_sq: float, n: int, *, radius: float) -> float:
    """Invert `Delta_q^2(n) = ((n+1)^3 / (2 pi^2 R^3)) P_X(n)`."""

    delta_q_sq = float(delta_q_sq)
    if not math.isfinite(delta_q_sq):
        raise ValueError("delta_q_sq must be finite")
    return delta_q_sq / delta_q_prefactor(n, radius=radius)


def covariance_from_delta_scalar(delta_scalar_sq: float, n: int, *, radius: float) -> float:
    """Invert `Delta_scalar^2(n) = prefactor * P_X(n)`."""

    delta_scalar_sq = float(delta_scalar_sq)
    if not math.isfinite(delta_scalar_sq):
        raise ValueError("delta_scalar_sq must be finite")
    return delta_scalar_sq / delta_scalar_prefactor(n, radius=radius)


def covariance_from_delta_ms(delta_ms_sq: float, n: int, *, radius: float) -> float:
    """Invert `Delta_MS^2(n) = prefactor * P_X(n)` on physical scalar shells."""

    delta_ms_sq = float(delta_ms_sq)
    if not math.isfinite(delta_ms_sq):
        raise ValueError("delta_ms_sq must be finite")
    return delta_ms_sq / delta_ms_prefactor(n, radius=radius)


def closed_shell_power_support(n: int, *, radius: float) -> ClosedShellPowerSupport:
    """Package one theorem-grade closed-shell power object."""

    n = _validate_shell(n)
    radius = _validate_radius(radius)
    ms_shell = None if n < 2 else ms_shell_wavenumber(n, radius=radius)
    ms_prefactor = None if n < 2 else delta_ms_prefactor(n, radius=radius)
    return ClosedShellPowerSupport(
        n=n,
        radius=radius,
        shell_degeneracy=s3_shell_degeneracy(n),
        shell_variance_prefactor=shell_variance_prefactor(n, radius=radius),
        q_shell=q_shell_wavenumber(n, radius=radius),
        scalar_shell=scalar_shell_wavenumber(n, radius=radius),
        ms_shell=ms_shell,
        delta_q_prefactor=delta_q_prefactor(n, radius=radius),
        delta_scalar_prefactor=delta_scalar_prefactor(n, radius=radius),
        delta_ms_prefactor=ms_prefactor,
        claim_status="derived / scoped",
        provenance_node_ids=("paper28.closed_s3_shell_power",),
        scope_boundary=(
            "Observer-side closed-S^3 shell definitions only.",
            "Does not by itself derive the physical IO source-side shell covariance law or the missing bridge typing.",
        ),
    )


__all__ = [
    "ClosedShellPowerSupport",
    "closed_shell_power_support",
    "covariance_from_delta_ms",
    "covariance_from_delta_q",
    "covariance_from_delta_scalar",
    "delta_ms_prefactor",
    "delta_q_prefactor",
    "delta_scalar_prefactor",
    "ms_shell_wavenumber",
    "q_shell_wavenumber",
    "s3_shell_degeneracy",
    "s3_volume",
    "scalar_shell_wavenumber",
    "shell_variance_prefactor",
]

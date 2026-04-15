"""Coupled Thomson-history tuple contract for the Phase 3 perturbation block.

Paper 37 fixes the surviving Thomson carrier more sharply than "change
`dkappa` somewhere." The exact closure, if it exists, must act on the coupled
tuple

`(thomson_drag_rate, thomson_hierarchy_rate, tau_c, dtau_c, slip, shear)`.

This module implements that contract and nothing stronger. It does not invent
the final IO-native operator on the tuple; it keeps that seam explicit.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Any, Protocol

from .recombination import OpenTheoremBoundaryError


def _float_tuple(values: tuple[float, ...] | list[float], *, name: str) -> tuple[float, ...]:
    """Validate a finite tuple of Thomson-history values."""

    coerced = tuple(float(value) for value in values)
    if not coerced:
        raise ValueError(f"{name} must not be empty")
    if any(not math.isfinite(value) for value in coerced):
        raise ValueError(f"{name} must contain only finite values")
    return coerced


@dataclass(frozen=True)
class ThomsonHistorySample:
    """One sample of the Paper 37 coupled Thomson-history tuple."""

    z_obs: float
    thomson_drag_rate: float
    thomson_hierarchy_rate: float
    tau_c: float
    dtau_c: float
    slip: float
    shear: float


@dataclass(frozen=True)
class ThomsonHistoryContract:
    """A typed sampled carrier for the coupled Thomson-history tuple."""

    z_obs: tuple[float, ...]
    thomson_drag_rate: tuple[float, ...]
    thomson_hierarchy_rate: tuple[float, ...]
    drag_rate_derivative: tuple[float, ...]
    tau_c: tuple[float, ...]
    dtau_c: tuple[float, ...]
    slip: tuple[float, ...]
    shear: tuple[float, ...]
    derivative_coordinate: str
    claim_status: str
    provenance_node_ids: tuple[str, ...]
    scope_boundary: tuple[str, ...]

    def __post_init__(self) -> None:
        size = len(self.z_obs)
        if size < 1:
            raise ValueError("z_obs must not be empty")
        vectors = (
            self.thomson_drag_rate,
            self.thomson_hierarchy_rate,
            self.drag_rate_derivative,
            self.tau_c,
            self.dtau_c,
            self.slip,
            self.shear,
        )
        if any(len(values) != size for values in vectors):
            raise ValueError("all Thomson-history vectors must match z_obs length")
        if any(z < 0.0 for z in self.z_obs):
            raise ValueError("z_obs values must be non-negative")
        if any(b <= a for a, b in zip(self.z_obs, self.z_obs[1:])):
            raise ValueError("z_obs must be strictly increasing")
        if any(rate <= 0.0 for rate in self.thomson_drag_rate):
            raise ValueError("thomson_drag_rate must stay strictly positive")
        if any(rate <= 0.0 for rate in self.thomson_hierarchy_rate):
            raise ValueError("thomson_hierarchy_rate must stay strictly positive")

    def sample(self, index: int) -> ThomsonHistorySample:
        """Return one sampled tuple entry."""

        return ThomsonHistorySample(
            z_obs=self.z_obs[index],
            thomson_drag_rate=self.thomson_drag_rate[index],
            thomson_hierarchy_rate=self.thomson_hierarchy_rate[index],
            tau_c=self.tau_c[index],
            dtau_c=self.dtau_c[index],
            slip=self.slip[index],
            shear=self.shear[index],
        )


class CoupledThomsonHistoryOperator(Protocol):
    """Protocol for a future exact operator acting on the Thomson-history tuple."""

    def apply(self, contract: ThomsonHistoryContract, **kwargs: Any) -> Any:
        """Apply the exact IO-native operator on the coupled Thomson-history tuple."""


def build_thomson_history_contract(
    z_obs: tuple[float, ...] | list[float],
    thomson_drag_rate: tuple[float, ...] | list[float],
    thomson_hierarchy_rate: tuple[float, ...] | list[float],
    drag_rate_derivative: tuple[float, ...] | list[float],
    slip: tuple[float, ...] | list[float],
    shear: tuple[float, ...] | list[float],
    *,
    derivative_coordinate: str = "local_time",
) -> ThomsonHistoryContract:
    """Build the sampled Paper 37 Thomson tuple from supplied rates.

    The theorem-grade part here is the carrier relation itself:

    - `tau_c = 1 / thomson_drag_rate`
    - `dtau_c = - d(thomson_drag_rate) * tau_c^2`

    The function does not infer the drag or hierarchy rates; callers must supply
    them from whatever later theorem-grade operator eventually closes that seam.
    """

    z_obs_t = _float_tuple(z_obs, name="z_obs")
    drag_t = _float_tuple(thomson_drag_rate, name="thomson_drag_rate")
    hierarchy_t = _float_tuple(thomson_hierarchy_rate, name="thomson_hierarchy_rate")
    derivative_t = _float_tuple(drag_rate_derivative, name="drag_rate_derivative")
    slip_t = _float_tuple(slip, name="slip")
    shear_t = _float_tuple(shear, name="shear")
    if any(rate <= 0.0 for rate in drag_t):
        raise ValueError("thomson_drag_rate must stay strictly positive")
    if any(rate <= 0.0 for rate in hierarchy_t):
        raise ValueError("thomson_hierarchy_rate must stay strictly positive")
    tau_c = tuple(1.0 / rate for rate in drag_t)
    dtau_c = tuple(-derivative * tau * tau for derivative, tau in zip(derivative_t, tau_c))
    return ThomsonHistoryContract(
        z_obs=z_obs_t,
        thomson_drag_rate=drag_t,
        thomson_hierarchy_rate=hierarchy_t,
        drag_rate_derivative=derivative_t,
        tau_c=tau_c,
        dtau_c=dtau_c,
        slip=slip_t,
        shear=shear_t,
        derivative_coordinate=str(derivative_coordinate),
        claim_status="derived / scoped",
        provenance_node_ids=("paper37.thomson_history_realization",),
        scope_boundary=(
            "This is the coupled Thomson-history carrier only.",
            "The exact IO-native operator acting on this tuple remains open.",
        ),
    )


class OpenCoupledThomsonHistoryOperator:
    """Explicit placeholder for the still-open Paper 37 Thomson operator."""

    def apply(self, contract: ThomsonHistoryContract, **kwargs: Any) -> Any:
        """Fail honestly until the exact tuple-level operator is derived."""

        raise OpenTheoremBoundaryError(
            "The coupled Thomson-history tuple is explicit, but the exact IO-native "
            "operator acting on `(thomson_drag_rate, thomson_hierarchy_rate, tau_c, "
            "dtau_c, slip, shear)` remains open."
        )

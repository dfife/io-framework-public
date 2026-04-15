"""Checks for the coupled Thomson-history tuple contract."""

from __future__ import annotations

import math
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from aio_calculator.recombination import OpenTheoremBoundaryError  # noqa: E402
from aio_calculator.thomson_history_contract import (  # noqa: E402
    OpenCoupledThomsonHistoryOperator,
    build_thomson_history_contract,
)


def test_thomson_history_contract_builds_tau_c_and_dtau_c_from_drag_rate() -> None:
    """The Paper 37 tuple formulas should be reproduced exactly."""

    contract = build_thomson_history_contract(
        [900.0, 1100.0],
        [10.0, 20.0],
        [11.0, 21.0],
        [-2.0, -4.0],
        [1.0e-5, 2.0e-5],
        [3.0e-5, 4.0e-5],
    )
    assert contract.claim_status == "derived / scoped"
    assert contract.provenance_node_ids == ("paper37.thomson_history_realization",)
    assert math.isclose(contract.tau_c[0], 0.1, rel_tol=0.0, abs_tol=1.0e-15)
    assert math.isclose(contract.tau_c[1], 0.05, rel_tol=0.0, abs_tol=1.0e-15)
    assert math.isclose(contract.dtau_c[0], 0.02, rel_tol=0.0, abs_tol=1.0e-15)
    assert math.isclose(contract.dtau_c[1], 0.01, rel_tol=0.0, abs_tol=1.0e-15)
    sample = contract.sample(1)
    assert math.isclose(sample.tau_c, 0.05, rel_tol=0.0, abs_tol=1.0e-15)
    assert math.isclose(sample.shear, 4.0e-5, rel_tol=0.0, abs_tol=1.0e-15)


def test_thomson_history_contract_rejects_nonpositive_drag_rates() -> None:
    """The tight-coupling time should stay well-defined on every sample."""

    with pytest.raises(ValueError):
        build_thomson_history_contract(
            [900.0],
            [0.0],
            [1.0],
            [0.0],
            [0.0],
            [0.0],
        )


def test_open_thomson_history_operator_refuses_to_fake_the_tuple_law() -> None:
    """The exact tuple-level operator should fail honestly until it is derived."""

    contract = build_thomson_history_contract(
        [900.0],
        [10.0],
        [11.0],
        [-2.0],
        [1.0e-5],
        [3.0e-5],
    )
    with pytest.raises(OpenTheoremBoundaryError):
        OpenCoupledThomsonHistoryOperator().apply(contract)

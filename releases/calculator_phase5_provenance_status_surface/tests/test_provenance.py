"""Checks for the theorem dictionary and explained-output layer."""

from __future__ import annotations

import json
import math
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path("/opt/cosmology-lab/calculator")
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from aio_calculator import (  # noqa: E402
    explain_active_branch_theta_star,
    explain_branch_rd_mpc,
    explain_eta_io_late,
    explain_background_snapshot,
    explain_recombination_point,
    explained_output_specs,
    theorem_graph,
)


def test_theta_star_explained_output_carries_full_chain() -> None:
    """The first explained output should ship the accepted theta_* theorem chain."""

    explained = explain_active_branch_theta_star().as_dict()
    assert explained["claim_status"].startswith("derived / scoped")
    assert explained["provenance_status"] == "full"
    assert explained["zero_fitted_parameters"] is True
    assert explained["conditional_on_premises"] == ["premise.1", "premise.2"]
    assert math.isclose(
        explained["theta_star_100"],
        1.048683904878751,
        rel_tol=0.0,
        abs_tol=1.0e-12,
    )
    assert explained["provenance"]["root_node"] == "paper37.active_branch_theta_star"
    assert explained["provenance"]["chain_ids"] == [
        "premise.1",
        "premise.2",
        "paper21.branch_assignment",
        "paper36.phase_equivalent_selector",
        "paper37.packet_coefficient_fixing",
        "paper37.highz_tail_slaving",
        "paper37.peak_window_tail_profile_audit",
        "paper37.selector_support_promotion",
        "paper37.active_branch_theta_star",
    ]
    theta_node = explained["provenance"]["nodes"]["paper37.active_branch_theta_star"]
    assert theta_node["label"] == "Active-branch Theta-star Theorem"
    assert theta_node["premises"] == [
        "`paper37.selector_support_promotion` fixes the carried physical selector leaf on the active branch.",
        "`paper36.phase_equivalent_selector` gives the exact observer-side map from that leaf to `theta_*`.",
    ]
    assert len(theta_node["proof_outline"]) == 3
    assert theta_node["scope_boundary"][0] == "Fixed active Paper 10 legacy projected branch only."
    assert theta_node["reference_note"].startswith("Supporting references only.")
    assert "`100theta_* = 1.048683904879`" in theta_node["statement"]
    comparison = explained["direct_observable_comparison"]
    assert math.isclose(
        comparison["predicted_value"],
        220.47514473507064,
        rel_tol=0.0,
        abs_tol=1.0e-12,
    )
    assert math.isclose(
        comparison["observed_reference"],
        220.0,
        rel_tol=0.0,
        abs_tol=1.0e-12,
    )
    assert "Planck assumes flat space" in explained["geometry_explanation"]


def test_recombination_explained_output_becomes_conditional_with_override() -> None:
    """Supplying `x_e` should change the chemistry-dependent rows to conditional."""

    explained = explain_recombination_point(1100.0, x_e_override=0.1).as_dict()
    assert explained["claim_status"].startswith("conditional")
    assert explained["provenance_status"] == "full"
    assert explained["zero_fitted_parameters"] is False
    assert explained["provenance"]["chain_ids"] == [
        "premise.1",
        "premise.2",
        "paper21.branch_assignment",
        "paper31.baryon_assignment",
        "paper29.sound_speed_selector",
        "paper31.local_background_state_map",
        "paper31.recombination_clock_transport",
    ]


def test_branch_rd_explained_output_carries_full_chain() -> None:
    """The active-branch `r_d` output should ship a full theorem chain."""

    explained = explain_branch_rd_mpc().as_dict()
    assert explained["provenance_status"] == "full"
    assert math.isclose(
        explained["r_d_mpc"],
        144.01351425392883,
        rel_tol=0.0,
        abs_tol=1.0e-12,
    )
    assert explained["provenance"]["chain_ids"] == [
        "premise.1",
        "premise.2",
        "paper21.branch_assignment",
        "paper29.sound_speed_selector",
        "paper31.geometric_pre_drag_ruler",
    ]
    selector = explained["provenance"]["nodes"]["paper29.sound_speed_selector"]
    assert "`R(z) = 3 rho_b(z) / [4 rho_gamma(z)]`" in selector["statement"]
    assert "omega_b,geom" in selector["statement"]


def test_eta_io_explained_output_carries_full_chain() -> None:
    """The late-time `eta_IO` output should ship a full theorem chain."""

    explained = explain_eta_io_late().as_dict()
    assert explained["provenance_status"] == "full"
    assert math.isclose(
        explained["eta_IO_late"],
        5.748778515173696e-10,
        rel_tol=0.0,
        abs_tol=1.0e-22,
    )
    assert explained["provenance"]["chain_ids"] == [
        "premise.1",
        "premise.2",
        "paper21.branch_assignment",
        "paper35.late_baryon_counting_law",
        "paper35.eta_io_late_closure",
    ]
    baryon_law = explained["provenance"]["nodes"]["paper35.late_baryon_counting_law"]
    assert baryon_law["authority_paths"] == []
    assert "`n_b = rho_b / m_bar" in baryon_law["statement"]
    closure = explained["provenance"]["nodes"]["paper35.eta_io_late_closure"]
    assert closure["label"] == "Late-time eta_IO Closure Theorem"
    assert "`eta_IO,late = C_eta(T_obs, m_bar) * omega_b,geom`" in closure["statement"]


def test_background_snapshot_explained_output_carries_full_chain() -> None:
    """The parameterized background snapshot should ship a full theorem chain."""

    explained = explain_background_snapshot(0.57).as_dict()
    assert explained["provenance_status"] == "full"
    assert math.isclose(
        explained["DM_mpc"],
        2165.6006007820824,
        rel_tol=0.0,
        abs_tol=1.0e-9,
    )
    assert explained["provenance"]["chain_ids"] == [
        "premise.1",
        "premise.2",
        "paper21.branch_assignment",
        "paper30.background_surface",
        "paper29.sound_speed_selector",
        "paper31.geometric_pre_drag_ruler",
    ]
    background = explained["provenance"]["nodes"]["paper30.background_surface"]
    assert "`H(z) = H_0 sqrt[Omega_r (1+z)^4 + Omega_m (1+z)^3 + Omega_k (1+z)^2 + Omega_Lambda]`" in background["statement"]
    assert explained["notes"][1].startswith("The BAO ratios")


def test_recombination_explained_output_carries_full_chain() -> None:
    """The default recombination primitives should ship a full theorem chain."""

    explained = explain_recombination_point(1100.0).as_dict()
    assert explained["provenance_status"] == "full"
    assert explained["provenance"]["chain_ids"] == [
        "premise.1",
        "premise.2",
        "paper21.branch_assignment",
        "paper31.baryon_assignment",
        "paper29.sound_speed_selector",
        "paper31.local_background_state_map",
        "local.saha_seed",
        "paper31.recombination_clock_transport",
    ]
    saha = explained["provenance"]["nodes"]["local.saha_seed"]
    assert saha["authority_paths"] == []
    assert "`x_e^2/(1-x_e) =" in saha["statement"]
    baryon = explained["provenance"]["nodes"]["paper31.baryon_assignment"]
    assert "`kappa'_loc = a_loc n_e sigma_T`" in baryon["statement"]


def test_provenance_specs_and_graph_expose_theta_and_scaffolds() -> None:
    """The theorem dictionary should expose full published outputs and theorem nodes."""

    specs = explained_output_specs()
    graph = theorem_graph()
    assert specs["theta_star_theorem"]["provenance_status"] == "full"
    assert specs["branch_rd_mpc"]["provenance_status"] == "full"
    assert specs["eta_io_late"]["provenance_status"] == "full"
    assert specs["background_snapshot"]["provenance_status"] == "full"
    assert specs["recombination_point"]["provenance_status"] == "full"
    assert "paper37.active_branch_theta_star" in graph
    assert graph["paper32.closed_s3_solver_spec"].claim_status.startswith("derived / scoped")
    assert graph["paper32.typed_baryon_slot_spec"].statement.endswith(
        "No silent one-slot collapse on `R` is licensed anywhere in the perturbation pipeline."
    )
    assert graph["premise.1"].scope_boundary[0].startswith("Applies only as a lab working assumption")
    assert len(graph["paper36.phase_equivalent_selector"].proof_outline) == 3
    assert graph["paper36.phase_equivalent_selector"].label == "Phase-equivalent Selector Theorem"
    assert "`theta_bare(z_sel) = r_s(z_sel) / D_M(z_sel)`" in graph["paper36.phase_equivalent_selector"].statement
    assert graph["paper37.packet_coefficient_fixing"].label == "Packet Coefficient Fixing Theorem"
    assert "`xr[1] = 3 x1s Dfplus_Ly[0]`" in graph["paper37.packet_coefficient_fixing"].statement
    assert graph["paper37.highz_tail_slaving"].label == "High-z Tail Slaving Theorem"
    assert graph["paper35.late_baryon_counting_law"].authority_paths == ()
    assert graph["paper31.local_background_state_map"].premises[1].startswith(
        "`paper31.baryon_assignment`"
    )
    assert graph["paper22.spatial_mode_ladder"].label == "Paper 22 Spatial Mode Ladder"
    assert "`lambda_n^(S) = n(n+2) / a^2`" in graph["paper22.spatial_mode_ladder"].statement
    assert graph["paper23.closed_scalar_operator"].label == "Paper 23 Closed Scalar Operator Theorem"
    assert "`lambda_n - 3 = (n-1)(n+3)`" in graph["paper23.closed_scalar_operator"].statement
    assert graph["paper28.closed_s3_shell_power"].label == "Paper 28 Closed S^3 Shell-power Definition"
    assert "`Delta_MS^2(n) = (((n-1)(n+1)(n+3)) / (2 pi^2 R^3)) P_X(n)`" in graph[
        "paper28.closed_s3_shell_power"
    ].statement
    assert graph["paper32.modular_dtn_field_transfer"].label == "Paper 32 Modular-DtN Field Transfer"
    assert "`P_src = B_+ o U_coex o T_field`" in graph["paper32.modular_dtn_field_transfer"].statement
    assert graph["paper32.typed_baryon_slot_spec"].label == "Typed Baryon-slot Specification"
    assert "reduced visibility/readout `omega_b,eff`" in graph["paper32.typed_baryon_slot_spec"].statement
    assert graph["paper31.stage2_markov_state"].label == "Paper 31 Stage-2 Markov State"
    assert "`Y_rec = (x_e, T_m, D_-(q;z), L_-(z))`" in graph["paper31.stage2_markov_state"].statement
    assert (
        graph["local.inherited_full_stage2_dynamic_history_builder"].label
        == "Inherited FULL Stage-2 Dynamic-history Builder Theorem"
    )
    assert "`H_loc(z) = (c / R_S) sqrt((1-u)/u^3)`" in graph[
        "local.inherited_full_stage2_dynamic_history_builder"
    ].statement
    assert "`D_-(q;z) = interp_Dfnu(lna_0, dlna, Dfminus_hist(q;.), N_z, -ln(1+z))`" in graph[
        "local.inherited_full_stage2_dynamic_history_builder"
    ].statement
    assert graph["paper37.thomson_history_realization"].label == "Thomson-history Realization Theorem"
    assert "`tau_c = 1 / thomson_drag_rate`" in graph["paper37.thomson_history_realization"].statement
    assert graph["local.closed_scalar_metric_state_builder"].label == "Closed Scalar Metric-state Builder Theorem"
    assert graph["local.closed_scalar_metric_state_builder"].claim_status == "derived / scoped as maps"
    assert "`psi = phi - 4.5 (a^2 / k_n^2) rho_plus_p_shear`" in graph[
        "local.closed_scalar_metric_state_builder"
    ].statement
    assert graph["local.closed_scalar_adiabatic_seed_bridge"].label == "Closed Scalar Adiabatic-seed Bridge Theorem"
    assert "`C_N^src = A_s W_N = A_s (N / N_p)^(-K_gauge / x)`" in graph[
        "local.closed_scalar_adiabatic_seed_bridge"
    ].statement
    assert graph["local.closed_scalar_acoustic_generator"].label == "Closed Scalar Acoustic Generator Theorem"
    assert graph["local.closed_scalar_acoustic_generator"].claim_status == "derived / scoped as maps"
    assert "`k_n^2 = n(n+2) / R_curv^2`" in graph["local.closed_scalar_acoustic_generator"].statement
    assert "`theta_b' = -a'/a theta_b + metric_euler + k_n^2 c_b^2 delta_b + R * drag_rate * (theta_gamma-theta_b)`" in graph[
        "local.closed_scalar_acoustic_generator"
    ].statement
    assert graph["local.closed_scalar_transfer_projector"].label == "Closed Scalar Transfer Projector Theorem"
    assert graph["local.closed_scalar_transfer_projector"].claim_status == "derived / scoped as maps"
    assert "`Phi_0 = sin(beta chi) / [beta sin chi]`" in graph[
        "local.closed_scalar_transfer_projector"
    ].statement
    assert "`Delta_l^T(q)` and `Delta_l^E(q)`" in graph["local.closed_scalar_transfer_projector"].statement
    assert graph["local.scoped_closed_scalar_pipeline"].label == "Scoped Closed-scalar Pipeline Theorem"
    assert graph["local.scoped_closed_scalar_pipeline"].claim_status == "conditional / scoped"
    assert "No silent one-slot collapse on the hierarchy-wide perturbation `R` slot appears anywhere in this composition." in graph[
        "local.scoped_closed_scalar_pipeline"
    ].statement
    assert graph["paper37.null_family_acoustic_readout"].label == "Null-family Acoustic Readout Theorem"
    assert "`omega_hat(eta) = (ev_eta tensor C_n) P_src(Phi)`" in graph[
        "paper37.null_family_acoustic_readout"
    ].statement
    assert graph["paper37.peak_functional_separation"].label == "Peak-functional Separation Theorem"
    assert "`100theta_s = 100 r_s(z_rec) / D_M(z_rec)`" in graph[
        "paper37.peak_functional_separation"
    ].statement


def test_theta_star_cli_json_includes_provenance() -> None:
    """The published theta_* CLI JSON should emit the explained record."""

    env = os.environ | {"PYTHONPATH": str(SRC)}
    result = subprocess.run(
        [sys.executable, "-m", "aio_calculator", "theta-star-theorem", "--json"],
        cwd=ROOT,
        env=env,
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(result.stdout)
    assert payload["output_id"] == "theta_star_theorem"
    assert payload["provenance"]["root_node"] == "paper37.active_branch_theta_star"
    assert payload["direct_observable_comparison"]["label"] == "First TT peak position"


def test_theta_star_cli_explain_prints_full_theorem_text() -> None:
    """Text-mode explain output should include theorem premises, proof outline, and scope."""

    env = os.environ | {"PYTHONPATH": str(SRC)}
    result = subprocess.run(
        [sys.executable, "-m", "aio_calculator", "theta-star-theorem", "--explain"],
        cwd=ROOT,
        env=env,
        check=True,
        capture_output=True,
        text=True,
    )
    assert "premise = `paper37.selector_support_promotion` fixes the carried physical selector leaf" in result.stdout
    assert "proof_outline = Evaluate the exact strict-bare selector backbone" in result.stdout
    assert "scope_boundary = Fixed active Paper 10 legacy projected branch only." in result.stdout

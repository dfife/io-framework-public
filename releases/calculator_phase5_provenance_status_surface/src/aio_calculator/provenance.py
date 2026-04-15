"""Provenance graph and explained-output surfaces for the calculator.

The calculator should publish numbers together with the authority chain that
licenses them. This module keeps that layer explicit instead of making every
intermediate arithmetic operation provenance-aware.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any

from .constants import ACTIVE_BRANCH, AUTHORITY_PATHS, ROOT
from .model import CurvedBackgroundModel, late_eta_io
from .recombination import (
    free_electron_density_m3,
    hydrogen_number_density_m3,
    local_background_state,
    local_baryon_loading_R,
    local_scattering_to_expansion_ratio,
    local_sound_speed_m_s,
    optical_depth_gradient_per_redshift,
    primitive_local_kappa_prime,
    saha_equilibrium_xe,
)
from .theorem_theta_star import compute_active_branch_theta_star


LAB_PREMISES_PATH = ROOT / "AGENTS.md"
ACTIVE_BRANCH_THETA_STAR_ELL_PEAK = 220.47514473507064
OBSERVED_FIRST_TT_PEAK_ELL_REFERENCE = 220.0
PLANCK_FLAT_REFERENCE_THETA_MC_100 = 1.04090
PLANCK_CLOSED_REFERENCE_THETA_MC_100 = 1.04116
PLANCK_CLOSED_REFERENCE_OMEGA_K = -0.044
THEOREM_REFERENCE_NOTE = (
    "Supporting references only. The theorem text carried on this node is the "
    "calculator's self-contained public dictionary entry."
)


@dataclass(frozen=True)
class TheoremNode:
    """One premise, theorem, audit, or scoped authority in the calculator graph."""

    node_id: str
    kind: str
    label: str
    claim_status: str
    statement: str
    scope: str
    authority_paths: tuple[str, ...]
    depends_on: tuple[str, ...] = ()
    premises: tuple[str, ...] = ()
    proof_outline: tuple[str, ...] = ()
    scope_boundary: tuple[str, ...] = ()
    notes: tuple[str, ...] = ()
    reference_note: str = THEOREM_REFERENCE_NOTE

    def as_dict(self) -> dict[str, Any]:
        return {
            "node_id": self.node_id,
            "kind": self.kind,
            "label": self.label,
            "claim_status": self.claim_status,
            "statement": self.statement,
            "scope": self.scope,
            "authority_paths": list(self.authority_paths),
            "depends_on": list(self.depends_on),
            "premises": list(self.premises),
            "proof_outline": list(self.proof_outline),
            "scope_boundary": list(self.scope_boundary),
            "notes": list(self.notes),
            "reference_note": self.reference_note,
        }


@dataclass(frozen=True)
class ObservableComparison:
    """Direct-observable comparison attached to an explained output."""

    label: str
    claim_status: str
    predicted_value: float
    observed_reference: float
    delta: float
    units: str
    note: str
    source_note: str
    source_links: tuple[str, ...] = ()

    def as_dict(self) -> dict[str, Any]:
        return {
            "label": self.label,
            "claim_status": self.claim_status,
            "predicted_value": self.predicted_value,
            "observed_reference": self.observed_reference,
            "delta": self.delta,
            "units": self.units,
            "note": self.note,
            "source_note": self.source_note,
            "source_links": list(self.source_links),
        }


@dataclass(frozen=True)
class ExplainedValue:
    """Published value plus its scope, conditions, and provenance chain."""

    output_id: str
    label: str
    primary_key: str
    primary_value: float | str
    units: str | None
    claim_status: str
    provenance_status: str
    payload: dict[str, Any]
    scope_boundary: tuple[str, ...]
    conditional_on: tuple[str, ...]
    provenance_root_id: str
    chain_ids: tuple[str, ...]
    premise_ids: tuple[str, ...]
    supporting_node_ids: tuple[str, ...] = ()
    zero_fitted_parameters: bool = False
    non_claims: tuple[str, ...] = ()
    notes: tuple[str, ...] = ()
    geometry_explanation: str | None = None
    comparison_context: dict[str, Any] = field(default_factory=dict)
    direct_observable_comparisons: tuple[ObservableComparison, ...] = ()

    def as_dict(
        self,
        *,
        nodes: dict[str, TheoremNode] | None = None,
        include_provenance: bool = True,
    ) -> dict[str, Any]:
        payload = dict(self.payload)
        payload.update(
            {
                "output_id": self.output_id,
                "label": self.label,
                "primary_key": self.primary_key,
                "primary_value": self.primary_value,
                "units": self.units,
                "claim_status": self.claim_status,
                "provenance_status": self.provenance_status,
                "zero_fitted_parameters": self.zero_fitted_parameters,
                "conditional_on_premises": list(self.conditional_on),
                "scope_boundary": list(self.scope_boundary),
                "non_claims": list(self.non_claims),
                "notes": list(self.notes),
            }
        )
        if self.geometry_explanation is not None:
            payload["geometry_explanation"] = self.geometry_explanation
        if self.comparison_context:
            payload["comparison_context"] = dict(self.comparison_context)
        if self.direct_observable_comparisons:
            comparisons = [row.as_dict() for row in self.direct_observable_comparisons]
            payload["direct_observable_comparisons"] = comparisons
            if len(comparisons) == 1:
                payload["direct_observable_comparison"] = comparisons[0]
        if include_provenance:
            graph = theorem_graph() if nodes is None else nodes
            payload["provenance"] = {
                "root_node": self.provenance_root_id,
                "premise_ids": list(self.premise_ids),
                "chain_ids": list(self.chain_ids),
                "supporting_node_ids": list(self.supporting_node_ids),
                "nodes": {node_id: graph[node_id].as_dict() for node_id in graph},
            }
        return payload


def theorem_graph() -> dict[str, TheoremNode]:
    """Return the current calculator theorem dictionary."""

    ag = str(LAB_PREMISES_PATH)
    theta_star = compute_active_branch_theta_star()
    rd_mpc = ACTIVE_BRANCH.rd_mpc
    eta_late = late_eta_io()
    return {
        "premise.1": TheoremNode(
            node_id="premise.1",
            kind="premise",
            label="Premise 1",
            claim_status="conditional premise",
            statement=(
                "We live inside a black hole, and the CMB is the event horizon, "
                "with Hawking radiation falling inward and being observed from "
                "the interior."
            ),
            scope="Global working assumption for IO model-building in this lab.",
            authority_paths=(ag,),
            proof_outline=(
                "This node is declared as a working premise of the calculator rather than proved internally.",
                "Any downstream node that lists `premise.1` is explicitly conditional on this premise.",
            ),
            scope_boundary=(
                "Applies only as a lab working assumption for IO model-building.",
                "Not presented here as an empirically established theorem.",
            ),
        ),
        "premise.2": TheoremNode(
            node_id="premise.2",
            kind="premise",
            label="Premise 2",
            claim_status="conditional premise",
            statement=(
                "The physics inside our black hole are the same as the physics "
                "outside our black hole."
            ),
            scope="Global working assumption for IO model-building in this lab.",
            authority_paths=(ag,),
            proof_outline=(
                "This node is declared as a working premise of the calculator rather than proved internally.",
                "Any downstream node that lists `premise.2` is explicitly conditional on this premise.",
            ),
            scope_boundary=(
                "Applies only as a lab working assumption for IO model-building.",
                "Not presented here as an empirically established theorem.",
            ),
        ),
        "paper21.branch_assignment": TheoremNode(
            node_id="paper21.branch_assignment",
            kind="theorem",
            label="Paper 21 TIO Branch Assignment",
            claim_status="derived / scoped",
            statement=(
                "The active calculator branch is the carried Paper 10 legacy "
                "projected branch used by the public runtime surface."
            ),
            scope="Calculator branch selection and carried active package.",
            authority_paths=(str(AUTHORITY_PATHS["paper21_tio_branch_assignment"]),),
            depends_on=("premise.1", "premise.2"),
            premises=(
                "`premise.1` and `premise.2` fix the IO setting in which a carried active branch is meaningful.",
                "The calculator publishes one carried active package rather than dynamically averaging over multiple branch candidates.",
            ),
            proof_outline=(
                "Read the carried runtime package selected by the Paper 21 branch-assignment result.",
                "Identify that public runtime package with the legacy Paper 10 projected branch used by the live calculator constants and derived outputs.",
                "Once this identification is fixed, all downstream calculator outputs inherit one branch label instead of refitting branch choice per observable.",
            ),
            scope_boundary=(
                "Applies only to the calculator's carried active package.",
                "Does not assert uniqueness of the branch outside the published runtime surface.",
            ),
        ),
        "paper22.spatial_mode_ladder": TheoremNode(
            node_id="paper22.spatial_mode_ladder",
            kind="theorem",
            label="Paper 22 Spatial Mode Ladder",
            claim_status="derived / scoped",
            statement=(
                "The closed `S^3` spatial carrier decomposes into scalar, vector, "
                "and TT tensor ladders with "
                "`lambda_n^(S) = n(n+2) / a^2`, "
                "`lambda_n^(V) = (n+1)^2 / a^2`, "
                "`lambda_n^(TT,rough) = (n(n+2)-2) / a^2`, "
                "multiplicities `(n+1)^2`, `2n(n+2)`, `2(n-1)(n+3)`, and "
                "diagonal-spin floors `J_min = 0,1,2` respectively."
            ),
            scope="Spatial harmonic carrier on closed `S^3`.",
            authority_paths=(str(AUTHORITY_PATHS["paper22_spatial_hodge_complex"]),),
            depends_on=("premise.1", "premise.2"),
            premises=(
                "`premise.1` and `premise.2` place the perturbation problem on the accepted IO closed-space setting.",
                "Paper 22 constructs the scalar/vector Hodge carriers and the TT extension on round `S^3`.",
            ),
            proof_outline=(
                "Decompose the round-`S^3` spatial Hilbert space into scalar, coexact-vector, and TT tensor branches.",
                "Read off the exact eigenvalues, multiplicities, and diagonal-spin supports for each branch.",
                "Use those branch laws as the theorem-grade spatial carrier for later perturbation work.",
            ),
            scope_boundary=(
                "Spatial carrier only.",
                "Does not by itself determine the dynamical perturbation/source equations.",
            ),
        ),
        "paper23.closed_scalar_operator": TheoremNode(
            node_id="paper23.closed_scalar_operator",
            kind="theorem",
            label="Paper 23 Closed Scalar Operator Theorem",
            claim_status="derived / scoped",
            statement=(
                "On the closed scalar hierarchy, the first curvature correction is "
                "`lambda_n - 3 = (n-1)(n+3)`, scalar hyperspherical support obeys "
                "`ell = 0,1,...,n`, and the physical inhomogeneous scalar spectrum "
                "begins at `n >= 2` with `n = 1` pure gauge."
            ),
            scope="Closed scalar shell operator and physical mode support.",
            authority_paths=(str(AUTHORITY_PATHS["paper23_scalar_perturbations"]),),
            depends_on=("paper22.spatial_mode_ladder",),
            premises=(
                "`paper22.spatial_mode_ladder` fixes the scalar harmonic carrier on `S^3`.",
                "The closed scalar perturbation problem lives on that discrete shell basis rather than a flat continuous `k` basis.",
            ),
            proof_outline=(
                "Start from the scalar `S^3` harmonic ladder with `lambda_n = n(n+2)`.",
                "Insert the closed-space scalar curvature correction to obtain `lambda_n - 3 = (n-1)(n+3)`.",
                "Classify `n = 0` as background, `n = 1` as gauge, and `n >= 2` as physical scalar support.",
            ),
            scope_boundary=(
                "Closed scalar shell operator and support only.",
                "Does not by itself close the full metric-plus-fluid source/acoustic hierarchy.",
            ),
        ),
        "paper28.closed_s3_shell_power": TheoremNode(
            node_id="paper28.closed_s3_shell_power",
            kind="theorem",
            label="Paper 28 Closed S^3 Shell-power Definition",
            claim_status="derived / scoped",
            statement=(
                "The exact observer-side closed-`S^3` shell covariance obeys "
                "`Var_n(X) = ((n+1)^2 / (2 pi^2 R^3)) P_X(n)`, with dimensionless "
                "shell conventions "
                "`Delta_q^2(n) = ((n+1)^3 / (2 pi^2 R^3)) P_X(n)`, "
                "`Delta_scalar^2(n) = (n(n+1)(n+2) / (2 pi^2 R^3)) P_X(n)`, and "
                "`Delta_MS^2(n) = (((n-1)(n+1)(n+3)) / (2 pi^2 R^3)) P_X(n)`."
            ),
            scope="Observer-side shell covariance and power-spectrum conventions on closed `S^3`.",
            authority_paths=(str(AUTHORITY_PATHS["paper28_closed_s3_power_definition"]),),
            depends_on=("paper22.spatial_mode_ladder", "paper23.closed_scalar_operator"),
            premises=(
                "`paper22.spatial_mode_ladder` fixes the exact scalar-shell degeneracy `(n+1)^2` on closed `S^3`.",
                "`paper23.closed_scalar_operator` fixes the physical scalar shell variable `k_MS(n) = sqrt((n-1)(n+3)) / R`.",
            ),
            proof_outline=(
                "Expand the observer-side scalar field in orthonormal closed-`S^3` hyperspherical harmonics.",
                "Write the equal-point variance shell by shell using the scalar degeneracy `(n+1)^2` and the volume `2 pi^2 R^3`.",
                "From that invariant shell variance, read off the exact `q`, scalar-Laplacian, and Mukhanov-Sasaki `Delta^2` conventions without importing the flat `k^3` law as primitive.",
            ),
            scope_boundary=(
                "Observer-side closed-shell power definitions only.",
                "Does not by itself derive the physical IO source-side shell covariance law or the missing bridge typing.",
            ),
        ),
        "paper30.background_surface": TheoremNode(
            node_id="paper30.background_surface",
            kind="theorem",
            label="Paper 30 Legacy Recompute Surface",
            claim_status="derived / scoped",
            statement=(
                "The active branch supports the late-time closed-FRW background "
                "surface with "
                "`H(z) = H_0 sqrt[Omega_r (1+z)^4 + Omega_m (1+z)^3 + Omega_k (1+z)^2 + Omega_Lambda]`, "
                "`D_M(z) = R_c sin(chi(z))`, "
                "`chi(z) = ∫_0^z dz' H_0 / H(z')`, and "
                "`t(z) = ∫_z^∞ dz' / ((1+z') H(z'))`."
            ),
            scope="Observer-side background geometry and BAO-side runtime surface.",
            authority_paths=(str(AUTHORITY_PATHS["paper30_legacy_recompute"]),),
            depends_on=("paper21.branch_assignment",),
            premises=(
                "`paper21.branch_assignment` fixes the active branch package.",
                "Closed-FRW background evolution on that branch is already part of the accepted runtime surface.",
            ),
            proof_outline=(
                "Evaluate the active-branch closed-FRW integrals for expansion, transverse distance, radial distance, volume distance, lookback time, and age.",
                "Export those quantities directly in the calculator without delegating geometry to a flat-space backend.",
                "Use the carried branch value consistently across the public background and BAO surfaces.",
            ),
            scope_boundary=(
                "Observer-side closed-FRW background geometry on the fixed active branch only.",
                "Does not by itself determine a full perturbation transfer solver.",
            ),
        ),
        "paper29.sound_speed_selector": TheoremNode(
            node_id="paper29.sound_speed_selector",
            kind="theorem",
            label="Paper 29 Sound-speed Baryon-slot Selector",
            claim_status="derived / scoped",
            statement=(
                "The local sound-speed loading term uses "
                "`R(z) = 3 rho_b(z) / [4 rho_gamma(z)]` with the unique "
                "theorem-grade baryon slot `omega_b,geom` on the rebuilt "
                "reduced-stack scope."
            ),
            scope="Local photon-baryon inertia coefficient for the active branch.",
            authority_paths=(str(AUTHORITY_PATHS["paper29_sound_speed_selector"]),),
            depends_on=("premise.1", "premise.2", "paper21.branch_assignment"),
            premises=(
                "`premise.1` and `premise.2` fix the IO setting for the local pre-recombination plasma.",
                "`paper21.branch_assignment` fixes the carried active branch used by the live calculator.",
            ),
            proof_outline=(
                "Identify `R(z)` as the local photon-baryon inertia coefficient rather than an observer-side readout scalar.",
                "Use the rebuilt Paper 29 slot audit to rule out the late clustering branch for this local fluid coefficient.",
                "Conclude that the unique theorem-grade slot for `R(z)` is `omega_b,geom` on the live calculator branch.",
            ),
            scope_boundary=(
                "Applies to the local sound-speed loading term `R(z)` on the active branch.",
                "Does not by itself close the full drag-epoch or BAO standard-ruler theorem.",
            ),
        ),
        "paper31.geometric_pre_drag_ruler": TheoremNode(
            node_id="paper31.geometric_pre_drag_ruler",
            kind="theorem",
            label="Paper 31 Geometric Pre-drag Ruler",
            claim_status="derived / scoped",
            statement=(
                "The active branch carries the published pre-drag ruler "
                "`r_d = ∫ c_s(z) / H(z) dz` with "
                "`c_s(z) = c / sqrt(3[1 + R(z)])`, yielding "
                f"`r_d = {rd_mpc:.12f} Mpc` on the calculator surface."
            ),
            scope="Active-branch BAO ruler slot.",
            authority_paths=(str(AUTHORITY_PATHS["paper31_legacy_recompute"]),),
            depends_on=("paper21.branch_assignment", "paper29.sound_speed_selector"),
            premises=(
                "`paper21.branch_assignment` fixes the active branch on which the ruler is read.",
                "`paper29.sound_speed_selector` fixes `R(z)` to the theorem-grade slot `omega_b,geom`.",
                "The published BAO surface uses one carried ruler slot rather than a per-query fit parameter.",
            ),
            proof_outline=(
                "Evaluate the active-branch sound-horizon / pre-drag integral using the carried closed background and the theorem-grade sound-speed slot.",
                "Expose that carried value as the calculator's published `r_d` slot.",
                "Use the same carried slot in `D_M/r_d`, `D_H/r_d`, and `D_V/r_d` outputs.",
            ),
            scope_boundary=(
                "Active-branch ruler slot only.",
                "Does not claim a universal branch-independent drag-ruler theorem.",
            ),
        ),
        "paper31.baryon_assignment": TheoremNode(
            node_id="paper31.baryon_assignment",
            kind="theorem",
            label="Paper 31 Baryon Assignment",
            claim_status="derived / scoped",
            statement=(
                "The active branch exposes typed baryon slots and assigns "
                "`omega_b,geom` as the local chemistry density entering "
                "`n_H(z)`, `n_e(z) = x_e n_H(z)`, and "
                "`kappa'_loc = a_loc n_e sigma_T` in the live recombination primitives."
            ),
            scope="Typed baryon-slot split on the active branch.",
            authority_paths=(str(AUTHORITY_PATHS["paper31_baryon_assignment"]),),
            depends_on=("paper21.branch_assignment",),
            premises=(
                "`paper21.branch_assignment` fixes the active branch package.",
                "The calculator distinguishes typed baryon slots for geometry, chemistry, and downstream operator use.",
            ),
            proof_outline=(
                "Separate the baryon inventory into typed calculator slots rather than one undifferentiated parameter.",
                "Assign `omega_b,geom` as the chemistry density used by the live recombination primitives on the active branch.",
                "Propagate that slot choice into the local background-state and opacity chains.",
            ),
            scope_boundary=(
                "Typed baryon assignment on the fixed active branch only.",
                "Does not assert a theorem-grade completion of every possible chemistry closure.",
            ),
        ),
        "paper31.local_background_state_map": TheoremNode(
            node_id="paper31.local_background_state_map",
            kind="theorem",
            label="Paper 31 Local Background State Map",
            claim_status="derived / scoped",
            statement=(
                "The calculator's local recombination state map "
                "(`H_loc`, `T_R,loc`, `n_H,geom`, `u`, `a_loc`) is a theorem-grade "
                "map on the active branch, with "
                "`H_loc = (c / r_s) sqrt[(1-u)/u^3]`, "
                "`T_R,loc = x^(-K_gauge) T_obs,0 (1+z)`, "
                "`a_loc = u R_U`, and `n_H,geom = rho_b,geom / m_H`."
            ),
            scope="Local recombination background-state primitives.",
            authority_paths=(str(AUTHORITY_PATHS["paper31_local_background_state_map"]),),
            depends_on=("paper21.branch_assignment", "paper31.baryon_assignment"),
            premises=(
                "`paper21.branch_assignment` fixes the active branch package.",
                "`paper31.baryon_assignment` fixes the local chemistry slot as `omega_b,geom`.",
            ),
            proof_outline=(
                "Start from the active-branch closed background and the typed chemistry slot.",
                "Construct the local recombination state map `H_loc`, `T_R,loc`, `n_H,geom`, `u`, and `a_loc` at a supplied redshift.",
                "Export those primitives as calculator-visible local-state quantities.",
            ),
            scope_boundary=(
                "Local recombination background-state primitives on the fixed active branch.",
                "Does not by itself close the exact dynamic-network recombination problem.",
            ),
        ),
        "paper31.recombination_clock_transport": TheoremNode(
            node_id="paper31.recombination_clock_transport",
            kind="theorem",
            label="Paper 31 Recombination Clock Transport",
            claim_status="derived / scoped",
            statement=(
                "The live primitive opacity chain derives "
                "`kappa'_loc = a_loc n_e sigma_T`, "
                "`d tau_obs / dz = kappa'_loc c / ((1+z) H_loc)`, and "
                "`Gamma_T / H_loc = n_e sigma_T c / H_loc` once the local "
                "background state and `omega_b,geom` chemistry slot are fixed."
            ),
            scope="Primitive local opacity and LOS clock transport.",
            authority_paths=(str(AUTHORITY_PATHS["paper31_clock_transport"]),),
            depends_on=("paper31.local_background_state_map",),
            premises=(
                "`paper31.local_background_state_map` provides the local branch background state.",
                "Chemistry-dependent outputs are derived only when `x_e` is supplied by the local Saha seed or another separately justified source.",
            ),
            proof_outline=(
                "Use the local background state and chemistry slot to build `kappa'_loc`, `d tau_obs / dz`, `Gamma_T/H_loc`, `R_local,geom`, and `c_s,local`.",
                "Treat the local Saha seed as the default derived ionization input in the published calculator.",
                "When a user overrides `x_e`, keep the local background state derived but mark chemistry-dependent rows as conditional.",
            ),
            scope_boundary=(
                "Primitive local opacity and LOS clock transport on the active branch.",
                "Not a theorem-grade exact dynamic-network recombination closure.",
            ),
        ),
        "local.saha_seed": TheoremNode(
            node_id="local.saha_seed",
            kind="theorem",
            label="Local Saha Seed Theorem",
            claim_status="derived / scoped under Premise 2 standard hydrogen microphysics",
            statement=(
                "The default ionization seed is fixed by the local Saha law "
                "`x_e^2/(1-x_e) = ((m_e k_B T_R,loc)/(2 pi hbar^2))^(3/2) "
                "exp(-chi_H/(k_B T_R,loc)) / n_H,geom`."
            ),
            scope="Default local ionization seed used by the published recombination primitives.",
            authority_paths=(),
            depends_on=("premise.2", "paper31.local_background_state_map", "paper31.baryon_assignment"),
            premises=(
                "`premise.2` licenses standard hydrogen microphysics inside the horizon.",
                "`paper31.local_background_state_map` fixes `T_R,loc` and `n_H,geom` on the active branch.",
                "`paper31.baryon_assignment` fixes the chemistry slot as `omega_b,geom`.",
            ),
            proof_outline=(
                "Use the active-branch local radiation temperature and hydrogen number density as the thermodynamic inputs.",
                "Apply the standard hydrogen Saha equilibrium equation to those local variables.",
                "Solve the algebraic relation for the default local seed `x_e` used by the published primitive surface.",
            ),
            scope_boundary=(
                "Default local equilibrium seed only.",
                "Does not claim an exact dynamic-network recombination history or visibility peak closure.",
            ),
            notes=(
                "No published paper reference is used here; the theorem text is carried self-contained in the calculator dictionary.",
            ),
        ),
        "paper32.closed_s3_solver_spec": TheoremNode(
            node_id="paper32.closed_s3_solver_spec",
            kind="theorem",
            label="Paper 32 S^3 Solver Specification",
            claim_status="derived / scoped",
            statement=(
                "The IO perturbation/transfer geometry is organized on closed "
                "S^3 spatial sections rather than on a flat `K=0` transfer basis."
            ),
            scope="Closed-space transfer geometry specification for the IO stack.",
            authority_paths=(str(AUTHORITY_PATHS["paper32_s3_solver_spec"]),),
            depends_on=("premise.1", "premise.2"),
            premises=(
                "`premise.1` and `premise.2` place the IO transfer problem on the interior black-hole branch with outside-equivalent microphysics.",
                "Spatial sections in the accepted IO perturbation stack are closed rather than flat.",
            ),
            proof_outline=(
                "Specify the perturbation and transfer geometry on closed `S^3` sections rather than a flat `K=0` basis.",
                "Use that specification to interpret acoustic and peak-location quantities in a closed-geometry transfer setting.",
                "Treat flat-space extractions as comparison conventions rather than native calculator geometry.",
            ),
            scope_boundary=(
                "Geometry specification for the IO transfer stack.",
                "Not a theorem-grade completion of the full TT/TE/EE solver by itself.",
            ),
        ),
        "paper32.modular_dtn_field_transfer": TheoremNode(
            node_id="paper32.modular_dtn_field_transfer",
            kind="theorem",
            label="Paper 32 Modular-DtN Field Transfer",
            claim_status="derived / scoped",
            statement=(
                "On the active scalar-source sector, the unique positive one-slot "
                "field transfer is "
                "`T_field = exp[-(K_g tensor log(r_s Lambda_DtN^coex)) / (2x)]`, "
                "with quadratic descendant "
                "`R_cov = T_field^* T_field`, full source block "
                "`P_src = B_+ o U_coex o T_field`, plus-branch shell window "
                "`W_N = (N / N_p)^(-K_gauge / x)`, and native amplitude "
                "`A_s = (25/9) [gamma^2 / (1 + gamma^2)] [1 / sqrt(2)] [exp(4 pi sqrt(2)) - 1]^-1`."
            ),
            scope="Active scalar-source block and one-slot post-bridge field sector.",
            authority_paths=(str(AUTHORITY_PATHS["paper32_modular_dtn_field_transfer"]),),
            depends_on=("premise.1", "premise.2"),
            premises=(
                "`premise.1` and `premise.2` place the source/readout problem on the accepted IO interior-horizon branch.",
                "The active source block is the one-slot modular-DtN field sector rather than the full perturbation hierarchy.",
            ),
            proof_outline=(
                "Use the coexact DtN spectrum to define the shell generator `Y = log(r_s Lambda_DtN^coex)`.",
                "Combine the reduced gauge modular weight with the accessible-line divisor `1/x` to obtain the unique positive source transfer `T_field`.",
                "Apply the plus bridge and pivot normalization to recover the source window and the native scalar amplitude on the active sector.",
            ),
            scope_boundary=(
                "Active scalar-source block only.",
                "Does not by itself close the exact Stage-2 history operator, the closed-S^3 perturbation hierarchy, or the peak/readout identification theorem.",
            ),
        ),
        "paper32.typed_baryon_slot_spec": TheoremNode(
            node_id="paper32.typed_baryon_slot_spec",
            kind="theorem",
            label="Typed Baryon-slot Specification",
            claim_status="derived / scoped",
            statement=(
                "The native solver preserves the typed baryon split: "
                "recombination chemistry `omega_b,geom`, primitive local opacity "
                "`omega_b,geom`, reduced visibility/readout `omega_b,eff`, while "
                "the full-hierarchy baryon-loading `R` slot and scalar metric-source "
                "slot remain open. No silent one-slot collapse on `R` is licensed "
                "anywhere in the perturbation pipeline."
            ),
            scope="Perturbation-era baryon typing on the closed `S^3` solver grammar.",
            authority_paths=(str(AUTHORITY_PATHS["paper32_s3_solver_spec"]),),
            depends_on=("paper32.closed_s3_solver_spec",),
            premises=(
                "`paper32.closed_s3_solver_spec` fixes the typed closed-`S^3` solver grammar.",
                "The perturbation block is not licensed to collapse to a one-slot baryon assignment.",
            ),
            proof_outline=(
                "Read the active typed baryon placements from Corollary 32.S3.1.",
                "Assign theorem-grade slots only where the stack actually closes them.",
                "Leave the hierarchy-wide `R` slot and scalar metric-source slot explicitly open instead of backfilling them from local helpers.",
                "Reject any silent one-slot reassignment of the full perturbation `R` slot to a local helper quantity.",
            ),
            scope_boundary=(
                "Typed solver grammar only.",
                "Does not derive a single theorem-grade baryon slot for the full hierarchy.",
                "In particular, the full-hierarchy `R` slot is not licensed to collapse silently to one local scalar anywhere in the composed pipeline.",
            ),
        ),
        "paper31.stage2_markov_state": TheoremNode(
            node_id="paper31.stage2_markov_state",
            kind="theorem",
            label="Paper 31 Stage-2 Markov State",
            claim_status="derived / scoped",
            statement=(
                "The exact Stage-2 hydrogen radiative-transfer branch admits a "
                "lossless Markov closure on "
                "`Y_rec = (x_e, T_m, D_-(q;z), L_-(z))`, and no fixed finite-dimensional "
                "scalar moment vector replaces that field exactly."
            ),
            scope="Exact Stage-2 history-state carrier.",
            authority_paths=(str(AUTHORITY_PATHS["paper31_stage2_markov_state"]),),
            depends_on=("premise.2",),
            premises=(
                "`premise.2` licenses the accepted exterior local atomic/radiative-transfer class inside the horizon.",
                "Stage 2 belongs to the local bulk radiative-transfer sector rather than an observer-side readout patch.",
            ),
            proof_outline=(
                "Audit the exact FULL Stage-2 update chain and identify the outgoing characteristic distortion field plus line-handoff sector.",
                "Show that the extended state `(x_e, T_m, D_-(q;z), L_-(z))` is a lossless Markov closure of the exact branch.",
                "Kill any fixed finite-dimensional scalar compression as an exact replacement.",
            ),
            scope_boundary=(
                "Exact Stage-2 state carrier only.",
                "Does not by itself supply the final explicit dynamic-network renormalization operator.",
            ),
        ),
        "local.inherited_full_stage2_dynamic_history_builder": TheoremNode(
            node_id="local.inherited_full_stage2_dynamic_history_builder",
            kind="theorem",
            label="Inherited FULL Stage-2 Dynamic-history Builder Theorem",
            claim_status="conditional / scoped",
            statement=(
                "On the active IO local background with "
                "`T_R,loc(z) = T_IO,0 (1+z)` and "
                "`H_loc(z) = (c / R_S) sqrt((1-u)/u^3)` for `u = 1 / [x (1+z)]`, "
                "the standalone inherited-FULL builder runs exact FULL HyRec history outside the forbidden pointwise wrapper and exports "
                "`Y_rec(z) = (x_e(z), T_m(z), D_-(q;z), L_-(z))` with "
                "`D_-(q;z) = interp_Dfnu(lna_0, dlna, Dfminus_hist(q;.), N_z, -ln(1+z))` and "
                "`L_-(z) = interp_Dfnu(lna_0, dlna, Dfminus_Ly_hist(.), N_z, -ln(1+z))`."
            ),
            scope="Conditional exact inherited-FULL Stage-2 history builder on the active IO local background.",
            authority_paths=(),
            depends_on=("premise.2", "paper31.local_background_state_map", "paper31.stage2_markov_state"),
            premises=(
                "`premise.2` licenses the inherited FULL atomic and radiative-transfer physics class on the local bulk branch.",
                "`paper31.local_background_state_map` fixes the active local thermal and Hubble histories entering the standalone driver.",
                "`paper31.stage2_markov_state` fixes the exact exported state grammar `Y_rec = (x_e, T_m, D_-(q;z), L_-(z))`.",
            ),
            proof_outline=(
                "Promote the existing standalone FULL-history route from the Paper 31 benchmark layer into the calculator instead of calling FULL HyRec through a pointwise `(z, x_e, T_m)` wrapper.",
                "Run FULL HyRec on the active IO local background arrays with the explicit history-grid fix used by the benchmark route.",
                "Export `x_e`, `T_m`, `Dfminus_hist`, and `Dfminus_Ly_hist` on the requested observer-redshift grid without silently collapsing the characteristic field to one preferred scalar.",
            ),
            scope_boundary=(
                "Conditional exact inherited-FULL history builder only.",
                "Uses inherited FULL atomic and radiative-transfer physics under Premise 2 rather than a new universal IO-native renormalization theorem.",
                "Does not pick a preferred one-dimensional compression of `D_-(q;z)` unless the caller chooses one explicitly.",
            ),
            notes=(
                "The theorem text is self-contained here; there is no published paper reference for this post-Paper-32 local completion step.",
            ),
        ),
        "paper37.thomson_history_realization": TheoremNode(
            node_id="paper37.thomson_history_realization",
            kind="theorem",
            label="Thomson-history Realization Theorem",
            claim_status="derived / scoped",
            statement=(
                "Any exact IO-native closure on the surviving acoustic branch must "
                "be realized on the coupled tuple "
                "`(thomson_drag_rate, thomson_hierarchy_rate, tau_c, dtau_c, slip, shear)` "
                "with `tau_c = 1 / thomson_drag_rate` and "
                "`dtau_c = - d(thomson_drag_rate) * tau_c^2`."
            ),
            scope="Coupled Thomson-history carrier for the perturbation hierarchy.",
            authority_paths=(str(AUTHORITY_PATHS["paper37_thomson_history_realization"]),),
            depends_on=("paper32.closed_s3_solver_spec", "paper31.stage2_markov_state"),
            premises=(
                "`paper32.closed_s3_solver_spec` fixes the perturbation block as part of the typed closed-`S^3` solver grammar.",
                "`paper31.stage2_markov_state` fixes the exact history-state carrier feeding the perturbation seam.",
                "The tight-coupling system depends on distinct drag and hierarchy rates together with `tau_c`, `dtau_c`, slip, and shear.",
            ),
            proof_outline=(
                "Localize the surviving acoustic perturbation seam to the broad Thomson-history leg rather than a narrow visibility patch.",
                "Read the carrier formulas for `thomson_drag_rate`, `thomson_hierarchy_rate`, `tau_c`, and `dtau_c` from the accepted local hierarchy code path.",
                "Promote the coupled tuple to the exact admissible carrier and kill one-site downstream rescalings as fake closures.",
            ),
            scope_boundary=(
                "Tuple carrier only.",
                "Does not yet derive the exact IO-native operator acting on that tuple.",
            ),
        ),
        "local.closed_scalar_metric_state_builder": TheoremNode(
            node_id="local.closed_scalar_metric_state_builder",
            kind="theorem",
            label="Closed Scalar Metric-state Builder Theorem",
            claim_status="derived / scoped as maps",
            statement=(
                "Once the Einstein-normalized scalar stress summary "
                "`(delta_rho, delta_p, rho_plus_p_theta, rho_plus_p_shear)` is supplied on one closed scalar shell, "
                "the Newtonian metric state is fixed by "
                "`psi = phi - 4.5 (a^2 / k_n^2) rho_plus_p_shear` and "
                "`phi' = -(a'/a) psi + 1.5 (a^2 / k_n^2) rho_plus_p_theta`, "
                "while the synchronous metric state is fixed by "
                "`h' = [k_n^2 s_2^2 eta + 1.5 a^2 delta_rho] / (0.5 a'/a)`, "
                "`eta' = [1.5 a^2 rho_plus_p_theta + 0.5 K h'] / (k_n^2 s_2^2)`, "
                "`alpha = (h' + 6 eta') / (2 k_n^2)`, and "
                "`alpha' = -2 (a'/a) alpha + eta - 4.5 (a^2 / k_n^2) rho_plus_p_shear`."
            ),
            scope="Einstein-side scalar metric-state reconstruction on one explicit closed shell.",
            authority_paths=(),
            depends_on=("paper23.closed_scalar_operator",),
            premises=(
                "`paper23.closed_scalar_operator` fixes the closed scalar shell geometry and the `s_2^2 = 1 - 3K/k_n^2` factor.",
                "The total scalar stress summary is supplied explicitly rather than guessed from a hidden matter model.",
            ),
            proof_outline=(
                "Write the scalar Einstein equations on one physical closed shell in Newtonian and synchronous gauge.",
                "Solve algebraically for the metric variables and their first derivatives from the explicit stress summary.",
                "Feed those metric variables into the acoustic quartet without introducing any extra closure factor.",
            ),
            scope_boundary=(
                "Metric-state builder from an explicit total scalar stress summary only.",
                "Does not derive the stress summary from a full multi-species perturbation hierarchy by itself.",
            ),
            notes=(
                "The theorem text is self-contained here; there is no published paper reference for this post-Paper-32 local completion step.",
            ),
        ),
        "local.closed_scalar_adiabatic_seed_bridge": TheoremNode(
            node_id="local.closed_scalar_adiabatic_seed_bridge",
            kind="theorem",
            label="Closed Scalar Adiabatic-seed Bridge Theorem",
            claim_status="derived / scoped",
            statement=(
                "On the active scalar-source branch, the source shell weight is "
                "`C_N^src = A_s W_N = A_s (N / N_p)^(-K_gauge / x)`, and the leading radiation-era closed-`S^3` adiabatic seed obeys "
                "`delta_gamma^(S) = -(k_n tau)^2 s_2^2 R_n / 3`, "
                "`theta_gamma^(S) = -k_n (k_n tau)^3 s_2^2 R_n / 36`, "
                "`delta_b^(S) = 3 delta_gamma^(S) / 4`, "
                "`theta_b^(S) = theta_gamma^(S)`, "
                "`eta^(S) = R_n [1 - (k_n tau)^2 / 36]`, "
                "followed by the explicit synchronous-to-Newtonian shift "
                "`delta_gamma^(N) = delta_gamma^(S) - 4 (a'/a) alpha`, "
                "`theta_gamma^(N) = theta_gamma^(S) + k_n^2 alpha`, "
                "`delta_b^(N) = delta_b^(S) - 3 (a'/a) alpha`, and "
                "`theta_b^(N) = theta_b^(S) + k_n^2 alpha`."
            ),
            scope="Active scalar-source shell weight plus leading closed-shell photon-baryon adiabatic seed.",
            authority_paths=(),
            depends_on=("paper32.modular_dtn_field_transfer", "paper23.closed_scalar_operator"),
            premises=(
                "`paper32.modular_dtn_field_transfer` fixes the active scalar-source shell weight `A_s W_N` on the plus branch.",
                "`paper23.closed_scalar_operator` fixes the physical scalar-shell support and the closed-shell geometric factor `s_2^2`.",
            ),
            proof_outline=(
                "Take the active scalar-source shell covariance `A_s W_N` from the source block without adding a new primordial fit.",
                "Write the leading radiation-era closed-shell photon-baryon adiabatic seed in synchronous gauge.",
                "Transform that seed explicitly to Newtonian gauge on the same shell and package the resulting hierarchy state.",
            ),
            scope_boundary=(
                "Leading photon-baryon adiabatic seed on the active scalar-source branch only.",
                "Does not derive low-shell puncture occupations, anomalous phase correlations, or full multi-species isocurvature families.",
            ),
            notes=(
                "The theorem text is self-contained here; there is no published paper reference for this post-Paper-32 local completion step.",
            ),
        ),
        "local.closed_scalar_transfer_projector": TheoremNode(
            node_id="local.closed_scalar_transfer_projector",
            kind="theorem",
            label="Closed Scalar Transfer Projector Theorem",
            claim_status="derived / scoped as maps",
            statement=(
                "Given an explicit closed-shell scalar source history, the transparent LOS source law is "
                "`S_T^(0) = exp(-kappa) phi' + g delta_gamma / 4`, "
                "`S_T^(1) = exp(-kappa) k_n psi + g theta_b / k_n` in Newtonian gauge, "
                "`S_T^(0) = -exp(-kappa) h' / 6 + g delta_gamma / 4`, "
                "`S_T^(1) = g theta_b / k_n`, "
                "`S_T^(2) = exp(-kappa) k_n^2 (2/3) s_2 alpha + g P` in synchronous gauge, "
                "with `S_T^(2) = g P` and `S_E = g P` on the scalar polarization source, "
                "and the exact closed radial chain is "
                "`Phi_0 = sin(beta chi) / [beta sin chi]`, "
                "`Phi_l = [(2l-1) cot chi Phi_{l-1} - sqrt(beta^2-(l-1)^2) Phi_{l-2}] / sqrt(beta^2-l^2)`, "
                "`dPhi_l/dchi = l cot chi Phi_l - sqrt(beta^2-(l+1)^2) Phi_{l+1}`, "
                "`d2Phi_l/dchi^2 = -2 cot chi dPhi_l/dchi + [l(l+1) csc^2 chi - beta^2 + 1] Phi_l`, "
                "so that `Delta_l^T(q)` and `Delta_l^E(q)` are fixed by explicit LOS integration on `chi = sqrt(K) (tau_0 - tau)`."
            ),
            scope="Closed scalar hierarchy-to-transfer projector on one explicit source history and one observer conformal time.",
            authority_paths=(),
            depends_on=(
                "paper22.spatial_mode_ladder",
                "paper23.closed_scalar_operator",
                "local.closed_scalar_metric_state_builder",
            ),
            premises=(
                "`paper22.spatial_mode_ladder` fixes the closed spatial carrier and the scalar radial support on `S^3`.",
                "`paper23.closed_scalar_operator` fixes the discrete scalar shell parameter `beta = n+1` and the physical shell support `n >= 2`.",
                "`local.closed_scalar_metric_state_builder` supplies the explicit scalar metric histories entering the transparent LOS source law.",
            ),
            proof_outline=(
                "Build the transparent scalar LOS sources directly from the hierarchy state, metric state, and observer-absolute visibility packet without rewriting them as hidden CLASS source patches.",
                "Evaluate the exact closed scalar radial chain from the stable recurrence on `beta = n+1` and the radial derivative identities.",
                "Integrate the explicit source and radial kernels on the supplied conformal-time grid to obtain `Delta_l^T(q)` and `Delta_l^E(q)` on the closed support.",
            ),
            scope_boundary=(
                "Exact source law and exact closed radial chain on one explicit scalar history.",
                "Numeric packet values still depend on explicit quadrature on the supplied conformal-time grid.",
                "Does not derive the hierarchy history automatically from the full perturbation evolution problem.",
            ),
            notes=(
                "The theorem text is self-contained here; there is no published paper reference for this post-Paper-32 local completion step.",
            ),
        ),
        "local.closed_scalar_acoustic_generator": TheoremNode(
            node_id="local.closed_scalar_acoustic_generator",
            kind="theorem",
            label="Closed Scalar Acoustic Generator Theorem",
            claim_status="derived / scoped as maps",
            statement=(
                "On one explicit physical closed-`S^3` scalar shell `n >= 2`, the "
                "local photon-baryon acoustic generator is fixed by "
                "`k_n^2 = n(n+2) / R_curv^2`, "
                "`q_n^2 = k_n^2 + K = (n+1)^2 / R_curv^2`, "
                "`s_l = sqrt(1 - K (l^2-1) / k_n^2)`, "
                "`cot_K^gen(tau) = sqrt(K) / [k_n tan(sqrt(K) tau)]`, "
                "local baryon loading `R = 3 rho_b / (4 rho_gamma)` on `omega_b,geom`, "
                "and the explicit scalar RHS "
                "`delta_gamma' = -(4/3)(theta_gamma + metric_continuity)`, "
                "`delta_b' = -(theta_b + metric_continuity)`, "
                "`theta_b' = -a'/a theta_b + metric_euler + k_n^2 c_b^2 delta_b + R * drag_rate * (theta_gamma-theta_b)`, "
                "`theta_gamma' = k_n^2 (delta_gamma/4 - s_2^2 F_2) + metric_euler + drag_rate * (theta_b-theta_gamma)`, "
                "with gauge-to-quartet maps "
                "`(metric_continuity, metric_euler, metric_shear, metric_shear_prime) = (-3 phi', k_n^2 psi, 0, 0)` in Newtonian gauge and "
                "`(h'/2, 0, k_n^2 alpha, k_n^2 alpha')` in synchronous gauge, "
                "with higher multipoles and the reduced TCA contract driven by the coupled tuple "
                "`(thomson_drag_rate, thomson_hierarchy_rate, tau_c, dtau_c, slip, shear)`. "
                "The local primitive loading `R(z)` used here is not a silent one-slot collapse of the full hierarchy-wide perturbation `R` slot."
            ),
            scope="Local affine scalar acoustic generator on an explicit sampled closed-`S^3` shell.",
            authority_paths=(str(AUTHORITY_PATHS["paper37_closed_scalar_acoustic_generator"]),),
            depends_on=(
                "paper23.closed_scalar_operator",
                "paper29.sound_speed_selector",
                "paper32.typed_baryon_slot_spec",
                "paper37.thomson_history_realization",
            ),
            premises=(
                "`paper23.closed_scalar_operator` fixes the discrete scalar shell support and the shifted scalar operator on `S^3`.",
                "`paper29.sound_speed_selector` fixes the theorem-grade local inertia loading `R(z)` on `omega_b,geom` for the primitive acoustic leg.",
                "`paper32.typed_baryon_slot_spec` forbids collapsing the hierarchy to one baryon slot and keeps the metric-source leg explicit.",
                "`paper37.thomson_history_realization` fixes the exact coupled Thomson tuple that an admissible local closure must consume.",
            ),
            proof_outline=(
                "Insert the closed-`S^3` scalar shell identities into the non-flat scalar hierarchy so the geometric recurrence factors are explicit on each discrete `n` shell.",
                "Use the theorem-grade local history sample `(x_e, T_m)` to recover `c_b^2` and its derivative, and use the theorem-grade primitive loading `R(z)` for the local momentum-loading leg.",
                "Feed the coupled Thomson tuple into the baryon drag, photon hierarchy damping, and tight-coupling contract equations to obtain the full local scalar photon-baryon RHS at explicit sample level.",
                "Conclude that the local generator itself is fixed once the external metric-drive and Stage-2/Thomson sample builders are supplied explicitly.",
            ),
            scope_boundary=(
                "Local explicit-sample scalar generator only.",
                "Does not derive the exact Stage-2 dynamic-network history builder or the total multi-species stress summary by itself.",
                "Does not by itself integrate the full scalar history from initial conditions to transfer packets without those explicit upstream builders.",
                "No theorem-grade hierarchy-wide one-slot collapse on `R` is claimed anywhere in this map.",
            ),
            notes=(
                "The theorem text is self-contained here; the linked report is supplementary supporting material only.",
            ),
        ),
        "local.scoped_closed_scalar_pipeline": TheoremNode(
            node_id="local.scoped_closed_scalar_pipeline",
            kind="theorem",
            label="Scoped Closed-scalar Pipeline Theorem",
            claim_status="conditional / scoped",
            statement=(
                "On the active scalar-source branch, the composed closed-`S^3` scalar map from "
                "`(P_src, C_N^src, ic_n, Y_rec, Thomson tuple, stress summary)` "
                "to `y^(n)(tau)`, then to `Delta_l^X(q)`, and then to shell-summed `C_l`, "
                "is carried end-to-end once the exact Stage-2 history enters through the conditional inherited-FULL builder. "
                "The carrier laws, metric formulas, projector formulas, and LOS formulas remain `derived / scoped as maps`, "
                "while the full composition is only `conditional / scoped` because it inherits the Stage-2 builder status. "
                "No silent one-slot collapse on the hierarchy-wide perturbation `R` slot appears anywhere in this composition."
            ),
            scope="Composed active-branch closed-scalar pipeline from source shell to transfer packets and shell-summed spectra.",
            authority_paths=(),
            depends_on=(
                "paper32.modular_dtn_field_transfer",
                "local.closed_scalar_adiabatic_seed_bridge",
                "local.inherited_full_stage2_dynamic_history_builder",
                "paper37.thomson_history_realization",
                "local.closed_scalar_metric_state_builder",
                "local.closed_scalar_acoustic_generator",
                "local.closed_scalar_transfer_projector",
                "paper28.closed_s3_shell_power",
                "paper32.closed_s3_solver_spec",
            ),
            premises=(
                "`paper32.modular_dtn_field_transfer` fixes the active scalar source block.",
                "`local.closed_scalar_adiabatic_seed_bridge` fixes the active closed-shell source-to-initial-condition bridge.",
                "`local.inherited_full_stage2_dynamic_history_builder` supplies the exact sampled Stage-2 history carrier at conditional inherited-FULL scope.",
                "`paper37.thomson_history_realization` fixes the exact coupled Thomson tuple that the local hierarchy map must consume.",
                "`local.closed_scalar_metric_state_builder`, `local.closed_scalar_acoustic_generator`, and `local.closed_scalar_transfer_projector` provide the explicit map-level formulas from shell data to transfer packets.",
                "`paper28.closed_s3_shell_power` and `paper32.closed_s3_solver_spec` supply the shell weighting and closed-space LOS assembly grammar.",
            ),
            proof_outline=(
                "Compose the active scalar source block, closed-shell seed bridge, sampled Stage-2 history, Thomson tuple, metric-state builder, local acoustic generator, and scalar transfer projector without inserting any hidden flat-space or CLASS default.",
                "Carry the resulting transfer packets into the explicit shell-weighted `C_l` assembly on the closed support.",
                "Track the claim status through the composition: map-level formulas remain `derived / scoped as maps`, while the full end-to-end pipeline inherits `conditional / scoped` status from the Stage-2 history builder.",
            ),
            scope_boundary=(
                "Full composed active-branch scalar pipeline only.",
                "Conditional on the inherited-FULL Stage-2 history builder rather than a universal IO-native Stage-2 renormalization theorem.",
                "No theorem-grade hierarchy-wide one-slot collapse on `R` is licensed anywhere in this composition.",
                "Not a universal automatic TT/TE/EE solver closure for arbitrary branches or sectors.",
            ),
            notes=(
                "The theorem text is self-contained here; there is no published paper reference for this post-Paper-32 composed-pipeline step.",
            ),
        ),
        "paper37.null_family_acoustic_readout": TheoremNode(
            node_id="paper37.null_family_acoustic_readout",
            kind="theorem",
            label="Null-family Acoustic Readout Theorem",
            claim_status="derived / scoped",
            statement=(
                "The explicit null-family readout field "
                "`omega_hat(eta) = (ev_eta tensor C_n) P_src(Phi)` can be built "
                "from the theorem-grade source block, and the resulting "
                "background acoustic estimator class "
                "`E_rs = integral_0^{eta_rec} c_s(eta) R_hist^ac(omega_hat(eta)) d eta` "
                "is itself one-slot on the current scoped sector."
            ),
            scope="Explicit null-family acoustic readout field and estimator class.",
            authority_paths=(str(AUTHORITY_PATHS["paper37_null_family_readout"]),),
            depends_on=("paper32.modular_dtn_field_transfer", "paper29.sound_speed_selector"),
            premises=(
                "`paper32.modular_dtn_field_transfer` closes the one-slot source/readout block `P_src`.",
                "`paper29.sound_speed_selector` fixes the theorem-grade local sound-speed slot entering the acoustic estimator kernel.",
                "Gauge-neutral direction collection and history evaluation preserve one-slot degree on the current scoped sector.",
            ),
            proof_outline=(
                "Evaluate the one-slot source block at fixed history label and readout direction to obtain `omega_hat(eta)`.",
                "Apply the already-closed homogeneous acoustic history-reduction operator to that explicit field.",
                "Integrate against the theorem-grade sound-speed kernel to obtain the background acoustic estimator class without creating a second gauge slot.",
            ),
            scope_boundary=(
                "Explicit readout field and estimator class only.",
                "Does not yet derive the exact acoustic endpoint/phase scalar or the final peak-position angle.",
            ),
        ),
        "paper37.peak_functional_separation": TheoremNode(
            node_id="paper37.peak_functional_separation",
            kind="theorem",
            label="Peak-functional Separation Theorem",
            claim_status="derived / scoped",
            statement=(
                "The background ratio "
                "`100theta_s = 100 r_s(z_rec) / D_M(z_rec)` is not, by itself, "
                "the exact physical peak-position readout `theta_peak`; theorem-grade "
                "numeric closure requires either the exact `A_peak` / closed-`S^3` "
                "perturbation readout or a separate theorem identifying that peak "
                "functional with the background ratio on the relevant scope."
            ),
            scope="Boundary between background acoustic ratios and physical peak-position readout.",
            authority_paths=(str(AUTHORITY_PATHS["paper37_peak_functional_separation"]),),
            depends_on=("paper32.closed_s3_solver_spec",),
            premises=(
                "`paper32.closed_s3_solver_spec` fixes the full linear IO transfer as a typed map with a perturbation/readout side beyond the source block.",
                "Peak-position observables live downstream of the primitive sky field and the quadratic power spectrum rather than at the raw background ratio alone.",
            ),
            proof_outline=(
                "Place `theta_peak` on the measurement chain `primitive field -> harmonic coefficients -> C_l -> A_peak`.",
                "Use the typed-transfer theorem to separate the background ratio from the unresolved perturbation/readout block.",
                "Conclude that no theorem may identify the numeric peak-position angle with `100theta_s` alone without an additional peak/readout identification theorem.",
            ),
            scope_boundary=(
                "Boundary theorem only.",
                "Does not itself derive the final `A_peak -> theta_peak` identification law.",
            ),
        ),
        "paper35.late_baryon_counting_law": TheoremNode(
            node_id="paper35.late_baryon_counting_law",
            kind="theorem",
            label="Late-time Baryon-counting Law",
            claim_status="derived / scoped under Premise 2 standard low-temperature baryonic matter",
            statement=(
                "On the late-time baryonic dust sector, "
                "`n_b = rho_b / m_bar * [1 + O(k_B T / (m_p c^2))]`, so the "
                "surviving normalization ambiguity is the standard mean-baryon-mass "
                "convention rather than an open IO-side bridge."
            ),
            scope="Late-time baryon-number conversion on the active branch.",
            authority_paths=(),
            depends_on=("premise.2", "paper21.branch_assignment"),
            premises=(
                "`premise.2` licenses standard low-temperature baryonic matter inside the horizon.",
                "`paper21.branch_assignment` fixes the active branch and its carried `omega_b,geom` slot.",
            ),
            proof_outline=(
                "Treat the late-time matter sector as nonrelativistic baryonic dust on the active branch.",
                "Convert rest-mass density to baryon number density with the standard mean mass per baryon.",
                "Keep the remaining normalization ambiguity explicit as a standard mass convention rather than an unresolved framework theorem gap.",
            ),
            scope_boundary=(
                "Late-time baryonic dust sector only.",
                "Does not provide a primordial/source-era baryogenesis theorem.",
            ),
            notes=(
                "No published paper reference is used here; the theorem text is carried self-contained in the calculator dictionary.",
            ),
        ),
        "paper35.eta_io_late_closure": TheoremNode(
            node_id="paper35.eta_io_late_closure",
            kind="theorem",
            label="Late-time eta_IO Closure Theorem",
            claim_status="derived / scoped",
            statement=(
                "The preferred late-time baryon-to-photon ratio "
                f"`eta_IO = n_b / n_gamma = {eta_late:.12e}` is closed on the "
                "active branch, equivalently "
                "`eta_IO,late = C_eta(T_obs, m_bar) * omega_b,geom`."
            ),
            scope="Late-time baryon-to-photon ratio convention used by the calculator.",
            authority_paths=(),
            depends_on=("paper21.branch_assignment", "paper35.late_baryon_counting_law"),
            premises=(
                "`paper21.branch_assignment` fixes the active branch package.",
                "`paper35.late_baryon_counting_law` converts the carried mass density to baryon number density on the late-time dust sector.",
                "The calculator needs one carried late-time `eta_IO` convention rather than multiple unresolved conventions.",
            ),
            proof_outline=(
                "Start from the active-branch physical-density slot `omega_b,geom` together with the late-time baryon-counting law.",
                "Convert the active-branch baryon density and observed CMB temperature into the baryon-to-photon prefactor `C_eta(T_obs, m_bar)`.",
                "Fix the preferred exported `eta_IO,late` convention to that closed branch value.",
                "Expose the convention directly through the calculator and bundle.",
            ),
            scope_boundary=(
                "Preferred late-time `eta_IO` convention on the active branch.",
                "Does not claim that every alternative mass convention is closed to theorem grade.",
            ),
            notes=(
                "No published paper reference is used here; the theorem text is carried self-contained in the calculator dictionary.",
            ),
        ),
        "paper36.phase_equivalent_selector": TheoremNode(
            node_id="paper36.phase_equivalent_selector",
            kind="theorem",
            label="Phase-equivalent Selector Theorem",
            claim_status="derived / scoped",
            statement=(
                "The strict-bare selector backbone solves "
                "`theta_bare(z_sel) = r_s(z_sel) / D_M(z_sel)` on the certified "
                "monotone interval and carries observer-side angle by "
                "`theta_obs = J_theta theta_bare` with fixed `J_theta`."
            ),
            scope="Strict-bare phase-ruler selector backbone.",
            authority_paths=(str(AUTHORITY_PATHS["paper36_phase_selector"]),),
            depends_on=("premise.1", "premise.2", "paper21.branch_assignment"),
            premises=(
                "`premise.1` and `premise.2` fix the IO setting.",
                "`paper21.branch_assignment` fixes the active branch package on which the selector is evaluated.",
                "The strict-bare selector interval is certified monotone on its published domain.",
            ),
            proof_outline=(
                "Use the certified monotone interval to make the strict-bare selector exactly invertible on the published branch domain.",
                "Map the selected bare phase-ruler leaf to observer-side `theta` with the fixed Jacobian `J_theta`.",
                "Reduce theorem-grade numeric `theta_*` to identifying the physical selector leaf carried by the active branch.",
            ),
            scope_boundary=(
                "Strict-bare selector backbone on the certified interval.",
                "Does not by itself identify which leaf is physical on the active branch.",
            ),
        ),
        "paper37.packet_coefficient_fixing": TheoremNode(
            node_id="paper37.packet_coefficient_fixing",
            kind="theorem",
            label="Packet Coefficient Fixing Theorem",
            claim_status="derived / scoped plus verified / support-promoted",
            statement=(
                "The outgoing-update and Ly-line coefficients are fixed on the "
                "surviving packet law by "
                "`xr[1] = 3 x1s Dfplus_Ly[0]` and "
                "`xr[0] = x1s exp(E32 / TR) Dfplus_Ly[1]`, yielding the "
                "support-reduced packet carrier close to the final active endpoint."
            ),
            scope="Packet-law closure on the surviving active endpoint family.",
            authority_paths=(
                str(AUTHORITY_PATHS["paper37_packet_coefficient_fixing"]),
                str(AUTHORITY_PATHS["paper37_packet1500_support_promotion"]),
            ),
            depends_on=("paper36.phase_equivalent_selector",),
            premises=(
                "`paper36.phase_equivalent_selector` reduces `theta_*` closure to fixing the active packet and leaf carrier.",
                "The surviving outgoing-update packet law is constrained by the accepted Paper 37 boundary transport identities.",
            ),
            proof_outline=(
                "Use the outgoing-update and Ly-line boundary transport identities to fix the live packet-law coefficients rather than fitting them.",
                "Construct the support-reduced packet carrier on the surviving active endpoint family with those fixed coefficients.",
                "Show that the reduced carrier lands very close to the final active endpoint while keeping the coefficients theorem-governed.",
            ),
            scope_boundary=(
                "Packet-law closure on the surviving active endpoint family.",
                "Does not yet prove that the surviving packet alone carries the physical selector leaf.",
            ),
        ),
        "paper37.highz_tail_slaving": TheoremNode(
            node_id="paper37.highz_tail_slaving",
            kind="theorem",
            label="High-z Tail Slaving Theorem",
            claim_status="derived / scoped plus verified / support sharpening",
            statement=(
                "Support above `z ~ 1500` is demoted to a slaved residual tail "
                "rather than an independent selector-bearing sector, with the "
                "reduced packet differing from the full endpoint family only by "
                "`Delta_theta = +5.386582264233e-06` and "
                "`Delta_ell = -4.390006880612e-04`."
            ),
            scope="Endpoint-family support decomposition.",
            authority_paths=(str(AUTHORITY_PATHS["paper37_highz_tail_slaving"]),),
            depends_on=("paper37.packet_coefficient_fixing",),
            premises=(
                "`paper37.packet_coefficient_fixing` isolates the live packet carrier near the active endpoint.",
                "Any support above `z ~ 1500` still has to be checked for an independent selector-bearing branch.",
            ),
            proof_outline=(
                "Audit the continuation of the active endpoint family above the reduced packet support.",
                "Show that the remaining high-`z` contribution is slaved to the packet carrier rather than introducing a second independent selector sector.",
                "Demote the high-`z` continuation to a residual tail in the active-branch support decomposition.",
            ),
            scope_boundary=(
                "Support decomposition on the active endpoint family.",
                "Does not by itself identify the physical selector leaf.",
            ),
        ),
        "paper37.peak_window_tail_profile_audit": TheoremNode(
            node_id="paper37.peak_window_tail_profile_audit",
            kind="audit",
            label="Peak-window Tail Profile Audit",
            claim_status="verified / scoped",
            statement=(
                "After the best pure-amplitude rescale is removed, the residual "
                "first-peak parent-profile mismatch obeys "
                "`RMS_rel[ell in [190,250]] = 2.950052007950388e-06`, so the "
                "remaining tail is not a second active selector-bearing branch."
            ),
            scope="First-peak TT parent-profile audit on the active endpoint family.",
            authority_paths=(str(AUTHORITY_PATHS["paper37_peak_window_tail_profile_audit"]),),
            depends_on=("paper37.highz_tail_slaving",),
            premises=(
                "`paper37.highz_tail_slaving` demotes the high-`z` continuation to a residual tail candidate.",
                "The physical relevance of that tail still has to be checked against the first-peak parent profile.",
            ),
            proof_outline=(
                "Compare the first-peak parent profile with and without the residual tail after removing the best pure-amplitude rescale.",
                "Measure the remaining mismatch on the peak window and show that it is tiny.",
                "Use that audit to rule out the residual tail as a second active selector-bearing branch.",
            ),
            scope_boundary=(
                "First-peak TT parent-profile audit on the active endpoint family.",
                "Verified only on the relevant first-peak window, not as a full-spectrum theorem.",
            ),
        ),
        "paper37.selector_support_promotion": TheoremNode(
            node_id="paper37.selector_support_promotion",
            kind="theorem",
            label="Selector-support Promotion Theorem",
            claim_status="derived / scoped plus verified / carried selector closure",
            statement=(
                "The support-certified cumulative packet `z_cross < 1500` carries "
                "the physical selector leaf on the active branch, fixing "
                f"`z_sel = {theta_star.selector_leaf_z:.12f}`."
            ),
            scope="Carried active-branch physical selector leaf.",
            authority_paths=(str(AUTHORITY_PATHS["paper37_selector_support_promotion"]),),
            depends_on=(
                "paper37.packet_coefficient_fixing",
                "paper37.highz_tail_slaving",
                "paper37.peak_window_tail_profile_audit",
            ),
            premises=(
                "`paper37.packet_coefficient_fixing` provides the support-reduced active carrier.",
                "`paper37.highz_tail_slaving` and `paper37.peak_window_tail_profile_audit` remove the residual tail as an independent selector branch.",
            ),
            proof_outline=(
                "Promote the cumulative packet `z_cross < 1500` from a reduced support object to the carried physical selector carrier on the active branch.",
                "Collapse the old endpoint-family selector interval to the leaf transported by that certified support packet.",
                "Feed the carried leaf back into the Paper 36 selector backbone as the physical active-branch leaf.",
            ),
            scope_boundary=(
                "Carried active-branch physical selector leaf only.",
                "Does not establish a universal selector-promotion theorem off branch.",
            ),
        ),
        "paper37.active_branch_theta_star": TheoremNode(
            node_id="paper37.active_branch_theta_star",
            kind="theorem",
            label="Active-branch Theta-star Theorem",
            claim_status="derived / scoped",
            statement=(
                "Evaluating the exact strict-bare selector backbone at the carried "
                "active selector leaf gives "
                f"`theta_bare = {theta_star.theta_bare_deg:.12f} deg`, "
                f"`theta_obs = {theta_star.theta_obs_deg:.12f} deg`, and "
                f"`100theta_* = {theta_star.theta_star_100:.12f}` on the fixed "
                "active branch package."
            ),
            scope="Fixed active Paper 10 legacy projected branch only.",
            authority_paths=(str(AUTHORITY_PATHS["paper37_active_theta_star"]),),
            depends_on=("paper37.selector_support_promotion", "paper36.phase_equivalent_selector"),
            premises=(
                "`paper37.selector_support_promotion` fixes the carried physical selector leaf on the active branch.",
                "`paper36.phase_equivalent_selector` gives the exact observer-side map from that leaf to `theta_*`.",
            ),
            proof_outline=(
                "Evaluate the exact strict-bare selector backbone at the carried active selector leaf.",
                "Obtain `theta_bare`, transport to `theta_obs` with the fixed Jacobian `J_theta`, and report `100theta_*` for the active branch.",
                "Check the same carried solution against the direct first TT peak observable so the derived number remains tied to the measured peak position.",
            ),
            scope_boundary=(
                "Fixed active Paper 10 legacy projected branch only.",
                "Theorem-grade numeric closure on the carried selector leaf only.",
                "Not a universal off-branch transfer theorem or a full TT/TE/EE solver closure.",
            ),
        ),
    }


def explained_output_specs() -> dict[str, dict[str, Any]]:
    """Return the currently published explained-output families."""

    return {
        "theta_star_theorem": {
            "label": "Theorem-grade active-branch theta_*",
            "claim_status": "derived / scoped",
            "provenance_status": "full",
            "zero_fitted_parameters": True,
            "conditional_on_premises": ["premise.1", "premise.2"],
            "parameters": {},
            "note": (
                "First fully explained calculator output; includes the complete "
                "accepted theorem chain and the direct-observable peak comparison."
            ),
        },
        "branch_rd_mpc": {
            "label": "Active-branch r_d",
            "claim_status": "derived / scoped",
            "provenance_status": "full",
            "zero_fitted_parameters": True,
            "conditional_on_premises": ["premise.1", "premise.2"],
            "parameters": {},
            "note": (
                "Full theorem chain installed for the active-branch pre-drag "
                "ruler, including the sound-speed baryon-slot selector."
            ),
        },
        "eta_io_late": {
            "label": "Late-time eta_IO",
            "claim_status": "derived / scoped",
            "provenance_status": "full",
            "zero_fitted_parameters": True,
            "conditional_on_premises": ["premise.1", "premise.2"],
            "parameters": {},
            "note": (
                "Full theorem chain installed for the preferred late-time "
                "`eta_IO` convention on the active branch."
            ),
        },
        "background_snapshot": {
            "label": "Closed-FRW background snapshot",
            "claim_status": "derived / scoped",
            "provenance_status": "full",
            "zero_fitted_parameters": True,
            "conditional_on_premises": ["premise.1", "premise.2"],
            "parameters": {
                "z": {"type": "float", "default": 0.57, "meaning": "observer-side redshift"}
            },
            "note": (
                "Full theorem chain installed for parameterized background "
                "snapshots, including the carried active-branch `r_d` slot."
            ),
        },
        "recombination_point": {
            "label": "Local recombination primitives at one z",
            "claim_status": "derived / scoped",
            "provenance_status": "full",
            "zero_fitted_parameters": True,
            "conditional_on_premises": ["premise.1", "premise.2"],
            "parameters": {
                "z": {"type": "float", "default": 1100.0, "meaning": "observer-side redshift"},
                "x_e_override": {
                    "type": "float | null",
                    "default": None,
                    "meaning": "optional user-supplied ionization fraction; makes the output conditional",
                },
            },
            "note": (
                "Full theorem chain installed for the default theorem-grade "
                "local-state primitives, with the override path kept explicitly conditional."
            ),
        },
    }


def explain_active_branch_theta_star() -> ExplainedValue:
    """Return the first fully explained published calculator output."""

    theta = compute_active_branch_theta_star()
    direct_peak = ObservableComparison(
        label="First TT peak position",
        claim_status="verified / scoped direct-observable comparison",
        predicted_value=ACTIVE_BRANCH_THETA_STAR_ELL_PEAK,
        observed_reference=OBSERVED_FIRST_TT_PEAK_ELL_REFERENCE,
        delta=ACTIVE_BRANCH_THETA_STAR_ELL_PEAK - OBSERVED_FIRST_TT_PEAK_ELL_REFERENCE,
        units="ell",
        note=(
            "The active-branch carrier peak lies at `ell_peak = 220.475...`, "
            "aligned with the observed first TT peak near `ell ≈ 220`. The "
            "direct observable agrees even though the extracted `100theta_*` "
            "depends on the geometry used in the transfer map."
        ),
        source_note=(
            "Paper 37 packet1500/selector-support chain for the IO carrier, "
            "compared against the observed first TT peak near `ell ≈ 220`."
        ),
    )
    return ExplainedValue(
        output_id="theta_star_theorem",
        label="Theorem-grade active-branch theta_*",
        primary_key="theta_star_100",
        primary_value=theta.theta_star_100,
        units="100theta_*",
        claim_status=(
            "derived / scoped, zero fitted parameters, conditional on Premises 1 and 2"
        ),
        provenance_status="full",
        payload={
            **theta.as_dict(),
            "ell_peak": ACTIVE_BRANCH_THETA_STAR_ELL_PEAK,
            "observed_first_peak_ell_reference": OBSERVED_FIRST_TT_PEAK_ELL_REFERENCE,
            "first_peak_delta": (
                ACTIVE_BRANCH_THETA_STAR_ELL_PEAK - OBSERVED_FIRST_TT_PEAK_ELL_REFERENCE
            ),
        },
        scope_boundary=(
            "Fixed active Paper 10 legacy projected branch only.",
            "Theorem-grade numeric closure on the carried selector leaf only.",
        ),
        conditional_on=("premise.1", "premise.2"),
        provenance_root_id="paper37.active_branch_theta_star",
        chain_ids=(
            "premise.1",
            "premise.2",
            "paper21.branch_assignment",
            "paper36.phase_equivalent_selector",
            "paper37.packet_coefficient_fixing",
            "paper37.highz_tail_slaving",
            "paper37.peak_window_tail_profile_audit",
            "paper37.selector_support_promotion",
            "paper37.active_branch_theta_star",
        ),
        premise_ids=("premise.1", "premise.2"),
        supporting_node_ids=("paper32.closed_s3_solver_spec",),
        zero_fitted_parameters=True,
        non_claims=(
            "Not a universal off-branch transfer theorem.",
            "Not a universal reduction theorem for arbitrary TT parent-profile deformations.",
            "Not a theorem-grade full TT/TE/EE solver closure.",
        ),
        notes=(
            "This number is published as a theorem-grade calculator output.",
            "The direct observable is the first TT peak location; `100theta_*` is a geometry-dependent extraction.",
        ),
        geometry_explanation=(
            "This number differs from Planck's reported value because Planck "
            "assumes flat space in its standard `K=0` extraction convention, "
            "while the IO framework derives a closed `K=+1` geometry and "
            "evaluates the active-branch selector leaf there. The direct "
            "observable is the peak position. On that direct observable, the "
            "active-branch carrier agrees with the measured first TT peak near "
            "`ell ≈ 220`."
        ),
        comparison_context={
            "planck_flat_reference_theta_mc_100": PLANCK_FLAT_REFERENCE_THETA_MC_100,
            "planck_closed_reference_theta_mc_100": PLANCK_CLOSED_REFERENCE_THETA_MC_100,
            "planck_closed_reference_omegak": PLANCK_CLOSED_REFERENCE_OMEGA_K,
            "statement": (
                "Planck's own non-flat refits keep `100theta_MC` near `1.0411`, "
                "so the IO calculator presents its `100theta_*` as a competing "
                "closed-geometry derivation rather than as a tension in the "
                "direct first-peak observable."
            ),
        },
        direct_observable_comparisons=(direct_peak,),
    )


def explain_branch_rd_mpc() -> ExplainedValue:
    """Return the full explained value for the active-branch `r_d`."""

    return ExplainedValue(
        output_id="branch_rd_mpc",
        label="Active-branch pre-drag ruler",
        primary_key="r_d_mpc",
        primary_value=ACTIVE_BRANCH.rd_mpc,
        units="Mpc",
        claim_status="derived / scoped active-branch published ruler",
        provenance_status="full",
        payload={
            "branch_label": ACTIVE_BRANCH.label,
            "r_d_mpc": ACTIVE_BRANCH.rd_mpc,
        },
        scope_boundary=(
            "Fixed active branch package only.",
            "Published pre-drag ruler slot carried by the live BAO/background surface.",
        ),
        conditional_on=("premise.1", "premise.2"),
        provenance_root_id="paper31.geometric_pre_drag_ruler",
        chain_ids=(
            "premise.1",
            "premise.2",
            "paper21.branch_assignment",
            "paper29.sound_speed_selector",
            "paper31.geometric_pre_drag_ruler",
        ),
        premise_ids=("premise.1", "premise.2"),
        zero_fitted_parameters=True,
        notes=(
            "This is the theorem-grade pre-drag ruler used by the live BAO ratios.",
            "The sound-speed baryon slot is fixed before the ruler is carried into the calculator surface.",
        ),
    )


def explain_eta_io_late() -> ExplainedValue:
    """Return the full explained value for `eta_IO,late`."""

    value = late_eta_io()
    return ExplainedValue(
        output_id="eta_io_late",
        label="Late-time eta_IO",
        primary_key="eta_IO_late",
        primary_value=value,
        units=None,
        claim_status="derived / scoped preferred Paper 35 late-time convention",
        provenance_status="full",
        payload={
            "branch_label": ACTIVE_BRANCH.label,
            "eta_IO_late": value,
        },
        scope_boundary=(
            "Preferred late-time `eta_IO` convention on the active branch.",
            "Late-time baryonic dust sector only; not a primordial freeze-out theorem.",
        ),
        conditional_on=("premise.1", "premise.2"),
        provenance_root_id="paper35.eta_io_late_closure",
        chain_ids=(
            "premise.1",
            "premise.2",
            "paper21.branch_assignment",
            "paper35.late_baryon_counting_law",
            "paper35.eta_io_late_closure",
        ),
        premise_ids=("premise.1", "premise.2"),
        zero_fitted_parameters=True,
        notes=(
            "This is the preferred late-time calculator convention for `eta_IO`.",
            "The chain closes on the active branch without introducing fitted cosmological parameters.",
        ),
    )


def explain_background_snapshot(z: float) -> ExplainedValue:
    """Return a full explained background snapshot at one redshift."""

    model = CurvedBackgroundModel()
    snapshot = model.snapshot(z)
    snapshot["eta_IO_late"] = late_eta_io()
    return ExplainedValue(
        output_id="background_snapshot",
        label="Closed-FRW background snapshot",
        primary_key="DM_mpc",
        primary_value=snapshot["DM_mpc"],
        units="Mpc",
        claim_status="derived / scoped active-branch background snapshot",
        provenance_status="full",
        payload={"z": z, **snapshot},
        scope_boundary=(
            "Closed-FRW observer-side background geometry on the fixed active branch.",
            "BAO ratios inherit the carried active-branch `r_d` slot.",
        ),
        conditional_on=("premise.1", "premise.2"),
        provenance_root_id="paper30.background_surface",
        chain_ids=(
            "premise.1",
            "premise.2",
            "paper21.branch_assignment",
            "paper30.background_surface",
            "paper29.sound_speed_selector",
            "paper31.geometric_pre_drag_ruler",
        ),
        premise_ids=("premise.1", "premise.2"),
        zero_fitted_parameters=True,
        notes=(
            "This snapshot is evaluated on the theorem-grade active closed-FRW branch.",
            "The BAO ratios in the payload inherit the carried pre-drag ruler `r_d`.",
        ),
    )


def explain_recombination_point(
    z: float,
    x_e_override: float | None = None,
) -> ExplainedValue:
    """Return a full explained recombination-point payload."""

    state = local_background_state(z)
    x_e = saha_equilibrium_xe(z) if x_e_override is None else x_e_override
    claim_status = (
        "derived / scoped local recombination primitives on omega_b,geom"
        if x_e_override is None
        else "conditional on supplied ionization fraction over a derived local background state map"
    )
    chain_ids = (
        (
            "premise.1",
            "premise.2",
            "paper21.branch_assignment",
            "paper31.baryon_assignment",
            "paper29.sound_speed_selector",
            "paper31.local_background_state_map",
            "local.saha_seed",
            "paper31.recombination_clock_transport",
        )
        if x_e_override is None
        else (
            "premise.1",
            "premise.2",
            "paper21.branch_assignment",
            "paper31.baryon_assignment",
            "paper29.sound_speed_selector",
            "paper31.local_background_state_map",
            "paper31.recombination_clock_transport",
        )
    )
    notes = (
        "Uses the local Saha seed when no override is supplied.",
        "Setting `x_e_override` changes the chemistry-dependent rows from derived to conditional.",
    )
    return ExplainedValue(
        output_id="recombination_point",
        label="Local recombination primitives at one redshift",
        primary_key="kappa_prime_loc",
        primary_value=primitive_local_kappa_prime(z, x_e),
        units=None,
        claim_status=claim_status,
        provenance_status="full",
        payload={
            "z": z,
            "x_e": x_e,
            "u": state.u,
            "a_loc_m": state.a_loc_m,
            "H_loc_s_inv": state.H_loc_s_inv,
            "T_r_loc_K": state.T_r_loc_K,
            "n_H_geom_m3": hydrogen_number_density_m3(z),
            "n_e_m3": free_electron_density_m3(z, x_e),
            "kappa_prime_loc": primitive_local_kappa_prime(z, x_e),
            "d_tau_obs_dz": optical_depth_gradient_per_redshift(z, x_e),
            "Gamma_T_over_H_loc": local_scattering_to_expansion_ratio(z, x_e),
            "R_local_geom": local_baryon_loading_R(z),
            "c_s_local_m_s": local_sound_speed_m_s(z),
        },
        scope_boundary=(
            "Derived local background-state map on the active branch.",
            "Chemistry-dependent quantities are derived only when `x_e` comes from the local Saha seed.",
            "Local `R` and `c_s` rows inherit the theorem-grade `omega_b,geom` sound-speed slot.",
        ),
        conditional_on=("premise.1", "premise.2"),
        provenance_root_id="paper31.recombination_clock_transport",
        chain_ids=chain_ids,
        premise_ids=("premise.1", "premise.2"),
        zero_fitted_parameters=x_e_override is None,
        notes=notes,
    )


def published_explained_outputs() -> dict[str, dict[str, Any]]:
    """Return the default explained-output bundle shipped to the web surface."""

    nodes = theorem_graph()
    return {
        "theta_star_theorem": explain_active_branch_theta_star().as_dict(nodes=nodes),
        "branch_rd_mpc": explain_branch_rd_mpc().as_dict(nodes=nodes),
        "eta_io_late": explain_eta_io_late().as_dict(nodes=nodes),
        "background_snapshot_z_0_57": explain_background_snapshot(0.57).as_dict(nodes=nodes),
        "recombination_point_z_1100": explain_recombination_point(1100.0).as_dict(nodes=nodes),
    }


__all__ = [
    "ACTIVE_BRANCH_THETA_STAR_ELL_PEAK",
    "ExplainedValue",
    "ObservableComparison",
    "TheoremNode",
    "explain_active_branch_theta_star",
    "explain_background_snapshot",
    "explain_branch_rd_mpc",
    "explain_eta_io_late",
    "explain_recombination_point",
    "explained_output_specs",
    "published_explained_outputs",
    "theorem_graph",
]

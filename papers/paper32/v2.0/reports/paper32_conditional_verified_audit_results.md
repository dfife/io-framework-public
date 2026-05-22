# Paper 32 CONDITIONAL_VERIFIED audit results

Status: `discipline audit / index`, not a theorem surface

## Scope

- theorem-named files scanned: `108`
- excluded non-theorem infrastructure files: `3`
  - `paper32_bounce_theorem_grade_upgrade_program_report.md`
  - `paper32_cosmo_late_time_theorem_memo.md`
  - `paper32_s8_theorem_supported_internal_point_memo.md`
- active theorem-report / theorem-package surfaces audited: `105`
- touched upstream theorem/report nodes inline-verified: `32`
- touched auxiliary files excluded from inline verification: `2`
  - `/opt/cosmology-lab/results/paper25/paper25_degree_theorem_identity_pin_reconciliation_analysis.py`
  - `/opt/cosmology-lab/results/paper29/paper29_sound_speed_baryon_selector_audit_report.md`

## Summary

- theorem surfaces audited: `105`
- `CLEAN`: `46`
- `CONDITIONAL_VERIFIED`: `58`
- `NEEDS_REVIEW`: `1`
- `CIRCULAR`: `0`
- rule enforced: only `CLEAN` and `CONDITIONAL_VERIFIED` theorems may be cited as premises

## Paper 32 per-theorem outcomes

| File | Result | Admissions surfaced | Notes |
|---|---|---|---|
| `paper32_baryon_loading_no_single_slot_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_bounce_theorem_grade_upgrade_closure_report.md` | `CONDITIONAL_VERIFIED` | ADMITTED_EXTENSION(Paper 32 extended fermionic/chiral IO-EC theory); ADMITTED_HIGH_DENSITY_CRITERION(imported high-density bounce attachment criterion) | Extension-side theorem surface; theorem-grade only after surfacing the explicit Paper 32 extension axioms. |
| `paper32_bridge_selection_and_typed_gmp_theorems.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_continuous_bridge_cycle_consistency_selector_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_SELECTOR_RULE(cycle-consistency at the recurrent support radius on the continuous bridge family) | Post-bounce closure is conditional on surfaced selector principles or bridge-family admissions. |
| `paper32_extended_io_ec_normalization_theorem_report.md` | `CONDITIONAL_VERIFIED` | ADMITTED_EXTENSION(Paper 32 extended fermionic/chiral IO-EC theory) | Extension-side theorem surface; theorem-grade only after surfacing the explicit Paper 32 extension axioms. |
| `paper32_fermionic_bridge_centered_occupancy_theorem_report.md` | `CONDITIONAL_VERIFIED` | ADMITTED_EXTENSION(Paper 32 extended fermionic/chiral IO-EC theory) | Extension-side theorem surface; theorem-grade only after surfacing the explicit Paper 32 extension axioms. |
| `paper32_fermionic_bridge_kms_casimir_normalization_theorem_report.md` | `CONDITIONAL_VERIFIED` | ADMITTED_EXTENSION(Paper 32 extended fermionic/chiral IO-EC theory) | Extension-side theorem surface; theorem-grade only after surfacing the explicit Paper 32 extension axioms. |
| `paper32_fermionic_bridge_minimal_normalization_uniqueness_theorem_report.md` | `CONDITIONAL_VERIFIED` | ADMITTED_EXTENSION(Paper 32 extended fermionic/chiral IO-EC theory); ADMITTED_NEW_PRINCIPLE_FAMILY(minimal admissible new-principle family on the chiral J=1/2 bridge quotient) | Extension-side theorem surface; theorem-grade only after surfacing the explicit Paper 32 extension axioms. |
| `paper32_fermionic_bridge_support_conformal_descent_theorem_report.md` | `CONDITIONAL_VERIFIED` | ADMITTED_EXTENSION(Paper 32 extended fermionic/chiral IO-EC theory) | Extension-side theorem surface; theorem-grade only after surfacing the explicit Paper 32 extension axioms. |
| `paper32_growth_background_assignment_closure_theorem_report.md` | `CONDITIONAL_VERIFIED` | ADMITTED_ACTIVE_BRANCH(Paper 10 legacy branch solver instantiation) | Conditional only on the surfaced active legacy branch. |
| `paper32_hidden_bulk_21cm_reduced_bridge_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_CLASS(restricted hidden-bulk localized family / handoff-packet class); ADMITTED_CLASS(reduced 21-cm late-probe class on the same IO branch) | Hidden-bulk closure survives only on the surfaced restricted family and late-law admissions. |
| `paper32_hidden_bulk_continuation_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_hidden_bulk_cross_era_bridge_nogo_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_CLASS(restricted hidden-bulk localized family / handoff-packet class); ADMITTED_LATE_LAW(fixed or reduced late local source/heating family) | Hidden-bulk closure survives only on the surfaced restricted family and late-law admissions. |
| `paper32_hidden_bulk_initial_data_bridge_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_CLASS(restricted hidden-bulk localized family / handoff-packet class); ADMITTED_LATE_LAW(fixed or reduced late local source/heating family) | Hidden-bulk closure survives only on the surfaced restricted family and late-law admissions. |
| `paper32_hidden_bulk_joint_selector_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_CLASS(restricted hidden-bulk localized family / handoff-packet class); ADMITTED_LATE_LAW(fixed or reduced late local source/heating family) | Hidden-bulk closure survives only on the surfaced restricted family and late-law admissions. |
| `paper32_hidden_bulk_late_probe_coupling_nogo_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_hidden_bulk_lya_concrete_bridge_nogo_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_CLASS(restricted hidden-bulk localized family / handoff-packet class); ADMITTED_EXTERNAL_CLASS(imported or reduced Ly-alpha late-law family admissible under Premise 2) | Hidden-bulk closure survives only on the surfaced restricted family and late-law admissions. |
| `paper32_hidden_bulk_lya_conditional_bridge_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_CLASS(restricted hidden-bulk localized family / handoff-packet class); ADMITTED_EXTERNAL_CLASS(imported or reduced Ly-alpha late-law family admissible under Premise 2) | Hidden-bulk closure survives only on the surfaced restricted family and late-law admissions. |
| `paper32_hidden_bulk_lya_imported_family_bridge_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_CLASS(restricted hidden-bulk localized family / handoff-packet class); ADMITTED_EXTERNAL_CLASS(imported or reduced Ly-alpha late-law family admissible under Premise 2) | Hidden-bulk closure survives only on the surfaced restricted family and late-law admissions. |
| `paper32_hidden_bulk_lya_ionization_lift_nogo_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_hidden_bulk_lya_photoheating_reduction_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_CLASS(restricted hidden-bulk localized family / handoff-packet class); ADMITTED_EXTERNAL_CLASS(imported or reduced Ly-alpha late-law family admissible under Premise 2) | Hidden-bulk closure survives only on the surfaced restricted family and late-law admissions. |
| `paper32_hidden_bulk_lya_thermal_lift_nogo_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_CLASS(restricted hidden-bulk localized family / handoff-packet class); ADMITTED_EXTERNAL_CLASS(imported or reduced Ly-alpha late-law family admissible under Premise 2) | Hidden-bulk closure survives only on the surfaced restricted family and late-law admissions. |
| `paper32_hidden_bulk_minimal_late_family_selector_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_CLASS(restricted hidden-bulk localized family / handoff-packet class); ADMITTED_LATE_LAW(fixed or reduced late local source/heating family) | Hidden-bulk closure survives only on the surfaced restricted family and late-law admissions. |
| `paper32_hidden_bulk_operator_selection_nogo_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_hidden_bulk_recombination_coupling_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_hidden_bulk_recombination_response_rank_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_hidden_bulk_recombination_selector_nogo_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_hidden_bulk_reparameterization_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_hidden_bulk_two_parameter_selector_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_hidden_identification_repair_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_NORMALIZATION(P4 fixed-point normalization Z(e^x)=Q remains the explicit surviving premise) | Repair theorem is conditional on the remaining explicit P4 normalization premise. |
| `paper32_horizon_confinement_piston_nogo_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_horizon_support_clamp_bounce_attachment_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_BRANCH(fixed support-clamped hidden branch / ordinary post-clamp continuation class); ADMITTED_HIGH_DENSITY_CRITERION(imported high-density bounce attachment criterion) | Support-clamp theorem is conditional on the surfaced fixed-branch continuation class. |
| `paper32_horizon_support_clamp_clock_handoff_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_horizon_support_clamp_cooling_dominance_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_BRANCH(fixed support-clamped hidden branch / ordinary post-clamp continuation class) | Support-clamp theorem is conditional on the surfaced fixed-branch continuation class. |
| `paper32_horizon_support_clamp_expansion_kinetic_nogo_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_horizon_support_clamp_full_offload_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_BRANCH(fixed support-clamped hidden branch / ordinary post-clamp continuation class) | Support-clamp theorem is conditional on the surfaced fixed-branch continuation class. |
| `paper32_horizon_support_clamp_hot_ionization_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_BRANCH(fixed support-clamped hidden branch / ordinary post-clamp continuation class) | Support-clamp theorem is conditional on the surfaced fixed-branch continuation class. |
| `paper32_horizon_support_clamp_local_acceleration_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_horizon_support_clamp_local_cycle_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_BRANCH(fixed support-clamped hidden branch / ordinary post-clamp continuation class) | Support-clamp theorem is conditional on the surfaced fixed-branch continuation class. |
| `paper32_horizon_support_clamp_local_recollapse_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_horizon_support_clamp_mev_sector_density_nogo_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_horizon_support_clamp_minimal_thermalization_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_BRANCH(fixed support-clamped hidden branch / ordinary post-clamp continuation class); ADMITTED_RECEIVER(minimal thermal receiver realization) | Support-clamp theorem is conditional on the surfaced fixed-branch continuation class. |
| `paper32_horizon_support_clamp_nuclear_sink_nogo_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_BRANCH(fixed support-clamped hidden branch / ordinary post-clamp continuation class) | Support-clamp theorem is conditional on the surfaced fixed-branch continuation class. |
| `paper32_horizon_support_clamp_pair_equilibrium_nogo_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_BRANCH(fixed support-clamped hidden branch / ordinary post-clamp continuation class); ADMITTED_CONTINUATION(relativistic plasma / near-equilibrium continuation class) | Support-clamp theorem is conditional on the surfaced fixed-branch continuation class. |
| `paper32_horizon_support_clamp_phase_lift_cycle_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_BRANCH(fixed support-clamped hidden branch / ordinary post-clamp continuation class) | Support-clamp theorem is conditional on the surfaced fixed-branch continuation class. |
| `paper32_horizon_support_clamp_positive_pressure_recollapse_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_BRANCH(fixed support-clamped hidden branch / ordinary post-clamp continuation class); ADMITTED_CONTINUATION(ordinary positive-pressure perfect-fluid continuation) | Support-clamp theorem is conditional on the surfaced fixed-branch continuation class. |
| `paper32_horizon_support_clamp_recollapse_upper_bound_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_BRANCH(fixed support-clamped hidden branch / ordinary post-clamp continuation class); ADMITTED_CONTINUATION(ordinary positive-pressure perfect-fluid continuation) | Support-clamp theorem is conditional on the surfaced fixed-branch continuation class. |
| `paper32_horizon_support_clamp_relativistic_threshold_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_BRANCH(fixed support-clamped hidden branch / ordinary post-clamp continuation class); ADMITTED_CONTINUATION(relativistic plasma / near-equilibrium continuation class) | Support-clamp theorem is conditional on the surfaced fixed-branch continuation class. |
| `paper32_horizon_support_clamp_sparse_relativistic_plasma_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_BRANCH(fixed support-clamped hidden branch / ordinary post-clamp continuation class); ADMITTED_CONTINUATION(relativistic plasma / near-equilibrium continuation class) | Support-clamp theorem is conditional on the surfaced fixed-branch continuation class. |
| `paper32_horizon_support_clamp_support_observable_cycle_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_BRANCH(fixed support-clamped hidden branch / ordinary post-clamp continuation class) | Support-clamp theorem is conditional on the surfaced fixed-branch continuation class. |
| `paper32_horizon_support_clamp_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_BRANCH(fixed support-clamped hidden branch / ordinary post-clamp continuation class) | Support-clamp theorem is conditional on the surfaced fixed-branch continuation class. |
| `paper32_horizon_support_clamp_weak_sink_nogo_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_BRANCH(fixed support-clamped hidden branch / ordinary post-clamp continuation class) | Support-clamp theorem is conditional on the surfaced fixed-branch continuation class. |
| `paper32_informational_singularity_torsion_bounce_nogo_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_late_time_linear_clustering_inheritance_theorem_report.md` | `CONDITIONAL_VERIFIED` | ADMITTED_ACTIVE_BRANCH(Paper 10 legacy branch solver instantiation) | Conditional only on the surfaced active legacy branch. |
| `paper32_modular_dtn_field_transfer_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_observer_cosmology_termination_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_observer_readout_transition_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_p4_alpha_class_repair_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_p4_collar_cell_identification_theorem.md` | `NEEDS_REVIEW` | ADMITTED_REJECTED_ROUTE(rejected collar-cell identification closure) | Superseded/rejected collar-cell closure; not a live citeable theorem surface. |
| `paper32_p4_direct_class_assault_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_p4_direct_final_assault_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_p4_gaussian_gluing_determinant_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_p4_haar_cell_character_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_p4_haar_route_repair_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_p4_hidden_assumption_no_go_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_p4_microlocal_transport_channel_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_p4_product_compatibility_no_go_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_p4_source_class_lock_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_p4_unconditional_global_nogo_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_post_bounce_bridge_dichotomy_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_SELECTOR_RULE(post-bounce observer-bridge / semantic-restoration selector principles) | Post-bounce closure is conditional on surfaced selector principles or bridge-family admissions. |
| `paper32_post_bounce_clamp_continuity_mistyping_nogo_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_post_bounce_dual_scalar_packages_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_post_bounce_full_observer_return_nogo_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_post_bounce_full_scalar_dictionary_conditional_closure_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_SELECTOR_RULE(post-bounce observer-bridge / semantic-restoration selector principles) | Post-bounce closure is conditional on surfaced selector principles or bridge-family admissions. |
| `paper32_post_bounce_hard_scalar_selector_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_SELECTOR_RULE(post-bounce observer-bridge / semantic-restoration selector principles) | Post-bounce closure is conditional on surfaced selector principles or bridge-family admissions. |
| `paper32_post_bounce_minimal_observer_kinematic_package_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_SELECTOR_RULE(post-bounce observer-bridge / semantic-restoration selector principles) | Post-bounce closure is conditional on surfaced selector principles or bridge-family admissions. |
| `paper32_post_bounce_observer_bridge_family_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_SELECTOR_RULE(post-bounce observer-bridge / semantic-restoration selector principles) | Post-bounce closure is conditional on surfaced selector principles or bridge-family admissions. |
| `paper32_post_bounce_observer_bridge_selection_criterion_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_post_bounce_observer_dictionary_factorization_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_SELECTOR_RULE(post-bounce observer-bridge / semantic-restoration selector principles) | Post-bounce closure is conditional on surfaced selector principles or bridge-family admissions. |
| `paper32_post_bounce_observer_restart_morphology_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_post_bounce_optical_branch_family_nogo_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_post_bounce_optical_branch_two_parameter_reduction_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_SELECTOR_RULE(post-bounce observer-bridge / semantic-restoration selector principles); ADMITTED_FAMILY(seed optical-chemistry branch family on the post-bounce side) | Post-bounce closure is conditional on surfaced selector principles or bridge-family admissions. |
| `paper32_post_bounce_optical_moment_selector_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_SELECTOR_RULE(post-bounce observer-bridge / semantic-restoration selector principles); ADMITTED_SELECTOR_RULE(optical moment selector on the residual two-parameter branch) | Post-bounce closure is conditional on surfaced selector principles or bridge-family admissions. |
| `paper32_post_bounce_scalar_package_dichotomy_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_SELECTOR_RULE(post-bounce observer-bridge / semantic-restoration selector principles) | Post-bounce closure is conditional on surfaced selector principles or bridge-family admissions. |
| `paper32_post_bounce_semantic_clock_restoration_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_SELECTOR_RULE(post-bounce observer-bridge / semantic-restoration selector principles) | Post-bounce closure is conditional on surfaced selector principles or bridge-family admissions. |
| `paper32_post_bounce_semantic_hard_preference_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_SELECTOR_RULE(post-bounce observer-bridge / semantic-restoration selector principles) | Post-bounce closure is conditional on surfaced selector principles or bridge-family admissions. |
| `paper32_post_bounce_semantic_x_restoration_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_SELECTOR_RULE(post-bounce observer-bridge / semantic-restoration selector principles) | Post-bounce closure is conditional on surfaced selector principles or bridge-family admissions. |
| `paper32_post_bounce_soft_scalar_full_cycle_selector_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_SELECTOR_RULE(post-bounce observer-bridge / semantic-restoration selector principles) | Post-bounce closure is conditional on surfaced selector principles or bridge-family admissions. |
| `paper32_post_bounce_soft_scalar_return_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_SELECTOR_RULE(post-bounce observer-bridge / semantic-restoration selector principles) | Post-bounce closure is conditional on surfaced selector principles or bridge-family admissions. |
| `paper32_post_boundary_bulk_transition_law_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_post_boundary_effective_quotient_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_CLASS(reduced post-boundary late-family quotient on the admissible three-probe branch) | Post-boundary theorem closes only after surfacing the reduced late-family / imported-history admission. |
| `paper32_post_boundary_finite_family_closure_criterion_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_EXTERNAL_CLASS(imported finite-dimensional late source/heating family) | Post-boundary theorem closes only after surfacing the reduced late-family / imported-history admission. |
| `paper32_post_boundary_finite_family_realization_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_EXTERNAL_CLASS(imported finite-dimensional late source/heating family) | Post-boundary theorem closes only after surfacing the reduced late-family / imported-history admission. |
| `paper32_post_boundary_friedmann_typing_nogo_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_post_boundary_full_late_family_selection_nogo_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_post_boundary_lambda_typing_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_post_boundary_probe_hierarchy_eos_typing_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_reionization_reduced_history_closure_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_EXTERNAL_CLASS(admissible transported reionization observable-history branch) | Post-boundary theorem closes only after surfacing the reduced late-family / imported-history admission. |
| `paper32_s3_native_solver_specification_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_EXTERNAL_CLASS(reduced or imported reionization-history block on the same IO branch) | Post-boundary theorem closes only after surfacing the reduced late-family / imported-history admission. |
| `paper32_s8_complement_power_lattice_theorem_report.md` | `CONDITIONAL_VERIFIED` | ADMITTED_SELECTOR_CLASS(finite type-preserving one-slot complement-insertion selector class) | Post-boundary theorem closes only after surfacing the reduced late-family / imported-history admission. |
| `paper32_support_attached_observer_bridge_nogo_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_support_attached_observer_reactivation_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_SELECTOR_RULE(post-bounce observer-bridge / semantic-restoration selector principles) | Post-bounce closure is conditional on surfaced selector principles or bridge-family admissions. |
| `paper32_surviving_probe_operator_coupling_nogo_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |
| `paper32_tracial_collapse_cycle_assault_theorem.md` | `CONDITIONAL_VERIFIED` | ADMITTED_CONTINUATION(postulated pure-radiation continuation at x_crit) | Cycle assault remains conditional on the explicit postulated radiation-like continuation. |
| `paper32_typed_boundary_to_bulk_projection_theorem.md` | `CLEAN` | none | Current-stack scoped theorem or no-go with no surfaced admission. |

## Inline-verified theorem/report nodes from other papers touched by the Paper 32 chain

- `/opt/cosmology-lab/results/paper18/paper18_bdp_gap_closure_report.txt`
- `/opt/cosmology-lab/results/paper18/paper18_bdp_theorem_report.txt`
- `/opt/cosmology-lab/results/paper22/paper22_spatial_hodge_complex_report.txt`
- `/opt/cosmology-lab/results/paper25/paper25_v_vs_vprime_class_membership_report.txt`
- `/opt/cosmology-lab/results/paper28/paper28_io_dtn_subprincipal_report.md`
- `/opt/cosmology-lab/results/paper28/paper28_relative_kernel_one_slot_theorem_report.md`
- `/opt/cosmology-lab/results/paper29/paper29_direct_hz_confrontation_report.txt`
- `/opt/cosmology-lab/results/paper29/paper29_hubble_tension_actual_geometry_correction_report.txt`
- `/opt/cosmology-lab/results/paper29/paper29_schur_branch_observables_recompute_report.txt`
- `/opt/cosmology-lab/results/paper3/paper3_table1_expanding_recompute_report.txt`
- `/opt/cosmology-lab/results/paper31/paper31_active_scalar_full_window_closure_theorem.md`
- `/opt/cosmology-lab/results/paper31/paper31_cmb_acoustic_hierarchy_separation_theorem.md`
- `/opt/cosmology-lab/results/paper31/paper31_cmb_acoustic_operator_family_theorem_report.txt`
- `/opt/cosmology-lab/results/paper31/paper31_cmb_lya_21cm_complement_theorem.md`
- `/opt/cosmology-lab/results/paper31/paper31_external_reionization_import_theorem.md`
- `/opt/cosmology-lab/results/paper31/paper31_io_native_boltzmann_solver_architecture_theorem.md`
- `/opt/cosmology-lab/results/paper31/paper31_lya_forward_pipeline_import_theorem.md`
- `/opt/cosmology-lab/results/paper31/paper31_lya_internal_kernel_class_theorem.md`
- `/opt/cosmology-lab/results/paper31/paper31_reduced_source_state_identifiability_theorem.md`
- `/opt/cosmology-lab/results/paper31/paper31_reduced_to_physical_source_underdetermination_theorem.md`
- `/opt/cosmology-lab/results/paper31/paper31_reionization_clock_transport_theorem.md`
- `/opt/cosmology-lab/results/paper31/paper31_reionization_data_class_theorem.md`
- `/opt/cosmology-lab/results/paper31/paper31_reionization_functional_nogo_theorem.md`
- `/opt/cosmology-lab/results/paper31/paper31_reionization_inheritance_theorem.md`
- `/opt/cosmology-lab/results/paper31/paper31_seam3_full_weyl_closure_theorem.md`
- `/opt/cosmology-lab/results/paper31/paper31_seam3_internal_alpha_phi_theorem.md`
- `/opt/cosmology-lab/results/paper31/paper31_seam3_lensing_inheritance_theorem.md`
- `/opt/cosmology-lab/results/paper31/paper31_stage2_characteristic_field_inheritance_theorem.md`
- `/opt/cosmology-lab/results/paper31/paper31_stage2_dynamic_network_support_theorem.md`
- `/opt/cosmology-lab/results/paper31/paper31_stage2_lossless_characteristic_markov_theorem.md`
- `/opt/cosmology-lab/results/paper31/paper31_stage2_positivity_admissibility_theorem.md`
- `/opt/cosmology-lab/results/paper9_theorem_review/paper9_theorem_review.txt`

## David review flags

- `paper32_p4_collar_cell_identification_theorem.md` stays `NEEDS_REVIEW` because the file is explicitly superseded by a Cosmo-rejected closure and should not be cited as a live theorem surface
- no `CIRCULAR` Paper 32 theorem surfaces were found in this audit round

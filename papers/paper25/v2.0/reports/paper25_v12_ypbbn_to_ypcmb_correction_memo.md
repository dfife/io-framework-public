# Paper 25 v1.2 YPBBN -> YPCMB and Amplitude-Alignment Audit

Status: verified / configuration-audit / wrapper correction / amplitude alignment

## Executive Finding

- Paper 25 v1.2 has two corrections: inherited support rows now use `YPCMB / PRyMresults()[3]`, and the active BBN scorecard is amplitude-aligned to Paper 22 v1.4.
- The aligned amplitudes are `epsilon_w = ln(1+gamma^2) * L1 = 0.012300778733811872` and `epsilon_n = (1.72704/10) * L2 = 0.02384221534546833`.
- Paper 25's distinctive theorems are unchanged: the V-vs-V' class-membership result and Quadratic Thermal Covariance still select the quadratic weak branch.
- A support-script bug was fixed: `paper25_quadratic_weak_paper24_lithium_check_analysis.py` now varies `p24.EPSILON_W_P25`; the stale `p24.WEAK_DELTA_P22` assignment did not affect the current Paper 24 runner. The same wrapper now aligns both `p24.NUCLEAR_DELTA_P22` and `p24.epsilon_n`.

## Paper 25 Headline Scorecard

| quantity | Paper 25 v1.1 published text | Paper 25 v1.2 corrected/aligned |
| --- | ---: | ---: |
| `epsilon_w` | 0.012301 | 0.012300778733811872 |
| `epsilon_n` | inherited rounded branch | 0.02384221534546833 |
| `D/H` | not printed in headline | 2.5099388177672621e-05 |
| `D/H_sigma` | -0.61 | -0.568706 |
| `Y_p` | not printed in headline | 0.24771903130174175 |
| `Y_p_sigma` | +0.68 | +0.679758 |
| `Li7/H` | not printed in headline | 1.7508826463710944e-10 |
| `Li7/H_sigma` | +0.55 | +0.551234 |
| `chi2(D/H + Y_p + Li7)` | 1.13 | 1.089357 |

The corrected three-observable chi2 is not the Paper 22 two-observable `0.802`; Paper 25 includes Li-7, so the aligned Paper25/Paper24 lithium-pipeline score is `1.0893566013769407`.

## Branch Comparisons Under v1.2

| branch | epsilon_w | D/H sigma | Y_p sigma | Li7/H sigma | chi2_3obs |
| --- | ---: | ---: | ---: | ---: | ---: |
| exact-log quadratic, aligned | 0.012300778733812 | -0.568706 | +0.679758 | +0.551234 | 1.089357 |
| rounded/requested quadratic, aligned | 0.012248588238432 | -0.522824 | +0.676865 | +0.548656 | 1.032515 |
| linear `K_gauge * sqrt(L1)`, aligned | 0.025980346217023 | -0.087983 | +1.282189 | +0.583308 | 1.991999 |
| published-like weak `0.0271`, aligned | 0.027100000000000 | -0.052633 | +1.330516 | +0.578095 | 2.107236 |

The old `linear branch chi2 = 2.11` comparison updates to `1.991998955082098` under the corrected/aligned wrapper. The exact-log quadratic branch still beats the linear branch by `0.9026423537051573` in three-observable chi2.

## Corrected Round10-Inherited Support Rows

| row | D/H sigma | Y_p sigma legacy YPBBN | Y_p sigma corrected YPCMB | chi2 legacy | chi2 corrected |
| --- | ---: | ---: | ---: | ---: | ---: |
| `B_only_Kgauge_L1` | -0.552980 | +1.038052 | +0.704536 | 1.383340 | 0.802158 |
| `A_only_Kgauge_sqrtL1` | -0.136108 | +1.669571 | +1.333801 | 2.805993 | 1.797549 |
| `Vprime_branch` | +8.705878 | +12.063267 | +11.693657 | 221.314707 | 212.533915 |
| `K_gauge_linear_branch` | -0.136108 | +1.669571 | +1.333801 | 2.805993 | 1.797549 |

The quadratic support row now agrees with the corrected Paper 22 convention:
- `epsilon_w = 0.012300778733811872`
- `epsilon_n = 0.02384221534546833`
- `D/H_sigma = -0.552980`
- `Y_p_sigma = +0.704536`
- `chi2(D/H + Y_p) = 0.802158`

The V-prime branch remains catastrophically excluded after the correction:
- `Vprime Y_p_sigma = +11.693657`
- `Vprime chi2(D/H + Y_p) = 212.533915`
- `Vprime chi2(D/H + Y_p + Li7) = 401.743338`

## Inherited Appendix Updates

Step 239 should follow Paper 22 v1.4's corrected rerun:
- `Li7/H = 5.363335812718549e-10`
- `Li7/H_sigma = +12.204309`
- uniform-benchmark fractional consistency = `-0.509342%`

Recommendation for Steps 326, 327, and 340: use Paper 25 v1.2's own corrected/aligned rerun for the active scorecard, not the older Paper 24 v2.1-era rounded row. Historical Paper 24 context can remain only if explicitly labeled historical.
- active `D/H_sigma = -0.568706`
- active `Y_p_sigma = +0.679758`
- active `Li7/H_sigma = +0.551234`
- active `chi2_3obs = 1.089357`

## Source Verification

- Affected support scripts contain no direct `PRyMresults()` calls; they inherit the corrected Paper 22 Round10 helper.
- The Paper24 lithium-control script now mutates `p24.EPSILON_W_P25`, the variable actually read by `paper24_final_push_excited_branch_analysis.py`.
- The Paper24 lithium-control script also mutates `p24.epsilon_n`; otherwise the nuclear network suppression and the branch-exponent formula can silently disagree.
- Observational denominators are per IO Framework Observational Conventions v1: https://dfife.github.io/data/observational_conventions_v1.md.

## Docx Edit Locations

The full machine-readable location list is in the JSON. Primary locations for PI/docx review:
- `P21`: Beginning from two premises — (1) the observable universe exists inside a Schwarzschild black hole, and (2) the physics inside the horizon is the same as outside — this paper resolves the V-vs-V’ class-membership prob...
- `P23`: This result corrects Paper 22’s weak amplitude from ε_w = K_gauge × √L_1 to ε_w = K_gauge × L_1. The correction improves the BBN fit: PRyMordial-verified results give D/H = −0.61σ, Y_p = +0.68σ, Li-7/H = +0.55σ, with ...
- `P26`: The Interior Observer (IO) framework models the observable universe as the interior of a Schwarzschild black hole with mass M_U = 4.50 × 10⁵³ kg. Papers 1–24 derived all major cosmological observables from this single...
- `P39`: 5. The quadratic weak branch ε_w = K_gauge × L_1 gives χ² = 1.13 with all three BBN observables within 1σ. PRyMordial-VERIFIED.
- `P52`: V’’ = 2(1+γ²) = 2.1128
- `P104`: The quadratic weak branch ε_w = K_gauge × L_1 = 0.012301 gives χ² = 1.13, improving on the linear branch’s χ² = 2.11.
- `P161`: Exact BBN computation using PRyMordial with the Paper 24 v1.1 lithium pipeline:
- `P162`: The quadratic weak branch achieves all three primordial abundances within 1σ of observation with zero fitted parameters. The combined three-observable χ² drops from 2.11 to 1.13 — a 46% improvement. V’ is excluded at ...
- `P179`: NEW: ε_w = K_gauge × L_1 = 0.012301
- `P181`: Paper 22’s structural results (GMP, channel placement, bridge mechanics, spatial Hodge spectrum) are unchanged. Only the weak amplitude formula and its derivation status are corrected. Papers 23 and 24 are unaffected:...
- `P199`: Step 1: Schwarzschild radius (Paper 1 §2.1). r_s = 2GM_U/c² = 6.685 × 10²⁶ m. The observable universe sits within a factor 1.5 of its own Schwarzschild radius. STATUS: DERIVED (standard GR, exact)
- `P203`: Step 5: Compactness ratio (Paper 1 §2.1). x = r_s/R_U = 1.51899. The Schwarzschild radius exceeds the observable universe radius by a factor of 1.519, placing the observer deep inside the horizon at 65.8% of the Schwa...
- `P215`: Step 15: No-Go for semiclassical QFT (Paper 2 §3). Semiclassical QFT on stationary Schwarzschild CANNOT produce T_IO. Five candidate mechanisms examined and excluded (Bogoliubov coefficient analysis, 36/36 verificatio...
- `P240`: Step 33: Complete BBN scorecard: D/H at −1.2σ, Y_p at +0.6σ — DERIVED (conditional on BDP) [Paper 19: α=3/2 clustering branch gives ω_b = 0.01705; BOSS DR12 χ² = 73.06]
- `P250`: Step 37: V-hierarchy (Papers 9–13). Complete algebraic hierarchy of the generating potential: exp(V) = 1+γ² = 1.0564 (Paper 9), V′′ = 2(1+γ²) = 2.1128 (Paper 10), V′ = 2γ = 0.4750 (Paper 12), V = K_gauge = 0.05487 (Pa...
- `P263`: Step 49: Interior/exterior asymmetry (Paper 14). Observable corrections are interior projection effects arising from Premise 1 (observer inside a Schwarzschild BH). The no-hair theorem (standard GR) blocks exterior ac...
- `P270`: A.1.13 Paper 14 New Results: Kill Shot C (H₀ Composite)
- `P280`: Step 67: Boundary No-Go (Paper 15). Local Schwarzschild horizon scalars are x-independent: they depend only on r_s, not on the ratio r_s/R_U. Therefore local horizon quantities cannot distinguish the observer’s positi...
- `P307`: Step 92: Foundation closure. All three High gaps closed within the reduced Schwarzschild tangential thermal sector. Scope: reduced sector used by Papers 14–17, not full unreduced horizon algebra. STATUS: DERIVED (redu...
- `P311`: Step 95: CMP Modular Realization Theorem (Theorem 18.C). K_CMP = K_geom · I + K̂_g. On physical sector: ⟨K⟩ = K_geom + K_gauge = ln Δ. Additive decomposition from tensor product structure, no BCH correction. Numeric c...
- `P316`: Step 99: BDP Modular Derivation Theorem (Theorem 18.B). f_b = x⁻¹ · V′(α) = 2γ/x = 0.3127. Master identity f_b × F = ⟨K⟩/4 follows downstream. Numeric check: f_b × F − ⟨K⟩/4 = 0 to machine precision. STATUS: DERIVED/T...
- `P338`: Step 115: P(k) crisis diagnosis. Paper 18 P(k) catastrophe (chi-squared = 1056) was misdiagnosed as N_eff-driven. Paper 19 proves the dominant driver is the baryon mapping. STATUS: DERIVED
- `P339`: Step 116: Baryon Scalarization Theorem. Observable-class Jacobian: omega_b(O) = omega_b(alpha=1) x^(1-alpha_O). For P(k) clustering: alpha = 3/2, omega_b = 0.01705. Three bridge theorems, two surgical repairs. BOSS DR...
- `P341`: Step 118: Architectural shift (Paper 18). Project the Hamiltonian constraint, not the fluid. The correct IO approach projects the gravitational constraint equation onto the observer sector, rather than projecting indi...
- `P344`: Step 121: RT upgrade chain (Paper 19 §3). The complete derivation chain for the reduced-scope temperature transfer: Premise 1 (Schwarzschild interior) → isolated-horizon certification → RT/BY boundary framework → Asht...
- `P351`: Step 128: Schur N-slot dissolution and bare background tension. Observer-side curvature projector dissolved by global readout. Curvature rank n=0 confirmed. Bare dissolution branch gives 15.07 Gyr (6.3 sigma too old)....
- `P355`: omega_b,clust = 0.01705 (alpha = 3/2); BOSS DR12 chi-squared = 73.06; sigma_8 = 0.794; S_8 = 0.839
- `P375`: Step 147: Bare expansion diagnostic (Paper 20 §7). Switching from the observer to the bare expansion history shifts D_A by +3.44% but shifts r_s by only −0.04%. The acoustic angular scale is dominated by r_s, not D_A....
- `P380`: Step 152: BBN multi-channel incompatibility (Paper 20 §9). D/H fails at −3.9σ with N_eff = 3.044 (standard model). The D/H tension identifies a required radiation excess ΔN_eff ≈ 0.37. This excess cannot come from any...
- `P381`: Step 153: BBN measurement immunity (Paper 20 §11). Abundance ratios (D/H, Y_p, ⁷Li/H) are dimensionless. Both species share the same astrophysical geometry. Any boundary geometric correction cancels in the ratio. Obse...
- `P393`: Step 165: ΔN_eff target (Paper 20 §14). ΔN_eff ≈ 0.37 required to match D/H observation. Three premises needed (P_fullgrav, P_puncham, P_radmap) not yet in theorem stack. F_abs = 0.36879 derived as the absolute local ...
- `P411`: Step 179: Assembly gap decoupling (Theorem 21.C, Paper 21 §8.1). On the torsion-Λ homogeneous branch, d ln H₀_obs / d ln N_eff = 4.96×10⁻⁵. Achieving H₀_obs = 67.4 would require N_eff ≈ 6708. The assembly gap and D/H ...
- `P414`: Step 182: No dynamic scattering / Γ=1 / ΔN_eff=0 (Theorem 21.Bb). Full 3+1 mode-matching kernel open. STATUS: DERIVED/NO-GO (not yet theorem-grade bundled)
- `P423`: Step 191: BBN scorecard at N_eff = 3.4062 on T_IO branch. D/H = −0.08σ, Y_p = +1.72σ, χ² = 2.97. T_obs insertion gives χ² = 99.02 (class error). STATUS: DERIVED
- `P432`: Step 200: BBN scorecard at N_eff = 3.41279 on T_IO branch (Paper 21 §11). With F_abs route: D/H σ = +0.11 (was −3.916 at baseline), Y_p σ = +1.74, χ²(D/H + Y_p) = 2.97 (was 15.61 at baseline). The F_abs route substant...
- `P437`: Step 205: Uniform rate suppression no-go (21.AG computational). D/H-matching s = 0.892 gives Y_p = +5.73σ. Wrong abundance pattern. STATUS: DERIVED
- `P447`: Step 214: P_resp Three-Channel Architecture (Reconstruction). Non-separable candidate: R_spatial(E,T) = Σ κ_{s,n,J} Π_{0,n,J} ⊗ P_J + Σ κ_{v,n,J} Π_{1,n,J}^coex ⊗ P_J + Σ κ_{t,n,J} Π_{TT,n,J} ⊗ P_J, with hard selectio...
- `P454`: Step 221: Bounded-Ratio No-Go (Theorem 22.11). c_K/c_Γ ~ Ha ~ a⁻¹ ∝ (1+z). At BBN ~ 10⁹, at recombination ~ 1100; both are large-argument. Any untuned bounded saturator stays on plateau at both epochs. Cannot create B...
- `P455`: Step 222: Shutoff Localization Theorem (Theorem 22.12). From Theorems 22.8–22.11: epoch gate cannot live in Z_punc/F_abs/P_J (permanent), spatial projectors alone (stress scalarization), A-B connection monomials (triv...
- `P460`: Step 227: Full-Radiation Scaling Equivalence (Theorem 22.14). If ρ_r → (1+F_abs)ρ_r, then ΔN_eff,eq = [(1+β_rel N_eff,base)/β_rel] × F_abs = 2.746, so N_eff,eff = 5.790. This is NOT equivalent to ΔN_eff = F_abs. Catas...

## Version Note Draft

v1.2 (May 2026): PRyMordial output index correction (YPBBN -> YPCMB), observational denominator alignment to IO Framework Observational Conventions v1, and amplitude alignment to the Paper 22 v1.4 standard (epsilon_w = ln(1+gamma^2) x L_1 = 0.012300778733811872, epsilon_n = (1.72704/10) x L_2 = 0.02384221534546833). Paper 25 v1.1 support rows inherited Paper 22 Round10's YPBBN wrapper convention; the wrapper now reports YPCMB / PRyMresults()[3] and retains YPBBN only as an audit field. Corrected aligned scorecard: D/H = 2.509938817767262e-05 (-0.568706 sigma), Y_p = 0.24771903130174175 (+0.679758 sigma), Li-7/H = 1.7508826463710944e-10 (+0.551234 sigma), chi2(D/H + Y_p + Li-7) = 1.089357. The central theorem of this paper (the Quadratic Thermal Covariance Theorem) structurally proves that the physical weak rate is bilinear in the bridge field (a two-point function, not a one-point amplitude), which is the rate-vs-amplitude distinction underlying the aligned quadratic branch. Observational denominators per IO Framework Observational Conventions v1 (https://dfife.github.io/data/observational_conventions_v1.md). Paper 25's distinctive results (V-vs-V' Class-Membership Theorem, Quadratic Thermal Covariance, WMR closure) are unaffected by this correction.

# Paper 26 C2c Route-Exhaustion Report

Date: 2026-05-16

## Question

Can Paper 26 v2.0 `C2c` be fully closed?

`C2c` is the Hawking-state selection assertion that the one-particle covariance
`G^(1)` entering the scalar bridge correlator is the `S^2` Hawking thermal
covariance at the Schwarzschild Hawking temperature on the coexact carrier
identified by Paper 26 Lemma C2.2.

This report continues the prior C2c closure attempts until no viable
theorem-grade route remains.

## Executive Verdict

No full closure was found.

The obstruction is structural, not numerical:

1. Standard Hawking/QFT-on-curved-spacetime theorems thermalize field modes
   with respect to horizon/Killing time frequency.
2. Paper 26 `C2c` needs an additional identification: the scalar-bridge source
   covariance must be the covariance of a compact `S^2` coexact oscillator with
   one-particle Hamiltonian
   \[
   h_{\rm coex}=\hbar c\sqrt{\Delta^{(1,\rm coex)}_{S^2}} .
   \]
3. No theorem in the current IO stack or in the consulted standard literature
   forces that boundary oscillator Hamiltonian and state selection from P1 + P2
   alone.

The strongest positive result remains:

- fixed-carrier covariance uniqueness is theorem-grade;
- full physical state selection is not.

Once the carrier, dynamics, and Hawking/KMS quasi-free state class are chosen,
CCR/KMS uniqueness gives
\[
G_H^{(1)}|_{\ell=1}
=
\left(e^{4\pi\sqrt2}-1\right)^{-1} I .
\]
But choosing that state/dynamics package is exactly the unresolved step.

## Best Narrowing Found

The later Paper 31 rank-one quotient route is the best repair path for the
amplitude constant:

- replace full `C2c` by the narrower claim `C2q`;
- `C2q`: the physical state on the one-dimensional bridge quotient used by
  the scalar-amplitude slot is the Hawking thermal state of the lowest coexact
  boundary mode.

This closes less than `C2c`. It can protect the `A_s` amplitude slot only if the
manuscript explicitly states that the full coexact-carrier state is not being
claimed.

Even this narrowed route has a visible state-selection condition if read
strictly: the one-dimensional quotient must be identified as an actual Hawking
oscillator mode with Hamiltonian `hbar omega_1`, where
\[
\omega_1=\sqrt2\,c/r_s .
\]
That is not a consequence of generic Hawking thermality alone; it is a
boundary-mode identification.

Recommended label for the narrowed amplitude route:

`DERIVED/CONDITIONAL_VERIFIED` for the rank-one lowest-shell scalar-amplitude
quotient, with the condition explicitly named as the Hawking quotient
state-selection / boundary-mode identification.

Do not label full `C2c` as `DERIVED/THEOREM`.

## Route Tests

### 1. Kay-Wald / Hartle-Hawking-Israel Uniqueness

Status: partial support, not closure.

Kay-Wald proves strong uniqueness and thermal-property results for quasifree
Hadamard states on globally hyperbolic spacetimes with a one-parameter isometry
and a bifurcate Killing horizon. The result is explicitly about stationary
black-hole field algebras and KMS behavior at the Hawking temperature on the
appropriate wedge algebra.

This supports importing a distinguished Hartle-Hawking/KMS state in the
standard stationary Schwarzschild setting.

It does not close Paper 26 `C2c` because:

- Paper 26 uses the closed `K=+1` Oppenheimer-Snyder interior branch, not a
  theorem-grade stationary bifurcate-Killing spacetime for the scalar bridge
  source;
- the theorem is primarily about the full field algebra, not the IO scalar
  bridge quotient;
- it thermalizes in Killing frequency, not automatically in an angular
  `S^2` coexact Hodge oscillator spectrum.

Verdict: route stops at the missing carrier-embedding / generator-identification
theorem.

### 2. Sewell / Bisognano-Wichmann Horizon KMS Route

Status: partial support, not closure.

Sewell's generalized Hawking-Unruh result supports KMS behavior for fields
restricted to horizon-bounded submanifolds under the relevant axioms. This is
strong evidence that regular horizon field states have a thermal/KMS
description.

It still does not close `C2c` because the same missing identification remains:
the IO scalar bridge source must be proved to be the invariant subalgebra or
quotient of that horizon field algebra, with the correct one-particle dynamics.

Verdict: proves a valid thermal restriction principle after the algebra and
dynamics are identified; it does not identify the Paper 26 bridge covariance.

### 3. Gérard / Sanders Stationary KMS Results

Status: partial support, not closure.

Gérard proves existence and Hadamard properties of Hartle-Hawking-Israel states
for stationary black-hole spacetimes in the Kay-Wald setting. Sanders reviews
unique quasifree KMS states for linear scalar fields in stationary spacetimes.

These are useful external endpoints for a stationary equilibrium version of the
argument.

They do not supply:

- the OS-interior-to-stationary-HHI reduction;
- a coexact one-form boundary oscillator theorem;
- equality of the Paper 23 bridge covariance with the HHI two-point function
  restricted to the scalar bridge quotient.

Verdict: no full closure.

### 4. Collapse / Unruh / Fredenhagen-Haag Route

Status: no closure.

Collapse-state Hawking radiation naturally points toward the Unruh state, not
the Hartle-Hawking equilibrium state. It gives outgoing thermal radiation in
the relevant frequency variable, with angular labels entering as scattering
channels and greybody factors.

That is not the Paper 26 object. Paper 26 needs a compact boundary oscillator
occupation
\[
n_\ell=(e^{4\pi\sqrt{\ell(\ell+1)}}-1)^{-1}.
\]
Standard collapse/Hawking derivations do not provide that as a state-selection
theorem for the IO scalar bridge.

Verdict: route gives Hawking flux, not the required angular coexact covariance.

### 5. Euclidean Regularity / No-Conical-Singularity Route

Status: fixes temperature only.

Euclidean Schwarzschild regularity fixes the imaginary-time period and hence
the Hawking temperature. It is an excellent route to `T_H`.

It does not determine which boundary degrees of freedom are physical scalar
bridge source oscillators, nor does it force the source covariance `G^(1)`.

Verdict: temperature closure, not state/covariance closure.

### 6. Tomita-Takesaki / Modular Flow Route

Status: no independent state selection.

Tomita-Takesaki modular theory is state-relative. Given a von Neumann algebra
and a faithful normal state, it produces modular flow. It does not choose the
state.

The current Paper 17 reduced A-vacuum modular package also cannot hide the
`S^2` coexact Hawking carrier: the reduced physical sector has continuous
thermal/dilation spectrum, while the `S^2` coexact generator has pure point
angular Hodge spectrum.

Verdict: modular theory can propagate a chosen state; it cannot choose C2c.

### 7. Passivity / Complete Passivity Route

Status: no closure.

Pusz-Woronowicz passivity can characterize KMS equilibrium states for a fixed
dynamics. This is useful once the physical Hamiltonian is known.

For Paper 26, the missing object is precisely the physical dynamics and state
on the coexact source quotient. Complete passivity would have to be imposed for
that chosen dynamics; it does not derive the dynamics or the quotient
identification.

Verdict: restates the state-selection condition.

### 8. Maximum-Entropy / Gibbs Route

Status: no closure.

Maximizing entropy subject to a fixed energy expectation gives a Gibbs/KMS
state. But the Hamiltonian and constraint are not fixed by this variational
principle. Selecting them for the scalar bridge would be a new state-selection
input.

Verdict: no theorem-grade closure.

### 9. Sorkin-Johnston / Preferred-State Routes

Status: no closure.

Preferred-state proposals can sometimes define candidate states in bounded
regions or special spacetimes. They are not standard unique physical state
selection theorems for the IO OS-interior scalar bridge, and they do not yield
the Paper 26 Hawking coexact occupation law.

Verdict: not a viable closure route.

### 10. Isolated-Horizon / LQG Boundary State Route

Status: no closure.

Isolated-horizon LQG gives powerful structure: punctures, SU(2) Chern-Simons
boundary theory, entropy counting, and local Unruh/Hawking temperature
structures.

It does not supply a theorem that the scalar bridge source is a propagating
`S^2` coexact oscillator with Hamiltonian `c sqrt(Delta_coex)`. The Chern-Simons
boundary theory is topological; local oscillator dynamics require additional
structure.

Verdict: supports horizon microstructure, not C2c state selection.

### 11. Membrane-Paradigm / Edge-Mode Route

Status: no closure.

Membrane and edge-mode approaches can give horizon response functions,
dissipation, and boundary degrees of freedom. The natural dynamics are
response/diffusion or gauge-edge dynamics, not the exact real oscillator
Hamiltonian needed by Paper 26.

Verdict: possible future research direction, not current closure.

### 12. Boundary CFT / Cylinder Quantization Route

Status: no closure.

A 2+1-dimensional conformal boundary field on `R x S^2` would have a compact
mode spectrum and a thermal state. But selecting that CFT and its operator as
the scalar bridge source is new physics unless derived from the IO horizon
algebra.

Also, standard CFT cylinder spectra are determined by conformal weights and
representation data; they do not generically equal `sqrt(l(l+1))`.

Verdict: would be a new boundary theory, not a closure from current inputs.

### 13. Quasinormal-Mode Route

Status: no closure.

Black-hole quasinormal modes have complex frequencies determined by the radial
barrier and boundary conditions. They are not the real compact `S^2` coexact
oscillator frequencies used in Paper 26.

Verdict: wrong spectral object.

### 14. Empirical CMB / Planck Anchor Route

Status: rejected.

Using the observed scalar amplitude `A_s` or CMB anisotropy amplitude to set
the source covariance would be an empirical fit. It could define a calibrated
normalization, but it cannot support a zero-fitted-parameter prediction of
`A_s`.

Using FIRAS to fix the blackbody temperature does not fix scalar bridge
covariance. FIRAS is a photon temperature datum, not a scalar perturbation
source-state theorem.

Verdict: not admissible for closing C2c.

### 15. Later IO Paper 31 Rank-One Quotient Route

Status: best scoped repair, not full C2c closure.

Paper 31 narrows the needed object from the full coexact carrier to a
one-dimensional bridge quotient. That is the strongest valid direction:

- the scalar amplitude sees only `B G^(1) B^\dagger`;
- components in `ker(B)` are invisible;
- the lowest-shell branch can be reduced to one bridge-readable quotient line.

This removes the need to identify the entire coexact carrier state.

However, it still needs the theorem-grade statement that the quotient line is a
physical Hawking oscillator mode with the one-particle energy
`\hbar\sqrt2 c/r_s`. Without that, the argument has simply narrowed C2c to
`C2q`; it has not eliminated state selection.

Verdict:

- acceptable as a scoped repair if labeled
  `DERIVED/CONDITIONAL_VERIFIED` on the rank-one Hawking quotient
  state-selection package;
- not an unconditional proof of full `C2c`.

## Exact Missing Theorem

The theorem needed to close the issue is now precise.

### Horizon Coexact Quotient State-Selection Theorem

Prove all of the following from P1 + P2 + standard external physics:

1. The rank-one scalar bridge quotient is an IO-admissible horizon field mode,
   not merely a quotient of the bridge algebra.
2. Its physical one-particle Hamiltonian is
   \[
   h_1=\hbar c\sqrt{\Delta_{S^2}^{(1,\rm coex)}}|_{\ell=1}
      =\hbar\sqrt2\,c/r_s .
   \]
3. The physical state on that mode is the regular Hawking/KMS equilibrium state
   at
   \[
   \beta_H=4\pi r_s/(\hbar c).
   \]
4. The scalar bridge covariance is the thermal occupation of that mode, with
   the stated canonical coordinate normalization.

If this theorem is proved, the rank-one amplitude route closes. If the theorem
is strengthened to all shells, full `C2c` closes. No current result proves it.

## Forward Arithmetic Check

The existing forward-check script was rerun:

`/opt/cosmology-lab/tmp/io-framework-public/papers/paper26/v2.0/scripts/c2c_analysis/01_c2c_as_forward_check.py`

It reproduces the active body formula:

\[
A_s
=
\frac{25}{9}
\frac{\gamma^2}{1+\gamma^2}
\frac{1}{\sqrt2}
\frac{1}{e^{4\pi\sqrt2}-1}
=
2.0072459972737347\times10^{-9}.
\]

The same output preserves the guard that any appendix formula proportional to
`[2/(exp(4*pi*sqrt(2))-1)]^2` is not the active body formula and is numerically
inconsistent with `2.007e-9`.

## Recommended Paper 26 v2.0 Handling

1. Do not claim full `C2c` closure.
2. Replace the full-carrier claim with a narrower statement if desired:
   `C2q`, the rank-one lowest-shell Hawking quotient state-selection theorem.
3. Label the narrowed `A_s` chain:
   `DERIVED/CONDITIONAL_VERIFIED` on `C1` plus the rank-one Hawking quotient
   state-selection package.
4. State that full coexact-carrier C2c remains open unless the Horizon Coexact
   Quotient State-Selection Theorem is proved.
5. If the manuscript wants a hard theorem, insert only the fixed-carrier/KMS
   uniqueness theorem:
   once the quotient Hamiltonian and Hawking/KMS state class are selected, the
   occupation is unique. Do not let that theorem masquerade as state selection.

## Sources Consulted

- Kay and Wald (1991), "Theorems on the uniqueness and thermal properties of
  stationary, nonsingular, quasifree states on spacetimes with a bifurcate
  Killing horizon", Phys. Rep. 207, doi:10.1016/0370-1573(91)90015-E.
  https://colab.ws/articles/10.1016%2F0370-1573%2891%2990015-e
- Sewell (1982), "Quantum fields on manifolds: PCT and gravitationally induced
  thermal states", Ann. Phys. 141, doi:10.1016/0003-4916(82)90285-8.
  https://www.osti.gov/biblio/6713432
- Gérard (2018/2021), "The Hartle-Hawking-Israel state on stationary black hole
  spacetimes", arXiv:1806.07645.
  https://arxiv.org/abs/1806.07645
- Sanders (2012/2013), "Thermal equilibrium states of a linear scalar quantum
  field in stationary spacetimes", arXiv:1209.6068.
  https://arxiv.org/abs/1209.6068
- Hollands and Wald (2014/2015), "Quantum fields in curved spacetime",
  arXiv:1401.2026.
  https://arxiv.org/abs/1401.2026
- Fewster and Verch (2015), "Algebraic quantum field theory in curved
  spacetimes", arXiv:1504.00586.
  https://arxiv.org/abs/1504.00586
- Local IO reports:
  - `/opt/cosmology-lab/results/paper27/paper27_c2c_hawking_state_selection_memo.md`
  - `/opt/cosmology-lab/results/paper31/paper31_c2cp_rank_one_active_line_source_theorem.md`
  - `/opt/cosmology-lab/results/paper31/paper31_c2q_lowest_shell_hawking_theorem.md`
  - `/opt/cosmology-lab/results/paper33/paper33_ambient_extension_uniqueness_report.md`
  - `/opt/cosmology-lab/results/paper26/paper26_canonical_hawking_chain_audit.md`
  - `/opt/cosmology-lab/results/paper26/paper26_scalar_bridge_normalization_probe.md`

## Final Status

Full C2c: `OPEN/PREMISE_GAP`.

Fixed-carrier KMS covariance uniqueness: `DERIVED/THEOREM`.

Rank-one scalar-amplitude quotient route: viable only as
`DERIVED/CONDITIONAL_VERIFIED` with the Hawking quotient state-selection package
surfaced.

No hidden numerical fitting was found. The remaining problem is a real
state-selection / boundary-mode identification theorem, not arithmetic.

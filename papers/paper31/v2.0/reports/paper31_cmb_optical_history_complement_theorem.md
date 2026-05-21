# Paper 31 CMB Optical-History Complement Theorem

Date: 2026-04-03

## Question

After the failure of:

- typed recombination/opacity routing,
- source-packet dressings,
- the typed-opacity visibility family,
- the minimal metric+visibility family,
- and the naive geometric-drag / acoustic-hierarchy split,

is there a theorem-grade surviving IO deformation of the primary scalar CMB
branch?

More sharply:

can the surviving broad Thomson/diffusion correction be identified with the
intrinsic Rosetta complement factor on the reduced optical-history carrier?

## Executive result

The strongest honest result is:

- `derived / scoped`: the bridge complement cannot act on the primitive local
  Thomson drag/contact leg.
- `conditional / scoped`: if the reduced visibility-plus-hierarchy packet is
  the degree-2 optical-history descendant of the post-bridge observer-side
  photon readout, then the unique minimal intrinsic-complement deformation is
  the common factor
  \[
  c_{\rm vis}=h_{\rm hier}=f_\Gamma^2=e^{-2K_{\rm gauge}},
  \qquad
  d_{\rm drag}=1.
  \]
- `verified`: on the exact curved-kernel control compression this exact point is
  numerically almost indistinguishable from the best one-parameter common
  optical-history branch.
- `verified`: on the native zero-borrow branch the same exact factor makes the
  fit worse. So this is a closure of the **control optical-history branch**,
  not a universal theorem for every candidate CMB branch.

So the best current Paper 31 closure is:

\[
\boxed{
\text{control bulk}
\ +\ 
\text{exact curved Weyl kernel}
\ +\ 
\text{common optical-history complement }f_\Gamma^2
}
\]

with any further hierarchy split left open.

## Inputs

### Internal

1. `derived`: the primitive local Thomson kernel is shared by visibility and
   drag, but the equations do not force `kappa'` and `R` onto the same baryon
   slot.
2. `derived`: the local Thomson contact term is gauge-neutral and does not
   itself carry the surviving reduced gauge factor.
3. `derived / scoped`: reduced visibility/readout lives on the observer-side
   optical scalar-acoustic class.
4. `derived`: `C_l` and analogous power/covariance objects are degree-2
   same-fiber self-intensities, not primitive degree-1 transfer amplitudes.
5. `verified`: the surviving local ODE improvement lies in the broad
   Thomson/diffusion hierarchy, not in `R`, not in local metric forcing, and
   not in a narrow recombination-window operator.

### External

Standard LOS / radiative-transfer theory treats last-scattering attenuation as a
positive collision/readout contraction rather than a frequency-transfer law.
This licenses an optical-history semigroup interpretation on the observer-side
field once Premise 2 is accepted.

## 1. What the complement can and cannot act on

### `derived / scoped`

The primitive drag/contact leg is not the place for the intrinsic complement.

Reason:

1. the local Thomson kernel `kappa' = a n_e sigma_T` is a primitive local
   contact operator;
2. the local Thomson operator is gauge-neutral on the current stack;
3. the bridge complement survives only on a distinct post-bridge readout stage,
   not as a second projector on the same primitive source carrier.

So any Rosetta complement factor applied directly to the primitive drag/contact
kernel is an inadmissible typing move.

This is exactly why the naive geometric-drag theorem point died numerically.

## 2. Minimal optical-history semigroup

Let `X_opt` be the reduced observer-side optical-history field feeding the
primary scalar source packet. If the physical readout stage is a positive
contraction semigroup
\[
R_{\rm opt}(s)=e^{-sL_{\rm opt}},
\]
and if on the reduced central optical line
\[
L_{\rm opt}=K_{\rm gauge} I,
\]
then the field-level attenuation is
\[
X_{\rm opt}^{\rm obs}=e^{-K_{\rm gauge}}X_{\rm opt}^{\rm prim}
=f_\Gamma X_{\rm opt}^{\rm prim},
\qquad
f_\Gamma=\frac{1}{1+\gamma^2}.
\]

This is the standard collision/readout analogue of the old intrinsic-screening
route.

## 3. Why the surviving common factor is `f_Gamma^2`

### `conditional / scoped`

Assume:

1. the reduced visibility-plus-hierarchy packet is a descendant of the same
   post-bridge optical-history field `X_opt`;
2. reduction to that packet preserves observable type on the Paper 16 / 21
   descent logic;
3. the relevant primary `TT/TE/EE` object is still in the degree-2
   same-fiber self-intensity class rather than in a primitive degree-1 angular
   estimator class.

Then the complement acts on the packet with the degree-2 factor
\[
f_\Gamma^2=e^{-2K_{\rm gauge}},
\]
not with the one-leg factor `f_Gamma`.

Reason:

- the post-bridge field carries one factor `f_Gamma`,
- the observed primary power/covariance is degree-2 same-fiber intensity,
- therefore the minimal common optical-history descendant carries `f_Gamma^2`.

This is the exact analogue of the already-established `a_lm` versus `C_l`
degree split.

## 4. The theorem candidate in CLASS variables

On the exact curved-kernel control compression, define

\[
c_{\rm vis}=f_\Gamma^2,\qquad
d_{\rm drag}=1,\qquad
h_{\rm hier}=f_\Gamma^2.
\]

This is the minimal common optical-history complement point:

- visibility/history leg gets the common degree-2 complement factor,
- hierarchy damping leg gets the same common optical-history factor,
- primitive drag/contact remains local.

## 5. Numerical verification

Reproducible scans:

- [paper31_cmb_optical_history_complement_theorem.py](/opt/cosmology-lab/results/paper31/paper31_cmb_optical_history_complement_theorem.py)
- [paper31_cmb_optical_history_complement_theorem_report.txt](/opt/cosmology-lab/results/paper31/paper31_cmb_optical_history_complement_theorem_report.txt)
- [paper31_cmb_optical_history_branch_check.py](/opt/cosmology-lab/results/paper31/paper31_cmb_optical_history_branch_check.py)
- [paper31_cmb_optical_history_branch_check_report.txt](/opt/cosmology-lab/results/paper31/paper31_cmb_optical_history_branch_check_report.txt)

### Control compression

`verified`:

- baseline:
  \[
  \chi^2=2834.716042
  \]
- exact theorem candidate:
  \[
  (c,d,h)=(f_\Gamma^2,1,f_\Gamma^2)
  \Rightarrow
  \chi^2=2239.727302
  \]
- best one-parameter common optical-history family:
  \[
  c=h=a_{\rm best}=0.891216797,\qquad \chi^2=2238.840992
  \]

So the exact theorem candidate is only
\[
\Delta\chi^2 = 0.886309
\]
above the best one-parameter branch, with parameter shift
\[
|a_{\rm best}-f_\Gamma^2|=0.004845236.
\]

This is the strongest clean surviving numerical theorem foothold in the scalar
primary CMB chain.

Further checks:

- hierarchy-only `f_Gamma^2` helps:
  \[
  \chi^2=2585.708638
  \]
- visibility-only `f_Gamma^2` is catastrophic:
  \[
  \chi^2=3982.683495
  \]

So the complement does **not** live on visibility alone. It survives only as a
common optical-history packet.

### Native zero-borrow branch

`verified`:

- native baseline:
  \[
  \chi^2=3850.237903
  \]
- exact common `f_\Gamma^2` point:
  \[
  \chi^2=4341.056588
  \]

So the theorem candidate sharply **rejects** the native zero-borrow compression.

## 6. Exploratory deeper split

`verified`:
the structured point
\[
(c,d,h)=(f_\Gamma^2,1,f_\Gamma^3)
\]
lands very near the best unconstrained two-parameter optical-history family on
the control branch:

\[
\chi^2=2003.531409
\]
versus the unrestricted `d=1` optimum
\[
c_{\rm best}=0.903010211,\qquad
h_{\rm best}=0.852376311,\qquad
\chi^2=2000.522289.
\]

But:

- `not derived`: there is no theorem yet identifying the extra hierarchy factor
  `f_\Gamma^3`.
- `verified`: the same point still worsens the native branch.

So this is a live structured clue, not closure.

## 7. Final claim boundary

- `derived / scoped`: primitive drag/contact is not the carrier of the
  intrinsic complement.
- `conditional / scoped`: if the reduced visibility-plus-hierarchy packet is
  the degree-2 optical-history descendant of the post-bridge photon readout,
  then the unique minimal complement law is the common factor
  \[
  f_\Gamma^2=e^{-2K_{\rm gauge}}.
  \]
- `verified`: that exact point closes the one-parameter control optical-history
  branch to numerical near-equivalence.
- `verified`: it simultaneously rejects the native zero-borrow compression.
- `not derived`: the residual deeper hierarchy split beyond the common
  `f_\Gamma^2` law.

So the Paper 31 frontier is now:

1. **closed**: minimal control-branch optical-history complement law,
2. **open**: deeper hierarchy-only structure beyond that law,
3. **open**: theorem-grade identification of the true full CMB bulk branch
   beyond the control compression.

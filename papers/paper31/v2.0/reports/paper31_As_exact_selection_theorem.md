# Paper 31: Exact `A_s` Selection Theorem

Date: 2026-04-03

## Question

Can Paper 31 now close the exact scalar-amplitude selection problem between the
two carried candidates

\[
A_s = 2.0072459972737347\times 10^{-9}
\quad\text{and}\quad
A_s = 2.1141000090331526\times 10^{-9} \, ?
\]

The active lab context is:

- `\tau = K_{\rm gauge}/2` is already theorem-grade on the reduced source side,
- the Weyl-response bridge is closed at observable-class level,
- the old Paper 27 authority block selecting the higher amplitude against a
  GR-Planck target has been removed,
- the remaining obstacle was whether the framework still needs an
  IO-aware full Planck extraction with low-`\ell` EE in order to decide the
  exact `A_s`.

## Executive result

The strongest honest answer is:

- `derived / scoped`: **yes** for the native source-side scalar amplitude.
- `not derived`: **no** for a universal observationally extracted
  `(A_s,\tau_{\rm reio})` pair from scalar CMB alone.

So the exact selection problem splits cleanly:

\[
\boxed{
A_s^{\rm native}
=
2.0072459972737347\times10^{-9}
}
\]

within the active linear scalar-source sector,

while

\[
\boxed{
A_s^{\rm Planck\text{-}extracted}
}
\]

is not a theorem-grade framework constant because it is entangled with an
inherited late-visibility history and a survey/likelihood model.

Therefore the Paper 27 upward correction to

\[
2.1141000090331526\times10^{-9}
}
\]

is no longer the active exact selection. It remains only a conditional,
GR-Planck-calibrated observational package.

## 1. Native source-side amplitude is already closed

Paper 31 already closed the exact active scalar-source chain:

1. **Rank-one active-line source theorem**

   The physical state on the one-dimensional bridge quotient is uniquely the
   Hawking `\beta_H`-KMS state, giving the quotient coefficient

   \[
   g_q
   =
   \frac{\gamma^2}{1+\gamma^2}
   \frac{1}{\sqrt2}
   \frac{1}{e^{4\pi\sqrt2}-1}.
   \]

   Authority:
   [paper31_c2cp_rank_one_active_line_source_theorem.md](/opt/cosmology-lab/results/paper31/paper31_c2cp_rank_one_active_line_source_theorem.md)

2. **Shell-window factorization theorem**

   The scalar source covariance factorizes as

   \[
   P_{\rm src}(N)=g_q\,W_N,
   \]

   with canonical pivot normalization fixing

   \[
   A_s = \frac{25}{9} g_q.
   \]

   Authority:
   [paper31_shell_window_factorization_theorem.md](/opt/cosmology-lab/results/paper31/paper31_shell_window_factorization_theorem.md)

3. **Exact relative window choice**

   The exact relative shell window on the physical plus branch is

   \[
   W_N = \left(\frac{N}{N_p}\right)^{-K_{\rm gauge}/x}.
   \]

   Authority:
   [paper31_relative_window_choice_theorem.md](/opt/cosmology-lab/results/paper31/paper31_relative_window_choice_theorem.md)

4. **Active scalar full-window closure**

   Combining the previous steps closes the active linear scalar-source sector:

   \[
   A_s^{\rm native}
   =
   \frac{25}{9}
   \frac{\gamma^2}{1+\gamma^2}
   \frac{1}{\sqrt2}
   \frac{1}{e^{4\pi\sqrt2}-1}
   =
   2.0072459972737347\times 10^{-9}.
   \]

   Authority:
   [paper31_active_scalar_full_window_closure_theorem.md](/opt/cosmology-lab/results/paper31/paper31_active_scalar_full_window_closure_theorem.md)

So the native scalar amplitude is already theorem-grade in the scoped active
linear scalar-source stack.

## 2. `\tau = K_{\rm gauge}/2` is a different object and already survives

Paper 31 also sharpened the `\tau` side:

\[
\tau_{\rm cov,IO}=K_{\rm gauge}/2=0.02743640887145733
\]

survives as the unique theorem-grade reduced source-covariance constant.

Authority:

- [paper31_c1b_c3_formal_audit.md](/opt/cosmology-lab/results/paper31/paper31_c1b_c3_formal_audit.md)
- [paper31_native_three_sector_tau_theorem.md](/opt/cosmology-lab/results/paper31/paper31_native_three_sector_tau_theorem.md)

At the native source values,

\[
A_{\rm eff}=A_s e^{-2\tau}
=
1.9000701645543414\times10^{-9},
\]

which matches the carried Planck TT ridge at the sub-percent level.

This is supportive but not load-bearing for the theorem; the source-side
`A_s` is already closed independently.

## 3. Why the higher `A_s = 2.114...` no longer competes as the exact selection

The higher candidate entered as a Paper 27 correction selected against a
GR-Planck observational target.

Paper 31 subsequently proved:

1. the Weyl-response bridge suppresses the lensing response seen by a GR Planck
   pipeline,
2. the GR-based Planck extraction therefore biases inferred `A_s` and `\tau`
   downward/upward relative to an IO-aware extraction directionally,
3. the shared native `(A_s,\tau_{\rm reio})` target is mis-typed because
   `A_s` is native source-side while `\tau_{\rm reio}` is an inherited late
   astrophysical visibility moment.

Authorities:

- [paper31_seam3_full_weyl_closure_theorem.md](/opt/cosmology-lab/results/paper31/paper31_seam3_full_weyl_closure_theorem.md)
- [paper31_c1b_c3_formal_audit.md](/opt/cosmology-lab/results/paper31/paper31_c1b_c3_formal_audit.md)
- [paper31_native_As_tau_pair_decomposition_theorem.md](/opt/cosmology-lab/results/paper31/paper31_native_As_tau_pair_decomposition_theorem.md)

Therefore:

- `2.114...` is no longer the active exact selection of a framework constant,
- it is only a conditional observational package associated with a particular
  Planck-calibrated route.

## 4. Low-`\ell` EE does not reopen native `A_s`

The remaining low-`\ell` EE frontier is real, but it does not reopen the native
source-side amplitude theorem.

Paper 31 already proved:

- low-`\ell` EE and high-`\ell` attenuation are two different functionals of the
  same late visibility history,
- one scalar optical-depth number cannot in general close both sectors,
- `x_e(z)` is inherited late-time astrophysics, not a core scalar constant.

Authorities:

- [paper31_late_visibility_identification_theorem.md](/opt/cosmology-lab/results/paper31/paper31_late_visibility_identification_theorem.md)
- [paper31_visibility_moment_separation_theorem.md](/opt/cosmology-lab/results/paper31/paper31_visibility_moment_separation_theorem.md)
- [paper31_reionization_inheritance_theorem.md](/opt/cosmology-lab/results/paper31/paper31_reionization_inheritance_theorem.md)

The low-`\ell` EE check at the derived source-side point is actually favorable:

- floor `\tau = 0.0021`: `-2logpost = 359.268824`
- derived `\tau_{\rm cov,IO}`: `-2logpost = 354.274453`
- improvement: `\Delta(-2\log\mathcal L) = -4.994371`

Authority:
[paper31_lowE_tau_cov_point_report.txt](/opt/cosmology-lab/results/paper31/paper31_lowE_tau_cov_point_report.txt)

So low-`\ell` EE does not rescue `2.114...` as an exact source-side amplitude.
It only reinforces that the observational pair is not the right framework
object.

## 5. Theorem statement

### Exact `A_s` selection theorem

Status: `derived / scoped`

Premises:

1. the standing lab premises,
2. the rank-one active-line source theorem,
3. the shell-window factorization theorem,
4. the exact relative-window theorem,
5. the active scalar full-window closure theorem,
6. the Paper 31 pair-decomposition theorem separating native source amplitude
   from inherited late visibility history.

Statement:

Within the active linear scalar-source sector of the current IO stack, the exact
native scalar amplitude is

\[
\boxed{
A_s^{\rm native}
=
2.0072459972737347\times 10^{-9}.
}
\]

The competing value

\[
2.1141000090331526\times 10^{-9}
\]

is not the active exact selection of a framework constant. It is only a
conditional observational package associated with a Planck-calibrated route.

## 6. Boundary

What this does close:

- `derived / scoped`: the native exact `A_s` selection problem
- `derived / scoped`: the active exact source-side pair
  \[
  (A_s,\tau_{\rm cov,IO})
  =
  (2.0072459972737347\times10^{-9},\,K_{\rm gauge}/2)
  \]

What this does not close:

- the full observationally extracted Planck replacement pair
  `(A_s,\tau_{\rm reio})`
- the late reionization history `x_e(z)`
- any claim that `\tau_{\rm cov,IO}` is identical to astrophysical
  `\tau_{\rm reio}`

So the exact selection is closed **for the native source amplitude**, but not
for the observationally compressed late-visibility pair.

## Final verdict

- `derived / scoped`: `A_s^{\rm native} = 2.0072459972737347e-9`
- `derived / scoped`: `\tau_{\rm cov,IO} = K_{\rm gauge}/2`
- `conditional`: `A_s = 2.1141000090331526e-9` is demoted to an observational,
  Planck-calibrated package, not the active exact framework amplitude
- `open`: IO-aware full Planck extraction with imported reionization remains an
  observational inference problem, not the determinant of the native exact
  amplitude

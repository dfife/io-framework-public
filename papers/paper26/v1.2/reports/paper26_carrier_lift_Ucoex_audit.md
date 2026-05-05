# Paper 26 Carrier Lift `U_coex` Audit

Date: 2026-03-28

## Question

Compute the explicit lowest-shell carrier lift

\[
U_{\mathrm{coex}}:\Omega^1_{\mathrm{coex}}(S^2,\ell=1)
\longrightarrow
h_{br}\subset \Omega^1_{\mathrm{coex}}(S^3,n=1),
\]

and determine its exact `L^2` normalization.

## Short answer

`derived`: the reduced vector/Maurer-Cartan lift exists canonically on the lowest shells.

`derived`: the raw lift is **not** an isometry. It is an `SU(2)`-equivariant isomorphism up to a fixed scale.

`derived`: after unitary normalization, the lift is an isometry and introduces **no** distinguished dimensionless suppression factor near `1/225`.

So the pure carrier-lift geometry does **not** close the Hawking normalization gap.

## 1. Canonical reduced `S^2` carrier

For `u \in \mathbb R^3 \cong \operatorname{Im}(\mathbb H)`, define the canonical lowest-shell coexact `S^2` form

\[
\omega_u := *_2 d(u\cdot n),
\]

where `n : S^2 \to \mathbb R^3` is the unit normal / embedding coordinate.

This gives an `SO(3)`-equivariant identification

\[
\Xi_{S^2}:\mathbb R^3 \xrightarrow{\sim} \Omega^1_{\mathrm{coex}}(S^2,\ell=1).
\]

For a sphere of any radius `r_s`,

\[
\|\omega_u\|^2_{L^2(S^2_{r_s})}
=
\frac{8\pi}{3}|u|^2.
\]

Important point:

- `derived`: because `p=1` in `d=2`, the `L^2` norm of `1`-forms is conformally invariant under constant rescaling of the round metric.
- Therefore the `\ell=1` `S^2` coexact norm does **not** pick up an extra explicit `r_s` factor.

## 2. Canonical reduced `S^3` carrier

Paper 22 gives the lowest coexact shell on `S^3_a` as the left-invariant `1`-form sector.

With the physical orthonormal left-invariant coframe `(e^1,e^2,e^3)`,

\[
\Xi_{S^3}(u) := u_i e^i
\in
\Omega^1_{\mathrm{coex}}(S^3_a,n=1).
\]

Its `L^2` norm is

\[
\|\Xi_{S^3}(u)\|^2_{L^2(S^3_a)}
=
\operatorname{vol}(S^3_a)\,|u|^2
=
2\pi^2 a^3 |u|^2.
\]

So the raw Maurer-Cartan lift is

\[
\iota_{MC} := \Xi_{S^3}\circ \Xi_{S^2}^{-1},
\]

and its norm ratio is

\[
C_{MC}
=
\frac{\|\iota_{MC}(\omega)\|^2_{L^2(S^3_a)}}
     {\|\omega\|^2_{L^2(S^2_{r_s})}}
=
\frac{2\pi^2 a^3}{8\pi/3}
=
\frac{3\pi}{4}a^3.
\]

Using the active IO values

\[
r_s = 6.6835442422068\times 10^{26}\,\mathrm m,
\qquad
x = 1.519,
\qquad
a = r_s/x = 4.3999632930920346\times 10^{26}\,\mathrm m,
\]

this gives

\[
C_{MC}
=
2.0070504823573246\times 10^{80}.
\]

So:

- `derived`: the raw Maurer-Cartan lift is **not** an isometry.
- `derived`: it carries a fixed geometric scale.

## 3. Unitary carrier lift

If one wants an honest one-particle Hilbert-space lift, the canonically normalized unitary version is

\[
U_{\mathrm{coex}}
=
\sqrt{\frac{1}{C_{MC}}}\;\iota_{MC}
=
\sqrt{\frac{4}{3\pi a^3}}\;\iota_{MC}.
\]

Numerically,

\[
\sqrt{\frac{4}{3\pi a^3}}
=
7.058637058566201\times 10^{-41}.
\]

Then

\[
\|U_{\mathrm{coex}}\omega\|_{L^2(S^3_a)}
=
\|\omega\|_{L^2(S^2_{r_s})}.
\]

So the physically meaningful Hilbert-space lift is an isometry after this fixed normalization.

## 4. Raw Hopf pullback factor

For comparison, the ordinary Riemannian Hopf submersion

\[
\pi:S^3_a \to S^2_{a/2}
\]

has fiber length

\[
L_{\mathrm{fiber}} = 2\pi a.
\]

Hence for an ordinary horizontal `1`-form `\omega` on the base,

\[
\|\pi^*\omega\|^2_{L^2(S^3_a)}
=
(2\pi a)\,\|\omega\|^2_{L^2(S^2_{a/2})}.
\]

Numerically,

\[
2\pi a = 2.764578471528538\times 10^{27}\,\mathrm m.
\]

So:

- `derived`: the raw Hopf pullback picks up exactly the fiber-length factor.
- `derived boundary`: this is **not** the same as the reduced Maurer-Cartan `n=1` carrier lift, which is a representation-theoretic spin-1 intertwiner rather than ordinary horizontal pullback.

## 5. Eigenvalue comparison

The lowest-shell eigenvalues are

\[
\lambda_{S^2,\ell=1}^{(1,\mathrm{coex})} = \frac{2}{r_s^2},
\qquad
\lambda_{S^3,n=1}^{(1,\mathrm{coex})} = \frac{4}{a^2}.
\]

Their ratio on the active IO branch is

\[
\frac{\lambda_{S^3}}{\lambda_{S^2}}
=
\frac{4/a^2}{2/r_s^2}
=
2\left(\frac{r_s}{a}\right)^2
=
2x^2
=
4.614721999999998.
\]

So:

- `derived`: the lift does **not** preserve the eigenvalue.
- `derived`: the eigenvalue mismatch contributes only an `O(1)` geometric factor, not a hidden `10^{-2}` or `10^{-3}` suppression.

## 6. Does this close the factor of 225?

No.

The pure coexact carrier-lift geometry gives:

- either a raw dimensional scale (`C_{MC}` or `2\pi a`) that must be removed to define a unitary one-particle map,
- or, after unitary normalization, no distinguished extra dimensionless suppression at all.

So the honest conclusion is:

- `derived`: the reduced lowest-shell lift exists and can be normalized exactly.
- `derived`: the normalized lift is an isometry.
- `derived`: no natural dimensionless factor near `1/225` emerges from the pure `S^2 \to S^3` coexact lift geometry alone.

## 7. Best exact formula

The cleanest theorem-grade carrier lift from the current geometry is

\[
U_{\mathrm{coex}}
=
\sqrt{\frac{4}{3\pi a^3}}\;
\Xi_{S^3}\circ \Xi_{S^2}^{-1},
\]

with

\[
\Xi_{S^2}(u)=*_2 d(u\cdot n),
\qquad
\Xi_{S^3}(u)=u_i e^i.
\]

This is the reduced vector / adjoint / lowest-shell lift.

## Reproducibility

- [paper26_carrier_lift_Ucoex_audit.py](./paper26_carrier_lift_Ucoex_audit.py)
- [paper26_carrier_lift_Ucoex_audit_results.json](./paper26_carrier_lift_Ucoex_audit_results.json)

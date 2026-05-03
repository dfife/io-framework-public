# Paper 32: Bridge Selection and Typed GMP Theorems

## Discipline label

- label state: `CLEAN`
- registry check: Vectors 1-5 reviewed. No unresolved load-bearing circularity-vector hit remains on this surface after the present audit.
- chain verification: verified through the cited Paper 32 chain to assumed-good Papers 1-31 nodes; no surfaced admission or unresolved local premise step remains load-bearing on this surface.
- admitted inputs surfaced here: none.
- usage rule: this theorem may be cited as a premise because it is `CLEAN`.


Date: 2026-04-05

## Question

Can the Paper 32 transfer package promote the three surviving semiclassical
principles:

1. `SP-2 / H1`: bridge state selection,
2. `SP-3 / C2q`: Hawking state selection on the bridge-readable quotient,
3. `SP-4 / GMP`: geometric mode placement,

or do some of them remain irreducible on the current stack?

## Executive result

The strongest honest answer is:

- `derived / scoped theorem`:
  on the active one-slot bridge-readable quotient, the unique Paper 32 transfer
  map fixes the input quasi-free state uniquely once the bridge-readable output
  state is fixed.
- `derived / scoped no-go`:
  this does **not** imply uniqueness of the full ambient Paper 22 spatial KMS
  extension on the whole bridge CCR carrier.
- `derived / scoped theorem`:
  `C2q` closes cleanly on the lowest-shell bridge-readable quotient. The only
  state compatible with the derived bridge quotient, the derived transfer map,
  and the Hawking/KMS output law is the Hawking state.
- `derived / scoped theorem`:
  GMP is forced inside the realized typed bridge architecture: once block type,
  channel floor, background placement, and bridge grammar are enforced, the
  puncture-load-to-channel assignment is determined.
- `derived / no-go`:
  the old fully universal GMP statement still does not follow as a theorem
  about every abstract operator on the larger local algebra.

So the final grading is:

\[
\boxed{
\text{SP-2 closes only on the bridge-readable quotient, not on the full ambient
bridge extension.}
}
\]
\[
\boxed{
\text{SP-3 closes on the lowest-shell quotient.}
}
\]
\[
\boxed{
\text{SP-4 closes on the realized typed bridge class, not as a universal theorem
about all abstract operator classes.}
}
\]

## Claim discipline

- `derived`: forward consequence of stated premises and already-derived stack
- `verified`: computationally checked from explicit formulas
- `conditional`: depends on an extra class-membership claim not yet derived
- `reconstruction`: coherent organizing model, not yet derived
- `speculative`: idea worth exploring, not yet established

## 1. Shared setup

Carry forward the Paper 32 source/readout map
\[
\mathcal P_{\rm src}
=
B_+ \circ U_{\rm coex} \circ T_{\rm field},
\]
with
\[
T_{\rm field}
=
\exp\!\left[
 -\frac{1}{2x}
 \bigl(\hat K_g \otimes \log(r_s\Lambda_{\rm DtN}^{\rm coex})\bigr)
\right].
\]

On the physical reduced sector,
\[
\hat K_g = K_{\rm gauge} I,
\qquad
r_s \sigma_\ell = \ell + 1 = N,
\]
so on shell `N`
\[
T_{\rm field}|_N = N^{-K_{\rm gauge}/(2x)} I.
\]

Because `N >= 1` on the active shells and `K_{\rm gauge}, x > 0`, every active
shell factor is strictly positive:
\[
N^{-K_{\rm gauge}/(2x)} > 0.
\]

Hence `T_field` has no kernel on the active one-slot sector.

Define the bridge-readable quotient
\[
Q_{\rm br}
:=
h_{\rm src}^{\rm br}/\ker(\mathcal P_{\rm src}).
\]

Since `T_field` is injective on the active sector,
\[
\ker(\mathcal P_{\rm src})
=
\ker(B_+ \circ U_{\rm coex}),
\]
and `\mathcal P_{\rm src}` descends to an injective map
\[
\bar{\mathcal P}_{\rm src}: Q_{\rm br} \to {\rm im}(\mathcal P_{\rm src}).
\]

This is the exact mathematical point that was missing before Paper 32:
the transfer leg is now fixed and injective on the bridge-readable active class.

## Theorem 32.C - Bridge-Readable Pullback Uniqueness Theorem

Status: `derived / scoped`

Work on the active one-slot bridge-readable quotient `Q_br` in the scope of
Theorem 32.A.

Let `omega_1` and `omega_2` be centered quasi-free states on `CCR(Q_br)` with
covariances `G_1` and `G_2`. Let their bridge-readable output covariances be
\[
C_i = \bar{\mathcal P}_{\rm src}\, G_i\, \bar{\mathcal P}_{\rm src}^{\!*},
\qquad i=1,2.
\]

If
\[
C_1 = C_2,
\]
then
\[
G_1 = G_2.
\]

Equivalently: on the active one-slot quotient, the input quasi-free state is
uniquely determined by the bridge-readable output state.

### Proof

Because `\bar{\mathcal P}_{\rm src}` is injective on `Q_br`, it has an inverse
on its image. Therefore
\[
G_i
=
\bar{\mathcal P}_{\rm src}^{-1}\,
C_i\,
(\bar{\mathcal P}_{\rm src}^{-1})^{\!*}.
\]
So `C_1 = C_2` implies `G_1 = G_2`.

No deeper operator-algebra input is needed here: this is the linear-algebra
consequence of the now-derived injective one-slot transfer map.

## Corollary 32.C.1 - Exact H1 Boundary

Status: `derived / scoped boundary`

If `SP-2 / H1` is interpreted as:

> the physical bridge state on the active one-slot bridge-readable quotient is
> uniquely fixed,

then `H1` closes on that quotient.

If `SP-2 / H1` is interpreted as:

> the full ambient Paper 22 spatial KMS extension on
> `L^2(R,dnu) \otimes H_g \otimes \Omega^1_{\rm coex}(S^3)` is uniquely
> selected,

then `H1` does **not** follow.

### Reason

The quotient theorem fixes only the bridge-readable class. It does not fix:

- covariance support on invisible directions,
- the full spatial generator on the ambient bridge CCR carrier,
- or the unique choice of Paper 22 Construction 1 among all `O(4)`-equivariant
  positive functions of the spatial Laplacians.

So Paper 32 kills quotient degeneracy, but it does not kill full ambient
extension degeneracy.

This is the honest answer to the user's state-selection question:

\[
\boxed{
\text{unique transfer operator + fixed output} \Rightarrow
\text{unique quotient state,}
}
\]
\[
\boxed{
\text{but not unique ambient extension on the full bridge carrier.}
}
\]

## 2. Hawking restriction on the lowest-shell quotient

Paper 31 already proved the lowest-shell bridge-quotient reduction:

- the scalar-amplitude chain depends only on the one-dimensional bridge
  quotient,
- that quotient has canonical boundary representative in
  `\Omega^1_{\rm coex}(S^2,\ell=1)`,
- the lowest-shell frequency is
  \[
  \omega_1 = \frac{\sqrt2\,c}{r_s},
  \qquad
  \beta_H \hbar \omega_1 = 4\pi\sqrt2.
  \]

External black-hole QFT within the two standing lab premises supplies the
Hawking/Hartle-Hawking-Israel state on the black-hole field algebra, and the
standard stationary-mode restriction gives a `beta_H`-KMS state on the
invariant `\ell=1` mode algebra. On a one-mode bosonic CCR algebra, the
`beta_H`-KMS state is unique.

So the only remaining question after Paper 31 was:

> could a different bridge-readable input state survive once the Paper 32
> transfer/readout map is imposed?

The answer is now no.

## Theorem 32.D - Hawking Quotient Transfer-Lock Theorem

Status: `derived / scoped`

On the canonical lowest-shell bridge-readable quotient `Q_1`:

1. Paper 23 no-doubling reduces the scalar-amplitude problem to that quotient.
2. Paper 31 fixes the canonical Hawking-active boundary representative in the
   coexact `\ell=1` shell.
3. Standard Hawking/HHI theory on stationary bifurcate Killing horizons gives
   the Hawking `beta_H`-KMS state on that invariant mode algebra.
4. The one-mode `beta_H`-KMS state is unique.
5. By Theorem 32.C, the Paper 32 bridge/readout map admits no second input
   state with the same bridge-readable output on that quotient.

Therefore the physical state on `Q_1` is uniquely the Hawking thermal state.

In particular,
\[
g_H = \frac{1}{e^{4\pi\sqrt2}-1}
\]
is uniquely selected on the lowest-shell quotient.

Since
\[
T_{\rm field}|_{Q_1}
=
2^{-K_{\rm gauge}/(2x)} I,
\]
the transfer leg contributes only the already-derived deterministic positive
quotient factor. It does not open a second state-selection freedom.

### Consequence for `A_s`

The Paper 31 amplitude law is therefore transfer-locked:
\[
A_s
=
\frac{25}{9}\,
\frac{\gamma^2}{1+\gamma^2}\,
\frac{1}{\sqrt2}\,
\frac{1}{e^{4\pi\sqrt2}-1}
=
2.0072459972737347\times 10^{-9}.
\]

So `SP-3 / C2q` is now best graded as:

\[
\boxed{
\text{derived / scoped theorem on the lowest-shell bridge-readable quotient.}
}
\]

## 3. Typed geometric mode placement

The old universal GMP target asked for more than the current stack could bear:
it asked that every physically admissible puncture-to-matter map be geometric.

Paper 27 already killed that strongest wording on the larger local algebra.

What Paper 32 adds is a much sharper typed architecture:

- source/readout is a typed block,
- thermodynamic history is a different typed block,
- perturbations live on a closed-`S^3` typed block,
- and the actual bridge/readout maps are one-slot typed intertwiners rather
  than arbitrary operators with no spatial leg.

Inside that typed class, the geometric placement question changes from

> "could there exist some abstract non-geometric operator somewhere in the larger
> algebra?"

to

> "once tensor type and bridge grammar are fixed, is there any residual freedom
> in where the puncture load lands?"

The answer to the second question is now no.

## Theorem 32.E - Typed Geometric Mode Placement Theorem

Status: `derived / scoped`

Assume the physical source/readout map belongs to the realized typed bridge
class determined by:

1. Theorem 32.B typed block architecture.
2. Paper 22 spatial Hodge carriers on `S^3`.
3. Paper 22 channel-floor law
   \[
   J_{\min} = s
   \]
   for local bundle spin `s = 0,1,2`.
4. Paper 22 background placement:
   the homogeneous Ashtekar-Barbero field lies in the lowest coexact `1`-form
   channel.
5. Paper 23 bridge uniqueness and multiplicity-one branch rules.
6. Paper 23 shell-selection rule
   \[
   N = n-1 \quad \text{or} \quad N = n+1
   \]
   on the background-contraction bridge.

Then the puncture-load-to-channel assignment is fixed by tensor type:

### Scalar slot

Scalar output belongs to the scalar branch `s = 0`, so
\[
J_{\min} = 0.
\]
The scalar bridge is the unique zero-order `SU(2)`-equivariant scalarization of
the active slot after background identification, unique up to normalization.

### Vector / connection slot

Connection-type output belongs to the coexact `1`-form branch `s = 1`, so
\[
J_{\min} = 1.
\]
Because the background `\bar A = \Gamma + \gamma K` itself lies in the lowest
coexact vector shell, the active vector placement is fixed to the lowest
admissible vector channel.

### TT slot

TT output belongs to the TT branch `s = 2`, so
\[
J_{\min} = 2.
\]
The vector-to-TT zero-order bridge is again unique up to normalization on each
allowed branch.

Therefore, inside the realized typed bridge architecture, geometric mode
placement is not an extra postulate. It is forced by:

- block type,
- channel floor,
- background placement,
- and multiplicity-one bridge grammar.

## Corollary 32.E.1 - Exact GMP Upgrade

Status: `derived / scoped`

Inside the realized typed bridge class actually used by the IO bridge program:

\[
\boxed{
\text{GMP closes.}
}
\]

More precisely:

- the spatial channel is fixed by tensor type,
- the minimal puncture load is fixed by `J_min = s`,
- and the actual one-slot bridge intertwiners are multiplicity-one once the
  background is fixed.

So within this class there is no independent selector-level freedom left.

## Corollary 32.E.2 - Universal GMP Still Does Not Follow

Status: `derived / no-go boundary`

The old stronger statement

> every abstract physically admissible puncture-to-matter operator on the full
> local algebra is geometric

still does not follow.

Reason:

- the Paper 27 bypass class with identity spatial leg is not a typed
  boundary-to-bulk bridge map;
- Theorem 32.B does not prove that every physical matter observable belongs to
  the typed bridge/readout class;
- therefore the larger algebra still contains non-geometric operator classes not
  killed by block typing alone.

So the exact honest grading is:

\[
\boxed{
\text{typed GMP: derived;}
}
\]
\[
\boxed{
\text{universal GMP: not derived on the present stack.}
}
\]

## 4. Dead ends and routes that failed

### Dead end A: operator uniqueness does not imply ambient KMS uniqueness

The naive route

> unique `T_field` therefore unique full bridge state

fails.

It fails because the equilibrium state on the full bridge CCR carrier still
depends on the full ambient dynamics, not merely on one injective quotient map.

### Dead end B: transfer theory alone does not create Hawking thermality

Paper 32 transfer theory does not by itself prove Hawking thermality. The
Hawking input comes from black-hole QFT on stationary horizons plus one-mode KMS
uniqueness. What Paper 32 adds is transfer-lock: no second quotient state
survives once the bridge map is fixed.

### Dead end C: typed block architecture does not kill every bypass operator

Typed block structure forces GMP only inside the typed bridge class. It does not
automatically remove all non-geometric operators on the larger rate-dressing
algebra.

## 5. Final status by target

### `SP-2 / H1`

- `derived / scoped`: yes on the bridge-readable quotient
- `not derived`: no on the full ambient Paper 22 spatial KMS extension

### `SP-3 / C2q`

- `derived / scoped`: yes on the lowest-shell bridge-readable quotient

### `SP-4 / GMP`

- `derived / scoped`: yes on the realized typed bridge class
- `not derived`: no as a universal theorem on the larger local algebra

## Literature used

These external sources were used only where the internal stack genuinely needed
black-hole-QFT or CCR/KMS support:

1. Ko Sanders, "On the construction of Hartle-Hawking-Israel states across a
   static bifurcate Killing horizon" (existence plus Kay-Wald uniqueness
   context):
   https://arxiv.org/abs/1310.5537

2. Christian Gerard, "The Hartle-Hawking-Israel state on stationary black hole
   spacetimes" (unique Hadamard extension statement):
   https://arxiv.org/abs/1806.07645

3. Jan Derezinski, "Introduction to representations of the canonical
   commutation and anticommutation relations" (quasi-free CCR / Araki-Woods
   background used for the one-mode KMS uniqueness step):
   https://arxiv.org/abs/math-ph/0511030

## Bottom line

Paper 32 does not magically turn all three semiclassical seams into one
universal closure.

What it does do is sharper and better:

- it closes bridge state selection on the bridge-readable quotient,
- it locks `C2q` as a true theorem on the lowest-shell quotient,
- and it closes GMP on the realized typed bridge architecture while preserving
  the honest no-go boundary against the old fully universal wording.

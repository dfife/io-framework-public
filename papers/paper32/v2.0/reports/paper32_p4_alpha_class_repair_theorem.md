# Paper 32 - P4 Alpha-Class Repair Theorem

## Discipline label

- label state: `CLEAN`
- registry check: Vectors 1-5 reviewed. No unresolved load-bearing circularity-vector hit remains on this surface after the present audit.
- chain verification: verified through the cited Paper 32 chain to assumed-good Papers 1-31 nodes; no surfaced admission or unresolved local premise step remains load-bearing on this surface.
- admitted inputs surfaced here: none.
- usage rule: this theorem may be cited as a premise because it is `CLEAN`.


Date: 2026-04-05

## Executive result

`derived / scoped`: on the active Paper 32 source block, the DtN spectral-scale
measure is an `alpha = 1` observable.

This does **not** follow from "same carrier" alone. Cosmo's objection is
correct at that level. The closure uses four ingredients together:

1. Paper 18 classifies `alpha` by **primitive observable type**:
   line / `1`-form, area / `2`-form, volume / `3`-form.
2. Paper 25 shows that `V` versus `V'` is a **modular-readout versus
   variational** split and is not the same thing as changing `alpha`.
3. Paper 22 and Paper 28 place the active source datum on the coexact
   `1`-form connection carrier and identify the reduced source Hessian as the
   coexact `1`-form DtN operator.
4. Paper 28's relative-kernel theorem shows the physical boundary object
   entering P4 is a **derivative-free one-slot positive line operator** on that
   same carrier.

So the relevant question is not "the Hessian is second-order, so is it
alpha = 2?" The correct question is: what geometric object is the physical
readout transporting and measuring? On the current source block, it transports
and measures boundary connection perturbations in the coexact `1`-form sector.
That is the Paper 18 line class, hence `alpha = 1`.

`verified`: the counterfactual `alpha = 2` branch is **not** killed by the bare
identity `Z(e^(x^2)) = Q`; if one rewrites the entire counting law with
`1/x^2`, that identity still holds tautologically. So the honest kill on
`alpha = 2` is **typing**, not standalone numerics. Numerically, the
`alpha = 2` branch instead predicts the wrong source-block slope:

\[
\beta_{alpha=2} = \frac{K_{gauge}}{x^2} = 0.023781635272033575,
\]

which shifts the pivot source branch to

\[
n_s^{alpha=2} \approx 0.9762347465432093,
\]

instead of the accepted Paper 28 / Paper 32 branch near `0.96388`.

## The gap to close

Cosmo's remaining objection is precise:

> same carrier does not imply same observable class.

That objection is correct in general. Paper 25 already proves that two
different observable classes can live on the same carrier and read different
functions of the same gauge parameter. So the question is narrower:

> does the DtN spectral-scale readout belong to the Paper 18 line / `1`-form
> class, or does the Hessian status promote it to the area / `2`-form class?

The answer is yes, it belongs to the line / `1`-form class on the active
source block.

## Local stack used

### Paper 18

From [paper18_bdp_theorem_report.txt](/opt/cosmology-lab/results/paper18/paper18_bdp_theorem_report.txt):

- Proposition 18.11:
  connection `1`-form plus primitive line transport implies line scaling
  `R_U / r_s = 1/x`.
- Corollary 18.12:
  `alpha` is selected by observable type:
  `0`-form / scalar, `1`-form / line, `2`-form / area, `3`-form / volume.

From [paper18_bdp_gap_closure_report.txt](/opt/cosmology-lab/results/paper18/paper18_bdp_gap_closure_report.txt):

- the primitive observable for the `1`-form class is its line integral;
- BDP is derivative-built yet still `alpha = 1`.

So Paper 18 does **not** classify by "how many derivatives appear in some
later operator." It classifies by the primitive geometric observable being
measured.

### Paper 22

From [paper22_spatial_hodge_complex_report.txt](/opt/cosmology-lab/results/paper22/paper22_spatial_hodge_complex_report.txt):

\[
A = \Gamma + \gamma K
\]

is, in the active homogeneous gauge, an `su(2)`-valued coexact `1`-form on
`S^3`.

Therefore the active source perturbation `delta A` is a coexact connection
`1`-form perturbation.

### Paper 28

From [paper28_io_dtn_subprincipal_report.md](/opt/cosmology-lab/results/paper28/paper28_io_dtn_subprincipal_report.md):

- the source field is a boundary Ashtekar-Barbero `1`-form;
- the active source carrier is the coexact `1`-form sector;
- the reduced source Hessian is the coexact `1`-form DtN operator.

From [paper28_relative_kernel_one_slot_theorem_report.md](/opt/cosmology-lab/results/paper28/paper28_relative_kernel_one_slot_theorem_report.md):

\[
R_\gamma := O_\gamma O_0^{-1}
\]

is:

- one-slot,
- derivative-free,
- line-typed,
- a positive endomorphism of the single active coexact `1`-form carrier.

This is the crucial extra ingredient beyond "same carrier." The physical P4
object is not just any scalar extracted from a Hessian. It is already proved to
be a one-slot positive line object on that carrier.

### Paper 25

From [paper25_degree_theorem_identity_pin_reconciliation_analysis.py](/opt/cosmology-lab/results/paper25/paper25_degree_theorem_identity_pin_reconciliation_analysis.py) and [paper25_v_vs_vprime_class_membership_report.txt](/opt/cosmology-lab/results/paper25/paper25_v_vs_vprime_class_membership_report.txt):

- `V` versus `V'` is decided by fixed modular-readout class versus
  variational/relative class;
- this split is not the same as changing `alpha`;
- derivative-built observables can still be `alpha = 1` if the primitive datum
  is a `1`-form transfer object.

So Paper 25 supports Cosmo's warning in one sense and defeats it in another:

- yes, same carrier alone is not enough;
- no, reading `V` versus `V'` on the same carrier is **not** evidence for
  `alpha = 2`.

It is evidence that payload class and `alpha` class are distinct.

## External mathematics

The external operator theory supports the same separation:

1. Joshi-Lionheart show that the Dirichlet-to-Neumann map for the `k`-form
   Laplace equation has a full symbol on the boundary. That is a map attached
   to boundary `k`-form data, not a promotion to `(k+1)`-form data.
   Source: <https://arxiv.org/abs/math/9911212>
2. Sharafutdinov-Shonkwiler define the complete Dirichlet-to-Neumann map for
   differential forms in terms of boundary operators on differential forms.
   Source: <https://arxiv.org/abs/1011.1194>
3. Raulot-Savo compute the spectrum of the Dirichlet-to-Neumann operator
   acting on differential `p`-forms.
   Source: <https://arxiv.org/abs/1202.3605>
4. ter Elst-Gordon-Waurick give a first-order-system representation of the
   Dirichlet-to-Neumann operator. This reinforces that operator order and
   boundary bundle type are distinct notions.
   Source: <https://arxiv.org/abs/1707.05734>

These sources do not prove the IO coefficient by themselves. They do support
the specific structural claim used here:

> a DtN operator derived from a second variation still acts on the boundary
> differential-form data of the same degree; its Hessian origin does not by
> itself change the observable from line / `1`-form class to area / `2`-form
> class.

## Theorem 32.P4Alpha.1 - Observable rank is not operator order

Work in the Paper 18 alpha-ladder.

If an observable is typed by primitive transport / readout of a `k`-form datum,
then its `alpha`-class is determined by that primitive geometric rank:

- scalar / point / `0`-form -> `alpha = 0`
- line / connection / `1`-form -> `alpha = 1`
- area / plaquette / curvature / `2`-form -> `alpha = 2`
- volume / `3`-form -> `alpha = 3`

The differential order of a later operator used to realize the readout does not
by itself change the `alpha`-class.

### Proof

Paper 18 Proposition 18.11 and Corollary 18.12 explicitly classify by
primitive observable type. The proof of the `1`-form law uses the sentence:

> a connection is a `1`-form and its primitive gauge observable is line
> transport / Wilson-line type data, not area or volume weight.

Paper 18's own BDP observable is already a counterexample to the claim that
operator order fixes `alpha`: it is built from a first variation of transport,
yet it remains `alpha = 1` because the primitive observable is a `1`-form line
transfer datum.

Paper 25 then sharpens the orthogonality:

- `V` versus `V'` is fixed modular-readout versus variational class;
- this is not the same distinction as `alpha = 1` versus `alpha = 2`.

So the alpha-ladder is typed by primitive geometric object, while the payload
split `V` versus `V'` is typed by modular-readout versus variational grammar.
These are different axes.

QED.

## Theorem 32.P4Alpha.2 - DtN source spectral scale is alpha = 1

On the active Paper 32 source block, the DtN spectral-scale measure belongs to
the `alpha = 1` line class.

### Proof

1. By Paper 22, the active source perturbation is a coexact connection
   `1`-form:

   \[
   \delta A \in \Omega^1_{coex}(S^3; su(2)).
   \]

2. By Paper 28, the reduced source Hessian is the coexact `1`-form
   Dirichlet-to-Neumann operator. So the active boundary readout is the DtN
   response of boundary connection `1`-form data.

3. By the external DtN form literature, a DtN map for differential forms acts
   on boundary differential forms of the same degree. Its Hessian origin does
   not promote the measured boundary datum from a `1`-form object to a `2`-form
   plaquette object.

4. By Paper 28's relative-kernel theorem, the physical P4 boundary object

   \[
   R_\gamma = O_\gamma O_0^{-1}
   \]

   is not a two-slot self-intensity and not a variational derivative. It is a
   derivative-free one-slot positive line operator on the coexact `1`-form
   carrier.

5. By Theorem 32.P4Alpha.1, the relevant `alpha` is therefore determined by the
   primitive measured object: line / connection / `1`-form.

Hence the DtN spectral-scale measure on the active source block is

\[
\boxed{\alpha = 1.}
\]

Therefore the accessible divisor is

\[
\boxed{\frac{1}{x}}
\]

and not `1/x^2`.

QED.

## Corollary 32.P4Alpha.2b - Kill B falls on the active source block

The remaining Cosmo objection

> same carrier is not same class

is resolved here in the only honest way:

- `same carrier` alone is indeed insufficient;
- but `same carrier + derivative-free + one-slot + line-typed + coexact 1-form
  DtN` is enough.

So Kill B falls on the active source block.

## Counterfactual alpha = 2 audit

If one **ignores** the typing theorem and forces the DtN spectral measure into
the area class, then the accessible law would become

\[
d\mu_{acc}^{(2)} = \frac{1}{x^2}\frac{ds}{s},
\qquad
n_{acc}^{(2)}(s) = \frac{\ln s}{x^2}.
\]

Then one accessible cell would be redefined by

\[
n_{acc}^{(2)}(b_2)=1
\quad\Rightarrow\quad
b_2 = e^{x^2}.
\]

With the same constant logarithmic payload `K_gauge`, this gives

\[
Z_{alpha=2}(s) = s^{K_{gauge}/x^2},
\qquad
Z_{alpha=2}(e^{x^2}) = e^{K_{gauge}} = Q.
\]

So:

- `verified`: `alpha = 2` is **not** killed by the bare identity
  `Z(e^(x^2)) = Q`;
- `verified`: if one instead keeps the already-used `e^x` cell while changing
  only the exponent, then `Z_{alpha=2}(e^x) = 1.0367847149459515 != Q`, but
  that mixed comparison is not the self-consistent `alpha = 2` branch.

The honest way `alpha = 2` fails is different:

it predicts the wrong source-block slope.

At the pivot shell `N = 712`:

- `alpha = 1` branch:
  \[
  n_s^{avg} \approx 0.9638834816804986
  \]
- `alpha = 2` branch:
  \[
  n_s^{avg} \approx 0.9762347465432093
  \]

So `alpha = 2` is excluded by typed source-block structure and the accepted
Paper 28 / Paper 32 slope law, not by the isolated algebraic identity alone.

## Why Paper 25 does not reopen alpha

Paper 25's `V` versus `V'` distinction does **not** imply a change in `alpha`.

The correct reading is:

- `alpha` tells you the geometric observable class:
  line, area, volume, etc.
- `V` versus `V'` tells you the payload/readout class:
  fixed modular-readout versus variational/relative.

These are different axes.

In particular:

- BDP is `alpha = 1` and reads `V'`;
- the fixed modular-readout source character is `alpha = 1` and reads `V`.

So different functions of the same gauge variable can live on the same
`alpha = 1` class. That is not evidence for `alpha = 2`.

## Consequence for P4

Once Kill B is repaired, the repaired P4 chain is:

1. the DtN source spectral-scale measure is `alpha = 1`;
2. therefore the accessible counter is
   \[
   n_{acc}(s)=\frac{\ln s}{x};
   \]
3. the constant logarithmic payload is
   \[
   K_{gauge} = \ln(1+\gamma^2);
   \]
4. therefore
   \[
   Z(s)=s^{K_{gauge}/x};
   \]
5. on one accessible cell `s = e^x`,
   \[
   Z(e^x)=e^{K_{gauge}}=Q=1+\gamma^2.
   \]

So P4 remains `derived / scoped` on the active source block.

## Exact claim boundary

`derived / scoped`:

- the DtN spectral-scale measure on the active source block is `alpha = 1`;
- operator order does not promote it to `alpha = 2`;
- Kill B falls;
- P4 stays closed on the active source block.

`verified`:

- the self-consistent `alpha = 2` branch does not numerically self-destruct at
  the identity level;
- it instead gives the wrong source-block slope and wrong pivot `n_s`.

`important honesty point`:

- if someone reopens the deeper class-membership statement that the active
  source correction belongs to the kernel-level one-slot finite transfer
  character on the DtN line semigroup, then the surviving seam is that broader
  class-membership theorem, not Kill B by itself.

Given the current Paper 28 / Paper 32 accepted stack, however, Kill B is the
remaining seam and it is now closed.

## Sources

- Joshi-Lionheart, harmonic differential forms and DtN full symbol:
  <https://arxiv.org/abs/math/9911212>
- Sharafutdinov-Shonkwiler, complete DtN map for differential forms:
  <https://arxiv.org/abs/1011.1194>
- Raulot-Savo, DtN spectrum acting on differential `p`-forms:
  <https://arxiv.org/abs/1202.3605>
- ter Elst-Gordon-Waurick, DtN as first-order boundary system:
  <https://arxiv.org/abs/1707.05734>

# Paper 32 - Full Active Source-Block Derivation of P4

Date: 2026-04-05

## Question

Can the Paper 32 direct-class result be promoted from

- the **exact flat PG collar model**

to

- the **full active reduced source block**

so that

\[
P4:\qquad Z(e^x)=Q=1+\gamma^2
\]

is fully `derived / scoped` on the physical source block, not only on the exact
model collar?

## Executive result

Yes.

The exact flat-collar hypothesis can be removed. The real class-forcing input is
not the special shell law `\sigma_\ell=(\ell+1)/r_s`; it is the stronger
statement that the physical reduced source map is **DtN-type on the canonical
coexact carrier**.

That statement is already in the stack:

1. Paper 28 proves that on the canonical coexact carrier, the reduced boundary
   action is of DtN type.
2. External DtN factorization theory proves that every such DtN map is an
   elliptic order-`1` boundary-normal transport operator.
3. The direct Paper 32 class criterion only used:
   - open one-dimensional transport,
   - one inserted first variation along that line,
   - line-length scaling.

Those three facts hold for the full DtN-type source map exactly as they hold for
the exact flat-collar model. Therefore the physical source map lies in the same
`\alpha=1` observable class as Paper 18's open-transport variation, on the full
active reduced source block.

Once that is in place, the rest of the P4 chain is already local and derived:

- Paper 28 relative-kernel typing:
  \[
  R_\gamma = O_\gamma O_0^{-1}
  \]
  is a one-slot positive line operator on the canonical coexact carrier;
- the active scalar source readout uses the unique local scalar bridge channel;
- the one-cell local reduced source ratio is
  \[
  O_\gamma^{\rm cell}=Q\,O_0^{\rm cell},
  \qquad Q=1+\gamma^2=e^{K_{\rm gauge}}.
  \]

Hence

\[
Z(s)=s^{K_{\rm gauge}/x},
\qquad
Z(e^x)=Q.
\]

So P4 is `derived / scoped` on the **full active reduced source block**.

## Claim discipline

- `derived`: mathematically proved from stated assumptions
- `verified`: numerically checked from explicit formulas
- `conditional`: valid if an extra stated hypothesis holds
- `reconstruction`: coherent explanatory model, not yet derived
- `speculative`: idea worth exploring, not yet established

## 1. What the direct assault actually needed

The earlier direct-class theorem was written on the exact flat PG collar, but
its proof used only the following abstract criterion extracted from Paper 18:

\[
\boxed{
\text{open 1D transport}
\;+\;
\text{single inserted variation}
\;+\;
\text{line-length scaling}
\Longrightarrow
\alpha=1.
}
\]

The proof did **not** use:

- the exact Karpukhin shell law `\sigma_\ell=(\ell+1)/r_s`,
- the exact Euclidean ball multiplicities,
- or any shell-specific feature beyond the existence of the DtN transport
  semigroup.

So if those three transport features hold for the physical reduced source map,
the exact same `\alpha=1` conclusion follows.

## 2. The physical source map is already DtN-typed

Paper 28's boundary RG selection theorem records as `derived`:

\[
\text{on the canonical coexact carrier, the reduced boundary action is of DtN type.}
\]

Call the physical reduced source Hessian on that active block

\[
\Lambda_{\rm src}.
\]

The point is:

- this is not merely "another operator on the same carrier";
- it is the actual **DtN-type boundary map** of the source problem.

So the remaining class question is:

> what `\alpha`-class does a DtN-type boundary map belong to?

That is a mathematical question about the observable map itself, not about the
carrier alone.

## 3. External DtN theorem on general elliptic connection problems

Let `L` be a second-order elliptic boundary value problem on a vector bundle
over a collar, with Dirichlet boundary data, and let `\Lambda_L` be its DtN map.

Standard DtN factorization theory gives:

1. `\Lambda_L` is an elliptic pseudodifferential operator of order `1`.
2. `L` factors near the boundary into first-order normal pieces modulo
   smoothing.
3. `\Lambda_L` is represented at the boundary by that first-order normal
   factor.

In particular, `\Lambda_L` generates the open normal transport semigroup

\[
P_t=e^{-t\Lambda_L},\qquad t\ge 0.
\]

For a differentiable family `\Lambda_{L,\varepsilon}`, Duhamel gives

\[
\frac{d}{d\varepsilon}e^{-t\Lambda_{L,\varepsilon}}\Big|_{\varepsilon=0}
=
-\int_0^t
e^{-(t-s)\Lambda_{L,0}}\,
\dot\Lambda_{L,0}\,
e^{-s\Lambda_{L,0}}
\,ds.
\]

That is exactly:

- open transport on a one-dimensional base `t`,
- one inserted perturbation,
- integrated along that one-dimensional base.

So every DtN-type source map has the same primitive transport grammar used in
Paper 18's `\alpha=1` theorem.

## 4. Main transport-class promotion theorem

## Theorem 32.KB.3 - DtN-Type Promotion Theorem

Status: `derived / scoped`

Assume:

1. the physical reduced source map on the active source block is DtN-type on
   the canonical coexact carrier;
2. Paper 18's `\alpha` classification is determined by primitive observable
   type:
   open one-dimensional transport with one inserted first variation scales as a
   line observable;
3. accessibility acts on the primitive observable class, not on the detailed
   shell formula.

Then the physical reduced source map belongs to the same `\alpha=1`
observable class as the Paper 18 first variation of open covariant transport.

### Proof

By assumption 1 and the standard DtN factorization theorem, the physical source
map is a first-order boundary-normal transport operator. Therefore it generates
the open semigroup

\[
P_t=e^{-t\Lambda_{\rm src}}
\]

on the one-dimensional collar-normal base.

For any differentiable perturbation of the source problem, Duhamel gives a
single inserted variation integrated along that same normal line.

So the physical source map satisfies exactly the three structural hypotheses
actually used in the Paper 18 `\alpha=1` proof:

1. open one-dimensional transport,
2. one inserted first variation,
3. line-length scaling on homologous transfer curves.

Therefore the physical source map lies in the `\alpha=1` observable class.

QED.

## 5. Why lower-order DtN deformations do not reopen the class question

Paper 28 already proved that, within the natural local reduced-hessian class:

- the reduced source action is DtN-type;
- genuine `O(1)` shell deformations are excluded;
- any local zeroth-order boundary endomorphism is shell-blind;
- remaining same-class corrections are lower-order.

Those facts can change:

- the detailed shell law,
- the subprincipal offset,
- and the `O(\ell^{-1})` remainder.

They do **not** change:

- the existence of the open normal transport semigroup,
- the one-dimensional transport base,
- or the inserted-variation grammar.

So they cannot change the primitive `\alpha`-class. They only deform the same
`\alpha=1` DtN transport observable inside its class.

This is exactly the step that removes the old "exact flat PG collar" caveat.

## 6. Accessible generator on the full active source block

Let

\[
Y_{\rm src}:=\log(r_s\Lambda_{\rm src}).
\]

Because Theorem 32.KB.3 identifies the physical source map as `\alpha=1`, the
Paper 18 line-accessibility divisor applies directly to the physical source
generator:

\[
\boxed{
N_{\rm acc}
=
\frac1x\,Y_{\rm src}
=
\frac1x \log(r_s\Lambda_{\rm src}).
}
\]

One accessible line cell is therefore characterized by

\[
N_{\rm acc}=1
\qquad\Longleftrightarrow\qquad
Y_{\rm src}=x
\qquad\Longleftrightarrow\qquad
s=e^x.
\]

This does not require the special exact shell law. It uses only the logarithmic
DtN scale of the actual physical source map.

## 7. Local source payload and character

The remaining inputs are already local and derived:

1. Paper 28 relative-kernel one-slot theorem:
   \[
   R_\gamma=O_\gamma O_0^{-1}
   \]
   is a one-slot positive line operator.
2. Paper 23 bridge uniqueness plus Paper 28 local scalar-channel audit:
   the active scalar source readout uses the unique local scalar bridge channel.
3. The local source-cell ratio is
   \[
   O_\gamma^{\rm cell}=Q\,O_0^{\rm cell},
   \qquad
   Q=1+\gamma^2=e^{K_{\rm gauge}}.
   \]

Therefore the unique continuous positive source character is

\[
Z
=
\exp(K_{\rm gauge}N_{\rm acc}),
\]

so

\[
\boxed{
Z(s)
=
\exp\!\left(K_{\rm gauge}\frac{\log s}{x}\right)
=
s^{K_{\rm gauge}/x}.
}
\]

Evaluating on one accessible cell gives

\[
\boxed{
Z(e^x)=e^{K_{\rm gauge}}=Q=1+\gamma^2.
}
\]

## Corollary 32.KB.3a - P4 Is Fully Derived On The Full Active Reduced Source Block

Status: `derived / scoped`

On the full active reduced source block,

\[
\boxed{
P4:\qquad Z(e^x)=Q=1+\gamma^2
}
\]

is no longer an explicit premise.

## Corollary 32.KB.3b - Theorem 32.A Source Coefficient Is Fully Derived On The Physical Source Block

Status: `derived / scoped`

On the same scope,

\[
\eta=\frac{K_{\rm gauge}}{x}
\]

is fully derived from:

- DtN typing of the reduced source map,
- the direct class theorem for DtN transport observables,
- one-slot positive line typing of the relative kernel,
- and the local source-cell payload `Q`.

## Exact boundary

### Derived / scoped

- the physical reduced source map is in the same `\alpha=1` transport class as
  Paper 18's open-transport variation whenever it is DtN-type on the canonical
  coexact carrier;
- Paper 28 already certifies the active reduced source block as DtN-type;
- therefore P4 is fully derived on the full active reduced source block.

### Not claimed

- a theorem about arbitrary unreduced observables outside the active source
  block;
- literal microscopic identity between the DtN source map and the Wilson-line
  variation of Paper 18;
- anything about unrelated observable classes supported on the same carrier.

## Numerical check

With the lab constants

- `x = 1.519`
- `gamma = 0.2375`
- `Q = 1 + gamma^2 = 1.05640625`
- `K_gauge = ln(Q) = 0.05487281774291466`

the derived source character is

\[
Z(s)=s^{0.036124303978219},
\]

and on one accessible source cell

\[
Z(e^x)=e^{K_{\rm gauge}}=1.05640625=Q.
\]

## Source support

- Paper 18 - BDP Upgrade Theorem:
  `\alpha=1` is fixed by primitive open one-dimensional transport with one
  inserted `1`-form variation.
- Paper 28 - Boundary RG Selection Principle:
  the reduced boundary action is DtN-type on the canonical coexact carrier.
- Paper 28 - Relative Kernel One-Slot Theorem:
  the physical source ratio is a one-slot positive line operator.
- Paper 28 - Coexact Bridge Population Audit:
  the active local scalar bridge channel is unique and fiberwise one-dimensional.
- C. Valero, *A uniqueness result for the Calderon problem with partial data for
  connections and potentials on Riemannian manifolds*:
  DtN maps for elliptic connection problems are order-1 pseudodifferential
  operators and arise from first-order normal factorization at the boundary.
- Raulot-Savo:
  DtN maps on differential forms remain order-1 boundary operators on the form
  carrier.

## Final status

\[
\boxed{
\text{Yes. P4 is fully derived on the full active reduced source block.}
}
\]

# Paper 31 §13.6 Weyl Half-Order Kernel Derivation Audit

Date: 2026-05-21

## Question

Can the step

```text
alpha_delta - alpha_Phi = 3/2 - 2 = -1/2
```

to the CMB Weyl/lensing kernel large-k exponent

```text
M_IO(k) ~ x^(-1/2) (k/k_p)^(-1/2)
```

be promoted from `RECONSTRUCTION` to theorem grade using the existing IO stack
through Paper 35 plus standard external physics?

## Executive Result

Yes, but only for the **large-k / principal-symbol exponent** in the scalar
Born/Weyl observable class. The exact finite-shell multiplier

```text
M_N^IO = x^(-1/2) * [ (lambda_N - 3)/(lambda_Np - 3) ]^(-1/4)
```

does not become a global exact theorem from the current stack. It remains the
minimal/natural representative unless an additional theorem excludes lower-order
or non-minimal spectral dressings.

Recommended split:

```text
DERIVED/CONDITIONAL_VERIFIED:
  principal-symbol / large-k exponent -1/2 for the scalar Born Weyl-lensing
  kernel, conditional on the Paper 31 scalar Weyl observable class and the
  standard local-natural pseudodifferential realization of observable-class
  order gaps.

RECONSTRUCTION or DERIVED/CONDITIONAL_VERIFIED with explicit minimality scope:
  exact finite-shell pure-power multiplier with no lower-order spectral
  corrections.
```

No PlanckLite fitted tilt is used in the derivation. The fitted `-0.4625` value
remains numerical confirmation only.

## Route 1: Local-Natural Pseudodifferential Order Route

### Verdict

Closes the large-k exponent. Partial for the exact finite-shell multiplier.

### Theorem 31.K1: Observable-Class Gap to Principal Spectral Order

Status: `DERIVED/CONDITIONAL_VERIFIED` for the linear scalar Born/Weyl CMB
lensing observable class.

Statement. Let the density-side observable and Weyl-side observable be the
Paper 31 scalar Born observables with class exponents

```text
alpha_delta = 3/2,
alpha_Phi = 2.
```

Assume the relative field-level Weyl kernel is local-natural, rotationally
invariant on the closed `S^3` scalar sector, and realizes the class conversion
by a scalar pseudodifferential operator on the physical inhomogeneous scalar
shells. Then the principal symbol of the relative kernel has homogeneous degree

```text
alpha_delta - alpha_Phi = -1/2.
```

Equivalently, in the local high-shell limit,

```text
M_IO(k) ~ x^(-1/2) (k/k_p)^(-1/2).
```

### Proof

1. Paper 19/Paper 31 establish the density readout as the transport /
   continuity scalarization class:

   ```text
   alpha_delta = 3/2.
   ```

2. Paper 31's internal Weyl-potential theorem establishes the Weyl/Bardeen
   seed as the intrinsic-slice curvature scalarization class:

   ```text
   alpha_Phi = 2.
   ```

3. Therefore the relative observable-class exponent is

   ```text
   alpha_delta - alpha_Phi = -1/2.
   ```

4. Under standard local-covariant field theory on a compact homogeneous
   spatial slice, a scalar rotationally invariant linear operator is represented
   microlocally by a scalar pseudodifferential operator. Its principal symbol is
   homogeneous in cotangent momentum:

   ```text
   sigma_pr(A)(c xi) = c^m sigma_pr(A)(xi),
   ```

   where `m` is the pseudodifferential order.

5. A relative observable-class conversion by `Delta alpha` changes inverse-
   length weight by exactly `Delta alpha`. Therefore the relative
   pseudodifferential order is

   ```text
   m = alpha_delta - alpha_Phi = -1/2.
   ```

6. On the closed `S^3` scalar sector,

   ```text
   -Delta_S3 Q_N = lambda_N Q_N,
   lambda_N = N(N+2).
   ```

   The physical inhomogeneous scalar curvature shell uses

   ```text
   L := -Delta_S3 - 3,
   L Q_N = (lambda_N - 3) Q_N.
   ```

7. Standard spectral calculus gives the principal realization of order `m` as

   ```text
   L^(m/2).
   ```

   With `m = -1/2`, this is

   ```text
   L^(-1/4),
   ```

   so the mode multiplier has leading shell dependence

   ```text
   (lambda_N - 3)^(-1/4).
   ```

8. In the high-shell / local-FRW limit,

   ```text
   lambda_N - 3 ~ N^2,
   k ~ N/R,
   ```

   hence

   ```text
   (lambda_N - 3)^(-1/4) ~ k^(-1/2).
   ```

9. The constant observable-class Jacobian ratio from Paper 31 is

   ```text
   J_Phi/J_delta = x^(alpha_delta-alpha_Phi) = x^(-1/2).
   ```

10. Normalizing at a pivot shell gives the principal large-k representative

   ```text
   M_IO(k) ~ x^(-1/2) (k/k_p)^(-1/2).
   ```

QED.

### Chain

```text
Theorem 31.K1
  <- Paper 31 v2.0 internal alpha_Phi = 2 theorem for Weyl/Bardeen seed
  <- Paper 19 v1.5 alpha_delta = 3/2 transport/continuity scalarization class
  <- Paper 22 v2.0 spatial Hodge/S^3 scalar-sector structure
  <- Paper 23 scalar shell dictionary and physical inhomogeneous shell operator
     lambda_N - 3
  <- standard spectral theorem and pseudodifferential principal-symbol
     calculus on compact homogeneous manifolds
  <- standard scalar Born weak-lensing/Weyl observable grammar imported under P2
  <- P1, closed K=+1 OS interior with S^3 spatial slices
  <- P2, exterior physics imported inside the horizon.
```

## Route 2: Exact Finite-Shell Pure-Power Multiplier

### Verdict

Partial only. The current stack supports the minimal natural representative,
but does not force uniqueness of the exact finite-shell function.

The theorem above forces the principal symbol:

```text
M_N = x^(-1/2) [ (lambda_N - 3)/(lambda_Np - 3) ]^(-1/4)
      * [1 + lower-order spectral corrections].
```

To remove the bracket, the stack would need an additional theorem:

```text
No Lower-Order Weyl-Kernel Dressing Theorem:
  on the scalar Born Weyl observable class, every IO-admissible rotationally
  invariant, local-natural, pivot-normalized relative kernel with the required
  class order is exactly the pure spectral power L^(-1/4).
```

That theorem is not currently banked. Without it, functions such as

```text
L^(-1/4) * h(L/L_p)
```

with `h(1)=1` and `h(t)=1+O(t^-1/2)` preserve the same principal exponent while
changing finite-shell behavior. Those functions are not fitted by the theorem;
they are simply not excluded by the current stack.

## Route 3: Paper 28 / Paper 32 Fixed-Point Closure Analogy

### Verdict

Does not close Paper 31 §13.6 globally.

Paper 28 / Paper 32 close multiplicative DtN fixed-point class membership for
the active reduced scalar-source block. That is a theorem-grade result, but
its scope is the primordial source covariance/readout block:

```text
C_phys = T_field^* C_0 T_field.
```

The CMB Weyl lensing kernel is an observer-side projected Weyl/light-deflection
operator, not the same source-block covariance. Importing the Paper 28 fixed-
point theorem directly into §13.6 would overextend its scope.

It can be cited as precedent for how a pure power becomes theorem-grade when a
source-block character is forced. It cannot by itself force the exact Weyl
lensing finite-shell kernel.

## Route 4: Paper 23 n-to-k Dictionary

### Verdict

Partial only.

The dictionary maps the spectral shell weight to the high-k exponent:

```text
lambda_N - 3 ~ k^2
```

so an eigenvalue multiplier power `-1/4` maps to a k-space power `-1/2`.

But the dictionary does not derive the eigenvalue power. It only translates it.

## Route 5: S8 / E_G Weyl-Response Bridge

### Verdict

Partial only.

Paper 31's Weyl-response bridge gives the constant class Jacobian

```text
J_Phi/J_delta = x^(-1/2).
```

That closes the constant response ratio for scalar Born weak-lensing
observables. It does not by itself derive the scale-dependent `k^-1/2` tilt.
The scale dependence enters only after adding the local-natural
pseudodifferential-order realization in Route 1.

## Route 6: PlanckLite Surrogate Fit

### Verdict

No theorem closure.

The surrogate fit value

```text
t_lens = -0.4625
```

is useful independent numerical confirmation. It cannot be used to derive the
exponent. Treating it as the selector would be an observational fit pattern.

## Route 7: Standard Poisson / GR Lensing Kernel

### Verdict

No closure.

The standard closed-FRW scalar equations and the Weyl/Bardeen potential
relations are necessary background physics, but they do not fix the IO
observer-side typed readout kernel. The bulk Poisson relation remains intact;
the issue is the boundary observer's relative readout of density-class and
Weyl-class observables. Standard GR alone therefore cannot supply the IO
kernel exponent.

## Recommended Claim Text

Use this split in Paper 31 if §13.6 is revised:

```text
The large-k exponent is theorem-grade in the scalar Born/Weyl observable class.
The observable-class gap alpha_delta-alpha_Phi=-1/2 fixes the principal
pseudodifferential order of the local-natural relative Weyl kernel. On the
closed S^3 scalar sector, the physical inhomogeneous shell operator is
L=-Delta_S3-3 with eigenvalues lambda_N-3, so the minimal principal
representative is L^(-1/4). Since lambda_N-3 ~ k^2 at high shell number, the
kernel has large-k form x^(-1/2)(k/k_p)^(-1/2).

This promotes the asymptotic half-order tilt to
DERIVED/CONDITIONAL_VERIFIED for the linear scalar Born/Weyl observable class.
The exact finite-shell pure-power multiplier remains the minimal natural
representative, not a fully forced global theorem, unless a separate no-lower-
order-dressing theorem is proved.
```

## Final Boundary

The current `RECONSTRUCTION` label is too weak for the large-k exponent but
appropriate for the exact finite-shell pure-power form if stated without a
minimality/scope qualifier.

Strongest honest upgrade:

```text
Large-k exponent -1/2:
  DERIVED/CONDITIONAL_VERIFIED
  scoped to scalar Born/Weyl CMB lensing principal-symbol class.

Exact finite-shell M_N pure-power law:
  RECONSTRUCTION, or DERIVED/CONDITIONAL_VERIFIED only if explicitly scoped as
  the minimal local-natural principal representative with no claim that all
  lower-order spectral dressings are excluded.
```


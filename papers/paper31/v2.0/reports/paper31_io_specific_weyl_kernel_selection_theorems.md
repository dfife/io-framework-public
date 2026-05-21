# Paper 31 - IO-Specific Weyl-Kernel Selection Theorems

Date: 2026-05-21

## Purpose

Answer whether Paper 31 can add IO-specific, non-universal selection theorems
that remove the finite-shell lower-order dressing freedom in the CMB Weyl
half-order kernel.

Short answer: yes, but only with a visible scope condition. The clean route is
not a universal statement about all possible scalar kernels on `S^3`. It is a
selection theorem for the **Paper 31 scalar Born/Weyl typed readout quotient**:
the kernel is the unique continuous positive multiplicative character realizing
the `alpha_delta -> alpha_Phi` class conversion on the IO scalar-shell line
scale.

That theorem selects the pure finite-shell power. It does not claim that raw
abstract spectral dressings are impossible as algebraic operators.

## Definitions

### Definition 31.KS1: Scalar Born/Weyl Typed Readout Quotient

The scalar Born/Weyl typed readout quotient is the observer-side linear scalar
lensing class in which:

1. the density-side input is the Paper 19 transport/continuity scalarization
   class with `alpha_delta = 3/2`;
2. the Weyl-side output is the Paper 31 intrinsic-slice curvature scalarization
   class with `alpha_Phi = 2`;
3. the bulk scalar equations are the standard closed-FRW scalar perturbation
   equations on the `K=+1` `S^3` interior;
4. the observer-side lensing operator is restricted to the scalar Born channel:
   no vector lensing, tensor lensing, post-Born corrections, nonlinear
   structure, survey noise, or late-time astrophysical transfer packaging.

Status: `DERIVED/CONDITIONAL_VERIFIED` as a definition of the already-scoped
Paper 31 observable class.

Chain:

```text
Definition 31.KS1
  <- Paper 31 v2.0 Weyl-response bridge theorem for linear scalar lensing
  <- Paper 31 internal alpha_Phi = 2 theorem
  <- Paper 19 alpha_delta = 3/2 transport/continuity scalarization theorem
  <- standard scalar Born weak-lensing grammar imported under P2
  <- P1, closed K=+1 OS interior with S^3 scalar sector
  <- P2, exterior physics imported inside the horizon.
```

### Definition 31.KS2: IO-Admissible Single-Character Weyl Kernel

An IO-admissible single-character Weyl kernel on the quotient of Definition
31.KS1 is a mode multiplier `M(s)` on the positive scalar shell line-scale
variable

```text
s_N := (lambda_N - 3)/(lambda_Np - 3) > 0
```

such that:

1. `M(s)` is real, positive, and continuous for `s > 0`;
2. `M(1)=x^(alpha_delta-alpha_Phi)=x^(-1/2)`;
3. after factoring out the constant readout Jacobian, the residual shell
   function

   ```text
   m(s) := M(s)/M(1)
   ```

   is a multiplicative character of the scalar shell line-scale:

   ```text
   m(s_1 s_2)=m(s_1)m(s_2);
   ```

4. the character has principal pseudodifferential order

   ```text
   alpha_delta-alpha_Phi = -1/2.
   ```

This is not a universal definition of every algebraically writable operator on
`L^2(S^3)`. It is the IO readout-selection criterion for a kernel that carries
only the typed class conversion and no independent finite-shell transfer
physics.

Status: `DERIVED/CONDITIONAL_VERIFIED` if cited only as the admissibility
criterion for the Paper 31 scalar Born/Weyl typed readout quotient. It would be
a new premise if asserted for arbitrary Weyl kernels outside this quotient.

Chain:

```text
Definition 31.KS2
  <- Definition 31.KS1
  <- Paper 28 v2.0 Theorem 28.5, multiplicative composition / Cauchy character
     theorem for scale-line readout characters
  <- Paper 31 §13 Weyl-response bridge: the class conversion is a readout
     character, not a modification of the bulk Poisson equation
  <- standard functional calculus and spectral theorem for positive
     self-adjoint scalar shell operators
  <- P1 and P2 through Definition 31.KS1.
```

## Lemma 31.KS3: Continuous Positive Character Rigidity

Statement. If `m:(0,infinity)->(0,infinity)` is continuous and satisfies

```text
m(s_1 s_2)=m(s_1)m(s_2),
```

then there is a unique real number `p` such that

```text
m(s)=s^p.
```

Proof. Define `g(u)=log m(e^u)`. Positivity makes the logarithm well-defined,
and multiplicativity gives

```text
g(u+v)=g(u)+g(v).
```

Continuity gives the standard continuous Cauchy solution

```text
g(u)=p u
```

for a unique real `p`. Therefore

```text
m(e^u)=e^{pu},
```

so `m(s)=s^p`. QED.

Status: `IMPORTED/EMPIRICAL` as standard real analysis / Cauchy character
theorem, or `DERIVED/THEOREM` if treated as an elementary mathematical lemma
inside Paper 31.

Chain:

```text
Lemma 31.KS3
  <- standard continuous Cauchy functional equation on the multiplicative
     positive real group.
```

## Lemma 31.KS4: Principal Order Fixes the Character Exponent

Statement. On the scalar Born/Weyl typed readout quotient, the character
exponent in Lemma 31.KS3 is

```text
p = (alpha_delta-alpha_Phi)/2 = -1/4
```

when written as a function of the eigenvalue line-scale

```text
s_N = (lambda_N - 3)/(lambda_Np - 3),
```

and is

```text
alpha_delta-alpha_Phi = -1/2
```

when written as a large-`k` power.

Proof. The class gap is

```text
alpha_delta-alpha_Phi = 3/2 - 2 = -1/2.
```

This is the pseudodifferential order of the relative field-level class
conversion on the scalar Born/Weyl quotient. On `S^3`, the physical scalar
shell operator is

```text
L = -Delta_S3 - 3,
L Q_N = (lambda_N - 3) Q_N.
```

A pseudodifferential operator of order `q` is represented at principal spectral
level by `L^(q/2)`. Therefore, with `q=-1/2`, the eigenvalue character is

```text
s_N^(-1/4).
```

Because `lambda_N-3 ~ k^2` at high shell number, this becomes the large-`k`
power

```text
k^(-1/2).
```

QED.

Status: `DERIVED/CONDITIONAL_VERIFIED` on Definition 31.KS1.

Chain:

```text
Lemma 31.KS4
  <- Definition 31.KS1
  <- Paper 31 internal alpha_Phi = 2 theorem
  <- Paper 19 alpha_delta = 3/2 theorem
  <- Paper 23 scalar shell dictionary / physical inhomogeneous shell
     lambda_N - 3
  <- standard spectral calculus on compact manifolds
  <- P1 and P2.
```

## Theorem 31.KS5: IO-Specific Weyl-Kernel Single-Character Selection

Statement. Within the scalar Born/Weyl typed readout quotient of Definition
31.KS1, if the CMB Weyl kernel is restricted to the IO-admissible
single-character class of Definition 31.KS2, then the unique finite-shell mode
multiplier is

```text
M_N^IO
  = x^(-1/2)
    [ (lambda_N - 3)/(lambda_Np - 3) ]^(-1/4).
```

Its high-shell / local-`k` representative is

```text
M_IO(k) ~ x^(-1/2) (k/k_p)^(-1/2).
```

Proof. By Definition 31.KS2, write

```text
M(s)=M(1)m(s),
M(1)=x^(alpha_delta-alpha_Phi)=x^(-1/2).
```

The residual function `m` is a continuous positive multiplicative character.
By Lemma 31.KS3,

```text
m(s)=s^p
```

for a unique real `p`. By Lemma 31.KS4, the eigenvalue-scale exponent is

```text
p=-1/4.
```

Therefore

```text
M(s)=x^(-1/2)s^(-1/4).
```

Substituting the scalar shell line-scale

```text
s=s_N=(lambda_N-3)/(lambda_Np-3)
```

gives

```text
M_N^IO
  = x^(-1/2)
    [ (lambda_N - 3)/(lambda_Np - 3) ]^(-1/4).
```

Since `lambda_N-3 ~ k^2` at high shell number, the large-`k` form is

```text
M_IO(k) ~ x^(-1/2)(k/k_p)^(-1/2).
```

QED.

Status: `DERIVED/CONDITIONAL_VERIFIED` for the scalar Born/Weyl typed readout
quotient and the single-character IO-admissible kernel class. Not a universal
theorem for arbitrary spectral dressings on the raw scalar algebra.

Chain:

```text
Theorem 31.KS5
  <- Definition 31.KS1, scalar Born/Weyl typed readout quotient
  <- Definition 31.KS2, IO-admissible single-character Weyl kernel
  <- Lemma 31.KS3, continuous positive character rigidity
  <- Lemma 31.KS4, class gap fixes spectral exponent
  <- Paper 31 Weyl-response bridge theorem
  <- Paper 31 internal alpha_Phi = 2 theorem
  <- Paper 19 alpha_delta = 3/2 theorem
  <- Paper 23 scalar shell dictionary / lambda_N - 3 physical shell operator
  <- Paper 28 v2.0 Theorem 28.5, multiplicative composition theorem
  <- standard scalar Born weak-lensing grammar imported under P2
  <- standard spectral theorem / functional calculus on compact manifolds
  <- P1, closed K=+1 OS interior with S^3 scalar sector
  <- P2, exterior physics imported inside the horizon.
```

## Theorem 31.KS6: Lower-Order Dressing Exclusion Within the Single-Character Class

Statement. In the IO-admissible single-character class of Definition 31.KS2,
no nontrivial finite-shell dressing

```text
M_N = x^(-1/2) s_N^(-1/4) h(s_N)
```

is allowed unless `h(s)=1` for all `s>0`.

Proof. Since both `M(s)/M(1)` and `s^(-1/4)` are multiplicative characters,
their quotient

```text
h(s)=m(s)/s^(-1/4)
```

is also a continuous positive multiplicative character. The principal-order
condition requires `h` to have order zero. By Lemma 31.KS3, `h(s)=s^r` for
some real `r`. Order zero gives `r=0`, hence `h(s)=1`. QED.

Status: `DERIVED/CONDITIONAL_VERIFIED` within the single-character class.

Chain:

```text
Theorem 31.KS6
  <- Definition 31.KS2
  <- Lemma 31.KS3
  <- Lemma 31.KS4
  <- Theorem 31.KS5.
```

## Corollary 31.KS7: Raw Spectral Dressing No-Go

Statement. The exact finite-shell pure-power kernel is not selected on the raw
scalar algebra if Definition 31.KS2 is not imposed. There are infinitely many
pivot-normalized, rotationally invariant spectral functions with the same
principal exponent:

```text
M_N = x^(-1/2) s_N^(-1/4) h(s_N),
```

where `h(1)=1` and `h(s)=1+o(1)` at large `s`, but `h` is not identically one.

These dressings preserve the large-`k` exponent while changing finite-shell
behavior.

Status: `DERIVED/NO-GO` for an unscoped universal finite-shell selection claim.

Chain:

```text
Corollary 31.KS7
  <- standard spectral functional calculus on the positive scalar shell
     operator L=-Delta_S3-3
  <- existence of nontrivial smooth pivot-normalized functions h(s)
  <- P1 supplies the compact S^3 scalar shell operator.
```

## Recommended Manuscript Boundary

Recommended replacement for the §13.6 status paragraph:

```text
Status: DERIVED/CONDITIONAL_VERIFIED on the scalar Born/Weyl typed readout
quotient. The large-k exponent follows from the observable-class gap
alpha_delta-alpha_Phi=-1/2 and the S^3 scalar shell dictionary. The exact
finite-shell pure-power multiplier follows if the CMB Weyl kernel is restricted
to the IO single-character readout class: the kernel carries only the typed
class conversion and no independent finite-shell transfer physics. On the raw
scalar algebra, non-character lower-order spectral dressings remain writable;
they are excluded only from the typed single-character IO readout quotient, not
from mathematics in general.
```

This is stronger than the old `RECONSTRUCTION` label but still honest. The
selection theorem is not universal; it is IO-specific and quotient-scoped.


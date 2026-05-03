# Paper 35 equivariant surface-selector no-go theorem

## Discipline label

- label state: `CLEAN`
- registry check: Vectors 1-4 reviewed. No unresolved load-bearing circularity-vector hit remains on this surface after the present audit.
- chain verification: verified through the cited Paper 35 puncture-symmetry and surface representation chain to assumed-good Papers 1-31 nodes; no surfaced admissions or unresolved local premise steps remain load-bearing on this surface.
- admitted inputs surfaced here: none.
- usage rule: this theorem may be cited as a premise because it is `CLEAN`.
## Headline

- status: `derived / exhausted equivariant surface-selector boundary`
- No nontrivial visible-sector selector exists as a current-stack equivariant observable on the neutral puncture sector. The only surviving positive surface route is an explicitly symmetry-breaking selector B_sel with nonzero q.

## Theorem 1: Equivariant Selector Weights Are Constant

- status: `derived / scoped`
- neutral tuple: `a = (a_1,...,a_n),   sum_i a_i = 0 mod k`
- visible charge: `q_vis(a) = sum_i w_i a_i mod k`
- selector weights: `w_i in {0,1}`
- equivariance: `sigma.w = w   for all sigma in Sym_n`
- conclusion: `w_i = c for all i,   c in {0,1}`
- Represent a candidate visible-sector selector on an n-puncture neutral tuple by slot weights w_i in {0,1}, so q_vis(a) = sum_i w_i a_i mod k. If the selector is equivariant under the full puncture permutation action, then sigma.w = w for every sigma in Sym_n. Hence all w_i are equal. Idempotence then forces only the trivial choices w = 0 or w = (1,...,1).

## Theorem 2: Nontrivial Equivariant Visible Charge Is Impossible

- status: `derived / strongest current-stack surface no-go`
- equivariant weights: `w = c(1,...,1),   c in {0,1}`
- visible charge reduction: `q_vis(a) = c sum_i a_i = 0 mod k`
- current stack selector: `no nontrivial equivariant selector exists`
- For the only equivariant idempotent weights w = c(1,...,1), the induced visible charge is q_vis(a) = c sum_i a_i = 0 mod k on every physical neutral tuple. Therefore no nontrivial visible/compensator split with q != 0 can be realized by a current-stack equivariant selector.

## Theorem 3: Exact Future Surface Object

- status: `derived / sharpened future surface target`
- future exact object: `(B_sel, q),   q in Z_k \ {0}`
- symmetry breaking: `[B_sel, Sym_n] != 0`
- current value: `B_sel,current = none,   q_current = 0`
- previous boundary import: `The future compensator route is now reduced from a geometric marked defect to one exact physical-surface datum: a sector selector P_vis together with a nonzero charge q in Z_k. On the current stack that selector is absent.`
- The remaining positive surface route is not an arbitrary projector P_vis. It is a symmetry-breaking selector B_sel together with a nonzero charge q in Z_k. Any positive future theorem must therefore add a genuine symmetry-breaking surface datum or state; it cannot arise from the current tracial puncture-symmetric sector alone.


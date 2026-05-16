Paper 26 C2 Channel-Separation Audit
====================================

Question
--------

Can the apparent tension

    background temperature uses radial / Carlip-Virasoro counting
    while perturbation amplitude uses angular / S^2 mode counting

be resolved by saying that the two observables pass through different framework
channels?


Short answer
------------

`derived`: yes, the stack already distinguishes the two observable channels.

`derived`: the scalar perturbation bridge is a spatial/coexact covariance
channel:

    C^(0) = B G^(1) B^dagger.

`derived`: the Paper 2 temperature derivation is a Carlip-Cardy thermodynamic
channel built from the horizon algebra and radial/timelike mode counting. It
does not use the later Paper 23 scalar bridge operator `B`.

`conditional`: this does **not** yet prove that the perturbation source is
literally the `S^2` angular Hawking spectrum. Papers 22-23 prove the `S^3`
coexact bridge carrier; the `S^2 -> S^3` lowest-shell coexact lift is a later
Paper 26 reduced construction.

So the strongest honest conclusion is:

    different observable classes can legitimately use different counting
    channels,

but the full "background = radial, perturbations = S^2 angular" slogan is only
partly theorem-grade at present.


I. What the bridge side actually proves
---------------------------------------

Paper 22 closes the spatial one-particle carrier:

    the Ashtekar-Barbero background lies in the lowest coexact 1-form channel
    on S^3.

See:

    /opt/cosmology-lab/results/paper22/paper22_spatial_hodge_complex_report.txt

Paper 23 then closes the scalar bridge grammar:

    H_(1) = direct-sum W_n^(sigma),
    H_(0,phys) = direct-sum H_N^(0),
    B : H_(1) -> H_(0,phys),
    C^(0) = B G^(1) B^dagger.

See:

    /opt/cosmology-lab/results/paper23/paper23_state_covariance_resolution_report.txt
    /opt/cosmology-lab/results/paper23/paper23_bridge_uniqueness_report.txt

At the raw bridge level, the scalar bridge is a unique one-slot map built from
the homogeneous background connection in the lowest coexact vector channel.

Therefore:

- `derived`: perturbation statistics in Paper 23 live on the bridge covariance
  channel.
- `derived`: that channel is spatial/coexact, not a thermodynamic/Cardy scalar.


II. What the bridge side does NOT yet prove
-------------------------------------------

Papers 22-23 by themselves prove the coexact bridge carrier on `S^3`, not a
full theorem that the physical boundary source is already an `S^2` coexact mode
with Hawking angular occupation.

The later Paper 26 reduced lift audit proves only the lowest-shell carrier map

    U_coex : Omega^1_coex(S^2, ell=1) -> h_br subset Omega^1_coex(S^3, n=1)

as an `SU(2)`-equivariant reduced lift.

See:

    /opt/cosmology-lab/results/paper26/paper26_carrier_lift_Ucoex_audit.md

So:

- `derived`: perturbations use the spatial/coexact bridge carrier.
- `conditional`: translating that into literal `S^2` angular Hawking counting
  still needs the source-side carrier identification.


III. What the temperature side actually proves
----------------------------------------------

The original Paper 2 source states that the temperature boost is derived from
Carlip-Virasoro dimensional reduction:

    c_3D = 6 r_s^2 / l_P^2,
    c_1D = 6 r_s / l_P,
    T_IO / T_H = sqrt(c_3D / c_1D).

The same text explicitly says the interior observer counts modes along the
timelike/radial direction.

This is visible directly in:

    /opt/cosmology-lab/results/Full Papers/Interior_Observer_Paper2_v1_6.docx

The Paper 2 derivation chain is a thermodynamic/Cardy one:

    horizon algebra
      -> central charges
      -> Cardy temperature ratio
      -> T_IO.

It does mention a "holographic thermalization bridge" connecting 1+1D horizon
states to the 3+1D interior photon bath, but that is a background
thermodynamic-consistency construction, not the later Paper 23 scalar
perturbation bridge operator

    B : H_(1) -> H_(0,phys).

Therefore:

- `derived`: the Paper 2 background temperature does not pass through the Paper
  23 bridge operator.
- `derived`: its native channel is Carlip/Cardy thermodynamics, not bridge
  covariance.


IV. Existing stack support for distinct channels
------------------------------------------------

The later stack already supports the idea that different observables can live
on different channels.

1. Paper 16 open-transport audit:

   tangential horizon data and radial/interior transfer are distinct objects;
   no automatic identification exists.

   See:

       /opt/cosmology-lab/results/paper16/paper16_open_transport_audit_report.txt

2. Paper 16 transport-consistency audit:

   no universal preserved transport law can drag one horizon factor across all
   observables without breaking already-validated sectors.

   See:

       /opt/cosmology-lab/results/paper16/paper16_transport_consistency_audit_report.txt

3. Paper 21 / later Paper 26 visibility audit:

   local bulk thermodynamic observables and optical/readout observables are
   already distinct observable classes.

   See:

       /opt/cosmology-lab/results/paper26/paper26_visibility_class_promotion_attempt.md

So nothing in Papers 1-25 forces one universal counting channel for every
observable.


V. Strongest clean statement
----------------------------

Lemma C2.1 (background/perturbation channel separation)

Within the current stack:

1. background temperature belongs to the Carlip-Cardy thermodynamic channel and
   is derived from radial/timelike mode counting on the horizon algebra;
2. scalar perturbation statistics belong to the Paper 23 bridge covariance
   channel

       C^(0) = B G^(1) B^dagger,

   whose one-particle source carrier is the spatial/coexact vector sector.

Hence the framework does not require the same mode-counting channel for the two
observables.


Proof
-----

Item 1 is the direct Paper 2 derivation chain described in Section III.

Item 2 is the Paper 22-23 bridge infrastructure described in Section I.

The two constructions use different carriers, different operators, and
different observable grammars:

    thermodynamic/Cardy scalar
    versus
    bridge-pushed covariance.

Therefore a single universal counting rule does not follow.

QED.


VI. Does this resolve the hostile-referee objection?
----------------------------------------------------

Partly.

It resolves the strong version of the objection:

    "the framework must use one and the same counting channel for all
     observables."

That statement is false on the current stack.

But it does **not** yet resolve the strongest source-side version:

    "Paper 26 has already proved that perturbations specifically inherit
     S^2 angular Hawking counting while the background specifically inherits
     radial Carlip-Virasoro counting."

That stronger statement is still only:

- `derived` on the background side,
- `conditional` on the perturbation source side.

The exact remaining bottleneck is:

    certify the physical boundary perturbation source as the S^2 coexact angular
    carrier feeding the Paper 23 bridge.


VII. Honest verdict
-------------------

- `derived`: background thermodynamics and perturbation covariance already live
  on different observable channels.
- `derived`: nothing in Papers 1-25 contradicts that separation.
- `conditional`: the specific slogan

      background = radial/Carlip-Virasoro,
      perturbations = S^2 angular/bridge

  is not yet fully theorem-grade because the perturbation source-side `S^2`
  carrier identification still rests on the later reduced lift / Hawking
  branch.

What future AI must not say without new proof:

- "Papers 22-23 already prove the scalar bridge reads S^2 coexact modes"
- "Paper 2 and Paper 23 use one common bridge object"
- "the full C2 separation is completely closed"

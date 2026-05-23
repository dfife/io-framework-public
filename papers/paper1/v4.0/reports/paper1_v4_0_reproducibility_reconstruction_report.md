# Paper 1 v4.0 Reproducibility Reconstruction Report

Date: 2026-05-23

## Scope

No complete saved Paper 1 v4.0 script set was found in the lab workspace or the
public bundle tree. This bundle therefore reconstructs the local Paper 1
arithmetic directly from the v4.0 manuscript and current public IO bundle
conventions.

The reconstructed scripts cover:

- Schwarzschild radius and line-scale constants from `M_U`, `R_U`, and CODATA
  constants.
- The local Hawking-temperature chain, including the geometric boost factor and
  Planck-temperature identity.
- The scoped interior greybody theorem flag `Gamma(omega)=1`.
- The torsion/effective dark-energy formula as written in the manuscript.
- Cross-paper source pointers for inherited Paper 17, Paper 32, Paper 34, and
  Paper 35 claims.

## Validation Result

The bundle validator reports:

```text
SUMMARY total_checks=24 pass_count=24 fail_count=0
```

## Manuscript Synchronization Findings

### Dark-Energy Density

Using the Paper 1 v4.0 stated constants

```text
M_U = 4.50e53 kg
R_U = 4.40e26 m
gamma_BI = 0.2375
```

the formula

```text
rho_Lambda,torsion = 9*pi*c^2/[32*G*r_s^2*(1+gamma_BI^2)]
rho_Lambda,eff = rho_Lambda,torsion*(r_s/R_U)^2
```

gives

```text
rho_Lambda,torsion = 2.5213519352125205e-27 kg/m^3
rho_Lambda,eff     = 5.817572055422853e-27 kg/m^3
```

The manuscript quotes legacy values

```text
rho_Lambda,torsion = 2.62e-27 kg/m^3
rho_Lambda,eff     = 6.05e-27 kg/m^3
```

The bundle does not force the legacy values. It records the mismatch as an
explicit audit flag.

### Paper 32 v2.0 SHA Prefix

The Paper 1 v4.0 manuscript states that inherited recollapse/cycle values are
from `paper32-v2.0` at SHA prefix `fadeea1d`. The current public repository
manifest records `2e1ff99e182c27234575c8a1687281bea86e9d05a84eeed4b27cd5930322d70b`
for `paper32-v2.0`.

The bundle records this as a synchronization flag. The inherited numerical
values are treated as source-bound Paper 32 support, not rederived locally in
Paper 1.

## Claim Boundary

This bundle is `VERIFIED` for the local arithmetic it recomputes. It does not
upgrade inherited Paper 17, Paper 32, Paper 34, or Paper 35 claims beyond their
own published bundle labels.


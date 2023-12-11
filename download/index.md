---
title: Download
subtitle: FEniCSx fenicsxversion
permalink: /download/
---

## Getting started

The latest stable release of FEniCSx is version {{ site.fenicsxversion }},
which was released in {{ site.fenicsxversiondate }}. The easiest way to start using FEniCSx is to install it using conda:

```bash
conda install fenics-dolfinx
```

## Other installation options

The source code of all the components of FEniCSx can be found [on GitHub](https://github.com/FEniCS/):

- [<i class="fa-brands fa-github"></i> UFL](https://github.com/FEniCS/ufl)
- [<i class="fa-brands fa-github"></i> Basix](https://github.com/FEniCS/basix)
- [<i class="fa-brands fa-github"></i> FFCx](https://github.com/FEniCS/ffcx)
- [<i class="fa-brands fa-github"></i> DOLFINx](https://github.com/FEniCS/dolfinx)

Detailed instructions for installing FEniCSx from source, or using some binary distributions can be found
[in the installation page of the DOLFINx docs](https://github.com/FEniCS/dolfinx#installation).

## FEniCSx vs legacy FEniCS

FEniCSx is the latest iteration of FEniCS, and boasts a number of 
major improvements over the legacy library,
including support for a wide range of cell types and elements, memory
parallelisation, and complex number support. FEniCSx is comprised of
the libraries UFL, Basix, FFCx and DOLFINx. The latest version of
FEniCSx ({{ site.fenicsxversion }}) was released in
{{ site.fenicsxversiondate }}.
We recommend that new users use the latest release of FEniCSx.


Updates are now very rarely made to the legacy FEniCS library. We recommend that users consider
using FEniCSx instead of the legacy library. Lecacy FEniCS is comprised
of the libraries UFL legacy, FIAT, FFC and DOLFIN. The latest version of legacy
FEniCS ({{ site.fenicsversion }}) was released in
{{ site.fenicsversiondate }}.
Instructions for installing the legacy FEniCS (version {{
site.fenicsversion }}) can be found [here](archive.md).

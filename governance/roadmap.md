---
title: Roadmap 2021-
permalink: roadmap
---

## Introduction
The FEniCS core libraries have undergone a major redevelopment to bring new functionality, improved performance and better underpinning software engineering. The FEniCS Project is now approximately 20 years old, and over that time our understanding has developed and the available tools have changed significantly. The latest developments of FEniCS follow these principles:

- Compact, modular core designed to be extensible and to support custom additions
- Reduced public interface that could be kept more stable
- Proper namespacing
- Use of established standards and conventions wherever possible (design, packaging, testing, etc)
- Properly separated C++ and Python interfaces
- Simplified software engineering
- Distributed memory parallel design throughout
- Improved documentation
- Faster just-in-time compilation
- Support for modern Python JIT tools, e.g. [numba](http://numba.pydata.org/)
- Simple implementation of fast user 'kernels' from Python
- Just one way to perform an operation wherever possible

## New core functionality
### Short-term
- Support for ADIOS2 I/O
- Implemention of PointSource
- Support wider range of FE types (e.g. serendipity)
- FunctionSpaces on facets

### Longer-term
- Heterogenous compute platforms
- Mixed geometry meshes (e.g. quads/triangles hex/prism/pyramid/tet)

## Development
Development is taking place on [GitHub](https://github.com/FEniCS) under the
[DOLFINx](https://github.com/FEniCS/dolfinx), [Basix](https://github.com/FEniCS/basix),
[UFL](https://github.com/FEniCS/ufl) and [FFCx](https://github.com/FEniCS/ffcx) repositories. The 
first "alpha" releases of DOLFINx, Basix and FFCx are now available, although some features 
are still awaiting reimplementation. The DOLFIN, FFC, FIAT and dijitso projects are now 
considered legacy.

## Releases

We have published an "alpha" release of FEniCSx (DOLFINx, FFCx, Basix, UFL) as
{{ site.fenicsxversion }} in {{ site.fenicsxversiondate }}. The legacy FEniCS Project
(DOLFIN, FFC, FIAT, UFL), is still available with release number {{ site.fenicsversion }}.

# Future of previous FEniCS packages

We know that a number of users and developers are wondering about the future of the FEniCS packages. 

Going forward, we:

- encourage all developers to engage with the FEniCSx development;
- encourage users and developers to discuss potential features/bug fixes on the FEniCS Slack Channel before making a pull request to FEniCS 2019.1.0 packages.
- will accept occasional high quality pull requests and bug fixes into the FEniCS 2019.1.0 components


---
title: The FEniCS Tutorial
permalink: tutorial
---

![The FEniCS tutorial](/assets/img/docs/tutorial.png){: .image-right }
The FEniCS Tutorial is the perfect guide for new users. The tutorial explains the fundamental 
concepts of the finite element method, FEniCS programming, and demonstrates how to quickly 
solve a range of PDEs. The tutorial assumes no prior knowledge of the finite element method. 
The tutorial is an updated and expanded version of the popular first chapter of the
[FEniCS Book](book.md).

The FEniCS Tutorial was first published in 2017 with Springer.

## Accessing the tutorial
The book [Solving PDEs in Python – The FEniCS Tutorial I](http://www.springer.com/gp/book/9783319524610)
is published as part of the series [Simula Springer Briefs on Computing](http://www.springer.com/series/13548).
The book is open access and the eBook can be downloaded for free from Springer. The book can also
be accessed directly from this page, both as a PDF file and in HTML. Pick your Poisson and follow
one of the links below.

- [Springer eBook](http://www.springer.com/gp/book/9783319524610) (**free**)
- [Springer print](http://www.springer.com/gp/book/9783319524610) (softcover)

## Comments and corrections
Comments and corrections can be reported as [issues for the Git repository of the book](https://github.com/hplgit/fenics-tutorial/issues)
or via email to [logg@chalmers.se](mailto:logg@chalmers.se). Note that fixes will be incorporated
directly into the PDF and HTML versions of the book accessible above, but will take a longer time
to propagate to the Springer print and eBook versions.

## Example programs
All example programs from the tutorial can be accessed directly from the
[Git repository of the book](https://github.com/hplgit/fenics-tutorial)
or by following the links below.

- [ft01_poisson.py](https://github.com/hplgit/fenics-tutorial/blob/master/pub/python/vol1/ft01_poisson.py)
- [ft02_poisson_membrane.py](https://github.com/hplgit/fenics-tutorial/blob/master/pub/python/vol1/ft02_poisson_membrane.py)
- [ft03_heat.py](https://github.com/hplgit/fenics-tutorial/blob/master/pub/python/vol1/ft03_heat.py)
- [ft04_heat_gaussian.py](https://github.com/hplgit/fenics-tutorial/blob/master/pub/python/vol1/ft04_heat_gaussian.py)
- [ft05_poisson_nonlinear.py](https://github.com/hplgit/fenics-tutorial/blob/master/pub/python/vol1/ft04_heat_gaussian.py)
- [ft06_elasticity.py](https://github.com/hplgit/fenics-tutorial/blob/master/pub/python/vol1/ft06_elasticity.py)
- [ft07_navier_stokes_channel.py](https://github.com/hplgit/fenics-tutorial/blob/master/pub/python/vol1/ft07_navier_stokes_channel.py)
- [ft08_navier_stokes_cylinder.py](https://github.com/hplgit/fenics-tutorial/blob/master/pub/python/vol1/ft08_navier_stokes_cylinder.py)
- [ft09_reaction_system.py](https://github.com/hplgit/fenics-tutorial/blob/master/pub/python/vol1/ft09_reaction_system.py)
- [ft10_poisson_extended.py](https://github.com/hplgit/fenics-tutorial/blob/master/pub/python/vol1/ft10_poisson_extended.py)
- [ft11_magnetostatics.py](https://github.com/hplgit/fenics-tutorial/blob/master/pub/python/vol1/ft11_magnetostatics.py)
- [ft12_poisson_solver.py](https://github.com/hplgit/fenics-tutorial/blob/master/pub/python/vol1/ft12_poisson_solver.py)
- [boxfield.py](https://github.com/hplgit/fenics-tutorial/blob/master/src/vol1/python/boxfield.py)

**Note**: To run [ft09_reaction_system.py](https://github.com/hplgit/fenics-tutorial/blob/master/pub/python/vol1/ft09_reaction_system.py),
you must first run [ft08_navier_stokes_cylinder.py](https://github.com/hplgit/fenics-tutorial/blob/master/pub/python/vol1/ft08_navier_stokes_cylinder.py)
to generate the geometry and flow field data for the reaction system.

## How to cite
If you use the FEniCS tutorial in your research, please use the following citation data:

```bibtex
@book{LangtangenLogg2017,
  title = {Solving PDEs in Python},
  author = {Hans Petter Langtangen and Anders Logg},
  year = {2017},
  publisher = {Springer},
  doi = {10.1007/978-3-319-52462-7},
  isbn = {978-3-319-52461-0},
}
```

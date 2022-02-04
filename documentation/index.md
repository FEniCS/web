---
title: FEniCS Documentation
subtitle: fenicsversion
permalink: /documentation/
---

The FEniCSx documentation includes a set of books, collections of documented demo programs and reference manuals.

## The FEniCSx Tutorial
![The FEniCSx tutorial](/assets/img/docs/tutorial.png){: .image-right }
If you are new to FEniCS and want to quickly get started with solving PDEs in Python,
the [FEniCSx tutorial](https://jorgensd.github.io/dolfinx-tutorial/) is a good place to start.
The tutorial explains the fundamental concepts of the finite element method, FEniCSx programming, and
demonstrates how to quickly solve a range of PDEs.
The FEniCSx Tutorial based on the [FEniCS Tutorial](tutorial.md) book which was published as part of the series
[Simula Springer Briefs on Computing](http://www.springer.com/series/13548).

## API Documentation
FEniCSx is comprised of four main components:

- UFL ([latest docs](https://fenics.readthedocs.io/projects/ufl/en/latest/)) (the Unified Form Language) is a form language
  that allows the user to write a wide variety of finite element forms in Python.
- Basix ([latest docs](https://docs.fenicsproject.org/basix/main/)) is a element definition and tabulation library
  that provides all the information FEniCSx needs about elements on the reference cell.
- FFCx ([latest docs](https://docs.fenicsproject.org/ffcx/main)) (the FEniCSx Form Compiler) is the Python library that interprets
  UFL forms and generates C code to assemble these on cells.
- DOLFINx ([latest C++ docs](https://docs.fenicsproject.org/dolfinx/main/cpp/), [latest Python docs](https://docs.fenicsproject.org/dolfinx/main/python/))
  is the main user interface of FEniCSx, and handles meshes and linear algebra solvers among other things.

API documentation of the latest version of each component can be found using the links above. Documentation of
other versions can be found at [docs.fenicsproject.org](https://docs.fenicsproject.org/).

# The FEniCS book
![The FEniCS book](/assets/img/docs/book.png){: .image-right }
The book [Automated Solution of Differential Equations by the Finite Element Method](book.md)
explains the theoretical background and design of FEniCS. It describes the FEniCS software
components in detail and showcases a number of applications of FEniCS to problems in fluid
mechanics, solid mechanics, electromagnetics, and geophysics. The book was published in 2012,
and was based on the legacy FEniCS library, so the code examples in the book are out of date.
However, the book still gives a good description of the many of the design principles that
FEniCSx is based on.

The book is available as a [free ebook](http://launchpad.net/fenics-book/trunk/final/+download/fenics-book-2011-10-27-final.pdf),
or can be bought from [Springer](http://www.springer.com/mathematics/computational+science+%26+engineering/book/978-3-642-23098-1)
or many other bookshops.

## Legacy FEniCS
Documnetation for the legacy version of FEniCS (version {{ site.fenicsversion }}) can be found [here](archive.md).

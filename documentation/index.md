---
title: FEniCS Documentation
subtitle: fenicsversion
---

The FEniCS documentation includes a set of books, collections of documented demo programs and reference manuals.

## The FEniCS Tutorial
![The FEniCS tutorial]({{ site.webroot }}assets/img/docs/tutorial.png){: .image-right }
If you are new to FEniCS and want to quickly get started with solving PDEs in Python,
the [FEniCS Tutorial]({{ site.webroot }}documentation/tutorial) is a good starting point. The tutorial 
explains the fundamental concepts of the finite element method, FEniCS programming, and 
demonstrates how to quickly solve a range of PDEs. The tutorial assumes no prior knowledge of 
the finite element method. The FEniCS Tutorial is published as part of the series
[Simula Springer Briefs on Computing](http://www.springer.com/series/13548).
The book is open access and the eBook can be downloaded for free 
from Springer.

Note that some of the FEniCS Tutorial example code may be obsolete, see the
[FEniCS Tutorial page]({{ site.webroot }}documentation/tutorial)
for how to report comments and corrections.

## The FEniCS API Documentation
The FEniCS Project consists of a number of components with DOLFIN and UFL providing the main 
user interface. For detailed documentation of the FEniCS programming interface, use the

- [DOLFIN (C++) API](https://fenicsproject.org/olddocs/dolfin/latest/cpp/classes.html) Class Index
- [DOLFIN (Python) API](https://fenicsproject.org/olddocs/dolfin/latest/python/) reference

Not the version you are looking for? See also the list of
[documentation for other DOLFIN versions](https://fenicsproject.org/olddocs/dolfin/).
Some advanced user and more developer-oriented information can also be found in the 
[FEniCS Reference Manual on Read the docs](https://fenics.readthedocs.io/en/latest/).

The [DOLFIN ChangeLog](https://fenics.readthedocs.io/projects/dolfin/en/latest/ChangeLog.html)
provides an overview of changes in the FEniCS programming interfaces between different versions.

## The FEniCS Demos
The FEniCS demo programs (demos) are a good starting point for building your own FEniCS 
applications, and many users find these useful. The demos are included in the
[FEniCS source repositories](https://bitbucket.org/fenics-project/),
which are hosted on Bitbucket. For easy reference, we here provide quick links 
to the demos:

- [DOLFIN C++ demos](https://bitbucket.org/fenics-project/dolfin/src/master/demo/) (development version)
- [DOLFIN Python demos](https://bitbucket.org/fenics-project/dolfin/src/master/python/demo/) (development version)

# The FEniCS book
![The FEniCS book]({{ site.webroot }}assets/img/docs/book.png){: .image-right }

The book [Automated Solution of Differential Equations by the Finite Element Method]({{ site.webroot }}documentation/book.md)
explains the theoretical background and design of FEniCS. It describes the FEniCS software
components in detail and showcases a number of applications of FEniCS to problems in fluid
mechanics, solid mechanics, electromagnetics, and geophysics. The book was published in 2012,
which means that some of the examples presented in the book may use old interfaces that are no
longer supported by FEniCS. However, the book still gives a good description of the design of
FEniCS.

## The FEniCS Notebooks
The FEniCS Notebooks are a collection of documented Jupyter/Python notebooks illustrating 
various features of FEniCS and the application of FEniCS to a range of PDEs. The FEniCS 
Notebooks are currently in preparation.

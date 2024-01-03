---
title: Citing FEniCS
subtitle: Legacy FEniCS
permalink: /citing/legacy/
---

## Legacy citations

This page lists citations for legacy FEniCS and should be used if your code starts with `import dolfin`.
If your code starts with `import dolfinx`, then you can find the list of relevant ciations for FEniCSx on
[the main citations page](index.md).

If you use FEniCS in your research, the developers would be grateful if you would cite the
relevant publications. FEniCS is organized as a collection of components, so to give proper
credit to the developers of FEniCS, please cite the indicated references **for each relevant
component**. You can find this list of papers in BibTeX format [here](/assets/citations.bib).

### Main FEniCS citations

{% include _paper.html
  bibtype="article"
  id="AlnaesEtal2015"
  title="The FEniCS Project Version 1.5"
  author="M. S. Alnaes, J. Blechta, J. Hake, A. Johansson, B. Kehlet, A. Logg, C. Richardson, J. Ring, M. E. Rognes and G. N. Wells"
  journal="Archive of Numerical Software"
  volume="3"
  year="2015"
  doi="10.11588/ans.2015.100.20553"
%}

{% include _paper.html
  bibtype="book"
  id="LoggEtal2012"
  title="Automated Solution of Differential Equations by the Finite Element Method"
  author="A. Logg, K.-A. Mardal, G. N. Wells et al"
  bookpublisher="Springer"
  year="2012"
  doi="10.1007/978-3-642-23099-8"
%}

### DOLFIN
{% include _paper.html
  bibtype="article"
  id="LoggWells2010"
  title="DOLFIN: Automated Finite Element Computing"
  author="A. Logg and G. N. Wells"
  journal="ACM Transactions on Mathematical Software"
  volume="37"
  year="2010"
  doi="10.1145/1731022.1731030"
  arxiv="1103.6248"
%}

{% include _paper.html
  bibtype="incollection"
  id="LoggEtal_10_2012"
  title="DOLFIN: a C++/Python Finite Element Library"
  author="A. Logg, G. N. Wells and J. Hake"
  book="Automated Solution of Differential Equations by the Finite Element Method"
  bookvolume="84"
  bookseries="Lecture Notes in Computational Science and Engineering"
  bookeditor="A. Logg, K.-A. Mardal and G. N. Wells"
  bookpublisher="Springer"
  bookchapter="10"
  year="2012"
%}

### FFC
{% include _paper.html
  bibtype="article"
  id="KirbyLogg2006"
  title="A Compiler for Variational Forms"
  author="R. C. Kirby and A. Logg"
  journal="ACM Transactions on Mathematical Software"
  volume="32"
  year="2006"
  doi="10.1145/1163641.1163644"
  arxiv="1112.0402"
%}

{% include _paper.html
  bibtype="incollection"
  id="LoggEtal_11_2012"
  title="FFC: the FEniCS Form Compiler"
  author="A. Logg, K. B. Ølgaard, M. E. Rognes and G. N. Wells"
  book="Automated Solution of Differential Equations by the Finite Element Method"
  bookvolume="84"
  bookseries="Lecture Notes in Computational Science and Engineering"
  bookeditor="A. Logg, K.-A. Mardal and G. N. Wells"
  bookpublisher="Springer"
  bookchapter="11"
  year="2012"
%}

{% include _paper.html
  bibtype="article"
  id="OlgaardWells2010"
  title="Optimisations for Quadrature Representations of Finite Element Tensors Through Automated Code Generation"
  author="K. B. Ølgaard and G. N. Wells"
  journal="ACM Transactions on Mathematical Software"
  volume="37"
  year="2010"
  doi="10.1145/1644001.1644009"
  arxiv="1104.0199"
%}

### FIAT
{% include _paper.html
  bibtype="article"
  id="Kirby2004"
  title="Algorithm 839: FIAT, a New Paradigm for Computing Finite Element Basis Functions"
  author="R. C. Kirby"
  journal="ACM Transactions on Mathematical Software"
  volume="30"
  pagestart="502" pageend="516"
  year="2004"
  doi="10.1145/1039813.1039820"
%}

{% include _paper.html
  bibtype="incollection"
  id="kirby2010"
  title="FIAT: Numerical Construction of Finite Element Basis Functions"
  author="R. C. Kirby"
  book="Automated Solution of Differential Equations by the Finite Element Method"
  bookvolume="84"
  bookseries="Lecture Notes in Computational Science and Engineering"
  bookeditor="A. Logg, K.-A. Mardal and G. N. Wells"
  bookpublisher="Springer"
  bookchapter="13"
  year="2012"
%}

### UFL
{% include _paper.html
  bibtype="article"
  id="AlnaesEtal2014"
  title="Unified Form Language: A domain-specific language for weak formulations of partial differential equations"
  author="M. S. Alnaes, A. Logg, K. B. Ølgaard, M. E. Rognes and G. N. Wells"
  journal="ACM Transactions on Mathematical Software"
  volume="40"
  year="2014"
  doi="10.1145/2566630"
  arxiv="1211.4047"
%}

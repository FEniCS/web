---
title: Citing FEniCS
permalink: /citing/
---
If you use FEniCS in your research, the developers would be grateful if you would cite the
relevant publications. FEniCS is organized as a collection of components, so to give proper
credit to the developers of FEniCS, please cite the indicated references **for each relevant
component**.

You can find this list of papers in BibTeX format [here](/assets/citations.bib).

To see a variety of applications of FEniCS, you can take a look at [this list of recent papers that cite FEniCS](https://scholar.google.com/scholar?hl=en&as_sdt=2005&sciodt=0,5&cites=2599384670914385341,17770978774251756625,11448541870608622893,543273511654441124,14605055523284224439,12866126847560384055,14201058291201976279,3289611746284990832,3651475191867995052,10591416677298451301,6832515800031607486&scipsc=&q=&scisbd=1).

## FEniCSx
If your code starts with `import dolfinx`, you should cite these papers.

### Basix

{% include _paper.html
  bibtype="article"
  id="ScroggsEtal2022"
  title="Construction of arbitrary order finite element degree-of-freedom maps on polygonal and polyhedral cell meshes"
  author="M. W. Scroggs, J. S. Dokken, C. N. Richardson, and G. N. Wells"
  journal="ACM Transactions on Mathematical Software"
  year="2022"
  doi="10.1145/3524456"
  arxiv="2102.11901"
  volume="48"
  number="2"
  pagestart="18:1"
  pageend="18:23"
%}

{% include _paper.html
  bibtype="article"
  id="BasixJoss"
  title="Basix: a runtime finite element basis evaluation library"
  author="M. W. Scroggs, I. A. Baratta, C. N. Richardson, and G. N. Wells"
  journal="Journal of Open Source Software"
  year="2022"
  doi="10.21105/joss.03982"
  volume="7"
  number="73"
  pagestart="3982"
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


## Legacy FEniCS
If your code starts with `import dolfin`, you should cite these papers.

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

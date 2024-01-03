---
title: Citing FEniCS
permalink: /citing/
---
## Main FEniCSx citations
If you use FEniCS in your research, the developers would be grateful if you would cite the
relevant publications.

If your code starts with `import dolfinx`, you are using FEniCSx and should cite the paper on this page.
FEniCSx is organized as a collection of components, so to give proper
credit, please cite the indicated references **for each relevant
component**. You can find this list of papers in BibTeX format [here](/assets/citations.bib).

### DOLFINx

{% include _paper.html
  bibtype="article"
  id="BarattaEtal2023"
  title="DOLFINx: The next generation FEniCS problem solving environment"
  author="I. A. Baratta, J. P. Dean, J. S. Dokken, M. Habera, J. S. Hale, C. N. Richardson, M. E. Rognes, M. W. Scroggs, N. Sime, and G. N. Wells"
  journal="preprint"
  year="2023"
  doi="10.5281/zenodo.10447666"
%}

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

## Papers that use FEniCS
To see a variety of applications of FEniCS, you can take a look at [this list of recent papers that cite FEniCS](https://scholar.google.com/scholar?hl=en&as_sdt=2005&sciodt=0,5&cites=2599384670914385341,17770978774251756625,11448541870608622893,543273511654441124,14605055523284224439,12866126847560384055,14201058291201976279,3289611746284990832,3651475191867995052,10591416677298451301,6832515800031607486&scipsc=&q=&scisbd=1).


## Legacy FEniCS
If you are using legacy FEniCS and your code starts with `import dolfin`,
you can find a list of relevant citations [on the legacy citations page](legacy.md).

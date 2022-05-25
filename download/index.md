---
title: Download
permalink: /download/
---

# Getting started

The latest stable release of FEniCSx is version {{ site.fenicsxversion
}}, which was released in {{ site.fenicsxversiondate }}.


## Installation

FEniCSx can be [built from source
manually](https://docs.fenicsproject.org/dolfinx/main/python/installation.html#source)
or using [Spack](https://github.com/FEniCS/dolfinx#spack).

Binary distributions are are
[available](https://docs.fenicsproject.org/dolfinx/main/python/installation.html)
as Debian/Ubuntu packages and in Docker images.


## Running FEniCSx with JupyterLab using Docker

An easy way to get started with FEniCSx in JupyterLab is with Docker.
This image can be downloaded by running:

```bash
docker pull dolfinx/lab
```

The image can then be started by running:

```bash
docker run -p 8888:8888 dolfinx/lab
```

A URL will then be output in the terminal that leads to the Jupyter lab.
From there, Jupyter notebooks and Python scripts can be created and run.


## Legacy FEniCS

Instructions for installing the legacy version of FEniCS (version {{
site.fenicsversion }}) can be found [here](archive.md).

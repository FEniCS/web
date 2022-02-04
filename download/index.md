---
title: Download
permalink: /download/
---

The latest stable release of FEniCSx is version {{ site.fenicsxversion }}, which was released
in {{ site.fenicsxversiondate }}.

## Running a Jupyter lab using Docker
The easiest way to start using FEniCSx is to run the Jupyter lab Docker image. This image contains
the latest version of FEniCSx and is automatically updated nightly. It can be used to run FEniCSx
without having to install it on your local system.

This image can be downloaded by running:

```bash
docker pull dolfinx/lab
```

The image can then be started by running:

```bash
docker run -p 8888:8888 dolfinx/lab
```

A URL will then be output in the terminal that leads to the Jupyter lab. From there, Jupyter notebooks and
Python scripts can be created and run.

## Alternative installation methods
Details of alternative installation methods can be found [here](https://docs.fenicsproject.org/dolfinx/main/python/installation.html).

## Legacy FEniCS
Instructions for installing the legacy version of FEniCS (version {{ site.fenicsversion }}) can be found [here](archive.md).

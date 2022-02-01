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

## Developing FEniCSx using the Docker dev-env
If you want to run FEniCSx from a Docker image while developing the source code, you can use the FEniCSx
development environment image. This image contains all the dependencies of the FEniCSx libraries. It can
be downloaded by running:

```bash
docker pull dolfinx/dev-env
```

You can then build your own version of the FEniCSx libraries inside this image. For example, if your copies
of the source code of UFL, Basix, FFCx and DOLFINx are stored in `/home/username/development/`, you can
run the Docker image with these folders shared by running:

```bash
docker run -ti -v /home/username/development/:/mnt/development dolfinx/dev-env
```

Inside the Docker image, your source code folder will be available at `/mnt/development`. You can navigate
to that folder and build the components.

## Legacy FEniCS
Instructions for installing the legacy version of FEniCS (version {{ site.fenicsversion }}) can be found [here](archive.md).

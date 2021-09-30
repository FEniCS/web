---
title: Download
permalink: /download/
---

The latest stable release of FEniCS is version {{ site.fenicsversion }}, which was released
in {{ site.fenicsversiondate }}.

## FEniCS on Docker
To use our prebuilt, high-performance [Docker](https://www.docker.com/community-edition) images,
first install [Docker CE](https://www.docker.com/products/docker-desktop) for your platform
(Windows, Mac or Linux) and then run the following command:

```bash
curl -s https://get.fenicsproject.org | bash
```

To run the FEniCS Docker image, use the command `fenicsproject run`. For more options and
features, see `fenicsproject help`.

Alternatively, you can start a container with the following `docker` command:

```bash
docker run -ti -p 127.0.0.1:8000:8000 -v $(pwd):/home/fenics/shared -w /home/fenics/shared quay.io/fenicsproject/stable:current
```

For detailed instructions, see the [FEniCS Reference Manual](http://fenics-containers.readthedocs.io/en/latest/index.html).

## FEniCS on Windows 10
To install FEniCS on Windows 10, enable the [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
and install the Ubuntu distribution. Then follow the instructions for Ubuntu below.

## Ubuntu FEniCS on Ubuntu
To install FEniCS on Ubuntu, run the following commands:

```bash
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:fenics-packages/fenics
sudo apt-get update
sudo apt-get install fenics
```

For detailed instructions, see the [FEniCS Reference Manual](http://fenics-containers.readthedocs.io/en/latest/index.html).

## FEniCS on Anaconda
To use our prebuilt Anaconda Python packages (Linux and Mac only), first
[install Anaconda](https://docs.continuum.io/anaconda/install), then run following commands in
your terminal:


```bash
conda create -n fenicsproject -c conda-forge fenics
source activate fenicsproject
```

For further information on using Anaconda, see the [documentation](https://docs.continuum.io/anaconda/).

Installing FEniCS via Anaconda is also supported in [Microsoft Azure Notebooks](https://notebooks.azure.com/).
In the first cell of a new Jupyter notebook, type:

```python
!conda config --add channels conda-forge
!conda install fenics
```

**Warning**: FEniCS Anaconda recipes are maintained by the community and distributed binary 
packages do not have a full feature set yet, especially regarding sparse direct solvers and 
input/output facilities.

**Update**. 2017.2.0 release on `conda-forge` features MUMPS direct solver, but lacks SuperLU_dist and MPI-enabled HDF5.

## Building FEniCS from source
For installation in high performance computing clusters we recommend always building from source.
For detailed instructions, see the [FEniCS Reference Manual](http://fenics-containers.readthedocs.io/en/latest/index.html).

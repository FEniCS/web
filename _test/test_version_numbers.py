"""Test FEniCS version numbers."""

import os
import github
import yaml
import datetime


def site_params():
    """Return the params set in hugo.yaml."""
    with open(os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "../hugo.yaml"
    )) as f:
        return yaml.load(f, Loader=yaml.FullLoader)["params"]


def dolfinx_repo():
    """Return the DOLFINx repository, authenticated if a token is set."""
    if "GITHUB_TOKEN" in os.environ:
        git = github.Github(os.environ["GITHUB_TOKEN"])
    else:
        git = github.Github()
    return git.get_repo("fenics/dolfinx")


def test_fenicsx_version_number():
    """Test that the FEniCSx version number is up to date."""
    config = site_params()
    dolfinx = dolfinx_repo()

    latest_tag = dolfinx.get_tags()[0]

    name = latest_tag.name
    p = name.rfind('.')
    name = name[:p]
    if name[0] == "v":
        name = name[1:]

    acceptable_dates = []
    for tag in dolfinx.get_tags():
        if tag.name.startswith(name) or tag.name.startswith("v" + name):
            c = dolfinx.get_commit(tag.commit.sha)

            y, m, _ = c.raw_data["commit"]["author"]["date"].split("-", 2)
            y = int(y)
            m = int(m)
            date = datetime.datetime(year=y, month=m, day=1)
            acceptable_dates.append(date.strftime("%B %Y"))

    assert str(config["fenicsxversion"]) == name
    assert config["fenicsxversiondate"] in acceptable_dates


def test_dolfinx_version_number():
    """Test that the DOLFINx version used in doc links is up to date."""
    config = site_params()

    # dolfinxversion appears in the URL of the DOLFINx documentation, so it
    # has to be a version that was actually released. It carries a .postN
    # suffix that the tags do not, as the docs are built from the Python
    # package version.
    version = str(config["dolfinxversion"]).split(".post")[0]
    tags = [t.name.lstrip("v") for t in dolfinx_repo().get_tags()]
    assert version in tags, f"v{version} is not a DOLFINx tag"

    # It must also be the release that fenicsxversion names.
    assert version.startswith(str(config["fenicsxversion"]))

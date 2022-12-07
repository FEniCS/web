"""Test FEniCS version numbers."""

import os
import github
import yaml
import datetime


def test_fenicsx_version_number():
    """Test that the FEniCSx version number is up to date."""
    with open(os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "../_config.yml"
    )) as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    git = github.Github()

    dolfinx = git.get_repo("fenics/dolfinx")

    latest_tag = dolfinx.get_tags()[0]
    commit = dolfinx.get_commit(latest_tag.commit.sha)

    name = latest_tag.name
    p = name.rfind('.')
    name = name[:p]
    if name[0] == "v":
        name = name[1:]

    acceptable_dates = []
    for tag in dolfinx.get_tags():
        if tag.startswith(name) or tag.startswith("v"+name):
            commit = dolfinx.get_commit(latest_tag.commit.sha)

            year, month, _ = commit.raw_data["commit"]["author"]["date"].split("-", 2)
            year = int(year)
            month = int(month)
            date = datetime.datetime(year=year, month=month, day=1)
            acceptable_dates.append(date.strftime("%B %Y"))

    assert str(config["fenicsxversion"]) == name
    assert config["fenicsxversiondate"] in acceptable_dates

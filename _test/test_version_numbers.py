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

    # FIXME: revert this to [0] once there is not a draft tag
    latest_tag = dolfinx.get_tags()[1]

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

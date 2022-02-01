"Define fixtures and other test helpers."

import pytest


def pytest_addoption(parser):
    parser.addoption("--has-fenicsx", type="int", default=0)


@pytest.fixture
def has_fenicsx(request):
    return request.config.getoption("--has-fenicsx") > 0

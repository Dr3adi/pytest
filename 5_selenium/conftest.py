import pytest
from selenium import webdriver


@pytest.fixture()
def driver(request):
    browser = webdriver.Chrome()
    request.addfinalizer(browser.quit)
    return browser


def pytest_addoption(parser):
    parser.addoption(
        "--brw",
        action="store",
        default="Chrome",
        help="Browser is Chrome"
    )


@pytest.fixture
def brw_param(request):
    return request.config.getoption("--brw")

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser is Chrome"
    )


@pytest.fixture()
def browser(request):
    open_browser = request.config.getoption("--browser")
    if open_browser == 'chrome':
        driver = webdriver.Chrome()
    elif open_browser == 'edge':
        driver = webdriver.Edge()
    else:
        raise ValueError(f'Browser {open_browser} is not supported')
    driver.maximize_window()
    driver.implicitly_wait(20)
    request.addfinalizer(driver.quit)
    return driver


@pytest.fixture(scope='module')
def base_url():
    return 'https://ab.onliner.by'
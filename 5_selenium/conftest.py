import pytest
from selenium import webdriver

@pytest.fixture()
def driver(request):
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    # открытие браузера на весь экран
    browser.maximize_window()
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


@pytest.fixture(params=['chrome', 'edge'])
def parametrize_browser(request):
    browser_param = request.param
    if browser_param == 'chrome':
        driver = webdriver.Chrome()
    elif browser_param == 'edge':
        driver = webdriver.Edge()
    driver.implicitly_wait(20)
    driver.get('https://yandex.by/')
    request.addfinalizer(driver.quit)
    return driver
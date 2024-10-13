import pytest
from selenium import webdriver


@pytest.fixture()
def driver(request):
    browser = webdriver.Chrome()
    request.addfinalizer(browser.quit)
    return browser

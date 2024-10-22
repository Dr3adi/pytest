from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def test_selenium_example(driver):
    driver.get('http://selenium.dev/')
    assert driver.title == 'Selenium'


def test_brw_param(brw_param):
    # pytest.\5_selenium\ --brw=Chrome -v
    if brw_param == 'Chrome':
        browser = webdriver.Chrome()
        browser.get('https://www.google.com/')
        assert browser.title == 'Google'
    # pytest.\5_selenium\ --brw=Edge -v
    elif brw_param == 'Edge':
        # опция запуска браузера без закрытия
        browser_option = webdriver.EdgeOptions()
        browser_option.add_experimental_option("detach", True)
        browser = webdriver.Edge(options=browser_option)
        browser.get('https://yandex.by/')
        assert browser.title == 'Яндекс — быстрый поиск в интернете'
        browser.find_element(By.CLASS_NAME, 'informers3__item-icon').click()


def test_parametrize_browser(parametrize_browser):
    parametrize_browser.find_element(By.CLASS_NAME, 'alice-fab').click()


def test_ya_search():
    ya = webdriver.Edge()
    ya.implicitly_wait(20)
    ya.get('https://yandex.by/')
    ya_search = ya.find_element(By.ID, 'text')
    ya_search.send_keys('test')
    sleep(3)
    ya_search = ya.find_element(By.CLASS_NAME, 'services-suggest__list')
    ya_search.find_element(By.LINK_TEXT, 'Игры').click()
    sleep(3)

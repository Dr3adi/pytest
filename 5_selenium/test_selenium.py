from selenium import webdriver


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

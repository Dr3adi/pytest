from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select


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

    # получение css проперти
    css_property = ya_search.value_of_css_property('color')
    print(css_property)
    css_property = ya_search.value_of_css_property('display')
    print(css_property)
    # ввод текста в строку
    ya_search.send_keys('test')
    sleep(3)
    ya_search = ya.find_element(By.CLASS_NAME, 'services-suggest__list')
    ya_search.find_element(By.LINK_TEXT, 'Игры').click()
    sleep(3)


# работа с селектами
def test_ab_onliner(driver):
    driver.implicitly_wait(20)
    driver.get('https://ab.onliner.by/')
    s1 = Select(driver.find_element(By.XPATH,
                                    '//*[@id="container"]/div/div/div/div/div/div[2]/div/div/div[3]/div/div[2]/div[2]/div[2]/div[5]/div/div/div/div/div[2]/div/div/div[1]/div/select'))
    s1.select_by_index(5)
    sleep(5)

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select


def test_ab_onliner_page(browser, base_url):
    browser.get(base_url + '/bmw')
    element = browser.find_element(By.CLASS_NAME, 'fast-search__input')
    element.send_keys('samsung')
    sleep(5)
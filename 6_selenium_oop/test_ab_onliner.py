from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from utils import clear_input
from selenium.webdriver.support.select import Select
from locators import CatalogPage


def test_ab_onliner_page(browser, base_url):
    browser.get(base_url + '/bmw')
    # Распаковка с помощью * позволяет передать каждый элемент кортежа как отдельный аргумент в метод find_element.
    # Таким образом, это эквивалентно записи:
    # element = browser.find_element(class_name, 'fast-search__input')
    element = browser.find_element(*CatalogPage.fast_search__input)
    element.send_keys('samsung')
    sleep(5)
    clear_input(element)

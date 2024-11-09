from selenium.webdriver.common.keys import Keys


def clear_input(element):
    element.send_keys(Keys.CONTROL + 'a')
    element.send_keys(Keys.DELETE)
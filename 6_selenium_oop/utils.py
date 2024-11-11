from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def clear_input(element):
    element.send_keys(Keys.CONTROL + 'a')
    element.send_keys(Keys.DELETE)


def wait_element(driver, by, value, delay=10):
    try:
        element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((by, value)))
        return element
    finally:
        driver.quit()
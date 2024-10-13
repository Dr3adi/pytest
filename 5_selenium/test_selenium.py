def test_selenium_example(driver):
    driver.get('http://selenium.dev/')
    assert driver.title == 'Selenium'

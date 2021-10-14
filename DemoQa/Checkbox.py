from selenium import webdriver
import time

driver = webdriver.Chrome()
def test_checkbox():
    driver.get('https://www.demoqa.com/checkbox')
    driver.maximize_window()
    time.sleep(1)
    driver.find_element_by_class_name('rct-checkbox').click()
    time.sleep(1)
    assert 'home' in driver.find_element_by_class_name('text-success').text
    time.sleep(1)
    driver.close()
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.demoqa.com/links')
driver.maximize_window()

def test_switchlink():
    time.sleep(1)
    driver.find_element_by_link_text('Home').click()
    time.sleep(5)
    driver.switch_to_window(driver.window_handles[0])
    time.sleep(1)


def test_link():
    driver.find_element_by_link_text('Created').click()
    time.sleep(2)
    assert 'Link has responded with staus 201 and status text Created' in driver.find_element_by_id('linkResponse').text

    driver.close()

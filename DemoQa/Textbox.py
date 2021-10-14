from selenium import webdriver
import time

driver = webdriver.Chrome()

def test_textbox():
    driver.get('https://www.demoqa.com/text-box')
    driver.maximize_window()
    time.sleep(1)
    driver.find_element_by_id('userName').send_keys('Morgan')
    time.sleep(1)
    driver.find_element_by_id('userEmail').send_keys('morgan@gmail.com')
    time.sleep(1)
    driver.find_element_by_id('currentAddress').send_keys('Indonesia')
    time.sleep(1)
    driver.find_element_by_id('permanentAddress').send_keys('Indonesia')
    time.sleep(1)
    driver.find_element_by_id('submit').click()
    time.sleep(1)
    assert 'Morgan' in driver.find_element_by_id('name').text



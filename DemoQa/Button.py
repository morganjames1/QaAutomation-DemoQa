from selenium import webdriver
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get('https://www.demoqa.com/buttons')
driver.maximize_window()

def test_rightclick():
    time.sleep(1)
    # driver.refresh()
    time.sleep(2)
    source = driver.find_element_by_id('rightClickBtn')
    action = ActionChains(driver)
    action.context_click(source).perform()
    assert 'You have done a right click' in driver.find_element_by_id('rightClickMessage').text
    time.sleep(2)

def test_doubleclick():
    time.sleep(1)
    source = driver.find_element_by_id('doubleClickBtn')
    action = ActionChains(driver)
    action.double_click(source).perform()
    time.sleep(1)
    assert 'You have done a double click' in driver.find_element_by_id('doubleClickMessage').text
    
def test_click():
    time.sleep(1)
    # source = driver.find_element_by_id('c4Wb3')
    # source = driver.find_elements_by_css_selector('#c4Wb3')
    source = driver.find_elements_by_xpath('//*[@id="c4Wb3"]')
    action = ActionChains(driver)
    action.click(source).perform()
    time.sleep(1)
    assert 'You have done a dynamic click' in driver.find_element_by_id('dynamicClickMessage').text
    time.sleep(1)
    driver.close()








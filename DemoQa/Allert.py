from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get('https://www.demoqa.com/alerts')
driver.maximize_window()
time.sleep(1)

def test_alert():
    driver.find_element_by_id('alertButton').click()
    time.sleep(2)
    driver.switch_to.alert.accept()
    time.sleep(2)
    assert 'Click Button to see alert' in driver.find_element_by_xpath('//*[@id="javascriptAlertsWrapper"]/div[1]/div[1]/span').text
    time.sleep(2)

def test_alert5scnd():
    driver.find_element_by_id('timerAlertButton').click()
    time.sleep(6)
    driver.switch_to.alert.accept()
    time.sleep(2)
    assert 'On button click, alert will appear after 5 seconds' in driver.find_element_by_xpath('//*[@id="javascriptAlertsWrapper"]/div[2]/div[1]/span').text
    time.sleep(2)

def test_confirmbox():
    driver.find_element_by_id('confirmButton').click()
    time.sleep(2)
    driver.switch_to.alert.accept() 
    # driver.switch_to.alert.dismiss()
    time.sleep(2)
    assert 'You selected Ok' in driver.find_element_by_xpath('//*[@id="confirmResult"]').text
    time.sleep(2)

def test_promptbox():
    driver.find_element_by_id('promtButton').click()
    time.sleep(1)
    driver.switch_to.alert.send_keys('Saya sedang test')
    time.sleep(3)
    driver.switch_to.alert.accept()
    time.sleep(2)
    assert 'You entered Saya sedang test' in driver.find_element_by_xpath('//*[@id="promptResult"]').text
    time.sleep(2)

    driver.close()









from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pyautogui


driver = webdriver.Chrome()

driver.get('https://www.demoqa.com/automation-practice-form')
driver.maximize_window()
# driver.find_element_by_id('firstName').send_keys('Morgan')
# time.sleep(1)
# driver.find_element_by_id('lastName').send_keys('James')
# time.sleep(1)
# driver.find_element_by_id('userEmail').send_keys('jamess@gmail.com')
# time.sleep(1)
# driver.find_element_by_css_selector('#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(1)').click()
# time.sleep(1)
# driver.find_element_by_id('userNumber').send_keys('089648946287')
# time.sleep(1)
# driver.find_element_by_css_selector('#hobbiesWrapper > div.col-md-9.col-sm-12 > div:nth-child(1)').click()
# time.sleep(1)
# driver.find_element_by_id('uploadPicture').send_keys('H:\FD\IMG.jpg')
# time.sleep(1)
# driver.find_element_by_id('currentAddress').send_keys('Hallo Dunia')
# time.sleep(2)
# driver.find_element_by_css_selector('#state > div > div.css-1wy0on6 > div').click()
time.sleep(2)
driver.find_element_by_css_selector('#state > div > div.css-1hwfws3 > div.css-1uccc91-singleValue').click()
pyautogui.typewrite('Haryana')
pyautogui.press('enter')


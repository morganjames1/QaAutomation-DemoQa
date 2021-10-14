from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import pyautogui


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://www.demoqa.com/select-menu')
time.sleep(2)



driver.find_element_by_xpath('//*[@id="selectOne"]/div/div[2]/div').click()
pyautogui.typewrite('Prof.')
pyautogui.press('enter')

time.sleep(1)
pilih = Select(driver.find_element_by_css_selector('#oldSelectMenu'))
time.sleep(1)
pilih.select_by_visible_text('Yellow')

time.sleep(1)

driver.find_element_by_xpath('//*[@id="selectMenuContainer"]/div[7]/div/div/div/div[2]/div').click()

time.sleep(2)

driver.find_element_by_css_selector('#selectMenuContainer > div:nth-child(7) > div > div > div > div.css-1wy0on6 > div').click()
pyautogui.typewrite('Red')
pyautogui.press('enter')
pyautogui.typewrite('Black')
pyautogui.press('enter')





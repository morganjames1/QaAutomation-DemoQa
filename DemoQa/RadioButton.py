from selenium import webdriver
import time
# from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('https://www.demoqa.com/radio-button')
time.sleep(1)
driver.maximize_window()
time.sleep(1)

driver.find_element_by_id('yesRadio').click()
# pilih = Select(driver.find_element_by_xpath('//*[@id="yesRadio"]'))
# time.sleep(1)
# pilih.select_by_visible_text('Yes')





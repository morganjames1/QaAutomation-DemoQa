from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.demoqa.com/webtables')
driver.maximize_window()
time.sleep(1)
# driver.find_element_by_id('addNewRecordButton').click()
# time.sleep(1)
# driver.find_element_by_id('firstName').send_keys('Morgan')
# time.sleep(1)
# driver.find_element_by_id('lastName').send_keys('James')
# time.sleep(1)
# driver.find_element_by_id('userEmail').send_keys('morgan@gmail.com')
# time.sleep(1)
# driver.find_element_by_id('age').send_keys('23')
# time.sleep(1)
# driver.find_element_by_id('salary').send_keys('10000')
# time.sleep(1)
# driver.find_element_by_id('department').send_keys('Technology')
# time.sleep(1)
# driver.find_element_by_id('submit').click()
# time.sleep(2)
# driver.find_element_by_id('delete-record-1').click()
# Edit Data
driver.find_element_by_id('edit-record-1').click()
time.sleep(1)

driver.find_element_by_id('firstName').clear()
time.sleep(1)
driver.find_element_by_id('firstName').send_keys('Marsel')

time.sleep(1)
driver.find_element_by_id('lastName').clear()
time.sleep(1)
driver.find_element_by_id('lastName').send_keys('Putri')

time.sleep(1)
driver.find_element_by_id('userEmail').clear()
time.sleep(1)
driver.find_element_by_id('userEmail').send_keys('putri@gmail.com')
time.sleep(1)

driver.find_element_by_id('age').clear()
time.sleep(1)
driver.find_element_by_id('age').send_keys('23')
time.sleep(1)

driver.find_element_by_id('salary').clear()
time.sleep(1)
driver.find_element_by_id('salary').send_keys('130000')
time.sleep(1)

driver.find_element_by_id('department').clear()
time.sleep(1)
driver.find_element_by_id('department').send_keys('Accounting')
time.sleep(1)

driver.find_element_by_id('submit').click()



from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('https://www.facebook.com/')
driver.maximize_window()
time.sleep(2)
# Login Sudah punya akun
# driver.find_element_by_id('email').send_keys('woi@mail.com')
# time.sleep(2)
# driver.find_element_by_id('pass').send_keys('test123')
# driver.find_element_by_name('login').click()
# driver.find_element_by_class_name('_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy').click()

# Daftar Baru
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]/a').click()
time.sleep(2)
driver.find_element_by_name('firstname').send_keys('james')
time.sleep(1)
driver.find_element_by_name('lastname').send_keys('morg')
time.sleep(1)
driver.find_element_by_name('reg_email__').send_keys('1234567890')
time.sleep(1)
driver.find_element_by_name('reg_passwd__').send_keys('qwerty123')
time.sleep(2)
pilihd = Select(driver.find_element_by_id('day'))
pilihd.select_by_value('17')
time.sleep(1)
pilihm = Select(driver.find_element_by_id('month'))
pilihm.select_by_value('5')
time.sleep(1)
pilihy = Select(driver.find_element_by_id('year'))
pilihy.select_by_value('1997')
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span[2]/input').click()





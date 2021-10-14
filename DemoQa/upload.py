from selenium import webdriver
import time
import pyautogui
    
driver = webdriver.Chrome()

def test_uploadbutton():
    driver.get("https://gofile.io/uploadFiles")
    driver.implicitly_wait(10)
    driver.maximize_window()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="rowUploadButton"]/div/div/div/div/div/div[1]/div/button').click()
    time.sleep(2)
    pyautogui.write(r"H:\FD\IMG.jpg")
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(10)
    assert 'Your files have been successfully uploaded' in driver.find_element_by_xpath('//*[@id="rowUploadSuccess"]/div/div/div/div[1]/div/div/h5').text


def test_upload1():
    driver.get('https://www.demoqa.com/upload-download')
    time.sleep(2)
    driver.maximize_window()
    time.sleep(2)
    driver.find_element_by_id('uploadFile').send_keys('H:\FD\IMG.jpg')
    time.sleep(2)
    assert 'C:\\fakepath\\IMG.jpg' in driver.find_element_by_id('uploadedFilePath').text
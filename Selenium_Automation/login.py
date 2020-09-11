from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="C:\\python\\Python_Drivers\\chromedriver.exe")
driver.get('https://demo.actitime.com/')
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element_by_id('username').send_keys('admin')
driver.find_element_by_name('pwd').send_keys('manager')
#driver.find_element_by_xpath("//div[text()='Login ']").click()
driver.find_element_by_id('loginButton').click()
driver.find_element_by_xpath("//a[@id='logoutLink']").click()

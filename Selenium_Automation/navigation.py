from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="C:\\python\\Python_Drivers\\chromedriver.exe")
driver.get('https://demo.actitime.com/')
time.sleep(2)
print(driver.title)
driver.get('https://www.nationalexpress.com')
time.sleep(2)
print(driver.title)
driver.back()
time.sleep(2)
print(driver.title)
driver.forward()
time.sleep(2)
print(driver.title)
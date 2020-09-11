from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="C:\\python\\Python_Drivers\\chromedriver.exe")
driver.get('https://google.com/')
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element_by_name('q').send_keys('Jesus Christ')
driver.find_element_by_xpath("//span[@class='wFncld z1asCe MZy1Rb']").click()
button=driver.find_element_by_name('btnK').click()

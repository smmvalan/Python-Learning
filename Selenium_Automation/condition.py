from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="C:\\python\\Python_Drivers\\chromedriver.exe")
'''
driver.get("https://demo.actitime.com")
# it verify the elements condition
userEle=driver.find_element_by_id("username")
print(userEle.is_displayed())
print(userEle.is_enabled())
# password element
pwdEle=driver.find_element_by_name("pwd")
print(pwdEle.is_displayed())
print(pwdEle.is_enabled())

# After login 
userEle.send_keys('admin')
pwdEle.send_keys('manager')
driver.find_element_by_id('loginButton').click()
'''
driver.get("https://krninformatix.com/sample.html")
chkStatus=driver.find_element_by_id('rem').click()
radStatus=driver.find_element_by_id('male')
print(radStatus.is_displayed())
print(radStatus.is_enabled())


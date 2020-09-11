from selenium import webdriver

import time
driver=webdriver.Chrome(executable_path="C:\\python\\Python_Drivers\\chromedriver.exe")
driver.get("https://www.amazon.co.uk")
cookie=driver.get_cookies()
print(len(cookie)) # no of cookies available
print(cookie) # cookie pair

# Adding new cookie

cookie={'name':'Mycookie','value':'123456'} # cookie is a dictionary
driver.add_cookie(cookie)

cookie=driver.get_cookies()
print(len(cookie)) # no of cookies available
print(cookie) # cookie pair

# Delete the cookie

driver.delete_cookie('Mycookie')
print(len(cookie))

driver.delete_all_cookies()
print(len(cookie))
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="C:\\python\\Python_Drivers\\chromedriver.exe")
driver.get("https://demo.actitime.com")
driver.implicitly_wait(5)
driver.maximize_window
# Check the expected title with actual title
assert "actiTIME - Login" in driver.title

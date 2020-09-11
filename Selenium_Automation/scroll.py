from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
driver=webdriver.Chrome(executable_path="C:\\python\\Python_Drivers\\chromedriver.exe")
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
''' Method one
driver.execute_script("window.scrollBy(0,2000)","")
Method 2
flag=driver.find_element_by_xpath("//td[text()='India']")
driver.execute_script("arguments[0].scrollIntoView();",flag)
'''
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
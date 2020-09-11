from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="C:\\python\\Python_Drivers\\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element_by_xpath("//button[text()='Click Me']").click()
time.sleep(5)
driver.switch_to_alert().accept() # accept alert window by ok
driver.find_element_by_xpath("//button[text()='Click Me']").click()
time.sleep(5)
driver.switch_to_alert().dismiss() # close alert window by dismiss
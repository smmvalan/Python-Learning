from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(executable_path="C:\\python\\Python_Drivers\\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()

admin=driver.find_element_by_xpath("//b[text()='Admin']")
management=driver.find_element_by_link_text("User Management")
users=driver.find_element_by_link_text("Users")

action=ActionChains(driver)
action.move_to_element("admin").move_to_element("management").move_to_element("users").click().perform
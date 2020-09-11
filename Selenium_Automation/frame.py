from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="C:\\python\\Python_Drivers\\chromedriver.exe")
driver.get("https://www.selenium.dev/selenium/docs/api/java/")

driver.switch_to_frame("packageListFrame") # first frame
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(3)

driver.switch_to.default_content() #default frame
driver.switch_to_frame("packageFrame") # second frame
time.sleep(3)

driver.find_element_by_link_text("WebDriver").click()
time.sleep(3)
driver.switch_to.default_content() # default frame

driver.switch_to_frame("classFrame") # third 
driver.find_element_by_xpath("(//a[text()='Deprecated'])[1]").click()


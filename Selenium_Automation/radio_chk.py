from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="C:\\python\\Python_Drivers\\chromedriver.exe")
driver.get("https://krninformatix.com/sample.html")
driver.implicitly_wait(10)
# working with the radio button
status=driver.find_element_by_id("male").is_displayed
print(status)
driver.find_element_by_id("male").click()
status=driver.find_element_by_id("male").is_selected
print(status)
driver.find_element_by_id("rem").click()
status=driver.find_element_by_id("rem").is_selected
print(status)
driver.close()

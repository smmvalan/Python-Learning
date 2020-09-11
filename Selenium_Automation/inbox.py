from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
driver=webdriver.Chrome(executable_path="C:\\python\\Python_Drivers\\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.implicitly_wait(10)
driver.maximize_window()
# How to find out the textboxes in webpage
txtBox=driver.find_elements(By.CLASS_NAME,"text_field")
print(len(txtBox))

# Status of textboxes
status=driver.find_element_by_id("RESULT_TextField-1").is_displayed
print(status) # True or False
status1=driver.find_element_by_id("RESULT_TextField-1").is_enabled
print("Enabled or not:",status1) # True or False

# How to add the values into textbox

driver.find_element(By.ID,"RESULT_TextField-1").send_keys("Mickle")
driver.find_element(By.ID,"RESULT_TextField-2").send_keys("Soosai")
driver.find_element_by_id("RESULT_TextField-3").send_keys("123456")
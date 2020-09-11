from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
driver=webdriver.Chrome(executable_path="C:\\python\\Python_Drivers\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://www.expedia.com")

driver.maximize_window
# driver.find_element_by_id("tab-flight-tab-hp").click()
driver.find_element(By.ID,"tab-flight-tab-hp").click()

time.sleep(2)
driver.find_element_by_id("flight-origin-hp-flight").send_keys("SFO")
time.sleep(2)
driver.find_element_by_id("flight-destination-hp-flight").send_keys("NYC")

driver.find_element_by_id("flight-departing-hp-flight").clear()

driver.find_element_by_id("flight-departing-hp-flight").send_keys("12/10/2020")
time.sleep(2)
driver.find_element_by_id("flight-returning-hp-flight").clear()

driver.find_element_by_id("flight-returning-hp-flight").send_keys("15/10/2020")
#driver.find_element_by_xpath("//form[@id='gcw-hotel-form-hp-hotel']//button[contains(@class,'gcw-submit')]").click()
#wait= WebDriverWait (driver, 10)
#element=wait.until(EC.element_to_be_selected)
from selenium import webdriver
from selenium.webdriver import ActionChains
driver=webdriver.Chrome(executable_path="C:\\python\\Python_Drivers\\chromedriver.exe")
driver.get("https://krninformatix.com/sample.html")
driver.maximize_window()

driver.find_element_by_id("brow").send_keys("C://FeliC-2.pdf")

driver.close()


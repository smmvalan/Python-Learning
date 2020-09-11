from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="C:\\python\\Python_Drivers\\chromedriver.exe")
driver.get("http://magento-demo.lexiconn.com/")
driver.maximize_window
driver.implicitly_wait(20)
driver.find_element_by_id("search").send_keys("Bed & Bath")
txt=driver.find_element_by_xpath("//button[@class='button search-button']")
txt.click()

tot=driver.find_elements_by_xpath("//h2[@class='product-name']")
print(len(tot))
for product in tot:
    print(product.text)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path="C:\\python\\Python_Drivers\\chromedriver.exe")
driver.get("http://magento-demo.lexiconn.com")
links=driver.find_elements(By.TAG_NAME,"a")
print("No of links are presented in the links:", len(links)) # how many links
for sum in links:
    print(sum.text)

#driver.find_element(By.LINK_TEXT,"http://magento-demo.lexiconn.com/ecomerce/magento").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"header-").click()
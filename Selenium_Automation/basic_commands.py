from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="C:\\python\\Python_Drivers\\chromedriver.exe")
driver.get("http://magento-demo.lexiconn.com/")
#driver.maximize_window()
driver.implicitly_wait(2)
driver.find_element_by_xpath("//input[@id='search']").send_keys('bed & bath')
driver.find_element_by_xpath("//button[@title='Search']").click()
time.sleep(5)
driver.find_element_by_xpath("//a[text()='Gramercy Throw']").click()
time.sleep(20)


'''print (len(lis))
for i in lis:
     print(i)
     '''

driver.close()





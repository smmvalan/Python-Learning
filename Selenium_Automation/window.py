from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="C:\\python\\Python_Drivers\\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")
driver.find_element_by_xpath("//button[@class='btn btn-info']").click()
print(driver.current_window_handle) # parent window unique or id print
handles=driver.window_handles # open all browser values ( 2 windows)
for handle in handles:
    driver.switch_to_window(handle)
    print(driver.title)
    if driver.title=="Frames & windows":
        driver.close()
driver.quit()

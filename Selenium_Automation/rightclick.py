from selenium import webdriver
from selenium.webdriver import ActionChains
driver=webdriver.Chrome(executable_path="C:\\python\\Python_Drivers\\chromedriver.exe")
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
button=driver.find_element_by_xpath("//span[text()='right click me']") # function key f12 open the source code
action=ActionChains(driver)
action.context_click(button).perform()




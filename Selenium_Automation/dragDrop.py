from selenium import webdriver
from selenium.webdriver import ActionChains
driver=webdriver.Chrome(executable_path="C:\\python\\Python_Drivers\\chromedriver.exe")
driver.get("http://www.dhtmlgoodies.com/submitted-scripts/i-google-like-drag-drop/index.html")
driver.maximize_window()
source1=driver.find_element_by_xpath("//*[@id='block-2']")
target1=driver.find_element_by_xpath("//*[@id='block-4']")
action=ActionChains(driver)
action.drag_and_drop(source1,target1).perform()

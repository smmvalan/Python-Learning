from selenium import webdriver
from selenium.webdriver import ActionChains
driver=webdriver.Chrome(executable_path="C:\\python\\Python_Drivers\\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
element=driver.find_element_by_xpath("//button[text()='Copy Text']").click()
action=ActionChains(driver)
action.double_click(element).perform()
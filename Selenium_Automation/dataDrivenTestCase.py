from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import openpyxl
import xlUtil
driver=webdriver.Chrome(executable_path="C:\\python\\Python_Drivers\\chromedriver.exe")
driver.get("https://demo.actitime.com/login.do")
path="C:\\python\\data\\active.xlsx"
row=xlUtil.getRowCount(path,'Sheet1')
col=xlUtil.getColumCount(path,'Sheet1')
print(row)

for r in range(2,row+1):
    username=xlUtil.readDataFile(path,"Sheet1",r,1)
    password= xlUtil.readDataFile(path,"Sheet1",r,2)
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_name("pwd").send_keys(password)

    driver.find_element_by_xpath("//div[text()='Login ']").click()

    if driver.title =="actiTIME - Login":
        print("Login is Successful")
        xlUtil.writeDataFile(path,"Sheet1",r,3,"pass") 
    else:
        xlUtil.writeDataFile(path,"Sheet1",r,3,"fail")
        
    driver.find_element_by_class_name("logout").click()
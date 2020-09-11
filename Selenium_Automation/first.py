from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#webdriver.Chrome('.//Selenium_Driver/chromedriver.exe')
#driver=webdriver.Ie(executable_path='C:\\Users\\User\\Desktop\\python\\Driver\\IEDriverServer.exe')
driver=webdriver.Firefox(executable_path='C:\\Users\\User\\Desktop\\python\\Driver\\geckodriver.exe')
driver.get('https://www.google.com/')
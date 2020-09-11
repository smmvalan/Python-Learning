from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\python\\Python_Drivers\\chromedriver.exe")
driver.get("https://www.amazon.co.uk")
#driver.save_screenshot("c:\\python\\homepage.png"
driver.get_screenshot_as_file("c:\\python\\homepage2.jpg")
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromeOptions= Options()
chromeOptions.add_experimental_option("prefs",{"download.default_directory": "C:\\download"})

driver=webdriver.Chrome(executable_path="C:\\python\\Python_Drivers\\chromedriver.exe",chrome_options=chromeOptions)
driver.get("https://krninformatix.com/download.php")
driver.maximize_window()
driver.find_element_by_xpath("(//a[text()='Download'])[2]").click()
from selenium import webdriver

fp=webdriver.FirefoxProfile()
fp.set_preference("browser.helperApps.neverAsk.saveToDisk","text/plain/zip") #MIME
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir","C:\\download")
fp.set_preference("browser.download.folderlist",2)
fp.set_preference("pdfjs.disables",True)
driver=webdriver.Firefox(executable_path="C:\\python\\Python_Drivers\\geckodriver.exe",firefox_profile=fp)
driver.get("https://krninformatix.com/download.php")
driver.maximize_window()
driver.find_element_by_xpath("(//a[text()='Download'])[2]").click()
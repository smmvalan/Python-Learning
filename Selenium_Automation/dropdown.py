from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome(executable_path="C:\\python\\Python_Drivers\\chromedriver.exe")
driver.get("https://krninformatix.com/sample.html")
driver.implicitly_wait(2)
# Method1 drop=Select(driver.find_element_by_id("city"))
element=driver.find_element_by_id("city")
drp=Select(element)


# we can identify in 3 methods

# select by visible text
drp.select_by_visible_text('Chennai')

# select by index. Index start from 0
drp.select_by_index(0) # select by bangalore

# select by value
drp.select_by_value('3') # select by mumbai

# count all drop down options
print(len(drp.options))

allOptions=drp.options

for option in allOptions:
    print(option.text)
   
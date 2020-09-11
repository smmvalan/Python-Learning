from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="C:\\python\\Python_Drivers\\chromedriver.exe")
driver.get("https://krninformatix.com/learn.html")
row=len(driver.find_elements_by_xpath("html/body/table/tbody/tr")) # row
col=row=len(driver.find_elements_by_xpath("html/body/table/tbody/tr[1]/td"))
print(row,col)

# To extract the values from tables
starrepeat = '*'*100
print(starrepeat)
print("No"    +" "+"Browser"+""+ "box"+" Status")

print(starrepeat)

for r in range(1,row+1):
    for c in range(1,col+1):
        value=driver.find_element_by_xpath("html/body/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text   # row and column are in. it needs to be converted as string
        # concordination or type casting
        print(value,end='  ') # product
    print()

              
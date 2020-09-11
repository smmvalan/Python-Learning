from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="C:\\python\\Python_Drivers\\chromedriver.exe")
#driver.maximize_window()
driver.get('https://web.whatsapp.com/')
input("Enter any keys to confirm after the scan:")
name=input("Enter the whatapp name:")
# find out the xpath of whatapp name
user=driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
user.click()


txtMessage = 'This message has been sent through python script as a trial. Hello Sweet Heart. Dont waste your time to sitting in the Chair.What are you doing. I am very busy with automation'


count =1
# send the text
msgBox=driver.find_element_by_xpath("(//div[contains(@class,'_3FRCZ')])[2]")


for i in range(count):
    msgBox.send_keys(txtMessage)
# Click the button
    button=driver.find_element_by_class_name('_1U1xa')
    button.click()
print('completed')


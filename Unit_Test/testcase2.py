import unittest
from selenium import webdriver

class searchEngineTest (unittest.TestCase):
    def test_Google(self):  # test method always start with test
        self.driver=webdriver.Chrome(executable_path="C:\\python\\Python_Drivers\\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        print("Title of the page is: " + self.driver.title)
        self.driver.close()

    def testBing(self):
        self.driver=webdriver.Chrome(executable_path="C:\\python\\Python_Drivers\\chromedriver.exe")
        self.driver.get("https://www.bing.com/")
        print("Title of the page is :" + self.driver.title)
        self.driver.close()

if  __name__ == "__main__" :    
    unittest.main()
        
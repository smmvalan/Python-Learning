import unittest
from selenium import webdriver
class assertTest (unittest.TestCase):
    def testName(self):
        driver= webdriver.Chrome(executable_path = "C:\\python\\Python_Drivers\\chromedriver.exe")
        #driver=None
        self.assertIsNone(driver)    
        
if __name__ == "__main__":
    unittest.main()
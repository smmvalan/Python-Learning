import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        self.driver= webdriver.Chrome(executable_path = "C:\\python\\Python_Drivers\\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        webPage=self.driver.title
        #self.assertEqual("Google", webPage,"webpage title is not same")
        #self.assertNotEqual("Google123", webPage)
        #self.assertTrue (webPage=='Google')
        self.assertFalse (webPage=="Google")

if __name__ == "__main__":
    unittest.main()
import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        list = ("python, selenium, java")
       # self.assertIn("python", list)  # true
        self.assertNotIn ("python", list) # false
if __name__ == "__main__":
    unittest.main()
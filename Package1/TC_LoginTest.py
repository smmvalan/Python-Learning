import unittest

from selenium import webdriver

class LoginTest(unittest.TestCase):
    def test_loginbyEmail(self):
        print("This is login by email test")
        self.assertTrue(True)

    def test_loginbyFacebook(self):
        print("This is login by facebook test")
        self.assertTrue(True)

    def test_loginbyTweeter(self):
        print("This is login by tweeter test")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
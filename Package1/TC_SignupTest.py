import unittest
from selenium import webdriver

class SignupTest(unittest.TestCase):
    def test_signupbyEmail(self):
        print("This is sign by email test")
        self.assertTrue(True)

    def test_signbyFacebook(self):
        print("This is sign by facebook test")
        self.assertTrue(True)

    def test_signbyTweeter(self):
        print("This is sign by tweeter test")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
import unittest
from selenium import webdriver

def setUpModule (): # will be executed before executing any class
    print ("setUpModule")

def tearDownModule():
    print ("tearDownModule")

class AppTesting(unittest.TestCase):
    @classmethod # decorator
    def setUp(cls):   # Execute before all methods
        print("This is login Test")
    @classmethod           # decorator
    def tearDown(cls):      # execute after all test methods
        print("This is logout Test")

    @classmethod
    def setUpClass(cls):     # Execute once when the class is started
        print("Open Application")

    @classmethod
    def tearDownClass(self):
        print("Close Application")

    def test_advantage (self):
        print("This is Advanced search test")    
    
    def test_prepaidRecharge(self):
        print("This is prepaid Recharge test")
        
    def test_postpaidRecharge(self):
        print (" This is post paidRecharge test")
if __name__ == "__main__":
    unittest.main()
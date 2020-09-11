import pytest
@pytest. yield_fixture()
def setup():
    print("once before every method")
    yield
    print("once after every method")

def testmethod1 (setup):
    print ("This is the test method1")

def testmethod2 (setup):
    print ("This is the test method2")

# execute : pytest -v-s test_demo.py

# pytest -v-s test_demo
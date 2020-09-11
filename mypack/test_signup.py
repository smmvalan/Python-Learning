import pytest

@pytest.yield_fixture()

def setup():
    print("opening the url to signup")
    yield
    print("Closing url after signup")


def test_signupByemail():
    print ("This is signup by email test")


def test_signupByFacebool():
    print ("This is signup by facebook test")

    #pytest -v -s mypack test_login.py to execute the program in terminal. if you give the path where the mypack is saved

    particularly one test method to be executed

    pytest -v -s mypack test_login.py::loginByFacebooks
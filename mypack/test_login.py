import pytest

@pytest.yield_fixture()

def setup():
    print("opening the browser before login")
    yield
    print("Closing browser after login")


def test_loginByemail():
    print ("This is Login by email test")


def test_loginByFacebool():
    print ("This is Login by facebook test")

    #pytest -v -s mypack test_login.py to execute the program in terminal
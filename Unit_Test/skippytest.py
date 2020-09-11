import unittest
class Apptesting(unittest.TestCase):

    @unittest.SkipTest #decorator
    def test_search(self):
        print("This is search test")

    @unittest.skip ("I am skipping this test method because of it is ready")
    def test_advanceSearch(self):
        print ("This is adv search method")

    @unittest.skipIf(1==1, "numbers are not equals")
    def test_prepadidRecharge(self):
        print(" This is pre paid recharge")

    def test_postpaidRecharge(self):
        print("This is post paid recharge")

    def test_loginbyGmail(self):
        print("This is loging by Gmail")

    def test_loginbyTweeter(self):
        print("This is loging by Tweeter")

if __name__ =="__main__":
    unittest.main()
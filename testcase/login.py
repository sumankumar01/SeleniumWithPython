import unittest

from selenium import webdriver
from pageobjects.LoginPage import loginpage1



class Login(unittest.TestCase):



    @classmethod
    def setUpClass(cls):
        print('Executed Before the all the method executed in class')

    @classmethod
    def tearDownClass(cls):
        print('executed after the all the method executed in class')

    def setUp(self):
        print("Setup the environment")
        self.driver=webdriver.Chrome()
        self.driver.get("http://www.newtours.demoaut.com/")


    def tearDown(self):
        print("cleaning the environment")

    def testloginScanario(self):
        print("running the test case1 {0.driver}".format(self))

        loginpage1(self.driver).EnterCredential()

    def testReservation(self):
        print("running the test case1 {0.driver}".format(self))
        Login().testloginScanario()
        
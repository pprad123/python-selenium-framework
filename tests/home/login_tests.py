#from selenium import webdriver
#from selenium.webdriver.common.by import By
#import time
#from selenium.webdriver import ActionChains
from pages.home.login_pages import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest



@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class LoginTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_validLogin(self):
        #self.driver.get(self.baseURL)
        #self.lp = LoginPage(self.driver)
        self.lp.login("preeti_pradhan2005@yahoo.co.in", "Mylord_03")
        result1 = self.lp.verifyLoginTitle()
        #assert result1 == True
        self.ts.mark(result1,"TitleVerification")

        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin",result2,"LoginVerification")

        #assert result2 == True


'''
    @pytest.mark.run(order=2)
    def test_InvalidLogin(self):

    # baseURL = "https://www.amazon.in/"
    # self.driver.get(self.baseURL)
    # self.lp = LoginPage(self.driver)

        self.lp.login("preeti_pradhan2005@yahoo.co.in", "mylord_03")

        result = self.lp.verifyLoginFaild()

        assert result == True
'''













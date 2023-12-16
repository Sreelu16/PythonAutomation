
import random
import string


from base.basepage import BasePage
from base.Reporter import Reporter
from utilities.common.Login import Login
from utilities.teststatus import TestStatus
import test_data.testData as tD
import unittest
import pytest
import time
import utilities.Constants as constant



@pytest.mark.usefixtures("oneTimeSetUpLauncher", "setUp")
class VerifyHomePage(unittest.TestCase, BasePage):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.ts = TestStatus(self.driver)
        self.reports = Reporter(self.driver, self.__class__.__name__)
        self.login = Login(self.driver, self.reports)
        self.homePageLocator = self.pageLocators('HomePage', 'HomePageLocator.json')

        print('Inside the Class Setup function')

    def test_login_in(self):
        try:
            self.login.qaToolsLogin()

            self.driver.quit()
        finally:
            self.reports.writeResult()

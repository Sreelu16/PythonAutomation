#@author Sreelakshmi
#Class Description: Login functions to be used across all test cases
import time
from base.basepage import BasePage
import test_data.testData as tD
import utilities.Constants as constant


class Login(BasePage):
    def __init__(self, driver, report):
        super().__init__(driver)
        self.loginPageLocator = self.pageLocators('LoginPage', 'LoginPageLocators.json')
        self.driver = driver
        self.reports = report

    def getLocator(self, locatorId):
        return self.pageLocators(locatorId)

    def qaToolsLogin(self):
        self.reports.report(constant.TYPE_STEP, "Click on login link on Qa tools home page")
        self.elementClick(*self.locator(self.loginPageLocator, 'loginlink'))
        self.reports.report(constant.TYPE_STEP, "Enter username on portal login page")
        self.enterInTextBox(tD.testData('Username'), *self.locator(self.loginPageLocator, 'username'))
        self.reports.report(constant.TYPE_STEP, "Enter password on portal login page")
        self.enterInTextBox(tD.testData('Password'), *self.locator(self.loginPageLocator, 'Password'))
        self.reports.report(constant.TYPE_STEP, "Click on continue button on portal login page")
        self.elementClick(*self.locator(self.loginPageLocator, 'loginButton'))
        time.sleep(15)

from base.selenium_driver import SeleniumDriver
import time
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from pages.home.navigation_page import NavigationPage

#class LoginPage(SeleniumDriver):
class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _login_link = "//a[@href='/sign_in']"
    _email_field = "//input[@id='user_email']"
    _password_field = "user_password"
    _login_button = "commit"
    _logout = "//div[@id='navbar']//a[@href='/sign_out']"

    # Perform Actions
    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, locatorType="xpath")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")

    def login(self, email="", password=""):
        self.clickLoginLink()
        time.sleep(3)
        self.clearFields()
        #time.sleep(2)
        self.enterEmail(email)
        self.enterPassword(password)
        time.sleep(3)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//a[@class='fedora-navbar-link navbar-link dropdown-toggle open-my-profile-dropdown']",
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[contains(text(), 'Invalid email or password')]", locatorType="xpath")
        return result

    # def verifyLoginTitle(self):
    #     if "Google" in self.getTitle():
    #         return True
    #     else:
    #         return False

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Let's Kode It")

    def clearFields(self):
        emailField = self.getElement(locator=self._email_field, locatorType="xpath")
        emailField.clear()

        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()

    def logout(self):
        self.nav.navigateToUserSettings()
        logoutLinkElement = self.waitForElement(locator=self._logout, locatorType="xpath", pollFrequency=1)
        self.elementClick(element=logoutLinkElement)
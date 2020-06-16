from base.selenium_driver import SeleniumDriver
import time
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

#class LoginPage(SeleniumDriver):
class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _my_courses = "//a[contains(text(), 'My Courses')]"
    _all_courses = "//a[contains(text(), 'All Courses')]"
    _practice = "//a[contains(text(), 'Practice')]"
    # _user_settings_icon = "//div[@id='navbar']//span[text()='Test']"
    _user_settings_icon = "//a[@class='fedora-navbar-link navbar-link dropdown-toggle open-my-profile-dropdown']"

    # Perform Actions
    def navigateToMyCourses(self):
        self.elementClick(locator=self._my_courses, locatorType="xpath")

    def navigateToAllCourses(self):
        self.elementClick(locator=self._all_courses, locatorType="xpath")

    def navigateToPractice(self):
        self.elementClick(locator=self._practice, locatorType="xpath")

    def navigateToUserSettings(self):
        userSettingsElement = self.waitForElement(locator=self._user_settings_icon,
                                                  locatorType="xpath", pollFrequency=1)
        # self.elementClick(locator=self._user_settings_icon, locatorType="xpath")
        self.elementClick(element=userSettingsElement)
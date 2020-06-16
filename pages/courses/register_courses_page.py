import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time

class RegisterCoursesPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _search_box = "//input[@id='search-courses']"
    _search_icon = "//button[@id='search-course-button']"
    # _course = "//div[@data-course-id='56740']//div[contains(text(), 'JavaScript for beginners')]"
    # _course = "//div[contains(@class,'course-listing-title') and contains(text(), 'JavaScript for beginners')]"
    _course = "//div[contains(@class,'course-listing-title') and contains(text(), '{0}')]"
    _all_courses = "//div[@class='course-listing-title']"
    _enroll_button = "//button[@id='enroll-button-top']"
    _cc_num = "//input[@aria-label='Credit or debit card number']"
    _exp_date = "//input[@name='exp-date']"
    _cc_cvv = "//input[@name='cvc']"
    _zip = "//input[@name='postal']"
    _terms_and_policies = "//input[@id='agreed_to_terms_checkbox']"
    # _submit_enroll = "//button[@class='btn btn-primary spc__button is-disabled']"
    _submit_enroll = "//button[@id='confirm-purchase']"

    # Perform Actions
    # Enter course name
    def clickSearchBox(self):
        self.elementClick(self._search_box, "xpath")

    def enterCourseName(self, name):
        self.sendKeys(name, self._search_box, "xpath")
        self.elementClick(self._search_icon, "xpath")

    # def selectCourseToEnroll(self):
    #     self.elementClick(self._course, "xpath")

    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(locator=self._course.format(fullCourseName), locatorType="xpath")

    def clickEnrollButton(self):
        self.elementClick(self._enroll_button, "xpath")

    def enterCardNum(self, num):
        # self.switchToFrame(name="__privateStripeFrame16")
        # self.sendKeys(num, self._cc_num, "xpath")
        time.sleep(7)
        self.switchFrameByIndex(self._cc_num, locatorType="xpath")
        self.sendKeysWhenReady(num, locator=self._cc_num, locatorType="xpath")
        # self.sendKeysCustom(num, self._cc_num, "xpath")
        self.switchToDefaultContent()

    def enterCardExp(self, exp):
        # self.switchToFrame(name="__privateStripeFrame17")
        self.switchFrameByIndex(self._exp_date, locatorType="xpath")
        self.sendKeys(exp, self._exp_date, "xpath")
        self.switchToDefaultContent()

    def enterCardCVV(self, cvv):
        # self.switchToFrame(name="__privateStripeFrame18")
        self.switchFrameByIndex(self._cc_cvv, locatorType="xpath")
        self.sendKeys(cvv, self._cc_cvv, "xpath")
        self.switchToDefaultContent()

    def enterZip(self, zip):
        # self.switchToFrame(name="__privateStripeFrame19")
        self.switchFrameByIndex(self._zip, locatorType="xpath")
        self.sendKeys(zip, self._zip, "xpath")
        self.switchToDefaultContent()

    def checkTermsAndPolicy(self):
        self.elementClick(self._terms_and_policies, "xpath")

    def clickEnrollSubmitButton(self):
        self.elementClick(self._submit_enroll, "xpath")

    def enterCreditCardInformation(self, num, exp, cvv, zip):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)
        self.enterZip(zip)
        self.checkTermsAndPolicy()

    def enrollCourse(self, num="", exp="", cvv="", zip=""):
        self.clickEnrollButton()
        self.webScroll("down")
        self.enterCreditCardInformation(num, exp, cvv, zip)

        # This step of clicking on Enroll Submit button is not included in the framework by tutor
        # self.clickEnrollSubmitButton()

    def verifyEnrollFailed(self):
        result = self.isEnabled(locator=self._submit_enroll, locatorType="xpath", info="Enroll Button")
        return not result

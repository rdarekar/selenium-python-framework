from pages.home.login_page import LoginPage
from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterMultipleCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        # self.lp = LoginPage(self.driver)
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners", "41811 5705 8102 5900", "10/21", "665", "411018"),
              ("Learn Python 3 from scratch", "41811 5705 8102 5900", "10/21", "665", "411018"))
    @unpack     # This decorator will unpack all the tuple / list elements into multiple arguments
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVV, zip):
        # self.lp.login("test@email.com", "abcabc")
        self.courses.clickSearchBox()
        self.courses.enterCourseName(courseName)
        # self.courses.selectCourseToEnroll()
        self.courses.selectCourseToEnroll(courseName)
        self.courses.clickEnrollButton()
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCVV, zip=zip)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment Failed Verification")

        # self.driver.find_element_by_link_text("All Courses").click()
        self.driver.find_element_by_xpath("//a[@class='navbar-brand header-logo']").click()
        # self.driver.get("https://learn.letskodeit.com/courses")
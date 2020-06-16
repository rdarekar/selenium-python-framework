from pages.home.login_page import LoginPage
from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    def test_invalidEnrollment(self):
        self.lp.login("test@email.com", "abcabc")
        self.courses.clickSearchBox()
        self.courses.enterCourseName("JavaScript")
        # self.courses.selectCourseToEnroll()
        self.courses.selectCourseToEnroll("JavaScript for beginners")
        self.courses.clickEnrollButton()
        self.courses.enrollCourse(num="4181 5705 8102 5900", exp="10/21", cvv="665", zip="411018")
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment Failed Verification")
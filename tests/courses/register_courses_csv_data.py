from pages.home.login_page import LoginPage
from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
from pages.home.navigation_page import NavigationPage

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        # self.lp = LoginPage(self.driver)
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.driver.find_element_by_xpath("//a[@class='navbar-brand header-logo']").click()

        # self.driver.get("https://learn.letskodeit.com/courses")

        self.nav.navigateToAllCourses()


    @pytest.mark.run(order=1)
    @data(*getCSVData("D:\\sachin_thakare\\python_programs\\letskodeit\\framework_pom_screenshot\\testdata.csv"))
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

        # Commenting the below lines, as we are using the same lines under setUp()
        # self.driver.find_element_by_xpath("//a[@class='navbar-brand header-logo']").click()
        # self.driver.get("https://learn.letskodeit.com/courses")
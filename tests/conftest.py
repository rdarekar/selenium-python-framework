import pytest
from selenium import webdriver
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import LoginPage

@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")

@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser, osType):
    #print("Running conftest demo one time setUp")
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    lp = LoginPage(driver)
    lp.login("test@email.com", "abcabc")


    # if browser == "firefox":
    #     baseURL = "https://letskodeit.teachable.com/"
    #     driver = webdriver.Firefox()
    #     driver.maximize_window()
    #     driver.implicitly_wait(3)
    #     driver.get(baseURL)
    #     print("Running tests on FF")
    # else:
    #     baseURL = "https://letskodeit.teachable.com/"
    #     driver = webdriver.Chrome()
    #     driver.maximize_window()
    #     driver.implicitly_wait(3)
    #     driver.get(baseURL)
    #     print("Running tests on Chrome")

    # We need to add "value" attribute, the one we created above to the test class using "request" keyword
    # If the class attribute from the request we are getting is not None then make the "value" guy as a class attribute
    # so that it can be available to all the instance, the complete class we are going to use
    if request.cls is not None:
        request.cls.driver = driver
    # The yield will return the value where a "fixture" is used. And "fixture" is used in "TestClassDemo"
    yield driver
    #driver.quit()
    #print("Running conftest demo one time tearDown")
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of Operating System")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")

import pytest
from selenium import webdriver
from base.webdriverfactory import WebDriverFactory
from pages.home.login_pages import LoginPage

@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")

    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()

    lp = LoginPage(driver)
    lp.login("preeti_pradhan2005@yahoo.co.in", "Mylord_03")
    # if browser == 'firefox':
    #     baseURL = "https://www.amazon.in/"
    #     driver = webdriver.Firefox()
    #     driver.maximize_window()
    #     driver.get(baseURL)
    #     driver.implicitly_wait(4)
    #     print("Running tests on FF")
    # else:
    #     baseURL = "https://www.amazon.in/"
    #     driver = webdriver.Chrome()
    #     driver.maximize_window()
    #     driver.get(baseURL)
    #     print("Running tests on chrome")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    #driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
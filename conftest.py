__author__ = 'AMMA'
from selenium import webdriver
import pytest
def pytest_addoption(parser):
    parser.addoption('--browser',action='store',default='chrome')

@pytest.fixture(scope='class')
def setup(request):
    browser=request.config.getoption('--browser')
    if browser=='chrome':
        driver=webdriver.Chrome(executable_path='C:/Users/satheesh/PycharmProjects/Selenium/chromedriver.exe')
    elif browser=='firefox':
        driver=webdriver.Firefox(executable_path='C:/Users/satheesh/PycharmProjects/Selenium/geckodriver.exe')
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver=driver
    yield
    driver.close()
    driver.quit()


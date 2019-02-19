import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
class TestLogin():

    @pytest.fixture(scope='session')
    def test_setup(self):
        global driver
        driver=webdriver.Chrome(executable_path='C:\\Users\\satheesh\\PycharmProjects\\Selenium\\chromedriver.exe')
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()




    def test_login(self,test_setup):
        driver.get('http://www.gcrit.com/build3/admin')
        driver.find_element_by_name('username').send_keys('admin')
        driver.find_element_by_name('password').send_keys('admin@123')
        driver.find_element_by_id('tdb1').click()
        assert 'http://www.gcrit.com/build3/admin/index.php' == driver.current_url

    def test_login2(self, test_setup):
        driver.find_element(By.LINK_TEXT, 'Logoff').click()
        print('Sucesffull')

        # else:
        #     print('Login Un Sucessfull --FAILED')
    # def test_logout(self,test_setup):
    #     driver.find_element(By.LINK_TEXT,'Logoff').click()
    #     print('Sucesffull')




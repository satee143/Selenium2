import unittest
from selenium import webdriver
from Exercise.POMREPOSITORY2 import loginpage
import time
import HtmlTestRunner
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),".","."))



class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path='C:/Users\satheesh/PycharmProjects/Selenium/chromedriver.exe')
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def test_callfunc(self):
        driver=self.driver
        login1=loginpage(driver)
        self.driver.get('http://www.gcrit.com/build3/admin')
        login1.enter_username('admin')
        login1.enter_password('admin@123')
        login1.login_click()
        time.sleep(4)
        login1.catalog_click()
        if 'http://www.gcrit.com/build3/' in driver.current_url:
            print('Login sucessfull and page redirected to user interface--PASS')
        else:
            print('Login Sucessfull and Page not redirected to user interface -- Failed')



if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/satheesh/PycharmProjects/Selenium/Reports'))

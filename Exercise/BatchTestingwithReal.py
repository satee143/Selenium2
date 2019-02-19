__author__ = 'AMMA'
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
import unittest
import HtmlTestRunner
# IN THIS IT WILL OPEN BROWSER AND CLOSE BROWSER FOR EACH FUNCTION/METHOD
class BatchTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        global driver
        driver=webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
        driver.maximize_window()
        time.sleep(3)

    @classmethod
    def tearDown(self):
        driver.close()
        driver.quit()

    def Page_open(self,uname,pwd):
        driver.get('http://www.gcrit.com/build3/admin')
        driver.find_element_by_name('username').send_keys(uname)
        driver.find_element_by_name('password').send_keys(pwd)
        driver.find_element_by_id('tdb1').click()


#Test Case1:
    def test_case1(self):
        self.Page_open('admin','admin@123')

        if 'http://www.gcrit.com/build3/admin/index.php' in driver.current_url:
            print('Test Case 1: USER LOGIN-- Sucessfull--Passed')
        else:
            print('Test Case 1: USER LOGIN--Test Failed--Failed')
#Test Case 2:
    def test_case2(self):
        self.Page_open('admin','admin123')
        if 'Invalid administrator login attempt' in driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td').text :
            print("Test Case 2: ERROR MESSAGE--User Login Failed with Invalid id and Password & Received Correct Error--Passed")
        else:
            print('Test Case 2: ERROR MESSAGE--User Login Failed with Invalid id and Password & Received In Correct Error--Failed')
#Test Case 3
    def test_case3(self):
        self.Page_open('admin','admin@123')

        driver.find_element_by_link_text('Online Catalog').click()
        time.sleep(4)
        if 'http://www.gcrit.com/build3' in driver.current_url:
            print('Test Case 3: REDIRECT --Page Redirected Sucessfull--Passed')
        else:
            print('Test Case 3: REDIRECT -- Page Redirection is Un Sucessfull --Failed')







if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/satheesh/PycharmProjects/Selenium/Reports'))

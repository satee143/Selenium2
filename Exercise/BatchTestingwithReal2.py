__author__ = 'AMMA'
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
import unittest
import HtmlTestRunner
# IN THIS IT WILL OPEN BROWSER AND CLOSE BROWSER FOR ONLY ONES FOR ALL METHOS/FUNCTIONS
class BatchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
        cls.driver.maximize_window()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def Page_open(self,uname,pwd):
        self.driver.get('http://www.gcrit.com/build3/admin')
        self.driver.find_element_by_name('username').send_keys(uname)
        self.driver.find_element_by_name('password').send_keys(pwd)
        self.driver.find_element_by_id('tdb1').click()




#Test Case1:
    def test_case1(self):
        self.Page_open('admin','admin@123')

        if 'http://www.gcrit.com/build3/admin/index.php' in self.driver.current_url:
            print('Test Case 1: USER LOGIN-- Sucessfull--Passed')
        else:
            print('Test Case 1: USER LOGIN--Test Failed--Failed')
#Test Case 2:
    def test_case2(self):
        self.driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td[2]/a').click()
        time.sleep(3)
        self.Page_open('admin','admin123')
        if 'Invalid administrator login attempt' in self.driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td').text :
            print("Test Case 2: ERROR MESSAGE--User Login Failed with Invalid id and Password & Received Correct Error--Passed")
        else:
            print('Test Case 2: ERROR MESSAGE--User Login Failed with Invalid id and Password & Received In Correct Error--Failed')
#Test Case 3
    def test_case3(self):
        self.Page_open('admin','admin@123')

        self.driver.find_element_by_link_text('Online Catalog').click()
        time.sleep(4)
        if 'http://www.gcrit.com/build3' in self.driver.current_url:
            print('Test Case 3: REDIRECT --Page Redirected Sucessfull--Passed')
        else:
            print('Test Case 3: REDIRECT -- Page Redirection is Un Sucessfull --Failed')







if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/satheesh/PycharmProjects/Selenium/Reports'))

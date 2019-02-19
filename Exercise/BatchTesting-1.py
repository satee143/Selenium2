__author__ = 'AMMA'
from selenium import webdriver
import unittest
from selenium .common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
class batch_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
        cls.driver.maximize_window()
    def admin_login(self,uname,pwd):
        self.driver.get('http://www.gcrit.com/build3/admin/')
        self.driver.find_element_by_name('username').send_keys(uname)
        self.driver.find_element_by_name('password').send_keys(pwd)
        self.driver.find_element_by_id('tdb1').click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



batch_test.admin_login('self','admin','admin@123')






# #CASE-1 Verify Admin Login in GCR shop admin login interface
#
# launch_browser()
# admin_login('admin','admin@123')
# url=driver.current_url
# if 'http://www.gcrit.com/build3/admin/index.php' in url:
#     print('Test case-1 Login is Sucessfull-- Pass')
# else:
#     print('Test Case-1 login is Un Sucessfull--Failed')
# close_browser()
# #time.sleep(5)
#
# launch_browser()
# admin_login('admin','admin@1223')
# error=driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td').text
# if 'The maximum number of login attempts has been reached. Please try again in 5 minute' in error:
#     print('Test case-1 Login is Sucessfull-- Pass')
# else:
#     print('Test Case-1 login is Un Sucessfull--Failed')
# close_browser()


if __name__ == '__main__':
    unittest.main


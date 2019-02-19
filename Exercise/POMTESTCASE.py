from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
import unittest
from Exercise.POMREPOSITORY import login

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
        cls.driver.maximize_window()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


    def test_login_valid(self):
        driver=self.driver
        driver.get('http://www.gcrit.com/build3/admin')
        login1=login(driver)
        login1.enter_username('admin')
        login1.enter_password('admin@1123')
        login1.click_login()
        if 'http://www.gcrit.com/build3/admin/index.php' in driver.current_url:
            print('Login Sucessfull--Passed')

        elif 'Invalid administrator login attempt' in driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td').text:
            print("Test Case 2: ERROR MESSAGE--User Login Failed with Invalid id and Password & Received Correct Error--Passed")
        else:
            print('Test Case 2: ERROR MESSAGE--User Login Failed with Invalid id and Password & Received In Correct Error--Failed')




if __name__ == '__main__':
    unittest.main()

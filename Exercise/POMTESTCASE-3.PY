from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time,os,sys
import unittest
from Exercise.POMREPOSITORY3 import user_interface_login


import HtmlTestRunner
sys.path.append(os.path.join(os.path.dirname(__file__),".","."))

class test_setup(unittest.TestCase):
	def setUp(self):
		
		self.driver=webdriver.Chrome(executable_path='C:/Users\satheesh/PycharmProjects/Selenium/chromedriver.exe')
		
		self.driver.maximize_window()
		self.driver.implicitly_wait(10)
	def tearDown(self):
		self.driver.close()

	def test_login(self):
		driver = self.driver
		login=user_interface_login(driver)

		self.driver.get('http://gcrit.com/build3')
		login.login_link()
		login.username_method('satee143@gmail.com')
		login.password_method('satee@1432')
		login.login_method()
		time.sleep(4)

		if driver.find_element_by_class_name('ui-button-text').is_displayed() == True:
			print('user login sucessfull to USER INTERFACE -- PASS')
		else:
			print('User Login Un sucessfull to USER INTERFACE -- FAILED')

 
if __name__ == '__main__':
	unittest.main()


	
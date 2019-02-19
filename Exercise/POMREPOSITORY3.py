import unittest
class user_interface_login(unittest.TestCase):
	def __init__(self,driver):
		self.driver=driver

		self.username_editbox_name='email_address'
		self.password_editbox_name='password'
		self.login_button_xpath='//*[@id="tdb5"]/span[2]'
		self.login_link_link_name='login'


	def username_method(self,uname):
		self.driver.find_element_by_name(self.username_editbox_name).clear()
		self.driver.find_element_by_name(self.username_editbox_name).send_keys(uname)

	def password_method(self,pwd):
		self.driver.find_element_by_name(self.password_editbox_name).clear()
		self.driver.find_element_by_name(self.password_editbox_name).send_keys(pwd)
	def login_link(self):
		self.driver.find_element_by_link_text(self.login_link_link_name).click()

	def login_method(self):
		self.driver.find_element_by_xpath(self.login_button_xpath).click()


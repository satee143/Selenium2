import unittest
import HtmlTestRunner
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))

class loginpage(unittest.TestCase):
    def __init__(self,driver):
        self.driver=driver

        self.username_textbox_name='username'
        self.password_textbox_name='password'
        self.login_button_id='tdb1'
        self.catalog_link_text='Online Catalog'

    def enter_username(self,uname):
        self.driver.find_element_by_name(self.username_textbox_name).clear()
        self.driver.find_element_by_name(self.username_textbox_name).send_keys(uname)

    def enter_password(self,pwd):
        self.driver.find_element_by_name(self.password_textbox_name).clear()
        self.driver.find_element_by_name(self.password_textbox_name).send_keys(pwd)

    def login_click(self):
        self.driver.find_element_by_id(self.login_button_id).click()

    def catalog_click(self):
        self.driver.find_element_by_link_text(self.catalog_link_text).click()



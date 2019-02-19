import unittest


class login(unittest.TestCase):
    def __init__(self,driver):
        self.driver=driver
        self.username_textbox_name = 'username'
        self.password_textbox_name = 'password'
        self.login_button_id = 'tdb1'



    def enter_username(self,uname):
        self.driver.find_element_by_name(self.username_textbox_name).clear()
        self.driver.find_element_by_name(self.username_textbox_name).send_keys(uname)


    def enter_password(self,pwd):
        self.driver.find_element_by_name(self.password_textbox_name).clear()
        self.driver.find_element_by_name(self.password_textbox_name).send_keys(pwd)

    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()



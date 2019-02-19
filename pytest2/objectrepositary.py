from selenium import webdriver
from selenium.webdriver.support.select import Select
import HtmlTestRunner
class user_registration():


    #global driver
    def __init__(self,driver):
        self.driver=driver
        self.gender_radio_name='gender'
        self.firstname_editbox_name='firstname'
        self.lastname_editbox_name='lastname'
        self.dateofbirth_editbox_name='dob'
        self.email_editbox_name='email_address'
        self.company_name_editbox_name='company'
        self.street_address_editbox_name='street_address'
        self.suburb_editbox_name='suburb'
        self.postalcode_editbox_name='postcode'
        self.city_editbox_name='city'
        self.state_editbox_name='state'
        self.country_select_box_name='country'
        self.telephone_editbox_name='telephone'
        self.fax_editbox_name='fax'
        self.newsletter_checkbox_name='newsletter'
        self.passowrd_editbox_name='password'
        self.confirm_password_editbox_name='confirmation'
        self.submit_button_id='tdb4'

    def gender_selection(self):
        #self.driver.find_element_by_name(self.gender_radio_name).clear()
        self.driver.find_element_by_name(self.gender_radio_name).click()

    def firstname_enter(self, fname):
        self.driver.find_element_by_name(self.firstname_editbox_name).clear()
        self.driver.find_element_by_name(self.firstname_editbox_name).send_keys(fname)

    def lastname_enter(self, lname):
        self.driver.find_element_by_name(self.lastname_editbox_name).clear()
        self.driver.find_element_by_name(self.lastname_editbox_name).send_keys(lname)

    def dateofbirth_enter(self, dob):
        self.driver.find_element_by_name(self.dateofbirth_editbox_name).clear()
        self.driver.find_element_by_name(self.dateofbirth_editbox_name).send_keys(dob)

    def email_enter(self, email):
        self.driver.find_element_by_name(self.email_editbox_name).clear()
        self.driver.find_element_by_name(self.email_editbox_name).send_keys(email)

    def company_enter(self,company):
        self.driver.find_element_by_name(self.company_name_editbox_name).clear()
        self.driver.find_element_by_name(self.company_name_editbox_name).send_keys(company)

    def street_address_enter(self,street):
        self.driver.find_element_by_name(self.street_address_editbox_name).clear()
        self.driver.find_element_by_name(self.street_address_editbox_name).send_keys(street)

    def suburb_enter(self,suburb):
        self.driver.find_element_by_name(self.suburb_editbox_name).clear()
        self.driver.find_element_by_name(self.suburb_editbox_name).send_keys(suburb)

    def postalcode_enter(self, post):
        self.driver.find_element_by_name(self.postalcode_editbox_name).clear()
        self.driver.find_element_by_name(self.postalcode_editbox_name).send_keys(post)

    def city_enter(self, city1):
        self.driver.find_element_by_name(self.city_editbox_name).clear()
        self.driver.find_element_by_name(self.city_editbox_name).send_keys(city1)

    def state_enter(self, state):
        self.driver.find_element_by_name(self.state_editbox_name).clear()
        self.driver.find_element_by_name(self.state_editbox_name).send_keys(state)

    def country_select(self, country):
        #self.driver.find_element_by_name(self.country_select_box_name).clear()
        count = Select(self.driver.find_element_by_name(self.country_select_box_name))
        count.select_by_visible_text(country)

    def telephone_enter(self, telephone):
        self.driver.find_element_by_name(self.telephone_editbox_name).clear()
        self.driver.find_element_by_name(self.telephone_editbox_name).send_keys(telephone)

    def fax_enter(self, fax):
        self.driver.find_element_by_name(self.fax_editbox_name).clear()
        self.driver.find_element_by_name(self.fax_editbox_name).send_keys(fax)

    def newsletter_selection(self):
        self.driver.find_element_by_name(self.newsletter_checkbox_name).click()

    def password_enter(self, password):
        self.driver.find_element_by_name(self.passowrd_editbox_name).clear()
        self.driver.find_element_by_name(self.passowrd_editbox_name).send_keys(password)

    def confirmpassword_enter(self, confirm):
        self.driver.find_element_by_name(self.confirm_password_editbox_name).clear()
        self.driver.find_element_by_name(self.confirm_password_editbox_name).send_keys(confirm)

    def submit_click(self):
        self.driver.find_element_by_id(self.submit_button_id).click()





__author__ = 'AMMA'

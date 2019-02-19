import time

from selenium import webdriver
import pytest

from pytest2.utils import utils as utils
#from pytest2.utills.utils import utils as utils
from pytest2.objectrepositary import user_registration



@pytest.mark.usefixtures('setup')
class Test_user_creation():


    # @pytest.fixture()
    # def test_setup(self):
    #     global driver
    #     driver=webdriver.Chrome(executable_path='C:/Users/satheesh/PycharmProjects/Selenium/chromedriver.exe')
    #     driver.maximize_window()
    #     yield
    #     driver.close()
    #     driver.quit()

    # def test_run(self,test_setup):
    #     driver.get('http://gcrit.com/build3')

    def test_creation(self):
        driver=self.driver
        driver.get(utils.URL)
        driver.find_element_by_link_text('create an account').click()
        creation=user_registration(driver)
        time.sleep(4)
        creation.gender_selection()
        creation.firstname_enter('DUSA')
        creation.lastname_enter('SATHEESH')
        creation.dateofbirth_enter('07/29/1987')
        creation.email_enter(utils.USERNAME)
        creation.company_enter('Student')
        creation.street_address_enter('Ramnagar')
        creation.suburb_enter('cpd')
        creation.postalcode_enter('505001')
        creation.city_enter('karimnagar')
        creation.state_enter('Telanganana')
        creation.country_select('India')
        creation.telephone_enter('9989858000')
        creation.fax_enter('9989858000')
        creation.newsletter_selection()
        creation.password_enter(utils.PASSWORD)
        creation.confirmpassword_enter('satee@1432')
        creation.submit_click()
        time.sleep(4)
        if 'Your Account Has Been Created!' in  driver.find_element_by_xpath('//*[@id="bodyContent"]/h1').text :
            print('USER LOGIN SUCESSFULL')
        else:
            print('User Creation Failed')







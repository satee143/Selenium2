from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
import time

# Browser Intilalization
driver=webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
driver.maximize_window()

#Launching GCR Shop admin webpage
driver.get('http://www.gcrit.com/build3/index.php')
driver.find_element_by_link_text('login').click()

#Login into the Admin interface
driver.find_element_by_name('email_address').send_keys('satee143@gmail.com')
driver.find_element_by_name('password').send_keys('satee@142')
driver.find_element_by_id('tdb5').click()
try:
    message=driver.find_element_by_link_text('Log Off').is_displayed()
    print('Login sucessfull')
except NoSuchElementException as exception:
    message=driver.find_element_by_xpath('//*[@id="bodyContent"]/table/tbody/tr/td').text
    if 'Not match for E-Mail Address' in message:
        print('error retrived')
    else:
        print('Failed')
driver.close()
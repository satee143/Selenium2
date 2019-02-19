from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
driver.maximize_window()

# Navigate to URL
driver.get('http://gcrit.com/build3/')
time.sleep(2)

# Click on Login Page
driver.find_element_by_link_text('login').click()
driver.find_element_by_name('email_address').send_keys('satee143@gmail.com')
driver.find_element_by_name('password').send_keys('satee@142')
driver.find_element_by_xpath('//*[@id="tdb5"]/span[2]').click()

#CHecking the validation

try:
    result = driver.find_element_by_link_text('Log Off').is_displayed()
    print('Customer Login is Sucessfull -- Passed')

except: #NoSuchElementException as exception:
    print('Customer Login is Not sucessfull -- Failed')
driver.close()


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
import time

# Browser Intilalization
driver=webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
driver.maximize_window()

#Launching GCR Shop admin webpage
driver.get('http://www.gcrit.com/build3/admin')

#Login into the Admin interface
driver.find_element_by_name('username').send_keys('admin')
driver.find_element_by_name('password').send_keys('admin@123')
driver.find_element_by_id('tdb1').click()
time.sleep(4)
url=driver.current_url
# IF it sucesss Login
if 'http://www.gcrit.com/build3/admin/index.php' in url:
    print('User Login sucessfull')

# it is Unlogin with error message validation
elif 'Innvalid' in driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td').text:
    print('Login failed error message --Passed')

# it is Unlogin with error message validation
else:
    print('Login Failed error message --Failed')

driver.close()
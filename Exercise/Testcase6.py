from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
#ACCOUNT CREATION AND CAPTCHA ENTER
#Driver Intilaization

driver=webdriver.Firefox(executable_path='../drivers/geckodriver.exe')
driver.maximize_window()


#URL loading
driver.get('https://www.gcreddy.com')
driver.find_element_by_link_text('Software Testing Forum').click()
driver.find_element_by_link_text('Register').click()

#Account Creation
driver.find_element_by_name('agreed').click()
username=driver.find_element_by_name('username')
username.send_keys('satee148')

email=driver.find_element_by_name('email')
email.send_keys('satee148@gmail.com')

password=driver.find_element_by_id('new_password')
password.send_keys('satee@1432')

cnfpassword=driver.find_element_by_id('password_confirm')
cnfpassword.send_keys('satee@1432')
captcha=input('Enter the Captcha from the page')
driver.find_element_by_id('confirm_code').send_keys(captcha)

#Button submission

driver.find_element_by_id('submit').click()

confirmation=driver.find_element_by_css_selector('#message > div > p').text
print(confirmation)

if 'Your' in confirmation:
    print('User Registration is sucessfull -- passed')
else:
    print('User registration is un sucessfull -- Fail')

driver.close()


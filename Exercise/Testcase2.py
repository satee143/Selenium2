from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
driver= webdriver.Firefox(executable_path='../drivers/geckodriver.exe')
driver.get('http://google.com')
element='yahoo'
# link1=driver.find_element_by_link_text('yahoo')
# Result = link1.is_displayed()
#Postive Tesing
# if Result is True:
#     print('Gmail Link found --Pass')
# else:
#     print('Gmail link not found -- Fail')
# #Exception Handling
try:
    driver.find_element_by_link_text('yahoo').is_displayed()
    print('Found')
except NoSuchElementException as exception:
    print(element,'-link is not avalible in google home page: Failed')
driver.close()

#Negative Testing
# if Result is not True:
#     print("Link is avalible in Google page: Passed")
# else:
#     print('Gmail link is not avalible in google home page: Failed')
# driver.close()

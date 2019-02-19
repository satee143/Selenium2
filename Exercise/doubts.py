from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
driver=webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
driver.get('https://google.com')
try:
    driver.find_element_by_link_text('yahoo').is_displayed()
    print('Found')
except NoSuchElementException as exception:
    print('element not found')

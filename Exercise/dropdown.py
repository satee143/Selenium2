from typing import List

from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Chrome(executable_path='C:/Users/satheesh/PycharmProjects/Selenium/drivers/chromedriver.exe')
driver.get('http://www.gcrit.com/build3/create_account.php')
country=driver.find_element_by_name('country')
a= Select(country)
#a.select_by_index(2)
a.select_by_visible_text('India')
l=driver.find_elements_by_name('country')
print(l)
m=len(l)
print(m)
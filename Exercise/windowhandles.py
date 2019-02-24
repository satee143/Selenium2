__author__ = 'AMMA'
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest


driver=webdriver.Chrome(executable_path='C:/Users/satheesh/PycharmProjects/Selenium/drivers/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://learn.letskodeit.com/p/practice')
print(driver.current_window_handle)
driver.find_element(By.ID,'openwindow').click()
print(driver.current_window_handle)
path='C:/Users/satheesh/PycharmProjects/Selenium/drivers/'+str(round(time.time()*1000))+'.png'
driver.save_screenshot(path)
print('Windows Handles are')
for handle in driver.window_handles:

    if handle not in driver.current_window_handle:
        break
driver.switch_to.window(handle)

driver.find_element_by_id('search-courses').send_keys('Hello Python')

import time

from selenium import webdriver

driver= webdriver.Ie(executable_path='../Exercise/drivers/IEDriverServer.exe')
driver.maximize_window()
driver.get('http://tg.meeseva.gov.in/')
driver.find_element_by_name('UserId').send_keys('123456')

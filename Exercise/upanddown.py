import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Firefox(executable_path='../drivers/geckodriver.exe')
driver.maximize_window()
driver.get('https://en.wikipedia.org/wiki/Main_Page')
elm = driver.find_element_by_tag_name('html')
elm.send_keys(Keys.END)
time.sleep(5)
elm.send_keys(Keys.HOME)

__author__ = 'AMMA'
from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path='C:/Users/satheesh/PycharmProjects/Selenium/chromedriver.exe')
driver.maximize_window()
driver.get('https://www.toolsqa.com/handling-alerts-using-selenium-webdriver/')
driver.find_element_by_id('button1').click()
driver.window_handles
driver.switch_to_window()
print(driver.switch_to.alert.text)
#driver.switch_to.alert.accept()
print()
time.sleep(8)
driver.quit()
from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
driver.get('https://mail.rediff.com/cgi-bin/login.cgi')

driver.find_element_by_name('proceed').click()
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()
#print(popup.text)
driver.find_element_by_id('login1').send_keys('satee143')
driver.find_element_by_id('password').send_keys('dusa143')
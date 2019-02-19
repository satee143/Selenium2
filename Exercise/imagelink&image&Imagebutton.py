from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
driver.get('http://google.com')
google=driver.find_element_by_id('hplogo')
print(google.get_attribute('title'))
driver.get('http://newtours.demoaut.com/')
driver.find_element_by_name('login').click()
driver.get('https://www.seleniumhq.org/')
driver.find_element_by_xpath('//*[@id="choice"]/tbody/tr/td[2]/center/a/img').click()



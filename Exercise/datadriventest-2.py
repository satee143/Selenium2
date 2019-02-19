__author__ = 'AMMA'
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

f=open('../drivers/abc.txt','r')
d=[]
n=0
for line in f:
    d=line.split()
    n=n+1
    driver=webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
    driver.maximize_window()
    driver.get('http://www.gcrit.com/build3/admin/login.php')
    time.sleep(2)
    driver.find_element_by_name('username').send_keys(d[0])
    driver.find_element_by_name('password').send_keys(d[1])
    driver.find_element_by_id('tdb1').click()
    error=driver.find_element_by_xpath('/html/body/table[1]/tbody/tr/td').text
    if 'The maximum number of login attempts has been reached. Please try again in 5 minutes' in error:
        print(n,'Retrived Correct path=-- Passed')
    else:
        print(n,'Retrived message is invalid---Fail')
    driver.close()


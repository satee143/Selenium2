__author__ = 'AMMA'
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
n=0
f=open('../drivers/abc.txt',"r")
d=[]
for line in f:
    d=line.split()
    driver=webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
    driver.maximize_window()
    driver.get('http://www.gcrit.com/build3/admin/')
    driver.find_element_by_name('username').send_keys(d[0])
    driver.find_element_by_name('password').send_keys(d[1])
    driver.find_element_by_id('tdb1').click()
    url=driver.current_url
    n=n+1
    if 'http://www.gcrit.com/build3/admin/index.php' in url :
        print(n,'Admin Login is Sucessfull---Passed')
    else:
        print(n,'Admin Login is Un Sucessfull -- Failed')
    driver.close()



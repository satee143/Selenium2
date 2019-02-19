__author__ = 'AMMA'
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

for browser in range(1,4):
    if browser == 1:
        driver=webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
        driver.get('https://google.com')
        browser="Google Chrome"

    elif browser == 2:
        driver=webdriver.Firefox(executable_path='../drivers/geckodriver.exe')
        driver.get('https://google.com')
        browser="Mozilla Firefox"


    elif browser == 3:
        driver=webdriver.Ie(executable_path='../drivers/IEDriverServer.exe')
        driver.get('http://google.com')
        browser="Internet Explorer"
    title=driver.title
    if 'Google' in title:
        print(browser,'Google Application Launched--Passed')
    else:
        print(browser,"Google Application Launch Failed")
    driver.quit()




from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
import time,openpyxl

wk=openpyxl.load_workbook('C:/Users\satheesh/PycharmProjects/Selenium/abcd.xlsx')
ws=wk['Sheet1']
rows=ws.max_row
column=ws.max_column
n=1
d=[]
for i in range(1,rows+1):
    d.clear()

    for j in range(1,column+1):

        d.append(ws.cell(i,j).value)
    driver=webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
    driver.maximize_window()
    driver.get('http://www.gcrit.com/build3/admin/')
    driver.find_element_by_name('username').send_keys(d[0])
    driver.find_element_by_name('password').send_keys(d[1])
    driver.find_element_by_id('tdb1').click()
    url=driver.current_url

    if 'http://www.gcrit.com/build3/admin/index.php' in url :
        print(n,'Admin Login is Sucessfull---Passed')
    else:
        print(n,'Admin Login is Un Sucessfull -- Failed')
    n=n+1
    driver.close()

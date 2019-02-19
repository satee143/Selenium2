from selenium import webdriver
import time

#Browser Intiallization
driver=webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
driver.maximize_window()

#Login website
driver.get('http://www.gcrit.com/build3/admin')
url1=driver.current_url
print(url1)

#CLick on user Interface Login
driver.find_element_by_link_text('Online Catalog').click()
url2=driver.current_url
print(url2)

if 'http://www.gcrit.com/build3/' in url2:
    print('Application Redirected from admin to user -- Pass')
else:
    print()
    print('Application Not Redirected from admin to user -- Fail')
time.sleep(3)
if 'http://www.gcrit.com/build3/admin' in url1:
    print('URL MATHCHES')
else:
    print('URL mismatch')
driver.close()
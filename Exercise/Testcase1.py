from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
driver.maximize_window()
driver.get('https://en.wikipedia.org/wiki/Selenium_(software)')
driver.find_element_by_link_text('Create account').click()
time.sleep(3)
#POSTIVE TESTING
# url1=driver.current_url
# if 'wikipedia.org' in url1:
#     print('1st verification Result :'+ 'It is an internal link - Passed')
# else:
#     print('1st verification Result :'+ 'It is not an internal link - Failed')
# driver.back()
# time.sleep(2)
# driver.find_element_by_partial_link_text('www.seleniumhq').click()
# time.sleep(3)
# url2=driver.current_url
# if 'wikipedia.org' not in url2:
#     print('2nd Verification Point:'+ 'It is an outgoing link -- Passed')
# else:
#     print('2nnd verification Result: '+'It is not an outgoing link -- Failed')
# driver.close()



#Negative Testing
url1=driver.current_url
if 'wikipedia.org' not in url1:
    print('1st verification Result :''It is not an internal link - Failed')
else:
    print('1st verification Result :'+ 'It is  an internal link - Passed')
driver.back()
time.sleep(2)
driver.find_element_by_partial_link_text('www.seleniumhq').click()
time.sleep(3)
url2=driver.current_url
if 'wikipedia.org'  in url2:
    print('2nd Verification Point:'+'It is not an outgoing link -- Failed')
else:
    print('2nnd verification Result:'+'It is  an outgoing link -- passed')
driver.close()
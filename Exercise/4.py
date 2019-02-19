import time

from selenium import webdriver

driver= webdriver.Chrome(executable_path='../Exercise/drivers/chromedriver.exe')
driver.get('http://www.gmail.com')
aa = driver.find_element_by_id('identifierId')
aa.send_keys('dusa.skumar@gmail.com')
time.sleep(3)
aa.clear()
#driver.find_element_by_id('identifierId').clear()
ds2=driver.find_element_by_xpath('//*[@id="identifierNext"]/content/span').click()
ds=driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/content/section/div/content/div[1]/div/div[2]/div[2]/div')
print(ds.text)
if( ds.text == 'Enter an email or phone number'):
    print("suceed")
else:
    print('fail')


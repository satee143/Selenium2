from selenium import webdriver
driver=webdriver.Chrome(executable_path='../Exercise/drivers/chromedriver.exe')
driver.get('http://www.gcrit.com/build3')
#a = driver.find_element_by_partial_link_text('Gma').click()

driver.find_element_by_xpath('//*[@id="bodyContent"]/div/div[1]/a[2]/u').click()
print(driver.find_element_by_xpath('//*[@id="bodyContent"]/form/div/div[2]/table/tbody/tr[1]/td[2]/input[1]').is_selected())
driver.find_element_by_xpath('//*[@id="bodyContent"]/form/div/div[2]/table/tbody/tr[1]/td[2]/input[2]').click()
print(driver.find_element_by_xpath('//*[@id="bodyContent"]/form/div/div[2]/table/tbody/tr[1]/td[2]/input[1]').is_selected())
print(driver.find_element_by_xpath('//*[@id="bodyContent"]/form/div/div[2]/table/tbody/tr[1]/td[2]/input[2]').is_selected())

#print(a.is_displayed())
#print(a.is_enabled())
driver.quit()
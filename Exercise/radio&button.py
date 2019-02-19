from selenium import webdriver

import time

driver=webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
driver.fullscreen_window()
driver.get('http://www.gcrit.com/build3/create_account.php')
radio = driver.find_element_by_name('gender')
print('Radio button displayed status:',radio.is_displayed())
print('Radio button enabled status:',radio.is_enabled())
print('Male Radio button Selected status :',radio.is_selected())
print('Female radio button is selected or not :',driver.find_element_by_xpath('//*[@id="bodyContent"]/form/div/div[2]/table/tbody/tr[1]/td[2]/input[2]').is_selected())
time.sleep(3)
radio.click()
print('Male Radio button Selected status :',radio.is_selected())

button=driver.find_element_by_css_selector('#tdb4 > span.ui-button-text')
print(button.is_displayed())
print(button.is_enabled())
button.click()
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()
print(button.is_selected())  # If we perform selected operation on except radio button and check box its always shows FALSE

driver.find_element_by_name('newsletter').click()
time.sleep(4)
driver.close()
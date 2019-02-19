from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
driver.get('http://www.gcrit.com/build3/create_account.php')
newsletter =driver.find_element_by_name('newsletter')
#Check box is Displayed or Not
print(newsletter.is_displayed())
#Check box is enabled or Not
print(newsletter.is_enabled())
#Check box is Selected or Not
print(newsletter.is_selected())
time.sleep(3)
newsletter.click()
print(newsletter.is_selected())
time.sleep(2)
driver.quit()
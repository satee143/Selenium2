from selenium import webdriver
import time
#Enable Browser
driver=webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
#Browser Maxmize
driver.maximize_window()
#Getting Webpage
driver.get("https://google.com")
#Checking Gmail link Displayed or not
webelement= driver.find_element_by_link_text('Gmail')
print(webelement.is_displayed())
#Checking Gmail Link is Enabled or Not
print(webelement.is_enabled())
#Getting the Link Name
print(webelement.text)
time.sleep(4)
#Redirects to Gmail link
webelement.click()
#close Broswer
driver.quit()


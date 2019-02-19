import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox(executable_path='../Exercise/drivers/geckodriver.exe')
#driver.set_page_load_timeout(20)
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("284346")
#driver.find_element_by_id("txtPassword").send_keys("satee@143")
driver.find_element_by_name("btnK").click()
time.sleep(10)
driver.close()
driver.quit()
print('Test Completed')
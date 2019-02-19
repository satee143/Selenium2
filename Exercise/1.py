import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="../Exercise/drivers/chromedriver.exe")
driver.maximize_window()
a = driver.get('http://tg.meeseva.gov.in/')

time.sleep(3)
driver.refresh()
print(driver.title)
print(driver.current_url)
driver.find_element_by_partial_link_text("Unlock").click()
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()

time.sleep(3)

driver.close()
time.sleep(3)
driver.quit()

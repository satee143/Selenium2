import time
from selenium  import webdriver
driver=webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
driver.get('http://www.gcrit.com/build3/')
driver.find_element_by_partial_link_text('create').click()
enabled=driver.find_element_by_xpath('//*[@id="tdb4"]/span[2]')
enabled1=driver.find_element_by_name('newsletter')
ena5=enabled.is_selected()
ena1=enabled1.is_selected()
ena2=enabled.is_displayed()
ena3=enabled.is_enabled()
print('button Displayed=',ena2)
print('button=',ena3)
print('newsletter is selected',ena1)
driver.minimize_window()
time.sleep(3)
driver.maximize_window()
time.sleep(3)
driver.fullscreen_window()
time.sleep(3)
enabled1.click()
ena4=enabled1.is_selected()
print('newsletter is selected',ena4)
print('button is enabled',ena5)
print(driver.window_handles)
print(driver.page_source)
driver.quit()
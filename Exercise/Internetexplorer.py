from selenium import webdriver
path="../Exercise/IEDriverServer.exe"
driver=webdriver.Ie(executable_path=path)
driver.get('https://google.com')
driver.find_element_by_id('q').send_keys('Hello')
driver.find_element_by_name('btnK').click()

driver.close()
driver.quit()

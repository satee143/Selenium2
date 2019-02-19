from selenium import webdriver
driver=webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
driver.get('https://seleniumhq.github.io/selenium/docs/api/java/index.html')
driver.switch_to.frame('classFrame')
a=driver.find_element_by_link_text('org.openqa.selenium.edge')
a.click()
print(driver.title)

driver.switch_to.default_content()
driver.switch_to.frame(0)
driver.find_element_by_link_text('org.openqa.selenium.remote.http').click()
print(driver.title)
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
driver.maximize_window()

# Navigate to GCRSHOP webpage
driver.get('http://gcrit.com/build3/')
time.sleep(3)

#Click on Create account
driver.find_element_by_xpath('//*[@id="bodyContent"]/div/div[1]/a[2]/u').click()

# Account Details Enter

# Gender Selection for Male
gender= driver.find_element_by_name('gender')
gender.click()

# Entering First Name
fname=driver.find_element_by_name('firstname')
fname.send_keys('satheesh')

# Entering Last Name
lname=driver.find_element_by_name('lastname')
lname.send_keys('doosa')

#Entering Date of Birth in mm/dd/yyyy format
dob=driver.find_element_by_id('dob')
dob.send_keys('01/20/1988')

#Entering email with valid mail format
email=driver.find_element_by_name('email_address')
email.send_keys('satee1s43@gmail.com')

#Entering street address
street=driver.find_element_by_name('street_address')
street.send_keys('ramnagar')

#Entering Postal code
postcode=driver.find_element_by_name('postcode')
postcode.send_keys('505415')

#Entering City Name
city=driver.find_element_by_name('city')
city.send_keys('karimnagar')

#Enering State
state=driver.find_element_by_name('state')
state.send_keys('telangana')

#Selecting country from the dropdown list
# country=driver.find_element_by_name('country')
# country1=Select(country)
# country1.select_by_visible_text('India')
Select(driver.find_element_by_name('country')).select_by_visible_text('India')

#Entering Telephone Number
telephone=driver.find_element_by_name('telephone')
telephone.send_keys('9989884111')

#Entering Password
password=driver.find_element_by_name('password')
password.send_keys('satee@1432')

#Confirm Password entering
confirmpwd=driver.find_element_by_name('confirmation')
confirmpwd.send_keys('satee@1432')


#Submiting the button
time.sleep(4)
submit=driver.find_element_by_xpath('//*[@id="tdb4"]/span[2]')
submit.click()

#Message
message=driver.find_element_by_xpath('//*[@id="bodyContent"]/h1').text

if message=='Your Account Has Been Created!':
    print('Account Creation sucessfull')

else:
    print("Account Creation Failed")

time.sleep(3)
driver.close()







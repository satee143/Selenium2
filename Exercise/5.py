import unittest
from selenium import webdriver


#class logintest(unittest.TestCase):
  #  def setUp(self):

      #  self.driver = webdriver.Firefox()


#def test_filldetails(self):
   # driver = self.driver

driver= webdriver.Chrome(executable_path='../Exercise/drivers/chromedriver.exe')
driver.maximize_window()
driver.get('http://localhost:63342/myFirstTest/multipleclass.html')

driver.implicitly_wait(30)
element1= driver.find_element_by_css_selector("label.class-name1")
string1=str(element1.text)
print(string1.strip())


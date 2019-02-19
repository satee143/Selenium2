from selenium import webdriver
import unittest


class batch_test(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     cls.driver=webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
    #     cls.driver.maximize_window()
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_automationstepbystep(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Doosa")
        self.driver.find_element_by_name("btnK").click()

    # def admin_login(self):
    #     self.driver.get('https://www.google.com/')
    #     self.driver.find_element_by_name('q').send_keys('dusa143')
    #     #self.driver.find_element_by_name('password').send_keys(pwd)
    #     self.driver.find_element_by_name('btnK').click()

    def admin_login2(self):
        self.driver.get('http://www.google.com/')
        self.driver.find_element_by_name('q').send_keys('satee143')
        #self.driver.find_element_by_name('password').send_keys(pwd)
        self.driver.find_element_by_name('btnK').click()


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test completed')

if __name__ == '__main__':
     unittest.main()

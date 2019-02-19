from selenium import webdriver
import unittest


class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_search_automationstepbystep(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Automation Step by Step")
        self.driver.find_element_by_name("btnK").click()

    def test_search_raghav(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("gmail")
        self.driver.find_element_by_name("btnK").click()

    @classmethod
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main()
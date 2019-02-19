import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os,time,sys
#Browser open and close Each Test Method execution
import pytest

class TestCase():
    @pytest.fixture
    def test_setUp(self):
        self.driver=webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
        self.driver.maximize_window()
        yield
        self.driver.quit()


    def test_VerifyGcrTitle(self,test_setUp):
        self.driver.get('https://gcrit.com/build3/admin')
        #self.assertEqual('GCR Shop',self.driver.title)

    def test_VerifyGoogleTitle(self,test_setUp):
        self.driver.get('https://google.com')
        assert 'https://www.google.com/' == self.driver.current_url
    

    def test_VerifyYahooTitle(self,test_setUp):
        self.driver.get('https://in.yahoo.com')
        #self.assertEqual('Yahoo',self.driver.title)
    

import unittest
from selenium import webdriver
from Utility.ReadTestData import jsonFiledata
class loginpage1:


    def __init__(self,driver):
         self.driver = driver

    def EnterCredential(self):
        ele = self.driver.find_element_by_xpath("//input[@name='userName']").text
        assert ele in self.driver.page_source
        self.driver.save_screenshot("screenshot.png")
        self.driver.find_element_by_xpath("//input[@name='userName']").send_keys(jsonFiledata().testdata("LoginPage", "Username"))
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(jsonFiledata().testdata("LoginPage", "Password"))
        self.driver.find_element_by_xpath("//input[@name='login']").click()


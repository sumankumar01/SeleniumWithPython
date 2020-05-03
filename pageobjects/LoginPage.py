import unittest


class loginpage1:


    def __init__(self,driver):
         self.driver = driver

    def EnterCredential(self):
        ele = self.driver.find_element_by_xpath("//input[@name='userName']").text
        assert ele in self.driver.page_source
        self.driver.find_element_by_xpath("//input[@name='userName']").send_keys("mercury")
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys("mercury")
        self.driver.find_element_by_xpath("//input[@name='login']").click()


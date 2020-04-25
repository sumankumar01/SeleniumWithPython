import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Hpflight(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.newtours.demoaut.com/")

    def login(self):
        driver=self.driver
        ele=driver.find_element_by_xpath("//input[@name='userName']").text
        assert ele in driver.page_source
        driver.find_element_by_xpath("//input[@name='userName']").send_keys("mercury")
        driver.find_element_by_xpath("//input[@name='password']").send_keys("mercury")
        driver.find_element_by_xpath("//input[@name='login']").click()

        ele = driver.find_element_by_xpath("//select[@name='airline']//option[1]").text

        # if ele == "Blue Skies Airlines":
        #     assertTrue(True, "not the correct page")
        # else:
        #     assertTrue(False, "Not authorized")

        assert ele in driver.page_source

    def tearDown(self):
        driver=self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()
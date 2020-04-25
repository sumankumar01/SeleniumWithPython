from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

#driver = webdriver.Chrome(executable_path=r"C:\Users\kumar\AppData\Local\Programs\Python\Python38-32\Scripts\chromedriver.exe")

driver=webdriver.Chrome()
driver.get("http://www.newtours.demoaut.com/")

assert "Welcome: Mercury Tours" in driver.title

driver.find_element_by_xpath("//input[@name='userName']").send_keys("mercury")
driver.find_element_by_xpath("//input[@name='password']").send_keys("mercury")
driver.find_element_by_xpath("//input[@name='login']").click()

ele=driver.find_element_by_xpath("//select[@name='airline']//option[1]").text

# if ele == "Blue Skies Airlines":
#     assertTrue(True, "not the correct page")
# else:
#     assertTrue(False, "Not authorized")

assert ele in driver.page_source

driver.close()

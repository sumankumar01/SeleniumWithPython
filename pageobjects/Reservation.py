from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Utility.ReadTestData import jsonFiledata

class reservationPage:

    def __init__(self, driver):
        self.driver = driver
        self.passangercount_select_name="passCount"
        self.departingFrom_select_name="fromPort"
        self.departingFrom_Month_select_name = "fromMonth"
        self.departingFrom_Day_select_name = "fromDay"
        self.arrvingIn_select_name = "toPort"
        self.arrvingIn_Month_select_name = "toMonth"
        self.arrvingIn_Day_select_name = "toDay"
        self.airline_select_name = "airline"
        self.continue_button_name = "findFlights"

    def flightDetails(self):
        #self.driver.find_element_by_name(self.passanger_select_name)
        select = Select(self.driver.find_element_by_name(self.passangercount_select_name))
        select.select_by_index(2)

        select = Select(self.driver.find_element_by_name(self.departingFrom_select_name))
        #value=jsonFiledata().testdata("Reservation", "departingFrom_select_name")
        select.select_by_value(jsonFiledata().testdata("Reservation", "departingFrom_select_name"))
        #select.select_by_visible_text("Frankfurt")

        select = Select(self.driver.find_element_by_name(self.departingFrom_Month_select_name))
        select.select_by_index(5)

        select = Select(self.driver.find_element_by_name(self.departingFrom_Day_select_name))
        select.select_by_index(10)


        select = Select(self.driver.find_element_by_name(self.arrvingIn_select_name))
        select.select_by_index(3)
        select = Select(self.driver.find_element_by_name(self.arrvingIn_Month_select_name))
        select.select_by_index(5)
        select = Select(self.driver.find_element_by_name(self.arrvingIn_Day_select_name))
        select.select_by_index(10)

        select = Select(self.driver.find_element_by_name(self.airline_select_name))
        select.select_by_index(3)
        self.driver.save_screenshot("screenshot.png")
        self.driver.find_element_by_name(self.continue_button_name).click()
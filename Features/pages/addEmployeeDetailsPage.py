import time

from selenium.webdriver.common.by import By

from Features.pages.BasePage import BasePage


class AddEmployeeDetails(BasePage):

    def __int__(self, driver):
        super().__init__(driver)

    EmployeeListClickButton_xpath = "//a[normalize-space()='Employee List']"
    AddEmployeeButton_xpath = "//i[normalize-space()='add']"
    first_name_id = "first-name-box"
    last_name_id = "last-name-box"
    user_name_id = "username"
    user_pass_id = "password"
    user_conf_pass_id = "confirmPassword"
    click_on_location_button_xpath = "//button[@class='btn']"
    click_on_location_xpath = "//a[@id='bs-select-2-7']"
    click_on_next_step_id = "modal-save-button"
    date_of_id = "emp_birthday"
    marital_status_xpath = "(//input[@value='-- Select --'])[1]"
    click_next_step_xpath = "//button[normalize-space()='Next']"
    click_on_region_xpath = "(//i[contains(text(),'arrow_drop_down')])[8]"
    selected_region_xpath = "//a[@id='bs-select-12-1']"
    click_on_FTE_xpath = "(//i[contains(text(),'arrow_drop_down')])[9]"
    selected_FTE_xpath = "//a[@id='bs-select-13-3']"
    click_on_tempDept_xpath = "(//i[contains(text(),'arrow_drop_down')])[10]"
    selected_tempDept_xpath = "//a[@id='bs-select-14-1']"
    final_save_botton_xpath = "//button[normalize-space()='Save']"


    def clickOnEmployeeList(self):
        self.click_on_element("EmployeeListClickButton_xpath", self.EmployeeListClickButton_xpath)

    def click_on_add_botton(self):
        self.click_on_element("AddEmployeeButton_xpath", self.AddEmployeeButton_xpath)

    def Add_employee_details(self):
        self.type_into_element("first_name_id", self.first_name_id, "anjan")
        self.type_into_element("last_name_id", self.last_name_id, "ls")
        # time.sleep(5)

    def enter_user_name_And_pass(self):
        self.type_into_element("user_name_id", self.user_name_id, "anjanls")
        self.type_into_element("user_pass_id", self.user_pass_id, "anjanls25")
        self.type_into_element("user_conf_pass_id", self.user_conf_pass_id, "anjanls25")

    def click_on_location(self):
        self.click_on_element("click_on_location_button_xpath", self.click_on_location_button_xpath)
        self.click_on_element("click_on_location_xpath", self.click_on_location_xpath)

    def click_on_next_step(self):
        self.click_on_element("click_on_next_step_id", self.click_on_next_step_id)

    def date_of_birth(self):
        self.type_into_element("date_of_id", self.date_of_id, "Mon, 18 Sep 1998")

    def marital_status(self):
        self.get_elements("marital_status_xpath", self.marital_status_xpath)

    def final_click(self):
        self.click_on_element("click_next_step_xpath", self.click_next_step_xpath)

    def save_button(self):
        self.click_on_element("click_next_step_xpath", self.click_next_step_xpath)

    def click_on_regions(self):
        self.click_on_element("click_on_region_xpath",self.click_on_region_xpath)


    def click_on_selected_region(self):
        self.click_on_element("selected_region_xpath", self.selected_region_xpath)

    def click_on_FTE(self):
        self.click_on_element("click_on_FTE_xpath",self.click_on_FTE_xpath)

    def selected_FTE(self):
        self.click_on_element("selected_FTE_xpath", self.selected_FTE_xpath)

    def click_on_tempDept(self):
        self.click_on_element("click_on_tempDept_xpath",self.click_on_tempDept_xpath)

    def selected_tempDept(self):
        self.click_on_element("selected_tempDept_xpath", self.selected_tempDept_xpath)

    def final_save_botton(self):
        self.click_on_element("final_save_botton_xpath",self.final_save_botton_xpath)

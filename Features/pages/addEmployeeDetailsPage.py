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

    def clickOnEmployeeList(self):
        self.click_on_element("EmployeeListClickButton_xpath", self.EmployeeListClickButton_xpath)

    def click_on_add_botton(self):
        self.click_on_element("AddEmployeeButton_xpath", self.AddEmployeeButton_xpath)

    def Add_employee_details(self):
        self.type_into_element("first_name_id", self.first_name_id, "pavan")
        self.type_into_element("last_name_id", self.last_name_id, "kolli")
        # time.sleep(5)

    def enter_user_name_And_pass(self):
        self.type_into_element("user_name_id", self.user_name_id, "Pavan123")
        self.type_into_element("user_pass_id", self.user_pass_id, "Pavan@123")
        self.type_into_element("user_conf_pass_id", self.user_conf_pass_id, "Pavan@123")

    def click_on_location(self):
        self.click_on_element("click_on_location_button_xpath", self.click_on_location_button_xpath)
        self.click_on_element("click_on_location_xpath", self.click_on_location_xpath)

    def click_on_next_step(self):
        self.click_on_element("click_on_next_step_id", self.click_on_next_step_id)

    def date_of_birth(self):
        self.type_into_element("date_of_id", self.date_of_id, "Mon, 04 Sep 2023")

    def marital_status(self):
        self.get_elements("marital_status_xpath", self.marital_status_xpath)

    def final_click(self):
        self.click_on_element("click_next_step_xpath", self.click_next_step_xpath)

    def save_button(self):
        self.click_on_element("click_next_step_xpath", self.click_next_step_xpath)

        # context.driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()
        # context.driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()

        # context.driver.find_element(By.ID, "first-name-box").send_keys("pavan")
        # context.driver.find_element(By.ID, "last-name-box").send_keys("kolli")
        # context.driver.find_element(By.XPATH, "//label[@for='hasLoginDetails']").click()
        # context.driver.find_element(By.XPATH, "//label[@for='autoGenerateEmployeeId']").click()
        # context.driver.find_element(By.XPATH, "//label[@for='hasLoginDetails']").click()
        # context.driver.find_element(By.XPATH, "(//input[@autocomplete='off'])[1]").send_keys("pavan123")
        # context.driver.find_element(By.XPATH, "(//input[@autocomplete='off'])[2]").send_keys("pavan@123")
        # context.driver.find_element(By.XPATH, "(//input[@autocomplete='off'])[3]").send_keys("pavan@123")
        # self.driver.find_element(By.XPATH, AddEmployeeDetails)
        # self.driver.find_element(By.ID, AddEmployeeDetails).click()

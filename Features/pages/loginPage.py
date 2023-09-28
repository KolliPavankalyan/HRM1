import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from Features.pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    admin_name_class_name = "txtUsername"
    admin_password_class_name = "txtPassword"
    login_button_xpath = "//button[normalize-space()='Login']"
    employee_list_xpath = "//a[normalize-space()='Employee List']"
    failure_msg_class_name = "toast-message"
    username = "Admin"
    userpassword = "XSdz9L@Mf7"

    def enter_validUser(self,username):
        self.type_into_element("admin_name_class_name",self.admin_name_class_name, username)

    def enter_validPAssward(self,userpassword):
        self.type_into_element("admin_password_class_name", self.admin_password_class_name, userpassword)

    def login_button(self):
        self.click_on_element("login_button_xpath", self.login_button_xpath)

    def check_creditinals_correctOrNot(self):
        self.contains("employee_list_xpath",self.employee_list_xpath, "Employee List")

    def enter_invalid_user(self):
        self.type_into_element("admin_name_class_name", self.admin_name_class_name,"admin124")

    def enter_invalid_password(self):
        self.type_into_element("admin_password_class_name", self.admin_password_class_name,"pabanknd")

    def without_enter_anyValues(self):
        self.type_into_element("admin_password_class_name", self.admin_password_class_name, "")
        self.type_into_element("admin_password_class_name", self.admin_password_class_name, "")

    # def failure_msg(self):
    #     self.contains("failure_msg_class_name", self.failure_msg_class_name, "Invalid Credentials")


# class LoginPage:
#     def __init__(self, driver):
#         self.driver = driver
#
#     admin_name_locater = "txtUsername"
#     admin_password_locater = "txtPassword"
#     login_button_Xpath = "//button[normalize-space()='Login']"
#
#     def valid_conditionals(self):
#         self.driver.find_element(By.NAME, "txtUsername").send_keys("Admin")
#         self.driver.find_element(By.NAME, "txtPassword").send_keys("blbF9@RZH4")
#
#     def login_button(self):
#         self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
#
#     def check_creditinals_correctOrNot(self):
#         dashboard = self.driver.find_element(By.XPATH, "//a[normalize-space()='Employee List']")
#         time.sleep(10)
#         assert dashboard.text.__eq__("Employee List")
#

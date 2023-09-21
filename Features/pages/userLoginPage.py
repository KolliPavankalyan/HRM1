from Features.pages.BasePage import BasePage


class UserLoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    admin_name_class_name = "txtUsername"
    admin_password_class_name = "txtPassword"
    login_button_xpath = "//button[normalize-space()='Login']"
    employee_list_xpath = "//a[normalize-space()='Employee List']"

    def enter_uservalidUserName(self):
        self.type_into_element("admin_name_class_name", self.admin_name_class_name, "sowjanya")

    def enter_uservalidPassward(self):
        self.type_into_element("admin_password_class_name", self.admin_password_class_name, "sowjanya25")

    def user_login_button(self):
        self.click_on_element("login_button_xpath", self.login_button_xpath)

    def user_login_success_or_not(self):
        self.contains("employee_list_xpath", self.employee_list_xpath, "Employee List")

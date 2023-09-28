from Features.pages.BasePage import BasePage


class LeavePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    click_on_leave_xpath = "(//span[contains(text(),'Leave')])[1]"
    start_date_of_leave_id = "leave.assign_fromDate"
    end_date_of_leave_id = "leave.assign_toDate"
    leave_comment_id = "leave.assign_comments"
    leave_apply_button_xpath = "//button[@type='submit']"
    final_ok_xpath = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-button-margin']"
    logout_xpath = "//span[normalize-space()='Log Out']"
    action_xpath = "//input[@value='Select Action']"
    approve_xpath  = "//span[normalize-space()='Approve']"
    action_save_xpath = "//button[normalize-space()='Save']"
    employee_myleave_page_xpath = "//a[@class='top-level-menu-item active']"

    def click_on_leave_page(self):
        self.click_on_element("click_on_leave_xpath", self.click_on_leave_xpath)

    def enter_start_date_of_leave(self):
        self.type_into_element("start_date_of_leave_id",self.start_date_of_leave_id,"Fri, 19 oct 2023")

    def enter_end_date_of_leave(self):
        self.type_into_element("end_date_of_leave_id",self.end_date_of_leave_id,"Fri, 29 Sep 2023")

    def enter_leave_comment(self):

        self.type_into_element("leave_comment_id",self.leave_comment_id,"sick leave")

    def click_on_leave_apply_button(self):
        self.click_on_element("leave_apply_button_xpath",self.leave_apply_button_xpath)

    def click_on_final_ok_button_for_leave(self):
        self.click_on_element("final_ok_xpath",self.final_ok_xpath)

    def logout(self):
        self.click_on_element("logout_xpath",self.logout_xpath)

    def click_on_action(self):
        self.click_on_element("action_xpath",self.action_xpath)

    def approve_leave(self):
        self.click_on_element("approve_xpath",self.approve_xpath)

    def click_on_action_save_button(self):
        self.click_on_element("action_save_xpath",self.action_save_xpath)
    def click_on_myleave_page(self):
        self.click_on_element("employee_myleave_page_xpath",self.employee_myleave_page_xpath)

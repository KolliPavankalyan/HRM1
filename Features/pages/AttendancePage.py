from Features.pages.BasePage import BasePage


class AttendancePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    attendance_click_xpath = "(//span[contains(text(),'Attendance')])[1]"
    punch_in_botton_xpath = "//button[normalize-space()='In']"

    def click_on_attendance(self):
        self.click_on_element("attendance_click_xpath",self.attendance_click_xpath)

    def click_on_punch_in(self):
        self.click_on_element("punch_in_botton_xpath",self.punch_in_botton_xpath)

    def check_punch_in_or_not(self):
        self.contains("punch_in_botton_xpath",self.punch_in_botton_xpath,"Punched")




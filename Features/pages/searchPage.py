import time

from Features.pages.BasePage import BasePage


class SearchEmployee(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    search_employee_name_id = "employee_name_quick_filter_employee_list_value"
    click_on_quick_search_xpath = "//a[@ng-click='navbar.search()']"
    # click_on_employeeName_inSuggetion_class_name = "angucomplete-row"
    # search_employe_name_xpath = "//td[normalize-space()='Vinod Reddy Lambu']"

    def enter_employee_inSearchbar(self):
        self.type_into_element("search_employee_name_id",self.search_employee_name_id, "pavan")

    # def click_on_search_botton(self):
    #     self.click_on_element("click_on_quick_search_xpath",self.click_on_quick_search_xpath)

    def clickOn_employeeNameSuggetion(self):
       self.contains("search_employe_name_xpath",self.search_employe_name_xpath,"pavan")




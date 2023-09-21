import time

from Features.pages.BasePage import BasePage


class SearchEmployee(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    search_employee_name_id = "employee_name_quick_filter_employee_list_value"
    click_on_employeeName_inSuggetion_class_name = "angucomplete-row"
    search_employe_name_xpath = "//td[normalize-space()='Vinod Reddy Lambu']"

    def enter_employee_inSearchbar(self):
        self.type_into_element("search_employee_name_id",self.search_employee_name_id, "Vinod Reddy Lambu")


    def clickOn_employeeNameSuggetion(self):
       self.text_equal("search_employe_name_xpath",self.search_employe_name_xpath,"Vinod Reddy Lambu")




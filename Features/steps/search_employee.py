import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from Features.pages.addEmployeeDetailsPage import AddEmployeeDetails
from Features.pages.loginPage import LoginPage
from Features.pages.searchPage import SearchEmployee


@when(u'Click on Employee list')
def step_impl(context):
    context.login  = LoginPage(context.driver)
    context.addEmployee = AddEmployeeDetails(context.driver)
    context.searchPage  = SearchEmployee(context.driver)
    context.login.enter_validUser()
    context.login.enter_validPAssward()
    context.login.login_button()
    context.addEmployee.clickOnEmployeeList()






@when(u'Search name in EmployeeList Searchbar')
def step_impl(context):
    context.searchPage.enter_employee_inSearchbar()
    time.sleep(10)
    context.driver.find_element(By.ID, "quick_search_icon").click()
    time.sleep(10)
    context.searchPage.clickOn_employeeNameSuggetion()


@then(u'Check employee added or not')
def step_impl(context):
    pass

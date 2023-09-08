import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Features.pages.addEmployeeDetailsPage import AddEmployeeDetails
from Features.pages.loginPage import LoginPage


@given(u'Click on Employee list')
def step_impl(context):
    context.login = LoginPage(context.driver)
    context.addEmployee = AddEmployeeDetails(context.driver)


@when(u'Enter all the details of employee')
def step_impl(context):
    context.login.enter_validUser()
    context.login.enter_validPAssward()
    context.login.login_button()

    context.addEmployee.clickOnEmployeeList()
    time.sleep(10)
    # context.driver.find_element(By.XPATH, "//i[normalize-space()='add']").click()
    context.addEmployee.click_on_add_botton()
    time.sleep(5)
    context.addEmployee.Add_employee_details()
    context.driver.find_element(By.XPATH,
                                "//body[1]/div[2]/div[1]/div[1]/div[1]/div[2]/form[1]/oxd-decorator[1]/div[1]/div[2]/div[1]/div[5]/div[1]/div[1]/span[1]/div[2]").click()
    context.addEmployee.enter_user_name_And_pass()
    time.sleep(5)
    context.addEmployee.click_on_location()
    context.addEmployee.click_on_next_step()
    time.sleep(10)
    context.addEmployee.date_of_birth()
    context.addEmployee.final_click()
    time.sleep(10)
    # context.dropdowns = context.driver.find_elements(By.XPATH,"(//button[@role='combobox'])[7]")
    # context.dropdowns[0].click()
    time.sleep(10)
    # context.driver.find_element(By.XPATH,"(//a[@id='bs-select-26-1'])[1]").click()
    # context.addEmployee.final_click()





@when(u'Saving details')
def step_impl(context):
    pass
    # context.addEmployee.save_button()


@then(u'verifying Employee details added in database')
def step_impl(context):
    pass

import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from Features.pages.loginPage import LoginPage


# from selenium.webdriver.common.by import By
#
# from Features.pages.loginPage import LoginPage
# from Features.pages.userLoginPage import UserLoginPage
#
#


@when(u'I enter valid user email address and valid user password as into the fields')
def step_impl(context):
    context.login = LoginPage(context.driver)
    context.login.enter_validUser("")
    context.login.enter_validPAssward("")


@when(u'I click on user Login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()


@then(u'I should user is get logged in or not')
def step_impl(context):
    context.login.check_creditinals_correctOrNot()

# @when(u'I enter valid user email address and valid user password as into the fields')
# def step_impl(context):
#     context.login = LoginPage(context.driver)
#     context.login.enter_validUser("sowjanya")
#     context.login.enter_validPAssward("sowjanya25")
#
#
# @then(u'I should user is get logged in or not')
# def step_impl(context):
#     time.sleep(5)
#     context.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
#
#     time.sleep(10)
#
#
#

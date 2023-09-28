import time

from behave import *
from selenium import  webdriver
from selenium.webdriver.common.by import By

from Features.pages.AttendancePage import AttendancePage
from Features.pages.loginPage import LoginPage


@given(u'I navigated to user Login page for attendance')
def step_impl(context):
    context.login = LoginPage(context.driver)
    context.attendance = AttendancePage(context.driver)
    context.login.enter_validUser("")
    context.login.enter_validPAssward("")
    time.sleep(5)



@when(u'apply attendance punch in')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    time.sleep(10)
    context.attendance.click_on_attendance()
    time.sleep(10)
    context.attendance.click_on_punch_in()
    time.sleep(10)



@then(u'check employe punch in or not')
def step_impl(context):
    time.sleep(10)
    context.attendance.check_punch_in_or_not()
    time.sleep(10)




@when(u'apply attendance punch out')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    time.sleep(5)
    context.attendance.click_on_attendance()
    time.sleep(5)
    context.attendance.click_on_punch_out()
    time.sleep(5)


@then(u'check employe punch out or not')
def step_impl(context):
    time.sleep(5)
    context.attendance.check_punch_out_or_not()
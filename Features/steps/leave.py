import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from Features.pages.leavePage import LeavePage
from Features.pages.loginPage import LoginPage


@given(u'Log into dashboard page')
def step_impl(context):
    context.login = LoginPage(context.driver)
    context.leavePage  = LeavePage(context.driver)
    context.login.enter_validUser("sowjanya")
    context.login.enter_validPAssward("sowjanya25")
    context.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    time.sleep(10)

@when(u'enter into leave page')
def step_impl(context):
    context.leavePage.click_on_leave_page()
    time.sleep(10)



@when(u'apply leave in leave page')
def step_impl(context):
    context.leavePage.enter_start_date_of_leave()
    # context.leavePage.enter_end_date_of_leave()
    context.leavePage.enter_leave_comment()
    context.leavePage.click_on_leave_apply_button()
    time.sleep(10)
    context.leavePage.click_on_final_ok_button_for_leave()
    context.leavePage.logout()


@when(u'login to admin page and approved leave')
def step_impl(context):
    context.login.enter_validUser("Admin")
    context.login.enter_validPAssward("XSdz9L@Mf7")
    context.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    context.leavePage.click_on_leave_page()
    context.leavePage.click_on_action()
    time.sleep(10)
    context.leavePage.approve_leave()
    time.sleep(10)
    context.leavePage.click_on_action_save_button()
    time.sleep(10)



@then(u'check status of leave')
def step_impl(context):
    context.leavePage.logout()
    context.login.enter_validUser("sowjanya")
    context.login.enter_validPAssward("sowjanya25")
    context.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    context.leavePage.click_on_leave_page()
    time.sleep(10)
    context.leavePage.click_on_myleave_page()



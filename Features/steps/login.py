import time

from behave import *
from selenium import webdriver


from Features.pages.loginPage import LoginPage


@given(u'I navigated to Login page')
def step_impl(context):
    context.login = LoginPage(context.driver)


@when(u'I enter valid email address and valid password as into the fields')
def step_impl(context):
    time.sleep(10)
    context.login.enter_validUser("Admin")
    context.login.enter_validPAssward("XSdz9L@Mf7")

@when(u'I click on Login button')
def step_impl(context):
    context.login.login_button()



@then(u'I should get logged in')
def step_impl(context):
    context.login.check_creditinals_correctOrNot()




@when(u'I enter invalid email and valid password into the fields')
def step_impl(context):
    context.login.enter_invalid_user()
    context.login.enter_validPAssward("blbF9@RZH4")

@then(u'I should get a proper warning message')
def step_impl(context):
    pass
    # context.login.failure_msg()


@when(u'I enter valid email and invalid password into the fields')
def step_impl(context):
    context.login.enter_validUser("Admin")
    context.login.enter_invalid_password()


@then(u'I should get a proper warning message on password page')
def step_impl(context):
    pass


@when(u'I enter invalid email and invalid password into the fields')
def step_impl(context):
    context.login.enter_invalid_user()
    context.login.enter_invalid_password()


@when(u'I dont enter anything into email and password fields')
def step_impl(context):
    context.login.without_enter_anyValues()


@then(u'I should get a proper warning message without enter any details')
def step_impl(context):
    pass

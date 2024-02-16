import time
from datetime import datetime

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from features.pages.AccountPage import AccountPage
from features.pages.HomePage import HomePage
from features.pages.LoginPage import LoginPage


@given(u'I navigate to Login Page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account()
    context.home_page.select_login_option()


@when(u'I enter valid email and valid password into the fields')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address("gk@gmail.com")
    context.login_page.enter_password("1234")


@when(u'I click on Login button')
def step_impl(context):
    context.login_page.click_on_login_button()


@then(u'I should be successfully logged in')
def step_impl(context):
    context.account_page = AccountPage(context.driver)
    assert context.account_page.display_status_of_edit_your_account_information()


@when(u'I enter invalid email and valid password into the fields')
def step_impl(context):
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    invalid_email_generated = f"amotoori{time_stamp}@gmail.com"
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address(invalid_email_generated)
    context.login_page.enter_password("1234")


@then(u'I should get proper warning message')
def step_impl(context):
    actual_warning_message = context.login_page.retrieve_warning_message()
    print(f"actual text:  {actual_warning_message}")
    assert actual_warning_message == "Warning: No match for E-Mail Address and/or Password."


@when(u'I enter valid email and invalid password into the fields')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address("gk@gmail.com")
    context.login_page.enter_password("12345678900")


@when(u'I don\'t enter anything into email and password fields')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address("")
    context.login_page.enter_password("")

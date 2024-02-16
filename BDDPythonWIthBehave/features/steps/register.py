import time

from behave import *
from datetime import datetime

from features.pages.AccountSuccessPage import AccountSuccessPage
from features.pages.HomePage import HomePage
from features.pages.Register import RegisterPage
from utilities.config import TestData


@given(u'I navigate to Register Page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account()
    context.home_page.click_on_register_option()


@when(u'I enter details into mandatory fields')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.enter_first_name("TY")
    context.register_page.enter_last_name("YT")
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    generated_email = f"ty{time_stamp}@gmail.com"
    context.register_page.enter_email(generated_email)
    context.register_page.enter_telephone("1234567890")
    context.register_page.enter_password("1234567")
    context.register_page.enter_confirm_password("1234567")


@when(u'I select Privacy Policy option')
def step_impl(context):
    context.register_page.select_privacy_policy()


@when(u'I click on Continue button')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.click_continue_button()


@then(u'Account should get created')
def step_impl(context):
    context.account_success_page = AccountSuccessPage(context.driver)
    actual_text = context.account_success_page.retrieve_account_creation_message()
    print(f"Actual text : {actual_text}")
    assert actual_text == TestData.expected_account_created_message


@when(u'I enter details into all fields')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.enter_first_name("TY")
    context.register_page.enter_last_name("YT")
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    generated_email = f"ty{time_stamp}@gmail.com"
    context.register_page.enter_email(generated_email)
    context.register_page.enter_telephone("1234567890")
    context.register_page.enter_password("1234567")
    context.register_page.enter_confirm_password("1234567")
    context.register_page.select_yes_radio_button()


@when(u'I enter details into all fields except email field')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.enter_first_name("TY")
    context.register_page.enter_last_name("YT")
    context.register_page.enter_telephone("1234567890")
    context.register_page.enter_password("1234567")
    context.register_page.enter_confirm_password("1234567")
    context.register_page.select_yes_radio_button()


@when(u'I enter existing accounts email into email field')
def step_impl(context):
    context.register_page.enter_email("gk@gmail.com")


@then(u'Proper warning message informing about duplicate account should be displayed')
def step_impl(context):
    email_warning = context.register_page.retrieve_duplicate_email_warning()
    print(F"Actual_warning: {email_warning}")
    assert email_warning == "Warning: E-Mail Address is already registered!"



@when(u'I dont enter anything into the fields')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.enter_first_name("")
    context.register_page.enter_last_name("")
    context.register_page.enter_email("")
    context.register_page.enter_telephone("")
    context.register_page.enter_password("")
    context.register_page.enter_confirm_password("")


@then(u'Proper warning messages for every mandatory fields should be displayed')
def step_impl(context):
    context.register_page.verify_all_warnings(TestData.expected_privacy_warning,
                                              TestData.expected_first_name_warning,
                                              TestData.expected_last_name_warning,
                                              TestData.expected_email_warning,
                                              TestData.expected_telephone_warning,
                                              TestData.expected_password_warning)
    time.sleep(5)

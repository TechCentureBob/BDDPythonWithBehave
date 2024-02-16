import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from features.pages.HomePage import HomePage
from features.pages.SearchPage import SearchPage


@given(u'I am on HomePage')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    title = context.home_page.check_home_page_title()
    assert title == "Your Store"


@when(u'I enter a valid product into the Search box field')
def step_impl(context):
    context.home_page.enter_product_into_search_box_field("HP")


@when(u'I click on Search button')
def step_impl(context):
    context.home_page.click_on_search_button()


@then(u'Valid product should get displayed in Search results')
def step_impl(context):
    context.search_page = SearchPage(context.driver)
    assert context.search_page.display_status_of_valid_product()


@when(u'I enter invalid product into the Search box field')
def step_impl(context):
    context.home_page.enter_product_into_search_box_field("Honda")


@then(u'Proper message should be displayed in Search Results')
def step_impl(context):
    context.search_page = SearchPage(context.driver)
    message = context.search_page.retrieve_no_product_message()
    assert message == "There is no product that matches the search criteria.ABC"


@when(u'I don\'t enter anything into the Search box field')
def step_impl(context):
    context.home_page.enter_product_into_search_box_field("")

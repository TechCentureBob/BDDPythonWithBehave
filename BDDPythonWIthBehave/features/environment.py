import allure
from allure_commons.types import AttachmentType
from selenium import webdriver

from utilities.config import TestData


def before_scenario(context, driver):
    browser = TestData.browser
    if browser == "chrome":
        context.driver = webdriver.Chrome()
    elif browser == "firefox":
        context.driver = webdriver.Firefox()
    elif browser == "edge":
        context.driver = webdriver.Edge()

    context.driver.maximize_window()
    context.driver.get(TestData.url)


def after_scenario(context, driver):
    context.driver.quit()


def after_step(context, step):
    if step.status == "failed":
        allure.attach(context.driver.get_screenshot_as_png(), name="failed_screenshot",
                      attachment_type=AttachmentType.PNG)

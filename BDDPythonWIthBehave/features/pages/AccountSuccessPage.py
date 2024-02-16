from selenium.webdriver.common.by import By


class AccountSuccessPage:

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # Locators
    account_creation_message_xpath = "//div[@id='content']/h1"

    # Methods
    def retrieve_account_creation_message(self):
        return self.driver.find_element(By.XPATH, self.account_creation_message_xpath).text

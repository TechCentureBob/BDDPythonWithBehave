from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    email_address_field_name = "email"
    password_field_name = "password"
    login_button_xpath = "//input[@type='submit']"
    warning_message_xpath = "//div[@id='account-login']/div[1]"

    # Methods

    def enter_email_address(self, email_text):
        self.driver.find_element(By.NAME, self.email_address_field_name).send_keys(email_text)

    def enter_password(self, password_text):
        self.driver.find_element(By.NAME, self.password_field_name).send_keys(password_text)

    def click_on_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def retrieve_warning_message(self):
        return self.driver.find_element(By.XPATH, self.warning_message_xpath).text

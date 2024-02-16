from selenium.webdriver.common.by import By
from datetime import datetime


class RegisterPage:

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # Locators
    first_name_field_id = "input-firstname"
    last_name_field_id = "input-lastname"
    email_field_id = "input-email"
    telephone_field_id = "input-telephone"
    password_field_id = "input-password"
    confirm_password_field_id = "input-confirm"
    agree_field_name = "agree"
    continue_button_xpath = "//input[@value='Continue']"
    yes_radio_button_xpath = "//input[@name='newsletter'][@value=1]"
    duplicate_email_warning_xpath = "//div[@id='account-register']/div[1]"
    privacy_policy_warning_xpath = "//div[@id='account-register']/div[1]"
    first_name_warning_xpath = "//input[@id='input-firstname']/following-sibling::div"
    last_name_warning_xpath = "//input[@id='input-lastname']/following-sibling::div"
    email_warning_xpath = "//input[@id='input-email']/following-sibling::div"
    telephone_warning_xpath = "//input[@id='input-telephone']/following-sibling::div"
    password_warning_xpath = "//input[@id='input-password']/following-sibling::div"

    # Methods
    def enter_first_name(self, first_name_text):
        self.driver.find_element(By.ID, self.first_name_field_id).send_keys(first_name_text)

    def enter_last_name(self, last_name_text):
        self.driver.find_element(By.ID, self.last_name_field_id).send_keys(last_name_text)

    def enter_email(self, email_text):
        self.driver.find_element(By.ID, self.email_field_id).send_keys(email_text)

    def enter_telephone(self, telephone_text):
        self.driver.find_element(By.ID,self.telephone_field_id).send_keys(telephone_text)

    def enter_password(self, password_text):
        self.driver.find_element(By.ID, self.password_field_id).send_keys(password_text)

    def enter_confirm_password(self, confirm_password_text):
        self.driver.find_element(By.ID, self.confirm_password_field_id).send_keys(confirm_password_text)

    def select_privacy_policy(self):
        self.driver.find_element(By.NAME, self.agree_field_name).click()

    def click_continue_button(self):
        self.driver.find_element(By.XPATH, self.continue_button_xpath).click()

    def select_yes_radio_button(self):
        self.driver.find_element(By.XPATH, self.yes_radio_button_xpath).click()

    def fill_out_required_fields(self, first_name_text, last_name, email, telephone, password, confirm_password):
        self.enter_first_name(first_name_text)
        self.enter_last_name(last_name)
        self.enter_email(email)
        self.enter_telephone(telephone)
        self.enter_password(password)
        self.enter_confirm_password(confirm_password)

    def retrieve_duplicate_email_warning(self):
        return self.driver.find_element(By.XPATH, self.duplicate_email_warning_xpath).text

    def verify_all_warnings(self, expected_privacy_policy_warning, expected_first_name_warning_message,
                            expected_last_name_warning_message, expected_email_warning_message,
                            expected_telephone_warning_message, expected_password_warning_message):
        actual_policy_warning = self.driver.find_element(By.XPATH, self.privacy_policy_warning_xpath).text
        actual_warning_first_name = self.driver.find_element(By.XPATH, self.first_name_warning_xpath).text
        actual_warning_last_name = self.driver.find_element(By.XPATH, self.last_name_warning_xpath).text
        actual_warning_email = self.driver.find_element(By.XPATH,self.email_warning_xpath).text
        actual_warning_telephone = self.driver.find_element(By.XPATH, self.telephone_warning_xpath).text
        actual_warning_password = self.driver.find_element(By.XPATH, self.password_warning_xpath).text

        #condition

        assert actual_policy_warning == expected_privacy_policy_warning , "Doesn't match with expected warning"
        assert actual_warning_first_name == expected_first_name_warning_message
        assert actual_warning_last_name == expected_last_name_warning_message
        assert actual_warning_email == expected_email_warning_message
        assert actual_warning_telephone == expected_telephone_warning_message
        assert actual_warning_password == expected_password_warning_message
        return True







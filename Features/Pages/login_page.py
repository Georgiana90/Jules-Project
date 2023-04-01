from selenium.webdriver.common.by import By


class Login:
    BASE_URL = 'http://jules.app/'
    EMAIL_SELECTOR = (By.XPATH, '//input[@type="text"]')
    PASSWORD_SELECTOR = (By.XPATH, '//input[@type="password"]')
    LOGIN_SELECTOR = (By.XPATH, '//button[@data-test-id="login-button"]')
    VERIFY_TEXT = (By.XPATH, '//span[@aria-controls="simple-menu"]')
    COOKIES = (By.XPATH, '//button[@id="onesignal-slidedown-cancel-button"]')
    USER_OPTIONS = (By.XPATH, '//*[@data-test-id="user-options-business-button"]')
    LOG_OUT = (By.XPATH, '//span[contains(text(),"Log Out")]')
    LOG_OUT_ACCEPT = (By.XPATH, '//button[@data-test-id="confirm-logout-button"]')
    ERROR_MESSAGE = (By.XPATH, '//div[@data-test-id="signin-error"]')

    def __init__(self, browser):
        self.driver = browser.driver

    def go_to(self, page):
        self.driver.get(f'{self.BASE_URL}{page}')

    def input_email(self, username):
        email = self.driver.find_element(*self.EMAIL_SELECTOR)
        email.click()
        email.send_keys(username)

    def input_password(self, password):
        input_password = self.driver.find_element(*self.PASSWORD_SELECTOR)
        input_password.click()
        input_password.send_keys(password)

    def click_login_button(self):
        login_button = self.driver.find_element(*self.LOGIN_SELECTOR)
        login_button.click()

    def is_message_displayed(self):
        actual_account_message = self.driver.find_element(*self.VERIFY_TEXT).text
        expected_account_message = 'The Georgiana Household'
        assert actual_account_message == expected_account_message, "You are not logged in Jules account"

    def pop_up(self):
        pop_up = self.driver.find_element(*self.COOKIES)
        pop_up.click()

    def user_options(self):
        user_options = self.driver.find_element(*self.USER_OPTIONS)
        user_options.click()

    def log_out(self):
        log_out = self.driver.find_element(*self.LOG_OUT)
        log_out.click()

    def log_out_accept(self):
        log_out_accept = self.driver.find_element(*self.LOG_OUT_ACCEPT)
        log_out_accept.click()

    def get_current_url(self):
        return self.driver.current_url

    def check_login_url(self):
        if self.driver.current_url == 'https://jules.app/sign-in':
            assert True
        else:
            assert False, 'The URL did not match'

    def check_error_message(self, error_msg):

        actual_message = self.driver.find_element(*self.ERROR_MESSAGE).text
        assert actual_message == error_msg

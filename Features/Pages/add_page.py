from selenium.webdriver.common.by import By


class AddItem:
    BASE_URL = 'http://jules.app/'
    ADD_PAGE_SELECTOR = (By.XPATH, '//div[@data-test-id="add-flows-navigation-button"]')
    ADD_PERSON_SELECTOR = (By.XPATH, '//span[text() = "Person"]')
    FIRSTNAME_SELECTOR = (By.XPATH, '//div[1]/div/div/input')
    LASTNAME_SELECTOR = (By.XPATH, '//div[2]/div/div/input')
    SAVE_SELECTOR = (By.XPATH, '//button[@data-test-id="item-details-step-save-item-button"]')
    CONFIRM_MESSAGE = (By.XPATH, '//span[text()=" was added successfully!"]')
    FINISH_SELECTOR = (By.XPATH, '//button[@data-test-id="add-person-wizard-finish-button"]')
    INVALID_VALUE = (By.XPATH, '//p[contains(text(),"invalid field value")]')

    def __init__(self, browser):
        self.driver = browser.driver

    def go_to(self, page):
        self.driver.get(f'{self.BASE_URL}{page}')

    def select_add(self):
        select_add = self.driver.find_element(*self.ADD_PAGE_SELECTOR)
        select_add.click()

    def click_add_person(self):
        add_people = self.driver.find_element(*self.ADD_PERSON_SELECTOR)
        add_people.click()

    def input_first_name(self, firstname):
        input_firstname = self.driver.find_element(*self.FIRSTNAME_SELECTOR)
        input_firstname.click()
        input_firstname.send_keys(firstname)

    def input_last_name(self, lastname):
        input_lastname = self.driver.find_element(*self.LASTNAME_SELECTOR)
        input_lastname.click()
        input_lastname.send_keys(lastname)

    def click_save_button(self):
        save_button = self.driver.find_element(*self.SAVE_SELECTOR)
        save_button.click()

    def check_add_message(self):
        confirm_message = self.driver.find_element(*self.CONFIRM_MESSAGE).text
        expected_message = "John Doe was added successfully!"
        assert confirm_message == expected_message

    def click_finish(self):
        click_finish_button = self.driver.find_element(*self.FINISH_SELECTOR)
        click_finish_button.click()

    def check_invalid_field(self):
        actual_error = self.driver.find_element(*self.INVALID_VALUE).text
        expected_error = "invalid field value"
        assert actual_error == expected_error

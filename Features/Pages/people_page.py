from selenium.webdriver.common.by import By


class PeoplePage:
    BASE_URL = 'http://jules.app/'
    SEARCH_SELECTOR = (By.XPATH, '//input[@placeholder="Type to search..."]')
    LIST_ITEM_SELECTOR = (By.XPATH, '//div[@class="ListItem"]')
    SELECT_LIST = (By.XPATH, '//div[@style="padding-top: 4px;"]')
    DELETE_PEOPLE = (By.XPATH, '//div[@data-test-id="batch-delete-button"]')
    DELETE_ACCEPT = (By.XPATH, '//button[@data-test-id="batch-delete-dialog-delete-button"]')
    DELETE_CONFIRMATION = (By.XPATH, '//span[contains(text(),"All selected persons have been deleted successfully.")]')
    CLOSE_DELETE_ALERT = (By.XPATH, '//button[@aria-label="close"]')

    def __init__(self, browser):
        self.driver = browser.driver

    def go_to(self, page):
        self.driver.get(f'{self.BASE_URL}{page}')

    def search_bar_input(self, name):
        click_search = self.driver.find_element(*self.SEARCH_SELECTOR)
        click_search.click()
        click_search.send_keys(name)

    def verify_user_from_list(self, results):
        actual_list = self.driver.find_element(*self.LIST_ITEM_SELECTOR).text
        assert actual_list == results

    def select_option(self):
        select = self.driver.find_element(*self.SELECT_LIST)
        select.click()

    def delete_option(self):
        delete = self.driver.find_element(*self.DELETE_PEOPLE)
        delete.click()

    def accept_delete(self):
        click_delete = self.driver.find_element(*self.DELETE_ACCEPT)
        click_delete.click()

    def verify_delete_message(self):
        actual_text = self.driver.find_element(*self.DELETE_CONFIRMATION).text
        expected_text = 'All selected persons have been deleted successfully.'
        assert actual_text == expected_text

    def close_alert(self):
        delete_alert = self.driver.find_element(*self.CLOSE_DELETE_ALERT)
        delete_alert.click()


    def current_url(self):
        return self.driver.current_url

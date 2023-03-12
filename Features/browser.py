from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Browser:

    def __init__(self):
        service = Service(ChromeDriverManager().install())
        self.driver = Chrome(service=service)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def close(self):
        self.driver.quit()

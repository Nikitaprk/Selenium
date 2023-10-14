from conftest import driver
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.WebDriverWait = WebDriverWait
        self.driver = driver
        # self.wait = WebDriverWait(driver, 3)

    def find(self, args):
        return self.driver.find_element(*args)

    def finds(self, args):
        return self.driver.find_elements(*args)



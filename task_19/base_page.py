from conftest import driver
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        # self.wait = WebDriverWait(driver, 3)

    def find(self, args):
        return self.driver.find_element(*args)

    def finds(self, args):
        return self.driver.find_elements(*args)

    # def waiting(self, args):
    #     self.wait.until(EC.text_to_be_present_in_element(args))

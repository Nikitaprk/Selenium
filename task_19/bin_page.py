from base_page import BasePage
from conftest import driver
from selenium.webdriver.common.by import By

ALL_ELEMENTS = (By.XPATH, "//td[@class='item']")
REMOVE = (By.XPATH, "//button[text()='Remove']")


class Bin_page(BasePage):
    def __int__(self, driver):
        super().__init__(driver)

    def all_elements(self):
        return self.finds(ALL_ELEMENTS)

    def remove_action(self):
        self.find(REMOVE).click()

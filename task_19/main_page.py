from base_page import BasePage
from selenium.webdriver.common.by import By

DUCK_LOCATOR = (By.XPATH, "//li[starts-with(@class, 'product')]")
GO_TO_CART = (By.XPATH, "//a[text()='Checkout »']")


class Main_page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def select_duck(self):
        return self.find(DUCK_LOCATOR).click()

    def checkout(self):
        return self.find(GO_TO_CART).click()

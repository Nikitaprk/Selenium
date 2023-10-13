from base_page import BasePage
from conftest import driver
from selenium.webdriver.common.by import By

YELLOW_DUCK_LOCATOR = (By.XPATH, "//select[@name='options[Size]']")
YELLOW_DUCK_CHOOSE_SIZE = (By.XPATH, "//option[@value='Medium']")
ADD_TO_CART = (By.XPATH, "//button[@name='add_cart_product']")
CHECK_QUANTITY = (By.XPATH, "//span[@class='quantity']")
BACK_TO_MAIN = (By.XPATH, "//a[@href='http://localhost/litecart/en/']")


class Goods_page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def add(self):
        return self.find(ADD_TO_CART)

    def check_if_yellow(self):
        return self.finds(YELLOW_DUCK_LOCATOR)

    def yellow_duck_size(self):
        return self.find(YELLOW_DUCK_LOCATOR)

    def yellow_duck_choose_size(self):
        return self.find(YELLOW_DUCK_CHOOSE_SIZE)

    def check_quantity(self):
        self.find(CHECK_QUANTITY)

    def back_to_main(self):
        return self.find(BACK_TO_MAIN)

    # def wait_for(self, args):
    #     return self.waiting(CHECK_QUANTITY, args)

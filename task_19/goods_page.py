from base_page import BasePage
from conftest import driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

YELLOW_DUCK_LOCATOR = (By.XPATH, "//select[@name='options[Size]']")
YELLOW_DUCK_CHOOSE_SIZE = (By.XPATH, "//option[@value='Medium']")
ADD_TO_CART = (By.XPATH, "//button[@name='add_cart_product']")
CHECK_QUANTITY = (By.XPATH, "//span[@class='quantity']")
BACK_TO_MAIN = (By.XPATH, "//a[@href='http://localhost/litecart/en/']")


class Goods_page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 3)

    def add_to_cart(self, x):
        self.find(ADD_TO_CART).click()
        self.wait.until(EC.text_to_be_present_in_element(CHECK_QUANTITY, str(x)))

    def check_if_yellow(self):
        return self.finds(YELLOW_DUCK_LOCATOR)

    def yellow_duck_choose_size(self):
        self.find(YELLOW_DUCK_LOCATOR).click()
        self.find(YELLOW_DUCK_CHOOSE_SIZE).click()

    def check_quantity(self):
        self.find(CHECK_QUANTITY)

    def back_to_main(self):
        return self.find(BACK_TO_MAIN).click()

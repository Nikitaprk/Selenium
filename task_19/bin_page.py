from base_page import BasePage
from conftest import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ALL_ELEMENTS = (By.XPATH, "//td[@class='item']")
REMOVE = (By.XPATH, "//button[text()='Remove']")


class Bin_page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 3)

    def get_all_elements(self):
        return self.finds(ALL_ELEMENTS)

    def remove_action(self, elems):
        self.find(REMOVE).click()
        self.wait.until(EC.staleness_of(elems[0]))

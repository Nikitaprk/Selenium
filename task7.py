import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    chr_driver = webdriver.Chrome()
    chr_driver.get("http://localhost/litecart/en/")
    chr_driver.maximize_window()
    chr_driver.implicitly_wait(10)
    return chr_driver


def test_check_stickers2(driver):
    list_goods = driver.find_elements(By.XPATH, "//li[@class='product column shadow hover-light']")  # cписок всех товаров
    for x in range(len(driver.find_elements(By.XPATH, "//li[@class='product column shadow hover-light']"))):
        assert len(list_goods[x].find_elements(By.XPATH,".//div[starts-with(@class, 'sticker')]")) == 1  # внутри товара 1 элемент со стикером

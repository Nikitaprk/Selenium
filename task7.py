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


# def test_check_stickers2(driver):
#     list_goods = driver.find_elements(By.XPATH, "//div[@class='image-wrapper']")  # cписок всех товаров
#     for x in range(len(list_goods)):
#         assert len(list_goods[x].find_elements(By.XPATH,".//div[starts-with(@class, 'sticker')]")) == 1  # внутри товара 1 элемент со стикером

def test_check_stickers(driver):
    list_goods = driver.find_elements(By.XPATH, "//img[@class='image']")  # cписок всех товаров
    for x in range(len(list_goods)):
        assert len(list_goods[x].find_elements(By.XPATH,"./parent::*/div[starts-with(@class, 'sticker')]")) == 1  # внутри товара 1 элемент со стикером

# Выбрал семантически значимый признак. Вроде бы это class=image. Но так как этот класс находится на одном уровне
# со стикером, то для поиска стикера пришлось усложнить локатор: поднимаемся к родителю, а затем уже ищем стикер
# по другому поиск не работает
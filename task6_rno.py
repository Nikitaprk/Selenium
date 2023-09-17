import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    chr_driver = webdriver.Chrome()
    chr_driver.get("http://localhost/litecart/admin/login.php")
    chr_driver.maximize_window()
    chr_driver.implicitly_wait(1)
    chr_driver.find_element(By.XPATH, "//input[@type='text']").send_keys('admin')
    chr_driver.find_element(By.XPATH, "//input[@type='password']").send_keys('admin')
    chr_driver.find_element(By.NAME, 'remember_me').click()
    chr_driver.find_element(By.NAME, 'login').click()
    return chr_driver


def test_qwe(driver):
    for x in range(len(driver.find_elements(By.XPATH, "//li[@id='app-']"))):
        menu_list = driver.find_elements(By.XPATH, "//li[@id='app-']")  # создаем список всех элементов из меню
        menu_list[x].click()
        assert driver.find_element(By.TAG_NAME, "h1").is_displayed()  # проверяем наличие заголовка
        menu_list = driver.find_elements(By.XPATH, "//li[@id='app-']")  # пересоздаем список, т.к элементы изменились после клика
        if len(menu_list[x].find_elements(By.XPATH, "//ul[@class='docs']//li")) > 0:  # проверяем наличие дочернего списка
            for q in range(len(menu_list[x].find_elements(By.XPATH, "//ul[@class='docs']//li"))):
                subMenu_list = driver.find_elements(By.XPATH, "//ul[@class='docs']//li")
                subMenu_list[q].click()  # также проходимся по дочернему списку и кликаем по всем элементам
                assert driver.find_element(By.TAG_NAME, "h1").is_displayed()

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    chr_driver = webdriver.Chrome()
    chr_driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    chr_driver.maximize_window()
    chr_driver.find_element(By.XPATH, "//input[@type='text']").send_keys('admin')
    chr_driver.find_element(By.XPATH, "//input[@type='password']").send_keys('admin')
    chr_driver.find_element(By.NAME, 'remember_me').click()
    chr_driver.find_element(By.NAME, 'login').click()
    return chr_driver


def test_1(driver):
    wait = WebDriverWait(driver, 5)
    driver.find_element(By.XPATH, "//a[@class='button']").click()
    for x in driver.find_elements(By.XPATH, "//form[*]//a[@target='_blank']"):
        main_window = driver.current_window_handle  # пишем в переменную главную страницу
        x.click()
        for handel in driver.window_handles:
            if handel != main_window:
                driver.switch_to.window(handel)
        wait.until(EC.presence_of_element_located((By.XPATH, "//h1"))) # ждем пока страница не прогрузится, ищем заголовок в новой странице
        driver.close()  # закрываем выбранное рабочее окно
        driver.switch_to.window(main_window)  # переключаемся на главное окно
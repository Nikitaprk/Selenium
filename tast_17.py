import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    chr_driver = webdriver.Chrome()
    chr_driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
    chr_driver.maximize_window()
    chr_driver.find_element(By.XPATH, "//input[@type='text']").send_keys('admin')
    chr_driver.find_element(By.XPATH, "//input[@type='password']").send_keys('admin')
    chr_driver.find_element(By.NAME, 'remember_me').click()
    chr_driver.find_element(By.NAME, 'login').click()
    return chr_driver


def test123 (driver):
    elems = driver.find_elements(By.XPATH, "//td/a/i")
    for i in range(len(elems)):
        elems[i].click()
        assert len(driver.get_log('browser'))==0 # проверяем на каждой итерации, что сообщений нет
        driver.back()
        elems = driver.find_elements(By.XPATH, "//td/a/i")
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    chr_driver = webdriver.Chrome()
    chr_driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    chr_driver.maximize_window()
    chr_driver.implicitly_wait(1)
    chr_driver.find_element(By.XPATH, "//input[@type='text']").send_keys('admin')
    chr_driver.find_element(By.XPATH, "//input[@type='password']").send_keys('admin')
    chr_driver.find_element(By.NAME, 'remember_me').click()
    chr_driver.find_element(By.NAME, 'login').click()
    return chr_driver


def test_check_abc(driver):
    countries = driver.find_elements(By.XPATH, "//tr[@class='row']/td[3]/a")  # ищем все страны в списке
    for x in range(len(countries)):
        countries[x].click()  # переходим по каждой
        geo_zones = []
        for q in driver.find_elements(By.XPATH, "//select[contains(@name, 'zone_code' )]/option[@selected='selected']"):
            attr = q.get_attribute('innerText')  # ищем названия стран в списке
            geo_zones.append(attr)
        assert geo_zones == sorted(geo_zones)
        driver.back()
        countries = driver.find_elements(By.XPATH, "//tr[@class='row']/td[3]/a")


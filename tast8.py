import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    chr_driver = webdriver.Chrome()
    chr_driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    chr_driver.maximize_window()
    chr_driver.implicitly_wait(1)
    chr_driver.find_element(By.XPATH, "//input[@type='text']").send_keys('admin')
    chr_driver.find_element(By.XPATH, "//input[@type='password']").send_keys('admin')
    chr_driver.find_element(By.NAME, 'remember_me').click()
    chr_driver.find_element(By.NAME, 'login').click()
    return chr_driver


def test_check_abc(driver):
    names = []
    for x in driver.find_elements(By.XPATH, "//tr[@class='row']/td[5]"):
        names.append(x.get_attribute('textContent'))  # перебираем все элементы, достаем названия стран и добавляем их в список
    assert names == sorted(names)  # сравниваем наш список с таким же, но сортированным, узнаем был ли он отсортирован изначально


def test_check_abc_inner(driver):
    list_ = driver.find_elements(By.XPATH, "//tr[@class='row']/td[6]")  # ищем все зоны у стран
    for x in range(len(list_)):
        if int(list_[x].get_attribute('innerText')) > 0:  # если кол-во зон больше нуля
            list_[x].find_element(By.XPATH, './following::a').click()  # то переходим далее по ссылке
            names = []
            for q in driver.find_elements(By.XPATH, "//*[@id='table-zones']//td[3]"):
                if len(q.get_attribute('textContent'))>0:  # проверяем, что атрибут не пустой
                    names.append(q.get_attribute('textContent'))  # засовываем все зоны в список
            assert names == sorted(names)  # сравниваем его с им же, только отсортированным
            driver.back()
            list_ = driver.find_elements(By.XPATH, "//tr[@class='row']/td[6]") # заново ищем элементы


import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    chr_driver = webdriver.Chrome()
    chr_driver.get("http://localhost/litecart/en/")
    chr_driver.maximize_window()
#   chr_driver.implicitly_wait(2)
    return chr_driver


def test123(driver):
    wait = WebDriverWait(driver, 3)
    x = 1  # переменная для дальнейшего подсчета кол-во элементов в корзине
    for i in range(3):
        driver.find_element(By.XPATH, "//li[starts-with(@class, 'product')]").click()  # клик на первый попавшийся товар
        if len(driver.find_elements(By.XPATH, "//select[@name='options[Size]']")) == 1:  # проверка на товар с опцией размера
            driver.find_element(By.XPATH, "//select[@name='options[Size]']").click()
            driver.find_element(By.XPATH, "//option[@value='Medium']").click()
        driver.find_element(By.XPATH, "//button[@name='add_cart_product']").click()
        wait.until(EC.text_to_be_present_in_element((By.XPATH, "//span[@class='quantity']"), str(x))) # ждем пока корзина не пополнится ровно на 1 товар
        x += 1  # увеличиваем переменную для подсчета товаров в корзине на единицу
        driver.find_element(By.XPATH, "//a[@href='http://localhost/litecart/en/']").click()
    driver.find_element(By.XPATH, "//a[text()='Checkout »']").click()
    elems = driver.find_elements(By.XPATH, "//td[@class='item']")  # список всех элементов на странице Checkout
   # time.sleep(3) # добавил сюда ожидание для теста, чтобы было видно изначальное кол-во товаров на странице checkout, т.е первое удаление мгновенное
    for q in range(len(elems)):
        driver.find_element(By.XPATH, "//button[text()='Remove']").click()
        wait.until(EC.staleness_of(elems[0]))  # ждем пока не пропадет элемент из списка
        elems = driver.find_elements(By.XPATH, "//td[@class='item']")
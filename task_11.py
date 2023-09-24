import time

import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By

fake = Faker()

@pytest.fixture()
def driver():
    chr_driver = webdriver.Chrome()
    chr_driver.get("http://localhost/litecart/en/create_account")
    chr_driver.maximize_window()
    chr_driver.implicitly_wait(3)
    return chr_driver


def test_registration(driver):
    email = fake.email()
    phone = fake.phone_number()
    password = fake.password()
    driver.find_element(By.XPATH, "//input[@name='firstname']").send_keys('Nikita')
    driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys('Narchuk')
    driver.find_element(By.XPATH, "//input[@name='address1']").send_keys('address')
    driver.find_element(By.XPATH, "//input[@name='postcode']").send_keys("12345")
    driver.find_element(By.XPATH, "//input[@name='city']").send_keys(fake.city())
    driver.find_element(By.XPATH, "//span[@class='select2-selection__arrow']").click()
    driver.find_element(By.XPATH, "//li[text()='United States']").click()
    driver.find_element(By.XPATH, "//input[@name='email']").send_keys(email)
    driver.find_element(By.XPATH, "//input[@name='phone']").send_keys('89998887766')
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
    driver.find_element(By.XPATH, "//input[@name='confirmed_password']").send_keys(password)
    driver.find_element(By.XPATH, "//button[@name='create_account']").click()
    #  регистрация завершена
    driver.find_element(By.XPATH, "//div[@id='box-account']//a[text()='Logout']").click()
    driver.find_element(By.XPATH, "//input[@name='email']").send_keys(email)
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
    #  авторизация
    driver.find_element(By.XPATH, "//button[@name='login']").click()
    driver.find_element(By.XPATH, "//div[@id='box-account']//a[text()='Logout']").click()


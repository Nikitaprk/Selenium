import time
import pathlib
import os
# from pathlib import Path
import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By

# path = Path("pictures/te2st.jpg")
fake = Faker()


@pytest.fixture()
def driver():
    chr_driver = webdriver.Chrome()
    chr_driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog")
    chr_driver.maximize_window()
    chr_driver.find_element(By.XPATH, "//input[@type='text']").send_keys('admin')
    chr_driver.find_element(By.XPATH, "//input[@type='password']").send_keys('admin')
    chr_driver.find_element(By.NAME, 'login').click()
    chr_driver.implicitly_wait(3)
    return chr_driver


def test(driver):
    driver.find_element(By.XPATH, "//a[text()=' Add New Product']").click()
    # general
    driver.find_element(By.XPATH, "//label[text()=' Enabled']").click()
    driver.find_element(By.XPATH, "//input[@name='code']").send_keys('12345')
    driver.find_element(By.XPATH, "//input[@name='name[en]']").send_keys('new_product')
    driver.find_element(By.XPATH, "//input[@data-name='Rubber Ducks']").click()
    driver.find_element(By.XPATH, "//input[@value='1-3']").click()
    driver.find_element(By.XPATH, "//input[@name='quantity']").send_keys('100')
    driver.find_element(By.XPATH, "//input[@type='file']").send_keys(os.getcwd() + "\\pictures\\test.jpg")
    driver.find_element(By.XPATH, "//input[@name='date_valid_from']").send_keys('12.12.2023')
    driver.find_element(By.XPATH, "//input[@name='date_valid_to']").send_keys('12.12.2024')
    time.sleep(5)
    driver.find_element(By.XPATH, "//a[text()='Information']").click()
    # information
    driver.find_element(By.XPATH, "//select[@name='manufacturer_id']").click()
    driver.find_element(By.XPATH, "//option[text()='ACME Corp.']").click()
    driver.find_element(By.XPATH, "//input[@name='keywords']").send_keys('keyword')
    driver.find_element(By.XPATH, "//input[@name='short_description[en]']").send_keys('description')
    driver.find_element(By.XPATH, "//div[@class='trumbowyg-editor']").send_keys('description')
    driver.find_element(By.XPATH, "//input[@name='head_title[en]']").send_keys('head title')
    driver.find_element(By.XPATH, "//input[@name='meta_description[en]']").send_keys('meta description')
    time.sleep(5)
    driver.find_element(By.XPATH, "//a[text()='Prices']").click()
    # prices
    driver.find_element(By.XPATH, "//input[@name='purchase_price']").send_keys('10')
    driver.find_element(By.XPATH, "//select[@name='purchase_price_currency_code']").click()
    driver.find_element(By.XPATH, "//option[@value='USD']").click()
    driver.find_element(By.XPATH, "//input[@name='prices[USD]']").send_keys('10')
    driver.find_element(By.XPATH, "//input[@name='prices[EUR]']").send_keys('10')
    driver.find_element(By.XPATH, "//button[@name='save']").click()
    time.sleep(5)
    assert driver.find_element(By.XPATH, "//a[text()='new_product']") # проверяем, что товар появился в списке
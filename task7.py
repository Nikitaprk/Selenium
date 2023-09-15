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


def are_elements_present(driver, *args):
    return len(driver.find_elements(*args)) == 1


def test_blue_duck(driver):
    elem_1 = driver.find_element(By.XPATH, "//*[@id='box-most-popular']")
    elem_2 = elem_1.find_element(By.XPATH, ".//*[@href='http://localhost/litecart/en/rubber-ducks-c-1/blue-duck-p-4']")
    elem_3 = elem_2.find_elements(By.XPATH, ".//div[@class='sticker new']")
    assert len(elem_3) == 1


def test_purple_duck(driver):
    elem_1 = driver.find_element(By.XPATH, "//*[@id='box-most-popular']")
    elem_2 = elem_1.find_element(By.XPATH, ".//*[@href='http://localhost/litecart/en/rubber-ducks-c-1/purple-duck-p-5']")
    elem_3 = elem_2.find_elements(By.XPATH, ".//div[@class='sticker new']")
    assert len(elem_3) == 1


def test_red_duck(driver):
    elem_1 = driver.find_element(By.XPATH, "//*[@id='box-most-popular']")
    elem_2 = elem_1.find_element(By.XPATH, ".//*[@href='http://localhost/litecart/en/rubber-ducks-c-1/red-duck-p-3']")
    elem_3 = elem_2.find_elements(By.XPATH, ".//div[@class='sticker new']")
    assert len(elem_3) == 1


def test_green_duck(driver):
    elem_1 = driver.find_element(By.XPATH, "//*[@id='box-most-popular']")
    elem_2 = elem_1.find_element(By.XPATH, ".//*[@href='http://localhost/litecart/en/rubber-ducks-c-1/subcategory-c-2/green-duck-p-2']")
    elem_3 = elem_2.find_elements(By.XPATH, ".//div[@class='sticker new']")
    assert len(elem_3) == 1


def test_yellow_duck(driver):
    elem_1 = driver.find_element(By.XPATH, "//*[@id='box-most-popular']")
    elem_2 = elem_1.find_element(By.XPATH, ".//*[@href='http://localhost/litecart/en/rubber-ducks-c-1/subcategory-c-2/yellow-duck-p-1']")
    elem_3 = elem_2.find_elements(By.XPATH, ".//div[@class='sticker sale']")
    assert len(elem_3) == 1


def test_yellow_duck_campaigns(driver):
    elem_1 = driver.find_element(By.XPATH, "//*[@id='box-campaigns']")
    elem_2 = elem_1.find_element(By.XPATH, ".//*[@href='http://localhost/litecart/en/rubber-ducks-c-1/subcategory-c-2/yellow-duck-p-1']")
    elem_3 = elem_2.find_elements(By.XPATH, ".//div[@class='sticker sale']")
    assert len(elem_3) == 1


def test_yellow_duck_latest(driver):
    elem_1 = driver.find_element(By.XPATH, "//*[@id='box-latest-products']")
    elem_2 = elem_1.find_element(By.XPATH, ".//*[@href='http://localhost/litecart/en/rubber-ducks-c-1/subcategory-c-2/yellow-duck-p-1']")
    elem_3 = elem_2.find_elements(By.XPATH, ".//div[@class='sticker sale']")
    assert len(elem_3) == 1


def test_green_duck_latest(driver):
    elem_1 = driver.find_element(By.XPATH, "//*[@id='box-latest-products']")
    elem_2 = elem_1.find_element(By.XPATH, ".//*[@href='http://localhost/litecart/en/rubber-ducks-c-1/subcategory-c-2/green-duck-p-2']")
    elem_3 = elem_2.find_elements(By.XPATH, ".//div[@class='sticker new']")
    assert len(elem_3) == 1


def test_red_duck_latest(driver):
    elem_1 = driver.find_element(By.XPATH, "//*[@id='box-latest-products']")
    elem_2 = elem_1.find_element(By.XPATH, ".//*[@href='http://localhost/litecart/en/rubber-ducks-c-1/red-duck-p-3']")
    elem_3 = elem_2.find_elements(By.XPATH, ".//div[@class='sticker new']")
    assert len(elem_3) == 1


def test_blue_duck_latest(driver):
    elem_1 = driver.find_element(By.XPATH, "//*[@id='box-latest-products']")
    elem_2 = elem_1.find_element(By.XPATH, ".//*[@href='http://localhost/litecart/en/rubber-ducks-c-1/blue-duck-p-4']")
    elem_3 = elem_2.find_elements(By.XPATH, ".//div[@class='sticker new']")
    assert len(elem_3) == 1


def test_blue_purple_latest(driver):
    elem_1 = driver.find_element(By.XPATH, "//*[@id='box-latest-products']")
    elem_2 = elem_1.find_element(By.XPATH, ".//*[@href='http://localhost/litecart/en/rubber-ducks-c-1/purple-duck-p-5']")
    elem_3 = elem_2.find_elements(By.XPATH, ".//div[@class='sticker new']")
    assert len(elem_3) == 1

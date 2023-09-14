import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    chr_driver = webdriver.Chrome()
    chr_driver.get("http://localhost/litecart/admin/login.php")
    chr_driver.maximize_window()
    chr_driver.implicitly_wait(10)
    chr_driver.find_element(By.XPATH, "//input[@type='text']").send_keys('admin')
    chr_driver.find_element(By.XPATH, "//input[@type='password']").send_keys('admin')
    chr_driver.find_element(By.NAME, 'remember_me').click()
    chr_driver.find_element(By.NAME, 'login').click()
    return chr_driver


def test_appearence(driver):
    driver.find_element(By.XPATH, "//*[text()='Appearence']").click()
    driver.find_element(By.XPATH, "//*[text()='Template']").click()
    driver.find_element(By.XPATH, "//*[text()='Logotype']").click()
    assert driver.find_element(By.TAG_NAME, "h1").is_displayed()


def test_catalog(driver):
    driver.find_element(By.XPATH, "//span[text()='Catalog']").click()
    driver.find_element(By.XPATH, "//a[@href='http://localhost/litecart/admin/?app=catalog&doc=catalog']").click()
    driver.find_element(By.XPATH, "//*[text()='Product Groups']").click()
    driver.find_element(By.XPATH, "//*[text()='Option Groups']").click()
    driver.find_element(By.XPATH, "//*[text()='Manufacturers']").click()
    driver.find_element(By.XPATH, "//*[text()='Suppliers']").click()
    driver.find_element(By.XPATH, "//*[text()='Delivery Statuses']").click()
    driver.find_element(By.XPATH, "//*[text()='Sold Out Statuses']").click()
    driver.find_element(By.XPATH, "//*[text()='Quantity Units']").click()
    driver.find_element(By.XPATH, "//*[text()='CSV Import/Export']").click()
    assert driver.find_element(By.TAG_NAME, "h1").is_displayed()


def test_coutries(driver):
    driver.find_element(By.XPATH, "//*[text()='Countries']").click()
    assert driver.find_element(By.TAG_NAME, "h1").is_displayed()


def test_currencies(driver):
    driver.find_element(By.XPATH, "//*[text()='Currencies']").click()
    assert driver.find_element(By.TAG_NAME, "h1").is_displayed()


def test_customers(driver):
    driver.find_element(By.XPATH, "//*[text()='Customers']").click()
    driver.find_element(By.XPATH, "//li[@id='doc-customers']").click()
    driver.find_element(By.XPATH, "//*[text()='CSV Import/Export']").click()
    driver.find_element(By.XPATH, "//*[text()='Newsletter']").click()
    assert driver.find_element(By.TAG_NAME, "h1").is_displayed()


def test_geozones(driver):
    driver.find_element(By.XPATH, "//*[text()='Geo Zones']").click()
    assert driver.find_element(By.TAG_NAME, "h1").is_displayed()


def test_languages(driver):
    driver.find_element(By.XPATH, "//*[text()='Languages']").click()
    driver.find_element(By.ID, "doc-languages").click()
    driver.find_element(By.XPATH, "//*[text()='Storage Encoding']").click()
    assert driver.find_element(By.TAG_NAME, "h1").is_displayed()


def test_modules(driver):
    driver.find_element(By.XPATH, "//*[text()='Modules']").click()
    driver.find_element(By.XPATH, "//*[text()='Background Jobs']").click()
    driver.find_element(By.XPATH, "//*[text()='Customer']").click()
    driver.find_element(By.XPATH, "//*[text()='Shipping']").click()
    driver.find_element(By.XPATH, "//*[text()='Payment']").click()
    driver.find_element(By.XPATH, "//*[text()='Order Total']").click()
    driver.find_element(By.XPATH, "//*[text()='Order Success']").click()
    driver.find_element(By.XPATH, "//*[text()='Order Action']").click()
    assert driver.find_element(By.TAG_NAME, "h1").is_displayed()


def test_orders(driver):
    driver.find_element(By.XPATH, "//*[text()='Orders']").click()
    driver.find_element(By.ID, "doc-orders").click()
    driver.find_element(By.XPATH, "//*[text()='Order Statuses']").click()
    assert driver.find_element(By.TAG_NAME, "h1").is_displayed()


def test_pages(driver):
    driver.find_element(By.XPATH, "//*[text()='Pages']").click()
    assert driver.find_element(By.TAG_NAME, "h1").is_displayed()


def test_reports(driver):
    driver.find_element(By.XPATH, "//*[text()='Reports']").click()
    driver.find_element(By.XPATH, "//*[text()='Monthly Sales']").click()
    driver.find_element(By.XPATH, "//*[text()='Most Sold Products']").click()
    driver.find_element(By.XPATH, "//*[text()='Most Shopping Customers']").click()
    assert driver.find_element(By.TAG_NAME, "h1").is_displayed()


def test_settings(driver):
    driver.find_element(By.XPATH, "//*[text()='Settings']").click()
    driver.find_element(By.XPATH, "//*[text()='Store Info']").click()
    driver.find_element(By.XPATH, "//*[text()='Defaults']").click()
    driver.find_element(By.XPATH, "//*[text()='General']").click()
    driver.find_element(By.XPATH, "//*[text()='Listings']").click()
    driver.find_element(By.XPATH, "//*[text()='Images']").click()
    driver.find_element(By.XPATH, "//*[text()='Checkout']").click()
    driver.find_element(By.XPATH, "//*[text()='Advanced']").click()
    driver.find_element(By.XPATH, "//*[text()='Security']").click()
    assert driver.find_element(By.TAG_NAME, "h1").is_displayed()


def test_slides(driver):
    driver.find_element(By.XPATH, "//*[text()='Slides']").click()
    assert driver.find_element(By.TAG_NAME, "h1").is_displayed()


def test_tax(driver):
    driver.find_element(By.XPATH, "//*[text()='Tax']").click()
    driver.find_element(By.XPATH, "//*[text()='Tax Classes']").click()
    driver.find_element(By.XPATH, "//*[text()='Tax Rates']").click()
    assert driver.find_element(By.TAG_NAME, "h1").is_displayed()


def test_translations(driver):
    driver.find_element(By.XPATH, "//*[text()='Translations']").click()
    driver.find_element(By.XPATH, "//*[text()='Search Translations']").click()
    driver.find_element(By.XPATH, "//*[text()='Scan Files']").click()
    driver.find_element(By.XPATH, "//*[text()='CSV Import/Export']").click()
    assert driver.find_element(By.TAG_NAME, "h1").is_displayed()


def test_users(driver):
    driver.find_element(By.XPATH, "//*[text()='Users']").click()
    assert driver.find_element(By.TAG_NAME, "h1").is_displayed()


def test_vQmods(driver):
    driver.find_element(By.XPATH, "//*[text()='vQmods']").click()
    driver.find_element(By.ID, "doc-vqmods").click()
    assert driver.find_element(By.TAG_NAME, "h1").is_displayed()

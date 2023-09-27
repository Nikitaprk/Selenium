import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    chr_driver = webdriver.Chrome()
    #chr_driver = webdriver.Firefox()
    #chr_driver = webdriver.Edge()
    chr_driver.get("http://localhost/litecart/en/")
    chr_driver.maximize_window()
    chr_driver.implicitly_wait(2)
    return chr_driver


def test_ch(driver):
    elem = driver.find_element(By.XPATH, "//div[@id='box-campaigns']//li[starts-with(@class, 'product')]")
    #  берем конкретный первый товар исходя из трактовки задачи
    text = elem.find_element(By.XPATH, ".//div[@class='name']").get_attribute('textContent')
    regular_price = elem.find_element(By.XPATH, ".//s[@class='regular-price']").get_attribute('textContent')
    campaign_price = elem.find_element(By.XPATH, ".//strong[@class='campaign-price']").get_attribute('textContent')
    regular_price_cross = elem.find_element(By.XPATH, ".//s[@class='regular-price']").value_of_css_property('text-decoration')
    assert regular_price_cross == 'line-through solid rgb(119, 119, 119)' or 'line-through rgb(119, 119, 119)' # обычная цена зачеркнутая?

    regular_price_font = elem.find_element(By.XPATH, ".//s[@class='regular-price']").value_of_css_property('font-weight')
    campaign_price_font = elem.find_element(By.XPATH, ".//strong[@class='campaign-price']").value_of_css_property('font-weight')
    assert int(campaign_price_font)>int(regular_price_font) # сравниваем размер шрифта

    regular_price_color = elem.find_element(By.XPATH, ".//s[@class='regular-price']").value_of_css_property('color')
    assert regular_price_color == 'rgba(119, 119, 119, 1)' or 'rgba(119, 119, 119)' # обычная цена серая?
    campaign_price_color = elem.find_element(By.XPATH, ".//strong[@class='campaign-price']").value_of_css_property('color')
    assert campaign_price_color == 'rgba(204, 0, 0, 1)' or 'rgba(204, 0, 0' # цвет красный?

    elem.click()  # переходим на страницу товара

    inner_text = driver.find_element(By.XPATH, "//h1[@class='title']").get_attribute('textContent')
    inner_regular_price = driver.find_element(By.XPATH, "//s[@class='regular-price']").get_attribute('textContent')
    inner_campaign_price = driver.find_element(By.XPATH, "//strong[@class='campaign-price']").get_attribute('textContent')
    assert text == inner_text and regular_price == inner_regular_price and campaign_price == inner_campaign_price

    inner_regular_price_font = driver.find_element(By.XPATH, "//s[@class='regular-price']").value_of_css_property('font-weight')
    inner_campaign_price_font = driver.find_element(By.XPATH, "//strong[@class='campaign-price']").value_of_css_property('font-weight')
    assert int(inner_campaign_price_font)>int(inner_regular_price_font) # сравниваем размер шрифта на странице товара

    # сравниваем показатели текста и цены

    inner_regular_price_color = driver.find_element(By.XPATH, "//s[@class='regular-price']").value_of_css_property('color')
    assert inner_regular_price_color == 'rgba(102, 102, 102, 1)' or 'rgba(102, 102, 102)'
    inner_regular_campaign_color = driver.find_element(By.XPATH, "//strong[@class='campaign-price']").value_of_css_property('color')
    assert inner_regular_campaign_color == 'rgba(204, 0, 0, 1)' or 'rgba(204, 0, 0)'
    assert text == inner_text and regular_price == inner_regular_price and campaign_price == inner_campaign_price
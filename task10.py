import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
import ast

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
    assert regular_price_cross.startswith('line-through') # проверяем декоратор на наличия элемента зачеркивания текста

    regular_price_font = elem.find_element(By.XPATH, ".//s[@class='regular-price']").value_of_css_property('font-size')
    campaign_price_font = elem.find_element(By.XPATH, ".//strong[@class='campaign-price']").value_of_css_property('font-size')
    assert (ast.literal_eval(campaign_price_font[:-2])) > (ast.literal_eval(regular_price_font[:-2]))

    regular_price_color = elem.find_element(By.XPATH, ".//s[@class='regular-price']").value_of_css_property('color')
    try:
        red, green, blue,a= ast.literal_eval(regular_price_color.strip('rgba'))
        assert red == green == blue  # обычная цена серая?
    except:
        red, green, blue = ast.literal_eval(regular_price_color.strip('rgb'))
        assert red == green == blue  # обычная цена серая?
    campaign_price_color = elem.find_element(By.XPATH, ".//strong[@class='campaign-price']").value_of_css_property('color')
    try:
        red, green, blue,a= ast.literal_eval(campaign_price_color.strip('rgba'))
        assert green == 0 and blue == 0  # цвет красный?
    except:
        red, green, blue = ast.literal_eval(campaign_price_color.strip('rgb'))
        assert green == 0 and blue == 0  # цвет красный?

    elem.click()  # переходим на страницу товара

    inner_text = driver.find_element(By.XPATH, "//h1[@class='title']").get_attribute('textContent')
    inner_regular_price = driver.find_element(By.XPATH, "//s[@class='regular-price']").get_attribute('textContent')
    inner_campaign_price = driver.find_element(By.XPATH, "//strong[@class='campaign-price']").get_attribute('textContent')
    assert text == inner_text and regular_price == inner_regular_price and campaign_price == inner_campaign_price

    inner_regular_price_font = driver.find_element(By.XPATH, "//s[@class='regular-price']").value_of_css_property('font-size')
    inner_campaign_price_font = driver.find_element(By.XPATH, "//strong[@class='campaign-price']").value_of_css_property('font-size')
    # сравниваем размер шрифта на странице товара обрезая буквы "px", чтобы привести к числовому виду
    assert (ast.literal_eval(inner_campaign_price_font[:-2]))>(ast.literal_eval(inner_regular_price_font[:-2]))

    # сравниваем показатели текста и цены

    inner_regular_price_color = driver.find_element(By.XPATH, "//s[@class='regular-price']").value_of_css_property('color')
    try:
        red, green, blue,a= ast.literal_eval(inner_regular_price_color.strip('rgba'))
        assert red == green == blue  # цена серая?
    except:
        red, green, blue = ast.literal_eval(inner_regular_price_color.strip('rgb'))
        assert red == green == blue  # цена серая?
    inner_regular_campaign_color = driver.find_element(By.XPATH, "//strong[@class='campaign-price']").value_of_css_property('color')
    try:
        red, green, blue,a= ast.literal_eval(inner_regular_campaign_color.strip('rgba'))
        assert green == 0 and blue == 0  # цвет красный?
    except:
        red, green, blue= ast.literal_eval(inner_regular_campaign_color.strip('rgb'))
        assert green == 0 and blue == 0  # цвет красный?

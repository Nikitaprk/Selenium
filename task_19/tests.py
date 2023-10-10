#from conftest import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main_page import Main_page
from goods_page import Goods_page, CHECK_QUANTITY
from bin_page import Bin_page


main = Main_page()
goods_page = Goods_page()
bin_page = Bin_page()

# def test123(driver):
#     wait = WebDriverWait(driver, 3)
#     x = 1  # переменная для дальнейшего подсчета кол-во элементов в корзине
#     for i in range(3):
#         driver.find_element(By.XPATH, "//li[starts-with(@class, 'product')]").click()  # клик на первый попавшийся товар
#
#         if len(driver.find_elements(By.XPATH, "//select[@name='options[Size]']")) == 1:  # проверка на товар с опцией размера
#             driver.find_element(By.XPATH, "//select[@name='options[Size]']").click()
#             driver.find_element(By.XPATH, "//option[@value='Medium']").click()
#         driver.find_element(By.XPATH, "//button[@name='add_cart_product']").click()
#         wait.until(EC.text_to_be_present_in_element((By.XPATH, "//span[@class='quantity']"), str(x))) # ждем пока корзина не пополнится ровно на 1 товар
#         x += 1  # увеличиваем переменную для подсчета товаров в корзине на единицу
#         driver.find_element(By.XPATH, "//a[@href='http://localhost/litecart/en/']").click()
#
#         driver.find_element(By.XPATH, "//a[text()='Checkout »']").click()
#
#     elems = driver.find_elements(By.XPATH, "//td[@class='item']")  # список всех элементов на странице Checkout
#    # time.sleep(3) # добавил сюда ожидание для теста, чтобы было видно изначальное кол-во товаров на странице checkout, т.е первое удаление мгновенное
#     for q in range(len(elems)):
#         driver.find_element(By.XPATH, "//button[text()='Remove']").click()
#         wait.until(EC.staleness_of(elems[0]))  # ждем пока не пропадет элемент из списка
#         elems = driver.find_elements(By.XPATH, "//td[@class='item']")


def test1(driver):
    wait = WebDriverWait(driver, 3)
    x = 1
    for i in range(3):
        main.select_duck().click()
        if len(goods_page.check_if_yellow() == 1):
            goods_page.yellow_duck_size().click()
            goods_page.yellow_duck_choose_size().click()
        goods_page.add().click()
        wait.until(EC.text_to_be_present_in_element(CHECK_QUANTITY), str(x))
        x += 1
        goods_page.back_to_main().click()
        main.checkout().click()
    elems = bin_page.all_elements()
    for q in range(len(elems)):
        bin_page.remove_action()
        wait.until(EC.staleness_of(elems[0]))
        elems = bin_page.all_elements()


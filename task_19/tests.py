from main_page import Main_page
from goods_page import Goods_page
from bin_page import Bin_page


def test1(driver):
    main = Main_page(driver)
    goods_page = Goods_page(driver)
    bin_page = Bin_page(driver)
    x = 1
    for i in range(3):
        main.select_duck()
        if len(goods_page.check_if_yellow()) == 1:
            goods_page.yellow_duck_size()
            goods_page.yellow_duck_choose_size()
        goods_page.add_to_cart(x)  # передаем значение х для проверки значения около корзины для ожидания его появления
        x += 1
        goods_page.back_to_main()
    main.get_to_checkout()
    elems = bin_page.get_all_elements()
    for q in range(len(elems)):
        bin_page.remove_action(elems)
        elems = bin_page.get_all_elements()


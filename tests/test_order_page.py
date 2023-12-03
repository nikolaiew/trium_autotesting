import pytest
from ..pages.base_page import BasePage
from ..pages.order_page import OrderPage
from ..pages.signup_login_page import SignupLoginPage
from ..settings import sets


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.order_page
class TestOrderPage:

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.PROD_SERVER)
        page.open()
        # page.scroll_page(600, 3)  # тест методу для багаторазового скролінгу
        # page.make_screenshot('scr1')  # тест методу для скріншотів

    def test_login_to_cabinet(self, browser):
        page = SignupLoginPage(browser, sets.PROD_SERVER)
        page.click_account_button()
        page.click_login_button()
        page.is_h1_login()
        page.input_data_for_login(sets.TEST_EMAIL, sets.PASSWORD)
        page.click_enter_button()
        page.is_h2_login()
        page.explicitly_wait(2)
        page = OrderPage(browser, sets.PROD_SERVER)
        page.click_on_logo()

    def test_clean_cart_in_header(self, browser):
        page = OrderPage(browser, sets.PROD_SERVER)
        page.clean_cart_in_header()

    def test_add_cat_item_to_cart(self, browser):
        page = OrderPage(browser, sets.PROD_SERVER)
        global cat_item_price
        cat_item_price = page.add_cat_item_to_cart()
        page.explicitly_wait(sets.DEMO_DELAY)  # Демо-затримка
        page.scroll(400)                                     # скролл для зручності перегляду

    def test_plus_qty(self, browser):
        page = OrderPage(browser, sets.PROD_SERVER)
        page.check_qty(page.plus_qty(qty=2))

    def test_minus_qty(self, browser):
        page = OrderPage(browser, sets.PROD_SERVER)
        page.check_qty(page.minus_qty(qty=1))
        page.explicitly_wait(sets.DEMO_DELAY)  # Демо-затримка

    def test_item_price(self, browser):
        page = OrderPage(browser, sets.PROD_SERVER)
        page.check_item_price(cat_item_price)

    def test_item_sum(self, browser):
        page = OrderPage(browser, sets.PROD_SERVER)
        page.check_item_sum()

    def test_add_pop_item_to_cart(self, browser):
        page = OrderPage(browser, sets.PROD_SERVER)
        page.click_on_logo()
        page.add_pop_item_to_cart()
        page.scroll(400)                                     # скролл для зручності перегляду
        page.explicitly_wait(4)

    def test_del_item_from_cart(self, browser):
        page = OrderPage(browser, sets.PROD_SERVER)
        page.check_del_item()

    def test_add_bv_item_to_cart(self, browser):
        page = OrderPage(browser, sets.PROD_SERVER)
        page.click_on_logo()
        page.add_bv_item_to_cart()
        page.scroll(400)                                     # скролл для зручності перегляду
        page.explicitly_wait(4)

    def test_check_amount(self, browser):
        page = OrderPage(browser, sets.PROD_SERVER)
        page.check_amount()

    def test_input_data_for_order(self, browser):
        page = OrderPage(browser, sets.PROD_SERVER)
        page.input_data_for_order(sets.FIRSTNAME, sets.LASTNAME, sets.PHONE, sets.CITY, sets.ADDRESS)
        # page.scroll(200)
        page.explicitly_wait(5)

    # def test_checkout(self, browser):                         # тест виконання реального замовлення
    #     # self.link_to_cabinet = browser.current_url              # варіант викладача
    #     # page = SignupLoginPage(browser, self.link_to_cabinet)   # варіант викладача
    #     page = OrderPage(browser, sets.PROD_SERVER)               # стандартний варіант
    #     page.checkout()
    #     page.explicitly_wait(10)



from ..pages import base_page, locators
from ..settings import sets
import inspect


class OrderPage(base_page.BasePage):

    def click_on_logo(self):
        assert self.click_element(*locators.BasePageLocators.LOGO_HEADER), \
            "The element LOGO HEADER is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def add_cat_item_to_cart(self):
        assert self.click_element(*locators.BasePageLocators.VSI_KATEGORII), \
            "The menu 'ВСІ КАТЕГОРІЇ' is not present or intractable"
        self.explicitly_wait(sets.DEMO_DELAY)  # Демо-затримка
        assert self.click_element(*locators.BasePageLocators.AKSESUARY), \
            "The category 'Аксесуари ...' is not present or intractable"
        self.explicitly_wait(sets.DEMO_DELAY)  # Демо-затримка
        assert self.click_element(*locators.BasePageLocators.MYSHKY), \
            "The category 'Мишки' is not present or intractable"
        self.scroll_page(800)  # для firefox
        self.explicitly_wait(sets.DEMO_DELAY)  # Демо-затримка
        price = int(self.get_text(*locators.CategoryPageLocators.MYSHKA_12_PRICE)[:-4])  # 130
        assert self.hover_actions(*locators.CategoryPageLocators.MYSHKA_12), \
            "The item MYSHKA_12 is not present or intractable"
        self.explicitly_wait(sets.DEMO_DELAY)  # Демо-затримка
        assert self.click_element(*locators.CategoryPageLocators.MYSHKA_12_ADD_TO_CART), \
            "The button ADD_TO_CART is not present or intractable"
        self.explicitly_wait(sets.DEMO_DELAY)  # Демо-затримка
        assert self.click_element(*locators.CategoryPageLocators.TO_CHECKOUT_BUTTON), \
            "The button 'Оформити замовлення' is not present or intractable"
        print(f"\n{inspect.currentframe().f_code.co_name} - Ok  [myshka_1_price = {price}]")
        if price:
            return price

    def plus_qty(self, qty):
        start_qty = int(self.get_attribute(*locators.OrderPageLocators.ITEM_1_QTY, "value"))
        for i in range(0, qty):
            self.explicitly_wait(2)
            assert self.click_element(*locators.OrderPageLocators.ITEM_1_QTY_PLUS), \
                "The button '+' is not present or intractable"
        print(f"\n{inspect.currentframe().f_code.co_name} - Ok [{start_qty}+{qty}]")
        return start_qty + qty

    def minus_qty(self, qty):
        start_qty = int(self.get_attribute(*locators.OrderPageLocators.ITEM_1_QTY, "value"))
        for i in range(0, qty):
            self.explicitly_wait(2)
            assert self.click_element(*locators.OrderPageLocators.ITEM_1_QTY_MINUS), \
                "The button '-' is not present or intractable"
        print(f"\n{inspect.currentframe().f_code.co_name} - Ok [{start_qty}-{qty}]")
        return start_qty - qty

    def check_qty(self, qty):
        qty_actual = int(self.get_attribute(*locators.OrderPageLocators.ITEM_1_QTY, "value"))
        assert qty == qty_actual, \
            "QTY doesn't match to actual"
        print(f"{inspect.currentframe().f_code.co_name} - Ok [{qty}={qty_actual}]")

    def check_item_price(self, item_price):
        cart_price = int(self.get_text(*locators.OrderPageLocators.ITEM_1_PRICE)[:-4])
        assert item_price == cart_price, \
            "PRICE doesn't match to actual"
        print(f"\n{inspect.currentframe().f_code.co_name} - Ok [{item_price}={cart_price}]")

    def check_item_sum(self):
        cart_price = int(self.get_text(*locators.OrderPageLocators.ITEM_1_PRICE)[:-4])
        cart_qty = int(self.get_attribute(*locators.OrderPageLocators.ITEM_1_QTY, "value"))
        cart_sum = int(self.get_text(*locators.OrderPageLocators.ITEM_1_SUM)[:-4])
        assert (cart_price * cart_qty) == cart_sum, \
            "SUM doesn't match to actual"
        print(f"\n{inspect.currentframe().f_code.co_name} - Ok [{cart_price}*{cart_qty}={cart_sum}]")

    def add_pop_item_to_cart(self):
        self.scroll_page(1400)  # для firefox
        self.explicitly_wait(2)
        assert self.hover_actions(*locators.MainPageLocators.POPULAR_7), \
            "The item POPULAR_7 is not present or intractable"
        self.explicitly_wait(sets.DEMO_DELAY)  # Демо-затримка
        assert self.click_element(*locators.MainPageLocators.POPULAR_7_ADD_TO_CART), \
            "The button ADD_TO_CART is not present or intractable"
        self.explicitly_wait(sets.DEMO_DELAY)  # Демо-затримка
        assert self.click_element(*locators.CategoryPageLocators.TO_CHECKOUT_BUTTON), \
            "The button 'Оформити замовлення' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def check_del_item(self):
        try: start_qty_of_items = self.qty_of_elements(*locators.OrderPageLocators.QTY_OF_ITEMS)
        except: print("ERROR: no items to delete - the cart is empty")
        assert self.click_element(*locators.OrderPageLocators.ITEM_1_DEL), \
            "The button 'x' is not present or intractable"
        self.explicitly_wait(2)
        try: actual_qty_of_items = self.qty_of_elements(*locators.OrderPageLocators.QTY_OF_ITEMS)
        except: print("Something wrong")
        assert (start_qty_of_items - 1) == actual_qty_of_items, \
            "QTY OF ITEMS doesn't match to actual"
        print(f"\n{inspect.currentframe().f_code.co_name} - Ok [{start_qty_of_items}-1={actual_qty_of_items}]")

    def add_bv_item_to_cart(self):
        self.scroll_page(1600)  # для firefox
        self.explicitly_wait(sets.DEMO_DELAY)  # Демо-затримка
        assert self.click_element(*locators.MainPageLocators.BV_BLOKY_ZHYVLENNIA), \
            "The category 'БЛОКИ ЖИВЛЕННЯ ... Б/В' is not present or intractable"
        self.explicitly_wait(sets.DEMO_DELAY)  # Демо-затримка
        assert self.click_element(*locators.MainPageLocators.BV_BLOKY_ZHYVLENNIA_5), \
            "The item BLOKY_ZHYVLENNIA_5 is not present or intractable"
        self.explicitly_wait(sets.DEMO_DELAY)  # Демо-затримка
        assert self.click_element(*locators.ProductPageLocator.ADD_TO_CART), \
            "The button 'Додати до кошика' is not present or intractable"
        self.explicitly_wait(sets.DEMO_DELAY)  # Демо-затримка
        assert self.click_element(*locators.CategoryPageLocators.TO_CHECKOUT_BUTTON), \
            "The button 'Оформити замовлення' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def check_amount(self):
        item_1_sum = int(self.get_text(*locators.OrderPageLocators.ITEM_1_SUM)[:-4])  # 700
        item_2_sum = int(self.get_text(*locators.OrderPageLocators.ITEM_2_SUM)[:-4])  # 260
        items_amount = int(self.get_text(*locators.OrderPageLocators.AMOUNT_OF_ITEMS)[:-4])  # 960
        assert (item_1_sum + item_2_sum) == items_amount, \
            "AMOUNT doesn't match to actual"
        print(f"\n{inspect.currentframe().f_code.co_name} - Ok [{item_1_sum}+{item_2_sum}={items_amount}]")

    def input_data_for_order(self, fname, lname, phone, city, address):
        assert self.click_element(*locators.OrderPageLocators.NEW_PAYMENT_ADDRESS_RADIO_BUTTON), \
            "The radio button 'Я хочу використовувати нову адресу' is not present or intractable"
        assert self.input_data(*locators.OrderPageLocators.FIRSTNAME_INPUT, fname), \
            "The input 'Ім\'я' is not present"
        assert self.input_data(*locators.OrderPageLocators.LASTNAME_INPUT, lname), \
            "The input 'Прізвище' is not present"
        assert self.input_data(*locators.OrderPageLocators.PHONE_INPUT, phone), \
            "The input 'E-Mail' is not present"
        assert self.click_element(*locators.OrderPageLocators.REGION_INPUT), \
            "The pull-down menu 'Регіон' is not present"
        assert self.input_data(*locators.OrderPageLocators.CITY_INPUT, city), \
            "The input 'Місто' is not present"
        assert self.input_data(*locators.OrderPageLocators.ADDRESS_INPUT, address), \
            "The input 'Адреса' is not present"
        self.explicitly_wait(sets.DEMO_DELAY)  # Демо-затримка
        assert self.click_element(*locators.OrderPageLocators.SAMOVYVIZ_RADIO_BUTTON), \
            "The radio button 'Самовивіз ...' is not present or intractable"
        self.explicitly_wait(sets.DEMO_DELAY)  # Демо-затримка
        assert self.click_element(*locators.OrderPageLocators.CASH_RADIO_BUTTON), \
            "The radio button 'Оплата готівкою' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def checkout(self):
        assert self.click_element(*locators.OrderPageLocators.CHECKOUT_BUTTON), \
            "The button 'Продовжити' is not present or intractable"

    def is_checkout_success(self):
        assert self.is_element_present(*locators.OrderPageLocators.CHECKOUT_SUCCESS_MESSAGE), \
            "The header 'Ваше замовлення прийняте!' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")


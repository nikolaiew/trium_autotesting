from ..pages import base_page, locators
import inspect


class MainPage(base_page.BasePage):

    def is_logo(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGO), \
            "The element LOGO is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - Ok")

    def is_search_category(self):
        assert self.is_element_present(*locators.BasePageLocators.SEARCH_CATEGORY), \
            "The drop-down menu 'Категорії' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_search_category_web_cameras(self):
        assert self.click_element(*locators.BasePageLocators.SEARCH_CATEGORY), \
            "The drop-down menu 'Категорії' is not present"
        assert self.is_element_present(*locators.BasePageLocators.SEARCH_CATEGORY_WEB_CAMERAS), \
            "The section 'Веб-камери' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_search_input(self):
        assert self.is_element_present(*locators.BasePageLocators.SEARCH_INPUT), \
            "The input field 'Пошук' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_search_button(self):
        assert self.is_element_present(*locators.BasePageLocators.SEARCH_BUTTON), \
            "The button 'Пошук' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_account_button(self):
        assert self.is_element_present(*locators.BasePageLocators.ACCOUNT_BUTTON), \
            "The button 'Кабінет' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_compare_button(self):
        assert self.is_element_present(*locators.BasePageLocators.COMPARE_BUTTON), \
            "The button 'Порівняння' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_cart_button(self):
        assert self.is_element_present(*locators.BasePageLocators.CART_BUTTON), \
            "The button CART is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_language_button(self):
        assert self.is_element_present(*locators.BasePageLocators.LANGUAGE_BUTTON), \
            "The button 'Мова' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_language_ua_button(self):
        assert self.click_element(*locators.BasePageLocators.LANGUAGE_BUTTON), \
            "The button 'Мова' is not present"
        assert self.is_element_present(*locators.BasePageLocators.LANGUAGE_UA_BUTTON), \
            "The button 'Українська' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_language_ru_button(self):
        assert self.click_element(*locators.BasePageLocators.LANGUAGE_BUTTON), \
            "The button 'Мова' is not present"
        assert self.is_element_present(*locators.BasePageLocators.LANGUAGE_RU_BUTTON), \
            "The button 'Русский' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_phone(self):
        assert self.is_element_present(*locators.BasePageLocators.PHONE), \
            "The element PHONE NUMBER is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_mail_to(self):
        assert self.is_element_present(*locators.BasePageLocators.MAIL_TO), \
            "The element MAIL TO is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_vsi_kategorii(self):
        assert self.is_element_present(*locators.BasePageLocators.VSI_KATEGORII), \
            "The drop-down menu 'ВСІ КАТЕГОРІЇ' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_vsi_kategorii_myshky(self):
        assert self.click_element(*locators.BasePageLocators.VSI_KATEGORII), \
            "The drop-down menu 'ВСІ КАТЕГОРІЇ' is not present"
        assert self.click_element(*locators.BasePageLocators.AKSESUARY), \
            "The section 'Аксесуари для ноутбуків та ПК' is not present"
        assert self.is_element_present(*locators.BasePageLocators.MYSHKY), \
            "The section 'Мишки' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_golovna_button(self):
        assert self.is_element_present(*locators.BasePageLocators.GOLOVNA), \
            "The button 'ГОЛОВНА' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_pro_nas_button(self):
        assert self.is_element_present(*locators.BasePageLocators.PRO_NAS), \
            "The button 'ПРО НАС' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_dostavka_button(self):
        assert self.is_element_present(*locators.BasePageLocators.DOSTAVKA), \
            "The button 'ДОСТАВКА' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_oplata_button(self):
        assert self.is_element_present(*locators.BasePageLocators.OPLATA), \
            "The button 'ОПЛАТА' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_blog_button(self):
        assert self.is_element_present(*locators.BasePageLocators.BLOG), \
            "The button 'БЛОГ' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_kontakty_button(self):
        assert self.is_element_present(*locators.BasePageLocators.KONTAKTY), \
            "The button 'КОНТАКТИ' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_akcii_button(self):
        assert self.is_element_present(*locators.BasePageLocators.AKCII), \
            "The button 'АКЦІІ' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")


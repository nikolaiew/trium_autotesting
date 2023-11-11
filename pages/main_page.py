from ..pages import base_page, locators
import inspect


class MainPage(base_page.BasePage):

# header
    def is_logo_header(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGO_HEADER), \
            "The element LOGO is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - Ok")

    def is_search_cat(self):
        assert self.is_element_present(*locators.BasePageLocators.SEARCH_CATEGORY), \
            "The drop-down menu 'Категорії' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_search_cat_web_cameras(self):
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
        assert self.is_element_present(*locators.BasePageLocators.GOLOVNA_BUTTON), \
            "The button 'ГОЛОВНА' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_pro_nas_button(self):
        assert self.is_element_present(*locators.BasePageLocators.PRO_NAS_BUTTON), \
            "The button 'ПРО НАС' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_dostavka_button(self):
        assert self.is_element_present(*locators.BasePageLocators.DOSTAVKA_BUTTON), \
            "The button 'ДОСТАВКА' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_oplata_button(self):
        assert self.is_element_present(*locators.BasePageLocators.OPLATA_BUTTON), \
            "The button 'ОПЛАТА' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_blog_button(self):
        assert self.is_element_present(*locators.BasePageLocators.BLOG_BUTTON), \
            "The button 'БЛОГ' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_kontakty_button(self):
        assert self.is_element_present(*locators.BasePageLocators.KONTAKTY_BUTTON), \
            "The button 'КОНТАКТИ' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_akcii_button(self):
        assert self.is_element_present(*locators.BasePageLocators.AKCII_BUTTON), \
            "The button 'АКЦІІ' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

# body
    def is_main_slider(self):
        assert self.is_element_present(*locators.MainPageLocators.MAIN_SLIDER), \
            "The MAIN SLIDER is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_main_cat_left_button(self):
        assert self.is_element_present(*locators.MainPageLocators.MAIN_CAT_LEFT), \
            "The button 'Категорії' LEFT is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_main_cat_right_button(self):
        assert self.is_element_present(*locators.MainPageLocators.MAIN_CAT_RIGHT), \
            "The button 'Категорії' RIGHT is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_main_cat_panel(self):
        assert self.is_element_present(*locators.MainPageLocators.MAIN_CAT_PANEL), \
            "The panel 'Категорії' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_main_cat_items_qty(self):
        assert self.qty_of_elements(*locators.MainPageLocators.MAIN_CAT_ITEMS) == 25, \
            "The quantity of 'Категорії' items is not right"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_popular_panel(self):
        assert self.is_element_present(*locators.MainPageLocators.POPULAR_PANEL), \
            "The panel 'Популярні продукти' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_popular_7(self):
        assert self.is_element_present(*locators.MainPageLocators.POPULAR_7), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_banner(self):
        assert self.is_element_present(*locators.MainPageLocators.BANNER), \
            "The BANNER is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_bv_noutbuky(self):
        assert self.is_element_present(*locators.MainPageLocators.BV_NOUTBUKY), \
            "The button 'НОУТБУКИ Б/В' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_bv_bloky_zhyvlennia(self):
        assert self.is_element_present(*locators.MainPageLocators.BV_BLOKY_ZHYVLENNIA), \
            "The button 'БЛОКИ ЖИВЛЕННЯ... Б/В' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_bv_komplekt(self):
        assert self.is_element_present(*locators.MainPageLocators.BV_KOMPLEKT), \
            "The button 'КОМПЛЕКТ... Б/В' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_bv_sys_bloky(self):
        assert self.is_element_present(*locators.MainPageLocators.BV_SYS_BLOKY), \
            "The button 'СИСТЕМНІ БЛОКИ Б/В' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_bv_monobloky(self):
        assert self.is_element_present(*locators.MainPageLocators.BV_MONOBLOKY), \
            "The button 'МОНОБЛОКИ... Б/В' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_bv_monitory(self):
        assert self.is_element_present(*locators.MainPageLocators.BV_MONITORY), \
            "The button 'МОНІТОРИ Б/В' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_bv_zapchastyny(self):
        assert self.is_element_present(*locators.MainPageLocators.BV_ZAPCHASTYNY), \
            "The button 'ЗАПЧАСТИНИ... Б/В' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_bv_sys_bloky_6(self):
        assert self.is_element_present(*locators.MainPageLocators.BV_SYS_BLOKY_6), \
            "The element 'СИСТЕМНІ БЛОКИ Б/В #6' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_articles_qty(self):
        assert self.qty_of_elements(*locators.MainPageLocators.ARTICLES) == 3, \
            "The quantity of 'Останні статті' items is not right"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_text_block(self):
        assert self.is_element_present(*locators.MainPageLocators.TEXT_BLOCK), \
            "The TEXT BLOCK is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

# footer
    def is_logo_footer(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGO_FOOTER), \
            "The element LOGO FOOTER is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - Ok")

    def is_pro_nas_footer_button(self):
        assert self.is_element_present(*locators.BasePageLocators.PRO_NAS_FOOTER_BUTTON), \
            "The button 'ПРО НАС' (footer) is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_dostavka_footer_button(self):
        assert self.is_element_present(*locators.BasePageLocators.DOSTAVKA_FOOTER_BUTTON), \
            "The button 'ДОСТАВКА' (footer) is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_oplata_footer_button(self):
        assert self.is_element_present(*locators.BasePageLocators.OPLATA_FOOTER_BUTTON), \
            "The button 'ОПЛАТА' (footer) is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_blog_footer_button(self):
        assert self.is_element_present(*locators.BasePageLocators.BLOG_FOOTER_BUTTON), \
            "The button 'БЛОГ' (footer) is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_kontakty_footer_button(self):
        assert self.is_element_present(*locators.BasePageLocators.KONTAKTY_FOOTER_BUTTON), \
            "The button 'КОНТАКТИ' (footer) is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_noutbuky_bv_footer_button(self):
        assert self.is_element_present(*locators.BasePageLocators.NOUTBUKY_BV_FOOTER), \
            "The button 'Ноутбуки б/в' (footer) is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_monitory_bv_footer_button(self):
        assert self.is_element_present(*locators.BasePageLocators.MONITORY_BV_FOOTER), \
            "The button 'Монітори б/в' (footer) is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_komplekt_bv_footer_button(self):
        assert self.is_element_present(*locators.BasePageLocators.KOMPLEKT_BV_FOOTER), \
            "The button 'Комплекти... б/в' (footer) is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_sys_blok_bv_footer_button(self):
        assert self.is_element_present(*locators.BasePageLocators.SYS_BLOK_BV_FOOTER), \
            "The button 'Системний блок б/в' (footer) is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_zapchastyny_footer_button(self):
        assert self.is_element_present(*locators.BasePageLocators.ZAPCHASTYNY_FOOTER), \
            "The button 'Запчастини б/в' (footer) is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

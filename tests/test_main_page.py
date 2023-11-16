import pytest
from ..pages.base_page import BasePage
from ..pages.main_page import MainPage
from ..settings import sets


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.main_page
class aTestMainPage:

    def setup_method(self):
        pass

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.PROD_SERVER)
        page.open()

    def test_main_page_header(self, browser):
        # self.link_to_cabinet = browser.current_url      # варіант викладача
        # page = MainPage(browser, self.link_to_cabinet)  # варіант викладача
        page = MainPage(browser, sets.PROD_SERVER)        # стандартний варіант
        page.is_logo_header()
        page.is_search_cat()
        page.is_search_cat_web_cameras()
        page.is_search_input()
        page.is_search_button()
        page.is_account_button()
        page.is_signup_button()
        page.is_login_button()
        page.is_compare_button()
        page.is_cart_button()
        page.is_language_button()
        page.is_language_ua_button()
        page.is_language_ru_button()
        page.is_phone()
        page.is_mail_to()
        page.is_vsi_kategorii()
        page.is_vsi_kategorii_myshky()
        page.is_golovna_button()
        page.is_pro_nas_button()
        page.is_dostavka_button()
        page.is_oplata_button()
        page.is_blog_button()
        page.is_kontakty_button()
        page.is_akcii_button()

    def test_main_page_body(self, browser):
        # self.link_to_cabinet = browser.current_url      # варіант викладача
        # page = MainPage(browser, self.link_to_cabinet)  # варіант викладача
        page = MainPage(browser, sets.PROD_SERVER)        # стандартний варіант
        page.is_main_slider()
        page.is_main_cat_left_button()
        page.is_main_cat_right_button()
        page.is_main_cat_panel()
        page.is_main_cat_items_qty()  # qty
        page.is_popular_panel()
        page.is_popular_7()
        page.is_banner()
        page.is_bv_noutbuky()
        page.is_bv_bloky_zhyvlennia()
        page.is_bv_komplekt()
        page.is_bv_sys_bloky()
        page.is_bv_monobloky()
        page.is_bv_monitory()
        page.is_bv_zapchastyny()
        page.is_bv_sys_bloky_6()

    def test_main_page_footer(self, browser):
        # self.link_to_cabinet = browser.current_url      # варіант викладача
        # page = MainPage(browser, self.link_to_cabinet)  # варіант викладача
        page = MainPage(browser, sets.PROD_SERVER)        # стандартний варіант
        page.is_logo_footer()
        page.is_pro_nas_footer_button()
        page.is_dostavka_footer_button()
        page.is_oplata_footer_button()
        page.is_blog_footer_button()
        page.is_kontakty_footer_button()
        page.is_noutbuky_bv_footer_button()
        page.is_monitory_bv_footer_button()
        page.is_komplekt_bv_footer_button()
        page.is_sys_blok_bv_footer_button()
        page.is_zapchastyny_footer_button()


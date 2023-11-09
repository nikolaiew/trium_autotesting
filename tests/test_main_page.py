import pytest
from ..pages.base_page import BasePage
from ..pages.main_page import MainPage
from ..settings import sets


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.main_page
class TestMainPage:

    # def setup_method(self):  # якась заглушка? (запитати)
    #     pass

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.PROD_SERVER)
        page.open()

    def test_main_page_header(self, browser):
        # self.link_to_cabinet = browser.current_url      # варіант викладача
        # page = MainPage(browser, self.link_to_cabinet)  # варіант викладача
        page = MainPage(browser, sets.PROD_SERVER)        # стандартний варіант
        page.is_logo_header()
        page.is_search_category()
        page.is_search_category_web_cameras()
        page.is_search_input()
        page.is_search_button()
        page.is_account_button()
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




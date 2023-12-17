import pytest
from ..pages.base_page import BasePage
from ..pages.search_page import SearchPage
from ..settings import sets


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.search_page
class TestSearchPage:

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.PROD_SERVER)
        page.open()

    def test_search_match(self, browser):
        search_word = 'інвертор'
        page = SearchPage(browser, sets.PROD_SERVER)
        page.search_input(search_word)
        page.explicitly_wait(sets.DEMO_DELAY)  # Демо-затримка
        page.search_match_checking(search_word)


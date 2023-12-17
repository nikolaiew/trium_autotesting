from ..pages import base_page, locators
from ..settings import sets
import inspect


class SearchPage(base_page.BasePage):

    def search_input(self, search_1):
        assert self.input_data(*locators.BasePageLocators.SEARCH_INPUT, search_1), \
            "The SEARCH input field is not present or intractable"
        assert self.click_element(*locators.BasePageLocators.SEARCH_BUTTON), \
            "The button SEARCH is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def search_match_checking(self, search_1):
        self.explicitly_wait(2)
        assert self.are_elements_present(*locators.SearchPageLocators.SEARCH_PANEL_ITEMS), \
            "The elements of SEARCH PANEL is not present"
        search_items_qty = self.qty_of_elements(*locators.SearchPageLocators.SEARCH_PANEL_ITEMS)
        if search_items_qty < 5:
            qty = search_items_qty
        else:
            qty = 5
        for i in range(5):
            assert self.is_element_present(*locators.SearchPageLocators.SEARCH_PANEL_ITEM[i]), \
                "The element SEARCH_PANEL_ITEM_1 is not present"
            assert search_1 in self.get_text(*locators.SearchPageLocators.SEARCH_PANEL_ITEM[i]).lower(), \
                f"The element SEARCH_PANEL_ITEM_{i} is not equal to search"
        print(f"{inspect.currentframe().f_code.co_name} - Ok [{search_items_qty}, {search_1}]")

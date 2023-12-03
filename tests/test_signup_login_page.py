import pytest
import random
from ..pages.base_page import BasePage
from ..pages.signup_login_page import SignupLoginPage
from ..settings import sets


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.signup_login_page
class TestSignupLoginPage:

    def setup_method(self):
        hash_name = 'test_' + ("%032x" % random.getrandbits(128))[:6]
        self.email_for_signup = f"{hash_name}@mail.com"

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.PROD_SERVER)
        page.open()

    def test_signup(self, browser):
        page = SignupLoginPage(browser, sets.PROD_SERVER)
        page.click_account_button()
        page.explicitly_wait(sets.DEMO_DELAY)  # Демо-затримка
        page.click_signup_button()
        page.is_h1_signup()
        page.input_data_for_signup(sets.FIRSTNAME, sets.LASTNAME, self.email_for_signup, sets.PHONE, sets.PASSWORD)
        page.click_politics_checkbox()
        page.explicitly_wait(5)
        page.click_create_account_button()
        page.is_signup_success()
        page.explicitly_wait(5)

    def test_logout(self, browser):
        page = SignupLoginPage(browser, sets.PROD_SERVER)
        page.click_account_button()
        page.explicitly_wait(sets.DEMO_DELAY)  # Демо-затримка
        page.click_logout_button()
        page.is_h1_logout()
        page.explicitly_wait(5)

    def test_login(self, browser):
        page = SignupLoginPage(browser, sets.PROD_SERVER)
        page.click_account_button()
        page.explicitly_wait(sets.DEMO_DELAY)  # Демо-затримка
        page.click_login_button()
        page.is_h1_login()
        page.input_data_for_login(sets.TEST_EMAIL, sets.PASSWORD)
        page.explicitly_wait(3)
        page.click_enter_button()
        page.is_h2_login()
        page.explicitly_wait(5)


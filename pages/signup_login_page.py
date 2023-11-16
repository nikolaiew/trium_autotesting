from ..pages import base_page, locators
import inspect


class SignupLoginPage(base_page.BasePage):

    def click_account_button(self):
        assert self.click_element(*locators.BasePageLocators.ACCOUNT_BUTTON), \
            "The button 'Кабінет' is not present or intractable"
        print(f"\n{inspect.currentframe().f_code.co_name} - Ok")

    def click_signup_button(self):
        assert self.click_element(*locators.BasePageLocators.SIGNUP_BUTTON), \
            "The button 'Реєстрація' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_h1_signup(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.H1_SIGNUP), \
            "The header 'РЕЄСТРАЦІЯ' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def input_data_for_signup(self, fname, lname, email, phone, password):
        assert self.input_data(*locators.SignupLoginPageLocators.FIRSTNAME_INPUT, fname), \
            "The input 'Ім\'я' is not present"
        assert self.input_data(*locators.SignupLoginPageLocators.LASTNAME_INPUT, lname), \
            "The input 'Прізвище' is not present"
        assert self.input_data(*locators.SignupLoginPageLocators.EMAIL_INPUT, email), \
            "The input 'E-Mail' is not present"
        assert self.input_data(*locators.SignupLoginPageLocators.PHONE_INPUT, phone), \
            "The input 'Телефон' is not present"
        assert self.input_data(*locators.SignupLoginPageLocators.PASSWORD_INPUT, password), \
            "The input 'Пароль' is not present"
        assert self.input_data(*locators.SignupLoginPageLocators.CONFIRM_INPUT, password), \
            "The input 'Підтвердження пароля' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok [email: {email}]")

    def click_politics_checkbox(self):
        assert self.click_element(*locators.SignupLoginPageLocators.POLITICS_CHECKBOX), \
            "The checkbox 'Я прочитав... і згоден...' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def click_create_account_button(self):
        assert self.click_element(*locators.SignupLoginPageLocators.PRODOVZHYTY_BUTTON), \
            "The button 'Продовжити' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_signup_success(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.SIGNUP_SUCCESS_MESSAGE), \
            "The header 'Ваш обліковий запис створено!' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def click_logout_button(self):
        assert self.click_element(*locators.BasePageLocators.LOGOUT_BUTTON), \
            "The button 'Вихід' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_h1_logout(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.H1_LOGOUT), \
            "The header 'ВИХІД' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def click_login_button(self):
        assert self.click_element(*locators.BasePageLocators.LOGIN_BUTTON), \
            "The button 'Авторизація' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_h1_login(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.H1_LOGIN), \
            "The header 'ЗАРЕЄСТРОВАНИЙ КЛІЄНТ' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def input_data_for_login(self, email, password):
        assert self.input_data(*locators.SignupLoginPageLocators.EMAIL_INPUT, email), \
            "The input 'E-Mail' is not present"
        assert self.input_data(*locators.SignupLoginPageLocators.PASSWORD_INPUT, password), \
            "The input 'Пароль' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok [email: {email}]")

    def click_enter_button(self):
        assert self.click_element(*locators.SignupLoginPageLocators.SUBMIT_BUTTON), \
            "The button 'Увійти' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_h2_login(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.H2_LOGIN), \
            "The header 'Мій обліковий запис' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")


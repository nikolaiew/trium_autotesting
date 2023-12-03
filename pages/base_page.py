from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from ..settings import sets
import time


class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(sets.IMPLICITLY_WAIT)

    def explicitly_wait(self, value):
        time.sleep(value)

    def open(self):
        self.browser.get(self.url)

    def refresh(self):
        self.browser.refresh()

    def scroll(self, scrl):  # разовий скрол на потрібний рядок сторінки (в пікселях)
        self.browser.execute_script("window.scrollTo(0," + str(scrl) + ")")

    def scroll_page(self, page_height=600, qty=10):  # скрол всієї сторінки (для підгрузки/відображення елементів)
        scrl = page_height
        for timer in range(0, qty):
            self.browser.execute_script("window.scrollTo(0, " + str(scrl) + ")")
            scrl += page_height
            self.explicitly_wait(1)

    def is_element_present(self, how, what):
        try: self.browser.find_element(how, what)
        except NoSuchElementException: return False
        return True

    def are_elements_present(self, how, what):
        try: self.browser.find_elements(how, what)
        except NoSuchElementException: return False
        return True

    def qty_of_elements(self, how, what):  # повертає кількість елементів за однаковим локатором
        try: qty = len(self.browser.find_elements(how, what))
        except NoSuchElementException: return False
        return qty

    def is_element_appears_after_while(self, how, what, timeout):
        try:
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def hover_actions(self, how, what):
        try: hover = self.browser.find_element(how, what)
        except NoSuchElementException or ElementNotInteractableException or ElementClickInterceptedException: return False
        ActionChains(self.browser).move_to_element(hover).perform()
        return True

    def click_element(self, how, what):
        try: self.browser.find_element(how, what).click()
        except NoSuchElementException or ElementNotInteractableException or ElementClickInterceptedException: return False
        return True

    def input_data(self, how, what, data):
        try: self.browser.find_element(how, what).send_keys(data)
        except NoSuchElementException or ElementNotInteractableException: return False
        return True

    def clear_field(self, how, what):
        try: self.browser.find_element(how, what).clear()
        except NoSuchElementException or ElementNotInteractableException: return False
        return True

    def get_attribute(self, how, what, data):
        try: attribute = self.browser.find_element(how, what).get_attribute(data)
        except NoSuchElementException: return False
        return attribute

    def get_text(self, how, what):
        try: text = self.browser.find_element(how, what).text
        except NoSuchElementException: return False
        return text

    def make_screenshot(self, method_name):
        self.browser.find_element(By.TAG_NAME, 'body').screenshot(f"{method_name}.png")

    def login_to_cabinet(self, user_name, user_password):
        pass

    def logout_from_cabinet(self):
        pass


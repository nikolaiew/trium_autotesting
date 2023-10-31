from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGO = (By.XPATH, '//div[@class="row hbottom"]//img[@class="img-responsive"]')
    SEARCH_INPUT = (By.XPATH, '//input[@name="search"]')
    SEARCH_BUTTON = (By.XPATH, '//div[@class="input-group-btn"]/button')
    ACCOUNT_BUTTON = (By.XPATH, '//a[@href="index.php?route=account/account"]')
    COMPARE_BUTTON = (By.XPATH, '//a[@href="compare"]')
    CART_BUTTON = (By.XPATH, '//div[@id="cart"]')
    LANGUAGE_BUTTON = (By.XPATH, '//div[@id="form-language"]/div/button')
    LANGUAGE_UA = (By.XPATH, '//ul[@class="dropdown-menu"]/li[1]/button')
    LANGUAGE_RU = (By.XPATH, '//ul[@class="dropdown-menu"]/li[2]/button')
    PHONE = (By.XPATH, '//a[@href="tel:+380931775533"]')
    EMAIL = (By.XPATH, '//a[@href="mailto:info@trium.com.ua"]')



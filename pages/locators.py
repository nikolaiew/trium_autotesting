from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGO = (By.XPATH, '//div[@class="row hbottom"]//img[@class="img-responsive"]')
    SEARCH_CATEGORY = (By.XPATH, '//select[@id="madebyhand-search-category"]')
    SEARCH_CATEGORY_WEB_CAMERAS = (By.XPATH, '//option[@value="224"]')
    SEARCH_INPUT = (By.XPATH, '//input[@name="search"]')
    SEARCH_BUTTON = (By.XPATH, '//div[@class="input-group-btn"]/button')
    ACCOUNT_BUTTON = (By.XPATH, '//a[@href="index.php?route=account/account"]')
    COMPARE_BUTTON = (By.XPATH, '//a[@href="compare"]')
    CART_BUTTON = (By.XPATH, '//div[@id="cart"]')
    LANGUAGE_BUTTON = (By.XPATH, '//div[@id="form-language"]/div/button')
    LANGUAGE_UA_BUTTON = (By.XPATH, '//ul[@class="dropdown-menu"]/li[1]/button')
    LANGUAGE_RU_BUTTON = (By.XPATH, '//ul[@class="dropdown-menu"]/li[2]/button')
    PHONE = (By.XPATH, '//a[@href="tel:+380931775533"]')
    MAIL_TO = (By.XPATH, '//a[@href="mailto:info@trium.com.ua"]')

    VSI_KATEGORII = (By.XPATH, '//div[@id="wr-menu-icon"]')
    AKSESUARY = (By.XPATH, '//li/a[@href="aksjesuar-dlja-noutbukiv/"]')
    MYSHKY = (By.XPATH, '//a[@href="aksjesuar-dlja-noutbukiv/m-shk/"]')

    GOLOVNA = (By.XPATH, '//div[@id="right-colume-1"]/ul[1]/li[1]/a')
    PRO_NAS = (By.XPATH, '//div[@id="right-colume-1"]/ul[1]/li[2]/a')
    DOSTAVKA = (By.XPATH, '//div[@id="right-colume-1"]/ul[1]/li[3]/a')
    OPLATA = (By.XPATH, '//div[@id="right-colume-1"]/ul[1]/li[4]/a')
    BLOG = (By.XPATH, '//div[@id="right-colume-1"]/ul[1]/li[5]/a')
    KONTAKTY = (By.XPATH, '//div[@id="right-colume-1"]/ul[1]/li[5]/a')
    AKCII = (By.XPATH, '//a[@href="promo/"]')



# class MainPage:



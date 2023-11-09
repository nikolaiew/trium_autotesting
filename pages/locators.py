from selenium.webdriver.common.by import By


class BasePageLocators:
# header
    LOGO_HEADER = (By.XPATH, '//div[@class="row hbottom"]//img[@class="img-responsive"]')
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

    GOLOVNA_BUTTON = (By.XPATH, '//div[@id="right-colume-1"]/ul[1]/li[1]/a')
    PRO_NAS_BUTTON = (By.XPATH, '//div[@id="right-colume-1"]/ul[1]/li[2]/a')
    DOSTAVKA_BUTTON = (By.XPATH, '//div[@id="right-colume-1"]/ul[1]/li[3]/a')
    OPLATA_BUTTON = (By.XPATH, '//div[@id="right-colume-1"]/ul[1]/li[4]/a')
    BLOG_BUTTON = (By.XPATH, '//div[@id="right-colume-1"]/ul[1]/li[5]/a')
    KONTAKTY_BUTTON = (By.XPATH, '//div[@id="right-colume-1"]/ul[1]/li[5]/a')
    AKCII_BUTTON = (By.XPATH, '//a[@href="promo/"]')

#  footer
    LOGO_FOOTER = (By.XPATH, '//div[@class="hlogo"]/img[@class="img-responsive"]')
    PRO_NAS_FOOTER_BUTTON = (By.XPATH, '//div[@class="middle-footer ua"]//a[@href="about"]')
    DOSTAVKA_FOOTER_BUTTON = (By.XPATH, '//div[@class="middle-footer ua"]//a[@href="dostavka"]')
    OPLATA_FOOTER_BUTTON = (By.XPATH, '//div[@class="middle-footer ua"]//a[@href="oplata"]')
    BLOG_FOOTER_BUTTON = (By.XPATH, '//div[@class="middle-footer ua"]//a[@href="blog"]')
    KONTAKTY_FOOTER_BUTTON = (By.XPATH, '//div[@class="middle-footer ua"]//ul[1]//a[@href="contacts"]')

    NOUTBUKY_BV = (By.XPATH, '//div[@class="middle-footer ua"]//aside//li[1]')
    MONITORY_BV = (By.XPATH, '//div[@class="middle-footer ua"]//aside//li[2]')
    KOMPLEKT_PK = (By.XPATH, '//div[@class="middle-footer ua"]//aside//li[3]')
    SYS_BLOK_BV = (By.XPATH, '//div[@class="middle-footer ua"]//aside//li[4]')
    ZAPCHASTYNY = (By.XPATH, '//div[@class="middle-footer ua"]//aside//li[5]')

# class MainPage:



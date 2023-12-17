from selenium.webdriver.common.by import By
from ..settings import sets


class BasePageLocators:
# header
    LOGO_HEADER = (By.XPATH, '//div[@class="row hbottom"]//img[@class="img-responsive"]')
    SEARCH_CATEGORY = (By.XPATH, '//select[@id="madebyhand-search-category"]')
    SEARCH_CATEGORY_WEB_CAMERAS = (By.XPATH, '//option[@value="224"]')
    SEARCH_INPUT = (By.XPATH, '//input[@name="search"]')
    SEARCH_BUTTON = (By.XPATH, '//div[@class="input-group-btn"]/button')
    ACCOUNT_BUTTON = (By.XPATH, '//ul[@class="list-inline"]/li[1]/a')
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//span[text()="Особистий Кабінет"')
    LOGOUT_BUTTON = (By.XPATH, '//li/a[text()="Вихід"]')
    SIGNUP_BUTTON = (By.XPATH, '//a[@href="index.php?route=account/register"]')
    LOGIN_BUTTON = (By.XPATH, '//a[@href="index.php?route=account/login"]')
    COMPARE_BUTTON = (By.XPATH, '//a[@href="compare"]')
    CART_BUTTON = (By.XPATH, '//div[@id="cart"]')
    CART_ITEM_QTY = (By.XPATH, '//span[@class="total_item"]')
    CART_ITEM_DELETE = (By.XPATH, '//div[1]/div[@class="pull-right"]/button')
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

# footer
    LOGO_FOOTER = (By.XPATH, '//div[@class="hlogo"]/img[@class="img-responsive"]')
# Інформація
    PRO_NAS_FOOTER_BUTTON = (By.XPATH, '//div[@class="middle-footer ua"]//a[@href="about"]')
    DOSTAVKA_FOOTER_BUTTON = (By.XPATH, '//div[@class="middle-footer ua"]//a[@href="dostavka"]')
    OPLATA_FOOTER_BUTTON = (By.XPATH, '//div[@class="middle-footer ua"]//a[@href="oplata"]')
    BLOG_FOOTER_BUTTON = (By.XPATH, '//div[@class="middle-footer ua"]//a[@href="blog"]')
    KONTAKTY_FOOTER_BUTTON = (By.XPATH, '//div[@class="middle-footer ua"]//ul[1]//a[@href="contacts"]')
# Популярні категорії
    NOUTBUKY_BV_FOOTER = (By.XPATH, '//div[@class="middle-footer ua"]//aside//li[1]')
    MONITORY_BV_FOOTER = (By.XPATH, '//div[@class="middle-footer ua"]//aside//li[2]')
    KOMPLEKT_BV_FOOTER = (By.XPATH, '//div[@class="middle-footer ua"]//aside//li[3]')
    SYS_BLOK_BV_FOOTER = (By.XPATH, '//div[@class="middle-footer ua"]//aside//li[4]')
    ZAPCHASTYNY_FOOTER = (By.XPATH, '//div[@class="middle-footer ua"]//aside//li[5]')


class MainPageLocators:
    MAIN_SLIDER = (By.XPATH, '//div[@id="slideshow0"]')
# Категорії
    MAIN_CAT_LEFT = (By.XPATH, '//div[@id="cat-img"]//div[@class="owl-prev"]')
    MAIN_CAT_RIGHT = (By.XPATH, '//div[@id="cat-img"]//div[@class="owl-next"]')
    MAIN_CAT_PANEL = (By.XPATH, '//div[@class="homecategory"]//div[@class="row rless"]')
    MAIN_CAT_ITEMS = (By.XPATH, '//div[@class="homecategory"]//div[@class="owl-item"]')  # 25
# Популярні продукти
    POPULAR_PANEL = (By.XPATH, '//div[@id="feature"]')
    POPULAR_7 = (By.XPATH, '//div[@class="owl-item"][2]/div/div[2]')  # hover
    POPULAR_7_ADD_TO_CART = (By.XPATH, '//div[@class="owl-item"][2]/div/div[2]//button[1]')

    BANNER = (By.XPATH, '//div[@class="sellbanner"]')
# б/в продукти
    BV_NOUTBUKY = (By.XPATH, '//div[@id="catli"]//div[@class="owl-item"][1]')
    BV_BLOKY_ZHYVLENNIA = (By.XPATH, '//div[@id="catli"]//div[@class="owl-item"][2]')
    BV_KOMPLEKT = (By.XPATH, '//div[@id="catli"]//div[@class="owl-item"][3]')
    BV_SYS_BLOKY = (By.XPATH, '//div[@id="catli"]//div[@class="owl-item"][4]')
    BV_SYS_BLOKY_6 = (By.XPATH, '//div[@class="cat-tab"]/div[2]/div[4]//div[6]')
    BV_MONOBLOKY = (By.XPATH, '//div[@id="catli"]//div[@class="owl-item"][5]')
    BV_MONITORY = (By.XPATH, '//div[@id="catli"]//div[@class="owl-item"][6]')
    BV_ZAPCHASTYNY = (By.XPATH, '//div[@id="catli"]//div[@class="owl-item"][7]')
    BV_BLOKY_ZHYVLENNIA_5 = (By.XPATH, '//div[@id="tab-2"]//div[5]//div[@class="image col-xs-5"]')
# Останні статті
    ARTICLES = (By.XPATH, '//div[@class="blog_item"]')  # 3

    TEXT_BLOCK = (By.XPATH, '//div[@class="seo-text-home"]')


class SignupLoginPageLocators:
    ACCOUNT_VHID_BUTTON = (By.XPATH, '//aside[@id="column-right"]//a[1]')
    ACCOUNT_REIESTRACIIA_BUTTON = (By.XPATH, '//aside[@id="column-right"]//a[2]')
    ACCOUNT_ZABULY_PSW_BUTTON = (By.XPATH, '//aside[@id="column-right"]//a[3]')
    ACCOUNT_MOIA_INFO_BUTTON = (By.XPATH, '//aside[@id="column-right"]//a[4]')

#  signup
    H1_SIGNUP = (By.XPATH, '//div/h1[text()="Реєстрація"]')
    H1_LOGOUT = (By.XPATH, '//div/h1[text()="Вихід"]')
    HOME_PAGE_BUTTON = (By.XPATH, '//ul[@class="breadcrumb"]/li[1]')
    CABINET_BUTTON = (By.XPATH, '//ul[@class="breadcrumb"]/li[2]')
    FB_BUTTON = (By.XPATH, '//td[2]/a')
    GOOGLE_BUTTON = (By.XPATH, '//td[3]/a')

    FIRSTNAME_INPUT = (By.XPATH, '//input[@name="firstname"]')
    LASTNAME_INPUT = (By.XPATH, '//input[@name="lastname"]')
    EMAIL_INPUT = (By.XPATH, '//input[@name="email"]')
    PHONE_INPUT = (By.XPATH, '//input[@name="telephone"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name="password"]')
    CONFIRM_INPUT = (By.XPATH, '//input[@name="confirm"]')
    NEWSLETTER_YES_RADIO_BUTTON = (By.XPATH, '//div[@class="form-group"]/div/label[1]')
    NEWSLETTER_NO_RADIO_BUTTON = (By.XPATH, '//div[@class="form-group"]/div/label[2]')
    POLITICS_CHECKBOX = (By.XPATH, '//input[@name="agree"]')
    SUBMIT_BUTTON = (By.XPATH, '//input[@type="submit"]')

    SIGNUP_SUCCESS_MESSAGE = (By.XPATH, '//h1[text()="Ваш обліковий запис створено!"]')
    PRODOVZHYTY_BUTTON = (By.XPATH, '//input[@type="submit"]')

# login
    H1_LOGIN = (By.XPATH, '//div/h1[text()="Зареєстрований клієнт"]')
    H2_LOGIN = (By.XPATH, '//div/h2[text()="Мій обліковий запис"]')
    TO_SIGNUP_BUTTON = (By.XPATH, '//div[@class="well"]/a')
    ZABULY_PSW_BUTTON = (By.XPATH, '//div[@class="text-right"]/a')
    ENTER_BUTTON = (By.XPATH, '//input[@type="submit"]')


class OrderPageLocators:
# Дані платника
    EXISTING_PAYMENT_ADDRESS_RADIO_BUTTON = (By.XPATH, '//input[@id="payment-address-existing"]')
    NEW_PAYMENT_ADDRESS_RADIO_BUTTON = (By.XPATH, '//input[@id="payment-address-new"]')
    FIRSTNAME_INPUT = (By.XPATH, '//div[@id="payment-new"]/div[1]/input')
    LASTNAME_INPUT = (By.XPATH, '//div[@id="payment-new"]/div[2]/input')
    PHONE_INPUT = (By.XPATH, '//div[@id="payment-new"]/div[3]/input')
    REGION_INPUT = (By.XPATH, '//option[@value="' + sets.REGION + '"]')  # Львівська обл.
    CITY_INPUT = (By.XPATH, '//div[@id="payment-new"]/div[5]/input')
    ADDRESS_INPUT = (By.XPATH, '//div[@id="payment-new"]/div[6]/input')
# Способи доставки
    DOSTAVKA_NP_RADIO_BUTTON = (By.XPATH, '//input[@id="novaposhta.warehouse"]')
    SAMOVYVIZ_RADIO_BUTTON = (By.XPATH, '//input[@id="pickup.pickup"]')
# Способи оплати
    CASH_RADIO_BUTTON = (By.XPATH, '//input[@id="cheque"]')
    ADVANCE_RADIO_BUTTON = (By.XPATH, '//input[@id="cod"]')
# Таблиця товару
    ITEM_1_NAME = (By.XPATH, '//div[@id="cart1"]//td[2]/a')
    ITEM_1_QTY = (By.XPATH, '//div[@id="cart1"]//td[3]//input')
    ITEM_1_QTY_MINUS = (By.XPATH, '//div[@id="cart1"]//td[3]//span[1]/button')
    ITEM_1_QTY_PLUS = (By.XPATH, '//div[@id="cart1"]//td[3]//span[2]/button[1]')
    ITEM_1_DEL = (By.XPATH, '//div[@id="cart1"]//td[3]//span[2]/button[2]')
    ITEM_1_PRICE = (By.XPATH, '//div[@id="cart1"]//tbody//td[4]')
    ITEM_1_SUM = (By.XPATH, '//div[@id="cart1"]//tbody/tr[1]/td[5]')
    ITEM_2_SUM = (By.XPATH, '//div[@id="cart1"]//tbody/tr[2]/td[5]')
    QTY_OF_ITEMS = (By.XPATH, '//div[@id="cart1"]//tbody//td[2]')
    AMOUNT_OF_ITEMS = (By.XPATH, '//div[@id="totals-wrap"]/div[1]//span')

    CHECKOUT_BUTTON = (By.XPATH, '//button[@id="button-payment-method"]')

    CHECKOUT_SUCCESS_MESSAGE = (By.XPATH, '//h1[text()="Ваше замовлення прийняте!"]')  # CHECKOUT_SUCCESS_PAGE


class CabinetPageLocators:
    ZMINYTY_INFO_BUTTON = (By.XPATH, '//div[@class="row accrow"]/div[1]/a')
    ZMINYTY_PSW_BUTTON = (By.XPATH, '//div[@class="row accrow"]/div[2]/a')
    ZMINYTY_ADDRESS_BUTTON = (By.XPATH, '//div[@class="row accrow"]/div[3]/a')
    ORDERS_HISTORY_BUTTON = (By.XPATH, '//div[@class="row accrow"]/div[4]/a')

    ACCOUNT_MY_INFO_BUTTON = (By.XPATH, '//div[@class="list-group accolumn"]/a[1]')
    ACCOUNT_ZMINYTY_INFO_BUTTON = (By.XPATH, '//div[@class="list-group accolumn"]/a[2]')
    ACCOUNT_PSW_BUTTON = (By.XPATH, '//div[@class="list-group accolumn"]/a[3]')
    ACCOUNT_ORDERS_HISTORY_BUTTON = (By.XPATH, '//div[@class="list-group accolumn"]/a[4]')

    LOGOUT_BUTTON = (By.XPATH, '//h3/a')


class CategoryPageLocators:
    MYSHKA_1 = (By.XPATH, '//div[@class="row cpagerow"]/div[1]')  # hover
    MYSHKA_12 = (By.XPATH, '//div[@class="row cpagerow"]/div[12]')  # hover
    MYSHKA_1_PRICE = (By.XPATH, '//div[@class="row cpagerow"]/div[1]//div[@class="price"]')
    MYSHKA_12_PRICE = (By.XPATH, '//div[@class="row cpagerow"]/div[12]//div[@class="price"]')
    MYSHKA_1_ADD_TO_CART = (By.XPATH, '//div[@class="row cpagerow"]/div[1]//button[1]')
    MYSHKA_12_ADD_TO_CART = (By.XPATH, '//div[@class="row cpagerow"]/div[12]//button[1]')
    ALERT_SUCCESS_POPUP_WINDOW = (By.XPATH, '//div[@class="alert alert-success alert-dismissible alertsuc por"]')
    PRODOVZHYTY_BUTTON = (By.XPATH, '//div[@class="confirm_cart_div"]/button')
    TO_CHECKOUT_BUTTON = (By.XPATH, '//div/a[@href="index.php?route=checkout/cart"]')


class SearchPageLocators:
    SEARCH_PANEL_ITEMS = (By.XPATH, '//div[@class="row cpagerow rless"]/div')
    SEARCH_PANEL_ITEM_1 = (By.XPATH, '//div[@class="row cpagerow rless"]/div[1]//h4/a')
    SEARCH_PANEL_ITEM = []
    for i in range(1, 6):
        SEARCH_PANEL_ITEM.append((By.XPATH, '//div[@class="row cpagerow rless"]/div[' + str(i) + ']//h4/a'))


class ProductPageLocator:
    ADD_TO_CART = (By.XPATH, '//button[@id="button-cart"]')


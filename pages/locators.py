from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, '.btn.btn-add-to-basket')
    CHECK_TEXT_AFTER_ADD_CART = (By.CSS_SELECTOR, '.alert .alertinner strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_CART = (By.CSS_SELECTOR, '.basket-mini a.btn.btn-default')

class BasketPageLocators():
    CHECK_CART = (By.CSS_SELECTOR, '.basket-items')
    CHECK_TEXT_THAT_CART_IS_EMPTY = (By.CSS_SELECTOR, '#content_inner p')
from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, '.btn.btn-add-to-basket')
    CHECK_TEXT_AFTER_ADD_CART = (By.CSS_SELECTOR, '.alert .alertinner strong')
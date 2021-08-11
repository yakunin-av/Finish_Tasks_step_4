from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


# Структура:
#  LoginPage:
#    в should_be_login_url проверяем в assert не равена ли строка self.url через find строке login.  (!= -1)
#    в shold_be_login_form и register_form ищем через id login_form или register_form в locators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' not in current url"
        
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "LOGIN_FORM is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "REGISTER_FORM is not presented"

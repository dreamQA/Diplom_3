import allure

from locators import password_recovery_locator
from locators.password_recovery_locator import *
from pages.main_page import MainPage
from data import LOGIN

class PasswordRecoveryPage(MainPage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Нажимаем на кнопку восстановить пароль')
    def click_button_password_recovery(self):
        self.click_element(button_password_recovery)

    @allure.step('Вводим почту в поле восстановления пароля')
    def send_keys_email_input_recovery_password(self):
        self.send_keys(email_input_password_recovery, LOGIN)

    @allure.step('Нажимаем на кнопку восстановить')
    def click_button_recovery(self):
        self.click_element(button_recovery)

    @allure.step('Нажимаем на кнопку показать/скрыть пароль')
    def click_button_show_hide(self):
        self.click_element(show_hide_button)

    @allure.step('Метод возвращает кнопку показать/скрыть пароль')
    def get_show_password(self):
        return self.browser.find_element(*password_field)


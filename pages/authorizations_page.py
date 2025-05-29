import allure
from locators.authorizations_locator import *
from pages.main_page import MainPage

class AuthorizationsPage(MainPage):

    @allure.step('Заполнение поля "email" на странице авторизации')
    def send_keys_email_input(self, email):
            self.find(email_input).send_keys(email)

    @allure.step('Заполнение поля "password" на странице авторизации')
    def send_keys_password_input(self, password):
        self.find(password_input).send_keys(password)

    @allure.step('Нажимаем на кнопку "Войти"')
    def click_button_enter(self):
        self.find(button_enter).click()

    @allure.step('Метод открытия страницы "конструктор" с авторизацией')
    def login(self,email,password):
        with allure.step('Открываем страницу авторизации'):
            self.open()
        with allure.step('Нажимаем на кнопку "личный кабинет"'):
            self.click_personal_account()
        with allure.step('Заполняем поле "email" на странице авторизации'):
            self.send_keys_email_input(email)
        with allure.step('Заполняем поле "password" на странице авторизации'):
            self.send_keys_password_input(password)
        with allure.step('Нажимаем на кнопку "Войти"'):
            self.click_button_enter()

        
import allure

from pages.password_recovery_page import PasswordRecoveryPage
from url import *
import pytest

class TestPasswordRecovery:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке восстановить пароль')
    def test_password_recovery_page(self,browser):
        recovery_page = PasswordRecoveryPage(browser)
        with allure.step('Открываем страницу авторизации'):
            recovery_page.open(f'{URL}{LOGIN}')
        with allure.step('Нажимаем на кнопку восстановить пароль'):
            recovery_page.click_button_password_recovery()
        with allure.step('Проверка,что открылась нужная страница восстановления пароля'):
            assert recovery_page.get_current_url() == f'{URL}{FORGOT_PASSWORD}'


    @allure.title('Проверка заполняемости поля почты и нажатие кнопки "восстановить"')
    def test_password_field_email_and_restore_button_click(self,browser):
        recovery_page = PasswordRecoveryPage(browser)
        with allure.step('Открываем страницу авторизации'):
            recovery_page.open(f'{URL}{FORGOT_PASSWORD}')
        with allure.step('Заполняем поле почты'):
            recovery_page.send_keys_email_input_recovery_password()
        with allure.step('Нажимаем на кнопку "восстановить"'):
            recovery_page.click_button_recovery()
        with allure.step('Добавляем ожидание для загрузки страницы'):
            recovery_page.wait_for_page_load(f'{URL}{RESET_PASSWORD}')
        with allure.step('Проверка,что открылась нужная страница восстановления пароля'):
            assert recovery_page.get_current_url() == f'{URL}{RESET_PASSWORD}'

    @allure.title('Проверка логики:клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.')
    def test_show_hide_activates_password_field(self,browser):
        recovery_page = PasswordRecoveryPage(browser)
        with allure.step('Открываем страницу авторизации'):
            recovery_page.open(f'{URL}{LOGIN}')
        with allure.step('Нажимаем на кнопку восстановить пароль'):
            recovery_page.click_button_password_recovery()
        with allure.step('Заполняем поле почты'):
            recovery_page.send_keys_email_input_recovery_password()
        with allure.step('Нажимаем на кнопку восстановить'):
            recovery_page.click_button_recovery()
        with allure.step('Добавляем ожидание для загрузки страницы'):
            recovery_page.wait_for_page_load(f'{URL}{RESET_PASSWORD}')
        with allure.step('Нажимаем на кнопку показать/скрыть пароль'):
            recovery_page.click_button_show_hide()
        with allure.step('Проверяем,что поле теперь активно'):
            assert 'input_status_active' in recovery_page.get_show_password().get_attribute('class')
import allure
import pytest
from url import *
import pytest

class TestPersonalAccount:
    @allure.title('Переход по клику в личный кабинет')
    def test_personal_account_path(self,browser,prepare_for_personal_account):
        _, _, _, personal_account, _ = prepare_for_personal_account # _, игнорируемые значения из метода/функции, которые не используются в тесте
        with allure.step('Открываем главную страницу'):
            personal_account.open()
        with allure.step('Нажимаем на кнопку личный кабинет'):
            personal_account.click_personal_account()
        with allure.step('Проверка,что открылась страница авторизации'):
            assert personal_account.get_current_url() == f'{URL}{LOGIN}'

    @pytest.mark.usefixtures("prepare_for_personal_account")
    @allure.title('Переход в историю заказов')
    def test_path_to_order_history(self,browser,prepare_for_personal_account):
        _, email, password, personal_account, auth = prepare_for_personal_account
        with allure.step('Открываем страницу с конструктором'):
            auth.login(email, password)
        with allure.step('Нажимаем на кнопку личный кабинет'):
            personal_account.click_personal_account()
        with allure.step('Нажимаем на кнопку история заказов'):
            personal_account.click_button_history()
        with allure.step('Проверяем,что открылась страница история заказов'):
            assert personal_account.get_current_url() == f'{URL}{HISTORY}'

    @pytest.mark.usefixtures("prepare_for_personal_account")
    @allure.title('Проверка выхода из аккаунта')
    def test_logout_account(self,browser,prepare_for_personal_account):
        _, email, password, personal_account, auth = prepare_for_personal_account
        with allure.step('Открываем страницу с конструктором'):
            auth.login(email, password)
        with allure.step('Нажимаем на кнопку личный кабинет'):
            personal_account.click_personal_account()
        with allure.step('Нажимаем на кнопку выход'):
            personal_account.click_button_exit()
        with allure.step('Добавляем ожидание для загрузки страницы'):
            personal_account.wait_for_page_load(f'{URL}{LOGIN}')
        with allure.step('Проверка,что открылась нужная страница авторизации'):
            assert personal_account.get_current_url() == f'{URL}{LOGIN}'

            

import allure
from data import *
from locators.constructor_locator import ingredient
from url import *
import pytest



class TestBasicFunctionality:

    @allure.title('Проверка перехода на страницу "лента заказов" по нажатию')
    def test_navigate_to_order_feed(self, browser, prepare_for_constructor):
        response, _, _, _, constructor, order_feed_page = prepare_for_constructor
        with allure.step('Открываем страницу авторизации'):
            constructor.open(f'{URL}{LOGIN}')
        with allure.step('Нажимаем на кнопку лента заказов'):
            order_feed_page.click_order_feed_button()
        with allure.step('Проверяем,что совершился переход на страницу ленты заказов'):
            assert constructor.get_current_url() == f'{URL}{FEED}'

    @allure.title('Проверка: если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_order_details_popup_opens_on_click(self, browser, prepare_for_constructor):
        _, _, _, _, constructor, _ = prepare_for_constructor
        with allure.step('Открываем страницу с конструктором'):
            constructor.open(f'{URL}')
        with allure.step('Нажимаем на ингредиент'):
            constructor.click_ingredient()
        with allure.step('Проверяем,что открылось модальное окно с деталями'):
            assert constructor.get_modal_window_ingredient() == INGREDIENT_DETAILS

    @allure.title('Проверка:всплывающее окно закрывается кликом по крестику')
    def test_ingredient_popup_close(self, browser, prepare_for_constructor):
        _, _, _, _, constructor, _ = prepare_for_constructor
        with allure.step('Открываем страницу с конструктором'):
            constructor.open(f'{URL}')
        with allure.step('Нажимаем на ингредиент'):
            constructor.click_ingredient()
        with allure.step('Закрываем окно с выборкой ингредиентов'):
            constructor.click_close_modal_window_ingredient()
        with allure.step('Проверка что окно закрылось'):
            assert 'Modal_modal__P3_V5' in constructor.get_modal_class()

    @allure.title('Проверка:при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_counter_ingredient_up_when_added_to_order(self, browser, prepare_for_constructor):
        _, _, _, _, constructor, _ = prepare_for_constructor
        with allure.step('Открываем страницу с конструктором'):
            constructor.open(f'{URL}')
        with allure.step('Запрашиваем ингредиент и конструктер бургера'):
            ingredient = constructor.get_ingredient()
            burger_constructor = constructor.get_constructor_burger()
        with allure.step('Перемещаем ингредиент в конструктор'):
            constructor.drag_and_drop(ingredient, burger_constructor)
        with allure.step('Проверка,что счетчик увеличился'):
            assert constructor.get_count_ingredient() == COUNT_INGREDIENT

    @allure.title('Проверка:залогиненный пользователь может оформить заказ.')
    def test_auth_user_can_order(self, browser, prepare_for_constructor):
        _, email, password, auth, constructor, _ = prepare_for_constructor
        with allure.step('Открываем страницу конструктора.Авторизуемся'):
            auth.login(email, password)
        with allure.step('Добавляем ожидание для загрузки страницы с конструктором'):
            constructor.wait_for_page_load(f'{URL}')
        with allure.step('Собираем и оформляем заказ'):
            constructor.create_and_approve_order()
        with allure.step('Добавляем ожидание'):
            constructor.wait_loading_visability(browser)
            constructor.wait_loading_invisibility(browser)
        with allure.step('Проверка,что номер созданного заказа не 5000'):
            assert constructor.get_modal_order_text() != ORDER_NUMBER_FOR_TEST

import allure
from pages.main_page import MainPage
from url import *
from locators.personal_account_locator import *
from locators.order_feed_locator import *
import pytest

class TestOrderFeed:

    @allure.title('Проверка:если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_open_order_details_popup(self,browser,prepare_for_order):
        _, _, _, _, order_feed_page, _, _ = prepare_for_order
        with allure.step('Открываем главную страницу'):
            order_feed_page.open()
        with allure.step('Нажимаем на кнопку лента заказов'):
            order_feed_page.click_order_feed_button()
        with allure.step('Нажимаем на первый заказ в ленте'):
            order_feed_page.click_order_history()
        with allure.step('Проверка,что открылась страница с заказом'):
            assert order_feed_page.get_popup_order_history().is_displayed()

    @allure.title('Проверка: заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»,')
    def test_order_history_displayed_in_order_feed(self,browser,prepare_for_order):
        _, email, password, auth, order_feed_page,personal_account, constructor = prepare_for_order
        with allure.step('Открываем страницу конструктора.Авторизуемся'):
            auth.login(email,password)
        with allure.step('Добавляем ожидание для загрузки страницы'):
            constructor.wait_for_page_load(f'{URL}')
        with allure.step('Собираем и оформляем заказ'):
            constructor.create_and_approve_order()
        with allure.step('Добавляем ожидание для отображения окна с заказом'):
            constructor.wait_loading_visability(browser)
            constructor.wait_loading_invisibility(browser)
        with allure.step('Закрываем модальное окно с заказом'):
            constructor.get_close_modal_order()
        with allure.step('Нажимаем на кнопку личный кабинет'):
            constructor.click_personal_account()
        with allure.step('Добавляем ожидание для загрузки страницы'):
            constructor.wait_for_page_load(f'{URL}{PROFILE}')
        with allure.step('Нажимаем на кнопку история заказов'):
            personal_account.click_button_history()
        with allure.step('Добавляем ожидание'):
            personal_account.wait_for_order_history_item(order_history_item)
        with allure.step('Находим номер последнего заказа в личном кабинете'):
            last_order_number = personal_account.get_order_history_item()
        with allure.step('Нажимаем на кнопку лента заказов'):
            order_feed_page.click_order_feed_button()
        with allure.step('Добавляем ожидание'):
            personal_account.wait_for_order_history_item(number)
        with allure.step('Проверка,что последний заказ из личного кабинета отобразился в ленте заказов'):
            order_numbers_in_feed = order_feed_page.get_order()
            assert last_order_number in order_numbers_in_feed

    @allure.title('Проверка:при создании нового заказа счётчик Выполнено за всё время увеличивается,')
    def test_all_time_completed_orders_counter_increases(self,browser,prepare_for_order):
        _, email, password, auth, order_feed_page, _, constructor = prepare_for_order
        with allure.step('Открываем страницу с конструктором.Авторизуемся'):
            auth.login(email,password)
        with allure.step('Открываем страницу ленты заказов'):
            order_feed_page.click_order_feed_button()
        with allure.step('Ищем счетчик заказов за все время'):
            order_feed_page.find(completed_all_time)
        with allure.step('Сохраняем  текущее количество заказов'):
            count_number = order_feed_page.get_completed_all_time()
        with allure.step('Собираем и оформляем заказ'):
            constructor.create_order_and_check(browser)
        with allure.step('Проврка,что новое знаение счетчика не равно "count_number"'):
            assert order_feed_page.get_completed_all_time() != count_number

    @allure.title('Проверка:при создании нового заказа счётчик Выполнено за сегодня увеличивается,')
    def test_create_new_order_increases_today_counter(self,browser,prepare_for_order):
        _, email, password, auth, order_feed_page, _, constructor = prepare_for_order
        with allure.step('Открываем страницу с конструктором.Авторизуемся'):
            auth.login(email,password)
        with allure.step('Добавляем ожидание для загрузки страницы'):
            constructor.wait_for_page_load(f'{URL}')
        with allure.step('Открываем страницу ленты заказов'):
            order_feed_page.click_order_feed_button()
        with allure.step('Ищем счетчик заказов за сегодня'):
            order_feed_page.find(completed_today)
        with allure.step('Сохраняем количество заказов за сегодня до оформления нового'):
            count_number = order_feed_page.get_completed_today()
            constructor.create_order_and_check(browser)
        with allure.step('Проверка,что новое значение не равно "count_number"'):
            assert order_feed_page.get_completed_today() != count_number

    @allure.title('Проверка:после оформления заказа его номер появляется в разделе В работе.')
    def test_new_order_visibility_in_work(self,browser,prepare_for_order):
        _, email, password, auth, order_feed_page, _, constructor = prepare_for_order
        with allure.step('Открываем станицу с конструктором.Авторизауемся'):
            auth.login(email,password)
        with allure.step('Добавляем ожидание для загрузки страницы конструктора'):
            constructor.wait_for_page_load(f'{URL}')
        with allure.step('Собираем и оформляем заказ'):
            constructor.create_and_approve_order()
        with allure.step('Добавляем ожидание для отображения окна с заказом'):
            constructor.wait_loading_visability(browser)
            constructor.wait_loading_invisibility(browser)
        with allure.step('Получаем номер заказа'):
            number_order = '0' + constructor.get_modal_order_text()
        with allure.step('Закрываем окно с заказом'):
            constructor.get_close_modal_order()
        with allure.step('Открываем страницу лента заказов'):
            order_feed_page.click_order_feed_button()
        with allure.step('Получаем номер заказа в работе'):
            count_number = order_feed_page.get_at_work()
        with allure.step('Проверка,что номер заказа в работе совпадает с "number_order"'):
            assert count_number == number_order

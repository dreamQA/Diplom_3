import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.constructor_locator import *
from locators.order_feed_locator import *
from pages.main_page import MainPage
from url import *
from pages.order_feed_page import OrderFeedPage

class ConstructorPage(MainPage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Нажимаем на ингридиент')
    def click_ingredient(self):
        self.click_element(ingredient)

    @allure.step('Возвращаем счетчик-количества ингредиента')
    def get_count_ingredient(self):
        return self.get_text_of_element(count_ingredient)

    @allure.step('Возвращаем модальное окно с деталями ингредиента')
    def get_modal_window_ingredient(self):
        return self.get_text_of_element(modal_window_ingredient)

    @allure.step('Возвращаем класс модального окна')
    def get_modal_class(self):
        return self.get_attribute_element(close_modal,'class')

    @allure.step('Закрываем модальное окно деталей ингредиента')
    def click_close_modal_window_ingredient(self):
        self.click_element(close_modal_window_ingredient)

    @allure.step('Нажимаем на кнопку "Конструктор"')
    def click_constructor_button(self):
        self.click_element(constructor_button)

    @allure.step('Возвращаем ингредиент')
    def get_ingredient(self):
        return self.find(ingredient)

    @allure.step('Возвращаем булку')
    def get_buns(self):
        return self.find(buns)

    @allure.step('Возвращаем конструктор бургера')
    def get_constructor_burger(self):
        return self.find(constructor_burger)

    @allure.step('Перетаскиваем элемент в области')
    def drag_and_drop(self,source,target):
        self.actions.drag_and_drop(source,target).perform()

    @allure.step('Нажимаем оформить заказ')
    def click_order_button(self):
        self.click_element(order_button)

    @allure.step('Нажимаем на крестик для закрытия окна с заказом')
    def get_close_modal_order(self):
        return self.click_element(close_modal_order)

    @allure.step('Возвращаем номер заказа')
    def get_modal_order_text(self):
        return self.get_text_of_element(modal_order)

    def wait_for_order_item(self,locator):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.presence_of_element_located((By.XPATH,locator)))

    @allure.step('Собираем и оформляем заказ')
    def create_and_approve_order(self):
        ingredient = self.get_ingredient()
        buns = self.get_buns()
        constructor_burger = self.get_constructor_burger()
        self.drag_and_drop(buns,constructor_burger)
        self.drag_and_drop(ingredient,constructor_burger)
        self.click_order_button()

    def wait_loading_visability(self,browser):
        self.wait.until(EC.visibility_of_element_located(loading))

    def wait_loading_invisibility(self,browser):
        self.wait.until(EC.invisibility_of_element_located(loading))

    def create_order_and_check(self,browser):
       order_feed_page = OrderFeedPage(self.browser)
       user_order_history = ConstructorPage(browser)
       with allure.step('Нажимаем на кнопку "Конструктор"'):
           self.click_constructor_button()
       with allure.step('Добавляем ожидание для загрузки страницы'):
            order_feed_page.wait_for_page_load(f'{URL}')
       with allure.step('Собираем и оформляем заказ'):
            self.create_and_approve_order()
       with allure.step('Добавляем ожидание для появления модального окна с заказом'):
            user_order_history.wait_loading_visability(browser)
            user_order_history.wait_loading_invisibility(browser)
       with allure.step('Закрываем окно с заказом'):
            self.get_close_modal_order()
       with allure.step('Открываем страницу лента заказов'):
            order_feed_page.click_order_feed_button()
       with allure.step('Добавляем ожидание загрузки страницы'):
            order_feed_page.find(completed_all_time)





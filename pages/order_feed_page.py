import allure

from locators import order_feed_locator
from locators.order_feed_locator import *
from pages.main_page import MainPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class OrderFeedPage(MainPage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Метод нажатия на кнопку "Лента заказов"')
    def click_order_feed_button(self):
       self.click_element(order_feed_button)

    @allure.step('Метод возврата списка всех заказов в ленте')
    def get_order(self):
        order = self.find_elements(*number)
        for order_list in order:
            order_text = order_list.text
            return order_text

    @allure.step('Возвращаем количество заказов за все время')
    def get_completed_all_time(self):
        return self.get_text_of_element(completed_all_time)

    @allure.step('Возвращаем количество заказов за сегодня')
    def get_completed_today(self):
        return self.get_text_of_element(completed_today)

    @allure.step('Возвращаем количество заказов в работе')
    def get_at_work(self):
        return self.get_text_of_element(at_work)

    @allure.step('Метод нажатия на первый заказ из списка')
    def click_order_history(self):
        self.click_element(order_history)

    @allure.step('Метод возвращающий окно с информацией о заказе')
    def get_popup_order_history(self):
        return self.find(popup_order_history)

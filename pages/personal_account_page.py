import allure
from locators.personal_account_locator import *
from pages.main_page import MainPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PersonalAccountPage(MainPage):
    def __init__(self, browser):
        super().__init__(browser)

    @allure.step('Нажимаем на кнопку выйти')
    def click_button_exit(self):
        self.click_element(button_exit)

    @allure.step('Нажимаем на кнопку история заказов')
    def click_button_history(self):
        self.click_element(order_history_link)

    @allure.step('Возвращаем номер последнего заказа в личный кабинет')
    def get_order_history_item(self):
        return self.get_text_of_element(order_history_item)



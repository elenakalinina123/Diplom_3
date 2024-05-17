import allure

from selenium.common import TimeoutException

from ..data import urls
from ..locators import index_locators
from .base_page import BasePage


class IndexPage(BasePage):
    page_link = urls.base_url

    @allure.step('Кликаем по кнопке личный кабинет')
    def click_profile(self):
        self.click(index_locators.profile_button)

    @allure.step('Проверяем что мы на странице логина')
    def is_url_login(self):
        expected_url_string = urls.login_url
        self.wait_until_url_contains(expected_url_string)
        return expected_url_string in self.get_current_url()

    @allure.step('кликаем на конструктор')
    def click_constructor(self):
        self.click_wait(index_locators.constructor)

    @allure.step('кликаем на ленту заказов')
    def click_timeline(self):
        self.click_wait(index_locators.orders_timeline)

    @allure.step('кликаем на бургер 1')
    def click_burger_1(self):
        self.click(index_locators.burger_1)

    @allure.step('кликаем на бургер 2')
    def click_burger_2(self):
        self.click(index_locators.burger_2)

    @allure.step('проверяем не виден ли попап бургера 1')
    def is_burger_1_visible(self):
        try:
            self.wait_until_visibility(index_locators.burger_1_popup)
        except TimeoutException:
            return False
        return True

    @allure.step('проверяем виден ли попап бургера 2')
    def is_burger_2_visible(self):
        try:
            self.wait_until_visibility(index_locators.burger_2_popup)
        except TimeoutException:
            return False
        return True

    @allure.step('закрываем попап бургера 1')
    def click_burger_1_close(self):
        self.click(index_locators.burger_1_close)

    @allure.step('закрываем попап бургера 2')
    def click_burger_2_close(self):
        self.click(index_locators.burger_2_close)

    @allure.step('закрываем попап заказа')
    def click_order_popup_close(self):
        self.click_wait(index_locators.order_popup_close)

    @allure.step('проверяем не виден ли попап бургера 1')
    def is_burger_1_invisible(self):
        try:
            self.invisility_of_elememnt_located(index_locators.burger_1_popup)
        except TimeoutException:
            return False
        return True

    @allure.step('проверяем не виден ли попап бургера 2')
    def is_burger_2_invisible(self):
        try:
            self.invisility_of_elememnt_located(index_locators.burger_2_popup)
        except TimeoutException:
            return False
        return True

    @allure.step('проверяем виден ли таймлайн')
    def is_timeline_visible(self):
        try:
            self.wait_until_visibility(index_locators.orders_h1)
        except TimeoutException:
            return False
        return True

    @allure.step('проверяем виден ли конструктор')
    def is_constructor_visible(self):
        try:
            self.wait_until_visibility(index_locators.constructor_h1)
        except TimeoutException:
            return False
        return True

    @allure.step('перетаскиваем бургер в корзину')
    def add_burger_to_order(self):
        drag = self.wait_until_element_is_clickable(index_locators.burger_1)
        drop = self.wait_until_element_is_clickable(index_locators.basket_drop)
        self.drag_and_drop(drag, drop)

    @allure.step('перетаскиваем соус в корзину')
    def add_sauce_to_order(self):
        drag = self.wait_until_element_is_clickable(index_locators.sauce_spicy)
        drop = self.wait_until_element_is_clickable(index_locators.basket_drop)
        self.drag_and_drop(drag, drop)

    @allure.step('проверяем счетчик бургера')
    def check_burger_counter(self):
        counter = self.find_element(index_locators.burger_1_counter)
        return int(counter.text)

    @allure.step('создаём заказ')
    def create_order(self):
        self.add_burger_to_order()
        self.add_sauce_to_order()
        self.click(index_locators.create_order)
        order_number = int(self.wait_until_visibility(
            index_locators.order_number).text)
        self.click_order_popup_close()

        return order_number

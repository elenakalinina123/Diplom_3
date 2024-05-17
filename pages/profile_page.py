import allure

from ..data import urls
from ..locators import profile_locators
from ..pages.base_page import BasePage


class ProfilePage(BasePage):
    page_link = urls.profile_url

    @allure.step('нажимаем на кнопку история заказов')
    def click_order_history(self):
        self.click(profile_locators.order_history_button)

    @allure.step('проверка что адрес история заказов')
    def is_url_order_history(self):
        expected_string = profile_locators.order_history_string
        self.wait_until_url_contains(expected_string)

        return expected_string in self.get_current_url()

    @allure.step('нажимаем кнопку выйти')
    def click_log_out(self):
        self.click(profile_locators.logout_button)

    @allure.step('проверка что адрес логин')
    def is_url_login(self):
        expected_string = 'login'
        self.wait_until_url_contains(expected_string)

        return expected_string in self.get_current_url()

import allure

from ..data import urls
from ..locators import index_locators
from .base_page import BasePage


class IndexPage(BasePage):
    page_link = urls.base_url

    @allure.step('Кликаем по кнопке личный кабинет')
    def click_profile(self):
        button = self.wait_until_visibility(index_locators.profile_button)
        button.click()

    def is_url_login(self):
        expected_url_string = urls.login_url
        self.wait_until_url_contains(expected_url_string)
        return expected_url_string in self.get_current_url()

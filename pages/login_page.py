import allure

from ..data import data, urls
from ..locators import login_locators
from .base_page import BasePage


class LoginPage(BasePage):
    page_link = urls.login_url

    @allure.step('Кликаем по кнопке личный кабинет')
    def click_profile(self):
        self.wait_until_url_matches(urls.base_url)
        self.click(login_locators.profile_button).click()

    @allure.step('Кликаем кнопку восстановить пароль')
    def click_recover(self):
        self.click(login_locators.restore_password_button)

    @allure.step('Логинимся')
    def login(self, email, password):
        email_field = self.wait_until_visibility(login_locators.email_field)
        password_field = self.wait_until_visibility(
            login_locators.password_field)

        email_field.send_keys(email)
        password_field.send_keys(password)

        self.click(login_locators.login_button)

    @allure.step('Логиним тест-юзера')
    def login_test_user(self):
        email = data.test_user['email']
        password = data.test_user['password']
        self.login(email, password)

    @allure.step('Проверяем что залогинены')
    def is_logged_in(self):
        log_out_button = self.wait_until_visibility(
            login_locators.logout_button)

        return log_out_button.is_displayed()

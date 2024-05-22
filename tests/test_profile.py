import allure

from ..pages.index_page import IndexPage
from ..pages.login_page import LoginPage
from ..pages.profile_page import ProfilePage


class TestProfile:
    @allure.title('Тест перехода по кнопке Профиль')
    def test_profile_button(self, driver):
        index_page = IndexPage(driver)
        index_page.load()
        index_page.click_profile()
        assert index_page.is_url_login()

    @allure.title('Тест на успешный логин')
    def test_login(self, driver):
        login_page = LoginPage(driver)

        login_page.login_test_user()

        login_page.click_profile()

        assert login_page.is_logged_in()

    @allure.title('Тест перехода на историю заказов')
    def test_order_history(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.click_order_history()

        assert profile_page.is_url_order_history()

    @allure.title('Тест выхода из профиля')
    def test_logout(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.click_log_out()

        assert profile_page.is_url_login()

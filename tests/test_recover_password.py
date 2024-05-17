import allure

from ..data.data import test_email
from ..pages.forgot_password_page import ForgotPasswordPage
from ..pages.login_page import LoginPage


class TestRecoverPassword:
    @allure.title('Тест на переход на страницу восстановления пароля')
    def test_link_to_recover_password(self, driver):
        login_page = LoginPage(driver)
        forgot_page = ForgotPasswordPage(driver)

        login_page.load()
        login_page.click_recover()
        assert forgot_page.is_loaded()

    @allure.title('Тест на переход на страницу создания нового пароля')
    def test_enter_email(self, driver):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.input_email(test_email)
        forgot_page.click_recover()
        assert forgot_page.is_url_reset_password()

    @allure.title('Тест на работу кнопки "показать пароль"')
    def test_show_password(self, driver):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.click_show_password()

        assert forgot_page.is_active_password_field()

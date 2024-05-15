from ..pages.forgot_password_page import ForgotPasswordPage
from ..pages.login_page import LoginPage


class TestRecoverPassword:
    def test_link_to_recover_password(self, driver):
        login_page = LoginPage(driver)
        forgot_page = ForgotPasswordPage(driver)

        login_page.load()
        login_page.click_recover()
        assert forgot_page.is_loaded()

    def test_enter_email(self, driver, fixed_email):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.input_email(fixed_email)
        forgot_page.click_recover()
        assert forgot_page.is_url_reset_password()

    def test_show_password(self, driver):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.click_show_password()

        assert forgot_page.is_active_password_field()

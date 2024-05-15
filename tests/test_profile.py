from ..pages.index_page import IndexPage
from ..pages.login_page import LoginPage
from ..pages.profile_page import ProfilePage


class TestProfile:
    def test_profile_button(self, driver):
        index_page = IndexPage(driver)
        index_page.load()
        index_page.click_profile()
        assert index_page.is_url_login()

    def test_login(self, driver, fixed_user):
        email = fixed_user['email']
        password = fixed_user['password']
        login_page = LoginPage(driver)

        login_page.login(email, password)
        login_page.click_profile()
        assert login_page.is_logged_in()

    def test_order_history(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.click_order_history()

        assert profile_page.is_url_order_history()

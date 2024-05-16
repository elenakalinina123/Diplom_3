from ..data import urls
from ..locators import profile_locators
from ..pages.base_page import BasePage


class ProfilePage(BasePage):
    page_link = urls.profile_url

    def click_order_history(self):
        button = self.wait_until_visibility(
            profile_locators.order_history_button)
        button.click()

    def is_url_order_history(self):
        expected_string = profile_locators.order_history_string
        self.wait_until_url_contains(expected_string)

        return expected_string in self.get_current_url()

    def click_log_out(self):
        self.click(profile_locators.logout_button)

    def is_url_login(self):
        expected_string = 'login'
        self.wait_until_url_contains(expected_string)

        return expected_string in self.get_current_url()

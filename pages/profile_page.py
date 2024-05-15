from ..locators import profile_locators
from ..pages.base_page import BasePage


class ProfilePage(BasePage):
    page_link = profile_locators.url

    def click_order_history(self):
        button = self.wait_until_visibility(
            profile_locators.order_history_button)
        button.click()

    def is_url_order_history(self):
        expected_string = profile_locators.order_history_string
        self.wait_until_url_contains(expected_string)

        return expected_string in self.get_current_url()

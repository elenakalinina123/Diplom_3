import allure

from ..pages.feed_page import FeedPage
from ..pages.index_page import IndexPage
from ..pages.login_page import LoginPage


class TestFeed:
    @allure.title('Тест на открытие карточки продукта')
    def test_open_order(self, driver):
        feed_page = FeedPage(driver)
        feed_page.load()
        feed_page.click_order()

        assert feed_page.is_order_popup()

    @allure.title('Тест на работу счетчиков')
    def test_counters(self, driver):
        feed_page = FeedPage(driver)
        index_page = IndexPage(driver)
        login_page = LoginPage(driver)

        index_page.load()
        index_page.click_profile()
        login_page.login_test_user()

        index_page.click_timeline()
        before_counters = feed_page.check_counters()

        index_page.click_constructor()
        index_page.create_order()
        index_page.click_timeline()

        assert feed_page.check_counters() > before_counters

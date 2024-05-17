import allure

from ..pages.index_page import IndexPage
from ..pages.login_page import LoginPage


class TestIndex:
    @allure.title('Тест на открытие карточки продукта')
    def test_burger_1(self, driver):
        index_page = IndexPage(driver)
        index_page.load()
        index_page.click_burger_1()
        assert index_page.is_burger_1_visible()

    @allure.title('Тест на закрытие карточки продукта')
    def test_close_burger_1(self, driver):
        index_page = IndexPage(driver)
        index_page.click_burger_1_close()
        assert index_page.is_burger_1_invisible()

    @allure.title('Тест на открытие карточки продукта 2')
    def test_burger_2(self, driver):
        index_page = IndexPage(driver)
        index_page.click_burger_2()
        assert index_page.is_burger_2_visible()

    @allure.title('Тест на закрытие карточки продукта 2')
    def test_close_burger_2(self, driver):
        index_page = IndexPage(driver)
        index_page.click_burger_2_close()
        assert index_page.is_burger_2_invisible()

    @allure.title('Тест на счетчик продукта в заказе')
    def test_ingredient_counter(self, driver):
        index_page = IndexPage(driver)
        index_page.add_burger_to_order()
        assert index_page.check_burger_counter() == 2

    @allure.title('Тест на переход в Ленту заказов')
    def test_check_order_timeline(self, driver):
        index_page = IndexPage(driver)
        index_page.click_timeline()
        assert index_page.is_timeline_visible()

    @allure.title('Тест на переход в Конструктор')
    def test_check_constructor(self, driver):
        index_page = IndexPage(driver)
        index_page.click_constructor()
        assert index_page.is_constructor_visible()

    @allure.title('Тест заказа')
    def test_order(self, driver):
        index_page = IndexPage(driver)
        login_page = LoginPage(driver)

        index_page.load()
        index_page.click_profile()
        login_page.login_test_user()

        index_page.click_constructor()

        order_number = index_page.create_order()

        assert order_number

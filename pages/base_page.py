import allure

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    page_link = None
    driver = None

    @allure.step('инициализируем класс')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Загружаем страницу')
    def load(self):
        self.driver.get(self.page_link)

    @allure.step('ждем {time} секунд')
    def wait(self, time):
        wait = WebDriverWait(self.driver, time)
        return wait

    @allure.step('ждём видимости элемента')
    def wait_until_visibility(self, locator):
        return self.wait(10).until(
            EC.visibility_of_element_located(locator))

    @allure.step('ждём пока url не станет включать в себя {string}')
    def wait_until_url_contains(self, string):
        return self.wait(10).until(EC.url_contains(string))

    @allure.step('ждём пока url не перестанет включать в себя {string}')
    def wait_until_url_matches(self, string):
        return self.wait(10).until(EC.url_matches(string))

    @allure.step('ждем пока элемент станет кликабелен')
    def wait_until_element_is_clickable(self, element):
        self.wait(10).until(
            EC.element_to_be_clickable(element))

    @allure.step('кликаем по локатору')
    def click(self, locator):
        button = self.wait(10).until(EC.element_to_be_clickable(locator))
        button.location_once_scrolled_into_view
        # self.driver.execute_script("arguments[0].click();", button)
        button.click()

        return button

    def get_active_element(self):
        element = self.driver.switch_to.active_element
        return element

    @allure.step('находим элемент')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    # @allure.step('проверяем что найденный элемент активен')
    # def check_if_element_is_active(self, locator):
    #     return self.get_active_element() is self.find_element(locator)

    @allure.step('проверяем текущий url')
    def get_current_url(self):
        url = self.driver.current_url
        return url

    @allure.step('проверяем что страница сейчас загружена')
    def is_loaded(self):
        return self.get_current_url() == self.page_link

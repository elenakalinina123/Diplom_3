import pytest

from selenium import webdriver


@pytest.fixture(params=['chrome', 'firefox'], scope="class")
def driver(request):
    if request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()

    elif request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()

    yield driver
    driver.quit()

import pytest

from selenium import webdriver


@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def fixed_email():
    return 'didimadloba@mail.ge'


@pytest.fixture
def fixed_user():
    login_data = {'email': 'madlobainfo@mail.ge',
                  'password': 'madlobadidi'}
    return login_data

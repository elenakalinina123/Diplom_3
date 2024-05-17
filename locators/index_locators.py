from selenium.webdriver.common.by import By

profile_button = (By.XPATH, ".//p[text()='Личный Кабинет']")
constructor = (By.XPATH, ".//p[text()='Конструктор']")
orders_timeline = (By.XPATH, ".//p[text()='Лента Заказов']")

orders_h1 = (By.XPATH, ".//div/h1[text()='Лента заказов']")
constructor_h1 = (By.XPATH, ".//section/h1[text()='Соберите бургер']")

burger_1 = (By.XPATH, ".//div/ul/a/p[text()='Флюоресцентная булка R2-D3']/parent::a")  # noqa
burger_2 = (By.XPATH, ".//div/ul/a/p[text()='Краторная булка N-200i']/parent::a")  # noqa

burger_1_popup = (By.XPATH, ".//section/div/div/p[text()='Флюоресцентная булка R2-D3']")  # noqa
burger_2_popup = (By.XPATH, ".//section/div/div/p[text()='Краторная булка N-200i']")  # noqa

burger_1_close = (By.XPATH, ".//section/div/div/p[text()='Флюоресцентная булка R2-D3']/parent::div/following-sibling::button")  # noqa
burger_2_close = (By.XPATH, ".//section/div/div/p[text()='Краторная булка N-200i']/parent::div/following-sibling::button")  # noqa

order_popup_close = (By.XPATH, ".//p[text()='идентификатор заказа']/parent::div/following-sibling::button")  # noqa
order_number = (By.XPATH, './/p[text()="идентификатор заказа"]/preceding-sibling::h2')  # noqa

sauce_spicy = (By.XPATH, ".//div/ul/a/p[text()='Соус Spicy-X']/parent::a")

basket_drop = (By.XPATH, './/section/ul')

burger_1_counter = (By.XPATH, ".//div/ul/a/p[text()='Флюоресцентная булка R2-D3']/parent::a/div/p[contains(@class,'counter')]")  # noqa

create_order = (By.XPATH, './/button[text()="Оформить заказ"]')

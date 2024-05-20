from selenium.webdriver.common.by import By

total_counter = (By.XPATH, './/div/p[text()="Выполнено за все время:"]/following-sibling::p')  # noqa
day_counter = (By.XPATH, './/div/p[text()="Выполнено за сегодня:"]/following-sibling::p')  # noqa

first_order = (By.XPATH, './/h2[contains(text(), "бургер")]')
order_popup = (By.XPATH, './/div[contains(@class,"Modal_orderBox__1xWdi")]')

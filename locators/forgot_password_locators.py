from selenium.webdriver.common.by import By

email_field = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
recover_button = (By.XPATH, './/button[text()="Восстановить"]')
show_password_button = (
    By.XPATH, ".//fieldset/div/div/div/*[local-name()='svg']/parent::div")
password_field = (By.XPATH, ".//fieldset/div/div[label[text()='Пароль']]")

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Pages.basePage import BasePage


class LoginPage(BasePage):
    """登录页面"""

    def username_input_send_keys(self, value):
        username_input = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, "username")))
        username_input.send_keys(value)

    def username_input_clear(self):
        username_input = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, "username")))
        username_input.clear()

    def password_input_send_keys(self, value):
        password_input = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, "password")))
        password_input.send_keys(value)

    def password_input_clear(self):
        password_input = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, "password")))
        password_input.clear()

    def login_button_click(self):
        login_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, '//*[@id="root"]/div/div/div[3]/form/button[1]')))
        login_button.click()

    def register_button_click(self):
        register_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, '//*[@id="root"]/div/div/div[3]/form/button[2]')))
        register_button.click()

    def alert_text(self):
        alert = WebDriverWait(self.driver, 10).until(expected_conditions.alert_is_present())
        return alert.text

    def alert_ok(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def user_login(self, login_url='http://47.113.226.85/login', username='miniredtest', password='123456miniredQ'):
        self.driver.get(login_url)
        self.username_input_send_keys(username)
        self.password_input_send_keys(password)
        self.login_button_click()

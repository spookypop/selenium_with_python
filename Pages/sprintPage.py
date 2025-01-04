import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Pages.basePage import BasePage


class SprintPage(BasePage):
    """登录页面"""

    def sprint_name_input_send_keys(self, value):
        username_input = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, "sprint_name")))
        username_input.send_keys(value)

    def commit_button_click(self):
        login_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, '//*[@id="contentmain"]/form/div[2]/div/div/div/div/button/span')))
        login_button.click()

    def null_msg(self):
        null_msg = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.CLASS_NAME, "ant-form-item-explain-error")))
        time.sleep(2)
        return null_msg.text

    def alert_text(self):
        alert = WebDriverWait(self.driver, 10).until(expected_conditions.alert_is_present())
        return alert.text

    def alert_ok(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def create_sprint(self, sprint_url="http://127.0.0.1:3000/pages/CreateSprint", value=""):
        self.driver.get(sprint_url)
        self.sprint_name_input_send_keys(value)
        self.commit_button_click()

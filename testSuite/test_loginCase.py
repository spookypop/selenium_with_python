import time
import unittest
from Pages.loginPage import LoginPage
from config.chrom_driver import chrom_driver_init


class LoginTest(unittest.TestCase):
    """登录功能"""

    def setUp(self) -> None:
        self.driver = chrom_driver_init()
        time.sleep(2)
        self.driver.get("http://47.113.226.85/login")

    def tearDown(self) -> None:
        self.driver.quit()

    def test_error_password(self):
        """输入错误的密码，登录失败"""
        login_page = LoginPage(self.driver)
        login_page.username_input_send_keys('miniredtest')
        login_page.password_input_send_keys('123444')
        login_page.login_button_click()
        time.sleep(2)
        alert_text = login_page.alert_text()
        self.assertEqual(alert_text, '账号或密码不正确')

    def test_login_success(self):
        """输入正确的用户名和密码，登录成功"""
        login_page = LoginPage(self.driver)
        login_page.username_input_send_keys('miniredtest')
        login_page.password_input_send_keys('123456miniredQ')
        login_page.login_button_click()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, 'http://47.113.226.85/')

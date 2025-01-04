import time
import unittest
from Pages.loginPage import LoginPage
from config.chrom_driver import chrom_driver_init


class RegisterTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = chrom_driver_init()
        time.sleep(2)
        self.driver.get("http://127.0.0.1:3000/login")

    def test_password_boundary(self):
        login_page = LoginPage(self.driver)
        timestamp = time.time()
        timestamp_str = str(int(timestamp))
        username = 'user' + timestamp_str
        error_msg = "密码必须为6-18位，大小写字母和数字的组合"
        success_msg = '注册成功'
        # 测试密码边界值
        boundary = [('密码少于6位', username, '12345', error_msg),
                    ('密码多于18位', username, '1234567890123456789', error_msg),
                    ('密码没有大写字母', username, 'abc12345', error_msg),
                    ('正确的用户名密码', username, 'Abc123456', success_msg)]
        for data in boundary:
            print(data[0])
            login_page.username_input_send_keys(data[1])
            login_page.password_input_send_keys(data[2])
            login_page.register_button_click()
            alert_text = login_page.alert_text()
            self.assertEqual(alert_text, data[3])
            login_page.alert_ok()
            login_page.username_input_clear()
            login_page.password_input_clear()

    def tearDown(self) -> None:
        self.driver.quit()

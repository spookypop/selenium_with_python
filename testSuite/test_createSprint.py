import time
import unittest
from Pages.loginPage import LoginPage
from Pages.sprintPage import SprintPage
from config.chrom_driver import chrom_driver_init


class CreateSprint(unittest.TestCase):
    """迭代管理功能"""
    @classmethod
    def setUpClass(cls):
        cls.driver = chrom_driver_init()
        # 登录
        login_page = LoginPage(cls.driver)
        login_page.user_login()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_null_sprint_name(self):
        """迭代名称为空，创建失败"""
        sprint_page = SprintPage(self.driver)
        sprint_page.create_sprint()
        error_text = sprint_page.null_msg()
        self.assertEqual(error_text, "请输入迭代名称!")

    def test_duplicate_sprint_name(self):
        """迭代名称重复，创建失败"""
        sprint_page = SprintPage(self.driver)
        sprint_page.create_sprint(value='迭代20241227')
        alert_text = sprint_page.alert_text()
        self.assertEqual(alert_text, "迭代名称已存在")
        sprint_page.alert_ok()
        time.sleep(2)

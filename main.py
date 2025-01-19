import os
from html_reporter import HTMLTestRunner
from config.email_config import send_email_html_report
from testSuite.test_loginCase import LoginTest
import unittest

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # 将测试用例集添加到测试套件
    suite.addTest(loader.loadTestsFromTestCase(LoginTest))

    # 获取项目根目录
    root_path = os.path.dirname(os.path.abspath(__file__))
    # 测试报告存放路径
    report_path = os.path.join(root_path, 'reports/report.html')

    # 生成html格式的测试报告
    runner = HTMLTestRunner(report_path,  # 报告存放路径
                            title='自动化测试报告',  # 报告标题
                            description='核心模块自动化测试',  # 报告描述
                            open_in_browser=False  # 是否自动在浏览器打开
                            )

    runner.run(suite)

    # 读取测试报告内容
    with open(report_path, 'r') as report:
        content = report.read()

    # 测试报告发到指定邮箱
    send_email_html_report(content)

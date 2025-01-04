from selenium import webdriver


class BasePage:
    """页面初始化"""

    def __init__(self, driver):
        self.driver = driver


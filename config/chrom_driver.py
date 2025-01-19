from selenium import webdriver


def chrom_driver_init():
    """浏览器驱动初始化"""
    webdriver_path = './chromedriver'
    service = webdriver.ChromeService(executable_path=webdriver_path)
    option = webdriver.ChromeOptions()
    # 静默模式启动
    option.add_argument('headless')
    driver = webdriver.Chrome(service=service, options=option)
    return driver

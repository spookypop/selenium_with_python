from selenium import webdriver


def chrom_driver_init():
    webdriver_path = './chromedriver'
    service = webdriver.ChromeService(executable_path=webdriver_path)
    option = webdriver.ChromeOptions()
    option.add_argument('headless')  # 静默模式启动
    driver = webdriver.Chrome(service=service, options=option)
    return driver

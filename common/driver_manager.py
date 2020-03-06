from selenium import webdriver


# class DriverManager is designed to manager cross-browser drivers
class DriverManager(object):
    # define and start driver
    @classmethod
    def start_chrome_driver(cls):
        # Using ChromeDriver 80.0.3987.106
        cls._driver = webdriver.Chrome()
        return cls._driver

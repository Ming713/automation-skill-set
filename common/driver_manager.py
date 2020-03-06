import sys

from selenium import webdriver
from appium import webdriver as appium_wd



# class DriverManager is designed to manager cross-browser drivers
from common.constants import BROWSER_NAME, TARGET_ENV


class DriverManager(object):
    _all_drivers = []
    _driver = None
    _all_session_ids = []
    test_name = None

    @classmethod
    def init_browser(cls, preferences=None, desired_caps=None):
        if BROWSER_NAME.upper() == 'DESKTOP CHROME':
            chrome_ops = cls.init_chrome_options()

            caps = chrome_ops.to_capabilities()
            # caps['loggingPrefs'] = {'browser': 'SEVERE'}

            cls.start_chrome_driver(caps)

        elif BROWSER_NAME.upper() == 'MOBILE':
            caps = {
                "deviceName": "Pixel 2 API 29",
                "platformName": "Android",
                "appPackage": "com.google.android.gm",
                "appActivity": "ConversationListActivityGmail",
                "appiumVersion": "1.13.0",
                "deviceOrientation": "portrait",
                "deviceType": "phone",
                "newCommandTimeout": 600,
                "platformVersion": "10",
                "app": "/Users/mingli/automation-skill-set/resources/applications/android/gmail.apk",
                "autoGrantPermissions": True
            }
            cls.startup_mobile_browser_in_local(caps)
        else:
            sys.exit(-1)

        cls._all_drivers.append(cls._driver)
        cls._all_session_ids.append(cls._driver.session_id)

        return cls._driver
    @classmethod
    def init_chrome_options(cls):
        chrome_ops = webdriver.ChromeOptions()
        chrome_ops.add_argument("--test-type")
        chrome_ops.add_argument("--start-maximized")
        chrome_ops.add_argument('--enable-logging')
        chrome_ops.add_argument('--ignore-certificate-errors')
        chrome_ops.add_argument("--allow-running-insecure-content")

        return chrome_ops

    # @classmethod
    # def init_mobile_gmail_app(cls):
    #     caps = {
    #         "deviceName": "Pixel 2 API 29",
    #         "platformName": "Android",
    #         "appPackage": "com.google.android.gm",
    #         "appActivity": "ConversationListActivityGmail",
    #         "appiumVersion": "1.13.0",
    #         "deviceOrientation": "portrait",
    #         "deviceType": "phone",
    #         "newCommandTimeout": 600,
    #         "platformVersion": "10",
    #         "app": "/Users/mingli/autotestestexercise/mobile-test-scripts/gmail_android_app/resources/applications/android/gmail.apk",
    #         "autoGrantPermissions": True
    #     }
    #     if TARGET_ENV.upper() == 'LOCAL':
    #         cls.startup_mobile_browser_in_local(caps)


    @classmethod
    def startup_mobile_browser_in_local(cls, caps):
        caps.update({'autoGrantPermissions': True})

        cls._driver = appium_wd.Remote(desired_capabilities=caps,
                                       command_executor='http://127.0.0.1:4723/wd/hub')
        return cls._driver


    # define and start driver
    @classmethod
    def start_chrome_driver(cls, caps):
        # Using ChromeDriver 80.0.3987.106
        cls._driver = webdriver.Chrome(desired_capabilities=caps)
        return cls._driver

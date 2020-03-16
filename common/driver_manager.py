import sys

from selenium import webdriver
from appium import webdriver as appium_wd

# class DriverManager is designed to manager the cross-browser drivers
from common.constants import BROWSER_NAME, TARGET_ENV, BROWSER_VERSION


class DriverManager(object):
    _all_drivers = []
    _driver = None
    _all_session_ids = []
    test_name = None

    @classmethod
    def init_browser(cls):
        if TARGET_ENV.upper() == 'LOCALS':
            if BROWSER_NAME.upper() == 'DESKTOP CHROME':
                chrome_ops = cls.init_chrome_options()

                caps = chrome_ops.to_capabilities()
                cls.start_chrome_driver_in_local(caps)

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
                cls.startup_mobile_browser(caps)
            else:
                sys.exit(-1)
        elif TARGET_ENV.upper() == 'SELENIUM GRID':
            if BROWSER_NAME.upper() == 'DESKTOP CHROME':
                chrome_ops = cls.init_chrome_options()

                caps = chrome_ops.to_capabilities()
                cls.start_chrome_driver_in_selenium_grid(caps)

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
                cls.startup_mobile_browser(caps)

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

    @classmethod
    def startup_mobile_browser(cls, caps):
        caps.update({'autoGrantPermissions': True})

        cls._driver = appium_wd.Remote(desired_capabilities=caps,
                                       command_executor='http://127.0.0.1:4723/wd/hub')
        return cls._driver

    @classmethod
    def start_chrome_driver_in_local(cls, caps):
        cls._driver = webdriver.Chrome(desired_capabilities=caps)
        return cls._driver

    @classmethod
    def start_chrome_driver_in_selenium_grid(cls, caps):
        caps.update({"browserName": "chrome"})
        cls._driver = webdriver.Remote(desired_capabilities=caps,
                                       command_executor='http://127.0.0.1:4444/wd/hub')
        return cls._driver

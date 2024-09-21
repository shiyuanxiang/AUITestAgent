from appium import webdriver
from appium.options.android import UiAutomator2Options


class DriverHelper:
    driver = None
    pkg_n = 'com.example.wick'
    start_ac_n = 'com.example.wick.TestSelectorActivity'

    @staticmethod
    def get_driver():
        if DriverHelper.driver is None:
            DriverHelper.driver = DriverHelper.create_driver()
        return DriverHelper.driver

    @classmethod
    def create_driver(cls):
        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.platformVersion = '14'
        options.device_name = '43141JEKB03040'
        options.app_package = cls.pkg_n
        options.app_activity = cls.start_ac_n
        driver = webdriver.Remote('http://localhost:4723', options=options)
        return driver

    @classmethod
    def stop_driver(cls):
        if cls.driver is not None:
            cls.driver.quit()
            cls.driver = None

    @classmethod
    def scroll_all(cls):
        driver = cls.get_driver()
        end_y = driver.get_window_size()['height'] / 3
        start_y = driver.get_window_size()['height'] * 2 / 3
        _x = driver.get_window_size()['width'] / 2
        for i in range(5):
            driver.swipe(start_x=_x, start_y=start_y, end_x=_x, end_y=end_y, duration=500)

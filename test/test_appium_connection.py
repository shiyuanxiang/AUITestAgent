from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

options = UiAutomator2Options()
options.platform_name = 'Android'
options.platformVersion = '14'
options.device_name = '43141JEKB03040'
options.app_package = 'com.example.wick'
options.app_activity = 'com.example.wick.MainActivity'
driver = webdriver.Remote('http://localhost:4723', options=options)


while True:
    print(f"Current activity: {driver.current_activity}")
    time.sleep(1)



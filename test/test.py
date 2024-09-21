import time

from selenium.webdriver.common.by import By

from AUITestAgent.history import History
from AUITestAgent.observer import Observer
from AUITestAgent.selector import Selector
from AUITestAgent.executor import Executor
from AUITestAgent.monitor import Monitor
from AUITestAgent.driver_helper import DriverHelper


def main():
    driver = DriverHelper.get_driver()
    driver.find_element(By.ID, "com.example.wick:id/email").send_keys("hello")
    DriverHelper.scroll_all(scroll_times=1)
    print("Hello")
    element = driver.find_element(By.ID, "com.example.wick:id/page1")
    element.click()
    print(element.text)
    driver.back()


if __name__ == '__main__':
    main()

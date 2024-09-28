import time

from selenium.webdriver.common.by import By

from AUITestAgent.history import History
from AUITestAgent.observer import Observer
from AUITestAgent.selector import Selector
from AUITestAgent.executor import Executor
from AUITestAgent.monitor import Monitor
from AUITestAgent.driver_helper import DriverHelper


def main():
    observer = Observer()
    print(observer.get_ui_hierarchy())


if __name__ == '__main__':
    main()

from selenium.webdriver.common.by import By
from AUITestAgent.driver_helper import DriverHelper


class Executor:
    def __init__(self, history):
        self.history = history

    def execute(self, assistant_response):
        for action in assistant_response:
            self.execute_action(action)
            self.history.update(action)

    def execute_action(self, action):
        """
        Execute the action.
        :param action:
                {
                  "action": "click",
                  "target": "com.example.wick:id/page1",
                  "input text": ""
                }
        :return: None
        """
        driver = DriverHelper.get_driver()
        if action["action"] == "click":
            driver.find_element(By.ID, action["target"]).click()
        elif action["action"] == "input":
            driver.find_element(By.ID, action["target"]).send_keys(action["input text"])
        elif action["action"] == "scroll":
            DriverHelper.scroll_all()
        elif action["action"] == "back":
            driver.back()
        else:
            raise Exception(f"Unsupported action: {action['action']}")

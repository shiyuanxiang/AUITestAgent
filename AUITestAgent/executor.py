from selenium.webdriver.common.by import By
from driver_helper import DriverHelper


class Executor:
    def __init__(self, history):
        self.history = history
        self.driver = DriverHelper.get_driver()

    def execute(self, suggest_actions):
        before_ac = self.driver.current_activity
        for action in suggest_actions:
            self.execute_action(action)
            print(f'[executor] executed {action}')
            self.history.update(action)
            after_ac = self.driver.current_activity
            if before_ac != after_ac:
                print(f"[executor] go to next activity.")
                break

    def execute_action(self, action):
        """
        Execute the action.
        :param action:
                {
                  "action": "click",
                  "target": "com.example.wick:id/page1",
                  "input_text": ""
                }
        :return: None
        """
        if action["action"] == "back":
            self.driver.back()
            return

        ele = self.driver.find_element(By.ID, action["target"])
        if action["action"] == "click":
            ele.click()
        elif action["action"] == "input":
            ele.clear()
            ele.send_keys(action["input_text"])
        elif action["action"] == "scroll":
            DriverHelper.scroll_all(scroll_times=1)
        else:
            raise Exception(f"Unsupported action: {action['action']}")

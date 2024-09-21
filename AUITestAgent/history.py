class History:

    def __init__(self, task):
        self.task = task
        self.action_history = []

    def update(self, action):
        """
        Update the action history.
        :param action: {
            "action": "",
            "target": "",
            "input_text": ""
        }
        :return: None
        """
        if action["input_text"] != "":
            action_string = f"{action['action']} on {action['target']} with text={action['input_text']}"
        else:
            action_string = f"{action['action']} on {action['target']}"
        self.action_history.append(action_string)

    def get_action_history(self):
        return self.action_history

    def get_task(self):
        return self.task

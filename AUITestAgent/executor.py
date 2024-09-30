import requests


class Executor:
    def __init__(self, observer, history):
        self.observer = observer
        self.history = history

    def execute(self, suggest_actions):
        before_ac = self.observer.get_current_activity()
        for action in suggest_actions:
            self.execute_action(action)
            print(f'[executor] executed {action}')
            self.history.update(action)
            after_ac = self.observer.get_current_activity()
            if before_ac != after_ac:
                print(f"[executor] go to next activity.")
                break

    def execute_action(self, action):
        response = requests.post('http://localhost:5001/execute_action', json=action)
        print(f"[executor] {response.json()}")
        return response.json()

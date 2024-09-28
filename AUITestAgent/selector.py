from llama import Chatllama
import json


class Selector:
    def __init__(self, observer, history):
        self.observer = observer
        self.history = history
        prompt = self.read_prompt("./prompt02.json")
        self.llama = Chatllama(prompt=prompt)

    def read_prompt(self, prompt_path):
        with open(prompt_path, "r") as f:
            prompt = json.loads(f.read())
        for msg in prompt:
            msg["content"] = msg["content"].__str__()
        return prompt

    def select(self):
        user_prompt = self.make_user_prompt()
        suggest_actions = self.llama.chat(user_prompt, ";".join(self.observer.get_ui_hierarchy()))
        return suggest_actions

    def make_user_prompt(self):
        user_prompt = {"role": "user", "content": {}}
        user_prompt["content"]["task"] = self.history.get_task()
        user_prompt["content"]["action_history"] = self.history.get_action_history().__str__()
        user_prompt["content"]["current_activity"] = self.observer.get_current_activity()
        user_prompt["content"]["widgets"] = self.observer.get_ui_hierarchy().__str__()
        user_prompt["content"] = user_prompt["content"].__str__()
        return user_prompt

